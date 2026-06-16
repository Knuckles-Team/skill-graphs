# Sandboxes
Source: https://docs.langchain.com/oss/javascript/deepagents/sandboxes

Execute code in isolated environments with sandbox backends

Agents generate code, interact with filesystems, and run shell commands. Because we can't predict what an agent might do, it's important that its environment is isolated so it can't access credentials, files, or the network. Sandboxes provide this isolation by creating a boundary between the agent's execution environment and your host system.

In Deep Agents, **sandboxes are [backends](/oss/javascript/deepagents/backends)** that define the environment where the agent operates. Unlike other backends (State, Filesystem, Store) which only expose file operations, sandbox backends also give the agent an `execute` tool for running shell commands. When you configure a sandbox backend, the agent gets:

* All standard filesystem tools (`ls`, `read_file`, `write_file`, `edit_file`, `glob`, `grep`)
* The `execute` tool for running arbitrary shell commands in the sandbox
* A secure boundary that protects your host system

```mermaid theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
graph LR
    subgraph Agent
        LLM --> Tools
        Tools --> LLM
    end

    Agent <-- backend protocol --> Sandbox

    subgraph Sandbox
        Filesystem
        Bash
        Dependencies
    end

    classDef process fill:#E5F4FF,stroke:#006DDD,stroke-width:2px,color:#030710
    classDef output fill:#EBD0F0,stroke:#885270,stroke-width:2px,color:#441E33

    class LLM,Tools process
    class Filesystem,Bash,Dependencies output
```

## Why use sandboxes?

Sandboxes are used for security.
They let agents execute arbitrary code, access files, and use the network without compromising your credentials, local files, or host system.
This isolation is essential when agents run autonomously.

Sandboxes are especially useful for:

* Coding agents: Agents that run autonomously can use shell, git, clone repositories (many providers offer native git APIs, e.g., [Daytona's git operations](https://www.daytona.io/docs/en/git-operations/)), and run Docker-in-Docker for build and test pipelines
* Data analysis agents—Load files, install data analysis libraries (pandas, numpy, etc.), run statistical calculations, and create outputs like PowerPoint presentations in a safe, isolated environment

<Tip>
  **Using Deep Agents Code?** Deep Agents Code has built-in sandbox support via the `--sandbox` flag. See [Use remote sandboxes](/oss/javascript/deepagents/code/remote-sandboxes) for Deep Agents Code-specific setup, flags (`--sandbox-id`, `--sandbox-setup`), and examples.
</Tip>

<Note>
  **If you're looking for LangSmith sandboxes:** LangSmith provides first-party managed sandboxes you can use directly from the LangSmith UI or SDK without a third-party account required. For managed sandbox resources, snapshots, service URLs, and the auth proxy, refer to [LangSmith Sandboxes](/langsmith/sandboxes).
</Note>

## Basic usage

These examples assume you have already created a sandbox/devbox using the provider's SDK and have credentials set up. For signup, authentication, and provider-specific lifecycle details, see [Available providers](#available-providers).

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { createDeepAgent } from "deepagents";
import { ChatAnthropic } from "@langchain/anthropic";
import { DenoSandbox } from "@langchain/deno";

// Create and initialize the sandbox
const sandbox = await DenoSandbox.create({
  memoryMb: 1024,
  lifetime: "10m",
});

try {
  const agent = createDeepAgent({
    model: new ChatAnthropic({ model: "claude-opus-4-8" }),
    systemPrompt: "You are a JavaScript coding assistant with sandbox access.",
    backend: sandbox,
  });

  const result = await agent.invoke({
    messages: [
      {
        role: "user",
        content:
          "Create a simple HTTP server using Deno.serve and test it with curl",
      },
    ],
  });
} finally {
  await sandbox.close();
}
```

<Tip>
  [LangSmith](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=oss-deepagents-sandboxes) traces show which shell commands ran inside a sandbox and how the agent used filesystem tools. Follow the [observability quickstart](/langsmith/observability-quickstart) to get set up. For managed sandbox hosting, see [LangSmith Sandboxes](/langsmith/sandboxes).

  We recommend you also set up [LangSmith Engine](/langsmith/engine), which monitors your traces, detects issues, and proposes fixes.
</Tip>

## Available providers

<Note>
  Skills require `deepagents>=1.7.0`.
</Note>

<div>
  <a href="/oss/javascript/integrations/providers/modal">
    <img alt="" />

    <img alt="" />

    <span>Modal</span>
  </a>

  <a href="/oss/javascript/integrations/providers/daytona">
    <img alt="" />

    <img alt="" />

    <span>Daytona</span>
  </a>

  <a href="/oss/javascript/integrations/providers/deno">
    <img alt="" />

    <img alt="" />

    <span>Deno</span>
  </a>

  <a href="/oss/javascript/integrations/providers/node-vfs">
    <img alt="" />

    <img alt="" />

    <span>Node VFS</span>
  </a>

  <a href="/langsmith/sandboxes">
    <img alt="" />

    <span>LangSmith</span>
  </a>
</div>

Don't see your provider? You can implement your own sandbox backend. See [Contributing a sandbox integration](/oss/javascript/contributing/integrations-langchain).

## Lifecycle and scoping

Most applications choose either one sandbox per [thread](/langsmith/use-threads) (thread-scoped) or one shared sandbox for every thread on the same [assistant](/langsmith/assistants) (assistant-scoped).

Sandboxes consume resources and cost money until they are shut down. Make sure you shut sandboxes down once they are no longer in use.

For the full lifecycle table, async [graph factory](/langsmith/graph-rebuild) notes, TTL behavior, LangGraph Deployment wiring, and client-side examples, see [Sandbox lifecycle](/oss/javascript/deepagents/going-to-production#lifecycle) in Going to production.

### Thread-scoped (default)

Each conversation gets its own sandbox. The first run creates it; follow-up turns on the same thread reuse it. When the thread ends or the sandbox TTL expires, the environment goes away. Store the mapping with provider labels or metadata as in the following example so each run resolves to the same sandbox.

<Tip>
  When users can return after idle time, configure a TTL on the sandbox so the provider deletes or archives idle environments automatically.
</Tip>

<Tabs>
  <Tab title="Python">
    ```python agent.py theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from daytona import CreateSandboxFromSnapshotParams, Daytona
    from deepagents import create_deep_agent
    from langchain_core.runnables import RunnableConfig
    from langchain_daytona import DaytonaSandbox

    client = Daytona()

    async def agent(config: RunnableConfig):
        thread_id = config["configurable"]["thread_id"]  # [!code highlight]
        try:
            sandbox = await client.find_one(labels={"thread_id": thread_id})
        except Exception:
            sandbox = await client.create(
                CreateSandboxFromSnapshotParams(
                    labels={"thread_id": thread_id},
                    auto_delete_interval=3600,  # TTL: clean up when idle
                )
            )
        return create_deep_agent(
            model="google_genai:gemini-3.5-flash",
            backend=DaytonaSandbox(sandbox=sandbox)
        )
    ```
  </Tab>

  <Tab title="TypeScript">
    ```typescript src/agent.ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { Daytona } from "@daytonaio/sdk";
    import { DaytonaSandbox } from "@langchain/daytona";
    import { createDeepAgent } from "deepagents";
    import type { LangGraphRunnableConfig } from "@langchain/langgraph";

    const client = new Daytona();

    export async function agent(config: LangGraphRunnableConfig) {
      const threadId = config.configurable?.thread_id as string;  // [!code highlight]
      let sandbox;
      try {
        sandbox = await client.findOne({ labels: { thread_id: threadId } });
      } catch {
        sandbox = await client.create({
          labels: { thread_id: threadId },
          autoDeleteInterval: 3600, // TTL: clean up when idle
        });
      }
      return createDeepAgent({
        model: "google_genai:gemini-3.5-flash",
        backend: await DaytonaSandbox.fromId(sandbox.id),
      });
    }
    ```
  </Tab>
</Tabs>

### Assistant-scoped

Every thread on the same assistant reuses one sandbox. Files, installed packages, and cloned repositories persist across conversations.

<Warning>
  Assistant-scoped sandboxes accumulate in-sandbox state over time. Configure a TTL with your sandbox provider, use snapshots to reset periodically, or implement cleanup logic so disk and memory do not grow without bound.
</Warning>

<Tabs>
  <Tab title="Python">
    ```python agent.py theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from daytona import CreateSandboxFromSnapshotParams, Daytona
    from deepagents import create_deep_agent
    from langchain_core.runnables import RunnableConfig
    from langchain_daytona import DaytonaSandbox

    client = Daytona()

    async def agent(config: RunnableConfig):
        assistant_id = config["configurable"]["assistant_id"]  # [!code highlight]
        try:
            sandbox = await client.find_one(labels={"assistant_id": assistant_id})
        except Exception:
            sandbox = await client.create(
                CreateSandboxFromSnapshotParams(labels={"assistant_id": assistant_id})
            )
        return create_deep_agent(
            model="google_genai:gemini-3.5-flash",
            backend=DaytonaSandbox(sandbox=sandbox)
        )
    ```
  </Tab>

  <Tab title="TypeScript">
    ```typescript src/agent.ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { Daytona } from "@daytonaio/sdk";
    import { DaytonaSandbox } from "@langchain/daytona";
    import { createDeepAgent } from "deepagents";
    import type { LangGraphRunnableConfig } from "@langchain/langgraph";

    const client = new Daytona();

    export async function agent(config: LangGraphRunnableConfig) {
      const assistantId = config.configurable?.assistant_id as string;  // [!code highlight]
      let sandbox;
      try {
        sandbox = await client.findOne({ labels: { assistant_id: assistantId } });
      } catch {
        sandbox = await client.create({ labels: { assistant_id: assistantId } });
      }
      return createDeepAgent({
        model: "google_genai:gemini-3.5-flash",
        backend: await DaytonaSandbox.fromId(sandbox.id),
      });
    }
    ```
  </Tab>
</Tabs>

For manual create, execute, and teardown outside a graph factory, see [Basic usage](#basic-usage) and [sandbox integrations](/oss/javascript/integrations/sandboxes) for provider-specific APIs.

## Integration patterns

There are two architecture patterns for integrating agents with sandboxes, based on where the agent runs.

### Agent in sandbox pattern

The agent runs inside the sandbox and you communicate with it over the network. You build a Docker or VM image with your agent framework pre-installed, run it inside the sandbox, and connect from outside to send messages.

Benefits:

* ✅ Mirrors local development closely.
* ✅ Tight coupling between agent and environment.

Trade-offs:

* 🔴 API keys must live inside the sandbox (security risk).
* 🔴 Updates require rebuilding images.
* 🔴 Requires infrastructure for communication (WebSocket or HTTP layer).

To run an agent in a sandbox, build an image and install deepagents on it.

```dockerfile theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
FROM python:3.11
RUN pip install deepagents-code
```

Then run the agent inside the sandbox.
To use the agent inside the sandbox you have to add additional infrastructure to handle communication between your application and the agent inside the sandbox.

### Sandbox as tool pattern

The agent runs on your machine or server. When it needs to execute code, it calls sandbox tools (such as `execute`, `read_file`, or `write_file`) which invoke the provider's APIs to run operations in a remote sandbox.

Benefits:

* ✅ Update agent code instantly without rebuilding images.
* ✅ Cleaner separation between agent state and execution.
  * API keys stay outside the sandbox.
  * Sandbox failures don't lose agent state.
  * Option to run tasks in multiple sandboxes in parallel.
* ✅ Pay only for execution time.

Trade-offs:

* 🔴 Network latency on each execution call.

```typescript Example theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import "dotenv/config";
import { DaytonaSandbox } from "@langchain/daytona";
import { createDeepAgent } from "deepagents";

// Can also do this with E2B, Runloop, Modal
const sandbox = await DaytonaSandbox.create();

const agent = createDeepAgent({
  backend: sandbox,
  systemPrompt:
    "You are a coding assistant with sandbox access. You can create and run code in the sandbox.",
});

try {
  const result = await agent.invoke({
    messages: [
      {
        role: "user",
        content: "Create a hello world Python script and run it",
      },
    ],
  });
  const lastMessage = result.messages[result.messages.length - 1];
  console.log(
    typeof lastMessage.content === "string"
      ? lastMessage.content
      : String(lastMessage.content),
  );
} catch (err) {
  // Optional: delete the sandbox proactively on an exception
  await sandbox.close();
  throw err;
}
```

The examples in this doc use the sandbox as a tool pattern.
Choose the agent in sandbox pattern when your provider's SDK handles the communication layer and you want production to mirror local development.
Choose the sandbox as tool pattern when you need to iterate quickly on agent logic, keep API keys outside the sandbox, or prefer cleaner separation of concerns.

## How sandboxes work

### Isolation boundaries

All sandbox providers protect your host system from the agent's filesystem and shell operations. The agent cannot read your local files, access environment variables on your machine, or interfere with other processes. However, sandboxes alone do **not** protect against:

* **Context injection**: An attacker who controls part of the agent's input can instruct it to run arbitrary commands inside the sandbox. The sandbox is isolated, but the agent has full control within it.
* **Network exfiltration**: Unless network access is blocked, a context-injected agent can send data out of the sandbox over HTTP or DNS. Some providers support blocking network access (e.g., `blockNetwork: true` on Modal).

See [security considerations](#security-considerations) for how to handle secrets and mitigate these risks.

### The `execute` method

Sandbox backends have a simple architecture: the only method a provider must implement is `execute()`, which runs a shell command and returns its output. Every other filesystem operation (`read`, `write`, `edit`, `ls`, `glob`, `grep`) is built on top of `execute()` by the [`BaseSandbox`](https://reference.langchain.com/javascript/deepagents/backends/BaseSandbox) base class, which constructs scripts and runs them inside the sandbox via `execute()`.

```mermaid theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
graph TB
    subgraph "Agent tools"
        Tools["ls, read_file, ..."]
        execute
    end

    BaseSandbox["BaseSandbox<br/>(uses execute)"] --> Tools
    execute_method["execute()"] --> BaseSandbox
    execute_method --> execute
    Provider["Provider SDK"] --> execute_method

    classDef process fill:#E5F4FF,stroke:#006DDD,stroke-width:2px,color:#030710
    classDef trigger fill:#F6FFDB,stroke:#6E8900,stroke-width:2px,color:#2E3900

    class Tools,execute process
    class BaseSandbox,execute_method process
    class Provider trigger
```

This design means:

* **Adding a new provider is straightforward.** Implement `execute()`—the base class handles everything else.
* **The `execute` tool is conditionally available.** On every model call, the harness checks whether the backend implements [`SandboxBackendProtocol`](https://reference.langchain.com/javascript/deepagents/backends/SandboxBackendProtocol). If not, the tool is filtered out and the agent never sees it.

When the agent calls the `execute` tool, it provides a `command` string and gets back the combined stdout/stderr, exit code, and a truncation notice if the output was too large.

You can also call the backend `execute()` method directly in your application code.

For example:

```
4
[Command succeeded with exit code 0]
```

```
bash: foobar: command not found
[Command failed with exit code 127]
```

If a command produces very large output, the result is automatically saved to a file and the agent is instructed to use `read_file` to access it incrementally. This prevents context window overflow.

### Two planes of file access

There are two distinct ways files move in and out of a sandbox, and it's important to understand when to use each:

**Agent filesystem tools**: `read_file`, `write_file`, `edit_file`, `ls`, `glob`, `grep`, and `execute` are the tools the LLM calls during its execution. These go through `execute()` inside the sandbox. The agent uses them to read code, write files, and run commands as part of its task.

**File transfer APIs**: the `uploadFiles()` and `downloadFiles()` methods that your application code calls. These use the provider's native file transfer APIs (not shell commands) and are designed for moving files between your host environment and the sandbox. Use these to:

* **Seed the sandbox** with source code, configuration, or data before the agent runs
* **Retrieve artifacts** (generated code, build outputs, reports) after the agent finishes
* **Pre-populate dependencies** that the agent will need

```mermaid theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
graph LR
    subgraph "Your application"
        App[Application code]
    end

    subgraph "Agent"
        LLM --> Tools["read_file, write_file, ..."]
        Tools --> LLM
    end

    subgraph "Sandbox"
        FS[Filesystem]
    end

    App -- "Provider API" --> FS
    Tools -- "execute()" --> FS

    classDef trigger fill:#F6FFDB,stroke:#6E8900,stroke-width:2px,color:#2E3900
    classDef process fill:#E5F4FF,stroke:#006DDD,stroke-width:2px,color:#030710
    classDef output fill:#EBD0F0,stroke:#885270,stroke-width:2px,color:#441E33

    class App trigger
    class LLM,Tools process
    class FS output
```

## Working with files

### Seeding the sandbox

Use `uploadFiles()` to populate the sandbox before the agent runs. File contents are provided as `Uint8Array`:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const encoder = new TextEncoder();
const responses = await sandbox.uploadFiles([
  ["src/index.js", encoder.encode("console.log('Hello')")],
  ["package.json", encoder.encode('{"name": "my-app"}')],
]);

// Each response indicates success or failure
for (const res of responses) {
  if (res.error) {
    console.error(`Failed to upload ${res.path}: ${res.error}`);
  }
}
```

### Retrieving artifacts

Use `downloadFiles()` to retrieve files from the sandbox after the agent finishes:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const results = await sandbox.downloadFiles(["src/index.js", "output.txt"]);

const decoder = new TextDecoder();
for (const result of results) {
  if (result.content) {
    console.log(`${result.path}: ${decoder.decode(result.content)}`);
  } else {
    console.error(`Failed to download ${result.path}: ${result.error}`);
  }
}
```

<Note>
  Inside the sandbox, the agent uses its own filesystem tools (`read_file`, `write_file`): not `uploadFiles` or `downloadFiles`. Those methods are for your application code to move files across the boundary between your host and the sandbox.
</Note>

## Security considerations

Sandboxes isolate code execution from your host system, but they don't protect against **context injection**. An attacker who controls part of the agent's input can instruct it to read files, run commands, or exfiltrate data from within the sandbox. This makes credentials inside the sandbox especially dangerous.

<Warning>
  **Never put secrets inside a sandbox.** API keys, tokens, database credentials, and other secrets injected into a sandbox (via environment variables, mounted files, or the `secrets` option) can be read and exfiltrated by a context-injected agent. This applies even to short-lived or scoped credentials—if an agent can access them, so can an attacker.
</Warning>

### Handling secrets safely

If your agent needs to call authenticated APIs or access protected resources, you have two options:

1. **Keep secrets in tools outside the sandbox.** Define tools that run in your host environment (not inside the sandbox) and handle authentication there. The agent calls these tools by name, but never sees the credentials. This is the recommended approach.

2. **Use a network proxy that injects credentials.** Some sandbox providers support proxies that intercept outgoing HTTP requests from the sandbox and attach credentials (e.g., `Authorization` headers) before forwarding them. The agent never sees the secret—it just makes plain requests to a URL. This approach is not yet widely available across providers.

<Warning>
  If you must inject secrets into a sandbox (not recommended), take these precautions:

  * Enable [human-in-the-loop](/oss/javascript/deepagents/human-in-the-loop) approval for **all** tool calls, not just sensitive ones
  * Block or restrict network access from the sandbox to limit exfiltration paths
  * Use the narrowest possible credential scope and shortest possible lifetime
  * Monitor sandbox network traffic for unexpected outbound requests

  Even with these safeguards, this remains an unsafe workaround. A sufficiently creative enough context injection attack can bypass output filtering and HITL review.
</Warning>

### General best practices

* Review sandbox outputs before acting on them in your application
* Block sandbox network access when not needed
* Use [middleware](/oss/javascript/langchain/middleware) to filter or redact sensitive patterns in tool outputs
* Treat everything produced inside the sandbox as untrusted input

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/deepagents/sandboxes.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Skills
Source: https://docs.langchain.com/oss/javascript/deepagents/skills

Learn how to extend your deep agent's capabilities with skills

Skills package domain expertise, such as workflows, best practices, scripts, reference docs, and templates, into reusable directories. The agent gets a summary of the contents on startup and discovers and reads the contained files only when relevant.

Skills help you avoid context bloat by loading only summaries at startup and reading full instructions when a task requires them. You can share skills across agents and projects, and compose multiple skills in a single agent so each one covers a distinct capability.

<Note>
  Skills require `deepagents>=1.7.0`.
</Note>

<Tip>
  For ready-to-use skills that improve your agent's performance on LangChain ecosystem tasks, see the [LangChain Skills](https://github.com/langchain-ai/langchain-skills) repository.
</Tip>

## Usage

<Steps>
  <Step title="Create a top-level skills directory">
    Create a directory to hold all skills for your project, such as `skills/` under your backend root.
  </Step>

  <Step title="Create a subdirectory inside your skills directory for your skill">
    Each skill is a directory containing a `SKILL.md` file: a markdown file with YAML [frontmatter](#frontmatter-fields) (`name` and `description`) followed by instructions the agent follows when the skill is activated. A skill directory can also optionally include supporting files such as scripts, reference docs, and templates.

    <Tree>
      <Tree.Folder name="skills">
        <Tree.Folder name="langgraph-docs">
          <Tree.File name="SKILL.md" />

          <Tree.Folder name="scripts">
            <Tree.File name="fetch_docs.py" />
          </Tree.Folder>

          <Tree.Folder name="references">
            <Tree.File name="api-patterns.md" />

            <Tree.File name="style-guide.md" />
          </Tree.Folder>

          <Tree.Folder name="assets">
            <Tree.File name="report-template.md" />

            <Tree.File name="schema.json" />
          </Tree.Folder>
        </Tree.Folder>
      </Tree.Folder>
    </Tree>

    Deep agent skills follow the [Agent Skills specification](https://agentskills.io/specification).
  </Step>

  <Step title="Add a `SKILL.md` file with YAML frontmatter and instructions.">
    The `SKILL.md` starts with YAML [frontmatter](#frontmatter-fields) followed by markdown instructions:

    ```md theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    ---
    name: langgraph-docs
    description: Use this skill for requests related to LangGraph in order to fetch relevant documentation to provide accurate, up-to-date guidance.
    ---

    # langgraph-docs

    ## Overview

    This skill explains how to access LangGraph documentation to help answer questions and guide implementation.

    ## Instructions

    ### 1. Fetch the documentation index

    Use the fetch_url tool to read the following URL:
    https://docs.langchain.com/llms.txt

    This provides a structured list of all available documentation with descriptions.

    ### 2. Select relevant documentation

    Based on the question, identify 2-4 most relevant documentation URLs from the index. Prioritize:

    - Specific how-to guides for implementation questions
    - Core concept pages for understanding questions
    - Tutorials for end-to-end examples
    - Reference docs for API details

    ### 3. Fetch and synthesize

    Use the fetch_url tool to read the selected documentation URLs, then answer the user's question. Give a direct answer first, include the minimum necessary context, and link to the source pages rather than quoting long passages.
    ```

    <Note>
      Reference any [supporting resources](#add-supporting-resources) in your `SKILL.md` with a description of what each file contains and when to use it. The agent discovers these files through the references in the skill instructions.
    </Note>
  </Step>

  <Step title="Pass the skills path when creating your agent">
    Pass the path to your top-level skills directory in the `skills` argument when creating your agent:

    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { createDeepAgent, FilesystemBackend } from "deepagents";

    const backend = new FilesystemBackend({ rootDir: process.cwd() });

    const agent = await createDeepAgent({
      model: "anthropic:claude-sonnet-4-6",
      backend,
      skills: ["/skills/"],
    });
    ```

    This example uses `FilesystemBackend` to load skills from disk. For other storage options, including loading skills from remote sources, see [Backends and remote skill loading](#backends-and-remote-skill-loading).

    <ParamField type="list[str]">
      List of skill source paths.

      Paths must be specified using forward slashes and are relative to the backend's root.

      * If omitted, no skills are loaded.
      * When using `StateBackend` (default), provide skill files with `invoke(files={...})`. Use `create_file_data()` from `deepagents.backends.utils` to format file contents; raw strings are not supported.
      * With `FilesystemBackend`, skills are loaded from disk relative to the backend's `root_dir`.

      Later sources override earlier ones for skills with the same name (last one wins).

      <Note>
        When multiple skill sources contain a skill with the same name, the skill from the source listed later in the `skills` array takes precedence (last one wins). This lets you layer skills from different origins, such as base skills overridden by project-specific versions.
      </Note>
    </ParamField>
  </Step>

  <Step title="Invoke the agent">
    Send a task to the agent with `invoke()`. At startup, the agent loads each skill's [`name`](#frontmatter-fields) and [`description`](#frontmatter-fields) from [frontmatter](#frontmatter-fields) into the system prompt. When your task matches a skill's description, the agent reads that skill's `SKILL.md` and follows its instructions.

    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    const result = await agent.invoke(
      { messages: [{ role: "user", content: "What is LangGraph?" }] },
      { configurable: { thread_id: "1" } },
    );
    ```
  </Step>
</Steps>

## How skills work

As agents take on more complex tasks, the context they need grows with them. Loading all instructions into the system prompt wastes tokens on information irrelevant to the current task, and providing the same guidance manually across sessions does not scale.

<Info>
  Skills use **progressive disclosure**: the agent loads skill information in layers instead of all at once. At startup, it sees only each skill's name and description. When a skill is invoked, it reads the full `SKILL.md` instructions. Supporting files load afterward, only when the instructions call for them.
</Info>

Skills load in three levels. Each level adds more detail only when the task needs it:

| Level               | What loads                                                                                                                | When                                                             |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| **1. Metadata**     | [`name`](#frontmatter-fields) and [`description`](#frontmatter-fields) from `SKILL.md` [frontmatter](#frontmatter-fields) | Agent startup, for every configured skill                        |
| **2. Instructions** | Full `SKILL.md` body                                                                                                      | When the skill is invoked                                        |
| **3. Resources**    | [Supporting files](#add-supporting-resources) under `scripts/`, `references/`, and `assets/`                              | As needed after invocation, when the instructions reference them |

The following diagram shows what appears in agent context at a given moment. At startup, level 1 metadata for every skill is in the system prompt. When a skill is invoked, level 2 instructions join the context. Level 3 files stay on the backend until the agent reads them after invocation.

<div>
  <img alt="How skill components map into agent context at startup and activation" />
</div>

As the agent works through a task, it loads skill information in layers:

<div>
  <img alt="How skills load in layers from metadata to instructions to resources" />
</div>

In Deep Agents, [`SkillsMiddleware`](https://reference.langchain.com/javascript/deepagents/middleware/createSkillsMiddleware) (part of the [default middleware stack](/oss/javascript/deepagents/customization#default-stack-main-agent) when you pass `skills`) handles the first two levels, with the third level being handled by the LLM:

1. **Discovery** (level 1): At agent start, the middleware scans the configured skill paths, parses each `SKILL.md` [frontmatter](#frontmatter-fields), and injects the [`name`](#frontmatter-fields) and [`description`](#frontmatter-fields) fields into the system prompt.
2. **Read** (level 2): When the agent invokes a skill, it reads the full `SKILL.md` content via `read_file`.
3. **Execute** (level 3): After invocation, the agent follows the skill's instructions and reads supporting files (scripts, references, assets) only as the instructions require.

## When to use skills

If you find yourself giving similar instructions to an agent, especially if they are detailed and contain multiple steps, consider codifying the instructions for the agent. That way, in future when you want to accomplish a similar task, the agent will already know what to do.

<Tip>
  You can also ask your agent to write a skill for a task you worked on with the agent.
</Tip>

Skills are especially helpful for codifying:

* **Step-by-step workflows**: Workflows that span multiple steps, similar to recipes.
* **Domain-specific knowledge**: Instruct the agent on how to use tools for the workflow. For example, include information on where to pull information from, including other reference information or scripts that the skill may have access to.
* **Instructions with executable code**: Bundle procedures with scripts or modules the agent can run, so it follows tested logic instead of regenerating it from instructions each time. See [Execute code with skills](#execute-code-with-skills).
* **Guidelines**: Provide the agent with supporting instructions about guardrails to adhere to. For example, following a specific format or style guide, or specifying to always run tests as part of the workflow.

## Write effective skills

The [Agent Skills specification](https://agentskills.io/specification) includes guidance on structuring skills for reliable discovery and activation. The following recommendations build on that foundation with practical patterns for Deep Agents.

**Keep [frontmatter](#frontmatter-fields) concise** and the `SKILL.md` body under 5,000 tokens. Every skill's frontmatter is added to the system prompt at [discovery](#how-skills-work), while the full body is only read when activated. Keeping both layers small means you can load many skills without crowding the context window.

**Write specific descriptions.** During [discovery](#how-skills-work), the [`description`](#frontmatter-fields) field is the only information the agent sees for each skill. A good description tells the agent both what the skill does and when to activate it, with specific keywords the agent can match against:

```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# Good: specific about what and when
description: >-
  Extract text and tables from PDF files, fill PDF forms, and merge
  multiple PDFs. Use when working with PDF documents or when the user
  mentions PDFs, forms, or document extraction.
