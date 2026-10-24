    { messages: [inputMessage] },
    {
      configurable: {
        modelProvider: "openai",
        systemMessage: "Respond in Italian."
      }
    }
  );

  for (const message of response.messages) {
    console.log(`${message.getType()}: ${message.content}`);
  }
  ```

  ```
  human: hi
  ai: Ciao! Come posso aiutarti oggi?
  ```
</Accordion>

## Add retry policies

There are many use cases where you may wish for your node to have a custom retry policy, for example if you are calling an API, querying a database, or calling an LLM, etc. LangGraph lets you add retry policies to nodes.

To configure a retry policy, pass the `retryPolicy` parameter to the [`addNode`](https://reference.langchain.com/javascript/classes/_langchain_langgraph.index.Graph.html#addnode). The `retryPolicy` parameter takes in a `RetryPolicy` object. Below we instantiate a `RetryPolicy` object with the default parameters and associate it with a node:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { RetryPolicy } from "@langchain/langgraph";

const graph = new StateGraph(State)
  .addNode("nodeName", nodeFunction, { retryPolicy: {} })
  .compile();
```

By default, the retry policy retries on any exception except for the following:

* `TypeError`
* `SyntaxError`
* `ReferenceError`

<Accordion title="Extended example: customizing retry policies">
  Consider an example in which we are reading from a SQL database. Below we pass two different retry policies to nodes:

  ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import Database from "better-sqlite3";
  import { ChatAnthropic } from "@langchain/anthropic";
  import { StateGraph, StateSchema, MessagesValue, GraphNode, START, END } from "@langchain/langgraph";
  import { AIMessage } from "@langchain/core/messages";

  const State = new StateSchema({
    messages: MessagesValue,
  });

  // Create an in-memory database
  const db: typeof Database.prototype = new Database(":memory:");

  const model = new ChatAnthropic({ model: "claude-3-5-sonnet-20240620" });

  const callModel: GraphNode<typeof State> = async (state) => {
    const response = await model.invoke(state.messages);
    return { messages: [response] };
  };

  const queryDatabase: GraphNode<typeof State> = async (state) => {
    const queryResult: string = JSON.stringify(
      db.prepare("SELECT * FROM Artist LIMIT 10;").all(),
    );

    return { messages: [new AIMessage({ content: "queryResult" })] };
  };

  const workflow = new StateGraph(State)
    // Define the two nodes we will cycle between
    .addNode("call_model", callModel, { retryPolicy: { maxAttempts: 5 } })
    .addNode("query_database", queryDatabase, {
      retryPolicy: {
        retryOn: (e: any): boolean => {
          if (e instanceof Database.SqliteError) {
            // Retry on "SQLITE_BUSY" error
            return e.code === "SQLITE_BUSY";
          }
          return false; // Don't retry on other errors
        },
      },
    })
    .addEdge(START, "call_model")
    .addEdge("call_model", "query_database")
    .addEdge("query_database", END);

  const graph = workflow.compile();
  ```
</Accordion>

### Access execution info inside a node

You can access execution identity and retry information via `runtime.executionInfo`. This surfaces thread, run, and checkpoint identifiers as well as retry state, without needing to read from `config` directly.

| Attribute              | Type                  | Description                                                                                |
| ---------------------- | --------------------- | ------------------------------------------------------------------------------------------ |
| `threadId`             | `string \| undefined` | Thread ID for the current execution.                                                       |
| `runId`                | `string \| undefined` | Run ID for the current execution.                                                          |
| `checkpointId`         | `string`              | Checkpoint ID for the current execution.                                                   |
| `checkpointNs`         | `string`              | Checkpoint namespace for the current execution.                                            |
| `taskId`               | `string`              | Task ID for the current execution.                                                         |
| `nodeAttempt`          | `number`              | Current execution attempt number (1-indexed).                                              |
| `nodeFirstAttemptTime` | `number \| undefined` | Unix timestamp (seconds) of when the first attempt started. Stays the same across retries. |

#### Access thread and run IDs

Use `executionInfo` to access the thread ID, run ID, and other identity fields inside a node:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { StateGraph, StateSchema, START, END } from "@langchain/langgraph";
import * as z from "zod";

const State = new StateSchema({
  result: z.string(),
});

const myNode: GraphNode<typeof State> = async (state, runtime) => {
  const info = runtime.executionInfo;
  console.log(`Thread: ${info.threadId}, Run: ${info.runId}`);  // [!code highlight]
  return { result: "done" };
};

const graph = new StateGraph(State)
  .addNode("my_node", myNode)
  .addEdge(START, "my_node")
  .addEdge("my_node", END)
  .compile();
```

#### Adjust behavior based on retry state

When a node has a retry policy, use `executionInfo` to inspect the current attempt number and switch to a fallback after the first attempt fails:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { StateGraph, StateSchema, START, END } from "@langchain/langgraph";
import * as z from "zod";

const State = new StateSchema({
  result: z.string(),
});

const myNode: GraphNode<typeof State> = async (state, runtime) => {
  const info = runtime.executionInfo;
  if (info.nodeAttempt > 1) {  // [!code highlight]
    // use a fallback on retries
    return { result: await callFallbackApi() };
  }
  return { result: await callPrimaryApi() };
};

const graph = new StateGraph(State)
  .addNode("my_node", myNode, { retryPolicy: { maxAttempts: 3 } })
  .addEdge(START, "my_node")
  .addEdge("my_node", END)
  .compile();
```

`executionInfo` is available on the `Runtime` object even without a retry policy — `nodeAttempt` defaults to `1` and `nodeFirstAttemptTime` is set to the time the node starts executing.

### Access server info inside a node

When your graph runs on LangGraph Server, you can access server-specific metadata via `runtime.serverInfo`.

| Attribute     | Type               | Description                                                                     |
| ------------- | ------------------ | ------------------------------------------------------------------------------- |
| `assistantId` | `string`           | The assistant ID for the current deployment.                                    |
| `graphId`     | `string`           | The graph ID for the current deployment.                                        |
| `user`        | `BaseUser \| null` | The authenticated user, if [custom auth](/langsmith/custom-auth) is configured. |

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const myNode: GraphNode<typeof State> = async (state, runtime) => {
  const server = runtime.serverInfo;
  if (server != null) {
    console.log(`Assistant: ${server.assistantId}, Graph: ${server.graphId}`);  // [!code highlight]
    if (server.user != null) {
      console.log(`User: ${server.user.identity}`);
    }
  }
  return { result: "done" };
};
```

`serverInfo` is `null` when the graph is not running on LangGraph Server.

<Note>
  Requires `deepagents>=1.9.0` (or `@langchain/langgraph>=1.2.8`) for `runtime.executionInfo` and `runtime.serverInfo`.
</Note>

## Create a sequence of steps

<Info>
  **Prerequisites**
  This guide assumes familiarity with the above section on [state](#define-and-update-state).
</Info>

Here we demonstrate how to construct a simple sequence of steps. We will show:

1. How to build a sequential graph
2. Built-in short-hand for constructing similar graphs.

To add a sequence of nodes, we use the `.addNode` and `.addEdge` methods of our [graph](/oss/javascript/langgraph/graph-api#stategraph):

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { START, StateGraph } from "@langchain/langgraph";

const builder = new StateGraph(State)
  .addNode("step1", step1)
  .addNode("step2", step2)
  .addNode("step3", step3)
  .addEdge(START, "step1")
  .addEdge("step1", "step2")
  .addEdge("step2", "step3");
```

<Accordion title="Why split application steps into a sequence with LangGraph?">
  LangGraph makes it easy to add an underlying persistence layer to your application.
  This allows state to be checkpointed in between the execution of nodes, so your LangGraph nodes govern:

  * How state updates are [checkpointed](/oss/javascript/langgraph/persistence)
  * How interruptions are resumed in [human-in-the-loop](/oss/javascript/langgraph/interrupts) workflows
  * How we can "rewind" and branch-off executions using LangGraph's [time travel](/oss/javascript/langgraph/use-time-travel) features

  They also determine how execution steps are [streamed](/oss/javascript/langgraph/streaming), and how your application is visualized and debugged using [Studio](/langsmith/studio).

  Let's demonstrate an end-to-end example. We will create a sequence of three steps:

  1. Populate a value in a key of the state
  2. Update the same value
  3. Populate a different value

  Let's first define our [state](/oss/javascript/langgraph/graph-api#state). This governs the [schema of the graph](/oss/javascript/langgraph/graph-api#schema), and can also specify how to apply updates. See [Process state updates with reducers](#process-state-updates-with-reducers) for more detail.

  In our case, we will just keep track of two values:

  ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { StateSchema, GraphNode } from "@langchain/langgraph";
  import * as z from "zod";

  const State = new StateSchema({
    value1: z.string(),
    value2: z.number(),
  });
  ```

  Our [nodes](/oss/javascript/langgraph/graph-api#nodes) are just TypeScript functions that read our graph's state and make updates to it. The first argument to this function will always be the state:

  ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  const step1: GraphNode<typeof State> = (state) => {
    return { value1: "a" };
  };

  const step2: GraphNode<typeof State> = (state) => {
    const currentValue1 = state.value1;
    return { value1: `${currentValue1} b` };
  };

  const step3: GraphNode<typeof State> = (state) => {
    return { value2: 10 };
  };
  ```

  <Note>
    Note that when issuing updates to the state, each node can just specify the value of the key it wishes to update.

    By default, this will **overwrite** the value of the corresponding key. You can also use [reducers](/oss/javascript/langgraph/graph-api#reducers) to control how updates are processed—for example, you can append successive updates to a key instead. See [Process state updates with reducers](#process-state-updates-with-reducers) for more detail.
  </Note>

  Finally, we define the graph. We use [StateGraph](/oss/javascript/langgraph/graph-api#stategraph) to define a graph that operates on this state.

  We will then use [addNode](/oss/javascript/langgraph/graph-api#nodes) and [addEdge](/oss/javascript/langgraph/graph-api#edges) to populate our graph and define its control flow.

  ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { START, StateGraph } from "@langchain/langgraph";

  const graph = new StateGraph(State)
    .addNode("step1", step1)
    .addNode("step2", step2)
    .addNode("step3", step3)
    .addEdge(START, "step1")
    .addEdge("step1", "step2")
    .addEdge("step2", "step3")
    .compile();
  ```

  <Tip>
    **Specifying custom names**
    You can specify custom names for nodes using `.addNode`:

    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    const graph = new StateGraph(State)
    .addNode("myNode", step1)
    .compile();
    ```
  </Tip>

  Note that:

  * `.addEdge` takes the names of nodes, which for functions defaults to `node.name`.
  * We must specify the entry point of the graph. For this we add an edge with the [START node](/oss/javascript/langgraph/graph-api#start-node).
  * The graph halts when there are no more nodes to execute.

  We next [compile](/oss/javascript/langgraph/graph-api#compiling-your-graph) our graph. This provides a few basic checks on the structure of the graph (e.g., identifying orphaned nodes). If we were adding persistence to our application via a [checkpointer](/oss/javascript/langgraph/persistence), it would also be passed in here.

  LangGraph provides built-in utilities for visualizing your graph. Let's inspect our sequence. See [Visualize your graph](#visualize-your-graph) for detail on visualization.

  ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import * as fs from "node:fs/promises";

  const drawableGraph = await graph.getGraphAsync();
  const image = await drawableGraph.drawMermaidPng();
  const imageBuffer = new Uint8Array(await image.arrayBuffer());

  await fs.writeFile("graph.png", imageBuffer);
  ```

  Let's proceed with a simple invocation:

  ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  const result = await graph.invoke({ value1: "c" });
  console.log(result);
  ```

  ```
  { value1: 'a b', value2: 10 }
  ```

  Note that:

  * We kicked off invocation by providing a value for a single state key. We must always provide a value for at least one key.
  * The value we passed in was overwritten by the first node.
  * The second node updated the value.
  * The third node populated a different value.
</Accordion>

## Create branches

Parallel execution of nodes is essential to speed up overall graph operation. LangGraph offers native support for parallel execution of nodes, which can significantly enhance the performance of graph-based workflows. This parallelization is achieved through fan-out and fan-in mechanisms, utilizing both standard edges and [conditional\_edges](https://langchain-ai.github.io/langgraph/reference/graphs.md#langgraph.graph.MessageGraph.add_conditional_edges). Below are some examples showing how to add create branching dataflows that work for you.

### Run graph nodes in parallel

In this example, we fan out from `Node A` to `B and C` and then fan in to `D`. With our state, [we specify the reducer add operation](/oss/javascript/langgraph/graph-api#reducers). This will combine or accumulate values for the specific key in the State, rather than simply overwriting the existing value. For lists, this means concatenating the new list with the existing list. See the above section on [state reducers](#process-state-updates-with-reducers) for more detail on updating state with reducers.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { StateGraph, StateSchema, ReducedValue, GraphNode, START, END } from "@langchain/langgraph";
import * as z from "zod";

const State = new StateSchema({
  // The reducer makes this append-only
  aggregate: new ReducedValue(
    z.array(z.string()).default(() => []),
    { reducer: (x, y) => x.concat(y) }
  ),
});

const nodeA: GraphNode<typeof State> = (state) => {
  console.log(`Adding "A" to ${state.aggregate}`);
  return { aggregate: ["A"] };
};

const nodeB: GraphNode<typeof State> = (state) => {
  console.log(`Adding "B" to ${state.aggregate}`);
  return { aggregate: ["B"] };
};

const nodeC: GraphNode<typeof State> = (state) => {
  console.log(`Adding "C" to ${state.aggregate}`);
  return { aggregate: ["C"] };
};

const nodeD: GraphNode<typeof State> = (state) => {
  console.log(`Adding "D" to ${state.aggregate}`);
  return { aggregate: ["D"] };
};

const graph = new StateGraph(State)
  .addNode("a", nodeA)
  .addNode("b", nodeB)
  .addNode("c", nodeC)
  .addNode("d", nodeD)
  .addEdge(START, "a")
  .addEdge("a", "b")
  .addEdge("a", "c")
  .addEdge("b", "d")
  .addEdge("c", "d")
  .addEdge("d", END)
  .compile();
```

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import * as fs from "node:fs/promises";

const drawableGraph = await graph.getGraphAsync();
const image = await drawableGraph.drawMermaidPng();
const imageBuffer = new Uint8Array(await image.arrayBuffer());

await fs.writeFile("graph.png", imageBuffer);
```

With the reducer, you can see that the values added in each node are accumulated.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const result = await graph.invoke({
  aggregate: [],
});
console.log(result);
```

```
Adding "A" to []
Adding "B" to ['A']
Adding "C" to ['A']
Adding "D" to ['A', 'B', 'C']
{ aggregate: ['A', 'B', 'C', 'D'] }
```

<Note>
  In the above example, nodes `"b"` and `"c"` are executed concurrently in the same [superstep](/oss/javascript/langgraph/graph-api#graphs). Because they are in the same step, node `"d"` executes after both `"b"` and `"c"` are finished.

  Importantly, updates from a parallel superstep may not be ordered consistently. If you need a consistent, predetermined ordering of updates from a parallel superstep, you should write the outputs to a separate field in the state together with a value with which to order them.
</Note>

<Accordion title="Exception handling?">
  LangGraph executes nodes within [supersteps](/oss/javascript/langgraph/graph-api#graphs), meaning that while parallel branches are executed in parallel, the entire superstep is **transactional**. If any of these branches raises an exception, **none** of the updates are applied to the state (the entire superstep errors).

  Importantly, when using a [checkpointer](/oss/javascript/langgraph/persistence), results from successful nodes within a superstep are saved, and don't repeat when resumed.

  If you have error-prone (perhaps want to handle flakey API calls), LangGraph provides two ways to address this:

  1. You can write regular python code within your node to catch and handle exceptions.
  2. You can set a **[retry\_policy](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.RetryPolicy)** to direct the graph to retry nodes that raise certain types of exceptions. Only failing branches are retried, so you needn't worry about performing redundant work.

  Together, these let you perform parallel execution and fully control exception handling.
</Accordion>

<Tip>
  **Set max concurrency**
  You can control the maximum number of concurrent tasks by setting `max_concurrency` in the [configuration](https://reference.langchain.com/javascript/interfaces/_langchain_langgraph.index.LangGraphRunnableConfig.html) when invoking the graph.

  ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  const result = await graph.invoke({ value1: "c" }, {configurable: {max_concurrency: 10}});
  ```
</Tip>

### Conditional branching

If your fan-out should vary at runtime based on the state, you can use [`addConditionalEdges`](https://reference.langchain.com/javascript/classes/_langchain_langgraph.index.StateGraph.html#addconditionaledges) to select one or more paths using the graph state. See example below, where node `a` generates a state update that determines the following node.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { StateGraph, StateSchema, ReducedValue, GraphNode, ConditionalEdgeRouter, START, END } from "@langchain/langgraph";
import * as z from "zod";

const State = new StateSchema({
  aggregate: new ReducedValue(
    z.array(z.string()).default(() => []),
    { reducer: (x, y) => x.concat(y) }
  ),
  // Add a key to the state. We will set this key to determine
  // how we branch.
  which: z.string(),  // [!code highlight]
});

const nodeA: GraphNode<typeof State> = (state) => {
  console.log(`Adding "A" to ${state.aggregate}`);
  return { aggregate: ["A"], which: "c" };
};

const nodeB: GraphNode<typeof State> = (state) => {
  console.log(`Adding "B" to ${state.aggregate}`);
  return { aggregate: ["B"] };
};

const nodeC: GraphNode<typeof State> = (state) => {
  console.log(`Adding "C" to ${state.aggregate}`);
  return { aggregate: ["C"] };  // [!code highlight]
};

const conditionalEdge: ConditionalEdgeRouter<typeof State, "b" | "c"> = (state) => {
  // Fill in arbitrary logic here that uses the state
  // to determine the next node
  return state.which as "b" | "c";
};

const graph = new StateGraph(State)
  .addNode("a", nodeA)
  .addNode("b", nodeB)
  .addNode("c", nodeC)
  .addEdge(START, "a")
  .addEdge("b", END)
  .addEdge("c", END)
  .addConditionalEdges("a", conditionalEdge)
  .compile();
```

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import * as fs from "node:fs/promises";

const drawableGraph = await graph.getGraphAsync();
const image = await drawableGraph.drawMermaidPng();
const imageBuffer = new Uint8Array(await image.arrayBuffer());

await fs.writeFile("graph.png", imageBuffer);
```

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const result = await graph.invoke({ aggregate: [] });
console.log(result);
```

```
Adding "A" to []
Adding "C" to ['A']
{ aggregate: ['A', 'C'], which: 'c' }
```

<Tip>
  Your conditional edges can route to multiple destination nodes. For example:

  ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  const routeBcOrCd: ConditionalEdgeRouter<typeof State, "b" | "c" | "d"> = (state) => {
    if (state.which === "cd") {
      return ["c", "d"];
    }
    return ["b", "c"];
  };
  ```
</Tip>

## Map-Reduce and the send API

LangGraph supports map-reduce and other advanced branching patterns using the Send API. Here is an example of how to use it:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { StateGraph, StateSchema, ReducedValue, GraphNode, START, END, Send } from "@langchain/langgraph";
import * as z from "zod";

const OverallState = new StateSchema({
  topic: z.string(),
  subjects: z.array(z.string()),
  jokes: new ReducedValue(
    z.array(z.string()).default(() => []),
    { reducer: (x, y) => x.concat(y) }
  ),
  bestSelectedJoke: z.string(),
});

const generateTopics: GraphNode<typeof OverallState> = (state) => {
  return { subjects: ["lions", "elephants", "penguins"] };
};

const generateJoke: GraphNode<typeof OverallState> = (state) => {
  const jokeMap: Record<string, string> = {
    lions: "Why don't lions like fast food? Because they can't catch it!",
    elephants: "Why don't elephants use computers? They're afraid of the mouse!",
    penguins: "Why don't penguins like talking to strangers at parties? Because they find it hard to break the ice."
  };
  return { jokes: [jokeMap[state.subject]] };
};

const continueToJokes: ConditionalEdgeRouter<typeof OverallState, "generateJoke"> = (state) => {
  return state.subjects.map((subject) => new Send("generateJoke", { subject }));
};

const bestJoke: GraphNode<typeof OverallState> = (state) => {
  return { bestSelectedJoke: "penguins" };
};

const graph = new StateGraph(OverallState)
  .addNode("generateTopics", generateTopics)
  .addNode("generateJoke", generateJoke)
  .addNode("bestJoke", bestJoke)
  .addEdge(START, "generateTopics")
  .addConditionalEdges("generateTopics", continueToJokes)
  .addEdge("generateJoke", "bestJoke")
  .addEdge("bestJoke", END)
  .compile();
```

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import * as fs from "node:fs/promises";

const drawableGraph = await graph.getGraphAsync();
const image = await drawableGraph.drawMermaidPng();
const imageBuffer = new Uint8Array(await image.arrayBuffer());

await fs.writeFile("graph.png", imageBuffer);
```

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
// Call the graph: here we call it to generate a list of jokes
for await (const step of await graph.stream({ topic: "animals" })) {
  console.log(step);
}
```

```
{ generateTopics: { subjects: [ 'lions', 'elephants', 'penguins' ] } }
{ generateJoke: { jokes: [ "Why don't lions like fast food? Because they can't catch it!" ] } }
{ generateJoke: { jokes: [ "Why don't elephants use computers? They're afraid of the mouse!" ] } }
{ generateJoke: { jokes: [ "Why don't penguins like talking to strangers at parties? Because they find it hard to break the ice." ] } }
{ bestJoke: { bestSelectedJoke: 'penguins' } }
```

## Create and control loops

When creating a graph with a loop, we require a mechanism for terminating execution. This is most commonly done by adding a [conditional edge](/oss/javascript/langgraph/graph-api#conditional-edges) that routes to the [END](/oss/javascript/langgraph/graph-api#end-node) node once we reach some termination condition.

You can also set the graph recursion limit when invoking or streaming the graph. The recursion limit sets the number of [super-steps](/oss/javascript/langgraph/graph-api#graphs) that the graph is allowed to execute before it raises an error. Read more about the [recursion limit concept](/oss/javascript/langgraph/graph-api#recursion-limit).
