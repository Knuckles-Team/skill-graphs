# LangSmith Deployment
Source: https://docs.langchain.com/oss/javascript/langchain/deploy

When you're ready to deploy your LangChain agent to production, LangSmith provides a managed hosting platform designed for agent workloads. Traditional hosting platforms are built for stateless, short-lived web applications, while LangGraph is **purpose-built for stateful, long-running agents** that require persistent state and background execution. LangSmith handles the infrastructure, scaling, and operational concerns so you can deploy directly from your repository.

## Prerequisites

Before you begin, ensure you have the following:

* A [GitHub account](https://github.com/)
* A [LangSmith account](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=oss-langchain-deploy) (free to sign up)

## Deploy your agent

### 1. Create a repository on GitHub

Your application's code must reside in a GitHub repository to be deployed on LangSmith. Both public and private repositories are supported. For this quickstart, first make sure your app is LangGraph-compatible by following the [local server setup guide](/oss/javascript/langchain/studio). Then, push your code to the repository.

### 2. Deploy to LangSmith

<Steps>
  <Step title="Navigate to LangSmith Deployment">
    Log in to [LangSmith](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=snippets-oss-deploy-js). In the left sidebar, select **Deployments**.
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
  <Tab title="JavaScript">
    1. Install LangGraph JS:

    ```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    npm install @langchain/langgraph-sdk
    ```

    2. Send a message to the agent:

    ```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    const { Client } = await import("@langchain/langgraph-sdk");

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

<Tip>
  LangSmith offers additional hosting options, including self-hosted and hybrid. For more information, please see the [Platform setup overview](/langsmith/platform-setup).
</Tip>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/deploy.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Event streaming
Source: https://docs.langchain.com/oss/javascript/langchain/event-streaming

Stream real-time updates from LangChain agent runs

LangChain agents are built on LangGraph, so they support the same streaming stack with agent-focused projections for messages, tool calls, state, and custom updates.

For most application and frontend use cases, use **Event Streaming** through `stream_events(..., version="v3")`. Event Streaming returns a run object with typed projections, so each projection can be consumed independently instead of parsing stream-mode tuples.

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { createAgent, tool } from "langchain";
import * as z from "zod";

const getWeather = tool(
  async ({ city }) => `It's always sunny in ${city}!`,
  {
    name: "get_weather",
    description: "Get weather for a city.",
    schema: z.object({ city: z.string() }),
  }
);

const agent = createAgent({
  model: "gpt-5-nano",
  tools: [getWeather],
});

const stream = await agent.streamEvents(
  { messages: [{ role: "user", content: "What is the weather in SF?" }] },
  { version: "v3" }
);

for await (const message of stream.messages) {
  for await (const delta of message.text) {
    process.stdout.write(delta);
  }
}

const finalState = await stream.output;
```

## What you can stream

| Projection            | Use                                                                        |
| --------------------- | -------------------------------------------------------------------------- |
| `for event in stream` | Raw protocol events with full envelope and access to every channel.        |
| `stream.messages`     | Model message streams, one per LLM call.                                   |
| `message.text`        | Text deltas and final text for a message.                                  |
| `message.reasoning`   | Reasoning deltas for models that expose reasoning content.                 |
| `message.toolCalls`   | Tool-call argument chunks and finalized tool calls.                        |
| `message.output`      | Final message object after the model call completes.                       |
| `message.usage`       | Token usage metadata when the provider returns it.                         |
| `stream.values`       | Agent state snapshots.                                                     |
| `stream.output`       | Final agent state.                                                         |
| `stream.subgraphs`    | Nested graph runs (sub-agents and plain subgraphs).                        |
| `stream.extensions`   | Custom transformer projections.                                            |
| `stream.toolCalls`    | Tool execution lifecycle, inputs, output deltas, final output, and errors. |

`stream.messages` yields message streams. Each message stream exposes `.text`, `.reasoning`, `.toolCalls`, `.output`, and `.usage`. Async projections can be iterated for live deltas or awaited for final values.

## Agent messages

Use `stream.messages` when you want model output from each LLM call.

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const stream = await agent.streamEvents(input, { version: "v3" });

for await (const message of stream.messages) {
  process.stdout.write(`[${message.node}] `);
  for await (const delta of message.text) {
    process.stdout.write(delta);
  }

  const fullMessage = await message.output;
  console.log(fullMessage.content);

  const usage = await message.usage;
  if (usage) {
    console.log(usage);
  }
}
```

`message.output` gives you the finalized AI message, including provider-specific content blocks. In TypeScript, use `message.usage` when you only need token counts or other usage metadata; in Python, read usage from `message.output.usage_metadata`.

## Reasoning content

Reasoning content uses the same shape as text content, but it is available only when the selected model emits reasoning blocks.

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const stream = await agent.streamEvents(input, { version: "v3" });

for await (const message of stream.messages) {
  for await (const delta of message.reasoning) {
    process.stdout.write(`[thinking] ${delta}`);
  }

  for await (const delta of message.text) {
    process.stdout.write(delta);
  }
}
```

See the [reasoning guide](/oss/javascript/langchain/models#reasoning) and your provider's integration page for model configuration details.

## Tool calls

There are two useful tool-call projections:

* `message.tool_calls` streams tool-call argument chunks while the model is producing the tool call.
* `stream.tool_calls` streams the lifecycle of tool execution after the tool call starts.

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const stream = await agent.streamEvents(input, { version: "v3" });

await Promise.all([
  (async () => {
    for await (const message of stream.messages) {
      for await (const chunk of message.toolCalls) {
        console.log("tool call chunk", chunk);
      }
    }
  })(),
  (async () => {
    for await (const call of stream.toolCalls) {
      console.log(call.name, call.input);
      console.log(await call.output, await call.error);
    }
  })(),
]);
```

## Streaming sub-agents

When a `create_agent` call invokes another named `create_agent` (via a wrapping tool, typically), the inner agent's events flow at a nested namespace. The `name=` you pass to `create_agent` identifies that inner agent in the stream, so you can filter and label per agent.

Named sub-agents surface as handles on `stream.subgraphs`, alongside any plain subgraphs. Each handle exposes the inner agent's `.messages`, `.values`, `.toolCalls`, and `.output`; filter on `subagent.name` (the `name=` you passed) to act on a specific agent.

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { createAgent, tool } from "langchain";
import { z } from "zod";

const getWeather = tool(
  async ({ city }) => `It's always sunny in ${city}!`,
  { name: "get_weather", schema: z.object({ city: z.string() }) }
);

const weatherAgent = createAgent({
  model: "openai:gpt-5.5",
  tools: [getWeather],
  name: "weather_agent",
});

const callWeather = tool(
  async ({ query }) => {
    const result = await weatherAgent.invoke({
      messages: [{ role: "user", content: query }],
    });
    return result.messages.at(-1)?.text ?? "";
  },
  { name: "call_weather", schema: z.object({ query: z.string() }) }
);

const supervisor = createAgent({
  model: "openai:gpt-5.5",
  tools: [callWeather],
  name: "supervisor",
});

const stream = await supervisor.streamEvents(
  { messages: [{ role: "user", content: "What's the weather in Boston?" }] },
  { version: "v3" }
);

for await (const subagent of stream.subgraphs) {
  if (subagent.name !== "weather_agent") continue;
  process.stdout.write(`${subagent.name}: `);
  for await (const message of subagent.messages) {
    for await (const token of message.text) {
      process.stdout.write(token);
    }
  }
  process.stdout.write("\n");
}
```

Plain `StateGraph` subgraphs invoked from a tool also surface on `stream.subgraphs` — set `name=` on `.compile(name=...)` to get a label in `subagent.graph_name`.

Named sub-agents share the `stream.subgraphs` projection with plain subgraphs; the filter you write into your loop is what separates them.

## State and final output

Use `stream.values` for state snapshots and `stream.output` for the final agent state.

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const stream = await agent.streamEvents(input, { version: "v3" });

for await (const snapshot of stream.values) {
  console.log(snapshot);
}

const finalState = await stream.output;
```

## Multiple projections

Use concurrent consumers when you want multiple projections in JavaScript:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const stream = await agent.streamEvents(input, { version: "v3" });

await Promise.all([
  (async () => {
    for await (const message of stream.messages) {
      console.log(await message.text);
    }
  })(),
  (async () => {
    for await (const call of stream.toolCalls) {
      console.log(call.name, call.input);
    }
  })(),
]);
```

To access channels that aren't exposed as typed projections, or to inspect the full event envelope, iterate raw protocol events:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
for await (const event of stream) {
  console.log(event.method, event.params.namespace, event.params.data);
}
```

## Custom updates

Use custom stream transformers when your application needs a projection that is not built in, such as retrieval progress, artifacts, or domain-specific events.

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const stream = await agent.streamEvents(input, {
  version: "v3",
  transformers: [toolActivityTransformer],
});

for await (const activity of stream.extensions.toolActivity) {
  console.log(activity);
}
```

### Register transformers on middleware

<Note>Middleware-registered transformers require `langchain@1.4.3` or later.</Note>

Middleware can declare stream transformer factories alongside its hooks and tools. The factory shape differs between languages:

Pass `streamTransformers` to `createMiddleware` as a tuple of factories. Each factory has the shape `() => StreamTransformer<any>` (zero arguments) and is invoked once per scope. Returning a fresh transformer per call keeps each subgraph isolated.

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { createAgent, createMiddleware } from "langchain";

const toolActivityMiddleware = createMiddleware({
  name: "ToolActivityMiddleware",
  streamTransformers: [toolActivityTransformer],
});

const agent = createAgent({
  model: "gpt-5-nano",
  tools: [getWeather],
  middleware: [toolActivityMiddleware],
});
```

At compile time, `createAgent` merges middleware-registered factories with anything passed to its own `streamTransformers` option. The final order on the compiled graph is:

1. The built-in `ToolCallTransformer`.
2. Middleware-registered factories, in middleware order.
3. Caller-supplied `streamTransformers` from `createAgent`.

This keeps the built-in tool-call projection in front of consumer transformers and gives caller-supplied entries the final word.

See [Build your own projection](/oss/javascript/langgraph/event-streaming#build-your-own-projection) for the transformer contract.

## Related

* [Streaming](/oss/javascript/langchain/streaming) covers low-level Pregel stream modes.
* [Build your own projection](/oss/javascript/langgraph/event-streaming#build-your-own-projection) covers writing application-specific projections.
* [Frontend streaming patterns](/oss/javascript/langchain/frontend/overview) shows UI use cases built on streamed state.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/event-streaming.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Branching chat
Source: https://docs.langchain.com/oss/javascript/langchain/frontend/branching-chat

Edit messages and regenerate responses by forking from checkpoints

Conversations with AI agents are rarely linear. You may want to rephrase a
question, regenerate a response you didn't like, or explore a different
conversational path without losing the checkpoint history. Branching chat uses
LangGraph checkpoints as fork points: every edit or regeneration submits a new
run from the selected message's parent checkpoint.

<PatternEmbed />

<Note>
  This feature requires the [LangGraph Agent Server](../langgraph/local-server). Run your agent locally with `langgraph dev` or [deploy it to LangSmith](/langsmith/deployment) to use this pattern.
</Note>

## What is branching chat?

Branching chat treats a conversation as a checkpointed timeline rather than a
flat list. Each message has metadata that points to the checkpoint before that
message was created. Editing a message or regenerating a response submits a new
run from that checkpoint.

Key capabilities:

* **Edit any user message:** rewrite a previous prompt and re-run the agent from that point
* **Regenerate any AI response:** ask the agent to produce a different answer for the same input
* **Inspect history:** use the LangGraph client to load checkpoints when you need a branch timeline

## Set up stream metadata

Use the root stream for messages, then read per-message checkpoint metadata in
the component that renders each message. The metadata includes the parent
checkpoint ID to fork from.

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
      assistantId: "simple_agent",
    });

    return (
      <div>
        {stream.messages.map((msg) => (
          <MessageWithForkControls key={msg.id} stream={stream} message={msg} />
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
    assistantId: "simple_agent",
  });
  </script>

  <template>
    <div>
      <MessageWithForkControls
        v-for="msg in stream.messages.value"
        :key="msg.id"
        :stream="stream"
        :message="msg"
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
      assistantId: "simple_agent",
    });
  </script>

  <div>
    {#each stream.messages as msg (msg.id)}
      <Message
        message={msg}
        {stream}
      />
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
        <app-message
          [message]="msg"
          [stream]="stream"
        />
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

## Understand message metadata

The `useMessageMetadata(stream, messageId)` helper returns [MessageMetadata](https://reference.langchain.com/javascript/langchain-react/MessageMetadata)
for one message. Use it in the component that renders each message so the
metadata stays scoped to that message ID:

```tsx theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import type { BaseMessage } from "langchain";
import { useState } from "react";
import { useMessageMetadata, useStream } from "@langchain/react";

function Chat() {
  const stream = useStream<typeof myAgent>({
    apiUrl: AGENT_URL,
    assistantId: "simple_agent",
  });

  return stream.messages.map((message) => (
    <MessageWithForkControls
      key={message.id}
      stream={stream}
      message={message}
    />
  ));
}

function MessageWithForkControls({
  stream,
  message,
}: {
  stream: ReturnType<typeof useStream>;
  message: BaseMessage;
}) {
  const metadata = useMessageMetadata(stream, message.id);
  const checkpointId = metadata?.parentCheckpointId;
  const [editedText, setEditedText] = useState(message.text);

  return (
    <form
      onSubmit={(event) => {
        event.preventDefault();
        if (!checkpointId) return;

        stream.submit(
          { messages: [{ type: "human", content: editedText }] },
          { forkFrom: { checkpointId } }
        );
      }}
    >
      <textarea
        value={editedText}
        onChange={(event) => setEditedText(event.target.value)}
      />
      <button disabled={!checkpointId || editedText === message.text}>
        Submit edited branch
      </button>
    </form>
  );
}
```

`parentCheckpointId` is the checkpoint just before the message. Use it as the
fork point for edits and regenerations.

## Edit a message

To edit a user message and fork the conversation:

1. Get `parentCheckpointId` from the message's metadata
2. Submit the edited message with `forkFrom: { checkpointId }`
3. The agent re-runs from that point

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
function handleEdit(
  stream: ReturnType<typeof useStream>,
  originalMsg: HumanMessage,
  metadata: MessageMetadata | undefined,
  newText: string
) {
  if (!metadata?.parentCheckpointId) return;

  stream.submit(
    {
      messages: [{ type: "human", content: newText }],
    },
    { forkFrom: { checkpointId: metadata.parentCheckpointId } }
  );
}
```

After the edit:

* The agent re-runs from the fork point with the updated message
* The original path remains available in the thread history

## Regenerate a response

To regenerate an AI response without changing the input:

1. Get the `parent_checkpoint` from the AI message's metadata
2. Submit with empty input and `forkFrom: { checkpointId }`
3. The agent produces a fresh response from that point

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
function handleRegenerate(
  stream: ReturnType<typeof useStream>,
  metadata: MessageMetadata | undefined
) {
  if (!metadata?.parentCheckpointId) return;

  stream.submit(undefined, {
    forkFrom: { checkpointId: metadata.parentCheckpointId },
  });
}
```

Each regeneration creates a new path for the AI message at that position.

<Tip>
  Regeneration is useful for non-deterministic agents. Since LLM outputs vary
  with temperature, regenerating the same prompt often produces meaningfully
  different responses.
</Tip>

## How branching works under the hood

LangGraph persists every state transition as a **checkpoint**. When you submit
with `forkFrom`, the backend starts a new execution path from that point instead
of appending to the current conversation. The result is a tree structure:

```
User: "What is React?"
  └─ AI: "React is a JavaScript library..." (branch A)
  └─ AI: "React is a UI framework..." (branch B, regenerated)

User: "Tell me about hooks" (branch A)
  └─ AI: "Hooks are functions..."

User: "Tell me about JSX" (edited from branch A)
  └─ AI: "JSX is a syntax extension..."
```

Each path is persisted in the checkpoint store. Use
`stream.client.threads.getHistory(threadId)` when you want to build a separate
timeline view across checkpoints.

## Best practices

* **Read metadata near the message**: call `useMessageMetadata` in the component
  that renders the message controls.
* **Show fork controls on hover**: edit and regenerate buttons should appear on
  hover to keep the UI clean.
* **Refresh history on demand**: call `client.threads.getHistory()` only when
  rendering a timeline or after a fork settles.
* **Disable controls while streaming**: don't allow edits or regeneration
  while the agent is actively streaming a response. Check `stream.isLoading`
  before enabling these actions.
* **Preserve edit text on cancel**: if the user starts editing, then cancels,
  reset the textarea to the original message content.
* **Test with deep checkpoint trees**: users who edit and regenerate frequently
  can create many paths. Ensure timeline rendering remains performant.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/frontend/branching-chat.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Generative UI
Source: https://docs.langchain.com/oss/javascript/langchain/frontend/generative-ui

Render AI-generated user interfaces using json-render

Generative UI lets the AI generate complete user interfaces from natural language
prompts. Instead of rendering text responses in chat bubbles, the AI output **is**
the UI: forms, cards, dashboards, and more. The developer defines which components
are available (the "catalog"), and the AI composes them into a valid UI tree.

This pattern uses [json-render](https://json-render.dev), the Generative UI framework,
to define component catalogs, generate specs with AI, and render them safely across
React, Vue, Svelte, and Angular.

<PatternEmbed />

## How it works

1. **Define a catalog**: declare what components the AI can use, with typed props
2. **Prompt the AI**: describe the UI you want in natural language
3. **AI generates a spec**: a JSON document describing the component tree
4. **Render safely**: json-render's `Renderer` renders the spec using your components

The catalog acts as a guardrail: the AI can only use components you've defined,
with props that match your schema. The output is always predictable and safe.

## Define a component catalog

The catalog describes every component the AI is allowed to use. Each component has a
Zod schema for its props and a description that the AI reads to understand when to
use it:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { defineCatalog } from "@json-render/core";
import { schema } from "@json-render/react/schema";
import { z } from "zod";

const catalog = defineCatalog(schema, {
  components: {
    Card: {
      description: "A card container with optional title and padding",
      props: z.object({
        title: z.string().optional(),
        padding: z.enum(["sm", "md", "lg"]).optional(),
      }),
    },
    Stack: {
      description: "Layout children vertically or horizontally with consistent spacing",
      props: z.object({
        direction: z.enum(["vertical", "horizontal"]).optional(),
        gap: z.enum(["sm", "md", "lg"]).optional(),
      }),
    },
    TextInput: {
      description: "A text input field with optional label and placeholder",
      props: z.object({
        label: z.string().optional(),
        placeholder: z.string().optional(),
        type: z.enum(["text", "email", "password", "number", "textarea"]).optional(),
      }),
    },
    Button: {
      description: "A clickable button with label and style variants",
      props: z.object({
        label: z.string(),
        variant: z.enum(["primary", "secondary", "ghost", "link"]).optional(),
        fullWidth: z.boolean().optional(),
      }),
    },
  },
  actions: {},
});
```

<Tip>
  Keep catalogs focused. Include only components the AI needs for the use case.
  A smaller catalog produces better results than a kitchen-sink approach.
</Tip>

## Build a component registry

The registry maps each catalog component to its actual rendering implementation.
Use `defineRegistry` to get type-safe bindings between the catalog props and
your component functions:

<CodeGroup>
  ```tsx React theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { defineRegistry, Renderer, JSONUIProvider } from "@json-render/react";

  const { registry } = defineRegistry(catalog, {
    components: {
      Card: ({ props, children }) => (
        <div className="card">
          {props.title && <h2>{props.title}</h2>}
          {children}
        </div>
      ),
      Stack: ({ props, children }) => (
        <div className={`stack stack-${props.direction ?? "vertical"} gap-${props.gap ?? "md"}`}>
          {children}
        </div>
      ),
      TextInput: ({ props }) => (
        <div>
          {props.label && <label>{props.label}</label>}
          <input type={props.type ?? "text"} placeholder={props.placeholder} />
        </div>
      ),
      Button: ({ props }) => (
        <button className={props.variant ?? "primary"}>
          {props.label}
        </button>
      ),
    },
  });
  ```

  ```vue Vue theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  <script setup lang="ts">
  import { h } from "vue";
  import { defineRegistry, Renderer, JSONUIProvider } from "@json-render/vue";

  const { registry } = defineRegistry(catalog, {
    components: {
      Card: ({ props, children }) =>
        h("div", { class: "card" }, [
          props.title ? h("h2", null, props.title) : null,
          children,
        ]),
      Stack: ({ props, children }) =>
        h("div", { class: `stack stack-${props.direction ?? "vertical"} gap-${props.gap ?? "md"}` }, children),
      TextInput: ({ props }) =>
        h("div", null, [
          props.label ? h("label", null, props.label) : null,
          h("input", { type: props.type ?? "text", placeholder: props.placeholder }),
        ]),
      Button: ({ props }) =>
        h("button", { class: props.variant ?? "primary" }, props.label),
    },
  });
  </script>
  ```
</CodeGroup>

## Connect to the agent

The agent uses structured output to return a json-render spec. Set up `useStream`
with your agent's assistant ID, then extract the spec from the AI message's
`tool_calls`:

<CodeGroup>
  ```tsx React theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { useStream } from "@langchain/react";
  import { AIMessage } from "langchain";

  function GenerativeUI() {
    const stream = useStream<typeof myAgent>({
      apiUrl: "http://localhost:2024",
      assistantId: "generative_ui",
    });

    const aiMessage = stream.messages.find(AIMessage.isInstance);
    const rawSpec = aiMessage?.tool_calls?.[0]?.args;

    // ... filter and render (see streaming section below)
  }
  ```

  ```vue Vue theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  <script setup lang="ts">
  import { useStream } from "@langchain/vue";
  import { AIMessage } from "langchain";
  import { computed } from "vue";

  const stream = useStream<typeof myAgent>({
    apiUrl: "http://localhost:2024",
    assistantId: "generative_ui",
  });

  const aiMessage = computed(() => stream.messages.value.find(AIMessage.isInstance));
  const rawSpec = computed(() => aiMessage.value?.tool_calls?.[0]?.args);
  </script>
  ```

  ```svelte Svelte theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  <script lang="ts">
    import { useStream } from "@langchain/svelte";
    import { AIMessage } from "langchain";

    const stream = useStream<typeof myAgent>({
      apiUrl: "http://localhost:2024",
      assistantId: "generative_ui",
    });

    const aiMessage = $derived(stream.messages.find((m) => AIMessage.isInstance(m)));
    const rawSpec = $derived(aiMessage?.tool_calls?.[0]?.args);
  </script>
  ```

  ```ts Angular theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { Component } from "@angular/core";
  import { injectStream } from "@langchain/angular";
  import { AIMessage } from "langchain";

  @Component({
    selector: "app-generative-ui",
    template: `...`,
  })
  export class GenerativeUIComponent {
    stream = injectStream<typeof myAgent>({
      apiUrl: "http://localhost:2024",
      assistantId: "generative_ui",
    });

    get rawSpec() {
      const ai = this.stream.messages().find(AIMessage.isInstance);
      return ai?.tool_calls?.[0]?.args;
    }
  }
  ```
</CodeGroup>

## Stream and render progressively

During streaming, the spec is built up incrementally. Elements arrive one at a
time and may initially lack `type` or `props`. Filter to only complete elements
and pass `loading={true}` to the `Renderer`, which tells it to silently skip
children that haven't arrived yet. The UI builds up component by component:

```tsx theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
/*
 * Filter the streamed spec to only include elements with valid type/props,
 * enabling progressive rendering as the AI response builds up. Passing
 * loading={true} to the Renderer tells it to skip missing children silently.
 */
const spec = (() => {
  if (!rawSpec?.root || !rawSpec?.elements) return null;
  const rootEl = rawSpec.elements[rawSpec.root];
  if (!rootEl?.type || rootEl?.props == null) return null;

  const safeElements = {};
  for (const [key, el] of Object.entries(rawSpec.elements)) {
    if (el?.type && el?.props != null) {
      safeElements[key] = el;
    }
  }
  return { root: rawSpec.root, elements: safeElements };
})();

return (
  <>
    {spec && (
      <JSONUIProvider registry={registry}>
        <Renderer spec={spec} registry={registry} loading={stream.isLoading} />
      </JSONUIProvider>
    )}
  </>
);
```

<Note>
  The `JSONUIProvider` is required to set up json-render's internal context
  providers (state, visibility, validation, actions). The `Renderer` component
  must be rendered inside it.
</Note>

## The spec format

The AI agent generates a flat JSON spec with a `root` key pointing to the
root element and an `elements` map containing all components:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "root": "login-card",
  "elements": {
    "login-card": {
      "type": "Card",
      "props": { "title": "Login" },
      "children": ["login-stack"]
    },
    "login-stack": {
      "type": "Stack",
      "props": { "direction": "vertical", "gap": "md" },
      "children": ["email-input", "password-input", "submit-btn"]
    },
    "email-input": {
      "type": "TextInput",
      "props": { "label": "Email", "placeholder": "Enter your email", "type": "email" },
      "children": []
    },
    "password-input": {
      "type": "TextInput",
      "props": { "label": "Password", "placeholder": "Enter your password", "type": "password" },
      "children": []
    },
    "submit-btn": {
      "type": "Button",
      "props": { "label": "Sign In", "variant": "primary", "fullWidth": true },
      "children": []
    }
  }
}
```

Each element references its children by ID, and leaf elements like `TextInput`
and `Button` have empty `children` arrays.

## Best practices

* **Use descriptive component descriptions**: the AI uses these to understand when
  to use each component. Clear descriptions lead to better UI generation.
* **Validate before rendering**: always check that elements have valid `type` and
  non-null `props` before passing to the Renderer, since streaming delivers partial data.
* **Design for streaming**: pass `loading={true}` during streaming so the Renderer
  gracefully handles children that haven't arrived yet. Users see the UI build up
  in real time rather than waiting for the full response.
* **Style with design tokens**: use CSS custom properties so rendered components
  adapt to light and dark themes automatically.
* **Wrap with JSONUIProvider**: the `Renderer` must be inside a `JSONUIProvider`
  to access json-render's internal context for state, visibility, and actions.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/frontend/generative-ui.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Headless tools
Source: https://docs.langchain.com/oss/javascript/langchain/frontend/headless-tools

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

1. Register a schema-only tool definition on the agent.
2. Implement the matching tool in the frontend with `.implement(...)`.
3. Pass those implementations to `useStream({ tools: [...] })`.
4. When the agent emits a matching tool call, the client runs it and resumes
   the interrupted run with the tool result.

<Tip>
  Keep tool definitions and implementations in separate modules. Share the
  definitions between your agent and your frontend so the tool names and schemas
  stay aligned, then keep browser-only code in a client-only `impl` module.
</Tip>

## Register the tool on the agent

The playground defines a small set of client-side tools that follow the same
pattern: the agent exposes a tool schema, and the frontend handles the actual
execution.

Define the tools once in a shared `tools.ts` file and use that file from both
the agent and the frontend.

<CodeGroup>
  ```ts tools.ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import * as z from "zod";
  import { tool } from "langchain";

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

  ```ts agent.ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createAgent } from "langchain";
  import { MemorySaver } from "@langchain/langgraph";

  import { geolocationGet, memoryGet, memoryPut } from "./tools";

  export const agent = createAgent({
    model: "openai:gpt-5.5",
    tools: [memoryPut, memoryGet, geolocationGet],
    checkpointer: new MemorySaver(),
  });
  ```
</CodeGroup>

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

The agent state can be inferred from the agent definition:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import type { myAgent } from "./agent";

export type AgentState = typeof myAgent;
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
[Tool calling](/oss/javascript/langchain/frontend/tool-calling), where each tool result can
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
  with [Human-in-the-loop](/oss/javascript/langchain/frontend/human-in-the-loop).

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/frontend/headless-tools.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
