```
41
42
43
44
45
46
47
48
49
50
51
52
53
```
| ```
class ReasoningUIPart(BaseUIPart):
    """A reasoning part of a message."""

    type: Literal['reasoning'] = 'reasoning'

    text: str
    """The reasoning text."""

    state: Literal['streaming', 'done'] | None = None
    """The state of the reasoning part."""

    provider_metadata: ProviderMetadata | None = None
    """The provider metadata."""

```

---|---
####  text `instance-attribute`
```
text:

```

The reasoning text.
####  state `class-attribute` `instance-attribute`
```
state: ['streaming', 'done'] | None = None

```

The state of the reasoning part.
####  provider_metadata `class-attribute` `instance-attribute`
```
provider_metadata: ProviderMetadata[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.request_types.ProviderMetadata "ProviderMetadata



      module-attribute
   \(pydantic_ai.ui.vercel_ai.request_types.ProviderMetadata\)") | None = None

```

The provider metadata.
###  SourceUrlUIPart
Bases: `BaseUIPart[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.request_types.BaseUIPart "BaseUIPart \(pydantic_ai.ui.vercel_ai.request_types.BaseUIPart\)")`
A source part of a message.
Source code in `pydantic_ai_slim/pydantic_ai/ui/vercel_ai/request_types.py`
```
56
57
58
59
60
61
62
63
```
| ```
class SourceUrlUIPart(BaseUIPart):
    """A source part of a message."""

    type: Literal['source-url'] = 'source-url'
    source_id: str
    url: str
    title: str | None = None
    provider_metadata: ProviderMetadata | None = None

```

---|---
###  SourceDocumentUIPart
Bases: `BaseUIPart[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.request_types.BaseUIPart "BaseUIPart \(pydantic_ai.ui.vercel_ai.request_types.BaseUIPart\)")`
A document source part of a message.
Source code in `pydantic_ai_slim/pydantic_ai/ui/vercel_ai/request_types.py`
```
66
67
68
69
70
71
72
73
74
```
| ```
class SourceDocumentUIPart(BaseUIPart):
    """A document source part of a message."""

    type: Literal['source-document'] = 'source-document'
    source_id: str
    media_type: str
    title: str
    filename: str | None = None
    provider_metadata: ProviderMetadata | None = None

```

---|---
###  FileUIPart
Bases: `BaseUIPart[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.request_types.BaseUIPart "BaseUIPart \(pydantic_ai.ui.vercel_ai.request_types.BaseUIPart\)")`
A file part of a message.
Source code in `pydantic_ai_slim/pydantic_ai/ui/vercel_ai/request_types.py`
```
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
```
| ```
class FileUIPart(BaseUIPart):
    """A file part of a message."""

    type: Literal['file'] = 'file'

    media_type: str
    """
    IANA media type of the file.
    @see https://www.iana.org/assignments/media-types/media-types.xhtml
    """

    filename: str | None = None
    """Optional filename of the file."""

    url: str
    """
    The URL of the file.
    It can either be a URL to a hosted file or a [Data URL](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Data_URLs).
    """

    provider_metadata: ProviderMetadata | None = None
    """The provider metadata."""

```

---|---
####  media_type `instance-attribute`
```
media_type:

```

IANA media type of the file. @see https://www.iana.org/assignments/media-types/media-types.xhtml
####  filename `class-attribute` `instance-attribute`
```
filename:  | None = None

```

Optional filename of the file.
####  url `instance-attribute`
```
url:

```

The URL of the file. It can either be a URL to a hosted file or a
####  provider_metadata `class-attribute` `instance-attribute`
```
provider_metadata: ProviderMetadata[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.request_types.ProviderMetadata "ProviderMetadata



      module-attribute
   \(pydantic_ai.ui.vercel_ai.request_types.ProviderMetadata\)") | None = None

```

The provider metadata.
###  StepStartUIPart
Bases: `BaseUIPart[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.request_types.BaseUIPart "BaseUIPart \(pydantic_ai.ui.vercel_ai.request_types.BaseUIPart\)")`
A step boundary part of a message.
Source code in `pydantic_ai_slim/pydantic_ai/ui/vercel_ai/request_types.py`
```
101
102
103
104
```
| ```
class StepStartUIPart(BaseUIPart):
    """A step boundary part of a message."""

    type: Literal['step-start'] = 'step-start'

```

---|---
###  DataUIPart
Bases: `BaseUIPart[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.request_types.BaseUIPart "BaseUIPart \(pydantic_ai.ui.vercel_ai.request_types.BaseUIPart\)")`
Data part with dynamic type based on data name.
Source code in `pydantic_ai_slim/pydantic_ai/ui/vercel_ai/request_types.py`
```
107
108
109
110
111
112
```
| ```
class DataUIPart(BaseUIPart):
    """Data part with dynamic type based on data name."""

    type: Annotated[str, Field(pattern=r'^data-')]
    id: str | None = None
    data: Any

```

---|---
###  ToolApprovalRequested
Bases: `CamelBaseModel`
Tool approval in requested state (awaiting user response).
Source code in `pydantic_ai_slim/pydantic_ai/ui/vercel_ai/request_types.py`
```
115
116
117
118
119
```
| ```
class ToolApprovalRequested(CamelBaseModel):
    """Tool approval in requested state (awaiting user response)."""

    id: str
    """The approval request ID."""

```

---|---
####  id `instance-attribute`
```
id:

```

The approval request ID.
###  ToolApprovalResponded
Bases: `CamelBaseModel`
Tool approval in responded state (user has approved or denied).
Source code in `pydantic_ai_slim/pydantic_ai/ui/vercel_ai/request_types.py`
```
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
```
| ```
class ToolApprovalResponded(CamelBaseModel):
    """Tool approval in responded state (user has approved or denied)."""

    id: str
    """The approval request ID."""

    approved: bool
    """Whether the user approved the tool call."""

    reason: str | None = None
    """Optional reason for the approval or denial."""

```

---|---
####  id `instance-attribute`
```
id:

```

The approval request ID.
####  approved `instance-attribute`
```
approved:

```

Whether the user approved the tool call.
####  reason `class-attribute` `instance-attribute`
```
reason:  | None = None

```

Optional reason for the approval or denial.
###  ToolApproval `module-attribute`
```
ToolApproval = ToolApprovalRequested[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.request_types.ToolApprovalRequested "ToolApprovalRequested \(pydantic_ai.ui.vercel_ai.request_types.ToolApprovalRequested\)") | ToolApprovalResponded[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.request_types.ToolApprovalResponded "ToolApprovalResponded \(pydantic_ai.ui.vercel_ai.request_types.ToolApprovalResponded\)")

```

Union of tool approval states.
###  ToolInputStreamingPart
Bases: `BaseUIPart[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.request_types.BaseUIPart "BaseUIPart \(pydantic_ai.ui.vercel_ai.request_types.BaseUIPart\)")`
Tool part in input-streaming state.
Source code in `pydantic_ai_slim/pydantic_ai/ui/vercel_ai/request_types.py`
```
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
```
| ```
class ToolInputStreamingPart(BaseUIPart):
    """Tool part in input-streaming state."""

    type: Annotated[str, Field(pattern=r'^tool-')]
    tool_call_id: str
    state: Literal['input-streaming'] = 'input-streaming'
    input: Any | None = None
    provider_executed: bool | None = None
    call_provider_metadata: ProviderMetadata | None = None
    approval: ToolApproval | None = None

```

---|---
###  ToolInputAvailablePart
Bases: `BaseUIPart[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.request_types.BaseUIPart "BaseUIPart \(pydantic_ai.ui.vercel_ai.request_types.BaseUIPart\)")`
Tool part in input-available state.
Source code in `pydantic_ai_slim/pydantic_ai/ui/vercel_ai/request_types.py`
```
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
```
| ```
class ToolInputAvailablePart(BaseUIPart):
    """Tool part in input-available state."""

    type: Annotated[str, Field(pattern=r'^tool-')]
    tool_call_id: str
    state: Literal['input-available'] = 'input-available'
    input: Any | None = None
    provider_executed: bool | None = None
    call_provider_metadata: ProviderMetadata | None = None
    approval: ToolApproval | None = None

```

---|---
###  ToolOutputAvailablePart
Bases: `BaseUIPart[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.request_types.BaseUIPart "BaseUIPart \(pydantic_ai.ui.vercel_ai.request_types.BaseUIPart\)")`
Tool part in output-available state.
Source code in `pydantic_ai_slim/pydantic_ai/ui/vercel_ai/request_types.py`
```
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
```
| ```
class ToolOutputAvailablePart(BaseUIPart):
    """Tool part in output-available state."""

    type: Annotated[str, Field(pattern=r'^tool-')]
    tool_call_id: str
    state: Literal['output-available'] = 'output-available'
    input: Any | None = None
    output: Any | None = None
    provider_executed: bool | None = None
    call_provider_metadata: ProviderMetadata | None = None
    preliminary: bool | None = None
    approval: ToolApproval | None = None

```

---|---
###  ToolOutputErrorPart
Bases: `BaseUIPart[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.request_types.BaseUIPart "BaseUIPart \(pydantic_ai.ui.vercel_ai.request_types.BaseUIPart\)")`
Tool part in output-error state.
Source code in `pydantic_ai_slim/pydantic_ai/ui/vercel_ai/request_types.py`
```
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
```
| ```
class ToolOutputErrorPart(BaseUIPart):
    """Tool part in output-error state."""

    type: Annotated[str, Field(pattern=r'^tool-')]
    tool_call_id: str
    state: Literal['output-error'] = 'output-error'
    input: Any | None = None
    raw_input: Any | None = None
    error_text: str
    provider_executed: bool | None = None
    call_provider_metadata: ProviderMetadata | None = None
    approval: ToolApproval | None = None

```

---|---
###  ToolApprovalRequestedPart
Bases: `BaseUIPart[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.request_types.BaseUIPart "BaseUIPart \(pydantic_ai.ui.vercel_ai.request_types.BaseUIPart\)")`
Tool part in approval-requested state (awaiting user decision).
Source code in `pydantic_ai_slim/pydantic_ai/ui/vercel_ai/request_types.py`
```
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
```
| ```
class ToolApprovalRequestedPart(BaseUIPart):
    """Tool part in approval-requested state (awaiting user decision)."""

    type: Annotated[str, Field(pattern=r'^tool-')]
    tool_call_id: str
    state: Literal['approval-requested'] = 'approval-requested'
    input: Any | None = None
    provider_executed: bool | None = None
    call_provider_metadata: ProviderMetadata | None = None
    approval: ToolApproval | None = None

```

---|---
###  ToolApprovalRespondedPart
Bases: `BaseUIPart[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.request_types.BaseUIPart "BaseUIPart \(pydantic_ai.ui.vercel_ai.request_types.BaseUIPart\)")`
Tool part in approval-responded state (user approved/denied, execution pending).
Source code in `pydantic_ai_slim/pydantic_ai/ui/vercel_ai/request_types.py`
```
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
```
| ```
class ToolApprovalRespondedPart(BaseUIPart):
    """Tool part in approval-responded state (user approved/denied, execution pending)."""

    type: Annotated[str, Field(pattern=r'^tool-')]
    tool_call_id: str
    state: Literal['approval-responded'] = 'approval-responded'
    input: Any | None = None
    provider_executed: bool | None = None
    call_provider_metadata: ProviderMetadata | None = None
    approval: ToolApproval | None = None

```

---|---
###  ToolOutputDeniedPart
Bases: `BaseUIPart[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.request_types.BaseUIPart "BaseUIPart \(pydantic_ai.ui.vercel_ai.request_types.BaseUIPart\)")`
Tool part in output-denied state (tool was denied, terminal state).
Source code in `pydantic_ai_slim/pydantic_ai/ui/vercel_ai/request_types.py`
```
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
```
| ```
class ToolOutputDeniedPart(BaseUIPart):
    """Tool part in output-denied state (tool was denied, terminal state)."""

    type: Annotated[str, Field(pattern=r'^tool-')]
    tool_call_id: str
    state: Literal['output-denied'] = 'output-denied'
    input: Any | None = None
    provider_executed: bool | None = None
    call_provider_metadata: ProviderMetadata | None = None
    approval: ToolApproval | None = None

```

---|---
###  ToolUIPart `module-attribute`
```
ToolUIPart = (
    ToolInputStreamingPart[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.request_types.ToolInputStreamingPart "ToolInputStreamingPart \(pydantic_ai.ui.vercel_ai.request_types.ToolInputStreamingPart\)")
    | ToolInputAvailablePart[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.request_types.ToolInputAvailablePart "ToolInputAvailablePart \(pydantic_ai.ui.vercel_ai.request_types.ToolInputAvailablePart\)")
    | ToolOutputAvailablePart[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.request_types.ToolOutputAvailablePart "ToolOutputAvailablePart \(pydantic_ai.ui.vercel_ai.request_types.ToolOutputAvailablePart\)")
    | ToolOutputErrorPart[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.request_types.ToolOutputErrorPart "ToolOutputErrorPart \(pydantic_ai.ui.vercel_ai.request_types.ToolOutputErrorPart\)")
    | ToolApprovalRequestedPart[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.request_types.ToolApprovalRequestedPart "ToolApprovalRequestedPart \(pydantic_ai.ui.vercel_ai.request_types.ToolApprovalRequestedPart\)")
    | ToolApprovalRespondedPart[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.request_types.ToolApprovalRespondedPart "ToolApprovalRespondedPart \(pydantic_ai.ui.vercel_ai.request_types.ToolApprovalRespondedPart\)")
    | ToolOutputDeniedPart[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.request_types.ToolOutputDeniedPart "ToolOutputDeniedPart \(pydantic_ai.ui.vercel_ai.request_types.ToolOutputDeniedPart\)")
)

```

Union of all tool part types.
###  DynamicToolInputStreamingPart
Bases: `BaseUIPart[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.request_types.BaseUIPart "BaseUIPart \(pydantic_ai.ui.vercel_ai.request_types.BaseUIPart\)")`
Dynamic tool part in input-streaming state.
Source code in `pydantic_ai_slim/pydantic_ai/ui/vercel_ai/request_types.py`
```
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
```
| ```
class DynamicToolInputStreamingPart(BaseUIPart):
    """Dynamic tool part in input-streaming state."""

    type: Literal['dynamic-tool'] = 'dynamic-tool'
    tool_name: str
    tool_call_id: str
    state: Literal['input-streaming'] = 'input-streaming'
    input: Any | None = None
    call_provider_metadata: ProviderMetadata | None = None
    approval: ToolApproval | None = None

```

---|---
###  DynamicToolInputAvailablePart
Bases: `BaseUIPart[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.request_types.BaseUIPart "BaseUIPart \(pydantic_ai.ui.vercel_ai.request_types.BaseUIPart\)")`
Dynamic tool part in input-available state.
Source code in `pydantic_ai_slim/pydantic_ai/ui/vercel_ai/request_types.py`
```
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
```
| ```
class DynamicToolInputAvailablePart(BaseUIPart):
    """Dynamic tool part in input-available state."""

    type: Literal['dynamic-tool'] = 'dynamic-tool'
    tool_name: str
    tool_call_id: str
    state: Literal['input-available'] = 'input-available'
    input: Any
    call_provider_metadata: ProviderMetadata | None = None
    approval: ToolApproval | None = None

```

---|---
###  DynamicToolOutputAvailablePart
Bases: `BaseUIPart[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.request_types.BaseUIPart "BaseUIPart \(pydantic_ai.ui.vercel_ai.request_types.BaseUIPart\)")`
Dynamic tool part in output-available state.
Source code in `pydantic_ai_slim/pydantic_ai/ui/vercel_ai/request_types.py`
```
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
```
| ```
class DynamicToolOutputAvailablePart(BaseUIPart):
    """Dynamic tool part in output-available state."""

    type: Literal['dynamic-tool'] = 'dynamic-tool'
    tool_name: str
    tool_call_id: str
    state: Literal['output-available'] = 'output-available'
    input: Any
    output: Any
    call_provider_metadata: ProviderMetadata | None = None
    preliminary: bool | None = None
    approval: ToolApproval | None = None

```

---|---
###  DynamicToolOutputErrorPart
Bases: `BaseUIPart[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.request_types.BaseUIPart "BaseUIPart \(pydantic_ai.ui.vercel_ai.request_types.BaseUIPart\)")`
Dynamic tool part in output-error state.
Source code in `pydantic_ai_slim/pydantic_ai/ui/vercel_ai/request_types.py`
```
279
280
281
282
283
284
285
286
287
288
289
```
| ```
class DynamicToolOutputErrorPart(BaseUIPart):
    """Dynamic tool part in output-error state."""

    type: Literal['dynamic-tool'] = 'dynamic-tool'
    tool_name: str
    tool_call_id: str
    state: Literal['output-error'] = 'output-error'
    input: Any
    error_text: str
    call_provider_metadata: ProviderMetadata | None = None
    approval: ToolApproval | None = None

```

---|---
###  DynamicToolApprovalRequestedPart
Bases: `BaseUIPart[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.request_types.BaseUIPart "BaseUIPart \(pydantic_ai.ui.vercel_ai.request_types.BaseUIPart\)")`
Dynamic tool part in approval-requested state (awaiting user decision).
Source code in `pydantic_ai_slim/pydantic_ai/ui/vercel_ai/request_types.py`
```
292
293
294
295
296
297
298
299
300
301
```
| ```
class DynamicToolApprovalRequestedPart(BaseUIPart):
    """Dynamic tool part in approval-requested state (awaiting user decision)."""

    type: Literal['dynamic-tool'] = 'dynamic-tool'
    tool_name: str
    tool_call_id: str
    state: Literal['approval-requested'] = 'approval-requested'
    input: Any
    call_provider_metadata: ProviderMetadata | None = None
    approval: ToolApproval | None = None

```

---|---
###  DynamicToolApprovalRespondedPart
Bases: `BaseUIPart[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.request_types.BaseUIPart "BaseUIPart \(pydantic_ai.ui.vercel_ai.request_types.BaseUIPart\)")`
Dynamic tool part in approval-responded state (user approved/denied, execution pending).
Source code in `pydantic_ai_slim/pydantic_ai/ui/vercel_ai/request_types.py`
```
304
305
306
307
308
309
310
311
312
313
```
| ```
class DynamicToolApprovalRespondedPart(BaseUIPart):
    """Dynamic tool part in approval-responded state (user approved/denied, execution pending)."""

    type: Literal['dynamic-tool'] = 'dynamic-tool'
    tool_name: str
    tool_call_id: str
    state: Literal['approval-responded'] = 'approval-responded'
    input: Any
    call_provider_metadata: ProviderMetadata | None = None
    approval: ToolApproval | None = None

```

---|---
###  DynamicToolOutputDeniedPart
Bases: `BaseUIPart[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.request_types.BaseUIPart "BaseUIPart \(pydantic_ai.ui.vercel_ai.request_types.BaseUIPart\)")`
Dynamic tool part in output-denied state (tool was denied, terminal state).
Source code in `pydantic_ai_slim/pydantic_ai/ui/vercel_ai/request_types.py`
```
316
317
318
319
320
321
322
323
324
325
```
| ```
class DynamicToolOutputDeniedPart(BaseUIPart):
    """Dynamic tool part in output-denied state (tool was denied, terminal state)."""

    type: Literal['dynamic-tool'] = 'dynamic-tool'
    tool_name: str
    tool_call_id: str
    state: Literal['output-denied'] = 'output-denied'
    input: Any
    call_provider_metadata: ProviderMetadata | None = None
    approval: ToolApproval | None = None

```

---|---
###  DynamicToolUIPart `module-attribute`
```
DynamicToolUIPart = (
    DynamicToolInputStreamingPart[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.request_types.DynamicToolInputStreamingPart "DynamicToolInputStreamingPart \(pydantic_ai.ui.vercel_ai.request_types.DynamicToolInputStreamingPart\)")
    | DynamicToolInputAvailablePart[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.request_types.DynamicToolInputAvailablePart "DynamicToolInputAvailablePart \(pydantic_ai.ui.vercel_ai.request_types.DynamicToolInputAvailablePart\)")
    | DynamicToolOutputAvailablePart[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.request_types.DynamicToolOutputAvailablePart "DynamicToolOutputAvailablePart \(pydantic_ai.ui.vercel_ai.request_types.DynamicToolOutputAvailablePart\)")
    | DynamicToolOutputErrorPart[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.request_types.DynamicToolOutputErrorPart "DynamicToolOutputErrorPart \(pydantic_ai.ui.vercel_ai.request_types.DynamicToolOutputErrorPart\)")
    | DynamicToolApprovalRequestedPart[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.request_types.DynamicToolApprovalRequestedPart "DynamicToolApprovalRequestedPart \(pydantic_ai.ui.vercel_ai.request_types.DynamicToolApprovalRequestedPart\)")
    | DynamicToolApprovalRespondedPart[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.request_types.DynamicToolApprovalRespondedPart "DynamicToolApprovalRespondedPart \(pydantic_ai.ui.vercel_ai.request_types.DynamicToolApprovalRespondedPart\)")
    | DynamicToolOutputDeniedPart[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.request_types.DynamicToolOutputDeniedPart "DynamicToolOutputDeniedPart \(pydantic_ai.ui.vercel_ai.request_types.DynamicToolOutputDeniedPart\)")
)

```

Union of all dynamic tool part types.
###  UIMessagePart `module-attribute`
```
UIMessagePart = (
    TextUIPart[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.request_types.TextUIPart "TextUIPart \(pydantic_ai.ui.vercel_ai.request_types.TextUIPart\)")
    | ReasoningUIPart[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.request_types.ReasoningUIPart "ReasoningUIPart \(pydantic_ai.ui.vercel_ai.request_types.ReasoningUIPart\)")
    | ToolUIPart[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.request_types.ToolUIPart "ToolUIPart



      module-attribute
   \(pydantic_ai.ui.vercel_ai.request_types.ToolUIPart\)")
    | DynamicToolUIPart[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.request_types.DynamicToolUIPart "DynamicToolUIPart



      module-attribute
   \(pydantic_ai.ui.vercel_ai.request_types.DynamicToolUIPart\)")
    | SourceUrlUIPart[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.request_types.SourceUrlUIPart "SourceUrlUIPart \(pydantic_ai.ui.vercel_ai.request_types.SourceUrlUIPart\)")
    | SourceDocumentUIPart[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.request_types.SourceDocumentUIPart "SourceDocumentUIPart \(pydantic_ai.ui.vercel_ai.request_types.SourceDocumentUIPart\)")
    | FileUIPart[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.request_types.FileUIPart "FileUIPart \(pydantic_ai.ui.vercel_ai.request_types.FileUIPart\)")
    | DataUIPart[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.request_types.DataUIPart "DataUIPart \(pydantic_ai.ui.vercel_ai.request_types.DataUIPart\)")
    | StepStartUIPart[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.request_types.StepStartUIPart "StepStartUIPart \(pydantic_ai.ui.vercel_ai.request_types.StepStartUIPart\)")
)

```

Union of all message part types.
###  UIMessage
Bases: `CamelBaseModel`
A message as displayed in the UI by Vercel AI Elements.
Source code in `pydantic_ai_slim/pydantic_ai/ui/vercel_ai/request_types.py`
```
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
371
372
373
```
| ```
class UIMessage(CamelBaseModel):
    """A message as displayed in the UI by Vercel AI Elements."""

    id: str
    """A unique identifier for the message."""

    role: Literal['system', 'user', 'assistant']
    """The role of the message."""

    metadata: Any | None = None
    """The metadata of the message."""

    parts: list[UIMessagePart]
    """
    The parts of the message. Use this for rendering the message in the UI.
    System messages should be avoided (set the system prompt on the server instead).
    They can have text parts.
    User messages can have text parts and file parts.
    Assistant messages can have text, reasoning, tool invocation, and file parts.
    """

```

---|---
####  id `instance-attribute`
```
id:

```

A unique identifier for the message.
####  role `instance-attribute`
```
role: ['system', 'user', 'assistant']

```

The role of the message.
####  metadata `class-attribute` `instance-attribute`
```
metadata:  | None = None

```

The metadata of the message.
####  parts `instance-attribute`
```
parts: [UIMessagePart[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.request_types.UIMessagePart "UIMessagePart



      module-attribute
   \(pydantic_ai.ui.vercel_ai.request_types.UIMessagePart\)")]

```

The parts of the message. Use this for rendering the message in the UI. System messages should be avoided (set the system prompt on the server instead). They can have text parts. User messages can have text parts and file parts. Assistant messages can have text, reasoning, tool invocation, and file parts.
