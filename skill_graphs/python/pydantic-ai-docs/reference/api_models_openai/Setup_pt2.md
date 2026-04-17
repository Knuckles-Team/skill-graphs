        _profile = super().profile
        openai_profile = OpenAIModelProfile.from_profile(_profile)
        if not openai_profile.openai_chat_supports_web_search:
            new_tools = _profile.supported_builtin_tools - {WebSearchTool}
            _profile = replace(_profile, supported_builtin_tools=new_tools)
        return _profile

    @property
    @deprecated('Set the `system_prompt_role` in the `OpenAIModelProfile` instead.')
    def system_prompt_role(self) -> OpenAISystemPromptRole | None:
        return OpenAIModelProfile.from_profile(self.profile).openai_system_prompt_role

    def prepare_request(
        self,
        model_settings: ModelSettings | None,
        model_request_parameters: ModelRequestParameters,
    ) -> tuple[ModelSettings | None, ModelRequestParameters]:
        # Check for WebSearchTool before base validation to provide a helpful error message
        if (
            any(isinstance(tool, WebSearchTool) for tool in model_request_parameters.builtin_tools)
            and not OpenAIModelProfile.from_profile(self.profile).openai_chat_supports_web_search
        ):
            raise UserError(
                f'WebSearchTool is not supported with `OpenAIChatModel` and model {self.model_name!r}. '
                f'Please use `OpenAIResponsesModel` instead.'
            )
        return super().prepare_request(model_settings, model_request_parameters)

    async def request(
        self,
        messages: list[ModelMessage],
        model_settings: ModelSettings | None,
        model_request_parameters: ModelRequestParameters,
    ) -> ModelResponse:
        check_allow_model_requests()
        model_settings, model_request_parameters = self.prepare_request(
            model_settings,
            model_request_parameters,
        )
        response = await self._completions_create(
            messages, False, cast(OpenAIChatModelSettings, model_settings or {}), model_request_parameters
        )

        # Handle ModelResponse returned directly (for content filters)
        if isinstance(response, ModelResponse):
            return response

        model_response = self._process_response(response)
        return model_response

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
        model_settings_cast = cast(OpenAIChatModelSettings, model_settings or {})
        response = await self._completions_create(messages, True, model_settings_cast, model_request_parameters)
        async with response:
            yield await self._process_streamed_response(response, model_request_parameters, model_settings_cast)

    @overload
    async def _completions_create(
        self,
        messages: list[ModelMessage],
        stream: Literal[True],
        model_settings: OpenAIChatModelSettings,
        model_request_parameters: ModelRequestParameters,
    ) -> AsyncStream[ChatCompletionChunk]: ...

    @overload
    async def _completions_create(
        self,
        messages: list[ModelMessage],
        stream: Literal[False],
        model_settings: OpenAIChatModelSettings,
        model_request_parameters: ModelRequestParameters,
    ) -> chat.ChatCompletion | ModelResponse: ...

    async def _completions_create(
        self,
        messages: list[ModelMessage],
        stream: bool,
        model_settings: OpenAIChatModelSettings,
        model_request_parameters: ModelRequestParameters,
    ) -> chat.ChatCompletion | AsyncStream[ChatCompletionChunk] | ModelResponse:
        tools = self._get_tools(model_request_parameters)
        web_search_options = self._get_web_search_options(model_request_parameters)

        profile = OpenAIModelProfile.from_profile(self.profile)
        if not tools:
            tool_choice: Literal['none', 'required', 'auto'] | None = None
        elif not model_request_parameters.allow_text_output and profile.openai_supports_tool_choice_required:
            tool_choice = 'required'
        else:
            tool_choice = 'auto'

        openai_messages = await self._map_messages(messages, model_request_parameters)

        response_format: chat.completion_create_params.ResponseFormat | None = None
        if model_request_parameters.output_mode == 'native':
            output_object = model_request_parameters.output_object
            assert output_object is not None
            response_format = self._map_json_schema(output_object)
        elif (
            model_request_parameters.output_mode == 'prompted' and self.profile.supports_json_object_output
        ):  # pragma: no branch
            response_format = {'type': 'json_object'}

        _drop_sampling_params_for_reasoning(profile, model_settings)

        _drop_unsupported_params(profile, model_settings)

        try:
            extra_headers = model_settings.get('extra_headers', {})
            extra_headers.setdefault('User-Agent', get_user_agent())

            # OpenAI SDK type stubs incorrectly use 'in-memory' but API requires 'in_memory', so we have to use `Any` to not hit type errors
            prompt_cache_retention: Any = model_settings.get('openai_prompt_cache_retention', OMIT)
            return await self.client.chat.completions.create(
                model=self.model_name,
                messages=openai_messages,
                parallel_tool_calls=model_settings.get('parallel_tool_calls', OMIT),
                tools=tools or OMIT,
                tool_choice=tool_choice or OMIT,
                stream=stream,
                stream_options=self._get_stream_options(model_settings) if stream else OMIT,
                stop=model_settings.get('stop_sequences', OMIT),
                max_completion_tokens=model_settings.get('max_tokens', OMIT),
                timeout=model_settings.get('timeout', NOT_GIVEN),
                response_format=response_format or OMIT,
                seed=model_settings.get('seed', OMIT),
                reasoning_effort=model_settings.get('openai_reasoning_effort', OMIT),
                user=model_settings.get('openai_user', OMIT),
                web_search_options=web_search_options or OMIT,
                service_tier=model_settings.get('openai_service_tier', OMIT),
                prediction=model_settings.get('openai_prediction', OMIT),
                temperature=model_settings.get('temperature', OMIT),
                top_p=model_settings.get('top_p', OMIT),
                presence_penalty=model_settings.get('presence_penalty', OMIT),
                frequency_penalty=model_settings.get('frequency_penalty', OMIT),
                logit_bias=model_settings.get('logit_bias', OMIT),
                logprobs=model_settings.get('openai_logprobs', OMIT),
                top_logprobs=model_settings.get('openai_top_logprobs', OMIT),
                store=model_settings.get('openai_store', OMIT),
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

    def _validate_completion(self, response: chat.ChatCompletion) -> chat.ChatCompletion:
        """Hook that validates chat completions before processing.

        This method may be overridden by subclasses of `OpenAIChatModel` to apply custom completion validations.
        """
        return chat.ChatCompletion.model_validate(response.model_dump())

    def _process_provider_details(self, response: chat.ChatCompletion) -> dict[str, Any] | None:
        """Hook that response content to provider details.

        This method may be overridden by subclasses of `OpenAIChatModel` to apply custom mappings.
        """
        return _map_provider_details(response.choices[0])

    def _process_response(self, response: chat.ChatCompletion | str) -> ModelResponse:
        """Process a non-streamed response, and prepare a message to return."""
        # Although the OpenAI SDK claims to return a Pydantic model (`ChatCompletion`) from the chat completions function:
        # * it hasn't actually performed validation (presumably they're creating the model with `model_construct` or something?!)
        # * if the endpoint returns plain text, the return type is a string
        # Thus we validate it fully here.
        if not isinstance(response, chat.ChatCompletion):
            raise UnexpectedModelBehavior(
                f'Invalid response from {self.system} chat completions endpoint, expected JSON data'
            )

        timestamp = _now_utc()
        if not response.created:
            response.created = int(timestamp.timestamp())

        # Workaround for local Ollama which sometimes returns a `None` finish reason.
        if response.choices and (choice := response.choices[0]) and choice.finish_reason is None:  # pyright: ignore[reportUnnecessaryComparison]
            choice.finish_reason = 'stop'

        try:
            response = self._validate_completion(response)
        except ValidationError as e:
            raise UnexpectedModelBehavior(f'Invalid response from {self.system} chat completions endpoint: {e}') from e

        choice = response.choices[0]

        # Handle refusal responses (structured output safety filter)
        if choice.message.refusal:
            provider_details = self._process_provider_details(response) or {}
            provider_details.pop('finish_reason', None)
            provider_details['refusal'] = choice.message.refusal
            if response.created:  # pragma: no branch
                provider_details['timestamp'] = number_to_datetime(response.created)
            return ModelResponse(
                parts=[],
                usage=self._map_usage(response),
                model_name=response.model,
                timestamp=_now_utc(),
                provider_details=provider_details or None,
                provider_response_id=response.id,
                provider_name=self._provider.name,
                provider_url=self._provider.base_url,
                finish_reason='content_filter',
            )

        items: list[ModelResponsePart] = []

        if thinking_parts := self._process_thinking(choice.message):
            items.extend(thinking_parts)

        if choice.message.content:
            items.extend(
                (replace(part, id='content', provider_name=self.system) if isinstance(part, ThinkingPart) else part)
                for part in split_content_into_text_and_thinking(choice.message.content, self.profile.thinking_tags)
            )
        if choice.message.tool_calls is not None:
            for c in choice.message.tool_calls:
                if isinstance(c, ChatCompletionMessageFunctionToolCall):
                    part = ToolCallPart(c.function.name, c.function.arguments, tool_call_id=c.id)
                elif isinstance(c, ChatCompletionMessageCustomToolCall):  # pragma: no cover
                    # NOTE: Custom tool calls are not supported.
                    # See <https://github.com/pydantic/pydantic-ai/issues/2513> for more details.
                    raise RuntimeError('Custom tool calls are not supported')
                else:
                    assert_never(c)
                part.tool_call_id = _guard_tool_call_id(part)
                items.append(part)

        provider_details = self._process_provider_details(response)
        if response.created:  # pragma: no branch
            if provider_details is None:
                provider_details = {}
            provider_details['timestamp'] = number_to_datetime(response.created)

        return ModelResponse(
            parts=items,
            usage=self._map_usage(response),
            model_name=response.model,
            timestamp=timestamp,
            provider_details=provider_details or None,
            provider_response_id=response.id,
            provider_name=self._provider.name,
            provider_url=self._provider.base_url,
            finish_reason=self._map_finish_reason(choice.finish_reason),
        )

    def _process_thinking(self, message: chat.ChatCompletionMessage) -> list[ThinkingPart] | None:
        """Hook that maps reasoning tokens to thinking parts.

        This method may be overridden by subclasses of `OpenAIChatModel` to apply custom mappings.
        """
        profile = OpenAIModelProfile.from_profile(self.profile)
        custom_field = profile.openai_chat_thinking_field
        items: list[ThinkingPart] = []

        # Prefer the configured custom reasoning field, if present in profile.
        # Fall back to built-in fields if no custom field result was found.

        # The `reasoning_content` field is typically present in DeepSeek and Moonshot models.
        # https://api-docs.deepseek.com/guides/reasoning_model

        # The `reasoning` field is typically present in gpt-oss via Ollama and OpenRouter.
        # - https://cookbook.openai.com/articles/gpt-oss/handle-raw-cot#chat-completions-api
        # - https://openrouter.ai/docs/use-cases/reasoning-tokens#basic-usage-with-reasoning-tokens
        for field_name in (custom_field, 'reasoning', 'reasoning_content'):
            if not field_name:
                continue
            reasoning: str | None = getattr(message, field_name, None)
            if reasoning:  # pragma: no branch
                items.append(ThinkingPart(id=field_name, content=reasoning, provider_name=self.system))
                return items

        return items or None

    async def _process_streamed_response(
        self,
        response: AsyncStream[ChatCompletionChunk],
        model_request_parameters: ModelRequestParameters,
        model_settings: OpenAIChatModelSettings | None = None,
    ) -> OpenAIStreamedResponse:
        """Process a streamed response, and prepare a streaming response to return."""
        peekable_response = _utils.PeekableAsyncStream(response)
        first_chunk = await peekable_response.peek()
        if isinstance(first_chunk, _utils.Unset):
            raise UnexpectedModelBehavior(  # pragma: no cover
                'Streamed response ended without content or tool calls'
            )

        # When using Azure OpenAI and a content filter is enabled, the first chunk will contain a `''` model name,
        # so we set it from a later chunk in `OpenAIChatStreamedResponse`.
        model_name = first_chunk.model or self.model_name

        return self._streamed_response_cls(
            model_request_parameters=model_request_parameters,
            _model_name=model_name,
            _model_profile=self.profile,
            _response=peekable_response,
            _provider_name=self._provider.name,
            _provider_url=self._provider.base_url,
            _provider_timestamp=number_to_datetime(first_chunk.created) if first_chunk.created else None,
            _model_settings=model_settings,
        )

    @property
    def _streamed_response_cls(self) -> type[OpenAIStreamedResponse]:
        """Returns the `StreamedResponse` type that will be used for streamed responses.

        This method may be overridden by subclasses of `OpenAIChatModel` to provide their own `StreamedResponse` type.
        """
        return OpenAIStreamedResponse

    def _map_usage(self, response: chat.ChatCompletion) -> usage.RequestUsage:
        return _map_usage(response, self._provider.name, self._provider.base_url, self.model_name)

    def _get_stream_options(self, model_settings: OpenAIChatModelSettings) -> chat.ChatCompletionStreamOptionsParam:
        """Build stream_options for the API request.

        Returns a dict with include_usage=True and optionally continuous_usage_stats if configured.
        """
        options: dict[str, bool] = {'include_usage': True}
        if model_settings.get('openai_continuous_usage_stats'):
            options['continuous_usage_stats'] = True
        return cast(chat.ChatCompletionStreamOptionsParam, options)

    def _get_tools(self, model_request_parameters: ModelRequestParameters) -> list[chat.ChatCompletionToolParam]:
        return [self._map_tool_definition(r) for r in model_request_parameters.tool_defs.values()]

    def _get_web_search_options(self, model_request_parameters: ModelRequestParameters) -> WebSearchOptions | None:
        for tool in model_request_parameters.builtin_tools:
            if isinstance(tool, WebSearchTool):  # pragma: no branch
                if tool.user_location:
                    return WebSearchOptions(
                        search_context_size=tool.search_context_size,
                        user_location=WebSearchOptionsUserLocation(
                            type='approximate',
                            approximate=WebSearchOptionsUserLocationApproximate(**tool.user_location),
                        ),
                    )
                return WebSearchOptions(search_context_size=tool.search_context_size)
        return None

    @dataclass
    class _MapModelResponseContext:
        """Context object for mapping a `ModelResponse` to OpenAI chat completion parameters.

        This class is designed to be subclassed to add new fields for custom logic,
        collecting various parts of the model response (like text and tool calls)
        to form a single assistant message.
        """

        _model: OpenAIChatModel

        texts: list[str] = field(default_factory=list[str])
        thinkings: dict[str, list[str]] = field(default_factory=dict[str, list[str]])
        tool_calls: list[ChatCompletionMessageFunctionToolCallParam] = field(
            default_factory=list[ChatCompletionMessageFunctionToolCallParam]
        )

        def map_assistant_message(self, message: ModelResponse) -> chat.ChatCompletionAssistantMessageParam:
            for item in message.parts:
                if isinstance(item, TextPart):
                    self._map_response_text_part(item)
                elif isinstance(item, ThinkingPart):
                    self._map_response_thinking_part(item)
                elif isinstance(item, ToolCallPart):
                    self._map_response_tool_call_part(item)
                elif isinstance(item, BuiltinToolCallPart | BuiltinToolReturnPart):  # pragma: no cover
                    self._map_response_builtin_part(item)
                elif isinstance(item, FilePart):  # pragma: no cover
                    self._map_response_file_part(item)
                else:
                    assert_never(item)
            return self._into_message_param()

        def _into_message_param(self) -> chat.ChatCompletionAssistantMessageParam:
            """Converts the collected texts and tool calls into a single OpenAI `ChatCompletionAssistantMessageParam`.

            This method serves as a hook that can be overridden by subclasses
            to implement custom logic for how collected parts are transformed into the final message parameter.

            Returns:
                An OpenAI `ChatCompletionAssistantMessageParam` object representing the assistant's response.
            """
            message_param = chat.ChatCompletionAssistantMessageParam(role='assistant')
            # Note: model responses from this model should only have one text item, so the following
            # shouldn't merge multiple texts into one unless you switch models between runs:
            if self.thinkings:
                for field_name, contents in self.thinkings.items():
                    message_param[field_name] = '\n\n'.join(contents)
            if self.texts:
                message_param['content'] = '\n\n'.join(self.texts)
            else:
                message_param['content'] = None
            if self.tool_calls:
                message_param['tool_calls'] = self.tool_calls
            return message_param

        def _map_response_text_part(self, item: TextPart) -> None:
            """Maps a `TextPart` to the response context.

            This method serves as a hook that can be overridden by subclasses
            to implement custom logic for handling text parts.
            """
            self.texts.append(item.content)

        def _map_response_thinking_part(self, item: ThinkingPart) -> None:
            """Maps a `ThinkingPart` to the response context.

            This method serves as a hook that can be overridden by subclasses
            to implement custom logic for handling thinking parts.
            """
            profile = OpenAIModelProfile.from_profile(self._model.profile)
            include_method = profile.openai_chat_send_back_thinking_parts

            # Auto-detect: if thinking came from a custom field and from the same provider, use field mode
            # id='content' means it came from tags in content, not a custom field
            if include_method == 'auto':
                # Check if thinking came from a custom field from the same provider
                custom_field = profile.openai_chat_thinking_field
                matches_custom_field = (not custom_field) or (item.id == custom_field)

                if (
                    item.id
                    and item.id != 'content'
                    and item.provider_name == self._model.system
                    and matches_custom_field
                ):
                    # Store both content and field name for later use in _into_message_param
                    self.thinkings.setdefault(item.id, []).append(item.content)
                else:
                    # Fall back to tags mode
                    start_tag, end_tag = self._model.profile.thinking_tags
                    self.texts.append('\n'.join([start_tag, item.content, end_tag]))
            elif include_method == 'tags':
                start_tag, end_tag = self._model.profile.thinking_tags
                self.texts.append('\n'.join([start_tag, item.content, end_tag]))
            elif include_method == 'field':
                field = profile.openai_chat_thinking_field
                if field:  # pragma: no branch
                    self.thinkings.setdefault(field, []).append(item.content)

        def _map_response_tool_call_part(self, item: ToolCallPart) -> None:
            """Maps a `ToolCallPart` to the response context.

            This method serves as a hook that can be overridden by subclasses
            to implement custom logic for handling tool call parts.
            """
            self.tool_calls.append(self._model._map_tool_call(item))

        def _map_response_builtin_part(self, item: BuiltinToolCallPart | BuiltinToolReturnPart) -> None:
            """Maps a built-in tool call or return part to the response context.

            This method serves as a hook that can be overridden by subclasses
            to implement custom logic for handling built-in tool parts.
            """
            # OpenAI doesn't return built-in tool calls
            pass

        def _map_response_file_part(self, item: FilePart) -> None:
            """Maps a `FilePart` to the response context.

            This method serves as a hook that can be overridden by subclasses
            to implement custom logic for handling file parts.
            """
            # Files generated by models are not sent back to models that don't themselves generate files.
            pass

    def _map_model_response(self, message: ModelResponse) -> chat.ChatCompletionMessageParam:
        """Hook that determines how `ModelResponse` is mapped into `ChatCompletionMessageParam` objects before sending.

        Subclasses of `OpenAIChatModel` may override this method to provide their own mapping logic.
        """
        return self._MapModelResponseContext(self).map_assistant_message(message)

    def _map_finish_reason(
        self, key: Literal['stop', 'length', 'tool_calls', 'content_filter', 'function_call']
    ) -> FinishReason | None:
        """Hooks that maps a finish reason key to a [FinishReason][pydantic_ai.messages.FinishReason].

        This method may be overridden by subclasses of `OpenAIChatModel` to accommodate custom keys.
        """
        return _CHAT_FINISH_REASON_MAP.get(key)

    async def _map_messages(
        self, messages: Sequence[ModelMessage], model_request_parameters: ModelRequestParameters
    ) -> list[chat.ChatCompletionMessageParam]:
        """Just maps a `pydantic_ai.Message` to a `openai.types.ChatCompletionMessageParam`."""
        openai_messages: list[chat.ChatCompletionMessageParam] = []
        for message in messages:
            if isinstance(message, ModelRequest):
                async for item in self._map_user_message(message):
                    openai_messages.append(item)
            elif isinstance(message, ModelResponse):
