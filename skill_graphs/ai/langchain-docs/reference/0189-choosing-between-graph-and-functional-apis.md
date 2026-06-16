# Choosing between Graph and Functional APIs
Source: https://docs.langchain.com/oss/javascript/langgraph/choosing-apis

LangGraph provides two different APIs to build agent workflows: the **Graph API** and the **Functional API**. Both APIs share the same underlying runtime and can be used together in the same application, but they are designed for different use cases and development preferences.

This guide will help you understand when to use each API based on your specific requirements.

## Quick decision guide

Use the **Graph API** when you need:

* **Complex workflow visualization** for debugging and documentation
* **Explicit state management** with shared data across multiple nodes
* **Conditional branching** with multiple decision points
* **Parallel execution paths** that need to merge later
* **Team collaboration** where visual representation aids understanding

Use the **Functional API** when you want:

* **Minimal code changes** to existing procedural code
* **Standard control flow** (if/else, loops, function calls)
* **Function-scoped state** without explicit state management
* **Rapid prototyping** with less boilerplate
* **Linear workflows** with simple branching logic

## Detailed comparison

### When to use the Graph API

The [Graph API](/oss/javascript/langgraph/graph-api) uses a declarative approach where you define nodes, edges, and shared state to create a visual graph structure.

**1. Complex decision trees and branching logic**

When your workflow has multiple decision points that depend on various conditions, the Graph API makes these branches explicit and easy to visualize.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import * as z from "zod";
import {
  StateGraph,
  StateSchema,
  MessagesValue,
  START,
  END,
  type GraphNode,
  type ConditionalEdgeRouter,
} from "@langchain/langgraph";

// Graph API: Clear visualization of decision paths
const AgentState = new StateSchema({
  messages: MessagesValue,
  currentTool: z.string(),
  retryCount: z.number().default(0),
});

const shouldContinue: ConditionalEdgeRouter<typeof AgentState> = (state) => {
  if (state.retryCount > 3) {
    return END;
  } else if (state.currentTool === "search") {
    return "processSearch";
  } else {
    return "callLlm";
  }
};

const workflow = new StateGraph(AgentState)
  .addNode("callLlm", callLlmNode)
  .addNode("processSearch", searchNode)
  .addConditionalEdges("callLlm", shouldContinue);
```

**2. State management across multiple components**

When you need to share and coordinate state between different parts of your workflow, the Graph API's explicit state management is beneficial.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import * as z from "zod";
import { StateSchema, type GraphNode } from "@langchain/langgraph";

// Multiple nodes can access and modify shared state
const WorkflowState = new StateSchema({
  userInput: z.string(),
  searchResults: z.array(z.string()).default([]),
  generatedResponse: z.string().optional(),
  validationStatus: z.string().optional(),
});

const searchNode: GraphNode<typeof WorkflowState> = async (state) => {
  // Access shared state
  const results = await search(state.userInput);
  return { searchResults: results };
};

const validationNode: GraphNode<typeof WorkflowState> = async (state) => {
  // Access results from previous node
  const isValid = await validate(state.generatedResponse);
  return { validationStatus: isValid ? "valid" : "invalid" };
};
```

**3. Parallel processing with synchronization**

When you need to run multiple operations in parallel and then combine their results, the Graph API handles this naturally.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { START } from "@langchain/langgraph";

// Parallel processing of multiple data sources
workflow
  .addNode("fetchNews", fetchNews)
  .addNode("fetchWeather", fetchWeather)
  .addNode("fetchStocks", fetchStocks)
  .addNode("combineData", combineAllData)
  // All fetch operations run in parallel
  .addEdge(START, "fetchNews")
  .addEdge(START, "fetchWeather")
  .addEdge(START, "fetchStocks")
  // Combine waits for all parallel operations to complete
  .addEdge("fetchNews", "combineData")
  .addEdge("fetchWeather", "combineData")
  .addEdge("fetchStocks", "combineData");
```

**4. Team development and documentation**

The visual nature of the Graph API makes it easier for teams to understand, document, and maintain complex workflows.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
// Clear separation of concerns - each team member can work on different nodes
workflow
  .addNode("dataIngestion", dataTeamFunction)
  .addNode("mlProcessing", mlTeamFunction)
  .addNode("businessLogic", productTeamFunction)
  .addNode("outputFormatting", frontendTeamFunction);
```

### When to use the Functional API

The [Functional API](/oss/javascript/langgraph/functional-api) uses an imperative approach that integrates LangGraph features into standard procedural code.

**1. Existing procedural code**

When you have existing code that uses standard control flow and want to add LangGraph features with minimal refactoring.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { task, entrypoint } from "@langchain/langgraph";

// Functional API: Minimal changes to existing code
const processUserInput = task(
  "processUserInput",
  async (userInput: string) => {
    // Existing function with minimal changes
    return { processed: userInput.toLowerCase().trim() };
  }
);

const workflow = entrypoint(
  { checkpointer },
  async (userInput: string) => {
    // Standard control flow
    const processed = await processUserInput(userInput);

    let response: string;
    if (processed.processed.includes("urgent")) {
      response = await handleUrgentRequest(processed);
    } else {
      response = await handleNormalRequest(processed);
    }

    return response;
  }
);
```

**2. Linear workflows with simple logic**

When your workflow is primarily sequential with straightforward conditional logic.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { entrypoint, interrupt } from "@langchain/langgraph";

const essayWorkflow = entrypoint(
  { checkpointer },
  async (topic: string) => {
    // Linear flow with simple branching
    let outline = await createOutline(topic);

    if (outline.points.length < 3) {
      outline = await expandOutline(outline);
    }

    const draft = await writeDraft(outline);

    // Human review checkpoint
    const feedback = interrupt({ draft, action: "Please review" });

    let finalEssay: string;
    if (feedback === "approve") {
      finalEssay = draft;
    } else {
      finalEssay = await reviseEssay(draft, feedback);
    }

    return { essay: finalEssay };
  }
);
```

**3. Rapid prototyping**

When you want to quickly test ideas without the overhead of defining state schemas and graph structures.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { entrypoint } from "@langchain/langgraph";

const quickPrototype = entrypoint(
  { checkpointer },
  async (data: Record<string, unknown>) => {
    // Fast iteration - no state schema needed
    const step1Result = await processStep1(data);
    const step2Result = await processStep2(step1Result);

    return { finalResult: step2Result };
  }
);
```

**4. Function-scoped state management**

When your state is naturally scoped to individual functions and doesn't need to be shared broadly.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { task, entrypoint } from "@langchain/langgraph";

const analyzeDocument = task("analyzeDocument", async (document: string) => {
  // Local state management within function
  const sections = extractSections(document);
  const summaries = await Promise.all(sections.map(summarize));
  const keyPoints = extractKeyPoints(summaries);

  return {
    sections: sections.length,
    summaries,
    keyPoints,
  };
});

const documentProcessor = entrypoint(
  { checkpointer },
  async (document: string) => {
    const analysis = await analyzeDocument(document);
    // State is passed between functions as needed
    return await generateReport(analysis);
  }
);
```

## Combining both APIs

You can use both APIs together in the same application. This is useful when different parts of your system have different requirements.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import * as z from "zod";
import {
  StateGraph,
  StateSchema,
  entrypoint,
  type GraphNode,
} from "@langchain/langgraph";

// Define state for complex multi-agent coordination
const CoordinationState = new StateSchema({
  rawData: z.record(z.string(), z.unknown()),
  processedData: z.record(z.string(), z.unknown()).optional(),
});

// Simple data processing using Functional API
const dataProcessor = entrypoint({}, async (rawData: Record<string, unknown>) => {
  const cleaned = await cleanData(rawData);
  const transformed = await transformData(cleaned);
  return transformed;
});

// Use the functional API result in the graph
const orchestratorNode: GraphNode<typeof CoordinationState> = async (state) => {
  const processedData = await dataProcessor.invoke(state.rawData);
  return { processedData };
};

// Complex multi-agent coordination using Graph API
const coordinationGraph = new StateGraph(CoordinationState)
  .addNode("orchestrator", orchestratorNode)
  .addNode("agentA", agentANode)
  .addNode("agentB", agentBNode);
```

## Migration between APIs

### From Functional to Graph API

When your functional workflow grows complex, you can migrate to the Graph API:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import * as z from "zod";
import { entrypoint } from "@langchain/langgraph";

// Before: Functional API
const complexWorkflow = entrypoint(
  { checkpointer },
  async (inputData: Record<string, unknown>) => {
    const step1 = await processStep1(inputData);

    let result: unknown;
    if (step1.needsAnalysis) {
      const analysis = await analyzeData(step1);
      if (analysis.confidence > 0.8) {
        result = await highConfidencePath(analysis);
      } else {
        result = await lowConfidencePath(analysis);
      }
    } else {
      result = await simplePath(step1);
    }

    return result;
  }
);

// After: Graph API
import {
  StateGraph,
  StateSchema,
  type GraphNode,
  type ConditionalEdgeRouter,
} from "@langchain/langgraph";

const WorkflowState = new StateSchema({
  inputData: z.record(z.string(), z.unknown()),
  step1Result: z.record(z.string(), z.unknown()).optional(),
  analysis: z.record(z.string(), z.unknown()).optional(),
  finalResult: z.unknown().optional(),
});

const shouldAnalyze: ConditionalEdgeRouter<typeof WorkflowState> = (state) => {
  return state.step1Result?.needsAnalysis ? "analyze" : "simplePath";
};

const confidenceCheck: ConditionalEdgeRouter<typeof WorkflowState> = (state) => {
  return (state.analysis?.confidence as number) > 0.8
    ? "highConfidence"
    : "lowConfidence";
};

const workflow = new StateGraph(WorkflowState)
  .addNode("step1", processStep1Node)
  .addConditionalEdges("step1", shouldAnalyze)
  .addNode("analyze", analyzeDataNode)
  .addConditionalEdges("analyze", confidenceCheck);
// ... add remaining nodes and edges
```

### From Graph to Functional API

When your graph becomes overly complex for simple linear processes:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { z } from "zod/v4";
import { StateGraph, StateSchema, entrypoint } from "@langchain/langgraph";

// Before: Over-engineered Graph API
const SimpleState = new StateSchema({
  input: z.string(),
  step1: z.string().optional(),
  step2: z.string().optional(),
  result: z.string().optional(),
});

// After: Simplified Functional API
const simpleWorkflow = entrypoint(
  { checkpointer },
  async (inputData: string) => {
    const step1 = await processStep1(inputData);
    const step2 = await processStep2(step1);
    return await finalizeResult(step2);
  }
);
```

## Summary

Choose the **Graph API** when you need explicit control over workflow structure, complex branching, parallel processing, or team collaboration benefits.

Choose the **Functional API** when you want to add LangGraph features to existing code with minimal changes, have simple linear workflows, or need rapid prototyping capabilities.

Both APIs provide the same core LangGraph features (persistence, streaming, human-in-the-loop, memory) but package them in different paradigms to suit different development styles and use cases.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langgraph/choosing-apis.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# LangSmith Deployment
Source: https://docs.langchain.com/oss/javascript/langgraph/deploy

This guide shows you how to deploy your agent to **[LangSmith Cloud](/langsmith/deploy-to-cloud)**, a fully managed hosting platform designed for agent workloads. With Cloud deployment, you can deploy directly from your GitHub repository—LangSmith handles the infrastructure, scaling, and operational concerns.

Traditional hosting platforms are built for stateless, short-lived web applications. LangSmith Cloud is **purpose-built for stateful, long-running agents** that require persistent state and background execution.

<Tip>
  LangSmith offers multiple deployment options beyond Cloud, including [hybrid](/langsmith/hybrid), [standalone servers](/langsmith/deploy-standalone-server), and [self-hosted with control plane](/langsmith/deploy-with-control-plane). For more information, refer to the [Deployment overview](/langsmith/deployment).
</Tip>

## Prerequisites

Before you begin, ensure you have the following:

* A [GitHub account](https://github.com/)
* A [LangSmith account](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=oss-langgraph-deploy) (free to sign up)

## Deploy your agent

### 1. Create a repository on GitHub

Your application's code must reside in a GitHub repository to be deployed on LangSmith. Both public and private repositories are supported. For this quickstart, first make sure your app is LangGraph-compatible by following the [local server setup guide](/oss/javascript/langgraph/studio#set-up-local-agent-server). Then, push your code to the repository.

### 2. Deploy to LangSmith

<Steps>
  <Step title="Navigate to LangSmith Deployment">
    Log in to [LangSmith](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=oss-langgraph-deploy). In the left sidebar, select **Deployments**.
  </Step>

  <Step title="Create new deployment">
    Click the **+ New Deployment** button. A pane will open where you can fill in the required fields.
  </Step>

  <Step title="Link repository">
    If you are a first time user or adding a private repository that has not been previously connected, click the **Add new account** button and follow the instructions to connect your GitHub account.
  </Step>

  <Step title="Deploy repository">
    Select your application's repository. Click **Submit** to deploy. This may take about 15 minutes to complete. You can check the status in the **Deployment details** view.
  </Step>
</Steps>

### 3. Test your application in Studio

Once your application is deployed:

1. Select the deployment you just created to view more details.
2. Click the **Studio** button in the top right corner. Studio will open to display your graph.

### 4. Get the API URL for your deployment

1. In the **Deployment details** view in LangGraph, click the **API URL** to copy it to your clipboard.
2. Click the `URL` to copy it to the clipboard.

### 5. Test the API

You can now test the API:

<Tabs>
  <Tab title="TypeScript">
    1. Install LangGraph SDK:

    ```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    npm install @langchain/langgraph-sdk
    ```

    2. Send a message to the agent:

    ```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { Client } from "@langchain/langgraph-sdk";

    const client = new Client({ apiUrl: "your-deployment-url", apiKey: "your-langsmith-api-key" });

    const streamResponse = client.runs.stream(
      null,    // Threadless run
      "agent", // Name of agent. Defined in langgraph.json.
      {
        input: {
          "messages": [
            { "role": "user", "content": "What is LangGraph?"}
          ]
        },
        streamMode: "messages",
      }
    );

    for await (const chunk of streamResponse) {
      console.log(`Receiving new event of type: ${chunk.event}...`);
      console.log(JSON.stringify(chunk.data));
      console.log("\n\n");
    }
    ```
  </Tab>

  <Tab title="Rest API">
    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    curl -s --request POST \
        --url <DEPLOYMENT_URL>/runs/stream \
        --header 'Content-Type: application/json' \
        --header "X-Api-Key: <LANGSMITH API KEY> \
        --data "{
            \"assistant_id\": \"agent\", `# Name of agent. Defined in langgraph.json.`
            \"input\": {
                \"messages\": [
                    {
                        \"role\": \"human\",
                        \"content\": \"What is LangGraph?\"
                    }
                ]
            },
            \"stream_mode\": \"updates\"
        }"
    ```
  </Tab>
</Tabs>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langgraph/deploy.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Event streaming
Source: https://docs.langchain.com/oss/javascript/langgraph/event-streaming

Stream LangGraph runs with typed projections for messages, state, subgraphs, output, and extensions.

Event streaming is the recommended in-process streaming model for most LangGraph application code. It returns a run stream object that can be consumed in multiple ways at the same time.

## Quickstart

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const stream = await graph.streamEvents(
  { messages: [{ role: "user", content: "What is 42 * 17?" }] },
  { version: "v3" }
);

for await (const message of stream.messages) {
  for await (const token of message.text) {
    process.stdout.write(token);
  }
}

const finalState = await stream.output;
```

To stream against a graph deployed behind an Agent Server, see the [LangSmith Streaming API](/langsmith/streaming).

## How the pieces fit together

The streaming stack has two main layers:

1. **Streaming** emits raw graph execution events from the Pregel engine.
2. **Event streaming** normalizes those events, runs them through stream transformers, and exposes typed projections.

<div>
  <div>
    <div>
      <div>Pregel engine</div>
      <div>Runs graph steps</div>
    </div>

    <div>emits</div>

    <div>
      <div>Raw Pregel events</div>
      <div><code>updates</code>, <code>values</code>, <code>messages</code>, <code>custom</code>, <code>checkpoints</code>, <code>tasks</code>, <code>debug</code></div>
    </div>

    <div>sent to</div>

    <div>
      <div>Event router</div>
      <div>Routes each event through the transformer pipeline</div>
    </div>

    <div>cascades through</div>

    <div>
      <div>Stream transformers</div>

      <div>
        <div>ValuesTransformer</div>
        <div>MessagesTransformer</div>
        <div>...</div>
        <div>Custom transformers</div>
      </div>
    </div>

    <div>produces</div>

    <div>
      <div>Event Stream</div>
      <div>Projected events for application code</div>
    </div>
  </div>
</div>

The event router is the bridge between the two layers. It receives normalized Pregel events and passes each event through the registered stream transformers. Built-in transformers create standard projections such as `stream.messages`, `stream.values`, `stream.subgraphs`, and `stream.output`. Custom transformers can add application-specific projections under `stream.extensions`.

## What event streaming provides

The run stream exposes typed projections over one underlying event flow:

| Projection           | Use                                                |
| -------------------- | -------------------------------------------------- |
| `stream`             | Iterate every protocol event.                      |
| `stream.messages`    | Stream chat model messages and token deltas.       |
| `stream.values`      | Iterate state snapshots and await the final value. |
| `stream.output`      | Await the final output.                            |
| `stream.subgraphs`   | Discover and observe nested graph executions.      |
| `stream.interrupts`  | Inspect human-in-the-loop interrupt payloads.      |
| `stream.interrupted` | Check whether the run paused for human input.      |
| `stream.extensions`  | Consume custom stream transformer projections.     |

Multiple consumers can read these projections concurrently. Reading `stream.messages` does not consume events needed by `stream.values`, `stream.subgraphs`, or `stream.output`.

Event streaming sits one level above [streaming](/oss/javascript/langgraph/streaming), which exposes raw graph execution events through `stream_mode` modes such as `updates`, `values`, `messages`, `custom`, `checkpoints`, `tasks`, and `debug`. Use streaming when you need low-level access to those modes; use event streaming when application code benefits from typed projections.

## Stream messages

Use `stream.messages` for chat model output:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const stream = await graph.streamEvents(input, { version: "v3" });

for await (const message of stream.messages) {
  const text = await message.text;
  const usage = await message.usage;

  console.log(text);
  console.log(usage);
}
```

`message.text` is both an async iterable and a promise-like value. Iterate it for token-by-token output, or await it for the complete text.

## Stream subgraphs

Use `stream.subgraphs` to observe nested graph work without parsing namespace strings:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const stream = await graph.streamEvents(input, { version: "v3" });

for await (const subgraph of stream.subgraphs) {
  console.log(subgraph.name, subgraph.path);

  for await (const message of subgraph.messages) {
    console.log(await message.text);
  }
}
```

`subgraph.graph_name` is the `name` of the compiled graph or agent. A named agent dispatched from a tool (for example, a `create_agent(name=...)` invoked through the Deep Agents `task` tool) surfaces here under that name, and the `lifecycle` event that opens the scope carries a `cause` linking back to the dispatching tool call. See [Lifecycle](#lifecycle) for more information.

For product-specific streams, see [Deep Agents streaming](/oss/javascript/deepagents/event-streaming) for subagent streams and [LangChain agent streaming](/oss/javascript/langchain/streaming) for tool calls and middleware events.

## Stream state

Use `stream.values` to stream full state snapshots after each step:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const stream = await graph.streamEvents(input, { version: "v3" });

for await (const snapshot of stream.values) {
  console.log(snapshot);
}

const finalState = await stream.output;
```

## Stream multiple projections

Use concurrent consumers when you need multiple projections in JavaScript:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
await Promise.all([
  (async () => {
    for await (const message of stream.messages) {
      console.log(await message.text);
    }
  })(),
  (async () => {
    for await (const subgraph of stream.subgraphs) {
      console.log(subgraph.path);
    }
  })(),
]);
```

## Resume after an interrupt

When a graph pauses for human input, inspect `stream.interrupted` and `stream.interrupts`, then resume by calling `stream_events(..., version="v3")` again with `Command`.

Resume requires a graph compiled with a checkpointer and a config carrying a thread ID — see [persistence](/oss/javascript/langgraph/persistence).

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { Command } from "@langchain/langgraph";

let stream = await graph.streamEvents(input, { version: "v3" });

for await (const message of stream.messages) {
  console.log(await message.text);
}

if (stream.interrupted) {
  console.log(stream.interrupts);
}

stream = await graph.streamEvents(
  new Command({ resume: { decisions: [{ type: "approve" }] } }),
  { version: "v3" }
);
const finalState = await stream.output;
```

## Stream all protocol events

Use the run object itself when you want the raw protocol event stream:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const stream = await graph.streamEvents(
  { messages: [{ role: "user", content: "What is 42 * 17?" }] },
  { version: "v3" }
);

for await (const event of stream) {
  const namespace = event.params.namespace;
  console.log(namespace, event.method, event.params.data);
}
```

Each event is a `ProtocolEvent` envelope wrapping a channel-specific payload. The same shape is what a transformer's `process(event)` receives.

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
interface ProtocolEvent {
  readonly seq: number;         // strictly increasing within a run; use for ordering
  readonly method: string;      // channel name: "messages", "values", "updates", "custom", "tools", "lifecycle", ...
  readonly params: {
    readonly namespace: string[];  // path of "<name>:<runtime_id>" segments from the root graph; [] is the root
    readonly timestamp: number;    // wall-clock milliseconds; can drift, don't rely on for ordering
    readonly node?: string;        // graph node that emitted this event, when applicable
    readonly data: unknown;        // channel-specific payload; shape depends on `method`
  };
}
```

The `namespace` is a path from the root graph to the scope that emitted the event. The root is the empty array `[]`. Each child execution adds one `"name:runtime_id"` segment, so a nested tool call inside a subgraph looks like `["researcher:6f4d", "tools:91ac"]`. The name before `:` is the stable graph or node name; the suffix is a per-invocation runtime ID. Filter raw events by namespace yourself when you only care about a specific subtree — `stream.subgraphs` already does this for nested graph executions.

## Channels and event lifecycle

Raw events flow on channels. The channel name appears as the event's `method`; each channel emits a specific event shape.

| Channel         | Purpose                                                         |
| --------------- | --------------------------------------------------------------- |
| `values`        | Full graph state snapshots.                                     |
| `updates`       | Per-node state deltas.                                          |
| `messages`      | Content-block-centric chat model output.                        |
| `tools`         | Tool call start, streamed output, finish, and error events.     |
| `lifecycle`     | Run, subgraph, and subagent status changes.                     |
| `checkpoints`   | Lightweight checkpoint envelopes for branching and time travel. |
| `input`         | Human-in-the-loop input requests and responses.                 |
| `tasks`         | Pregel task creation and result events.                         |
| `custom`        | User-defined payloads from graph code.                          |
| `custom:<name>` | Application-defined stream transformer output.                  |

The typed projections (`stream.messages`, `stream.values`, etc.) are built from these channels. The channel name appears as the `method` field on raw events when you iterate the run object directly.

### Messages

The `messages` channel models output as content blocks. The data's `event` field is one of:

* `message-start`
* `content-block-start`
* `content-block-delta`
* `content-block-finish`
* `message-finish`

Content blocks have explicit boundaries: a block starts, emits zero or more deltas, and finishes before the next block in the same message starts. This makes token streaming, reasoning blocks, tool-call blocks, and multimodal content explicit without requiring provider-specific formats. `message-finish` may include token usage; unrecoverable model-call failures arrive as message error events.

To consume raw content-block events directly instead of using the `stream.messages` projection:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
for await (const event of stream) {
  if (event.method !== "messages") continue;

  const data = event.params.data;
  if (data.event !== "content-block-delta") continue;

  const block = data.delta ?? {};
  if (block.type === "text-delta") {
    process.stdout.write(block.text ?? "");
  } else if (block.type === "reasoning-delta") {
    process.stdout.write(`[thinking]${block.reasoning ?? ""}`);
  }
}
```

### Tools

The `tools` channel exposes tool execution. The data's `event` field is one of:

* `tool-started`
* `tool-output-delta`
* `tool-finished`
* `tool-error`

Tool events are correlated by tool call ID, so a tool execution can be joined back to its originating tool-call content block on the `messages` channel.

### Lifecycle

The `lifecycle` channel tracks root run, subgraph, and subagent status. The data's `event` field is one of:

* `started`
* `running`
* `completed`
* `failed`
* `interrupted`

Beyond `event`, lifecycle data may include an optional `graph_name`, `error`, and `cause` describing why a child scope started (parent tool call, fan-out send, edge transition).

## Build your own projection

Stream transformers are the projection layer in event streaming. They observe protocol events, keep their own state, and expose derived views of a run — things like tool activity, token totals, progress events, artifacts, or messages for another protocol. `StreamChannel` is the projection primitive transformers use to publish those views.

Built-in projections (`stream.messages`, `stream.values`, `stream.subgraphs`, `stream.output`) and product-specific projections (LangChain's `stream.tool_calls`, Deep Agents' `stream.subagents`) are themselves transformers using this same contract. User transformers stack on top via compile-time or call-time registration, and their projections appear under `stream.extensions`.

Write one when the existing projections don't match the shape an application needs.

### How transformers work

Event streaming starts with streaming output from the LangGraph Pregel engine. The runtime normalizes those chunks into protocol events, then a stream handler routes each event through a stack of stream transformers.

```mermaid theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
flowchart TD
    A[Pregel modes] --> B[Events]
    B --> C[Built-in projections]
    C --> D[User transformers]
    D --> E[Run projections]
```

The stream handler is the central dispatcher for one stream. For every protocol event, it:

1. Calls each registered transformer's `process(event)` hook in order.
2. Wires named `StreamChannel` pushes back onto the protocol event stream.
3. Stores the event in the run stream unless a transformer suppresses it.
4. Calls `finalize()` or `fail()` on every transformer when the run ends.

Transformers are observational. They do not call back into the graph runtime. Instead, they consume events and push derived values into `StreamChannel`, promises, or other projection objects.

### Transformer shape

A transformer implements the `StreamTransformer` interface:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
interface StreamTransformer<TProjection = unknown> {
  init(): TProjection;
  process(event: ProtocolEvent): boolean;
  finalize?(): void | PromiseLike<void>;
  fail?(err: unknown): void;
}
```

* `init()` creates the projection object. User transformer projections appear under `stream.extensions`.
* `process()` observes each protocol event. See [Stream all protocol events](#stream-all-protocol-events) for the `ProtocolEvent` shape. Return `false` only when you intentionally want to suppress the original event.
* `finalize()` closes or resolves non-channel projections after a successful stream.
* `fail()` propagates errors to non-channel projections.

### Declaring required stream modes

`required_stream_modes` controls which Pregel stream modes the underlying graph emits during the stream. The runtime takes the union of every registered transformer's `required_stream_modes` and passes that union as the `stream_mode` argument to the graph's `.stream()` call. **Modes that no transformer requests are never emitted** — declaring `("custom",)` is what causes `custom` events to flow through the run at all.

`process()` receives every event the graph emits and is responsible for filtering by `event["method"]`. The declaration turns on upstream emission; it does not narrow what `process()` sees. Valid values are the Pregel stream modes: `"messages"`, `"tools"`, `"custom"`, `"values"`, `"updates"`, `"checkpoints"`, `"tasks"`, `"debug"`. Each transformer must declare every mode it acts on — an omitted mode is not emitted by the graph and never reaches `process()`.

### StreamChannel

`StreamChannel` is the projection primitive a transformer uses for streaming values. It always exposes an iterable stream on `stream.extensions.<name>`. The constructor argument decides whether each `push()` also flows into the run's main event stream as a `custom:<name>` event—that is, whether the projection's values show up when iterating raw protocol events.

| Need                                           | Use                          |
| ---------------------------------------------- | ---------------------------- |
| Side-channel projection only                   | `new StreamChannel<T>()`     |
| Also flow each push into the main event stream | `new StreamChannel<T>(name)` |

Named channel payloads must be serializable, because each pushed value also becomes a `custom:<name>` protocol event in the main stream. Keep promises, async iterables, class instances, and other in-process handles in unnamed channels.

The stream handler owns channel lifecycle. Once `init()` returns a channel, the handler closes or fails it for you when the run ends. Transformers only push values.

### Example: named channel

Pass a string name to `StreamChannel` to expose a streaming projection through `stream.extensions` *and* forward each pushed value into the run's main event stream as a `custom:<name>` protocol event:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { StreamChannel } from "@langchain/langgraph";

const toolActivityTransformer = () => {
  const activity = new StreamChannel<{
    name: string;
    status: "started" | "finished" | "error";
  }>("toolActivity");

  return {
    init: () => ({ toolActivity: activity }),
    process(event) {
      if (event.method === "tools") {
        const data = event.params.data as { tool_name?: string; event?: string };
        if (data.tool_name && data.event) {
          activity.push({
            name: data.tool_name,
            status: data.event === "tool-error" ? "error" : "started",
          });
        }
      }
      return true;
    },
  };
};
```

### Example: unnamed channel

Without a name, the channel is a side-channel projection only — accessible on `stream.extensions` but not visible to consumers iterating raw events. This is the right choice for projections that hold in-process handles (promises, async iterables, class instances) that can't be serialized onto the main event stream.

The example below pairs an unnamed channel with `get_stream_writer`, which lets graph nodes emit `custom`-channel events that the transformer then drains into the projection:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { StreamChannel } from "@langchain/langgraph";

const customTransformer = () => {
  const custom = new StreamChannel<unknown>();

  return {
    init: () => ({ custom }),
    process(event) {
      if (event.method === "custom") {
        custom.push(event.params.data);
      }
      return true;
    },
  };
};
```

### Example: final-value projection

Use unnamed streams, promises, or other in-process objects when the projection should not flow into the main event stream:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const statsTransformer = () => {
  let totalTokens = 0;
  let resolveTotal!: (value: number) => void;
  const totalTokensPromise = new Promise<number>((resolve) => {
    resolveTotal = resolve;
  });

  return {
    init: () => ({ totalTokens: totalTokensPromise }),
    process(event) {
      if (event.method === "messages") {
        const data = event.params.data as { usage?: { output_tokens?: number } };
        totalTokens += data.usage?.output_tokens ?? 0;
      }
      return true;
    },
    finalize: () => resolveTotal(totalTokens),
  };
};
```

### Register at call time or compile time

Pass transformers at call time for local experimentation:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const stream = await graph.streamEvents(input, {
  version: "v3",
  transformers: [statsTransformer, toolActivityTransformer],
});
```

Compile transformers into the graph when every run of that graph should produce the projection:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const graph = builder.compile({
  transformers: [statsTransformer, toolActivityTransformer],
});
```

### Built-in: `ToolCallTransformer`

## Related

LangGraph defines the streaming primitives. For using streaming with LangChain or Deep Agents, review the relevant product docs:

* [LangChain agent streaming](/oss/javascript/langchain/event-streaming) covers ReAct-style agent messages, tool calls, and middleware updates.
* [Deep Agents streaming](/oss/javascript/deepagents/event-streaming) covers subagents, nested messages, and subagent tool calls.
* [LangChain frontend patterns](/oss/javascript/langchain/frontend/overview) and [LangGraph frontend patterns](/oss/javascript/langgraph/frontend/overview) show UI use cases built on top of streamed state.
* [LangSmith Streaming API](/langsmith/streaming) covers streaming against a graph deployed behind an Agent Server.

The wire-level event and command formats are defined in the [Agent Protocol](https://github.com/langchain-ai/agent-protocol) repository and consumable as [`langchain-protocol`](https://pypi.org/project/langchain-protocol/) on PyPI and [`@langchain/protocol`](https://www.npmjs.com/package/@langchain/protocol) on npm.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langgraph/event-streaming.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
