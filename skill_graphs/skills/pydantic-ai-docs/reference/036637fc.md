```
ListTaskPushNotificationConfigRequest = JSONRPCRequest[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.JSONRPCRequest "JSONRPCRequest \(fasta2a.schema.JSONRPCRequest\)")[
    ["tasks/pushNotificationConfig/list"],
    ListTaskPushNotificationConfigParams[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.ListTaskPushNotificationConfigParams "ListTaskPushNotificationConfigParams \(fasta2a.schema.ListTaskPushNotificationConfigParams\)"),
]

```

A JSON RPC request to list task push notification configs.
###  DeleteTaskPushNotificationConfigRequest `module-attribute`
```
DeleteTaskPushNotificationConfigRequest = JSONRPCRequest[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.JSONRPCRequest "JSONRPCRequest \(fasta2a.schema.JSONRPCRequest\)")[
    ["tasks/pushNotificationConfig/delete"],
    DeleteTaskPushNotificationConfigParams[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.DeleteTaskPushNotificationConfigParams "DeleteTaskPushNotificationConfigParams \(fasta2a.schema.DeleteTaskPushNotificationConfigParams\)"),
]

```

A JSON RPC request to delete a task push notification config.
###  A2ARequest `module-attribute`
```
A2ARequest = [
    [
        SendMessageRequest[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.SendMessageRequest "SendMessageRequest



      module-attribute
   \(fasta2a.schema.SendMessageRequest\)"),
        StreamMessageRequest[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.StreamMessageRequest "StreamMessageRequest



      module-attribute
   \(fasta2a.schema.StreamMessageRequest\)"),
        GetTaskRequest[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.GetTaskRequest "GetTaskRequest



      module-attribute
   \(fasta2a.schema.GetTaskRequest\)"),
        CancelTaskRequest[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.CancelTaskRequest "CancelTaskRequest



      module-attribute
   \(fasta2a.schema.CancelTaskRequest\)"),
        SetTaskPushNotificationRequest[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.SetTaskPushNotificationRequest "SetTaskPushNotificationRequest



      module-attribute
   \(fasta2a.schema.SetTaskPushNotificationRequest\)"),
        GetTaskPushNotificationRequest[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.GetTaskPushNotificationRequest "GetTaskPushNotificationRequest



      module-attribute
   \(fasta2a.schema.GetTaskPushNotificationRequest\)"),
        ResubscribeTaskRequest[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.ResubscribeTaskRequest "ResubscribeTaskRequest



      module-attribute
   \(fasta2a.schema.ResubscribeTaskRequest\)"),
        ListTaskPushNotificationConfigRequest[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.ListTaskPushNotificationConfigRequest "ListTaskPushNotificationConfigRequest



      module-attribute
   \(fasta2a.schema.ListTaskPushNotificationConfigRequest\)"),
        DeleteTaskPushNotificationConfigRequest[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.DeleteTaskPushNotificationConfigRequest "DeleteTaskPushNotificationConfigRequest



      module-attribute
   \(fasta2a.schema.DeleteTaskPushNotificationConfigRequest\)"),
    ],
    Discriminator[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Discriminator "pydantic.Discriminator")("method"),
]

```

A JSON RPC request to the A2A server.
###  A2AResponse `module-attribute`
```
A2AResponse:  = [
    SendMessageResponse[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.SendMessageResponse "SendMessageResponse



      module-attribute
   \(fasta2a.schema.SendMessageResponse\)"),
    StreamMessageResponse[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.StreamMessageResponse "StreamMessageResponse



      module-attribute
   \(fasta2a.schema.StreamMessageResponse\)"),
    GetTaskResponse[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.GetTaskResponse "GetTaskResponse



      module-attribute
   \(fasta2a.schema.GetTaskResponse\)"),
    CancelTaskResponse[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.CancelTaskResponse "CancelTaskResponse



      module-attribute
   \(fasta2a.schema.CancelTaskResponse\)"),
    SetTaskPushNotificationResponse[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.SetTaskPushNotificationResponse "SetTaskPushNotificationResponse



      module-attribute
   \(fasta2a.schema.SetTaskPushNotificationResponse\)"),
    GetTaskPushNotificationResponse[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.GetTaskPushNotificationResponse "GetTaskPushNotificationResponse



      module-attribute
   \(fasta2a.schema.GetTaskPushNotificationResponse\)"),
]

```

A JSON RPC response from the A2A server.
###  A2AClient
A client for the A2A protocol.
Source code in `.venv/lib/python3.12/site-packages/fasta2a/client.py`
```
31
32
33
34
35
36
37
38
39
40
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
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
```
| ```
class A2AClient:
    """A client for the A2A protocol."""

    def __init__(self, base_url: str = 'http://localhost:8000', http_client: httpx.AsyncClient | None = None) -> None:
        if http_client is None:
            self.http_client = httpx.AsyncClient(base_url=base_url)
        else:
            self.http_client = http_client
            self.http_client.base_url = base_url

    async def send_message(
        self,
        message: Message,
        *,
        metadata: dict[str, Any] | None = None,
        configuration: MessageSendConfiguration | None = None,
    ) -> SendMessageResponse:
        """Send a message using the A2A protocol.

        Returns a JSON-RPC response containing either a result (Task) or an error.
        """
        params = MessageSendParams(message=message)
        if metadata is not None:
            params['metadata'] = metadata
        if configuration is not None:
            params['configuration'] = configuration

        request_id = str(uuid.uuid4())
        payload = SendMessageRequest(jsonrpc='2.0', id=request_id, method='message/send', params=params)
        content = send_message_request_ta.dump_json(payload, by_alias=True)
        response = await self.http_client.post('/', content=content, headers={'Content-Type': 'application/json'})
        self._raise_for_status(response)

        return send_message_response_ta.validate_json(response.content)

    async def get_task(self, task_id: str) -> GetTaskResponse:
        payload = GetTaskRequest(jsonrpc='2.0', id=None, method='tasks/get', params={'id': task_id})
        content = a2a_request_ta.dump_json(payload, by_alias=True)
        response = await self.http_client.post('/', content=content, headers={'Content-Type': 'application/json'})
        self._raise_for_status(response)
        return get_task_response_ta.validate_json(response.content)

    def _raise_for_status(self, response: httpx.Response) -> None:
        if response.status_code >= 400:
            raise UnexpectedResponseError(response.status_code, response.text)

```

---|---
####  send_message `async`
```
send_message(
    message: Message[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.Message "Message \(fasta2a.schema.Message\)"),
    *,
    metadata: [, ] | None = None,
    configuration: MessageSendConfiguration[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.MessageSendConfiguration "MessageSendConfiguration \(fasta2a.schema.MessageSendConfiguration\)") | None = None
) -> SendMessageResponse[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.SendMessageResponse "SendMessageResponse



      module-attribute
   \(fasta2a.schema.SendMessageResponse\)")

```

Send a message using the A2A protocol.
Returns a JSON-RPC response containing either a result (Task) or an error.
Source code in `.venv/lib/python3.12/site-packages/fasta2a/client.py`
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
54
55
56
57
58
59
60
61
62
63
64
```
| ```
async def send_message(
    self,
    message: Message,
    *,
    metadata: dict[str, Any] | None = None,
    configuration: MessageSendConfiguration | None = None,
) -> SendMessageResponse:
    """Send a message using the A2A protocol.

    Returns a JSON-RPC response containing either a result (Task) or an error.
    """
    params = MessageSendParams(message=message)
    if metadata is not None:
        params['metadata'] = metadata
    if configuration is not None:
        params['configuration'] = configuration

    request_id = str(uuid.uuid4())
    payload = SendMessageRequest(jsonrpc='2.0', id=request_id, method='message/send', params=params)
    content = send_message_request_ta.dump_json(payload, by_alias=True)
    response = await self.http_client.post('/', content=content, headers={'Content-Type': 'application/json'})
    self._raise_for_status(response)

    return send_message_response_ta.validate_json(response.content)

```

---|---
###  UnexpectedResponseError
Bases:
An error raised when an unexpected response is received from the server.
Source code in `.venv/lib/python3.12/site-packages/fasta2a/client.py`
```
78
79
80
81
82
83
```
| ```
class UnexpectedResponseError(Exception):
    """An error raised when an unexpected response is received from the server."""

    def __init__(self, status_code: int, content: str) -> None:
        self.status_code = status_code
        self.content = content

```

---|---
© Pydantic Services Inc. 2024 to present
