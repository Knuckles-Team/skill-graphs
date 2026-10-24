        if tool_config:
            params['toolConfig'] = tool_config

        tools: list[ToolTypeDef] = list(tool_config['tools']) if tool_config else []
        self._limit_cache_points(system_prompt, bedrock_messages, tools)

        # Bedrock supports a set of specific extra parameters
        if model_settings:
            if guardrail_config := model_settings.get('bedrock_guardrail_config', None):
                params['guardrailConfig'] = guardrail_config
            if performance_configuration := model_settings.get('bedrock_performance_configuration', None):
                params['performanceConfig'] = performance_configuration
            if request_metadata := model_settings.get('bedrock_request_metadata', None):
                params['requestMetadata'] = request_metadata
            if additional_model_response_fields_paths := model_settings.get(
                'bedrock_additional_model_response_fields_paths', None
            ):
                params['additionalModelResponseFieldPaths'] = additional_model_response_fields_paths
            if additional_model_requests_fields := model_settings.get('bedrock_additional_model_requests_fields', None):
                params['additionalModelRequestFields'] = additional_model_requests_fields
            if prompt_variables := model_settings.get('bedrock_prompt_variables', None):
                params['promptVariables'] = prompt_variables
            if service_tier := model_settings.get('bedrock_service_tier', None):
                params['serviceTier'] = service_tier

        try:
            if stream:
                model_response = await anyio.to_thread.run_sync(
                    functools.partial(self.client.converse_stream, **params)
                )
            else:
                model_response = await anyio.to_thread.run_sync(functools.partial(self.client.converse, **params))
        except ClientError as e:
            status_code = e.response.get('ResponseMetadata', {}).get('HTTPStatusCode')
            if isinstance(status_code, int):
                raise ModelHTTPError(status_code=status_code, model_name=self.model_name, body=e.response) from e
            raise ModelAPIError(model_name=self.model_name, message=str(e)) from e
        return model_response

    @staticmethod
    def _map_inference_config(
        model_settings: ModelSettings | None,
    ) -> InferenceConfigurationTypeDef:
        model_settings = model_settings or {}
        inference_config: InferenceConfigurationTypeDef = {}

        if max_tokens := model_settings.get('max_tokens'):
            inference_config['maxTokens'] = max_tokens
        if (temperature := model_settings.get('temperature')) is not None:
            inference_config['temperature'] = temperature
        if top_p := model_settings.get('top_p'):
            inference_config['topP'] = top_p
        if stop_sequences := model_settings.get('stop_sequences'):
            inference_config['stopSequences'] = stop_sequences

        return inference_config

    def _map_tool_config(
        self,
        model_request_parameters: ModelRequestParameters,
        model_settings: BedrockModelSettings | None,
    ) -> ToolConfigurationTypeDef | None:
        tools = self._get_tools(model_request_parameters)
        for tool in model_request_parameters.builtin_tools:
            if tool.kind == CodeExecutionTool.kind:
                tools.append({'systemTool': {'name': 'nova_code_interpreter'}})
            else:
                raise NotImplementedError(
                    f"Builtin tool '{tool.kind}' is not supported yet. If it should be, please file an issue."
                )

        if not tools:
            return None

        profile = BedrockModelProfile.from_profile(self.profile)
        if (
            model_settings
            and model_settings.get('bedrock_cache_tool_definitions')
            and profile.bedrock_supports_tool_caching
        ):
            tools.append({'cachePoint': {'type': 'default'}})

        tool_choice: ToolChoiceTypeDef
        if not model_request_parameters.allow_text_output:
            tool_choice = {'any': {}}
        else:
            tool_choice = {'auto': {}}

        tool_config: ToolConfigurationTypeDef = {'tools': tools}
        if tool_choice and BedrockModelProfile.from_profile(self.profile).bedrock_supports_tool_choice:
            tool_config['toolChoice'] = tool_choice

        return tool_config

    async def _map_messages(  # noqa: C901
        self,
        messages: Sequence[ModelMessage],
        model_request_parameters: ModelRequestParameters,
        model_settings: BedrockModelSettings | None,
    ) -> tuple[list[SystemContentBlockTypeDef], list[MessageUnionTypeDef]]:
        """Maps a `pydantic_ai.Message` to the Bedrock `MessageUnionTypeDef`.

        Groups consecutive ToolReturnPart objects into a single user message as required by Bedrock Claude/Nova models.
        """
        settings = model_settings or BedrockModelSettings()
        profile = BedrockModelProfile.from_profile(self.profile)
        system_prompt: list[SystemContentBlockTypeDef] = []
        bedrock_messages: list[MessageUnionTypeDef] = []
        document_count: Iterator[int] = count(1)
        for message in messages:
            if isinstance(message, ModelRequest):
                for part in message.parts:
                    if isinstance(part, SystemPromptPart):
                        if part.content:  # pragma: no branch
                            system_prompt.append({'text': part.content})
                    elif isinstance(part, UserPromptPart):
                        bedrock_messages.extend(
                            await self._map_user_prompt(part, document_count, profile.bedrock_supports_prompt_caching)
                        )
                    elif isinstance(part, ToolReturnPart):
                        assert part.tool_call_id is not None
                        bedrock_messages.append(
                            {
                                'role': 'user',
                                'content': [
                                    {
                                        'toolResult': {
                                            'toolUseId': part.tool_call_id,
                                            'content': [
                                                {'text': part.model_response_str()}
                                                if profile.bedrock_tool_result_format == 'text'
                                                else {'json': part.model_response_object()}
                                            ],
                                            'status': 'success',
                                        }
                                    }
                                ],
                            }
                        )
                    elif isinstance(part, RetryPromptPart):
                        if part.tool_name is None:
                            bedrock_messages.append({'role': 'user', 'content': [{'text': part.model_response()}]})
                        else:
                            assert part.tool_call_id is not None
                            bedrock_messages.append(
                                {
                                    'role': 'user',
                                    'content': [
                                        {
                                            'toolResult': {
                                                'toolUseId': part.tool_call_id,
                                                'content': [{'text': part.model_response()}],
                                                'status': 'error',
                                            }
                                        }
                                    ],
                                }
                            )
                    else:
                        assert_never(part)
            elif isinstance(message, ModelResponse):
                content: list[ContentBlockOutputTypeDef] = []
                for item in message.parts:
                    if isinstance(item, TextPart):
                        content.append({'text': item.content})
                    elif isinstance(item, ThinkingPart):
                        if (
                            item.provider_name == self.system
                            and item.signature
                            and BedrockModelProfile.from_profile(self.profile).bedrock_send_back_thinking_parts
                        ):
                            if item.id == 'redacted_content':
                                reasoning_content: ReasoningContentBlockOutputTypeDef = {
                                    'redactedContent': item.signature.encode('utf-8'),
                                }
                            else:
                                reasoning_content: ReasoningContentBlockOutputTypeDef = {
                                    'reasoningText': {
                                        'text': item.content,
                                        'signature': item.signature,
                                    }
                                }
                            content.append({'reasoningContent': reasoning_content})
                        else:
                            start_tag, end_tag = self.profile.thinking_tags
                            content.append({'text': '\n'.join([start_tag, item.content, end_tag])})
                    elif isinstance(item, BuiltinToolCallPart):
                        if item.provider_name == self.system:
                            if item.tool_name == CodeExecutionTool.kind:
                                server_tool_use_block_param: ToolUseBlockOutputTypeDef = {
                                    'toolUseId': _utils.guard_tool_call_id(t=item),
                                    'name': 'nova_code_interpreter',
                                    'input': item.args_as_dict(),
                                    'type': 'server_tool_use',
                                }
                                content.append({'toolUse': server_tool_use_block_param})
                    elif isinstance(item, BuiltinToolReturnPart):
                        if item.provider_name == self.system:
                            if item.tool_name == CodeExecutionTool.kind:
                                tool_result: ToolResultBlockOutputTypeDef = {
                                    'toolUseId': _utils.guard_tool_call_id(t=item),
                                    'content': [{'json': cast(Any, item.content)}] if item.content else [],
                                    'type': 'nova_code_interpreter_result',
                                }
                                if item.provider_details and 'status' in item.provider_details:
                                    tool_result['status'] = item.provider_details['status']
                                content.append({'toolResult': tool_result})
                    else:
                        assert isinstance(item, ToolCallPart)
                        content.append(self._map_tool_call(item))
                if content:
                    bedrock_messages.append({'role': 'assistant', 'content': content})
            else:
                assert_never(message)

        # Merge together sequential user messages.
        processed_messages: list[MessageUnionTypeDef] = []
        last_message: dict[str, Any] | None = None
        for current_message in bedrock_messages:
            if (
                last_message is not None
                and current_message['role'] == last_message['role']
                and current_message['role'] == 'user'
            ):
                # Add the new user content onto the existing user message.
                last_content = list(last_message['content'])
                last_content.extend(current_message['content'])
                last_message['content'] = last_content
                continue

            # Add the entire message to the list of messages.
            processed_messages.append(current_message)
            last_message = cast(dict[str, Any], current_message)

        if instructions := self._get_instructions(messages, model_request_parameters):
            system_prompt.append({'text': instructions})

        if system_prompt and settings.get('bedrock_cache_instructions') and profile.bedrock_supports_prompt_caching:
            system_prompt.append({'cachePoint': {'type': 'default'}})

        if processed_messages and settings.get('bedrock_cache_messages') and profile.bedrock_supports_prompt_caching:
            last_user_content = self._get_last_user_message_content(processed_messages)
            if last_user_content is not None:
                # Note: _get_last_user_message_content ensures content doesn't already end with a cachePoint.
                _insert_cache_point_before_trailing_documents(last_user_content)

        return system_prompt, processed_messages

    @staticmethod
    def _get_last_user_message_content(messages: list[MessageUnionTypeDef]) -> list[Any] | None:
        """Get the content list from the last user message that can receive a cache point.

        Returns the content list if:
        - A user message exists
        - It has a non-empty content list
        - The last content block doesn't already have a cache point

        Returns None otherwise.
        """
        user_messages = [msg for msg in messages if msg.get('role') == 'user']
        if not user_messages:
            return None

        content = user_messages[-1].get('content')  # Last user message
        if not content or not isinstance(content, list) or len(content) == 0:
            return None

        last_block = content[-1]
        if not isinstance(last_block, dict):
            return None
        if 'cachePoint' in last_block:  # Skip if already has a cache point
            return None
        return content

    async def _map_user_prompt(  # noqa: C901
        self,
        part: UserPromptPart,
        document_count: Iterator[int],
        supports_prompt_caching: bool,
    ) -> list[MessageUnionTypeDef]:
        content: list[ContentBlockUnionTypeDef] = []
        if isinstance(part.content, str):
            content.append({'text': part.content})
        else:
            for item in part.content:
                if isinstance(item, str):
                    content.append({'text': item})
                elif isinstance(item, BinaryContent):
                    format = item.format
                    source: DocumentSourceTypeDef = {'bytes': item.data}
                    if item.is_document:
                        content.append(_make_document_block(f'Document {next(document_count)}', format, source))
                    elif item.is_image:
                        content.append(_make_image_block(format, source))
                    elif item.is_video:
                        content.append(_make_video_block(format, source))
                    else:
                        raise NotImplementedError('Binary content is not supported yet.')
                elif isinstance(item, ImageUrl | DocumentUrl | VideoUrl):
                    if item.url.startswith('s3://'):
                        source = _parse_s3_source(item.url)
                    else:
                        downloaded_item = await download_item(item, data_format='bytes', type_format='extension')
                        source = {'bytes': downloaded_item['data']}

                    try:
                        format = item.format
                    except (KeyError, ValueError):
                        # Unknown media type — fall back to raw subtype so the
                        # validation inside _make_*_block produces a clear UserError.
                        format = item.media_type.split('/', 1)[1]

                    if item.kind == 'image-url':
                        content.append(_make_image_block(format, source))
                    elif item.kind == 'document-url':
                        content.append(_make_document_block(f'Document {next(document_count)}', format, source))
                    elif item.kind == 'video-url':  # pragma: no branch
                        content.append(_make_video_block(format, source))
                elif isinstance(item, AudioUrl):  # pragma: no cover
                    raise NotImplementedError('Audio is not supported yet.')
                elif isinstance(item, UploadedFile):
                    # Verify provider matches
                    if item.provider_name != self.system:
                        raise UserError(
                            f'UploadedFile with `provider_name={item.provider_name!r}` cannot be used with BedrockConverseModel. '
                            f'Expected `provider_name` to be `{self.system!r}`.'
                        )
                    # UploadedFile.file_id should be an S3 URL for Bedrock
                    if not item.file_id.startswith('s3://'):
                        raise UserError(
                            f'UploadedFile for Bedrock must use an S3 URL (s3://bucket/key), got: {item.file_id}'
                        )
                    source = _parse_s3_source(item.file_id)

                    try:
                        format = item.format
                    except ValueError as e:
                        raise UserError(f'Unsupported media type for Bedrock UploadedFile: {item.media_type}') from e

                    if item.media_type.startswith('image/'):
                        content.append(_make_image_block(format, source))
                    elif item.media_type.startswith('video/'):
                        content.append(_make_video_block(format, source))
                    elif item.media_type.startswith('audio/'):
                        raise UserError('Audio files are not supported for Bedrock UploadedFile')
                    else:
                        content.append(_make_document_block(f'Document {next(document_count)}', format, source))
                elif isinstance(item, CachePoint):
                    if not supports_prompt_caching:
                        # Silently skip CachePoint for models that don't support prompt caching
                        continue
                    if not content or 'cachePoint' in content[-1]:
                        raise UserError(
                            'CachePoint cannot be the first content in a user message - there must be previous content to cache when using Bedrock. '
                            'To cache system instructions or tool definitions, use the `bedrock_cache_instructions` or `bedrock_cache_tool_definitions` settings instead.'
                        )
                    _insert_cache_point_before_trailing_documents(content, raise_if_cannot_insert=True)
                else:
                    assert_never(item)
        return [{'role': 'user', 'content': content}]

    @staticmethod
    def _map_tool_call(t: ToolCallPart) -> ContentBlockOutputTypeDef:
        return {
            'toolUse': {'toolUseId': _utils.guard_tool_call_id(t=t), 'name': t.tool_name, 'input': t.args_as_dict()}
        }

    @staticmethod
    def _limit_cache_points(
        system_prompt: list[SystemContentBlockTypeDef],
        bedrock_messages: list[MessageUnionTypeDef],
        tools: list[ToolTypeDef],
    ) -> None:
        """Limit the number of cache points in the request to Bedrock's maximum.

        Bedrock enforces a maximum of 4 cache points per request. This method ensures
        compliance by counting existing cache points and removing excess ones from messages.

        Strategy:
        1. Count cache points in system_prompt
        2. Count cache points in tools
        3. Raise UserError if system + tools already exceed MAX_CACHE_POINTS
        4. Calculate remaining budget for message cache points
        5. Traverse messages from newest to oldest, keeping the most recent cache points
           within the remaining budget
        6. Remove excess cache points from older messages to stay within limit

        Cache point priority (always preserved):
        - System prompt cache points
        - Tool definition cache points
        - Message cache points (newest first, oldest removed if needed)

        Raises:
            UserError: If system_prompt and tools combined already exceed MAX_CACHE_POINTS (4).
                      This indicates a configuration error that cannot be auto-fixed.
        """
        MAX_CACHE_POINTS = 4

        # Count existing cache points in system prompt
        used_cache_points = sum(1 for block in system_prompt if 'cachePoint' in block)

        # Count existing cache points in tools
        for tool in tools:
            if 'cachePoint' in tool:
                used_cache_points += 1

        # Calculate remaining cache points budget for messages
        remaining_budget = MAX_CACHE_POINTS - used_cache_points
        if remaining_budget < 0:  # pragma: no cover
            raise UserError(
                f'Too many cache points for Bedrock request. '
                f'System prompt and tool definitions already use {used_cache_points} cache points, '
                f'which exceeds the maximum of {MAX_CACHE_POINTS}.'
            )

        # Remove excess cache points from messages (newest to oldest)
        for message in reversed(bedrock_messages):
            content = message.get('content')
            if not content or not isinstance(content, list):  # pragma: no cover
                continue

            # Build a new content list, keeping only cache points within budget
            new_content: list[Any] = []
            for block in reversed(content):  # Process newest first
                is_cache_point = isinstance(block, dict) and 'cachePoint' in block
                if is_cache_point:
                    if remaining_budget > 0:
                        remaining_budget -= 1
                        new_content.append(block)
                else:
                    new_content.append(block)
            message['content'] = list(reversed(new_content))  # Restore original order

```

---|---
####  __init__
```
__init__(
    model_name: BedrockModelName[](https://ai.pydantic.dev/api/models/bedrock/#pydantic_ai.models.bedrock.BedrockModelName "BedrockModelName



      module-attribute
   \(pydantic_ai.models.bedrock.BedrockModelName\)"),
    *,
    provider: (
        ["bedrock", "gateway"] | Provider[](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.Provider "pydantic_ai.providers.Provider")[BaseClient]
    ) = "bedrock",
    profile: ModelProfileSpec | None = None,
    settings: ModelSettings[](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "ModelSettings \(pydantic_ai.settings.ModelSettings\)") | None = None
)

```

Initialize a Bedrock model.
Parameters:
Name | Type | Description | Default
---|---|---|---
`model_name` |  `BedrockModelName[](https://ai.pydantic.dev/api/models/bedrock/#pydantic_ai.models.bedrock.BedrockModelName "BedrockModelName



      module-attribute
   \(pydantic_ai.models.bedrock.BedrockModelName\)")` |  The name of the model to use. |  _required_
`model_name` |  `BedrockModelName[](https://ai.pydantic.dev/api/models/bedrock/#pydantic_ai.models.bedrock.BedrockModelName "BedrockModelName



      module-attribute
   \(pydantic_ai.models.bedrock.BedrockModelName\)")` |  The name of the Bedrock model to use. List of model names available  |  _required_
`provider` |  `Provider[](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.Provider "pydantic_ai.providers.Provider")[BaseClient]` |  The provider to use for authentication and API access. Can be either the string 'bedrock' or an instance of `Provider[BaseClient]`. If not provided, a new provider will be created using the other parameters. |  `'bedrock'`
`profile` |  `ModelProfileSpec | None` |  The model profile to use. Defaults to a profile picked by the provider based on the model name. |  `None`
`settings` |  `ModelSettings[](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "ModelSettings \(pydantic_ai.settings.ModelSettings\)") | None` |  Model-specific settings that will be used as defaults for this model. |  `None`
Source code in `pydantic_ai_slim/pydantic_ai/models/bedrock.py`
```
343
344
345
346
347
348
349
350
351
352
353
354
355
356
357
358
359
360
361
362
363
364
365
366
367
368
369
370
```
| ```
def __init__(
    self,
    model_name: BedrockModelName,
    *,
    provider: Literal['bedrock', 'gateway'] | Provider[BaseClient] = 'bedrock',
    profile: ModelProfileSpec | None = None,
    settings: ModelSettings | None = None,
):
    """Initialize a Bedrock model.

    Args:
        model_name: The name of the model to use.
        model_name: The name of the Bedrock model to use. List of model names available
            [here](https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html).
        provider: The provider to use for authentication and API access. Can be either the string
            'bedrock' or an instance of `Provider[BaseClient]`. If not provided, a new provider will be
            created using the other parameters.
        profile: The model profile to use. Defaults to a profile picked by the provider based on the model name.
        settings: Model-specific settings that will be used as defaults for this model.
