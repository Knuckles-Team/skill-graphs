# Harness capabilities
Source: https://docs.langchain.com/oss/javascript/deepagents/harness

A Deep Agents harness provides four categories of built-in capabilities that make building long-running, reliable agents easier:

<CardGroup>
  <Card title="Execution environment" icon="bolt" href="#execution-environment">
    Tools, virtual filesystem, optional sandbox, and REPL (interpreter)
  </Card>

  <Card title="Context management" icon="database" href="#context-management">
    Skills, memory, summarization, context offloading, and prompt caching
  </Card>

  <Card title="Delegation" icon="sitemap" href="#delegation">
    Subagent spawning and task planning
  </Card>

  <Card title="Steering" icon="user" href="#steering">
    Human-in-the-loop approval and interrupts
  </Card>
</CardGroup>

Alongside these four components, [harness profiles](#harness-profiles) let you package per-model configuration into reusable bundles.

<img alt="The Deep Agents open harness: planning, virtual filesystem, permissions, subagents, context management, code execution, human-in-the-loop, skills, and memory" />

## Execution environment

The execution environment is where an agent acts. It has four layers:

* **[Tools](#tools)**: custom functions, APIs, and databases the agent can call
* **[Virtual filesystem](#virtual-filesystem-access)**: file tools backed by pluggable backends
* **[Filesystem permissions](#filesystem-permissions)**: declarative access control over which paths agents can read or write
* **[Code execution](#code-execution)**: sandboxed shell execution and an in-process JavaScript interpreter

### Tools

Pass any Python callable, LangChain tool, or tool dict to `create_deep_agent` via the `tools=` parameter. These are the domain-specific actions your agent can take—web search, database queries, API calls, or any function you define.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from deepagents import create_deep_agent

agent = create_deep_agent(
    model="anthropic:claude-sonnet-4-6",
    tools=[search, fetch_page, run_query],
)
```

For more information on defining custom tools, using MCP servers, and the full list of built-in harness tools, see [Tools](/oss/javascript/deepagents/tools).

### Virtual filesystem access

The harness provides a configurable virtual filesystem which can be backed by different pluggable backends.
The backends support the following file system operations:

| Tool         | Description                                                                                                                                                                                                              |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `ls`         | List files in a directory with metadata (size, modified time)                                                                                                                                                            |
| `read_file`  | Read file contents with line numbers, supports offset/limit for large files. Also supports returning multimodal content blocks for non-text files (images, video, audio, and documents). See supported extensions below. |
| `write_file` | Create new files                                                                                                                                                                                                         |
| `edit_file`  | Perform exact string replacements in files (with global replace mode)                                                                                                                                                    |
| `glob`       | Find files matching patterns (e.g., `**/*.py`)                                                                                                                                                                           |
| `grep`       | Search file contents with multiple output modes (files only, content with context, or counts)                                                                                                                            |
| `execute`    | Run shell commands in the environment (available with [sandbox backends](/oss/javascript/deepagents/sandboxes) only)                                                                                                     |

<Accordion title="Supported multimodal file extensions">
  | Type                                                   | Extensions                                                                |
  | ------------------------------------------------------ | ------------------------------------------------------------------------- |
  | [Image](/oss/javascript/langchain/messages#multimodal) | `.png`, `.jpg`, `.jpeg`, `.gif`, `.webp`, `.heic`, `.heif`                |
  | [Video](/oss/javascript/langchain/messages#multimodal) | `.mp4`, `.mpeg`, `.mov`, `.avi`, `.flv`, `.mpg`, `.webm`, `.wmv`, `.3gpp` |
  | [Audio](/oss/javascript/langchain/messages#multimodal) | `.wav`, `.mp3`, `.aiff`, `.aac`, `.ogg`, `.flac`                          |
  | [File](/oss/javascript/langchain/messages#multimodal)  | `.pdf`, `.ppt`, `.pptx`                                                   |
</Accordion>

<Accordion title="Running without the default filesystem tools" icon="ban">
  To hide the filesystem tools listed above from the model, register a [harness profile](#harness-profiles) with `excluded_tools`:

  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import HarnessProfile, register_harness_profile

  register_harness_profile(
      "anthropic:claude-sonnet-4-6",
      HarnessProfile(
          excluded_tools=frozenset(
              {"ls", "read_file", "write_file", "edit_file", "glob", "grep"}
          ),
      ),
  )
  ```

  Removing [`FilesystemMiddleware`](https://reference.langchain.com/javascript/deepagents/middleware/createFilesystemMiddleware) itself via `excluded_middleware` is intentionally rejected—it is required scaffolding in the [default middleware stack](/oss/javascript/deepagents/customization#default-stack-main-agent). Use `excluded_tools` to hide only the model-visible tool surface and leave the middleware in place. To remove the `task` tool, see [Running without subagents](/oss/javascript/deepagents/subagents#running-without-subagents).
</Accordion>

The virtual filesystem is used by several other harness capabilities such as skills, memory, code execution, and context management.
You can also use the file system when building custom tools and middleware for Deep Agents.

For more information, see [backends](/oss/javascript/deepagents/backends).

### Filesystem permissions

The harness supports declarative permission rules that control which files and directories the agent can read or write. Permissions apply to the built-in filesystem tools listed above and are evaluated in declaration order with first-match-wins semantics.

**How it works:**

* Pass a list of rules to `permissions=` when creating the agent
* Each rule specifies `operations` (`"read"`, `"write"`), `paths` (glob patterns), and `mode` (`"allow"` or `"deny"`)
* The first matching rule wins. If no rule matches, the operation is allowed.

**Why it's useful:**

* Restrict agents to specific directories (e.g., `/workspace/`)
* Protect sensitive files (e.g., `.env`, credentials)
* Give subagents narrower access than the parent agent

Permissions do not apply to [sandbox backends](/oss/javascript/deepagents/sandboxes), which support arbitrary command execution via the `execute` tool. For custom validation logic, use [backend policy hooks](/oss/javascript/deepagents/backends#add-policy-hooks).

For the full rule structure, examples, and subagent inheritance, see [Permissions](/oss/javascript/deepagents/permissions).

### Code execution

Deep Agents supports code execution in two ways:

* [Sandbox backends](/oss/javascript/deepagents/sandboxes) expose an `execute` tool for shell commands in an isolated environment.
* [Interpreters](/oss/javascript/deepagents/interpreters) add an `eval` tool that runs JavaScript in a scoped QuickJS runtime.

Use sandbox backends when the agent needs to install dependencies, run tests, call CLIs, or work with an operating-system filesystem. Sandbox backends implement the `SandboxBackendProtocolV2`; when detected, the harness adds the `execute` tool to the agent's available tools.

Use interpreters when the agent needs a lightweight programmable layer for loops, batching, deterministic data transformations, or programmatic tool calling. Interpreters do not provide shell access, package installs, or filesystem and network access.

For sandbox setup, providers, and file transfer APIs, see [Sandboxes](/oss/javascript/deepagents/sandboxes). For the QuickJS runtime and programmatic tool calling, see [Interpreters](/oss/javascript/deepagents/interpreters).

## Context management

The context management component controls what the agent knows, how long it can operate within token limits, and what it retains across sessions. It has four layers:

* **[Skills](#skills)**—on-demand domain knowledge loaded progressively from skill files
* **[Memory](#memory)**—persistent instructions and preferences loaded at startup from `AGENTS.md` files
* **[Summarization and context offloading](#summarization-and-context-offloading)**—automatic compression of conversation history and large tool results
* **[Prompt caching](#prompt-caching)**—static prompt sections are cache-eligible to speed up inference and reduce cost on supported models

### Skills

The harness supports skills that provide specialized workflows and domain knowledge to your deep agent.

**How it works:**

* Skills follow the [Agent Skills standard](https://agentskills.io/)
* Each skill is a directory containing a `SKILL.md` file with instructions and metadata
* Skills can include additional scripts, reference docs, templates, and other resources
* Skills use progressive disclosure—they are only loaded when the agent determines they're useful for the current task
* Agent reads frontmatter from each `SKILL.md` file at startup, then reviews full skill content when needed

**Why it's useful:**

* Reduces token usage by only loading relevant skills when needed
* Bundles capabilities together into larger actions with additional context
* Provides specialized expertise without cluttering the system prompt
* Enables modular, reusable agent capabilities

For more information, see [Skills](/oss/javascript/deepagents/skills).

### Memory

The harness supports persistent memory files that provide extra context to your deep agent across conversations.
These files often contain general coding style, preferences, conventions, and guidelines that help the agent understand how to work with your codebase and follow your preferences.

**How it works:**

* Uses [`AGENTS.md` files](https://agents.md/) to provide persistent context
* Memory files are always loaded (unlike skills, which use progressive disclosure)
* Pass one or more file paths to the `memory` parameter when creating your agent
* Files are stored in the agent's backend (StateBackend, StoreBackend, or FilesystemBackend)
* The agent can update memory based on your interactions, feedback, and identified patterns

**Why it's useful:**

* Provides persistent context that does not need to be re-specified each conversation
* Useful for storing user preferences, project guidelines, or domain knowledge
* Always available to the agent, ensuring consistent behavior

For configuration details and examples, see [Memory](/oss/javascript/deepagents/customization#memory).

### Summarization and context offloading

The harness manages context so deep agents can handle long-running tasks within token limits while retaining the information they need.

**How it works:**

* **Input context**—System prompt, memory, skills, and tool prompts shape what the agent knows at startup
* **Compression**—Built-in offloading and summarization keep context within window limits as tasks progress
* **Isolation**—Subagents quarantine heavy work and return only results (see [Delegation](#delegation))
* **Long-term memory**—Persistent storage across threads via the virtual filesystem

**Why it's useful:**

* Enables multi-step tasks that exceed a single context window
* Keeps the most relevant information in scope without manual trimming
* Reduces token usage through automatic summarization and offloading

For configuration details, see [Context engineering](/oss/javascript/deepagents/context-engineering).

### Prompt caching

For Anthropic models, `create_deep_agent` automatically applies prompt caching to static sections of the system prompt—the base agent instructions, memory, and skill content that repeat on every turn. This avoids reprocessing the same tokens across calls, reducing both latency and cost on long-running agents.

Prompt caching is enabled by default when using an Anthropic model. No configuration is required.

For other providers, see [Middleware integrations](/oss/javascript/integrations/middleware#official-integrations) for available provider-specific caching middleware.

## Delegation

The delegation component enables agents to break large problems into smaller, parallelizable units of work. It has two layers:

* **[Task planning](#task-planning)**: a built-in `write_todos` tool for structured task tracking
* **[Subagents](#subagents)**: ephemeral child agents that handle isolated subtasks

### Task planning

The harness provides a `write_todos` tool that agents can use to maintain a structured task list.

**Features:**

* Track multiple tasks with statuses (`'pending'`, `'in_progress'`, `'completed'`)
* Persisted in agent state
* Helps agent organize complex multi-step work
* Useful for long-running tasks and planning

### Subagents

The harness allows the main agent to create ephemeral "subagents" for isolated multi-step tasks.

**Why it's useful:**

* **Context isolation**—Subagent's work does not clutter main agent's context
* **Parallel execution**—Multiple subagents can run concurrently
* **Specialization**—Subagents can have different tools and configurations
* **Token efficiency**—Large subtask context is compressed into a single result

**How it works:**

* Main agent has a `task` tool
* When invoked, it creates a fresh agent instance with its own context
* Subagent executes autonomously until completion
* Returns a single final report to the main agent
* Can use [default `general-purpose` subagent](/oss/javascript/deepagents/subagents#default-subagent) (enabled by default) or add [custom subagents](/oss/javascript/deepagents/subagents#custom-subagents)
* Subagents are stateless (cannot send multiple messages back)

<Accordion title="Running without subagents (no `task` tool)" icon="ban">
  To run an agent without the `task` tool, see [Running without subagents](/oss/javascript/deepagents/subagents#running-without-subagents). Do not try removing [`SubAgentMiddleware`](https://reference.langchain.com/javascript/deepagents/middleware/createSubAgentMiddleware) via `excluded_middleware`—that is intentionally rejected. Instead, disable the auto-added subagent via the [harness profile](#harness-profiles) and pass no synchronous subagents via `subagents=`. Async subagents are unaffected. See the [default middleware stack](/oss/javascript/deepagents/customization#default-stack-main-agent) for the full ordering.
</Accordion>

For more information, see [Subagents](/oss/javascript/deepagents/subagents).

## Steering

The steering component gives humans control over agent behavior at runtime.

### Human-in-the-loop

The harness can pause agent execution at specified tool calls to allow human approval or modification. This feature is opt-in via the `interrupt_on` parameter.

**Configuration:**

* Pass `interrupt_on` to `create_deep_agent` with a mapping of tool names to interrupt configurations
* Example: `interrupt_on={"edit_file": True}` pauses before every edit
* You can provide approval messages or modify tool inputs when prompted

**Why it's useful:**

* Safety gates for destructive operations
* User verification before expensive API calls
* Interactive debugging and guidance

For more information, see [Human-in-the-loop](/oss/javascript/deepagents/human-in-the-loop).

## Harness profiles

The harness can apply a declarative configuration bundle (a `HarnessProfile`) whenever a given provider or model is selected. Profiles tune runtime behavior after the model is built, without requiring per-agent setup code.

**How it works:**

* Register a profile under a provider name (`"openai"`) or a `provider:model` key (`"openai:gpt-5.5"`)
* `create_deep_agent` looks up and applies the profile when resolving the model
* Provider-level and model-level profiles merge at resolution time

**Why it's useful:**

* Package per-provider or per-model defaults (system-prompt tweaks, tool overrides, middleware) in one place
* Keep the `create_deep_agent` call site unchanged when switching models
* Ship reusable profiles as plugins via entry points

For the full field list, merge semantics, and plugin packaging, see [Profiles](/oss/javascript/deepagents/profiles).

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/deepagents/harness.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Human-in-the-loop
Source: https://docs.langchain.com/oss/javascript/deepagents/human-in-the-loop

Learn how to configure human approval for sensitive tool operations

Some tool operations may be sensitive and require human approval before execution. Deep Agents support human-in-the-loop workflows through LangGraph's interrupt capabilities. You can configure which tools require approval using the `interrupt_on` parameter. When `interrupt_on` is set, `HumanInTheLoopMiddleware` is added to the [default middleware stack](/oss/javascript/deepagents/customization#default-stack-main-agent). If a run is cancelled or interrupted before a tool returns a result, [`PatchToolCallsMiddleware`](https://reference.langchain.com/javascript/deepagents/middleware/createPatchToolCallsMiddleware) in the same stack repairs the message history automatically.

```mermaid theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
graph LR
    Agent[Agent] --> Check{Interrupt?}
    Check --> |no| Execute[Execute]
    Check --> |yes| Human{Human}

    Human --> |approve| Execute
    Human --> |edit| Execute
    Human --> |reject| ToolMessage[ToolMessage]
    Human --> |respond| ToolMessage

    Execute --> Agent
    ToolMessage --> Agent

    classDef trigger fill:#F6FFDB,stroke:#6E8900,stroke-width:2px,color:#2E3900
    classDef process fill:#E5F4FF,stroke:#006DDD,stroke-width:2px,color:#030710
    classDef decision fill:#FDF3FF,stroke:#7E65AE,stroke-width:2px,color:#504B5F
    classDef alert fill:#F8E8E6,stroke:#B27D75,stroke-width:2px,color:#634643

    class Agent trigger
    class Check,Human decision
    class Execute process
    class ToolMessage process
```

## Basic configuration

The `interrupt_on` parameter accepts a dictionary mapping tool names to interrupt configurations. Each tool can be configured with:

* **`True`**: Enable interrupts with default behavior (approve, edit, reject, respond allowed)
* **`False`**: Disable interrupts for this tool
* **`InterruptOnConfig`**: Custom configuration. Set `allowed_decisions` to control review options.

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { tool } from "langchain";
import { createDeepAgent } from "deepagents";
import { MemorySaver } from "@langchain/langgraph";
import { z } from "zod";

const removeFile = tool(
  async ({ path }: { path: string }) => {
    return `Deleted ${path}`;
  },
  {
    name: "remove_file",
    description: "Delete a file from the filesystem.",
    schema: z.object({
      path: z.string(),
    }),
  },
);

const fetchFile = tool(
  async ({ path }: { path: string }) => {
    return `Contents of ${path}`;
  },
  {
    name: "fetch_file",
    description: "Read a file from the filesystem.",
    schema: z.object({
      path: z.string(),
    }),
  },
);

const notifyEmail = tool(
  async ({
    to,
    subject,
    body,
  }: {
    to: string;
    subject: string;
    body: string;
  }) => {
    return `Sent email to ${to}`;
  },
  {
    name: "notify_email",
    description: "Send an email.",
    schema: z.object({
      to: z.string(),
      subject: z.string(),
      body: z.string(),
    }),
  },
);

// Checkpointer is REQUIRED for human-in-the-loop
const checkpointer = new MemorySaver();

const agent = createDeepAgent({
  model: "google_genai:gemini-3.5-flash",
  tools: [removeFile, fetchFile, notifyEmail],
  interruptOn: {
    remove_file: true, // Default: approve, edit, reject, respond
    fetch_file: false, // No interrupts needed
    notify_email: { allowedDecisions: ["approve", "reject"] }, // No editing
  },
  checkpointer, // Required!
});
```

## Decision types

The `allowed_decisions` list controls what actions a human can take when reviewing a tool call:

* **`"approve"`**: Execute the tool with the original arguments as proposed by the agent
* **`"edit"`**: Modify the tool arguments before execution
* **`"reject"`**: Skip executing this tool call entirely and return rejection feedback to the agent
* **`"respond"`**: Return the human's message directly as the tool result, skipping execution, for "ask user" style tools

Use `reject` when the human denies a proposed action. Use `respond` only when the human is acting as the tool, such as answering an `ask_user` prompt. Do not use `respond` to deny side-effecting tools, because its message may be treated by the model as a successful tool result.

You can customize which decisions are available for each tool:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const interruptOn = {
  // Sensitive operations: allow all options
  delete_file: { allowedDecisions: ["approve", "edit", "reject"] },

  // Moderate risk: approval or rejection only
  write_file: { allowedDecisions: ["approve", "reject"] },

  // Must approve (no rejection allowed)
  critical_operation: { allowedDecisions: ["approve"] },
};
```

## Handle interrupts

When an interrupt is triggered, the agent pauses execution and returns control. Check for interrupts in the result and handle them accordingly. If the user rejects an action, include a clear `message` that tells the agent the tool was not executed and what to do next.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { v7 as uuid7 } from "uuid";
import { Command } from "@langchain/langgraph";

// Create config with thread_id for state persistence
const config = { configurable: { thread_id: uuid7() } };

// Invoke the agent
let result = await agent.invoke({
  messages: [{ role: "user", content: "Delete the file temp.txt" }],
}, config);

// Check if execution was interrupted
if (result.__interrupt__) {
  // Extract interrupt information
  const interrupts = result.__interrupt__[0].value;
  const actionRequests = interrupts.actionRequests;
  const reviewConfigs = interrupts.reviewConfigs;

  // Create a lookup map from tool name to review config
  const configMap = Object.fromEntries(
    reviewConfigs.map((cfg) => [cfg.actionName, cfg])
  );

  // Display the pending actions to the user
  for (const action of actionRequests) {
    const reviewConfig = configMap[action.name];
    console.log(`Tool: ${action.name}`);
    console.log(`Arguments: ${JSON.stringify(action.args)}`);
    console.log(`Allowed decisions: ${reviewConfig.allowedDecisions}`);
  }

  // Get user decisions (one per actionRequest, in order)
  const decisions = [
    {
      type: "reject",
      message: "User rejected deleting temp.txt. Do not retry deletion.",
    }
  ];

  // Resume execution with decisions
  result = await agent.invoke(
    new Command({ resume: { decisions } }),
    config  // Must use the same config!
  );
}

// Process final result
console.log(result.messages[result.messages.length - 1].content);
```

## Multiple tool calls

When the agent calls multiple tools that require approval, all interrupts are batched together in a single interrupt. You must provide decisions for each one in order.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const config = { configurable: { thread_id: uuid7() } };

let result = await agent.invoke({
  messages: [{
    role: "user",
    content: "Delete temp.txt and send an email to admin@example.com"
  }]
}, config);

if (result.__interrupt__) {
  const interrupts = result.__interrupt__[0].value;
  const actionRequests = interrupts.actionRequests;

  // Two tools need approval
  console.assert(actionRequests.length === 2);

  // Provide decisions in the same order as actionRequests
  const decisions = [
    { type: "approve" },  // First tool: delete_file
    {
      type: "reject",
      message: "User rejected this action. Do not retry this tool call.",
    }  // Second tool: send_email
  ];

  result = await agent.invoke(
    new Command({ resume: { decisions } }),
    config
  );
}
```

## Rejection messages

When a reviewer returns a `reject` decision, Deep Agents skip the tool call and send rejection feedback back to the agent. If you omit `message`, the default feedback tells the model that the tool was not executed and not to retry the same tool call unless the user asks.

For sensitive or side-effecting tools, pass a domain-specific `message` with the decision. Be explicit about whether the agent should abandon the action, ask a follow-up question, or try a safer alternative.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const decisions = [
  {
    type: "reject",
    message: "User rejected deleting this file. Do not retry deletion. Ask which file to archive instead.",
  },
];
```

## Edit tool arguments

When `"edit"` is in the allowed decisions, you can modify the tool arguments before execution:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
if (result.__interrupt__) {
  const interrupts = result.__interrupt__[0].value;
  const actionRequest = interrupts.actionRequests[0];

  // Original args from the agent
  console.log(actionRequest.args);  // { to: "everyone@company.com", ... }

  // User decides to edit the recipient
  const decisions = [{
    type: "edit",
    editedAction: {
      name: actionRequest.name,  // Must include the tool name
      args: { to: "team@company.com", subject: "...", body: "..." }
    }
  }];

  result = await agent.invoke(
    new Command({ resume: { decisions } }),
    config
  );
}
```

## Subagent interrupts

When using subagents, you can use interrupts [on tool calls](#interrupts-on-tool-calls) and [within tool calls](#interrupts-within-tool-calls).

### Interrupts on tool calls

Each subagent can have its own `interrupt_on` configuration that overrides the main agent's settings:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const agent = createDeepAgent({
  tools: [deleteFile, readFile],
  interruptOn: {
    delete_file: true,
    read_file: false,
  },
  subagents: [{
    name: "file-manager",
    description: "Manages file operations",
    systemPrompt: "You are a file management assistant.",
    tools: [deleteFile, readFile],
    interruptOn: {
      // Override: require approval for reads in this subagent
      delete_file: true,
      read_file: true,  // Different from main agent!
    }
  }],
  checkpointer
});
```

When a subagent triggers an interrupt, the handling is the same—check for `interrupts` on the result and resume with `Command`.

### Interrupts within tool calls

Subagent tools can call `interrupt()` directly to pause execution and await approval:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { createAgent, tool } from "langchain";
import { ChatOpenAI } from "@langchain/openai";
import { HumanMessage } from "@langchain/core/messages";
import { MemorySaver, Command, interrupt } from "@langchain/langgraph";
import { createDeepAgent } from "deepagents";
import { z } from "zod";

const requestApproval = tool(
  async ({ actionDescription }: { actionDescription: string }) => {
    const approval = interrupt({
      type: "approval_request",
      action: actionDescription,
      message: `Please approve or reject: ${actionDescription}`,
    }) as { approved?: boolean; reason?: string };

    if (approval.approved) {
      return `Action '${actionDescription}' was APPROVED. Proceeding...`;
    } else {
      return `Action '${actionDescription}' was REJECTED. Reason: ${
        approval.reason || "No reason provided"
      }`;
    }
  },
  {
    name: "request_approval",
    description: "Request human approval before proceeding with an action.",
    schema: z.object({
      actionDescription: z
        .string()
        .describe("The action that requires approval"),
    }),
  }
);

async function main() {
  const checkpointer = new MemorySaver();
  const model = new ChatOpenAI({
    model: "gpt-4o-mini",
    maxTokens: 4096,
  });

  const compiledSubagent = createAgent({
    model: model,
    tools: [requestApproval],
    name: "approval-agent",
  });

  const parentAgent = await createDeepAgent({
    checkpointer: checkpointer,
    subagents: [
      {
        name: "approval-agent",
        description: "An agent that can request approvals",
        runnable: compiledSubagent as any,
      },
    ],
  });

  const threadId = "test_interrupt_directly";
  const config = { configurable: { thread_id: threadId } };

  console.log("Invoking agent - sub-agent will use request_approval tool...");

  let result = await parentAgent.invoke(
    {
      messages: [
        new HumanMessage({
          content:
            "Use the task tool to launch the approval-agent sub-agent. " +
            "Tell it to use the request_approval tool to request approval for 'deploying to production'.",
        }),
      ],
    },
    config
  );

  if (result.__interrupt__) {
    const interruptValue = result.__interrupt__[0].value as {
      type?: string;
      action?: string;
      message?: string;
    };
    console.log("\nInterrupt received!");
    console.log(`  Type: ${interruptValue.type}`);
    console.log(`  Action: ${interruptValue.action}`);
    console.log(`  Message: ${interruptValue.message}`);

    console.log("\nResuming with Command(resume={'approved': true})...");
    const result2 = await parentAgent.invoke(
      new Command({ resume: { approved: true } }),
      config
    );

    if (!result2.__interrupt__) {
      console.log("\nExecution completed!");
      // Find the tool response
      const toolMsgs = result2.messages?.filter((m) => m.type === "tool") || [];
      if (toolMsgs.length > 0) {
        const lastToolMsg = toolMsgs[toolMsgs.length - 1];
        console.log(`  Tool result: ${lastToolMsg.content}`);
      }
    } else {
      console.log("\nAnother interrupt occurred");
    }
  } else {
    console.log(
      "\n  No interrupt - the model may not have called request_approval"
    );
  }
}

main().catch(console.error);
```

When run, this produces the following output:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
Invoking agent - sub-agent will use request_approval tool...

Interrupt received!
  Type: approval_request
  Action: deploying to production
  Message: Please approve or reject: deploying to production

Resuming with Command(resume={'approved': true})...

Execution completed!
  Tool result: Approval for "deploying to production" has been granted. You can proceed with the deployment.
```

## Best practices

### Always use a checkpointer

Human-in-the-loop requires a checkpointer to persist agent state between the interrupt and resume:

### Use the same thread ID

When resuming, you must use the same config with the same `thread_id`:

### Match decision order to actions

The decisions list must match the order of `action_requests`:

### Tailor configurations by risk

Configure different tools based on their risk level:

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/deepagents/human-in-the-loop.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
