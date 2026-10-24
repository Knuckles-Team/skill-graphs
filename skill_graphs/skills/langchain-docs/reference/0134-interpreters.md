# Interpreters
Source: https://docs.langchain.com/oss/javascript/deepagents/interpreters

Run lightweight code inside Deep Agents to compose tools, orchestrate subagents, and transform structured data

Interpreters give agents a programmable workspace where they can explore data, coordinate tool calls, and keep intermediate work out of the model context. The agent writes code to express its intent, then an **in-memory** runtime executes that code and returns the relevant results.

Where [sandboxes](/oss/javascript/deepagents/sandboxes) are a code-first way for acting on an environment (such as running commands, installing dependencies, and editing files), interpreters are a code-first way for acting inside the agent loop: composing tools, preserving state, and deciding what information should return to the model.

<Warning>
  Interpreters are in [**beta**](/oss/javascript/versioning). APIs and lifecycle behavior may change between releases.
</Warning>

## Why use interpreters?

Most agent work alternates between model reasoning and tool calls. A model can fire several tool calls in one turn, but that batch is fixed the moment it is emitted. Nothing can loop, branch on a result, retry a failure, or feed one call's output into the next without another model turn, and every result returns to the model's context. The model also decides how many calls to issue, so asking it to dispatch work across hundreds of items is unreliable, and it tends to cover a sample rather than every one.

Interpreters give the agent a runtime for that work. A loop runs every iteration, tools are called from code, intermediate values stay in variables, and only a compact result returns to the model.

<CardGroup>
  <Card title="Programmatic tool calling (PTC)" icon="tool" href="#programmatic-tool-calling-ptc">
    Call selected tools from interpreter code, including loops, retries, branching, and parallel batches.
  </Card>

  <Card title="Programmatic subagents" icon="arrows-split" href="/oss/javascript/deepagents/programmatic-subagents">
    Dispatch subagents from code for fan-out, verification, and recursive workflows over large inputs.
  </Card>

  <Card title="Stateful work" icon="database" href="#how-interpreters-work">
    Keep intermediate values in runtime state without overloading the model context.
  </Card>

  <Card title="Deterministic transforms" icon="code" href="#how-interpreters-work">
    Sort, group, parse, validate, score, aggregate, and explore structured data in code.
  </Card>
</CardGroup>

## Choose a pattern

Use interpreters for code inside the agent loop: composing tools, preserving state, and controlling what returns to the model. Use [sandboxes](/oss/javascript/deepagents/sandboxes) for code against an environment: shell commands, package installs, tests, filesystem edits, and OS-level execution.

| Need                                                                                           | Use                                                                                          |
| ---------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| One or two simple external calls                                                               | Normal tool calling                                                                          |
| A small program that loops, branches, retries, or aggregates results                           | Interpreter                                                                                  |
| Many selected tool calls that should run from code                                             | Interpreter with [programmatic tool calling (PTC)](#programmatic-tool-calling-ptc)           |
| Many independent units of work, multiple perspectives, or recursive analysis over large inputs | Interpreter with [programmatic subagents](/oss/javascript/deepagents/programmatic-subagents) |
| Shell commands, package installs, tests, or full OS filesystem access                          | [Sandboxes](/oss/javascript/deepagents/sandboxes)                                            |

## Quickstart

Install the QuickJS middleware package, then pass interpreter middleware using the `middleware` argument on `create_deep_agent`.

<CodeGroup>
  ```bash npm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  npm install deepagents @langchain/quickjs
  ```

  ```bash pnpm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pnpm add deepagents @langchain/quickjs
  ```

  ```bash yarn theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  yarn add deepagents @langchain/quickjs
  ```
</CodeGroup>

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { createDeepAgent } from "deepagents";
import { createCodeInterpreterMiddleware } from "@langchain/quickjs";

const agent = createDeepAgent({
  model: "openai:gpt-5.5",
  middleware: [createCodeInterpreterMiddleware()],
});
```

## How interpreters work

The middleware adds an `eval` tool to the agent. When useful, the agent writes JavaScript and calls `eval`; you do not call the interpreter directly. The tool runs code in a persistent context, captures `console.log`, and returns the result of the last expression.

The agent can write code like this:

```javascript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const rows = [
  { team: "alpha", score: 8 },
  { team: "beta", score: 13 },
  { team: "alpha", score: 21 },
];

const totals = rows.reduce((acc, row) => {
  acc[row.team] = (acc[row.team] ?? 0) + row.score;
  console.log(`${row.team} score: ${acc[row.team]}`)
  return acc;
}, {});

totals;
```

Code runs against [**QuickJS**](https://github.com/quickjs-ng/quickjs), a lightweight JavaScript runtime. By default, interpreter code has no access to the host filesystem, network, shell, package manager, or clock. It can compute, hold state, and write to `console.log`, and nothing more.

Two explicit bridges extend that reach:

* **Tools**, through [programmatic tool calling (PTC)](#programmatic-tool-calling-ptc). Expose an allowlist of tools as async functions under the `tools` namespace. These can be the agent's own tools or standalone tools you define and pass in.
* **Subagents**, through [programmatic subagents](/oss/javascript/deepagents/programmatic-subagents). Dispatch configured subagents from code and orchestrate them in plain JavaScript.

Programmatic tool calling is off until you [enable it](#enable-ptc). Subagent dispatch is on by default whenever the agent has subagents, and you can turn it off. Nothing else crosses the QuickJS boundary unless you expose it.

## Programmatic tool calling (PTC)

Programmatic tool calling (PTC) exposes selected agent tools inside the interpreter under the global `tools` namespace. Instead of asking the model to issue one tool call, wait for the result, and then decide the next call, the agent can write code that calls tools in loops, branches, retries, or parallel batches.

This helps when intermediate results are only inputs to the next step: the interpreter filters or aggregates them before anything returns to the model, keeping multi-step workflows token-efficient. It is model-agnostic, implemented by middleware rather than a provider-specific tool-calling API.

The middleware exposes each allowlisted tool as an async function under `tools`. The agent calls it with `await`, processes the result in code, and the model sees only the final interpreter output, not every intermediate value. Tool names are converted to camel case while the input object still follows the tool's schema, so a tool named `web_search` becomes `tools.webSearch(...)`:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const result: string = await tools.webSearch({
  query: "deepagents interpreters",
});
```

### Enable PTC

Enable PTC with an explicit allowlist:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { createDeepAgent } from "deepagents";
import { createCodeInterpreterMiddleware } from "@langchain/quickjs";

const agent = createDeepAgent({
  model: "openai:gpt-5.5",
  middleware: [createCodeInterpreterMiddleware({ ptc: ["web_search"] })],
});
```

After PTC is enabled, the agent can call the allowlisted tool from interpreter code. This example searches several topics in parallel and combines the results before returning to the model:

```javascript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const topics = ["retrieval", "memory", "evaluation"];

const results = await Promise.all(
  topics.map((topic) =>
    tools.webSearch({ query: `${topic} best practices 2025` }),
  ),
);

results.join("\n\n");
```

<Warning>
  PTC calls currently execute through the interpreter bridge and do not go through the normal tool calling path. As a result, `interruptOn` approval workflows are not enforced per PTC-invoked tool call.
</Warning>

## Programmatic subagents

Programmatic subagents let the interpreter dispatch configured [subagents](/oss/javascript/deepagents/subagents) from code using the built-in `task()` global. A task that spans many independent units, such as reviewing every file in a directory or triaging a batch of tickets, becomes a loop that fans work out and synthesizes the results.

Use programmatic subagents for:

* **Fan-out and synthesize**: Run the same kind of work across many items in parallel, then combine the results.
* **Verification**: Send findings to independent verifier subagents and keep only confirmed results.
* **Recursive workflows**: Keep a working set in interpreter variables, select slices, call subagents, and refine the result.

For configuration, examples, orchestration patterns, and safety notes, see [Programmatic subagents](/oss/javascript/deepagents/programmatic-subagents).

## Security

Interpreters use QuickJS to run untrusted JavaScript with strict default isolation. Treat that as a scoped interpreter runtime, not a full production sandbox backend.

Every tool you expose through PTC is an outside capability that interpreter code can use. Treat the PTC allowlist as a permission boundary: expose only the tools the agent needs, and avoid bridging broad tools that can access sensitive systems, spend money, mutate data, or call unrestricted networks unless that behavior is intentional.

| Capability                                                  | Available by default | How to expose it                                                                                                        |
| ----------------------------------------------------------- | -------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| JavaScript execution                                        | Yes                  | Add interpreter middleware                                                                                              |
| Top-level `await`                                           | Yes                  | Use promises in interpreter code                                                                                        |
| `console.log` capture                                       | Yes                  | Disable with `captureConsole: false`                                                                                    |
| Agent tools                                                 | No                   | Add a PTC allowlist                                                                                                     |
| Filesystem access                                           | No                   | Add the [built-in filesystem tools](/oss/javascript/deepagents/harness#virtual-filesystem-access) via the PTC allowlist |
| Network access                                              | No                   | Expose a specific network tool through PTC                                                                              |
| Wall-clock or datetime access                               | No                   | Expose an explicit time tool if needed                                                                                  |
| Shell commands, package installs, tests, OS-level execution | No                   | Use a [sandbox backend](/oss/javascript/deepagents/sandboxes)                                                           |

## Configuration

`createCodeInterpreterMiddleware` accepts the following options:

| Option               | Default                          | Purpose                                                                                                                                                                                               |
| -------------------- | -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ptc`                | omitted                          | PTC allowlist: array of tool names or `StructuredToolInterface` instances.                                                                                                                            |
| `memoryLimitBytes`   | `64 * 1024 * 1024` <br />(64 MB) | QuickJS memory limit in bytes.                                                                                                                                                                        |
| `maxStackSizeBytes`  | `320 * 1024`                     | QuickJS stack size limit in bytes.                                                                                                                                                                    |
| `executionTimeoutMs` | `5000`                           | Per-eval timeout in milliseconds. Negative values disable the timeout.                                                                                                                                |
| `systemPrompt`       | `null`                           | Override the built-in interpreter system prompt.                                                                                                                                                      |
| `maxPtcCalls`        | `256`                            | Maximum `tools.*` calls per eval. Use `null` only in trusted environments.                                                                                                                            |
| `maxResultChars`     | `4000`                           | Maximum characters retained from console output, result, and error strings.                                                                                                                           |
| `toolName`           | `"eval"`                         | Name of the interpreter tool exposed to the model.                                                                                                                                                    |
| `captureConsole`     | `true`                           | Whether `console.log`, `console.warn`, and `console.error` output is captured.                                                                                                                        |
| `subagents`          | `true`                           | Expose the built-in `task()` global for [programmatic subagents](/oss/javascript/deepagents/programmatic-subagents). Set to `false` to require subagent dispatch through the normal `task` tool path. |

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/deepagents/interpreters.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Model Context Protocol
Source: https://docs.langchain.com/oss/javascript/deepagents/mcp

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/deepagents/mcp.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Memory
Source: https://docs.langchain.com/oss/javascript/deepagents/memory

Add persistent memory to agents built with Deep Agents so they learn and improve across conversations

Memory lets your agent learn and improve across conversations. Deep Agents makes memory first class with filesystem-backed memory: the agent reads and writes memory as files, and you control where those files are stored using [backends](/oss/javascript/deepagents/backends).

<Note>
  This page covers **long-term memory**: memory that persists across conversations. For short-term memory (conversation history and scratch files within a single session), see the [context engineering](/oss/javascript/deepagents/context-engineering) guide. Short-term memory is managed automatically as part of the agent's [state](/oss/javascript/langgraph/graph-api#state).

  <img alt="Short-term memory is scoped to a single thread via checkpoints; long-term memory persists across threads via the store" />
</Note>

## How memory works

1. **Point the agent at memory files.** Pass file paths to `memory=` when creating the agent. You can also pass [skills](/oss/javascript/deepagents/skills) via `skills=` for procedural memory (reusable instructions that tell the agent *how* to perform a task). A [backend](/oss/javascript/deepagents/backends) controls where files are stored and who can access them.
2. **Agent reads memory.** The agent can load memory files into the system prompt at startup, or read them on demand during the conversation. For example, [skills](/oss/javascript/deepagents/skills) use on-demand loading: the agent reads only skill descriptions at startup, then reads the full skill file only when it matches a task. This keeps context lean until a capability is needed.
3. **Agent updates memory (optional).** When the agent learns new information, it can use its built-in `edit_file` tool to update memory files. Updates can happen during the conversation (the default) or in the background between conversations via [background consolidation](#background-consolidation). Changes are persisted and available in the next conversation. Not all memory is writable: developer-defined [skills](/oss/javascript/deepagents/skills) and [organization policies](#organization-level-memory) are typically read-only. See [read-only vs writable memory](#read-only-vs-writable-memory) for details.

The two most common patterns are [agent-scoped memory](#agent-scoped-memory) (shared across all users) and [user-scoped memory](#user-scoped-memory) (isolated per user).

## Scoped memory

Agent memory can be scoped so the same memory files are accessible to everyone using the agent or memory files can be individual to each user.

### Agent-scoped memory

Give the agent its own persistent identity that evolves over time. Agent-scoped memory is shared across all users, so the agent builds up its own persona, accumulated knowledge, and learned preferences through every conversation. As it interacts with users, it develops expertise, refines its approach, and remembers what works. It can also learn and update [skills](/oss/javascript/deepagents/skills) when it has write access.

The key is the backend namespace: setting it to `(assistant_id,)` means every conversation for this agent reads and writes to the same memory file.

<Note>
  Accessing `rt.serverInfo` requires `deepagents>=1.9.0`. On older versions, read the assistant ID from `getConfig().metadata.assistantId` instead.
</Note>

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { createDeepAgent, CompositeBackend, StateBackend, StoreBackend } from "deepagents";

const agent = createDeepAgent({
  memory: ["/memories/AGENTS.md"],
  skills: ["/skills/"],
  backend: new CompositeBackend(
    new StateBackend(),
    {
      "/memories/": new StoreBackend({
        namespace: (rt) => [rt.serverInfo.assistantId],  // [!code highlight]
      }),
      "/skills/": new StoreBackend({
        namespace: (rt) => [rt.serverInfo.assistantId],  // [!code highlight]
      }),
    },
  ),
});
```

<Accordion title="Full example: seed memory and invoke">
  Populate the store with initial memories, then invoke the agent across two threads to see it remember and update what it learns.

  ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createDeepAgent, CompositeBackend, StateBackend, StoreBackend, createFileData } from "deepagents";
  import { InMemoryStore } from "@langchain/langgraph";

  const store = new InMemoryStore();  // Use platform store when deploying to LangSmith

  // Seed the memory file
  await store.put(
    ["my-agent"],
    "/memories/AGENTS.md",
    createFileData(`## Response style
  - Keep responses concise
  - Use code examples where possible
  `),
  );

  // Seed a skill
  await store.put(
    ["my-agent"],
    "/skills/langgraph-docs/SKILL.md",
    createFileData(`---
  name: langgraph-docs
  description: Fetch relevant LangGraph documentation to provide accurate guidance.
  ---

  # langgraph-docs

  Use the fetch_url tool to read https://docs.langchain.com/llms.txt, then fetch relevant pages.
  `),
  );

  const agent = createDeepAgent({
    memory: ["/memories/AGENTS.md"],
    skills: ["/skills/"],
    backend: (rt) => new CompositeBackend(
      new StateBackend(rt),
      {
        "/memories/": new StoreBackend(rt, {
          namespace: (rt) => ["my-agent"],
        }),
        "/skills/": new StoreBackend(rt, {
          namespace: (rt) => ["my-agent"],
        }),
      },
    ),
    store,
  });

  // Thread 1: the agent learns a new preference and saves it to memory
  const config1 = { configurable: { thread_id: crypto.randomUUID() } };
  await agent.invoke({
    messages: [{ role: "user", content: "I prefer detailed explanations. Remember that." }],
  }, config1);

  // Thread 2: the agent reads memory and applies the preference
  const config2 = { configurable: { thread_id: crypto.randomUUID() } };
  await agent.invoke({
    messages: [{ role: "user", content: "Explain how transformers work." }],
  }, config2);
  ```
</Accordion>

### User-scoped memory

Give each user their own memory file. The agent remembers preferences, context, and history per user while core agent instructions stay fixed. Users can also have per-user [skills](/oss/javascript/deepagents/skills) if stored in a user-scoped backend.

The namespace uses `(user_id,)` so each user gets an isolated copy of the memory file. User A's preferences never leak into User B's conversations.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { createDeepAgent, CompositeBackend, StateBackend, StoreBackend } from "deepagents";

const agent = createDeepAgent({
  memory: ["/memories/preferences.md"],
  skills: ["/skills/"],
  backend: new CompositeBackend(
    new StateBackend(),
    {
      "/memories/": new StoreBackend({
        namespace: (rt) => [rt.serverInfo.user.identity],
      }),
      "/skills/": new StoreBackend({
        namespace: (rt) => [rt.serverInfo.user.identity],
      }),
    },
  ),
});
```

<Accordion title="Full example: isolated memory across users">
  Seed per-user memories and invoke the agent as two different users. Each user sees only their own preferences.

  ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createDeepAgent, CompositeBackend, StateBackend, StoreBackend, createFileData } from "deepagents";
  import { InMemoryStore } from "@langchain/langgraph";

  const store = new InMemoryStore();  // Use platform store when deploying to LangSmith

  // Seed preferences for two users
  await store.put(
    ["user-alice"],
    "/memories/preferences.md",
    createFileData(`## Preferences
  - Likes concise bullet points
  - Prefers Python examples
  `),
  );
  await store.put(
    ["user-bob"],
    "/memories/preferences.md",
    createFileData(`## Preferences
  - Likes detailed explanations
  - Prefers TypeScript examples
  `),
  );

  // Seed a skill for Alice
  await store.put(
    ["user-alice"],
    "/skills/langgraph-docs/SKILL.md",
    createFileData(`---
  name: langgraph-docs
  description: Fetch relevant LangGraph documentation to provide accurate guidance.
  ---

  # langgraph-docs

  Use the fetch_url tool to read https://docs.langchain.com/llms.txt, then fetch relevant pages.
  `),
  );

  const agent = createDeepAgent({
    memory: ["/memories/preferences.md"],
    skills: ["/skills/"],
    backend: (rt) => new CompositeBackend(
      new StateBackend(rt),
      {
        "/memories/": new StoreBackend(rt, {
          namespace: (rt) => [rt.serverInfo.user.identity],
        }),
        "/skills/": new StoreBackend(rt, {
          namespace: (rt) => [rt.serverInfo.user.identity],
        }),
      },
    ),
    store,
  });

  // When deployed, each authenticated request resolves
  // `rt.serverInfo.user.identity` to the calling user, so Alice and Bob
  // automatically see only their own preferences.
  await agent.invoke(
    { messages: [{ role: "user", content: "How do I read a CSV file?" }] },
    { configurable: { thread_id: crypto.randomUUID() } },
  );
  ```
</Accordion>

## Advanced usage

On top of the basic configuration options for memory paths and scope, you can also configure more advanced parameters for memory:

| Dimension             | Question it answers             | Options                                                                                                                                                                                            |
| --------------------- | ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Duration**          | How long does it last?          | [Short-term](/oss/javascript/deepagents/context-engineering) (single conversation) or [long-term](#scoped-memory) (across conversations)                                                           |
| **Information type**  | What kind of information is it? | [Episodic](#episodic-memory) (past experiences), [procedural](/oss/javascript/deepagents/skills) (instructions and skills), or [semantic](/oss/javascript/concepts/memory#semantic-memory) (facts) |
| **Scope**             | Who can see and modify it?      | [User](#user-scoped-memory), [agent](#agent-scoped-memory), or [organization](#organization-level-memory)                                                                                          |
| **Update strategy**   | When are memories written?      | During conversation (default) or [between conversations](#background-consolidation)                                                                                                                |
| **Retrieval**         | How are memories read?          | Loaded into prompt (default) or on demand (e.g., [skills](/oss/javascript/deepagents/skills))                                                                                                      |
| **Agent permissions** | Can the agent write to memory?  | [Read-write](#read-only-vs-writable-memory) (default) or [read-only](#read-only-vs-writable-memory) (for shared policies)                                                                          |

### Episodic memory

Episodic memory stores records of past experiences: what happened, in what order, and what the outcome was. Unlike semantic memory (facts and preferences stored in files like `AGENTS.md`), episodic memory preserves the full conversational context so the agent can recall *how* a problem was solved, not just *what* was learned from it.

Deep Agents already use [checkpointers](/oss/javascript/langgraph/checkpointers#checkpoints) which is the mechanism that supports episodic memory: every conversation is persisted as a checkpointed thread.

To make past conversations searchable, wrap thread search in a tool. The `user_id` is pulled from the runtime context rather than passed as a parameter:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { Client } from "@langchain/langgraph-sdk";
import { tool } from "@langchain/core/tools";

const client = new Client({ apiUrl: "<DEPLOYMENT_URL>" });

const searchPastConversations = tool(
  async ({ query }, runtime) => {
    const userId = runtime.serverInfo.user.identity;  // [!code highlight]
    const threads = await client.threads.search({
      metadata: { userId },
      limit: 5,
    });
    const results = [];
    for (const thread of threads) {
      const history = await client.threads.getHistory(thread.threadId);
      results.push(history);
    }
    return JSON.stringify(results);
  },
  {
    name: "search_past_conversations",
    description: "Search past conversations for relevant context.",
  }
);
```

You can scope thread search by user or organization by adjusting the metadata filter:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
// Search conversations for a specific user
const userThreads = await client.threads.search({
  metadata: { userId },
  limit: 5,
});

// Search conversations across an organization
const orgThreads = await client.threads.search({
  metadata: { orgId },
  limit: 5,
});
```

This is useful for agents that perform complex, multi-step tasks. For example, a coding agent can look back at a past debugging session and skip straight to the likely root cause.

### Organization-level memory

Organization-level memory follows the same pattern as user-scoped memory, but with an organization-wide namespace instead of a per-user one. Use it for policies or knowledge that should apply across all users and agents in an organization.

Organization memory is typically **read-only** to prevent prompt injection via shared state. See [read-only vs writable memory](#read-only-vs-writable-memory) for details.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { createDeepAgent, CompositeBackend, StateBackend, StoreBackend } from "deepagents";

const agent = createDeepAgent({
  memory: [
    "/memories/preferences.md",
    "/policies/compliance.md",
  ],
  backend: new CompositeBackend(
    new StateBackend(),
    {
      "/memories/": new StoreBackend({
        namespace: (rt) => [rt.serverInfo.user.identity],
      }),
      "/policies/": new StoreBackend({
        namespace: (rt) => [rt.context.orgId],
      }),
    },
  ),
});
```

Populate organization memory from your application code:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { Client } from "@langchain/langgraph-sdk";
import { createFileData } from "deepagents";

const client = new Client({ apiUrl: "<DEPLOYMENT_URL>" });

await client.store.putItem(
  [orgId],
  "/compliance.md",
  createFileData(`## Compliance policies
- Never disclose internal pricing
- Always include disclaimers on financial advice
`),
);
```

Use [permissions](/oss/javascript/deepagents/permissions) to enforce that org-level memory is read-only, or [policy hooks](/oss/javascript/deepagents/backends#add-policy-hooks) for custom validation logic.

### Background consolidation

By default, the agent writes memories during the conversation (hot path). An alternative is to process memories **between conversations** as a background task, sometimes called **sleep time compute**. A separate deep agent reviews recent conversations, extracts key facts, and merges them with existing memories.

| Approach                               | Pros                                                                 | Cons                                                                    |
| -------------------------------------- | -------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| **Hot path** (during conversation)     | Memories available immediately, transparent to user                  | Adds latency, agent must multitask                                      |
| **Background** (between conversations) | No user-facing latency, can synthesize across multiple conversations | Memories not available until next conversation, requires a second agent |

For most applications, the hot path is sufficient. Add background consolidation when you need to reduce latency or improve memory quality across many conversations.

The recommended pattern is to deploy a **consolidation agent** alongside your main agent — a deep agent that reads recent conversation history, extracts key facts, and merges them into the memory store — and trigger it on a [cron schedule](#cron). Pick a cadence that reflects how often your users actually interact with the agent: a chat product with steady daily traffic might consolidate every few hours, while a tool used a handful of times per week only needs to run nightly or weekly. Consolidating much more often than users converse just burns tokens on no-op runs.

#### Consolidation agent

The consolidation agent reads recent conversation history and merges key facts into the memory store. Register it alongside your main agent in `langgraph.json`:

```typescript src/consolidation-agent.ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { createDeepAgent } from "deepagents";
import { Client } from "@langchain/langgraph-sdk";
import { tool } from "@langchain/core/tools";

const sdkClient = new Client({ apiUrl: "<DEPLOYMENT_URL>" });

const searchRecentConversations = tool(
  async ({ query }, runtime) => {
    const userId = runtime.serverInfo.user.identity;  // [!code highlight]

    const since = new Date(Date.now() - 6 * 60 * 60 * 1000).toISOString();
    const threads = await sdkClient.threads.search({
      metadata: { userId },
      updatedAfter: since,
      limit: 20,
    });
    const conversations = [];
    for (const thread of threads) {
      const history = await sdkClient.threads.getHistory(thread.threadId);
      conversations.push(history.values.messages);
    }
    return JSON.stringify(conversations);
  },
  {
    name: "search_recent_conversations",
    description: "Search this user's conversations updated in the last 6 hours.",
  }
);

const agent = createDeepAgent({
  model: "google_genai:gemini-3.5-flash",
  systemPrompt: `Review recent conversations and update the user's memory file.
Merge new facts, remove outdated information, and keep it concise.`,
  tools: [searchRecentConversations],
});

export { agent };
```

```json langgraph.json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "dependencies": ["."],
  "graphs": {
    "agent": "./src/agent.ts:agent",
    "consolidation_agent": "./src/consolidation-agent.ts:agent"
  },
  "env": ".env"
}
```

#### Cron

A [cron job](/langsmith/cron-jobs) runs the consolidation agent on a fixed schedule. The agent searches recent conversations and synthesizes them into memory. Match the schedule to your usage patterns so consolidation runs roughly track real activity.

```mermaid theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
graph LR
    Store[(Memory store)] -.->|reads| Conv1[Conversation 1]
    Store -.->|reads| Conv2[Conversation 2]
    Cron[Cron schedule] -->|periodic| Agent[Consolidation agent]
    Agent -->|writes| Store

    classDef trigger fill:#F6FFDB,stroke:#6E8900,stroke-width:2px,color:#2E3900
    classDef process fill:#E5F4FF,stroke:#006DDD,stroke-width:2px,color:#030710
    classDef output fill:#EBD0F0,stroke:#885270,stroke-width:2px,color:#441E33
    classDef schedule fill:#FDF3FF,stroke:#7E65AE,stroke-width:2px,color:#504B5F

    class Conv1,Conv2 trigger
    class Agent process
    class Store output
    class Cron schedule
```

Schedule the consolidation agent with a cron job:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { Client } from "@langchain/langgraph-sdk";

const client = new Client({ apiUrl: "<DEPLOYMENT_URL>" });

const cronJob = await client.crons.create(
  "consolidation_agent",
  {
    schedule: "0 */6 * * *",
    input: { messages: [{ role: "user", content: "Consolidate recent memories." }] },
  },
);
```

<Note>
  All cron schedules are interpreted in **UTC**. See [cron jobs](/langsmith/cron-jobs) for details on managing and deleting cron jobs.
</Note>

<Warning>
  The cron interval must match the lookback window inside the consolidation agent. The example above runs every 6 hours (`0 */6 * * *`) and the agent's `search_recent_conversations` tool looks back `timedelta(hours=6)` — keep these in sync. If the cron runs more often than the lookback, you'll reprocess the same conversations; if it runs less often, you'll drop memories that fall outside the window.
</Warning>

For more on deploying agents with background processes, see [going to production](/oss/javascript/deepagents/going-to-production).

### Read-only vs writable memory

By default, the agent can both read and write memory files. For shared state like organization policies or compliance rules, you may want to make memory **read-only** so the agent can reference it but not modify it. This prevents prompt injection via shared memory and ensures that only your application code controls what's in the file.

| Permission               | Use case                                                                                                                       | How it works                                                                                                                                                                                                                                                                |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Read-write** (default) | User preferences, agent self-improvement, learned [skills](/oss/javascript/deepagents/skills)                                  | Agent updates files via `edit_file` tool                                                                                                                                                                                                                                    |
| **Read-only**            | Organization policies, compliance rules, shared knowledge bases, developer-defined [skills](/oss/javascript/deepagents/skills) | Populate via application code or the [Store API](/langsmith/custom-store). Use [permissions](/oss/javascript/deepagents/permissions) to deny writes to specific paths, or [policy hooks](/oss/javascript/deepagents/backends#add-policy-hooks) for custom validation logic. |

**Security considerations:** If one user can write to memory that another user reads, a malicious user could inject instructions into shared state. To mitigate this:

* **Default to user scope** `(user_id)` unless you have a specific reason to share
* Use **read-only memory** for shared policies (populate via application code, not the agent)
* Add **human-in-the-loop** validation before the agent writes to shared memory. Use an [interrupt](/oss/javascript/langgraph/interrupts) to require human approval for writes to sensitive paths.

To enforce read-only memory, use [permissions](/oss/javascript/deepagents/permissions) to declaratively deny writes to specific paths. For custom validation logic (rate limiting, audit logging, content inspection), use [backend policy hooks](/oss/javascript/deepagents/backends#add-policy-hooks).

### Concurrent writes

Multiple threads can write to memory in parallel, but concurrent writes to the **same file** can cause last-write-wins conflicts. For user-scoped memory this is rare since users typically have one active conversation at a time. For agent-scoped or organization-scoped memory, consider using [background consolidation](#background-consolidation) to serialize writes, or structure memory as separate files per topic to reduce contention.

In practice, if a write fails due to a conflict, the LLM is usually smart enough to retry or recover gracefully, so a single lost write is not catastrophic.

### Multiple agents in the same deployment

To give each agent its own memory in a shared deployment, add `assistant_id` to the namespace:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
new StoreBackend({
  namespace: (rt) => [
    rt.serverInfo.assistantId,  // [!code highlight]
    rt.serverInfo.user.identity,
  ],
})
```

Use `assistant_id` alone if you only need per-agent isolation without per-user scoping.

<Tip>
  Use [LangSmith tracing](/langsmith/trace-with-langgraph) to audit what your agent writes to memory. Every file write appears as a tool call in the trace.
</Tip>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/deepagents/memory.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
