Returns:
Type | Description
---|---
`BaseNode[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.BaseNode "BaseNode \(pydantic_graph.nodes.BaseNode\)")[StateT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.StateT "StateT



      module-attribute
   \(pydantic_graph.nodes.StateT\)"), DepsT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.DepsT "DepsT



      module-attribute
   \(pydantic_graph.nodes.DepsT\)"), RunEndT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.RunEndT "RunEndT



      module-attribute
   \(pydantic_graph.nodes.RunEndT\)")] | End[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.End "End



      dataclass
   \(pydantic_graph.nodes.End\)")[RunEndT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.RunEndT "RunEndT



      module-attribute
   \(pydantic_graph.nodes.RunEndT\)")]` |  The next node returned by the graph logic, or an [`End`](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.End "End



      dataclass
  ") node if
`BaseNode[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.BaseNode "BaseNode \(pydantic_graph.nodes.BaseNode\)")[StateT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.StateT "StateT



      module-attribute
   \(pydantic_graph.nodes.StateT\)"), DepsT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.DepsT "DepsT



      module-attribute
   \(pydantic_graph.nodes.DepsT\)"), RunEndT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.RunEndT "RunEndT



      module-attribute
   \(pydantic_graph.nodes.RunEndT\)")] | End[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.End "End



      dataclass
   \(pydantic_graph.nodes.End\)")[RunEndT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.RunEndT "RunEndT



      module-attribute
   \(pydantic_graph.nodes.RunEndT\)")]` |  the run has completed.
Source code in `pydantic_graph/pydantic_graph/graph.py`
```
663
664
665
666
667
668
669
670
671
672
673
674
675
676
677
678
679
680
681
682
683
684
685
686
687
688
689
690
691
692
693
694
695
696
697
698
699
700
701
702
703
704
705
706
707
708
709
710
711
712
713
714
715
716
717
718
719
720
721
722
723
724
725
726
727
728
729
730
731
732
733
734
735
736
737
738
739
740
741
742
743
744
745
746
747
748
749
750
751
752
```
| ```
async def next(
    self, node: BaseNode[StateT, DepsT, RunEndT] | None = None
) -> BaseNode[StateT, DepsT, RunEndT] | End[RunEndT]:
    """Manually drive the graph run by passing in the node you want to run next.

    This lets you inspect or mutate the node before continuing execution, or skip certain nodes
    under dynamic conditions. The graph run should stop when you return an [`End`][pydantic_graph.nodes.End] node.

    Here's an example of using `next` to drive the graph from [above][pydantic_graph.graph.Graph]:
```py {title="next_never_42.py" noqa="I001" requires="never_42.py"}
    from copy import deepcopy
    from pydantic_graph import End
    from never_42 import Increment, MyState, never_42_graph

    async def main():
        state = MyState(48)
        async with never_42_graph.iter(Increment(), state=state) as graph_run:
            next_node = graph_run.next_node  # start with the first node
            node_states = [(next_node, deepcopy(graph_run.state))]

            while not isinstance(next_node, End):
                if graph_run.state.number == 50:
                    graph_run.state.number = 42
                next_node = await graph_run.next(next_node)
                node_states.append((next_node, deepcopy(graph_run.state)))

            print(node_states)
            '''
            [
                (Increment(), MyState(number=48)),
                (Check42(), MyState(number=49)),
                (End(data=49), MyState(number=49)),
            ]
            '''
```

    Args:
        node: The node to run next in the graph. If not specified, uses `self.next_node`, which is initialized to
            the `start_node` of the run and updated each time a new node is returned.

    Returns:
        The next node returned by the graph logic, or an [`End`][pydantic_graph.nodes.End] node if
        the run has completed.
    """
    if node is None:
        # This cast is necessary because self._next_node could be an `End`. You'll get a runtime error if that's
        # the case, but if it is, the only way to get there would be to have tried calling next manually after
        # the run finished. Either way, maybe it would be better to not do this cast...
        node = cast(BaseNode[StateT, DepsT, RunEndT], self._next_node)
        node_snapshot_id = node.get_snapshot_id()
    else:
        node_snapshot_id = node.get_snapshot_id()

    if node_snapshot_id != self._snapshot_id:
        await self.persistence.snapshot_node_if_new(node_snapshot_id, self.state, node)
        self._snapshot_id = node_snapshot_id

    if not isinstance(node, BaseNode):
        # While technically this is not compatible with the documented method signature, it's an easy mistake to
        # make, and we should eagerly provide a more helpful error message than you'd get otherwise.
        raise TypeError(f'`next` must be called with a `BaseNode` instance, got {node!r}.')

    node_id = node.get_node_id()
    if node_id not in self.graph.node_defs:
        raise exceptions.GraphRuntimeError(f'Node `{node}` is not in the graph.')

    with ExitStack() as stack:
        if self.graph.auto_instrument:  # pragma: no branch
            # Separate variable because we actually don't want logfire's f-string magic here,
            # we want the span_name to be preformatted for other backends
            # as requested in https://github.com/pydantic/pydantic-ai/issues/3173.
            span_name = f'run node {node_id}'
            stack.enter_context(logfire_span(span_name, node_id=node_id, node=node))

        async with self.persistence.record_run(node_snapshot_id):
            ctx = GraphRunContext(state=self.state, deps=self.deps)
            self._next_node = await node.run(ctx)

    if isinstance(self._next_node, End):
        self._snapshot_id = self._next_node.get_snapshot_id()
        await self.persistence.snapshot_end(self.state, self._next_node)
    elif isinstance(self._next_node, BaseNode):
        self._snapshot_id = self._next_node.get_snapshot_id()
        await self.persistence.snapshot_node(self.state, self._next_node)
    else:
        raise exceptions.GraphRuntimeError(
            f'Invalid node return type: `{type(self._next_node).__name__}`. Expected `BaseNode` or `End`.'
        )

    return self._next_node

```

---|---
####  __anext__ `async`
```
__anext__() -> (
    BaseNode[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.BaseNode "BaseNode \(pydantic_graph.nodes.BaseNode\)")[StateT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.StateT "StateT



      module-attribute
   \(pydantic_graph.nodes.StateT\)"), DepsT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.DepsT "DepsT



      module-attribute
   \(pydantic_graph.nodes.DepsT\)"), RunEndT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.RunEndT "RunEndT



      module-attribute
   \(pydantic_graph.nodes.RunEndT\)")] | End[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.End "End



      dataclass
   \(pydantic_graph.nodes.End\)")[RunEndT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.RunEndT "RunEndT



      module-attribute
   \(pydantic_graph.nodes.RunEndT\)")]
)

```

Use the last returned node as the input to `Graph.next`.
Source code in `pydantic_graph/pydantic_graph/graph.py`
```
757
758
759
760
761
762
763
764
765
766
```
| ```
async def __anext__(self) -> BaseNode[StateT, DepsT, RunEndT] | End[RunEndT]:
    """Use the last returned node as the input to `Graph.next`."""
    if not self._is_started:
        self._is_started = True
        return self._next_node

    if isinstance(self._next_node, End):
        raise StopAsyncIteration

    return await self.next(self._next_node)

```

---|---
###  GraphRunResult `dataclass`
Bases: `StateT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.StateT "StateT



      module-attribute
   \(pydantic_graph.nodes.StateT\)"), RunEndT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.RunEndT "RunEndT



      module-attribute
   \(pydantic_graph.nodes.RunEndT\)")]`
The final result of running a graph.
Source code in `pydantic_graph/pydantic_graph/graph.py`
```
772
773
774
775
776
777
778
779
780
781
782
783
784
785
786
787
788
789
790
791
792
793
794
795
796
797
798
799
```
| ```
@dataclass(init=False)
class GraphRunResult(Generic[StateT, RunEndT]):
    """The final result of running a graph."""

    output: RunEndT
    state: StateT
    persistence: BaseStatePersistence[StateT, RunEndT] = field(repr=False)

    def __init__(
        self,
        output: RunEndT,
        state: StateT,
        persistence: BaseStatePersistence[StateT, RunEndT],
        traceparent: str | None = None,
    ):
        self.output = output
        self.state = state
        self.persistence = persistence
        self.__traceparent = traceparent

    @overload
    def _traceparent(self, *, required: typing_extensions.Literal[False]) -> str | None: ...
    @overload
    def _traceparent(self) -> str: ...
    def _traceparent(self, *, required: bool = True) -> str | None:  # pragma: no cover
        if self.__traceparent is None and required:
            raise exceptions.GraphRuntimeError('No span was created for this graph run.')
        return self.__traceparent

```

---|---
© Pydantic Services Inc. 2024 to present
