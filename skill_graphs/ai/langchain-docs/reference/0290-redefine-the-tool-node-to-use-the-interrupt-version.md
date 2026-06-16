# Redefine the tool node to use the interrupt version
run_query_node = ToolNode([run_query_tool_with_interrupt], name="run_query")  # [!code highlight]
```

<Note>
  The above implementation follows the [tool interrupt example](/oss/python/langgraph/interrupts#interrupts-in-tools) in the broader [human-in-the-loop](/oss/python/langgraph/interrupts) guide. Refer to that guide for details and alternatives.
</Note>

Let's now re-assemble our graph. We will replace the programmatic check with human review. Note that we now include a [checkpointer](/oss/python/langgraph/persistence); this is required to pause and resume the run.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langgraph.checkpoint.memory import InMemorySaver

def should_continue(state: MessagesState) -> Literal[END, "run_query"]:
    messages = state["messages"]
    last_message = messages[-1]
    if not last_message.tool_calls:
        return END
    else:
        return "run_query"

builder = StateGraph(MessagesState)
builder.add_node(list_tables)
builder.add_node(call_get_schema)
builder.add_node(get_schema_node, "get_schema")
builder.add_node(generate_query)
builder.add_node(run_query_node, "run_query")

builder.add_edge(START, "list_tables")
builder.add_edge("list_tables", "call_get_schema")
builder.add_edge("call_get_schema", "get_schema")
builder.add_edge("get_schema", "generate_query")
builder.add_conditional_edges(
    "generate_query",
    should_continue,
)
builder.add_edge("run_query", "generate_query")

checkpointer = InMemorySaver()  # [!code highlight]
agent = builder.compile(checkpointer=checkpointer)  # [!code highlight]
```

We can invoke the graph as before. This time, execution is interrupted:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
question = "Which genre on average has the longest tracks?"

for step in agent.stream(
    {"messages": [{"role": "user", "content": question}]},
    config,
    stream_mode="values",
):
    if "__interrupt__" in step:
        action = step["__interrupt__"][0]
        print("INTERRUPTED:")
        for request in action.value:
            print(json.dumps(request, indent=2))
    elif "messages" in step:
        step["messages"][-1].pretty_print()
    else:
        raise ValueError(f"Unsupported stream step type: {type(step)}")
```

```
...

INTERRUPTED:
{
  "action": "sql_db_query",
  "args": {
    "query": "SELECT Genre.Name, AVG(Track.Milliseconds) AS AvgLength FROM Track JOIN Genre ON Track.GenreId = Genre.GenreId GROUP BY Genre.Name ORDER BY AvgLength DESC LIMIT 5;"
  },
  "description": "Please review the tool call"
}
```

We can accept or edit the tool call using [Command](/oss/python/langgraph/use-graph-api#combine-control-flow-and-state-updates-with-command):

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langgraph.types import Command

for step in agent.stream(
    Command(resume={"type": "accept"}),
    # Command(resume={"type": "edit", "args": {"query": "..."}}),
    config,
    stream_mode="values",
):
    if "__interrupt__" in step:
        action = step["__interrupt__"][0]
        print("INTERRUPTED:")
        for request in action.value:
            print(json.dumps(request, indent=2))
    elif "messages" in step:
        step["messages"][-1].pretty_print()
    else:
        raise ValueError(f"Unsupported stream step type: {type(step)}")
```

```
================================== Ai Message ==================================
Tool Calls:
  sql_db_query (call_t4yXkD6shwdTPuelXEmY3sAY)
 Call ID: call_t4yXkD6shwdTPuelXEmY3sAY
  Args:
    query: SELECT Genre.Name, AVG(Track.Milliseconds) AS AvgLength FROM Track JOIN Genre ON Track.GenreId = Genre.GenreId GROUP BY Genre.Name ORDER BY AvgLength DESC LIMIT 5;
================================= Tool Message =================================
Name: sql_db_query

[('Sci Fi & Fantasy', 2911783.0384615385), ('Science Fiction', 2625549.076923077), ('Drama', 2575283.78125), ('TV Shows', 2145041.0215053763), ('Comedy', 1585263.705882353)]
================================== Ai Message ==================================

The genre with the longest average track length is "Sci Fi & Fantasy" with an average length of about 2,911,783 milliseconds. Other genres with long average track lengths include "Science Fiction," "Drama," "TV Shows," and "Comedy."
```

Refer to the [human-in-the-loop guide](/oss/python/langgraph/interrupts) for details.

## Next steps

Check out the [Evaluate a graph](/langsmith/evaluate-graph) guide for evaluating LangGraph applications, including SQL agents like this one, using LangSmith.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langgraph/sql-agent.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Stores
Source: https://docs.langchain.com/oss/python/langgraph/stores

LangGraph stores provide cross-thread long-term memory, complementing per-thread checkpointer persistence.

Stores let agents persist information across threads, including user preferences, accumulated knowledge, and facts that should survive beyond a single conversation. Unlike [checkpointers](/oss/python/langgraph/checkpointers), which save the full graph state scoped to one thread, stores hold arbitrary key-value data accessible from any thread.

<img alt="Model of shared state" />

<Info>
  **Agent Server handles stores automatically**
  When using the [Agent Server](/langsmith/agent-server), you do not need to implement or configure stores manually. The API handles all storage infrastructure for you behind the scenes.
</Info>

<Note>
  [InMemoryStore](https://reference.langchain.com/python/langchain-core/stores/InMemoryStore) is suitable for development and testing. For production, use a persistent store like `PostgresStore`, `MongoDBStore`, or `RedisStore`. All implementations extend [BaseStore](https://reference.langchain.com/python/langchain-core/stores/BaseStore), which is the type annotation to use in node function signatures.
</Note>

## Basic usage

The following code snippet shows the [InMemoryStore](https://reference.langchain.com/python/langchain-core/stores/InMemoryStore) in isolation without using LangGraph:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langgraph.store.memory import InMemoryStore
store = InMemoryStore()
```

Memories are namespaced by a `tuple`, which is `(<user_id>, "memories")` in the following example. The namespace can be any length and represent anything, does not have to be user specific.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
user_id = "1"
namespace_for_memory = (user_id, "memories")
```

Use the `store.put` method to save memories to the namespace in the store. Specify the namespace, as defined above, and a key-value pair for the memory: the key is simply a unique identifier for the memory (`memory_id`) and the value (a dictionary) is the memory itself.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
memory_id = str(uuid.uuid4())
memory = {"food_preference" : "I like pizza"}
store.put(namespace_for_memory, memory_id, memory)
```

Read out memories from your namespace using the `store.search` method, which returns memories for a given user as a list, up to the `limit` argument (default `10`). With `InMemoryStore`, items are returned in insertion order, so the most recent memory is last in the list; other backends may order memories differently (see [Listing items in a namespace](#listing-items-in-a-namespace)).

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
memories = store.search(namespace_for_memory)
memories[-1].dict()
{'value': {'food_preference': 'I like pizza'},
 'key': '07e0caf4-1631-47b7-b15f-65515d4c1843',
 'namespace': ['1', 'memories'],
 'created_at': '2024-10-02T17:22:31.590602+00:00',
 'updated_at': '2024-10-02T17:22:31.590605+00:00'}
```

Each memory type is a Python class ([`Item`](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.Item)) with certain attributes. We can access it as a dictionary by converting with `.dict`.

The attributes it has are:

* `value`: The value (itself a dictionary) of this memory

* `key`: A unique key for this memory in this namespace

* `namespace`: A tuple of strings, the namespace of this memory type

  <Note>
    While the type is `tuple[str, ...]`, it may be serialized as a list when converted to JSON (for example, `['1', 'memories']`).
  </Note>

* `created_at`: Timestamp for when this memory was created

* `updated_at`: Timestamp for when this memory was updated

## Listing items in a namespace

Calling [`store.search`](https://reference.langchain.com/python/langgraph/store/#langgraph.store.base.BaseStore.search) (or the async [`store.asearch`](https://reference.langchain.com/python/langgraph/store/#langgraph.store.base.BaseStore.asearch)) with no `query` and no `filter` returns the items stored under `namespace_prefix`, up to `limit`. Use this to enumerate everything in a namespace when you don't need semantic ranking.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# Return up to 100 items stored under ("alice", "memories").
items = store.search(("alice", "memories"), limit=100)
```

Three behaviors to keep in mind:

* **`namespace_prefix` matches by prefix, not exactly.** `("alice",)` also returns items under `("alice", "memories")`, `("alice", "preferences")`, and so on. To restrict to a single level, pass the full namespace or filter the returned items client-side on `item.namespace`.
* **Results past `limit` are silently truncated.** There is no overflow signal—set `limit` above your expected maximum, or paginate with `offset`.
* **Default ordering depends on the store backend.** `PostgresStore` and `AsyncPostgresStore` return results ordered by `updated_at` descending (most recently updated first). `InMemoryStore` returns results in insertion order (most recently inserted last). Do not rely on a specific order across implementations; sort client-side on `item.updated_at` if order matters.

To page through a large namespace:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
page_size = 50
offset = 0
while True:
    page = store.search(("alice", "memories"), limit=page_size, offset=offset)
    if not page:
        break
    for item in page:
        pass
    offset += page_size
```

To discover which namespaces exist (for example, to iterate over every user before listing their memories), use [`store.list_namespaces`](https://reference.langchain.com/python/langgraph/store/#langgraph.store.base.BaseStore.list_namespaces) or [`store.alist_namespaces`](https://reference.langchain.com/python/langgraph/store/#langgraph.store.base.BaseStore.alist_namespaces):

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# All namespaces that start with ("alice",), truncated to two levels deep.
namespaces = store.list_namespaces(prefix=("alice",), max_depth=2)
```

## Semantic search

Beyond simple retrieval, the store also supports semantic search, allowing you to find memories based on meaning rather than exact matches. To enable this, configure the store with an embedding model:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain.embeddings import init_embeddings

store = InMemoryStore(
    index={
        "embed": init_embeddings("openai:text-embedding-3-small"),  # Embedding provider
        "dims": 1536,                              # Embedding dimensions
        "fields": ["food_preference", "$"]              # Fields to embed
    }
)
```

Now when searching, you can use natural language queries to find relevant memories:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# Find memories about food preferences

# (This can be done after putting memories into the store)
memories = store.search(
    namespace_for_memory,
    query="What does the user like to eat?",
    limit=3  # Return top 3 matches
)
```

You can control which parts of your memories get embedded by configuring the `fields` parameter or by specifying the `index` parameter when storing memories:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# Store with specific fields to embed
store.put(
    namespace_for_memory,
    str(uuid.uuid4()),
    {
        "food_preference": "I love Italian cuisine",
        "context": "Discussing dinner plans"
    },
    index=["food_preference"]  # Only embed "food_preferences" field
)

# Store without embedding (still retrievable, but not searchable)
store.put(
    namespace_for_memory,
    str(uuid.uuid4()),
    {"system_info": "Last updated: 2024-01-01"},
    index=False
)
```

## Using in LangGraph

The store works hand-in-hand with the checkpointer: the checkpointer saves state to threads, as discussed above, and the store allows you to store arbitrary information for access *across* threads. Compile the graph with both the checkpointer and the store as follows.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from dataclasses import dataclass
from langgraph.checkpoint.memory import InMemorySaver

@dataclass
class Context:
    user_id: str

# We need this because we want to enable threads (conversations)
checkpointer = InMemorySaver()

# ... Define the graph ...

# Compile the graph with the checkpointer and store
builder = StateGraph(MessagesState, context_schema=Context)

# ... add nodes and edges ...
graph = builder.compile(checkpointer=checkpointer, store=store)
```

Then invoke the graph with a `thread_id`, as before, and also with a `user_id`, which serves as the namespace for memories for this particular user as before.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# Invoke the graph
config = {"configurable": {"thread_id": "1"}}

# First let's just say hi to the AI
for update in graph.stream(
    {"messages": [{"role": "user", "content": "hi"}]},
    config,
    stream_mode="updates",
    context=Context(user_id="1"),
):
    print(update)
```

You can access the store and the `user_id` from *any node* by using the `Runtime` object. The `Runtime` is automatically injected by LangGraph when you add it as a parameter to your node function. You can use it to save memories:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langgraph.runtime import Runtime
from dataclasses import dataclass

@dataclass
class Context:
    user_id: str

async def update_memory(state: MessagesState, runtime: Runtime[Context]):

    # Get the user id from the runtime context
    user_id = runtime.context.user_id

    # Namespace the memory
    namespace = (user_id, "memories")

    # ... Analyze conversation and create a new memory

    # Create a new memory ID
    memory_id = str(uuid.uuid4())

    # We create a new memory
    await runtime.store.aput(namespace, memory_id, {"memory": memory})

```

You can also access the store from any node and use the `store.search` method to get memories. Memories are returned as a list of objects that can be converted to a dictionary.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
memories[-1].dict()
{'value': {'food_preference': 'I like pizza'},
 'key': '07e0caf4-1631-47b7-b15f-65515d4c1843',
 'namespace': ['1', 'memories'],
 'created_at': '2024-10-02T17:22:31.590602+00:00',
 'updated_at': '2024-10-02T17:22:31.590605+00:00'}
```

You access the memories and use them in model calls.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from dataclasses import dataclass
from langgraph.runtime import Runtime

@dataclass
class Context:
    user_id: str

async def call_model(state: MessagesState, runtime: Runtime[Context]):
    # Get the user id from the runtime context
    user_id = runtime.context.user_id

    # Namespace the memory
    namespace = (user_id, "memories")

    # Search based on the most recent message
    memories = await runtime.store.asearch(
        namespace,
        query=state["messages"][-1].content,
        limit=3
    )
    info = "\n".join([d.value["memory"] for d in memories])

    # ... Use memories in the model call
```

If you create a new thread, you can still access the same memories so long as the `user_id` is the same.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# Invoke the graph on a new thread
config = {"configurable": {"thread_id": "2"}}

# Let's say hi again
for update in graph.stream(
    {"messages": [{"role": "user", "content": "hi, tell me about my memories"}]},
    config,
    stream_mode="updates",
    context=Context(user_id="1"),
):
    print(update)
```

When you use LangSmith locally (e.g., in [Studio](/langsmith/studio)) or [hosted](/langsmith/platform-setup), the base store is available to use by default and you do not need to specify it during graph compilation. To enable semantic search, however, you **do** need to configure the indexing settings in your `langgraph.json` file. For example:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
    ...
    "store": {
        "index": {
            "embed": "openai:text-embeddings-3-small",
            "dims": 1536,
            "fields": ["$"]
        }
    }
}
```

See the [deployment guide](/langsmith/semantic-search) for more details and configuration options.

## Build a custom store

To use a storage backend other than the built-in implementations, subclass [BaseStore](https://reference.langchain.com/python/langchain-core/stores/BaseStore) and implement its required methods. The built-in [InMemoryStore](https://reference.langchain.com/python/langchain-core/stores/InMemoryStore) is the simplest reference implementation.

### Base contract

All five async methods are required. Sync counterparts (`put`, `get`, `delete`, `search`, `list_namespaces`) are optional but recommended for compatibility with sync graph execution.

| Method                                                                               | Description                                                         |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------- |
| `aput(namespace, key, value, index=None)`                                            | Store or overwrite a single item                                    |
| `aget(namespace, key)`                                                               | Retrieve a single item by key; return `None` if missing             |
| `adelete(namespace, key)`                                                            | Delete a single item                                                |
| `asearch(namespace_prefix, *, query=None, filter=None, limit=10, offset=0)`          | Search items under a namespace prefix; optionally by semantic query |
| `alist_namespaces(*, prefix=None, suffix=None, max_depth=None, limit=100, offset=0)` | List namespaces matching a prefix/suffix pattern                    |

Look up exact signatures before implementing:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import inspect
from langgraph.store.base import BaseStore
print(inspect.getsource(BaseStore))
```

### Namespace design

Namespaces are tuples of strings, e.g. `("user_id", "memories")`. Store implementations must support:

* **Prefix matching**: `asearch(("alice",))` returns items under `("alice",)`, `("alice", "memories")`, and any other sub-namespace.
* **Exact key lookup**: `aget(("alice", "memories"), "some-key")` must be O(1) or close to it.

For SQL backends, a common schema:

```sql theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
CREATE TABLE store_items (
    namespace   TEXT[] NOT NULL,
    key         TEXT NOT NULL,
    value       JSONB NOT NULL,
    created_at  TIMESTAMPTZ DEFAULT now(),
    updated_at  TIMESTAMPTZ DEFAULT now(),
    PRIMARY KEY (namespace, key)
);

CREATE INDEX ON store_items USING gin(namespace);
```

### Serialization

Store values are plain Python dicts — no special serializer is required. Serialize with `json.dumps` / `json.loads` or a JSONB column directly. Do not store raw Python objects that are not JSON-serializable.

### Semantic search support

If your backend supports vector search, implement the `query` parameter on `asearch`:

* Accept a `query: str | None` argument.
* When `query` is not `None`, embed it and rank results by cosine similarity.
* Results should include a `score` field on each `Item` when `query` is provided.

If your backend does not support vector search, raise `NotImplementedError` when `query` is passed.

### Testing

There is currently no conformance suite for custom stores. Test against [InMemoryStore](https://reference.langchain.com/python/langchain-core/stores/InMemoryStore) as the reference:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import pytest
from langgraph.store.memory import InMemoryStore
from your_module import YourStore

@pytest.fixture
async def store():
    async with YourStore.create() as s:
        yield s

@pytest.fixture
def reference():
    return InMemoryStore()

async def test_put_and_get(store, reference):
    ns = ("test", "ns")
    for s in [store, reference]:
        await s.aput(ns, "k1", {"val": 1})
        item = await s.aget(ns, "k1")
        assert item is not None
        assert item.value == {"val": 1}

async def test_delete(store, reference):
    ns = ("test", "ns")
    for s in [store, reference]:
        await s.aput(ns, "k1", {"val": 1})
        await s.adelete(ns, "k1")
        assert await s.aget(ns, "k1") is None

async def test_search_prefix(store, reference):
    for s in [store, reference]:
        await s.aput(("user", "memories"), "m1", {"text": "likes pizza"})
        results = await s.asearch(("user",))
        assert any(r.key == "m1" for r in results)
```

### Next steps

* [Add a custom store to Agent Server](/langsmith/custom-store) — deploying your implementation
* [Checkpointers](/oss/python/langgraph/checkpointers) — thread-scoped state persistence

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langgraph/stores.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Streaming
Source: https://docs.langchain.com/oss/python/langgraph/streaming

<Tip>
  For new applications, we recommend [event streaming](/oss/python/langgraph/event-streaming)—the typed-projection API introduced in LangGraph v1.2. Event streaming gives you separate iterators per projection (messages, values, subgraphs, output) so you can consume them independently instead of branching on `stream_mode` chunks.
</Tip>

This page covers LangGraph's stream-mode API. It exposes graph execution through stream modes such as `updates`, `values`, `messages`, `custom`, `checkpoints`, `tasks`, and `debug`. Use it when you need direct access to graph-runtime events or specific stream-mode output.

## Get started

### Basic usage

LangGraph graphs expose the [`stream`](https://reference.langchain.com/python/langgraph/pregel/#langgraph.pregel.Pregel.stream) (sync) and [`astream`](https://reference.langchain.com/python/langgraph/pregel/#langgraph.pregel.Pregel.astream) (async) methods to yield streamed outputs as iterators. Pass one or more [stream modes](#stream-modes) to control what data you receive.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
for chunk in graph.stream(
    {"topic": "ice cream"},
    stream_mode=["updates", "custom"],  # [!code highlight]
    version="v2",  # [!code highlight]
):
    if chunk["type"] == "updates":
        for node_name, state in chunk["data"].items():
            print(f"Node {node_name} updated: {state}")
    elif chunk["type"] == "custom":
        print(f"Status: {chunk['data']['status']}")
```

```shell title="Output" theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
Status: thinking of a joke...
Node generate_joke updated: {'joke': 'Why did the ice cream go to school? To get a sundae education!'}
```

<Accordion title="Full example">
  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from typing import TypedDict
  from langgraph.graph import StateGraph, START, END
  from langgraph.config import get_stream_writer

  class State(TypedDict):
      topic: str
      joke: str

  def generate_joke(state: State):
      writer = get_stream_writer()
      writer({"status": "thinking of a joke..."})
      return {"joke": f"Why did the {state['topic']} go to school? To get a sundae education!"}

  graph = (
      StateGraph(State)
      .add_node(generate_joke)
      .add_edge(START, "generate_joke")
      .add_edge("generate_joke", END)
      .compile()
  )

  for chunk in graph.stream(
      {"topic": "ice cream"},
      stream_mode=["updates", "custom"],
      version="v2",
  ):
      if chunk["type"] == "updates":
          for node_name, state in chunk["data"].items():
              print(f"Node {node_name} updated: {state}")
      elif chunk["type"] == "custom":
          print(f"Status: {chunk['data']['status']}")
  ```

  ```shell title="Output" theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  Status: thinking of a joke...
  Node generate_joke updated: {'joke': 'Why did the ice cream go to school? To get a sundae education!'}
  ```
</Accordion>

<Tip>
  Debug streaming events, inspect token-by-token LLM output, and monitor latency with [LangSmith](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=oss-langgraph-streaming). Follow the [tracing quickstart](/langsmith/trace-with-langgraph) to get set up.
</Tip>

### Stream output format (v2)

<Note>
  Requires LangGraph >= 1.1. All examples on this page use `version="v2"`.
</Note>

Pass `version="v2"` to `stream()` or `astream()` to get a unified output format. Every chunk is a `StreamPart` dict with a consistent shape — regardless of stream mode, number of modes, or subgraph settings:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
    "type": "values" | "updates" | "messages" | "custom" | "checkpoints" | "tasks" | "debug",
    "ns": (),           # namespace tuple, populated for subgraph events
    "data": ...,        # the actual payload (type varies by stream mode)
}
```

Each stream mode has a corresponding `TypedDict` containing [`ValuesStreamPart`](https://reference.langchain.com/python/langgraph/types/ValuesStreamPart), [`UpdatesStreamPart`](https://reference.langchain.com/python/langgraph/types/UpdatesStreamPart), [`MessagesStreamPart`](https://reference.langchain.com/python/langgraph/types/MessagesStreamPart), [`CustomStreamPart`](https://reference.langchain.com/python/langgraph/types/CustomStreamPart), [`CheckpointStreamPart`](https://reference.langchain.com/python/langgraph/types/CheckpointStreamPart), [`TasksStreamPart`](https://reference.langchain.com/python/langgraph/types/TasksStreamPart), [`DebugStreamPart`](https://reference.langchain.com/python/langgraph/types/DebugStreamPart). You can import these types from `langgraph.types`. The union type [`StreamPart`](https://reference.langchain.com/python/langgraph/types/StreamPart) is a disjoing union on `part["type"]`, enabling full type narrowing in editors and type checkers.

With v1 (default), the output format changes based on your streaming options (single mode returns raw data, multiple modes return `(mode, data)` tuples, subgraphs return `(namespace, data)` tuples). With v2, the format is always the same:

<CodeGroup>
  ```python v2 (new) theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  for chunk in graph.stream(inputs, stream_mode="updates", version="v2"):
      print(chunk["type"])  # "updates"
      print(chunk["ns"])    # ()
      print(chunk["data"])  # {"node_name": {"key": "value"}}
  ```

  ```python v1 (current default) theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  for chunk in graph.stream(inputs, stream_mode="updates"):
      print(chunk)  # {"node_name": {"key": "value"}}
  ```
</CodeGroup>

The v2 format also enables type narrowing, which means you can filter chunks by `chunk["type"]` and get the correct payload type. Each branch narrows `part["data"]` to the specific type for that mode:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
for part in graph.stream(
    {"topic": "ice cream"},
    stream_mode=["values", "updates", "messages", "custom"],
    version="v2",
):
    if part["type"] == "values":
        # ValuesStreamPart — full state snapshot after each step
        print(f"State: topic={part['data']['topic']}")
    elif part["type"] == "updates":
        # UpdatesStreamPart — only the changed keys from each node
        for node_name, state in part["data"].items():
            print(f"Node `{node_name}` updated: {state}")
    elif part["type"] == "messages":
        # MessagesStreamPart — (message_chunk, metadata) from LLM calls
        msg, metadata = part["data"]
        print(msg.content, end="", flush=True)
    elif part["type"] == "custom":
        # CustomStreamPart — arbitrary data from get_stream_writer()
        print(f"Progress: {part['data']['progress']}%")
```

## Stream modes

Pass one or more of the following stream modes as a list to the [`stream`](https://reference.langchain.com/python/langgraph/graphs/#langgraph.graph.state.CompiledStateGraph.stream) or [`astream`](https://reference.langchain.com/python/langgraph/graphs/#langgraph.graph.state.CompiledStateGraph.astream) methods:

| Mode                        | Type                                                                                                  | Description                                                                                                                          |
| :-------------------------- | :---------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------- |
| [values](#graph-state)      | [`ValuesStreamPart`](https://reference.langchain.com/python/langgraph/types/ValuesStreamPart)         | Full state after each step.                                                                                                          |
| [updates](#graph-state)     | [`UpdatesStreamPart`](https://reference.langchain.com/python/langgraph/types/UpdatesStreamPart)       | State updates after each step. Multiple updates in the same step are streamed separately.                                            |
| [messages](#llm-tokens)     | [`MessagesStreamPart`](https://reference.langchain.com/python/langgraph/types/MessagesStreamPart)     | 2-tuples of (LLM token, metadata) from LLM calls.                                                                                    |
| [custom](#custom-data)      | [`CustomStreamPart`](https://reference.langchain.com/python/langgraph/types/CustomStreamPart)         | Custom data emitted from nodes via [`get_stream_writer`](https://reference.langchain.com/python/langgraph/config/get_stream_writer). |
| [checkpoints](#checkpoints) | [`CheckpointStreamPart`](https://reference.langchain.com/python/langgraph/types/CheckpointStreamPart) | Checkpoint events (same format as `get_state()`). Requires a checkpointer.                                                           |
| [tasks](#tasks)             | [`TasksStreamPart`](https://reference.langchain.com/python/langgraph/types/TasksStreamPart)           | Task start/finish events with results and errors. Requires a checkpointer.                                                           |
| [debug](#debug)             | [`DebugStreamPart`](https://reference.langchain.com/python/langgraph/types/DebugStreamPart)           | All available info — combines `checkpoints` and `tasks` with extra metadata.                                                         |

<a />

### Graph state

Use the stream modes `updates` and `values` to stream the state of the graph as it executes.

* `updates` streams the **updates** to the state after each step of the graph.
* `values` streams the **full value** of the state after each step of the graph.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class State(TypedDict):
  topic: str
  joke: str

def refine_topic(state: State):
    return {"topic": state["topic"] + " and cats"}

def generate_joke(state: State):
    return {"joke": f"This is a joke about {state['topic']}"}

graph = (
  StateGraph(State)
  .add_node(refine_topic)
  .add_node(generate_joke)
  .add_edge(START, "refine_topic")
  .add_edge("refine_topic", "generate_joke")
  .add_edge("generate_joke", END)
  .compile()
)
```

<Tabs>
  <Tab title="updates">
    Use this to stream only the **state updates** returned by the nodes after each step. The streamed outputs include the name of the node as well as the update.

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    for chunk in graph.stream(
        {"topic": "ice cream"},
        stream_mode="updates",  # [!code highlight]
        version="v2",  # [!code highlight]
    ):
        if chunk["type"] == "updates":
            for node_name, state in chunk["data"].items():
                print(f"Node `{node_name}` updated: {state}")
    ```

    ```shell title="Output" theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    Node `refine_topic` updated: {'topic': 'ice cream and cats'}
    Node `generate_joke` updated: {'joke': 'This is a joke about ice cream and cats'}
    ```
  </Tab>

  <Tab title="values">
    Use this to stream the **full state** of the graph after each step.

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    for chunk in graph.stream(
        {"topic": "ice cream"},
        stream_mode="values",  # [!code highlight]
        version="v2",  # [!code highlight]
    ):
        if chunk["type"] == "values":
            print(f"topic: {chunk['data']['topic']}, joke: {chunk['data']['joke']}")
    ```

    ```shell title="Output" theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    topic: ice cream, joke:
    topic: ice cream and cats, joke:
    topic: ice cream and cats, joke: This is a joke about ice cream and cats
    ```
  </Tab>
</Tabs>

### LLM tokens

Use the `messages` streaming mode to stream Large Language Model (LLM) outputs **token by token** from any part of your graph, including nodes, tools, subgraphs, or tasks.

The streamed output from [`messages` mode](#stream-modes) is a tuple `(message_chunk, metadata)` where:

* `message_chunk`: the token or message segment from the LLM.
* `metadata`: a dictionary containing details about the graph node and LLM invocation.

> If your LLM is not available as a LangChain integration, you can stream its outputs using `custom` mode instead. See [use with any LLM](#use-with-any-llm) for details.

<Warning>
  **Manual config required for async in Python \< 3.11**
  When using Python \< 3.11 with async code, you must explicitly pass [`RunnableConfig`](https://reference.langchain.com/python/langchain-core/runnables/config/RunnableConfig) to `ainvoke()` to enable proper streaming. See [Async with Python \< 3.11](#async) for details or upgrade to Python 3.11+.
</Warning>

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from dataclasses import dataclass

from langchain.chat_models import init_chat_model
from langgraph.graph import StateGraph, START

@dataclass
class MyState:
    topic: str
    joke: str = ""

model = init_chat_model(model="gpt-5.4-mini")

def call_model(state: MyState):
    """Call the LLM to generate a joke about a topic"""
    # Note that message events are emitted even when the LLM is run using .invoke rather than .stream
    model_response = model.invoke(  # [!code highlight]
        [
            {"role": "user", "content": f"Generate a joke about {state.topic}"}
        ]
    )
    return {"joke": model_response.content}

graph = (
    StateGraph(MyState)
    .add_node(call_model)
    .add_edge(START, "call_model")
    .compile()
)

# The "messages" stream mode streams LLM tokens with metadata

# Use version="v2" for a unified StreamPart format
for chunk in graph.stream(
    {"topic": "ice cream"},
    stream_mode="messages",  # [!code highlight]
    version="v2",  # [!code highlight]
):
    if chunk["type"] == "messages":
        message_chunk, metadata = chunk["data"]
        if message_chunk.content:
            print(message_chunk.content, end="|", flush=True)
```

#### Filter by LLM invocation

You can associate `tags` with LLM invocations to filter the streamed tokens by LLM invocation.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain.chat_models import init_chat_model

# model_1 is tagged with "joke"
model_1 = init_chat_model(model="gpt-5.4-mini", tags=['joke'])

# model_2 is tagged with "poem"
model_2 = init_chat_model(model="gpt-5.4-mini", tags=['poem'])

graph = ... # define a graph that uses these LLMs

# The stream_mode is set to "messages" to stream LLM tokens

# The metadata contains information about the LLM invocation, including the tags
async for chunk in graph.astream(
    {"topic": "cats"},
    stream_mode="messages",  # [!code highlight]
    version="v2",  # [!code highlight]
):
    if chunk["type"] == "messages":
        msg, metadata = chunk["data"]
        # Filter the streamed tokens by the tags field in the metadata to only include
        # the tokens from the LLM invocation with the "joke" tag
        if metadata["tags"] == ["joke"]:
            print(msg.content, end="|", flush=True)
```

<Accordion title="Extended example: filtering by tags">
  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from typing import TypedDict

  from langchain.chat_models import init_chat_model
  from langgraph.graph import START, StateGraph

  # The joke_model is tagged with "joke"
  joke_model = init_chat_model(model="gpt-5.4-mini", tags=["joke"])
  # The poem_model is tagged with "poem"
  poem_model = init_chat_model(model="gpt-5.4-mini", tags=["poem"])

  class State(TypedDict):
        topic: str
        joke: str
        poem: str

  async def call_model(state, config):
        topic = state["topic"]
        print("Writing joke...")
        # Note: Passing the config through explicitly is required for python < 3.11
        # Since context var support wasn't added before then: https://docs.python.org/3/library/asyncio-task.html#creating-tasks
        # The config is passed through explicitly to ensure the context vars are propagated correctly
        # This is required for Python < 3.11 when using async code. Please see the async section for more details
        joke_response = await joke_model.ainvoke(
              [{"role": "user", "content": f"Write a joke about {topic}"}],
              config,
        )
        print("\n\nWriting poem...")
        poem_response = await poem_model.ainvoke(
              [{"role": "user", "content": f"Write a short poem about {topic}"}],
              config,
        )
        return {"joke": joke_response.content, "poem": poem_response.content}

  graph = (
        StateGraph(State)
        .add_node(call_model)
        .add_edge(START, "call_model")
        .compile()
  )

  # The stream_mode is set to "messages" to stream LLM tokens
  # The metadata contains information about the LLM invocation, including the tags
  async for chunk in graph.astream(
        {"topic": "cats"},
        stream_mode="messages",
        version="v2",
  ):
      if chunk["type"] == "messages":
          msg, metadata = chunk["data"]
          if metadata["tags"] == ["joke"]:
              print(msg.content, end="|", flush=True)
  ```
</Accordion>

#### Omit messages from the stream

Use the `nostream` tag to exclude LLM output from the stream entirely. Invocations tagged with `nostream` still run and produce output; their tokens are simply not emitted in `messages` mode.

This is useful when:

* You need LLM output for internal processing (for example structured output) but do not want to stream it to the client
* You stream the same content through a different channel (for example custom UI messages) and want to avoid duplicate output in the `messages` stream

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from typing import Any, TypedDict

from langchain_anthropic import ChatAnthropic
from langgraph.graph import START, StateGraph

stream_model = ChatAnthropic(model_name="claude-haiku-4-5-20251001")
internal_model = ChatAnthropic(model_name="claude-haiku-4-5-20251001").with_config(
    {"tags": ["nostream"]}
)

class State(TypedDict):
    topic: str
    answer: str
    notes: str

def answer(state: State) -> dict[str, Any]:
    r = stream_model.invoke(
        [{"role": "user", "content": f"Reply briefly about {state['topic']}"}]
    )
    return {"answer": r.content}

def internal_notes(state: State) -> dict[str, Any]:
    # Tokens from this model are omitted from stream_mode="messages" because of nostream
    r = internal_model.invoke(
        [{"role": "user", "content": f"Private notes on {state['topic']}"}]
    )
    return {"notes": r.content}

graph = (
    StateGraph(State)
    .add_node("write_answer", answer)
    .add_node("internal_notes", internal_notes)
    .add_edge(START, "write_answer")
    .add_edge("write_answer", "internal_notes")
    .compile()
)

initial_state: State = {"topic": "AI", "answer": "", "notes": ""}
stream = graph.stream(initial_state, stream_mode="messages")
```

#### Filter by node

To stream tokens only from specific nodes, use `stream_mode="messages"` and filter the outputs by the `langgraph_node` field in the streamed metadata:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# The "messages" stream mode streams LLM tokens with metadata
