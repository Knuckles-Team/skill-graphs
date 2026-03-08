###  SubmitMessage
Bases: `CamelBaseModel`
Submit message request.
Source code in `pydantic_ai_slim/pydantic_ai/ui/vercel_ai/request_types.py`
```
376
377
378
379
380
381
```
| ```
class SubmitMessage(CamelBaseModel, extra='allow'):
    """Submit message request."""

    trigger: Literal['submit-message'] = 'submit-message'
    id: str
    messages: list[UIMessage]

```

---|---
###  RegenerateMessage
Bases: `CamelBaseModel`
Ask the agent to regenerate a message.
Source code in `pydantic_ai_slim/pydantic_ai/ui/vercel_ai/request_types.py`
```
384
385
386
387
388
389
390
```
| ```
class RegenerateMessage(CamelBaseModel, extra='allow'):
    """Ask the agent to regenerate a message."""

    trigger: Literal['regenerate-message']
    id: str
    messages: list[UIMessage]
    message_id: str

```

---|---
###  RequestData `module-attribute`
```
RequestData = [
    SubmitMessage[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.request_types.SubmitMessage "SubmitMessage \(pydantic_ai.ui.vercel_ai.request_types.SubmitMessage\)") | RegenerateMessage[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.request_types.RegenerateMessage "RegenerateMessage \(pydantic_ai.ui.vercel_ai.request_types.RegenerateMessage\)"),
    Discriminator[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Discriminator "pydantic.Discriminator")("trigger"),
]

```

Union of all request data types.
Vercel AI response types (SSE chunks).
Converted to Python from: https://github.com/vercel/ai/blob/ai%406.0.57/packages/ai/src/ui-message-stream/ui-message-chunks.ts
Tool approval types (`ToolApprovalRequestChunk`, `ToolOutputDeniedChunk`) require AI SDK UI v6 or later.
###  ProviderMetadata `module-attribute`
```
ProviderMetadata = [, [, JSONValue]]

```

Provider metadata.
###  FinishReason `module-attribute`
```
FinishReason = (
    [
        "stop",
        "length",
        "content-filter",
        "tool-calls",
        "error",
        "other",
    ]
    | None
)

```

Reason why the model finished generating.
###  BaseChunk
Bases: `CamelBaseModel`,
Abstract base class for response SSE events.
Source code in `pydantic_ai_slim/pydantic_ai/ui/vercel_ai/response_types.py`
```
25
26
27
28
29
```
| ```
class BaseChunk(CamelBaseModel, ABC):
    """Abstract base class for response SSE events."""

    def encode(self, sdk_version: int) -> str:
        return self.model_dump_json(by_alias=True, exclude_none=True)

```

---|---
###  TextStartChunk
Bases: `BaseChunk[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.response_types.BaseChunk "BaseChunk \(pydantic_ai.ui.vercel_ai.response_types.BaseChunk\)")`
Text start chunk.
Source code in `pydantic_ai_slim/pydantic_ai/ui/vercel_ai/response_types.py`
```
32
33
34
35
36
37
```
| ```
class TextStartChunk(BaseChunk):
    """Text start chunk."""

    type: Literal['text-start'] = 'text-start'
    id: str
    provider_metadata: ProviderMetadata | None = None

```

---|---
###  TextDeltaChunk
Bases: `BaseChunk[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.response_types.BaseChunk "BaseChunk \(pydantic_ai.ui.vercel_ai.response_types.BaseChunk\)")`
Text delta chunk.
Source code in `pydantic_ai_slim/pydantic_ai/ui/vercel_ai/response_types.py`
```
40
41
42
43
44
45
46
```
| ```
class TextDeltaChunk(BaseChunk):
    """Text delta chunk."""

    type: Literal['text-delta'] = 'text-delta'
    delta: str
    id: str
    provider_metadata: ProviderMetadata | None = None

```

---|---
###  TextEndChunk
Bases: `BaseChunk[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.response_types.BaseChunk "BaseChunk \(pydantic_ai.ui.vercel_ai.response_types.BaseChunk\)")`
Text end chunk.
Source code in `pydantic_ai_slim/pydantic_ai/ui/vercel_ai/response_types.py`
```
49
50
51
52
53
54
```
| ```
class TextEndChunk(BaseChunk):
    """Text end chunk."""

    type: Literal['text-end'] = 'text-end'
    id: str
    provider_metadata: ProviderMetadata | None = None

```

---|---
###  ReasoningStartChunk
Bases: `BaseChunk[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.response_types.BaseChunk "BaseChunk \(pydantic_ai.ui.vercel_ai.response_types.BaseChunk\)")`
Reasoning start chunk.
Source code in `pydantic_ai_slim/pydantic_ai/ui/vercel_ai/response_types.py`
```
57
58
59
60
61
62
```
| ```
class ReasoningStartChunk(BaseChunk):
    """Reasoning start chunk."""

    type: Literal['reasoning-start'] = 'reasoning-start'
    id: str
    provider_metadata: ProviderMetadata | None = None

```

---|---
###  ReasoningDeltaChunk
Bases: `BaseChunk[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.response_types.BaseChunk "BaseChunk \(pydantic_ai.ui.vercel_ai.response_types.BaseChunk\)")`
Reasoning delta chunk.
Source code in `pydantic_ai_slim/pydantic_ai/ui/vercel_ai/response_types.py`
```
65
66
67
68
69
70
71
```
| ```
class ReasoningDeltaChunk(BaseChunk):
    """Reasoning delta chunk."""

    type: Literal['reasoning-delta'] = 'reasoning-delta'
    id: str
    delta: str
    provider_metadata: ProviderMetadata | None = None

```

---|---
###  ReasoningEndChunk
Bases: `BaseChunk[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.response_types.BaseChunk "BaseChunk \(pydantic_ai.ui.vercel_ai.response_types.BaseChunk\)")`
Reasoning end chunk.
Source code in `pydantic_ai_slim/pydantic_ai/ui/vercel_ai/response_types.py`
```
74
75
76
77
78
79
```
| ```
class ReasoningEndChunk(BaseChunk):
    """Reasoning end chunk."""

    type: Literal['reasoning-end'] = 'reasoning-end'
    id: str
    provider_metadata: ProviderMetadata | None = None

```

---|---
###  ErrorChunk
Bases: `BaseChunk[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.response_types.BaseChunk "BaseChunk \(pydantic_ai.ui.vercel_ai.response_types.BaseChunk\)")`
Error chunk.
Source code in `pydantic_ai_slim/pydantic_ai/ui/vercel_ai/response_types.py`
```
82
83
84
85
86
```
| ```
class ErrorChunk(BaseChunk):
    """Error chunk."""

    type: Literal['error'] = 'error'
    error_text: str

```

---|---
###  ToolInputStartChunk
Bases: `BaseChunk[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.response_types.BaseChunk "BaseChunk \(pydantic_ai.ui.vercel_ai.response_types.BaseChunk\)")`
Tool input start chunk.
Source code in `pydantic_ai_slim/pydantic_ai/ui/vercel_ai/response_types.py`
```
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
```
| ```
class ToolInputStartChunk(BaseChunk):
    """Tool input start chunk."""

    type: Literal['tool-input-start'] = 'tool-input-start'
    tool_call_id: str
    tool_name: str
    provider_executed: bool | None = None
    provider_metadata: ProviderMetadata | None = None
    dynamic: bool | None = None

    def encode(self, sdk_version: int) -> str:
        exclude = {'provider_metadata'} if sdk_version < 6 else None
        return self.model_dump_json(by_alias=True, exclude_none=True, exclude=exclude)

```

---|---
###  ToolInputDeltaChunk
Bases: `BaseChunk[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.response_types.BaseChunk "BaseChunk \(pydantic_ai.ui.vercel_ai.response_types.BaseChunk\)")`
Tool input delta chunk.
Source code in `pydantic_ai_slim/pydantic_ai/ui/vercel_ai/response_types.py`
```
104
105
106
107
108
109
```
| ```
class ToolInputDeltaChunk(BaseChunk):
    """Tool input delta chunk."""

    type: Literal['tool-input-delta'] = 'tool-input-delta'
    tool_call_id: str
    input_text_delta: str

```

---|---
###  ToolOutputAvailableChunk
Bases: `BaseChunk[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.response_types.BaseChunk "BaseChunk \(pydantic_ai.ui.vercel_ai.response_types.BaseChunk\)")`
Tool output available chunk.
Source code in `pydantic_ai_slim/pydantic_ai/ui/vercel_ai/response_types.py`
```
112
113
114
115
116
117
118
119
120
```
| ```
class ToolOutputAvailableChunk(BaseChunk):
    """Tool output available chunk."""

    type: Literal['tool-output-available'] = 'tool-output-available'
    tool_call_id: str
    output: Any
    provider_executed: bool | None = None
    dynamic: bool | None = None
    preliminary: bool | None = None

```

---|---
###  ToolInputAvailableChunk
Bases: `BaseChunk[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.response_types.BaseChunk "BaseChunk \(pydantic_ai.ui.vercel_ai.response_types.BaseChunk\)")`
Tool input available chunk.
Source code in `pydantic_ai_slim/pydantic_ai/ui/vercel_ai/response_types.py`
```
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
```
| ```
class ToolInputAvailableChunk(BaseChunk):
    """Tool input available chunk."""

    type: Literal['tool-input-available'] = 'tool-input-available'
    tool_call_id: str
    tool_name: str
    input: Any
    provider_executed: bool | None = None
    provider_metadata: ProviderMetadata | None = None
    dynamic: bool | None = None

```

---|---
###  ToolInputErrorChunk
Bases: `BaseChunk[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.response_types.BaseChunk "BaseChunk \(pydantic_ai.ui.vercel_ai.response_types.BaseChunk\)")`
Tool input error chunk.
Source code in `pydantic_ai_slim/pydantic_ai/ui/vercel_ai/response_types.py`
```
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
```
| ```
class ToolInputErrorChunk(BaseChunk):
    """Tool input error chunk."""

    type: Literal['tool-input-error'] = 'tool-input-error'
    tool_call_id: str
    tool_name: str
    input: Any
    provider_executed: bool | None = None
    provider_metadata: ProviderMetadata | None = None
    dynamic: bool | None = None
    error_text: str

```

---|---
###  ToolOutputErrorChunk
Bases: `BaseChunk[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.response_types.BaseChunk "BaseChunk \(pydantic_ai.ui.vercel_ai.response_types.BaseChunk\)")`
Tool output error chunk.
Source code in `pydantic_ai_slim/pydantic_ai/ui/vercel_ai/response_types.py`
```
148
149
150
151
152
153
154
155
```
| ```
class ToolOutputErrorChunk(BaseChunk):
    """Tool output error chunk."""

    type: Literal['tool-output-error'] = 'tool-output-error'
    tool_call_id: str
    error_text: str
    provider_executed: bool | None = None
    dynamic: bool | None = None

```

---|---
###  ToolApprovalRequestChunk
Bases: `BaseChunk[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.response_types.BaseChunk "BaseChunk \(pydantic_ai.ui.vercel_ai.response_types.BaseChunk\)")`
Tool approval request chunk for human-in-the-loop approval.
Requires AI SDK UI v6 or later.
Source code in `pydantic_ai_slim/pydantic_ai/ui/vercel_ai/response_types.py`
```
158
159
160
161
162
163
164
165
166
```
| ```
class ToolApprovalRequestChunk(BaseChunk):
    """Tool approval request chunk for human-in-the-loop approval.

    Requires AI SDK UI v6 or later.
    """

    type: Literal['tool-approval-request'] = 'tool-approval-request'
    approval_id: str
    tool_call_id: str

```

---|---
###  ToolOutputDeniedChunk
Bases: `BaseChunk[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.response_types.BaseChunk "BaseChunk \(pydantic_ai.ui.vercel_ai.response_types.BaseChunk\)")`
Tool output denied chunk when user denies tool execution.
Requires AI SDK UI v6 or later.
Source code in `pydantic_ai_slim/pydantic_ai/ui/vercel_ai/response_types.py`
```
169
170
171
172
173
174
175
176
```
| ```
class ToolOutputDeniedChunk(BaseChunk):
    """Tool output denied chunk when user denies tool execution.

    Requires AI SDK UI v6 or later.
    """

    type: Literal['tool-output-denied'] = 'tool-output-denied'
    tool_call_id: str

```

---|---
###  SourceUrlChunk
Bases: `BaseChunk[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.response_types.BaseChunk "BaseChunk \(pydantic_ai.ui.vercel_ai.response_types.BaseChunk\)")`
Source URL chunk.
Source code in `pydantic_ai_slim/pydantic_ai/ui/vercel_ai/response_types.py`
```
179
180
181
182
183
184
185
186
```
| ```
class SourceUrlChunk(BaseChunk):
    """Source URL chunk."""

    type: Literal['source-url'] = 'source-url'
    source_id: str
    url: str
    title: str | None = None
    provider_metadata: ProviderMetadata | None = None

```

---|---
###  SourceDocumentChunk
Bases: `BaseChunk[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.response_types.BaseChunk "BaseChunk \(pydantic_ai.ui.vercel_ai.response_types.BaseChunk\)")`
Source document chunk.
Source code in `pydantic_ai_slim/pydantic_ai/ui/vercel_ai/response_types.py`
```
189
190
191
192
193
194
195
196
197
```
| ```
class SourceDocumentChunk(BaseChunk):
    """Source document chunk."""

    type: Literal['source-document'] = 'source-document'
    source_id: str
    media_type: str
    title: str
    filename: str | None = None
    provider_metadata: ProviderMetadata | None = None

```

---|---
###  FileChunk
Bases: `BaseChunk[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.response_types.BaseChunk "BaseChunk \(pydantic_ai.ui.vercel_ai.response_types.BaseChunk\)")`
File chunk.
Source code in `pydantic_ai_slim/pydantic_ai/ui/vercel_ai/response_types.py`
```
200
201
202
203
204
205
```
| ```
class FileChunk(BaseChunk):
    """File chunk."""

    type: Literal['file'] = 'file'
    url: str
    media_type: str

```

---|---
###  DataChunk
Bases: `BaseChunk[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.response_types.BaseChunk "BaseChunk \(pydantic_ai.ui.vercel_ai.response_types.BaseChunk\)")`
Data chunk with dynamic type.
Source code in `pydantic_ai_slim/pydantic_ai/ui/vercel_ai/response_types.py`
```
208
209
210
211
212
213
214
```
| ```
class DataChunk(BaseChunk):
    """Data chunk with dynamic type."""

    type: Annotated[str, Field(pattern=r'^data-')]
    id: str | None = None
    data: Any
    transient: bool | None = None

```

---|---
###  StartStepChunk
Bases: `BaseChunk[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.response_types.BaseChunk "BaseChunk \(pydantic_ai.ui.vercel_ai.response_types.BaseChunk\)")`
Start step chunk.
Source code in `pydantic_ai_slim/pydantic_ai/ui/vercel_ai/response_types.py`
```
217
218
219
220
```
| ```
class StartStepChunk(BaseChunk):
    """Start step chunk."""

    type: Literal['start-step'] = 'start-step'

```

---|---
###  FinishStepChunk
Bases: `BaseChunk[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.response_types.BaseChunk "BaseChunk \(pydantic_ai.ui.vercel_ai.response_types.BaseChunk\)")`
Finish step chunk.
Source code in `pydantic_ai_slim/pydantic_ai/ui/vercel_ai/response_types.py`
```
223
224
225
226
```
| ```
class FinishStepChunk(BaseChunk):
    """Finish step chunk."""

    type: Literal['finish-step'] = 'finish-step'

```

---|---
###  StartChunk
Bases: `BaseChunk[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.response_types.BaseChunk "BaseChunk \(pydantic_ai.ui.vercel_ai.response_types.BaseChunk\)")`
Start chunk.
Source code in `pydantic_ai_slim/pydantic_ai/ui/vercel_ai/response_types.py`
```
229
230
231
232
233
234
```
| ```
class StartChunk(BaseChunk):
    """Start chunk."""

    type: Literal['start'] = 'start'
    message_id: str | None = None
    message_metadata: Any | None = None

```

---|---
###  FinishChunk
Bases: `BaseChunk[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.response_types.BaseChunk "BaseChunk \(pydantic_ai.ui.vercel_ai.response_types.BaseChunk\)")`
Finish chunk.
Source code in `pydantic_ai_slim/pydantic_ai/ui/vercel_ai/response_types.py`
```
237
238
239
240
241
242
```
| ```
class FinishChunk(BaseChunk):
    """Finish chunk."""

    type: Literal['finish'] = 'finish'
    finish_reason: FinishReason = None
    message_metadata: Any | None = None

```

---|---
###  AbortChunk
Bases: `BaseChunk[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.response_types.BaseChunk "BaseChunk \(pydantic_ai.ui.vercel_ai.response_types.BaseChunk\)")`
Abort chunk.
Source code in `pydantic_ai_slim/pydantic_ai/ui/vercel_ai/response_types.py`
```
245
246
247
248
249
```
| ```
class AbortChunk(BaseChunk):
    """Abort chunk."""

    type: Literal['abort'] = 'abort'
    reason: str | None = None

```

---|---
###  MessageMetadataChunk
Bases: `BaseChunk[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.response_types.BaseChunk "BaseChunk \(pydantic_ai.ui.vercel_ai.response_types.BaseChunk\)")`
Message metadata chunk.
Source code in `pydantic_ai_slim/pydantic_ai/ui/vercel_ai/response_types.py`
```
252
253
254
255
256
```
| ```
class MessageMetadataChunk(BaseChunk):
    """Message metadata chunk."""

    type: Literal['message-metadata'] = 'message-metadata'
    message_metadata: Any

```

---|---
###  DoneChunk
Bases: `BaseChunk[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.response_types.BaseChunk "BaseChunk \(pydantic_ai.ui.vercel_ai.response_types.BaseChunk\)")`
Done chunk.
Source code in `pydantic_ai_slim/pydantic_ai/ui/vercel_ai/response_types.py`
```
259
260
261
262
263
264
265
```
| ```
class DoneChunk(BaseChunk):
    """Done chunk."""

    type: Literal['done'] = 'done'

    def encode(self, sdk_version: int) -> str:
        return '[DONE]'

```

---|---
© Pydantic Services Inc. 2024 to present
