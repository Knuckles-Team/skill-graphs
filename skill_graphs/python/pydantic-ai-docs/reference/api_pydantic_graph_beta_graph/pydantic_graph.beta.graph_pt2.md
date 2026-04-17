
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

    Returns:
        A string containing the Mermaid diagram of the graph
    """
    return self.render()

```

---|---
###  GraphTaskRequest `dataclass`
A request to run a task representing the execution of a node in the graph.
GraphTaskRequest encapsulates all the information needed to execute a specific node, including its inputs and the fork context it's executing within.
Source code in `pydantic_graph/pydantic_graph/beta/graph.py`
```
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
```
| ```
@dataclass
class GraphTaskRequest:
    """A request to run a task representing the execution of a node in the graph.

    GraphTaskRequest encapsulates all the information needed to execute a specific
    node, including its inputs and the fork context it's executing within.
    """

    node_id: NodeID
    """The ID of the node to execute."""

    inputs: Any
    """The input data for the node."""

    fork_stack: ForkStack = field(repr=False)
    """Stack of forks that have been entered.

    Used by the GraphRun to decide when to proceed through joins.
    """

```

---|---
####  node_id `instance-attribute`
```
node_id: NodeID

```

The ID of the node to execute.
####  inputs `instance-attribute`
```
inputs:

```

The input data for the node.
####  fork_stack `class-attribute` `instance-attribute`
```
fork_stack: ForkStack = (repr=False)

```

Stack of forks that have been entered.
Used by the GraphRun to decide when to proceed through joins.
###  GraphTask `dataclass`
Bases: `GraphTaskRequest[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.GraphTaskRequest "GraphTaskRequest



      dataclass
   \(pydantic_graph.beta.graph.GraphTaskRequest\)")`
A task representing the execution of a node in the graph.
GraphTask encapsulates all the information needed to execute a specific node, including its inputs and the fork context it's executing within, and has a unique ID to identify the task within the graph run.
Source code in `pydantic_graph/pydantic_graph/beta/graph.py`
```
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
```
| ```
@dataclass
class GraphTask(GraphTaskRequest):
    """A task representing the execution of a node in the graph.

    GraphTask encapsulates all the information needed to execute a specific
    node, including its inputs and the fork context it's executing within,
    and has a unique ID to identify the task within the graph run.
    """

    task_id: TaskID = field(repr=False)
    """Unique identifier for this task."""

    @staticmethod
    def from_request(request: GraphTaskRequest, get_task_id: Callable[[], TaskID]) -> GraphTask:
        # Don't call the get_task_id callable, this is already a task
        if isinstance(request, GraphTask):
            return request
        return GraphTask(request.node_id, request.inputs, request.fork_stack, get_task_id())

```

---|---
####  task_id `class-attribute` `instance-attribute`
```
task_id: TaskID = (repr=False)

```

Unique identifier for this task.
###  GraphRun
Bases: `StateT[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.StateT "StateT



      module-attribute
   \(pydantic_graph.beta.graph.StateT\)"), DepsT[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.DepsT "DepsT



      module-attribute
   \(pydantic_graph.beta.graph.DepsT\)"), OutputT[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.OutputT "OutputT



      module-attribute
   \(pydantic_graph.beta.graph.OutputT\)")]`
A single execution instance of a graph.
GraphRun manages the execution state for a single run of a graph, including task scheduling, fork/join coordination, and result tracking.
Class Type Parameters:
Name | Bound or Constraints | Description | Default
---|---|---|---
`StateT` |  |  The type of the graph state |  _required_
`DepsT` |  |  The type of the dependencies |  _required_
`OutputT` |  |  The type of the output data |  _required_
Source code in `pydantic_graph/pydantic_graph/beta/graph.py`
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
441
442
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
473
474
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
496
497
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
522
523
524
525
526
527
```
| ```
class GraphRun(Generic[StateT, DepsT, OutputT]):
    """A single execution instance of a graph.

    GraphRun manages the execution state for a single run of a graph,
    including task scheduling, fork/join coordination, and result tracking.

    Type Parameters:
        StateT: The type of the graph state
        DepsT: The type of the dependencies
        OutputT: The type of the output data
    """

    def __init__(
        self,
        graph: Graph[StateT, DepsT, InputT, OutputT],
        *,
        state: StateT,
        deps: DepsT,
        inputs: InputT,
        traceparent: str | None,
    ):
        """Initialize a graph run.

        Args:
            graph: The graph to execute
            state: The graph state instance
            deps: The dependencies instance
            inputs: The input data for the graph
            traceparent: Optional trace parent for instrumentation
        """
        self.graph = graph
        """The graph being executed."""

        self.state = state
        """The graph state instance."""

        self.deps = deps
        """The dependencies instance."""

        self.inputs = inputs
        """The initial input data."""

        self._active_reducers: dict[tuple[JoinID, NodeRunID], JoinState] = {}
        """Active reducers for join operations."""

        self._next: EndMarker[OutputT] | Sequence[GraphTask] | None = None
        """The next item to be processed."""

        self._next_task_id = 0
        self._next_node_run_id = 0
        initial_fork_stack: ForkStack = (ForkStackItem(StartNode.id, self._get_next_node_run_id(), 0),)
        self._first_task = GraphTask(
            node_id=StartNode.id, inputs=inputs, fork_stack=initial_fork_stack, task_id=self._get_next_task_id()
        )
        self._iterator_task_group = create_task_group()
        self._iterator_instance = _GraphIterator[StateT, DepsT, OutputT](
            self.graph,
            self.state,
            self.deps,
            self._iterator_task_group,
            self._get_next_node_run_id,
            self._get_next_task_id,
        )
        self._iterator = self._iterator_instance.iter_graph(self._first_task)

        self.__traceparent = traceparent
        self._async_exit_stack = AsyncExitStack()

    async def __aenter__(self):
        self._async_exit_stack.enter_context(_unwrap_exception_groups())
        await self._async_exit_stack.enter_async_context(self._iterator_task_group)
        await self._async_exit_stack.enter_async_context(self._iterator_context())
        return self

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any):
        await self._async_exit_stack.__aexit__(exc_type, exc_val, exc_tb)

    @asynccontextmanager
    async def _iterator_context(self):
        try:
            yield
        finally:
            self._iterator_instance.iter_stream_sender.close()
            self._iterator_instance.iter_stream_receiver.close()
            await self._iterator.aclose()

    @overload
    def _traceparent(self, *, required: Literal[False]) -> str | None: ...
    @overload
    def _traceparent(self) -> str: ...
    def _traceparent(self, *, required: bool = True) -> str | None:
        """Get the trace parent for instrumentation.

        Args:
            required: Whether to raise an error if no traceparent exists

        Returns:
            The traceparent string, or None if not required and not set

        Raises:
            GraphRuntimeError: If required is True and no traceparent exists
        """
        if self.__traceparent is None and required:  # pragma: no cover
            raise exceptions.GraphRuntimeError('No span was created for this graph run')
        return self.__traceparent

    def __aiter__(self) -> AsyncIterator[EndMarker[OutputT] | Sequence[GraphTask]]:
        """Return self as an async iterator.

        Returns:
            Self for async iteration
        """
        return self

    async def __anext__(self) -> EndMarker[OutputT] | Sequence[GraphTask]:
        """Get the next item in the async iteration.

        Returns:
            The next execution result from the graph
        """
        if self._next is None:
            self._next = await anext(self._iterator)
        else:
            self._next = await self._iterator.asend(self._next)
        return self._next

    async def next(
        self, value: EndMarker[OutputT] | Sequence[GraphTaskRequest] | None = None
    ) -> EndMarker[OutputT] | Sequence[GraphTask]:
        """Advance the graph execution by one step.

        This method allows for sending a value to the iterator, which is useful
        for resuming iteration or overriding intermediate results.

        Args:
            value: Optional value to send to the iterator

        Returns:
            The next execution result: either an EndMarker, or sequence of GraphTasks
        """
        if self._next is None:
            # Prevent `TypeError: can't send non-None value to a just-started async generator`
            # if `next` is called before the `first_node` has run.
            await anext(self)
        if value is not None:
            if isinstance(value, EndMarker):
                self._next = value
            else:
                self._next = [GraphTask.from_request(gtr, self._get_next_task_id) for gtr in value]
        return await anext(self)

    @property
    def next_task(self) -> EndMarker[OutputT] | Sequence[GraphTask]:
        """Get the next task(s) to be executed.

        Returns:
            The next execution item, or the initial task if none is set
        """
        return self._next or [self._first_task]

    @property
    def output(self) -> OutputT | None:
        """Get the final output if the graph has completed.

        Returns:
            The output value if execution is complete, None otherwise
        """
        if isinstance(self._next, EndMarker):
            return self._next.value
        return None

    def _get_next_task_id(self) -> TaskID:
        next_id = TaskID(f'task:{self._next_task_id}')
        self._next_task_id += 1
        return next_id

    def _get_next_node_run_id(self) -> NodeRunID:
        next_id = NodeRunID(f'task:{self._next_node_run_id}')
        self._next_node_run_id += 1
        return next_id

```

---|---
####  __init__
```
__init__(
    graph: Graph[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.Graph "Graph



      dataclass
   \(pydantic_graph.beta.graph.Graph\)")[StateT[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.StateT "StateT



      module-attribute
   \(pydantic_graph.beta.graph.StateT\)"), DepsT[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.DepsT "DepsT



      module-attribute
   \(pydantic_graph.beta.graph.DepsT\)"), InputT[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.InputT "InputT



      module-attribute
   \(pydantic_graph.beta.graph.InputT\)"), OutputT[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.OutputT "OutputT



      module-attribute
   \(pydantic_graph.beta.graph.OutputT\)")],
    *,
    state: StateT[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.StateT "StateT



      module-attribute
   \(pydantic_graph.beta.graph.StateT\)"),
    deps: DepsT[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.DepsT "DepsT



      module-attribute
   \(pydantic_graph.beta.graph.DepsT\)"),
    inputs: InputT[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.InputT "InputT



      module-attribute
   \(pydantic_graph.beta.graph.InputT\)"),
    traceparent:  | None
)

```

Initialize a graph run.
Parameters:
Name | Type | Description | Default
---|---|---|---
`graph` |  `Graph[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.Graph "Graph



      dataclass
   \(pydantic_graph.beta.graph.Graph\)")[StateT[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.StateT "StateT



      module-attribute
   \(pydantic_graph.beta.graph.StateT\)"), DepsT[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.DepsT "DepsT



      module-attribute
   \(pydantic_graph.beta.graph.DepsT\)"), InputT[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.InputT "InputT



      module-attribute
   \(pydantic_graph.beta.graph.InputT\)"), OutputT[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.OutputT "OutputT



      module-attribute
   \(pydantic_graph.beta.graph.OutputT\)")]` |  The graph to execute |  _required_
`state` |  `StateT[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.StateT "StateT



      module-attribute
   \(pydantic_graph.beta.graph.StateT\)")` |  The graph state instance |  _required_
`deps` |  `DepsT[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.DepsT "DepsT



      module-attribute
   \(pydantic_graph.beta.graph.DepsT\)")` |  The dependencies instance |  _required_
`inputs` |  `InputT[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.InputT "InputT



      module-attribute
   \(pydantic_graph.beta.graph.InputT\)")` |  The input data for the graph |  _required_
`traceparent` |  |  Optional trace parent for instrumentation |  _required_
Source code in `pydantic_graph/pydantic_graph/beta/graph.py`
```
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
```
| ```
def __init__(
    self,
    graph: Graph[StateT, DepsT, InputT, OutputT],
    *,
    state: StateT,
    deps: DepsT,
    inputs: InputT,
    traceparent: str | None,
):
    """Initialize a graph run.

    Args:
        graph: The graph to execute
        state: The graph state instance
        deps: The dependencies instance
        inputs: The input data for the graph
        traceparent: Optional trace parent for instrumentation
    """
    self.graph = graph
    """The graph being executed."""

    self.state = state
    """The graph state instance."""

    self.deps = deps
    """The dependencies instance."""

    self.inputs = inputs
    """The initial input data."""

    self._active_reducers: dict[tuple[JoinID, NodeRunID], JoinState] = {}
    """Active reducers for join operations."""

    self._next: EndMarker[OutputT] | Sequence[GraphTask] | None = None
    """The next item to be processed."""

    self._next_task_id = 0
    self._next_node_run_id = 0
    initial_fork_stack: ForkStack = (ForkStackItem(StartNode.id, self._get_next_node_run_id(), 0),)
    self._first_task = GraphTask(
        node_id=StartNode.id, inputs=inputs, fork_stack=initial_fork_stack, task_id=self._get_next_task_id()
    )
    self._iterator_task_group = create_task_group()
    self._iterator_instance = _GraphIterator[StateT, DepsT, OutputT](
        self.graph,
        self.state,
        self.deps,
        self._iterator_task_group,
        self._get_next_node_run_id,
        self._get_next_task_id,
    )
    self._iterator = self._iterator_instance.iter_graph(self._first_task)

    self.__traceparent = traceparent
    self._async_exit_stack = AsyncExitStack()

```

---|---
####  graph `instance-attribute`
```
graph = graph

```

The graph being executed.
####  state `instance-attribute`
```
state = state

```

The graph state instance.
####  deps `instance-attribute`
```
deps = deps

```

The dependencies instance.
####  inputs `instance-attribute`
```
inputs = inputs

```

The initial input data.
####  __aiter__
```
__aiter__() -> (
    [EndMarker[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.EndMarker "EndMarker



      dataclass
   \(pydantic_graph.beta.graph.EndMarker\)")[OutputT[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.OutputT "OutputT



      module-attribute
   \(pydantic_graph.beta.graph.OutputT\)")] | [GraphTask[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.GraphTask "GraphTask



      dataclass
   \(pydantic_graph.beta.graph.GraphTask\)")]]
)

```

Return self as an async iterator.
Returns:
Type | Description
---|---
`EndMarker[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.EndMarker "EndMarker



      dataclass
   \(pydantic_graph.beta.graph.EndMarker\)")[OutputT[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.OutputT "OutputT



      module-attribute
   \(pydantic_graph.beta.graph.OutputT\)")] | GraphTask[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.GraphTask "GraphTask



      dataclass
   \(pydantic_graph.beta.graph.GraphTask\)")]]` |  Self for async iteration
Source code in `pydantic_graph/pydantic_graph/beta/graph.py`
```
454
455
456
457
458
459
460
```
| ```
def __aiter__(self) -> AsyncIterator[EndMarker[OutputT] | Sequence[GraphTask]]:
    """Return self as an async iterator.

    Returns:
        Self for async iteration
    """
    return self

```

---|---
####  __anext__ `async`
```
__anext__() -> EndMarker[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.EndMarker "EndMarker



      dataclass
   \(pydantic_graph.beta.graph.EndMarker\)")[OutputT[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.OutputT "OutputT



      module-attribute
   \(pydantic_graph.beta.graph.OutputT\)")] | [GraphTask[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.GraphTask "GraphTask



      dataclass
   \(pydantic_graph.beta.graph.GraphTask\)")]

```

Get the next item in the async iteration.
Returns:
Type | Description
---|---
`EndMarker[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.EndMarker "EndMarker



      dataclass
   \(pydantic_graph.beta.graph.EndMarker\)")[OutputT[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.OutputT "OutputT



      module-attribute
   \(pydantic_graph.beta.graph.OutputT\)")] | GraphTask[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.GraphTask "GraphTask



      dataclass
   \(pydantic_graph.beta.graph.GraphTask\)")]` |  The next execution result from the graph
Source code in `pydantic_graph/pydantic_graph/beta/graph.py`
```
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
async def __anext__(self) -> EndMarker[OutputT] | Sequence[GraphTask]:
    """Get the next item in the async iteration.

    Returns:
        The next execution result from the graph
    """
    if self._next is None:
        self._next = await anext(self._iterator)
    else:
        self._next = await self._iterator.asend(self._next)
    return self._next

```

---|---
####  next `async`
```
next(
    value: (
        EndMarker[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.EndMarker "EndMarker



      dataclass
   \(pydantic_graph.beta.graph.EndMarker\)")[OutputT[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.OutputT "OutputT



      module-attribute
   \(pydantic_graph.beta.graph.OutputT\)")]
        | [GraphTaskRequest[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.GraphTaskRequest "GraphTaskRequest



      dataclass
   \(pydantic_graph.beta.graph.GraphTaskRequest\)")]
        | None
    ) = None,
) -> EndMarker[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.EndMarker "EndMarker



      dataclass
   \(pydantic_graph.beta.graph.EndMarker\)")[OutputT[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.OutputT "OutputT



      module-attribute
   \(pydantic_graph.beta.graph.OutputT\)")] | [GraphTask[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.GraphTask "GraphTask



      dataclass
   \(pydantic_graph.beta.graph.GraphTask\)")]

```

Advance the graph execution by one step.
This method allows for sending a value to the iterator, which is useful for resuming iteration or overriding intermediate results.
Parameters:
Name | Type | Description | Default
---|---|---|---
`value` |  `EndMarker[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.EndMarker "EndMarker



      dataclass
   \(pydantic_graph.beta.graph.EndMarker\)")[OutputT[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.OutputT "OutputT



      module-attribute
   \(pydantic_graph.beta.graph.OutputT\)")] | GraphTaskRequest[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.GraphTaskRequest "GraphTaskRequest



      dataclass
   \(pydantic_graph.beta.graph.GraphTaskRequest\)")] | None` |  Optional value to send to the iterator |  `None`
Returns:
Type | Description
---|---
`EndMarker[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.EndMarker "EndMarker



      dataclass
   \(pydantic_graph.beta.graph.EndMarker\)")[OutputT[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.OutputT "OutputT



      module-attribute
   \(pydantic_graph.beta.graph.OutputT\)")] | GraphTask[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.GraphTask "GraphTask
