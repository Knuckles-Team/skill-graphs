# `pydantic_ai.run`
###  AgentRun `dataclass`
Bases: `AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)"), OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")]`
A stateful, async-iterable run of an [`Agent`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent "Agent



      dataclass
  ").
You generally obtain an `AgentRun` instance by calling `async with my_agent.iter(...) as agent_run:`.
Once you have an instance, you can use it to iterate through the run's nodes as they execute. When an [`End`](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.End "End



      dataclass
  ") is reached, the run finishes and [`result`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AgentRun.result "result



      property
  ") becomes available.
Example:
```
from pydantic_ai import Agent

agent = Agent('openai:gpt-5.2')

async def main():
    nodes = []
    # Iterate through the run, recording each node along the way:
    async with agent.iter('What is the capital of France?') as agent_run:
        async for node in agent_run:
            nodes.append(node)
    print(nodes)
    '''
    [
        UserPromptNode(
            user_prompt='What is the capital of France?',
            instructions_functions=[],
            system_prompts=(),
            system_prompt_functions=[],
            system_prompt_dynamic_functions={},
        ),
        ModelRequestNode(
            request=ModelRequest(
                parts=[
                    UserPromptPart(
                        content='What is the capital of France?',
                        timestamp=datetime.datetime(...),
                    )
                ],
                timestamp=datetime.datetime(...),
                run_id='...',
            )
        ),
        CallToolsNode(
            model_response=ModelResponse(
                parts=[TextPart(content='The capital of France is Paris.')],
                usage=RequestUsage(input_tokens=56, output_tokens=7),
                model_name='gpt-5.2',
                timestamp=datetime.datetime(...),
                run_id='...',
            )
        ),
        End(data=FinalResult(output='The capital of France is Paris.')),
    ]
    '''
    print(agent_run.result.output)
    #> The capital of France is Paris.

```

You can also manually drive the iteration using the [`next`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AgentRun.next "next



      async
  ") method for more granular control.
Source code in `pydantic_ai_slim/pydantic_ai/run.py`
```
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
```
| ```
@dataclasses.dataclass(repr=False)
class AgentRun(Generic[AgentDepsT, OutputDataT]):
    """A stateful, async-iterable run of an [`Agent`][pydantic_ai.agent.Agent].

    You generally obtain an `AgentRun` instance by calling `async with my_agent.iter(...) as agent_run:`.

    Once you have an instance, you can use it to iterate through the run's nodes as they execute. When an
    [`End`][pydantic_graph.nodes.End] is reached, the run finishes and [`result`][pydantic_ai.agent.AgentRun.result]
    becomes available.

    Example:
```python
    from pydantic_ai import Agent

    agent = Agent('openai:gpt-5.2')

    async def main():
        nodes = []
        # Iterate through the run, recording each node along the way:
        async with agent.iter('What is the capital of France?') as agent_run:
            async for node in agent_run:
                nodes.append(node)
        print(nodes)
        '''
        [
            UserPromptNode(
                user_prompt='What is the capital of France?',
                instructions_functions=[],
                system_prompts=(),
                system_prompt_functions=[],
                system_prompt_dynamic_functions={},
            ),
            ModelRequestNode(
                request=ModelRequest(
                    parts=[
                        UserPromptPart(
                            content='What is the capital of France?',
                            timestamp=datetime.datetime(...),
                        )
                    ],
                    timestamp=datetime.datetime(...),
                    run_id='...',
                )
            ),
            CallToolsNode(
                model_response=ModelResponse(
                    parts=[TextPart(content='The capital of France is Paris.')],
                    usage=RequestUsage(input_tokens=56, output_tokens=7),
                    model_name='gpt-5.2',
                    timestamp=datetime.datetime(...),
                    run_id='...',
                )
            ),
            End(data=FinalResult(output='The capital of France is Paris.')),
        ]
        '''
        print(agent_run.result.output)
        #> The capital of France is Paris.
```

    You can also manually drive the iteration using the [`next`][pydantic_ai.agent.AgentRun.next] method for
    more granular control.
    """

    _graph_run: GraphRun[
        _agent_graph.GraphAgentState, _agent_graph.GraphAgentDeps[AgentDepsT, Any], FinalResult[OutputDataT]
    ]

    @overload
    def _traceparent(self, *, required: Literal[False]) -> str | None: ...
    @overload
    def _traceparent(self) -> str: ...
    def _traceparent(self, *, required: bool = True) -> str | None:
        traceparent = self._graph_run._traceparent(required=False)  # type: ignore[reportPrivateUsage]
        if traceparent is None and required:  # pragma: no cover
            raise AttributeError('No span was created for this agent run')
        return traceparent

    @property
    def ctx(self) -> GraphRunContext[_agent_graph.GraphAgentState, _agent_graph.GraphAgentDeps[AgentDepsT, Any]]:
        """The current context of the agent run."""
        return GraphRunContext[_agent_graph.GraphAgentState, _agent_graph.GraphAgentDeps[AgentDepsT, Any]](
            state=self._graph_run.state, deps=self._graph_run.deps
        )

    @property
    def next_node(
        self,
    ) -> _agent_graph.AgentNode[AgentDepsT, OutputDataT] | End[FinalResult[OutputDataT]]:
        """The next node that will be run in the agent graph.

        This is the next node that will be used during async iteration, or if a node is not passed to `self.next(...)`.
        """
        task = self._graph_run.next_task
        return self._task_to_node(task)

    @property
    def result(self) -> AgentRunResult[OutputDataT] | None:
        """The final result of the run if it has ended, otherwise `None`.

        Once the run returns an [`End`][pydantic_graph.nodes.End] node, `result` is populated
        with an [`AgentRunResult`][pydantic_ai.agent.AgentRunResult].
        """
        graph_run_output = self._graph_run.output
        if graph_run_output is None:
            return None
        return AgentRunResult(
            graph_run_output.output,
            graph_run_output.tool_name,
            self._graph_run.state,
            self._graph_run.deps.new_message_index,
            self._traceparent(required=False),
        )

    def all_messages(self) -> list[_messages.ModelMessage]:
        """Return all messages for the run so far.

        Messages from older runs are included.
        """
        return self.ctx.state.message_history

    def all_messages_json(self, *, output_tool_return_content: str | None = None) -> bytes:
        """Return all messages from [`all_messages`][pydantic_ai.agent.AgentRun.all_messages] as JSON bytes.

        Returns:
            JSON bytes representing the messages.
        """
        return _messages.ModelMessagesTypeAdapter.dump_json(self.all_messages())

    def new_messages(self) -> list[_messages.ModelMessage]:
        """Return new messages for the run so far.

        Messages from older runs are excluded.
        """
        return self.all_messages()[self.ctx.deps.new_message_index :]

    def new_messages_json(self) -> bytes:
        """Return new messages from [`new_messages`][pydantic_ai.agent.AgentRun.new_messages] as JSON bytes.

        Returns:
            JSON bytes representing the new messages.
        """
        return _messages.ModelMessagesTypeAdapter.dump_json(self.new_messages())

    def __aiter__(
        self,
    ) -> AsyncIterator[_agent_graph.AgentNode[AgentDepsT, OutputDataT] | End[FinalResult[OutputDataT]]]:
        """Provide async-iteration over the nodes in the agent run."""
        return self

    async def __anext__(
        self,
    ) -> _agent_graph.AgentNode[AgentDepsT, OutputDataT] | End[FinalResult[OutputDataT]]:
        """Advance to the next node automatically based on the last returned node."""
        task = await anext(self._graph_run)
        return self._task_to_node(task)

    def _task_to_node(
        self, task: EndMarker[FinalResult[OutputDataT]] | JoinItem | Sequence[GraphTaskRequest]
    ) -> _agent_graph.AgentNode[AgentDepsT, OutputDataT] | End[FinalResult[OutputDataT]]:
        if isinstance(task, Sequence) and len(task) == 1:
            first_task = task[0]
            if isinstance(first_task.inputs, BaseNode):  # pragma: no branch
                base_node: BaseNode[  # pyright: ignore[reportUnknownVariableType]
                    _agent_graph.GraphAgentState,
                    _agent_graph.GraphAgentDeps[AgentDepsT, OutputDataT],
                    FinalResult[OutputDataT],
                ] = first_task.inputs  # pyright: ignore[reportUnknownMemberType]
                if _agent_graph.is_agent_node(node=base_node):  # pragma: no branch
                    return base_node
        if isinstance(task, EndMarker):
            return End(task.value)
        raise exceptions.AgentRunError(f'Unexpected node: {task}')  # pragma: no cover

    def _node_to_task(self, node: _agent_graph.AgentNode[AgentDepsT, OutputDataT]) -> GraphTaskRequest:
        return GraphTaskRequest(NodeStep(type(node)).id, inputs=node, fork_stack=())

    async def next(
        self,
        node: _agent_graph.AgentNode[AgentDepsT, OutputDataT],
    ) -> _agent_graph.AgentNode[AgentDepsT, OutputDataT] | End[FinalResult[OutputDataT]]:
        """Manually drive the agent run by passing in the node you want to run next.

        This lets you inspect or mutate the node before continuing execution, or skip certain nodes
        under dynamic conditions. The agent run should be stopped when you return an [`End`][pydantic_graph.nodes.End]
        node.

        Example:
    ```python
        from pydantic_ai import Agent
        from pydantic_graph import End

        agent = Agent('openai:gpt-5.2')

        async def main():
            async with agent.iter('What is the capital of France?') as agent_run:
                next_node = agent_run.next_node  # start with the first node
                nodes = [next_node]
                while not isinstance(next_node, End):
                    next_node = await agent_run.next(next_node)
                    nodes.append(next_node)
                # Once `next_node` is an End, we've finished:
                print(nodes)
                '''
                [
                    UserPromptNode(
                        user_prompt='What is the capital of France?',
                        instructions_functions=[],
                        system_prompts=(),
                        system_prompt_functions=[],
                        system_prompt_dynamic_functions={},
                    ),
                    ModelRequestNode(
                        request=ModelRequest(
                            parts=[
                                UserPromptPart(
                                    content='What is the capital of France?',
                                    timestamp=datetime.datetime(...),
                                )
                            ],
                            timestamp=datetime.datetime(...),
                            run_id='...',
                        )
                    ),
                    CallToolsNode(
                        model_response=ModelResponse(
                            parts=[TextPart(content='The capital of France is Paris.')],
                            usage=RequestUsage(input_tokens=56, output_tokens=7),
                            model_name='gpt-5.2',
                            timestamp=datetime.datetime(...),
                            run_id='...',
                        )
                    ),
                    End(data=FinalResult(output='The capital of France is Paris.')),
                ]
                '''
                print('Final result:', agent_run.result.output)
                #> Final result: The capital of France is Paris.
    ```

        Args:
            node: The node to run next in the graph.

        Returns:
            The next node returned by the graph logic, or an [`End`][pydantic_graph.nodes.End] node if
            the run has completed.
        """
        # Note: It might be nice to expose a synchronous interface for iteration, but we shouldn't do it
        # on this class, or else IDEs won't warn you if you accidentally use `for` instead of `async for` to iterate.
        task = [self._node_to_task(node)]
        try:
            task = await self._graph_run.next(task)
        except StopAsyncIteration:
            pass
        return self._task_to_node(task)

    # TODO (v2): Make this a property
    def usage(self) -> _usage.RunUsage:
        """Get usage statistics for the run so far, including token usage, model requests, and so on."""
        return self._graph_run.state.usage

    @property
    def metadata(self) -> dict[str, Any] | None:
        """Metadata associated with this agent run, if configured."""
        return self._graph_run.state.metadata

    @property
    def run_id(self) -> str:
        """The unique identifier for the agent run."""
        return self._graph_run.state.run_id

    def __repr__(self) -> str:  # pragma: no cover
        result = self._graph_run.output
        result_repr = '<run not finished>' if result is None else repr(result.output)
        return f'<{type(self).__name__} result={result_repr} usage={self.usage()}>'

```

---|---
####  ctx `property`
```
ctx: GraphRunContext[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.GraphRunContext "GraphRunContext



      dataclass
   \(pydantic_graph.GraphRunContext\)")[
    GraphAgentState, GraphAgentDeps[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)"), ]
]

```

The current context of the agent run.
####  next_node `property`
```
next_node: (
    AgentNode[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)"), OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")]
    | End[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.End "End



      dataclass
   \(pydantic_graph.End\)")[FinalResult[OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")]]
)

```

The next node that will be run in the agent graph.
This is the next node that will be used during async iteration, or if a node is not passed to `self.next(...)`.
####  result `property`
```
result: AgentRunResult[](https://ai.pydantic.dev/api/run/#pydantic_ai.run.AgentRunResult "AgentRunResult



      dataclass
   \(pydantic_ai.run.AgentRunResult\)")[OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")] | None

```

The final result of the run if it has ended, otherwise `None`.
Once the run returns an [`End`](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.End "End



      dataclass
  ") node, `result` is populated with an [`AgentRunResult`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AgentRunResult "AgentRunResult



      dataclass
  ").
####  all_messages
```
all_messages() -> [ModelMessage[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelMessage "ModelMessage



      module-attribute
   \(pydantic_ai.messages.ModelMessage\)")]

```

Return all messages for the run so far.
Messages from older runs are included.
Source code in `pydantic_ai_slim/pydantic_ai/run.py`
```
141
142
143
144
145
146
```
| ```
def all_messages(self) -> list[_messages.ModelMessage]:
    """Return all messages for the run so far.

    Messages from older runs are included.
    """
    return self.ctx.state.message_history

```

---|---
####  all_messages_json
```
all_messages_json(
    *, output_tool_return_content:  | None = None
) ->

```

Return all messages from [`all_messages`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AgentRun.all_messages "all_messages") as JSON bytes.
Returns:
Type | Description
---|---
|  JSON bytes representing the messages.
Source code in `pydantic_ai_slim/pydantic_ai/run.py`
```
148
149
150
151
152
153
154
```
| ```
def all_messages_json(self, *, output_tool_return_content: str | None = None) -> bytes:
    """Return all messages from [`all_messages`][pydantic_ai.agent.AgentRun.all_messages] as JSON bytes.

    Returns:
        JSON bytes representing the messages.
    """
    return _messages.ModelMessagesTypeAdapter.dump_json(self.all_messages())

```

---|---
####  new_messages
```
new_messages() -> [ModelMessage[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelMessage "ModelMessage



      module-attribute
   \(pydantic_ai.messages.ModelMessage\)")]

```

Return new messages for the run so far.
Messages from older runs are excluded.
Source code in `pydantic_ai_slim/pydantic_ai/run.py`
```
156
157
158
159
160
161
```
| ```
def new_messages(self) -> list[_messages.ModelMessage]:
    """Return new messages for the run so far.

    Messages from older runs are excluded.
    """
    return self.all_messages()[self.ctx.deps.new_message_index :]

```

---|---
####  new_messages_json
```
new_messages_json() ->

```

Return new messages from [`new_messages`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AgentRun.new_messages "new_messages") as JSON bytes.
Returns:
Type | Description
---|---
|  JSON bytes representing the new messages.
Source code in `pydantic_ai_slim/pydantic_ai/run.py`
```
163
164
165
166
167
168
169
```
| ```
def new_messages_json(self) -> bytes:
    """Return new messages from [`new_messages`][pydantic_ai.agent.AgentRun.new_messages] as JSON bytes.

    Returns:
        JSON bytes representing the new messages.
    """
    return _messages.ModelMessagesTypeAdapter.dump_json(self.new_messages())

```

---|---
####  __aiter__
```
__aiter__() -> (
    [
        AgentNode[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)"), OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")]
        | End[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.End "End



      dataclass
   \(pydantic_graph.End\)")[FinalResult[OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")]]
    ]
)

```

Provide async-iteration over the nodes in the agent run.
Source code in `pydantic_ai_slim/pydantic_ai/run.py`
```
171
172
173
174
175
```
| ```
def __aiter__(
    self,
) -> AsyncIterator[_agent_graph.AgentNode[AgentDepsT, OutputDataT] | End[FinalResult[OutputDataT]]]:
    """Provide async-iteration over the nodes in the agent run."""
    return self

```

---|---
####  __anext__ `async`
```
__anext__() -> (
    AgentNode[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)"), OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")]
    | End[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.End "End



      dataclass
   \(pydantic_graph.End\)")[FinalResult[OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")]]
)

```

Advance to the next node automatically based on the last returned node.
Source code in `pydantic_ai_slim/pydantic_ai/run.py`
```
177
178
179
180
181
182
```
| ```
async def __anext__(
    self,
) -> _agent_graph.AgentNode[AgentDepsT, OutputDataT] | End[FinalResult[OutputDataT]]:
    """Advance to the next node automatically based on the last returned node."""
    task = await anext(self._graph_run)
    return self._task_to_node(task)

```

---|---
####  next `async`
```
next(
    node: AgentNode[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)"), OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")],
) -> (
    AgentNode[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)"), OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")]
    | End[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.End "End



      dataclass
   \(pydantic_graph.End\)")[FinalResult[OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")]]
)

```

Manually drive the agent run by passing in the node you want to run next.
This lets you inspect or mutate the node before continuing execution, or skip certain nodes under dynamic conditions. The agent run should be stopped when you return an [`End`](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.End "End



      dataclass
  ") node.
Example:
```
from pydantic_ai import Agent
from pydantic_graph import End

agent = Agent('openai:gpt-5.2')

async def main():
    async with agent.iter('What is the capital of France?') as agent_run:
        next_node = agent_run.next_node  # start with the first node
        nodes = [next_node]
        while not isinstance(next_node, End):
            next_node = await agent_run.next(next_node)
            nodes.append(next_node)
        # Once `next_node` is an End, we've finished:
        print(nodes)
        '''
        [
            UserPromptNode(
                user_prompt='What is the capital of France?',
                instructions_functions=[],
                system_prompts=(),
                system_prompt_functions=[],
                system_prompt_dynamic_functions={},
            ),
            ModelRequestNode(
                request=ModelRequest(
                    parts=[
                        UserPromptPart(
                            content='What is the capital of France?',
                            timestamp=datetime.datetime(...),
                        )
                    ],
                    timestamp=datetime.datetime(...),
                    run_id='...',
                )
            ),
            CallToolsNode(
                model_response=ModelResponse(
                    parts=[TextPart(content='The capital of France is Paris.')],
                    usage=RequestUsage(input_tokens=56, output_tokens=7),
                    model_name='gpt-5.2',
                    timestamp=datetime.datetime(...),
                    run_id='...',
                )
            ),
            End(data=FinalResult(output='The capital of France is Paris.')),
        ]
        '''
        print('Final result:', agent_run.result.output)
        #> Final result: The capital of France is Paris.

```

Parameters:
Name | Type | Description | Default
---|---|---|---
`node` |  `AgentNode[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)"), OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")]` |  The node to run next in the graph. |  _required_
Returns:
Type | Description
---|---
`AgentNode[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)"), OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")] | End[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.End "End



      dataclass
   \(pydantic_graph.End\)")[FinalResult[OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")]]` |  The next node returned by the graph logic, or an [`End`](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.End "End



      dataclass
  ") node if
`AgentNode[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)"), OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")] | End[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.End "End



      dataclass
   \(pydantic_graph.End\)")[FinalResult[OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")]]` |  the run has completed.
Source code in `pydantic_ai_slim/pydantic_ai/run.py`
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
```
| ```
async def next(
    self,
    node: _agent_graph.AgentNode[AgentDepsT, OutputDataT],
) -> _agent_graph.AgentNode[AgentDepsT, OutputDataT] | End[FinalResult[OutputDataT]]:
    """Manually drive the agent run by passing in the node you want to run next.

    This lets you inspect or mutate the node before continuing execution, or skip certain nodes
    under dynamic conditions. The agent run should be stopped when you return an [`End`][pydantic_graph.nodes.End]
    node.

    Example:
```python
    from pydantic_ai import Agent
    from pydantic_graph import End

    agent = Agent('openai:gpt-5.2')

    async def main():
        async with agent.iter('What is the capital of France?') as agent_run:
            next_node = agent_run.next_node  # start with the first node
            nodes = [next_node]
            while not isinstance(next_node, End):
                next_node = await agent_run.next(next_node)
                nodes.append(next_node)
            # Once `next_node` is an End, we've finished:
            print(nodes)
            '''
            [
                UserPromptNode(
                    user_prompt='What is the capital of France?',
                    instructions_functions=[],
                    system_prompts=(),
                    system_prompt_functions=[],
                    system_prompt_dynamic_functions={},
                ),
                ModelRequestNode(
                    request=ModelRequest(
                        parts=[
                            UserPromptPart(
                                content='What is the capital of France?',
                                timestamp=datetime.datetime(...),
                            )
                        ],
                        timestamp=datetime.datetime(...),
                        run_id='...',
                    )
                ),
                CallToolsNode(
                    model_response=ModelResponse(
                        parts=[TextPart(content='The capital of France is Paris.')],
                        usage=RequestUsage(input_tokens=56, output_tokens=7),
                        model_name='gpt-5.2',
                        timestamp=datetime.datetime(...),
                        run_id='...',
                    )
                ),
                End(data=FinalResult(output='The capital of France is Paris.')),
            ]
            '''
            print('Final result:', agent_run.result.output)
            #> Final result: The capital of France is Paris.
```

    Args:
        node: The node to run next in the graph.

    Returns:
        The next node returned by the graph logic, or an [`End`][pydantic_graph.nodes.End] node if
        the run has completed.
    """
    # Note: It might be nice to expose a synchronous interface for iteration, but we shouldn't do it
    # on this class, or else IDEs won't warn you if you accidentally use `for` instead of `async for` to iterate.
    task = [self._node_to_task(node)]
    try:
        task = await self._graph_run.next(task)
    except StopAsyncIteration:
        pass
    return self._task_to_node(task)

```

---|---
####  usage
```
usage() -> RunUsage[](https://ai.pydantic.dev/api/usage/#pydantic_ai.usage.RunUsage "RunUsage



      dataclass
   \(pydantic_ai.usage.RunUsage\)")

```

Get usage statistics for the run so far, including token usage, model requests, and so on.
Source code in `pydantic_ai_slim/pydantic_ai/run.py`
```
284
285
286
```
| ```
def usage(self) -> _usage.RunUsage:
    """Get usage statistics for the run so far, including token usage, model requests, and so on."""
    return self._graph_run.state.usage

```

---|---
####  metadata `property`
```
metadata: [, ] | None

```

Metadata associated with this agent run, if configured.
####  run_id `property`
```
run_id:

```

The unique identifier for the agent run.
###  AgentRunResult `dataclass`
Bases: `OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")]`
The final result of an agent run.
Source code in `pydantic_ai_slim/pydantic_ai/run.py`
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
314
315
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
374
375
376
377
378
379
380
381
382
383
384
385
386
387
388
389
390
391
392
393
394
395
396
397
398
399
400
401
402
403
404
405
406
407
408
409
410
411
412
413
414
415
416
417
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
```
| ```
@dataclasses.dataclass
class AgentRunResult(Generic[OutputDataT]):
    """The final result of an agent run."""

    output: OutputDataT
    """The output data from the agent run."""

    _output_tool_name: str | None = dataclasses.field(repr=False, compare=False, default=None)
    _state: _agent_graph.GraphAgentState = dataclasses.field(
        repr=False, compare=False, default_factory=_agent_graph.GraphAgentState
    )
    _new_message_index: int = dataclasses.field(repr=False, compare=False, default=0)
    _traceparent_value: str | None = dataclasses.field(repr=False, compare=False, default=None)

    @overload
    def _traceparent(self, *, required: Literal[False]) -> str | None: ...
    @overload
    def _traceparent(self) -> str: ...
    def _traceparent(self, *, required: bool = True) -> str | None:
        if self._traceparent_value is None and required:  # pragma: no cover
            raise AttributeError('No span was created for this agent run')
        return self._traceparent_value

    def _set_output_tool_return(self, return_content: str) -> list[_messages.ModelMessage]:
        """Set return content for the output tool.

        Useful if you want to continue the conversation and want to set the response to the output tool call.
        """
        if not self._output_tool_name:
            raise ValueError('Cannot set output tool return content when the return type is `str`.')

        messages = self._state.message_history
        last_message = messages[-1]
        for idx, part in enumerate(last_message.parts):
            if isinstance(part, _messages.ToolReturnPart) and part.tool_name == self._output_tool_name:
                # Only do deepcopy when we have to modify
                copied_messages = list(messages)
                copied_last = deepcopy(last_message)
                copied_last.parts[idx].content = return_content  # type: ignore[misc]
                copied_messages[-1] = copied_last
                return copied_messages

        raise LookupError(f'No tool call found with tool name {self._output_tool_name!r}.')

    def all_messages(self, *, output_tool_return_content: str | None = None) -> list[_messages.ModelMessage]:
        """Return the history of _messages.

        Args:
            output_tool_return_content: The return content of the tool call to set in the last message.
                This provides a convenient way to modify the content of the output tool call if you want to continue
                the conversation and want to set the response to the output tool call. If `None`, the last message will
                not be modified.

        Returns:
            List of messages.
        """
        if output_tool_return_content is not None:
            return self._set_output_tool_return(output_tool_return_content)
        else:
            return self._state.message_history

    def all_messages_json(self, *, output_tool_return_content: str | None = None) -> bytes:
        """Return all messages from [`all_messages`][pydantic_ai.agent.AgentRunResult.all_messages] as JSON bytes.

        Args:
            output_tool_return_content: The return content of the tool call to set in the last message.
                This provides a convenient way to modify the content of the output tool call if you want to continue
                the conversation and want to set the response to the output tool call. If `None`, the last message will
                not be modified.

        Returns:
            JSON bytes representing the messages.
        """
        return _messages.ModelMessagesTypeAdapter.dump_json(
            self.all_messages(output_tool_return_content=output_tool_return_content)
        )

    def new_messages(self, *, output_tool_return_content: str | None = None) -> list[_messages.ModelMessage]:
        """Return new messages associated with this run.

        Messages from older runs are excluded.

        Args:
            output_tool_return_content: The return content of the tool call to set in the last message.
                This provides a convenient way to modify the content of the output tool call if you want to continue
                the conversation and want to set the response to the output tool call. If `None`, the last message will
                not be modified.

        Returns:
            List of new messages.
        """
        return self.all_messages(output_tool_return_content=output_tool_return_content)[self._new_message_index :]

    def new_messages_json(self, *, output_tool_return_content: str | None = None) -> bytes:
        """Return new messages from [`new_messages`][pydantic_ai.agent.AgentRunResult.new_messages] as JSON bytes.

        Args:
            output_tool_return_content: The return content of the tool call to set in the last message.
                This provides a convenient way to modify the content of the output tool call if you want to continue
                the conversation and want to set the response to the output tool call. If `None`, the last message will
                not be modified.

        Returns:
            JSON bytes representing the new messages.
        """
        return _messages.ModelMessagesTypeAdapter.dump_json(
            self.new_messages(output_tool_return_content=output_tool_return_content)
        )

    @property
    def response(self) -> _messages.ModelResponse:
        """Return the last response from the message history."""
        # The response may not be the very last item if it contained an output tool call. See `CallToolsNode._handle_final_result`.
        for message in reversed(self.all_messages()):
            if isinstance(message, _messages.ModelResponse):
                return message
        raise ValueError('No response found in the message history')  # pragma: no cover

    # TODO (v2): Make this a property
    def usage(self) -> _usage.RunUsage:
        """Return the usage of the whole run."""
        return self._state.usage

    # TODO (v2): Make this a property
    def timestamp(self) -> datetime:
        """Return the timestamp of last response."""
        return self.response.timestamp

    @property
    def metadata(self) -> dict[str, Any] | None:
        """Metadata associated with this agent run, if configured."""
        return self._state.metadata

    @property
    def run_id(self) -> str:
        """The unique identifier for the agent run."""
        return self._state.run_id

```

---|---
####  output `instance-attribute`
```
output: OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")

```

The output data from the agent run.
####  all_messages
```
all_messages(
    *, output_tool_return_content:  | None = None
) -> [ModelMessage[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelMessage "ModelMessage



      module-attribute
   \(pydantic_ai.messages.ModelMessage\)")]

```

Return the history of _messages.
Parameters:
Name | Type | Description | Default
---|---|---|---
`output_tool_return_content` |  |  The return content of the tool call to set in the last message. This provides a convenient way to modify the content of the output tool call if you want to continue the conversation and want to set the response to the output tool call. If `None`, the last message will not be modified. |  `None`
Returns:
Type | Description
---|---
`ModelMessage[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelMessage "ModelMessage



      module-attribute
   \(pydantic_ai.messages.ModelMessage\)")]` |  List of messages.
Source code in `pydantic_ai_slim/pydantic_ai/run.py`
```
348
349
350
351
352
353
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
```
| ```
def all_messages(self, *, output_tool_return_content: str | None = None) -> list[_messages.ModelMessage]:
    """Return the history of _messages.

    Args:
        output_tool_return_content: The return content of the tool call to set in the last message.
            This provides a convenient way to modify the content of the output tool call if you want to continue
            the conversation and want to set the response to the output tool call. If `None`, the last message will
            not be modified.

    Returns:
        List of messages.
    """
    if output_tool_return_content is not None:
        return self._set_output_tool_return(output_tool_return_content)
    else:
        return self._state.message_history

```

---|---
####  all_messages_json
```
all_messages_json(
    *, output_tool_return_content:  | None = None
) ->

```

Return all messages from [`all_messages`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AgentRunResult.all_messages "all_messages") as JSON bytes.
Parameters:
Name | Type | Description | Default
---|---|---|---
`output_tool_return_content` |  |  The return content of the tool call to set in the last message. This provides a convenient way to modify the content of the output tool call if you want to continue the conversation and want to set the response to the output tool call. If `None`, the last message will not be modified. |  `None`
Returns:
Type | Description
---|---
|  JSON bytes representing the messages.
Source code in `pydantic_ai_slim/pydantic_ai/run.py`
```
365
366
367
368
369
370
371
372
373
374
375
376
377
378
379
```
| ```
def all_messages_json(self, *, output_tool_return_content: str | None = None) -> bytes:
    """Return all messages from [`all_messages`][pydantic_ai.agent.AgentRunResult.all_messages] as JSON bytes.

    Args:
        output_tool_return_content: The return content of the tool call to set in the last message.
            This provides a convenient way to modify the content of the output tool call if you want to continue
            the conversation and want to set the response to the output tool call. If `None`, the last message will
            not be modified.

    Returns:
        JSON bytes representing the messages.
    """
    return _messages.ModelMessagesTypeAdapter.dump_json(
        self.all_messages(output_tool_return_content=output_tool_return_content)
    )

```

---|---
####  new_messages
```
new_messages(
    *, output_tool_return_content:  | None = None
) -> [ModelMessage[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelMessage "ModelMessage



      module-attribute
   \(pydantic_ai.messages.ModelMessage\)")]

```

Return new messages associated with this run.
Messages from older runs are excluded.
Parameters:
Name | Type | Description | Default
---|---|---|---
`output_tool_return_content` |  |  The return content of the tool call to set in the last message. This provides a convenient way to modify the content of the output tool call if you want to continue the conversation and want to set the response to the output tool call. If `None`, the last message will not be modified. |  `None`
Returns:
Type | Description
---|---
`ModelMessage[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelMessage "ModelMessage



      module-attribute
   \(pydantic_ai.messages.ModelMessage\)")]` |  List of new messages.
Source code in `pydantic_ai_slim/pydantic_ai/run.py`
```
381
382
383
384
385
386
387
388
389
390
391
392
393
394
395
```
| ```
def new_messages(self, *, output_tool_return_content: str | None = None) -> list[_messages.ModelMessage]:
    """Return new messages associated with this run.

    Messages from older runs are excluded.

    Args:
        output_tool_return_content: The return content of the tool call to set in the last message.
            This provides a convenient way to modify the content of the output tool call if you want to continue
            the conversation and want to set the response to the output tool call. If `None`, the last message will
            not be modified.

    Returns:
        List of new messages.
    """
    return self.all_messages(output_tool_return_content=output_tool_return_content)[self._new_message_index :]

```

---|---
####  new_messages_json
```
new_messages_json(
    *, output_tool_return_content:  | None = None
) ->

```

Return new messages from [`new_messages`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AgentRunResult.new_messages "new_messages") as JSON bytes.
Parameters:
Name | Type | Description | Default
---|---|---|---
`output_tool_return_content` |  |  The return content of the tool call to set in the last message. This provides a convenient way to modify the content of the output tool call if you want to continue the conversation and want to set the response to the output tool call. If `None`, the last message will not be modified. |  `None`
Returns:
Type | Description
---|---
|  JSON bytes representing the new messages.
Source code in `pydantic_ai_slim/pydantic_ai/run.py`
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
406
407
408
409
410
411
```
| ```
def new_messages_json(self, *, output_tool_return_content: str | None = None) -> bytes:
    """Return new messages from [`new_messages`][pydantic_ai.agent.AgentRunResult.new_messages] as JSON bytes.

    Args:
        output_tool_return_content: The return content of the tool call to set in the last message.
            This provides a convenient way to modify the content of the output tool call if you want to continue
            the conversation and want to set the response to the output tool call. If `None`, the last message will
            not be modified.

    Returns:
        JSON bytes representing the new messages.
    """
    return _messages.ModelMessagesTypeAdapter.dump_json(
        self.new_messages(output_tool_return_content=output_tool_return_content)
    )

```

---|---
####  response `property`
```
response: ModelResponse[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse "ModelResponse



      dataclass
   \(pydantic_ai.messages.ModelResponse\)")

```

Return the last response from the message history.
####  usage
```
usage() -> RunUsage[](https://ai.pydantic.dev/api/usage/#pydantic_ai.usage.RunUsage "RunUsage



      dataclass
   \(pydantic_ai.usage.RunUsage\)")

```

Return the usage of the whole run.
Source code in `pydantic_ai_slim/pydantic_ai/run.py`
```
423
424
425
```
| ```
def usage(self) -> _usage.RunUsage:
    """Return the usage of the whole run."""
    return self._state.usage

```

---|---
####  timestamp
```
timestamp() ->

```

Return the timestamp of last response.
Source code in `pydantic_ai_slim/pydantic_ai/run.py`
```
428
429
430
```
| ```
def timestamp(self) -> datetime:
    """Return the timestamp of last response."""
    return self.response.timestamp

```

---|---
####  metadata `property`
```
metadata: [, ] | None

```

Metadata associated with this agent run, if configured.
####  run_id `property`
```
run_id:

```

The unique identifier for the agent run.
###  AgentRunResultEvent `dataclass`
Bases: `OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")]`
An event indicating the agent run ended and containing the final result of the agent run.
Source code in `pydantic_ai_slim/pydantic_ai/run.py`
```
443
444
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
```
| ```
@dataclasses.dataclass(repr=False)
class AgentRunResultEvent(Generic[OutputDataT]):
    """An event indicating the agent run ended and containing the final result of the agent run."""

    result: AgentRunResult[OutputDataT]
    """The result of the run."""

    _: dataclasses.KW_ONLY

    event_kind: Literal['agent_run_result'] = 'agent_run_result'
    """Event type identifier, used as a discriminator."""

    __repr__ = _utils.dataclasses_no_defaults_repr

```

---|---
####  result `instance-attribute`
```
result: AgentRunResult[](https://ai.pydantic.dev/api/run/#pydantic_ai.run.AgentRunResult "AgentRunResult



      dataclass
   \(pydantic_ai.run.AgentRunResult\)")[OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")]

```

The result of the run.
####  event_kind `class-attribute` `instance-attribute`
```
event_kind: ["agent_run_result"] = "agent_run_result"

```

Event type identifier, used as a discriminator.
© Pydantic Services Inc. 2024 to present
