Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`
```
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
```
| ```
@pydantic.with_config({'alias_generator': to_camel})
class HttpSecurityScheme(TypedDict):
    """HTTP security scheme."""

    type: Literal['http']
    """The type of the security scheme. Must be 'http'."""

    scheme: str
    """The name of the HTTP Authorization scheme."""

    bearer_format: NotRequired[str]
    """A hint to the client to identify how the bearer token is formatted."""

    description: NotRequired[str]
    """Description of this security scheme."""

```

---|---
####  type `instance-attribute`
```
type: ['http']

```

The type of the security scheme. Must be 'http'.
####  scheme `instance-attribute`
```
scheme:

```

The name of the HTTP Authorization scheme.
####  bearer_format `instance-attribute`
```
bearer_format: []

```

A hint to the client to identify how the bearer token is formatted.
####  description `instance-attribute`
```
description: []

```

Description of this security scheme.
###  ApiKeySecurityScheme
Bases:
API Key security scheme.
Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`
```
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
```
| ```
@pydantic.with_config({'alias_generator': to_camel})
class ApiKeySecurityScheme(TypedDict):
    """API Key security scheme."""

    type: Literal['apiKey']
    """The type of the security scheme. Must be 'apiKey'."""

    name: str
    """The name of the header, query or cookie parameter to be used."""

    in_: Literal['query', 'header', 'cookie']
    """The location of the API key."""

    description: NotRequired[str]
    """Description of this security scheme."""

```

---|---
####  type `instance-attribute`
```
type: ['apiKey']

```

The type of the security scheme. Must be 'apiKey'.
####  name `instance-attribute`
```
name:

```

The name of the header, query or cookie parameter to be used.
####  in_ `instance-attribute`
```
in_: ['query', 'header', 'cookie']

```

The location of the API key.
####  description `instance-attribute`
```
description: []

```

Description of this security scheme.
###  OAuth2SecurityScheme
Bases:
OAuth2 security scheme.
Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`
```
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
```
| ```
@pydantic.with_config({'alias_generator': to_camel})
class OAuth2SecurityScheme(TypedDict):
    """OAuth2 security scheme."""

    type: Literal['oauth2']
    """The type of the security scheme. Must be 'oauth2'."""

    flows: dict[str, Any]
    """An object containing configuration information for the flow types supported."""

    description: NotRequired[str]
    """Description of this security scheme."""

```

---|---
####  type `instance-attribute`
```
type: ['oauth2']

```

The type of the security scheme. Must be 'oauth2'.
####  flows `instance-attribute`
```
flows: [, ]

```

An object containing configuration information for the flow types supported.
####  description `instance-attribute`
```
description: []

```

Description of this security scheme.
###  OpenIdConnectSecurityScheme
Bases:
OpenID Connect security scheme.
Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`
```
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
```
| ```
@pydantic.with_config({'alias_generator': to_camel})
class OpenIdConnectSecurityScheme(TypedDict):
    """OpenID Connect security scheme."""

    type: Literal['openIdConnect']
    """The type of the security scheme. Must be 'openIdConnect'."""

    open_id_connect_url: str
    """OpenId Connect URL to discover OAuth2 configuration values."""

    description: NotRequired[str]
    """Description of this security scheme."""

```

---|---
####  type `instance-attribute`
```
type: ['openIdConnect']

```

The type of the security scheme. Must be 'openIdConnect'.
####  open_id_connect_url `instance-attribute`
```
open_id_connect_url:

```

OpenId Connect URL to discover OAuth2 configuration values.
####  description `instance-attribute`
```
description: []

```

Description of this security scheme.
###  SecurityScheme `module-attribute`
```
SecurityScheme = [
    [
        HttpSecurityScheme[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.HttpSecurityScheme "HttpSecurityScheme \(fasta2a.schema.HttpSecurityScheme\)"),
        ApiKeySecurityScheme[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.ApiKeySecurityScheme "ApiKeySecurityScheme \(fasta2a.schema.ApiKeySecurityScheme\)"),
        OAuth2SecurityScheme[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.OAuth2SecurityScheme "OAuth2SecurityScheme \(fasta2a.schema.OAuth2SecurityScheme\)"),
        OpenIdConnectSecurityScheme[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.OpenIdConnectSecurityScheme "OpenIdConnectSecurityScheme \(fasta2a.schema.OpenIdConnectSecurityScheme\)"),
    ],
    Field[](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field "pydantic.Field")(discriminator="type"),
]

```

A security scheme for authentication.
###  AgentInterface
Bases:
An interface that the agent supports.
Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`
```
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
```
| ```
@pydantic.with_config({'alias_generator': to_camel})
class AgentInterface(TypedDict):
    """An interface that the agent supports."""

    transport: str
    """The transport protocol (e.g., 'jsonrpc', 'websocket')."""

    url: str
    """The URL endpoint for this transport."""

    description: NotRequired[str]
    """Description of this interface."""

```

---|---
####  transport `instance-attribute`
```
transport:

```

The transport protocol (e.g., 'jsonrpc', 'websocket').
####  url `instance-attribute`
```
url:

```

The URL endpoint for this transport.
####  description `instance-attribute`
```
description: []

```

Description of this interface.
###  AgentExtension
Bases:
A declaration of an extension supported by an Agent.
Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`
```
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
```
| ```
@pydantic.with_config({'alias_generator': to_camel})
class AgentExtension(TypedDict):
    """A declaration of an extension supported by an Agent."""

    uri: str
    """The URI of the extension."""

    description: NotRequired[str]
    """A description of how this agent uses this extension."""

    required: NotRequired[bool]
    """Whether the client must follow specific requirements of the extension."""

    params: NotRequired[dict[str, Any]]
    """Optional configuration for the extension."""

```

---|---
####  uri `instance-attribute`
```
uri:

```

The URI of the extension.
####  description `instance-attribute`
```
description: []

```

A description of how this agent uses this extension.
####  required `instance-attribute`
```
required: []

```

Whether the client must follow specific requirements of the extension.
####  params `instance-attribute`
```
params: [[, ]]

```

Optional configuration for the extension.
###  Skill
Bases:
Skills are a unit of capability that an agent can perform.
Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`
```
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
```
| ```
@pydantic.with_config({'alias_generator': to_camel})
class Skill(TypedDict):
    """Skills are a unit of capability that an agent can perform."""

    id: str
    """A unique identifier for the skill."""

    name: str
    """Human readable name of the skill."""

    description: str
    """A human-readable description of the skill.

    It will be used by the client or a human as a hint to understand the skill.
    """

    tags: list[str]
    """Set of tag-words describing classes of capabilities for this specific skill.

    Examples: "cooking", "customer support", "billing".
    """

    examples: NotRequired[list[str]]
    """The set of example scenarios that the skill can perform.

    Will be used by the client as a hint to understand how the skill can be used. (e.g. "I need a recipe for bread")
    """

    input_modes: list[str]
    """Supported mime types for input data."""

    output_modes: list[str]
    """Supported mime types for output data."""

```

---|---
####  id `instance-attribute`
```
id:

```

A unique identifier for the skill.
####  name `instance-attribute`
```
name:

```

Human readable name of the skill.
####  description `instance-attribute`
```
description:

```

A human-readable description of the skill.
It will be used by the client or a human as a hint to understand the skill.
####  tags `instance-attribute`
```
tags: []

```

Set of tag-words describing classes of capabilities for this specific skill.
Examples: "cooking", "customer support", "billing".
####  examples `instance-attribute`
```
examples: [[]]

```

The set of example scenarios that the skill can perform.
Will be used by the client as a hint to understand how the skill can be used. (e.g. "I need a recipe for bread")
####  input_modes `instance-attribute`
```
input_modes: []

```

Supported mime types for input data.
####  output_modes `instance-attribute`
```
output_modes: []

```

Supported mime types for output data.
###  Artifact
Bases:
Agents generate Artifacts as an end result of a Task.
Artifacts are immutable, can be named, and can have multiple parts. A streaming response can append parts to existing Artifacts.
A single Task can generate many Artifacts. For example, "create a webpage" could create separate HTML and image Artifacts.
Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`
```
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
```
| ```
@pydantic.with_config({'alias_generator': to_camel})
class Artifact(TypedDict):
    """Agents generate Artifacts as an end result of a Task.

    Artifacts are immutable, can be named, and can have multiple parts. A streaming response can append parts to
    existing Artifacts.

    A single Task can generate many Artifacts. For example, "create a webpage" could create separate HTML and image
    Artifacts.
    """

    artifact_id: str
    """Unique identifier for the artifact."""

    name: NotRequired[str]
    """The name of the artifact."""

    description: NotRequired[str]
    """A description of the artifact."""

    parts: list[Part]
    """The parts that make up the artifact."""

    metadata: NotRequired[dict[str, Any]]
    """Metadata about the artifact."""

    extensions: NotRequired[list[str]]
    """Array of extensions."""

    append: NotRequired[bool]
    """Whether to append this artifact to an existing one."""

    last_chunk: NotRequired[bool]
    """Whether this is the last chunk of the artifact."""

```

---|---
####  artifact_id `instance-attribute`
```
artifact_id:

```

Unique identifier for the artifact.
####  name `instance-attribute`
```
name: []

```

The name of the artifact.
####  description `instance-attribute`
```
description: []

```

A description of the artifact.
####  parts `instance-attribute`
```
parts: [Part[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.Part "Part



      module-attribute
   \(fasta2a.schema.Part\)")]

```

The parts that make up the artifact.
####  metadata `instance-attribute`
```
metadata: [[, ]]

```

Metadata about the artifact.
####  extensions `instance-attribute`
```
extensions: [[]]

```

Array of extensions.
####  append `instance-attribute`
```
append: []

```

Whether to append this artifact to an existing one.
####  last_chunk `instance-attribute`
```
last_chunk: []

```

Whether this is the last chunk of the artifact.
###  PushNotificationConfig
Bases:
Configuration for push notifications.
A2A supports a secure notification mechanism whereby an agent can notify a client of an update outside a connected session via a PushNotificationService. Within and across enterprises, it is critical that the agent verifies the identity of the notification service, authenticates itself with the service, and presents an identifier that ties the notification to the executing Task.
The target server of the PushNotificationService should be considered a separate service, and is not guaranteed (or even expected) to be the client directly. This PushNotificationService is responsible for authenticating and authorizing the agent and for proxying the verified notification to the appropriate endpoint (which could be anything from a pub/sub queue, to an email inbox or other service, etc.).
For contrived scenarios with isolated client-agent pairs (e.g. local service mesh in a contained VPC, etc.) or isolated environments without enterprise security concerns, the client may choose to simply open a port and act as its own PushNotificationService. Any enterprise implementation will likely have a centralized service that authenticates the remote agents with trusted notification credentials and can handle online/offline scenarios. (This should be thought of similarly to a mobile Push Notification Service).
Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`
```
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
287
288
289
290
291
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
302
```
| ```
@pydantic.with_config({'alias_generator': to_camel})
class PushNotificationConfig(TypedDict):
    """Configuration for push notifications.

    A2A supports a secure notification mechanism whereby an agent can notify a client of an update
    outside a connected session via a PushNotificationService. Within and across enterprises,
    it is critical that the agent verifies the identity of the notification service, authenticates
    itself with the service, and presents an identifier that ties the notification to the executing
    Task.

    The target server of the PushNotificationService should be considered a separate service, and
    is not guaranteed (or even expected) to be the client directly. This PushNotificationService is
    responsible for authenticating and authorizing the agent and for proxying the verified notification
    to the appropriate endpoint (which could be anything from a pub/sub queue, to an email inbox or
    other service, etc.).

    For contrived scenarios with isolated client-agent pairs (e.g. local service mesh in a contained
    VPC, etc.) or isolated environments without enterprise security concerns, the client may choose to
    simply open a port and act as its own PushNotificationService. Any enterprise implementation will
    likely have a centralized service that authenticates the remote agents with trusted notification
    credentials and can handle online/offline scenarios. (This should be thought of similarly to a
    mobile Push Notification Service).
    """

    id: NotRequired[str]
    """Server-assigned identifier."""

    url: str
    """The URL to send push notifications to."""

    token: NotRequired[str]
    """Token unique to this task/session."""

    authentication: NotRequired[SecurityScheme]
    """Authentication details for push notifications."""

```

---|---
####  id `instance-attribute`
```
id: []

```

Server-assigned identifier.
####  url `instance-attribute`
```
url:

```

The URL to send push notifications to.
####  token `instance-attribute`
```
token: []

```

Token unique to this task/session.
####  authentication `instance-attribute`
```
authentication: [SecurityScheme[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.SecurityScheme "SecurityScheme



      module-attribute
   \(fasta2a.schema.SecurityScheme\)")]

```

Authentication details for push notifications.
###  TaskPushNotificationConfig
Bases:
Configuration for task push notifications.
Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`
```
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
@pydantic.with_config({'alias_generator': to_camel})
class TaskPushNotificationConfig(TypedDict):
    """Configuration for task push notifications."""

    id: str
    """The task id."""

    push_notification_config: PushNotificationConfig
    """The push notification configuration."""

```

---|---
####  id `instance-attribute`
```
id:

```

The task id.
####  push_notification_config `instance-attribute`
```
push_notification_config: PushNotificationConfig[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.PushNotificationConfig "PushNotificationConfig \(fasta2a.schema.PushNotificationConfig\)")

```

The push notification configuration.
###  Message
Bases:
A Message contains any content that is not an Artifact.
This can include things like agent thoughts, user context, instructions, errors, status, or metadata.
All content from a client comes in the form of a Message. Agents send Messages to communicate status or to provide instructions (whereas generated results are sent as Artifacts).
A Message can have multiple parts to denote different pieces of content. For example, a user request could include a textual description from a user and then multiple files used as context from the client.
Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`
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
326
327
328
329
330
331
332
333
334
335
336
337
338
339
340
341
342
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
```
| ```
@pydantic.with_config({'alias_generator': to_camel})
class Message(TypedDict):
    """A Message contains any content that is not an Artifact.

    This can include things like agent thoughts, user context, instructions, errors, status, or metadata.

    All content from a client comes in the form of a Message. Agents send Messages to communicate status or to provide
    instructions (whereas generated results are sent as Artifacts).

    A Message can have multiple parts to denote different pieces of content. For example, a user request could include
    a textual description from a user and then multiple files used as context from the client.
    """

    role: Literal['user', 'agent']
    """The role of the message."""

    parts: list[Part]
    """The parts of the message."""

    kind: Literal['message']
    """Event type."""

    metadata: NotRequired[dict[str, Any]]
    """Metadata about the message."""

    # Additional fields
    message_id: str
    """Identifier created by the message creator."""

    context_id: NotRequired[str]
    """The context the message is associated with."""

    task_id: NotRequired[str]
    """Identifier of task the message is related to."""

    reference_task_ids: NotRequired[list[str]]
    """Array of task IDs this message references."""

    extensions: NotRequired[list[str]]
    """Array of extensions."""

```

---|---
####  role `instance-attribute`
```
role: ['user', 'agent']

```

The role of the message.
####  parts `instance-attribute`
```
parts: [Part[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.Part "Part



      module-attribute
   \(fasta2a.schema.Part\)")]

```

The parts of the message.
####  kind `instance-attribute`
```
kind: ['message']

```

Event type.
####  metadata `instance-attribute`
```
metadata: [[, ]]

```

Metadata about the message.
####  message_id `instance-attribute`
```
message_id:

```

Identifier created by the message creator.
####  context_id `instance-attribute`
```
context_id: []

```

The context the message is associated with.
####  task_id `instance-attribute`
```
task_id: []

```

Identifier of task the message is related to.
####  reference_task_ids `instance-attribute`
```
reference_task_ids: [[]]

```

Array of task IDs this message references.
####  extensions `instance-attribute`
```
extensions: [[]]

```

Array of extensions.
###  TextPart
Bases: `_BasePart`
A part that contains text.
Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`
```
364
365
366
367
368
369
370
371
372
```
| ```
@pydantic.with_config({'alias_generator': to_camel})
class TextPart(_BasePart):
    """A part that contains text."""

    kind: Literal['text']
    """The kind of the part."""

    text: str
    """The text of the part."""

```

---|---
####  kind `instance-attribute`
```
kind: ['text']

```

The kind of the part.
####  text `instance-attribute`
```
text:

```

The text of the part.
###  FileWithBytes
Bases:
File with base64 encoded data.
Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`
```
375
376
377
378
379
380
381
382
383
```
| ```
@pydantic.with_config({'alias_generator': to_camel})
class FileWithBytes(TypedDict):
    """File with base64 encoded data."""

    bytes: str
    """The base64 encoded content of the file."""

    mime_type: NotRequired[str]
    """Optional mime type for the file."""

```

---|---
####  bytes `instance-attribute`
```
bytes:

```

The base64 encoded content of the file.
####  mime_type `instance-attribute`
```
mime_type: []

```

Optional mime type for the file.
###  FileWithUri
Bases:
File with URI reference.
Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`
```
386
387
388
389
390
391
392
393
394
```
| ```
@pydantic.with_config({'alias_generator': to_camel})
class FileWithUri(TypedDict):
    """File with URI reference."""

    uri: str
    """The URI of the file."""

    mime_type: NotRequired[str]
    """The mime type of the file."""

```

---|---
####  uri `instance-attribute`
```
uri:

```

The URI of the file.
####  mime_type `instance-attribute`
```
mime_type: []

```

The mime type of the file.
###  FilePart
Bases: `_BasePart`
A part that contains a file.
Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`
```
397
398
399
400
401
402
403
404
405
```
| ```
@pydantic.with_config({'alias_generator': to_camel})
class FilePart(_BasePart):
    """A part that contains a file."""

    kind: Literal['file']
    """The kind of the part."""

    file: FileWithBytes | FileWithUri
    """The file content - either bytes or URI."""

```

---|---
####  kind `instance-attribute`
```
kind: ['file']

```

The kind of the part.
####  file `instance-attribute`
```
file: FileWithBytes[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.FileWithBytes "FileWithBytes \(fasta2a.schema.FileWithBytes\)") | FileWithUri[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.FileWithUri "FileWithUri \(fasta2a.schema.FileWithUri\)")

```

The file content - either bytes or URI.
###  DataPart
Bases: `_BasePart`
A part that contains structured data.
Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`
```
408
409
410
411
412
413
414
415
416
```
| ```
@pydantic.with_config({'alias_generator': to_camel})
class DataPart(_BasePart):
    """A part that contains structured data."""

    kind: Literal['data']
    """The kind of the part."""

    data: dict[str, Any]
    """The data of the part."""

```

---|---
####  kind `instance-attribute`
```
kind: ['data']

```

The kind of the part.
####  data `instance-attribute`
```
data: [, ]

```

The data of the part.
###  Part `module-attribute`
```
Part = [
    [TextPart[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.TextPart "TextPart \(fasta2a.schema.TextPart\)"), FilePart[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.FilePart "FilePart \(fasta2a.schema.FilePart\)"), DataPart[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.DataPart "DataPart \(fasta2a.schema.DataPart\)")],
    Field[](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field "pydantic.Field")(discriminator="kind"),
]

```

A fully formed piece of content exchanged between a client and a remote agent as part of a Message or an Artifact.
Each Part has its own content type and metadata.
###  TaskState `module-attribute`
```
TaskState:  = [
    "submitted",
    "working",
    "input-required",
    "completed",
    "canceled",
    "failed",
    "rejected",
    "auth-required",
    "unknown",
]

```

The possible states of a task.
###  TaskStatus
Bases:
Status and accompanying message for a task.
Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`
```
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
```
| ```
@pydantic.with_config({'alias_generator': to_camel})
class TaskStatus(TypedDict):
    """Status and accompanying message for a task."""

    state: TaskState
    """The current state of the task."""

    message: NotRequired[Message]
    """Additional status updates for client."""

    timestamp: NotRequired[str]
    """ISO datetime value of when the status was updated."""

```

---|---
####  state `instance-attribute`
```
state: TaskState[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.TaskState "TaskState



      module-attribute
   \(fasta2a.schema.TaskState\)")

```

The current state of the task.
####  message `instance-attribute`
```
message: [Message[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.Message "Message \(fasta2a.schema.Message\)")]

```

Additional status updates for client.
####  timestamp `instance-attribute`
```
timestamp: []

```

ISO datetime value of when the status was updated.
###  Task
Bases:
A Task is a stateful entity that allows Clients and Remote Agents to achieve a specific outcome.
Clients and Remote Agents exchange Messages within a Task. Remote Agents generate results as Artifacts. A Task is always created by a Client and the status is always determined by the Remote Agent.
Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`
