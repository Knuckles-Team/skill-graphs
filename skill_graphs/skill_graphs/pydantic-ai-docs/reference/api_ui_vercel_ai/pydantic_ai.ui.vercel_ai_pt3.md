                            provider_name=provider_meta.get('provider_name'),
                            provider_details=provider_meta.get('provider_details'),
                        )
                    )
                elif isinstance(part, ToolUIPart | DynamicToolUIPart):
                    if isinstance(part, DynamicToolUIPart):
                        tool_name = part.tool_name
                        builtin_tool = False
                    else:
                        tool_name = part.type.removeprefix('tool-')
                        builtin_tool = part.provider_executed

                    tool_call_id = part.tool_call_id

                    args: str | dict[str, Any] | None = part.input

                    if isinstance(args, str):
                        try:
                            parsed = json.loads(args)
                            if isinstance(parsed, dict):
                                args = cast(dict[str, Any], parsed)
                        except json.JSONDecodeError:
                            pass
                    elif isinstance(args, dict) or args is None:
                        pass
                    else:
                        assert_never(args)

                    provider_meta = load_provider_metadata(part.call_provider_metadata)
                    part_id = provider_meta.get('id')
                    provider_name = provider_meta.get('provider_name')
                    provider_details = provider_meta.get('provider_details')

                    if builtin_tool:
                        # For builtin tools, we need to create 2 parts (BuiltinToolCall & BuiltinToolReturn) for a single Vercel ToolOutput
                        # The call and return metadata are combined in the output part.
                        # So we extract and return them to the respective parts
                        call_meta = return_meta = {}
                        has_tool_output = isinstance(
                            part, (ToolOutputAvailablePart, ToolOutputErrorPart, ToolOutputDeniedPart)
                        )

                        if has_tool_output:
                            call_meta, return_meta = cls._load_builtin_tool_meta(provider_meta)

                        builder.add(
                            BuiltinToolCallPart(
                                tool_name=tool_name,
                                tool_call_id=tool_call_id,
                                args=args,
                                id=call_meta.get('id') or part_id,
                                provider_name=call_meta.get('provider_name') or provider_name,
                                provider_details=call_meta.get('provider_details') or provider_details,
                            )
                        )

                        if has_tool_output:
                            if isinstance(part, ToolOutputErrorPart):
                                output: Any = part.error_text
                                outcome: Literal['success', 'failed', 'denied'] = 'failed'
                            elif isinstance(part, ToolOutputDeniedPart):
                                output = _denial_reason(part)
                                outcome = 'denied'
                            else:
                                output = part.output if isinstance(part, ToolOutputAvailablePart) else None
                                outcome = 'success'
                            builder.add(
                                BuiltinToolReturnPart(
                                    tool_name=tool_name,
                                    tool_call_id=tool_call_id,
                                    content=output,
                                    provider_name=return_meta.get('provider_name') or provider_name,
                                    provider_details=return_meta.get('provider_details') or provider_details,
                                    outcome=outcome,
                                )
                            )
                    else:
                        builder.add(
                            ToolCallPart(
                                tool_name=tool_name,
                                tool_call_id=tool_call_id,
                                args=args,
                                id=part_id,
                                provider_name=provider_name,
                                provider_details=provider_details,
                            )
                        )

                        if part.state == 'output-available':
                            builder.add(
                                ToolReturnPart(tool_name=tool_name, tool_call_id=tool_call_id, content=part.output)
                            )
                        elif part.state == 'output-error':
                            builder.add(
                                ToolReturnPart(
                                    tool_name=tool_name,
                                    tool_call_id=tool_call_id,
                                    content=part.error_text,
                                    outcome='failed',
                                )
                            )
                        elif part.state == 'output-denied':
                            builder.add(
                                ToolReturnPart(
                                    tool_name=tool_name,
                                    tool_call_id=tool_call_id,
                                    content=_denial_reason(part),
                                    outcome='denied',
                                )
                            )
                elif isinstance(part, DataUIPart):  # pragma: no cover
                    # Contains custom data that shouldn't be sent to the model
                    pass
                elif isinstance(part, SourceUrlUIPart):  # pragma: no cover
                    # TODO: Once we support citations: https://github.com/pydantic/pydantic-ai/issues/3126
                    pass
                elif isinstance(part, SourceDocumentUIPart):  # pragma: no cover
                    # TODO: Once we support citations: https://github.com/pydantic/pydantic-ai/issues/3126
                    pass
                elif isinstance(part, StepStartUIPart):  # pragma: no cover
                    # Nothing to do here
                    pass
                else:
                    assert_never(part)
        else:
            assert_never(msg.role)

    return builder.messages

```

---|---
####  dump_messages `classmethod`
```
dump_messages(
    messages: [ModelMessage[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelMessage "ModelMessage



      module-attribute
   \(pydantic_ai.messages.ModelMessage\)")],
    *,
    generate_message_id: (
        [
            [
                ModelRequest[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelRequest "ModelRequest



      dataclass
   \(pydantic_ai.messages.ModelRequest\)") | ModelResponse[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse "ModelResponse



      dataclass
   \(pydantic_ai.messages.ModelResponse\)"),
                ["system", "user", "assistant"],
                ,
            ],
            ,
        ]
        | None
    ) = None
) -> [UIMessage[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.request_types.UIMessage "UIMessage \(pydantic_ai.ui.vercel_ai.request_types.UIMessage\)")]

```

Transform Pydantic AI messages into Vercel AI messages.
Parameters:
Name | Type | Description | Default
---|---|---|---
`messages` |  `ModelMessage[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelMessage "ModelMessage



      module-attribute
   \(pydantic_ai.messages.ModelMessage\)")]` |  A sequence of ModelMessage objects to convert |  _required_
`generate_message_id` |  `ModelRequest[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelRequest "ModelRequest



      dataclass
   \(pydantic_ai.messages.ModelRequest\)") | ModelResponse[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse "ModelResponse



      dataclass
   \(pydantic_ai.messages.ModelResponse\)"), ` |  Optional custom function to generate message IDs. If provided, it receives the message, the role ('system', 'user', or 'assistant'), and the message index (incremented per UIMessage appended), and should return a unique string ID. If not provided, uses `provider_response_id` for responses, run_id-based IDs for messages with run_id, or a deterministic UUID5 fallback. |  `None`
Returns:
Type | Description
---|---
`UIMessage[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.request_types.UIMessage "UIMessage \(pydantic_ai.ui.vercel_ai.request_types.UIMessage\)")]` |  A list of UIMessage objects in Vercel AI format
Source code in `pydantic_ai_slim/pydantic_ai/ui/vercel_ai/_adapter.py`
```
684
685
686
687
688
689
690
691
692
693
694
695
696
697
698
699
700
701
702
703
704
705
706
707
708
709
710
711
712
713
714
715
716
717
718
719
720
721
722
723
724
725
726
727
728
729
730
731
732
733
734
735
736
737
738
739
740
741
742
743
744
745
746
```
| ```
@classmethod
def dump_messages(
    cls,
    messages: Sequence[ModelMessage],
    *,
    generate_message_id: Callable[[ModelRequest | ModelResponse, Literal['system', 'user', 'assistant'], int], str]
    | None = None,
) -> list[UIMessage]:
    """Transform Pydantic AI messages into Vercel AI messages.

    Args:
        messages: A sequence of ModelMessage objects to convert
        generate_message_id: Optional custom function to generate message IDs. If provided,
            it receives the message, the role ('system', 'user', or 'assistant'), and the
            message index (incremented per UIMessage appended), and should return a unique
            string ID. If not provided, uses `provider_response_id` for responses,
            run_id-based IDs for messages with run_id, or a deterministic UUID5 fallback.

    Returns:
        A list of UIMessage objects in Vercel AI format
    """
    tool_results: dict[str, ToolReturnPart | RetryPromptPart] = {}

    for msg in messages:
        if isinstance(msg, ModelRequest):
            for part in msg.parts:
                if isinstance(part, ToolReturnPart):
                    tool_results[part.tool_call_id] = part
                elif isinstance(part, RetryPromptPart) and part.tool_name:
                    tool_results[part.tool_call_id] = part

    id_generator = generate_message_id or _generate_message_id
    result: list[UIMessage] = []
    message_index = 0

    for msg in messages:
        if isinstance(msg, ModelRequest):
            system_ui_parts, user_ui_parts = cls._dump_request_message(msg)
            if system_ui_parts:
                result.append(
                    UIMessage(id=id_generator(msg, 'system', message_index), role='system', parts=system_ui_parts)
                )
                message_index += 1

            if user_ui_parts:
                result.append(
                    UIMessage(id=id_generator(msg, 'user', message_index), role='user', parts=user_ui_parts)
                )
                message_index += 1

        elif isinstance(  # pragma: no branch
            msg, ModelResponse
        ):
            ui_parts: list[UIMessagePart] = cls._dump_response_message(msg, tool_results)
            if ui_parts:  # pragma: no branch
                result.append(
                    UIMessage(id=id_generator(msg, 'assistant', message_index), role='assistant', parts=ui_parts)
                )
                message_index += 1
        else:
            assert_never(msg)

    return result

```

---|---
###  VercelAIEventStream `dataclass`
Bases: `UIEventStream[](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.UIEventStream "UIEventStream



      dataclass
   \(pydantic_ai.ui.UIEventStream\)")[RequestData[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.request_types.RequestData "RequestData



      module-attribute
   \(pydantic_ai.ui.vercel_ai.request_types.RequestData\)"), BaseChunk[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.response_types.BaseChunk "BaseChunk \(pydantic_ai.ui.vercel_ai.response_types.BaseChunk\)"), AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)"), OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")]`
UI event stream transformer for the Vercel AI protocol.
Source code in `pydantic_ai_slim/pydantic_ai/ui/vercel_ai/_event_stream.py`
```
 78
 79
 80
 81
 82
 83
 84
 85
 86
 87
 88
 89
 90
 91
 92
 93
 94
 95
 96
 97
 98
 99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
208
209
210
211
212
213
214
215
216
217
218
219
220
221
222
223
224
225
226
227
228
229
230
231
232
233
234
235
236
237
238
239
240
241
242
243
244
245
246
247
248
249
250
251
252
253
254
255
256
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
284
285
286
```
| ```
@dataclass
class VercelAIEventStream(UIEventStream[RequestData, BaseChunk, AgentDepsT, OutputDataT]):
    """UI event stream transformer for the Vercel AI protocol."""

    _: KW_ONLY
    sdk_version: Literal[5, 6] = 5
    """Vercel AI SDK version to target. Setting to 6 enables tool approval streaming."""

    _step_started: bool = False
    _finish_reason: FinishReason = None

    @property
    def response_headers(self) -> Mapping[str, str] | None:
        return VERCEL_AI_DSP_HEADERS

    def encode_event(self, event: BaseChunk) -> str:
        return f'data: {event.encode(self.sdk_version)}\n\n'

    async def before_stream(self) -> AsyncIterator[BaseChunk]:
        yield StartChunk()

    async def before_response(self) -> AsyncIterator[BaseChunk]:
        if self._step_started:
            yield FinishStepChunk()

        self._step_started = True
        yield StartStepChunk()

    async def after_stream(self) -> AsyncIterator[BaseChunk]:
        yield FinishStepChunk()

        yield FinishChunk(finish_reason=self._finish_reason)
        yield DoneChunk()

    async def handle_run_result(self, event: AgentRunResultEvent) -> AsyncIterator[BaseChunk]:
        pydantic_reason = event.result.response.finish_reason
        if pydantic_reason:
            self._finish_reason = _FINISH_REASON_MAP.get(pydantic_reason, 'other')

        # Emit tool approval requests for deferred approvals (only when sdk_version >= 6)
        output = event.result.output
        if self.sdk_version >= 6 and isinstance(output, DeferredToolRequests):
            for tool_call in output.approvals:
                yield ToolApprovalRequestChunk(
                    approval_id=str(uuid4()),
                    tool_call_id=tool_call.tool_call_id,
                )
            return
        return
        yield

    async def on_error(self, error: Exception) -> AsyncIterator[BaseChunk]:
        self._finish_reason = 'error'
        yield ErrorChunk(error_text=str(error))

    async def handle_text_start(self, part: TextPart, follows_text: bool = False) -> AsyncIterator[BaseChunk]:
        provider_metadata = dump_provider_metadata(
            id=part.id, provider_name=part.provider_name, provider_details=part.provider_details
        )
        if follows_text:
            message_id = self.message_id
        else:
            message_id = self.new_message_id()
            yield TextStartChunk(id=message_id, provider_metadata=provider_metadata)

        if part.content:
            yield TextDeltaChunk(id=message_id, delta=part.content, provider_metadata=provider_metadata)

    async def handle_text_delta(self, delta: TextPartDelta) -> AsyncIterator[BaseChunk]:
        if delta.content_delta:  # pragma: no branch
            provider_metadata = dump_provider_metadata(
                provider_name=delta.provider_name, provider_details=delta.provider_details
            )
            yield TextDeltaChunk(id=self.message_id, delta=delta.content_delta, provider_metadata=provider_metadata)

    async def handle_text_end(self, part: TextPart, followed_by_text: bool = False) -> AsyncIterator[BaseChunk]:
        if not followed_by_text:
            provider_metadata = dump_provider_metadata(
                id=part.id, provider_name=part.provider_name, provider_details=part.provider_details
            )
            yield TextEndChunk(id=self.message_id, provider_metadata=provider_metadata)

    async def handle_thinking_start(
        self, part: ThinkingPart, follows_thinking: bool = False
    ) -> AsyncIterator[BaseChunk]:
        message_id = self.new_message_id()
        provider_metadata = dump_provider_metadata(
            id=part.id,
            signature=part.signature,
            provider_name=part.provider_name,
            provider_details=part.provider_details,
        )
        yield ReasoningStartChunk(id=message_id, provider_metadata=provider_metadata)
        if part.content:
            yield ReasoningDeltaChunk(id=message_id, delta=part.content, provider_metadata=provider_metadata)

    async def handle_thinking_delta(self, delta: ThinkingPartDelta) -> AsyncIterator[BaseChunk]:
        if delta.content_delta:  # pragma: no branch
            provider_metadata = dump_provider_metadata(
                provider_name=delta.provider_name,
                signature=delta.signature_delta,
                provider_details=delta.provider_details,
            )
            yield ReasoningDeltaChunk(
                id=self.message_id, delta=delta.content_delta, provider_metadata=provider_metadata
            )

    async def handle_thinking_end(
        self, part: ThinkingPart, followed_by_thinking: bool = False
    ) -> AsyncIterator[BaseChunk]:
        provider_metadata = dump_provider_metadata(
            id=part.id,
            signature=part.signature,
            provider_name=part.provider_name,
            provider_details=part.provider_details,
        )
        yield ReasoningEndChunk(id=self.message_id, provider_metadata=provider_metadata)

    def handle_tool_call_start(self, part: ToolCallPart | BuiltinToolCallPart) -> AsyncIterator[BaseChunk]:
        return self._handle_tool_call_start(part)

    def handle_builtin_tool_call_start(self, part: BuiltinToolCallPart) -> AsyncIterator[BaseChunk]:
        return self._handle_tool_call_start(part, provider_executed=True)

    async def _handle_tool_call_start(
        self,
        part: ToolCallPart | BuiltinToolCallPart,
        tool_call_id: str | None = None,
        provider_executed: bool | None = None,
    ) -> AsyncIterator[BaseChunk]:
        tool_call_id = tool_call_id or part.tool_call_id
        yield ToolInputStartChunk(
            tool_call_id=tool_call_id,
            tool_name=part.tool_name,
            provider_executed=provider_executed,
            provider_metadata=dump_provider_metadata(
                id=part.id, provider_name=part.provider_name, provider_details=part.provider_details
            ),
        )
        if part.args:
            yield ToolInputDeltaChunk(tool_call_id=tool_call_id, input_text_delta=part.args_as_json_str())

    async def handle_tool_call_delta(self, delta: ToolCallPartDelta) -> AsyncIterator[BaseChunk]:
        tool_call_id = delta.tool_call_id or ''
        assert tool_call_id, '`ToolCallPartDelta.tool_call_id` must be set'
        yield ToolInputDeltaChunk(
            tool_call_id=tool_call_id,
            input_text_delta=delta.args_delta if isinstance(delta.args_delta, str) else _json_dumps(delta.args_delta),
        )

    async def handle_tool_call_end(self, part: ToolCallPart) -> AsyncIterator[BaseChunk]:
        yield ToolInputAvailableChunk(
            tool_call_id=part.tool_call_id,
            tool_name=part.tool_name,
            input=part.args_as_dict(),
            provider_metadata=dump_provider_metadata(
                id=part.id, provider_name=part.provider_name, provider_details=part.provider_details
            ),
        )

    async def handle_builtin_tool_call_end(self, part: BuiltinToolCallPart) -> AsyncIterator[BaseChunk]:
        yield ToolInputAvailableChunk(
            tool_call_id=part.tool_call_id,
            tool_name=part.tool_name,
            input=part.args_as_dict(),
            provider_executed=True,
            provider_metadata=dump_provider_metadata(
                id=part.id, provider_name=part.provider_name, provider_details=part.provider_details
            ),
        )

    async def handle_builtin_tool_return(self, part: BuiltinToolReturnPart) -> AsyncIterator[BaseChunk]:
        if self.sdk_version >= 6 and part.outcome == 'denied':
            yield ToolOutputDeniedChunk(tool_call_id=part.tool_call_id)
        elif part.outcome == 'failed':
            yield ToolOutputErrorChunk(tool_call_id=part.tool_call_id, error_text=part.model_response_str())
        else:
            yield ToolOutputAvailableChunk(
                tool_call_id=part.tool_call_id,
                output=tool_return_output(part),
                provider_executed=True,
            )

    async def handle_file(self, part: FilePart) -> AsyncIterator[BaseChunk]:
        file = part.content
        yield FileChunk(url=file.data_uri, media_type=file.media_type)

    async def handle_function_tool_result(self, event: FunctionToolResultEvent) -> AsyncIterator[BaseChunk]:
        part = event.result
        tool_call_id = part.tool_call_id

        if self.sdk_version >= 6 and isinstance(part, ToolReturnPart) and part.outcome == 'denied':
            yield ToolOutputDeniedChunk(tool_call_id=tool_call_id)
        elif isinstance(part, RetryPromptPart):
            yield ToolOutputErrorChunk(tool_call_id=tool_call_id, error_text=part.model_response())
        elif isinstance(part, ToolReturnPart) and part.outcome == 'failed':
            yield ToolOutputErrorChunk(tool_call_id=tool_call_id, error_text=part.model_response_str())
        else:
            yield ToolOutputAvailableChunk(tool_call_id=tool_call_id, output=tool_return_output(part))

        # ToolOutputAvailableChunk/ToolOutputErrorChunk.output may hold user parts
        # (e.g. text, images) that Vercel AI does not currently have chunk types for.

        # Check for data-carrying Vercel AI chunks returned by tool calls via metadata.
        # Only data-carrying chunks (DataChunk, SourceUrlChunk, etc.) are yielded;
        # protocol-control chunks are filtered out by iter_metadata_chunks.
        if isinstance(part, ToolReturnPart):
            for chunk in iter_metadata_chunks(part):
                yield chunk

```

---|---
####  sdk_version `class-attribute` `instance-attribute`
```
sdk_version: [5, 6] = 5

```

Vercel AI SDK version to target. Setting to 6 enables tool approval streaming.
Vercel AI request types (UI messages).
Converted to Python from: https://github.com/vercel/ai/blob/ai%406.0.57/packages/ai/src/ui/ui-messages.ts
Tool approval types (`ToolApprovalRequested`, `ToolApprovalResponded`) require AI SDK v6 or later.
###  ProviderMetadata `module-attribute`
```
ProviderMetadata = [, [, JSONValue]]

```

Provider metadata.
###  BaseUIPart
Bases: `CamelBaseModel`,
Abstract base class for all UI parts.
Source code in `pydantic_ai_slim/pydantic_ai/ui/vercel_ai/request_types.py`
```
22
23
```
| ```
class BaseUIPart(CamelBaseModel, ABC):
    """Abstract base class for all UI parts."""

```

---|---
###  TextUIPart
Bases: `BaseUIPart[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.request_types.BaseUIPart "BaseUIPart \(pydantic_ai.ui.vercel_ai.request_types.BaseUIPart\)")`
A text part of a message.
Source code in `pydantic_ai_slim/pydantic_ai/ui/vercel_ai/request_types.py`
```
26
27
28
29
30
31
32
33
34
35
36
37
38
```
| ```
class TextUIPart(BaseUIPart):
    """A text part of a message."""

    type: Literal['text'] = 'text'

    text: str
    """The text content."""

    state: Literal['streaming', 'done'] | None = None
    """The state of the text part."""

    provider_metadata: ProviderMetadata | None = None
    """The provider metadata."""

```

---|---
####  text `instance-attribute`
```
text:

```

The text content.
####  state `class-attribute` `instance-attribute`
```
state: ['streaming', 'done'] | None = None

```

The state of the text part.
####  provider_metadata `class-attribute` `instance-attribute`
```
provider_metadata: ProviderMetadata[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.request_types.ProviderMetadata "ProviderMetadata



      module-attribute
   \(pydantic_ai.ui.vercel_ai.request_types.ProviderMetadata\)") | None = None

```

The provider metadata.
###  ReasoningUIPart
Bases: `BaseUIPart[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.request_types.BaseUIPart "BaseUIPart \(pydantic_ai.ui.vercel_ai.request_types.BaseUIPart\)")`
A reasoning part of a message.
Source code in `pydantic_ai_slim/pydantic_ai/ui/vercel_ai/request_types.py`
