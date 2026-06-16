
    import {
      END,
      MemorySaver,
      START,
      StateGraph,
      StateSchema,
    } from "@langchain/langgraph";
    import type { GraphNode } from "@langchain/langgraph";

    const State = new StateSchema({
      url: z.string(),
      result: z.string().optional(),
    });

    const callApi: GraphNode<typeof State> = async (state) => {
      const response = await fetch(state.url);  // [!code highlight]
      const text = await response.text();
      const result = text.slice(0, 100);
      return { result };
    };

    const builder = new StateGraph(State)
      .addNode("callApi", callApi)
      .addEdge(START, "callApi")
      .addEdge("callApi", END);

    const checkpointer = new MemorySaver();
    const graph = builder.compile({ checkpointer });

    const threadId = uuid7();
    const config = { configurable: { thread_id: threadId } };

    await graph.invoke({ url: "https://www.example.com" }, config);
    ```
  </Tab>

  <Tab title="With task">
    ```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { v7 as uuid7 } from "uuid";
    import * as z from "zod";

    import {
      END,
      MemorySaver,
      START,
      StateGraph,
      StateSchema,
      task,
    } from "@langchain/langgraph";
    import type { GraphNode } from "@langchain/langgraph";

    const State = new StateSchema({
      urls: z.array(z.string()),
      results: z.array(z.string()).optional(),
    });

    const makeRequest = task("makeRequest", async (url: string) => {
      const response = await fetch(url);  // [!code highlight]
      const text = await response.text();
      return text.slice(0, 100);
    });

    const callApi: GraphNode<typeof State> = async (state) => {
      const pending = state.urls.map((url) => makeRequest(url));  // [!code highlight]
      const results = await Promise.all(pending);
      return { results };
    };

    const builder = new StateGraph(State)
      .addNode("callApi", callApi)
      .addEdge(START, "callApi")
      .addEdge("callApi", END);

    const checkpointer = new MemorySaver();
    const graph = builder.compile({ checkpointer });

    const threadId = uuid7();
    const config = { configurable: { thread_id: threadId } };

    await graph.invoke({ urls: ["https://www.example.com"] }, config);
    ```
  </Tab>
</Tabs>

### `START` node

The [`START`](https://reference.langchain.com/javascript/langchain-langgraph/index/START) Node is a special node that represents the node that sends user input to the graph. The main purpose for referencing this node is to determine which nodes should be called first.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { START } from "@langchain/langgraph";

graph.addEdge(START, "nodeA");
```

### `END` node

The `END` Node is a special node that represents a terminal node. This node is referenced when you want to denote which edges have no actions after they are done.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { END } from "@langchain/langgraph";

graph.addEdge("nodeA", END);
```

### Node caching

LangGraph supports caching of tasks/nodes based on the input to the node. To use caching:

* Specify a cache when compiling a graph (or specifying an entrypoint)
* Specify a cache policy for nodes. Each cache policy supports:
  * `keyFunc`, which is used to generate a cache key based on the input to a node.
  * `ttl`, the time to live for the cache in seconds. If not specified, the cache will never expire.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { StateGraph, StateSchema, GraphNode, START } from "@langchain/langgraph";
import { InMemoryCache } from "@langchain/langgraph-checkpoint";
import { z } from "zod/v4";

const State = new StateSchema({
  x: z.number(),
  result: z.number(),
});

const expensiveNode: GraphNode<typeof State> = async (state) => {
  // Simulate an expensive operation
  await new Promise((resolve) => setTimeout(resolve, 3000));
  return { result: state.x * 2 };
};

const graph = new StateGraph(State)
  .addNode("expensive_node", expensiveNode, { cachePolicy: { ttl: 3 } })
  .addEdge(START, "expensive_node")
  .compile({ cache: new InMemoryCache() });

await graph.invoke({ x: 5 }, { streamMode: "updates" });   // [!code highlight]
// [{"expensive_node": {"result": 10}}]
await graph.invoke({ x: 5 }, { streamMode: "updates" });   // [!code highlight]
// [{"expensive_node": {"result": 10}, "__metadata__": {"cached": true}}]
```

## Edges

Edges define how the logic is routed and how the graph decides to stop. This is a big part of how your agents work and how different nodes communicate with each other. There are a few key types of edges:

* Normal Edges: Go directly from one node to the next.
* Conditional Edges: Call a function to determine which node(s) to go to next.
* Entry Point: Which node to call first when user input arrives.
* Conditional Entry Point: Call a function to determine which node(s) to call first when user input arrives.

A node can have multiple outgoing edges. If a node has multiple outgoing edges, **all** of those destination nodes will be executed in parallel as a part of the next superstep.

<Warning>
  For each node, choose one routing mechanism: use normal edges for static routing, or use conditional edges / [`Command`](https://reference.langchain.com/javascript/langchain-langgraph/index/Command) for dynamic routing. Do not mix normal edges and dynamic routing from the same node, because both paths can execute and make graph behavior harder to reason about.
</Warning>

### Normal edges

If you **always** want to go from node A to node B, you can use the [`addEdge`](https://reference.langchain.com/javascript/classes/_langchain_langgraph.index.StateGraph.html#addEdge) method directly.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
graph.addEdge("nodeA", "nodeB");
```

### Conditional edges

If you want to **optionally** route to one or more edges (or optionally terminate), you can use the [`addConditionalEdges`](https://reference.langchain.com/javascript/classes/_langchain_langgraph.index.StateGraph.html#addConditionalEdges) method. This method accepts the name of a node and a "routing function" to call after that node is executed:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
graph.addConditionalEdges("nodeA", routingFunction);
```

Similar to nodes, the `routingFunction` accepts the current `state` of the graph and returns a value.

By default, the return value `routingFunction` is used as the name of the node (or list of nodes) to send the state to next. All those nodes will be run in parallel as a part of the next superstep.

You can optionally provide an object that maps the `routingFunction`'s output to the name of the next node.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
graph.addConditionalEdges("nodeA", routingFunction, {
  true: "nodeB",
  false: "nodeC",
});
```

<Tip>
  Use [`Command`](#command) instead of conditional edges if you want to combine state updates and routing in a single function.
</Tip>

### Entry point

The entry point is the first node(s) that are run when the graph starts. You can use the [`addEdge`](https://reference.langchain.com/javascript/classes/_langchain_langgraph.index.StateGraph.html#addEdge) method from the virtual [`START`](https://reference.langchain.com/javascript/langchain-langgraph/index/START) node to the first node to execute to specify where to enter the graph.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { START } from "@langchain/langgraph";

graph.addEdge(START, "nodeA");
```

### Conditional entry point

A conditional entry point lets you start at different nodes depending on custom logic. You can use [`addConditionalEdges`](https://reference.langchain.com/javascript/classes/_langchain_langgraph.index.StateGraph.html#addConditionalEdges) from the virtual [`START`](https://reference.langchain.com/javascript/langchain-langgraph/index/START) node to accomplish this.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { START } from "@langchain/langgraph";

graph.addConditionalEdges(START, routingFunction);
```

You can optionally provide an object that maps the `routingFunction`'s output to the name of the next node.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
graph.addConditionalEdges(START, routingFunction, {
  true: "nodeB",
  false: "nodeC",
});
```

## `Send`

By default, `Nodes` and `Edges` are defined ahead of time and operate on the same shared state. However, there can be cases where the exact edges are not known ahead of time and/or you may want different versions of `State` to exist at the same time. A common example of this is with map-reduce design patterns. In this design pattern, a first node may generate a list of objects, and you may want to apply some other node to all those objects. The number of objects may be unknown ahead of time (meaning the number of edges may not be known) and the input `State` to the downstream `Node` should be different (one for each generated object).

To support this design pattern, LangGraph supports returning [`Send`](https://reference.langchain.com/javascript/langchain-langgraph/index/Send) objects from conditional edges. `Send` takes two arguments: first is the name of the node, and second is the state to pass to that node.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { Send } from "@langchain/langgraph";

graph.addConditionalEdges("nodeA", (state) => {
  return state.subjects.map(
    (subject) => new Send("generateJoke", { subject })
  );
});
```

## `Command`

[`Command`](https://reference.langchain.com/javascript/langchain-langgraph/index/Command) is a versatile primitive for controlling graph execution. It accepts four parameters:

* `update`: Apply state updates (similar to returning updates from a node).
* `goto`: Navigate to specific nodes (similar to [conditional edges](#conditional-edges)).
* `graph`: Target a parent graph when navigating from [subgraphs](/oss/javascript/langgraph/use-subgraphs).
* `resume`: Provide a value to resume execution after an [interrupt](/oss/javascript/langgraph/interrupts).

`Command` is used in three contexts:

* **[Return from nodes](#return-from-nodes)**: Use `update`, `goto`, and `graph` to combine state updates with control flow.
* **[Input to `invoke` or `stream`](#input-to-invoke-or-stream)**: Use `resume` to continue execution after an interrupt.
* **[Return from tools](#return-from-tools)**: Similar to return from nodes, combine state updates and control flow from inside a tool.

### Return from nodes

#### `update` and `goto`

Return [`Command`](https://reference.langchain.com/javascript/langchain-langgraph/index/Command) from node functions to update state and route to the next node in a single step:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { Command } from "@langchain/langgraph";

graph.addNode("myNode", (state) => {
  return new Command({
    update: { foo: "bar" },
    goto: "myOtherNode",
  });
});
```

With [`Command`](https://reference.langchain.com/javascript/langchain-langgraph/index/Command) you can also achieve dynamic control flow behavior (identical to [conditional edges](#conditional-edges)):

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { Command } from "@langchain/langgraph";

graph.addNode("myNode", (state) => {
  if (state.foo === "bar") {
    return new Command({
      update: { foo: "baz" },
      goto: "myOtherNode",
    });
  }
});
```

Use [`Command`](https://reference.langchain.com/javascript/langchain-langgraph/index/Command) when you need to **both** update state **and** route to a different node. If you only need to route without updating state, use [conditional edges](#conditional-edges) instead.

When using [`Command`](https://reference.langchain.com/javascript/langchain-langgraph/index/Command) in your node functions, you must add the `ends` parameter when adding the node to specify which nodes it can route to:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
builder.addNode("myNode", myNode, {
  ends: ["myOtherNode", END],
});
```

<Warning>
  [`Command`](https://reference.langchain.com/javascript/langchain-langgraph/index/Command) only adds dynamic edges—static edges defined with `add_edge` / `addEdge` still execute. For example, if `node_a` returns `Command(goto="my_other_node")` and you also have `graph.add_edge("node_a", "node_b")`, both `node_b` and `my_other_node` will run. For each node, use either [`Command`](https://reference.langchain.com/javascript/langchain-langgraph/index/Command) or static edges to route to the next nodes, not both.
</Warning>

Check out this [how-to guide](/oss/javascript/langgraph/use-graph-api#combine-control-flow-and-state-updates-with-command) for an end-to-end example of how to use [`Command`](https://reference.langchain.com/javascript/langchain-langgraph/index/Command).

#### `graph`

If you are using [subgraphs](/oss/javascript/langgraph/use-subgraphs), you can navigate from a node within a subgraph to a different node in the parent graph by specifying `graph: Command.PARENT` in `Command`:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { Command } from "@langchain/langgraph";

graph.addNode("myNode", (state) => {
  return new Command({
    update: { foo: "bar" },
    goto: "otherSubgraph", // where `otherSubgraph` is a node in the parent graph
    graph: Command.PARENT,
  });
});
```

<Note>
  Setting `graph` to `Command.PARENT` will navigate to the closest parent graph.

  When you send updates from a subgraph node to a parent graph node for a key that's shared by both parent and subgraph [state schemas](#schema), you **must** define a [reducer](#reducers) for the key you're updating in the parent graph state.
</Note>

This is particularly useful when implementing [multi-agent handoffs](/oss/javascript/langchain/multi-agent/handoffs). Check out [Navigate to a node in a parent graph](/oss/javascript/langgraph/use-graph-api#navigate-to-a-node-in-a-parent-graph) for detail.

### Input to `invoke` or `stream`

<Warning>
  `new Command({ resume: ... })` is the **only** `Command` pattern intended as input to `invoke()`/`stream()`. Do not use `new Command({ update: ... })` as input to continue multi-turn conversations—because passing any `Command` as input resumes from the latest checkpoint (i.e. the last step that ran, not `__start__`), the graph will appear stuck if it already finished. To continue a conversation on an existing thread, pass a plain input object:

  ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  // WRONG - graph resumes from the latest checkpoint
  // (last step that ran), appears stuck
  await graph.invoke(new Command({ update: { messages: [{ role: "user", content: "follow up" }] } }), config);  // [!code --]

  // CORRECT - plain object restarts from __start__
  await graph.invoke({ messages: [{ role: "user", content: "follow up" }] }, config);  // [!code ++]
  ```
</Warning>

#### `resume`

Use `new Command({ resume: ... })` to provide a value and resume graph execution after an [interrupt](/oss/javascript/langgraph/interrupts). The value passed to `resume` becomes the return value of the `interrupt()` call inside the paused node:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { Command, interrupt } from "@langchain/langgraph";

const humanReview = async (state: typeof StateAnnotation.State) => {
  // Pauses the graph and waits for a value
  const answer = interrupt("Do you approve?");
  return { messages: [{ role: "user", content: answer }] };
};

// First invocation - hits the interrupt and pauses
const result = await graph.invoke({ messages: [...] }, config);

// Resume with a value - the interrupt() call returns "yes"
const resumed = await graph.invoke(new Command({ resume: "yes" }), config);
```

Check out the [interrupts conceptual guide](/oss/javascript/langgraph/interrupts) for full details on interrupt patterns, including multiple interrupts and validation loops.

### Return from tools

You can return [`Command`](https://reference.langchain.com/javascript/langchain-langgraph/index/Command) from tools to update graph state and control flow. Use `update` to modify state (e.g., saving customer information looked up during a conversation) and `goto` to route to a specific node after the tool completes.

<Warning>
  When used inside tools, `goto` adds a dynamic edge—any static edges already defined on the node that called the tool will still execute. For each node, use either tool-driven dynamic routing or static edges to route to the next nodes, not both.
</Warning>

Refer to [Use inside tools](/oss/javascript/langgraph/use-graph-api#use-inside-tools) for detail.

## Graph migrations

LangGraph can easily handle migrations of graph definitions (nodes, edges, and state) even when using a checkpointer to track state.

* For threads at the end of the graph (i.e. not interrupted) you can change the entire topology of the graph (i.e. all nodes and edges, remove, add, rename, etc)
* For threads currently interrupted, we support all topology changes other than renaming / removing nodes (as that thread could now be about to enter a node that no longer exists) -- if this is a blocker please reach out and we can prioritize a solution.
* For modifying state, we have full backwards and forwards compatibility for adding and removing keys
* State keys that are renamed lose their saved state in existing threads
* State keys whose types change in incompatible ways could currently cause issues in threads with state from before the change -- if this is a blocker please reach out and we can prioritize a solution.

## Runtime context

When creating a graph, you can specify a `contextSchema` for runtime context passed to nodes. This is useful for passing
information to nodes that is not part of the graph state. For example, you might want to pass dependencies such as model name or a database connection.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { StateGraph, StateSchema } from "@langchain/langgraph";
import * as z from "zod";

const State = new StateSchema({
  input: z.string(),
  output: z.string(),
});

const ContextSchema = z.object({
  llm: z.union([z.literal("openai"), z.literal("anthropic")]),
});

const graph = new StateGraph(State, ContextSchema);
```

You can then pass this configuration into the graph using the `context` property.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const config = { context: { llm: "anthropic" } };

await graph.invoke(inputs, config);
```

You can then access and use this context inside a node or conditional edge:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { Runtime, GraphNode } from "@langchain/langgraph";
import * as z from "zod";

const nodeA: GraphNode<typeof State> = (state, config) => {
  const llm = getLLM(runtime.context?.llm);
  // ...
  return {};
};
```

See [Add runtime configuration](/oss/javascript/langgraph/use-graph-api#add-runtime-configuration) for a full breakdown on configuration.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
graph.addNode("myNode", (state, config) => {
  const llmType = config.context?.llm || "openai";
  const llm = getLLM(llmType);
  return { results: `Hello, ${state.input}!` };
});
```

### Recursion limit

The recursion limit sets the maximum number of [super-steps](#graphs) the graph can execute during a single execution. Once the limit is reached, LangGraph will raise `GraphRecursionError`. By default this value is set to 25 steps. The recursion limit can be set on any graph at runtime, and is passed to `invoke`/`stream` via the config object. Importantly, `recursionLimit` is a standalone `config` key and should not be passed inside the `configurable` key as all other user-defined configuration. See the example below:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
await graph.invoke(inputs, {
  recursionLimit: 5,
  context: { llm: "anthropic" },
});
```

### Accessing and handling the recursion counter

The current step counter is accessible in `config.metadata.langgraph_step` within any node, allowing for proactive recursion handling before hitting the recursion limit. This enables you to implement graceful degradation strategies within your graph logic.

#### How it works

The step counter is stored in `config.metadata.langgraph_step`. LangGraph increments this counter as the graph executes and raises a `GraphRecursionError` once the configured `recursionLimit` is exceeded.

#### Accessing the current step counter

You can access the current step counter within any node to monitor execution progress.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { RunnableConfig } from "@langchain/core/runnables";
import { StateGraph } from "@langchain/langgraph";

const myNode: GraphNode<typeof State> = async (state, config) => {
  const currentStep = config.metadata?.langgraph_step;
  console.log(`Currently on step: ${currentStep}`);
  return state;
}
```

Design your graph with explicit termination conditions, and catch `GraphRecursionError` as a safety net:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import {
  StateGraph,
  StateSchema,
  ReducedValue,
  GraphNode,
  ConditionalEdgeRouter,
  END,
  GraphRecursionError
} from "@langchain/langgraph";
import { z } from "zod/v4";

const State = new StateSchema({
  messages: new ReducedValue(
    z.array(z.string()).default(() => []),
    { reducer: (x, y) => x.concat(y) }
  ),
});

// Build graph with explicit termination logic
const graph = new StateGraph(State)
  .addNode("reasoning", async (state) => {
    // Normal processing - design your graph with explicit termination conditions
    return {
      messages: ["thinking..."]
    };
  })
  .addConditionalEdges("reasoning", (state) => {
    // Add your termination condition here
    if (state.messages.length >= 5) {
      return END;
    }
    return "reasoning";
  });

const app = graph.compile();

// Catch GraphRecursionError as a safety net
try {
  const result = await app.invoke(
    { messages: [] },
    { recursionLimit: 10 }
  );
} catch (error) {
  if (error instanceof GraphRecursionError) {
    console.log("Recursion limit reached, handling gracefully");
    // Handle the error - return partial results, notify user, etc.
  }
}
```

#### Proactive vs reactive approaches

There are two main approaches to handling recursion limits: proactive (monitoring within the graph) and reactive (catching errors externally).

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import {
  StateGraph,
  StateSchema,
  ReducedValue,
  GraphNode,
  ConditionalEdgeRouter,
  END,
  GraphRecursionError
} from "@langchain/langgraph";
import { z } from "zod/v4";

const State = new StateSchema({
  messages: new ReducedValue(
    z.array(z.string()).default(() => []),
    { reducer: (x, y) => x.concat(y) }
  ),
});

// Build graph with explicit termination logic
const builder = new StateGraph(State)
  .addNode("agent", async (state) => {
    return {
      messages: ["Processing..."]
    };
  })
  .addConditionalEdges("agent", (state) => {
    // Design termination conditions into your graph
    if (state.messages.length >= 5) {
      return END;
    }
    return "agent";
  });

const graph = builder.compile();

// Reactive Approach - catch GraphRecursionError as safety net
try {
  const result = await graph.invoke(
    { messages: [] },
    { recursionLimit: 10 }
  );
} catch (error) {
  if (error instanceof GraphRecursionError) {
    // Handle externally after graph execution fails
    console.log("Recursion limit exceeded, handling gracefully");
  }
}
```

The reactive approach catches `GraphRecursionError` after the limit is exceeded. Design your graph with explicit termination conditions to avoid hitting the limit in the first place.

| Approach                                  | Detection            | Handling                   | Control Flow               |
| ----------------------------------------- | -------------------- | -------------------------- | -------------------------- |
| Reactive (catching `GraphRecursionError`) | After limit exceeded | Outside graph in try/catch | Graph execution terminated |

**Reactive advantages:**

* Simple implementation
* No need to modify graph logic
* Centralized error handling

#### Other available metadata

Along with `langgraph_step`, the following metadata is also available in `config.metadata`:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const inspectMetadata: GraphNode<typeof State> = async (state, config) => {
  const metadata = config.metadata;

  console.log(`Step: ${metadata?.langgraph_step}`);
  console.log(`Node: ${metadata?.langgraph_node}`);
  console.log(`Triggers: ${metadata?.langgraph_triggers}`);
