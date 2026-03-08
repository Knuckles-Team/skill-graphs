            decision = self.decision()
            for destination in destinations:
                # We don't actually use this decision mechanism, but we need to build the edges for parent-fork finding
                decision = decision.branch(self.match(NoneType).to(destination))
            return edge.to(decision)

    # Graph building
    def build(self, validate_graph_structure: bool = True) -> Graph[StateT, DepsT, GraphInputT, GraphOutputT]:
        """Build the final executable graph from the accumulated nodes and edges.

        This method performs validation, normalization, and analysis of the graph
        structure to create a complete, executable graph instance.

        Args:
            validate_graph_structure: whether to perform validation of the graph structure
                See the docstring of _validate_graph_structure below for more details.

        Returns:
            A complete Graph instance ready for execution

        Raises:
            ValueError: If the graph structure is invalid (e.g., join without parent fork)
        """
        nodes = self._nodes
        edges_by_source = self._edges_by_source

        nodes, edges_by_source = _replace_placeholder_node_ids(nodes, edges_by_source)
        nodes, edges_by_source = _flatten_paths(nodes, edges_by_source)
        nodes, edges_by_source = _normalize_forks(nodes, edges_by_source)
        if validate_graph_structure:
            _validate_graph_structure(nodes, edges_by_source)
        parent_forks = _collect_dominating_forks(nodes, edges_by_source)
        intermediate_join_nodes = _compute_intermediate_join_nodes(nodes, parent_forks)

        return Graph[StateT, DepsT, GraphInputT, GraphOutputT](
            name=self.name,
            state_type=unpack_type_expression(self.state_type),
            deps_type=unpack_type_expression(self.deps_type),
            input_type=unpack_type_expression(self.input_type),
            output_type=unpack_type_expression(self.output_type),
            nodes=nodes,
            edges_by_source=edges_by_source,
            parent_forks=parent_forks,
            intermediate_join_nodes=intermediate_join_nodes,
            auto_instrument=self.auto_instrument,
        )

```

---|---
####  __init__
```
__init__(
    *,
    name:  | None = None,
    state_type: TypeOrTypeExpression[StateT] = ,
    deps_type: TypeOrTypeExpression[DepsT] = ,
    input_type: TypeOrTypeExpression[
        GraphInputT
    ] = ,
    output_type: TypeOrTypeExpression[
        GraphOutputT
    ] = ,
    auto_instrument:  = True
)

```

Initialize a graph builder.
Parameters:
Name | Type | Description | Default
---|---|---|---
`name` |  |  Optional name for the graph, if not provided the name will be inferred from the calling frame on the first call to a graph method. |  `None`
`state_type` |  `TypeOrTypeExpression[StateT]` |  The type of the graph state |
`deps_type` |  `TypeOrTypeExpression[DepsT]` |  The type of the dependencies |
`input_type` |  `TypeOrTypeExpression[GraphInputT]` |  The type of the graph input data |
`output_type` |  `TypeOrTypeExpression[GraphOutputT]` |  The type of the graph output data |
`auto_instrument` |  |  Whether to automatically create instrumentation spans |  `True`
Source code in `pydantic_graph/pydantic_graph/beta/graph_builder.py`
```
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
```
| ```
def __init__(
    self,
    *,
    name: str | None = None,
    state_type: TypeOrTypeExpression[StateT] = NoneType,
    deps_type: TypeOrTypeExpression[DepsT] = NoneType,
    input_type: TypeOrTypeExpression[GraphInputT] = NoneType,
    output_type: TypeOrTypeExpression[GraphOutputT] = NoneType,
    auto_instrument: bool = True,
):
    """Initialize a graph builder.

    Args:
        name: Optional name for the graph, if not provided the name will be inferred from the calling frame on the first call to a graph method.
        state_type: The type of the graph state
        deps_type: The type of the dependencies
        input_type: The type of the graph input data
        output_type: The type of the graph output data
        auto_instrument: Whether to automatically create instrumentation spans
    """
    self.name = name

    self.state_type = state_type
    self.deps_type = deps_type
    self.input_type = input_type
    self.output_type = output_type

    self.auto_instrument = auto_instrument

    self._nodes = {}
    self._edges_by_source = defaultdict(list)
    self._decision_index = 1

    self._start_node = StartNode[GraphInputT]()
    self._end_node = EndNode[GraphOutputT]()

```

---|---
####  name `instance-attribute`
```
name:  | None = name

```

Optional name for the graph, if not provided the name will be inferred from the calling frame on the first call to a graph method.
####  state_type `instance-attribute`
```
state_type: TypeOrTypeExpression[StateT] = state_type

```

The type of the graph state.
####  deps_type `instance-attribute`
```
deps_type: TypeOrTypeExpression[DepsT] = deps_type

```

The type of the dependencies.
####  input_type `instance-attribute`
```
input_type: TypeOrTypeExpression[GraphInputT] = input_type

```

The type of the graph input data.
####  output_type `instance-attribute`
```
output_type: TypeOrTypeExpression[GraphOutputT] = (
    output_type
)

```

The type of the graph output data.
####  auto_instrument `instance-attribute`
```
auto_instrument:  = auto_instrument

```

Whether to automatically create instrumentation spans.
####  start_node `property`
```
start_node: StartNode[](https://ai.pydantic.dev/api/pydantic_graph/beta_node/#pydantic_graph.beta.node.StartNode "StartNode \(pydantic_graph.beta.node.StartNode\)")[GraphInputT]

```

Get the start node for the graph.
Returns:
Type | Description
---|---
`StartNode[](https://ai.pydantic.dev/api/pydantic_graph/beta_node/#pydantic_graph.beta.node.StartNode "StartNode \(pydantic_graph.beta.node.StartNode\)")[GraphInputT]` |  The start node that receives the initial graph input
####  end_node `property`
```
end_node: EndNode[](https://ai.pydantic.dev/api/pydantic_graph/beta_node/#pydantic_graph.beta.node.EndNode "EndNode \(pydantic_graph.beta.node.EndNode\)")[GraphOutputT]

```

Get the end node for the graph.
Returns:
Type | Description
---|---
`EndNode[](https://ai.pydantic.dev/api/pydantic_graph/beta_node/#pydantic_graph.beta.node.EndNode "EndNode \(pydantic_graph.beta.node.EndNode\)")[GraphOutputT]` |  The end node that produces the final graph output
####  step
```
step(
    *, node_id:  | None = None, label:  | None = None
) -> [
    [StepFunction[](https://ai.pydantic.dev/api/pydantic_graph/beta_step/#pydantic_graph.beta.step.StepFunction "StepFunction \(pydantic_graph.beta.step.StepFunction\)")[StateT, DepsT, InputT, OutputT]],
    Step[](https://ai.pydantic.dev/api/pydantic_graph/beta_step/#pydantic_graph.beta.step.Step "Step



      dataclass
   \(pydantic_graph.beta.step.Step\)")[StateT, DepsT, InputT, OutputT],
]

```

```
step(
    call: StepFunction[](https://ai.pydantic.dev/api/pydantic_graph/beta_step/#pydantic_graph.beta.step.StepFunction "StepFunction \(pydantic_graph.beta.step.StepFunction\)")[StateT, DepsT, InputT, OutputT],
    *,
    node_id:  | None = None,
    label:  | None = None
) -> Step[](https://ai.pydantic.dev/api/pydantic_graph/beta_step/#pydantic_graph.beta.step.Step "Step



      dataclass
   \(pydantic_graph.beta.step.Step\)")[StateT, DepsT, InputT, OutputT]

```

```
step(
    call: (
        StepFunction[](https://ai.pydantic.dev/api/pydantic_graph/beta_step/#pydantic_graph.beta.step.StepFunction "StepFunction \(pydantic_graph.beta.step.StepFunction\)")[StateT, DepsT, InputT, OutputT] | None
    ) = None,
    *,
    node_id:  | None = None,
    label:  | None = None
) -> (
    Step[](https://ai.pydantic.dev/api/pydantic_graph/beta_step/#pydantic_graph.beta.step.Step "Step



      dataclass
   \(pydantic_graph.beta.step.Step\)")[StateT, DepsT, InputT, OutputT]
    | [
        [StepFunction[](https://ai.pydantic.dev/api/pydantic_graph/beta_step/#pydantic_graph.beta.step.StepFunction "StepFunction \(pydantic_graph.beta.step.StepFunction\)")[StateT, DepsT, InputT, OutputT]],
        Step[](https://ai.pydantic.dev/api/pydantic_graph/beta_step/#pydantic_graph.beta.step.Step "Step



      dataclass
   \(pydantic_graph.beta.step.Step\)")[StateT, DepsT, InputT, OutputT],
    ]
)

```

Create a step from a step function.
This method can be used as a decorator or called directly to create a step node from an async function.
Parameters:
Name | Type | Description | Default
---|---|---|---
`call` |  `StepFunction[](https://ai.pydantic.dev/api/pydantic_graph/beta_step/#pydantic_graph.beta.step.StepFunction "StepFunction \(pydantic_graph.beta.step.StepFunction\)")[StateT, DepsT, InputT, OutputT] | None` |  The step function to wrap |  `None`
`node_id` |  |  Optional ID for the node |  `None`
`label` |  |  Optional human-readable label |  `None`
Returns:
Type | Description
---|---
`Step[](https://ai.pydantic.dev/api/pydantic_graph/beta_step/#pydantic_graph.beta.step.Step "Step



      dataclass
   \(pydantic_graph.beta.step.Step\)")[StateT, DepsT, InputT, OutputT] | StepFunction[](https://ai.pydantic.dev/api/pydantic_graph/beta_step/#pydantic_graph.beta.step.StepFunction "StepFunction \(pydantic_graph.beta.step.StepFunction\)")[StateT, DepsT, InputT, OutputT]], Step[](https://ai.pydantic.dev/api/pydantic_graph/beta_step/#pydantic_graph.beta.step.Step "Step



      dataclass
   \(pydantic_graph.beta.step.Step\)")[StateT, DepsT, InputT, OutputT]]` |  Either a Step instance or a decorator function
Source code in `pydantic_graph/pydantic_graph/beta/graph_builder.py`
```
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
```
| ```
def step(
    self,
    call: StepFunction[StateT, DepsT, InputT, OutputT] | None = None,
    *,
    node_id: str | None = None,
    label: str | None = None,
) -> (
    Step[StateT, DepsT, InputT, OutputT]
    | Callable[[StepFunction[StateT, DepsT, InputT, OutputT]], Step[StateT, DepsT, InputT, OutputT]]
):
    """Create a step from a step function.

    This method can be used as a decorator or called directly to create
    a step node from an async function.

    Args:
        call: The step function to wrap
        node_id: Optional ID for the node
        label: Optional human-readable label

    Returns:
        Either a Step instance or a decorator function
    """
    if call is None:

        def decorator(
            func: StepFunction[StateT, DepsT, InputT, OutputT],
        ) -> Step[StateT, DepsT, InputT, OutputT]:
            return self.step(call=func, node_id=node_id, label=label)

        return decorator

    node_id = node_id or get_callable_name(call)

    step = Step[StateT, DepsT, InputT, OutputT](id=NodeID(node_id), call=call, label=label)

    return step

```

---|---
####  stream
```
stream(
    *, node_id:  | None = None, label:  | None = None
) -> [
    [StreamFunction[](https://ai.pydantic.dev/api/pydantic_graph/beta_step/#pydantic_graph.beta.step.StreamFunction "StreamFunction \(pydantic_graph.beta.step.StreamFunction\)")[StateT, DepsT, InputT, OutputT]],
    Step[](https://ai.pydantic.dev/api/pydantic_graph/beta_step/#pydantic_graph.beta.step.Step "Step



      dataclass
   \(pydantic_graph.beta.step.Step\)")[StateT, DepsT, InputT, [OutputT]],
]

```

```
stream(
    call: StreamFunction[](https://ai.pydantic.dev/api/pydantic_graph/beta_step/#pydantic_graph.beta.step.StreamFunction "StreamFunction \(pydantic_graph.beta.step.StreamFunction\)")[StateT, DepsT, InputT, OutputT],
    *,
    node_id:  | None = None,
    label:  | None = None
) -> Step[](https://ai.pydantic.dev/api/pydantic_graph/beta_step/#pydantic_graph.beta.step.Step "Step



      dataclass
   \(pydantic_graph.beta.step.Step\)")[StateT, DepsT, InputT, [OutputT]]

```

```
stream(
    call: (
        StreamFunction[](https://ai.pydantic.dev/api/pydantic_graph/beta_step/#pydantic_graph.beta.step.StreamFunction "StreamFunction \(pydantic_graph.beta.step.StreamFunction\)")[StateT, DepsT, InputT, OutputT]
        | None
    ) = None,
    *,
    node_id:  | None = None,
    label:  | None = None
) -> (
    Step[](https://ai.pydantic.dev/api/pydantic_graph/beta_step/#pydantic_graph.beta.step.Step "Step



      dataclass
   \(pydantic_graph.beta.step.Step\)")[StateT, DepsT, InputT, [OutputT]]
    | [
        [StreamFunction[](https://ai.pydantic.dev/api/pydantic_graph/beta_step/#pydantic_graph.beta.step.StreamFunction "StreamFunction \(pydantic_graph.beta.step.StreamFunction\)")[StateT, DepsT, InputT, OutputT]],
        Step[](https://ai.pydantic.dev/api/pydantic_graph/beta_step/#pydantic_graph.beta.step.Step "Step



      dataclass
   \(pydantic_graph.beta.step.Step\)")[StateT, DepsT, InputT, [OutputT]],
    ]
)

```

```
stream(
    call: (
        StreamFunction[](https://ai.pydantic.dev/api/pydantic_graph/beta_step/#pydantic_graph.beta.step.StreamFunction "StreamFunction \(pydantic_graph.beta.step.StreamFunction\)")[StateT, DepsT, InputT, OutputT]
        | None
    ) = None,
    *,
    node_id:  | None = None,
    label:  | None = None
) -> (
    Step[](https://ai.pydantic.dev/api/pydantic_graph/beta_step/#pydantic_graph.beta.step.Step "Step



      dataclass
   \(pydantic_graph.beta.step.Step\)")[StateT, DepsT, InputT, [OutputT]]
    | [
        [StreamFunction[](https://ai.pydantic.dev/api/pydantic_graph/beta_step/#pydantic_graph.beta.step.StreamFunction "StreamFunction \(pydantic_graph.beta.step.StreamFunction\)")[StateT, DepsT, InputT, OutputT]],
        Step[](https://ai.pydantic.dev/api/pydantic_graph/beta_step/#pydantic_graph.beta.step.Step "Step



      dataclass
   \(pydantic_graph.beta.step.Step\)")[StateT, DepsT, InputT, [OutputT]],
    ]
)

```

Create a step from an async iterator (which functions like a "stream").
This method can be used as a decorator or called directly to create a step node from an async function.
Parameters:
Name | Type | Description | Default
---|---|---|---
`call` |  `StreamFunction[](https://ai.pydantic.dev/api/pydantic_graph/beta_step/#pydantic_graph.beta.step.StreamFunction "StreamFunction \(pydantic_graph.beta.step.StreamFunction\)")[StateT, DepsT, InputT, OutputT] | None` |  The step function to wrap |  `None`
`node_id` |  |  Optional ID for the node |  `None`
`label` |  |  Optional human-readable label |  `None`
Returns:
Type | Description
---|---
`Step[](https://ai.pydantic.dev/api/pydantic_graph/beta_step/#pydantic_graph.beta.step.Step "Step



      dataclass
   \(pydantic_graph.beta.step.Step\)")[StateT, DepsT, InputT, OutputT]] | StreamFunction[](https://ai.pydantic.dev/api/pydantic_graph/beta_step/#pydantic_graph.beta.step.StreamFunction "StreamFunction \(pydantic_graph.beta.step.StreamFunction\)")[StateT, DepsT, InputT, OutputT]], Step[](https://ai.pydantic.dev/api/pydantic_graph/beta_step/#pydantic_graph.beta.step.Step "Step



      dataclass
   \(pydantic_graph.beta.step.Step\)")[StateT, DepsT, InputT, OutputT]]]` |  Either a Step instance or a decorator function
Source code in `pydantic_graph/pydantic_graph/beta/graph_builder.py`
```
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
```
| ```
def stream(
    self,
    call: StreamFunction[StateT, DepsT, InputT, OutputT] | None = None,
    *,
    node_id: str | None = None,
    label: str | None = None,
) -> (
    Step[StateT, DepsT, InputT, AsyncIterable[OutputT]]
    | Callable[
        [StreamFunction[StateT, DepsT, InputT, OutputT]],
        Step[StateT, DepsT, InputT, AsyncIterable[OutputT]],
    ]
):
    """Create a step from an async iterator (which functions like a "stream").

    This method can be used as a decorator or called directly to create
    a step node from an async function.

    Args:
        call: The step function to wrap
        node_id: Optional ID for the node
        label: Optional human-readable label

    Returns:
        Either a Step instance or a decorator function
    """
    if call is None:

        def decorator(
            func: StreamFunction[StateT, DepsT, InputT, OutputT],
        ) -> Step[StateT, DepsT, InputT, AsyncIterable[OutputT]]:
            return self.stream(call=func, node_id=node_id, label=label)

        return decorator

    # We need to wrap the call so that we can call `await` even though the result is an async iterator
    async def wrapper(ctx: StepContext[StateT, DepsT, InputT]):
        return call(ctx)

    node_id = node_id or get_callable_name(call)

    return self.step(call=wrapper, node_id=node_id, label=label)

```

---|---
####  add
```
add(*edges: EdgePath[StateT, DepsT]) -> None

```

Add one or more edge paths to the graph.
This method processes edge paths and automatically creates any necessary fork nodes for broadcasts and maps.
Parameters:
Name | Type | Description | Default
---|---|---|---
`*edges` |  `EdgePath[StateT, DepsT]` |  The edge paths to add to the graph |  `()`
Source code in `pydantic_graph/pydantic_graph/beta/graph_builder.py`
```
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
```
| ```
def add(self, *edges: EdgePath[StateT, DepsT]) -> None:  # noqa: C901
    """Add one or more edge paths to the graph.

    This method processes edge paths and automatically creates any necessary
    fork nodes for broadcasts and maps.

    Args:
        *edges: The edge paths to add to the graph
    """

    def _handle_path(p: Path):
        """Process a path and create necessary fork nodes.

        Args:
            p: The path to process
        """
        for item in p.items:
            if isinstance(item, BroadcastMarker):
                new_node = Fork[Any, Any](id=item.fork_id, is_map=False, downstream_join_id=None)
                self._insert_node(new_node)
                for path in item.paths:
                    _handle_path(Path(items=[*path.items]))
            elif isinstance(item, MapMarker):
                new_node = Fork[Any, Any](id=item.fork_id, is_map=True, downstream_join_id=item.downstream_join_id)
                self._insert_node(new_node)
            elif isinstance(item, DestinationMarker):
                pass

    def _handle_destination_node(d: AnyDestinationNode):
        if id(d) in destination_ids:
            return  # prevent infinite recursion if there is a cycle of decisions

        destination_ids.add(id(d))
        destinations.append(d)
        self._insert_node(d)
        if isinstance(d, Decision):
            for branch in d.branches:
                _handle_path(branch.path)
                for d2 in branch.destinations:
                    _handle_destination_node(d2)

    destination_ids = set[int]()
    destinations: list[AnyDestinationNode] = []
    for edge in edges:
        for source_node in edge.sources:
            self._insert_node(source_node)
            self._edges_by_source[source_node.id].append(edge.path)
        for destination_node in edge.destinations:
            _handle_destination_node(destination_node)
        _handle_path(edge.path)

    # Automatically create edges from step function return hints including `BaseNode`s
    for destination in destinations:
        if not isinstance(destination, Step) or isinstance(destination, NodeStep):
            continue
        parent_namespace = _utils.get_parent_namespace(inspect.currentframe())
        type_hints = get_type_hints(destination.call, localns=parent_namespace, include_extras=True)
        try:
            return_hint = type_hints['return']
        except KeyError:
            pass
        else:
            edge = self._edge_from_return_hint(destination, return_hint)
            if edge is not None:
                self.add(edge)

```

---|---
####  add_edge
```
add_edge(
    source: Source[T],
    destination: Destination[T],
    *,
    label:  | None = None
) -> None

```

Add a simple edge between two nodes.
Parameters:
Name | Type | Description | Default
---|---|---|---
`source` |  `Source[T]` |  The source node |  _required_
`destination` |  `Destination[T]` |  The destination node |  _required_
`label` |  |  Optional label for the edge |  `None`
Source code in `pydantic_graph/pydantic_graph/beta/graph_builder.py`
```
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
def add_edge(self, source: Source[T], destination: Destination[T], *, label: str | None = None) -> None:
    """Add a simple edge between two nodes.

    Args:
        source: The source node
        destination: The destination node
        label: Optional label for the edge
    """
    builder = self.edge_from(source)
    if label is not None:
        builder = builder.label(label)
    self.add(builder.to(destination))

```

---|---
####  add_mapping_edge
```
add_mapping_edge(
    source: Source[[T]],
    map_to: Destination[T],
    *,
    pre_map_label:  | None = None,
    post_map_label:  | None = None,
    fork_id: ForkID | None = None,
    downstream_join_id: JoinID | None = None
) -> None

```

Add an edge that maps iterable data across parallel paths.
Parameters:
Name | Type | Description | Default
---|---|---|---
`source` |  `Source[T]]` |  The source node that produces iterable data |  _required_
`map_to` |  `Destination[T]` |  The destination node that receives individual items |  _required_
`pre_map_label` |  |  Optional label before the map operation |  `None`
`post_map_label` |  |  Optional label after the map operation |  `None`
`fork_id` |  `ForkID | None` |  Optional ID for the fork node produced for this map operation |  `None`
`downstream_join_id` |  `JoinID | None` |  Optional ID of a join node that will always be downstream of this map. Specifying this ensures correct handling if you try to map an empty iterable. |  `None`
Source code in `pydantic_graph/pydantic_graph/beta/graph_builder.py`
```
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
def add_mapping_edge(
    self,
    source: Source[Iterable[T]],
    map_to: Destination[T],
    *,
    pre_map_label: str | None = None,
    post_map_label: str | None = None,
    fork_id: ForkID | None = None,
    downstream_join_id: JoinID | None = None,
) -> None:
    """Add an edge that maps iterable data across parallel paths.

    Args:
        source: The source node that produces iterable data
        map_to: The destination node that receives individual items
        pre_map_label: Optional label before the map operation
        post_map_label: Optional label after the map operation
        fork_id: Optional ID for the fork node produced for this map operation
        downstream_join_id: Optional ID of a join node that will always be downstream of this map.
            Specifying this ensures correct handling if you try to map an empty iterable.
    """
    builder = self.edge_from(source)
    if pre_map_label is not None:
        builder = builder.label(pre_map_label)
    builder = builder.map(fork_id=fork_id, downstream_join_id=downstream_join_id)
    if post_map_label is not None:
        builder = builder.label(post_map_label)
    self.add(builder.to(map_to))

```

---|---
####  edge_from
```
edge_from(
    *sources: Source[SourceOutputT],
) -> EdgePathBuilder[StateT, DepsT, SourceOutputT]

```

Create an edge path builder starting from the given source nodes.
Parameters:
Name | Type | Description | Default
---|---|---|---
`*sources` |  `Source[SourceOutputT]` |  The source nodes to start the edge path from |  `()`
Returns:
Type | Description
---|---
`EdgePathBuilder[StateT, DepsT, SourceOutputT]` |  An EdgePathBuilder for constructing the complete edge path
Source code in `pydantic_graph/pydantic_graph/beta/graph_builder.py`
```
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
def edge_from(self, *sources: Source[SourceOutputT]) -> EdgePathBuilder[StateT, DepsT, SourceOutputT]:
    """Create an edge path builder starting from the given source nodes.

    Args:
        *sources: The source nodes to start the edge path from

    Returns:
        An EdgePathBuilder for constructing the complete edge path
    """
    return EdgePathBuilder[StateT, DepsT, SourceOutputT](
        sources=sources, path_builder=PathBuilder(working_items=[])
    )

```

---|---
####  decision
```
decision(
    *, note:  | None = None, node_id:  | None = None
) -> Decision[](https://ai.pydantic.dev/api/pydantic_graph/beta_decision/#pydantic_graph.beta.decision.Decision "Decision



      dataclass
   \(pydantic_graph.beta.decision.Decision\)")[StateT, DepsT, ]

```

Create a new decision node.
Parameters:
Name | Type | Description | Default
---|---|---|---
`note` |  |  Optional note to describe the decision logic |  `None`
`node_id` |  |  Optional ID for the node produced for this decision logic |  `None`
Returns:
Type | Description
---|---
`Decision[](https://ai.pydantic.dev/api/pydantic_graph/beta_decision/#pydantic_graph.beta.decision.Decision "Decision
