# Graph execution
Source: https://docs.langchain.com/oss/javascript/langgraph/frontend/graph-execution

Visualize multi-step graph pipelines with per-node status and streaming content

LangGraph agents aren't black boxes. Every graph is composed of **named nodes**
that execute in sequence or in parallel: classify, research, analyze,
synthesize. Graph execution cards make this pipeline visible by rendering a card
for each node, showing its status, streaming its content in real time, and
tracking completion across the entire workflow. Users see exactly what the agent
is doing, which step it's on, and what each step produced.

This pattern is especially useful for production agents because it turns graph
structure into product UX. Instead of treating the run as a single assistant
response, you can expose the same checkpoints, node names, state keys, and
stream metadata that LangGraph uses internally.

<PatternEmbed />

## How graph nodes map to UI cards

A LangGraph graph defines a series of nodes, each responsible for a specific
task. For example, a research pipeline might have:

1. **Classify**: categorize the user's query
2. **Research**: gather relevant information
3. **Analyze**: draw conclusions from the research
4. **Synthesize**: produce a final, polished response

Each node writes its output to a specific key in the graph's state. On the
frontend, you don't need to hardcode that mapping as [`useStream`](https://reference.langchain.com/javascript/langchain-react/index/useStream) discovers
each node as it runs via `stream.subgraphs` and exposes a
[`SubgraphDiscoverySnapshot`](https://reference.langchain.com/javascript/langchain-react/SubgraphDiscoverySnapshot) for every observed step:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
// Nodes are discovered automatically — no hardcoded list needed
const graphNodes = [...stream.subgraphs.values()];

// Each snapshot carries the node name and current status
graphNodes.forEach((node) => {
  console.log(node.nodeName, node.status); // "classify", "running"
});
```

Use `node.nodeName` for labels in the progress bar and card headers. Pass each
snapshot to `useMessages(stream, node)` to render node-scoped streaming content
without coupling the UI to graph state key names.

This mapping becomes the contract between your graph and your UI. Backend
authors can add, rename, or reorder nodes intentionally, while frontend authors
decide how each state key should be visualized: a status badge, markdown panel,
table, chart, trace view, or approval card.

## Setting up `useStream`

Wire up [`useStream`](https://reference.langchain.com/javascript/langchain-react/index/useStream) as usual. The key properties you'll use are `messages`
(for the conversation) and `subgraphs` (for the graph nodes discovered in the
current run). Pass each discovered subgraph snapshot to a selector to read the
messages scoped to that node.

<Info>
  The code examples use `useStream<typeof myAgent>` for type-safe stream state. See Type inference for [Python](/oss/python/langchain/frontend/overview#type-inference) or [JavaScript](/oss/javascript/langchain/frontend/overview#type-inference) backends.
</Info>

<CodeGroup>
  ```tsx React theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { useStream } from "@langchain/react";

  const AGENT_URL = "http://localhost:2024";

  export function PipelineChat() {
    const stream = useStream<typeof myAgent>({
      apiUrl: AGENT_URL,
      assistantId: "graph_execution_cards",
    });
    const graphNodes = [...stream.subgraphs.values()];

    return (
      <div>
        <PipelineProgress nodes={graphNodes} isLoading={stream.isLoading} />
        <NodeCardList nodes={graphNodes} stream={stream} isLoading={stream.isLoading} />
      </div>
    );
  }
  ```

  ```vue Vue theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  <script setup lang="ts">
  import { useStream } from "@langchain/vue";

  const AGENT_URL = "http://localhost:2024";

  const stream = useStream<typeof myAgent>({
    apiUrl: AGENT_URL,
    assistantId: "graph_execution_cards",
  });
  </script>

  <template>
    <div>
      <PipelineProgress
        :nodes="[...stream.subgraphs.value.values()]"
        :is-loading="stream.isLoading.value"
      />
      <NodeCardList
        :nodes="[...stream.subgraphs.value.values()]"
        :stream="stream"
        :is-loading="stream.isLoading.value"
      />
    </div>
  </template>
  ```

  ```svelte Svelte theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  <script lang="ts">
    import { useStream } from "@langchain/svelte";

    const AGENT_URL = "http://localhost:2024";

    const stream = useStream<typeof myAgent>({
      apiUrl: AGENT_URL,
      assistantId: "graph_execution_cards",
    });
  </script>

  <div>
    <PipelineProgress nodes={[...stream.subgraphs.values()]} isLoading={stream.isLoading} />
    <NodeCardList
      nodes={[...stream.subgraphs.values()]}
      {stream}
      isLoading={stream.isLoading}
    />
  </div>
  ```

  ```ts Angular theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { Component, computed } from "@angular/core";
  import { injectStream } from "@langchain/angular";

  const AGENT_URL = "http://localhost:2024";

  @Component({
    selector: "app-pipeline-chat",
    template: `
      <div>
        <app-pipeline-progress
          [nodes]="graphNodes()"
          [isLoading]="stream.isLoading()"
        />
        <app-node-card-list
          [nodes]="graphNodes()"
          [stream]="stream"
          [isLoading]="stream.isLoading()"
        />
      </div>
    `,
  })
  export class PipelineChatComponent {
    stream = injectStream<typeof myAgent>({
      apiUrl: AGENT_URL,
      assistantId: "graph_execution_cards",
    });

    graphNodes = computed(() => [...this.stream.subgraphs().values()]);
  }
  ```
</CodeGroup>

## Routing streaming tokens to nodes

As the graph streams, each discovered subgraph snapshot identifies the node it
belongs to. Pass that snapshot to a selector hook or composable to read the
messages scoped to that node:

```tsx theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { AIMessage } from "langchain";
import { useMessages, type AnyStream, type SubgraphDiscoverySnapshot } from "@langchain/react";

function NodeCard({
  node,
  stream,
}: {
  node: SubgraphDiscoverySnapshot;
  stream: AnyStream;
}) {
  const messages = useMessages(stream, node);
  const lastAIMessage = messages.find(AIMessage.isInstance);
  const streamingContent = lastAIMessage?.text ?? "";

  return <NodeCardBody node={node} content={streamingContent} />;
}
```

The first mounted selector opens a scoped subscription for that node namespace.
When the node card unmounts, the subscription is released automatically.

## Determining node status

Each discovered node carries its current status. Use `node.status` directly;
the discovery snapshot reports `"pending"`, `"running"`, `"complete"`, or
`"error"`:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
type NodeStatus = SubgraphDiscoverySnapshot["status"];

const status: NodeStatus = node.status;
```

## Building the pipeline progress bar

A horizontal progress bar at the top gives users a bird's-eye view of the
entire pipeline. Each step is a labeled segment that fills in as nodes complete:

```tsx theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
function PipelineProgress({
  nodes,
  isLoading,
}: {
  nodes: SubgraphDiscoverySnapshot[];
  isLoading: boolean;
}) {
  const firstIncompleteIdx = nodes.findIndex((node) => node.status !== "complete");

  return (
    <div className="flex items-center gap-1">
      {nodes.map((node, i) => {
        const isRunning =
          isLoading && node.status !== "complete" && firstIncompleteIdx === i;
        const colors = {
          pending: "bg-gray-200 text-gray-500",
          running: "bg-blue-400 text-white animate-pulse",
          complete: "bg-green-500 text-white",
          error: "bg-red-500 text-white",
        };
        const status = isRunning ? "running" : node.status;

        return (
          <div key={node.id} className="flex items-center">
            <div
              className={`rounded-full px-3 py-1 text-xs font-medium ${colors[status]}`}
            >
              {node.nodeName}
            </div>
            {i < nodes.length - 1 && (
              <div
                className={`mx-1 h-0.5 w-6 ${
                  status === "complete" ? "bg-green-500" : "bg-gray-200"
                }`}
              />
            )}
          </div>
        );
      })}
    </div>
  );
}
```

## Building collapsible NodeCard components

Each node gets its own card that shows the status badge, content (streaming or
final), and a collapsible body for long outputs:

```tsx theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
function NodeCard({
  node,
  stream,
}: {
  node: SubgraphDiscoverySnapshot;
  stream: AnyStream;
}) {
  const [open, setOpen] = useState(node.status === "running");
  const messages = useMessages(stream, node);
  const lastAIMessage = messages.find(AIMessage.isInstance);

  useEffect(() => {
    if (node.status === "running") setOpen(true);
    if (node.status === "complete") setOpen(false);
  }, [node.status]);

  return (
    <div className="rounded-lg border bg-white shadow-sm">
      <button
        onClick={() => setOpen(!open)}
        className="flex w-full items-center justify-between p-4"
      >
        <div className="flex items-center gap-3">
          <h3 className="font-semibold">{node.nodeName}</h3>
          <StatusBadge status={node.status} />
        </div>
        <span className={open ? "rotate-90" : ""}>▶</span>
      </button>

      {open && (
        <div className="border-t px-4 py-3">
          <div className="prose prose-sm max-w-none">
            {lastAIMessage?.text?.trim()
              ? <Markdown>{lastAIMessage.text}</Markdown>
              : <p className="italic text-gray-500">Processing...</p>}
          </div>
        </div>
      )}
    </div>
  );
}
```

## Streaming vs. completed content

The node card reads scoped messages for both streaming and final content. This
avoids assuming that a graph node name matches the state key it writes to (for
example, `do_research` writes to `research` in the playground graph):

| Source                      | When to use                                                                            |
| --------------------------- | -------------------------------------------------------------------------------------- |
| `useMessages(stream, node)` | Render node-scoped streaming and final messages                                        |
| `stream.values`             | Read whole-graph state such as the final `synthesis` field, using the actual state key |

The pattern is: show the most recent scoped AI message in the node card, and
use `stream.values` only when you intentionally need a graph state field.

Because scoped messages are tied to the producing node, the UI can support
parallel graph paths without guessing from message order. Each card updates from
the stream events that belong to its node, and completed values remain available
through `stream.values`.

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
function NodeContent({ stream, node }: { stream: AnyStream; node: SubgraphDiscoverySnapshot }) {
  const messages = useMessages(stream, node);
  const content = messages.find(AIMessage.isInstance)?.text ?? "";

  return <Markdown>{content}</Markdown>;
}
```

<Tip>
  Streaming content may include partial tokens or markdown that hasn't been
  fully formed yet. If you render markdown, make sure your renderer handles
  incomplete syntax gracefully (e.g., an unclosed bold marker `**`).
</Tip>

## Putting it all together

Here's the full card list that combines routing, status detection, and card
rendering:

```tsx theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
function NodeCardList({
  nodes,
  stream,
  isLoading,
}: {
  nodes: SubgraphDiscoverySnapshot[];
  stream: AnyStream;
  isLoading: boolean;
}) {
  const firstIncompleteIdx = nodes.findIndex((node) => node.status !== "complete");

  return (
    <div className="space-y-3">
      {nodes.map((node, i) => {
        const isComplete = node.status === "complete";
        const isRunning = isLoading && !isComplete && firstIncompleteIdx === i;
        if (!isComplete && !isRunning) return null;

        return <NodeCard key={node.id} node={node} stream={stream} />;
      })}
    </div>
  );
}
```

## Use cases

Graph execution cards work well for any multi-step pipeline where visibility
matters:

* **Research pipelines**: classify → gather sources → analyze → synthesize a
  report
* **Content generation**: outline → draft → fact-check → edit → publish
* **Data processing**: ingest → validate → transform → aggregate → export
* **Code generation**: understand requirements → plan architecture → write
  code → review → test
* **Decision workflows**: gather context → evaluate options → score
  alternatives → recommend

## Handling dynamic pipelines

Not all graphs have a fixed set of nodes. Some pipelines add or skip nodes
based on the input. The discovery map contains only nodes observed for the
current thread:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const activeNodes = [...stream.subgraphs.values()];
```

This ensures your UI only shows cards for nodes that are relevant to the
current execution, avoiding empty placeholder cards.

<Info>
  If your graph has conditional branching (e.g., skip "Research" for simple
  factual queries), skipped nodes will not appear in `stream.subgraphs`. Your
  pipeline progress bar can render discovered nodes only or dim expected nodes
  that have no matching snapshot.
</Info>

## Best practices

* **Discover nodes from the stream**. Render cards from `stream.subgraphs`
  rather than hardcoding expected nodes; conditional or skipped steps won't
  appear until they run.
* **Treat state keys as UI contracts**. Decide which graph outputs should be
  stable enough for the frontend to render, and keep those keys documented next
  to the graph definition.
* **Use scoped messages for node cards**. They work while a node is streaming
  and after it completes, without coupling UI cards to state key names.
* **Auto-collapse completed nodes**. In long pipelines, auto-collapse finished
  cards so users can focus on the currently active step.
* **Show estimated timing**. If you have historical data on how long each node
  takes, display a time estimate to set user expectations.
* **Add a global progress indicator**. Complement per-node cards with an
  overall progress bar (e.g., "Step 2 of 4") at the top of the pipeline view.
* **Handle errors per node**. If a node fails, show the error in its card
  without collapsing the entire pipeline. Other nodes may still complete
  successfully.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langgraph/frontend/graph-execution.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Overview
Source: https://docs.langchain.com/oss/javascript/langgraph/frontend/overview

Render LangGraph agents to the frontend

Build frontends that visualize LangGraph pipelines in real time. These patterns
show how to render multi-step graph execution with per-node status and streaming
content from custom `StateGraph` workflows.

LangGraph's frontend advantage is that the UI can follow the same structure as
the graph. Nodes, state keys, checkpoints, interrupts, subgraphs, and streamed
messages are all visible runtime concepts, so you can build interfaces that
explain what the system is doing instead of hiding execution behind one
assistant message.

<Note>
  These patterns use the v1 frontend SDK packages. If you are using an earlier version, see the migration guides for [React](https://github.com/langchain-ai/langgraphjs/blob/main/libs/sdk-react/docs/v1-migration.md), [Vue](https://github.com/langchain-ai/langgraphjs/blob/main/libs/sdk-vue/docs/v1-migration.md), [Svelte](https://github.com/langchain-ai/langgraphjs/blob/main/libs/sdk-svelte/docs/v1-migration.md), and [Angular](https://github.com/langchain-ai/langgraphjs/blob/main/libs/sdk-angular/docs/v1-migration.md).
</Note>

## Architecture

LangGraph graphs are composed of named nodes connected by edges. Each node executes a step (classify, research, analyze, synthesize) and writes output to a specific state key. On the frontend, the SDK stream handle provides reactive access to node outputs, streaming tokens, and discovered subgraphs so you can map each node to a UI card.

```mermaid theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
%%{
  init: {
    "fontFamily": "monospace",
    "flowchart": {
      "curve": "curve"
    }
  }
}%%
graph LR
  FRONTEND["useStream()"]
  GRAPH["StateGraph"]
  N1["Node A"]
  N2["Node B"]
  N3["Node C"]

  GRAPH --"stream"--> FRONTEND
  FRONTEND --"submit"--> GRAPH
  GRAPH --> N1
  N1 --> N2
  N2 --> N3

  classDef blueHighlight fill:#DBEAFE,stroke:#2563EB,color:#1E3A8A;
  classDef greenHighlight fill:#DCFCE7,stroke:#16A34A,color:#14532D;
  classDef orangeHighlight fill:#FEF3C7,stroke:#D97706,color:#92400E;
  class FRONTEND blueHighlight;
  class GRAPH greenHighlight;
  class N1,N2,N3 orangeHighlight;
```

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { Annotation, MessagesAnnotation, StateGraph, START, END } from "@langchain/langgraph";

const State = Annotation.Root({
  ...MessagesAnnotation.spec,
  classification: Annotation<string>(),
  research: Annotation<string>(),
  analysis: Annotation<string>(),
  synthesis: Annotation<string>(),
});

const graph = new StateGraph(State)
  .addNode("classify", classifyNode)
  .addNode("do_research", researchNode)
  .addNode("analyze", analyzeNode)
  .addNode("synthesize", synthesizeNode)
  .addEdge(START, "classify")
  .addEdge("classify", "do_research")
  .addEdge("do_research", "analyze")
  .addEdge("analyze", "synthesize")
  .addEdge("synthesize", END)
  .compile();
```

On the frontend, [`useStream`](https://reference.langchain.com/javascript/langchain-react/index/useStream) exposes `stream.subgraphs` for graph-node discovery
and selector helpers such as `useMessages(stream, node)` for node-scoped
streaming content. `stream.values` still holds the full graph state when you
need fields such as the final `synthesis`. Angular uses the same stream API
shape through [`injectStream`](https://reference.langchain.com/javascript/langchain-angular/injectStream).

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { useStream } from "@langchain/react";

function Pipeline() {
  const stream = useStream<typeof graph>({
    apiUrl: "http://localhost:2024",
    assistantId: "pipeline",
  });

  const classification = stream.values?.classification;
  const research = stream.values?.research;
  const analysis = stream.values?.analysis;
  const graphNodes = [...stream.subgraphs.values()];
}
```

## What makes this different from a chat stream

Custom graphs often power product workflows: research pipelines, approval flows,
data pipelines, data enrichment, code review, planning, and multi-step analysis. The
frontend SDK lets you render these workflows using graph-native signals:

| Runtime concept        | Frontend UX                                                                                            |
| ---------------------- | ------------------------------------------------------------------------------------------------------ |
| **Named nodes**        | One card, timeline step, or status badge per graph node.                                               |
| **State keys**         | Dedicated UI regions for typed outputs such as classification, sources, analysis, and final synthesis. |
| **Streaming metadata** | Route partial messages to the node that produced them.                                                 |
| **Checkpoints**        | Inspect or resume from prior graph states for debugging and auditability.                              |
| **Interrupts**         | Pause a node for human input, approval, or correction, then continue.                                  |
| **Subgraphs**          | Reveal nested execution only when the user needs more detail.                                          |

Because the SDK exposes these concepts directly, you can scale from a simple
chat panel to a full workflow debugger without changing the backend protocol.

## Patterns

<CardGroup>
  <Card title="Graph execution" icon="chart-dots" href="/oss/javascript/langgraph/frontend/graph-execution">
    Visualize multi-step graph pipelines with per-node status and streaming content.
  </Card>

  <Card title="Custom stream channels" icon="broadcast" href="/oss/javascript/langgraph/frontend/custom-stream-channels">
    Stream custom server-side data to the frontend and read it with `useExtension` and `useChannel`.
  </Card>
</CardGroup>

## Related patterns

The [LangChain frontend patterns](/oss/javascript/langchain/frontend/overview)—markdown messages, tool calling, human-in-the-loop, resumable streams, and time travel—work with any LangGraph graph. The stream API provides the same core data model whether you use `createAgent`, `createDeepAgent`, or a custom `StateGraph`.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langgraph/frontend/overview.md) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Functional API overview
Source: https://docs.langchain.com/oss/javascript/langgraph/functional-api

The **Functional API** allows you to add LangGraph's key features ([persistence](/oss/javascript/langgraph/persistence), [memory](/oss/javascript/langgraph/add-memory), [human-in-the-loop](/oss/javascript/langgraph/interrupts), and [streaming](/oss/javascript/langgraph/streaming)) to your applications with minimal changes to your existing code.

It is designed to integrate these features into existing code that may use standard language primitives for branching and control flow, such as `if` statements, `for` loops, and function calls. Unlike many data orchestration frameworks that require restructuring code into an explicit pipeline or DAG, the Functional API allows you to incorporate these capabilities without enforcing a rigid execution model.

The Functional API uses two key building blocks:

* **`entrypoint`**: An entrypoint encapsulates workflow logic and manages execution flow, including handling long-running tasks and interrupts.
* **`task`**: Represents a discrete unit of work, such as an API call or data processing step, that can be executed asynchronously within an entrypoint. Tasks return a future-like object that can be awaited or resolved synchronously.

This provides a minimal abstraction for building workflows with state management and streaming.

<Tip>
  For information on how to use the functional API, see [Use Functional API](/oss/javascript/langgraph/use-functional-api).
</Tip>

## Functional API vs. Graph API

For users who prefer a more declarative approach, LangGraph's [Graph API](/oss/javascript/langgraph/graph-api) allows you to define workflows using a Graph paradigm. Both APIs share the same underlying runtime, so you can use them together in the same application.

Here are some key differences:

* **Control flow**: The Functional API does not require thinking about graph structure. You can use standard Python constructs to define workflows. This will usually trim the amount of code you need to write.
* **Short-term memory**: The **GraphAPI** requires declaring a [**State**](/oss/javascript/langgraph/graph-api#state) and may require defining [**reducers**](/oss/javascript/langgraph/graph-api#reducers) to manage updates to the graph state. `@entrypoint` and `@tasks` do not require explicit state management as their state is scoped to the function and is not shared across functions.
* **Checkpointing**: Both APIs generate and use checkpoints. In the **Graph API** a new checkpoint is generated after every [superstep](/oss/javascript/langgraph/graph-api). In the **Functional API**, when tasks are executed, their results are saved to an existing checkpoint associated with the given entrypoint instead of creating a new checkpoint.
* **Visualization**: The Graph API makes it easy to visualize the workflow as a graph which can be useful for debugging, understanding the workflow, and sharing with others. The Functional API does not support visualization as the graph is dynamically generated during runtime.

## Example

Below we demonstrate a simple application that writes an essay and [interrupts](/oss/javascript/langgraph/interrupts) to request human review.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { MemorySaver, entrypoint, task, interrupt } from "@langchain/langgraph";

const writeEssay = task("writeEssay", async (topic: string) => {
  // A placeholder for a long-running task.
  await new Promise((resolve) => setTimeout(resolve, 1000));
  return `An essay about topic: ${topic}`;
});

const workflow = entrypoint(
  { checkpointer: new MemorySaver(), name: "workflow" },
  async (topic: string) => {
    const essay = await writeEssay(topic);
    const isApproved = interrupt({
      // Any json-serializable payload provided to interrupt as argument.
      // It will be surfaced on the client side as an Interrupt when streaming data
      // from the workflow.
      essay, // The essay we want reviewed.
      // We can add any additional information that we need.
      // For example, introduce a key called "action" with some instructions.
      action: "Please approve/reject the essay",
    });

    return {
      essay, // The essay that was generated
      isApproved, // Response from HIL
    };
  }
);
```

<Accordion title="Detailed Explanation">
  This workflow will write an essay about the topic "cat" and then pause to get a review from a human. The workflow can be interrupted for an indefinite amount of time until a review is provided.

  When the workflow is resumed, it executes from the very start, but because the result of the `writeEssay` task was already saved, the task result will be loaded from the checkpoint instead of being recomputed.

  ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { v7 as uuid7 } from "uuid";
  import { MemorySaver, entrypoint, task, interrupt } from "@langchain/langgraph";

  const writeEssay = task("writeEssay", async (topic: string) => {
    // This is a placeholder for a long-running task.
    await new Promise(resolve => setTimeout(resolve, 1000));
    return `An essay about topic: ${topic}`;
  });

  const workflow = entrypoint(
    { checkpointer: new MemorySaver(), name: "workflow" },
    async (topic: string) => {
      const essay = await writeEssay(topic);
      const isApproved = interrupt({
        // Any json-serializable payload provided to interrupt as argument.
        // It will be surfaced on the client side as an Interrupt when streaming data
        // from the workflow.
        essay, // The essay we want reviewed.
        // We can add any additional information that we need.
        // For example, introduce a key called "action" with some instructions.
        action: "Please approve/reject the essay",
      });

      return {
        essay, // The essay that was generated
        isApproved, // Response from HIL
      };
    }
  );

  const threadId = uuid7();

  const config = {
    configurable: {
      thread_id: threadId
    }
  };

  for await (const item of workflow.stream("cat", config)) {
    console.log(item);
  }
  ```

  ```console theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  { writeEssay: 'An essay about topic: cat' }
  {
    __interrupt__: [{
      value: { essay: 'An essay about topic: cat', action: 'Please approve/reject the essay' },
      resumable: true,
      ns: ['workflow:f7b8508b-21c0-8b4c-5958-4e8de74d2684'],
      when: 'during'
    }]
  }
  ```

  An essay has been written and is ready for review. Once the review is provided, we can resume the workflow:

  ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { Command } from "@langchain/langgraph";

  // Get review from a user (e.g., via a UI)
  // In this case, we're using a bool, but this can be any json-serializable value.
  const humanReview = true;

  const stream = await workflow.stream(
    new Command({ resume: humanReview }),
    config
  );
  for await (const item of stream) {
    console.log(item);
  }
  ```

  ```console theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  { workflow: { essay: 'An essay about topic: cat', isApproved: true } }
  ```

  The workflow has been completed and the review has been added to the essay.
</Accordion>

## Entrypoint

The [`entrypoint`](https://reference.langchain.com/javascript/langchain-langgraph/index/entrypoint) function can be used to create a workflow from a function. It encapsulates workflow logic and manages execution flow, including handling *long-running tasks* and [interrupts](/oss/javascript/langgraph/interrupts).

### Definition

An **entrypoint** is defined by calling the `entrypoint` function with configuration and a function.

The function **must accept a single positional argument**, which serves as the workflow input. If you need to pass multiple pieces of data, use an object as the input type for the first argument.

Creating an entrypoint with a function produces a workflow instance which helps to manage the execution of the workflow (e.g., handles streaming, resumption, and checkpointing).

You will often want to pass a **checkpointer** to the `entrypoint` function to enable persistence and use features like **human-in-the-loop**.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { entrypoint } from "@langchain/langgraph";

const myWorkflow = entrypoint(
  { checkpointer, name: "workflow" },
  async (someInput: Record<string, any>): Promise<number> => {
    // some logic that may involve long-running tasks like API calls,
    // and may be interrupted for human-in-the-loop
    return result;
  }
);
```

<Warning>
  **Serialization**
  The **inputs** and **outputs** of entrypoints must be JSON-serializable to support checkpointing. Please see the [serialization](#serialization) section for more details.
</Warning>

### Executing

Using the [`entrypoint`](#entrypoint) function will return an object that can be executed using the `invoke` and `stream` methods.

<Tabs>
  <Tab title="Invoke">
    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    const config = {
      configurable: {
        thread_id: "some_thread_id"
      }
    };
    await myWorkflow.invoke(someInput, config); // Wait for the result
    ```
  </Tab>

  <Tab title="Stream">
    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    const config = {
      configurable: {
        thread_id: "some_thread_id"
      }
    };

    for await (const chunk of myWorkflow.stream(someInput, config)) {
      console.log(chunk);
    }
    ```
  </Tab>
</Tabs>

### Resuming

Resuming an execution after an [interrupt](https://reference.langchain.com/javascript/langchain-langgraph/index/interrupt) can be done by passing a **resume** value to the [`Command`](https://reference.langchain.com/javascript/langchain-langgraph/index/Command) primitive.

<Tabs>
  <Tab title="Invoke">
    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { Command } from "@langchain/langgraph";

    const config = {
      configurable: {
        thread_id: "some_thread_id"
      }
    };

    await myWorkflow.invoke(new Command({ resume: someResumeValue }), config);
    ```
  </Tab>

  <Tab title="Stream">
    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { Command } from "@langchain/langgraph";

    const config = {
      configurable: {
        thread_id: "some_thread_id"
      }
    };

    const stream = await myWorkflow.stream(
      new Command({ resume: someResumableValue }),
      config,
    )

    for await (const chunk of stream) {
      console.log(chunk);
    }
    ```
  </Tab>
</Tabs>

**Resuming after an error**

To resume after an error, run the `entrypoint` with `null` and the same **thread id** (config).

This assumes that the underlying **error** has been resolved and execution can proceed successfully.

<Tabs>
  <Tab title="Invoke">
    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    const config = {
      configurable: {
        thread_id: "some_thread_id"
      }
    };

    await myWorkflow.invoke(null, config);
    ```
  </Tab>

  <Tab title="Stream">
    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    const config = {
      configurable: {
        thread_id: "some_thread_id"
      }
    };

    for await (const chunk of myWorkflow.stream(null, config)) {
      console.log(chunk);
    }
    ```
  </Tab>
</Tabs>

### Short-term memory

When an `entrypoint` is defined with a `checkpointer`, it stores information between successive invocations on the same **thread id** in [checkpoints](/oss/javascript/langgraph/checkpointers#checkpoints).

This allows accessing the state from the previous invocation using the `getPreviousState` function.

By default, the `getPreviousState` function returns the return value of the previous invocation.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { entrypoint, getPreviousState } from "@langchain/langgraph";

const myWorkflow = entrypoint(
  { checkpointer, name: "workflow" },
  async (number: number) => {
    const previous = getPreviousState<number>() ?? 0;
    return number + previous;
  }
);

const config = {
  configurable: {
    thread_id: "some_thread_id",
  },
};

await myWorkflow.invoke(1, config); // 1 (previous was undefined)
await myWorkflow.invoke(2, config); // 3 (previous was 1 from the previous invocation)
```

#### `entrypoint.final`

[`entrypoint.final`](https://reference.langchain.com/javascript/functions/_langchain_langgraph.index.entrypoint.html#final) is a special primitive that can be returned from an entrypoint and allows **decoupling** the value that is **saved in the checkpoint** from the **return value of the entrypoint**.

The first value is the return value of the entrypoint, and the second value is the value that will be saved in the checkpoint.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { entrypoint, getPreviousState } from "@langchain/langgraph";

const myWorkflow = entrypoint(
  { checkpointer, name: "workflow" },
  async (number: number) => {
    const previous = getPreviousState<number>() ?? 0;
    // This will return the previous value to the caller, saving
    // 2 * number to the checkpoint, which will be used in the next invocation
    // for the `previous` parameter.
    return entrypoint.final({
      value: previous,
      save: 2 * number,
    });
  }
);

const config = {
  configurable: {
    thread_id: "1",
  },
};

await myWorkflow.invoke(3, config); // 0 (previous was undefined)
await myWorkflow.invoke(1, config); // 6 (previous was 3 * 2 from the previous invocation)
```

## Task

A **task** represents a discrete unit of work, such as an API call or data processing step. It has two key characteristics:

* **Asynchronous Execution**: Tasks are designed to be executed asynchronously, allowing multiple operations to run concurrently without blocking.
* **Checkpointing**: Task results are saved to a checkpoint, enabling resumption of the workflow from the last saved state. (See [persistence](/oss/javascript/langgraph/persistence) for more details).

### Definition

Tasks are defined using the `task` function, which wraps a regular function.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { task } from "@langchain/langgraph";

const slowComputation = task("slowComputation", async (inputValue: any) => {
  // Simulate a long-running operation
  return result;
});
```

<Warning>
  **Serialization**
  The **outputs** of tasks must be JSON-serializable to support checkpointing.
</Warning>

### Execution

**Tasks** can only be called from within an **entrypoint**, another **task**, or a [state graph node](/oss/javascript/langgraph/graph-api#nodes).

Tasks *cannot* be called directly from the main application code.

When you call a **task**, it returns a Promise that can be awaited.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const myWorkflow = entrypoint(
  { checkpointer, name: "workflow" },
  async (someInput: number): Promise<number> => {
    return await slowComputation(someInput);
  }
);
```

## When to use a task

**Tasks** are useful in the following scenarios:

* **Checkpointing**: When you need to save the result of a long-running operation to a checkpoint, so you don't need to recompute it when resuming the workflow.
* **Human-in-the-loop**: If you're building a workflow that requires human intervention, you MUST use **tasks** to encapsulate any randomness (e.g., API calls) to ensure that the workflow can be resumed correctly. See the [determinism](#determinism) section for more details.
* **Parallel Execution**: For I/O-bound tasks, **tasks** enable parallel execution, allowing multiple operations to run concurrently without blocking (e.g., calling multiple APIs).
* **Observability**: Wrapping operations in **tasks** provides a way to track the progress of the workflow and monitor the execution of individual operations using [LangSmith](/langsmith/observability).
* **Retryable Work**: When work needs to be retried to handle failures or inconsistencies, **tasks** provide a way to encapsulate and manage the retry logic.

## Serialization

There are two key aspects to serialization in LangGraph:

1. `entrypoint` inputs and outputs must be JSON-serializable.
2. `task` outputs must be JSON-serializable.

These requirements are necessary for enabling checkpointing and workflow resumption. Use primitives like objects, arrays, strings, numbers, and booleans to ensure that your inputs and outputs are serializable.

Serialization ensures that workflow state, such as task results and intermediate values, can be reliably saved and restored. This is critical for enabling human-in-the-loop interactions, fault tolerance, and parallel execution.

Providing non-serializable inputs or outputs will result in a runtime error when a workflow is configured with a checkpointer.

## Determinism

When you resume a workflow run, the code does **NOT** resume from the **same line of code** where execution stopped. Execution returns to a checkpoint boundary, and the workflow **replays** forward until it reaches the pause again.

For the Functional API, replay starts at the beginning of the **entrypoint** while LangGraph restores completed [**task**](/oss/javascript/langgraph/functional-api#task) and [**subgraph**](/oss/javascript/langgraph/use-subgraphs) results from the checkpointer instead of recomputing them. That preserves the recorded order of steps across pauses, including for long-running or non-deterministic **task** outputs.

To use features like **human-in-the-loop**, you must place non-deterministic work (for example, random values) and side effects (for example, file writes or API calls) in [**tasks**](/oss/javascript/langgraph/functional-api#task).

Different runs of a workflow can produce different results, but resuming a **specific** thread should replay the same persisted **task** and **subgraph** results.

To ensure that your workflow is deterministic and can be consistently replayed, follow these guidelines:

* **Avoid repeating work**: In an **entrypoint**, if you chain several side effects (for example, logging, file writes, or network calls), give each its own **task** so resume restores their outputs from the checkpointer instead of running them again.
* **Encapsulate non-deterministic operations**: Keep values that can change between attempts (for example, random numbers or wall-clock reads) inside **tasks**, so replay lines up with what was checkpointed.
* **Use idempotent operations**: For partial task failures and retries, see [Idempotency](#idempotency).

## Idempotency

Idempotency ensures that running the same operation multiple times produces the same result. This helps prevent duplicate API calls and redundant processing if a step is rerun due to a failure. Always place API calls inside **tasks** functions for checkpointing, and design them to be idempotent in case of re-execution.
This is particularly important for operations that result in data writes.
When a workflow resumes, LangGraph replays completed **task** results from the checkpoint. A **task** that started but did not finish may run again on that resume, so design side effects to be idempotent. Use idempotency keys or verify existing results to avoid unintended duplication.

## Common pitfalls

### Handling side effects

Encapsulate side effects (e.g., writing to a file, sending an email) in tasks to ensure they are not executed multiple times when resuming a workflow.

<Tabs>
  <Tab title="Incorrect">
    In this example, a side effect (writing to a file) is directly included in the workflow, so it will be executed a second time when resuming the workflow.

    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { entrypoint, interrupt } from "@langchain/langgraph";
    import fs from "fs";

    const myWorkflow = entrypoint(
      { checkpointer, name: "workflow },
      async (inputs: Record<string, any>) => {
        // This code will be executed a second time when resuming the workflow.
        // Which is likely not what you want.
        fs.writeFileSync("output.txt", "Side effect executed");
        const value = interrupt("question");
        return value;
      }
    );
    ```
  </Tab>

  <Tab title="Correct">
    In this example, the side effect is encapsulated in a task, ensuring consistent execution upon resumption.

    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { entrypoint, task, interrupt } from "@langchain/langgraph";
    import * as fs from "fs";

    const writeToFile = task("writeToFile", async () => {
      fs.writeFileSync("output.txt", "Side effect executed");
    });

    const myWorkflow = entrypoint(
      { checkpointer, name: "workflow" },
      async (inputs: Record<string, any>) => {
        // The side effect is now encapsulated in a task.
        await writeToFile();
        const value = interrupt("question");
        return value;
      }
    );
    ```
  </Tab>
</Tabs>

### Non-deterministic control flow

Operations that might give different results each time (like getting current time or random numbers) should be encapsulated in tasks to ensure that on resume, the same result is returned.

* In a task: Get random number (5) → interrupt → resume → (returns 5 again) → ...
* Not in a task: Get random number (5) → interrupt → resume → get new random number (7) → ...

This is especially important when using **human-in-the-loop** workflows with multiple interrupt calls. LangGraph keeps a list of resume values for each task/entrypoint. When an interrupt is encountered, it's matched with the corresponding resume value. This matching is strictly **index-based**, so the order of the resume values should match the order of the interrupts.

If order of execution is not maintained when resuming, one [`interrupt`](https://reference.langchain.com/javascript/langchain-langgraph/index/interrupt) call may be matched with the wrong `resume` value, leading to incorrect results.

Please read the section on [determinism](#determinism) for more details.

<Tabs>
  <Tab title="Incorrect">
    In this example, the workflow uses the current time to determine which task to execute. This is non-deterministic because the result of the workflow depends on the time at which it is executed.

    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { entrypoint, interrupt } from "@langchain/langgraph";

    const myWorkflow = entrypoint(
      { checkpointer, name: "workflow" },
      async (inputs: { t0: number }) => {
        const t1 = Date.now();

        const deltaT = t1 - inputs.t0;

        if (deltaT > 1000) {
          const result = await slowTask(1);
          const value = interrupt("question");
          return { result, value };
        } else {
          const result = await slowTask(2);
          const value = interrupt("question");
          return { result, value };
        }
      }
    );
    ```
  </Tab>

  <Tab title="Correct">
    In this example, the workflow uses the input `t0` to determine which task to execute. This is deterministic because the result of the workflow depends only on the input.

    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { entrypoint, task, interrupt } from "@langchain/langgraph";

    const getTime = task("getTime", () => Date.now());

    const myWorkflow = entrypoint(
      { checkpointer, name: "workflow" },
      async (inputs: { t0: number }): Promise<any> => {
        const t1 = await getTime();

        const deltaT = t1 - inputs.t0;

        if (deltaT > 1000) {
          const result = await slowTask(1);
          const value = interrupt("question");
          return { result, value };
        } else {
          const result = await slowTask(2);
          const value = interrupt("question");
          return { result, value };
        }
      }
    );
    ```
  </Tab>
</Tabs>

## Learn more

* [How to use the Functional API](/oss/javascript/langgraph/use-functional-api)
* [Graph API conceptual overview](/oss/javascript/langgraph/graph-api)
* [Choosing between Graph API and Functional API](/oss/javascript/langgraph/choosing-apis)

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langgraph/functional-api.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
