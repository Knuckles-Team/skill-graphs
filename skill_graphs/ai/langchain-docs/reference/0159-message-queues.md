# Message queues
Source: https://docs.langchain.com/oss/javascript/langchain/frontend/message-queues

Queue multiple messages and manage them while the agent processes sequentially

Message queuing lets users send multiple messages in rapid succession without waiting for the agent to finish processing the current one. Each message is accepted immediately, queued for the active thread, and processed sequentially, giving you full visibility and control over the pending work.

<PatternEmbed />

<Note>
  This feature requires the [LangGraph Agent Server](../langgraph/local-server). Run your agent locally with `langgraph dev` or [deploy it to LangSmith](/langsmith/deployment) to use this pattern.
</Note>

## Why message queues?

In a typical chat interface, users must wait for the agent to finish responding before sending another message. This creates friction in several scenarios:

* **Batch questions**: a user wants to ask five related questions at once rather than waiting for each answer
* **Follow-up chains**: submitting clarifications or additional context while the agent is still working
* **Automated testing sequences**: programmatically sending a series of prompts to validate agent behavior
* **Data entry workflows**: feeding structured inputs one after another for processing

Message queuing solves this by accepting all submissions immediately and processing them in order.

This is an agent UX primitive rather than a cosmetic chat feature. The SDK keeps
track of the queue as part of the stream controller, so your UI can show pending
work, cancel stale requests, and keep the composer active while the current run
continues.

## How it works

Pass `multitaskStrategy: "enqueue"` when you want a submission to wait behind
the currently running request. While the agent is processing, queued submissions
are added to the active thread's queue. Once the current run completes, the
next queued message is dispatched automatically.

Read queue state with the companion queue helper for your framework:

| Property           | Type                            | Description                              |
| ------------------ | ------------------------------- | ---------------------------------------- |
| `queue.entries`    | `SubmissionQueueEntry[]`        | Array of all pending queue entries       |
| `queue.size`       | `number`                        | Number of entries currently in the queue |
| `queue.cancel(id)` | `(id: string) => Promise<void>` | Cancel a specific queued entry by ID     |
| `queue.clear()`    | `() => Promise<void>`           | Cancel all queued entries                |

Each [SubmissionQueueEntry](https://reference.langchain.com/javascript/langchain-react/SubmissionQueueEntry) object contains:

| Field       | Type     | Description                                               |
| ----------- | -------- | --------------------------------------------------------- |
| `id`        | `string` | Unique identifier for this queue entry                    |
| `values`    | `object` | The input values (including messages) that were submitted |
| `options`   | `object` | Any additional options passed with the submission         |
| `createdAt` | `string` | ISO timestamp of when the entry was created               |

## Setting up `useStream`

Connect [`useStream`](https://reference.langchain.com/javascript/langchain-react/index/useStream) to your agent, then pair it with the submission queue
helper for your framework. Call `stream.submit()` to send messages while a run
is in progress; pass `multitaskStrategy: "enqueue"` on submissions that should
wait behind the active request. Read `queue.entries` and `queue.size` to render
pending work, and use `queue.cancel()` or `queue.clear()` to remove items before
they start processing.

<Info>
  The code examples use `useStream<typeof myAgent>` for type-safe stream state. See Type inference for [Python](/oss/python/langchain/frontend/overview#type-inference) or [JavaScript](/oss/javascript/langchain/frontend/overview#type-inference) backends.
</Info>

<CodeGroup>
  ```tsx React theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { useStream, useSubmissionQueue } from "@langchain/react";

  function Chat() {
    const stream = useStream<typeof myAgent>({
      apiUrl: "http://localhost:2024",
      assistantId: "simple_agent",
    });
    const queue = useSubmissionQueue(stream);

    const handleSubmit = (text: string) => {
      stream.submit({
        messages: [{ type: "human", content: text }],
      });
    };

    const pendingCount = queue.size;
    const entries = queue.entries;

    return (
      <div>
        <MessageList messages={stream.messages} />
        {pendingCount > 0 && <QueueList entries={entries} queue={queue} />}
        <ChatInput onSubmit={handleSubmit} />
      </div>
    );
  }
  ```

  ```vue Vue theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  <script setup lang="ts">
  import { useStream, useSubmissionQueue } from "@langchain/vue";
  import { computed } from "vue";

  const stream = useStream<typeof myAgent>({
    apiUrl: "http://localhost:2024",
    assistantId: "simple_agent",
  });
  const queue = useSubmissionQueue(stream);

  function handleSubmit(text: string) {
    stream.submit({
      messages: [{ type: "human", content: text }],
    });
  }

  const pendingCount = computed(() => queue.size.value);
  const entries = computed(() => queue.entries.value);
  </script>

  <template>
    <div>
      <MessageList :messages="stream.messages" />
      <QueueList v-if="pendingCount > 0" :entries="entries" :queue="queue" />
      <ChatInput @submit="handleSubmit" />
    </div>
  </template>
  ```

  ```svelte Svelte theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  <script lang="ts">
    import { useStream, useSubmissionQueue } from "@langchain/svelte";

    const stream = useStream<typeof myAgent>({
      apiUrl: "http://localhost:2024",
      assistantId: "simple_agent",
    });
    const queue = useSubmissionQueue(stream);

    function handleSubmit(text: string) {
      stream.submit({
        messages: [{ type: "human", content: text }],
      });
    }
  </script>

  <div>
    <MessageList messages={stream.messages} />
    {#if queue.size > 0}
      <QueueList entries={queue.entries} {queue} />
    {/if}
    <ChatInput on:submit={(e) => handleSubmit(e.detail)} />
  </div>
  ```

  ```ts Angular theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { Component } from "@angular/core";
  import { injectStream, injectSubmissionQueue } from "@langchain/angular";

  @Component({
    selector: "app-chat",
    template: `
      <message-list [messages]="stream.messages()" />
      @if (queue.size() > 0) {
        <queue-list [entries]="queue.entries()" [queue]="queue" />
      }
      <chat-input (onSubmit)="handleSubmit($event)" />
    `,
  })
  export class ChatComponent {
    stream = injectStream<typeof myAgent>({
      apiUrl: "http://localhost:2024",
      assistantId: "simple_agent",
    });
    queue = injectSubmissionQueue(this.stream);

    handleSubmit(text: string) {
      this.stream.submit({
        messages: [{ type: "human", content: text }],
      });
    }
  }
  ```
</CodeGroup>

## Displaying the queue

Build a `QueueList` component that shows each pending message with a cancel button. This gives users visibility into what's waiting and the ability to remove items they no longer need.

```tsx theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
function QueueList({ entries, queue }) {
  return (
    <div className="queue-panel">
      <div className="queue-header">
        <span>Queued messages ({entries.length})</span>
        <button onClick={() => queue.clear()}>Clear all</button>
      </div>
      <ul className="queue-entries">
        {entries.map((entry) => {
          const text = entry.values?.messages?.at(-1)?.content ?? "Pending...";
          return (
            <li key={entry.id} className="queue-entry">
              <span className="queue-text">{text}</span>
              <span className="queue-time">
                {new Date(entry.createdAt).toLocaleTimeString()}
              </span>
              <button
                className="queue-cancel"
                onClick={() => queue.cancel(entry.id)}
              >
                Cancel
              </button>
            </li>
          );
        })}
      </ul>
    </div>
  );
}
```

<Tip>
  Display the first few characters of each queued message as a preview so users can quickly identify which items to cancel without reading full messages.
</Tip>

## Cancelling queued messages

You have two levels of cancellation:

### Cancel a single entry

Remove a specific message from the queue by its ID. The agent will skip it and move to the next entry.

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
await queue.cancel(entryId);
```

### Clear the entire queue

Remove all pending messages at once. Useful when the user changes context or wants to start over.

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
await queue.clear();
```

<Note>
  Cancelling a queue entry only affects messages that have **not yet started
  processing**. If the agent is already working on a message, cancelling it from
  the queue has no effect. Use `stream.stop()` to interrupt the current run.
</Note>

## Chaining follow-up submissions with `onCreated`

The `onCreated` callback fires when a new run is created, giving you a hook to submit follow-up messages programmatically. This is useful for building multi-step workflows where the next question depends on the previous submission being accepted.

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
stream.submit(
  { messages: [{ type: "human", content: "What is quantum computing?" }] },
  {
    onCreated(run) {
      console.log("Run created:", run.runId);
      // Chain a follow-up
      stream.submit({
        messages: [{ type: "human", content: "Give me a simple analogy." }],
      });
    },
  }
);
```

This pattern naturally fills the queue. The first message starts processing
immediately, and the follow-up is queued behind it.

## Starting a new thread

When a user wants to begin a fresh conversation, update the reactive `threadId`
that you pass into the stream. Passing `null` clears the current thread binding;
the next submission creates a new thread.

<CodeGroup>
  ```tsx React theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  function NewThreadButton() {
    const [threadId, setThreadId] = useState<string | null>(null);
    const stream = useStream<typeof myAgent>({ threadId, onThreadId: setThreadId });

    return (
      <button onClick={() => setThreadId(null)}>
        New conversation
      </button>
    );
  }
  ```

  ```vue Vue theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  <script setup lang="ts">
  const threadId = ref<string | null>(null);
  const stream = useStream<typeof myAgent>({
    threadId,
    onThreadId: (id) => (threadId.value = id),
  });
  </script>

  <template>
    <button @click="threadId = null">New conversation</button>
  </template>
  ```

  ```svelte Svelte theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  <script lang="ts">
    let threadId = $state<string | null>(null);
    const stream = useStream<typeof myAgent>({
      threadId: () => threadId,
      onThreadId: (id) => (threadId = id),
    });
  </script>

  <button onclick={() => (threadId = null)}>New conversation</button>
  ```

  ```ts Angular theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  threadId = signal<string | null>(null);
  stream = injectStream<typeof myAgent>({
    threadId: this.threadId,
    onThreadId: (id) => this.threadId.set(id),
  });

  // In template:
  // <button (click)="threadId.set(null)">New conversation</button>
  ```
</CodeGroup>

## Best practices

* **Limit queue size**: While there is no hard client-side limit on queue size,
  be mindful that very large queues can degrade user experience. Consider
  showing a warning when the queue exceeds a reasonable threshold (e.g., 10
  items).
* **Show queue position**: Number each queued item so users know the processing order.
* **Preserve input focus**: Keep the input field focused after submission so users can type the next message immediately.
* **Animate transitions**: Smoothly move items from the queue panel into the message list as they start processing.
* **Handle errors gracefully**: If a queued message fails, surface the error without blocking subsequent queue entries.
* **Debounce rapid submissions**: For automated or programmatic submissions, add a small delay between messages to avoid overwhelming the server.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/frontend/message-queues.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Overview
Source: https://docs.langchain.com/oss/javascript/langchain/frontend/overview

Build generative UIs with real-time streaming from LangChain agents

Build rich, interactive frontends for agents created with `createAgent`. These
patterns cover everything from basic message rendering to advanced workflows
like human-in-the-loop approval, queued submissions, durable stream rejoin, and
time travel debugging.

LangChain frontend SDKs are built for **agent applications**, not only
token-streaming chatbots. The same hook that renders messages also exposes the
agent's durable thread state, tool-call lifecycle, interrupts, checkpoint
history, and custom state values, so your UI can become a control plane for
long-running agent work.

<Note>
  These patterns use the v1 frontend SDK packages. If you are using an earlier version, see the migration guides for [React](https://github.com/langchain-ai/langgraphjs/blob/main/libs/sdk-react/docs/v1-migration.md), [Vue](https://github.com/langchain-ai/langgraphjs/blob/main/libs/sdk-vue/docs/v1-migration.md), [Svelte](https://github.com/langchain-ai/langgraphjs/blob/main/libs/sdk-svelte/docs/v1-migration.md), and [Angular](https://github.com/langchain-ai/langgraphjs/blob/main/libs/sdk-angular/docs/v1-migration.md).
</Note>

## Architecture

Every pattern follows the same architecture: a `createAgent` backend streams state to a frontend via the SDK stream API.

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
  BACKEND["createAgent()"]

  BACKEND --"stream"--> FRONTEND
  FRONTEND --"submit"--> BACKEND

  classDef blueHighlight fill:#E5F4FF,stroke:#006DDD,color:#030710;
  classDef greenHighlight fill:#F6FFDB,stroke:#6E8900,color:#2E3900;
  class FRONTEND blueHighlight;
  class BACKEND greenHighlight;
```

On the backend, `createAgent` produces a compiled LangGraph graph that exposes a streaming API. On the frontend, the stream handle connects to that API and provides reactive state — messages, tool calls, interrupts, values, and thread metadata — that you render with any framework.

## Why use the LangChain frontend SDKs?

Most AI UI libraries help you append streamed text to a chat transcript.
LangChain's SDKs expose the richer runtime semantics that production agents
need:

| Capability                      | What it enables in your UI                                                                                                       |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| **Durable threads**             | Reload a page, switch devices, or rejoin a run without losing the conversation state.                                            |
| **Typed agent state**           | Render any state key, not just messages: todos, pipeline outputs, citations, sandbox files, metrics, or custom business objects. |
| **Tool-call lifecycle**         | Show pending, completed, and failed tool calls as purpose-built UI cards instead of raw JSON.                                    |
| **Interrupts**                  | Pause execution for human approval, edits, or missing information, then resume from the exact point where the agent stopped.     |
| **Checkpoints**                 | Build edit, retry, branch, audit, and time-travel flows from persisted state snapshots.                                          |
| **Nested execution**            | Visualize deep agents, subagents, and graph nodes without flattening everything into one unreadable stream.                      |
| **Framework-native reactivity** | Use the same protocol from React, Vue, Svelte, or Angular while keeping idiomatic hooks, composables, stores, or signals.        |

These primitives let you design UIs where users can inspect, steer, pause,
resume, and fork agent work while it is happening.

<CodeGroup>
  ```ts agent.ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createAgent } from "langchain";
  import { MemorySaver } from "@langchain/langgraph";

  const agent = createAgent({
    model: "openai:gpt-5.5",
    tools: [getWeather, searchWeb],
    checkpointer: new MemorySaver(),
  });
  ```

  ```tsx Chat.tsx theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { useStream } from "@langchain/react";
  import type { agent } from "./agent";

  function Chat() {
    const stream = useStream<typeof agent>({
      apiUrl: "http://localhost:2024",
      assistantId: "agent",
    });

    return (
      <div>
        {stream.messages.map((msg) => (
          <Message key={msg.id} message={msg} />
        ))}
      </div>
    );
  }
  ```
</CodeGroup>

React, Vue, and Svelte use `useStream`. Angular uses `injectStream`:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { useStream } from "@langchain/react";      // React
import { useStream } from "@langchain/vue";        // Vue
import { useStream } from "@langchain/svelte";     // Svelte
import { injectStream } from "@langchain/angular"; // Angular
```

## Type inference

Pass a type parameter to [`useStream`](https://reference.langchain.com/javascript/langchain-react/index/useStream) (or [`injectStream`](https://reference.langchain.com/javascript/langchain-angular/injectStream) in Angular) for type-safe access to `stream.messages`, `stream.toolCalls`, `stream.interrupt`, `stream.values`, and other reactive state.

Import your agent and pass `typeof myAgent` as the type parameter. TypeScript infers the state schema from the compiled graph:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import type { myAgent } from "./agent";

const stream = useStream<typeof myAgent>({
  apiUrl: "http://localhost:2024",
  assistantId: "agent",
});
```

Custom state keys are inferred automatically, no manual interface required.

## Patterns

### Render messages and output

<CardGroup>
  <Card title="Markdown messages" icon="markdown" href="/oss/javascript/langchain/frontend/markdown-messages">
    Parse and render streamed markdown with proper formatting and code highlighting.
  </Card>

  <Card title="Structured output" icon="layout-grid" href="/oss/javascript/langchain/frontend/structured-output">
    Render typed agent responses as custom UI components instead of plain text.
  </Card>

  <Card title="Reasoning tokens" icon="brain" href="/oss/javascript/langchain/frontend/reasoning-tokens">
    Display model thinking processes in collapsible blocks.
  </Card>

  <Card title="Generative UI" icon="wand" href="/oss/javascript/langchain/frontend/generative-ui">
    Render AI-generated user interfaces from natural language prompts using json-render.
  </Card>
</CardGroup>

### Display agent actions

<CardGroup>
  <Card title="Tool calling" icon="tool" href="/oss/javascript/langchain/frontend/tool-calling">
    Show tool calls as rich, type-safe UI cards with loading and error states.
  </Card>

  <Card title="Headless tools" icon="device-desktop" href="/oss/javascript/langchain/frontend/headless-tools">
    Run browser and device APIs on the client while keeping typed tool schemas on the agent.
  </Card>

  <Card title="Human-in-the-loop" icon="user-check" href="/oss/javascript/langchain/frontend/human-in-the-loop">
    Pause the agent for human review with approve, reject, and edit workflows.
  </Card>
</CardGroup>

### Manage conversations

<CardGroup>
  <Card title="Branching chat" icon="git-branch" href="/oss/javascript/langchain/frontend/branching-chat">
    Edit messages, regenerate responses, and navigate conversation branches.
  </Card>

  <Card title="Message queues" icon="list-check" href="/oss/javascript/langchain/frontend/message-queues">
    Queue multiple messages while the agent processes them sequentially.
  </Card>
</CardGroup>

### Advanced streaming

<CardGroup>
  <Card title="Join & rejoin streams" icon="plug-connected" href="/oss/javascript/langchain/frontend/join-rejoin">
    Disconnect from and reconnect to running agent streams without losing progress.
  </Card>

  <Card title="Time travel" icon="clock" href="/oss/javascript/langchain/frontend/time-travel">
    Inspect, navigate, and resume from any checkpoint in the conversation history.
  </Card>
</CardGroup>

## Choosing a frontend pattern

Start from the UX question your application needs to answer:

| If users need to...                        | Start with                                                                                                                                                                                                                      |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Understand what the agent is doing         | [Tool calling](/oss/javascript/langchain/frontend/tool-calling) and [reasoning tokens](/oss/javascript/langchain/frontend/reasoning-tokens)                                                                                     |
| Safely approve sensitive actions           | [Human-in-the-loop](/oss/javascript/langchain/frontend/human-in-the-loop)                                                                                                                                                       |
| Send work while a run is active            | [Message queues](/oss/javascript/langchain/frontend/message-queues)                                                                                                                                                             |
| Leave and come back to long-running work   | [Join & rejoin streams](/oss/javascript/langchain/frontend/join-rejoin)                                                                                                                                                         |
| Edit or retry from an earlier turn         | [Branching chat](/oss/javascript/langchain/frontend/branching-chat) and [time travel](/oss/javascript/langchain/frontend/time-travel)                                                                                           |
| Render state as an application, not a chat | [Structured output](/oss/javascript/langchain/frontend/structured-output), [generative UI](/oss/javascript/langchain/frontend/generative-ui), and [Deep Agents frontend patterns](/oss/javascript/deepagents/frontend/overview) |

## Integrations

The stream API is UI-agnostic. Use it with any component library or generative UI
framework. Component libraries can own the presentation layer while LangChain's
SDK owns the agent runtime state, resumability, interrupts, and checkpoint
semantics underneath.

<CardGroup>
  <Card title="AI Elements" icon="package" href="/oss/javascript/langchain/frontend/integrations/ai-elements">
    Composable shadcn/ui components for AI chat: `Conversation`, `Message`, `Tool`, `Reasoning`.
  </Card>

  <Card title="assistant-ui" icon="package" href="/oss/javascript/langchain/frontend/integrations/assistant-ui">
    Headless React framework with built-in thread management, branching, and attachment support.
  </Card>

  <Card title="OpenUI" icon="package" href="/oss/javascript/langchain/frontend/integrations/openui">
    Generative UI library for data-rich reports and dashboards using the openui-lang component DSL.
  </Card>
</CardGroup>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/frontend/overview.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Reasoning tokens
Source: https://docs.langchain.com/oss/javascript/langchain/frontend/reasoning-tokens

Display model thinking and reasoning processes in collapsible blocks

Reasoning tokens expose the internal thought process of advanced models like OpenAI's GPT-5 and Anthropic's Claude with extended thinking. These models produce structured content blocks that separate reasoning from the final answer, letting you build UIs that show *how* the model arrived at its response.

<PatternEmbed />

## What are reasoning tokens?

When models with reasoning capabilities process a prompt, they generate two distinct types of content:

1. **Reasoning blocks**: the model's internal chain-of-thought, problem decomposition, and step-by-step analysis
2. **Text blocks**: the final, polished response presented to the user

These are delivered as typed content blocks within an `AIMessage`, accessible via the `contentBlocks` property:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
// Reasoning block
{ type: "reasoning", reasoning: "Let me think about this step by step..." }

// Text block
{ type: "text", text: "The answer is 42." }
```

<Note>
  Not all models produce reasoning tokens. This pattern applies specifically to models that support extended thinking or chain-of-thought output. Standard chat models return only text blocks.
</Note>

## Use cases

* **Transparency**: show users the model's reasoning process to build trust in its answers
* **Debugging**: inspect the model's thought process to identify where it goes wrong
* **Educational tools**: teach students problem-solving by revealing how an AI approaches questions
* **Decision support**: let domain experts validate the reasoning behind recommendations
* **Quality assurance**: audit reasoning chains for compliance in regulated industries

## Extracting reasoning and text blocks

The `contentBlocks` array on an `AIMessage` contains all blocks in the order they were generated. Filter them by `type` to separate reasoning from text:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { AIMessage } from "langchain";

function extractBlocks(msg: AIMessage) {
  const reasoningBlocks = msg.contentBlocks
    .filter((b) => b.type === "reasoning")
    .map((b) => b.reasoning);

  const textBlocks = msg.contentBlocks
    .filter((b) => b.type === "text")
    .map((b) => b.text);

  return {
    reasoning: reasoningBlocks.join(""),
    text: textBlocks.join(""),
  };
}
```

A single message may contain multiple reasoning blocks (e.g., if the model pauses its reasoning, produces partial text, then reasons further). Joining them gives you the complete thought process.

## Accessing messages from `useStream`

Connect [`useStream`](https://reference.langchain.com/javascript/langchain-react/index/useStream) to your reasoning-capable agent and iterate
`stream.messages` in your chat UI. Branch on `HumanMessage.isInstance` and
`AIMessage.isInstance`, then pass each assistant message to a component that
reads `contentBlocks` and separates reasoning from text. Set `isStreaming` on
the last message while `stream.isLoading` is true so thinking blocks update as
tokens arrive.

<Info>
  The code examples use `useStream<typeof myAgent>` for type-safe stream state. See Type inference for [Python](/oss/python/langchain/frontend/overview#type-inference) or [JavaScript](/oss/javascript/langchain/frontend/overview#type-inference) backends.
</Info>

<CodeGroup>
  ```tsx React theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { useStream } from "@langchain/react";
  import { AIMessage, HumanMessage } from "langchain";

  function Chat() {
    const stream = useStream<typeof myAgent>({
      apiUrl: "http://localhost:2024",
      assistantId: "reasoning",
    });

    return (
      <div className="messages">
        {stream.messages.map((msg, i) => {
          if (HumanMessage.isInstance(msg)) {
            return <HumanBubble key={i} text={msg.text} />;
          }
          if (AIMessage.isInstance(msg)) {
            return (
              <AIResponse
                key={i}
                message={msg}
                isStreaming={stream.isLoading && i === stream.messages.length - 1}
              />
            );
          }
          return null;
        })}
      </div>
    );
  }
  ```

  ```vue Vue theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  <script setup lang="ts">
  import { useStream } from "@langchain/vue";
  import { AIMessage, HumanMessage } from "langchain";

  const stream = useStream<typeof myAgent>({
    apiUrl: "http://localhost:2024",
    assistantId: "reasoning",
  });
  </script>

  <template>
    <div class="messages">
      <template v-for="(msg, i) in stream.messages.value" :key="i">
        <HumanBubble v-if="HumanMessage.isInstance(msg)" :text="msg.text" />
        <AIResponse
          v-else-if="AIMessage.isInstance(msg)"
          :message="msg"
          :isStreaming="stream.isLoading.value && i === stream.messages.value.length - 1"
        />
      </template>
    </div>
  </template>
  ```

  ```svelte Svelte theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  <script lang="ts">
    import { useStream } from "@langchain/svelte";
    import { AIMessage, HumanMessage } from "langchain";

    const stream = useStream<typeof myAgent>({
      apiUrl: "http://localhost:2024",
      assistantId: "reasoning",
    });
  </script>

  <div class="messages">
    {#each stream.messages as msg, i}
      {#if HumanMessage.isInstance(msg)}
        <HumanBubble text={msg.text} />
      {:else if AIMessage.isInstance(msg)}
        <AIResponse
          message={msg}
          isStreaming={stream.isLoading && i === stream.messages.length - 1}
        />
      {/if}
    {/each}
  </div>
  ```

  ```ts Angular theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { Component } from "@angular/core";
  import { injectStream } from "@langchain/angular";
  import { AIMessage, HumanMessage } from "langchain";

  @Component({
    selector: "app-chat",
    template: `
      <div class="messages">
        @for (msg of stream.messages(); track $index) {
          @if (isHuman(msg)) {
            <human-bubble [text]="msg.text" />
          } @else if (isAI(msg)) {
            <ai-response
              [message]="msg"
              [isStreaming]="stream.isLoading() && $index === stream.messages().length - 1"
            />
          }
        }
      </div>
    `,
  })
  export class ChatComponent {
    stream = injectStream<typeof myAgent>({
      apiUrl: "http://localhost:2024",
      assistantId: "reasoning",
    });

    isHuman = HumanMessage.isInstance;
    isAI = AIMessage.isInstance;
  }
  ```
</CodeGroup>

## Building a ThinkingBubble component

The `ThinkingBubble` presents reasoning tokens in a visually distinct, collapsible container. Users can expand it to see the full thought process or collapse it to focus on the final answer.

```tsx theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { useState } from "react";

function ThinkingBubble({
  reasoning,
  isStreaming,
}: {
  reasoning: string;
  isStreaming: boolean;
}) {
  const [isExpanded, setIsExpanded] = useState(false);

  const charCount = reasoning.length;
  const previewLength = 120;
  const preview =
    reasoning.length > previewLength
      ? reasoning.slice(0, previewLength) + "..."
      : reasoning;

  return (
    <div className="thinking-bubble">
      <button
        className="thinking-header"
        onClick={() => setIsExpanded(!isExpanded)}
      >
        <span className="thinking-icon">
          {isStreaming ? (
            <span className="thinking-spinner" />
          ) : (
            "💭"
          )}
        </span>
        <span className="thinking-label">
          {isStreaming ? "Thinking..." : `Thought process (${charCount} chars)`}
        </span>
        <span className={`chevron ${isExpanded ? "expanded" : ""}`}>▶</span>
      </button>

      {isExpanded && (
        <div className="thinking-content">
          <pre>{reasoning}</pre>
        </div>
      )}

      {!isExpanded && !isStreaming && (
        <div className="thinking-preview">{preview}</div>
      )}
    </div>
  );
}
```

## Rendering the complete AI response

Combine the `ThinkingBubble` and a standard text bubble into a single `AIResponse` component:

```tsx theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
function AIResponse({
  message,
  isStreaming,
}: {
  message: AIMessage;
  isStreaming: boolean;
}) {
  const reasoningBlocks = message.contentBlocks
    .filter((b) => b.type === "reasoning")
    .map((b) => b.reasoning)
    .join("");

  const textBlocks = message.contentBlocks
    .filter((b) => b.type === "text")
    .map((b) => b.text)
    .join("");

  const hasReasoning = reasoningBlocks.length > 0;
  const hasText = textBlocks.length > 0;

  const isReasoningPhase = isStreaming && !hasText;
  const isTextPhase = isStreaming && hasText;

  return (
    <div className="ai-response">
      {hasReasoning && (
        <ThinkingBubble
          reasoning={reasoningBlocks}
          isStreaming={isReasoningPhase}
        />
      )}
      {hasText && (
        <div className="ai-text-bubble">
          <p>{textBlocks}</p>
          {isTextPhase && <span className="cursor-blink">▊</span>}
        </div>
      )}
    </div>
  );
}
```

## Handling edge cases

### Messages without reasoning

Not every AI message will contain reasoning blocks. When `contentBlocks` has only text blocks, render a standard message bubble without the ThinkingBubble.

### Empty reasoning blocks

Some models produce empty reasoning blocks as placeholders. Filter these out:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const meaningfulReasoning = message.contentBlocks
  .filter((b) => b.type === "reasoning" && b.reasoning.trim().length > 0);
```

### Multiple reasoning-text cycles

A single message can alternate between reasoning and text blocks. If you need to preserve this interleaving, iterate `contentBlocks` in order rather than grouping by type:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
message.contentBlocks.forEach((block) => {
  if (block.type === "reasoning") {
    // Render ThinkingBubble
  } else if (block.type === "text") {
    // Render text paragraph
  }
});
```

## Best practices

* **Default to collapsed**: show reasoning on demand, not by default
* **Show character count**: gives users a quick sense of how much thinking went into the response
* **Differentiate visually**: use distinct colors, borders, or backgrounds so reasoning is never confused with the actual answer
* **Animate transitions**: smooth expand/collapse animations improve perceived quality
* **Consider accessibility**: use proper ARIA attributes (`aria-expanded`, `aria-controls`) on the toggle button
* **Truncate in previews**: show a short preview of the reasoning when collapsed so users can decide whether to expand

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/frontend/reasoning-tokens.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
