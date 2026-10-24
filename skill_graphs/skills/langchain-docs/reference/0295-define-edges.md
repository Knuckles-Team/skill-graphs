# Define edges
def route(state: State) -> Literal["b", END]:
    if len(state["aggregate"]) < 7:
        return "b"
    else:
        return END

builder.add_edge(START, "a")
builder.add_conditional_edges("a", route)
builder.add_edge("b", "a")
graph = builder.compile()
```

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from IPython.display import Image, display

display(Image(graph.get_graph().draw_mermaid_png()))
```

<img alt="Simple loop graph" />

This architecture is similar to a [ReAct agent](/oss/python/langgraph/workflows-agents) in which node `"a"` is a tool-calling model, and node `"b"` represents the tools.

In our `route` conditional edge, we specify that we should end after the `"aggregate"` list in the state passes a threshold length.

Invoking the graph, we see that we alternate between nodes `"a"` and `"b"` before terminating once we reach the termination condition.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
graph.invoke({"aggregate": []})
```

```
Node A sees []
Node B sees ['A']
Node A sees ['A', 'B']
Node B sees ['A', 'B', 'A']
Node A sees ['A', 'B', 'A', 'B']
Node B sees ['A', 'B', 'A', 'B', 'A']
Node A sees ['A', 'B', 'A', 'B', 'A', 'B']
```

### Impose a recursion limit

In some applications, we may not have a guarantee that we will reach a given termination condition. In these cases, we can set the graph's [recursion limit](/oss/python/langgraph/graph-api#recursion-limit). This will raise a `GraphRecursionError` after a given number of [supersteps](/oss/python/langgraph/graph-api#graphs). We can then catch and handle this exception:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langgraph.errors import GraphRecursionError

try:
    graph.invoke({"aggregate": []}, {"recursion_limit": 4})
except GraphRecursionError:
    print("Recursion Error")
```

```
Node A sees []
Node B sees ['A']
Node C sees ['A', 'B']
Node D sees ['A', 'B']
Node A sees ['A', 'B', 'C', 'D']
Recursion Error
```

<Accordion title="Extended example: return state on hitting recursion limit">
  Instead of raising `GraphRecursionError`, we can introduce a new key to the state that keeps track of the number of steps remaining until reaching the recursion limit. We can then use this key to determine if we should end the run.

  LangGraph implements a special `RemainingSteps` annotation. Under the hood, it creates a `ManagedValue` channel -- a state channel that will exist for the duration of our graph run and no longer.

  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import operator
  from typing import Annotated, Literal
  from typing_extensions import TypedDict
  from langgraph.graph import StateGraph, START, END
  from langgraph.managed.is_last_step import RemainingSteps

  class State(TypedDict):
      aggregate: Annotated[list, operator.add]
      remaining_steps: RemainingSteps

  def a(state: State):
      print(f'Node A sees {state["aggregate"]}')
      return {"aggregate": ["A"]}

  def b(state: State):
      print(f'Node B sees {state["aggregate"]}')
      return {"aggregate": ["B"]}

  # Define nodes
  builder = StateGraph(State)
  builder.add_node(a)
  builder.add_node(b)

  # Define edges
  def route(state: State) -> Literal["b", END]:
      if state["remaining_steps"] <= 2:
          return END
      else:
          return "b"

  builder.add_edge(START, "a")
  builder.add_conditional_edges("a", route)
  builder.add_edge("b", "a")
  graph = builder.compile()

  # Test it out
  result = graph.invoke({"aggregate": []}, {"recursion_limit": 4})
  print(result)
  ```

  ```
  Node A sees []
  Node B sees ['A']
  Node A sees ['A', 'B']
  {'aggregate': ['A', 'B', 'A']}
  ```
</Accordion>

<Accordion title="Extended example: loops with branches">
  To better understand how the recursion limit works, let's consider a more complex example. Below we implement a loop, but one step fans out into two nodes:

  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import operator
  from typing import Annotated, Literal
  from typing_extensions import TypedDict
  from langgraph.graph import StateGraph, START, END

  class State(TypedDict):
      aggregate: Annotated[list, operator.add]

  def a(state: State):
      print(f'Node A sees {state["aggregate"]}')
      return {"aggregate": ["A"]}

  def b(state: State):
      print(f'Node B sees {state["aggregate"]}')
      return {"aggregate": ["B"]}

  def c(state: State):
      print(f'Node C sees {state["aggregate"]}')
      return {"aggregate": ["C"]}

  def d(state: State):
      print(f'Node D sees {state["aggregate"]}')
      return {"aggregate": ["D"]}

  # Define nodes
  builder = StateGraph(State)
  builder.add_node(a)
  builder.add_node(b)
  builder.add_node(c)
  builder.add_node(d)

  # Define edges
  def route(state: State) -> Literal["b", END]:
      if len(state["aggregate"]) < 7:
          return "b"
      else:
          return END

  builder.add_edge(START, "a")
  builder.add_conditional_edges("a", route)
  builder.add_edge("b", "c")
  builder.add_edge("b", "d")
  builder.add_edge(["c", "d"], "a")
  graph = builder.compile()
  ```

  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from IPython.display import Image, display

  display(Image(graph.get_graph().draw_mermaid_png()))
  ```

  <img alt="Complex loop graph with branches" />

  This graph looks complex, but can be conceptualized as loop of [supersteps](/oss/python/langgraph/graph-api#graphs):

  1. Node A
  2. Node B
  3. Nodes C and D
  4. Node A
  5. ...

  We have a loop of four supersteps, where nodes C and D are executed concurrently.

  Invoking the graph as before, we see that we complete two full "laps" before hitting the termination condition:

  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  result = graph.invoke({"aggregate": []})
  ```

  ```
  Node A sees []
  Node B sees ['A']
  Node D sees ['A', 'B']
  Node C sees ['A', 'B']
  Node A sees ['A', 'B', 'C', 'D']
  Node B sees ['A', 'B', 'C', 'D', 'A']
  Node D sees ['A', 'B', 'C', 'D', 'A', 'B']
  Node C sees ['A', 'B', 'C', 'D', 'A', 'B']
  Node A sees ['A', 'B', 'C', 'D', 'A', 'B', 'C', 'D']
  ```

  However, if we set the recursion limit to four, we only complete one lap because each lap is four supersteps:

  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langgraph.errors import GraphRecursionError

  try:
      result = graph.invoke({"aggregate": []}, {"recursion_limit": 4})
  except GraphRecursionError:
      print("Recursion Error")
  ```

  ```
  Node A sees []
  Node B sees ['A']
  Node C sees ['A', 'B']
  Node D sees ['A', 'B']
  Node A sees ['A', 'B', 'C', 'D']
  Recursion Error
  ```
</Accordion>

## Async

Using the async programming paradigm can produce significant performance improvements when running [IO-bound](https://en.wikipedia.org/wiki/I/O_bound) code concurrently (e.g., making concurrent API requests to a chat model provider).

To convert a `sync` implementation of the graph to an `async` implementation, you will need to:

1. Update `nodes` use `async def` instead of `def`.
2. Update the code inside to use `await` appropriately.
3. Invoke the graph with `.ainvoke` or `.astream` as desired.

Because many LangChain objects implement the [Runnable Protocol](https://python.langchain.com/docs/expression_language/interface/) which has `async` variants of all the `sync` methods it's typically fairly quick to upgrade a `sync` graph to an `async` graph.

See example below. To demonstrate async invocations of underlying LLMs, we will include a chat model:

<Tabs>
  <Tab title="OpenAI">
    👉 Read the [OpenAI chat model integration docs](/oss/python/integrations/chat/openai/)

    ```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    pip install -U "langchain[openai]"
    ```

    <CodeGroup>
      ```python init_chat_model theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import os
      from langchain.chat_models import init_chat_model

      os.environ["OPENAI_API_KEY"] = "sk-..."

      model = init_chat_model("gpt-5.5")
      ```

      ```python Model Class theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import os
      from langchain_openai import ChatOpenAI

      os.environ["OPENAI_API_KEY"] = "sk-..."

      model = ChatOpenAI(model="gpt-5.5")
      ```
    </CodeGroup>
  </Tab>

  <Tab title="Anthropic">
    👉 Read the [Anthropic chat model integration docs](/oss/python/integrations/chat/anthropic/)

    ```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    pip install -U "langchain[anthropic]"
    ```

    <CodeGroup>
      ```python init_chat_model theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import os
      from langchain.chat_models import init_chat_model

      os.environ["ANTHROPIC_API_KEY"] = "sk-..."

      model = init_chat_model("claude-sonnet-4-6")
      ```

      ```python Model Class theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import os
      from langchain_anthropic import ChatAnthropic

      os.environ["ANTHROPIC_API_KEY"] = "sk-..."

      model = ChatAnthropic(model="claude-sonnet-4-6")
      ```
    </CodeGroup>
  </Tab>

  <Tab title="Azure">
    👉 Read the [Azure chat model integration docs](/oss/python/integrations/chat/azure_chat_openai/)

    ```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    pip install -U "langchain[openai]"
    ```

    <CodeGroup>
      ```python init_chat_model theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import os
      from langchain.chat_models import init_chat_model

      os.environ["AZURE_OPENAI_API_KEY"] = "..."
      os.environ["AZURE_OPENAI_ENDPOINT"] = "..."
      os.environ["OPENAI_API_VERSION"] = "2025-03-01-preview"

      model = init_chat_model(
          "azure_openai:gpt-5.5",
          azure_deployment=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"],
      )
      ```

      ```python Model Class theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import os
      from langchain_openai import AzureChatOpenAI

      os.environ["AZURE_OPENAI_API_KEY"] = "..."
      os.environ["AZURE_OPENAI_ENDPOINT"] = "..."
      os.environ["OPENAI_API_VERSION"] = "2025-03-01-preview"

      model = AzureChatOpenAI(
          model="gpt-5.5",
          azure_deployment=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"]
      )
      ```
    </CodeGroup>
  </Tab>

  <Tab title="Google Gemini">
    👉 Read the [Google GenAI chat model integration docs](/oss/python/integrations/chat/google_generative_ai/)

    ```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    pip install -U "langchain[google-genai]"
    ```

    <CodeGroup>
      ```python init_chat_model theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import os
      from langchain.chat_models import init_chat_model

      os.environ["GOOGLE_API_KEY"] = "..."

      model = init_chat_model("google_genai:gemini-2.5-flash-lite")
      ```

      ```python Model Class theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import os
      from langchain_google_genai import ChatGoogleGenerativeAI

      os.environ["GOOGLE_API_KEY"] = "..."

      model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
      ```
    </CodeGroup>
  </Tab>

  <Tab title="AWS Bedrock">
    👉 Read the [AWS Bedrock chat model integration docs](/oss/python/integrations/chat/bedrock/)

    ```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    pip install -U "langchain[aws]"
    ```

    <CodeGroup>
      ```python init_chat_model theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from langchain.chat_models import init_chat_model

      # Follow the steps here to configure your credentials:
      # https://docs.aws.amazon.com/bedrock/latest/userguide/getting-started.html

      model = init_chat_model(
          "anthropic.claude-3-5-sonnet-20240620-v1:0",
          model_provider="bedrock_converse",
      )
      ```

      ```python Model Class theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from langchain_aws import ChatBedrock

      model = ChatBedrock(model="anthropic.claude-3-5-sonnet-20240620-v1:0")
      ```
    </CodeGroup>
  </Tab>

  <Tab title="HuggingFace">
    👉 Read the [HuggingFace chat model integration docs](/oss/python/integrations/chat/huggingface/)

    ```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    pip install -U "langchain[huggingface]"
    ```

    <CodeGroup>
      ```python init_chat_model theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import os
      from langchain.chat_models import init_chat_model

      os.environ["HUGGINGFACEHUB_API_TOKEN"] = "hf_..."

      model = init_chat_model(
          "microsoft/Phi-3-mini-4k-instruct",
          model_provider="huggingface",
          temperature=0.7,
          max_tokens=1024,
      )
      ```

      ```python Model Class theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import os
      from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

      os.environ["HUGGINGFACEHUB_API_TOKEN"] = "hf_..."

      llm = HuggingFaceEndpoint(
          repo_id="microsoft/Phi-3-mini-4k-instruct",
          temperature=0.7,
          max_length=1024,
      )
      model = ChatHuggingFace(llm=llm)
      ```
    </CodeGroup>
  </Tab>

  <Tab title="OpenRouter">
    👉 Read the [OpenRouter chat model integration docs](/oss/python/integrations/chat/openrouter/)

    ```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    pip install -U "langchain-openrouter"
    ```

    <CodeGroup>
      ```python init_chat_model theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import os
      from langchain.chat_models import init_chat_model

      os.environ["OPENROUTER_API_KEY"] = "sk-..."

      model = init_chat_model(
          "auto",
          model_provider="openrouter",
      )
      ```

      ```python Model Class theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import os
      from langchain_openrouter import ChatOpenRouter

      os.environ["OPENROUTER_API_KEY"] = "sk-..."

      model = ChatOpenRouter(model="auto")
      ```
    </CodeGroup>
  </Tab>
</Tabs>

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain.chat_models import init_chat_model
from langgraph.graph import MessagesState, StateGraph

async def node(state: MessagesState):  # [!code highlight]
    new_message = await llm.ainvoke(state["messages"])  # [!code highlight]
    return {"messages": [new_message]}

builder = StateGraph(MessagesState).add_node(node).set_entry_point("node")
graph = builder.compile()

input_message = {"role": "user", "content": "Hello"}
result = await graph.ainvoke({"messages": [input_message]})  # [!code highlight]
```

<Tip>
  **Async streaming**
  See the [streaming guide](/oss/python/langgraph/streaming) for examples of streaming with async.
</Tip>

## Combine control flow and state updates with `Command`

It can be useful to combine control flow (edges) and state updates (nodes). For example, you might want to BOTH perform state updates AND decide which node to go to next in the SAME node. LangGraph provides a way to do so by returning a [Command](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.Command) object from node functions:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
def my_node(state: State) -> Command[Literal["my_other_node"]]:
    return Command(
        # state update
        update={"foo": "bar"},
        # control flow
        goto="my_other_node"
    )
```

We show an end-to-end example below. Let's create a simple graph with 3 nodes: A, B and C. We will first execute node A, and then decide whether to go to Node B or Node C next based on the output of node A.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import random
from typing_extensions import TypedDict, Literal
from langgraph.graph import StateGraph, START
from langgraph.types import Command

# Define graph state
class State(TypedDict):
    foo: str

# Define the nodes

def node_a(state: State) -> Command[Literal["node_b", "node_c"]]:
    print("Called A")
    value = random.choice(["b", "c"])
    # this is a replacement for a conditional edge function
    if value == "b":
        goto = "node_b"
    else:
        goto = "node_c"

    # note how Command allows you to BOTH update the graph state AND route to the next node
    return Command(
        # this is the state update
        update={"foo": value},
        # this is a replacement for an edge
        goto=goto,
    )

def node_b(state: State):
    print("Called B")
    return {"foo": state["foo"] + "b"}

def node_c(state: State):
    print("Called C")
    return {"foo": state["foo"] + "c"}
```

We can now create the [`StateGraph`](https://reference.langchain.com/python/langgraph/graph/state/StateGraph) with the above nodes. Notice that the graph doesn't have [conditional edges](/oss/python/langgraph/graph-api#conditional-edges) for routing! This is because control flow is defined with [`Command`](https://reference.langchain.com/python/langgraph/types/Command) inside `node_a`.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
builder = StateGraph(State)
builder.add_edge(START, "node_a")
builder.add_node(node_a)
builder.add_node(node_b)
builder.add_node(node_c)

# NOTE: there are no edges between nodes A, B and C!

graph = builder.compile()
```

<Warning>
  You might have noticed that we used [`Command`](https://reference.langchain.com/python/langgraph/types/Command) as a return type annotation, e.g. `Command[Literal["node_b", "node_c"]]`. This is necessary for the graph rendering and tells LangGraph that `node_a` can navigate to `node_b` and `node_c`.
</Warning>

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from IPython.display import display, Image

display(Image(graph.get_graph().draw_mermaid_png()))
```

<img alt="Command-based graph navigation" />

If we run the graph multiple times, we'd see it take different paths (A -> B or A -> C) based on the random choice in node A.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
graph.invoke({"foo": ""})
```

```
Called A
Called C
```

### Navigate to a node in a parent graph

If you are using [subgraphs](/oss/python/langgraph/use-subgraphs), you might want to navigate from a node within a subgraph to a different subgraph (i.e. a different node in the parent graph). To do so, you can specify `graph=Command.PARENT` in `Command`:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
def my_node(state: State) -> Command[Literal["my_other_node"]]:
    return Command(
        update={"foo": "bar"},
        goto="other_subgraph",  # where `other_subgraph` is a node in the parent graph
        graph=Command.PARENT
    )
```

Let's demonstrate this using the above example. We'll do so by changing `nodeA` in the above example into a single-node graph that we'll add as a subgraph to our parent graph.

<Warning>
  **State updates with `Command.PARENT`**
  When you send updates from a subgraph node to a parent graph node for a key that's shared by both parent and subgraph [state schemas](/oss/python/langgraph/graph-api#schema), you **must** define a [reducer](/oss/python/langgraph/graph-api#reducers) for the key you're updating in the parent graph state. See the example below.
</Warning>

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import operator
from typing_extensions import Annotated

class State(TypedDict):
    # NOTE: we define a reducer here
    foo: Annotated[str, operator.add]  # [!code highlight]

def node_a(state: State):
    print("Called A")
    value = random.choice(["a", "b"])
    # this is a replacement for a conditional edge function
    if value == "a":
        goto = "node_b"
    else:
        goto = "node_c"

    # note how Command allows you to BOTH update the graph state AND route to the next node
    return Command(
        update={"foo": value},
        goto=goto,
        # this tells LangGraph to navigate to node_b or node_c in the parent graph
        # NOTE: this will navigate to the closest parent graph relative to the subgraph
        graph=Command.PARENT,  # [!code highlight]
    )

subgraph = StateGraph(State).add_node(node_a).add_edge(START, "node_a").compile()

def node_b(state: State):
    print("Called B")
    # NOTE: since we've defined a reducer, we don't need to manually append
    # new characters to existing 'foo' value. instead, reducer will append these
    # automatically (via operator.add)
    return {"foo": "b"}  # [!code highlight]

def node_c(state: State):
    print("Called C")
    return {"foo": "c"}  # [!code highlight]

builder = StateGraph(State)
builder.add_edge(START, "subgraph")
builder.add_node("subgraph", subgraph)
builder.add_node(node_b)
builder.add_node(node_c)

graph = builder.compile()
```

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
graph.invoke({"foo": ""})
```

```
Called A
Called C
```

### Use inside tools

A common use case is updating graph state from inside a tool. For example, in a customer support application you might want to look up customer information based on their account number or ID in the beginning of the conversation. To update the graph state from the tool, you can return `Command(update={"my_custom_key": "foo", "messages": [...]})` from the tool:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain.tools import ToolRuntime

@tool
def lookup_user_info(runtime: ToolRuntime):
    """Use this to look up user information to better assist them with their questions."""
    user_info = get_user_info(runtime.server_info.user.identity)  # [!code highlight]
    return Command(
        update={
            # update the state keys
            "user_info": user_info,
            # update the message history
            "messages": [ToolMessage("Successfully looked up user information", tool_call_id=runtime.tool_call_id)]
        }
    )
```

<Warning>
  You MUST include `messages` (or any state key used for the message history) in `Command.update` when returning [`Command`](https://reference.langchain.com/python/langgraph/types/Command) from a tool and the list of messages in `messages` MUST contain a `ToolMessage`. This is necessary for the resulting message history to be valid (LLM providers require AI messages with tool calls to be followed by the tool result messages).
</Warning>

If you are using tools that update state via [`Command`](https://reference.langchain.com/python/langgraph/types/Command), we recommend using prebuilt [`ToolNode`](https://reference.langchain.com/python/langgraph/agents/#langgraph.prebuilt.tool_node.ToolNode) which automatically handles tools returning [`Command`](https://reference.langchain.com/python/langgraph/types/Command) objects and propagates them to the graph state. If you're writing a custom node that calls tools, you would need to manually propagate [`Command`](https://reference.langchain.com/python/langgraph/types/Command) objects returned by the tools as the update from the node.

## Visualize your graph

Here we demonstrate how to visualize the graphs you create.

You can visualize any arbitrary [Graph](https://langchain-ai.github.io/langgraph/reference/graphs/), including [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph).

Let's have some fun by drawing fractals :).

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import random
from typing import Annotated, Literal
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages

class State(TypedDict):
    messages: Annotated[list, add_messages]

class MyNode:
    def __init__(self, name: str):
        self.name = name
    def __call__(self, state: State):
        return {"messages": [("assistant", f"Called node {self.name}")]}

def route(state) -> Literal["entry_node", END]:
    if len(state["messages"]) > 10:
        return END
    return "entry_node"

def add_fractal_nodes(builder, current_node, level, max_level):
    if level > max_level:
        return
    # Number of nodes to create at this level
    num_nodes = random.randint(1, 3)  # Adjust randomness as needed
    for i in range(num_nodes):
        nm = ["A", "B", "C"][i]
        node_name = f"node_{current_node}_{nm}"
        builder.add_node(node_name, MyNode(node_name))
        builder.add_edge(current_node, node_name)
        # Recursively add more nodes
        r = random.random()
        if r > 0.2 and level + 1 < max_level:
            add_fractal_nodes(builder, node_name, level + 1, max_level)
        elif r > 0.05:
            builder.add_conditional_edges(node_name, route, node_name)
        else:
            # End
            builder.add_edge(node_name, END)

def build_fractal_graph(max_level: int):
    builder = StateGraph(State)
    entry_point = "entry_node"
    builder.add_node(entry_point, MyNode(entry_point))
    builder.add_edge(START, entry_point)
    add_fractal_nodes(builder, entry_point, 1, max_level)
    # Optional: set a finish point if required
    builder.add_edge(entry_point, END)  # or any specific node
    return builder.compile()

app = build_fractal_graph(3)
```

### Mermaid

We can also convert a graph class into Mermaid syntax.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
print(app.get_graph().draw_mermaid())
```

```
%%{init: {'flowchart': {'curve': 'linear'}}}%%
graph TD;
    tart__([<p>__start__</p>]):::first
    ry_node(entry_node)
    e_entry_node_A(node_entry_node_A)
    e_entry_node_B(node_entry_node_B)
    e_node_entry_node_B_A(node_node_entry_node_B_A)
    e_node_entry_node_B_B(node_node_entry_node_B_B)
    e_node_entry_node_B_C(node_node_entry_node_B_C)
    nd__([<p>__end__</p>]):::last
    tart__ --> entry_node;
    ry_node --> __end__;
    ry_node --> node_entry_node_A;
    ry_node --> node_entry_node_B;
    e_entry_node_B --> node_node_entry_node_B_A;
    e_entry_node_B --> node_node_entry_node_B_B;
    e_entry_node_B --> node_node_entry_node_B_C;
    e_entry_node_A -.-> entry_node;
    e_entry_node_A -.-> __end__;
    e_node_entry_node_B_A -.-> entry_node;
    e_node_entry_node_B_A -.-> __end__;
    e_node_entry_node_B_B -.-> entry_node;
    e_node_entry_node_B_B -.-> __end__;
    e_node_entry_node_B_C -.-> entry_node;
    e_node_entry_node_B_C -.-> __end__;
    ssDef default fill:#f2f0ff,line-height:1.2
    ssDef first fill-opacity:0
    ssDef last fill:#bfb6fc
```

### PNG

If preferred, we could render the Graph into a `.png`. Here we could use three options:

* Using Mermaid.ink API (does not require additional packages)
* Using Mermaid + Pyppeteer (requires `pip install pyppeteer`)
* Using graphviz (which requires `pip install graphviz`)

**Using Mermaid.Ink**

By default, `draw_mermaid_png()` uses Mermaid.Ink's API to generate the diagram.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from IPython.display import Image, display
from langchain_core.runnables.graph import CurveStyle, MermaidDrawMethod, NodeStyles

display(Image(app.get_graph().draw_mermaid_png()))
```

<img alt="Fractal graph visualization" />

**Using Mermaid + Pyppeteer**

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import nest_asyncio

nest_asyncio.apply()  # Required for Jupyter Notebook to run async functions

display(
    Image(
        app.get_graph().draw_mermaid_png(
            curve_style=CurveStyle.LINEAR,
            node_colors=NodeStyles(first="#ffdfba", last="#baffc9", default="#fad7de"),
            wrap_label_n_words=9,
            output_file_path=None,
            draw_method=MermaidDrawMethod.PYPPETEER,
            background_color="white",
            padding=10,
        )
    )
)
```

**Using Graphviz**

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
try:
    display(Image(app.get_graph().draw_png()))
except ImportError:
    print(
        "You likely need to install dependencies for pygraphviz, see more here https://github.com/pygraphviz/pygraphviz/blob/main/INSTALL.txt"
    )
```

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langgraph/use-graph-api.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Subgraphs
Source: https://docs.langchain.com/oss/python/langgraph/use-subgraphs

This guide explains the mechanics of using subgraphs. A subgraph is a [graph](/oss/python/langgraph/graph-api#graphs) that is used as a [node](/oss/python/langgraph/graph-api#nodes) in another graph.

Subgraphs are useful for:

* Building [multi-agent systems](/oss/python/langchain/multi-agent)
* Reusing a set of nodes in multiple graphs
* Distributing development: when you want different teams to work on different parts of the graph independently, you can define each part as a subgraph, and as long as the subgraph interface (the input and output schemas) is respected, the parent graph can be built without knowing any details of the subgraph

## Setup

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install -U langgraph
  ```

  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv add langgraph
  ```
</CodeGroup>

<Tip>
  **Set up LangSmith for LangGraph development**
  Sign up for [LangSmith](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=oss-langgraph-use-subgraphs) to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph—read more about [how to get started with LangSmith](https://docs.smith.langchain.com).
</Tip>

## Define subgraph communication

When adding subgraphs, you need to define how the parent graph and the subgraph communicate:

| Pattern                                                         | When to use                                                                                                        | State schemas                                                                                                  |
| --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------- |
| [Call a subgraph inside a node](#call-a-subgraph-inside-a-node) | Parent and subgraph have **different state schemas** (no shared keys), or you need to transform state between them | You write a wrapper function that maps parent state to subgraph input and subgraph output back to parent state |
| [Add a subgraph as a node](#add-a-subgraph-as-a-node)           | Parent and subgraph **share state keys**—the subgraph reads from and writes to the same channels as the parent     | You pass the compiled subgraph directly to `add_node`—no wrapper function needed                               |

<a />

### Call a subgraph inside a node

When the parent graph and subgraph have **different state schemas** (no shared keys), invoke the subgraph inside a node function. This is common when you want to keep a private message history for each agent in a [multi-agent](/oss/python/langchain/multi-agent) system.

The node function transforms the parent state to the subgraph state before invoking the subgraph, and transforms the results back to the parent state before returning.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from typing_extensions import TypedDict
from langgraph.graph.state import StateGraph, START

class SubgraphState(TypedDict):
    bar: str

# Subgraph

def subgraph_node_1(state: SubgraphState):
    return {"bar": "hi! " + state["bar"]}

subgraph_builder = StateGraph(SubgraphState)
subgraph_builder.add_node(subgraph_node_1)
subgraph_builder.add_edge(START, "subgraph_node_1")
subgraph = subgraph_builder.compile()

# Parent graph

class State(TypedDict):
    foo: str

def call_subgraph(state: State):
    # Transform the state to the subgraph state
    subgraph_output = subgraph.invoke({"bar": state["foo"]})  # [!code highlight]
    # Transform response back to the parent state
    return {"foo": subgraph_output["bar"]}

builder = StateGraph(State)
builder.add_node("node_1", call_subgraph)
builder.add_edge(START, "node_1")
graph = builder.compile()
```

<Accordion title="Full example: different state schemas">
  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from typing_extensions import TypedDict
  from langgraph.graph.state import StateGraph, START

  # Define subgraph
  class SubgraphState(TypedDict):
      # note that none of these keys are shared with the parent graph state
      bar: str
      baz: str

  def subgraph_node_1(state: SubgraphState):
      return {"baz": "baz"}

  def subgraph_node_2(state: SubgraphState):
      return {"bar": state["bar"] + state["baz"]}

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

  def node_2(state: ParentState):
      # Transform the state to the subgraph state
      response = subgraph.invoke({"bar": state["foo"]})
      # Transform response back to the parent state
      return {"foo": response["bar"]}

  builder = StateGraph(ParentState)
  builder.add_node("node_1", node_1)
  builder.add_node("node_2", node_2)
  builder.add_edge(START, "node_1")
  builder.add_edge("node_1", "node_2")
  graph = builder.compile()

  stream = graph.stream_events({"foo": "foo"}, version="v3")
  for event in stream:
      if event["method"] == "updates":
          print(event["params"]["namespace"], event["params"]["data"])
  ```

  ```
  [] {'node_1': {'foo': 'hi! foo'}}
  ['node_2:577b710b-64ae-31fb-9455-6a4d4cc2b0b9'] {'subgraph_node_1': {'baz': 'baz'}}
  ['node_2:577b710b-64ae-31fb-9455-6a4d4cc2b0b9'] {'subgraph_node_2': {'bar': 'hi! foobaz'}}
  [] {'node_2': {'foo': 'hi! foobaz'}}
  ```
</Accordion>

<Accordion title="Full example: different state schemas (two levels of subgraphs)">
  This is an example with two levels of subgraphs: parent -> child -> grandchild.

  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  # Grandchild graph
  from typing_extensions import TypedDict
  from langgraph.graph.state import StateGraph, START, END

  class GrandChildState(TypedDict):
      my_grandchild_key: str

  def grandchild_1(state: GrandChildState) -> GrandChildState:
      # NOTE: child or parent keys will not be accessible here
      return {"my_grandchild_key": state["my_grandchild_key"] + ", how are you"}

  grandchild = StateGraph(GrandChildState)
  grandchild.add_node("grandchild_1", grandchild_1)

  grandchild.add_edge(START, "grandchild_1")
  grandchild.add_edge("grandchild_1", END)

  grandchild_graph = grandchild.compile()

  # Child graph
  class ChildState(TypedDict):
      my_child_key: str

  def call_grandchild_graph(state: ChildState) -> ChildState:
      # NOTE: parent or grandchild keys won't be accessible here
      grandchild_graph_input = {"my_grandchild_key": state["my_child_key"]}
      grandchild_graph_output = grandchild_graph.invoke(grandchild_graph_input)
      return {"my_child_key": grandchild_graph_output["my_grandchild_key"] + " today?"}

  child = StateGraph(ChildState)
  # We're passing a function here instead of just compiled graph (`grandchild_graph`)
  child.add_node("child_1", call_grandchild_graph)
  child.add_edge(START, "child_1")
  child.add_edge("child_1", END)
  child_graph = child.compile()

  # Parent graph
  class ParentState(TypedDict):
      my_key: str

  def parent_1(state: ParentState) -> ParentState:
      # NOTE: child or grandchild keys won't be accessible here
      return {"my_key": "hi " + state["my_key"]}

  def parent_2(state: ParentState) -> ParentState:
      return {"my_key": state["my_key"] + " bye!"}

  def call_child_graph(state: ParentState) -> ParentState:
      child_graph_input = {"my_child_key": state["my_key"]}
      child_graph_output = child_graph.invoke(child_graph_input)
      return {"my_key": child_graph_output["my_child_key"]}

  parent = StateGraph(ParentState)
  parent.add_node("parent_1", parent_1)
  # We're passing a function here instead of just a compiled graph (`child_graph`)
  parent.add_node("child", call_child_graph)
  parent.add_node("parent_2", parent_2)

  parent.add_edge(START, "parent_1")
  parent.add_edge("parent_1", "child")
  parent.add_edge("child", "parent_2")
  parent.add_edge("parent_2", END)

  parent_graph = parent.compile()

  stream = parent_graph.stream_events({"my_key": "Bob"}, version="v3")
  for event in stream:
      if event["method"] == "updates":
          print(event["params"]["namespace"], event["params"]["data"])
  ```

  ```
  [] {'parent_1': {'my_key': 'hi Bob'}}
  ['child:2e26e9ce-602f-862c-aa66-1ea5a4655e3b', 'child_1:781bb3b1-3971-84ce-810b-acf819a03f9c'] {'grandchild_1': {'my_grandchild_key': 'hi Bob, how are you'}}
  ['child:2e26e9ce-602f-862c-aa66-1ea5a4655e3b'] {'child_1': {'my_child_key': 'hi Bob, how are you today?'}}
  [] {'child': {'my_key': 'hi Bob, how are you today?'}}
  [] {'parent_2': {'my_key': 'hi Bob, how are you today? bye!'}}
  ```
</Accordion>

<a />

### Add a subgraph as a node

When the parent graph and subgraph **share state keys**, you can pass a compiled subgraph directly to `add_node`. No wrapper function is needed—the subgraph reads from and writes to the parent's state channels automatically. For example, in [multi-agent](/oss/python/langchain/multi-agent) systems, the agents often communicate over a shared [messages](/oss/python/langgraph/graph-api#why-use-messages) key.

<img alt="SQL agent graph" />

If your subgraph shares state keys with the parent graph, you can follow these steps to add it to your graph:

1. Define the subgraph workflow (`subgraph_builder` in the example below) and compile it
2. Pass compiled subgraph to the [`add_node`](https://reference.langchain.com/python/langgraph/graph/state/StateGraph/add_node) method when defining the parent graph workflow

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from typing_extensions import TypedDict
from langgraph.graph.state import StateGraph, START

class State(TypedDict):
    foo: str

# Subgraph

def subgraph_node_1(state: State):
    return {"foo": "hi! " + state["foo"]}

subgraph_builder = StateGraph(State)
subgraph_builder.add_node(subgraph_node_1)
subgraph_builder.add_edge(START, "subgraph_node_1")
subgraph = subgraph_builder.compile()

# Parent graph

builder = StateGraph(State)
builder.add_node("node_1", subgraph)  # [!code highlight]
builder.add_edge(START, "node_1")
graph = builder.compile()
```

<Accordion title="Full example: shared state schemas">
  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from typing_extensions import TypedDict
  from langgraph.graph.state import StateGraph, START

  # Define subgraph
  class SubgraphState(TypedDict):
      foo: str  # shared with parent graph state
      bar: str  # private to SubgraphState

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

  stream = graph.stream_events({"foo": "foo"}, version="v3")
  for event in stream:
      if event["method"] == "updates" and not event["params"]["namespace"]:
          print(event["params"]["data"])
  ```

  ```
  {'node_1': {'foo': 'hi! foo'}}
  {'node_2': {'foo': 'hi! foobar'}}
  ```
</Accordion>

## Subgraph persistence

When you use a subgraph, you need to decide what happens to its internal data between calls. Consider a customer support bot that delegates to specialist subagents: should the "billing expert" subagent remember the customer's earlier questions, or start fresh each time it's called?

The `checkpointer` parameter on `.compile()` controls subgraph persistence:

| Mode                                      | `checkpointer=`  | Behavior                                                                                                                                                                                                 |
| ----------------------------------------- | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Per-invocation](#per-invocation-default) | `None` (default) | Each call starts fresh and inherits the parent's checkpointer to support [interrupts](/oss/python/langgraph/interrupts) and [durable execution](/oss/python/langgraph/persistence) within a single call. |
| [Per-thread](#per-thread)                 | `True`           | State accumulates across calls on the same thread. Each call picks up where the last one left off.                                                                                                       |
| [Stateless](#stateless)                   | `False`          | No checkpointing at all—runs like a plain function call. No interrupts or durable execution.                                                                                                             |

Per-invocation is the right choice for most applications, including [multi-agent](/oss/python/langchain/multi-agent) systems where subagents handle independent requests. Use per-thread when a subagent needs multi-turn conversation memory (for example, a research assistant that builds context over several exchanges).

<Note>
  The parent graph must be compiled with a checkpointer for subgraph persistence features (interrupts, state inspection, per-thread memory) to work. See [persistence](/oss/python/langgraph/persistence).
</Note>

<Info>
  The examples below use LangChain's [`create_agent`](https://reference.langchain.com/python/langchain/agents/factory/create_agent), which is a common way to build agents. `create_agent` produces a [LangGraph graph](/oss/python/langgraph/graph-api) under the hood, so all subgraph persistence concepts apply directly. If you're building with raw LangGraph `StateGraph`, the same patterns and configuration options apply—see the [Graph API](/oss/python/langgraph/graph-api) for details.
</Info>

### Stateful

Stateful subgraphs inherit the parent graph's checkpointer, which enables [interrupts](/oss/python/langgraph/interrupts), [persistence](/oss/python/langgraph/persistence), and state inspection. The two stateful modes differ in how long state is retained.

#### Per-invocation (default)

<Tip>
  This is the recommended mode for most applications, including [multi-agent](/oss/python/langchain/multi-agent) systems where subagents are invoked as tools. It supports [interrupts](/oss/python/langgraph/interrupts), [persistence](/oss/python/langgraph/persistence), and parallel calls while keeping each invocation isolated.
</Tip>

Use per-invocation persistence when each call to the subgraph is independent and the subagent doesn't need to remember anything from previous calls. This is the most common pattern, especially for [multi-agent](/oss/python/langchain/multi-agent) systems where subagents handle one-off requests like "look up this customer's order" or "summarize this document."

Omit `checkpointer` or set it to `None`. Each call starts fresh, but within a single call the subgraph inherits the parent's checkpointer and can use `interrupt()` to pause and resume.

The following examples use two subagents (fruit expert, veggie expert) wrapped as tools for an outer agent:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain.agents import create_agent
from langchain.tools import tool
from langgraph.checkpoint.memory import MemorySaver
from langgraph.types import Command, interrupt

@tool
def fruit_info(fruit_name: str) -> str:
    """Look up fruit info."""
    return f"Info about {fruit_name}"

@tool
def veggie_info(veggie_name: str) -> str:
    """Look up veggie info."""
    return f"Info about {veggie_name}"

# Subagents - no checkpointer setting (inherits parent)
fruit_agent = create_agent(
    model="gpt-5.4-mini",
    tools=[fruit_info],
    prompt="You are a fruit expert. Use the fruit_info tool. Respond in one sentence.",
)

veggie_agent = create_agent(
    model="gpt-5.4-mini",
    tools=[veggie_info],
    prompt="You are a veggie expert. Use the veggie_info tool. Respond in one sentence.",
)

# Wrap subagents as tools for the outer agent
@tool
def ask_fruit_expert(question: str) -> str:
    """Ask the fruit expert. Use for ALL fruit questions."""
    response = fruit_agent.invoke(
        {"messages": [{"role": "user", "content": question}]},
    )
    return response["messages"][-1].content

@tool
def ask_veggie_expert(question: str) -> str:
    """Ask the veggie expert. Use for ALL veggie questions."""
    response = veggie_agent.invoke(
        {"messages": [{"role": "user", "content": question}]},
    )
    return response["messages"][-1].content
