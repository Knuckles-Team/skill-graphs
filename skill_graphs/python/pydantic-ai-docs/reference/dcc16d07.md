                if item is self:
                    self.name = name
                    return
            if parent_frame.f_locals != parent_frame.f_globals:  # pragma: no branch
                # if we couldn't find the agent in locals and globals are a different dict, try globals
                for name, item in parent_frame.f_globals.items():  # pragma: no branch
                    if item is self:
                        self.name = name
                        return

```

---|---
####  __init__
```
__init__(
    *,
    nodes: [[BaseNode[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.BaseNode "BaseNode \(pydantic_graph.nodes.BaseNode\)")[StateT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.StateT "StateT



      module-attribute
   \(pydantic_graph.nodes.StateT\)"), DepsT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.DepsT "DepsT



      module-attribute
   \(pydantic_graph.nodes.DepsT\)"), RunEndT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.RunEndT "RunEndT



      module-attribute
   \(pydantic_graph.nodes.RunEndT\)")]]],
    name:  | None = None,
    state_type: [StateT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.StateT "StateT



      module-attribute
   \(pydantic_graph.nodes.StateT\)")] | Unset = UNSET,
    run_end_type: [RunEndT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.RunEndT "RunEndT



      module-attribute
   \(pydantic_graph.nodes.RunEndT\)")] | Unset = UNSET,
    auto_instrument:  = True
)

```

Create a graph from a sequence of nodes.
Parameters:
Name | Type | Description | Default
---|---|---|---
`nodes` |  `BaseNode[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.BaseNode "BaseNode \(pydantic_graph.nodes.BaseNode\)")[StateT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.StateT "StateT



      module-attribute
   \(pydantic_graph.nodes.StateT\)"), DepsT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.DepsT "DepsT



      module-attribute
   \(pydantic_graph.nodes.DepsT\)"), RunEndT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.RunEndT "RunEndT



      module-attribute
   \(pydantic_graph.nodes.RunEndT\)")]]]` |  The nodes which make up the graph, nodes need to be unique and all be generic in the same state type. |  _required_
`name` |  |  Optional name for the graph, if not provided the name will be inferred from the calling frame on the first call to a graph method. |  `None`
`state_type` |  `StateT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.StateT "StateT



      module-attribute
   \(pydantic_graph.nodes.StateT\)")] | Unset` |  The type of the state for the graph, this can generally be inferred from `nodes`. |  `UNSET`
`run_end_type` |  `RunEndT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.RunEndT "RunEndT



      module-attribute
   \(pydantic_graph.nodes.RunEndT\)")] | Unset` |  The type of the result of running the graph, this can generally be inferred from `nodes`. |  `UNSET`
`auto_instrument` |  |  Whether to create a span for the graph run and the execution of each node's run method. |  `True`
Source code in `pydantic_graph/pydantic_graph/graph.py`
```
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
```
| ```
def __init__(
    self,
    *,
    nodes: Sequence[type[BaseNode[StateT, DepsT, RunEndT]]],
    name: str | None = None,
    state_type: type[StateT] | _utils.Unset = _utils.UNSET,
    run_end_type: type[RunEndT] | _utils.Unset = _utils.UNSET,
    auto_instrument: bool = True,
):
    """Create a graph from a sequence of nodes.

    Args:
        nodes: The nodes which make up the graph, nodes need to be unique and all be generic in the same
            state type.
        name: Optional name for the graph, if not provided the name will be inferred from the calling frame
            on the first call to a graph method.
        state_type: The type of the state for the graph, this can generally be inferred from `nodes`.
        run_end_type: The type of the result of running the graph, this can generally be inferred from `nodes`.
        auto_instrument: Whether to create a span for the graph run and the execution of each node's run method.
    """
    self.name = name
    self._state_type = state_type
    self._run_end_type = run_end_type
    self.auto_instrument = auto_instrument

    parent_namespace = _utils.get_parent_namespace(inspect.currentframe())
    self.node_defs = {}
    for node in nodes:
        self._register_node(node, parent_namespace)

    self._validate_edges()

```

---|---
####  run `async`
```
run(
    start_node: BaseNode[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.BaseNode "BaseNode \(pydantic_graph.nodes.BaseNode\)")[StateT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.StateT "StateT



      module-attribute
   \(pydantic_graph.nodes.StateT\)"), DepsT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.DepsT "DepsT



      module-attribute
   \(pydantic_graph.nodes.DepsT\)"), RunEndT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.RunEndT "RunEndT



      module-attribute
   \(pydantic_graph.nodes.RunEndT\)")],
    *,
    state: StateT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.StateT "StateT



      module-attribute
   \(pydantic_graph.nodes.StateT\)") = None,
    deps: DepsT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.DepsT "DepsT



      module-attribute
   \(pydantic_graph.nodes.DepsT\)") = None,
    persistence: (
        BaseStatePersistence[](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.BaseStatePersistence "BaseStatePersistence \(pydantic_graph.persistence.BaseStatePersistence\)")[StateT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.StateT "StateT



      module-attribute
   \(pydantic_graph.nodes.StateT\)"), RunEndT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.RunEndT "RunEndT



      module-attribute
   \(pydantic_graph.nodes.RunEndT\)")] | None
    ) = None,
    infer_name:  = True
) -> GraphRunResult[](https://ai.pydantic.dev/api/pydantic_graph/graph/#pydantic_graph.graph.GraphRunResult "GraphRunResult



      dataclass
   \(pydantic_graph.graph.GraphRunResult\)")[StateT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.StateT "StateT



      module-attribute
   \(pydantic_graph.nodes.StateT\)"), RunEndT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.RunEndT "RunEndT



      module-attribute
   \(pydantic_graph.nodes.RunEndT\)")]

```

Run the graph from a starting node until it ends.
Parameters:
Name | Type | Description | Default
---|---|---|---
`start_node` |  `BaseNode[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.BaseNode "BaseNode \(pydantic_graph.nodes.BaseNode\)")[StateT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.StateT "StateT



      module-attribute
   \(pydantic_graph.nodes.StateT\)"), DepsT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.DepsT "DepsT



      module-attribute
   \(pydantic_graph.nodes.DepsT\)"), RunEndT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.RunEndT "RunEndT



      module-attribute
   \(pydantic_graph.nodes.RunEndT\)")]` |  the first node to run, since the graph definition doesn't define the entry point in the graph, you need to provide the starting node. |  _required_
`state` |  `StateT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.StateT "StateT



      module-attribute
   \(pydantic_graph.nodes.StateT\)")` |  The initial state of the graph. |  `None`
`deps` |  `DepsT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.DepsT "DepsT



      module-attribute
   \(pydantic_graph.nodes.DepsT\)")` |  The dependencies of the graph. |  `None`
`persistence` |  `BaseStatePersistence[](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.BaseStatePersistence "BaseStatePersistence \(pydantic_graph.persistence.BaseStatePersistence\)")[StateT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.StateT "StateT



      module-attribute
   \(pydantic_graph.nodes.StateT\)"), RunEndT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.RunEndT "RunEndT



      module-attribute
   \(pydantic_graph.nodes.RunEndT\)")] | None` |  State persistence interface, defaults to [`SimpleStatePersistence`](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.in_mem.SimpleStatePersistence "SimpleStatePersistence



      dataclass
  ") if `None`. |  `None`
`infer_name` |  |  Whether to infer the graph name from the calling frame. |  `True`
Returns:
Type | Description
---|---
`GraphRunResult[](https://ai.pydantic.dev/api/pydantic_graph/graph/#pydantic_graph.graph.GraphRunResult "GraphRunResult



      dataclass
   \(pydantic_graph.graph.GraphRunResult\)")[StateT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.StateT "StateT



      module-attribute
   \(pydantic_graph.nodes.StateT\)"), RunEndT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.RunEndT "RunEndT



      module-attribute
   \(pydantic_graph.nodes.RunEndT\)")]` |  A `GraphRunResult` containing information about the run, including its final result.
Here's an example of running the graph from [above](https://ai.pydantic.dev/api/pydantic_graph/graph/#pydantic_graph.graph.Graph "Graph



      dataclass
  "):
run_never_42.py```
from never_42 import Increment, MyState, never_42_graph

async def main():
    state = MyState(1)
    await never_42_graph.run(Increment(), state=state)
    print(state)
    #> MyState(number=2)

    state = MyState(41)
    await never_42_graph.run(Increment(), state=state)
    print(state)
    #> MyState(number=43)

```

Source code in `pydantic_graph/pydantic_graph/graph.py`
```
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
```
| ```
async def run(
    self,
    start_node: BaseNode[StateT, DepsT, RunEndT],
    *,
    state: StateT = None,
    deps: DepsT = None,
    persistence: BaseStatePersistence[StateT, RunEndT] | None = None,
    infer_name: bool = True,
) -> GraphRunResult[StateT, RunEndT]:
    """Run the graph from a starting node until it ends.

    Args:
        start_node: the first node to run, since the graph definition doesn't define the entry point in the graph,
            you need to provide the starting node.
        state: The initial state of the graph.
        deps: The dependencies of the graph.
        persistence: State persistence interface, defaults to
            [`SimpleStatePersistence`][pydantic_graph.SimpleStatePersistence] if `None`.
        infer_name: Whether to infer the graph name from the calling frame.

    Returns:
        A `GraphRunResult` containing information about the run, including its final result.

    Here's an example of running the graph from [above][pydantic_graph.graph.Graph]:

```py {title="run_never_42.py" noqa="I001" requires="never_42.py"}
    from never_42 import Increment, MyState, never_42_graph

    async def main():
        state = MyState(1)
        await never_42_graph.run(Increment(), state=state)
        print(state)
        #> MyState(number=2)

        state = MyState(41)
        await never_42_graph.run(Increment(), state=state)
        print(state)
        #> MyState(number=43)
```
    """
    if infer_name and self.name is None:
        self._infer_name(inspect.currentframe())

    async with self.iter(
        start_node, state=state, deps=deps, persistence=persistence, infer_name=False
    ) as graph_run:
        async for _node in graph_run:
            pass

    result = graph_run.result
    assert result is not None, 'GraphRun should have a result'
    return result

```

---|---
####  run_sync
```
run_sync(
    start_node: BaseNode[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.BaseNode "BaseNode \(pydantic_graph.nodes.BaseNode\)")[StateT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.StateT "StateT



      module-attribute
   \(pydantic_graph.nodes.StateT\)"), DepsT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.DepsT "DepsT



      module-attribute
   \(pydantic_graph.nodes.DepsT\)"), RunEndT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.RunEndT "RunEndT



      module-attribute
   \(pydantic_graph.nodes.RunEndT\)")],
    *,
    state: StateT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.StateT "StateT



      module-attribute
   \(pydantic_graph.nodes.StateT\)") = None,
    deps: DepsT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.DepsT "DepsT



      module-attribute
   \(pydantic_graph.nodes.DepsT\)") = None,
    persistence: (
        BaseStatePersistence[](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.BaseStatePersistence "BaseStatePersistence \(pydantic_graph.persistence.BaseStatePersistence\)")[StateT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.StateT "StateT



      module-attribute
   \(pydantic_graph.nodes.StateT\)"), RunEndT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.RunEndT "RunEndT



      module-attribute
   \(pydantic_graph.nodes.RunEndT\)")] | None
    ) = None,
    infer_name:  = True
) -> GraphRunResult[](https://ai.pydantic.dev/api/pydantic_graph/graph/#pydantic_graph.graph.GraphRunResult "GraphRunResult



      dataclass
   \(pydantic_graph.graph.GraphRunResult\)")[StateT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.StateT "StateT



      module-attribute
   \(pydantic_graph.nodes.StateT\)"), RunEndT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.RunEndT "RunEndT



      module-attribute
   \(pydantic_graph.nodes.RunEndT\)")]

```

Synchronously run the graph.
This is a convenience method that wraps [`self.run`](https://ai.pydantic.dev/api/pydantic_graph/graph/#pydantic_graph.graph.Graph.run "run



      async
  ") with `loop.run_until_complete(...)`. You therefore can't use this method inside async code or if there's an active event loop.
Parameters:
Name | Type | Description | Default
---|---|---|---
`start_node` |  `BaseNode[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.BaseNode "BaseNode \(pydantic_graph.nodes.BaseNode\)")[StateT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.StateT "StateT



      module-attribute
   \(pydantic_graph.nodes.StateT\)"), DepsT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.DepsT "DepsT



      module-attribute
   \(pydantic_graph.nodes.DepsT\)"), RunEndT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.RunEndT "RunEndT



      module-attribute
   \(pydantic_graph.nodes.RunEndT\)")]` |  the first node to run, since the graph definition doesn't define the entry point in the graph, you need to provide the starting node. |  _required_
`state` |  `StateT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.StateT "StateT



      module-attribute
   \(pydantic_graph.nodes.StateT\)")` |  The initial state of the graph. |  `None`
`deps` |  `DepsT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.DepsT "DepsT



      module-attribute
   \(pydantic_graph.nodes.DepsT\)")` |  The dependencies of the graph. |  `None`
`persistence` |  `BaseStatePersistence[](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.BaseStatePersistence "BaseStatePersistence \(pydantic_graph.persistence.BaseStatePersistence\)")[StateT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.StateT "StateT



      module-attribute
   \(pydantic_graph.nodes.StateT\)"), RunEndT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.RunEndT "RunEndT



      module-attribute
   \(pydantic_graph.nodes.RunEndT\)")] | None` |  State persistence interface, defaults to [`SimpleStatePersistence`](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.in_mem.SimpleStatePersistence "SimpleStatePersistence



      dataclass
  ") if `None`. |  `None`
`infer_name` |  |  Whether to infer the graph name from the calling frame. |  `True`
Returns:
Type | Description
---|---
`GraphRunResult[](https://ai.pydantic.dev/api/pydantic_graph/graph/#pydantic_graph.graph.GraphRunResult "GraphRunResult



      dataclass
   \(pydantic_graph.graph.GraphRunResult\)")[StateT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.StateT "StateT



      module-attribute
   \(pydantic_graph.nodes.StateT\)"), RunEndT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.RunEndT "RunEndT



      module-attribute
   \(pydantic_graph.nodes.RunEndT\)")]` |  The result type from ending the run and the history of the run.
Source code in `pydantic_graph/pydantic_graph/graph.py`
```
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
```
| ```
def run_sync(
    self,
    start_node: BaseNode[StateT, DepsT, RunEndT],
    *,
    state: StateT = None,
    deps: DepsT = None,
    persistence: BaseStatePersistence[StateT, RunEndT] | None = None,
    infer_name: bool = True,
) -> GraphRunResult[StateT, RunEndT]:
    """Synchronously run the graph.

    This is a convenience method that wraps [`self.run`][pydantic_graph.graph.Graph.run] with `loop.run_until_complete(...)`.
    You therefore can't use this method inside async code or if there's an active event loop.

    Args:
        start_node: the first node to run, since the graph definition doesn't define the entry point in the graph,
            you need to provide the starting node.
        state: The initial state of the graph.
        deps: The dependencies of the graph.
        persistence: State persistence interface, defaults to
            [`SimpleStatePersistence`][pydantic_graph.SimpleStatePersistence] if `None`.
        infer_name: Whether to infer the graph name from the calling frame.

    Returns:
        The result type from ending the run and the history of the run.
    """
    if infer_name and self.name is None:  # pragma: no branch
        self._infer_name(inspect.currentframe())

    return _utils.get_event_loop().run_until_complete(
        self.run(start_node, state=state, deps=deps, persistence=persistence, infer_name=False)
    )

```

---|---
####  iter `async`
```
iter(
    start_node: BaseNode[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.BaseNode "BaseNode \(pydantic_graph.nodes.BaseNode\)")[StateT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.StateT "StateT



      module-attribute
   \(pydantic_graph.nodes.StateT\)"), DepsT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.DepsT "DepsT



      module-attribute
   \(pydantic_graph.nodes.DepsT\)"), RunEndT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.RunEndT "RunEndT



      module-attribute
   \(pydantic_graph.nodes.RunEndT\)")],
    *,
    state: StateT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.StateT "StateT



      module-attribute
   \(pydantic_graph.nodes.StateT\)") = None,
    deps: DepsT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.DepsT "DepsT



      module-attribute
   \(pydantic_graph.nodes.DepsT\)") = None,
    persistence: (
        BaseStatePersistence[](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.BaseStatePersistence "BaseStatePersistence \(pydantic_graph.persistence.BaseStatePersistence\)")[StateT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.StateT "StateT



      module-attribute
   \(pydantic_graph.nodes.StateT\)"), RunEndT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.RunEndT "RunEndT



      module-attribute
   \(pydantic_graph.nodes.RunEndT\)")] | None
    ) = None,
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

A contextmanager which can be used to iterate over the graph's nodes as they are executed.
This method returns a `GraphRun` object which can be used to async-iterate over the nodes of this `Graph` as they are executed. This is the API to use if you want to record or interact with the nodes as the graph execution unfolds.
The `GraphRun` can also be used to manually drive the graph execution by calling [`GraphRun.next`](https://ai.pydantic.dev/api/pydantic_graph/graph/#pydantic_graph.graph.GraphRun.next "next



      async
  ").
The `GraphRun` provides access to the full run history, state, deps, and the final result of the run once it has completed.
For more details, see the API documentation of [`GraphRun`](https://ai.pydantic.dev/api/pydantic_graph/graph/#pydantic_graph.graph.GraphRun "GraphRun").
Parameters:
Name | Type | Description | Default
---|---|---|---
`start_node` |  `BaseNode[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.BaseNode "BaseNode \(pydantic_graph.nodes.BaseNode\)")[StateT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.StateT "StateT



      module-attribute
   \(pydantic_graph.nodes.StateT\)"), DepsT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.DepsT "DepsT



      module-attribute
   \(pydantic_graph.nodes.DepsT\)"), RunEndT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.RunEndT "RunEndT



      module-attribute
   \(pydantic_graph.nodes.RunEndT\)")]` |  the first node to run. Since the graph definition doesn't define the entry point in the graph, you need to provide the starting node. |  _required_
`state` |  `StateT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.StateT "StateT



      module-attribute
   \(pydantic_graph.nodes.StateT\)")` |  The initial state of the graph. |  `None`
`deps` |  `DepsT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.DepsT "DepsT



      module-attribute
   \(pydantic_graph.nodes.DepsT\)")` |  The dependencies of the graph. |  `None`
`persistence` |  `BaseStatePersistence[](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.BaseStatePersistence "BaseStatePersistence \(pydantic_graph.persistence.BaseStatePersistence\)")[StateT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.StateT "StateT



      module-attribute
   \(pydantic_graph.nodes.StateT\)"), RunEndT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.RunEndT "RunEndT



      module-attribute
   \(pydantic_graph.nodes.RunEndT\)")] | None` |  State persistence interface, defaults to [`SimpleStatePersistence`](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.in_mem.SimpleStatePersistence "SimpleStatePersistence



      dataclass
  ") if `None`. |  `None`
`span` |  `AbstractSpan] | None` |  The span to use for the graph run. If not provided, a new span will be created. |  `None`
`infer_name` |  |  Whether to infer the graph name from the calling frame. |  `True`
Returns: A GraphRun that can be async iterated over to drive the graph to completion.
Source code in `pydantic_graph/pydantic_graph/graph.py`
```
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
```
| ```
@asynccontextmanager
async def iter(
    self,
    start_node: BaseNode[StateT, DepsT, RunEndT],
    *,
    state: StateT = None,
    deps: DepsT = None,
    persistence: BaseStatePersistence[StateT, RunEndT] | None = None,
    span: AbstractContextManager[AbstractSpan] | None = None,
    infer_name: bool = True,
