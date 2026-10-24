# Join & rejoin streams
Source: https://docs.langchain.com/oss/python/langchain/frontend/join-rejoin

Disconnect from and reconnect to running agent streams

Join and rejoin lets you disconnect from a running agent stream without stopping the agent, then reconnect to it later. The agent continues executing server-side while the client is away, and you pick up the stream exactly where you left off.

<PatternEmbed />

<Note>
  This feature requires the [LangGraph Agent Server](../langgraph/local-server). Run your agent locally with `langgraph dev` or [deploy it to LangSmith](/langsmith/deployment) to use this pattern.
</Note>

## Why join & rejoin?

Traditional streaming APIs tightly couple the client and server: if the client disconnects, the stream is lost. Join and rejoin breaks this coupling, enabling several important patterns:

* **Network interruptions**: mobile users moving between cell towers or Wi-Fi networks can seamlessly resume
* **Page navigation**: users navigating away from a chat page and returning later without losing progress
* **Mobile backgrounding**: apps suspended by the OS can rejoin the stream when foregrounded
* **Long-running tasks**: agents performing multi-minute operations (research, code generation, data analysis) where users don't need to keep the page open
* **Multi-device handoff**: start a conversation on your phone, rejoin on your desktop

## Core concepts

The join/rejoin pattern involves three key mechanisms:

| Method / Option                  | Purpose                                                                |
| -------------------------------- | ---------------------------------------------------------------------- |
| `threadId`                       | Bind the stream to the LangGraph thread you want to observe            |
| `onThreadId`                     | Persist newly-created thread IDs so a remount can reconnect            |
| `stream.disconnect()`            | Leave the stream client-side while the agent keeps running server-side |
| Remount with the same `threadId` | Reattach to in-flight work for that thread                             |

<Note>
  **Join/rejoin uses `stream.disconnect()`, not `stream.stop()`.** By default, `stream.stop()` **cancels the active run**: it disconnects the client *and* cancels the run on the server. For join/rejoin, call `stream.disconnect()` (alias for `stop({ cancel: false })`) so the agent continues processing while you are away.

  To cancel execution explicitly from app code, use `stream.stop()` or [`client.runs.cancel`](https://reference.langchain.com/javascript/langchain-langgraph-sdk/client/RunsClient/cancel).
</Note>

## Setting up `useStream`

The key setup step is persisting `threadId`. When the component remounts with
the same thread ID, the stream attaches to the thread's current state and any
in-flight run.

<Info>
  The code examples use `useStream<typeof myAgent>` for type-safe stream state. See Type inference for [Python](/oss/python/langchain/frontend/overview#type-inference) or [JavaScript](/oss/javascript/langchain/frontend/overview#type-inference) backends.
</Info>

<CodeGroup>
  ```tsx React theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { useStream } from "@langchain/react";
  import { useCallback, useState } from "react";

  function Chat() {
    const [connected, setConnected] = useState(true);
    const [mountKey, setMountKey] = useState(0);
    const [threadId, setThreadId] = useState<string | null>(
      () => sessionStorage.getItem("activeThreadId"),
    );

    const stream = useStream<typeof myAgent>({
      apiUrl: "http://localhost:2024",
      assistantId: "join_rejoin",
      threadId,
      onThreadId(id) {
        setThreadId(id);
        if (id) sessionStorage.setItem("activeThreadId", id);
      },
    });

    const disconnect = useCallback(() => {
      void stream.disconnect();
      setConnected(false);
    }, [stream]);

    const rejoin = useCallback(() => {
      setMountKey((key) => key + 1);
      setConnected(true);
    }, []);

    return (
      <div key={mountKey}>
        <ConnectionStatus connected={connected} />
        <MessageList messages={stream.messages} />
        <ChatControls
          stream={stream}
          threadId={threadId}
          connected={connected}
          onDisconnect={disconnect}
          onRejoin={rejoin}
        />
      </div>
    );
  }
  ```

  ```vue Vue theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  <script setup lang="ts">
  import { useStream } from "@langchain/vue";
  import { ref } from "vue";

  const connected = ref(true);
  const mountKey = ref(0);
  const threadId = ref<string | null>(sessionStorage.getItem("activeThreadId"));

  const stream = useStream<typeof myAgent>({
    apiUrl: "http://localhost:2024",
    assistantId: "join_rejoin",
    threadId,
    onThreadId(id) {
      threadId.value = id;
      if (id) sessionStorage.setItem("activeThreadId", id);
    },
  });

  function disconnect() {
    void stream.disconnect();
    connected.value = false;
  }

  function rejoin() {
    mountKey.value += 1;
    connected.value = true;
  }
  </script>

  <template>
    <div :key="mountKey">
      <ConnectionStatus :connected="connected" />
      <MessageList :messages="stream.messages" />
      <ChatControls
        :stream="stream"
        :threadId="threadId"
        :connected="connected"
        @disconnect="disconnect"
        @rejoin="rejoin"
      />
    </div>
  </template>
  ```

  ```svelte Svelte theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  <script lang="ts">
    import { useStream } from "@langchain/svelte";

    let connected = $state(true);
    let mountKey = $state(0);
    let threadId = $state<string | null>(sessionStorage.getItem("activeThreadId"));

    const stream = useStream<typeof myAgent>({
      apiUrl: "http://localhost:2024",
      assistantId: "join_rejoin",
      threadId: () => threadId,
      onThreadId(id) {
        threadId = id;
        if (id) sessionStorage.setItem("activeThreadId", id);
      },
    });

    function disconnect() {
      void stream.disconnect();
      connected = false;
    }

    function rejoin() {
      mountKey += 1;
      connected = true;
    }
  </script>

  <div key={mountKey}>
    <ConnectionStatus {connected} />
    <MessageList messages={stream.messages} />
    <ChatControls
      {threadId}
      {connected}
      onDisconnect={disconnect}
      onRejoin={rejoin}
    />
  </div>
  ```

  ```ts Angular theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { Component, signal } from "@angular/core";
  import { injectStream } from "@langchain/angular";

  @Component({
    selector: "app-chat",
    template: `
      <connection-status [connected]="connected()" />
      <message-list [messages]="stream.messages()" />
      <chat-controls
        [stream]="stream"
        [threadId]="threadId()"
        [connected]="connected()"
        (disconnect)="disconnect()"
        (rejoin)="rejoin()"
      />
    `,
  })
  export class ChatComponent {
    threadId = signal<string | null>(sessionStorage.getItem("activeThreadId"));
    connected = signal(true);
    mountKey = signal(0);

    stream = injectStream<typeof myAgent>({
      apiUrl: "http://localhost:2024",
      assistantId: "join_rejoin",
      threadId: this.threadId,
      onThreadId: (id) => {
        this.threadId.set(id);
        if (id) sessionStorage.setItem("activeThreadId", id);
      },
    });

    disconnect() {
      void this.stream.disconnect();
      this.connected.set(false);
    }

    rejoin() {
      this.mountKey.update((key) => key + 1);
      this.connected.set(true);
    }
  }
  ```
</CodeGroup>

## Submitting messages

Submit messages normally. The thread ID binding is what allows a later remount
to reconnect to the same conversation:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
stream.submit({ messages: [{ type: "human", content: text }] });
```

## Disconnecting from a stream

Call `stream.disconnect()` to leave the stream without cancelling the run. The agent continues processing server-side.

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
await stream.disconnect();
// equivalent to: await stream.stop({ cancel: false })
```

Do **not** use `stream.stop()` here — by default it cancels the run on the server.

After calling `disconnect()`:

* `stream.isLoading` becomes `false`
* Your own `connected` flag should also become `false`
* The message list retains all messages received up to the disconnect point
* The agent continues running on the server
* No new messages are received until you rejoin

## Rejoining a stream

Remount the stream consumer with the saved thread ID to reconnect. In React, the
demo bumps a `mountKey`; in other frameworks, use the equivalent remount or
conditional-render pattern:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
setMountKey((key) => key + 1);
setConnected(true);
```

After rejoining:

* `connected` becomes `true`
* Any messages generated while disconnected are delivered
* New streaming messages resume in real-time
* If the agent is still running, `stream.isLoading` becomes `true`; if it has
  already finished, you receive the final state immediately

## Best practices

* **Use `disconnect()` for join/rejoin, `stop()` to cancel**: navigating away or backgrounding the app should call `stream.disconnect()`. A user-facing "Stop" or "Cancel" button should call `stream.stop()` (or [`client.runs.cancel`](https://reference.langchain.com/javascript/langchain-langgraph-sdk/client/RunsClient/cancel)).
* **Always save the thread ID**: without it, rejoining is impossible. Use both component state and persistent storage for resilience.
* **Show clear connection state**: users should always know whether they are receiving live updates or viewing a snapshot.
* **Auto-rejoin on visibility change**: use the Page Visibility API to automatically rejoin when the user returns to the tab.
* **Set reasonable timeouts**: if a rejoin attempt takes too long, fall back to fetching the thread history instead.
* **Clean up stale threads**: remove persisted thread IDs when the user starts over or the backend reports that the thread is unavailable.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/frontend/join-rejoin.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Markdown messages
Source: https://docs.langchain.com/oss/python/langchain/frontend/markdown-messages

Render LLM responses as rich, formatted markdown with proper streaming support

LLMs naturally produce markdown-formatted text, including headings, lists, code blocks,
tables, and inline formatting. Rendering this content as plain text wastes the
structure the model is providing. This pattern shows you how to parse and render
markdown in real time as it streams from the agent, across all major frontend
frameworks.

<PatternEmbed />

## How markdown rendering works

The rendering pipeline has three steps:

1. **Receive:** [`useStream`](https://reference.langchain.com/javascript/langchain-react/index/useStream) accumulates the streamed text into `msg.text` on
   each AI message, updating reactively as new tokens arrive.
2. **Parse:** A markdown parser converts the raw text to HTML (or a React
   element tree). This runs on every update but is fast enough for chat-length
   content (\< 5ms for a 5 KB message).
3. **Render:** The parsed output is rendered into the DOM. React uses virtual
   DOM diffing; Vue and Svelte use `v-html` / `{@html}` with sanitized HTML.

## Setting up `useStream`

The markdown pattern uses a simple chat agent with no special configuration.
Wire up [`useStream`](https://reference.langchain.com/javascript/langchain-react/index/useStream) with your agent URL and assistant ID.

<Info>
  The code examples use `useStream<typeof myAgent>` for type-safe stream state. See Type inference for [Python](/oss/python/langchain/frontend/overview#type-inference) or [JavaScript](/oss/javascript/langchain/frontend/overview#type-inference) backends.
</Info>

<CodeGroup>
  ```tsx React theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { useStream } from "@langchain/react";
  import { AIMessage, HumanMessage } from "langchain";

  const AGENT_URL = "http://localhost:2024";

  export function Chat() {
    const stream = useStream<typeof myAgent>({
      apiUrl: AGENT_URL,
      assistantId: "simple_agent",
    });

    return (
      <div>
        {stream.messages.map((msg) => {
          if (AIMessage.isInstance(msg)) {
            return <Markdown key={msg.id}>{msg.text}</Markdown>;
          }
          if (HumanMessage.isInstance(msg)) {
            return <p key={msg.id}>{msg.text}</p>;
          }
        })}
      </div>
    );
  }
  ```

  ```vue Vue theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  <script setup lang="ts">
  import { useStream } from "@langchain/vue";
  import { AIMessage, HumanMessage } from "langchain";

  const AGENT_URL = "http://localhost:2024";

  const stream = useStream<typeof myAgent>({
    apiUrl: AGENT_URL,
    assistantId: "simple_agent",
  });
  </script>

  <template>
    <div>
      <template v-for="msg in stream.messages.value" :key="msg.id">
        <Markdown v-if="AIMessage.isInstance(msg)">{{ msg.text }}</Markdown>
        <p v-else-if="HumanMessage.isInstance(msg)">{{ msg.text }}</p>
      </template>
    </div>
  </template>
  ```

  ```svelte Svelte theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  <script lang="ts">
    import { useStream } from "@langchain/svelte";
    import { AIMessage, HumanMessage } from "langchain";

    const AGENT_URL = "http://localhost:2024";

    const stream = useStream<typeof myAgent>({
      apiUrl: AGENT_URL,
      assistantId: "simple_agent",
    });
  </script>

  <div>
    {#each stream.messages as msg (msg.id)}
      {#if AIMessage.isInstance(msg)}
        <Markdown content={msg.text} />
      {:else if HumanMessage.isInstance(msg)}
        <p>{msg.text}</p>
      {/if}
    {/each}
  </div>
  ```

  ```ts Angular theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { Component } from "@angular/core";
  import { injectStream } from "@langchain/angular";

  const AGENT_URL = "http://localhost:2024";

  @Component({
    selector: "app-chat",
    template: `
      @for (msg of stream.messages(); track msg.id) {
        <app-markdown [content]="msg.text" />
      }
    `,
  })
  export class ChatComponent {
    stream = injectStream<typeof myAgent>({
      apiUrl: AGENT_URL,
      assistantId: "simple_agent",
    });
  }
  ```
</CodeGroup>

## Choosing a markdown library

Each framework has a natural choice for markdown rendering:

| Framework | Library                         | Output                           | Why                                                                |
| --------- | ------------------------------- | -------------------------------- | ------------------------------------------------------------------ |
| React     | `react-markdown` + `remark-gfm` | React elements                   | Component-based, virtual DOM diffing, no `dangerouslySetInnerHTML` |
| Vue       | `marked` + `dompurify`          | Sanitized HTML via `v-html`      | Lightweight, fast, GFM built-in                                    |
| Svelte    | `marked` + `dompurify`          | Sanitized HTML via `{@html}`     | Same as Vue, consistent API                                        |
| Angular   | `marked` + `dompurify`          | Sanitized HTML via `[innerHTML]` | Same as Vue/Svelte                                                 |

<Tip>
  React's `react-markdown` converts markdown directly to React elements, so it
  doesn't need HTML sanitization. There's no `dangerouslySetInnerHTML` involved.
  For Vue, Svelte, and Angular, always sanitize the parsed HTML with `dompurify`
  before rendering.
</Tip>

## Building the Markdown component

<CodeGroup>
  ```tsx React theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import ReactMarkdown from "react-markdown";
  import remarkGfm from "remark-gfm";

  export function Markdown({ children }: { children: string }) {
    return (
      <div className="markdown-content">
        <ReactMarkdown remarkPlugins={[remarkGfm]}>
          {children}
        </ReactMarkdown>
      </div>
    );
  }
  ```

  ```vue Vue theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  <script setup lang="ts">
  import { computed, useSlots } from "vue";
  import { marked } from "marked";
  import DOMPurify from "dompurify";

  marked.setOptions({ gfm: true, breaks: true });

  const slots = useSlots();

  const html = computed(() => {
    const slot = slots.default?.();
    const text = slot
      ?.map((vnode) =>
        typeof vnode.children === "string" ? vnode.children : ""
      )
      .join("") ?? "";
    if (!text) return "";
    return DOMPurify.sanitize(marked.parse(text) as string);
  });
  </script>

  <template>
    <div class="markdown-content" v-html="html" />
  </template>
  ```

  ```svelte Svelte theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  <script lang="ts">
    import { marked } from "marked";
    import DOMPurify from "dompurify";

    let { content }: { content: string } = $props();

    marked.setOptions({ gfm: true, breaks: true });

    let html = $derived.by(() => {
      if (!content) return "";
      return DOMPurify.sanitize(marked.parse(content) as string);
    });
  </script>

  <div class="markdown-content">
    {@html html}
  </div>
  ```

  ```ts Angular theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { Component, Input, computed, signal } from "@angular/core";
  import { marked } from "marked";
  import DOMPurify from "dompurify";

  marked.setOptions({ gfm: true, breaks: true });

  @Component({
    selector: "app-markdown",
    template: `<div class="markdown-content" [innerHTML]="html()"></div>`,
  })
  export class MarkdownComponent {
    @Input() set content(value: string) {
      this._content.set(value);
    }

    private _content = signal("");

    html = computed(() => {
      const text = this._content();
      if (!text) return "";
      return DOMPurify.sanitize(marked.parse(text) as string);
    });
  }
  ```
</CodeGroup>

## Sanitizing HTML output

When rendering parsed markdown as raw HTML (`v-html`, `{@html}`, `[innerHTML]`),
you must sanitize the output to prevent cross-site scripting (XSS). LLM
responses may contain arbitrary text, including markup that a markdown parser
could turn into executable HTML.

Use `dompurify` to strip dangerous elements:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import DOMPurify from "dompurify";

const safeHtml = DOMPurify.sanitize(rawHtml);
```

DOMPurify removes `<script>` tags, `onclick` attributes, `javascript:` URLs,
and other XSS vectors while preserving safe markdown output like headings,
lists, code blocks, tables, and links.

<Note>
  React's `react-markdown` does not need `dompurify` because it produces React
  elements directly, no raw HTML injection is involved.
</Note>

## Streaming considerations

`useStream` updates `msg.text` reactively as each token arrives. The markdown
component re-parses on every update. For typical chat messages, this is
performant:

* `marked` parses at \~1 MB/s. A 5 KB message takes \< 5ms
* `react-markdown` + remark pipeline is similarly fast for chat-length content
* The browser's layout engine handles the DOM update efficiently

For very long responses (> 50 KB), consider these optimizations:

* **Throttle renders:** use `requestAnimationFrame` to batch updates at 60fps
  instead of re-rendering on every token
* **Incremental parsing:** parse only new content and append to a rendered
  buffer (advanced, typically not needed for chat UIs)

<Info>
  For most chat applications, the simple approach of re-parsing the full message
  on each token is sufficient. Only optimize if you observe janky scrolling or
  dropped frames with very long messages.
</Info>

## Best practices

* **Always sanitize:** when using `v-html`, `{@html}`, or `[innerHTML]`,
  always run the parsed output through `dompurify`. Never trust raw HTML from a
  markdown parser fed with LLM output.
* **Enable GFM:** GitHub Flavored Markdown adds tables, strikethrough, task
  lists, and autolinks. These features are commonly used by LLMs.
* **Handle empty content:** check for empty strings before parsing to avoid
  rendering empty containers.
* **Use `breaks: true`:** enable line break conversion so single newlines in
  LLM output render as `<br>` rather than being ignored. LLMs often use single
  newlines for visual separation.
* **Style for chat context:** use compact margins and sizes appropriate for
  chat bubbles, not full-width article layouts.
* **Test with rich content:** verify rendering with headings, nested lists,
  code blocks with long lines, wide tables, and blockquotes to catch overflow
  or layout issues.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/frontend/markdown-messages.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Message queues
Source: https://docs.langchain.com/oss/python/langchain/frontend/message-queues

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
Source: https://docs.langchain.com/oss/python/langchain/frontend/overview

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
  ```python agent.py theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langchain import create_agent
  from langgraph.checkpoint.memory import MemorySaver

  agent = create_agent(
      model="openai:gpt-5.5",
      tools=[get_weather, search_web],
      checkpointer=MemorySaver(),
  )
  ```

  ```ts types.ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  export interface GraphState {
    messages: BaseMessage[];
  }
  ```

  ```tsx Chat.tsx theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { useStream } from "@langchain/react";
  import type { GraphState } from "./types";

  function Chat() {
    const stream = useStream<GraphState>({
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

Define a TypeScript interface that matches your agent's state schema and pass it as the type parameter:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import type { BaseMessage } from "langchain";

interface AgentState {
  messages: BaseMessage[];
}

const stream = useStream<AgentState>({
  apiUrl: "http://localhost:2024",
  assistantId: "agent",
});
```

Use the graph name from `langgraph.json` as `assistantId`. In the pattern examples throughout this guide, replace `typeof myAgent` with your interface name (for example, `AgentState`).

If your agent exposes custom state keys, extend the interface:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import type { BaseMessage, Todo } from "langchain";

interface AgentState {
  messages: BaseMessage[];
  todos: Todo[];
}
```

## Patterns

### Render messages and output

<CardGroup>
  <Card title="Markdown messages" icon="markdown" href="/oss/python/langchain/frontend/markdown-messages">
    Parse and render streamed markdown with proper formatting and code highlighting.
  </Card>

  <Card title="Structured output" icon="layout-grid" href="/oss/python/langchain/frontend/structured-output">
    Render typed agent responses as custom UI components instead of plain text.
  </Card>

  <Card title="Reasoning tokens" icon="brain" href="/oss/python/langchain/frontend/reasoning-tokens">
    Display model thinking processes in collapsible blocks.
  </Card>

  <Card title="Generative UI" icon="wand" href="/oss/python/langchain/frontend/generative-ui">
    Render AI-generated user interfaces from natural language prompts using json-render.
  </Card>
</CardGroup>

### Display agent actions

<CardGroup>
  <Card title="Tool calling" icon="tool" href="/oss/python/langchain/frontend/tool-calling">
    Show tool calls as rich, type-safe UI cards with loading and error states.
  </Card>

  <Card title="Headless tools" icon="device-desktop" href="/oss/python/langchain/frontend/headless-tools">
    Run browser and device APIs on the client while keeping typed tool schemas on the agent.
  </Card>

  <Card title="Human-in-the-loop" icon="user-check" href="/oss/python/langchain/frontend/human-in-the-loop">
    Pause the agent for human review with approve, reject, and edit workflows.
  </Card>
</CardGroup>

### Manage conversations

<CardGroup>
  <Card title="Branching chat" icon="git-branch" href="/oss/python/langchain/frontend/branching-chat">
    Edit messages, regenerate responses, and navigate conversation branches.
  </Card>

  <Card title="Message queues" icon="list-check" href="/oss/python/langchain/frontend/message-queues">
    Queue multiple messages while the agent processes them sequentially.
  </Card>
</CardGroup>

### Advanced streaming

<CardGroup>
  <Card title="Join & rejoin streams" icon="plug-connected" href="/oss/python/langchain/frontend/join-rejoin">
    Disconnect from and reconnect to running agent streams without losing progress.
  </Card>

  <Card title="Time travel" icon="clock" href="/oss/python/langchain/frontend/time-travel">
    Inspect, navigate, and resume from any checkpoint in the conversation history.
  </Card>
</CardGroup>

## Choosing a frontend pattern

Start from the UX question your application needs to answer:

| If users need to...                        | Start with                                                                                                                                                                                                          |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Understand what the agent is doing         | [Tool calling](/oss/python/langchain/frontend/tool-calling) and [reasoning tokens](/oss/python/langchain/frontend/reasoning-tokens)                                                                                 |
| Safely approve sensitive actions           | [Human-in-the-loop](/oss/python/langchain/frontend/human-in-the-loop)                                                                                                                                               |
| Send work while a run is active            | [Message queues](/oss/python/langchain/frontend/message-queues)                                                                                                                                                     |
| Leave and come back to long-running work   | [Join & rejoin streams](/oss/python/langchain/frontend/join-rejoin)                                                                                                                                                 |
| Edit or retry from an earlier turn         | [Branching chat](/oss/python/langchain/frontend/branching-chat) and [time travel](/oss/python/langchain/frontend/time-travel)                                                                                       |
| Render state as an application, not a chat | [Structured output](/oss/python/langchain/frontend/structured-output), [generative UI](/oss/python/langchain/frontend/generative-ui), and [Deep Agents frontend patterns](/oss/python/deepagents/frontend/overview) |

## Integrations

The stream API is UI-agnostic. Use it with any component library or generative UI
framework. Component libraries can own the presentation layer while LangChain's
SDK owns the agent runtime state, resumability, interrupts, and checkpoint
semantics underneath.

<CardGroup>
  <Card title="AI Elements" icon="package" href="/oss/python/langchain/frontend/integrations/ai-elements">
    Composable shadcn/ui components for AI chat: `Conversation`, `Message`, `Tool`, `Reasoning`.
  </Card>

  <Card title="assistant-ui" icon="package" href="/oss/python/langchain/frontend/integrations/assistant-ui">
    Headless React framework with built-in thread management, branching, and attachment support.
  </Card>

  <Card title="OpenUI" icon="package" href="/oss/python/langchain/frontend/integrations/openui">
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
