# Use version="v2" for a unified StreamPart format
for chunk in graph.stream(
    inputs,
    stream_mode="messages",  # [!code highlight]
    version="v2",  # [!code highlight]
):
    if chunk["type"] == "messages":
        msg, metadata = chunk["data"]
        # Filter the streamed tokens by the langgraph_node field in the metadata
        # to only include the tokens from the specified node
        if msg.content and metadata["langgraph_node"] == "some_node_name":
            ...
```

<Accordion title="Extended example: streaming LLM tokens from specific nodes">
  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from typing import TypedDict
  from langgraph.graph import START, StateGraph
  from langchain_openai import ChatOpenAI

  model = ChatOpenAI(model="gpt-5.4-mini")

  class State(TypedDict):
        topic: str
        joke: str
        poem: str

  def write_joke(state: State):
        topic = state["topic"]
        joke_response = model.invoke(
              [{"role": "user", "content": f"Write a joke about {topic}"}]
        )
        return {"joke": joke_response.content}

  def write_poem(state: State):
        topic = state["topic"]
        poem_response = model.invoke(
              [{"role": "user", "content": f"Write a short poem about {topic}"}]
        )
        return {"poem": poem_response.content}

  graph = (
        StateGraph(State)
        .add_node(write_joke)
        .add_node(write_poem)
        # write both the joke and the poem concurrently
        .add_edge(START, "write_joke")
        .add_edge(START, "write_poem")
        .compile()
  )

  # The "messages" stream mode streams LLM tokens with metadata
  # Use version="v2" for a unified StreamPart format
  for chunk in graph.stream(
      {"topic": "cats"},
      stream_mode="messages",  # [!code highlight]
      version="v2",  # [!code highlight]
  ):
      if chunk["type"] == "messages":
          msg, metadata = chunk["data"]
          # Filter the streamed tokens by the langgraph_node field in the metadata
          # to only include the tokens from the write_poem node
          if msg.content and metadata["langgraph_node"] == "write_poem":
              print(msg.content, end="|", flush=True)
  ```
</Accordion>

### Custom data

To send **custom user-defined data** from inside a LangGraph node or tool, follow these steps:

1. Use [`get_stream_writer`](https://reference.langchain.com/python/langgraph/config/get_stream_writer) to access the stream writer and emit custom data.
2. Set `stream_mode="custom"` when calling `.stream()` or `.astream()` to get the custom data in the stream. You can combine multiple modes (e.g., `["updates", "custom"]`), but at least one must be `"custom"`.

<Warning>
  **No [`get_stream_writer`](https://reference.langchain.com/python/langgraph/config/get_stream_writer) in async for Python \< 3.11**
  In async code running on Python \< 3.11, [`get_stream_writer`](https://reference.langchain.com/python/langgraph/config/get_stream_writer) will not work.
  Instead, add a `writer` parameter to your node or tool and pass it manually.
  See [Async with Python \< 3.11](#async) for usage examples.
</Warning>

<Tabs>
  <Tab title="node">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from typing import TypedDict
    from langgraph.config import get_stream_writer
    from langgraph.graph import StateGraph, START

    class State(TypedDict):
        query: str
        answer: str

    def node(state: State):
        # Get the stream writer to send custom data
        writer = get_stream_writer()
        # Emit a custom key-value pair (e.g., progress update)
        writer({"custom_key": "Generating custom data inside node"})
        return {"answer": "some data"}

    graph = (
        StateGraph(State)
        .add_node(node)
        .add_edge(START, "node")
        .compile()
    )

    inputs = {"query": "example"}

    # Set stream_mode="custom" to receive the custom data in the stream
    for chunk in graph.stream(inputs, stream_mode="custom", version="v2"):
        if chunk["type"] == "custom":
            print(f"Custom event: {chunk['data']['custom_key']}")
    ```
  </Tab>

  <Tab title="tool">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from langchain.tools import tool
    from langgraph.config import get_stream_writer

    @tool
    def query_database(query: str) -> str:
        """Query the database."""
        # Access the stream writer to send custom data
        writer = get_stream_writer()  # [!code highlight]
        # Emit a custom key-value pair (e.g., progress update)
        writer({"data": "Retrieved 0/100 records", "type": "progress"})  # [!code highlight]
        # perform query
        # Emit another custom key-value pair
        writer({"data": "Retrieved 100/100 records", "type": "progress"})
        return "some-answer"

    graph = ... # define a graph that uses this tool

    # Set stream_mode="custom" to receive the custom data in the stream
    for chunk in graph.stream(inputs, stream_mode="custom", version="v2"):
        if chunk["type"] == "custom":
            print(f"{chunk['data']['type']}: {chunk['data']['data']}")
    ```
  </Tab>
</Tabs>

### Subgraph outputs

To include outputs from [subgraphs](/oss/python/langgraph/use-subgraphs) in the streamed outputs, you can set `subgraphs=True` in the `.stream()` method of the parent graph. This will stream outputs from both the parent graph and any subgraphs.

The outputs will be streamed as tuples `(namespace, data)`, where `namespace` is a tuple with the path to the node where a subgraph is invoked, e.g. `("parent_node:<task_id>", "child_node:<task_id>")`.

<Tabs>
  <Tab title="v2 (LangGraph >= 1.1)">
    With `version="v2"`, subgraph events use the same `StreamPart` format. The `ns` field identifies the source:

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    for chunk in graph.stream(
        {"foo": "foo"},
        subgraphs=True,  # [!code highlight]
        stream_mode="updates",
        version="v2", # [!code highlight]
    ):
        print(chunk["type"])  # "updates"
        print(chunk["ns"])    # () for root, ("node_name:<task_id>",) for subgraph
        print(chunk["data"])  # {"node_name": {"key": "value"}}
    ```
  </Tab>

  <Tab title="v1 (default)">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    for chunk in graph.stream(
        {"foo": "foo"},
        # Set subgraphs=True to stream outputs from subgraphs
        subgraphs=True,  # [!code highlight]
        stream_mode="updates",
    ):
        print(chunk)
    ```
  </Tab>
</Tabs>

<Accordion title="Extended example: streaming from subgraphs">
  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langgraph.graph import START, StateGraph
  from typing import TypedDict

  # Define subgraph
  class SubgraphState(TypedDict):
      foo: str  # note that this key is shared with the parent graph state
      bar: str

  def subgraph_node_1(state: SubgraphState):
      return {"bar": "bar"}

  def subgraph_node_2(state: SubgraphState):
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

  for chunk in graph.stream(
      {"foo": "foo"},
      stream_mode="updates",
      # Set subgraphs=True to stream outputs from subgraphs
      subgraphs=True,  # [!code highlight]
      version="v2",  # [!code highlight]
  ):
      if chunk["type"] == "updates":
          if chunk["ns"]:
              print(f"Subgraph {chunk['ns']}: {chunk['data']}")
          else:
              print(f"Root: {chunk['data']}")
  ```

  ```
  Root: {'node_1': {'foo': 'hi! foo'}}
  Subgraph ('node_2:dfddc4ba-c3c5-6887-5012-a243b5b377c2',): {'subgraph_node_1': {'bar': 'bar'}}
  Subgraph ('node_2:dfddc4ba-c3c5-6887-5012-a243b5b377c2',): {'subgraph_node_2': {'foo': 'hi! foobar'}}
  Root: {'node_2': {'foo': 'hi! foobar'}}
  ```

  **Note** that we are receiving not just the node updates, but we also the namespaces which tell us what graph (or subgraph) we are streaming from.
</Accordion>

### Checkpoints

Use the `checkpoints` streaming mode to receive checkpoint events as the graph executes. Each checkpoint event has the same format as the output of `get_state()`. Requires a [checkpointer](/oss/python/langgraph/persistence).

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langgraph.checkpoint.memory import MemorySaver

graph = (
    StateGraph(State)
    .add_node(refine_topic)
    .add_node(generate_joke)
    .add_edge(START, "refine_topic")
    .add_edge("refine_topic", "generate_joke")
    .add_edge("generate_joke", END)
    .compile(checkpointer=MemorySaver())
)

config = {"configurable": {"thread_id": "1"}}

for chunk in graph.stream(
    {"topic": "ice cream"},
    config=config,
    stream_mode="checkpoints",  # [!code highlight]
    version="v2",  # [!code highlight]
):
    if chunk["type"] == "checkpoints":
        print(chunk["data"])
```

### Tasks

Use the `tasks` streaming mode to receive task start and finish events as the graph executes. Task events include information about which node is running, its results, and any errors. Requires a [checkpointer](/oss/python/langgraph/persistence).

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langgraph.checkpoint.memory import MemorySaver

graph = (
    StateGraph(State)
    .add_node(refine_topic)
    .add_node(generate_joke)
    .add_edge(START, "refine_topic")
    .add_edge("refine_topic", "generate_joke")
    .add_edge("generate_joke", END)
    .compile(checkpointer=MemorySaver())
)

config = {"configurable": {"thread_id": "1"}}

for chunk in graph.stream(
    {"topic": "ice cream"},
    config=config,
    stream_mode="tasks",  # [!code highlight]
    version="v2",  # [!code highlight]
):
    if chunk["type"] == "tasks":
        print(chunk["data"])
```

<a />

### Debug

Use the `debug` streaming mode to stream as much information as possible throughout the execution of the graph. The streamed outputs include the name of the node as well as the full state.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
for chunk in graph.stream(
    {"topic": "ice cream"},
    stream_mode="debug",  # [!code highlight]
    version="v2",  # [!code highlight]
):
    if chunk["type"] == "debug":
        print(chunk["data"])
```

<Note>
  The `debug` mode combines `checkpoints` and `tasks` events with additional metadata. Use `checkpoints` or `tasks` directly if you only need a subset of the debug information.
</Note>

### Multiple modes at once

You can pass a list as the `stream_mode` parameter to stream multiple modes at once.

With `version="v2"`, every chunk is a `StreamPart` dict. Use `chunk["type"]` to distinguish between modes:

<CodeGroup>
  ```python v2 theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  for chunk in graph.stream(inputs, stream_mode=["updates", "custom"], version="v2"):
      if chunk["type"] == "updates":
          for node_name, state in chunk["data"].items():
              print(f"Node `{node_name}` updated: {state}")
      elif chunk["type"] == "custom":
          print(f"Custom event: {chunk['data']}")
  ```

  ```python v1 theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  for mode, chunk in graph.stream(inputs, stream_mode=["updates", "custom"]):
      print(chunk)
  ```
</CodeGroup>

## Advanced

### Use with any LLM

You can use `stream_mode="custom"` to stream data from **any LLM API**—even if that API does **not** implement the LangChain chat model interface.

This lets you integrate raw LLM clients or external services that provide their own streaming interfaces, making LangGraph highly flexible for custom setups.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langgraph.config import get_stream_writer

def call_arbitrary_model(state):
    """Example node that calls an arbitrary model and streams the output"""
    # Get the stream writer to send custom data
    writer = get_stream_writer()  # [!code highlight]
    # Assume you have a streaming client that yields chunks
    # Generate LLM tokens using your custom streaming client
    for chunk in your_custom_streaming_client(state["topic"]):
        # Use the writer to send custom data to the stream
        writer({"custom_llm_chunk": chunk})  # [!code highlight]
    return {"result": "completed"}

graph = (
    StateGraph(State)
    .add_node(call_arbitrary_model)
    # Add other nodes and edges as needed
    .compile()
)

# Set stream_mode="custom" to receive the custom data in the stream
for chunk in graph.stream(
    {"topic": "cats"},
    stream_mode="custom",  # [!code highlight]
    version="v2",  # [!code highlight]
):
    if chunk["type"] == "custom":
        # The chunk data will contain the custom data streamed from the llm
        print(chunk["data"])
```

<Accordion title="Extended example: streaming arbitrary chat model">
  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import operator
  import json

  from typing import TypedDict
  from typing_extensions import Annotated
  from langgraph.graph import StateGraph, START

  from openai import AsyncOpenAI

  openai_client = AsyncOpenAI()
  model_name = "gpt-5.4-mini"

  async def stream_tokens(model_name: str, messages: list[dict]):
      response = await openai_client.chat.completions.create(
          messages=messages, model=model_name, stream=True
      )
      role = None
      async for chunk in response:
          delta = chunk.choices[0].delta

          if delta.role is not None:
              role = delta.role

          if delta.content:
              yield {"role": role, "content": delta.content}

  # this is our tool
  async def get_items(place: str) -> str:
      """Use this tool to list items one might find in a place you're asked about."""
      writer = get_stream_writer()
      response = ""
      async for msg_chunk in stream_tokens(
          model_name,
          [
              {
                  "role": "user",
                  "content": (
                      "Can you tell me what kind of items "
                      f"i might find in the following place: '{place}'. "
                      "List at least 3 such items separating them by a comma. "
                      "And include a brief description of each item."
                  ),
              }
          ],
      ):
          response += msg_chunk["content"]
          writer(msg_chunk)

      return response

  class State(TypedDict):
      messages: Annotated[list[dict], operator.add]

  # this is the tool-calling graph node
  async def call_tool(state: State):
      ai_message = state["messages"][-1]
      tool_call = ai_message["tool_calls"][-1]

      function_name = tool_call["function"]["name"]
      if function_name != "get_items":
          raise ValueError(f"Tool {function_name} not supported")

      function_arguments = tool_call["function"]["arguments"]
      arguments = json.loads(function_arguments)

      function_response = await get_items(**arguments)
      tool_message = {
          "tool_call_id": tool_call["id"],
          "role": "tool",
          "name": function_name,
          "content": function_response,
      }
      return {"messages": [tool_message]}

  graph = (
      StateGraph(State)
      .add_node(call_tool)
      .add_edge(START, "call_tool")
      .compile()
  )
  ```

  Let's invoke the graph with an [`AIMessage`](https://reference.langchain.com/python/langchain-core/messages/ai/AIMessage) that includes a tool call:

  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  inputs = {
      "messages": [
          {
              "content": None,
              "role": "assistant",
              "tool_calls": [
                  {
                      "id": "1",
                      "function": {
                          "arguments": '{"place":"bedroom"}',
                          "name": "get_items",
                      },
                      "type": "function",
                  }
              ],
          }
      ]
  }

  async for chunk in graph.astream(
      inputs,
      stream_mode="custom",
      version="v2",
  ):
      if chunk["type"] == "custom":
          print(chunk["data"]["content"], end="|", flush=True)
  ```
</Accordion>

### Disable streaming for specific chat models

If your application mixes models that support streaming with those that do not, you may need to explicitly disable streaming for
models that do not support it.

Set `streaming=False` when initializing the model.

<Tabs>
  <Tab title="init_chat_model">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from langchain.chat_models import init_chat_model

    model = init_chat_model(
        "claude-sonnet-4-6",
        # Set streaming=False to disable streaming for the chat model
        streaming=False  # [!code highlight]
    )
    ```
  </Tab>

  <Tab title="Chat model interface">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from langchain_openai import ChatOpenAI

    # Set streaming=False to disable streaming for the chat model
    model = ChatOpenAI(model="o1-preview", streaming=False)
    ```
  </Tab>
</Tabs>

<Note>
  Not all chat model integrations support the `streaming` parameter. If your model doesn't support it, use `disable_streaming=True` instead. This parameter is available on all chat models via the base class.
</Note>

### Migrate to v2

The v2 streaming format (used throughout this page) provides a unified output format. Here's a summary of the key differences and how to migrate:

| Scenario                    | v1 (default)                       | v2 (`version="v2"`)                               |
| --------------------------- | ---------------------------------- | ------------------------------------------------- |
| Single stream mode          | Raw data (dict)                    | `StreamPart` dict with `type`, `ns`, `data`       |
| Multiple stream modes       | `(mode, data)` tuples              | Same `StreamPart` dict, filter on `chunk["type"]` |
| Subgraph streaming          | `(namespace, data)` tuples         | Same `StreamPart` dict, check `chunk["ns"]`       |
| Multiple modes + subgraphs  | `(namespace, mode, data)` triples  | Same `StreamPart` dict                            |
| `invoke()` return type      | Plain dict (state)                 | `GraphOutput` with `.value` and `.interrupts`     |
| Interrupt location (stream) | `__interrupt__` key in state dict  | `interrupts` field on `values` stream parts       |
| Interrupt location (invoke) | `__interrupt__` key in result dict | `.interrupts` attribute on `GraphOutput`          |
| Pydantic/dataclass output   | Returns plain dict                 | Coerces to model/dataclass instance               |

#### v2 invoke format

When you pass `version="v2"` to `invoke()` or `ainvoke()`, it returns a [`GraphOutput`](https://reference.langchain.com/python/langgraph/types/GraphOutput) object with `.value` and `.interrupts` attributes:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langgraph.types import GraphOutput

result = graph.invoke(inputs, version="v2")

assert isinstance(result, GraphOutput)
result.value       # your output — dict, Pydantic model, or dataclass
result.interrupts  # tuple[Interrupt, ...], empty if none occurred
```

With any stream mode other than the default `"values"`, `invoke(..., stream_mode="updates", version="v2")` returns `list[StreamPart]` instead of `list[tuple]`.

<Warning>
  Dict-style access on `GraphOutput` (`result["key"]`, `"key" in result`, `result["__interrupt__"]`) still works for backwards compatibility but is **deprecated** and will be removed in a future version. Migrate to `result.value` and `result.interrupts`.
</Warning>

This separates state from interrupt metadata. With v1, interrupts are embedded in the returned dict under `__interrupt__`:

<CodeGroup>
  ```python v2 (new) theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  config = {"configurable": {"thread_id": "thread-1"}}
  result = graph.invoke(inputs, config=config, version="v2")

  if result.interrupts:
      print(result.interrupts[0].value)
      graph.invoke(Command(resume=True), config=config, version="v2")
  ```

  ```python v1 (current default) theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  config = {"configurable": {"thread_id": "thread-1"}}
  result = graph.invoke(inputs, config=config)

  if "__interrupt__" in result:
      print(result["__interrupt__"][0].value)
      graph.invoke(Command(resume=True), config=config)
  ```
</CodeGroup>

#### Pydantic and dataclass state coercion

When your graph state is a Pydantic model or dataclass, v2 `values` mode automatically coerces output to the correct type:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from pydantic import BaseModel
from typing import Annotated
import operator

class MyState(BaseModel):
    value: str
    items: Annotated[list[str], operator.add]

# With version="v2", chunk["data"] is a MyState instance
for chunk in graph.stream(
    {"value": "x", "items": []}, stream_mode="values", version="v2"
):
    print(type(chunk["data"]))  # <class 'MyState'>
```

<a />

### Async with Python \< 3.11

In Python versions \< 3.11, [asyncio tasks](https://docs.python.org/3/library/asyncio-task.html#asyncio.create_task) do not support the `context` parameter.
This limits LangGraph ability to automatically propagate context, and affects LangGraph's streaming mechanisms in two key ways:

1. You **must** explicitly pass [`RunnableConfig`](https://python.langchain.com/docs/concepts/runnables/#runnableconfig) into async LLM calls (e.g., `ainvoke()`), as callbacks are not automatically propagated.
2. You **cannot** use [`get_stream_writer`](https://reference.langchain.com/python/langgraph/config/get_stream_writer) in async nodes or tools—you must pass a `writer` argument directly.

<Accordion title="Extended example: async LLM call with manual config">
  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from typing import TypedDict
  from langgraph.graph import START, StateGraph
  from langchain.chat_models import init_chat_model

  model = init_chat_model(model="gpt-5.4-mini")

  class State(TypedDict):
      topic: str
      joke: str

  # Accept config as an argument in the async node function
  async def call_model(state, config):
      topic = state["topic"]
      print("Generating joke...")
      # Pass config to model.ainvoke() to ensure proper context propagation
      joke_response = await model.ainvoke(  # [!code highlight]
          [{"role": "user", "content": f"Write a joke about {topic}"}],
          config,
      )
      return {"joke": joke_response.content}

  graph = (
      StateGraph(State)
      .add_node(call_model)
      .add_edge(START, "call_model")
      .compile()
  )

  # Set stream_mode="messages" to stream LLM tokens
  async for chunk in graph.astream(
      {"topic": "ice cream"},
      stream_mode="messages",  # [!code highlight]
      version="v2",  # [!code highlight]
  ):
      if chunk["type"] == "messages":
          message_chunk, metadata = chunk["data"]
          if message_chunk.content:
              print(message_chunk.content, end="|", flush=True)
  ```
</Accordion>

<Accordion title="Extended example: async custom streaming with stream writer">
  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from typing import TypedDict
  from langgraph.types import StreamWriter

  class State(TypedDict):
        topic: str
        joke: str

  # Add writer as an argument in the function signature of the async node or tool
  # LangGraph will automatically pass the stream writer to the function
  async def generate_joke(state: State, writer: StreamWriter):  # [!code highlight]
        writer({"custom_key": "Streaming custom data while generating a joke"})
        return {"joke": f"This is a joke about {state['topic']}"}

  graph = (
        StateGraph(State)
        .add_node(generate_joke)
        .add_edge(START, "generate_joke")
        .compile()
  )

  # Set stream_mode="custom" to receive the custom data in the stream  # [!code highlight]
  async for chunk in graph.astream(
        {"topic": "ice cream"},
        stream_mode="custom",
        version="v2",
  ):
        if chunk["type"] == "custom":
            print(chunk["data"])
  ```
</Accordion>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langgraph/streaming.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# LangSmith Studio
Source: https://docs.langchain.com/oss/python/langgraph/studio

When building agents with LangChain locally, it's helpful to visualize what's happening inside your agent, interact with it in real-time, and debug issues as they occur. **LangSmith Studio** is a free visual interface for developing and testing your LangChain agents from your local machine.

Studio connects to your locally running agent to show you each step your agent takes: the prompts sent to the model, tool calls and their results, and the final output. You can test different inputs, inspect intermediate states, and iterate on your agent's behavior without additional code or deployment.

This pages describes how to set up Studio with your local LangChain agent.

## Prerequisites

Before you begin, ensure you have the following:

* **A LangSmith account**: Sign up (for free) or log in at [smith.langchain.com](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=oss-langgraph-studio).
* **A LangSmith API key**: Follow the [Create an API key](/langsmith/create-account-api-key) guide.
* If you don't want data [traced](/langsmith/observability-concepts#traces) to LangSmith, set `LANGSMITH_TRACING=false` in your application's `.env` file. With tracing disabled, no data leaves your local server.

## Set up local Agent server

### 1. Install the LangGraph CLI

The [LangGraph CLI](/langsmith/cli) provides a local development server (also called [Agent Server](/langsmith/agent-server)) that connects your agent to Studio.

```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# Python >= 3.11 is required.
pip install --upgrade "langgraph-cli[inmem]"
```

### 2. Prepare your agent

If you already have a LangChain agent, you can use it directly. This example uses a simple email agent:

```python title="agent.py" theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain.agents import create_agent

def send_email(to: str, subject: str, body: str):
    """Send an email"""
    email = {
        "to": to,
        "subject": subject,
        "body": body
    }
    # ... email sending logic

    return f"Email sent to {to}"

agent = create_agent(
    "gpt-5.5",
    tools=[send_email],
    system_prompt="You are an email assistant. Always use the send_email tool.",
)
```

### 3. Environment variables

Studio requires a LangSmith API key to connect your local agent. Create a `.env` file in the root of your project and add your API key from [LangSmith](https://smith.langchain.com/settings).

<Warning>
  Ensure your `.env` file is not committed to version control, such as Git.
</Warning>

```bash .env theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
LANGSMITH_API_KEY=lsv2...
```

### 4. Create a LangGraph config file

The LangGraph CLI uses a configuration file to locate your agent and manage dependencies. Create a `langgraph.json` file in your app's directory:

```json title="langgraph.json" theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "dependencies": ["."],
  "graphs": {
    "agent": "./src/agent.py:agent"
  },
  "env": ".env"
}
```

The [`create_agent`](https://reference.langchain.com/python/langchain/agents/factory/create_agent) function automatically returns a compiled LangGraph graph, which is what the `graphs` key expects in the configuration file.

<Info>
  For detailed explanations of each key in the JSON object of the configuration file, refer to the [LangGraph configuration file reference](/langsmith/cli#configuration-file).
</Info>

At this point, the project structure will look like this:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
my-app/
├── src
│   └── agent.py
├── .env
└── langgraph.json
```

### 5. Install dependencies

Install your project dependencies from the root directory:

<CodeGroup>
  ```shell pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install langchain langchain-openai
  ```

  ```shell uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv add langchain langchain-openai
  ```
</CodeGroup>

### 6. View your agent in Studio

Start the development server to connect your agent to Studio:

```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
langgraph dev
```

<Warning>
  Safari blocks `localhost` connections to Studio. To work around this, run the above command with `--tunnel` to access Studio via a secure tunnel. You'll need to manually add the tunnel URL to allowed origins by clicking **Connect to a local server** in the Studio UI. See the [troubleshooting guide](/langsmith/troubleshooting-studio#safari-connection-issues) for steps.
</Warning>

Once the server is running, your agent is accessible both via API at `http://127.0.0.1:2024` and through the Studio UI at `https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024`:

<Frame>
  <img alt="Agent view in the Studio UI" />
</Frame>

With Studio connected to your local agent, you can iterate quickly on your agent's behavior. Run a test input, inspect the full execution trace including prompts, tool arguments, return values, and token/latency metrics in [LangSmith](/langsmith/observability-studio). When something goes wrong, Studio captures exceptions with the surrounding state to help you understand what happened.

The development server supports hot-reloading—make changes to prompts or tool signatures in your code, and Studio reflects them immediately. Re-run conversation threads from any step to test your changes without starting over. This workflow scales from simple single-tool agents to complex multi-node graphs.

For more information on how to run Studio, refer to the following guides in the [LangSmith docs](/langsmith/observability):

* [Run application](/langsmith/use-studio#run-application)
* [Manage assistants](/langsmith/use-studio#manage-assistants)
* [Manage threads](/langsmith/use-studio#manage-threads)
* [Iterate on prompts](/langsmith/observability-studio)
* [Debug LangSmith traces](/langsmith/observability-studio#debug-langsmith-traces)
* [Add node to dataset](/langsmith/observability-studio#add-node-to-dataset)

## Video guide

<Frame>
  <iframe title="Studio" />
</Frame>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langgraph/studio.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Test
Source: https://docs.langchain.com/oss/python/langgraph/test

After you've prototyped your LangGraph agent, a natural next step is to add tests. This guide covers some useful patterns you can use when writing unit tests.

Note that this guide is LangGraph-specific and covers scenarios around graphs with custom structures - if you are just getting started, check out [Test](/oss/python/langchain/test/) that uses LangChain's built-in [`create_agent`](https://reference.langchain.com/python/langchain/agents/factory/create_agent) instead.

## Prerequisites

First, make sure you have [`pytest`](https://docs.pytest.org/) installed:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
$ pip install -U pytest
```

## Getting started

Because many LangGraph agents depend on state, a useful pattern is to create your graph before each test where you use it, then compile it within tests with a new checkpointer instance.

The below example shows how this works with a simple, linear graph that progresses through `node1` and `node2`. Each node updates the single state key `my_key`:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import pytest

from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver

def create_graph() -> StateGraph:
    class MyState(TypedDict):
        my_key: str

    graph = StateGraph(MyState)
    graph.add_node("node1", lambda state: {"my_key": "hello from node1"})
    graph.add_node("node2", lambda state: {"my_key": "hello from node2"})
    graph.add_edge(START, "node1")
    graph.add_edge("node1", "node2")
    graph.add_edge("node2", END)
    return graph

def test_basic_agent_execution() -> None:
    checkpointer = MemorySaver()
    graph = create_graph()
    compiled_graph = graph.compile(checkpointer=checkpointer)
    result = compiled_graph.invoke(
        {"my_key": "initial_value"},
        config={"configurable": {"thread_id": "1"}}
    )
    assert result["my_key"] == "hello from node2"
```

## Testing individual nodes and edges

Compiled LangGraph agents expose references to each individual node as `graph.nodes`. You can take advantage of this to test individual nodes within your agent. Note that this will bypass any checkpointers passed when compiling the graph:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import pytest

from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver

def create_graph() -> StateGraph:
    class MyState(TypedDict):
        my_key: str

    graph = StateGraph(MyState)
    graph.add_node("node1", lambda state: {"my_key": "hello from node1"})
    graph.add_node("node2", lambda state: {"my_key": "hello from node2"})
    graph.add_edge(START, "node1")
    graph.add_edge("node1", "node2")
    graph.add_edge("node2", END)
    return graph

def test_individual_node_execution() -> None:
    # Will be ignored in this example
    checkpointer = MemorySaver()
    graph = create_graph()
    compiled_graph = graph.compile(checkpointer=checkpointer)
    # Only invoke node 1
    result = compiled_graph.nodes["node1"].invoke(
        {"my_key": "initial_value"},
    )
    assert result["my_key"] == "hello from node1"
```

## Partial execution

For agents made up of larger graphs, you may wish to test partial execution paths within your agent rather than the entire flow end-to-end. In some cases, it may make semantic sense to [restructure these sections as subgraphs](/oss/python/langgraph/use-subgraphs), which you can invoke in isolation as normal.

However, if you do not wish to make changes to your agent graph's overall structure, you can use LangGraph's persistence mechanisms to simulate a state where your agent is paused right before the beginning of the desired section, and will pause again at the end of the desired section. The steps are as follows:

1. Compile your agent with a checkpointer (the in-memory checkpointer [`InMemorySaver`](https://reference.langchain.com/python/langgraph/checkpoints/#langgraph.checkpoint.memory.InMemorySaver) will suffice for testing).
2. Call your agent's [`update_state`](/oss/python/langgraph/use-time-travel) method with an [`as_node`](/oss/python/langgraph/use-time-travel#from-a-specific-node) parameter set to the name of the node *before* the one you want to start your test.
3. Invoke your agent with the same `thread_id` you used to update the state and an `interrupt_after` parameter set to the name of the node you want to stop at.

Here's an example that executes only the second and third nodes in a linear graph:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import pytest

from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver

def create_graph() -> StateGraph:
    class MyState(TypedDict):
        my_key: str

    graph = StateGraph(MyState)
    graph.add_node("node1", lambda state: {"my_key": "hello from node1"})
    graph.add_node("node2", lambda state: {"my_key": "hello from node2"})
    graph.add_node("node3", lambda state: {"my_key": "hello from node3"})
    graph.add_node("node4", lambda state: {"my_key": "hello from node4"})
    graph.add_edge(START, "node1")
    graph.add_edge("node1", "node2")
    graph.add_edge("node2", "node3")
    graph.add_edge("node3", "node4")
    graph.add_edge("node4", END)
    return graph

def test_partial_execution_from_node2_to_node3() -> None:
    checkpointer = MemorySaver()
    graph = create_graph()
    compiled_graph = graph.compile(checkpointer=checkpointer)
    compiled_graph.update_state(
        config={
          "configurable": {
            "thread_id": "1"
          }
        },
        # The state passed into node 2 - simulating the state at
        # the end of node 1
        values={"my_key": "initial_value"},
        # Update saved state as if it came from node 1
        # Execution will resume at node 2
        as_node="node1",
    )
    result = compiled_graph.invoke(
        # Resume execution by passing None
        None,
        config={"configurable": {"thread_id": "1"}},
        # Stop after node 3 so that node 4 doesn't run
        interrupt_after="node3",
    )
    assert result["my_key"] == "hello from node3"
```

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langgraph/test.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Thinking in LangGraph
Source: https://docs.langchain.com/oss/python/langgraph/thinking-in-langgraph

Learn how to think about building agents with LangGraph

When you build an agent with LangGraph, you will first break it apart into discrete steps called **nodes**. Then, you will describe the different decisions and transitions from each of your nodes. Finally, you connect nodes together through a shared **state** that each node can read from and write to.

In this walkthrough, we'll guide you through the thought process of building a customer support email agent with LangGraph.

## Start with the process you want to automate

Imagine that you need to build an AI agent that handles customer support emails. Your product team has given you these requirements:

```txt theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
The agent should:

- Read incoming customer emails
- Classify them by urgency and topic
- Search relevant documentation to answer questions
- Draft appropriate responses
- Escalate complex issues to human agents
- Schedule follow-ups when needed

Example scenarios to handle:

1. Simple product question: "How do I reset my password?"
2. Bug report: "The export feature crashes when I select PDF format"
3. Urgent billing issue: "I was charged twice for my subscription!"
4. Feature request: "Can you add dark mode to the mobile app?"
5. Complex technical issue: "Our API integration fails intermittently with 504 errors"
```

To implement an agent in LangGraph, you will usually follow the same five steps.

## Step 1: Map out your workflow as discrete steps

Start by identifying the distinct steps in your process. Each step will become a **node** (a function that does one specific thing). Then, sketch how these steps connect to each other.

```mermaid theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
flowchart TD
    A[START] --> B[Read Email]
    B --> C[Classify Intent]

    C -.-> D[Doc Search]
    C -.-> E[Bug Track]
    C -.-> F[Human Review]

    D --> G[Draft Reply]
    E --> G
    F --> G

    G -.-> H[Human Review]
    G -.-> I[Send Reply]

    H --> J[END]
    I --> J[END]

    classDef process fill:#E5F4FF,stroke:#006DDD,stroke-width:2px,color:#030710
    class A,B,C,D,E,F,G,H,I,J process
```

The arrows in this diagram show possible paths, but the actual decision of which path to take happens inside each node.

Now that we've identified the components in our workflow, let's understand what each node needs to do:

* `Read Email`: Extract and parse the email content
* `Classify Intent`: Use an LLM to categorize urgency and topic, then route to appropriate action
* `Doc Search`: Query your knowledge base for relevant information
* `Bug Track`: Create or update issue in tracking system
* `Draft Reply`: Generate an appropriate response
* `Human Review`: Escalate to human agent for approval or handling
* `Send Reply`: Dispatch the email response

<Tip>
  Notice that some nodes make decisions about where to go next (`Classify Intent`, `Draft Reply`, `Human Review`), while others always proceed to the same next step (`Read Email` always goes to `Classify Intent`, `Doc Search` always goes to `Draft Reply`).
</Tip>

## Step 2: Identify what each step needs to do

For each node in your graph, determine what type of operation it represents and what context it needs to work properly.

<CardGroup>
  <Card title="LLM steps" icon="brain" href="#llm-steps">
    Use when you need to understand, analyze, generate text, or make reasoning decisions
  </Card>

  <Card title="Data steps" icon="database" href="#data-steps">
    Use when you need to retrieve information from external sources
  </Card>

  <Card title="Action steps" icon="bolt" href="#action-steps">
    Use when you need to perform external actions
  </Card>

  <Card title="User input steps" icon="user" href="#user-input-steps">
    Use when you need human intervention
  </Card>
</CardGroup>

### LLM steps

When a step needs to understand, analyze, generate text, or make reasoning decisions:

<AccordionGroup>
  <Accordion title="Classify intent">
    * Static context (prompt): Classification categories, urgency definitions, response format
    * Dynamic context (from state): Email content, sender information
    * Desired outcome: Structured classification that determines routing
  </Accordion>

  <Accordion title="Draft reply">
    * Static context (prompt): Tone guidelines, company policies, response templates
    * Dynamic context (from state): Classification results, search results, customer history
    * Desired outcome: Professional email response ready for review
  </Accordion>
</AccordionGroup>

### Data steps

When a step needs to retrieve information from external sources:

<AccordionGroup>
  <Accordion title="Document search">
    * Parameters: Query built from intent and topic
    * Retry strategy: Yes, with exponential backoff for transient failures
    * Caching: Could cache common queries to reduce API calls
  </Accordion>

  <Accordion title="Customer history lookup">
    * Parameters: Customer email or ID from state
    * Retry strategy: Yes, but with fallback to basic info if unavailable
    * Caching: Yes, with time-to-live to balance freshness and performance
  </Accordion>
</AccordionGroup>

### Action steps

When a step needs to perform an external action:

<AccordionGroup>
  <Accordion title="Send reply">
    * When to execute node: After approval (human or automated)
    * Retry strategy: Yes, with exponential backoff for network issues
    * Should not cache: Each send is a unique action
  </Accordion>

  <Accordion title="Bug track">
    * When to execute node: Always when intent is "bug"
    * Retry strategy: Yes, critical to not lose bug reports
    * Returns: Ticket ID to include in response
  </Accordion>
</AccordionGroup>

### User input steps

When a step needs human intervention:

<AccordionGroup>
  <Accordion title="Human review node">
    * Context for decision: Original email, draft response, urgency, classification
    * Expected input format: Approval boolean plus optional edited response
    * When triggered: High urgency, complex issues, or quality concerns
  </Accordion>
</AccordionGroup>

## Step 3: Design your state

State is the shared [memory](/oss/python/concepts/memory) accessible to all nodes in your agent. Think of it as the notebook your agent uses to keep track of everything it learns and decides as it works through the process.

### What belongs in state?

Ask yourself these questions about each piece of data:

<CardGroup>
  <Card title="Include in state" icon="check">
    Does it need to persist across steps? If yes, it goes in state.
  </Card>

  <Card title="Don't store" icon="code">
    Can you derive it from other data? If yes, compute it when needed instead of storing it in state.
  </Card>
</CardGroup>

For our email agent, we need to track:

* The original email and sender info (can't reconstruct these later)
* Classification results (needed by multiple later/downstream nodes)
* Search results and customer data (expensive to re-fetch)
* The draft response (needs to persist through review)
* Execution metadata (for debugging and recovery)

### Keep state raw, format prompts on-demand

<Tip>
  A key principle: your state should store raw data, not formatted text. Format prompts inside nodes when you need them.
</Tip>

This separation means:

* Different nodes can format the same data differently for their needs
* You can change prompt templates without modifying your state schema
* Debugging is clearer—you see exactly what data each node received
* Your agent can evolve without breaking existing state

Let's define our state:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from typing import TypedDict, Literal
