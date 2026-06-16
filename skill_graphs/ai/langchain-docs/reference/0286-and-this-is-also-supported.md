# and this is also supported
{"messages": [{"type": "human", "content": "message"}]}
```

Since the state updates are always deserialized into LangChain `Messages` when using [`add_messages`](https://reference.langchain.com/python/langgraph/graph/message/add_messages), you should use dot notation to access message attributes, like `state["messages"][-1].content`.

Below is an example of a graph that uses [`add_messages`](https://reference.langchain.com/python/langgraph/graph/message/add_messages) as its reducer function.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain.messages import AnyMessage
from langgraph.graph.message import add_messages
from typing import Annotated
from typing_extensions import TypedDict

class GraphState(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]
```

#### MessagesState

Since having a list of messages in your state is so common, there exists a prebuilt state called `MessagesState` which makes it easy to use messages. `MessagesState` is defined with a single `messages` key which is a list of `AnyMessage` objects and uses the [`add_messages`](https://reference.langchain.com/python/langgraph/graph/message/add_messages) reducer. Typically, there is more state to track than just messages, so we see people subclass this state and add more fields, like:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langgraph.graph import MessagesState

class State(MessagesState):
    documents: list[str]
```

## Nodes

In LangGraph, nodes are Python functions (either synchronous or asynchronous) that accept the following arguments:

1. `state`—The [state](#state) of the graph
2. `config`—A [`RunnableConfig`](https://reference.langchain.com/python/langchain-core/runnables/config/RunnableConfig) object that contains configuration information like `thread_id` and tracing information like `tags`
3. `runtime`—A `Runtime` object that contains [runtime `context`](#runtime-context) and other information like `store`, `stream_writer`, `execution_info`, `server_info`, `heartbeat` (for idle timeout refresh), and `control` (for [graceful shutdown](/oss/python/langgraph/fault-tolerance#graceful-shutdown))

Similar to `NetworkX`, you add these nodes to a graph using the [`add_node`](https://reference.langchain.com/python/langgraph/graph/state/StateGraph/add_node) method:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from dataclasses import dataclass
from typing_extensions import TypedDict

from langgraph.graph import StateGraph
from langgraph.runtime import Runtime

class State(TypedDict):
    input: str
    results: str

@dataclass
class Context:
    user_id: str

builder = StateGraph(State)

def plain_node(state: State):
    return state

def node_with_runtime(state: State, runtime: Runtime[Context]):
    print("In node: ", runtime.context.user_id)
    return {"results": f"Hello, {state['input']}!"}

def node_with_execution_info(state: State, runtime: Runtime):
    print("In node with thread_id: ", runtime.execution_info.thread_id)  # [!code highlight]
    return {"results": f"Hello, {state['input']}!"}

builder.add_node("plain_node", plain_node)
builder.add_node("node_with_runtime", node_with_runtime)
builder.add_node("node_with_execution_info", node_with_execution_info)
...
```

Behind the scenes, functions are converted to [`RunnableLambda`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableLambda), which add batch and async support to your function, along with [native tracing and debugging](/langsmith/observability).

If you add a node to a graph without specifying a name, it will be given a default name equivalent to the function name.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
builder.add_node(my_node)

# You can then create edges to/from this node by referencing it as `"my_node"`
```

### Re-execution and idempotency

When you compile with a [checkpointer](/oss/python/langgraph/persistence), LangGraph saves checkpoints at [super-step](#graphs) boundaries, not mid-function inside a node. If execution stops and later resumes (for example after an [interrupt](/oss/python/langgraph/interrupts) or a [retry](/oss/python/langgraph/fault-tolerance#retries)), the affected **node** runs again from the start of its function. Code and side effects before the pause run again.

**Idempotency.** Design **node** logic so re-execution does not corrupt state. If a node inserts a database row, running it twice should not create duplicate rows unless that is intentional. Use idempotency keys, upserts, or read-before-write checks. For effects around `interrupt()`, see [Side effects called before `interrupt` must be idempotent](/oss/python/langgraph/interrupts#side-effects-called-before-interrupt-must-be-idempotent).

**Graph changes.** [Determinism](/oss/python/langgraph/functional-api#determinism) rules about code changes do not apply to graph structure. You can add or remove **nodes** and edges without breaking resume for existing threads. Resumed runs use saved state and execute whatever graph you compile now.

**Tasks and interrupts inside a node.** If a **node** calls [**tasks**](/oss/python/langgraph/functional-api#task) or [`interrupt`](https://reference.langchain.com/python/langgraph/types/interrupt), stricter determinism rules apply on resume. LangGraph restores completed **task** results from the checkpointer, but changing **task** or [`interrupt`](https://reference.langchain.com/python/langgraph/types/interrupt) order in code before the resume point can mismatch cached values. A [Functional API](/oss/python/langgraph/functional-api) **entrypoint** compiles to a single **node** that runs the whole entrypoint method this way. See [Determinism](/oss/python/langgraph/functional-api#determinism), [Idempotency](/oss/python/langgraph/functional-api#idempotency), and [Using tasks in nodes](#using-tasks-in-nodes).

### Using tasks in nodes

If a [node](#nodes) contains multiple operations, you may find it easier to implement each operation as a [**task**](/oss/python/langgraph/functional-api#task) instead of splitting the logic across multiple nodes. Task results are checkpointed when the graph uses a checkpointer, so resuming a thread can skip completed **task** work inside the node.

<Tabs>
  <Tab title="Original">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from typing import NotRequired

    import requests
    from langchain_core.utils.uuid import uuid7
    from langgraph.checkpoint.memory import InMemorySaver
    from langgraph.graph import END, START, StateGraph
    from typing_extensions import TypedDict

    class State(TypedDict):
        url: str
        result: NotRequired[str]

    def call_api(state: State):
        """Example node that makes an API request."""
        result = requests.get(state["url"]).text[:100]  # [!code highlight]
        return {"result": result}

    builder = StateGraph(State)
    builder.add_node("call_api", call_api)
    builder.add_edge(START, "call_api")
    builder.add_edge("call_api", END)

    checkpointer = InMemorySaver()
    graph = builder.compile(checkpointer=checkpointer)

    thread_id = str(uuid7())
    config = {"configurable": {"thread_id": thread_id}}

    graph.invoke({"url": "https://www.example.com"}, config)
    ```
  </Tab>

  <Tab title="With task">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from typing import NotRequired

    import requests
    from langchain_core.utils.uuid import uuid7
    from langgraph.checkpoint.memory import InMemorySaver
    from langgraph.func import task
    from langgraph.graph import END, START, StateGraph
    from typing_extensions import TypedDict

    class State(TypedDict):
        urls: list[str]
        results: NotRequired[list[str]]

    @task
    def _make_request(url: str):
        """Make a request."""
        return requests.get(url).text[:100]  # [!code highlight]

    def call_api(state: State):
        """Example node that makes API requests as checkpointed tasks."""
        futures = [_make_request(url) for url in state["urls"]]  # [!code highlight]
        results = [f.result() for f in futures]
        return {"results": results}

    builder = StateGraph(State)
    builder.add_node("call_api", call_api)
    builder.add_edge(START, "call_api")
    builder.add_edge("call_api", END)

    checkpointer = InMemorySaver()
    graph = builder.compile(checkpointer=checkpointer)

    thread_id = str(uuid7())
    config = {"configurable": {"thread_id": thread_id}}

    graph.invoke({"urls": ["https://www.example.com"]}, config)
    ```
  </Tab>
</Tabs>

### `START` node

The [`START`](https://reference.langchain.com/python/langgraph/constants/START) Node is a special node that represents the node that sends user input to the graph. The main purpose for referencing this node is to determine which nodes should be called first.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langgraph.graph import START

graph.add_edge(START, "node_a")
```

### `END` node

The `END` Node is a special node that represents a terminal node. This node is referenced when you want to denote which edges have no actions after they are done.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langgraph.graph import END

graph.add_edge("node_a", END)
```

### Node caching

LangGraph supports caching of tasks/nodes based on the input to the node. To use caching:

* Specify a cache when compiling a graph (or specifying an entrypoint)
* Specify a cache policy for nodes. Each cache policy supports:
  * `key_func` used to generate a cache key based on the input to a node, which defaults to a `hash` of the input with pickle.
  * `ttl`, the time to live for the cache in seconds. If not specified, the cache will never expire.

For example:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import time
from typing_extensions import TypedDict
from langgraph.graph import StateGraph
from langgraph.cache.memory import InMemoryCache
from langgraph.types import CachePolicy

class State(TypedDict):
    x: int
    result: int

builder = StateGraph(State)

def expensive_node(state: State) -> dict[str, int]:
    # expensive computation
    time.sleep(2)
    return {"result": state["x"] * 2}

builder.add_node("expensive_node", expensive_node, cache_policy=CachePolicy(ttl=3))
builder.set_entry_point("expensive_node")
builder.set_finish_point("expensive_node")

graph = builder.compile(cache=InMemoryCache())

print(graph.invoke({"x": 5}, stream_mode='updates'))    # [!code highlight]

# [{'expensive_node': {'result': 10}}]
print(graph.invoke({"x": 5}, stream_mode='updates'))    # [!code highlight]

# [{'expensive_node': {'result': 10}, '__metadata__': {'cached': True}}]
```

<Note>
  `set_entry_point(node)` defines the first node the graph will execute.
  It is equivalent to `builder.add_edge(START, node)`.

  `set_finish_point(node)` defines the last node in the graph.
  It is equivalent to `builder.add_edge(node, END)`.

  Both methods are valid but `add_edge(START, ...)` and `add_edge(..., END)`
  are the recommended modern syntax.
</Note>

1. First run takes two seconds to run (due to mocked expensive computation).
2. Second run utilizes cache and returns quickly.

## Edges

Edges define how the logic is routed and how the graph decides to stop. This is a big part of how your agents work and how different nodes communicate with each other. There are a few key types of edges:

* Normal Edges: Go directly from one node to the next.
* Conditional Edges: Call a function to determine which node(s) to go to next.
* Entry Point: Which node to call first when user input arrives.
* Conditional Entry Point: Call a function to determine which node(s) to call first when user input arrives.

A node can have multiple outgoing edges. If a node has multiple outgoing edges, **all** of those destination nodes will be executed in parallel as a part of the next superstep.

<Warning>
  For each node, choose one routing mechanism: use normal edges for static routing, or use conditional edges / [`Command`](https://reference.langchain.com/python/langgraph/types/Command) for dynamic routing. Do not mix normal edges and dynamic routing from the same node, because both paths can execute and make graph behavior harder to reason about.
</Warning>

### Normal edges

If you **always** want to go from node A to node B, you can use the [`add_edge`](https://reference.langchain.com/python/langgraph/pregel/_draw/add_edge) method directly.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
graph.add_edge("node_a", "node_b")
```

### Conditional edges

If you want to **optionally** route to one or more edges (or optionally terminate), you can use the [`add_conditional_edges`](https://reference.langchain.com/python/langgraph/graph/state/StateGraph/add_conditional_edges) method. This method accepts the name of a node and a "routing function" to call after that node is executed:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
graph.add_conditional_edges("node_a", routing_function)
```

Similar to nodes, the `routing_function` accepts the current `state` of the graph and returns a value.

By default, the return value `routing_function` is used as the name of the node (or list of nodes) to send the state to next. All those nodes will be run in parallel as a part of the next superstep.

You can optionally provide a dictionary that maps the `routing_function`'s output to the name of the next node.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
graph.add_conditional_edges("node_a", routing_function, {True: "node_b", False: "node_c"})
```

<Tip>
  Use [`Command`](#command) instead of conditional edges if you want to combine state updates and routing in a single function.
</Tip>

### Entry point

The entry point is the first node(s) that are run when the graph starts. You can use the [`add_edge`](https://reference.langchain.com/python/langgraph/pregel/_draw/add_edge) method from the virtual [`START`](https://reference.langchain.com/python/langgraph/constants/START) node to the first node to execute to specify where to enter the graph.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langgraph.graph import START

graph.add_edge(START, "node_a")
```

### Conditional entry point

A conditional entry point lets you start at different nodes depending on custom logic. You can use [`add_conditional_edges`](https://reference.langchain.com/python/langgraph/graph/state/StateGraph/add_conditional_edges) from the virtual [`START`](https://reference.langchain.com/python/langgraph/constants/START) node to accomplish this.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langgraph.graph import START

graph.add_conditional_edges(START, routing_function)
```

You can optionally provide a dictionary that maps the `routing_function`'s output to the name of the next node.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
graph.add_conditional_edges(START, routing_function, {True: "node_b", False: "node_c"})
```

## `Send`

By default, `Nodes` and `Edges` are defined ahead of time and operate on the same shared state. However, there can be cases where the exact edges are not known ahead of time and/or you may want different versions of `State` to exist at the same time. A common example of this is with [map-reduce](/oss/python/langgraph/use-graph-api#map-reduce-and-the-send-api) design patterns. In this design pattern, a first node may generate a list of objects, and you may want to apply some other node to all those objects. The number of objects may be unknown ahead of time (meaning the number of edges may not be known) and the input `State` to the downstream `Node` should be different (one for each generated object).

To support this design pattern, LangGraph supports returning [`Send`](https://reference.langchain.com/python/langgraph/types/Send) objects from conditional edges. `Send` takes two arguments: first is the name of the node, and second is the state to pass to that node.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langgraph.types import Send

def continue_to_jokes(state: OverallState):
    return [Send("generate_joke", {"subject": s}) for s in state['subjects']]

graph.add_conditional_edges("node_a", continue_to_jokes)
```

## `Command`

[`Command`](https://reference.langchain.com/python/langgraph/types/Command) is a versatile primitive for controlling graph execution. It accepts four parameters:

* `update`: Apply state updates (similar to returning updates from a node).
* `goto`: Navigate to specific nodes (similar to [conditional edges](#conditional-edges)).
* `graph`: Target a parent graph when navigating from [subgraphs](/oss/python/langgraph/use-subgraphs).
* `resume`: Provide a value to resume execution after an [interrupt](/oss/python/langgraph/interrupts).

`Command` is used in three contexts:

* **[Return from nodes](#return-from-nodes)**: Use `update`, `goto`, and `graph` to combine state updates with control flow.
* **[Input to `invoke` or `stream`](#input-to-invoke-or-stream)**: Use `resume` to continue execution after an interrupt.
* **[Return from tools](#return-from-tools)**: Similar to return from nodes, combine state updates and control flow from inside a tool.

### Return from nodes

#### `update` and `goto`

Return [`Command`](https://reference.langchain.com/python/langgraph/types/Command) from node functions to update state and route to the next node in a single step:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
def my_node(state: State) -> Command[Literal["my_other_node"]]:
    return Command(
        # state update
        update={"foo": "bar"},
        # control flow
        goto="my_other_node"
    )
```

With [`Command`](https://reference.langchain.com/python/langgraph/types/Command) you can also achieve dynamic control flow behavior (identical to [conditional edges](#conditional-edges)):

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
def my_node(state: State) -> Command[Literal["my_other_node"]]:
    if state["foo"] == "bar":
        return Command(update={"foo": "baz"}, goto="my_other_node")
```

Use [`Command`](https://reference.langchain.com/python/langgraph/types/Command) when you need to **both** update state **and** route to a different node. If you only need to route without updating state, use [conditional edges](#conditional-edges) instead.

<Note>
  When returning [`Command`](https://reference.langchain.com/python/langgraph/types/Command) in your node functions, you must add return type annotations with the list of node names the node is routing to, e.g. `Command[Literal["my_other_node"]]`. This is necessary for the graph rendering and tells LangGraph that `my_node` can navigate to `my_other_node`.
</Note>

<Warning>
  [`Command`](https://reference.langchain.com/python/langgraph/types/Command) only adds dynamic edges—static edges defined with `add_edge` / `addEdge` still execute. For example, if `node_a` returns `Command(goto="my_other_node")` and you also have `graph.add_edge("node_a", "node_b")`, both `node_b` and `my_other_node` will run. For each node, use either [`Command`](https://reference.langchain.com/python/langgraph/types/Command) or static edges to route to the next nodes, not both.
</Warning>

Check out this [how-to guide](/oss/python/langgraph/use-graph-api#combine-control-flow-and-state-updates-with-command) for an end-to-end example of how to use [`Command`](https://reference.langchain.com/python/langgraph/types/Command).

#### `graph`

If you are using [subgraphs](/oss/python/langgraph/use-subgraphs), you can navigate from a node within a subgraph to a different node in the parent graph by specifying `graph=Command.PARENT` in [`Command`](https://reference.langchain.com/python/langgraph/types/Command):

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
def my_node(state: State) -> Command[Literal["other_subgraph"]]:
    return Command(
        update={"foo": "bar"},
        goto="other_subgraph",  # where `other_subgraph` is a node in the parent graph
        graph=Command.PARENT
    )
```

<Note>
  Setting `graph` to `Command.PARENT` will navigate to the closest parent graph.

  When you send updates from a subgraph node to a parent graph node for a key that's shared by both parent and subgraph [state schemas](#schema), you **must** define a [reducer](#reducers) for the key you're updating in the parent graph state. See this [example](/oss/python/langgraph/use-graph-api#navigate-to-a-node-in-a-parent-graph).
</Note>

This is particularly useful when implementing [multi-agent handoffs](/oss/python/langchain/multi-agent/handoffs). Check out [Navigate to a node in a parent graph](/oss/python/langgraph/use-graph-api#navigate-to-a-node-in-a-parent-graph) for detail.

### Input to `invoke` or `stream`

<Warning>
  `Command(resume=...)` is the **only** `Command` pattern intended as input to `invoke()`/`stream()`. Do not use `Command(update=...)` as input to continue multi-turn conversations—because passing any `Command` as input resumes from the latest checkpoint (i.e. the last step that ran, not `__start__`), the graph will appear stuck if it already finished. To continue a conversation on an existing thread, pass a plain input dict:

  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  # WRONG - graph resumes from the latest checkpoint
  # (last step that ran), appears stuck
  graph.invoke(Command(update={  # [!code --]
      "messages": [{"role": "user", "content": "follow up"}]  # [!code --]
  }), config)  # [!code --]

  # CORRECT - plain dict restarts from __start__
  graph.invoke( {  # [!code ++]
      "messages": [{"role": "user", "content": "follow up"}]  # [!code ++]
  }, config)  # [!code ++]
  ```
</Warning>

#### `resume`

Use `Command(resume=...)` to provide a value and resume graph execution after an [interrupt](/oss/python/langgraph/interrupts). The value passed to `resume` becomes the return value of the `interrupt()` call inside the paused node:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from typing import TypedDict

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, START, StateGraph
from langgraph.types import Command, interrupt

class State(TypedDict):
    messages: list[dict]

def human_review(state: State):
    # Pauses the graph and waits for a value
    answer = interrupt("Do you approve?")
    return {"messages": [{"role": "user", "content": answer}]}

graph = (
    StateGraph(State)
    .add_node("human_review", human_review)
    .add_edge(START, "human_review")
    .add_edge("human_review", END)
    .compile(checkpointer=InMemorySaver())
)

config = {"configurable": {"thread_id": "graph-api-resume"}}

# First run - hits the interrupt and pauses
stream = graph.stream_events({"messages": []}, config, version="v3")
_ = stream.output  # drive the stream to completion
print(stream.interrupts)

# Resume with a value - the interrupt() call returns "yes"
resumed = graph.stream_events(Command(resume="yes"), config, version="v3")
final = resumed.output
```

Check out the [interrupts conceptual guide](/oss/python/langgraph/interrupts) for full details on interrupt patterns, including multiple interrupts and validation loops.

### Return from tools

You can return [`Command`](https://reference.langchain.com/python/langgraph/types/Command) from tools to update graph state and control flow. Use `update` to modify state (e.g., saving customer information looked up during a conversation) and `goto` to route to a specific node after the tool completes.

<Warning>
  When used inside tools, `goto` adds a dynamic edge—any static edges already defined on the node that called the tool will still execute. For each node, use either tool-driven dynamic routing or static edges to route to the next nodes, not both.
</Warning>

Refer to [Use inside tools](/oss/python/langgraph/use-graph-api#use-inside-tools) for detail.

## Graph migrations

LangGraph can easily handle migrations of graph definitions (nodes, edges, and state) even when using a checkpointer to track state.

* For threads at the end of the graph (i.e. not interrupted) you can change the entire topology of the graph (i.e. all nodes and edges, remove, add, rename, etc)
* For threads currently interrupted, we support all topology changes other than renaming / removing nodes (as that thread could now be about to enter a node that no longer exists) -- if this is a blocker please reach out and we can prioritize a solution.
* For modifying state, we have full backwards and forwards compatibility for adding and removing keys
* State keys that are renamed lose their saved state in existing threads
* State keys whose types change in incompatible ways could currently cause issues in threads with state from before the change -- if this is a blocker please reach out and we can prioritize a solution.

## Runtime context

When creating a graph, you can specify a `context_schema` for runtime context passed to nodes. This is useful for passing
information to nodes that is not part of the graph state. For example, you might want to pass dependencies such as model name or a database connection.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
@dataclass
class ContextSchema:
    llm_provider: str = "openai"

graph = StateGraph(State, context_schema=ContextSchema)
```

You can then pass this context into the graph using the `context` parameter of the `invoke` method.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
graph.invoke(inputs, context={"llm_provider": "anthropic"})
```

You can then access and use this context inside a node or conditional edge:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langgraph.runtime import Runtime

def node_a(state: State, runtime: Runtime[ContextSchema]):
    llm = get_llm(runtime.context.llm_provider)
    # ...
```

See [Add runtime configuration](/oss/python/langgraph/use-graph-api#add-runtime-configuration) for a full breakdown on configuration.

### Recursion limit

The recursion limit sets the maximum number of [super-steps](#graphs) the graph can execute during a single execution. Once the limit is reached, LangGraph will raise `GraphRecursionError`. Starting in version 1.0.6, the default recursion limit is set to 1000 steps. The recursion limit can be set on any graph at runtime, and is passed to `invoke`/`stream` via the config dictionary. Importantly, `recursion_limit` is a standalone `config` key and should not be passed inside the `configurable` key as all other user-defined configuration. See the example below:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
graph.invoke(inputs, config={"recursion_limit": 5}, context={"llm": "anthropic"})
```

Read [Recursion limit](/oss/python/langgraph/graph-api#recursion-limit) to learn more about how the recursion limit works.

### Accessing and handling the recursion counter

The current step counter is accessible in `config["metadata"]["langgraph_step"]` within any node, allowing for proactive recursion handling before hitting the recursion limit. This enables you to implement graceful degradation strategies within your graph logic.

#### How it works

The step counter is stored in `config["metadata"]["langgraph_step"]`. LangGraph increments this counter as the graph executes and raises a `GraphRecursionError` once the configured `recursion_limit` is exceeded.

#### Accessing the current step counter

You can access the current step counter within any node to monitor execution progress.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_core.runnables import RunnableConfig
from langgraph.graph import StateGraph

def my_node(state: dict, config: RunnableConfig) -> dict:
    current_step = config["metadata"]["langgraph_step"]
    print(f"Currently on step: {current_step}")
    return state
```

#### Proactive recursion handling

LangGraph provides a `RemainingSteps` managed value that tracks how many steps remain before hitting the recursion limit. This allows for graceful degradation within your graph.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from typing import Annotated, Literal
from langgraph.graph import StateGraph, START, END
from langgraph.managed import RemainingSteps

class State(TypedDict):
    messages: Annotated[list, lambda x, y: x + y]
    remaining_steps: RemainingSteps  # Managed value - tracks steps until limit

def reasoning_node(state: State) -> dict:
    # RemainingSteps is automatically populated by LangGraph
    remaining = state["remaining_steps"]

    # Check if we're running low on steps
    if remaining <= 2:
        return {"messages": ["Approaching limit, wrapping up..."]}

    # Normal processing
    return {"messages": ["thinking..."]}

def route_decision(state: State) -> Literal["reasoning_node", "fallback_node"]:
    """Route based on remaining steps"""
    if state["remaining_steps"] <= 2:
        return "fallback_node"
    return "reasoning_node"

def fallback_node(state: State) -> dict:
    """Handle cases where recursion limit is approaching"""
    return {"messages": ["Reached complexity limit, providing best effort answer"]}

# Build graph
builder = StateGraph(State)
builder.add_node("reasoning_node", reasoning_node)
builder.add_node("fallback_node", fallback_node)
builder.add_edge(START, "reasoning_node")
builder.add_conditional_edges("reasoning_node", route_decision)
builder.add_edge("fallback_node", END)

graph = builder.compile()

# RemainingSteps works with any recursion_limit
result = graph.invoke({"messages": []}, {"recursion_limit": 10})
```

#### Proactive vs reactive approaches

There are two main approaches to handling recursion limits: proactive (monitoring within the graph) and reactive (catching errors externally).

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from typing import Annotated, Literal, TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.managed import RemainingSteps
from langgraph.errors import GraphRecursionError

class State(TypedDict):
    messages: Annotated[list, lambda x, y: x + y]
    remaining_steps: RemainingSteps

# Proactive Approach (recommended) - using RemainingSteps
def agent_with_monitoring(state: State) -> dict:
    """Proactively monitor and handle recursion within the graph"""
    remaining = state["remaining_steps"]

    # Early detection - route to internal handling
    if remaining <= 2:
        return {
            "messages": ["Approaching limit, returning partial result"]
        }

    # Normal processing
    return {"messages": [f"Processing... ({remaining} steps remaining)"]}

def route_decision(state: State) -> Literal["agent", END]:
    if state["remaining_steps"] <= 2:
        return END
    return "agent"

# Build graph
builder = StateGraph(State)
builder.add_node("agent", agent_with_monitoring)
builder.add_edge(START, "agent")
builder.add_conditional_edges("agent", route_decision)
graph = builder.compile()

# Proactive: Graph completes gracefully
result = graph.invoke({"messages": []}, {"recursion_limit": 10})

# Reactive Approach (fallback) - catching error externally
try:
    result = graph.invoke({"messages": []}, {"recursion_limit": 10})
except GraphRecursionError as e:
    # Handle externally after graph execution fails
    result = {"messages": ["Fallback: recursion limit exceeded"]}
```

The key differences between these approaches are:

| Approach                                  | Detection            | Handling                             | Control Flow                       |
| ----------------------------------------- | -------------------- | ------------------------------------ | ---------------------------------- |
| Proactive (using `RemainingSteps`)        | Before limit reached | Inside graph via conditional routing | Graph continues to completion node |
| Reactive (catching `GraphRecursionError`) | After limit exceeded | Outside graph in try/catch           | Graph execution terminated         |

**Proactive advantages:**

* Graceful degradation within the graph
* Can save intermediate state in checkpoints
* Better user experience with partial results
* Graph completes normally (no exception)

**Reactive advantages:**

* Simpler implementation
* No need to modify graph logic
* Centralized error handling

#### Other available metadata

Along with `langgraph_step`, the following metadata is also available in `config["metadata"]`:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
def inspect_metadata(state: dict, config: RunnableConfig) -> dict:
    metadata = config["metadata"]

    print(f"Step: {metadata['langgraph_step']}")
    print(f"Node: {metadata['langgraph_node']}")
    print(f"Triggers: {metadata['langgraph_triggers']}")
    print(f"Path: {metadata['langgraph_path']}")
    print(f"Checkpoint NS: {metadata['langgraph_checkpoint_ns']}")

    return state
```

## Visualization

It's often nice to be able to visualize graphs, especially as they get more complex. LangGraph comes with several built-in ways to visualize graphs. See [Visualize your graph](/oss/python/langgraph/use-graph-api#visualize-your-graph) for more info.

## Observability and Tracing

To trace, debug and evaluate your agents, use [LangSmith](/langsmith/observability).

## Learn more

* [How to use the Graph API](/oss/python/langgraph/use-graph-api)
* [Functional API conceptual overview](/oss/python/langgraph/functional-api)
* [Choosing between Graph API and Functional API](/oss/python/langgraph/choosing-apis)

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langgraph/graph-api.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Install LangGraph
Source: https://docs.langchain.com/oss/python/langgraph/install

To install the base LangGraph package:

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install -U langgraph
  ```

  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv add langgraph
  ```
</CodeGroup>

To use LangGraph you will usually want to access LLMs and define tools.
You can do this however you see fit.

One way to do this (which we will use in the docs) is to use [LangChain](/oss/python/langchain/overview).

Install LangChain with:

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install -U langchain
  # Requires Python 3.10+
  ```

  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv add langchain
  # Requires Python 3.10+
  ```
</CodeGroup>

To work with specific LLM provider packages, you will need install them separately.

Refer to the [integrations](/oss/python/integrations/providers/overview) page for provider-specific installation instructions.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langgraph/install.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Interrupts
Source: https://docs.langchain.com/oss/python/langgraph/interrupts

Interrupts allow you to pause graph execution at specific points and wait for external input before continuing. This enables human-in-the-loop patterns where you need external input to proceed. When an interrupt is triggered, LangGraph saves the graph state using its [persistence](/oss/python/langgraph/persistence) layer and waits indefinitely until you resume execution.

Interrupts work by calling the `interrupt()` function at any point in your graph nodes. The function accepts any JSON-serializable value which is surfaced to the caller. When you're ready to continue, you resume execution by re-invoking the graph using `Command`, which then becomes the return value of the `interrupt()` call from inside the node.

Unlike static breakpoints (which pause before or after specific nodes), interrupts are **dynamic**: they can be placed anywhere in your code and can be conditional based on your application logic.

* **Checkpointing keeps your place:** the checkpointer writes the exact graph state so you can resume later, even when in an error state.
* **`thread_id` is your pointer:** set `config={"configurable": {"thread_id": ...}}` to tell the checkpointer which state to load.
* **Interrupt payloads surface via `stream.interrupts`:** when using [event streaming](/oss/python/langgraph/event-streaming) (`graph.stream_events(..., version="v3")`), the values you pass to `interrupt()` appear on `stream.interrupts`, and `stream.interrupted` is `True` when the run pauses for input.

The `thread_id` you choose is effectively your persistent cursor. Reusing it resumes the same checkpoint; using a new value starts a brand-new thread with an empty state.

## Pause using `interrupt`

The [`interrupt`](https://reference.langchain.com/python/langgraph/types/interrupt) function pauses graph execution and returns a value to the caller. When you call [`interrupt`](https://reference.langchain.com/python/langgraph/types/interrupt) within a node, LangGraph saves the current graph state and waits for you to resume execution with input.

To use [`interrupt`](https://reference.langchain.com/python/langgraph/types/interrupt), you need:

1. A **checkpointer** to persist the graph state (use a durable checkpointer in production)
2. A **thread ID** in your config so the runtime knows which state to resume from
3. To call `interrupt()` where you want to pause (payload must be JSON-serializable)

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langgraph.types import interrupt

def approval_node(state: State):
    # Pause and ask for approval
    approved = interrupt("Do you approve this action?")

    # When you resume, Command(resume=...) returns that value here
    return {"approved": approved}
```

When you call [`interrupt`](https://reference.langchain.com/python/langgraph/types/interrupt), here's what happens:

1. **Graph execution gets suspended** at the exact point where [`interrupt`](https://reference.langchain.com/python/langgraph/types/interrupt) is called

2. **State is saved** using the checkpointer so execution can be resumed later, In production, this should be a persistent checkpointer (e.g. backed by a database)

3. **Value is returned** to the caller on `stream.interrupts` when using [event streaming](/oss/python/langgraph/event-streaming) (`graph.stream_events(..., version="v3")`), or under `__interrupt__` with the default `invoke()` API; it can be any JSON-serializable value (string, object, array, etc.)

4. **Graph waits indefinitely** until you resume execution with a response

5. **Response is passed back** into the node when you resume, becoming the return value of the `interrupt()` call

## Resuming interrupts

After an interrupt pauses execution, you resume the graph by invoking it again with a `Command` that contains the resume value. The resume value is passed back to the `interrupt` call, allowing the node to continue execution with the external input.

The recommended way to drive a graph that may interrupt is [event streaming](/oss/python/langgraph/event-streaming) — it surfaces interrupts via `stream.interrupts` and `stream.interrupted`, and exposes the final state through `stream.output`.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langgraph.types import Command

# Initial run - hits the interrupt and pauses

# thread_id is the persistent pointer (stores a stable ID in production)
config = {"configurable": {"thread_id": "thread-1"}}
stream = graph.stream_events({"input": "data"}, config=config, version="v3")

# Drain the stream to drive the run; stream.output awaits the final state.
final = stream.output

# stream.interrupted is True when the run paused for human input, and

# stream.interrupts contains the payloads passed to interrupt().
if stream.interrupted:
    print(stream.interrupts)
    # > (Interrupt(value='Do you approve this action?'),)

# Resume with the human's response

# The resume payload becomes the return value of interrupt() inside the node
resumed = graph.stream_events(Command(resume=True), config=config, version="v3")
final = resumed.output
```

<Note>
  The default `graph.invoke(...)` API still works and surfaces interrupts under `result["__interrupt__"]`. Use it when you don't need streamed projections; otherwise prefer `graph.stream_events(..., version="v3")`.
</Note>

**Key points about resuming:**

* You must use the **same thread ID** when resuming that was used when the interrupt occurred
* The value passed to `Command(resume=...)` becomes the return value of the [`interrupt`](https://reference.langchain.com/python/langgraph/types/interrupt) call
* The node restarts from the beginning of the node where the [`interrupt`](https://reference.langchain.com/python/langgraph/types/interrupt) was called when resumed, so any code before the [`interrupt`](https://reference.langchain.com/python/langgraph/types/interrupt) runs again
* You can pass any JSON-serializable value as the resume value

<Warning>
  `Command(resume=...)` is the **only** `Command` pattern intended as input to `invoke()`/`stream()`/`stream_events()`. The other `Command` parameters (`update`, `goto`, `graph`) are designed for [returning from node functions](/oss/python/langgraph/graph-api#command). Do not pass `Command(update=...)` as input to continue multi-turn conversations—pass a plain input dict instead.
</Warning>

## Common patterns

The key thing that interrupts unlock is the ability to pause execution and wait for external input. This is useful for a variety of use cases, including:

* <Icon icon="circle-check" /> [Approval workflows](#approve-or-reject): Pause before executing critical actions (API calls, database changes, financial transactions)
* <Icon icon="link" /> [Handling multiple interrupts](#handling-multiple-interrupts): Pair interrupt IDs with resume values when resuming multiple interrupts in a single invocation
* <Icon icon="pencil" /> [Review and edit](#review-and-edit-state): Let humans review and modify LLM outputs or tool calls before continuing
* <Icon icon="tool" /> [Interrupting tool calls](#interrupts-in-tools): Pause before executing tool calls to review and edit the tool call before execution
* <Icon icon="shield-check" /> [Validating human input](#validating-human-input): Pause before proceeding to the next step to validate human input

### Stream with human-in-the-loop (HITL) interrupts

When building interactive agents with human-in-the-loop workflows, you can use [event streaming](/oss/python/langgraph/event-streaming) to consume message chunks and state snapshots concurrently while handling interrupts.

Use the typed projections returned by `graph.stream_events(..., version="v3")` in a loop until the run finishes:

* Stream AI responses token-by-token via `stream.messages`
* Observe per-step state snapshots via `stream.values`
* Detect interrupts via `stream.interrupted` and read their payloads from `stream.interrupts`
* Resume execution by calling `stream_events` again with `Command(resume=...)` and repeat until `stream.interrupted` is false

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langgraph.types import Command

stream_input: dict | Command = initial_input

while True:
    stream = graph.stream_events(stream_input, config=config, version="v3")

    # Stream LLM message chunks (including any in subgraphs) as they arrive.
    for message in stream.messages:
        for token in message.text:
            display_streaming_content(token)

    # After the run finishes (or pauses), check for interrupts and resume.
    if not stream.interrupted:
        final_state = stream.output
        break

    interrupt_info = stream.interrupts[0].value
    user_response = get_user_input(interrupt_info)
    stream_input = Command(resume=user_response)
```

* **`stream.messages`**: Chat-model output as content blocks; iterate each `message.text` for token deltas. For nested subgraphs, read message chunks from `stream.subgraphs[*].messages`.
* **`stream.values`**: Full state snapshots after each step
* **`stream.interrupted` / `stream.interrupts`**: After each run, check whether the graph paused; read payloads from `stream.interrupts`
* **`Command(resume=...)`**: Pass as the next `stream_events` input to resume; loop until the run completes without interrupting

### Handling multiple interrupts

When parallel branches interrupt simultaneously (for example, fan-out to multiple nodes that each call `interrupt()`), you may need to resume multiple interrupts in a single invocation.
When resuming multiple interrupts with a single invocation, map each interrupt ID to its resume value.
This ensures each response is paired with the correct interrupt at runtime.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from typing import Annotated, TypedDict
import operator

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, START, StateGraph
from langgraph.types import Command, interrupt

class State(TypedDict):
    vals: Annotated[list[str], operator.add]

def node_a(state):
    answer = interrupt("question_a")
    return {"vals": [f"a:{answer}"]}

def node_b(state):
    answer = interrupt("question_b")
    return {"vals": [f"b:{answer}"]}

graph = (
    StateGraph(State)
    .add_node("a", node_a)
    .add_node("b", node_b)
    .add_edge(START, "a")
    .add_edge(START, "b")
    .add_edge("a", END)
    .add_edge("b", END)
    .compile(checkpointer=InMemorySaver())
)

config = {"configurable": {"thread_id": "1"}}

# Step 1: stream events to drive the run; both parallel nodes hit interrupt() and pause
stream = graph.stream_events({"vals": []}, config, version="v3")
_ = stream.output  # drive the stream to completion

# stream.interrupts contains the pending Interrupt payloads
print(stream.interrupts)

# > (Interrupt(value='question_a', id='...'), Interrupt(value='question_b', id='...'))

# Step 2: resume all pending interrupts at once
resume_map = {
    i.id: f"answer for {i.value}" for i in stream.interrupts
}
resumed = graph.stream_events(Command(resume=resume_map), config, version="v3")

print("Final state:", resumed.output)
