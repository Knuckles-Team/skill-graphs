# Structured output
Source: https://docs.langchain.com/oss/javascript/langchain/frontend/structured-output

Render structured agent responses with custom UI components instead of plain text

Structured output lets the agent return typed, machine-readable data instead of plain text. Instead of rendering a single string, you get a structured object you can map to any UI: cards, tables, charts, step-by-step breakdowns, or domain-specific renderers.

<PatternEmbed />

## What is structured output?

Instead of returning a free-form text response, the agent uses a tool call to return a structured object conforming to a predefined schema. This gives you:

* **Type-safe data**: parse the response into a known TypeScript type
* **Precise rendering control**: render each field with its own UI treatment
* **Consistent formatting**: every response follows the same structure regardless of the underlying model

The agent accomplishes this by calling a "structured output" tool whose arguments contain the response data. The tool itself doesn't execute any logic and is purely a vehicle for returning typed data.

## Use cases

* **Product comparisons**: feature tables, pros/cons lists, ratings
* **Data analysis**: summaries with metrics, breakdowns, and highlights
* **Step-by-step guides**: ordered instructions with descriptions and code snippets
* **Recipes**: ingredients, steps, timings, and nutritional info
* **Math and science**: formulas rendered with LaTeX, step-by-step derivations
* **Travel planning**: itineraries with dates, locations, and cost estimates

## Define a schema

Define a TypeScript type for the structured data the agent returns. The shape of this schema determines how you render the UI.

The following is the math-solution schema used by the embedded demo:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
interface MathSolution {
  problem: string; // The original math problem
  steps: {
    explanation: string;
    latex: string; // Optional display math for this step
  }[]; // Step-by-step derivation
  finalAnswer: string; // Plain-text final answer
  finalAnswerLatex: string; // LaTeX representation of the final answer
}
```

Your schema can be anything. The pattern works the same way regardless of shape.

## Extract structured output from messages

The structured output lives in the `tool_calls` array of the last `AIMessage`. Extract it by finding the AI message and accessing the first tool call's arguments:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { AIMessage } from "langchain";

function extractStructuredOutput<T>(messages: any[]): T | null {
  const aiMessage = messages.find(AIMessage.isInstance);
  const toolCall = aiMessage?.tool_calls?.[0];
  if (!toolCall) return null;

  return toolCall.args as T;
}
```

<Note>
  The structured output tool call may not have `args` populated until the agent finishes streaming. During streaming, `args` may be partially populated or undefined. Always check for completeness before rendering.
</Note>

## Set up `useStream`

Connect [`useStream`](https://reference.langchain.com/javascript/langchain-react/index/useStream) to your structured-output agent, then read
`stream.messages` and extract the typed payload from the latest [`AIMessage`](https://reference.langchain.com/javascript/langchain-core/messages/AIMessage)
tool call. Render your custom UI once `args` is complete, show a loading state
while `stream.isLoading` is true (tool arguments may stream in gradually), and
use `stream.submit()` to send the next prompt.

<Info>
  The code examples use `useStream<typeof myAgent>` for type-safe stream state. See Type inference for [Python](/oss/python/langchain/frontend/overview#type-inference) or [JavaScript](/oss/javascript/langchain/frontend/overview#type-inference) backends.
</Info>

<CodeGroup>
  ```tsx React theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { useStream } from "@langchain/react";
  import { AIMessage } from "langchain";

  function MathSolutionChat() {
    const stream = useStream<typeof myAgent>({
      apiUrl: "http://localhost:2024",
      assistantId: "structured_output_latex",
    });

    const solution = extractStructuredOutput<MathSolution>(stream.messages);

    return (
      <div>
        {!solution && !stream.isLoading && (
          <PromptInput onSubmit={(text) =>
            stream.submit({ messages: [{ type: "human", content: text }] })
          } />
        )}
        {stream.isLoading && <LoadingIndicator />}
        {solution && <SolutionCard solution={solution} />}
      </div>
    );
  }
  ```

  ```vue Vue theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  <script setup lang="ts">
  import { useStream } from "@langchain/vue";
  import { AIMessage } from "langchain";
  import { computed } from "vue";

  const stream = useStream<typeof myAgent>({
    apiUrl: "http://localhost:2024",
    assistantId: "structured_output_latex",
  });

  const solution = computed(() =>
    extractStructuredOutput<MathSolution>(stream.messages.value)
  );

  function handleSubmit(text: string) {
    stream.submit({ messages: [{ type: "human", content: text }] });
  }
  </script>

  <template>
    <div>
      <PromptInput v-if="!solution && !stream.isLoading" @submit="handleSubmit" />
      <LoadingIndicator v-if="stream.isLoading" />
      <SolutionCard v-if="solution" :solution="solution" />
    </div>
  </template>
  ```

  ```svelte Svelte theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  <script lang="ts">
    import { useStream } from "@langchain/svelte";
    import { AIMessage } from "langchain";

    const stream = useStream<typeof myAgent>({
      apiUrl: "http://localhost:2024",
      assistantId: "structured_output_latex",
    });

    const solution = $derived(extractStructuredOutput<MathSolution>(stream.messages));

    function handleSubmit(text: string) {
      stream.submit({ messages: [{ type: "human", content: text }] });
    }
  </script>

  <div>
    {#if !solution && !stream.isLoading}
      <PromptInput on:submit={(e) => handleSubmit(e.detail)} />
    {/if}
    {#if stream.isLoading}
      <LoadingIndicator />
    {/if}
    {#if solution}
      <SolutionCard {solution} />
    {/if}
  </div>
  ```

  ```ts Angular theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { Component, computed } from "@angular/core";
  import { injectStream } from "@langchain/angular";

  @Component({
    selector: "app-math-solution-chat",
    template: `
      @if (!solution() && !stream.isLoading()) {
        <prompt-input (onSubmit)="handleSubmit($event)" />
      }
      @if (stream.isLoading()) {
        <loading-indicator />
      }
      @if (solution()) {
        <solution-card [solution]="solution()" />
      }
    `,
  })
  export class MathSolutionChatComponent {
    stream = injectStream<typeof myAgent>({
      apiUrl: "http://localhost:2024",
      assistantId: "structured_output_latex",
    });

    solution = computed(() =>
      extractStructuredOutput<MathSolution>(this.stream.messages())
    );

    handleSubmit(text: string) {
      this.stream.submit({
        messages: [{ type: "human", content: text }],
      });
    }
  }
  ```
</CodeGroup>

## Render the structured data

Once you have a typed object, build a component that maps each field to the
appropriate UI element. This is the core of the pattern: turning structured
data into a purpose-built interface.

```tsx theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
function LatexBlock({ latex }: { latex: string }) {
  return <div className="latex-block">{latex}</div>; // Render with KaTeX or MathJax.
}

function SolutionCard({ solution }: { solution: MathSolution }) {
  return (
    <div className="solution-card">
      <h3>{solution.problem}</h3>
      <ol>
        {solution.steps.map((step, i) => (
          <li key={i}>
            <span>{step.explanation}</span>
            {step.latex && <LatexBlock latex={step.latex} />}
          </li>
        ))}
      </ol>
      <strong>{solution.finalAnswer}</strong>
      {solution.finalAnswerLatex && <LatexBlock latex={solution.finalAnswerLatex} />}
    </div>
  );
}
```

## Handle partial streaming data

During streaming, the tool call arguments may be incomplete JSON. Guard against this in your extraction logic:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
function extractStructuredOutput<T>(
  messages: any[],
  requiredFields: string[] = [],
): T | null {
  const aiMessages = messages.filter(AIMessage.isInstance);
  if (aiMessages.length === 0) return null;

  const lastAI = aiMessages[aiMessages.length - 1];
  const toolCall = lastAI.tool_calls?.[0];
  if (!toolCall?.args) return null;

  const args = toolCall.args as Record<string, unknown>;
  const hasRequired = requiredFields.every(
    (field) => args[field] !== undefined
  );

  if (requiredFields.length > 0 && !hasRequired) return null;
  return args as T;
}
```

Use the `requiredFields` parameter to wait until critical fields are populated before rendering:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const solution = extractStructuredOutput<MathSolution>(stream.messages, [
  "problem",
  "steps",
  "finalAnswer",
]);
```

## Render progressively during streaming

Rather than waiting for the complete structured output, render fields as they arrive. This gives users immediate feedback while the agent is still generating:

```tsx theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
function ProgressiveSolutionCard({ messages }: { messages: any[] }) {
  const partial = extractStructuredOutput<Partial<MathSolution>>(messages);
  if (!partial) return null;

  return (
    <div className="solution-card">
      {partial.problem && <h3>{partial.problem}</h3>}

      {partial.steps && partial.steps.length > 0 && (
        <div className="solution-steps">
          <h4>Steps</h4>
          {partial.steps.map((step, i) => (
            <div key={i} className="step">
              <div className="step-number">Step {i + 1}</div>
              <p>{step.explanation}</p>
              {step.latex && <LatexBlock latex={step.latex} />}
            </div>
          ))}
        </div>
      )}

      {partial.finalAnswer && <strong>{partial.finalAnswer}</strong>}
    </div>
  );
}
```

<Tip>
  Progressive rendering works well when the schema has a natural top-to-bottom
  order: problem, then derivation steps, then final answer. The agent typically
  generates fields in schema order, so the UI fills in naturally.
</Tip>

## Best practices

* **Validate before rendering**: always check that required fields exist before rendering, since streaming may deliver partial data
* **Use a generic extraction function**: parameterize your extraction logic with a type and required fields so it works across different schemas
* **Render progressively**: show fields as they arrive rather than waiting for the complete object, so users see immediate feedback
* **Provide fallback representations**: if a field supports rich rendering (LaTeX, Markdown, charts), also include a plain-text equivalent in your schema as a fallback
* **Keep schemas flat when possible**: deeply nested schemas are harder to render progressively and more likely to break during partial streaming
* **Match UI to data**: choose the rendering strategy that best represents each field type (tables for arrays, cards for nested objects, badges for status fields)

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/frontend/structured-output.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Time travel
Source: https://docs.langchain.com/oss/javascript/langchain/frontend/time-travel

Inspect, navigate, and resume from any checkpoint in the conversation history

Every state change in a LangGraph agent creates a **checkpoint**, a complete
snapshot of the agent's state at that moment. Time travel lets you inspect any
checkpoint, view the exact state the agent held, and **resume execution from
that point** to explore alternative paths. It's a debugger, an undo button, and
an audit log all in one.

<PatternEmbed />

<Note>
  This feature requires the [LangGraph Agent Server](../langgraph/local-server). Run your agent locally with `langgraph dev` or [deploy it to LangSmith](/langsmith/deployment) to use this pattern.
</Note>

## How checkpoints work

LangGraph persists agent state after every node execution. Each persisted state
is a [ThreadState](https://reference.langchain.com/javascript/langchain-langgraph-sdk/index/ThreadState) object that captures:

* **checkpoint**: metadata identifying this specific snapshot (ID, timestamp)
* **values**: the full agent state at this point (messages, custom keys)
* **tasks**: the graph nodes that were scheduled to run next
* **next**: the names of upcoming nodes in the execution plan

This creates a linear timeline of every decision the agent made, every tool it
called, and every response it produced. Your UI can render this timeline and let
users jump to any point.

## Setting up `useStream`

Create the stream for your agent, then fetch checkpoint history explicitly from
the LangGraph client for the active thread. Resuming from a checkpoint uses
`forkFrom: { checkpointId }`.

<Info>
  The code examples use `useStream<typeof myAgent>` for type-safe stream state. See Type inference for [Python](/oss/python/langchain/frontend/overview#type-inference) or [JavaScript](/oss/javascript/langchain/frontend/overview#type-inference) backends.
</Info>

<CodeGroup>
  ```tsx React theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { useStream } from "@langchain/react";
  import { useEffect, useState } from "react";

  const AGENT_URL = "http://localhost:2024";

  export function TimeTravelChat() {
    const [threadId, setThreadId] = useState<string | null>(null);
    const [history, setHistory] = useState<ThreadState[]>([]);
    const stream = useStream<typeof myAgent>({
      apiUrl: AGENT_URL,
      assistantId: "time_travel",
      threadId,
      onThreadId: setThreadId,
    });

    useEffect(() => {
      if (!threadId || stream.isLoading) return;
      stream.client.threads.getHistory(threadId).then(setHistory);
    }, [stream.client, threadId, stream.isLoading]);

    function resumeFrom(cp: ThreadState) {
      stream.submit({}, {
        forkFrom: { checkpointId: cp.checkpoint.checkpoint_id },
      });
    }

    return (
      <div className="flex h-screen">
        <ChatPanel messages={stream.messages} />
        <TimelineSidebar history={history} onSelect={resumeFrom} />
      </div>
    );
  }
  ```

  ```vue Vue theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  <script setup lang="ts">
  import { useStream } from "@langchain/vue";
  import { ref, watch } from "vue";

  const AGENT_URL = "http://localhost:2024";
  const threadId = ref<string | null>(null);
  const history = ref<ThreadState[]>([]);

  const stream = useStream<typeof myAgent>({
    apiUrl: AGENT_URL,
    assistantId: "time_travel",
    threadId,
    onThreadId: (id) => (threadId.value = id),
  });

  watch(
    [threadId, stream.isLoading],
    async ([id, isLoading]) => {
      if (isLoading) return;
      history.value = id
        ? ((await stream.client.threads.getHistory(id)) as ThreadState[])
        : [];
    },
    { immediate: true },
  );

  function resumeFrom(cp: ThreadState) {
    stream.submit({}, {
      forkFrom: { checkpointId: cp.checkpoint.checkpoint_id },
    });
  }
  </script>

  <template>
    <div class="flex h-screen">
      <ChatPanel :messages="stream.messages.value" />
      <TimelineSidebar :history="history" @select="resumeFrom" />
    </div>
  </template>
  ```

  ```svelte Svelte theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  <script lang="ts">
    import { useStream } from "@langchain/svelte";

    const AGENT_URL = "http://localhost:2024";
    let threadId = $state<string | null>(null);
    let history = $state<ThreadState[]>([]);

    const stream = useStream<typeof myAgent>({
      apiUrl: AGENT_URL,
      assistantId: "time_travel",
      threadId: () => threadId,
      onThreadId: (id) => (threadId = id),
    });

    $effect(() => {
      if (!threadId) {
        history = [];
        return;
      }
      if (stream.isLoading) return;
      stream.client.threads.getHistory(threadId).then((states) => {
        history = states as ThreadState[];
      });
    });

    function resumeFrom(cp: ThreadState) {
      stream.submit({}, {
        forkFrom: { checkpointId: cp.checkpoint.checkpoint_id },
      });
    }
  </script>

  <div class="flex h-screen">
    <ChatPanel messages={stream.messages} />
    <TimelineSidebar {history} onSelect={resumeFrom} />
  </div>
  ```

  ```ts Angular theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { Component, effect, signal } from "@angular/core";
  import { injectStream } from "@langchain/angular";

  const AGENT_URL = "http://localhost:2024";

  @Component({
    selector: "app-time-travel-chat",
    template: `
      <div class="flex h-screen">
        <app-chat-panel [messages]="stream.messages()" />
        <app-timeline-sidebar
          [history]="history()"
          (select)="resumeFrom($event)"
        />
      </div>
    `,
  })
  export class TimeTravelChatComponent {
    threadId = signal<string | null>(null);
    history = signal<ThreadState[]>([]);

    stream = injectStream<typeof myAgent>({
      apiUrl: AGENT_URL,
      assistantId: "time_travel",
      threadId: this.threadId,
      onThreadId: (id) => this.threadId.set(id),
    });

    constructor() {
      effect(() => {
        if (this.stream.isLoading()) return;
        void this.refreshHistory(this.threadId());
      });
    }

    async refreshHistory(id: string | null) {
      this.history.set(id
        ? ((await this.stream.client.threads.getHistory(id)) as ThreadState[])
        : []);
    }

    resumeFrom(cp: ThreadState) {
      this.stream.submit({}, {
        forkFrom: { checkpointId: cp.checkpoint.checkpoint_id },
      });
    }
  }
  ```
</CodeGroup>

## Building a checkpoint timeline

The timeline sidebar shows every checkpoint as a clickable entry. Each entry
displays the node that ran and how many messages existed at that point:

```tsx theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
function TimelineSidebar({
  history,
  onSelect,
}: {
  history: ThreadState[];
  onSelect: (cp: ThreadState) => void;
}) {
  return (
    <aside className="w-80 overflow-y-auto border-l bg-gray-50 p-4">
      <h2 className="mb-4 text-sm font-semibold uppercase text-gray-500">
        Checkpoint Timeline
      </h2>
      <div className="space-y-2">
        {history.map((cp, i) => {
          const taskName = cp.tasks?.[0]?.name ?? "unknown";
          const msgCount = (cp.values?.messages as unknown[])?.length ?? 0;

          return (
            <button
              key={cp.checkpoint.checkpoint_id}
              onClick={() => onSelect(cp)}
              className="w-full rounded-lg border bg-white p-3 text-left
                         hover:border-blue-400 hover:shadow-sm transition-all"
            >
              <div className="flex items-center justify-between">
                <span className="text-xs text-gray-400">#{i + 1}</span>
                <NodeBadge name={taskName} />
              </div>
              <p className="mt-1 text-sm font-medium">{taskName}</p>
              <p className="text-xs text-gray-500">
                {msgCount} message{msgCount !== 1 ? "s" : ""}
              </p>
            </button>
          );
        })}
      </div>
    </aside>
  );
}
```

## Inspecting checkpoint state

Clicking a checkpoint should show the full state at that point. A JSON viewer
gives developers complete visibility into what the agent knew and decided:

```tsx theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
function CheckpointInspector({ checkpoint }: { checkpoint: ThreadState }) {
  const [expanded, setExpanded] = useState(false);

  return (
    <div className="rounded-lg border bg-white p-4">
      <div className="flex items-center justify-between">
        <h3 className="font-semibold">
          Checkpoint {checkpoint.checkpoint.checkpoint_id.slice(0, 8)}...
        </h3>
        <button
          onClick={() => setExpanded(!expanded)}
          className="text-sm text-blue-600 hover:underline"
        >
          {expanded ? "Collapse" : "Expand"} state
        </button>
      </div>

      <div className="mt-2 space-y-1 text-sm">
        <p>
          <strong>Node:</strong>{" "}
          {checkpoint.tasks?.[0]?.name ?? "—"}
        </p>
        <p>
          <strong>Next:</strong>{" "}
          {checkpoint.next?.join(", ") || "—"}
        </p>
        <p>
          <strong>Messages:</strong>{" "}
          {(checkpoint.values?.messages as unknown[])?.length ?? 0}
        </p>
      </div>

      {expanded && (
        <div className="mt-3 max-h-96 overflow-auto rounded bg-gray-900 p-3">
          <pre className="text-xs text-gray-200">
            {JSON.stringify(checkpoint.values, null, 2)}
          </pre>
        </div>
      )}
    </div>
  );
}
```

<Tip>
  For production UIs, consider using a proper JSON viewer component with
  collapsible nodes instead of raw `JSON.stringify`. Libraries like
  `react-json-view` or `react-json-tree` give users a much better exploration
  experience.
</Tip>

## Resuming from a checkpoint

The core of time travel is the ability to **resume execution from any prior
checkpoint**. When a user selects a checkpoint, call `submit` with `null` input
and pass the checkpoint ID:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
stream.submit({}, {
  forkFrom: { checkpointId: selectedCheckpoint.checkpoint.checkpoint_id },
});
```

This tells LangGraph to:

1. Roll back to the selected checkpoint's state
2. Re-execute the graph from that point forward
3. Stream the new results to the client

The existing messages after the selected checkpoint are replaced by the new
execution path. This effectively creates a **branch** in the conversation
timeline.

<Note>
  Resuming from a checkpoint does not delete the original timeline. The previous
  checkpoints remain available in the history. This means users can always go back
  and try a different path without losing any prior work.
</Note>

## The SplitView layout

Time travel works best with a split layout, with the main chat on the left and the
timeline on the right:

```tsx theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
function TimeTravelLayout() {
  const [threadId, setThreadId] = useState<string | null>(null);
  const [history, setHistory] = useState<ThreadState[]>([]);
  const stream = useStream<typeof myAgent>({
    apiUrl: AGENT_URL,
    assistantId: "time_travel",
    threadId,
    onThreadId: setThreadId,
  });

  const [selectedCheckpoint, setSelectedCheckpoint] =
    useState<ThreadState | null>(null);

  useEffect(() => {
    if (!threadId || stream.isLoading) return;
    stream.client.threads.getHistory(threadId).then(setHistory);
  }, [stream.client, threadId, stream.isLoading]);

  return (
    <div className="flex h-screen">
      {/* Main chat area */}
      <main className="flex-1 overflow-y-auto p-6">
        <div className="mx-auto max-w-2xl space-y-4">
          {stream.messages.map((msg) => (
            <Message key={msg.id} message={msg} />
          ))}
        </div>
        <ChatInput
          onSubmit={(text) =>
            stream.submit({ messages: [{ type: "human", content: text }] })
          }
          isLoading={stream.isLoading}
        />
      </main>

      {/* Timeline sidebar */}
      <aside className="w-96 overflow-y-auto border-l bg-gray-50">
        <TimelineSidebar
          history={history}
          selected={selectedCheckpoint}
          onSelect={setSelectedCheckpoint}
          onResume={(cp) =>
            stream.submit({}, {
              forkFrom: { checkpointId: cp.checkpoint.checkpoint_id },
            })
          }
        />
        {selectedCheckpoint && (
          <CheckpointInspector checkpoint={selectedCheckpoint} />
        )}
      </aside>
    </div>
  );
}
```

## Extracting checkpoint metadata

Transform raw checkpoint data into display-friendly entries for your timeline:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
function formatCheckpoints(history: ThreadState[]) {
  return history.map((cp, index) => ({
    index,
    id: cp.checkpoint?.checkpoint_id,
    taskName: cp.tasks?.[0]?.name ?? "unknown",
    messageCount: (cp.values?.messages as unknown[])?.length ?? 0,
    hasInterrupts: cp.tasks?.some((t) => t.interrupts?.length) ?? false,
    nextNodes: cp.next ?? [],
  }));
}
```

This makes it easy to render timeline entries with meaningful labels instead of
raw IDs.

## Use cases

Time travel is invaluable across many scenarios:

* **Debugging agent behavior**: step through the agent's decisions to
  understand why it chose a particular path
* **Undoing actions**: if the agent took a wrong turn, resume from an earlier
  checkpoint and try again
* **Exploring alternatives**: fork from a mid-conversation checkpoint to see
  how different inputs change the outcome
* **Auditing**: review the complete history of an agent's actions for
  compliance, quality assurance, or post-incident analysis
* **Teaching**: walk through an agent's execution step by step to explain how
  multi-step reasoning works

<Info>
  Time travel is especially powerful when combined with
  [human-in-the-loop](/oss/javascript/langchain/frontend/human-in-the-loop) patterns. If a human reviewer
  rejects an agent's action at an interrupt, they can resume from the checkpoint
  before the action was taken and provide corrective input.
</Info>

## Handling interrupts in the timeline

Checkpoints that contain interrupts (human-in-the-loop pauses) deserve special
visual treatment. They represent moments where the agent stopped and waited for
human input:

```tsx theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
function TimelineEntry({
  checkpoint,
  index,
}: {
  checkpoint: ThreadState;
  index: number;
}) {
  const hasInterrupt = checkpoint.tasks?.some(
    (t) => t.interrupts && t.interrupts.length > 0
  );

  return (
    <div
      className={`rounded-lg border p-3 ${
        hasInterrupt
          ? "border-amber-300 bg-amber-50"
          : "border-gray-200 bg-white"
      }`}
    >
      <div className="flex items-center gap-2">
        <span className="text-xs text-gray-400">#{index + 1}</span>
        {hasInterrupt && (
          <span className="rounded bg-amber-200 px-1.5 py-0.5 text-xs font-medium text-amber-800">
            Interrupt
          </span>
        )}
      </div>
      <p className="mt-1 text-sm font-medium">
        {checkpoint.tasks?.[0]?.name ?? "—"}
      </p>
    </div>
  );
}
```

## Best practices

* **Load history lazily**: for threads with hundreds of checkpoints, paginate
  or load only the most recent N entries to keep the UI responsive.
* **Show meaningful labels**: display node names and message counts instead of
  raw checkpoint IDs. Users need context, not UUIDs.
* **Confirm before resuming**: resuming from an old checkpoint replaces the
  current execution path. Show a confirmation dialog so users don't
  accidentally lose the current conversation state.
* **Highlight the current checkpoint**: make it visually obvious which
  checkpoint corresponds to the current state of the conversation.
* **Support keyboard navigation**: power users will want to step through
  checkpoints with arrow keys. Add keyboard handlers to the timeline for a
  smooth debugging experience.
* **Diff state between checkpoints**: for advanced users, showing what changed
  between two consecutive checkpoints can reveal exactly how the agent's state
  evolved at each step.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/frontend/time-travel.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Tool calling
Source: https://docs.langchain.com/oss/javascript/langchain/frontend/tool-calling

Display agent tool calls with rich, type-safe UI cards

Agents can invoke external tools like weather APIs, calculators, web search,
database queries, and more. The results are in raw JSON. This pattern shows you
how to render
structured, type-safe UI cards for every tool call your agent makes, complete
with loading states and error handling.

<PatternEmbed />

## How tool calling works

When a LangGraph agent decides it needs external data, it emits one or more
**tool calls** as part of an AI message. Each tool call includes:

* **name**: the tool being invoked (e.g. `"get_weather"`, `"calculator"`)
* **args**: the structured arguments passed to the tool
* **id**: a unique identifier linking the call to its result

The agent runtime executes the tool, and the result comes back as a
`ToolMessage`. The [`useStream`](https://reference.langchain.com/javascript/langchain-react/index/useStream) hook unifies all of this into a single
`toolCalls` array you can render directly.

## Setting up `useStream`

The first step is wiring up [`useStream`](https://reference.langchain.com/javascript/langchain-react/index/useStream) to your agent backend. The hook returns
reactive state including a `toolCalls` array that updates in real time as the
agent streams.

<Info>
  The code examples use `useStream<typeof myAgent>` for type-safe stream state. See Type inference for [Python](/oss/python/langchain/frontend/overview#type-inference) or [JavaScript](/oss/javascript/langchain/frontend/overview#type-inference) backends.
</Info>

<CodeGroup>
  ```tsx React theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { useStream } from "@langchain/react";

  const AGENT_URL = "http://localhost:2024";

  export function Chat() {
    const stream = useStream<typeof myAgent>({
      apiUrl: AGENT_URL,
      assistantId: "tool_calling",
    });

    return (
      <div>
        {stream.messages.map((msg) => (
          <Message key={msg.id} message={msg} toolCalls={stream.toolCalls} />
        ))}
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
    assistantId: "tool_calling",
  });
  </script>

  <template>
    <div>
      <Message
        v-for="msg in stream.messages.value"
        :key="msg.id"
        :message="msg"
        :tool-calls="stream.toolCalls.value"
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
      assistantId: "tool_calling",
    });
  </script>

  <div>
    {#each stream.messages as msg (msg.id)}
      <Message message={msg} toolCalls={stream.toolCalls} />
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
        <app-message [message]="msg" [toolCalls]="stream.toolCalls()" />
      }
    `,
  })
  export class ChatComponent {
    stream = injectStream<typeof myAgent>({
      apiUrl: AGENT_URL,
      assistantId: "tool_calling",
    });
  }
  ```
</CodeGroup>

## The AssembledToolCall type

Each entry in the `toolCalls` array is an `AssembledToolCall` object:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
interface AssembledToolCall<
  TName extends string = string,
  TInput = unknown,
  TOutput = unknown,
> {
  name: TName;
  callId: string;
  id: string;
  namespace: string[];
  input: TInput;
  args: TInput;
  output: TOutput | null;
  status: "running" | "finished" | "error";
  error: string | undefined;
}
```

| Property    | Description                                                                    |
| ----------- | ------------------------------------------------------------------------------ |
| `name`      | The name of the tool (e.g. `"get_weather"`)                                    |
| `callId`    | Unique ID matching the AI message's `tool_calls` entry                         |
| `id`        | Alias for `callId`, matching message-level tool calls                          |
| `namespace` | Namespace where the tool call was emitted                                      |
| `input`     | Structured arguments the agent passed to the tool                              |
| `args`      | Alias for `input`, matching message-level tool calls                           |
| `output`    | Tool output after a successful call, or `null` while running or after an error |
| `status`    | Lifecycle state: `"running"`, `"finished"`, or `"error"`                       |
| `error`     | Error details when the tool call fails                                         |

## Filtering tool calls per message

An AI message may trigger multiple tool calls, and your chat may contain many AI
messages. To render the right tool cards under each message, filter by matching
`callId` against the message's `tool_calls` array:

```tsx theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
function Message({
  message,
  toolCalls,
}: {
  message: AIMessage;
  toolCalls: AssembledToolCall[];
}) {
  const messageToolCalls = toolCalls.filter((tc) =>
    message.tool_calls?.find((t) => t.id === tc.callId)
  );

  return (
    <div>
      <p>{message.text}</p>
      {messageToolCalls.map((tc) => (
        <ToolCard key={tc.callId} toolCall={tc} />
      ))}
    </div>
  );
}
```

## Building specialized tool cards

Rather than dumping raw JSON, build dedicated UI components for each tool. Use
`name` to select the right card:

```tsx theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
function ToolCard({ toolCall }: { toolCall: AssembledToolCall }) {
  if (toolCall.status === "running") {
    return <LoadingCard name={toolCall.name} />;
  }

  if (toolCall.status === "error") {
    return <ErrorCard name={toolCall.name} error={toolCall.error} />;
  }

  switch (toolCall.name) {
    case "get_weather":
      return <WeatherCard input={toolCall.input} output={toolCall.output} />;
    case "calculator":
      return (
        <CalculatorCard input={toolCall.input} output={toolCall.output} />
      );
    case "web_search":
      return <SearchCard input={toolCall.input} output={toolCall.output} />;
    default:
      return <GenericToolCard toolCall={toolCall} />;
  }
}
```

### Weather card example

```tsx theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
function WeatherCard({
  input,
  output,
}: {
  input: { location: string };
  output: { temperature: number; condition: string };
}) {
  return (
    <div className="rounded-lg border p-4">
      <div className="flex items-center gap-2">
        <CloudIcon />
        <h3 className="font-semibold">{input.location}</h3>
      </div>
      <div className="mt-2 text-3xl font-bold">{output.temperature}°F</div>
      <p className="text-muted-foreground">{output.condition}</p>
    </div>
  );
}
```

### Loading and error states

Always handle the pending and error states to give users clear feedback:

```tsx theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
function LoadingCard({ name }: { name: string }) {
  return (
    <div className="flex items-center gap-2 rounded-lg border p-4 animate-pulse">
      <Spinner />
      <span>Running {name}...</span>
    </div>
  );
}

function ErrorCard({ name, error }: { name: string; error?: unknown }) {
  return (
    <div className="rounded-lg border border-red-300 bg-red-50 p-4">
      <h3 className="font-semibold text-red-700">Error in {name}</h3>
      <p className="text-sm text-red-600">
        {String(error ?? "Tool execution failed")}
      </p>
    </div>
  );
}
```

## Type-safe tool arguments

If your tools are defined with structured schemas, you can use the
`ToolCallFromTool` utility type to get fully typed `args`:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { tool } from "@langchain/core/tools";
import { z } from "zod";

const getWeather = tool(async ({ location }) => { /* ... */ }, {
  name: "get_weather",
  description: "Get the current weather for a location",
  schema: z.object({
    location: z.string().describe("City name"),
  }),
});

type WeatherToolCall = ToolCallFromTool<typeof getWeather>;
// WeatherToolCall.input and WeatherToolCall.args are now { location: string }
```

<Tip>
  Using `ToolCallFromTool` gives you compile-time safety. If the tool schema
  changes, your UI components will flag type errors immediately.
</Tip>

## Rendering tool calls inline with streaming text

Tool calls often arrive interleaved with streamed text. The [`useStream`](https://reference.langchain.com/javascript/langchain-react/index/useStream) hook
keeps `toolCalls` in sync with the stream, so pending cards appear as soon as
the agent emits the call, before the tool has finished executing.

This means users see:

1. The AI's text as it streams in
2. A loading card the moment a tool call is emitted
3. The card updates to show the result once the tool completes

<Note>
  Tool calls update in place. The same `callId` transitions from `"running"` to
  `"finished"` (or `"error"`), so your UI re-renders the same component
  with new state.
</Note>

## Handling multiple concurrent tool calls

Agents can invoke several tools in parallel. The `toolCalls` array will contain
multiple entries with `status: "running"` simultaneously. Each resolves
independently, so your UI should handle partial completion gracefully:

```tsx theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
function ToolCallList({ toolCalls }: { toolCalls: AssembledToolCall[] }) {
  const pending = toolCalls.filter((tc) => tc.status === "running");
  const completed = toolCalls.filter((tc) => tc.status === "finished");

  return (
    <div className="space-y-2">
      {completed.map((tc) => (
        <ToolCard key={tc.callId} toolCall={tc} />
      ))}
      {pending.map((tc) => (
        <LoadingCard key={tc.callId} name={tc.name} />
      ))}
    </div>
  );
}
```

## Best practices

Follow these guidelines when building tool call UIs:

* **Always handle all three states**: `running`, `finished`, and `error`.
  Users should never see a blank card.
* **Validate results safely**. Tool outputs are typed as `unknown` until you
  narrow them for a specific card.
* **Provide a generic fallback**. Not every tool needs a bespoke card. Render
  a collapsible JSON view for unknown tool names.
* **Show the tool name and args during loading**. Users want to know *what*
  the agent is doing, even before the result arrives.
* **Keep cards compact**. Tool cards sit inline with chat messages. Avoid
  overwhelming the conversation with oversized widgets.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/frontend/tool-calling.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Get help
Source: https://docs.langchain.com/oss/javascript/langchain/get-help

Connect with the LangChain community, access learning resources, and get the support you need to build with confidence.

## Learning resources

Start your journey or deepen your knowledge with our comprehensive learning materials.

* **[Chat LangChain](https://chat.langchain.com/)**: Ask the docs anything about LangChain, powered by real-time docs
* **[API Reference](https://reference.langchain.com/python/)**: Complete documentation for all LangChain packages

## Community support

Get help from fellow developers and the LangChain team through our active community channels.

* **[Community Forum](https://forum.langchain.com/)**: Ask questions, share solutions, and discuss best practices
* **[Community Slack](https://www.langchain.com/join-community)**: Connect with other builders and get quick help

## Professional support

For enterprise needs and critical applications, access dedicated support channels.

* **[Support portal](https://support.langchain.com/)**: Submit tickets and track support requests
* **[LangSmith status](https://status.smith.langchain.com/)**: Real-time status of LangSmith services and APIs

## Contribute

Help us improve LangChain for everyone. Whether you're fixing bugs, adding features, or improving documentation, we welcome your contributions.

* **[Contributing Guide](/oss/javascript/contributing/overview)**: Everything you need to know about contributing to LangChain

## Stay connected

Follow us for the latest updates, announcements, and community highlights.

* **[X (Twitter)](https://x.com/langchain)**: Daily updates and community spotlights
* **[LinkedIn](https://www.linkedin.com/company/langchain/)**: Professional network and company updates

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/get-help.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
