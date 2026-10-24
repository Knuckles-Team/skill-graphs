```
445
446
447
448
449
450
451
452
453
454
455
456
457
458
459
460
461
462
463
464
465
466
467
468
469
470
471
472
```
| ```
@pydantic.with_config({'alias_generator': to_camel})
class Task(TypedDict):
    """A Task is a stateful entity that allows Clients and Remote Agents to achieve a specific outcome.

    Clients and Remote Agents exchange Messages within a Task. Remote Agents generate results as Artifacts.
    A Task is always created by a Client and the status is always determined by the Remote Agent.
    """

    id: str
    """Unique identifier for the task."""

    context_id: str
    """The context the task is associated with."""

    kind: Literal['task']
    """Event type."""

    status: TaskStatus
    """Current status of the task."""

    history: NotRequired[list[Message]]
    """Optional history of messages."""

    artifacts: NotRequired[list[Artifact]]
    """Collection of artifacts created by the agent."""

    metadata: NotRequired[dict[str, Any]]
    """Extension metadata."""

```

---|---
####  id `instance-attribute`
```
id:

```

Unique identifier for the task.
####  context_id `instance-attribute`
```
context_id:

```

The context the task is associated with.
####  kind `instance-attribute`
```
kind: ['task']

```

Event type.
####  status `instance-attribute`
```
status: TaskStatus[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.TaskStatus "TaskStatus \(fasta2a.schema.TaskStatus\)")

```

Current status of the task.
####  history `instance-attribute`
```
history: [[Message[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.Message "Message \(fasta2a.schema.Message\)")]]

```

Optional history of messages.
####  artifacts `instance-attribute`
```
artifacts: [[Artifact[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.Artifact "Artifact \(fasta2a.schema.Artifact\)")]]

```

Collection of artifacts created by the agent.
####  metadata `instance-attribute`
```
metadata: [[, ]]

```

Extension metadata.
###  TaskStatusUpdateEvent
Bases:
Sent by server during message/stream requests.
Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`
```
475
476
477
478
479
480
481
482
483
484
485
486
487
488
489
490
491
492
493
494
495
```
| ```
@pydantic.with_config({'alias_generator': to_camel})
class TaskStatusUpdateEvent(TypedDict):
    """Sent by server during message/stream requests."""

    task_id: str
    """The id of the task."""

    context_id: str
    """The context the task is associated with."""

    kind: Literal['status-update']
    """Event type."""

    status: TaskStatus
    """The status of the task."""

    final: bool
    """Indicates the end of the event stream."""

    metadata: NotRequired[dict[str, Any]]
    """Extension metadata."""

```

---|---
####  task_id `instance-attribute`
```
task_id:

```

The id of the task.
####  context_id `instance-attribute`
```
context_id:

```

The context the task is associated with.
####  kind `instance-attribute`
```
kind: ['status-update']

```

Event type.
####  status `instance-attribute`
```
status: TaskStatus[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.TaskStatus "TaskStatus \(fasta2a.schema.TaskStatus\)")

```

The status of the task.
####  final `instance-attribute`
```
final:

```

Indicates the end of the event stream.
####  metadata `instance-attribute`
```
metadata: [[, ]]

```

Extension metadata.
###  TaskArtifactUpdateEvent
Bases:
Sent by server during message/stream requests.
Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`
```
498
499
500
501
502
503
504
505
506
507
508
509
510
511
512
513
514
515
516
517
518
519
520
521
```
| ```
@pydantic.with_config({'alias_generator': to_camel})
class TaskArtifactUpdateEvent(TypedDict):
    """Sent by server during message/stream requests."""

    task_id: str
    """The id of the task."""

    context_id: str
    """The context the task is associated with."""

    kind: Literal['artifact-update']
    """Event type identification."""

    artifact: Artifact
    """The artifact that was updated."""

    append: NotRequired[bool]
    """Whether to append to existing artifact (true) or replace (false)."""

    last_chunk: NotRequired[bool]
    """Indicates this is the final chunk of the artifact."""

    metadata: NotRequired[dict[str, Any]]
    """Extension metadata."""

```

---|---
####  task_id `instance-attribute`
```
task_id:

```

The id of the task.
####  context_id `instance-attribute`
```
context_id:

```

The context the task is associated with.
####  kind `instance-attribute`
```
kind: ['artifact-update']

```

Event type identification.
####  artifact `instance-attribute`
```
artifact: Artifact[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.Artifact "Artifact \(fasta2a.schema.Artifact\)")

```

The artifact that was updated.
####  append `instance-attribute`
```
append: []

```

Whether to append to existing artifact (true) or replace (false).
####  last_chunk `instance-attribute`
```
last_chunk: []

```

Indicates this is the final chunk of the artifact.
####  metadata `instance-attribute`
```
metadata: [[, ]]

```

Extension metadata.
###  TaskIdParams
Bases:
Parameters for a task id.
Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`
```
524
525
526
527
528
529
530
531
532
```
| ```
@pydantic.with_config({'alias_generator': to_camel})
class TaskIdParams(TypedDict):
    """Parameters for a task id."""

    id: str
    """The unique identifier for the task."""

    metadata: NotRequired[dict[str, Any]]
    """Optional metadata associated with the request."""

```

---|---
####  id `instance-attribute`
```
id:

```

The unique identifier for the task.
####  metadata `instance-attribute`
```
metadata: [[, ]]

```

Optional metadata associated with the request.
###  TaskQueryParams
Bases: `TaskIdParams[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.TaskIdParams "TaskIdParams \(fasta2a.schema.TaskIdParams\)")`
Query parameters for a task.
Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`
```
535
536
537
538
539
540
```
| ```
@pydantic.with_config({'alias_generator': to_camel})
class TaskQueryParams(TaskIdParams):
    """Query parameters for a task."""

    history_length: NotRequired[int]
    """Number of recent messages to be retrieved."""

```

---|---
####  history_length `instance-attribute`
```
history_length: []

```

Number of recent messages to be retrieved.
###  MessageSendConfiguration
Bases:
Configuration for the send message request.
Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`
```
543
544
545
546
547
548
549
550
551
552
553
554
555
556
557
```
| ```
@pydantic.with_config({'alias_generator': to_camel})
class MessageSendConfiguration(TypedDict):
    """Configuration for the send message request."""

    accepted_output_modes: list[str]
    """Accepted output modalities by the client."""

    blocking: NotRequired[bool]
    """If the server should treat the client as a blocking request."""

    history_length: NotRequired[int]
    """Number of recent messages to be retrieved."""

    push_notification_config: NotRequired[PushNotificationConfig]
    """Where the server should send notifications when disconnected."""

```

---|---
####  accepted_output_modes `instance-attribute`
```
accepted_output_modes: []

```

Accepted output modalities by the client.
####  blocking `instance-attribute`
```
blocking: []

```

If the server should treat the client as a blocking request.
####  history_length `instance-attribute`
```
history_length: []

```

Number of recent messages to be retrieved.
####  push_notification_config `instance-attribute`
```
push_notification_config: [
    PushNotificationConfig[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.PushNotificationConfig "PushNotificationConfig \(fasta2a.schema.PushNotificationConfig\)")
]

```

Where the server should send notifications when disconnected.
###  MessageSendParams
Bases:
Parameters for message/send method.
Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`
```
560
561
562
563
564
565
566
567
568
569
570
571
```
| ```
@pydantic.with_config({'alias_generator': to_camel})
class MessageSendParams(TypedDict):
    """Parameters for message/send method."""

    configuration: NotRequired[MessageSendConfiguration]
    """Send message configuration."""

    message: Message
    """The message being sent to the server."""

    metadata: NotRequired[dict[str, Any]]
    """Extension metadata."""

```

---|---
####  configuration `instance-attribute`
```
configuration: [MessageSendConfiguration[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.MessageSendConfiguration "MessageSendConfiguration \(fasta2a.schema.MessageSendConfiguration\)")]

```

Send message configuration.
####  message `instance-attribute`
```
message: Message[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.Message "Message \(fasta2a.schema.Message\)")

```

The message being sent to the server.
####  metadata `instance-attribute`
```
metadata: [[, ]]

```

Extension metadata.
###  TaskSendParams
Bases:
Internal parameters for task execution within the framework.
Note: This is not part of the A2A protocol - it's used internally for broker/worker communication.
Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`
```
574
575
576
577
578
579
580
581
582
583
584
585
586
587
588
589
590
591
592
593
594
595
```
| ```
@pydantic.with_config({'alias_generator': to_camel})
class TaskSendParams(TypedDict):
    """Internal parameters for task execution within the framework.

    Note: This is not part of the A2A protocol - it's used internally
    for broker/worker communication.
    """

    id: str
    """The id of the task."""

    context_id: str
    """The context id for the task."""

    message: Message
    """The message to process."""

    history_length: NotRequired[int]
    """Number of recent messages to be retrieved."""

    metadata: NotRequired[dict[str, Any]]
    """Extension metadata."""

```

---|---
####  id `instance-attribute`
```
id:

```

The id of the task.
####  context_id `instance-attribute`
```
context_id:

```

The context id for the task.
####  message `instance-attribute`
```
message: Message[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.Message "Message \(fasta2a.schema.Message\)")

```

The message to process.
####  history_length `instance-attribute`
```
history_length: []

```

Number of recent messages to be retrieved.
####  metadata `instance-attribute`
```
metadata: [[, ]]

```

Extension metadata.
###  ListTaskPushNotificationConfigParams
Bases:
Parameters for getting list of pushNotificationConfigurations associated with a Task.
Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`
```
598
599
600
601
602
603
604
605
606
```
| ```
@pydantic.with_config({'alias_generator': to_camel})
class ListTaskPushNotificationConfigParams(TypedDict):
    """Parameters for getting list of pushNotificationConfigurations associated with a Task."""

    id: str
    """Task id."""

    metadata: NotRequired[dict[str, Any]]
    """Extension metadata."""

```

---|---
####  id `instance-attribute`
```
id:

```

Task id.
####  metadata `instance-attribute`
```
metadata: [[, ]]

```

Extension metadata.
###  DeleteTaskPushNotificationConfigParams
Bases:
Parameters for removing pushNotificationConfiguration associated with a Task.
Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`
```
609
610
611
612
613
614
615
616
617
618
619
620
```
| ```
@pydantic.with_config({'alias_generator': to_camel})
class DeleteTaskPushNotificationConfigParams(TypedDict):
    """Parameters for removing pushNotificationConfiguration associated with a Task."""

    id: str
    """Task id."""

    push_notification_config_id: str
    """The push notification config id to delete."""

    metadata: NotRequired[dict[str, Any]]
    """Extension metadata."""

```

---|---
####  id `instance-attribute`
```
id:

```

Task id.
####  push_notification_config_id `instance-attribute`
```
push_notification_config_id:

```

The push notification config id to delete.
####  metadata `instance-attribute`
```
metadata: [[, ]]

```

Extension metadata.
###  JSONRPCMessage
Bases:
A JSON RPC message.
Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`
```
623
624
625
626
627
628
629
630
```
| ```
class JSONRPCMessage(TypedDict):
    """A JSON RPC message."""

    jsonrpc: Literal['2.0']
    """The JSON RPC version."""

    id: int | str | None
    """The request id."""

```

---|---
####  jsonrpc `instance-attribute`
```
jsonrpc: ['2.0']

```

The JSON RPC version.
####  id `instance-attribute`
```
id:  |  | None

```

The request id.
###  JSONRPCRequest
Bases: `JSONRPCMessage[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.JSONRPCMessage "JSONRPCMessage \(fasta2a.schema.JSONRPCMessage\)")`, `Method, Params]`
A JSON RPC request.
Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`
```
637
638
639
640
641
642
643
644
```
| ```
class JSONRPCRequest(JSONRPCMessage, Generic[Method, Params]):
    """A JSON RPC request."""

    method: Method
    """The method to call."""

    params: Params
    """The parameters to pass to the method."""

```

---|---
####  method `instance-attribute`
```
method: Method

```

The method to call.
####  params `instance-attribute`
```
params: Params

```

The parameters to pass to the method.
###  JSONRPCError
Bases: `CodeT, MessageT]`
A JSON RPC error.
Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`
```
655
656
657
658
659
660
661
662
663
664
665
```
| ```
class JSONRPCError(TypedDict, Generic[CodeT, MessageT]):
    """A JSON RPC error."""

    code: CodeT
    """A number that indicates the error type that occurred."""

    message: MessageT
    """A string providing a short description of the error."""

    data: NotRequired[Any]
    """A primitive or structured value containing additional information about the error."""

```

---|---
####  code `instance-attribute`
```
code: CodeT

```

A number that indicates the error type that occurred.
####  message `instance-attribute`
```
message: MessageT

```

A string providing a short description of the error.
####  data `instance-attribute`
```
data: []

```

A primitive or structured value containing additional information about the error.
###  JSONRPCResponse
Bases: `JSONRPCMessage[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.JSONRPCMessage "JSONRPCMessage \(fasta2a.schema.JSONRPCMessage\)")`, `ResultT, ErrorT]`
A JSON RPC response.
Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`
```
672
673
674
675
676
```
| ```
class JSONRPCResponse(JSONRPCMessage, Generic[ResultT, ErrorT]):
    """A JSON RPC response."""

    result: NotRequired[ResultT]
    error: NotRequired[ErrorT]

```

---|---
###  JSONParseError `module-attribute`
```
JSONParseError = JSONRPCError[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.JSONRPCError "JSONRPCError \(fasta2a.schema.JSONRPCError\)")[
    [-32700], ["Invalid JSON payload"]
]

```

A JSON RPC error for a parse error.
###  InvalidRequestError `module-attribute`
```
InvalidRequestError = JSONRPCError[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.JSONRPCError "JSONRPCError \(fasta2a.schema.JSONRPCError\)")[
    [-32600],
    ["Request payload validation error"],
]

```

A JSON RPC error for an invalid request.
###  MethodNotFoundError `module-attribute`
```
MethodNotFoundError = JSONRPCError[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.JSONRPCError "JSONRPCError \(fasta2a.schema.JSONRPCError\)")[
    [-32601], ["Method not found"]
]

```

A JSON RPC error for a method not found.
###  InvalidParamsError `module-attribute`
```
InvalidParamsError = JSONRPCError[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.JSONRPCError "JSONRPCError \(fasta2a.schema.JSONRPCError\)")[
    [-32602], ["Invalid parameters"]
]

```

A JSON RPC error for invalid parameters.
###  InternalError `module-attribute`
```
InternalError = JSONRPCError[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.JSONRPCError "JSONRPCError \(fasta2a.schema.JSONRPCError\)")[
    [-32603], ["Internal error"]
]

```

A JSON RPC error for an internal error.
###  TaskNotFoundError `module-attribute`
```
TaskNotFoundError = JSONRPCError[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.JSONRPCError "JSONRPCError \(fasta2a.schema.JSONRPCError\)")[
    [-32001], ["Task not found"]
]

```

A JSON RPC error for a task not found.
###  TaskNotCancelableError `module-attribute`
```
TaskNotCancelableError = JSONRPCError[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.JSONRPCError "JSONRPCError \(fasta2a.schema.JSONRPCError\)")[
    [-32002], ["Task not cancelable"]
]

```

A JSON RPC error for a task not cancelable.
###  PushNotificationNotSupportedError `module-attribute`
```
PushNotificationNotSupportedError = JSONRPCError[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.JSONRPCError "JSONRPCError \(fasta2a.schema.JSONRPCError\)")[
    [-32003],
    ["Push notification not supported"],
]

```

A JSON RPC error for a push notification not supported.
###  UnsupportedOperationError `module-attribute`
```
UnsupportedOperationError = JSONRPCError[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.JSONRPCError "JSONRPCError \(fasta2a.schema.JSONRPCError\)")[
    [-32004],
    ["This operation is not supported"],
]

```

A JSON RPC error for an unsupported operation.
###  ContentTypeNotSupportedError `module-attribute`
```
ContentTypeNotSupportedError = JSONRPCError[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.JSONRPCError "JSONRPCError \(fasta2a.schema.JSONRPCError\)")[
    [-32005], ["Incompatible content types"]
]

```

A JSON RPC error for incompatible content types.
###  InvalidAgentResponseError `module-attribute`
```
InvalidAgentResponseError = JSONRPCError[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.JSONRPCError "JSONRPCError \(fasta2a.schema.JSONRPCError\)")[
    [-32006], ["Invalid agent response"]
]

```

A JSON RPC error for invalid agent response.
###  SendMessageRequest `module-attribute`
```
SendMessageRequest = JSONRPCRequest[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.JSONRPCRequest "JSONRPCRequest \(fasta2a.schema.JSONRPCRequest\)")[
    ["message/send"], MessageSendParams[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.MessageSendParams "MessageSendParams \(fasta2a.schema.MessageSendParams\)")
]

```

A JSON RPC request to send a message.
###  SendMessageResponse `module-attribute`
```
SendMessageResponse = JSONRPCResponse[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.JSONRPCResponse "JSONRPCResponse \(fasta2a.schema.JSONRPCResponse\)")[
    [Task[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.Task "Task \(fasta2a.schema.Task\)"), Message[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.Message "Message \(fasta2a.schema.Message\)")], JSONRPCError[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.JSONRPCError "JSONRPCError \(fasta2a.schema.JSONRPCError\)")[, ]
]

```

A JSON RPC response to send a message.
###  StreamMessageRequest `module-attribute`
```
StreamMessageRequest = JSONRPCRequest[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.JSONRPCRequest "JSONRPCRequest \(fasta2a.schema.JSONRPCRequest\)")[
    ["message/stream"], MessageSendParams[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.MessageSendParams "MessageSendParams \(fasta2a.schema.MessageSendParams\)")
]

```

A JSON RPC request to stream a message.
###  StreamMessageResponse `module-attribute`
```
StreamMessageResponse = JSONRPCResponse[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.JSONRPCResponse "JSONRPCResponse \(fasta2a.schema.JSONRPCResponse\)")[
    [
        Task[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.Task "Task \(fasta2a.schema.Task\)"),
        Message[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.Message "Message \(fasta2a.schema.Message\)"),
        TaskStatusUpdateEvent[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.TaskStatusUpdateEvent "TaskStatusUpdateEvent \(fasta2a.schema.TaskStatusUpdateEvent\)"),
        TaskArtifactUpdateEvent[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.TaskArtifactUpdateEvent "TaskArtifactUpdateEvent \(fasta2a.schema.TaskArtifactUpdateEvent\)"),
    ],
    JSONRPCError[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.JSONRPCError "JSONRPCError \(fasta2a.schema.JSONRPCError\)")[, ],
]

```

A JSON RPC response to a StreamMessageRequest.
###  GetTaskRequest `module-attribute`
```
GetTaskRequest = JSONRPCRequest[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.JSONRPCRequest "JSONRPCRequest \(fasta2a.schema.JSONRPCRequest\)")[
    ["tasks/get"], TaskQueryParams[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.TaskQueryParams "TaskQueryParams \(fasta2a.schema.TaskQueryParams\)")
]

```

A JSON RPC request to get a task.
###  GetTaskResponse `module-attribute`
```
GetTaskResponse = JSONRPCResponse[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.JSONRPCResponse "JSONRPCResponse \(fasta2a.schema.JSONRPCResponse\)")[Task[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.Task "Task \(fasta2a.schema.Task\)"), TaskNotFoundError[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.TaskNotFoundError "TaskNotFoundError



      module-attribute
   \(fasta2a.schema.TaskNotFoundError\)")]

```

A JSON RPC response to get a task.
###  CancelTaskRequest `module-attribute`
```
CancelTaskRequest = JSONRPCRequest[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.JSONRPCRequest "JSONRPCRequest \(fasta2a.schema.JSONRPCRequest\)")[
    ["tasks/cancel"], TaskIdParams[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.TaskIdParams "TaskIdParams \(fasta2a.schema.TaskIdParams\)")
]

```

A JSON RPC request to cancel a task.
###  CancelTaskResponse `module-attribute`
```
CancelTaskResponse = JSONRPCResponse[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.JSONRPCResponse "JSONRPCResponse \(fasta2a.schema.JSONRPCResponse\)")[
    Task[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.Task "Task \(fasta2a.schema.Task\)"), [TaskNotCancelableError[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.TaskNotCancelableError "TaskNotCancelableError



      module-attribute
   \(fasta2a.schema.TaskNotCancelableError\)"), TaskNotFoundError[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.TaskNotFoundError "TaskNotFoundError



      module-attribute
   \(fasta2a.schema.TaskNotFoundError\)")]
]

```

A JSON RPC response to cancel a task.
###  SetTaskPushNotificationRequest `module-attribute`
```
SetTaskPushNotificationRequest = JSONRPCRequest[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.JSONRPCRequest "JSONRPCRequest \(fasta2a.schema.JSONRPCRequest\)")[
    ["tasks/pushNotification/set"],
    TaskPushNotificationConfig[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.TaskPushNotificationConfig "TaskPushNotificationConfig \(fasta2a.schema.TaskPushNotificationConfig\)"),
]

```

A JSON RPC request to set a task push notification.
###  SetTaskPushNotificationResponse `module-attribute`
```
SetTaskPushNotificationResponse = JSONRPCResponse[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.JSONRPCResponse "JSONRPCResponse \(fasta2a.schema.JSONRPCResponse\)")[
    TaskPushNotificationConfig[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.TaskPushNotificationConfig "TaskPushNotificationConfig \(fasta2a.schema.TaskPushNotificationConfig\)"),
    PushNotificationNotSupportedError[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.PushNotificationNotSupportedError "PushNotificationNotSupportedError



      module-attribute
   \(fasta2a.schema.PushNotificationNotSupportedError\)"),
]

```

A JSON RPC response to set a task push notification.
###  GetTaskPushNotificationRequest `module-attribute`
```
GetTaskPushNotificationRequest = JSONRPCRequest[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.JSONRPCRequest "JSONRPCRequest \(fasta2a.schema.JSONRPCRequest\)")[
    ["tasks/pushNotification/get"], TaskIdParams[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.TaskIdParams "TaskIdParams \(fasta2a.schema.TaskIdParams\)")
]

```

A JSON RPC request to get a task push notification.
###  GetTaskPushNotificationResponse `module-attribute`
```
GetTaskPushNotificationResponse = JSONRPCResponse[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.JSONRPCResponse "JSONRPCResponse \(fasta2a.schema.JSONRPCResponse\)")[
    TaskPushNotificationConfig[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.TaskPushNotificationConfig "TaskPushNotificationConfig \(fasta2a.schema.TaskPushNotificationConfig\)"),
    PushNotificationNotSupportedError[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.PushNotificationNotSupportedError "PushNotificationNotSupportedError



      module-attribute
   \(fasta2a.schema.PushNotificationNotSupportedError\)"),
]

```

A JSON RPC response to get a task push notification.
###  ResubscribeTaskRequest `module-attribute`
```
ResubscribeTaskRequest = JSONRPCRequest[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.JSONRPCRequest "JSONRPCRequest \(fasta2a.schema.JSONRPCRequest\)")[
    ["tasks/resubscribe"], TaskIdParams[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.TaskIdParams "TaskIdParams \(fasta2a.schema.TaskIdParams\)")
]

```

A JSON RPC request to resubscribe to a task.
###  ListTaskPushNotificationConfigRequest `module-attribute`
