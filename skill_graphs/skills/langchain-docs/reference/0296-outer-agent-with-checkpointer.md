# Outer agent with checkpointer
agent = create_agent(
    model="gpt-5.4-mini",
    tools=[ask_fruit_expert, ask_veggie_expert],
    prompt=(
        "You have two experts: ask_fruit_expert and ask_veggie_expert. "
        "ALWAYS delegate questions to the appropriate expert."
    ),
    checkpointer=MemorySaver(),
)
```

<Tabs>
  <Tab title="Interrupts">
    Each invocation can use `interrupt()` to pause and resume. Add `interrupt()` to a tool function to require user approval before proceeding:

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    @tool
    def fruit_info(fruit_name: str) -> str:
        """Look up fruit info."""
        interrupt("continue?")  # [!code highlight]
        return f"Info about {fruit_name}"
    ```

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from langgraph.types import Command

    config = {"configurable": {"thread_id": "1"}}

    # Stream events - the subagent's tool calls interrupt()
    stream = agent.stream_events(
        {"messages": [{"role": "user", "content": "Tell me about apples"}]},
        config=config,
        version="v3",
    )
    output = stream.output  # drive the stream to completion
    # stream.interrupts contains pending interrupts (and stream.interrupted is True)

    # Resume - approve the interrupt
    resumed = agent.stream_events(Command(resume=True), config=config, version="v3")
    final = resumed.output
    ```
  </Tab>

  <Tab title="Multi-turn">
    Each invocation starts with a fresh subagent state. The subagent does not remember previous calls:

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    config = {"configurable": {"thread_id": "1"}}

    # First call
    response = agent.invoke(
        {"messages": [{"role": "user", "content": "Tell me about apples"}]},
        config=config,
    )
    # Subagent message count: 4

    # Second call - subagent starts fresh, no memory of apples
    response = agent.invoke(
        {"messages": [{"role": "user", "content": "Now tell me about bananas"}]},
        config=config,
    )
    # Subagent message count: 4 (still fresh!)
    ```
  </Tab>

  <Tab title="Multiple subgraph calls">
    Multiple calls to the same subgraph work without conflicts, since each invocation gets its own checkpoint namespace:

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    config = {"configurable": {"thread_id": "1"}}

    # LLM calls ask_fruit_expert for both apples and bananas
    response = agent.invoke(
        {"messages": [{"role": "user", "content": "Tell me about apples and bananas"}]},
        config=config,
    )
    # Subagent message count: 4 (apples - fresh)
    # Subagent message count: 4 (bananas - fresh)
    ```
  </Tab>
</Tabs>

#### Per-thread

Use per-thread persistence when a subagent needs to remember previous interactions. For example, a research assistant that builds up context over several exchanges, or a coding assistant that tracks what files it has already edited. The subagent's conversation history and data accumulate across calls on the same thread. Each call picks up where the last one left off.

Compile with `checkpointer=True` to enable this behavior.

<Warning>
  Per-thread subgraphs do not support parallel tool calls. When an LLM has access to a per-thread subagent as a tool, it may try to call that tool multiple times in parallel (for example, asking the fruit expert about apples and bananas simultaneously). This causes checkpoint conflicts because both calls write to the same namespace.

  The examples below use LangChain's `ToolCallLimitMiddleware` to prevent this. If you're building with pure LangGraph `StateGraph`, you need to prevent parallel tool calls yourself—for example, by configuring your model to disable parallel tool calling or by adding logic to ensure the same subgraph is not invoked multiple times in parallel.
</Warning>

The following examples use a fruit expert subagent compiled with `checkpointer=True`:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain.agents import create_agent
from langchain.agents.middleware import ToolCallLimitMiddleware
from langchain.tools import tool
from langgraph.checkpoint.memory import MemorySaver
from langgraph.types import Command, interrupt

@tool
def fruit_info(fruit_name: str) -> str:
    """Look up fruit info."""
    return f"Info about {fruit_name}"

# Subagent with checkpointer=True for persistent state
fruit_agent = create_agent(
    model="gpt-5.4-mini",
    tools=[fruit_info],
    prompt="You are a fruit expert. Use the fruit_info tool. Respond in one sentence.",
    checkpointer=True,  # [!code highlight]
)

# Wrap subagent as a tool for the outer agent
@tool
def ask_fruit_expert(question: str) -> str:
    """Ask the fruit expert. Use for ALL fruit questions."""
    response = fruit_agent.invoke(
        {"messages": [{"role": "user", "content": question}]},
    )
    return response["messages"][-1].content

# Outer agent with checkpointer

# Use ToolCallLimitMiddleware to prevent parallel calls to per-thread subagents,

# which would cause checkpoint conflicts.
agent = create_agent(
    model="gpt-5.4-mini",
    tools=[ask_fruit_expert],
    prompt="You have a fruit expert. ALWAYS delegate fruit questions to ask_fruit_expert.",
    middleware=[  # [!code highlight]
        ToolCallLimitMiddleware(tool_name="ask_fruit_expert", run_limit=1),  # [!code highlight]
    ],  # [!code highlight]
    checkpointer=MemorySaver(),
)
```

<Tabs>
  <Tab title="Interrupts">
    Per-thread subagents support `interrupt()` just like per-invocation. Add `interrupt()` to a tool function to require user approval:

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    @tool
    def fruit_info(fruit_name: str) -> str:
        """Look up fruit info."""
        interrupt("continue?")  # [!code highlight]
        return f"Info about {fruit_name}"
    ```

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from langgraph.types import Command

    config = {"configurable": {"thread_id": "1"}}

    # Stream events - the subagent's tool calls interrupt()
    stream = agent.stream_events(
        {"messages": [{"role": "user", "content": "Tell me about apples"}]},
        config=config,
        version="v3",
    )
    output = stream.output  # drive the stream to completion
    # stream.interrupts contains pending interrupts (and stream.interrupted is True)

    # Resume - approve the interrupt
    resumed = agent.stream_events(Command(resume=True), config=config, version="v3")
    final = resumed.output
    ```
  </Tab>

  <Tab title="Multi-turn">
    State accumulates across invocations—the subagent remembers past conversations:

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    config = {"configurable": {"thread_id": "1"}}

    # First call
    response = agent.invoke(
        {"messages": [{"role": "user", "content": "Tell me about apples"}]},
        config=config,
    )
    # Subagent message count: 4

    # Second call - subagent REMEMBERS apples conversation
    response = agent.invoke(
        {"messages": [{"role": "user", "content": "Now tell me about bananas"}]},
        config=config,
    )
    # Subagent message count: 8 (accumulated!)
    ```
  </Tab>

  <Tab title="Multiple subgraph calls">
    When you have multiple **different** per-thread subgraphs (for example, a fruit expert and a veggie expert), each one needs its own storage space so their checkpoints don't overwrite each other. This is called **namespace isolation**.

    If you [call subgraphs inside a node](#call-a-subgraph-inside-a-node), LangGraph assigns namespaces based on call order (first call, second call, etc.). This means reordering your calls can mix up which subgraph loads which state. To avoid this, wrap each subagent in its own `StateGraph` with a unique node name—this gives each subgraph a stable, unique namespace:

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from langgraph.graph import MessagesState, StateGraph

    def create_sub_agent(model, *, name, **kwargs):
        """Wrap an agent with a unique node name for namespace isolation."""
        agent = create_agent(model=model, name=name, **kwargs)
        return (
            StateGraph(MessagesState)
            .add_node(name, agent)  # unique name → stable namespace  # [!code highlight]
            .add_edge("__start__", name)
            .compile()
        )

    fruit_agent = create_sub_agent(
        "gpt-5.4-mini", name="fruit_agent",
        tools=[fruit_info], prompt="...", checkpointer=True,
    )
    veggie_agent = create_sub_agent(
        "gpt-5.4-mini", name="veggie_agent",
        tools=[veggie_info], prompt="...", checkpointer=True,
    )

    config = {"configurable": {"thread_id": "1"}}

    # First call - LLM calls both fruit and veggie experts
    response = agent.invoke(
        {"messages": [{"role": "user", "content": "Tell me about cherries and broccoli"}]},
        config=config,
    )
    # Fruit subagent message count: 4
    # Veggie subagent message count: 4

    # Second call - both agents accumulate independently
    response = agent.invoke(
        {"messages": [{"role": "user", "content": "Now tell me about oranges and carrots"}]},
        config=config,
    )
    # Fruit subagent message count: 8 (remembers cherries!)
    # Veggie subagent message count: 8 (remembers broccoli!)
    ```

    Subgraphs [added as nodes](#add-a-subgraph-as-a-node) already get name-based namespaces automatically, so they don't need this wrapper.
  </Tab>
</Tabs>

### Stateless

Use this when you want to run a subagent like a plain function call with no checkpointing overhead. The subgraph cannot pause/resume and does not benefit from [durable execution](/oss/python/langgraph/persistence). Compile with `checkpointer=False`.

<Warning>
  Without checkpointing, the subgraph has no durable execution. If the process crashes mid-run, the subgraph cannot recover and must be re-run from the beginning.
</Warning>

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
subgraph_builder = StateGraph(...)
subgraph = subgraph_builder.compile(checkpointer=False)  # [!code highlight]
```

### Checkpointer reference

Control subgraph persistence with the `checkpointer` parameter on `.compile()`:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
subgraph = builder.compile(checkpointer=False)  # or True / None
```

| Feature                              | Per-invocation (default) | Per-thread            | Stateless |
| ------------------------------------ | ------------------------ | --------------------- | --------- |
| `checkpointer=`                      | `None`                   | `True`                | `False`   |
| Interrupts (HITL)                    | ✅                        | ✅                     | ❌         |
| Multi-turn memory                    | ❌                        | ✅                     | ❌         |
| Multiple calls (different subgraphs) | ✅                        | <Tooltip>⚠️</Tooltip> | ✅         |
| Multiple calls (same subgraph)       | ✅                        | ❌                     | ✅         |
| State inspection                     | <Tooltip>⚠️</Tooltip>    | ✅                     | ❌         |

* **Interrupts (HITL)**: The subgraph can use [interrupt()](/oss/python/langgraph/interrupts) to pause execution and wait for user input, then resume where it left off.
* **Multi-turn memory**: The subgraph retains its state across multiple invocations within the same [thread](/oss/python/langgraph/checkpointers#threads). Each call picks up where the last one left off rather than starting fresh.
* **Multiple calls (different subgraphs)**: Multiple different subgraph instances can be invoked within a single node without checkpoint namespace conflicts.
* **Multiple calls (same subgraph)**: The same subgraph instance can be invoked multiple times within a single node. With stateful persistence, these calls write to the same checkpoint namespace and conflict—use per-invocation persistence instead.
* **State inspection**: The subgraph's state is available via `get_state(config, subgraphs=True)` for debugging and monitoring.

## View subgraph state

When you enable [persistence](/oss/python/langgraph/persistence), you can inspect the subgraph state using the subgraphs option. With [stateless](#stateless) checkpointing (`checkpointer=False`), no subgraph checkpoints are saved, so subgraph state is not available.

<Note>
  Viewing subgraph state requires that LangGraph can **statically discover** the subgraph—i.e., it is [added as a node](#add-a-subgraph-as-a-node) or [called inside a node](#call-a-subgraph-inside-a-node). It does not work when a subgraph is called inside a [tool](/oss/python/langchain/tools) function or other indirection (e.g., the [subagents](/oss/python/langchain/multi-agent/subagents) pattern). Interrupts still propagate to the top-level graph regardless of nesting.
</Note>

<Tabs>
  <Tab title="Per-invocation">
    Returns subgraph state for the **current invocation only**. Each invocation starts fresh.

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from langgraph.graph import START, StateGraph
    from langgraph.checkpoint.memory import MemorySaver
    from langgraph.types import interrupt, Command
    from typing_extensions import TypedDict

    class State(TypedDict):
        foo: str

    # Subgraph
    def subgraph_node_1(state: State):
        value = interrupt("Provide value:")
        return {"foo": state["foo"] + value}

    subgraph_builder = StateGraph(State)
    subgraph_builder.add_node(subgraph_node_1)
    subgraph_builder.add_edge(START, "subgraph_node_1")
    subgraph = subgraph_builder.compile()  # inherits parent checkpointer

    # Parent graph
    builder = StateGraph(State)
    builder.add_node("node_1", subgraph)
    builder.add_edge(START, "node_1")

    checkpointer = MemorySaver()
    graph = builder.compile(checkpointer=checkpointer)

    config = {"configurable": {"thread_id": "1"}}

    graph.invoke({"foo": ""}, config)

    # View subgraph state for the current invocation
    subgraph_state = graph.get_state(config, subgraphs=True).tasks[0].state  # [!code highlight]

    # Resume the subgraph
    graph.invoke(Command(resume="bar"), config)
    ```
  </Tab>

  <Tab title="Per-thread">
    Returns **accumulated** subgraph state across all invocations on this thread.

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from langgraph.graph import START, StateGraph, MessagesState
    from langgraph.checkpoint.memory import MemorySaver

    # Subgraph with its own persistent state
    subgraph_builder = StateGraph(MessagesState)
    # ... add nodes and edges
    subgraph = subgraph_builder.compile(checkpointer=True)  # [!code highlight]

    # Parent graph
    builder = StateGraph(MessagesState)
    builder.add_node("agent", subgraph)
    builder.add_edge(START, "agent")

    checkpointer = MemorySaver()
    graph = builder.compile(checkpointer=checkpointer)

    config = {"configurable": {"thread_id": "1"}}

    graph.invoke({"messages": [{"role": "user", "content": "hi"}]}, config)
    graph.invoke({"messages": [{"role": "user", "content": "what did I say?"}]}, config)

    # View accumulated subgraph state (includes messages from both invocations)
    subgraph_state = graph.get_state(config, subgraphs=True).tasks[0].state  # [!code highlight]
    ```
  </Tab>
</Tabs>

## Stream subgraph outputs

To observe nested graph executions, we recommend [event streaming](/oss/python/langgraph/event-streaming): the `stream.subgraphs` projection discovers each nested run and exposes its `path`, `messages`, and `values` without parsing namespace strings.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
stream = graph.stream_events({"foo": "foo"}, version="v3")  # [!code highlight]

for subgraph in stream.subgraphs:
    print(subgraph.graph_name, subgraph.path)

    for snapshot in subgraph.values:
        print(subgraph.path, snapshot)
```

If you need the raw protocol events, iterate the stream directly and filter on `event["method"]` and `event["params"]["namespace"]`:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
stream = graph.stream_events({"foo": "foo"}, version="v3")
for event in stream:
    if event["method"] == "updates":
        print(event["params"]["namespace"], event["params"]["data"])
```

<Accordion title="Stream from subgraphs">
  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from typing_extensions import TypedDict
  from langgraph.graph.state import StateGraph, START

  # Define subgraph
  class SubgraphState(TypedDict):
      foo: str
      bar: str

  def subgraph_node_1(state: SubgraphState):
      return {"bar": "bar"}

  def subgraph_node_2(state: SubgraphState):
      # note that this node is using a state key ('bar') that is only available in the subgraph
      # and is sending update on the shared state key ('foo')
      return {"foo": state["foo"] + state["bar"]}

  subgraph_builder = StateGraph(SubgraphState)
  subgraph_builder.add_node(subgraph_node_1)
  subgraph_builder.add_node(subgraph_node_2)
  subgraph_builder.add_edge(START, "subgraph_node_1")
  subgraph_builder.add_edge("subgraph_node_1", "subgraph_node_2")
  subgraph = subgraph_builder.compile()

  # Define parent graph
  class ParentState(TypedDict):
      foo: str

  def node_1(state: ParentState):
      return {"foo": "hi! " + state["foo"]}

  builder = StateGraph(ParentState)
  builder.add_node("node_1", node_1)
  builder.add_node("node_2", subgraph)
  builder.add_edge(START, "node_1")
  builder.add_edge("node_1", "node_2")
  graph = builder.compile()

  stream = graph.stream_events({"foo": "foo"}, version="v3")  # [!code highlight]
  for event in stream:
      if event["method"] == "updates":
          print(event["params"]["namespace"], event["params"]["data"])
  ```

  ```
  [] {'node_1': {'foo': 'hi! foo'}}
  ['node_2:e58e5673-a661-ebb0-70d4-e298a7fc28b7'] {'subgraph_node_1': {'bar': 'bar'}}
  ['node_2:e58e5673-a661-ebb0-70d4-e298a7fc28b7'] {'subgraph_node_2': {'foo': 'hi! foobar'}}
  [] {'node_2': {'foo': 'hi! foobar'}}
  ```
</Accordion>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langgraph/use-subgraphs.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Use time-travel
Source: https://docs.langchain.com/oss/python/langgraph/use-time-travel

Replay past executions and fork to explore alternative paths in LangGraph

## Overview

LangGraph supports time travel through [checkpoints](/oss/python/langgraph/checkpointers#checkpoints):

* **[Replay](#replay)**: Retry from a prior checkpoint.
* **[Fork](#fork)**: Branch from a prior checkpoint with modified state to explore an alternative path.

Both work by resuming from a prior checkpoint. Nodes before the checkpoint are not re-executed (results are already saved). Nodes after the checkpoint re-execute, including any LLM calls, API requests, and [interrupts](/oss/python/langgraph/interrupts) (which may produce different results).

## Replay

Invoke the graph with a prior checkpoint's config to replay from that point.

<Warning>
  Replay re-executes nodes—it doesn't just read from cache. LLM calls, API requests, and [interrupts](/oss/python/langgraph/interrupts) fire again and may return different results. Replaying from the final checkpoint (no `next` nodes) is a no-op.
</Warning>

<img alt="Replay" />

Use [`get_state_history`](https://reference.langchain.com/python/langgraph/graphs/#langgraph.graph.state.CompiledStateGraph.get_state_history) to find the checkpoint you want to replay from, then call [`invoke`](https://reference.langchain.com/python/langgraph/graphs/#langgraph.graph.state.CompiledStateGraph.invoke) with that checkpoint's config:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langgraph.graph import StateGraph, START
from langgraph.checkpoint.memory import InMemorySaver
from typing_extensions import TypedDict, NotRequired
from langchain_core.utils.uuid import uuid7

class State(TypedDict):
    topic: NotRequired[str]
    joke: NotRequired[str]

def generate_topic(state: State):
    return {"topic": "socks in the dryer"}

def write_joke(state: State):
    return {"joke": f"Why do {state['topic']} disappear? They elope!"}

checkpointer = InMemorySaver()
graph = (
    StateGraph(State)
    .add_node("generate_topic", generate_topic)
    .add_node("write_joke", write_joke)
    .add_edge(START, "generate_topic")
    .add_edge("generate_topic", "write_joke")
    .compile(checkpointer=checkpointer)
)

# Step 1: Run the graph
config = {"configurable": {"thread_id": str(uuid7())}}
result = graph.invoke({}, config)

# Step 2: Find a checkpoint to replay from
history = list(graph.get_state_history(config))

# History is in reverse chronological order
for state in history:
    print(f"next={state.next}, checkpoint_id={state.config['configurable']['checkpoint_id']}")

# Step 3: Replay from a specific checkpoint

# Find the checkpoint before write_joke
before_joke = next(s for s in history if s.next == ("write_joke",))
replay_result = graph.invoke(None, before_joke.config)

# write_joke re-executes (runs again), generate_topic does not
```

## Fork

Fork creates a new branch from a past checkpoint with modified state. Call [`update_state`](https://reference.langchain.com/python/langgraph/graphs/#langgraph.graph.state.CompiledStateGraph.update_state) on a prior checkpoint to create the fork, then [`invoke`](https://reference.langchain.com/python/langgraph/graphs/#langgraph.graph.state.CompiledStateGraph.invoke) with `None` to continue execution.

<img alt="Fork" />

<Warning>
  `update_state` does **not** roll back a thread. It creates a new checkpoint that branches from the specified point. The original execution history remains intact.
</Warning>

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# Find checkpoint before write_joke
history = list(graph.get_state_history(config))
before_joke = next(s for s in history if s.next == ("write_joke",))

# Fork: update state to change the topic
fork_config = graph.update_state(
    before_joke.config,
    values={"topic": "chickens"},
)

# Resume from the fork — write_joke re-executes with the new topic
fork_result = graph.invoke(None, fork_config)
print(fork_result["joke"])  # A joke about chickens, not socks
```

### From a specific node

When you call [`update_state`](https://reference.langchain.com/python/langgraph/graphs/#langgraph.graph.state.CompiledStateGraph.update_state), values are applied using the specified node's writers (including [reducers](/oss/python/langgraph/graph-api#reducers)). The checkpoint records that node as having produced the update, and execution resumes from that node's successors.

By default, LangGraph infers `as_node` from the checkpoint's version history. When forking from a specific checkpoint, this inference is almost always correct.

Specify `as_node` explicitly when:

* **Parallel branches**: Multiple nodes updated state in the same step, and LangGraph can't determine which was last (`InvalidUpdateError`).
* **No execution history**: Setting up state on a fresh thread (common in [testing](/oss/python/langgraph/test)).
* **Skipping nodes**: Set `as_node` to a later node to make the graph think that node already ran.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# graph: generate_topic -> write_joke

# Treat this update as if generate_topic produced it.

# Execution resumes at write_joke (the successor of generate_topic).
fork_config = graph.update_state(
    before_joke.config,
    values={"topic": "chickens"},
    as_node="generate_topic",
)
```

## Interrupts

If your graph uses [`interrupt`](https://reference.langchain.com/python/langgraph/types/interrupt) for [human-in-the-loop](/oss/python/langgraph/interrupts) workflows, interrupts are always re-triggered during time travel. The node containing the interrupt re-executes, and `interrupt()` pauses for a new `Command(resume=...)`.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langgraph.types import interrupt, Command

class State(TypedDict):
    value: list[str]

def ask_human(state: State):
    answer = interrupt("What is your name?")
    return {"value": [f"Hello, {answer}!"]}

def final_step(state: State):
    return {"value": ["Done"]}

graph = (
    StateGraph(State)
    .add_node("ask_human", ask_human)
    .add_node("final_step", final_step)
    .add_edge(START, "ask_human")
    .add_edge("ask_human", "final_step")
    .compile(checkpointer=InMemorySaver())
)

config = {"configurable": {"thread_id": "1"}}

# First run: hits interrupt
graph.invoke({"value": []}, config)

# Resume with answer
graph.invoke(Command(resume="Alice"), config)

# Replay from before ask_human
history = list(graph.get_state_history(config))
before_ask = [s for s in history if s.next == ("ask_human",)][-1]

replay_result = graph.invoke(None, before_ask.config)

# Pauses at interrupt — waiting for new Command(resume=...)

# Fork from before ask_human
fork_config = graph.update_state(before_ask.config, {"value": ["forked"]})
fork_result = graph.invoke(None, fork_config)

# Pauses at interrupt — waiting for new Command(resume=...)

# Resume the forked interrupt with a different answer
graph.invoke(Command(resume="Bob"), fork_config)

# Result: {"value": ["forked", "Hello, Bob!", "Done"]}
```

### Multiple interrupts

If your graph collects input at several points (for example, a multi-step form), you can fork from between the interrupts to change a later answer without re-asking earlier questions.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
def ask_name(state):
    name = interrupt("What is your name?")
    return {"value": [f"name:{name}"]}

def ask_age(state):
    age = interrupt("How old are you?")
    return {"value": [f"age:{age}"]}

# Graph: ask_name -> ask_age -> final

# After completing both interrupts:

# Fork from BETWEEN the two interrupts (after ask_name, before ask_age)
history = list(graph.get_state_history(config))
between = [s for s in history if s.next == ("ask_age",)][-1]

fork_config = graph.update_state(between.config, {"value": ["modified"]})
result = graph.invoke(None, fork_config)

# ask_name result preserved ("name:Alice")

# ask_age pauses at interrupt — waiting for new answer
```

## Subgraphs

Time travel with [subgraphs](/oss/python/langgraph/use-subgraphs) depends on whether the subgraph has its own checkpointer. This determines the granularity of checkpoints you can time travel from.

<Tabs>
  <Tab title="Inherited checkpointer (default)">
    By default, a subgraph inherits the parent's checkpointer. The parent treats the entire subgraph as a **single super-step** — there is only one parent-level checkpoint for the whole subgraph execution. Time traveling from before the subgraph re-executes it from scratch.

    You cannot time travel to a point *between* nodes in a default subgraph — you can only time travel from the parent level.

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    # Subgraph without its own checkpointer (default)
    subgraph = (
        StateGraph(State)
        .add_node("step_a", step_a)       # Has interrupt()
        .add_node("step_b", step_b)       # Has interrupt()
        .add_edge(START, "step_a")
        .add_edge("step_a", "step_b")
        .compile()  # No checkpointer — inherits from parent
    )

    graph = (
        StateGraph(State)
        .add_node("subgraph_node", subgraph)
        .add_edge(START, "subgraph_node")
        .compile(checkpointer=InMemorySaver())
    )

    config = {"configurable": {"thread_id": "1"}}

    # Complete both interrupts
    graph.invoke({"value": []}, config)            # Hits step_a interrupt
    graph.invoke(Command(resume="Alice"), config)  # Hits step_b interrupt
    graph.invoke(Command(resume="30"), config)     # Completes

    # Time travel from before the subgraph
    history = list(graph.get_state_history(config))
    before_sub = [s for s in history if s.next == ("subgraph_node",)][-1]

    fork_config = graph.update_state(before_sub.config, {"value": ["forked"]})
    result = graph.invoke(None, fork_config)
    # The entire subgraph re-executes from scratch
    # You cannot time travel to a point between step_a and step_b
    ```
  </Tab>

  <Tab title="Subgraph checkpointer">
    Set `checkpointer=True` on the subgraph to give it its own checkpoint history. This creates checkpoints at each step **within** the subgraph, allowing you to time travel from a specific point inside it — for example, between two interrupts.

    Use [`get_state`](https://reference.langchain.com/python/langgraph/graphs/#langgraph.graph.state.CompiledStateGraph.get_state) with `subgraphs=True` to access the subgraph's own checkpoint config, then fork from it:

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    # Subgraph with its own checkpointer
    subgraph = (
        StateGraph(State)
        .add_node("step_a", step_a)       # Has interrupt()
        .add_node("step_b", step_b)       # Has interrupt()
        .add_edge(START, "step_a")
        .add_edge("step_a", "step_b")
        .compile(checkpointer=True)  # Own checkpoint history
    )

    graph = (
        StateGraph(State)
        .add_node("subgraph_node", subgraph)
        .add_edge(START, "subgraph_node")
        .compile(checkpointer=InMemorySaver())
    )

    config = {"configurable": {"thread_id": "1"}}

    # Run until step_a interrupt
    graph.invoke({"value": []}, config)

    # Resume step_a -> hits step_b interrupt
    graph.invoke(Command(resume="Alice"), config)

    # Get the subgraph's own checkpoint (between step_a and step_b)
    parent_state = graph.get_state(config, subgraphs=True)
    sub_config = parent_state.tasks[0].state.config

    # Fork from the subgraph checkpoint
    fork_config = graph.update_state(sub_config, {"value": ["forked"]})
    result = graph.invoke(None, fork_config)
    # step_b re-executes, step_a's result is preserved
    ```
  </Tab>
</Tabs>

See [subgraph persistence](/oss/python/langgraph/use-subgraphs#subgraph-persistence) for more on configuring subgraph checkpointers.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langgraph/use-time-travel.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Workflows and agents
Source: https://docs.langchain.com/oss/python/langgraph/workflows-agents

This guide reviews common workflow and agent patterns.

* Workflows have predetermined code paths and are designed to operate in a certain order.
* Agents are dynamic and define their own processes and tool usage.

<img alt="Agent Workflow" />

LangGraph offers several benefits when building agents and workflows, including [persistence](/oss/python/langgraph/persistence), [streaming](/oss/python/langgraph/streaming), and support for debugging as well as [deployment](/oss/python/langgraph/deploy).

<Tip>
  Trace and compare these workflow patterns with [LangSmith](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=oss-langgraph-workflows-agents). Follow the [tracing quickstart](/langsmith/trace-with-langgraph) to see how data flows through each step. We recommend you also set up [LangSmith Engine](/langsmith/engine) which monitors your traces, detects issues, and proposes fixes.
</Tip>

## Setup

To build a workflow or agent, you can use [any chat model](/oss/python/integrations/chat) that supports structured outputs and tool calling. The following example uses Anthropic:

1. Install dependencies:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
pip install langchain_core langchain-anthropic langgraph
```

2. Initialize the LLM:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import os
import getpass

from langchain_anthropic import ChatAnthropic

def _set_env(var: str):
    if not os.environ.get(var):
        os.environ[var] = getpass.getpass(f"{var}: ")

_set_env("ANTHROPIC_API_KEY")

llm = ChatAnthropic(model="claude-sonnet-4-6")
```

## LLMs and augmentations

Workflows and agentic systems are based on LLMs and the various augmentations you add to them. [Tool calling](/oss/python/langchain/tools), [structured outputs](/oss/python/langchain/structured-output), and [short term memory](/oss/python/langchain/short-term-memory) are a few options for tailoring LLMs to your needs.

<img alt="LLM augmentations" />

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# Schema for structured output
from pydantic import BaseModel, Field

class SearchQuery(BaseModel):
    search_query: str = Field(None, description="Query that is optimized web search.")
    justification: str = Field(
        None, description="Why this query is relevant to the user's request."
    )

# Augment the LLM with schema for structured output
structured_llm = llm.with_structured_output(SearchQuery)

# Invoke the augmented LLM
output = structured_llm.invoke("How does Calcium CT score relate to high cholesterol?")

# Define a tool
def multiply(a: int, b: int) -> int:
    return a * b

# Augment the LLM with tools
llm_with_tools = llm.bind_tools([multiply])

# Invoke the LLM with input that triggers the tool call
msg = llm_with_tools.invoke("What is 2 times 3?")
