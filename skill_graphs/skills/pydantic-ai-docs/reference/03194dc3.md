# `pydantic_graph.beta`
The next version of the pydantic-graph framework with enhanced graph execution capabilities.
This module provides a parallel control flow graph execution framework with support for: - 'Step' nodes for task execution - 'Decision' nodes for conditional branching - 'Fork' nodes for parallel execution coordination - 'Join' nodes and 'Reducer's for re-joining parallel executions - Mermaid diagram generation for graph visualization
###  Graph `dataclass`
Bases: `StateT[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.StateT "StateT



      module-attribute
   \(pydantic_graph.beta.graph.StateT\)"), DepsT[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.DepsT "DepsT



      module-attribute
   \(pydantic_graph.beta.graph.DepsT\)"), InputT[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.InputT "InputT



      module-attribute
   \(pydantic_graph.beta.graph.InputT\)"), OutputT[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.OutputT "OutputT



      module-attribute
   \(pydantic_graph.beta.graph.OutputT\)")]`
A complete graph definition ready for execution.
The Graph class represents a complete workflow graph with typed inputs, outputs, state, and dependencies. It contains all nodes, edges, and metadata needed for execution.
Class Type Parameters:
Name | Bound or Constraints | Description | Default
---|---|---|---
`StateT` |  |  The type of the graph state |  _required_
`DepsT` |  |  The type of the dependencies |  _required_
`InputT` |  |  The type of the input data |  _required_
`OutputT` |  |  The type of the output data |  _required_
Source code in `pydantic_graph/pydantic_graph/beta/graph.py`
```
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
302
303
304
```
| ```
@dataclass(repr=False)
class Graph(Generic[StateT, DepsT, InputT, OutputT]):
    """A complete graph definition ready for execution.

    The Graph class represents a complete workflow graph with typed inputs,
    outputs, state, and dependencies. It contains all nodes, edges, and
    metadata needed for execution.

    Type Parameters:
        StateT: The type of the graph state
        DepsT: The type of the dependencies
        InputT: The type of the input data
        OutputT: The type of the output data
    """

    name: str | None
    """Optional name for the graph, if not provided the name will be inferred from the calling frame on the first call to a graph method."""

    state_type: type[StateT]
    """The type of the graph state."""

    deps_type: type[DepsT]
    """The type of the dependencies."""

    input_type: type[InputT]
    """The type of the input data."""

    output_type: type[OutputT]
    """The type of the output data."""

    auto_instrument: bool
    """Whether to automatically create instrumentation spans."""

    nodes: dict[NodeID, AnyNode]
    """All nodes in the graph indexed by their ID."""

    edges_by_source: dict[NodeID, list[Path]]
    """Outgoing paths from each source node."""

    parent_forks: dict[JoinID, ParentFork[NodeID]]
    """Parent fork information for each join node."""

    intermediate_join_nodes: dict[JoinID, set[JoinID]]
    """For each join, the set of other joins that appear between it and its parent fork.

    Used to determine which joins are "final" (have no other joins as intermediates) and
    which joins should preserve fork stacks when proceeding downstream."""

    def get_parent_fork(self, join_id: JoinID) -> ParentFork[NodeID]:
        """Get the parent fork information for a join node.

        Args:
            join_id: The ID of the join node

        Returns:
            The parent fork information for the join

        Raises:
            RuntimeError: If the join ID is not found or has no parent fork
        """
        result = self.parent_forks.get(join_id)
        if result is None:
            raise RuntimeError(f'Node {join_id} is not a join node or did not have a dominating fork (this is a bug)')
        return result

    def is_final_join(self, join_id: JoinID) -> bool:
        """Check if a join is 'final' (has no downstream joins with the same parent fork).

        A join is non-final if it appears as an intermediate node for another join
        with the same parent fork.

        Args:
            join_id: The ID of the join node

        Returns:
            True if the join is final, False if it's non-final
        """
        # Check if this join appears in any other join's intermediate_join_nodes
        for intermediate_joins in self.intermediate_join_nodes.values():
            if join_id in intermediate_joins:
                return False
        return True

    async def run(
        self,
        *,
        state: StateT = None,
        deps: DepsT = None,
        inputs: InputT = None,
        span: AbstractContextManager[AbstractSpan] | None = None,
        infer_name: bool = True,
    ) -> OutputT:
        """Execute the graph and return the final output.

        This is the main entry point for graph execution. It runs the graph
        to completion and returns the final output value.

        Args:
            state: The graph state instance
            deps: The dependencies instance
            inputs: The input data for the graph
            span: Optional span for tracing/instrumentation
            infer_name: Whether to infer the graph name from the calling frame.

        Returns:
            The final output from the graph execution
        """
        if infer_name and self.name is None:
            inferred_name = infer_obj_name(self, depth=2)
            if inferred_name is not None:  # pragma: no branch
                self.name = inferred_name

        async with self.iter(state=state, deps=deps, inputs=inputs, span=span, infer_name=False) as graph_run:
            # Note: This would probably be better using `async for _ in graph_run`, but this tests the `next` method,
            # which I'm less confident will be implemented correctly if not used on the critical path. We can change it
            # once we have tests, etc.
            event: Any = None
            while True:
                try:
                    event = await graph_run.next(event)
                except StopAsyncIteration:
                    assert isinstance(event, EndMarker), 'Graph run should end with an EndMarker.'
                    return cast(EndMarker[OutputT], event).value

    @asynccontextmanager
    async def iter(
        self,
        *,
        state: StateT = None,
        deps: DepsT = None,
        inputs: InputT = None,
        span: AbstractContextManager[AbstractSpan] | None = None,
        infer_name: bool = True,
    ) -> AsyncIterator[GraphRun[StateT, DepsT, OutputT]]:
        """Create an iterator for step-by-step graph execution.

        This method allows for more fine-grained control over graph execution,
        enabling inspection of intermediate states and results.

        Args:
            state: The graph state instance
            deps: The dependencies instance
            inputs: The input data for the graph
            span: Optional span for tracing/instrumentation
            infer_name: Whether to infer the graph name from the calling frame.

        Yields:
            A GraphRun instance that can be iterated for step-by-step execution
        """
        if infer_name and self.name is None:
            inferred_name = infer_obj_name(self, depth=3)  # depth=3 because asynccontextmanager adds one
            if inferred_name is not None:  # pragma: no branch
                self.name = inferred_name

        with ExitStack() as stack:
            entered_span: AbstractSpan | None = None
            if span is None:
                if self.auto_instrument:
                    entered_span = stack.enter_context(logfire_span('run graph {graph.name}', graph=self))
            else:
                entered_span = stack.enter_context(span)
            traceparent = None if entered_span is None else get_traceparent(entered_span)
            async with GraphRun[StateT, DepsT, OutputT](
                graph=self,
                state=state,
                deps=deps,
                inputs=inputs,
                traceparent=traceparent,
            ) as graph_run:
                yield graph_run

    def render(self, *, title: str | None = None, direction: StateDiagramDirection | None = None) -> str:
        """Render the graph as a Mermaid diagram string.

        Args:
            title: Optional title for the diagram
            direction: Optional direction for the diagram layout

        Returns:
            A string containing the Mermaid diagram representation
        """
        from pydantic_graph.beta.mermaid import build_mermaid_graph

        return build_mermaid_graph(self.nodes, self.edges_by_source).render(title=title, direction=direction)

    def __repr__(self) -> str:
        super_repr = super().__repr__()  # include class and memory address
        # Insert the result of calling `__str__` before the final '>' in the repr
        return f'{super_repr[:-1]}\n{self}\n{super_repr[-1]}'

    def __str__(self) -> str:
        """Return a Mermaid diagram representation of the graph.

        Returns:
            A string containing the Mermaid diagram of the graph
        """
        return self.render()

```

---|---
####  name `instance-attribute`
```
name:  | None

```

Optional name for the graph, if not provided the name will be inferred from the calling frame on the first call to a graph method.
####  state_type `instance-attribute`
```
state_type: [StateT[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.StateT "StateT



      module-attribute
   \(pydantic_graph.beta.graph.StateT\)")]

```

The type of the graph state.
####  deps_type `instance-attribute`
```
deps_type: [DepsT[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.DepsT "DepsT



      module-attribute
   \(pydantic_graph.beta.graph.DepsT\)")]

```

The type of the dependencies.
####  input_type `instance-attribute`
```
input_type: [InputT[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.InputT "InputT



      module-attribute
   \(pydantic_graph.beta.graph.InputT\)")]

```

The type of the input data.
####  output_type `instance-attribute`
```
output_type: [OutputT[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.OutputT "OutputT



      module-attribute
   \(pydantic_graph.beta.graph.OutputT\)")]

```

The type of the output data.
####  auto_instrument `instance-attribute`
```
auto_instrument:

```

Whether to automatically create instrumentation spans.
####  nodes `instance-attribute`
```
nodes: [NodeID, AnyNode]

```

All nodes in the graph indexed by their ID.
####  edges_by_source `instance-attribute`
```
edges_by_source: [NodeID, [Path]]

```

Outgoing paths from each source node.
####  parent_forks `instance-attribute`
```
parent_forks: [JoinID, ParentFork[NodeID]]

```

Parent fork information for each join node.
####  intermediate_join_nodes `instance-attribute`
```
intermediate_join_nodes: [JoinID, [JoinID]]

```

For each join, the set of other joins that appear between it and its parent fork.
Used to determine which joins are "final" (have no other joins as intermediates) and which joins should preserve fork stacks when proceeding downstream.
####  get_parent_fork
```
get_parent_fork(join_id: JoinID) -> ParentFork[NodeID]

```

Get the parent fork information for a join node.
Parameters:
Name | Type | Description | Default
---|---|---|---
`join_id` |  `JoinID` |  The ID of the join node |  _required_
Returns:
Type | Description
---|---
`ParentFork[NodeID]` |  The parent fork information for the join
Raises:
Type | Description
---|---
|  If the join ID is not found or has no parent fork
Source code in `pydantic_graph/pydantic_graph/beta/graph.py`
```
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
```
| ```
def get_parent_fork(self, join_id: JoinID) -> ParentFork[NodeID]:
    """Get the parent fork information for a join node.

    Args:
        join_id: The ID of the join node

    Returns:
        The parent fork information for the join

    Raises:
        RuntimeError: If the join ID is not found or has no parent fork
    """
    result = self.parent_forks.get(join_id)
    if result is None:
        raise RuntimeError(f'Node {join_id} is not a join node or did not have a dominating fork (this is a bug)')
    return result

```

---|---
####  is_final_join
```
is_final_join(join_id: JoinID) ->

```

Check if a join is 'final' (has no downstream joins with the same parent fork).
A join is non-final if it appears as an intermediate node for another join with the same parent fork.
Parameters:
Name | Type | Description | Default
---|---|---|---
`join_id` |  `JoinID` |  The ID of the join node |  _required_
Returns:
Type | Description
---|---
|  True if the join is final, False if it's non-final
Source code in `pydantic_graph/pydantic_graph/beta/graph.py`
```
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
```
| ```
def is_final_join(self, join_id: JoinID) -> bool:
    """Check if a join is 'final' (has no downstream joins with the same parent fork).

    A join is non-final if it appears as an intermediate node for another join
    with the same parent fork.

    Args:
        join_id: The ID of the join node

    Returns:
        True if the join is final, False if it's non-final
    """
    # Check if this join appears in any other join's intermediate_join_nodes
    for intermediate_joins in self.intermediate_join_nodes.values():
        if join_id in intermediate_joins:
            return False
    return True

```

---|---
####  run `async`
```
run(
    *,
    state: StateT[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.StateT "StateT



      module-attribute
   \(pydantic_graph.beta.graph.StateT\)") = None,
    deps: DepsT[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.DepsT "DepsT



      module-attribute
   \(pydantic_graph.beta.graph.DepsT\)") = None,
    inputs: InputT[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.InputT "InputT



      module-attribute
   \(pydantic_graph.beta.graph.InputT\)") = None,
    span: (
        [AbstractSpan] | None
    ) = None,
    infer_name:  = True
) -> OutputT[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.OutputT "OutputT



      module-attribute
   \(pydantic_graph.beta.graph.OutputT\)")

```

Execute the graph and return the final output.
This is the main entry point for graph execution. It runs the graph to completion and returns the final output value.
Parameters:
Name | Type | Description | Default
---|---|---|---
`state` |  `StateT[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.StateT "StateT



      module-attribute
   \(pydantic_graph.beta.graph.StateT\)")` |  The graph state instance |  `None`
`deps` |  `DepsT[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.DepsT "DepsT



      module-attribute
   \(pydantic_graph.beta.graph.DepsT\)")` |  The dependencies instance |  `None`
`inputs` |  `InputT[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.InputT "InputT



      module-attribute
   \(pydantic_graph.beta.graph.InputT\)")` |  The input data for the graph |  `None`
`span` |  `AbstractSpan] | None` |  Optional span for tracing/instrumentation |  `None`
`infer_name` |  |  Whether to infer the graph name from the calling frame. |  `True`
Returns:
Type | Description
---|---
`OutputT[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.OutputT "OutputT



      module-attribute
   \(pydantic_graph.beta.graph.OutputT\)")` |  The final output from the graph execution
Source code in `pydantic_graph/pydantic_graph/beta/graph.py`
```
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
```
| ```
async def run(
    self,
    *,
    state: StateT = None,
    deps: DepsT = None,
    inputs: InputT = None,
    span: AbstractContextManager[AbstractSpan] | None = None,
    infer_name: bool = True,
) -> OutputT:
    """Execute the graph and return the final output.

    This is the main entry point for graph execution. It runs the graph
    to completion and returns the final output value.

    Args:
        state: The graph state instance
        deps: The dependencies instance
        inputs: The input data for the graph
        span: Optional span for tracing/instrumentation
        infer_name: Whether to infer the graph name from the calling frame.

    Returns:
        The final output from the graph execution
    """
    if infer_name and self.name is None:
        inferred_name = infer_obj_name(self, depth=2)
        if inferred_name is not None:  # pragma: no branch
            self.name = inferred_name

    async with self.iter(state=state, deps=deps, inputs=inputs, span=span, infer_name=False) as graph_run:
        # Note: This would probably be better using `async for _ in graph_run`, but this tests the `next` method,
        # which I'm less confident will be implemented correctly if not used on the critical path. We can change it
        # once we have tests, etc.
        event: Any = None
        while True:
            try:
                event = await graph_run.next(event)
            except StopAsyncIteration:
                assert isinstance(event, EndMarker), 'Graph run should end with an EndMarker.'
                return cast(EndMarker[OutputT], event).value

```

---|---
####  iter `async`
```
iter(
    *,
    state: StateT[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.StateT "StateT



      module-attribute
   \(pydantic_graph.beta.graph.StateT\)") = None,
    deps: DepsT[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.DepsT "DepsT



      module-attribute
   \(pydantic_graph.beta.graph.DepsT\)") = None,
    inputs: InputT[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.InputT "InputT



      module-attribute
   \(pydantic_graph.beta.graph.InputT\)") = None,
    span: (
        [AbstractSpan] | None
    ) = None,
    infer_name:  = True
) -> [GraphRun[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.GraphRun "GraphRun \(pydantic_graph.beta.graph.GraphRun\)")[StateT[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.StateT "StateT



      module-attribute
   \(pydantic_graph.beta.graph.StateT\)"), DepsT[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.DepsT "DepsT



      module-attribute
   \(pydantic_graph.beta.graph.DepsT\)"), OutputT[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.OutputT "OutputT



      module-attribute
   \(pydantic_graph.beta.graph.OutputT\)")]]

```

Create an iterator for step-by-step graph execution.
This method allows for more fine-grained control over graph execution, enabling inspection of intermediate states and results.
Parameters:
Name | Type | Description | Default
---|---|---|---
`state` |  `StateT[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.StateT "StateT



      module-attribute
   \(pydantic_graph.beta.graph.StateT\)")` |  The graph state instance |  `None`
`deps` |  `DepsT[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.DepsT "DepsT



      module-attribute
   \(pydantic_graph.beta.graph.DepsT\)")` |  The dependencies instance |  `None`
`inputs` |  `InputT[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.InputT "InputT



      module-attribute
   \(pydantic_graph.beta.graph.InputT\)")` |  The input data for the graph |  `None`
`span` |  `AbstractSpan] | None` |  Optional span for tracing/instrumentation |  `None`
`infer_name` |  |  Whether to infer the graph name from the calling frame. |  `True`
Yields:
Type | Description
---|---
`GraphRun[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.GraphRun "GraphRun \(pydantic_graph.beta.graph.GraphRun\)")[StateT[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.StateT "StateT



      module-attribute
   \(pydantic_graph.beta.graph.StateT\)"), DepsT[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.DepsT "DepsT



      module-attribute
   \(pydantic_graph.beta.graph.DepsT\)"), OutputT[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.OutputT "OutputT



      module-attribute
   \(pydantic_graph.beta.graph.OutputT\)")]]` |  A GraphRun instance that can be iterated for step-by-step execution
Source code in `pydantic_graph/pydantic_graph/beta/graph.py`
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
```
| ```
@asynccontextmanager
async def iter(
    self,
    *,
    state: StateT = None,
    deps: DepsT = None,
    inputs: InputT = None,
    span: AbstractContextManager[AbstractSpan] | None = None,
    infer_name: bool = True,
) -> AsyncIterator[GraphRun[StateT, DepsT, OutputT]]:
    """Create an iterator for step-by-step graph execution.

    This method allows for more fine-grained control over graph execution,
    enabling inspection of intermediate states and results.

    Args:
        state: The graph state instance
        deps: The dependencies instance
        inputs: The input data for the graph
        span: Optional span for tracing/instrumentation
        infer_name: Whether to infer the graph name from the calling frame.

    Yields:
        A GraphRun instance that can be iterated for step-by-step execution
    """
    if infer_name and self.name is None:
        inferred_name = infer_obj_name(self, depth=3)  # depth=3 because asynccontextmanager adds one
        if inferred_name is not None:  # pragma: no branch
            self.name = inferred_name

    with ExitStack() as stack:
        entered_span: AbstractSpan | None = None
        if span is None:
            if self.auto_instrument:
                entered_span = stack.enter_context(logfire_span('run graph {graph.name}', graph=self))
        else:
            entered_span = stack.enter_context(span)
        traceparent = None if entered_span is None else get_traceparent(entered_span)
        async with GraphRun[StateT, DepsT, OutputT](
            graph=self,
            state=state,
            deps=deps,
            inputs=inputs,
            traceparent=traceparent,
        ) as graph_run:
            yield graph_run

```

---|---
####  render
```
render(
    *,
    title:  | None = None,
    direction: StateDiagramDirection | None = None
) ->

```

Render the graph as a Mermaid diagram string.
Parameters:
Name | Type | Description | Default
---|---|---|---
`title` |  |  Optional title for the diagram |  `None`
`direction` |  `StateDiagramDirection | None` |  Optional direction for the diagram layout |  `None`
Returns:
Type | Description
---|---
|  A string containing the Mermaid diagram representation
Source code in `pydantic_graph/pydantic_graph/beta/graph.py`
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
290
291
```
| ```
def render(self, *, title: str | None = None, direction: StateDiagramDirection | None = None) -> str:
    """Render the graph as a Mermaid diagram string.

    Args:
        title: Optional title for the diagram
        direction: Optional direction for the diagram layout

    Returns:
        A string containing the Mermaid diagram representation
    """
    from pydantic_graph.beta.mermaid import build_mermaid_graph

    return build_mermaid_graph(self.nodes, self.edges_by_source).render(title=title, direction=direction)

```

---|---
####  __str__
```
__str__() ->

```

Return a Mermaid diagram representation of the graph.
Returns:
Type | Description
---|---
|  A string containing the Mermaid diagram of the graph
Source code in `pydantic_graph/pydantic_graph/beta/graph.py`
```
298
299
300
301
302
303
304
```
| ```
def __str__(self) -> str:
    """Return a Mermaid diagram representation of the graph.
