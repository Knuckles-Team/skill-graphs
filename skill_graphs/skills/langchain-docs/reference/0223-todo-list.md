# Todo list
Source: https://docs.langchain.com/oss/python/deepagents/frontend/todo-list

Track agent progress with a real-time todo list synced from agent state

Not every agent interaction is a chat. Sometimes the agent is executing a
multi-step plan, and the best way to show progress is a **todo list** that
updates in real time. The deep agent todo list pattern reads a `todos` array
directly from the agent's state, rendering each item with its current status as
the agent works through its plan. It's a progress dashboard built on the same
`useStream` hook you use for chat. It shows that agent state can power any UI,
not just message bubbles.

<PatternEmbed />

## How it works

Deep agents include a built-in **`todos` state** that tracks task progress as
the agent works through its plan. As the agent executes, it updates each
todo's status from `"pending"` to `"in_progress"` to `"completed"`. The
[`useStream`](https://reference.langchain.com/javascript/langchain-react/index/useStream) hook exposes this state via `stream.values.todos`, and your UI
renders it reactively.

The flow looks like this:

1. User submits a request
2. Agent creates a plan and populates `todos` in its state
3. Agent begins executing each todo transitions through `pending` →
   `in_progress` → `completed`
4. `stream.values.todos` updates in real time as the agent progresses
5. Your UI re-renders the todo list with current statuses

## Setting up `useStream`

No special configuration is needed. Point [`useStream`](https://reference.langchain.com/javascript/langchain-react/index/useStream) at your agent and
read the `todos` from `stream.values`.

<Info>
  The code examples use `useStream<typeof myAgent>` for type-safe stream state. See Type inference for [Python](/oss/python/langchain/frontend/overview#type-inference) or [JavaScript](/oss/javascript/langchain/frontend/overview#type-inference) backends.
</Info>

<CodeGroup>
  ```tsx React theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { useStream } from "@langchain/react";

  const AGENT_URL = "http://localhost:2024";

  export function TodoAgent() {
    const stream = useStream<typeof myAgent>({
      apiUrl: AGENT_URL,
      assistantId: "deep_agent_todo_list",
    });

    const todos = stream.values?.todos ?? [];

    return (
      <div>
        <TodoList todos={todos} />
        {stream.messages.map((msg) => (
          <Message key={msg.id} message={msg} />
        ))}
      </div>
    );
  }
  ```

  ```vue Vue theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  <script setup lang="ts">
  import { useStream } from "@langchain/vue";
  import { computed } from "vue";

  const AGENT_URL = "http://localhost:2024";

  const stream = useStream<typeof myAgent>({
    apiUrl: AGENT_URL,
    assistantId: "deep_agent_todo_list",
  });

  const todos = computed(() => stream.values.value?.todos ?? []);
  </script>

  <template>
    <div>
      <TodoList :todos="todos" />
      <Message
        v-for="msg in stream.messages.value"
        :key="msg.id"
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
      assistantId: "deep_agent_todo_list",
    });

    const todos = $derived(stream.values?.todos ?? []);
  </script>

  <div>
    <TodoList {todos} />
    {#each stream.messages as msg (msg.id)}
      <Message message={msg} />
    {/each}
  </div>
  ```

  ```ts Angular theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { Component, computed } from "@angular/core";
  import { injectStream } from "@langchain/angular";

  const AGENT_URL = "http://localhost:2024";

  @Component({
    selector: "app-todo-agent",
    template: `
      <div>
        <app-todo-list [todos]="todos()" />
        @for (msg of stream.messages(); track msg.id) {
          <app-message [message]="msg" />
        }
      </div>
    `,
  })
  export class TodoAgentComponent {
    stream = injectStream<typeof myAgent>({
      apiUrl: AGENT_URL,
      assistantId: "deep_agent_todo_list",
    });

    todos = computed(() => this.stream.values()?.todos ?? []);
  }
  ```
</CodeGroup>

## Building the TodoList component

The todo list renders each item with a status icon, color coding, and visual
styling that reflects the current state:

```tsx theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
function TodoList({ todos }: { todos: Todo[] }) {
  const completed = todos.filter((t) => t.status === "completed").length;
  const percentage = todos.length
    ? Math.round((completed / todos.length) * 100)
    : 0;

  return (
    <div className="rounded-lg border bg-white p-4 shadow-sm">
      <div className="mb-4 flex items-center justify-between">
        <h2 className="text-lg font-semibold">Agent Progress</h2>
        <span className="text-sm text-gray-500">
          {completed}/{todos.length} tasks
        </span>
      </div>

      <ProgressBar percentage={percentage} />

      <ul className="mt-4 space-y-2">
        {todos.map((todo, i) => (
          <TodoItem key={i} todo={todo} />
        ))}
      </ul>
    </div>
  );
}
```

## Progress bar

A visual progress bar gives users an at-a-glance summary of overall completion:

```tsx theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
function ProgressBar({ percentage }: { percentage: number }) {
  return (
    <div className="space-y-1">
      <div className="flex items-center justify-between text-xs text-gray-500">
        <span>Progress</span>
        <span>{percentage}%</span>
      </div>
      <div className="h-2 overflow-hidden rounded-full bg-gray-200">
        <div
          className="h-full rounded-full bg-green-500 transition-all duration-500"
          style={{ width: `${percentage}%` }}
        />
      </div>
    </div>
  );
}
```

## Individual todo items

Each item gets a status icon, color-coded text, and strikethrough styling for
completed tasks:

```tsx theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
function TodoItem({ todo }: { todo: Todo }) {
  const config = {
    pending: {
      icon: "○",
      textClass: "text-gray-600",
      bgClass: "bg-gray-50",
      iconClass: "text-gray-400",
    },
    in_progress: {
      icon: "◉",
      textClass: "text-amber-800",
      bgClass: "bg-amber-50 border-amber-200",
      iconClass: "text-amber-500 animate-pulse",
    },
    completed: {
      icon: "✓",
      textClass: "text-green-800 line-through",
      bgClass: "bg-green-50 border-green-200",
      iconClass: "text-green-500",
    },
  };

  const style = config[todo.status];

  return (
    <li
      className={`flex items-start gap-3 rounded-md border px-3 py-2 ${style.bgClass}`}
    >
      <span className={`mt-0.5 text-lg leading-none ${style.iconClass}`}>
        {style.icon}
      </span>
      <span className={`text-sm ${style.textClass}`}>{todo.content}</span>
    </li>
  );
}
```

The `in_progress` icon uses `animate-pulse` to draw attention to the currently
active task.

## Calculating progress

Derive progress metrics directly from the todos array:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const todos = stream.values?.todos ?? [];

const completed = todos.filter((t) => t.status === "completed").length;
const inProgress = todos.filter((t) => t.status === "in_progress").length;
const pending = todos.filter((t) => t.status === "pending").length;
const percentage = todos.length
  ? Math.round((completed / todos.length) * 100)
  : 0;
```

These values update reactively as the agent modifies its state, keeping the
progress bar and counters in sync.

## Combining with chat messages

The todo list works alongside the regular chat interface. A practical layout
shows the todo list as a persistent sidebar or header panel, with chat messages
below:

```tsx theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
function TodoAgentLayout() {
  const stream = useStream<typeof myAgent>({
    apiUrl: AGENT_URL,
    assistantId: "deep_agent_todo_list",
  });

  const todos = stream.values?.todos ?? [];

  return (
    <div className="flex h-screen flex-col">
      {todos.length > 0 && (
        <div className="border-b bg-gray-50 p-4">
          <TodoList todos={todos} />
        </div>
      )}

      <main className="flex-1 overflow-y-auto p-6">
        <div className="mx-auto max-w-2xl space-y-4">
          {stream.messages.map((msg) => (
            <Message key={msg.id} message={msg} />
          ))}
        </div>
      </main>

      <ChatInput
        onSubmit={(text) =>
          stream.submit({ messages: [{ type: "human", content: text }] })
        }
        isLoading={stream.isLoading}
      />
    </div>
  );
}
```

<Tip>
  Show the todo list only when `todos.length > 0`. Before the agent creates its
  plan, there's nothing to display. Showing an empty component wastes space.
</Tip>

## Use cases

The todo list pattern fits any scenario where an agent executes a structured
plan:

* **Project planning**: agent breaks a project into tasks and works through
  them sequentially
* **Research workflows**: each research question becomes a todo that the agent
  investigates and completes
* **Data processing**: steps like ingestion, validation, transformation, and
  export each get their own todo
* **Onboarding flows**: agent walks through setup steps, checking off each one
  as it configures services
* **Report generation**: sections of a report become todos: gather data,
  analyze trends, write summary, format output

## Handling empty and loading states

Handle the initial state before the agent has created its plan:

```tsx theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
function TodoList({ todos, isLoading }: { todos: Todo[]; isLoading: boolean }) {
  if (todos.length === 0 && !isLoading) {
    return null;
  }

  if (todos.length === 0 && isLoading) {
    return (
      <div className="rounded-lg border bg-white p-4 shadow-sm">
        <div className="flex items-center gap-2 text-sm text-gray-500">
          <span className="animate-spin">⟳</span>
          Agent is creating a plan...
        </div>
      </div>
    );
  }

  return (
    <div className="rounded-lg border bg-white p-4 shadow-sm">
      {/* ... full todo list rendering */}
    </div>
  );
}
```

## Best practices

* **Show the todo list prominently**. It's the primary progress indicator for
  plan-based agents. Don't bury it below the fold.
* **Animate status transitions**. Smooth transitions make the agent feel more
  responsive. Use CSS transitions on background color, text decoration, and
  opacity.
* **Only highlight one `in_progress` item**. Agents typically work on one task
  at a time. If multiple items show as `in_progress`, the UI gets noisy.
  Consider only pulsing the first one.
* **Collapse or dim completed items**. As the list grows, completed items
  become less relevant. Reduce their visual weight so users focus on what's
  still happening.
* **Show the progress percentage**. A single number like "67% complete" is
  immediately understandable, even from across the room.
* **Keep the todo list in sync**. Because `stream.values` updates reactively,
  the todo list stays current automatically. Don't add manual polling or
  refresh logic.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/deepagents/frontend/todo-list.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Going to production
Source: https://docs.langchain.com/oss/python/deepagents/going-to-production

Take your deep agent to production with persistent memory, sandboxes, resilience middleware, and deployment options

This guide covers considerations for taking a deep agent from a local prototype to a production deployment. It walks through scoping memory, configuring execution environments, adding guardrails, and connecting a frontend.

## Overview

Agents use information from memory and their execution environment to accomplish tasks.
In production, there are a few primitives that determine how information is shared and accessed:

* **Thread**: a single conversation. Message history and scratch files are scoped to the thread by default and don't carry over.
* **User**: someone interacting with your agent. Memory and files can be private to a user or shared across users. Identity and authorization comes from your [auth layer](/langsmith/auth).
* **Assistant**: a configured agent instance. Memory and files can be tied to one assistant or shared across all of them.

This page covers:

* **[LangSmith Deployments](#langsmith-deployments)**: managed infrastructure with auth, webhooks, and cron
* **[Production considerations](#production-considerations)**: invocation, multi-tenancy, authentication, credentials, async, and durability
* **[Memory](#memory)**: persist information across conversations
* **[Execution environment](#execution-environment)**: file storage and code execution
* **[Guardrails](#guardrails)**: rate limiting, error handling, and data privacy
* **[Frontend](#frontend)**: connect your UI to a deployed agent

## LangSmith Deployments

<img alt="Managed Deep Agents packages your agent configuration, tools, and runtime settings for LangSmith" />

The recommended path for taking a Deep Agent to production is [Managed Deep Agents](/langsmith/managed-deep-agents-overview), an API-first hosted runtime for creating, running, and operating deep agents in LangSmith. Managed Deep Agents is currently in private preview ([join the waitlist](https://www.langchain.com/langsmith-managed-deep-agents-waitlist)). For teams that need custom application code, custom routes, advanced authentication, or full Agent Server APIs, you can configure a [LangSmith Deployment](/langsmith/deployment) directly. Either path provisions the infrastructure your agent needs: [threads](/langsmith/use-threads), [runs](/langsmith/runs), a store, and a checkpointer, so you don't have to set these up yourself. A traditional LangSmith Deployment also gives you [authentication](/langsmith/auth), [webhooks](/langsmith/use-webhooks), [cron jobs](/langsmith/cron-jobs), and [observability](/langsmith/observability) out of the box, and can expose your agent via [MCP](/langsmith/server-mcp) or [A2A](/langsmith/server-a2a).

<Tip>
  LangSmith Cloud deployments automatically send traces to a project named after your deployment. Open [LangSmith](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=oss-deepagents-going-to-production) to debug runs and monitor usage. For hybrid or self-hosted setups, see [LangSmith tracing](/langsmith/data-plane#langsmith-tracing). We recommend you also set up [LangSmith Engine](/langsmith/engine), which monitors your traces, detects issues, and proposes fixes.
</Tip>

All code snippets on this page use the following `langgraph.json` unless otherwise specified:

```json langgraph.json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "dependencies": ["."],
  "graphs": {
    "agent": "./agent.py:agent"
  },
  "env": ".env"
}
```

`langgraph.json` is the configuration file that tells the LangGraph platform how to build and run your application. It lives at the root of your project and is required for both local development (with `langgraph dev`) and production deployment. The key fields are:

| Field          | Description                                                                                                                                                                                                                                     |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `dependencies` | Packages to install. `["."]` installs the current directory as a package (reads from `requirements.txt`, `pyproject.toml`, or `package.json`).                                                                                                  |
| `graphs`       | Maps graph IDs to their code locations. Each entry is `"<id>": "./<file>:<variable>"`, where `<id>` is the name you use to invoke the graph via the API, and `<variable>` is the compiled graph or constructor function exported from `<file>`. |
| `env`          | Path to a `.env` file with environment variables (API keys, secrets). These are set at build time and available at runtime.                                                                                                                     |

For the full set of configuration options (custom Docker steps, store indexing, auth handlers, and more), see [application structure](/oss/python/langgraph/application-structure).

## Production considerations

### Invoking the agent

In production, every invocation should carry two run-level parameters:

* **`thread_id`** (passed via `config={"configurable": {"thread_id": ...}}`): a stable identifier for the conversation. The [checkpointer](#durability) uses it to persist and resume message history, so follow-up turns continue the same conversation. Generate a new `thread_id` to start a fresh conversation.
* **`context`**: per-run data your tools and middleware read at invocation time, for example `user_id`, API keys, feature flags, or session metadata. Define the shape with `context_schema` and access it via `runtime.context`. See [Runtime context](/oss/python/deepagents/context-engineering#runtime-context).

The two are independent and almost always passed together:

<CodeGroup>
  ```python Google theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from dataclasses import dataclass

  from deepagents import create_deep_agent
  from langchain_core.utils.uuid import uuid7

  @dataclass
  class Context:
      user_id: str

  agent = create_deep_agent(
      model="google_genai:gemini-3.5-flash",
      context_schema=Context,
  )

  # Start a conversation
  config = {"configurable": {"thread_id": str(uuid7())}}
  agent.invoke(
      {"messages": [{"role": "user", "content": "Plan a 3-day trip to Tokyo"}]},
      config=config,
      context=Context(user_id="user-123"),
  )

  # Follow-up on the same conversation: reuse the same thread_id
  agent.invoke(
      {"messages": [{"role": "user", "content": "Make it 5 days instead"}]},
      config=config,
      context=Context(user_id="user-123"),
  )
  ```

  ```python OpenAI theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from dataclasses import dataclass

  from deepagents import create_deep_agent
  from langchain_core.utils.uuid import uuid7

  @dataclass
  class Context:
      user_id: str

  agent = create_deep_agent(
      model="openai:gpt-5.5",
      context_schema=Context,
  )

  # Start a conversation
  config = {"configurable": {"thread_id": str(uuid7())}}
  agent.invoke(
      {"messages": [{"role": "user", "content": "Plan a 3-day trip to Tokyo"}]},
      config=config,
      context=Context(user_id="user-123"),
  )

  # Follow-up on the same conversation: reuse the same thread_id
  agent.invoke(
      {"messages": [{"role": "user", "content": "Make it 5 days instead"}]},
      config=config,
      context=Context(user_id="user-123"),
  )
  ```

  ```python Anthropic theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from dataclasses import dataclass

  from deepagents import create_deep_agent
  from langchain_core.utils.uuid import uuid7

  @dataclass
  class Context:
      user_id: str

  agent = create_deep_agent(
      model="anthropic:claude-sonnet-4-6",
      context_schema=Context,
  )

  # Start a conversation
  config = {"configurable": {"thread_id": str(uuid7())}}
  agent.invoke(
      {"messages": [{"role": "user", "content": "Plan a 3-day trip to Tokyo"}]},
      config=config,
      context=Context(user_id="user-123"),
  )

  # Follow-up on the same conversation: reuse the same thread_id
  agent.invoke(
      {"messages": [{"role": "user", "content": "Make it 5 days instead"}]},
      config=config,
      context=Context(user_id="user-123"),
  )
  ```

  ```python OpenRouter theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from dataclasses import dataclass

  from deepagents import create_deep_agent
  from langchain_core.utils.uuid import uuid7

  @dataclass
  class Context:
      user_id: str

  agent = create_deep_agent(
      model="openrouter:anthropic/claude-sonnet-4-6",
      context_schema=Context,
  )

  # Start a conversation
  config = {"configurable": {"thread_id": str(uuid7())}}
  agent.invoke(
      {"messages": [{"role": "user", "content": "Plan a 3-day trip to Tokyo"}]},
      config=config,
      context=Context(user_id="user-123"),
  )

  # Follow-up on the same conversation: reuse the same thread_id
  agent.invoke(
      {"messages": [{"role": "user", "content": "Make it 5 days instead"}]},
      config=config,
      context=Context(user_id="user-123"),
  )
  ```

  ```python Fireworks theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from dataclasses import dataclass

  from deepagents import create_deep_agent
  from langchain_core.utils.uuid import uuid7

  @dataclass
  class Context:
      user_id: str

  agent = create_deep_agent(
      model="fireworks:accounts/fireworks/models/qwen3p5-397b-a17b",
      context_schema=Context,
  )

  # Start a conversation
  config = {"configurable": {"thread_id": str(uuid7())}}
  agent.invoke(
      {"messages": [{"role": "user", "content": "Plan a 3-day trip to Tokyo"}]},
      config=config,
      context=Context(user_id="user-123"),
  )

  # Follow-up on the same conversation: reuse the same thread_id
  agent.invoke(
      {"messages": [{"role": "user", "content": "Make it 5 days instead"}]},
      config=config,
      context=Context(user_id="user-123"),
  )
  ```

  ```python Baseten theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from dataclasses import dataclass

  from deepagents import create_deep_agent
  from langchain_core.utils.uuid import uuid7

  @dataclass
  class Context:
      user_id: str

  agent = create_deep_agent(
      model="baseten:zai-org/GLM-5",
      context_schema=Context,
  )

  # Start a conversation
  config = {"configurable": {"thread_id": str(uuid7())}}
  agent.invoke(
      {"messages": [{"role": "user", "content": "Plan a 3-day trip to Tokyo"}]},
      config=config,
      context=Context(user_id="user-123"),
  )

  # Follow-up on the same conversation: reuse the same thread_id
  agent.invoke(
      {"messages": [{"role": "user", "content": "Make it 5 days instead"}]},
      config=config,
      context=Context(user_id="user-123"),
  )
  ```

  ```python Ollama theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from dataclasses import dataclass

  from deepagents import create_deep_agent
  from langchain_core.utils.uuid import uuid7

  @dataclass
  class Context:
      user_id: str

  agent = create_deep_agent(
      model="ollama:devstral-2",
      context_schema=Context,
  )

  # Start a conversation
  config = {"configurable": {"thread_id": str(uuid7())}}
  agent.invoke(
      {"messages": [{"role": "user", "content": "Plan a 3-day trip to Tokyo"}]},
      config=config,
      context=Context(user_id="user-123"),
  )

  # Follow-up on the same conversation: reuse the same thread_id
  agent.invoke(
      {"messages": [{"role": "user", "content": "Make it 5 days instead"}]},
      config=config,
      context=Context(user_id="user-123"),
  )
  ```
</CodeGroup>

When deploying with the LangGraph SDK, the SDK manages threads for you and you pass the returned `thread_id` to each run:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langgraph_sdk import get_client

client = get_client(url="<DEPLOYMENT_URL>", api_key="<LANGSMITH_API_KEY>")

thread = await client.threads.create()
async for chunk in client.runs.stream(
    thread["thread_id"],  # [!code highlight]
    "agent",
    input={"messages": [{"role": "user", "content": "Plan a 3-day trip to Tokyo"}]},
    context={"user_id": "user-123"},  # [!code highlight]
    stream_mode="updates",
):
    print(chunk.data)
```

<Tip>
  `thread_id` scopes the *conversation* (message history, checkpoints). `context` carries *per-run* data your tools and middleware read. They are independent: changing one does not affect the other, and you can pass either or both.
</Tip>

### Multi-tenancy

When your agent serves multiple users, you need to handle three concerns: verifying who each user is, controlling what they can access, and managing the credentials the agent uses to act on their behalf.

<img alt="Three authentication layers compose: end-user auth, agent-acting-as-user auth, and team RBAC" />

#### User identity and access control

[LangSmith Deployments](/langsmith/deployment) supports [custom authentication](/langsmith/custom-auth) to establish user identity and [authorization handlers](/langsmith/auth) to control access to resources like threads, assistants, and store namespaces. Authorization handlers run after authentication succeeds and can:

* Tag resources with ownership metadata (e.g., `owner: user_id`)
* Return filters so users only see their own resources
* Deny access with HTTP 403 for unauthorized operations

For a step-by-step tutorial, see [Make conversations private](/langsmith/resource-auth). For a walkthrough, watch the [custom auth video](https://www.youtube.com/watch?v=DkNqgCz8cjE).

How you [scope memory](#scoping) and [execution environments](#execution-environment) determines what data is shared between users. See the sections below for details.

#### Team access control (RBAC)

LangSmith's [role-based access control](/langsmith/rbac) governs who on your team can deploy, configure, and monitor agents. This is separate from end-user authorization above.

| Role             | Access                                                                |
| ---------------- | --------------------------------------------------------------------- |
| Workspace Admin  | Full permissions including settings and member management             |
| Workspace Editor | Create and modify resources, but cannot delete runs or manage members |
| Workspace Viewer | Read-only access                                                      |

Custom roles with granular permissions are available on Enterprise plans. See the [RBAC reference](/langsmith/rbac) for the full permission model.

#### End-user credentials

When your agent needs to call external APIs on behalf of a user (e.g., reading their GitHub repos, sending Slack messages, querying their data warehouse), you need a way to pass the user's credentials through to the agent without hardcoding them.

**OAuth via Agent Auth.** [Agent Auth](/langsmith/agent-auth) provides a managed OAuth 2.0 flow. Configure an OAuth provider, and the agent can request tokens scoped to each user. On first use, the agent [interrupts](/oss/python/langgraph/interrupts) execution and presents an OAuth consent URL. After the user authenticates, the agent resumes with a valid token. Tokens are stored and refreshed automatically.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_auth import Client
from langchain.tools import tool, ToolRuntime

auth_client = Client()
