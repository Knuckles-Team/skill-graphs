        if system_prompt and (cache_instructions := model_settings.get('anthropic_cache_instructions')):
            # If True, use '5m'; otherwise use the specified ttl value
            ttl: Literal['5m', '1h'] = '5m' if cache_instructions is True else cache_instructions
            system_prompt_blocks = [
                BetaTextBlockParam(
                    type='text',
                    text=system_prompt,
                    cache_control=self._build_cache_control(ttl),
                )
            ]
            return system_prompt_blocks, anthropic_messages

        return system_prompt, anthropic_messages

    @staticmethod
    def _limit_cache_points(
        system_prompt: str | list[BetaTextBlockParam],
        anthropic_messages: list[BetaMessageParam],
        tools: list[BetaToolUnionParam],
    ) -> None:
        """Limit the number of cache points in the request to Anthropic's maximum.

        Anthropic enforces a maximum of 4 cache points per request. This method ensures
        compliance by counting existing cache points and removing excess ones from messages.

        Strategy:
        1. Count cache points in system_prompt (can be multiple if list of blocks)
        2. Count cache points in tools (can be in any position, not just last)
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
        used_cache_points = (
            sum(1 for block in system_prompt if 'cache_control' in cast(dict[str, Any], block))
            if isinstance(system_prompt, list)
            else 0
        )

        # Count existing cache points in tools (any tool may have cache_control)
        # Note: cache_control can be in the middle of tools list if builtin tools are added after
        for tool in tools:
            if 'cache_control' in tool:
                used_cache_points += 1

        # Calculate remaining cache points budget for messages
        remaining_budget = MAX_CACHE_POINTS - used_cache_points
        if remaining_budget < 0:  # pragma: no cover
            raise UserError(
                f'Too many cache points for Anthropic request. '
                f'System prompt and tool definitions already use {used_cache_points} cache points, '
                f'which exceeds the maximum of {MAX_CACHE_POINTS}.'
            )
        # Remove excess cache points from messages (newest to oldest)
        for message in reversed(anthropic_messages):
            content = message['content']
            if isinstance(content, str):  # pragma: no cover
                continue

            # Process content blocks in reverse order (newest first)
            for block in reversed(cast(list[BetaContentBlockParam], content)):
                block_dict = cast(dict[str, Any], block)

                if 'cache_control' in block_dict:
                    if remaining_budget > 0:
                        remaining_budget -= 1
                    else:
                        # Exceeded limit, remove this cache point
                        del block_dict['cache_control']

    def _build_cache_control(self, ttl: Literal['5m', '1h'] = '5m') -> BetaCacheControlEphemeralParam:
        """Build cache control dict, automatically omitting TTL for Bedrock clients.

        Args:
            ttl: The cache time-to-live ('5m' or '1h'). Ignored for Bedrock clients.

        Returns:
            A cache control dict suitable for the current client type.
        """
        if isinstance(self.client, AsyncAnthropicBedrock):
            # Bedrock doesn't support TTL, use cast to satisfy type checker
            return cast(BetaCacheControlEphemeralParam, {'type': 'ephemeral'})
        return BetaCacheControlEphemeralParam(type='ephemeral', ttl=ttl)

    def _add_cache_control_to_last_param(
        self, params: list[BetaContentBlockParam], ttl: Literal['5m', '1h'] = '5m'
    ) -> None:
        """Add cache control to the last content block param.

        See https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching for more information.

        Args:
            params: List of content block params to modify.
            ttl: The cache time-to-live ('5m' or '1h'). This is automatically ignored for
                 Bedrock clients, which don't support explicit TTL parameters.
        """
        if not params:
            raise UserError(
                'CachePoint cannot be the first content in a user message - there must be previous content to attach the CachePoint to. '
                'To cache system instructions or tool definitions, use the `anthropic_cache_instructions` or `anthropic_cache_tool_definitions` settings instead.'
            )

        # Only certain types support cache_control
        # See https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching#what-can-be-cached
        cacheable_types = {'text', 'tool_use', 'server_tool_use', 'image', 'tool_result', 'document'}
        # Cast needed because BetaContentBlockParam is a union including response Block types (Pydantic models)
        # that don't support dict operations, even though at runtime we only have request Param types (TypedDicts).
        last_param = cast(dict[str, Any], params[-1])
        if last_param['type'] not in cacheable_types:
            raise UserError(f'Cache control not supported for param type: {last_param["type"]}')

        # Add cache_control to the last param
        last_param['cache_control'] = self._build_cache_control(ttl)

    @staticmethod
    def _map_binary_data(data: bytes, media_type: str) -> BetaContentBlockParam:
        # Anthropic SDK accepts file-like objects (IO[bytes]) and handles base64 encoding internally
        if media_type.startswith('image/'):
            return BetaImageBlockParam(
                source={'data': io.BytesIO(data), 'media_type': media_type, 'type': 'base64'},  # type: ignore
                type='image',
            )
        elif media_type == 'application/pdf':
            return BetaRequestDocumentBlockParam(
                source=BetaBase64PDFSourceParam(
                    data=io.BytesIO(data),
                    media_type='application/pdf',
                    type='base64',
                ),
                type='document',
            )
        elif media_type == 'text/plain':
            return BetaRequestDocumentBlockParam(
                source=BetaPlainTextSourceParam(data=data.decode('utf-8'), media_type=media_type, type='text'),
                type='document',
            )
        else:
            raise RuntimeError(f'Unsupported binary content media type for Anthropic: {media_type}')

    async def _map_user_prompt(  # noqa: C901
        self,
        part: UserPromptPart,
    ) -> AsyncGenerator[BetaContentBlockParam | CachePoint]:
        if isinstance(part.content, str):
            if part.content:  # Only yield non-empty text
                yield BetaTextBlockParam(text=part.content, type='text')
        else:
            for item in part.content:
                if isinstance(item, str):
                    if item:  # Only yield non-empty text
                        yield BetaTextBlockParam(text=item, type='text')
                elif isinstance(item, CachePoint):
                    yield item
                elif isinstance(item, BinaryContent):
                    yield AnthropicModel._map_binary_data(item.data, item.media_type)
                elif isinstance(item, ImageUrl):
                    if item.force_download:
                        downloaded = await download_item(item, data_format='bytes')
                        yield AnthropicModel._map_binary_data(downloaded['data'], item.media_type)
                    else:
                        yield BetaImageBlockParam(source={'type': 'url', 'url': item.url}, type='image')
                elif isinstance(item, DocumentUrl):
                    if item.media_type == 'application/pdf':
                        if item.force_download:
                            downloaded = await download_item(item, data_format='bytes')
                            yield AnthropicModel._map_binary_data(downloaded['data'], item.media_type)
                        else:
                            yield BetaRequestDocumentBlockParam(
                                source={'url': item.url, 'type': 'url'}, type='document'
                            )
                    elif item.media_type == 'text/plain':
                        downloaded_item = await download_item(item, data_format='text')
                        yield BetaRequestDocumentBlockParam(
                            source=BetaPlainTextSourceParam(
                                data=downloaded_item['data'], media_type=item.media_type, type='text'
                            ),
                            type='document',
                        )
                    else:  # pragma: no cover
                        raise RuntimeError(f'Unsupported media type: {item.media_type}')
                elif isinstance(item, UploadedFile):
                    # Verify provider matches
                    if item.provider_name != self.system:
                        raise UserError(
                            f'UploadedFile with `provider_name={item.provider_name!r}` cannot be used with AnthropicModel. '
                            f'Expected `provider_name` to be `{self.system!r}`.'
                        )
                    if item.media_type.startswith('image/'):
                        yield BetaImageBlockParam(
                            source=BetaFileImageSourceParam(file_id=item.file_id, type='file'),
                            type='image',
                        )
                    elif item.media_type.startswith(('text/', 'application/')):
                        yield BetaRequestDocumentBlockParam(
                            source=BetaFileDocumentSourceParam(file_id=item.file_id, type='file'),
                            type='document',
                        )
                    else:
                        raise UserError(
                            f'Unsupported media type {item.media_type!r} for Anthropic file upload. '
                            'Only image and document (text/application) types are supported.'
                        )
                else:
                    raise RuntimeError(f'Unsupported content type: {type(item)}')  # pragma: no cover

    def _map_tool_definition(self, f: ToolDefinition) -> BetaToolParam:
        """Maps a `ToolDefinition` dataclass to an Anthropic `BetaToolParam` dictionary."""
        tool_param: BetaToolParam = {
            'name': f.name,
            'description': f.description or '',
            'input_schema': f.parameters_json_schema,
        }
        if f.strict and self.profile.supports_json_schema_output:
            tool_param['strict'] = f.strict
        return tool_param

    @staticmethod
    def _build_output_config(
        model_request_parameters: ModelRequestParameters, model_settings: AnthropicModelSettings
    ) -> BetaOutputConfigParam | None:
        output_format: BetaJSONOutputFormatParam | None = None
        if model_request_parameters.output_mode == 'native':
            assert model_request_parameters.output_object is not None
            output_format = {'type': 'json_schema', 'schema': model_request_parameters.output_object.json_schema}

        effort = model_settings.get('anthropic_effort')

        if output_format is None and effort is None:
            return None

        config: BetaOutputConfigParam = {}
        if output_format is not None:
            config['format'] = output_format
        if effort is not None:
            config['effort'] = effort
        return config

```

---|---
####  __init__
```
__init__(
    model_name: AnthropicModelName[](https://ai.pydantic.dev/api/models/anthropic/#pydantic_ai.models.anthropic.AnthropicModelName "AnthropicModelName



      module-attribute
   \(pydantic_ai.models.anthropic.AnthropicModelName\)"),
    *,
    provider: (
        ["anthropic", "gateway"]
        | Provider[](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.Provider "pydantic_ai.providers.Provider")[AsyncAnthropicClient]
    ) = "anthropic",
    profile: ModelProfileSpec | None = None,
    settings: ModelSettings[](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "ModelSettings \(pydantic_ai.settings.ModelSettings\)") | None = None
)

```

Initialize an Anthropic model.
Parameters:
Name | Type | Description | Default
---|---|---|---
`model_name` |  `AnthropicModelName[](https://ai.pydantic.dev/api/models/anthropic/#pydantic_ai.models.anthropic.AnthropicModelName "AnthropicModelName



      module-attribute
   \(pydantic_ai.models.anthropic.AnthropicModelName\)")` |  The name of the Anthropic model to use. List of model names available  |  _required_
`provider` |  `Provider[](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.Provider "pydantic_ai.providers.Provider")[AsyncAnthropicClient]` |  The provider to use for the Anthropic API. Can be either the string 'anthropic' or an instance of `Provider[AsyncAnthropicClient]`. Defaults to 'anthropic'. |  `'anthropic'`
`profile` |  `ModelProfileSpec | None` |  The model profile to use. Defaults to a profile picked by the provider based on the model name. The default 'anthropic' provider will use the default `..profiles.anthropic.anthropic_model_profile`. |  `None`
`settings` |  `ModelSettings[](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "ModelSettings \(pydantic_ai.settings.ModelSettings\)") | None` |  Default model settings for this model instance. |  `None`
Source code in `pydantic_ai_slim/pydantic_ai/models/anthropic.py`
```
257
258
259
260
261
262
263
264
265
266
267
268
269
270
271
272
273
274
275
276
277
278
279
280
281
282
283
```
| ```
def __init__(
    self,
    model_name: AnthropicModelName,
    *,
    provider: Literal['anthropic', 'gateway'] | Provider[AsyncAnthropicClient] = 'anthropic',
    profile: ModelProfileSpec | None = None,
    settings: ModelSettings | None = None,
):
    """Initialize an Anthropic model.

    Args:
        model_name: The name of the Anthropic model to use. List of model names available
            [here](https://docs.anthropic.com/en/docs/about-claude/models).
        provider: The provider to use for the Anthropic API. Can be either the string 'anthropic' or an
            instance of `Provider[AsyncAnthropicClient]`. Defaults to 'anthropic'.
        profile: The model profile to use. Defaults to a profile picked by the provider based on the model name.
            The default 'anthropic' provider will use the default `..profiles.anthropic.anthropic_model_profile`.
        settings: Default model settings for this model instance.
    """
    self._model_name = model_name

    if isinstance(provider, str):
        provider = infer_provider('gateway/anthropic' if provider == 'gateway' else provider)
    self._provider = provider
    self.client = provider.client

    super().__init__(settings=settings, profile=profile or provider.model_profile)

```

---|---
####  model_name `property`
```
model_name: AnthropicModelName[](https://ai.pydantic.dev/api/models/anthropic/#pydantic_ai.models.anthropic.AnthropicModelName "AnthropicModelName



      module-attribute
   \(pydantic_ai.models.anthropic.AnthropicModelName\)")

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

The set of builtin tool types this model can handle.
Source code in `pydantic_ai_slim/pydantic_ai/models/anthropic.py`
```
299
300
301
302
```
| ```
@classmethod
def supported_builtin_tools(cls) -> frozenset[type[AbstractBuiltinTool]]:
    """The set of builtin tool types this model can handle."""
    return frozenset({WebSearchTool, CodeExecutionTool, WebFetchTool, MemoryTool, MCPServerTool})

```

---|---
###  AnthropicStreamedResponse `dataclass`
Bases: `StreamedResponse[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.StreamedResponse "StreamedResponse



      dataclass
   \(pydantic_ai.models.StreamedResponse\)")`
Implementation of `StreamedResponse` for Anthropic models.
Source code in `pydantic_ai_slim/pydantic_ai/models/anthropic.py`
```
1242
1243
1244
1245
1246
1247
1248
1249
1250
1251
1252
1253
1254
1255
1256
1257
1258
1259
1260
1261
1262
1263
1264
1265
1266
1267
1268
1269
1270
1271
1272
1273
1274
1275
1276
1277
1278
1279
1280
1281
1282
1283
1284
1285
1286
1287
1288
1289
1290
1291
1292
1293
1294
1295
1296
1297
1298
1299
1300
1301
1302
1303
1304
1305
1306
1307
1308
1309
1310
1311
1312
1313
1314
1315
1316
1317
1318
1319
1320
1321
1322
1323
1324
1325
1326
1327
1328
1329
1330
1331
1332
1333
1334
1335
1336
1337
1338
1339
1340
1341
1342
1343
1344
1345
1346
1347
1348
1349
1350
1351
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
1381
1382
1383
1384
1385
1386
1387
1388
1389
1390
1391
1392
1393
1394
1395
1396
1397
1398
1399
1400
1401
1402
1403
1404
1405
1406
1407
1408
1409
1410
1411
1412
1413
```
| ```
@dataclass
class AnthropicStreamedResponse(StreamedResponse):
    """Implementation of `StreamedResponse` for Anthropic models."""

    _model_name: AnthropicModelName
    _response: AsyncIterable[BetaRawMessageStreamEvent]
    _provider_name: str
    _provider_url: str
    _timestamp: datetime = field(default_factory=_utils.now_utc)

    async def _get_event_iterator(self) -> AsyncIterator[ModelResponseStreamEvent]:  # noqa: C901
        current_block: BetaContentBlock | None = None

        builtin_tool_calls: dict[str, BuiltinToolCallPart] = {}
        async for event in self._response:
            if isinstance(event, BetaRawMessageStartEvent):
                self._usage = _map_usage(event, self._provider_name, self._provider_url, self._model_name)
                self.provider_response_id = event.message.id
                if event.message.container:
                    self.provider_details = self.provider_details or {}
                    self.provider_details['container_id'] = event.message.container.id

            elif isinstance(event, BetaRawContentBlockStartEvent):
                current_block = event.content_block
                if isinstance(current_block, BetaTextBlock) and current_block.text:
                    for event_ in self._parts_manager.handle_text_delta(
                        vendor_part_id=event.index, content=current_block.text
                    ):
                        yield event_
                elif isinstance(current_block, BetaThinkingBlock):
                    for event_ in self._parts_manager.handle_thinking_delta(
                        vendor_part_id=event.index,
                        content=current_block.thinking,
                        signature=current_block.signature,
                        provider_name=self.provider_name,
                    ):
                        yield event_
                elif isinstance(current_block, BetaRedactedThinkingBlock):
                    for event_ in self._parts_manager.handle_thinking_delta(
                        vendor_part_id=event.index,
                        id='redacted_thinking',
                        signature=current_block.data,
                        provider_name=self.provider_name,
                    ):
                        yield event_
                elif isinstance(current_block, BetaToolUseBlock):
                    maybe_event = self._parts_manager.handle_tool_call_delta(
                        vendor_part_id=event.index,
                        tool_name=current_block.name,
                        args=cast(dict[str, Any], current_block.input) or None,
                        tool_call_id=current_block.id,
                    )
                    if maybe_event is not None:  # pragma: no branch
                        yield maybe_event
                elif isinstance(current_block, BetaServerToolUseBlock):
                    call_part = _map_server_tool_use_block(current_block, self.provider_name)
                    builtin_tool_calls[call_part.tool_call_id] = call_part
                    yield self._parts_manager.handle_part(
                        vendor_part_id=event.index,
                        part=call_part,
                    )
                elif isinstance(current_block, BetaWebSearchToolResultBlock):
                    yield self._parts_manager.handle_part(
                        vendor_part_id=event.index,
                        part=_map_web_search_tool_result_block(current_block, self.provider_name),
                    )
                elif isinstance(current_block, BetaCodeExecutionToolResultBlock):
                    yield self._parts_manager.handle_part(
                        vendor_part_id=event.index,
                        part=_map_code_execution_tool_result_block(current_block, self.provider_name),
                    )
                elif isinstance(current_block, BetaWebFetchToolResultBlock):  # pragma: lax no cover
                    yield self._parts_manager.handle_part(
                        vendor_part_id=event.index,
                        part=_map_web_fetch_tool_result_block(current_block, self.provider_name),
                    )
                elif isinstance(current_block, BetaMCPToolUseBlock):
                    call_part = _map_mcp_server_use_block(current_block, self.provider_name)
                    builtin_tool_calls[call_part.tool_call_id] = call_part

                    args_json = call_part.args_as_json_str()
                    # Drop the final `{}}` so that we can add tool args deltas
                    args_json_delta = args_json[:-3]
                    assert args_json_delta.endswith('"tool_args":'), (
                        f'Expected {args_json_delta!r} to end in `"tool_args":`'
                    )

                    yield self._parts_manager.handle_part(
                        vendor_part_id=event.index, part=replace(call_part, args=None)
                    )
                    maybe_event = self._parts_manager.handle_tool_call_delta(
                        vendor_part_id=event.index,
                        args=args_json_delta,
                    )
                    if maybe_event is not None:  # pragma: no branch
                        yield maybe_event
                elif isinstance(current_block, BetaMCPToolResultBlock):
                    call_part = builtin_tool_calls.get(current_block.tool_use_id)
                    yield self._parts_manager.handle_part(
                        vendor_part_id=event.index,
                        part=_map_mcp_server_result_block(current_block, call_part, self.provider_name),
                    )

            elif isinstance(event, BetaRawContentBlockDeltaEvent):
                if isinstance(event.delta, BetaTextDelta):
                    for event_ in self._parts_manager.handle_text_delta(
                        vendor_part_id=event.index, content=event.delta.text
                    ):
                        yield event_
                elif isinstance(event.delta, BetaThinkingDelta):
                    for event_ in self._parts_manager.handle_thinking_delta(
                        vendor_part_id=event.index,
                        content=event.delta.thinking,
                        provider_name=self.provider_name,
                    ):
                        yield event_
                elif isinstance(event.delta, BetaSignatureDelta):
                    for event_ in self._parts_manager.handle_thinking_delta(
                        vendor_part_id=event.index,
                        signature=event.delta.signature,
                        provider_name=self.provider_name,
                    ):
                        yield event_
                elif isinstance(event.delta, BetaInputJSONDelta):
                    maybe_event = self._parts_manager.handle_tool_call_delta(
                        vendor_part_id=event.index,
                        args=event.delta.partial_json,
                    )
                    if maybe_event is not None:  # pragma: no branch
                        yield maybe_event
                # TODO(Marcelo): We need to handle citations.
                elif isinstance(event.delta, BetaCitationsDelta):
                    pass

            elif isinstance(event, BetaRawMessageDeltaEvent):
                self._usage = _map_usage(event, self._provider_name, self._provider_url, self._model_name, self._usage)
