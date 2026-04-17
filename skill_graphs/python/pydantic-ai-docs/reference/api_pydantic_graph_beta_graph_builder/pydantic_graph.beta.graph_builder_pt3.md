
      dataclass
   \(pydantic_graph.beta.decision.Decision\)")[StateT, DepsT, ` |  A new Decision node with no branches
Source code in `pydantic_graph/pydantic_graph/beta/graph_builder.py`
```
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
© Pydantic Services Inc. 2024 to present
