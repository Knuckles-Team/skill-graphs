# Interpreters
Source: https://docs.langchain.com/oss/python/deepagents/interpreters

Run lightweight code inside Deep Agents to compose tools, orchestrate subagents, and transform structured data

Interpreters give agents a programmable workspace where they can explore data, coordinate tool calls, and keep intermediate work out of the model context. The agent writes code to express its intent, then an **in-memory** runtime executes that code and returns the relevant results.

Where [sandboxes](/oss/python/deepagents/sandboxes) are a code-first way for acting on an environment (such as running commands, installing dependencies, and editing files), interpreters are a code-first way for acting inside the agent loop: composing tools, preserving state, and deciding what information should return to the model.

<Warning>
  Interpreters are in [**beta**](/oss/python/versioning). APIs and lifecycle behavior may change between releases.
</Warning>

<Note>
  Interpreters require `langchain-quickjs>=0.1.0` and Python `>=3.11`.
</Note>

## Why use interpreters?

Most agent work alternates between model reasoning and tool calls. A model can fire several tool calls in one turn, but that batch is fixed the moment it is emitted. Nothing can loop, branch on a result, retry a failure, or feed one call's output into the next without another model turn, and every result returns to the model's context. The model also decides how many calls to issue, so asking it to dispatch work across hundreds of items is unreliable, and it tends to cover a sample rather than every one.

Interpreters give the agent a runtime for that work. A loop runs every iteration, tools are called from code, intermediate values stay in variables, and only a compact result returns to the model.

<CardGroup>
  <Card title="Programmatic tool calling (PTC)" icon="tool" href="#programmatic-tool-calling-ptc">
    Call selected tools from interpreter code, including loops, retries, branching, and parallel batches.
  </Card>

  <Card title="Programmatic subagents" icon="arrows-split" href="/oss/python/deepagents/programmatic-subagents">
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

Use interpreters for code inside the agent loop: composing tools, preserving state, and controlling what returns to the model. Use [sandboxes](/oss/python/deepagents/sandboxes) for code against an environment: shell commands, package installs, tests, filesystem edits, and OS-level execution.

| Need                                                                                           | Use                                                                                      |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| One or two simple external calls                                                               | Normal tool calling                                                                      |
| A small program that loops, branches, retries, or aggregates results                           | Interpreter                                                                              |
| Many selected tool calls that should run from code                                             | Interpreter with [programmatic tool calling (PTC)](#programmatic-tool-calling-ptc)       |
| Many independent units of work, multiple perspectives, or recursive analysis over large inputs | Interpreter with [programmatic subagents](/oss/python/deepagents/programmatic-subagents) |
| Shell commands, package installs, tests, or full OS filesystem access                          | [Sandboxes](/oss/python/deepagents/sandboxes)                                            |

## Quickstart

Install the QuickJS middleware package, then pass interpreter middleware using the `middleware` argument on `create_deep_agent`.

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install -U "deepagents[quickjs]"
  ```

  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv add "deepagents[quickjs]"
  ```
</CodeGroup>

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from deepagents import create_deep_agent
from langchain_quickjs import CodeInterpreterMiddleware

agent = create_deep_agent(
    model="openai:gpt-5.5",
    middleware=[CodeInterpreterMiddleware()],
)
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

By default, interpreter state also persists across turns in the same thread by snapshotting the working state after each agent run, and restoring it before the next run.

Code runs against [**QuickJS**](https://github.com/quickjs-ng/quickjs), a lightweight JavaScript runtime. By default, interpreter code has no access to the host filesystem, network, shell, package manager, or clock. It can compute, hold state, and write to `console.log`, and nothing more.

Two explicit bridges extend that reach:

* **Tools**, through [programmatic tool calling (PTC)](#programmatic-tool-calling-ptc). Expose an allowlist of tools as async functions under the `tools` namespace. These can be the agent's own tools or standalone tools you define and pass in.
* **Subagents**, through [programmatic subagents](/oss/python/deepagents/programmatic-subagents). Dispatch configured subagents from code and orchestrate them in plain JavaScript.

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

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from deepagents import create_deep_agent
from langchain_quickjs import CodeInterpreterMiddleware

agent = create_deep_agent(
    model="openai:gpt-5.5",
    middleware=[CodeInterpreterMiddleware(ptc=["web_search"])],
)
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
  PTC calls currently execute through the interpreter bridge and do not go through the normal tool calling path. As a result, `interrupt_on` approval workflows are not enforced per PTC-invoked tool call.
</Warning>

## Programmatic subagents

Programmatic subagents let the interpreter dispatch configured [subagents](/oss/python/deepagents/subagents) from code using the built-in `task()` global. A task that spans many independent units, such as reviewing every file in a directory or triaging a batch of tickets, becomes a loop that fans work out and synthesizes the results.

Use programmatic subagents for:

* **Fan-out and synthesize**: Run the same kind of work across many items in parallel, then combine the results.
* **Verification**: Send findings to independent verifier subagents and keep only confirmed results.
* **Recursive workflows**: Keep a working set in interpreter variables, select slices, call subagents, and refine the result.

For configuration, examples, orchestration patterns, and safety notes, see [Programmatic subagents](/oss/python/deepagents/programmatic-subagents).

## Persistence

`CodeInterpreterMiddleware` snapshots interpreter state after each agent run and restores it before the next run by default. A snapshot is a serialized copy of the interpreter's in-memory JavaScript state, including globals, variables, functions, and imported modules that exist when the agent finishes running code.

Across conversation turns, the lifecycle is:

1. A turn starts, and `CodeInterpreterMiddleware` restores the latest interpreter snapshot for the thread.
2. The agent calls `eval`, and the code can read or mutate interpreter variables.
3. The agent run finishes, and the middleware snapshots the updated interpreter state into graph state.
4. The next turn starts from that restored interpreter state instead of an empty runtime.

Within a single agent run, repeated `eval` calls use the live interpreter context object. The middleware does not snapshot and restore between those calls; it snapshots the context when the run completes so it can be restored on a later turn or checkpoint replay.

<Note>
  Between conversation turns, snapshots only retain values that can be reasonably serialized. Use them for data, not for live runtime objects. Functions, classes, and other unserializable values are restored as unaccessible artifacts. If interpreter code accesses one after restore, the eval tool will throw an error like `Value for 'fn' was not restored because it is not serializable (type: function).`
</Note>

Snapshots preserve interpreter memory, not outside-world effects. If interpreter code calls a tool through PTC, restoring a prior interpreter snapshot does not undo side effects from that tool call. It only restores the interpreter variables that recorded or processed the result.

When the graph uses a checkpointer, this pairs with [LangGraph time travel](/oss/python/langgraph/use-time-travel). Restoring a graph checkpoint can restore the interpreter snapshot stored in graph state, so you can return to an earlier agent context and interpreter state while debugging or replaying.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from deepagents import create_deep_agent
from langchain_quickjs import CodeInterpreterMiddleware
from langgraph.checkpoint.memory import MemorySaver

checkpointer = MemorySaver()

agent = create_deep_agent(
    model="openai:gpt-5.5",
    checkpointer=checkpointer,
    middleware=[
        CodeInterpreterMiddleware(
            snapshot_between_turns=True,  # Default
        )
    ],
)
```

You can disable cross-turn snapshots with `snapshot_between_turns=False`.

## Security

Interpreters use QuickJS to run untrusted JavaScript with strict default isolation. Treat that as a scoped interpreter runtime, not a full production sandbox backend.

Every tool you expose through PTC is an outside capability that interpreter code can use. Treat the PTC allowlist as a permission boundary: expose only the tools the agent needs, and avoid bridging broad tools that can access sensitive systems, spend money, mutate data, or call unrestricted networks unless that behavior is intentional.

| Capability                                                  | Available by default | How to expose it                                                                                                    |
| ----------------------------------------------------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------- |
| JavaScript execution                                        | Yes                  | Add interpreter middleware                                                                                          |
| Top-level `await`                                           | Yes                  | Use promises in interpreter code                                                                                    |
| `console.log` capture                                       | Yes                  | Disable with `capture_console=False`                                                                                |
| Agent tools                                                 | No                   | Add a PTC allowlist                                                                                                 |
| Filesystem access                                           | No                   | Add the [built-in filesystem tools](/oss/python/deepagents/harness#virtual-filesystem-access) via the PTC allowlist |
| Network access                                              | No                   | Expose a specific network tool through PTC                                                                          |
| Wall-clock or datetime access                               | No                   | Expose an explicit time tool if needed                                                                              |
| Shell commands, package installs, tests, OS-level execution | No                   | Use a [sandbox backend](/oss/python/deepagents/sandboxes)                                                           |

<Note>
  **How code execution works**

  Interpreter code runs in an embedded QuickJS context, not a separate VM or process. In Python, this runtime is provided by [`quickjs-rs`](https://github.com/langchain-ai/quickjs-rs), which documents the same-process execution boundary in its [Security guide](https://github.com/langchain-ai/quickjs-rs#security).

  Treat interpreters as a capability-scoped execution layer, not a host-memory isolation boundary. For untrusted or semi-trusted code, run agents in isolated worker processes or containers and keep the PTC allowlist narrow.
</Note>

## Configuration

`CodeInterpreterMiddleware` accepts the following options:

| Kwarg                    | Default                          | Purpose                                                                                                                                                                                           |
| ------------------------ | -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `memory_limit`           | `64 * 1024 * 1024` <br />(64 MB) | QuickJS heap memory limit in bytes.                                                                                                                                                               |
| `timeout`                | `5.0`                            | Per-eval timeout in seconds.                                                                                                                                                                      |
| `max_ptc_calls`          | `256`                            | Maximum `tools.*` calls per eval. Use `None` only in trusted environments.                                                                                                                        |
| `tool_name`              | `"eval"`                         | Name of the interpreter tool exposed to the model.                                                                                                                                                |
| `max_result_chars`       | `4000`                           | Maximum characters returned from result and stdout blocks.                                                                                                                                        |
| `capture_console`        | `True`                           | Whether `console.log`, `console.warn`, and `console.error` output is captured.                                                                                                                    |
| `subagents`              | `True`                           | Expose the built-in `task()` global for [programmatic subagents](/oss/python/deepagents/programmatic-subagents). Set to `False` to require subagent dispatch through the normal `task` tool path. |
| `ptc`                    | `None`                           | PTC allowlist: list of tool names or `BaseTool` instances.                                                                                                                                        |
| `snapshot_between_turns` | `True`                           | Whether interpreter state snapshots persist across agent turns.                                                                                                                                   |
| `max_snapshot_bytes`     | `None`                           | Maximum serialized snapshot size. Defaults to `memory_limit`.                                                                                                                                     |

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
Source: https://docs.langchain.com/oss/python/deepagents/mcp

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
Source: https://docs.langchain.com/oss/python/deepagents/memory

Add persistent memory to agents built with Deep Agents so they learn and improve across conversations

Memory lets your agent learn and improve across conversations. Deep Agents makes memory first class with filesystem-backed memory: the agent reads and writes memory as files, and you control where those files are stored using [backends](/oss/python/deepagents/backends).

<Note>
  This page covers **long-term memory**: memory that persists across conversations. For short-term memory (conversation history and scratch files within a single session), see the [context engineering](/oss/python/deepagents/context-engineering) guide. Short-term memory is managed automatically as part of the agent's [state](/oss/python/langgraph/graph-api#state).

  <img alt="Short-term memory is scoped to a single thread via checkpoints; long-term memory persists across threads via the store" />
</Note>

## How memory works

1. **Point the agent at memory files.** Pass file paths to `memory=` when creating the agent. You can also pass [skills](/oss/python/deepagents/skills) via `skills=` for procedural memory (reusable instructions that tell the agent *how* to perform a task). A [backend](/oss/python/deepagents/backends) controls where files are stored and who can access them.
2. **Agent reads memory.** The agent can load memory files into the system prompt at startup, or read them on demand during the conversation. For example, [skills](/oss/python/deepagents/skills) use on-demand loading: the agent reads only skill descriptions at startup, then reads the full skill file only when it matches a task. This keeps context lean until a capability is needed.
3. **Agent updates memory (optional).** When the agent learns new information, it can use its built-in `edit_file` tool to update memory files. Updates can happen during the conversation (the default) or in the background between conversations via [background consolidation](#background-consolidation). Changes are persisted and available in the next conversation. Not all memory is writable: developer-defined [skills](/oss/python/deepagents/skills) and [organization policies](#organization-level-memory) are typically read-only. See [read-only vs writable memory](#read-only-vs-writable-memory) for details.

The two most common patterns are [agent-scoped memory](#agent-scoped-memory) (shared across all users) and [user-scoped memory](#user-scoped-memory) (isolated per user).

## Scoped memory

Agent memory can be scoped so the same memory files are accessible to everyone using the agent or memory files can be individual to each user.

### Agent-scoped memory

Give the agent its own persistent identity that evolves over time. Agent-scoped memory is shared across all users, so the agent builds up its own persona, accumulated knowledge, and learned preferences through every conversation. As it interacts with users, it develops expertise, refines its approach, and remembers what works. It can also learn and update [skills](/oss/python/deepagents/skills) when it has write access.

The key is the backend namespace: setting it to `(assistant_id,)` means every conversation for this agent reads and writes to the same memory file.

<Note>
  Accessing `rt.server_info` requires `deepagents>=0.5.0`. On older versions, read the assistant ID from `get_config()["metadata"]["assistant_id"]` instead.
</Note>

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from deepagents import create_deep_agent
from deepagents.backends import CompositeBackend, StateBackend, StoreBackend

agent = create_deep_agent(
    model="google_genai:gemini-3.5-flash",
    memory=["/memories/AGENTS.md"],
    skills=["/skills/"],
    backend=CompositeBackend(
        default=StateBackend(),
        routes={
            "/memories/": StoreBackend(
                namespace=lambda rt: (
                    rt.server_info.assistant_id,  # [!code highlight]
                ),
            ),
            "/skills/": StoreBackend(
                namespace=lambda rt: (
                    rt.server_info.assistant_id,  # [!code highlight]
                ),
            ),
        },
    ),
)
```

<Accordion title="Full example: seed memory and invoke">
  Populate the store with initial memories, then invoke the agent across two threads to see it remember and update what it learns.

  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langchain_core.utils.uuid import uuid7

  from deepagents import create_deep_agent
  from deepagents.backends import CompositeBackend, StateBackend, StoreBackend
  from deepagents.backends.utils import create_file_data
  from langgraph.store.memory import InMemoryStore

  store = InMemoryStore()  # Use platform store when deploying to LangSmith

  # Seed the memory file
  store.put(
      ("my-agent",),
      "/memories/AGENTS.md",
      create_file_data("""## Response style
  - Keep responses concise
  - Use code examples where possible
  """),
  )

  # Seed a skill
  store.put(
      ("my-agent",),
      "/skills/langgraph-docs/SKILL.md",
      create_file_data("""---
  name: langgraph-docs
  description: Fetch relevant LangGraph documentation to provide accurate guidance.
  ---

  # langgraph-docs

  Use the fetch_url tool to read https://docs.langchain.com/llms.txt, then fetch relevant pages.
  """),
  )

  agent = create_deep_agent(
      model="google_genai:gemini-3.5-flash",
      memory=["/memories/AGENTS.md"],
      skills=["/skills/"],
      backend=lambda rt: CompositeBackend(
          default=StateBackend(rt),
          routes={
              "/memories/": StoreBackend(
                  rt, namespace=lambda rt: ("my-agent",)
              ),
              "/skills/": StoreBackend(
                  rt, namespace=lambda rt: ("my-agent",)
              ),
          },
      ),
      store=store,
  )

  # Thread 1: the agent learns a new preference and saves it to memory
  config1 = {"configurable": {"thread_id": str(uuid7())}}
  agent.invoke(
      {"messages": [{"role": "user", "content": "I prefer detailed explanations. Remember that."}]},
      config=config1,
  )

  # Thread 2: the agent reads memory and applies the preference
  config2 = {"configurable": {"thread_id": str(uuid7())}}
  agent.invoke(
      {"messages": [{"role": "user", "content": "Explain how transformers work."}]},
      config=config2,
  )
  ```
</Accordion>

### User-scoped memory

Give each user their own memory file. The agent remembers preferences, context, and history per user while core agent instructions stay fixed. Users can also have per-user [skills](/oss/python/deepagents/skills) if stored in a user-scoped backend.

The namespace uses `(user_id,)` so each user gets an isolated copy of the memory file. User A's preferences never leak into User B's conversations.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from deepagents import create_deep_agent
from deepagents.backends import CompositeBackend, StateBackend, StoreBackend

agent = create_deep_agent(
    model="google_genai:gemini-3.5-flash",
    memory=["/memories/preferences.md"],
    skills=["/skills/"],
    backend=CompositeBackend(
        default=StateBackend(),
        routes={
            "/memories/": StoreBackend(
                namespace=lambda rt: (rt.server_info.user.identity,),
            ),
            "/skills/": StoreBackend(
                namespace=lambda rt: (rt.server_info.user.identity,),
            ),
        },
    ),
)
```

<Accordion title="Full example: isolated memory across users">
  Seed per-user memories and invoke the agent as two different users. Each user sees only their own preferences.

  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langchain_core.utils.uuid import uuid7

  from deepagents import create_deep_agent
  from deepagents.backends import CompositeBackend, StateBackend, StoreBackend
  from deepagents.backends.utils import create_file_data
  from langgraph.store.memory import InMemoryStore

  store = InMemoryStore()  # Use platform store when deploying to LangSmith

  # Seed preferences for two users
  store.put(
      ("user-alice",),
      "/memories/preferences.md",
      create_file_data("""## Preferences
  - Likes concise bullet points
  - Prefers Python examples
  """),
  )
  store.put(
      ("user-bob",),
      "/memories/preferences.md",
      create_file_data("""## Preferences
  - Likes detailed explanations
  - Prefers TypeScript examples
  """),
  )

  # Seed a skill for Alice
  store.put(
      ("user-alice",),
      "/skills/langgraph-docs/SKILL.md",
      create_file_data("""---
  name: langgraph-docs
  description: Fetch relevant LangGraph documentation to provide accurate guidance.
  ---

  # langgraph-docs

  Use the fetch_url tool to read https://docs.langchain.com/llms.txt, then fetch relevant pages.
  """),
  )

  agent = create_deep_agent(
      model="google_genai:gemini-3.5-flash",
      memory=["/memories/preferences.md"],
      skills=["/skills/"],
      backend=lambda rt: CompositeBackend(
          default=StateBackend(rt),
          routes={
              "/memories/": StoreBackend(
                  rt,
                  namespace=lambda rt: (rt.server_info.user.identity,),
              ),
              "/skills/": StoreBackend(
                  rt,
                  namespace=lambda rt: (rt.server_info.user.identity,),
              ),
          },
      ),
      store=store,
  )

  # When deployed, each authenticated request resolves
  # `rt.server_info.user.identity` to the calling user, so Alice and Bob
  # automatically see only their own preferences.
  agent.invoke(
      {"messages": [{"role": "user", "content": "How do I read a CSV file?"}]},
      config={"configurable": {"thread_id": str(uuid7())}},
  )
  ```
</Accordion>

## Advanced usage

On top of the basic configuration options for memory paths and scope, you can also configure more advanced parameters for memory:

| Dimension             | Question it answers             | Options                                                                                                                                                                                    |
| --------------------- | ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Duration**          | How long does it last?          | [Short-term](/oss/python/deepagents/context-engineering) (single conversation) or [long-term](#scoped-memory) (across conversations)                                                       |
| **Information type**  | What kind of information is it? | [Episodic](#episodic-memory) (past experiences), [procedural](/oss/python/deepagents/skills) (instructions and skills), or [semantic](/oss/python/concepts/memory#semantic-memory) (facts) |
| **Scope**             | Who can see and modify it?      | [User](#user-scoped-memory), [agent](#agent-scoped-memory), or [organization](#organization-level-memory)                                                                                  |
| **Update strategy**   | When are memories written?      | During conversation (default) or [between conversations](#background-consolidation)                                                                                                        |
| **Retrieval**         | How are memories read?          | Loaded into prompt (default) or on demand (e.g., [skills](/oss/python/deepagents/skills))                                                                                                  |
| **Agent permissions** | Can the agent write to memory?  | [Read-write](#read-only-vs-writable-memory) (default) or [read-only](#read-only-vs-writable-memory) (for shared policies)                                                                  |

### Episodic memory

Episodic memory stores records of past experiences: what happened, in what order, and what the outcome was. Unlike semantic memory (facts and preferences stored in files like `AGENTS.md`), episodic memory preserves the full conversational context so the agent can recall *how* a problem was solved, not just *what* was learned from it.

Deep Agents already use [checkpointers](/oss/python/langgraph/checkpointers#checkpoints) which is the mechanism that supports episodic memory: every conversation is persisted as a checkpointed thread.

To make past conversations searchable, wrap thread search in a tool. The `user_id` is pulled from the runtime context rather than passed as a parameter:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langgraph_sdk import get_client
from langchain.tools import tool, ToolRuntime

client = get_client(url="<DEPLOYMENT_URL>")

@tool
async def search_past_conversations(query: str, runtime: ToolRuntime) -> str:
    """Search past conversations for relevant context."""
    user_id = runtime.server_info.user.identity  # [!code highlight]
    threads = await client.threads.search(
        metadata={"user_id": user_id},
        limit=5,
    )
    results = []
    for thread in threads:
        history = await client.threads.get_history(thread_id=thread["thread_id"])
        results.append(history)
    return str(results)
```

You can scope thread search by user or organization by adjusting the metadata filter:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# Search conversations for a specific user
threads = await client.threads.search(
    metadata={"user_id": user_id},
    limit=5,
)

# Search conversations across an organization
threads = await client.threads.search(
    metadata={"org_id": org_id},
    limit=5,
)
```

This is useful for agents that perform complex, multi-step tasks. For example, a coding agent can look back at a past debugging session and skip straight to the likely root cause.

### Organization-level memory

Organization-level memory follows the same pattern as user-scoped memory, but with an organization-wide namespace instead of a per-user one. Use it for policies or knowledge that should apply across all users and agents in an organization.

Organization memory is typically **read-only** to prevent prompt injection via shared state. See [read-only vs writable memory](#read-only-vs-writable-memory) for details.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from deepagents import create_deep_agent
from deepagents.backends import CompositeBackend, StateBackend, StoreBackend

agent = create_deep_agent(
    model="google_genai:gemini-3.5-flash",
    memory=[
        "/memories/preferences.md",
        "/policies/compliance.md",
    ],
    backend=CompositeBackend(
        default=StateBackend(),
        routes={
            "/memories/": StoreBackend(
                namespace=lambda rt: (rt.server_info.user.identity,),
            ),
            "/policies/": StoreBackend(
                namespace=lambda rt: (rt.context.org_id,),
            ),
        },
    ),
)
```

Populate organization memory from your application code:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langgraph_sdk import get_client
from deepagents.backends.utils import create_file_data

client = get_client(url="<DEPLOYMENT_URL>")

await client.store.put_item(
    (org_id,),
    "/compliance.md",
    create_file_data("""## Compliance policies
- Never disclose internal pricing
- Always include disclaimers on financial advice
"""),
)
```

Use [permissions](/oss/python/deepagents/permissions) to enforce that org-level memory is read-only, or [policy hooks](/oss/python/deepagents/backends#add-policy-hooks) for custom validation logic.

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

```python consolidation_agent.py theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from datetime import datetime, timedelta, timezone

from deepagents import create_deep_agent
from langchain.tools import tool, ToolRuntime
from langgraph_sdk import get_client

sdk_client = get_client(url="<DEPLOYMENT_URL>")

@tool
async def search_recent_conversations(query: str, runtime: ToolRuntime) -> str:
    """Search this user's conversations updated in the last 6 hours."""
    user_id = runtime.server_info.user.identity  # [!code highlight]

    since = datetime.now(timezone.utc) - timedelta(hours=6)
    threads = await sdk_client.threads.search(
        metadata={"user_id": user_id},
        updated_after=since.isoformat(),
        limit=20,
    )
    conversations = []
    for thread in threads:
        history = await sdk_client.threads.get_history(
            thread_id=thread["thread_id"]
        )
        conversations.append(history["values"]["messages"])
    return str(conversations)

agent = create_deep_agent(
    model="google_genai:gemini-3.5-flash",
    system_prompt="""Review recent conversations and update the user's memory file.
Merge new facts, remove outdated information, and keep it concise.""",
    tools=[search_recent_conversations],
)
```

```json langgraph.json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "dependencies": ["."],
  "graphs": {
    "agent": "./agent.py:agent",
    "consolidation_agent": "./consolidation_agent.py:agent"
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

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langgraph_sdk import get_client

client = get_client(url="<DEPLOYMENT_URL>")

cron_job = await client.crons.create(
    assistant_id="consolidation_agent",
    schedule="0 */6 * * *",
    input={"messages": [{"role": "user", "content": "Consolidate recent memories."}]},
)
```

<Note>
  All cron schedules are interpreted in **UTC**. See [cron jobs](/langsmith/cron-jobs) for details on managing and deleting cron jobs.
</Note>

<Warning>
  The cron interval must match the lookback window inside the consolidation agent. The example above runs every 6 hours (`0 */6 * * *`) and the agent's `search_recent_conversations` tool looks back `timedelta(hours=6)` — keep these in sync. If the cron runs more often than the lookback, you'll reprocess the same conversations; if it runs less often, you'll drop memories that fall outside the window.
</Warning>

For more on deploying agents with background processes, see [going to production](/oss/python/deepagents/going-to-production).

### Read-only vs writable memory

By default, the agent can both read and write memory files. For shared state like organization policies or compliance rules, you may want to make memory **read-only** so the agent can reference it but not modify it. This prevents prompt injection via shared memory and ensures that only your application code controls what's in the file.

| Permission               | Use case                                                                                                                   | How it works                                                                                                                                                                                                                                                        |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Read-write** (default) | User preferences, agent self-improvement, learned [skills](/oss/python/deepagents/skills)                                  | Agent updates files via `edit_file` tool                                                                                                                                                                                                                            |
| **Read-only**            | Organization policies, compliance rules, shared knowledge bases, developer-defined [skills](/oss/python/deepagents/skills) | Populate via application code or the [Store API](/langsmith/custom-store). Use [permissions](/oss/python/deepagents/permissions) to deny writes to specific paths, or [policy hooks](/oss/python/deepagents/backends#add-policy-hooks) for custom validation logic. |

**Security considerations:** If one user can write to memory that another user reads, a malicious user could inject instructions into shared state. To mitigate this:

* **Default to user scope** `(user_id)` unless you have a specific reason to share
* Use **read-only memory** for shared policies (populate via application code, not the agent)
* Add **human-in-the-loop** validation before the agent writes to shared memory. Use an [interrupt](/oss/python/langgraph/interrupts) to require human approval for writes to sensitive paths.

To enforce read-only memory, use [permissions](/oss/python/deepagents/permissions) to declaratively deny writes to specific paths. For custom validation logic (rate limiting, audit logging, content inspection), use [backend policy hooks](/oss/python/deepagents/backends#add-policy-hooks).

### Concurrent writes

Multiple threads can write to memory in parallel, but concurrent writes to the **same file** can cause last-write-wins conflicts. For user-scoped memory this is rare since users typically have one active conversation at a time. For agent-scoped or organization-scoped memory, consider using [background consolidation](#background-consolidation) to serialize writes, or structure memory as separate files per topic to reduce contention.

In practice, if a write fails due to a conflict, the LLM is usually smart enough to retry or recover gracefully, so a single lost write is not catastrophic.

### Multiple agents in the same deployment

To give each agent its own memory in a shared deployment, add `assistant_id` to the namespace:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
StoreBackend(
    namespace=lambda rt: (
        rt.server_info.assistant_id,  # [!code highlight]
        rt.server_info.user.identity,
    ),
)
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
