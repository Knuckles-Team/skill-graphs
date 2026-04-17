    """
    self._model_name = model_name

    if isinstance(provider, str):
        provider = infer_provider('gateway/bedrock' if provider == 'gateway' else provider)
    self._provider = provider
    self.client = cast('BedrockRuntimeClient', provider.client)

    super().__init__(settings=settings, profile=profile or provider.model_profile)

```

---|---
####  model_name `property`
```
model_name:

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
Source code in `pydantic_ai_slim/pydantic_ai/models/bedrock.py`
```
386
387
388
389
```
| ```
@classmethod
def supported_builtin_tools(cls) -> frozenset[type[AbstractBuiltinTool]]:
    """The set of builtin tool types this model can handle."""
    return frozenset({CodeExecutionTool})

```

---|---
####  count_tokens `async`
```
count_tokens(
    messages: [ModelMessage[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelMessage "ModelMessage



      module-attribute
   \(pydantic_ai.ModelMessage\)")],
    model_settings: ModelSettings[](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "ModelSettings \(pydantic_ai.settings.ModelSettings\)") | None,
    model_request_parameters: ModelRequestParameters[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.ModelRequestParameters "ModelRequestParameters



      dataclass
   \(pydantic_ai.models.ModelRequestParameters\)"),
) -> RequestUsage[](https://ai.pydantic.dev/api/usage/#pydantic_ai.usage.RequestUsage "RequestUsage



      dataclass
   \(pydantic_ai.usage.RequestUsage\)")

```

Count the number of tokens, works with limited models.
Check the actual supported models on
Source code in `pydantic_ai_slim/pydantic_ai/models/bedrock.py`
```
418
419
420
421
422
423
424
425
426
427
428
429
430
431
432
433
434
435
436
437
438
439
440
441
442
443
444
445
446
447
```
| ```
async def count_tokens(
    self,
    messages: list[ModelMessage],
    model_settings: ModelSettings | None,
    model_request_parameters: ModelRequestParameters,
) -> usage.RequestUsage:
    """Count the number of tokens, works with limited models.

    Check the actual supported models on <https://docs.aws.amazon.com/bedrock/latest/userguide/count-tokens.html>
    """
    model_settings, model_request_parameters = self.prepare_request(model_settings, model_request_parameters)
    settings = cast(BedrockModelSettings, model_settings or {})
    system_prompt, bedrock_messages = await self._map_messages(messages, model_request_parameters, settings)
    params: CountTokensRequestTypeDef = {
        'modelId': remove_bedrock_geo_prefix(self.model_name),
        'input': {
            'converse': {
                'messages': bedrock_messages,
                'system': system_prompt,
            },
        },
    }
    try:
        response = await anyio.to_thread.run_sync(functools.partial(self.client.count_tokens, **params))
    except ClientError as e:
        status_code = e.response.get('ResponseMetadata', {}).get('HTTPStatusCode')
        if isinstance(status_code, int):
            raise ModelHTTPError(status_code=status_code, model_name=self.model_name, body=e.response) from e
        raise ModelAPIError(model_name=self.model_name, message=str(e)) from e
    return usage.RequestUsage(input_tokens=response['inputTokens'])

```

---|---
###  BedrockStreamedResponse `dataclass`
Bases: `StreamedResponse[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.StreamedResponse "StreamedResponse



      dataclass
   \(pydantic_ai.models.StreamedResponse\)")`
Implementation of `StreamedResponse` for Bedrock models.
Source code in `pydantic_ai_slim/pydantic_ai/models/bedrock.py`
```
1027
1028
1029
1030
1031
1032
1033
1034
1035
1036
1037
1038
1039
1040
1041
1042
1043
1044
1045
1046
1047
1048
1049
1050
1051
1052
1053
1054
1055
1056
1057
1058
1059
1060
1061
1062
1063
1064
1065
1066
1067
1068
1069
1070
1071
1072
1073
1074
1075
1076
1077
1078
1079
1080
1081
1082
1083
1084
1085
1086
1087
1088
1089
1090
1091
1092
1093
1094
1095
1096
1097
1098
1099
1100
1101
1102
1103
1104
1105
1106
1107
1108
1109
1110
1111
1112
1113
1114
1115
1116
1117
1118
1119
1120
1121
1122
1123
1124
1125
1126
1127
1128
1129
1130
1131
1132
1133
1134
1135
1136
1137
1138
1139
1140
1141
1142
1143
1144
1145
1146
1147
1148
1149
1150
1151
1152
1153
1154
1155
1156
1157
1158
1159
1160
1161
1162
1163
1164
1165
1166
1167
1168
1169
1170
1171
1172
1173
1174
1175
1176
1177
1178
1179
1180
1181
1182
1183
1184
1185
1186
1187
1188
1189
1190
1191
1192
```
| ```
@dataclass
class BedrockStreamedResponse(StreamedResponse):
    """Implementation of `StreamedResponse` for Bedrock models."""

    _model_name: BedrockModelName
    _event_stream: EventStream[ConverseStreamOutputTypeDef]
    _provider_name: str
    _provider_url: str
    _timestamp: datetime = field(default_factory=_utils.now_utc)
    _provider_response_id: str | None = None

    async def _get_event_iterator(self) -> AsyncIterator[ModelResponseStreamEvent]:  # noqa: C901
        """Return an async iterator of [`ModelResponseStreamEvent`][pydantic_ai.messages.ModelResponseStreamEvent]s.

        This method should be implemented by subclasses to translate the vendor-specific stream of events into
        pydantic_ai-format events.
        """
        if self._provider_response_id is not None:  # pragma: no cover
            self.provider_response_id = self._provider_response_id

        chunk: ConverseStreamOutputTypeDef
        tool_ids: dict[int, str] = {}

        # Bedrock has deltas for built-in tool returns, which aren't supported by parts manager.
        # We accumulate the deltas here and yield the complete return part once the content block ends
        builtin_tool_returns: dict[int, BuiltinToolReturnPart] = {}

        async for chunk in _AsyncIteratorWrapper(self._event_stream):
            match chunk:
                case {'messageStart': _}:
                    continue
                case {'messageStop': message_stop}:
                    raw_finish_reason = message_stop['stopReason']
                    self.provider_details = {'finish_reason': raw_finish_reason}
                    self.finish_reason = _FINISH_REASON_MAP.get(raw_finish_reason)
                case {'metadata': metadata}:
                    if 'usage' in metadata:  # pragma: no branch
                        self._usage += self._map_usage(metadata)
                case {'contentBlockStart': content_block_start}:
                    index = content_block_start['contentBlockIndex']
                    start = content_block_start['start']
                    if 'toolUse' in start:
                        tool_use_start = start['toolUse']
                        tool_id = tool_use_start['toolUseId']
                        tool_ids[index] = tool_id
                        tool_name = tool_use_start['name']
                        if tool_use_start.get('type') == 'server_tool_use':
                            if tool_name == 'nova_code_interpreter':  # pragma: no branch
                                part = BuiltinToolCallPart(
                                    tool_name=CodeExecutionTool.kind,
                                    tool_call_id=tool_id,
                                    provider_name=self.provider_name,
                                )
                                yield self._parts_manager.handle_part(vendor_part_id=index, part=part)
                        elif maybe_event := self._parts_manager.handle_tool_call_delta(
                            vendor_part_id=index,
                            tool_name=tool_name,
                            args=None,
                            tool_call_id=tool_id,
                        ):  # pragma: no branch
                            yield maybe_event
                    elif 'toolResult' in start:  # pragma: no branch
                        tool_result_start = start['toolResult']
                        tool_id = tool_result_start['toolUseId']

                        if tool_result_start.get('type') == 'nova_code_interpreter_result':  # pragma: no branch
                            return_part = BuiltinToolReturnPart(
                                provider_name=self.provider_name,
                                tool_name=CodeExecutionTool.kind,
                                content=None,
                                tool_call_id=tool_id,
                                provider_details={'status': tool_result_start['status']}
                                if 'status' in tool_result_start
                                else {},
                            )
                            builtin_tool_returns[index] = return_part
                            # Don't yield anything yet - we wait for content block end

                case {'contentBlockDelta': content_block_delta}:
                    index = content_block_delta['contentBlockIndex']
                    delta = content_block_delta['delta']
                    if 'reasoningContent' in delta:
                        if redacted_content := delta['reasoningContent'].get('redactedContent'):
                            for event in self._parts_manager.handle_thinking_delta(
                                vendor_part_id=index,
                                id='redacted_content',
                                signature=redacted_content.decode('utf-8'),
                                provider_name=self.provider_name,
                            ):
                                yield event
                        else:
                            signature = delta['reasoningContent'].get('signature')
                            for event in self._parts_manager.handle_thinking_delta(
                                vendor_part_id=index,
                                content=delta['reasoningContent'].get('text'),
                                signature=signature,
                                provider_name=self.provider_name if signature else None,
                            ):
                                yield event
                    if text := delta.get('text'):
                        for event in self._parts_manager.handle_text_delta(vendor_part_id=index, content=text):
                            yield event
                    if 'toolUse' in delta:
                        tool_use = delta['toolUse']
                        maybe_event = self._parts_manager.handle_tool_call_delta(
                            vendor_part_id=index,
                            tool_name=tool_use.get('name'),
                            args=tool_use.get('input'),
                            tool_call_id=tool_ids[index],
                        )
                        if maybe_event:  # pragma: no branch
                            yield maybe_event
                    if 'toolResult' in delta:  # pragma: no branch
                        if (
                            return_part := builtin_tool_returns.get(index)
                        ) and return_part.tool_name == CodeExecutionTool.kind:  # pragma: no branch
                            # For now, only process `contentBlockDelta.toolResult` for Code Exe tool.

                            if tr_content := delta['toolResult']:  # pragma: no branch
                                # Goal here is to convert to object form.
                                # This assumes the first item is the relevant one.
                                return_part.content = tr_content[0].get('json')

                            # Don't yield anything yet - we wait for content block end

                case {'contentBlockStop': content_block_stop}:
                    index = content_block_stop['contentBlockIndex']
                    if return_part := builtin_tool_returns.get(index):
                        # Emit the complete built-in tool return only once when the block closes.
                        yield self._parts_manager.handle_part(vendor_part_id=index, part=return_part)
                    tool_ids.pop(index, None)
                    builtin_tool_returns.pop(index, None)

                case _:  # pragma: no cover
                    pass  # pyright wants match statements to be exhaustive

    @property
    def model_name(self) -> str:
        """Get the model name of the response."""
        return self._model_name

    @property
    def provider_name(self) -> str:
        """Get the provider name."""
        return self._provider_name

    @property
    def provider_url(self) -> str:
        """Get the provider base URL."""
        return self._provider_url

    @property
    def timestamp(self) -> datetime:
        return self._timestamp

    def _map_usage(self, metadata: ConverseStreamMetadataEventTypeDef) -> usage.RequestUsage:
        input_tokens = metadata['usage']['inputTokens']
        output_tokens = metadata['usage']['outputTokens']
        cache_read_tokens = metadata['usage'].get('cacheReadInputTokens', 0)
        cache_write_tokens = metadata['usage'].get('cacheWriteInputTokens', 0)
        return usage.RequestUsage(
            input_tokens=input_tokens + cache_write_tokens + cache_read_tokens,
            output_tokens=output_tokens,
            cache_read_tokens=cache_read_tokens,
            cache_write_tokens=cache_write_tokens,
        )

```

---|---
####  model_name `property`
```
model_name:

```

Get the model name of the response.
####  provider_name `property`
```
provider_name:

```

Get the provider name.
####  provider_url `property`
```
provider_url:

```

Get the provider base URL.
© Pydantic Services Inc. 2024 to present
