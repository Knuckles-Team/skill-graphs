


      dataclass
   \(pydantic_graph.beta.graph.GraphTask\)")]` |  The next execution result: either an EndMarker, or sequence of GraphTasks
Source code in `pydantic_graph/pydantic_graph/beta/graph.py`
```
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
```
| ```
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

```

---|---
####  next_task `property`
```
next_task: EndMarker[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.EndMarker "EndMarker



      dataclass
   \(pydantic_graph.beta.graph.EndMarker\)")[OutputT[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.OutputT "OutputT



      module-attribute
   \(pydantic_graph.beta.graph.OutputT\)")] | [GraphTask[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.GraphTask "GraphTask



      dataclass
   \(pydantic_graph.beta.graph.GraphTask\)")]

```

Get the next task(s) to be executed.
Returns:
Type | Description
---|---
`EndMarker[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.EndMarker "EndMarker



      dataclass
   \(pydantic_graph.beta.graph.EndMarker\)")[OutputT[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.OutputT "OutputT



      module-attribute
   \(pydantic_graph.beta.graph.OutputT\)")] | GraphTask[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.GraphTask "GraphTask



      dataclass
   \(pydantic_graph.beta.graph.GraphTask\)")]` |  The next execution item, or the initial task if none is set
####  output `property`
```
output: OutputT[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.OutputT "OutputT



      module-attribute
   \(pydantic_graph.beta.graph.OutputT\)") | None

```

Get the final output if the graph has completed.
Returns:
Type | Description
---|---
`OutputT[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.OutputT "OutputT



      module-attribute
   \(pydantic_graph.beta.graph.OutputT\)") | None` |  The output value if execution is complete, None otherwise
© Pydantic Services Inc. 2024 to present
