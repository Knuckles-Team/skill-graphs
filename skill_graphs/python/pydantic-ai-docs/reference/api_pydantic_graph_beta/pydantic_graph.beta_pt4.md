459
460
461
462
463
464
465
466
467
```
| ```
def decision(self, *, note: str | None = None, node_id: str | None = None) -> Decision[StateT, DepsT, Never]:
    """Create a new decision node.

    Args:
        note: Optional note to describe the decision logic
        node_id: Optional ID for the node produced for this decision logic

    Returns:
        A new Decision node with no branches
    """
    return Decision(id=NodeID(node_id or generate_placeholder_node_id('decision')), branches=[], note=note)

```

---|---
####  match
```
match(
    source: TypeOrTypeExpression[SourceT],
    *,
    matches: [[], ] | None = None
) -> DecisionBranchBuilder[](https://ai.pydantic.dev/api/pydantic_graph/beta_decision/#pydantic_graph.beta.decision.DecisionBranchBuilder "DecisionBranchBuilder



      dataclass
   \(pydantic_graph.beta.decision.DecisionBranchBuilder\)")[
    StateT, DepsT, SourceT, SourceT,
]

```

Create a decision branch matcher.
Parameters:
Name | Type | Description | Default
---|---|---|---
`source` |  `TypeOrTypeExpression[SourceT]` |  The type or type expression to match against |  _required_
`matches` |  |  Optional custom matching function |  `None`
Returns:
Type | Description
---|---
`DecisionBranchBuilder[](https://ai.pydantic.dev/api/pydantic_graph/beta_decision/#pydantic_graph.beta.decision.DecisionBranchBuilder "DecisionBranchBuilder



      dataclass
   \(pydantic_graph.beta.decision.DecisionBranchBuilder\)")[StateT, DepsT, SourceT, SourceT, ` |  A DecisionBranchBuilder for constructing the branch
Source code in `pydantic_graph/pydantic_graph/beta/graph_builder.py`
```
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
```
| ```
def match(
    self,
    source: TypeOrTypeExpression[SourceT],
    *,
    matches: Callable[[Any], bool] | None = None,
) -> DecisionBranchBuilder[StateT, DepsT, SourceT, SourceT, Never]:
    """Create a decision branch matcher.

    Args:
        source: The type or type expression to match against
        matches: Optional custom matching function

    Returns:
        A DecisionBranchBuilder for constructing the branch
    """
    # Note, the following node_id really is just a placeholder and shouldn't end up in the final graph
    # This is why we don't expose a way for end users to override the value used here.
    node_id = NodeID(generate_placeholder_node_id('match_decision'))
    decision = Decision[StateT, DepsT, Never](id=node_id, branches=[], note=None)
    new_path_builder = PathBuilder[StateT, DepsT, SourceT](working_items=[])
    return DecisionBranchBuilder(decision=decision, source=source, matches=matches, path_builder=new_path_builder)

```

---|---
####  match_node
```
match_node(
    source: [SourceNodeT],
    *,
    matches: [[], ] | None = None
) -> DecisionBranch[](https://ai.pydantic.dev/api/pydantic_graph/beta_decision/#pydantic_graph.beta.decision.DecisionBranch "DecisionBranch



      dataclass
   \(pydantic_graph.beta.decision.DecisionBranch\)")[SourceNodeT]

```

Create a decision branch for BaseNode subclasses.
This is similar to match() but specifically designed for matching against BaseNode types from the v1 system.
Parameters:
Name | Type | Description | Default
---|---|---|---
`source` |  `SourceNodeT]` |  The BaseNode subclass to match against |  _required_
`matches` |  |  Optional custom matching function |  `None`
Returns:
Type | Description
---|---
`DecisionBranch[](https://ai.pydantic.dev/api/pydantic_graph/beta_decision/#pydantic_graph.beta.decision.DecisionBranch "DecisionBranch



      dataclass
   \(pydantic_graph.beta.decision.DecisionBranch\)")[SourceNodeT]` |  A DecisionBranch for the BaseNode type
Source code in `pydantic_graph/pydantic_graph/beta/graph_builder.py`
```
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
```
| ```
def match_node(
    self,
    source: type[SourceNodeT],
    *,
    matches: Callable[[Any], bool] | None = None,
) -> DecisionBranch[SourceNodeT]:
    """Create a decision branch for BaseNode subclasses.

    This is similar to match() but specifically designed for matching
    against BaseNode types from the v1 system.

    Args:
        source: The BaseNode subclass to match against
        matches: Optional custom matching function

    Returns:
        A DecisionBranch for the BaseNode type
    """
    node = NodeStep(source)
    path = Path(items=[DestinationMarker(node.id)])
    return DecisionBranch(source=source, matches=matches, path=path, destinations=[node])

```

---|---
####  node
```
node(
    node_type: [BaseNode[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.BaseNode "BaseNode \(pydantic_graph.nodes.BaseNode\)")[StateT, DepsT, GraphOutputT]],
) -> EdgePath[StateT, DepsT]

```

Create an edge path from a BaseNode class.
This method integrates v1-style BaseNode classes into the v2 graph system by analyzing their type hints and creating appropriate edges.
Parameters:
Name | Type | Description | Default
---|---|---|---
`node_type` |  `BaseNode[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.BaseNode "BaseNode \(pydantic_graph.nodes.BaseNode\)")[StateT, DepsT, GraphOutputT]]` |  The BaseNode subclass to integrate |  _required_
Returns:
Type | Description
---|---
`EdgePath[StateT, DepsT]` |  An EdgePath representing the node and its connections
Raises:
Type | Description
---|---
`GraphSetupError[](https://ai.pydantic.dev/api/pydantic_graph/exceptions/#pydantic_graph.exceptions.GraphSetupError "GraphSetupError \(pydantic_graph.exceptions.GraphSetupError\)")` |  If the node type is missing required type hints
Source code in `pydantic_graph/pydantic_graph/beta/graph_builder.py`
```
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
528
529
530
531
532
533
534
535
536
537
538
539
540
541
542
543
544
545
546
```
| ```
def node(
    self,
    node_type: type[BaseNode[StateT, DepsT, GraphOutputT]],
) -> EdgePath[StateT, DepsT]:
    """Create an edge path from a BaseNode class.

    This method integrates v1-style BaseNode classes into the v2 graph
    system by analyzing their type hints and creating appropriate edges.

    Args:
        node_type: The BaseNode subclass to integrate

    Returns:
        An EdgePath representing the node and its connections

    Raises:
        GraphSetupError: If the node type is missing required type hints
    """
    parent_namespace = _utils.get_parent_namespace(inspect.currentframe())
    type_hints = get_type_hints(node_type.run, localns=parent_namespace, include_extras=True)
    try:
        return_hint = type_hints['return']
    except KeyError as e:  # pragma: no cover
        raise exceptions.GraphSetupError(
            f'Node {node_type} is missing a return type hint on its `run` method'
        ) from e

    node = NodeStep(node_type)

    edge = self._edge_from_return_hint(node, return_hint)
    if not edge:  # pragma: no cover
        raise exceptions.GraphSetupError(f'Node {node_type} is missing a return type hint on its `run` method')

    return edge

```

---|---
####  build
```
build(
    validate_graph_structure:  = True,
) -> Graph[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.Graph "Graph



      dataclass
   \(pydantic_graph.beta.graph.Graph\)")[StateT, DepsT, GraphInputT, GraphOutputT]

```

Build the final executable graph from the accumulated nodes and edges.
This method performs validation, normalization, and analysis of the graph structure to create a complete, executable graph instance.
Parameters:
Name | Type | Description | Default
---|---|---|---
`validate_graph_structure` |  |  whether to perform validation of the graph structure See the docstring of _validate_graph_structure below for more details. |  `True`
Returns:
Type | Description
---|---
`Graph[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.Graph "Graph



      dataclass
   \(pydantic_graph.beta.graph.Graph\)")[StateT, DepsT, GraphInputT, GraphOutputT]` |  A complete Graph instance ready for execution
Raises:
Type | Description
---|---
|  If the graph structure is invalid (e.g., join without parent fork)
Source code in `pydantic_graph/pydantic_graph/beta/graph_builder.py`
```
638
639
640
641
642
643
644
645
646
647
648
649
650
651
652
653
654
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
```
| ```
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
###  EndNode
Bases: `InputT[](https://ai.pydantic.dev/api/pydantic_graph/beta_node/#pydantic_graph.beta.node.InputT "InputT



      module-attribute
   \(pydantic_graph.beta.node.InputT\)")]`
Terminal node representing the completion of graph execution.
The EndNode marks the successful completion of a graph execution flow and can collect the final output data.
Source code in `pydantic_graph/pydantic_graph/beta/node.py`
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
```
| ```
class EndNode(Generic[InputT]):
    """Terminal node representing the completion of graph execution.

    The EndNode marks the successful completion of a graph execution flow
    and can collect the final output data.
    """

    id = NodeID('__end__')
    """Fixed identifier for the end node."""

    def _force_variance(self, inputs: InputT) -> None:  # pragma: no cover
        """Force type variance for proper generic typing.

        This method exists solely for type checking purposes and should never be called.

        Args:
            inputs: Input data of type InputT.

        Raises:
            RuntimeError: Always, as this method should never be executed.
        """
        raise RuntimeError('This method should never be called, it is just defined for typing purposes.')

```

---|---
####  id `class-attribute` `instance-attribute`
```
id = NodeID('__end__')

```

Fixed identifier for the end node.
###  StartNode
Bases: `OutputT[](https://ai.pydantic.dev/api/pydantic_graph/beta_node/#pydantic_graph.beta.node.OutputT "OutputT



      module-attribute
   \(pydantic_graph.beta.node.OutputT\)")]`
Entry point node for graph execution.
The StartNode represents the beginning of a graph execution flow.
Source code in `pydantic_graph/pydantic_graph/beta/node.py`
```
26
27
28
29
30
31
32
33
```
| ```
class StartNode(Generic[OutputT]):
    """Entry point node for graph execution.

    The StartNode represents the beginning of a graph execution flow.
    """

    id = NodeID('__start__')
    """Fixed identifier for the start node."""

```

---|---
####  id `class-attribute` `instance-attribute`
```
id = NodeID('__start__')

```

Fixed identifier for the start node.
###  StepContext `dataclass`
Bases: `StateT, DepsT, InputT]`
Context information passed to step functions during graph execution.
The step context provides access to the current graph state, dependencies, and input data for a step.
Class Type Parameters:
Name | Bound or Constraints | Description | Default
---|---|---|---
`StateT` |  |  The type of the graph state |  _required_
`DepsT` |  |  The type of the dependencies |  _required_
`InputT` |  |  The type of the input data |  _required_
Source code in `pydantic_graph/pydantic_graph/beta/step.py`
```
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
```
| ```
@dataclass(init=False)
class StepContext(Generic[StateT, DepsT, InputT]):
    """Context information passed to step functions during graph execution.

    The step context provides access to the current graph state, dependencies, and input data for a step.

    Type Parameters:
        StateT: The type of the graph state
        DepsT: The type of the dependencies
        InputT: The type of the input data
    """

    _state: StateT
    """The current graph state."""
    _deps: DepsT
    """The graph run dependencies."""
    _inputs: InputT
    """The input data for this step."""

    def __init__(self, *, state: StateT, deps: DepsT, inputs: InputT):
        self._state = state
        self._deps = deps
        self._inputs = inputs

    @property
    def state(self) -> StateT:
        return self._state

    @property
    def deps(self) -> DepsT:
        return self._deps

    @property
    def inputs(self) -> InputT:
        """The input data for this step.

        This must be a property to ensure correct variance behavior
        """
        return self._inputs

```

---|---
####  inputs `property`
```
inputs: InputT

```

The input data for this step.
This must be a property to ensure correct variance behavior
###  StepNode `dataclass`
Bases: `BaseNode[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.BaseNode "BaseNode \(pydantic_graph.nodes.BaseNode\)")[StateT, DepsT, `
A base node that represents a step with bound inputs.
StepNode bridges between the v1 and v2 graph execution systems by wrapping a [`Step`](https://ai.pydantic.dev/api/pydantic_graph/beta_step/#pydantic_graph.beta.step.Step "Step



      dataclass
  ") with bound inputs in a BaseNode interface. It is not meant to be run directly but rather used to indicate transitions to v2-style steps.
Source code in `pydantic_graph/pydantic_graph/beta/step.py`
```
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
```
| ```
@dataclass
class StepNode(BaseNode[StateT, DepsT, Any]):
    """A base node that represents a step with bound inputs.

    StepNode bridges between the v1 and v2 graph execution systems by wrapping
    a [`Step`][pydantic_graph.beta.step.Step] with bound inputs in a BaseNode interface.
    It is not meant to be run directly but rather used to indicate transitions
    to v2-style steps.
    """

    step: Step[StateT, DepsT, Any, Any]
    """The step to execute."""

    inputs: Any
    """The inputs bound to this step."""

    async def run(self, ctx: GraphRunContext[StateT, DepsT]) -> BaseNode[StateT, DepsT, Any] | End[Any]:
        """Attempt to run the step node.

        Args:
            ctx: The graph execution context

        Returns:
            The result of step execution

        Raises:
            NotImplementedError: Always raised as StepNode is not meant to be run directly
        """
        raise NotImplementedError(
            '`StepNode` is not meant to be run directly, it is meant to be used in `BaseNode` subclasses to indicate a transition to v2-style steps.'
        )

```

---|---
####  step `instance-attribute`
```
step: Step[](https://ai.pydantic.dev/api/pydantic_graph/beta_step/#pydantic_graph.beta.step.Step "Step



      dataclass
   \(pydantic_graph.beta.step.Step\)")[StateT, DepsT, , ]

```

The step to execute.
####  inputs `instance-attribute`
```
inputs:

```

The inputs bound to this step.
####  run `async`
```
run(
    ctx: GraphRunContext[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.GraphRunContext "GraphRunContext



      dataclass
   \(pydantic_graph.nodes.GraphRunContext\)")[StateT, DepsT],
) -> BaseNode[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.BaseNode "BaseNode \(pydantic_graph.nodes.BaseNode\)")[StateT, DepsT, ] | End[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.End "End



      dataclass
   \(pydantic_graph.nodes.End\)")[]

```

Attempt to run the step node.
Parameters:
Name | Type | Description | Default
---|---|---|---
`ctx` |  `GraphRunContext[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.GraphRunContext "GraphRunContext



      dataclass
   \(pydantic_graph.nodes.GraphRunContext\)")[StateT, DepsT]` |  The graph execution context |  _required_
Returns:
Type | Description
---|---
`BaseNode[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.BaseNode "BaseNode \(pydantic_graph.nodes.BaseNode\)")[StateT, DepsT, End[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.End "End



      dataclass
   \(pydantic_graph.nodes.End\)")[` |  The result of step execution
Raises:
Type | Description
---|---
|  Always raised as StepNode is not meant to be run directly
Source code in `pydantic_graph/pydantic_graph/beta/step.py`
```
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
```
| ```
async def run(self, ctx: GraphRunContext[StateT, DepsT]) -> BaseNode[StateT, DepsT, Any] | End[Any]:
    """Attempt to run the step node.

    Args:
        ctx: The graph execution context

    Returns:
        The result of step execution

    Raises:
        NotImplementedError: Always raised as StepNode is not meant to be run directly
    """
    raise NotImplementedError(
        '`StepNode` is not meant to be run directly, it is meant to be used in `BaseNode` subclasses to indicate a transition to v2-style steps.'
    )

```

---|---
###  TypeExpression
Bases: `T]`
A workaround for type checker limitations when using complex type expressions.
```
This class serves as a wrapper for types that cannot normally be used in positions

```

requiring `type[T]`, such as `Any`, `Union[...]`, or `Literal[...]`. It provides a way to pass these complex type expressions to functions expecting concrete types.
Example
Instead of `output_type=Union[str, int]` (which may cause type errors), use `output_type=TypeExpression[Union[str, int]]`.
Note
This is a workaround for the lack of TypeForm in the Python type system.
Source code in `pydantic_graph/pydantic_graph/beta/util.py`
```
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
```
| ```
class TypeExpression(Generic[T]):
    """A workaround for type checker limitations when using complex type expressions.

        This class serves as a wrapper for types that cannot normally be used in positions
    requiring `type[T]`, such as `Any`, `Union[...]`, or `Literal[...]`. It provides a
        way to pass these complex type expressions to functions expecting concrete types.

    Example:
            Instead of `output_type=Union[str, int]` (which may cause type errors),
            use `output_type=TypeExpression[Union[str, int]]`.

    Note:
            This is a workaround for the lack of TypeForm in the Python type system.
    """

    pass

```

---|---
© Pydantic Services Inc. 2024 to present
