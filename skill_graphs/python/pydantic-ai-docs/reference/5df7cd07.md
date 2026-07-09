# `fasta2a`
###  FastA2A
Bases: `Starlette`
The main class for the FastA2A library.
Source code in `.venv/lib/python3.12/site-packages/fasta2a/applications.py`
```
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
```
| ```
class FastA2A(Starlette):
    """The main class for the FastA2A library."""

    def __init__(
        self,
        *,
        storage: Storage,
        broker: Broker,
        # Agent card
        name: str | None = None,
        url: str = 'http://localhost:8000',
        version: str = '1.0.0',
        description: str | None = None,
        provider: AgentProvider | None = None,
        skills: list[Skill] | None = None,
        # Starlette
        debug: bool = False,
        routes: Sequence[Route] | None = None,
        middleware: Sequence[Middleware] | None = None,
        exception_handlers: dict[Any, ExceptionHandler] | None = None,
        lifespan: Lifespan[FastA2A] | None = None,
    ):
        if lifespan is None:
            lifespan = _default_lifespan

        super().__init__(
            debug=debug,
            routes=routes,
            middleware=middleware,
            exception_handlers=exception_handlers,
            lifespan=lifespan,
        )

        self.name = name or 'My Agent'
        self.url = url
        self.version = version
        self.description = description
        self.provider = provider
        self.skills = skills or []
        # NOTE: For now, I don't think there's any reason to support any other input/output modes.
        self.default_input_modes = ['application/json']
        self.default_output_modes = ['application/json']

        self.task_manager = TaskManager(broker=broker, storage=storage)

        # Setup
        self._agent_card_json_schema: bytes | None = None
        self.router.add_route(
            '/.well-known/agent-card.json', self._agent_card_endpoint, methods=['HEAD', 'GET', 'OPTIONS']
        )
        self.router.add_route('/', self._agent_run_endpoint, methods=['POST'])
        self.router.add_route('/docs', self._docs_endpoint, methods=['GET'])

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope['type'] == 'http' and not self.task_manager.is_running:
            raise RuntimeError('TaskManager was not properly initialized.')
        await super().__call__(scope, receive, send)

    async def _agent_card_endpoint(self, request: Request) -> Response:
        if self._agent_card_json_schema is None:
            agent_card = AgentCard(
                name=self.name,
                description=self.description or 'An AI agent exposed as an A2A agent.',
                url=self.url,
                version=self.version,
                protocol_version='0.3.0',
                skills=self.skills,
                default_input_modes=self.default_input_modes,
                default_output_modes=self.default_output_modes,
                capabilities=AgentCapabilities(
                    streaming=False, push_notifications=False, state_transition_history=False
                ),
            )
            if self.provider is not None:
                agent_card['provider'] = self.provider
            self._agent_card_json_schema = agent_card_ta.dump_json(agent_card, by_alias=True)
        return Response(content=self._agent_card_json_schema, media_type='application/json')

    async def _docs_endpoint(self, request: Request) -> Response:
        """Serve the documentation interface."""
        docs_path = Path(__file__).parent / 'static' / 'docs.html'
        return FileResponse(docs_path, media_type='text/html')

    async def _agent_run_endpoint(self, request: Request) -> Response:
        """This is the main endpoint for the A2A server.

        Although the specification allows freedom of choice and implementation, I'm pretty sure about some decisions.

        1. The server will always either send a "submitted" or a "failed" on `message/send`.
            Never a "completed" on the first message.
        2. There are three possible ends for the task:
            2.1. The task was "completed" successfully.
            2.2. The task was "canceled".
            2.3. The task "failed".
        3. The server will send a "working" on the first chunk on `tasks/pushNotification/get`.
        """
        data = await request.body()
        a2a_request = a2a_request_ta.validate_json(data)

        if a2a_request['method'] == 'message/send':
            jsonrpc_response = await self.task_manager.send_message(a2a_request)
        elif a2a_request['method'] == 'tasks/get':
            jsonrpc_response = await self.task_manager.get_task(a2a_request)
        elif a2a_request['method'] == 'tasks/cancel':
            jsonrpc_response = await self.task_manager.cancel_task(a2a_request)
        else:
            raise NotImplementedError(f'Method {a2a_request["method"]} not implemented.')
        return Response(
            content=a2a_response_ta.dump_json(jsonrpc_response, by_alias=True), media_type='application/json'
        )

```

---|---
###  Broker `dataclass`
Bases:
The broker class is in charge of scheduling the tasks.
The HTTP server uses the broker to schedule tasks.
The simple implementation is the `InMemoryBroker`, which is the broker that runs the tasks in the same process as the HTTP server. That said, this class can be extended to support remote workers.
Source code in `.venv/lib/python3.12/site-packages/fasta2a/broker.py`
```
19
20
21
22
23
24
25
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
```
| ```
@dataclass
class Broker(ABC):
    """The broker class is in charge of scheduling the tasks.

    The HTTP server uses the broker to schedule tasks.

    The simple implementation is the `InMemoryBroker`, which is the broker that
    runs the tasks in the same process as the HTTP server. That said, this class can be
    extended to support remote workers.
    """

    @abstractmethod
    async def run_task(self, params: TaskSendParams) -> None:
        """Send a task to be executed by the worker."""
        raise NotImplementedError('send_run_task is not implemented yet.')

    @abstractmethod
    async def cancel_task(self, params: TaskIdParams) -> None:
        """Cancel a task."""
        raise NotImplementedError('send_cancel_task is not implemented yet.')

    @abstractmethod
    async def __aenter__(self) -> Self: ...

    @abstractmethod
    async def __aexit__(self, exc_type: Any, exc_value: Any, traceback: Any): ...

    @abstractmethod
    def receive_task_operations(self) -> AsyncIterator[TaskOperation]:
        """Receive task operations from the broker.

        On a multi-worker setup, the broker will need to round-robin the task operations
        between the workers.
        """

```

---|---
####  run_task `abstractmethod` `async`
```
run_task(params: TaskSendParams[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.TaskSendParams "TaskSendParams \(fasta2a.schema.TaskSendParams\)")) -> None

```

Send a task to be executed by the worker.
Source code in `.venv/lib/python3.12/site-packages/fasta2a/broker.py`
```
30
31
32
33
```
| ```
@abstractmethod
async def run_task(self, params: TaskSendParams) -> None:
    """Send a task to be executed by the worker."""
    raise NotImplementedError('send_run_task is not implemented yet.')

```

---|---
####  cancel_task `abstractmethod` `async`
```
cancel_task(params: TaskIdParams[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.TaskIdParams "TaskIdParams \(fasta2a.schema.TaskIdParams\)")) -> None

```

Cancel a task.
Source code in `.venv/lib/python3.12/site-packages/fasta2a/broker.py`
```
35
36
37
38
```
| ```
@abstractmethod
async def cancel_task(self, params: TaskIdParams) -> None:
    """Cancel a task."""
    raise NotImplementedError('send_cancel_task is not implemented yet.')

```

---|---
####  receive_task_operations `abstractmethod`
```
receive_task_operations() -> [TaskOperation]

```

Receive task operations from the broker.
On a multi-worker setup, the broker will need to round-robin the task operations between the workers.
Source code in `.venv/lib/python3.12/site-packages/fasta2a/broker.py`
```
46
47
48
49
50
51
52
```
| ```
@abstractmethod
def receive_task_operations(self) -> AsyncIterator[TaskOperation]:
    """Receive task operations from the broker.

    On a multi-worker setup, the broker will need to round-robin the task operations
    between the workers.
    """

```

---|---
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
###  Storage
Bases: `ContextT]`
A storage to retrieve and save tasks, as well as retrieve and save context.
The storage serves two purposes: 1. Task storage: Stores tasks in A2A protocol format with their status, artifacts, and message history 2. Context storage: Stores conversation context in a format optimized for the specific agent implementation
Source code in `.venv/lib/python3.12/site-packages/fasta2a/storage.py`
```
17
18
19
20
21
22
23
24
25
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
```
| ```
class Storage(ABC, Generic[ContextT]):
    """A storage to retrieve and save tasks, as well as retrieve and save context.

    The storage serves two purposes:
    1. Task storage: Stores tasks in A2A protocol format with their status, artifacts, and message history
    2. Context storage: Stores conversation context in a format optimized for the specific agent implementation
    """

    @abstractmethod
    async def load_task(self, task_id: str, history_length: int | None = None) -> Task | None:
        """Load a task from storage.

        If the task is not found, return None.
        """

    @abstractmethod
    async def submit_task(self, context_id: str, message: Message) -> Task:
        """Submit a task to storage."""

    @abstractmethod
    async def update_task(
        self,
        task_id: str,
        state: TaskState,
        new_artifacts: list[Artifact] | None = None,
        new_messages: list[Message] | None = None,
    ) -> Task:
        """Update the state of a task. Appends artifacts and messages, if specified."""

    @abstractmethod
    async def load_context(self, context_id: str) -> ContextT | None:
        """Retrieve the stored context given the `context_id`."""

    @abstractmethod
    async def update_context(self, context_id: str, context: ContextT) -> None:
        """Updates the context for a `context_id`.

        Implementing agent can decide what to store in context.
        """

```

---|---
####  load_task `abstractmethod` `async`
```
load_task(
    task_id: , history_length:  | None = None
) -> Task[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.Task "Task \(fasta2a.schema.Task\)") | None

```

Load a task from storage.
If the task is not found, return None.
Source code in `.venv/lib/python3.12/site-packages/fasta2a/storage.py`
```
25
26
27
28
29
30
```
| ```
@abstractmethod
async def load_task(self, task_id: str, history_length: int | None = None) -> Task | None:
    """Load a task from storage.

    If the task is not found, return None.
    """

```

---|---
####  submit_task `abstractmethod` `async`
```
submit_task(context_id: , message: Message[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.Message "Message \(fasta2a.schema.Message\)")) -> Task[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.Task "Task \(fasta2a.schema.Task\)")

```

Submit a task to storage.
Source code in `.venv/lib/python3.12/site-packages/fasta2a/storage.py`
```
32
33
34
```
| ```
@abstractmethod
async def submit_task(self, context_id: str, message: Message) -> Task:
    """Submit a task to storage."""

```

---|---
####  update_task `abstractmethod` `async`
```
update_task(
    task_id: ,
    state: TaskState[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.TaskState "TaskState



      module-attribute
   \(fasta2a.schema.TaskState\)"),
    new_artifacts: [Artifact[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.Artifact "Artifact \(fasta2a.schema.Artifact\)")] | None = None,
    new_messages: [Message[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.Message "Message \(fasta2a.schema.Message\)")] | None = None,
) -> Task[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.Task "Task \(fasta2a.schema.Task\)")

```

Update the state of a task. Appends artifacts and messages, if specified.
Source code in `.venv/lib/python3.12/site-packages/fasta2a/storage.py`
```
36
37
38
39
40
41
42
43
44
```
| ```
@abstractmethod
async def update_task(
    self,
    task_id: str,
    state: TaskState,
    new_artifacts: list[Artifact] | None = None,
    new_messages: list[Message] | None = None,
) -> Task:
    """Update the state of a task. Appends artifacts and messages, if specified."""

```

---|---
####  load_context `abstractmethod` `async`
```
load_context(context_id: ) -> ContextT | None

```

Retrieve the stored context given the `context_id`.
Source code in `.venv/lib/python3.12/site-packages/fasta2a/storage.py`
```
46
47
48
```
| ```
@abstractmethod
async def load_context(self, context_id: str) -> ContextT | None:
    """Retrieve the stored context given the `context_id`."""

```

---|---
####  update_context `abstractmethod` `async`
```
update_context(context_id: , context: ContextT) -> None

```

Updates the context for a `context_id`.
Implementing agent can decide what to store in context.
Source code in `.venv/lib/python3.12/site-packages/fasta2a/storage.py`
```
50
51
52
53
54
55
```
| ```
@abstractmethod
async def update_context(self, context_id: str, context: ContextT) -> None:
    """Updates the context for a `context_id`.

    Implementing agent can decide what to store in context.
    """

```

---|---
###  Worker `dataclass`
Bases: `ContextT]`
A worker is responsible for executing tasks.
Source code in `.venv/lib/python3.12/site-packages/fasta2a/worker.py`
```
22
23
24
25
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
```
| ```
@dataclass
class Worker(ABC, Generic[ContextT]):
    """A worker is responsible for executing tasks."""

    broker: Broker
    storage: Storage[ContextT]

    @asynccontextmanager
    async def run(self) -> AsyncIterator[None]:
        """Run the worker.

        It connects to the broker, and it makes itself available to receive commands.
        """
        async with anyio.create_task_group() as tg:
            tg.start_soon(self._loop)
            yield
            tg.cancel_scope.cancel()

    async def _loop(self) -> None:
        async for task_operation in self.broker.receive_task_operations():
            await self._handle_task_operation(task_operation)

    async def _handle_task_operation(self, task_operation: TaskOperation) -> None:
        try:
            with use_span(task_operation['_current_span']):
                with tracer.start_as_current_span(
                    f'{task_operation["operation"]} task', attributes={'logfire.tags': ['fasta2a']}
                ):
                    if task_operation['operation'] == 'run':
                        await self.run_task(task_operation['params'])
                    elif task_operation['operation'] == 'cancel':
                        await self.cancel_task(task_operation['params'])
                    else:
                        assert_never(task_operation)
        except Exception:
            await self.storage.update_task(task_operation['params']['id'], state='failed')

    @abstractmethod
    async def run_task(self, params: TaskSendParams) -> None: ...

    @abstractmethod
    async def cancel_task(self, params: TaskIdParams) -> None: ...

    @abstractmethod
    def build_message_history(self, history: list[Message]) -> list[Any]: ...

    @abstractmethod
    def build_artifacts(self, result: Any) -> list[Artifact]: ...

```

---|---
####  run `async`
```
run() -> [None]

```

Run the worker.
It connects to the broker, and it makes itself available to receive commands.
Source code in `.venv/lib/python3.12/site-packages/fasta2a/worker.py`
```
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
@asynccontextmanager
async def run(self) -> AsyncIterator[None]:
    """Run the worker.

    It connects to the broker, and it makes itself available to receive commands.
    """
    async with anyio.create_task_group() as tg:
        tg.start_soon(self._loop)
        yield
        tg.cancel_scope.cancel()

```

---|---
This module contains the schema for the agent card.
###  AgentCard
Bases:
The card that describes an agent.
Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`
```
13
14
15
16
17
18
19
20
21
22
23
24
25
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
```
| ```
@pydantic.with_config({'alias_generator': to_camel})
class AgentCard(TypedDict):
    """The card that describes an agent."""

    name: str
    """Human readable name of the agent e.g. "Recipe Agent"."""

    description: str
    """A human-readable description of the agent.

    Used to assist users and other agents in understanding what the agent can do.
    (e.g. "Agent that helps users with recipes and cooking.")
    """

    url: str
    """A URL to the address the agent is hosted at."""

    version: str
    """The version of the agent - format is up to the provider. (e.g. "1.0.0")"""

    protocol_version: str
    """The version of the A2A protocol this agent supports."""

    provider: NotRequired[AgentProvider]
    """The service provider of the agent."""

    documentation_url: NotRequired[str]
    """A URL to documentation for the agent."""

    icon_url: NotRequired[str]
    """A URL to an icon for the agent."""

    preferred_transport: NotRequired[str]
    """The transport of the preferred endpoint. If empty, defaults to JSONRPC."""

    additional_interfaces: NotRequired[list[AgentInterface]]
    """Announcement of additional supported transports."""

    capabilities: AgentCapabilities
    """The capabilities of the agent."""

    security: NotRequired[list[dict[str, list[str]]]]
    """Security requirements for contacting the agent."""

    security_schemes: NotRequired[dict[str, SecurityScheme]]
    """Security scheme definitions."""

    default_input_modes: list[str]
    """Supported mime types for input data."""

    default_output_modes: list[str]
    """Supported mime types for output data."""

    skills: list[Skill]
    """The set of skills, or distinct capabilities, that the agent can perform."""

```

---|---
####  name `instance-attribute`
```
name:

```

Human readable name of the agent e.g. "Recipe Agent".
####  description `instance-attribute`
```
description:

```

A human-readable description of the agent.
Used to assist users and other agents in understanding what the agent can do. (e.g. "Agent that helps users with recipes and cooking.")
####  url `instance-attribute`
```
url:

```

A URL to the address the agent is hosted at.
####  version `instance-attribute`
```
version:

```

The version of the agent - format is up to the provider. (e.g. "1.0.0")
####  protocol_version `instance-attribute`
```
protocol_version:

```

The version of the A2A protocol this agent supports.
####  provider `instance-attribute`
```
provider: [AgentProvider[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.AgentProvider "AgentProvider \(fasta2a.schema.AgentProvider\)")]

```

The service provider of the agent.
####  documentation_url `instance-attribute`
```
documentation_url: []

```

A URL to documentation for the agent.
####  icon_url `instance-attribute`
```
icon_url: []

```

A URL to an icon for the agent.
####  preferred_transport `instance-attribute`
```
preferred_transport: []

```

The transport of the preferred endpoint. If empty, defaults to JSONRPC.
####  additional_interfaces `instance-attribute`
```
additional_interfaces: [[AgentInterface[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.AgentInterface "AgentInterface \(fasta2a.schema.AgentInterface\)")]]

```

Announcement of additional supported transports.
####  capabilities `instance-attribute`
```
capabilities: AgentCapabilities[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.AgentCapabilities "AgentCapabilities \(fasta2a.schema.AgentCapabilities\)")

```

The capabilities of the agent.
####  security `instance-attribute`
```
security: [[[, []]]]

```

Security requirements for contacting the agent.
####  security_schemes `instance-attribute`
```
security_schemes: [[, SecurityScheme[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.SecurityScheme "SecurityScheme



      module-attribute
   \(fasta2a.schema.SecurityScheme\)")]]

```

Security scheme definitions.
####  default_input_modes `instance-attribute`
```
default_input_modes: []

```

Supported mime types for input data.
####  default_output_modes `instance-attribute`
```
default_output_modes: []

```

Supported mime types for output data.
####  skills `instance-attribute`
```
skills: [Skill[](https://ai.pydantic.dev/api/fasta2a/#fasta2a.schema.Skill "Skill \(fasta2a.schema.Skill\)")]

```

The set of skills, or distinct capabilities, that the agent can perform.
###  AgentProvider
Bases:
The service provider of the agent.
Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`
```
73
74
75
76
77
78
79
80
```
| ```
class AgentProvider(TypedDict):
    """The service provider of the agent."""

    organization: str
    """The name of the agent provider's organization."""

    url: str
    """A URL for the agent provider's website or relevant documentation."""

```

---|---
####  organization `instance-attribute`
```
organization:

```

The name of the agent provider's organization.
####  url `instance-attribute`
```
url:

```

A URL for the agent provider's website or relevant documentation.
###  AgentCapabilities
Bases:
The capabilities of the agent.
Source code in `.venv/lib/python3.12/site-packages/fasta2a/schema.py`
```
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
```
| ```
@pydantic.with_config({'alias_generator': to_camel})
class AgentCapabilities(TypedDict):
    """The capabilities of the agent."""

    streaming: NotRequired[bool]
    """Whether the agent supports streaming."""

    push_notifications: NotRequired[bool]
    """Whether the agent can notify updates to client."""

    state_transition_history: NotRequired[bool]
    """Whether the agent exposes status change history for tasks."""

```

---|---
####  streaming `instance-attribute`
```
streaming: []

```

Whether the agent supports streaming.
####  push_notifications `instance-attribute`
```
push_notifications: []

```

Whether the agent can notify updates to client.
####  state_transition_history `instance-attribute`
```
state_transition_history: []

```

Whether the agent exposes status change history for tasks.
###  HttpSecurityScheme
Bases:
HTTP security scheme.
