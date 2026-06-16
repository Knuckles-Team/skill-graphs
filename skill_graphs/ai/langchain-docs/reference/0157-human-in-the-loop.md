# Human-in-the-Loop
Source: https://docs.langchain.com/oss/javascript/langchain/frontend/human-in-the-loop

Add approval workflows with interrupt-based human review

Not every agent action should run unsupervised. When an agent is about to send
an email, delete a record, execute a financial transaction, or perform any
irreversible operation, you need a human to review and approve the action first.
The Human-in-the-Loop (HITL) pattern lets your agent pause execution, present
the pending action to the user, and resume only after explicit approval.

Because HITL is built on LangGraph interrupts and checkpoints, the pause is
durable. A user can refresh the page, a reviewer can answer from a different
component, and the agent still resumes from the exact point where execution
stopped instead of replaying the whole run.

<PatternEmbed />

## How interrupts work

LangGraph agents support **interrupts**, explicit pause points where the agent
yields control back to the client. When the agent hits an interrupt:

1. The agent stops executing and emits an interrupt payload
2. The [`useStream`](https://reference.langchain.com/javascript/langchain-react/index/useStream) hook surfaces the interrupt via `stream.interrupt`
3. Your UI renders a review card with approve/reject/edit options
4. The user makes a decision
5. Your code calls `stream.submit()` with a resume command
6. The agent picks up where it left off

The frontend SDK keeps the interrupt alongside the rest of the thread state, so
your UI can render it wherever it makes sense: inline in the transcript, in a
review queue, in an admin dashboard, or in a modal that blocks the next user
action until the decision is made.

## Setting up `useStream`

Connect [`useStream`](https://reference.langchain.com/javascript/langchain-react/index/useStream) to your human-in-the-loop agent. When the graph hits an
interrupt, the hook exposes the pending payload on `stream.interrupt`. Render an
approval card while that value is set, then resume the run with
`stream.submit(null, { command: { resume: response } })` after the user
approves, rejects, or edits the action.

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
      assistantId: "human_in_the_loop",
    });

    const interrupt = stream.interrupt;

    return (
      <div>
        {stream.messages.map((msg) => (
          <Message key={msg.id} message={msg} />
        ))}
        {interrupt && (
          <ApprovalCard
            interrupt={interrupt}
            onRespond={(response) =>
              stream.submit(null, { command: { resume: response } })
            }
          />
        )}
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
    assistantId: "human_in_the_loop",
  });

  function handleRespond(response: HITLResponse) {
    stream.submit(null, { command: { resume: response } });
  }
  </script>

  <template>
    <div>
      <Message
        v-for="msg in stream.messages.value"
        :key="msg.id"
        :message="msg"
      />
      <ApprovalCard
        v-if="stream.interrupt.value"
        :interrupt="stream.interrupt.value"
        @respond="handleRespond"
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
      assistantId: "human_in_the_loop",
    });

    function handleRespond(response: HITLResponse) {
      stream.submit(null, { command: { resume: response } });
    }
  </script>

  <div>
    {#each stream.messages as msg (msg.id)}
      <Message message={msg} />
    {/each}

    {#if stream.interrupt}
      <ApprovalCard interrupt={stream.interrupt} onRespond={handleRespond} />
    {/if}
  </div>
  ```

  ```ts Angular theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { Component } from "@angular/core";
  import { injectStream } from "@langchain/angular";
  import type { HITLResponse } from "langchain";

  const AGENT_URL = "http://localhost:2024";

  @Component({
    selector: "app-chat",
    template: `
      @for (msg of stream.messages(); track msg.id) {
        <app-message [message]="msg" />
      }
      @if (stream.interrupt()) {
        <app-approval-card
          [interrupt]="stream.interrupt()"
          (respond)="handleRespond($event)"
        />
      }
    `,
  })
  export class ChatComponent {
    stream = injectStream<typeof myAgent>({
      apiUrl: AGENT_URL,
      assistantId: "human_in_the_loop",
    });

    handleRespond(response: HITLResponse) {
      this.stream.submit(null, { command: { resume: response } });
    }
  }
  ```
</CodeGroup>

## The interrupt payload

When the agent pauses, `stream.interrupt` contains a [HITLRequest](https://reference.langchain.com/javascript/langchain/index/HITLRequest) with the
following structure:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
interface HITLRequest {
  actionRequests: ActionRequest[];
  reviewConfigs: ReviewConfig[];
}

interface ActionRequest {
  name: string;
  args: Record<string, unknown>;
  description?: string;
}

interface ReviewConfig {
  allowedDecisions: ("approve" | "reject" | "edit" | "respond")[];
}
```

| Property                           | Description                                                           |
| ---------------------------------- | --------------------------------------------------------------------- |
| `actionRequests`                   | Array of pending actions the agent wants to perform                   |
| `actionRequests[].name`            | The action name (e.g. `"send_email"`, `"delete_record"`)              |
| `actionRequests[].args`            | Structured arguments for the action                                   |
| `actionRequests[].description`     | Optional human-readable description of what the action does           |
| `reviewConfigs`                    | Per-action configuration controlling which decisions are allowed      |
| `reviewConfigs[].allowedDecisions` | Which buttons to show: `"approve"`, `"reject"`, `"edit"`, `"respond"` |

## Decision types

The HITL pattern supports four decision types:

### Approve

The user confirms the action should proceed as-is:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const response: HITLResponse = {
  decisions: [{ type: "approve" }],
};

stream.submit(null, { command: { resume: response } });
```

### Reject

The user denies the action with an optional reason. The tool is not executed:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const response: HITLResponse = {
  decisions: [
    {
      type: "reject",
      message: "The email tone is too aggressive. Do not send it.",
    },
  ],
};

stream.submit(null, { command: { resume: response } });
```

<Note>
  When an action is rejected, the agent receives the rejection reason and can
  decide how to proceed. If you omit `message`, the backend uses a default
  message that tells the model the tool was not executed and not to retry the
  same tool call unless the user asks. For side-effecting tools, pass a clear
  message that tells the agent whether to abandon the action, ask a follow-up
  question, or try a safer alternative.
</Note>

### Edit

The user modifies the action's arguments before approving:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const response: HITLResponse = {
  decisions: [
    {
      type: "edit",
      editedAction: {
        name: actionRequest.name,
        args: {
          ...actionRequest.args,
          subject: "Updated subject line",
          body: "Revised email body with softer language.",
        },
      },
    },
  ],
};

stream.submit(null, { command: { resume: response } });
```

### Respond

The user provides a direct reply for "ask user" style tools. The `message` becomes the tool result and the tool itself is not executed:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const response: HITLResponse = {
  decisions: [{ type: "respond", message: "Blue." }],
};

stream.submit(null, { command: { resume: response } });
```

<Note>
  Use `respond` when the tool is intentionally a placeholder for human input, for example, an `ask_user` tool that prompts the agent to collect information from the user. Do not use `respond` to deny a proposed action, because it is returned to the model as a successful tool result.
</Note>

## Building the ApprovalCard

Here is the decision wiring used by the approval cards. The UI can split each
action into its own card, but the resume payload is a single `HITLResponse`
with one decision per pending action:

```tsx theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
async function approveAll() {
  const resume: HITLResponse = {
    decisions: actionRequests.map(() => ({ type: "approve" })),
  };
  await stream.submit(null, { command: { resume } });
}

async function rejectOne(index: number, message: string) {
  const resume: HITLResponse = {
    decisions: actionRequests.map((_, i) =>
      i === index
        ? { type: "reject", message }
        : { type: "reject", message: "Rejected along with other actions" },
    ),
  };
  await stream.submit(null, { command: { resume } });
}

async function editOne(index: number, editedArgs: Record<string, unknown>) {
  const originalAction = actionRequests[index];
  const resume: HITLResponse = {
    decisions: actionRequests.map((_, i) =>
      i === index
        ? {
            type: "edit",
            editedAction: { name: originalAction.name, args: editedArgs },
          }
        : { type: "approve" },
    ),
  };
  await stream.submit(null, { command: { resume } });
}
```

## The resume flow

After the user makes a decision, the full cycle looks like this:

1. Call `stream.submit(null, { command: { resume: hitlResponse } })`
2. The [`useStream`](https://reference.langchain.com/javascript/langchain-react/index/useStream) hook sends the resume command to the LangGraph backend
3. The agent receives the `HITLResponse` and continues execution. Each entry in
   `decisions` may be one of:
   * `{ type: "approve" }`: The agent continues executing the action
   * `{ type: "reject", message }`: The tool is not executed, and the agent receives the rejection message before deciding its next step
   * `{ type: "edit", editedAction }`: The agent runs the tool with edited arguments
   * `{ type: "respond", message }`: The human's message is returned directly as the tool result without executing the tool
4. The `interrupt` property resets to `null` as the agent resumes streaming

<Tip>
  You can chain multiple HITL checkpoints in a single agent run. For example, an
  agent might ask for approval to search, then ask again before sending an email
  with the results. Each interrupt is handled independently.
</Tip>

## Handling multiple pending actions

An interrupt can contain multiple `actionRequests` when the agent wants to
perform several actions at once. Render a card for each and collect all
decisions before resuming:

```tsx theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
function MultiActionReview({
  interrupt,
  onRespond,
}: {
  interrupt: { value: HITLRequest };
  onRespond: (response: HITLResponse) => void;
}) {
  const [decisions, setDecisions] = useState<Record<number, HITLResponse["decisions"][number]>>({});
  const request = interrupt.value;

  const allDecided =
    Object.keys(decisions).length === request.actionRequests.length;

  return (
    <div className="space-y-4">
      {request.actionRequests.map((action, i) => (
        <SingleActionCard
          key={i}
          action={action}
          config={request.reviewConfigs[i]}
          onDecide={(response) =>
            setDecisions((prev) => ({ ...prev, [i]: response }))
          }
        />
      ))}
      {allDecided && (
        <button
          className="rounded bg-green-600 px-4 py-2 text-white"
          onClick={() =>
            onRespond({
              decisions: request.actionRequests.map((_, i) => decisions[i]),
            })
          }
        >
          Submit All Decisions
        </button>
      )}
    </div>
  );
}
```

## Best practices

Keep these guidelines in mind when implementing HITL workflows:

* **Show clear context**. Always display *what* the agent wants to do and
  *why*. Include the action description and the full arguments.
* **Make approve the easiest path**. If the action looks correct, approving
  should be a single click. Reserve multi-step flows for reject/edit.
* **Validate edited args**. When users edit action arguments, validate the
  JSON structure before sending. Show inline errors for malformed input.
* **Persist the interrupt state**. If the user refreshes the page, the
  interrupt should still be visible. [`useStream`](https://reference.langchain.com/javascript/langchain-react/index/useStream) handles this via the thread's
  checkpoint.
* **Log all decisions**. For audit trails, log every approve/reject/edit
  decision with timestamps and the user who made the decision.
* **Set timeouts thoughtfully**. Long-running agents should not block
  indefinitely on human review. Consider showing how long the agent has been
  waiting.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/frontend/human-in-the-loop.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# AI Elements
Source: https://docs.langchain.com/oss/javascript/langchain/frontend/integrations/ai-elements

Composable shadcn/ui-based components for AI chat interfaces with useStream

[AI Elements](https://elements.ai-sdk.dev/) is a composable, shadcn/ui-based component library purpose-built for AI chat interfaces. Components like `Conversation`, `Message`, `Tool`, `Reasoning`, and `PromptInput` are designed to drop directly into any React project and wire to `stream.messages` with minimal glue code.

<ExampleEmbed />

<Tip>
  Clone and run the [full AI Elements example](https://github.com/langchain-ai/langgraphjs/tree/main/examples/ai-elements) to see tool call rendering, reasoning display, streaming messages, and more in a working project.
</Tip>

## How it works

1. **Install components as source files:** AI Elements ships via a CLI that adds components directly to your project (shadcn/ui registry style)
2. **Map messages to components:** iterate `stream.messages`, render `HumanMessage` instances as user bubbles and `AIMessage` instances as assistant responses
3. **Compose richer UIs:** wrap tool calls in `<Tool>`, reasoning in `<Reasoning>`, and everything in `<Conversation>` for scroll management

## Installation

Install AI Elements components via the CLI. They're added as editable source files into your project:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
npm install @langchain/react
npx ai-elements@latest add conversation message prompt-input tool reasoning suggestion
```

## Wiring useStream

Render AI Elements components directly from `stream.messages`. Each LangChain `BaseMessage` maps to a component:

```tsx theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { useStream } from "@langchain/react";
import { HumanMessage, AIMessage } from "langchain";

import {
  Conversation,
  ConversationContent,
  ConversationScrollButton,
} from "@/components/ai-elements/conversation";
import {
  Message,
  MessageContent,
  MessageResponse,
} from "@/components/ai-elements/message";
import {
  Tool,
  ToolHeader,
  ToolContent,
  ToolInput,
  ToolOutput,
} from "@/components/ai-elements/tool";
import {
  Reasoning,
  ReasoningTrigger,
  ReasoningContent,
} from "@/components/ai-elements/reasoning";
import {
  PromptInput,
  PromptInputBody,
  PromptInputTextarea,
  PromptInputFooter,
  PromptInputSubmit,
} from "@/components/ai-elements/prompt-input";

function getReasoningText(msg: AIMessage) {
  return msg.contentBlocks.find((block) => block.type === "reasoning")?.reasoning ?? "";
}

function getTextContent(msg: AIMessage) {
  return msg.text;
}

function getToolCalls(msg: AIMessage) {
  return (msg.tool_calls ?? []).map((tc) => ({
    id: tc.id,
    name: tc.name,
    args: tc.args,
    state: "input-available" as const,
  }));
}

export function Chat() {
  const stream = useStream({
    apiUrl: "http://localhost:2024",
    assistantId: "ai_elements",
  });

  return (
    <div className="flex flex-col h-dvh">
      <Conversation className="flex-1">
        <ConversationContent>
          {stream.messages.map((msg, i) => {
            if (HumanMessage.isInstance(msg)) {
              return (
                <Message key={i} from="user">
                  <MessageContent>{msg.text}</MessageContent>
                </Message>
              );
            }
            if (AIMessage.isInstance(msg)) {
              return (
                <div key={i}>
                  {/* Reasoning block (shows when model emits thinking tokens) */}
                  <Reasoning>
                    <ReasoningTrigger />
                    <ReasoningContent>{getReasoningText(msg)}</ReasoningContent>
                  </Reasoning>

                  {/* Inline tool calls with input/output display */}
                  {getToolCalls(msg).map((tc) => (
                    <Tool key={tc.id} defaultOpen>
                      <ToolHeader type={`tool-${tc.name}`} state={tc.state} />
                      <ToolContent>
                        <ToolInput input={tc.args} />
                        {tc.output && (
                          <ToolOutput output={tc.output} errorText={undefined} />
                        )}
                      </ToolContent>
                    </Tool>
                  ))}

                  {/* Streamed text response */}
                  <Message from="assistant">
                    <MessageContent>
                      <MessageResponse>{getTextContent(msg)}</MessageResponse>
                    </MessageContent>
                  </Message>
                </div>
              );
            }
          })}
        </ConversationContent>
        <ConversationScrollButton />
      </Conversation>

      <PromptInput
        onSubmit={({ text }) =>
          stream.submit({ messages: [{ type: "human", content: text }] })
        }
      >
        <PromptInputBody>
          <PromptInputTextarea placeholder="Ask me something..." />
        </PromptInputBody>
        <PromptInputFooter>
          <PromptInputSubmit
            status={stream.isLoading ? "streaming" : "ready"}
          />
        </PromptInputFooter>
      </PromptInput>
    </div>
  );
}
```

## Best practices

* **Edit source files freely:** components ship in your project, not as an external package dependency, so you can change anything without forking
* **Use `MessageResponse` for streaming:** it handles streamed partial tokens correctly; avoid rendering raw message content directly during streaming
* **Wrap in `Conversation`:** the `Conversation` component manages scroll behaviour so new messages auto-scroll into view
* **Gate on `isInstance`:** use `HumanMessage.isInstance(msg)` and `AIMessage.isInstance(msg)` rather than checking `msg.getType()` for proper TypeScript narrowing

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/frontend/integrations/ai-elements.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# assistant-ui
Source: https://docs.langchain.com/oss/javascript/langchain/frontend/integrations/assistant-ui

Headless React AI chat framework with a full runtime layer, bridged to useStream

[assistant-ui](https://www.assistant-ui.com/) is a headless React UI framework for AI chat. It provides a full runtime layer—thread management, message branching, attachment handling—that connects to [`useStream`](https://reference.langchain.com/javascript/langchain-react/index/useStream) via the `useExternalStoreRuntime` adapter.

<ExampleEmbed />

<Tip>
  Clone and run the [full assistant-ui example](https://github.com/langchain-ai/langgraphjs/tree/main/examples/assistant-ui-claude) to see a Claude-style chat interface wired to a LangChain agent with `useExternalStoreRuntime`.
</Tip>

## How it works

1. **Stream with [`useStream`](https://reference.langchain.com/javascript/langchain-react/index/useStream)** — connect to your agent and get reactive messages, loading state, and submit/cancel callbacks
2. **Adapt with `useExternalStoreRuntime`** — bridge `stream.messages` into assistant-ui's runtime format by converting `BaseMessage[]` to `ThreadMessageLike[]`
3. **Provide the runtime** — wrap your UI in `AssistantRuntimeProvider` and render any assistant-ui thread component

## Installation

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
bun add @assistant-ui/react @assistant-ui/react-markdown
```

## Wiring `useStream`

The `useExternalStoreRuntime` adapter bridges `stream.messages` into the assistant-ui runtime. Pass it to `AssistantRuntimeProvider` and render any thread component:

```tsx theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { useCallback, useMemo } from "react";
import {
  AssistantRuntimeProvider,
  useExternalStoreRuntime,
  type AppendMessage,
  type ThreadMessageLike,
} from "@assistant-ui/react";
import { useStream } from "@langchain/react";
import { Thread } from "@assistant-ui/react";

export function Chat() {
  const stream = useStream({
    apiUrl: "http://localhost:2024",
    assistantId: "claude",
  });

  const onNew = useCallback(
    async (message: AppendMessage) => {
      const text = message.content
        .filter((c) => c.type === "text")
        .map((c) => c.text)
        .join("");
      await stream.submit({ messages: [{ type: "human", content: text }] });
    },
    [stream],
  );

  // Convert LangChain messages to assistant-ui's ThreadMessageLike format
  const messages = useMemo(
    () => toThreadMessages(stream.messages),
    [stream.messages],
  );

  const runtime = useExternalStoreRuntime<ThreadMessageLike>({
    messages,
    onNew,
    onCancel: () => stream.stop(),
    convertMessage: (m) => m,
  });

  return (
    <AssistantRuntimeProvider runtime={runtime}>
      <Thread />
    </AssistantRuntimeProvider>
  );
}
```

### Converting messages

`toThreadMessages` maps LangChain `BaseMessage[]` to the `ThreadMessageLike[]` format assistant-ui expects. Handle each message type — human, AI, and tool — and convert content blocks, tool calls, and reasoning tokens:

```tsx expandable theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { AIMessage, HumanMessage, ToolMessage, type BaseMessage } from "langchain";
import type { ThreadMessageLike } from "@assistant-ui/react";

export function toThreadMessages(messages: BaseMessage[]): ThreadMessageLike[] {
  const result: ThreadMessageLike[] = [];

  for (const msg of messages) {
    if (HumanMessage.isInstance(msg)) {
      result.push({
        role: "user",
        content: [{ type: "text", text: msg.text }],
      });
    } else if (AIMessage.isInstance(msg)) {
      const parts: ThreadMessageLike["content"] = [];

      // Reasoning tokens
      const reasoning = msg.contentBlocks.find((block) => block.type === "reasoning")?.reasoning;
      if (reasoning) parts.push({ type: "reasoning", text: reasoning });

      // Tool calls
      for (const tc of msg.tool_calls ?? []) {
        parts.push({
          type: "tool-call",
          toolCallId: tc.id ?? "",
          toolName: tc.name,
          args: tc.args,
        });
      }

      // Text response
      const text = msg.text;
      if (text) parts.push({ type: "text", text });

      result.push({ role: "assistant", content: parts });
    } else if (ToolMessage.isInstance(msg)) {
      // Attach tool results to the preceding assistant message
      const last = result[result.length - 1];
      if (last?.role === "assistant") {
        for (const part of last.content) {
          if (
            part.type === "tool-call" &&
            part.toolCallId === msg.tool_call_id
          ) {
            (part as { result?: string }).result = msg.text;
          }
        }
      }
    }
  }

  return result;
}
```

## Customising the thread UI

`<Thread />` ships a complete default thread UI including message list, composer, and scroll management. Customise individual parts by overriding component slots:

```tsx theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { Thread, ThreadMessages, Composer } from "@assistant-ui/react";

function CustomThread() {
  return (
    <Thread.Root>
      <ThreadMessages
        components={{
          UserMessage: MyUserMessage,
          AssistantMessage: MyAssistantMessage,
          ToolFallback: MyToolCard,
        }}
      />
      <Composer />
    </Thread.Root>
  );
}
```

## Best practices

* **Memoise message conversion:** wrap `toThreadMessages(stream.messages)` in `useMemo` to avoid re-running the conversion on every render
* **Handle attachments:** use `CompositeAttachmentAdapter` with `SimpleImageAttachmentAdapter` for image uploads; extend with custom adapters for files
* **Use branching:** assistant-ui has built-in message branching support via `MessageBranch`; pair edits with `useMessageMetadata` and `forkFrom` when you need LangGraph checkpoint forks
* **Thread persistence:** persist `threadId` with `onThreadId` and pass it back into [`useStream`](https://reference.langchain.com/javascript/langchain-react/index/useStream) on page load so assistant-ui reconnects to the same thread

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/frontend/integrations/assistant-ui.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# CopilotKit
Source: https://docs.langchain.com/oss/javascript/langchain/frontend/integrations/copilotkit

Use CopilotKit with LangGraph, Deep Agents, and React with custom endpoints, the Python AG-UI bridge, and structured generative UI

[CopilotKit](https://www.copilotkit.ai/) provides a full React chat runtime and pairs especially well with LangGraph when you want the agent to return **structured UI payloads** instead of only plain text. In this pattern, your LangGraph deployment serves both the graph API and a custom CopilotKit endpoint, while the frontend parses assistant messages into dynamic React components.

On the server, the [copilotkit](https://pypi.org/project/copilotkit/) package provides [`CopilotKitMiddleware`](https://docs.copilotkit.ai) so a LangGraph graph, a LangChain agent, or a [Deep Agent](/oss/javascript/deepagents/overview) can speak the [Agent UI (AG-UI)](https://docs.ag-ui.com/) wire protocol, stream tool and message events to a chat UI, and read or write the shared **CopilotKit** slice of state, with helpers to mount a CopilotKit-compatible HTTP endpoint in front of your graph.

This approach is useful when you want:

* a ready-made chat runtime instead of wiring `stream.messages` yourself
* a custom server endpoint that can add provider-specific behavior next to your deployed graph
* structured generative UI rendered from a constrained component registry

[CopilotKit for LangGraph](https://docs.copilotkit.ai/langgraph) also documents [generative UI](https://docs.copilotkit.ai/langgraph/generative-ui), [human in the loop](https://docs.copilotkit.ai/langgraph/human-in-the-loop) (HITL), and [shared state](https://docs.copilotkit.ai/langgraph/shared-state) on top of the same middleware and clients.

<Info>
  For CopilotKit-specific APIs, UI patterns, and runtime configuration, see the
  [CopilotKit docs](https://docs.copilotkit.ai/langgraph). For a Deep Agent walkthrough, see
  [Deep Agents and CopilotKit](https://docs.copilotkit.ai/langgraph/deep-agents) in the CopilotKit docs.
</Info>

<ExampleEmbed />

## How it works

At a high level, CopilotKit sits between your React app and the LangGraph deployment. The frontend sends conversation state to a custom `/api/copilotkit` route mounted alongside the graph API, that route forwards the request to LangGraph, and the response comes back with both assistant messages and any structured UI payloads your component registry can render.

1. **Deploy the graph as usual** using LangSmith or using a LangGraph development server.
2. **Extend the deployment with an HTTP app** that mounts a CopilotKit route next to the graph API.
3. **Wrap the frontend in `CopilotKit`** and point it at that custom runtime URL.
4. **Register dynamic UI components** and parse assistant responses into those components at render time.

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
  USER["User input"]
  UI["CopilotKit React app"]
  ENDPOINT["/api/copilotkit"]
  GRAPH["LangGraph deployment"]
  RENDER["Hashbrown UI kit"]

  USER --> UI
  UI --> ENDPOINT
  ENDPOINT --> GRAPH
  GRAPH --> ENDPOINT
  ENDPOINT --> UI
  UI --> RENDER
```

## Installation

For the backend endpoint:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
bun add @copilotkit/runtime hono
```

For the frontend app:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
bun add @copilotkit/react-core @copilotkit/react-ui @hashbrownai/core @hashbrownai/react
```

## Extend the LangGraph deployment with a custom endpoint

The key idea is that the LangGraph deployment does not only serve graphs. It can also load an HTTP app, which lets you mount extra routes next to the deployment itself.

In `langgraph.json`, point `http.app` at your custom app entrypoint:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "graphs": {
    "copilotkit_shadify": "./src/agents/copilotkit-shadify.ts:agent"
  },
  "http": {
    "app": "./src/api/app.ts:app"
  }
}
```

Then create the Hono app and register the CopilotKit route:

```ts app.ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { Hono } from "hono";
import { registerCopilotKit } from "./copilotkit.js";

export const app = new Hono();

registerCopilotKit(app);
```

This custom app is the important extension point: it mounts a CopilotKit-aware runtime without replacing the underlying LangGraph deployment.

Inside that route, create a `CopilotRuntime` and point it back at the deployed graph using `LangGraphAgent`:

```ts expandable copilotkit.ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { type Hono } from "hono";

import { createCopilotEndpointSingleRoute, CopilotRuntime } from "@copilotkit/runtime/v2";
import { LangGraphAgent } from "@copilotkit/runtime/langgraph";

const defaultAgentHost = process.env.LANGGRAPH_DEPLOYMENT_URL || "http://127.0.0.1:2024";
const agentUrl = defaultAgentHost.startsWith("http")
  ? defaultAgentHost
  : `http://${defaultAgentHost}`;

class BridgedLangGraphAgent extends LangGraphAgent {
  override prepareRunAgentInput(
    input: Parameters<LangGraphAgent["prepareRunAgentInput"]>[0],
  ): ReturnType<LangGraphAgent["prepareRunAgentInput"]> {
    const prepared = super.prepareRunAgentInput(input);

    return {
      ...prepared,
      context: normalizeCopilotContext(prepared.context) as ReturnType<
        LangGraphAgent["prepareRunAgentInput"]
      >["context"],
    };
  }

  override async getAssistant(): Promise<Awaited<ReturnType<LangGraphAgent["getAssistant"]>>> {
    const assistants = await this.client.assistants.search({
      graphId: this.graphId,
      limit: 100,
    });

    const assistant = assistants.find((candidate) => candidate.graph_id === this.graphId);
    if (assistant) {
      return assistant;
    }

    return super.getAssistant();
  }
}

export function registerCopilotKit(app: Hono) {
  const runtime = new CopilotRuntime({
    agents: {
      default: new BridgedLangGraphAgent({
        deploymentUrl: agentUrl,
        graphId: "copilotkit_shadify",
      }),
    },
  });

  const copilotApp = createCopilotEndpointSingleRoute({
    runtime,
    basePath: "/api/copilotkit",
  });

  app.route("/", copilotApp);
}

function normalizeCopilotContext(context: unknown): unknown {
  if (!Array.isArray(context)) {
    return context;
  }

  const normalizedEntries = context.flatMap((item) => {
    if (!item || typeof item !== "object") {
      return [];
    }

    const entry = item as { description?: unknown; value?: unknown };
    return typeof entry.description === "string" ? [[entry.description, entry.value] as const] : [];
  });

  return Object.fromEntries(normalizedEntries);
}
```

The route adapter is only half of the TypeScript setup. Your LangChain agent also needs middleware that reads the forwarded `output_schema` and turns it into a structured `responseFormat` for the model:

```ts expandable agent.ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { createAgent, createMiddleware, toolStrategy } from "langchain";
import { z } from "zod";

import { deepSearchTool, searchWebTool } from "../tools/index.js";

const contextSchema = z.object({
  output_schema: z.unknown().optional(),
});

const structuredOutputMiddleware = createMiddleware({
  name: "CopilotKitStructuredOutput",
  contextSchema,
  wrapModelCall: async (request, handler) => {
    const rawOutputSchema = getRuntimeOutputSchema(request.runtime);
    const schema = normalizeOutputSchema(rawOutputSchema);
    if (!schema) {
      return handler(request);
    }

    const responseFormat = toolStrategy(
      schema as unknown as Parameters<typeof toolStrategy>[0],
      {
        toolMessageContent: "Structured UI response generated.",
      },
    );

    return handler({
      ...request,
      responseFormat,
    });
  },
});

export const agent = createAgent({
  model: process.env.COPILOTKIT_MODEL ?? "google_genai:gemini-3.5-flash",
  contextSchema,
  middleware: [structuredOutputMiddleware],
  tools: [searchWebTool, deepSearchTool],
  systemPrompt: `You are a helpful UI assistant inspired by the CopilotKit Shadify example.

Build rich visual responses with the available UI components when they add value.
Only wrap actual UI layouts inside cards. Plain Markdown answers should stay as Markdown.
Use rows for side-by-side layouts with at most two columns.
Prefer simple, polished outputs over dense dashboards.
When using charts, make labels and values concise and easy to read.
When showing code, prefer the code_block component.
When researching topics, use the available search tools first and then present the result cleanly.`,
});

function normalizeOutputSchema(value: unknown): Record<string, unknown> | null {
  let schema = value;

  if (typeof schema === "string") {
    try {
      schema = JSON.parse(schema);
    } catch {
      return null;
    }
  }

  if (!schema || typeof schema !== "object" || Array.isArray(schema)) {
    return null;
  }

  const normalized = { ...(schema as Record<string, unknown>) };

  if (!normalized.title) {
    normalized.title = "CopilotKitStructuredOutput";
  }

  if (!normalized.description) {
    normalized.description = "Structured response schema for the CopilotKit preview.";
  }

  return normalized;
}

function getRuntimeOutputSchema(runtime: {
  context?: { output_schema?: unknown };
  configurable?: Record<string, unknown>;
}): unknown {
  if (runtime.context?.output_schema !== undefined) {
    return runtime.context.output_schema;
  }

  const configurable = runtime.configurable;
  if (!configurable || typeof configurable !== "object" || Array.isArray(configurable)) {
    return undefined;
  }

  return configurable.output_schema;
}
```

This middleware is what makes `useAgentContext({ description: "output_schema", ... })` useful on the frontend. The CopilotKit runtime forwards the schema, and the agent turns it into the structured output contract the model must follow.

The result is a clean separation of concerns:

* LangGraph still owns graph execution and persistence
* CopilotKit owns the chat-facing runtime contract
* your custom endpoint glues them together inside one deployment

Follow the CopilotKit documentation for [LangGraphHttpAgent](https://docs.copilotkit.ai/langgraph) or `LangGraphAgent` in the Node **CopilotRuntime**; the **Python** graph and middleware still define tool behavior and agent logic.
:::

## Structure the frontend app

On the frontend, wrap your app in `CopilotKit` and point it at the custom runtime URL:

```tsx theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { CopilotKit } from "@copilotkit/react-core";
import { CopilotChat, useAgentContext } from "@copilotkit/react-core/v2";
import { s } from "@hashbrownai/core";

import { useChatKit } from "@/components/chat/chat-kit";
import { chatTheme } from "@/lib/chat-theme";

export function App() {
  return (
    <CopilotKit runtimeUrl={import.meta.env.VITE_RUNTIME_URL ?? "/api/copilotkit"}>
      <Page />
    </CopilotKit>
  );
}

function Page() {
  const chatKit = useChatKit();

  useAgentContext({
    description: "output_schema",
    value: s.toJsonSchema(chatKit.schema),
  });

  return <CopilotChat {...chatTheme} />;
}
```

There are two important pieces here:

* `runtimeUrl="/api/copilotkit"` sends the chat to your custom backend route rather than directly to the raw LangGraph API
* `useAgentContext(...)` sends the UI schema to the agent so the model knows what structured output format it should produce

## Register the dynamic components

The component registry lives in `useChatKit()`. This is where you define the set of components the agent is allowed to emit, such as cards, rows, columns, charts, code blocks, and buttons.

```tsx theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { s } from "@hashbrownai/core";
import { exposeComponent, exposeMarkdown, useUiKit } from "@hashbrownai/react";

import { Button } from "@/components/ui/button";
import { Card } from "@/components/ui/card";
import { CodeBlock } from "@/components/ui/code-block";
import { Row, Column } from "@/components/ui/layout";
import { SimpleChart } from "@/components/ui/simple-chart";

export function useChatKit() {
  return useUiKit({
    components: [
      exposeMarkdown(),
      exposeComponent(Card, {
        name: "card",
        description: "Card to wrap generative UI content.",
        children: "any",
      }),
      exposeComponent(Row, {
        name: "row",
        props: {
          gap: s.string("Tailwind gap size") as never,
        },
        children: "any",
      }),
      exposeComponent(Column, {
        name: "column",
        children: "any",
      }),
      exposeComponent(SimpleChart, {
        name: "chart",
        props: {
          labels: s.array("Category labels", s.string("A label")),
          values: s.array("Numeric values", s.number("A value")),
        },
        children: false,
      }),
      exposeComponent(CodeBlock, {
        name: "code_block",
        props: {
          code: s.streaming.string("The code to display"),
          language: s.string("Programming language") as never,
        },
        children: false,
      }),
      exposeComponent(Button, {
        name: "button",
        children: "text",
      }),
    ],
  });
}
```

This registry becomes the contract between the agent and the UI. The model is not generating arbitrary JSX. It is generating structured data that must validate against the components and props you exposed.

## Render assistant messages as dynamic UI

Once the assistant response arrives, the custom message renderer decides how to display it. In this example:

* assistant messages are parsed as structured JSON against the UI kit schema
* valid structured output is rendered as real React components
* user messages are rendered as ordinary chat bubbles

```tsx theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import type { AssistantMessage } from "@ag-ui/core";
import type { RenderMessageProps } from "@copilotkit/react-ui";
import { useJsonParser } from "@hashbrownai/react";
import { memo } from "react";

import { useChatKit } from "@/components/chat/chat-kit";
import { Squircle } from "@/components/squircle";

const AssistantMessageRenderer = memo(function AssistantMessageRenderer({
  message,
}: {
  message: AssistantMessage;
}) {
  const kit = useChatKit();
  const { value } = useJsonParser(message.content ?? "", kit.schema);

  if (!value) return null;

  return (
    <div className="group/msg mt-2 flex w-full justify-start">
      <div className="magic-text-output w-full px-1 py-1">{kit.render(value)}</div>
    </div>
  );
});

export function CustomMessageRenderer({ message }: RenderMessageProps) {
  if (message.role === "assistant") {
    return <AssistantMessageRenderer message={message} />;
  }

  return (
    <div className="flex w-full justify-end">
      <Squircle className="w-full max-w-[64ch] px-4 py-3">
        <pre>{typeof message.content === "string" ? message.content : JSON.stringify(message.content, null, 2)}</pre>
      </Squircle>
    </div>
  );
}
```

This renderer pattern is what makes the integration feel native:

* CopilotKit handles chat state and transport
* the custom renderer decides how assistant payloads become UI
* [Hashbrown](https://hashbrown.dev/) turns validated structured data into concrete React elements

## Resources

* [Deep Agents and CopilotKit](https://docs.copilotkit.ai/langgraph/deep-agents) in the CopilotKit documentation — end-to-end Next.js, dev server, and **Deep Agent** path
* [CopilotKit: LangGraph features](https://docs.copilotkit.ai/langgraph) — generative UI, HITL, shared state
* [LangGraph deployment](/oss/javascript/langgraph/deploy) — production and dev server

## Best practices

* **Keep the custom endpoint thin:** use it to adapt CopilotKit to your graph deployment, not to duplicate business logic already inside the graph
* **Send the schema explicitly:** `useAgentContext` should describe the UI contract every time the page mounts
* **Register a constrained component set:** expose only the components and props you actually want the model to use
* **Treat rendering as a parsing step:** parse assistant content against your schema before rendering it
* **Keep user messages plain:** only assistant messages need the structured renderer; user messages can stay normal chat bubbles

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/frontend/integrations/copilotkit.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
