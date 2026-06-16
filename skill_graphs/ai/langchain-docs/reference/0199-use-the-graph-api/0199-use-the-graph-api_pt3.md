
Let's consider a simple graph with a loop to better understand how these mechanisms work.

<Tip>
  To return the last value of your state instead of receiving a recursion limit error, see the [next section](#impose-a-recursion-limit).
</Tip>

When creating a loop, you can include a conditional edge that specifies a termination condition:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const route: ConditionalEdgeRouter<typeof State, "b"> = (state) => {
  if (terminationCondition(state)) {
    return END;
  } else {
    return "b";
  }
};

const graph = new StateGraph(State)
  .addNode("a", nodeA)
  .addNode("b", nodeB)
  .addEdge(START, "a")
  .addConditionalEdges("a", route)
  .addEdge("b", "a")
  .compile();
```

To control the recursion limit, specify `"recursionLimit"` in the config. This will raise a `GraphRecursionError`, which you can catch and handle:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { GraphRecursionError } from "@langchain/langgraph";

try {
  await graph.invoke(inputs, { recursionLimit: 3 });
} catch (error) {
  if (error instanceof GraphRecursionError) {
    console.log("Recursion Error");
  }
}
```

Let's define a graph with a simple loop. Note that we use a conditional edge to implement a termination condition.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { StateGraph, StateSchema, ReducedValue, GraphNode, ConditionalEdgeRouter, START, END } from "@langchain/langgraph";
import * as z from "zod";

const State = new StateSchema({
  // The reducer makes this append-only
  aggregate: new ReducedValue(
    z.array(z.string()).default(() => []),
    { reducer: (x, y) => x.concat(y) }
  ),
});

const nodeA: GraphNode<typeof State> = (state) => {
  console.log(`Node A sees ${state.aggregate}`);
  return { aggregate: ["A"] };
};

const nodeB: GraphNode<typeof State> = (state) => {
  console.log(`Node B sees ${state.aggregate}`);
  return { aggregate: ["B"] };
};

// Define edges
const route: ConditionalEdgeRouter<typeof State, "b"> = (state) => {
  if (state.aggregate.length < 7) {
    return "b";
  } else {
    return END;
  }
};

const graph = new StateGraph(State)
  .addNode("a", nodeA)
  .addNode("b", nodeB)
  .addEdge(START, "a")
  .addConditionalEdges("a", route)
  .addEdge("b", "a")
  .compile();
```

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import * as fs from "node:fs/promises";

const drawableGraph = await graph.getGraphAsync();
const image = await drawableGraph.drawMermaidPng();
const imageBuffer = new Uint8Array(await image.arrayBuffer());

await fs.writeFile("graph.png", imageBuffer);
```

This architecture is similar to a [ReAct agent](/oss/javascript/langgraph/workflows-agents) in which node `"a"` is a tool-calling model, and node `"b"` represents the tools.

In our `route` conditional edge, we specify that we should end after the `"aggregate"` list in the state passes a threshold length.

Invoking the graph, we see that we alternate between nodes `"a"` and `"b"` before terminating once we reach the termination condition.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const result = await graph.invoke({ aggregate: [] });
console.log(result);
```

```
Node A sees []
Node B sees ['A']
Node A sees ['A', 'B']
Node B sees ['A', 'B', 'A']
Node A sees ['A', 'B', 'A', 'B']
Node B sees ['A', 'B', 'A', 'B', 'A']
Node A sees ['A', 'B', 'A', 'B', 'A', 'B']
{ aggregate: ['A', 'B', 'A', 'B', 'A', 'B', 'A'] }
```

### Impose a recursion limit

In some applications, we may not have a guarantee that we will reach a given termination condition. In these cases, we can set the graph's [recursion limit](/oss/javascript/langgraph/graph-api#recursion-limit). This will raise a `GraphRecursionError` after a given number of [supersteps](/oss/javascript/langgraph/graph-api#graphs). We can then catch and handle this exception:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { GraphRecursionError } from "@langchain/langgraph";

try {
  await graph.invoke({ aggregate: [] }, { recursionLimit: 4 });
} catch (error) {
  if (error instanceof GraphRecursionError) {
    console.log("Recursion Error");
  }
}
```

```
Node A sees []
Node B sees ['A']
Node A sees ['A', 'B']
Node B sees ['A', 'B', 'A']
Node A sees ['A', 'B', 'A', 'B']
Recursion Error
```

## Combine control flow and state updates with `Command`

It can be useful to combine control flow (edges) and state updates (nodes). For example, you might want to BOTH perform state updates AND decide which node to go to next in the SAME node. LangGraph provides a way to do so by returning a [Command](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.Command) object from node functions:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { Command } from "@langchain/langgraph";

const myNode = (state: State): Command => {
  return new Command({
    // state update
    update: { foo: "bar" },
    // control flow
    goto: "myOtherNode"
  });
};
```

We show an end-to-end example below. Let's create a simple graph with 3 nodes: A, B and C. We will first execute node A, and then decide whether to go to Node B or Node C next based on the output of node A.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { StateGraph, StateSchema, GraphNode, Command, START } from "@langchain/langgraph";
import * as z from "zod";

// Define graph state
const State = new StateSchema({
  foo: z.string(),
});

// Define the nodes

const nodeA: GraphNode<typeof State, "nodeB" | "nodeC"> = (state) => {
  console.log("Called A");
  const value = Math.random() > 0.5 ? "b" : "c";
  // this is a replacement for a conditional edge function
  const goto = value === "b" ? "nodeB" : "nodeC";

  // note how Command allows you to BOTH update the graph state AND route to the next node
  return new Command({
    // this is the state update
    update: { foo: value },
    // this is a replacement for an edge
    goto,
  });
};

const nodeB: GraphNode<typeof State> = (state) => {
  console.log("Called B");
  return { foo: state.foo + "b" };
};

const nodeC: GraphNode<typeof State> = (state) => {
  console.log("Called C");
  return { foo: state.foo + "c" };
};
```

We can now create the `StateGraph` with the above nodes. Notice that the graph doesn't have [conditional edges](/oss/javascript/langgraph/graph-api#conditional-edges) for routing! This is because control flow is defined with `Command` inside `nodeA`.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const graph = new StateGraph(State)
  .addNode("nodeA", nodeA, {
    ends: ["nodeB", "nodeC"],
  })
  .addNode("nodeB", nodeB)
  .addNode("nodeC", nodeC)
  .addEdge(START, "nodeA")
  .compile();
```

<Warning>
  You might have noticed that we used `ends` to specify which nodes `nodeA` can navigate to. This is necessary for the graph rendering and tells LangGraph that `nodeA` can navigate to `nodeB` and `nodeC`.
</Warning>

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import * as fs from "node:fs/promises";

const drawableGraph = await graph.getGraphAsync();
const image = await drawableGraph.drawMermaidPng();
const imageBuffer = new Uint8Array(await image.arrayBuffer());

await fs.writeFile("graph.png", imageBuffer);
```

If we run the graph multiple times, we'd see it take different paths (A -> B or A -> C) based on the random choice in node A.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const result = await graph.invoke({ foo: "" });
console.log(result);
```

```
Called A
Called C
{ foo: 'cc' }
```

### Navigate to a node in a parent graph

If you are using [subgraphs](/oss/javascript/langgraph/use-subgraphs), you might want to navigate from a node within a subgraph to a different subgraph (i.e. a different node in the parent graph). To do so, you can specify `graph=Command.PARENT` in `Command`:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const myNode = (state: State): Command => {
  return new Command({
    update: { foo: "bar" },
    goto: "otherSubgraph",  // where `otherSubgraph` is a node in the parent graph
    graph: Command.PARENT
  });
};
```

Let's demonstrate this using the above example. We'll do so by changing `nodeA` in the above example into a single-node graph that we'll add as a subgraph to our parent graph.

<Warning>
  **State updates with `Command.PARENT`**
  When you send updates from a subgraph node to a parent graph node for a key that's shared by both parent and subgraph [state schemas](/oss/javascript/langgraph/graph-api#schema), you **must** define a [reducer](/oss/javascript/langgraph/graph-api#reducers) for the key you're updating in the parent graph state. See the example below.
</Warning>

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { StateGraph, StateSchema, ReducedValue, GraphNode, Command, START } from "@langchain/langgraph";
import * as z from "zod";

const State = new StateSchema({
  // NOTE: we define a reducer here
  foo: new ReducedValue(  // [!code highlight]
    z.string().default(""),
    { reducer: (x, y) => x + y }
  ),
});

const nodeA: GraphNode<typeof State, "nodeB" | "nodeC"> = (state) => {
  console.log("Called A");
  const value = Math.random() > 0.5 ? "nodeB" : "nodeC";

  // note how Command allows you to BOTH update the graph state AND route to the next node
  return new Command({
    update: { foo: "a" },  // [!code highlight]
    goto: value,
    // this tells LangGraph to navigate to nodeB or nodeC in the parent graph
    // NOTE: this will navigate to the closest parent graph relative to the subgraph
    graph: Command.PARENT,
  });
};

const subgraph = new StateGraph(State)
  .addNode("nodeA", nodeA, { ends: ["nodeB", "nodeC"] })
  .addEdge(START, "nodeA")
  .compile();

const nodeB: GraphNode<typeof State> = (state) => {
  console.log("Called B");  // [!code highlight]
  // NOTE: since we've defined a reducer, we don't need to manually append
  // new characters to existing 'foo' value. instead, reducer will append these
  // automatically
  return { foo: "b" };
};  // [!code highlight]

const nodeC: GraphNode<typeof State> = (state) => {
  console.log("Called C");
  return { foo: "c" };
};

const graph = new StateGraph(State)
  .addNode("subgraph", subgraph, { ends: ["nodeB", "nodeC"] })
  .addNode("nodeB", nodeB)
  .addNode("nodeC", nodeC)
  .addEdge(START, "subgraph")
  .compile();
```

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const result = await graph.invoke({ foo: "" });
console.log(result);
```

```
Called A
Called C
{ foo: 'ac' }
```

### Use inside tools

A common use case is updating graph state from inside a tool. For example, in a customer support application you might want to look up customer information based on their account number or ID in the beginning of the conversation. To update the graph state from the tool, you can return `Command(update={"my_custom_key": "foo", "messages": [...]})` from the tool:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { tool } from "@langchain/core/tools";
import { Command } from "@langchain/langgraph";
import * as z from "zod";

const lookupUserInfo = tool(
  async (input, runtime) => {
    const userId = runtime.serverInfo?.user?.identity;  // [!code highlight]
    const userInfo = getUserInfo(userId);
    return new Command({
      update: {
        // update the state keys
        userInfo: userInfo,
        // update the message history
        messages: [{
          role: "tool",
          content: "Successfully looked up user information",
          tool_call_id: runtime.toolCall.id
        }]
      }
    });
  },
  {
    name: "lookupUserInfo",
    description: "Use this to look up user information to better assist them with their questions.",
    schema: z.object({}),
  }
);
```

<Warning>
  You MUST include `messages` (or any state key used for the message history) in `Command.update` when returning [`Command`](https://reference.langchain.com/javascript/langchain-langgraph/index/Command) from a tool and the list of messages in `messages` MUST contain a `ToolMessage`. This is necessary for the resulting message history to be valid (LLM providers require AI messages with tool calls to be followed by the tool result messages).
</Warning>

If you are using tools that update state via [`Command`](https://reference.langchain.com/javascript/langchain-langgraph/index/Command), we recommend using prebuilt [`ToolNode`](https://reference.langchain.com/javascript/langchain-langgraph/prebuilt/ToolNode) which automatically handles tools returning [`Command`](https://reference.langchain.com/javascript/langchain-langgraph/index/Command) objects and propagates them to the graph state. If you're writing a custom node that calls tools, you would need to manually propagate [`Command`](https://reference.langchain.com/javascript/langchain-langgraph/index/Command) objects returned by the tools as the update from the node.

## Visualize your graph

Here we demonstrate how to visualize the graphs you create.

You can visualize any arbitrary [Graph](https://langchain-ai.github.io/langgraph/reference/graphs/), including [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph).

Let's create a simple example graph to demonstrate visualization.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { StateGraph, StateSchema, MessagesValue, ReducedValue, GraphNode, ConditionalEdgeRouter, START, END } from "@langchain/langgraph";
import * as z from "zod";

const State = new StateSchema({
  messages: MessagesValue,
  value: new ReducedValue(
    z.number().default(0),
    { reducer: (x, y) => x + y }
  ),
});

const node1: GraphNode<typeof State> = (state) => {
  return { value: state.value + 1 };
};

const node2: GraphNode<typeof State> = (state) => {
  return { value: state.value * 2 };
};

const router: ConditionalEdgeRouter<typeof State, "node2"> = (state) => {
  if (state.value < 10) {
    return "node2";
  }
  return END;
};

const app = new StateGraph(State)
  .addNode("node1", node1)
  .addNode("node2", node2)
  .addEdge(START, "node1")
  .addConditionalEdges("node1", router)
  .addEdge("node2", "node1")
  .compile();
```

### Mermaid

We can also convert a graph class into Mermaid syntax.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const drawableGraph = await app.getGraphAsync();
console.log(drawableGraph.drawMermaid());
```

```
%%{init: {'flowchart': {'curve': 'linear'}}}%%
graph TD;
    tart__([<p>__start__</p>]):::first
    e1(node1)
    e2(node2)
    nd__([<p>__end__</p>]):::last
    tart__ --> node1;
    e1 -.-> node2;
    e1 -.-> __end__;
    e2 --> node1;
    ssDef default fill:#f2f0ff,line-height:1.2
    ssDef first fill-opacity:0
    ssDef last fill:#bfb6fc
```

### PNG

If preferred, we could render the Graph into a `.png`. This uses the Mermaid.ink API to generate the diagram.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import * as fs from "node:fs/promises";

const drawableGraph = await app.getGraphAsync();
const image = await drawableGraph.drawMermaidPng();
const imageBuffer = new Uint8Array(await image.arrayBuffer());

await fs.writeFile("graph.png", imageBuffer);
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
