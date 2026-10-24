# Headless tools
Source: https://docs.langchain.com/oss/python/langchain/frontend/headless-tools

Run browser and device APIs on the client with headless tool implementations

Headless tools let your agent call tools whose real execution must happen in the
user's app instead of on the server. The agent still sees a normal tool schema,
but the implementation lives in the frontend, where it can access browser APIs
like IndexedDB, geolocation, clipboard, canvas, or file pickers.

This pattern is especially useful when data should stay local to the device.
The playground example on this page uses a small browser-memory toolkit backed
by IndexedDB plus a geolocation tool that runs entirely on the client.

<PatternEmbed />

## How headless tools work

At a high level, headless tools split the tool schema from the browser-only implementation.

1. Register a tool on the agent that immediately calls `interrupt()` to defer execution to the frontend.
2. Mirror the same tool names and argument fields in frontend definitions.
3. Implement the matching tools in the frontend with `.implement(...)` and pass
   them to `useStream({ tools: [...] })`.
4. When the agent invokes a matching tool, the client handles the action and
   resumes the interrupted run with the tool result.

## Register the tool on the agent

The playground defines a small set of client-side tools that follow the same
pattern: the agent exposes a tool schema, and the frontend handles the actual
execution.

Define normal tools on the server that immediately call `interrupt()`, then
mirror the same tool names and argument fields in a
frontend `tools.ts` file.

```python agent.py theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from typing import Any

from langchain import create_agent
from langchain.tools import ToolRuntime, tool
from langgraph.checkpoint.memory import MemorySaver
from langgraph.types import interrupt
from pydantic import BaseModel

class MemoryPutInput(BaseModel):
    key: str
    value: Any

class MemoryGetInput(BaseModel):
    key: str

class GeolocationGetInput(BaseModel):
    save: bool = True

def _interrupt_for_client(
    tool_name: str,
    args: dict[str, Any],
    runtime: ToolRuntime,
) -> Any:
    return interrupt({
        "type": "tool",
        "tool_call": {
            "id": runtime.tool_call_id,
            "name": tool_name,
            "args": args,
        },
    })

@tool(
    "memory_put",
    description="Store a memory in the user's browser.",
    args_schema=MemoryPutInput,
)
def memory_put(key: str, value: Any, runtime: ToolRuntime) -> Any:
    return _interrupt_for_client(
        "memory_put",
        {"key": key, "value": value},
        runtime,
    )

@tool(
    "memory_get",
    description="Look up a memory stored in the user's browser.",
    args_schema=MemoryGetInput,
)
def memory_get(key: str, runtime: ToolRuntime) -> Any:
    return _interrupt_for_client("memory_get", {"key": key}, runtime)

@tool(
    "geolocation_get",
    description="Get the user's current location from the browser.",
    args_schema=GeolocationGetInput,
)
def geolocation_get(runtime: ToolRuntime, save: bool = True) -> Any:
    return _interrupt_for_client(
        "geolocation_get",
        {"save": save},
        runtime,
    )

agent = create_agent(
    model="openai:gpt-5.5",
    tools=[memory_put, memory_get, geolocation_get],
    checkpointer=MemorySaver(),
)
```

Each tool interrupts with a structured payload the frontend can handle, then
returns the value provided when the run resumes. Mirror the same tool names and
schemas on the client so the frontend can attach implementations.

```ts tools.ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import * as z from "zod";
import { tool } from "langchain";

// Mirror the Python tool names and schemas on the client.
export const memoryPut = tool({
  name: "memory_put",
  description: "Store a memory in the user's browser.",
  schema: z.object({
    key: z.string(),
    value: z.unknown(),
  }),
});

export const memoryGet = tool({
  name: "memory_get",
  description: "Look up a memory stored in the user's browser.",
  schema: z.object({
    key: z.string(),
  }),
});

export const geolocationGet = tool({
  name: "geolocation_get",
  description: "Get the user's current location from the browser.",
  schema: z.object({
    save: z.boolean().optional(),
  }),
});
```

## Implement the browser behavior

Put the client-only behavior in a separate module and attach it with
`.implement(...)`. The real playground includes a fuller IndexedDB store with
search, listing, expiration, and delete operations. The following example shows
the same shape at a higher level:

```ts impl.ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import {
  geolocationGet as geolocationGetDefinition,
  memoryGet as memoryGetDefinition,
  memoryPut as memoryPutDefinition,
} from "./tools";

async function saveMemory(key: string, value: unknown) {
  localStorage.setItem(`agent-memory:${key}`, JSON.stringify(value));
}

async function getMemory(key: string) {
  const value = localStorage.getItem(`agent-memory:${key}`);
  return value ? JSON.parse(value) : null;
}

export const memoryPut = memoryPutDefinition.implement(async ({ key, value }) => {
  await saveMemory(key, value);
  return { success: true, key };
});

export const memoryGet = memoryGetDefinition.implement(async ({ key }) => {
  const value = await getMemory(key);
  return value === null ? { found: false, key } : { found: true, key, value };
});

export const geolocationGet = geolocationGetDefinition.implement(
  async ({ save = true }) => {
    const position = await new Promise<GeolocationPosition>((resolve, reject) =>
      navigator.geolocation.getCurrentPosition(resolve, reject),
    );

    const location = {
      latitude: position.coords.latitude,
      longitude: position.coords.longitude,
      accuracy: position.coords.accuracy,
    };

    if (save) {
      await saveMemory("user_location", location);
    }

    return location;
  },
);
```

## Wire the implementations into `useStream`

Pass the implemented tools to `useStream`. When the agent emits a matching tool
call, the hook runs the client implementation and resumes the run for you.

Define a TypeScript interface matching your agent's state schema and pass it as
a type parameter to `useStream` for type-safe access to state values:

```ts types.ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
export interface AgentState {
  messages: BaseMessage[];
}
```

<CodeGroup>
  ```tsx React theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { useStream } from "@langchain/react";

  import { geolocationGet, memoryGet, memoryPut } from "./impl";
  import type { AgentState } from "./types";

  const AGENT_URL = "http://localhost:2024";

  export function Chat() {
    const stream = useStream<AgentState>({
      apiUrl: AGENT_URL,
      assistantId: "headless_tools",
      tools: [memoryPut, memoryGet, geolocationGet],
    });

    return <ChatView messages={stream.messages} toolCalls={stream.toolCalls} />;
  }
  ```

  ```vue Vue theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  <script setup lang="ts">
  import { useStream } from "@langchain/vue";

  import { geolocationGet, memoryGet, memoryPut } from "./impl";
  import type { AgentState } from "./types";

  const AGENT_URL = "http://localhost:2024";

  const stream = useStream<AgentState>({
    apiUrl: AGENT_URL,
    assistantId: "headless_tools",
    tools: [memoryPut, memoryGet, geolocationGet],
  });
  </script>

  <template>
    <ChatView
      :messages="stream.messages.value"
      :tool-calls="stream.toolCalls.value"
    />
  </template>
  ```

  ```svelte Svelte theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  <script lang="ts">
    import { useStream } from "@langchain/svelte";

    import { geolocationGet, memoryGet, memoryPut } from "./impl";
    import type { AgentState } from "./types";

    const AGENT_URL = "http://localhost:2024";

    const { messages, toolCalls } = useStream<AgentState>({
      apiUrl: AGENT_URL,
      assistantId: "headless_tools",
      tools: [memoryPut, memoryGet, geolocationGet],
    });
  </script>

  <ChatView messages={$messages} toolCalls={$toolCalls} />
  ```

  ```ts Angular theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { Component } from "@angular/core";
  import { useStream } from "@langchain/angular";

  import { geolocationGet, memoryGet, memoryPut } from "./impl";
  import type { AgentState } from "./types";

  const AGENT_URL = "http://localhost:2024";

  @Component({
    selector: "app-chat",
    template: `
      <app-chat-view
        [messages]="stream.messages()"
        [toolCalls]="stream.toolCalls()"
      />
    `,
  })
  export class ChatComponent {
    stream = useStream<AgentState>({
      apiUrl: AGENT_URL,
      assistantId: "headless_tools",
      tools: [memoryPut, memoryGet, geolocationGet],
    });
  }
  ```
</CodeGroup>

## Render tool activity inline

The playground renders each memory or geolocation operation as its own card and
keeps a small memory stats panel near the input. The key step is matching each
entry in `stream.toolCalls` back to the AI message that triggered it:

```tsx theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import type { ToolCallWithResult, DefaultToolCall } from "@langchain/react";

function Message({ message, toolCalls }: {
  message: AIMessage,
  toolCalls: ToolCallWithResult[]
}) {
  const messageToolCalls = toolCalls.filter((tc) =>
    message.tool_calls?.some((call) => call.id === tc.call.id),
  );

  return (
    <div>
      {message.text && <p>{message.text}</p>}
      {messageToolCalls.map((tc) => (
        <HeadlessToolCard key={tc.call.id} toolCall={tc} />
      ))}
    </div>
  );
}
```

This works especially well with the richer UI patterns from
[Tool calling](/oss/python/langchain/frontend/tool-calling), where each tool result can
render as a specialized card instead of raw JSON.

## Use cases

Use headless tools when the work depends on APIs or data that only exist in the
client:

* Local memory in IndexedDB or `localStorage`
* Device APIs like geolocation, clipboard, camera, or file pickers
* Canvas, audio, or other browser-only rendering primitives
* Privacy-sensitive data that should stay on the user's device
* UI actions that need direct access to in-memory frontend state

## Best practices

* Keep tools small and typed. Prefer many narrow tools over one generic
  "run arbitrary browser code" tool.
* Return JSON-serializable results. Do not try to return DOM nodes, file
  handles, or other non-serializable browser objects.
* Share definitions, separate implementations. The agent and client should agree
  on tool names and schemas, but only the client should load browser APIs.
* Surface tool state in the UI. Use `stream.toolCalls` and `onTool` to show
  pending, success, and error states.
* Add review when needed. For sensitive client-side actions, pair this pattern
  with [Human-in-the-loop](/oss/python/langchain/frontend/human-in-the-loop).

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/frontend/headless-tools.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Human-in-the-Loop
Source: https://docs.langchain.com/oss/python/langchain/frontend/human-in-the-loop

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
Source: https://docs.langchain.com/oss/python/langchain/frontend/integrations/ai-elements

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
Source: https://docs.langchain.com/oss/python/langchain/frontend/integrations/assistant-ui

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
