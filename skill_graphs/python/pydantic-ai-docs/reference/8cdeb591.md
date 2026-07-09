        """
        self._model_name = model_name

        if isinstance(provider, str):
            provider = infer_provider('gateway/openai' if provider == 'gateway' else provider)
        self._provider = provider
        self.client = provider.client

        super().__init__(settings=settings, profile=profile or provider.model_profile)

    @property
    def base_url(self) -> str:
        return str(self.client.base_url)

    @property
    def model_name(self) -> OpenAIModelName:
        """The model name."""
        return self._model_name

    @property
    def system(self) -> str:
        """The model provider."""
        return self._provider.name

    @classmethod
    def supported_builtin_tools(cls) -> frozenset[type[AbstractBuiltinTool]]:
        """Return the set of builtin tool types this model can handle."""
        return frozenset({WebSearchTool, CodeExecutionTool, FileSearchTool, MCPServerTool, ImageGenerationTool})

    async def request(
        self,
        messages: list[ModelRequest | ModelResponse],
        model_settings: ModelSettings | None,
        model_request_parameters: ModelRequestParameters,
    ) -> ModelResponse:
        check_allow_model_requests()
        model_settings, model_request_parameters = self.prepare_request(
            model_settings,
            model_request_parameters,
        )
        response = await self._responses_create(
            messages, False, cast(OpenAIResponsesModelSettings, model_settings or {}), model_request_parameters
        )

        # Handle ModelResponse
        if isinstance(response, ModelResponse):
            return response

        return self._process_response(
            response, cast(OpenAIResponsesModelSettings, model_settings or {}), model_request_parameters
        )

    @asynccontextmanager
    async def request_stream(
        self,
        messages: list[ModelMessage],
        model_settings: ModelSettings | None,
        model_request_parameters: ModelRequestParameters,
        run_context: RunContext[Any] | None = None,
    ) -> AsyncIterator[StreamedResponse]:
        check_allow_model_requests()
        model_settings, model_request_parameters = self.prepare_request(
            model_settings,
            model_request_parameters,
        )
        response = await self._responses_create(
            messages, True, cast(OpenAIResponsesModelSettings, model_settings or {}), model_request_parameters
        )
        async with response:
            yield await self._process_streamed_response(
                response, cast(OpenAIResponsesModelSettings, model_settings or {}), model_request_parameters
            )

    def _process_response(  # noqa: C901
        self,
        response: responses.Response,
        model_settings: OpenAIResponsesModelSettings,
        model_request_parameters: ModelRequestParameters,
    ) -> ModelResponse:
        """Process a non-streamed response, and prepare a message to return."""
        items: list[ModelResponsePart] = []
        refusal_text: str | None = None
        for item in response.output:
            if isinstance(item, responses.ResponseReasoningItem):
                signature = item.encrypted_content
                # Handle raw CoT content from gpt-oss models
                provider_details: dict[str, Any] = {}
                raw_content: list[str] | None = [c.text for c in item.content] if item.content else None
                if raw_content:
                    provider_details['raw_content'] = raw_content

                if item.summary:
                    for summary in item.summary:
                        # We use the same id for all summaries so that we can merge them on the round trip.
                        items.append(
                            ThinkingPart(
                                content=summary.text,
                                id=item.id,
                                signature=signature,
                                provider_name=self.system,
                                provider_details=provider_details or None,
                            )
                        )
                        # We only need to store the signature and raw_content once.
                        signature = None
                        provider_details = {}
                elif signature or provider_details:
                    items.append(
                        ThinkingPart(
                            content='',
                            id=item.id,
                            signature=signature,
                            provider_name=self.system,
                            provider_details=provider_details or None,
                        )
                    )
            elif isinstance(item, responses.ResponseOutputMessage):
                for content in item.content:
                    if isinstance(content, responses.ResponseOutputRefusal):
                        refusal_text = content.refusal
                    elif isinstance(content, responses.ResponseOutputText):  # pragma: no branch
                        part_provider_details: dict[str, Any] | None = None
                        if content.logprobs:
                            part_provider_details = {'logprobs': _map_logprobs(content.logprobs)}
                        if model_settings.get('openai_include_raw_annotations') and content.annotations:
                            part_provider_details = part_provider_details or {}
                            part_provider_details['annotations'] = responses_output_text_annotations_ta.dump_python(
                                list(content.annotations), warnings=False
                            )
                        items.append(
                            TextPart(
                                content.text,
                                id=item.id,
                                provider_name=self.system,
                                provider_details=part_provider_details,
                            )
                        )
            elif isinstance(item, responses.ResponseFunctionToolCall):
                items.append(
                    ToolCallPart(
                        item.name, item.arguments, tool_call_id=item.call_id, id=item.id, provider_name=self.system
                    )
                )
            elif isinstance(item, responses.ResponseCodeInterpreterToolCall):
                call_part, return_part, file_parts = _map_code_interpreter_tool_call(item, self.system)
                items.append(call_part)
                if file_parts:
                    items.extend(file_parts)
                items.append(return_part)
            elif isinstance(item, responses.ResponseFunctionWebSearch):
                call_part, return_part = _map_web_search_tool_call(item, self.system)
                items.append(call_part)
                items.append(return_part)
            elif isinstance(item, responses.response_output_item.ImageGenerationCall):
                call_part, return_part, file_part = _map_image_generation_tool_call(item, self.system)
                items.append(call_part)
                if file_part:  # pragma: no branch
                    items.append(file_part)
                items.append(return_part)
            elif isinstance(item, responses.ResponseComputerToolCall):  # pragma: no cover
                # Pydantic AI doesn't yet support the ComputerUse built-in tool
                pass
            elif isinstance(item, responses.ResponseCustomToolCall):  # pragma: no cover
                # Support is being implemented in https://github.com/pydantic/pydantic-ai/pull/2572
                pass
            elif isinstance(item, responses.response_output_item.LocalShellCall):  # pragma: no cover
                # Pydantic AI doesn't yet support the `codex-mini-latest` LocalShell built-in tool
                pass
            elif isinstance(item, responses.ResponseFileSearchToolCall):
                call_part, return_part = _map_file_search_tool_call(item, self.system)
                items.append(call_part)
                items.append(return_part)
            elif isinstance(item, responses.response_output_item.McpCall):
                call_part, return_part = _map_mcp_call(item, self.system)
                items.append(call_part)
                items.append(return_part)
            elif isinstance(item, responses.response_output_item.McpListTools):
                call_part, return_part = _map_mcp_list_tools(item, self.system)
                items.append(call_part)
                items.append(return_part)
            elif isinstance(item, responses.response_output_item.McpApprovalRequest):  # pragma: no cover
                # Pydantic AI doesn't yet support McpApprovalRequest (explicit tool usage approval)
                pass

        finish_reason: FinishReason | None = None
        provider_details: dict[str, Any] = {}
        raw_finish_reason = details.reason if (details := response.incomplete_details) else response.status
        if raw_finish_reason:
            provider_details['finish_reason'] = raw_finish_reason
            finish_reason = _RESPONSES_FINISH_REASON_MAP.get(raw_finish_reason)
        if response.created_at:  # pragma: no branch
            provider_details['timestamp'] = number_to_datetime(response.created_at)

        if refusal_text is not None:
            items = []
            finish_reason = 'content_filter'
            provider_details.pop('finish_reason', None)
            provider_details['refusal'] = refusal_text

        return ModelResponse(
            parts=items,
            usage=_map_usage(response, self._provider.name, self._provider.base_url, self.model_name),
            model_name=response.model,
            provider_response_id=response.id,
            timestamp=_now_utc(),
            provider_name=self._provider.name,
            provider_url=self._provider.base_url,
            finish_reason=finish_reason,
            provider_details=provider_details or None,
        )

    async def _process_streamed_response(
        self,
        response: AsyncStream[responses.ResponseStreamEvent],
        model_settings: OpenAIResponsesModelSettings,
        model_request_parameters: ModelRequestParameters,
    ) -> OpenAIResponsesStreamedResponse:
        """Process a streamed response, and prepare a streaming response to return."""
        peekable_response = _utils.PeekableAsyncStream(response)
        first_chunk = await peekable_response.peek()
        if isinstance(first_chunk, _utils.Unset):  # pragma: no cover
            raise UnexpectedModelBehavior('Streamed response ended without content or tool calls')

        assert isinstance(first_chunk, responses.ResponseCreatedEvent)
        return OpenAIResponsesStreamedResponse(
            model_request_parameters=model_request_parameters,
            _model_name=first_chunk.response.model,
            _model_settings=model_settings,
            _response=peekable_response,
            _provider_name=self._provider.name,
            _provider_url=self._provider.base_url,
            _provider_timestamp=number_to_datetime(first_chunk.response.created_at)
            if first_chunk.response.created_at
            else None,
        )

    @overload
    async def _responses_create(
        self,
        messages: list[ModelRequest | ModelResponse],
        stream: Literal[False],
        model_settings: OpenAIResponsesModelSettings,
        model_request_parameters: ModelRequestParameters,
    ) -> responses.Response: ...

    @overload
    async def _responses_create(
        self,
        messages: list[ModelRequest | ModelResponse],
        stream: Literal[True],
        model_settings: OpenAIResponsesModelSettings,
        model_request_parameters: ModelRequestParameters,
    ) -> AsyncStream[responses.ResponseStreamEvent]: ...

    async def _responses_create(  # noqa: C901
        self,
        messages: list[ModelRequest | ModelResponse],
        stream: bool,
        model_settings: OpenAIResponsesModelSettings,
        model_request_parameters: ModelRequestParameters,
    ) -> responses.Response | AsyncStream[responses.ResponseStreamEvent] | ModelResponse:
        tools = (
            self._get_builtin_tools(model_request_parameters)
            + list(model_settings.get('openai_builtin_tools', []))
            + self._get_tools(model_request_parameters)
        )
        profile = OpenAIModelProfile.from_profile(self.profile)
        if not tools:
            tool_choice: Literal['none', 'required', 'auto'] | None = None
        elif not model_request_parameters.allow_text_output and profile.openai_supports_tool_choice_required:
            tool_choice = 'required'
        else:
            tool_choice = 'auto'

        previous_response_id = model_settings.get('openai_previous_response_id')
        if previous_response_id == 'auto':
            previous_response_id, messages = self._get_previous_response_id_and_new_messages(messages)

        instructions, openai_messages = await self._map_messages(messages, model_settings, model_request_parameters)
        reasoning = self._get_reasoning(model_settings)

        text: responses.ResponseTextConfigParam | None = None
        if model_request_parameters.output_mode == 'native':
            output_object = model_request_parameters.output_object
            assert output_object is not None
            text = {'format': self._map_json_schema(output_object)}
        elif (
            model_request_parameters.output_mode == 'prompted' and self.profile.supports_json_object_output
        ):  # pragma: no branch
            text = {'format': {'type': 'json_object'}}

            # Without this trick, we'd hit this error:
            # > Response input messages must contain the word 'json' in some form to use 'text.format' of type 'json_object'.
            # Apparently they're only checking input messages for "JSON", not instructions.
            assert isinstance(instructions, str)
            system_prompt_count = sum(1 for m in openai_messages if m.get('role') == 'system')
            openai_messages.insert(
                system_prompt_count, responses.EasyInputMessageParam(role='system', content=instructions)
            )
            instructions = OMIT

        if verbosity := model_settings.get('openai_text_verbosity'):
            text = text or {}
            text['verbosity'] = verbosity

        _drop_sampling_params_for_reasoning(profile, model_settings)

        _drop_unsupported_params(profile, model_settings)

        include: list[responses.ResponseIncludable] = []
        if profile.openai_supports_encrypted_reasoning_content:
            include.append('reasoning.encrypted_content')
        if model_settings.get('openai_include_code_execution_outputs'):
            include.append('code_interpreter_call.outputs')
        if model_settings.get('openai_include_web_search_sources'):
            include.append('web_search_call.action.sources')
        if model_settings.get('openai_include_file_search_results'):
            include.append('file_search_call.results')
        if model_settings.get('openai_logprobs'):
            include.append('message.output_text.logprobs')

        # When there are no input messages and we're not reusing a previous response,
        # the OpenAI API will reject a request without any input,
        # even if there are instructions.
        # To avoid this provide an explicit empty user message.
        if not openai_messages and not previous_response_id:
            openai_messages.append(
                responses.EasyInputMessageParam(
                    role='user',
                    content='',
                )
            )

        try:
            extra_headers = model_settings.get('extra_headers', {})
            extra_headers.setdefault('User-Agent', get_user_agent())
            # OpenAI SDK type stubs incorrectly use 'in-memory' but API requires 'in_memory', so we have to use `Any` to not hit type errors
            prompt_cache_retention: Any = model_settings.get('openai_prompt_cache_retention', OMIT)
            return await self.client.responses.create(
                input=openai_messages,
                model=self.model_name,
                instructions=instructions,
                parallel_tool_calls=model_settings.get('parallel_tool_calls', OMIT),
                tools=tools or OMIT,
                tool_choice=tool_choice or OMIT,
                max_output_tokens=model_settings.get('max_tokens', OMIT),
                stream=stream,
                temperature=model_settings.get('temperature', OMIT),
                top_p=model_settings.get('top_p', OMIT),
                truncation=model_settings.get('openai_truncation', OMIT),
                timeout=model_settings.get('timeout', NOT_GIVEN),
                service_tier=model_settings.get('openai_service_tier', OMIT),
                previous_response_id=previous_response_id or OMIT,
                top_logprobs=model_settings.get('openai_top_logprobs', OMIT),
                store=model_settings.get('openai_store', OMIT),
                reasoning=reasoning,
                user=model_settings.get('openai_user', OMIT),
                text=text or OMIT,
                include=include or OMIT,
                prompt_cache_key=model_settings.get('openai_prompt_cache_key', OMIT),
                prompt_cache_retention=prompt_cache_retention,
                extra_headers=extra_headers,
                extra_body=model_settings.get('extra_body'),
            )
        except APIStatusError as e:
            if model_response := _check_azure_content_filter(e, self.system, self.model_name):
                return model_response

            if (status_code := e.status_code) >= 400:
                raise ModelHTTPError(status_code=status_code, model_name=self.model_name, body=e.body) from e
            raise  # pragma: lax no cover
        except APIConnectionError as e:
            raise ModelAPIError(model_name=self.model_name, message=e.message) from e

    def _get_reasoning(self, model_settings: OpenAIResponsesModelSettings) -> Reasoning | Omit:
        reasoning_effort = model_settings.get('openai_reasoning_effort', None)
        reasoning_summary = model_settings.get('openai_reasoning_summary', None)
        reasoning_generate_summary = model_settings.get('openai_reasoning_generate_summary', None)

        if reasoning_summary and reasoning_generate_summary:  # pragma: no cover
            raise ValueError('`openai_reasoning_summary` and `openai_reasoning_generate_summary` cannot both be set.')

        if reasoning_generate_summary is not None:  # pragma: no cover
            warnings.warn(
                '`openai_reasoning_generate_summary` is deprecated, use `openai_reasoning_summary` instead',
                DeprecationWarning,
            )
            reasoning_summary = reasoning_generate_summary

        reasoning: Reasoning = {}
        if reasoning_effort:
            reasoning['effort'] = reasoning_effort
        if reasoning_summary:
            reasoning['summary'] = reasoning_summary
        return reasoning or OMIT

    def _get_tools(self, model_request_parameters: ModelRequestParameters) -> list[responses.FunctionToolParam]:
        return [self._map_tool_definition(r) for r in model_request_parameters.tool_defs.values()]

    def _get_builtin_tools(self, model_request_parameters: ModelRequestParameters) -> list[responses.ToolParam]:
        tools: list[responses.ToolParam] = []
        has_image_generating_tool = False
        for tool in model_request_parameters.builtin_tools:
            if isinstance(tool, WebSearchTool):
                web_search_tool = responses.WebSearchToolParam(
                    type='web_search', search_context_size=tool.search_context_size
                )
                if tool.user_location:
                    web_search_tool['user_location'] = responses.web_search_tool_param.UserLocation(
                        type='approximate', **tool.user_location
                    )
                if tool.allowed_domains:
                    web_search_tool['filters'] = responses.web_search_tool_param.Filters(
                        allowed_domains=tool.allowed_domains
                    )
                tools.append(web_search_tool)
            elif isinstance(tool, FileSearchTool):
                file_search_tool = cast(
                    responses.FileSearchToolParam,
                    {'type': 'file_search', 'vector_store_ids': list(tool.file_store_ids)},
                )
                tools.append(file_search_tool)
            elif isinstance(tool, CodeExecutionTool):
                has_image_generating_tool = True
                tools.append({'type': 'code_interpreter', 'container': {'type': 'auto'}})
            elif isinstance(tool, MCPServerTool):
                mcp_tool = responses.tool_param.Mcp(
                    type='mcp',
                    server_label=tool.id,
                    require_approval='never',
                )

                if tool.authorization_token:  # pragma: no branch
                    mcp_tool['authorization'] = tool.authorization_token

                if tool.allowed_tools is not None:  # pragma: no branch
                    mcp_tool['allowed_tools'] = tool.allowed_tools

                if tool.description:  # pragma: no branch
                    mcp_tool['server_description'] = tool.description

                if tool.headers:  # pragma: no branch
                    mcp_tool['headers'] = tool.headers

                if tool.url.startswith(MCP_SERVER_TOOL_CONNECTOR_URI_SCHEME + ':'):
                    _, connector_id = tool.url.split(':', maxsplit=1)
                    mcp_tool['connector_id'] = connector_id  # pyright: ignore[reportGeneralTypeIssues]
                else:
                    mcp_tool['server_url'] = tool.url

                tools.append(mcp_tool)
            elif isinstance(tool, ImageGenerationTool):  # pragma: no branch
                has_image_generating_tool = True
                size = _resolve_openai_image_generation_size(tool)
                output_compression = tool.output_compression if tool.output_compression is not None else 100
                tools.append(
                    responses.tool_param.ImageGeneration(
                        type='image_generation',
                        background=tool.background,
                        input_fidelity=tool.input_fidelity,
                        moderation=tool.moderation,
                        output_compression=output_compression,
                        output_format=tool.output_format or 'png',
                        partial_images=tool.partial_images,
                        quality=tool.quality,
                        size=size,
                    )
                )
            else:
                raise UserError(  # pragma: no cover
                    f'`{tool.__class__.__name__}` is not supported by `OpenAIResponsesModel`. If it should be, please file an issue.'
                )

        if model_request_parameters.allow_image_output and not has_image_generating_tool:
            tools.append({'type': 'image_generation'})
        return tools

    def _map_tool_definition(self, f: ToolDefinition) -> responses.FunctionToolParam:
        return {
            'name': f.name,
            'parameters': f.parameters_json_schema,
            'type': 'function',
            'description': f.description,
            'strict': bool(
                f.strict and OpenAIModelProfile.from_profile(self.profile).openai_supports_strict_tool_definition
            ),
        }

    def _get_previous_response_id_and_new_messages(
        self, messages: list[ModelMessage]
    ) -> tuple[str | None, list[ModelMessage]]:
        # When `openai_previous_response_id` is set to 'auto', the most recent
        # `provider_response_id` from the message history is selected and all
        # earlier messages are omitted. This allows the OpenAI SDK to reuse
        # server-side history for efficiency. The returned tuple contains the
        # `previous_response_id` (if found) and the trimmed list of messages.
        previous_response_id = None
        trimmed_messages: list[ModelMessage] = []
        for m in reversed(messages):
            if isinstance(m, ModelResponse) and m.provider_name == self.system:
                previous_response_id = m.provider_response_id
                break
            else:
                trimmed_messages.append(m)

        if previous_response_id and trimmed_messages:
            return previous_response_id, list(reversed(trimmed_messages))
        else:
            return None, messages

    async def _map_messages(  # noqa: C901
        self,
        messages: list[ModelMessage],
        model_settings: OpenAIResponsesModelSettings,
        model_request_parameters: ModelRequestParameters,
    ) -> tuple[str | Omit, list[responses.ResponseInputItemParam]]:
        """Maps a `pydantic_ai.Message` to a `openai.types.responses.ResponseInputParam` i.e. the OpenAI Responses API input format.

        For `ThinkingParts`, this method:
        - Sends `signature` back as `encrypted_content` (for official OpenAI reasoning)
        - Sends `content` back as `summary` text
        - Sends `provider_details['raw_content']` back as `content` items (for gpt-oss raw CoT)

        Raw CoT is sent back to improve model performance in multi-turn conversations.
