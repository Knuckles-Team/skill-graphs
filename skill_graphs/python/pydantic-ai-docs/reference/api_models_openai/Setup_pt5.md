        """
        profile = OpenAIModelProfile.from_profile(self.profile)
        send_item_ids = model_settings.get(
            'openai_send_reasoning_ids', profile.openai_supports_encrypted_reasoning_content
        )

        openai_messages: list[responses.ResponseInputItemParam] = []
        for message in messages:
            if isinstance(message, ModelRequest):
                for part in message.parts:
                    if isinstance(part, SystemPromptPart):
                        openai_messages.append(responses.EasyInputMessageParam(role='system', content=part.content))
                    elif isinstance(part, UserPromptPart):
                        openai_messages.append(await self._map_user_prompt(part))
                    elif isinstance(part, ToolReturnPart):
                        call_id = _guard_tool_call_id(t=part)
                        call_id, _ = _split_combined_tool_call_id(call_id)
                        item = FunctionCallOutput(
                            type='function_call_output',
                            call_id=call_id,
                            output=part.model_response_str(),
                        )
                        openai_messages.append(item)
                    elif isinstance(part, RetryPromptPart):
                        if part.tool_name is None:
                            openai_messages.append(
                                Message(role='user', content=[{'type': 'input_text', 'text': part.model_response()}])
                            )
                        else:
                            call_id = _guard_tool_call_id(t=part)
                            call_id, _ = _split_combined_tool_call_id(call_id)
                            item = FunctionCallOutput(
                                type='function_call_output',
                                call_id=call_id,
                                output=part.model_response(),
                            )
                            openai_messages.append(item)
                    else:
                        assert_never(part)
            elif isinstance(message, ModelResponse):
                message_item: responses.ResponseOutputMessageParam | None = None
                reasoning_item: responses.ResponseReasoningItemParam | None = None
                web_search_item: responses.ResponseFunctionWebSearchParam | None = None
                file_search_item: responses.ResponseFileSearchToolCallParam | None = None
                code_interpreter_item: responses.ResponseCodeInterpreterToolCallParam | None = None
                for item in message.parts:
                    should_send_item_id = send_item_ids and (
                        item.provider_name == self.system
                        or (item.provider_name is None and message.provider_name == self.system)
                    )

                    if isinstance(item, TextPart):
                        if item.id and should_send_item_id:
                            if message_item is None or message_item['id'] != item.id:  # pragma: no branch
                                message_item = responses.ResponseOutputMessageParam(
                                    role='assistant',
                                    id=item.id,
                                    content=[],
                                    type='message',
                                    status='completed',
                                )
                                openai_messages.append(message_item)

                            message_item['content'] = [
                                *message_item['content'],
                                responses.ResponseOutputTextParam(
                                    text=item.content, type='output_text', annotations=[]
                                ),
                            ]
                        else:
                            openai_messages.append(
                                responses.EasyInputMessageParam(role='assistant', content=item.content)
                            )
                    elif isinstance(item, ToolCallPart):
                        call_id = _guard_tool_call_id(t=item)
                        call_id, id = _split_combined_tool_call_id(call_id)
                        id = id or item.id

                        param = responses.ResponseFunctionToolCallParam(
                            name=item.tool_name,
                            arguments=item.args_as_json_str(),
                            call_id=call_id,
                            type='function_call',
                        )
                        if profile.openai_responses_requires_function_call_status_none:
                            param['status'] = None  # type: ignore[reportGeneralTypeIssues]
                        if id and should_send_item_id:  # pragma: no branch
                            param['id'] = id
                        openai_messages.append(param)
                    elif isinstance(item, BuiltinToolCallPart):
                        if should_send_item_id:  # pragma: no branch
                            if (
                                item.tool_name == CodeExecutionTool.kind
                                and item.tool_call_id
                                and (args := item.args_as_dict())
                                and (container_id := args.get('container_id'))
                            ):
                                code_interpreter_item = responses.ResponseCodeInterpreterToolCallParam(
                                    id=item.tool_call_id,
                                    code=args.get('code'),
                                    container_id=container_id,
                                    outputs=None,  # These can be read server-side
                                    status='completed',
                                    type='code_interpreter_call',
                                )
                                openai_messages.append(code_interpreter_item)
                            elif (
                                item.tool_name == WebSearchTool.kind
                                and item.tool_call_id
                                and (args := item.args_as_dict())
                            ):
                                # We need to exclude None values because of https://github.com/pydantic/pydantic-ai/issues/3653
                                args = {k: v for k, v in args.items() if v is not None}
                                web_search_item = responses.ResponseFunctionWebSearchParam(
                                    id=item.id or item.tool_call_id,
                                    action=cast(responses.response_function_web_search_param.Action, args),
                                    status='completed',
                                    type='web_search_call',
                                )
                                openai_messages.append(web_search_item)
                            elif (  # pragma: no cover
                                item.tool_name == FileSearchTool.kind
                                and item.tool_call_id
                                and (args := item.args_as_dict())
                            ):
                                file_search_item = cast(
                                    responses.ResponseFileSearchToolCallParam,
                                    {
                                        'id': item.id or item.tool_call_id,
                                        'queries': args.get('queries', []),
                                        'status': 'completed',
                                        'type': 'file_search_call',
                                    },
                                )
                                openai_messages.append(file_search_item)
                            elif item.tool_name == ImageGenerationTool.kind and item.tool_call_id:
                                # The cast is necessary because of https://github.com/openai/openai-python/issues/2648
                                image_generation_item = cast(
                                    responses.response_input_item_param.ImageGenerationCall,
                                    {
                                        'id': item.tool_call_id,
                                        'type': 'image_generation_call',
                                    },
                                )
                                openai_messages.append(image_generation_item)
                            elif (  # pragma: no branch
                                item.tool_name.startswith(MCPServerTool.kind)
                                and item.tool_call_id
                                and (server_id := item.tool_name.split(':', 1)[1])
                                and (args := item.args_as_dict())
                                and (action := args.get('action'))
                            ):
                                if action == 'list_tools':
                                    mcp_list_tools_item = responses.response_input_item_param.McpListTools(
                                        id=item.tool_call_id,
                                        type='mcp_list_tools',
                                        server_label=server_id,
                                        tools=[],  # These can be read server-side
                                    )
                                    openai_messages.append(mcp_list_tools_item)
                                elif (  # pragma: no branch
                                    action == 'call_tool'
                                    and (tool_name := args.get('tool_name'))
                                    and (tool_args := args.get('tool_args'))
                                ):
                                    mcp_call_item = responses.response_input_item_param.McpCall(
                                        id=item.tool_call_id,
                                        server_label=server_id,
                                        name=tool_name,
                                        arguments=to_json(tool_args).decode(),
                                        error=None,  # These can be read server-side
                                        output=None,  # These can be read server-side
                                        type='mcp_call',
                                    )
                                    openai_messages.append(mcp_call_item)

                    elif isinstance(item, BuiltinToolReturnPart):
                        if should_send_item_id:  # pragma: no branch
                            content_is_dict = isinstance(item.content, dict)
                            status = cast(dict[str, Any], item.content).get('status') if content_is_dict else None
                            kind_to_item = {
                                CodeExecutionTool.kind: code_interpreter_item,
                                WebSearchTool.kind: web_search_item,
                                FileSearchTool.kind: file_search_item,
                            }
                            if status and (builtin_item := kind_to_item.get(item.tool_name)) is not None:
                                builtin_item['status'] = status
                            elif item.tool_name == ImageGenerationTool.kind:
                                # Image generation result does not need to be sent back, just the `id` off of `BuiltinToolCallPart`.
                                pass
                            elif item.tool_name.startswith(MCPServerTool.kind):  # pragma: no branch
                                # MCP call result does not need to be sent back, just the fields off of `BuiltinToolCallPart`.
                                pass
                    elif isinstance(item, FilePart):
                        # This was generated by the `ImageGenerationTool` or `CodeExecutionTool`,
                        # and does not need to be sent back separately from the corresponding `BuiltinToolReturnPart`.
                        # If `send_item_ids` is false, we won't send the `BuiltinToolReturnPart`, but OpenAI does not have a type for files from the assistant.
                        pass
                    elif isinstance(item, ThinkingPart):
                        # Get raw CoT content from provider_details if present and from this provider
                        raw_content: list[str] | None = None
                        if item.provider_name == self.system:
                            raw_content = (item.provider_details or {}).get('raw_content')

                        if item.id and (should_send_item_id or raw_content):
                            signature: str | None = None
                            if (
                                item.signature
                                and item.provider_name == self.system
                                and profile.openai_supports_encrypted_reasoning_content
                            ):
                                signature = item.signature

                            if (reasoning_item is None or reasoning_item['id'] != item.id) and (
                                signature or item.content or raw_content
                            ):  # pragma: no branch
                                reasoning_item = responses.ResponseReasoningItemParam(
                                    id=item.id,
                                    summary=[],
                                    encrypted_content=signature,
                                    type='reasoning',
                                )
                                openai_messages.append(reasoning_item)

                            if item.content:
                                # The check above guarantees that `reasoning_item` is not None
                                assert reasoning_item is not None
                                reasoning_item['summary'] = [
                                    *reasoning_item['summary'],
                                    ReasoningSummary(text=item.content, type='summary_text'),
                                ]

                            if raw_content:
                                # Send raw CoT back
                                assert reasoning_item is not None
                                reasoning_item['content'] = [
                                    ReasoningContent(text=text, type='reasoning_text') for text in raw_content
                                ]
                        else:
                            start_tag, end_tag = profile.thinking_tags
                            openai_messages.append(
                                responses.EasyInputMessageParam(
                                    role='assistant', content='\n'.join([start_tag, item.content, end_tag])
                                )
                            )
                    else:
                        assert_never(item)
            else:
                assert_never(message)
        instructions = self._get_instructions(messages, model_request_parameters) or OMIT
        return instructions, openai_messages

    def _map_json_schema(self, o: OutputObjectDefinition) -> responses.ResponseFormatTextJSONSchemaConfigParam:
        response_format_param: responses.ResponseFormatTextJSONSchemaConfigParam = {
            'type': 'json_schema',
            'name': o.name or DEFAULT_OUTPUT_TOOL_NAME,
            'schema': o.json_schema,
        }
        if o.description:
            response_format_param['description'] = o.description
        if OpenAIModelProfile.from_profile(self.profile).openai_supports_strict_tool_definition:  # pragma: no branch
            response_format_param['strict'] = o.strict
        return response_format_param

    async def _map_user_prompt(self, part: UserPromptPart) -> responses.EasyInputMessageParam:  # noqa: C901
        content: str | list[responses.ResponseInputContentParam]
        if isinstance(part.content, str):
            content = part.content
        else:
            content = []
            for item in part.content:
                if isinstance(item, str):
                    content.append(responses.ResponseInputTextParam(text=item, type='input_text'))
                elif isinstance(item, BinaryContent):
                    if item.is_image:
                        detail: Literal['auto', 'low', 'high'] = 'auto'
                        if metadata := item.vendor_metadata:
                            detail = cast(
                                Literal['auto', 'low', 'high'],
                                metadata.get('detail', 'auto'),
                            )
                        content.append(
                            responses.ResponseInputImageParam(
                                image_url=item.data_uri,
                                type='input_image',
                                detail=detail,
                            )
                        )
                    elif item.is_document:
                        content.append(
                            responses.ResponseInputFileParam(
                                type='input_file',
                                file_data=item.data_uri,
                                # NOTE: Type wise it's not necessary to include the filename, but it's required by the
                                # API itself. If we add empty string, the server sends a 500 error - which OpenAI needs
                                # to fix. In any case, we add a placeholder name.
                                filename=f'filename.{item.format}',
                            )
                        )
                    elif item.is_audio:
                        raise NotImplementedError('Audio as binary content is not supported for OpenAI Responses API.')
                    else:  # pragma: no cover
                        raise RuntimeError(f'Unsupported binary content type: {item.media_type}')
                elif isinstance(item, ImageUrl):
                    detail: Literal['auto', 'low', 'high'] = 'auto'
                    image_url = item.url
                    if metadata := item.vendor_metadata:
                        detail = cast(Literal['auto', 'low', 'high'], metadata.get('detail', 'auto'))
                    if item.force_download:
                        downloaded_item = await download_item(item, data_format='base64_uri', type_format='extension')
                        image_url = downloaded_item['data']

                    content.append(
                        responses.ResponseInputImageParam(
                            image_url=image_url,
                            type='input_image',
                            detail=detail,
                        )
                    )
                elif isinstance(item, AudioUrl | DocumentUrl):
                    if item.force_download:
                        downloaded_item = await download_item(item, data_format='base64_uri', type_format='extension')
                        content.append(
                            responses.ResponseInputFileParam(
                                type='input_file',
                                file_data=downloaded_item['data'],
                                filename=f'filename.{downloaded_item["data_type"]}',
                            )
                        )
                    else:
                        content.append(
                            responses.ResponseInputFileParam(
                                type='input_file',
                                file_url=item.url,
                            )
                        )
                elif isinstance(item, VideoUrl):  # pragma: no cover
                    raise NotImplementedError('VideoUrl is not supported for OpenAI.')
                elif isinstance(item, UploadedFile):
                    # Verify provider matches
                    if item.provider_name != self.system:
                        raise UserError(
                            f'UploadedFile with `provider_name={item.provider_name!r}` cannot be used with OpenAIResponsesModel. '
                            f'Expected `provider_name` to be `{self.system!r}`.'
                        )
                    content.append(
                        responses.ResponseInputFileParam(
                            type='input_file',
                            file_id=item.file_id,
                        )
                    )
                elif isinstance(item, CachePoint):
                    # OpenAI doesn't support prompt caching via CachePoint, so we filter it out
                    pass
                else:
                    assert_never(item)
        return responses.EasyInputMessageParam(role='user', content=content)

```

---|---
####  __init__
```
__init__(
    model_name: OpenAIModelName[](https://ai.pydantic.dev/api/models/openai/#pydantic_ai.models.openai.OpenAIModelName "OpenAIModelName



      module-attribute
   \(pydantic_ai.models.openai.OpenAIModelName\)"),
    *,
    provider: (
        OpenAIResponsesCompatibleProvider
        | ["openai", "gateway"]
        | Provider[](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.Provider "pydantic_ai.providers.Provider")[AsyncOpenAI]
    ) = "openai",
    profile: ModelProfileSpec | None = None,
    settings: ModelSettings[](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "ModelSettings \(pydantic_ai.settings.ModelSettings\)") | None = None
)

```

Initialize an OpenAI Responses model.
Parameters:
Name | Type | Description | Default
---|---|---|---
`model_name` |  `OpenAIModelName[](https://ai.pydantic.dev/api/models/openai/#pydantic_ai.models.openai.OpenAIModelName "OpenAIModelName



      module-attribute
   \(pydantic_ai.models.openai.OpenAIModelName\)")` |  The name of the OpenAI model to use. |  _required_
`provider` |  `OpenAIResponsesCompatibleProvider | Provider[](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.Provider "pydantic_ai.providers.Provider")[AsyncOpenAI]` |  The provider to use. Defaults to `'openai'`. |  `'openai'`
`profile` |  `ModelProfileSpec | None` |  The model profile to use. Defaults to a profile picked by the provider based on the model name. |  `None`
`settings` |  `ModelSettings[](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "ModelSettings \(pydantic_ai.settings.ModelSettings\)") | None` |  Default model settings for this model instance. |  `None`
Source code in `pydantic_ai_slim/pydantic_ai/models/openai.py`
```
1352
1353
1354
1355
1356
1357
1358
1359
1360
1361
1362
1363
1364
1365
1366
1367
1368
1369
1370
1371
1372
1373
1374
1375
1376
1377
1378
1379
1380
```
| ```
def __init__(
    self,
    model_name: OpenAIModelName,
    *,
    provider: OpenAIResponsesCompatibleProvider
    | Literal[
        'openai',
        'gateway',
    ]
    | Provider[AsyncOpenAI] = 'openai',
    profile: ModelProfileSpec | None = None,
    settings: ModelSettings | None = None,
):
    """Initialize an OpenAI Responses model.

    Args:
        model_name: The name of the OpenAI model to use.
        provider: The provider to use. Defaults to `'openai'`.
        profile: The model profile to use. Defaults to a profile picked by the provider based on the model name.
        settings: Default model settings for this model instance.
    """
    self._model_name = model_name

    if isinstance(provider, str):
        provider = infer_provider('gateway/openai' if provider == 'gateway' else provider)
    self._provider = provider
    self.client = provider.client

    super().__init__(settings=settings, profile=profile or provider.model_profile)

```

---|---
####  model_name `property`
```
model_name: OpenAIModelName[](https://ai.pydantic.dev/api/models/openai/#pydantic_ai.models.openai.OpenAIModelName "OpenAIModelName



      module-attribute
   \(pydantic_ai.models.openai.OpenAIModelName\)")

```

The model name.
####  system `property`
```
system:

```

The model provider.
####  supported_builtin_tools `classmethod`
```
supported_builtin_tools() -> (
    [[AbstractBuiltinTool[](https://ai.pydantic.dev/api/builtin_tools/#pydantic_ai.builtin_tools.AbstractBuiltinTool "AbstractBuiltinTool



      dataclass
   \(pydantic_ai.builtin_tools.AbstractBuiltinTool\)")]]
)

```

Return the set of builtin tool types this model can handle.
Source code in `pydantic_ai_slim/pydantic_ai/models/openai.py`
```
1396
1397
1398
1399
```
| ```
@classmethod
def supported_builtin_tools(cls) -> frozenset[type[AbstractBuiltinTool]]:
    """Return the set of builtin tool types this model can handle."""
    return frozenset({WebSearchTool, CodeExecutionTool, FileSearchTool, MCPServerTool, ImageGenerationTool})

```

---|---
###  OpenAIStreamedResponse `dataclass`
Bases: `StreamedResponse[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.StreamedResponse "StreamedResponse



      dataclass
   \(pydantic_ai.models.StreamedResponse\)")`
Implementation of `StreamedResponse` for OpenAI models.
Source code in `pydantic_ai_slim/pydantic_ai/models/openai.py`
```
2255
2256
2257
2258
2259
2260
2261
2262
2263
2264
2265
2266
2267
2268
2269
2270
2271
2272
2273
2274
2275
2276
2277
2278
2279
2280
2281
2282
2283
2284
2285
2286
2287
2288
2289
2290
2291
2292
2293
2294
2295
2296
2297
2298
2299
