) -> AsyncIterator[GraphRun[StateT, DepsT, RunEndT]]:
    """A contextmanager which can be used to iterate over the graph's nodes as they are executed.

    This method returns a `GraphRun` object which can be used to async-iterate over the nodes of this `Graph` as
    they are executed. This is the API to use if you want to record or interact with the nodes as the graph
    execution unfolds.

    The `GraphRun` can also be used to manually drive the graph execution by calling
    [`GraphRun.next`][pydantic_graph.graph.GraphRun.next].

    The `GraphRun` provides access to the full run history, state, deps, and the final result of the run once
    it has completed.

    For more details, see the API documentation of [`GraphRun`][pydantic_graph.graph.GraphRun].

    Args:
        start_node: the first node to run. Since the graph definition doesn't define the entry point in the graph,
            you need to provide the starting node.
        state: The initial state of the graph.
        deps: The dependencies of the graph.
        persistence: State persistence interface, defaults to
            [`SimpleStatePersistence`][pydantic_graph.SimpleStatePersistence] if `None`.
        span: The span to use for the graph run. If not provided, a new span will be created.
        infer_name: Whether to infer the graph name from the calling frame.

    Returns: A GraphRun that can be async iterated over to drive the graph to completion.
    """
    if infer_name and self.name is None:
        # f_back because `asynccontextmanager` adds one frame
        if frame := inspect.currentframe():  # pragma: no branch
            self._infer_name(frame.f_back)

    if persistence is None:
        persistence = SimpleStatePersistence()
    persistence.set_graph_types(self)

    with ExitStack() as stack:
        entered_span: AbstractSpan | None = None
        if span is None:
            if self.auto_instrument:  # pragma: no branch
                # Separate variable because we actually don't want logfire's f-string magic here,
                # we want the span_name to be preformatted for other backends
                # as requested in https://github.com/pydantic/pydantic-ai/issues/3173.
                span_name = f'run graph {self.name}'
                entered_span = stack.enter_context(logfire_span(span_name, graph=self))
        else:
            entered_span = stack.enter_context(span)
        traceparent = None if entered_span is None else get_traceparent(entered_span)
        yield GraphRun[StateT, DepsT, RunEndT](
            graph=self,
            start_node=start_node,
            persistence=persistence,
            state=state,
            deps=deps,
            traceparent=traceparent,
        )

```

---|---
####  iter_from_persistence `async`
```
iter_from_persistence(
    persistence: BaseStatePersistence[](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.BaseStatePersistence "BaseStatePersistence \(pydantic_graph.persistence.BaseStatePersistence\)")[StateT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.StateT "StateT



      module-attribute
   \(pydantic_graph.nodes.StateT\)"), RunEndT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.RunEndT "RunEndT



      module-attribute
   \(pydantic_graph.nodes.RunEndT\)")],
    *,
    deps: DepsT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.DepsT "DepsT



      module-attribute
   \(pydantic_graph.nodes.DepsT\)") = None,
    span: (
        [AbstractSpan] | None
    ) = None,
    infer_name:  = True
) -> [GraphRun[](https://ai.pydantic.dev/api/pydantic_graph/graph/#pydantic_graph.graph.GraphRun "GraphRun \(pydantic_graph.graph.GraphRun\)")[StateT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.StateT "StateT



      module-attribute
   \(pydantic_graph.nodes.StateT\)"), DepsT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.DepsT "DepsT



      module-attribute
   \(pydantic_graph.nodes.DepsT\)"), RunEndT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.RunEndT "RunEndT



      module-attribute
   \(pydantic_graph.nodes.RunEndT\)")]]

```

A contextmanager to iterate over the graph's nodes as they are executed, created from a persistence object.
This method has similar functionality to [`iter`](https://ai.pydantic.dev/api/pydantic_graph/graph/#pydantic_graph.graph.Graph.iter "iter



      async
  "), but instead of passing the node to run, it will restore the node and state from state persistence.
Parameters:
Name | Type | Description | Default
---|---|---|---
`persistence` |  `BaseStatePersistence[](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.BaseStatePersistence "BaseStatePersistence \(pydantic_graph.persistence.BaseStatePersistence\)")[StateT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.StateT "StateT



      module-attribute
   \(pydantic_graph.nodes.StateT\)"), RunEndT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.RunEndT "RunEndT



      module-attribute
   \(pydantic_graph.nodes.RunEndT\)")]` |  The state persistence interface to use. |  _required_
`deps` |  `DepsT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.DepsT "DepsT



      module-attribute
   \(pydantic_graph.nodes.DepsT\)")` |  The dependencies of the graph. |  `None`
`span` |  `AbstractSpan] | None` |  The span to use for the graph run. If not provided, a new span will be created. |  `None`
`infer_name` |  |  Whether to infer the graph name from the calling frame. |  `True`
Returns: A GraphRun that can be async iterated over to drive the graph to completion.
Source code in `pydantic_graph/pydantic_graph/graph.py`
```
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
305
306
307
308
```
| ```
@asynccontextmanager
async def iter_from_persistence(
    self,
    persistence: BaseStatePersistence[StateT, RunEndT],
    *,
    deps: DepsT = None,
    span: AbstractContextManager[AbstractSpan] | None = None,
    infer_name: bool = True,
) -> AsyncIterator[GraphRun[StateT, DepsT, RunEndT]]:
    """A contextmanager to iterate over the graph's nodes as they are executed, created from a persistence object.

    This method has similar functionality to [`iter`][pydantic_graph.graph.Graph.iter],
    but instead of passing the node to run, it will restore the node and state from state persistence.

    Args:
        persistence: The state persistence interface to use.
        deps: The dependencies of the graph.
        span: The span to use for the graph run. If not provided, a new span will be created.
        infer_name: Whether to infer the graph name from the calling frame.

    Returns: A GraphRun that can be async iterated over to drive the graph to completion.
    """
    if infer_name and self.name is None:
        # f_back because `asynccontextmanager` adds one frame
        if frame := inspect.currentframe():  # pragma: no branch
            self._infer_name(frame.f_back)

    persistence.set_graph_types(self)

    snapshot = await persistence.load_next()
    if snapshot is None:
        raise exceptions.GraphRuntimeError('Unable to restore snapshot from state persistence.')

    snapshot.node.set_snapshot_id(snapshot.id)

    if self.auto_instrument and span is None:  # pragma: no branch
        span = logfire_span('run graph {graph.name}', graph=self)

    with ExitStack() as stack:
        entered_span = None if span is None else stack.enter_context(span)
        traceparent = None if entered_span is None else get_traceparent(entered_span)
        yield GraphRun[StateT, DepsT, RunEndT](
            graph=self,
            start_node=snapshot.node,
            persistence=persistence,
            state=snapshot.state,
            deps=deps,
            snapshot_id=snapshot.id,
            traceparent=traceparent,
        )

```

---|---
####  initialize `async`
```
initialize(
    node: BaseNode[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.BaseNode "BaseNode \(pydantic_graph.nodes.BaseNode\)")[StateT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.StateT "StateT



      module-attribute
   \(pydantic_graph.nodes.StateT\)"), DepsT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.DepsT "DepsT



      module-attribute
   \(pydantic_graph.nodes.DepsT\)"), RunEndT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.RunEndT "RunEndT



      module-attribute
   \(pydantic_graph.nodes.RunEndT\)")],
    persistence: BaseStatePersistence[](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.BaseStatePersistence "BaseStatePersistence \(pydantic_graph.persistence.BaseStatePersistence\)")[StateT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.StateT "StateT



      module-attribute
   \(pydantic_graph.nodes.StateT\)"), RunEndT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.RunEndT "RunEndT



      module-attribute
   \(pydantic_graph.nodes.RunEndT\)")],
    *,
    state: StateT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.StateT "StateT



      module-attribute
   \(pydantic_graph.nodes.StateT\)") = None,
    infer_name:  = True
) -> None

```

Initialize a new graph run in persistence without running it.
This is useful if you want to set up a graph run to be run later, e.g. via [`iter_from_persistence`](https://ai.pydantic.dev/api/pydantic_graph/graph/#pydantic_graph.graph.Graph.iter_from_persistence "iter_from_persistence



      async
  ").
Parameters:
Name | Type | Description | Default
---|---|---|---
`node` |  `BaseNode[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.BaseNode "BaseNode \(pydantic_graph.nodes.BaseNode\)")[StateT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.StateT "StateT



      module-attribute
   \(pydantic_graph.nodes.StateT\)"), DepsT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.DepsT "DepsT



      module-attribute
   \(pydantic_graph.nodes.DepsT\)"), RunEndT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.RunEndT "RunEndT



      module-attribute
   \(pydantic_graph.nodes.RunEndT\)")]` |  The node to run first. |  _required_
`persistence` |  `BaseStatePersistence[](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.BaseStatePersistence "BaseStatePersistence \(pydantic_graph.persistence.BaseStatePersistence\)")[StateT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.StateT "StateT



      module-attribute
   \(pydantic_graph.nodes.StateT\)"), RunEndT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.RunEndT "RunEndT



      module-attribute
   \(pydantic_graph.nodes.RunEndT\)")]` |  State persistence interface. |  _required_
`state` |  `StateT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.StateT "StateT



      module-attribute
   \(pydantic_graph.nodes.StateT\)")` |  The start state of the graph. |  `None`
`infer_name` |  |  Whether to infer the graph name from the calling frame. |  `True`
Source code in `pydantic_graph/pydantic_graph/graph.py`
```
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
```
| ```
async def initialize(
    self,
    node: BaseNode[StateT, DepsT, RunEndT],
    persistence: BaseStatePersistence[StateT, RunEndT],
    *,
    state: StateT = None,
    infer_name: bool = True,
) -> None:
    """Initialize a new graph run in persistence without running it.

    This is useful if you want to set up a graph run to be run later, e.g. via
    [`iter_from_persistence`][pydantic_graph.graph.Graph.iter_from_persistence].

    Args:
        node: The node to run first.
        persistence: State persistence interface.
        state: The start state of the graph.
        infer_name: Whether to infer the graph name from the calling frame.
    """
    if infer_name and self.name is None:
        self._infer_name(inspect.currentframe())

    persistence.set_graph_types(self)
    await persistence.snapshot_node(state, node)

```

---|---
####  mermaid_code
```
mermaid_code(
    *,
    start_node: (
        [NodeIdent[](https://ai.pydantic.dev/api/pydantic_graph/mermaid/#pydantic_graph.mermaid.NodeIdent "NodeIdent



      module-attribute
   \(pydantic_graph.mermaid.NodeIdent\)")] | NodeIdent[](https://ai.pydantic.dev/api/pydantic_graph/mermaid/#pydantic_graph.mermaid.NodeIdent "NodeIdent



      module-attribute
   \(pydantic_graph.mermaid.NodeIdent\)") | None
    ) = None,
    title:  | None | [False] = None,
    edge_labels:  = True,
    notes:  = True,
    highlighted_nodes: (
        [NodeIdent[](https://ai.pydantic.dev/api/pydantic_graph/mermaid/#pydantic_graph.mermaid.NodeIdent "NodeIdent



      module-attribute
   \(pydantic_graph.mermaid.NodeIdent\)")] | NodeIdent[](https://ai.pydantic.dev/api/pydantic_graph/mermaid/#pydantic_graph.mermaid.NodeIdent "NodeIdent



      module-attribute
   \(pydantic_graph.mermaid.NodeIdent\)") | None
    ) = None,
    highlight_css:  = DEFAULT_HIGHLIGHT_CSS[](https://ai.pydantic.dev/api/pydantic_graph/mermaid/#pydantic_graph.mermaid.DEFAULT_HIGHLIGHT_CSS "DEFAULT_HIGHLIGHT_CSS



      module-attribute
   \(pydantic_graph.mermaid.DEFAULT_HIGHLIGHT_CSS\)"),
    infer_name:  = True,
    direction: StateDiagramDirection[](https://ai.pydantic.dev/api/pydantic_graph/mermaid/#pydantic_graph.mermaid.StateDiagramDirection "StateDiagramDirection



      module-attribute
   \(pydantic_graph.mermaid.StateDiagramDirection\)") | None = None
) ->

```

Generate a diagram representing the graph as
This method calls [`pydantic_graph.mermaid.generate_code`](https://ai.pydantic.dev/api/pydantic_graph/mermaid/#pydantic_graph.mermaid.generate_code "generate_code").
Parameters:
Name | Type | Description | Default
---|---|---|---
`start_node` |  `NodeIdent[](https://ai.pydantic.dev/api/pydantic_graph/mermaid/#pydantic_graph.mermaid.NodeIdent "NodeIdent



      module-attribute
   \(pydantic_graph.mermaid.NodeIdent\)")] | NodeIdent[](https://ai.pydantic.dev/api/pydantic_graph/mermaid/#pydantic_graph.mermaid.NodeIdent "NodeIdent



      module-attribute
   \(pydantic_graph.mermaid.NodeIdent\)") | None` |  The node or nodes which can start the graph. |  `None`
`title` |  |  The title of the diagram, use `False` to not include a title. |  `None`
`edge_labels` |  |  Whether to include edge labels. |  `True`
`notes` |  |  Whether to include notes on each node. |  `True`
`highlighted_nodes` |  `NodeIdent[](https://ai.pydantic.dev/api/pydantic_graph/mermaid/#pydantic_graph.mermaid.NodeIdent "NodeIdent



      module-attribute
   \(pydantic_graph.mermaid.NodeIdent\)")] | NodeIdent[](https://ai.pydantic.dev/api/pydantic_graph/mermaid/#pydantic_graph.mermaid.NodeIdent "NodeIdent



      module-attribute
   \(pydantic_graph.mermaid.NodeIdent\)") | None` |  Optional node or nodes to highlight. |  `None`
`highlight_css` |  |  The CSS to use for highlighting nodes. |  `DEFAULT_HIGHLIGHT_CSS[](https://ai.pydantic.dev/api/pydantic_graph/mermaid/#pydantic_graph.mermaid.DEFAULT_HIGHLIGHT_CSS "DEFAULT_HIGHLIGHT_CSS



      module-attribute
   \(pydantic_graph.mermaid.DEFAULT_HIGHLIGHT_CSS\)")`
`infer_name` |  |  Whether to infer the graph name from the calling frame. |  `True`
`direction` |  `StateDiagramDirection[](https://ai.pydantic.dev/api/pydantic_graph/mermaid/#pydantic_graph.mermaid.StateDiagramDirection "StateDiagramDirection



      module-attribute
   \(pydantic_graph.mermaid.StateDiagramDirection\)") | None` |  The direction of flow. |  `None`
Returns:
Type | Description
---|---
|  The mermaid code for the graph, which can then be rendered as a diagram.
Here's an example of generating a diagram for the graph from [above](https://ai.pydantic.dev/api/pydantic_graph/graph/#pydantic_graph.graph.Graph "Graph



      dataclass
  "):
mermaid_never_42.py```
from never_42 import Increment, never_42_graph

print(never_42_graph.mermaid_code(start_node=Increment))
'''
---
title: never_42_graph
---
stateDiagram-v2
  [*] --> Increment
  Increment --> Check42
  Check42 --> Increment
  Check42 --> [*]
'''

```

The rendered diagram will look like this:
Source code in `pydantic_graph/pydantic_graph/graph.py`
```
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
```
| ```
def mermaid_code(
    self,
    *,
    start_node: Sequence[mermaid.NodeIdent] | mermaid.NodeIdent | None = None,
    title: str | None | typing_extensions.Literal[False] = None,
    edge_labels: bool = True,
    notes: bool = True,
    highlighted_nodes: Sequence[mermaid.NodeIdent] | mermaid.NodeIdent | None = None,
    highlight_css: str = mermaid.DEFAULT_HIGHLIGHT_CSS,
    infer_name: bool = True,
    direction: mermaid.StateDiagramDirection | None = None,
) -> str:
    """Generate a diagram representing the graph as [mermaid](https://mermaid.js.org/) diagram.

    This method calls [`pydantic_graph.mermaid.generate_code`][pydantic_graph.mermaid.generate_code].

    Args:
        start_node: The node or nodes which can start the graph.
        title: The title of the diagram, use `False` to not include a title.
        edge_labels: Whether to include edge labels.
        notes: Whether to include notes on each node.
        highlighted_nodes: Optional node or nodes to highlight.
        highlight_css: The CSS to use for highlighting nodes.
        infer_name: Whether to infer the graph name from the calling frame.
        direction: The direction of flow.

    Returns:
        The mermaid code for the graph, which can then be rendered as a diagram.

    Here's an example of generating a diagram for the graph from [above][pydantic_graph.graph.Graph]:

```py {title="mermaid_never_42.py" requires="never_42.py"}
    from never_42 import Increment, never_42_graph

    print(never_42_graph.mermaid_code(start_node=Increment))
    '''
    ---
    title: never_42_graph
    ---
    stateDiagram-v2
      [*] --> Increment
      Increment --> Check42
      Check42 --> Increment
      Check42 --> [*]
    '''
```

    The rendered diagram will look like this:

```mermaid
    ---
    title: never_42_graph
    ---
    stateDiagram-v2
      [*] --> Increment
      Increment --> Check42
      Check42 --> Increment
      Check42 --> [*]
```
    """
    if infer_name and self.name is None:
        self._infer_name(inspect.currentframe())
    if title is None and self.name:
        title = self.name
    return mermaid.generate_code(
        self,
        start_node=start_node,
        highlighted_nodes=highlighted_nodes,
        highlight_css=highlight_css,
        title=title or None,
        edge_labels=edge_labels,
        notes=notes,
        direction=direction,
    )

```

---|---
####  mermaid_image
```
mermaid_image(
    infer_name:  = True, **kwargs: [MermaidConfig[](https://ai.pydantic.dev/api/pydantic_graph/mermaid/#pydantic_graph.mermaid.MermaidConfig "MermaidConfig \(pydantic_graph.mermaid.MermaidConfig\)")]
) ->

```

Generate a diagram representing the graph as an image.
The format and diagram can be customized using `kwargs`, see [`pydantic_graph.mermaid.MermaidConfig`](https://ai.pydantic.dev/api/pydantic_graph/mermaid/#pydantic_graph.mermaid.MermaidConfig "MermaidConfig").
Uses external service
This method makes a request to `mermaid.ink` is a free service not affiliated with Pydantic.
Parameters:
Name | Type | Description | Default
---|---|---|---
`infer_name` |  |  Whether to infer the graph name from the calling frame. |  `True`
`**kwargs` |  `MermaidConfig[](https://ai.pydantic.dev/api/pydantic_graph/mermaid/#pydantic_graph.mermaid.MermaidConfig "MermaidConfig \(pydantic_graph.mermaid.MermaidConfig\)")]` |  Additional arguments to pass to `mermaid.request_image`. |  `{}`
Returns:
Type | Description
---|---
|  The image bytes.
Source code in `pydantic_graph/pydantic_graph/graph.py`
```
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
```
| ```
def mermaid_image(
    self, infer_name: bool = True, **kwargs: typing_extensions.Unpack[mermaid.MermaidConfig]
) -> bytes:
    """Generate a diagram representing the graph as an image.

    The format and diagram can be customized using `kwargs`,
    see [`pydantic_graph.mermaid.MermaidConfig`][pydantic_graph.mermaid.MermaidConfig].

    !!! note "Uses external service"
        This method makes a request to [mermaid.ink](https://mermaid.ink) to render the image, `mermaid.ink`
        is a free service not affiliated with Pydantic.

    Args:
        infer_name: Whether to infer the graph name from the calling frame.
        **kwargs: Additional arguments to pass to `mermaid.request_image`.

    Returns:
        The image bytes.
    """
    if infer_name and self.name is None:
        self._infer_name(inspect.currentframe())
    if 'title' not in kwargs and self.name:
        kwargs['title'] = self.name
    return mermaid.request_image(self, **kwargs)

```

---|---
####  mermaid_save
```
mermaid_save(
    path:  | ,
    /,
    *,
    infer_name:  = True,
    **kwargs: [MermaidConfig[](https://ai.pydantic.dev/api/pydantic_graph/mermaid/#pydantic_graph.mermaid.MermaidConfig "MermaidConfig \(pydantic_graph.mermaid.MermaidConfig\)")],
) -> None

```

Generate a diagram representing the graph and save it as an image.
The format and diagram can be customized using `kwargs`, see [`pydantic_graph.mermaid.MermaidConfig`](https://ai.pydantic.dev/api/pydantic_graph/mermaid/#pydantic_graph.mermaid.MermaidConfig "MermaidConfig").
Uses external service
This method makes a request to `mermaid.ink` is a free service not affiliated with Pydantic.
Parameters:
Name | Type | Description | Default
---|---|---|---
`path` |  |  The path to save the image to. |  _required_
`infer_name` |  |  Whether to infer the graph name from the calling frame. |  `True`
`**kwargs` |  `MermaidConfig[](https://ai.pydantic.dev/api/pydantic_graph/mermaid/#pydantic_graph.mermaid.MermaidConfig "MermaidConfig \(pydantic_graph.mermaid.MermaidConfig\)")]` |  Additional arguments to pass to `mermaid.save_image`. |  `{}`
Source code in `pydantic_graph/pydantic_graph/graph.py`
```
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
```
| ```
def mermaid_save(
    self, path: Path | str, /, *, infer_name: bool = True, **kwargs: typing_extensions.Unpack[mermaid.MermaidConfig]
) -> None:
    """Generate a diagram representing the graph and save it as an image.

    The format and diagram can be customized using `kwargs`,
    see [`pydantic_graph.mermaid.MermaidConfig`][pydantic_graph.mermaid.MermaidConfig].

    !!! note "Uses external service"
        This method makes a request to [mermaid.ink](https://mermaid.ink) to render the image, `mermaid.ink`
        is a free service not affiliated with Pydantic.

    Args:
        path: The path to save the image to.
        infer_name: Whether to infer the graph name from the calling frame.
        **kwargs: Additional arguments to pass to `mermaid.save_image`.
    """
    if infer_name and self.name is None:
        self._infer_name(inspect.currentframe())
    if 'title' not in kwargs and self.name:
        kwargs['title'] = self.name
    mermaid.save_image(path, self, **kwargs)

```

---|---
####  get_nodes
```
get_nodes() -> (
    [[BaseNode[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.BaseNode "BaseNode \(pydantic_graph.nodes.BaseNode\)")[StateT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.StateT "StateT



      module-attribute
   \(pydantic_graph.nodes.StateT\)"), DepsT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.DepsT "DepsT



      module-attribute
   \(pydantic_graph.nodes.DepsT\)"), RunEndT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.RunEndT "RunEndT



      module-attribute
   \(pydantic_graph.nodes.RunEndT\)")]]]
)

```

Get the nodes in the graph.
Source code in `pydantic_graph/pydantic_graph/graph.py`
```
458
459
460
```
| ```
def get_nodes(self) -> Sequence[type[BaseNode[StateT, DepsT, RunEndT]]]:
    """Get the nodes in the graph."""
    return [node_def.node for node_def in self.node_defs.values()]

```

---|---
###  GraphRun
Bases: `StateT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.StateT "StateT



      module-attribute
   \(pydantic_graph.nodes.StateT\)"), DepsT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.DepsT "DepsT



      module-attribute
   \(pydantic_graph.nodes.DepsT\)"), RunEndT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.RunEndT "RunEndT



      module-attribute
   \(pydantic_graph.nodes.RunEndT\)")]`
A stateful, async-iterable run of a [`Graph`](https://ai.pydantic.dev/api/pydantic_graph/graph/#pydantic_graph.graph.Graph "Graph
