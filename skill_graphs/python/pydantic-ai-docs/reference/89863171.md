# `pydantic_ai.ui.ag_ui`
AG-UI protocol integration for Pydantic AI agents.
###  AGUIAdapter `dataclass`
Bases: `UIAdapter[](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.UIAdapter "UIAdapter



      dataclass
   \(pydantic_ai.ui.UIAdapter\)")[RunAgentInput, Message, BaseEvent, AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)"), OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")]`
UI adapter for the Agent-User Interaction (AG-UI) protocol.
Source code in `pydantic_ai_slim/pydantic_ai/ui/ag_ui/_adapter.py`
```
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
```
| ```
class AGUIAdapter(UIAdapter[RunAgentInput, Message, BaseEvent, AgentDepsT, OutputDataT]):
    """UI adapter for the Agent-User Interaction (AG-UI) protocol."""

    @classmethod
    def build_run_input(cls, body: bytes) -> RunAgentInput:
        """Build an AG-UI run input object from the request body."""
        return RunAgentInput.model_validate_json(body)

    def build_event_stream(self) -> UIEventStream[RunAgentInput, BaseEvent, AgentDepsT, OutputDataT]:
        """Build an AG-UI event stream transformer."""
        return AGUIEventStream(self.run_input, accept=self.accept)

    @cached_property
    def messages(self) -> list[ModelMessage]:
        """Pydantic AI messages from the AG-UI run input."""
        return self.load_messages(self.run_input.messages)

    @cached_property
    def toolset(self) -> AbstractToolset[AgentDepsT] | None:
        """Toolset representing frontend tools from the AG-UI run input."""
        if self.run_input.tools:
            return _AGUIFrontendToolset[AgentDepsT](self.run_input.tools)
        return None

    @cached_property
    def state(self) -> dict[str, Any] | None:
        """Frontend state from the AG-UI run input."""
        state = self.run_input.state
        if state is None:
            return None

        if isinstance(state, Mapping) and not state:
            return None

        return cast('dict[str, Any]', state)

    @classmethod
    def load_messages(cls, messages: Sequence[Message]) -> list[ModelMessage]:  # noqa: C901
        """Transform AG-UI messages into Pydantic AI messages."""
        builder = MessagesBuilder()
        tool_calls: dict[str, str] = {}  # Tool call ID to tool name mapping.
        for msg in messages:
            match msg:
                case UserMessage(content=content):
                    if isinstance(content, str):
                        builder.add(UserPromptPart(content=content))
                    else:
                        user_prompt_content: list[Any] = []
                        for part in content:
                            match part:
                                case TextInputContent(text=text):
                                    user_prompt_content.append(text)
                                case BinaryInputContent():
                                    if part.url:
                                        try:
                                            binary_part = BinaryContent.from_data_uri(part.url)
                                        except ValueError:
                                            media_type_constructors = {
                                                'image': ImageUrl,
                                                'video': VideoUrl,
                                                'audio': AudioUrl,
                                            }
                                            media_type_prefix = part.mime_type.split('/', 1)[0]
                                            constructor = media_type_constructors.get(media_type_prefix, DocumentUrl)
                                            binary_part = constructor(url=part.url, media_type=part.mime_type)
                                    elif part.data:
                                        binary_part = BinaryContent(
                                            data=b64decode(part.data), media_type=part.mime_type
                                        )
                                    else:  # pragma: no cover
                                        raise ValueError('BinaryInputContent must have either a `url` or `data` field.')
                                    user_prompt_content.append(binary_part)
                                case _:  # pragma: no cover
                                    raise ValueError(f'Unsupported user message part type: {type(part)}')

                        if user_prompt_content:  # pragma: no branch
                            content_to_add = (
                                user_prompt_content[0]
                                if len(user_prompt_content) == 1 and isinstance(user_prompt_content[0], str)
                                else user_prompt_content
                            )
                            builder.add(UserPromptPart(content=content_to_add))

                case SystemMessage(content=content) | DeveloperMessage(content=content):
                    builder.add(SystemPromptPart(content=content))

                case AssistantMessage(content=content, tool_calls=tool_calls_list):
                    if content:
                        builder.add(TextPart(content=content))
                    if tool_calls_list:
                        for tool_call in tool_calls_list:
                            tool_call_id = tool_call.id
                            tool_name = tool_call.function.name
                            tool_calls[tool_call_id] = tool_name

                            if tool_call_id.startswith(BUILTIN_TOOL_CALL_ID_PREFIX):
                                _, provider_name, original_id = tool_call_id.split('|', 2)
                                builder.add(
                                    BuiltinToolCallPart(
                                        tool_name=tool_name,
                                        args=tool_call.function.arguments,
                                        tool_call_id=original_id,
                                        provider_name=provider_name,
                                    )
                                )
                            else:
                                builder.add(
                                    ToolCallPart(
                                        tool_name=tool_name,
                                        tool_call_id=tool_call_id,
                                        args=tool_call.function.arguments,
                                    )
                                )
                case ToolMessage() as tool_msg:
                    tool_call_id = tool_msg.tool_call_id
                    tool_name = tool_calls.get(tool_call_id)
                    if tool_name is None:  # pragma: no cover
                        raise ValueError(f'Tool call with ID {tool_call_id} not found in the history.')

                    if tool_call_id.startswith(BUILTIN_TOOL_CALL_ID_PREFIX):
                        _, provider_name, original_id = tool_call_id.split('|', 2)
                        builder.add(
                            BuiltinToolReturnPart(
                                tool_name=tool_name,
                                content=tool_msg.content,
                                tool_call_id=original_id,
                                provider_name=provider_name,
                            )
                        )
                    else:
                        builder.add(
                            ToolReturnPart(
                                tool_name=tool_name,
                                content=tool_msg.content,
                                tool_call_id=tool_call_id,
                            )
                        )

                case ActivityMessage():
                    pass

        return builder.messages

```

---|---
####  build_run_input `classmethod`
```
build_run_input(body: ) -> RunAgentInput

```

Build an AG-UI run input object from the request body.
Source code in `pydantic_ai_slim/pydantic_ai/ui/ag_ui/_adapter.py`
```
96
97
98
99
```
| ```
@classmethod
def build_run_input(cls, body: bytes) -> RunAgentInput:
    """Build an AG-UI run input object from the request body."""
    return RunAgentInput.model_validate_json(body)

```

---|---
####  build_event_stream
```
build_event_stream() -> (
    UIEventStream[](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.UIEventStream "UIEventStream



      dataclass
   \(pydantic_ai.ui.UIEventStream\)")[
        RunAgentInput, BaseEvent, AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)"), OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")
    ]
)

```

Build an AG-UI event stream transformer.
Source code in `pydantic_ai_slim/pydantic_ai/ui/ag_ui/_adapter.py`
```
101
102
103
```
| ```
def build_event_stream(self) -> UIEventStream[RunAgentInput, BaseEvent, AgentDepsT, OutputDataT]:
    """Build an AG-UI event stream transformer."""
    return AGUIEventStream(self.run_input, accept=self.accept)

```

---|---
####  messages `cached` `property`
```
messages: [ModelMessage[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelMessage "ModelMessage



      module-attribute
   \(pydantic_ai.messages.ModelMessage\)")]

```

Pydantic AI messages from the AG-UI run input.
####  toolset `cached` `property`
```
toolset: AbstractToolset[](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.AbstractToolset "AbstractToolset \(pydantic_ai.toolsets.AbstractToolset\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")] | None

```

Toolset representing frontend tools from the AG-UI run input.
####  state `cached` `property`
```
state: [, ] | None

```

Frontend state from the AG-UI run input.
####  load_messages `classmethod`
```
load_messages(
    messages: [Message],
) -> [ModelMessage[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelMessage "ModelMessage



      module-attribute
   \(pydantic_ai.messages.ModelMessage\)")]

```

Transform AG-UI messages into Pydantic AI messages.
Source code in `pydantic_ai_slim/pydantic_ai/ui/ag_ui/_adapter.py`
```
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
```
| ```
@classmethod
def load_messages(cls, messages: Sequence[Message]) -> list[ModelMessage]:  # noqa: C901
    """Transform AG-UI messages into Pydantic AI messages."""
    builder = MessagesBuilder()
    tool_calls: dict[str, str] = {}  # Tool call ID to tool name mapping.
    for msg in messages:
        match msg:
            case UserMessage(content=content):
                if isinstance(content, str):
                    builder.add(UserPromptPart(content=content))
                else:
                    user_prompt_content: list[Any] = []
                    for part in content:
                        match part:
                            case TextInputContent(text=text):
                                user_prompt_content.append(text)
                            case BinaryInputContent():
                                if part.url:
                                    try:
                                        binary_part = BinaryContent.from_data_uri(part.url)
                                    except ValueError:
                                        media_type_constructors = {
                                            'image': ImageUrl,
                                            'video': VideoUrl,
                                            'audio': AudioUrl,
                                        }
                                        media_type_prefix = part.mime_type.split('/', 1)[0]
                                        constructor = media_type_constructors.get(media_type_prefix, DocumentUrl)
                                        binary_part = constructor(url=part.url, media_type=part.mime_type)
                                elif part.data:
                                    binary_part = BinaryContent(
                                        data=b64decode(part.data), media_type=part.mime_type
                                    )
                                else:  # pragma: no cover
                                    raise ValueError('BinaryInputContent must have either a `url` or `data` field.')
                                user_prompt_content.append(binary_part)
                            case _:  # pragma: no cover
                                raise ValueError(f'Unsupported user message part type: {type(part)}')

                    if user_prompt_content:  # pragma: no branch
                        content_to_add = (
                            user_prompt_content[0]
                            if len(user_prompt_content) == 1 and isinstance(user_prompt_content[0], str)
                            else user_prompt_content
                        )
                        builder.add(UserPromptPart(content=content_to_add))

            case SystemMessage(content=content) | DeveloperMessage(content=content):
                builder.add(SystemPromptPart(content=content))

            case AssistantMessage(content=content, tool_calls=tool_calls_list):
                if content:
                    builder.add(TextPart(content=content))
                if tool_calls_list:
                    for tool_call in tool_calls_list:
                        tool_call_id = tool_call.id
                        tool_name = tool_call.function.name
                        tool_calls[tool_call_id] = tool_name

                        if tool_call_id.startswith(BUILTIN_TOOL_CALL_ID_PREFIX):
                            _, provider_name, original_id = tool_call_id.split('|', 2)
                            builder.add(
                                BuiltinToolCallPart(
                                    tool_name=tool_name,
                                    args=tool_call.function.arguments,
                                    tool_call_id=original_id,
                                    provider_name=provider_name,
                                )
                            )
                        else:
                            builder.add(
                                ToolCallPart(
                                    tool_name=tool_name,
                                    tool_call_id=tool_call_id,
                                    args=tool_call.function.arguments,
                                )
                            )
            case ToolMessage() as tool_msg:
                tool_call_id = tool_msg.tool_call_id
                tool_name = tool_calls.get(tool_call_id)
                if tool_name is None:  # pragma: no cover
                    raise ValueError(f'Tool call with ID {tool_call_id} not found in the history.')

                if tool_call_id.startswith(BUILTIN_TOOL_CALL_ID_PREFIX):
                    _, provider_name, original_id = tool_call_id.split('|', 2)
                    builder.add(
                        BuiltinToolReturnPart(
                            tool_name=tool_name,
                            content=tool_msg.content,
                            tool_call_id=original_id,
                            provider_name=provider_name,
                        )
                    )
                else:
                    builder.add(
                        ToolReturnPart(
                            tool_name=tool_name,
                            content=tool_msg.content,
                            tool_call_id=tool_call_id,
                        )
                    )

            case ActivityMessage():
                pass

    return builder.messages

```

---|---
###  AGUIEventStream `dataclass`
Bases: `UIEventStream[](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.UIEventStream "UIEventStream



      dataclass
   \(pydantic_ai.ui.UIEventStream\)")[RunAgentInput, BaseEvent, AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)"), OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")]`
UI event stream transformer for the Agent-User Interaction (AG-UI) protocol.
Source code in `pydantic_ai_slim/pydantic_ai/ui/ag_ui/_event_stream.py`
```
 72
 73
 74
 75
 76
 77
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
```
| ```
@dataclass
class AGUIEventStream(UIEventStream[RunAgentInput, BaseEvent, AgentDepsT, OutputDataT]):
    """UI event stream transformer for the Agent-User Interaction (AG-UI) protocol."""

    _thinking_text: bool = False
    _builtin_tool_call_ids: dict[str, str] = field(default_factory=dict[str, str])
    _error: bool = False

    @property
    def _event_encoder(self) -> EventEncoder:
        return EventEncoder(accept=self.accept or SSE_CONTENT_TYPE)

    @property
    def content_type(self) -> str:
        return self._event_encoder.get_content_type()

    def encode_event(self, event: BaseEvent) -> str:
        return self._event_encoder.encode(event)

    @staticmethod
    def _get_timestamp() -> int:
        return int(now_utc().timestamp() * 1_000)

    async def handle_event(self, event: NativeEvent) -> AsyncIterator[BaseEvent]:
        """Override to set timestamps on all AG-UI events."""
        async for agui_event in super().handle_event(event):
            if agui_event.timestamp is None:
                agui_event.timestamp = self._get_timestamp()
            yield agui_event

    async def before_stream(self) -> AsyncIterator[BaseEvent]:
        yield RunStartedEvent(
            thread_id=self.run_input.thread_id,
            run_id=self.run_input.run_id,
            timestamp=self._get_timestamp(),
        )

    async def before_response(self) -> AsyncIterator[BaseEvent]:
        # Prevent parts from a subsequent response being tied to parts from an earlier response.
        # See https://github.com/pydantic/pydantic-ai/issues/3316
        self.new_message_id()
        return
        yield  # Make this an async generator

    async def after_stream(self) -> AsyncIterator[BaseEvent]:
        if not self._error:
            yield RunFinishedEvent(
                thread_id=self.run_input.thread_id,
                run_id=self.run_input.run_id,
                timestamp=self._get_timestamp(),
            )

    async def on_error(self, error: Exception) -> AsyncIterator[BaseEvent]:
        self._error = True
        yield RunErrorEvent(message=str(error), timestamp=self._get_timestamp())

    async def handle_text_start(self, part: TextPart, follows_text: bool = False) -> AsyncIterator[BaseEvent]:
        if follows_text:
            message_id = self.message_id
        else:
            message_id = self.new_message_id()
            yield TextMessageStartEvent(message_id=message_id)

        if part.content:  # pragma: no branch
            yield TextMessageContentEvent(message_id=message_id, delta=part.content)

    async def handle_text_delta(self, delta: TextPartDelta) -> AsyncIterator[BaseEvent]:
        if delta.content_delta:  # pragma: no branch
            yield TextMessageContentEvent(message_id=self.message_id, delta=delta.content_delta)

    async def handle_text_end(self, part: TextPart, followed_by_text: bool = False) -> AsyncIterator[BaseEvent]:
        if not followed_by_text:
            yield TextMessageEndEvent(message_id=self.message_id)

    async def handle_thinking_start(
        self, part: ThinkingPart, follows_thinking: bool = False
    ) -> AsyncIterator[BaseEvent]:
        if not follows_thinking:
            yield ThinkingStartEvent(type=EventType.THINKING_START)

        if part.content:
            yield ThinkingTextMessageStartEvent(type=EventType.THINKING_TEXT_MESSAGE_START)
            yield ThinkingTextMessageContentEvent(type=EventType.THINKING_TEXT_MESSAGE_CONTENT, delta=part.content)
            self._thinking_text = True

    async def handle_thinking_delta(self, delta: ThinkingPartDelta) -> AsyncIterator[BaseEvent]:
        if not delta.content_delta:
            return  # pragma: no cover

        if not self._thinking_text:
            yield ThinkingTextMessageStartEvent(type=EventType.THINKING_TEXT_MESSAGE_START)
            self._thinking_text = True

        yield ThinkingTextMessageContentEvent(type=EventType.THINKING_TEXT_MESSAGE_CONTENT, delta=delta.content_delta)

    async def handle_thinking_end(
        self, part: ThinkingPart, followed_by_thinking: bool = False
    ) -> AsyncIterator[BaseEvent]:
        if self._thinking_text:
            yield ThinkingTextMessageEndEvent(type=EventType.THINKING_TEXT_MESSAGE_END)
            self._thinking_text = False

        if not followed_by_thinking:
            yield ThinkingEndEvent(type=EventType.THINKING_END)

    def handle_tool_call_start(self, part: ToolCallPart | BuiltinToolCallPart) -> AsyncIterator[BaseEvent]:
        return self._handle_tool_call_start(part)

    def handle_builtin_tool_call_start(self, part: BuiltinToolCallPart) -> AsyncIterator[BaseEvent]:
        tool_call_id = part.tool_call_id
        builtin_tool_call_id = '|'.join([BUILTIN_TOOL_CALL_ID_PREFIX, part.provider_name or '', tool_call_id])
        self._builtin_tool_call_ids[tool_call_id] = builtin_tool_call_id
        tool_call_id = builtin_tool_call_id

        return self._handle_tool_call_start(part, tool_call_id)

    async def _handle_tool_call_start(
        self, part: ToolCallPart | BuiltinToolCallPart, tool_call_id: str | None = None
    ) -> AsyncIterator[BaseEvent]:
        tool_call_id = tool_call_id or part.tool_call_id
        parent_message_id = self.message_id

        yield ToolCallStartEvent(
            tool_call_id=tool_call_id, tool_call_name=part.tool_name, parent_message_id=parent_message_id
        )
        if part.args:
            yield ToolCallArgsEvent(tool_call_id=tool_call_id, delta=part.args_as_json_str())

    async def handle_tool_call_delta(self, delta: ToolCallPartDelta) -> AsyncIterator[BaseEvent]:
        tool_call_id = delta.tool_call_id
        assert tool_call_id, '`ToolCallPartDelta.tool_call_id` must be set'
        if tool_call_id in self._builtin_tool_call_ids:
            tool_call_id = self._builtin_tool_call_ids[tool_call_id]
        yield ToolCallArgsEvent(
            tool_call_id=tool_call_id,
            delta=delta.args_delta if isinstance(delta.args_delta, str) else json.dumps(delta.args_delta),
        )

    async def handle_tool_call_end(self, part: ToolCallPart) -> AsyncIterator[BaseEvent]:
        yield ToolCallEndEvent(tool_call_id=part.tool_call_id)

    async def handle_builtin_tool_call_end(self, part: BuiltinToolCallPart) -> AsyncIterator[BaseEvent]:
        yield ToolCallEndEvent(tool_call_id=self._builtin_tool_call_ids[part.tool_call_id])

    async def handle_builtin_tool_return(self, part: BuiltinToolReturnPart) -> AsyncIterator[BaseEvent]:
        tool_call_id = self._builtin_tool_call_ids[part.tool_call_id]
        # Use a one-off message ID instead of `self.new_message_id()` to avoid
        # mutating `self.message_id`, which is used as `parent_message_id` for
        # subsequent tool calls in the same response.
        yield ToolCallResultEvent(
            message_id=str(uuid4()),
            type=EventType.TOOL_CALL_RESULT,
            role='tool',
            tool_call_id=tool_call_id,
            content=part.model_response_str(),
        )

    async def handle_function_tool_result(self, event: FunctionToolResultEvent) -> AsyncIterator[BaseEvent]:
