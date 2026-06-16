# Applies conventions without prompting
```

### AGENTS.md files

[`AGENTS.md` files](https://agents.md/) provide persistent context that is always loaded at session start:

* **Global**: `~/.deepagents/<agent_name>/AGENTS.md`—loaded every session.
* **Project**: `.deepagents/AGENTS.md` in any git project root—loaded when Deep Agents Code is run from within that project.

Both files are appended to the system prompt at startup.

### How memory works

The agent may also read its memory files when answering project-specific questions or when you reference past work or patterns.

The agent updates `AGENTS.md` as you provide information on how it should behave, feedback on its work, or instructions to remember something.
It also updates its memory if it identifies patterns or preferences from your interactions.

To add more structured project knowledge in additional memory files, add them in `.deepagents/` and reference them in the `AGENTS.md` file.
You must reference additional files in the `AGENTS.md` file for the agent to be aware of them.
The additional files are not read on startup but the agent can reference and update them when needed.

### When to use global vs. project AGENTS.md

Use a global `AGENTS.md` (`~/.deepagents/agent/AGENTS.md`) for:

* Your personality, style, and universal coding preferences
* General tone and communication style
* Universal coding preferences (formatting, type hints, etc.)
* Tool usage patterns that apply everywhere
* Workflows and methodologies that don't change per-project

Use a project `AGENTS.md` (`.deepagents/AGENTS.md` in project root) for:

* Project-specific context and conventions
* Project architecture and design patterns
* Coding conventions specific to this codebase
* Testing strategies and deployment processes
* Team guidelines and project structure

## Skills

Skills package domain expertise, such as workflows, best practices, scripts, and reference docs, into reusable directories that the agent discovers and reads only when relevant.
Deep agent skills follow the [Agent Skills specification](https://agentskills.io/). For more on how skills work and how to write effective ones, see [Skills](/oss/javascript/deepagents/skills).

At startup, Deep Agents Code reads the name and description from each `SKILL.md` file's frontmatter. When a task matches a skill's description, the agent reads the skill file and follows its instructions. Discovery runs again on `/reload`.

### Add a skill

<Steps>
  <Step title="Create a skill">
    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    # User skill (stored in ~/.deepagents/<agent_name>/skills/)
    dcode skills create test-skill

    # Project skill (stored in .deepagents/skills/)
    dcode skills create test-skill --project
    ```

    This generates:

    ```plaintext theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    skills/
    └── test-skill
        └── SKILL.md
    ```
  </Step>

  <Step title="Edit SKILL.md">
    Open the generated `SKILL.md` and edit the file to include your instructions.
  </Step>

  <Step title="Add optional resources">
    Optionally add additional scripts or other resources to the `test-skill` folder. For more information, see [Usage](/oss/javascript/deepagents/skills#add-supporting-resources).
  </Step>
</Steps>

You can also copy existing skills directly to the agent's folder:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
mkdir -p ~/.deepagents/<agent_name>/skills
cp -r examples/skills/web-research ~/.deepagents/<agent_name>/skills/
```

### Install community skills

You can use tools like Vercel's [Skills CLI](https://github.com/vercel-labs/skills) to install community [Agent Skills](https://agentskills.io/) in your environment and make them available to your deep agents:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# Install a skill globally
npx skills add vercel-labs/agent-skills --skill web-design-guidelines -a deepagents -g -y

# List installed skills
npx skills ls -a deepagents -g
```

Global installs (`-g`) symlink skills into `~/.deepagents/agent/skills/`—the default agent's user-level skills directory. Project-level installs (omit `-g`) place skills in `.deepagents/skills/` relative to the current directory, making them available to any agent running in that project regardless of agent name.

<Note>
  Global installs target the default `agent` directory only. If you use a custom-named agent, either use project-level installs or manually symlink the skill into `~/.deepagents/{your-agent}/skills/`.
</Note>

### Skill discovery

Skills are loaded from the following directories at startup:

```text theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
~/.deepagents/<agent_name>/skills/
~/.agents/skills/
.deepagents/skills/
.agents/skills/
~/.claude/skills/          (experimental)
.claude/skills/            (experimental)
```

When duplicate skill names exist, later-precedence directories override earlier ones (see [App data](/oss/javascript/deepagents/code/data-locations#skills)).

For project-specific skills (under `.deepagents/skills/` or `.agents/skills/`), the project root is identified by a containing `.git` folder.

### Invoke a skill mid-session

Inside an interactive session, run a skill directly with the `/skill:<name>` slash command:

```text theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
/skill:code-review
/skill:code-review review the auth module
```

The skill's `SKILL.md` instructions are injected into the prompt along with any arguments you pass.

### Launch with a skill

The `--skill` flag invokes a skill immediately on launch, in either interactive (TUI) or non-interactive (headless) mode:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# Open the TUI and immediately run a skill
dcode --skill code-review

# Pass a request to the skill with -m
dcode --skill code-review -m 'review the auth module'

# Pipe content into a skill
cat diff.txt | dcode --skill code-review

# Pipe content and add a request
cat diff.txt | dcode --skill code-review -m 'focus on security'

# Run a skill headlessly
dcode --skill code-review -n 'review this patch'

# Quiet mode (only agent output on stdout)
dcode --skill code-review -n 'review this patch' -q
```

<Note>
  `--skill` with `--quiet` or `--no-stream` requires `-n` (non-interactive mode).
</Note>

### List skills

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# List all user skills
dcode skills list

# List project skills
dcode skills list --project

# Get detailed info about a specific skill
dcode skills info test-skill
dcode skills info test-skill --project
```

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/deepagents/code/memory-and-skills.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Deep Agents Code
Source: https://docs.langchain.com/oss/javascript/deepagents/code/overview

Terminal coding agent built on the Deep Agents SDK

Deep Agents Code (`dcode`) is an open source coding agent built on the [Deep Agents SDK](/oss/javascript/deepagents/quickstart).
It works with any large language model and supports switching between providers or models mid-session.
Persistent memory carries context across conversations, customizable skills shape its behavior, and approval controls gate code execution.

## Quickstart

<Steps>
  <Step title="Install and launch" icon="terminal">
    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    curl -LsSf https://langch.in/dcode | bash
    ```
  </Step>

  <Step title="Add provider credentials" icon="key">
    Deep Agents Code works with any tool-calling LLM. OpenAI, Anthropic, and Google are available out of the box.

    Use the `/auth` command to connect with a provider. See [Providers](/oss/javascript/deepagents/code/providers) for the full list and credential details.

    <Note>
      Web search uses [Tavily](https://tavily.com) and requires `TAVILY_API_KEY`. See [Enable web search](/oss/javascript/deepagents/code/configuration#enable-web-search-with-tavily).
    </Note>
  </Step>

  <Step title="Choose a model (optional)" icon="cpu">
    Run `/model` inside a session to open the interactive switcher, or launch with `--model`:

    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    dcode --model anthropic:claude-opus-4-8
    dcode --model openai:gpt-5.5
    dcode --model fireworks:accounts/fireworks/models/deepseek-v4-pro
    dcode --model baseten:moonshotai/Kimi-K2.6
    ```

    See [Model providers](/oss/javascript/deepagents/code/providers) for the full provider list, open weights options, and credential details.
  </Step>

  <Step title="Give the agent a task" icon="message">
    ```txt theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    Create a Python script that prints "Hello, World!"
    ```

    The agent interprets the query and proposes changes with diffs for your approval before modifying files. If needed, it can run shell commands to test the code, check documentation, or search the web for up-to-date information.
  </Step>

  <Step title="Enable tracing (optional)" icon="chart-dots">
    To log agent operations, tool calls, and decisions in LangSmith, add the following to `~/.deepagents/.env` or export the variables in your shell:

    ```bash title="~/.deepagents/.env" theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    LANGSMITH_TRACING=true
    LANGSMITH_API_KEY=lsv2_...
    LANGSMITH_PROJECT=optional-project-name  # Specify a project name or default to "deepagents-code"
    ```

    For more details and usage, see [Trace with LangSmith](#trace-with-langsmith).
  </Step>
</Steps>

<Note>
  Deep Agents Code is not officially supported on Windows. Windows users can try running it under [Windows Subsystem for Linux (WSL)](https://learn.microsoft.com/en-us/windows/wsl/install).
</Note>

## Capabilities

Deep Agents Code has the following built-in capabilities:

* <Icon icon="file" /> **File operations** - read, write, and edit files on disk.
* <Icon icon="terminal" /> **Shell execution** - execute commands to run tests, build projects, manage dependencies, and interact with version control.
* <Icon icon="cloud" /> **[Remote sandboxes](/oss/javascript/deepagents/code/remote-sandboxes)** - run agent tools remotely instead of on your local machine.
* <Icon icon="search" /> **Web search** - search the web for up-to-date information and documentation. Requires a [Tavily API key](/oss/javascript/deepagents/code/configuration#enable-web-search-with-tavily).
* <Icon icon="list-check" /> **Task planning and tracking** - break down complex tasks into discrete steps and track progress.
* <Icon icon="users" /> **[Subagents](/oss/javascript/deepagents/code/subagents)** - delegate work to task-specific subagents.
* <Icon icon="brain" /> **[Memory storage and retrieval](/oss/javascript/deepagents/code/memory-and-skills#memory)** - store and retrieve information across sessions, enabling agents to remember project conventions and learned patterns.
* <Icon icon="arrows-minimize" /> **Context compaction & offloading** - summarize older conversation messages and offload originals to storage.
* <Icon icon="user" /> **Human-in-the-loop** - require human approval for sensitive tool operations.
* <Icon icon="puzzle" /> **[Skills](/oss/javascript/deepagents/code/memory-and-skills#skills)** - extend agent capabilities with custom expertise and instructions.
* <Icon icon="plug" /> **[MCP tools](/oss/javascript/deepagents/code/mcp-tools)** - load external tools from [Model Context Protocol](https://modelcontextprotocol.io/) servers.
* <Icon icon="chart-dots" /> **[Tracing](/oss/javascript/deepagents/code/overview#trace-with-langsmith)** - trace agent operations in LangSmith for observability and debugging.

<Accordion title="Full list of built-in tools">
  ## Built-in tools

  The agent comes with the following built-in tools which are available without configuration:

  | Tool                    | Description                                                                                                                        | Human-in-the-Loop    |
  | ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | -------------------- |
  | `ls`                    | List files and directories                                                                                                         | -                    |
  | `read_file`             | Read contents of a file; returns multimodal blocks for images, audio, video, and PDFs                                              | -                    |
  | `write_file`            | Create or overwrite a file                                                                                                         | Required<sup>1</sup> |
  | `edit_file`             | Make targeted edits to existing files                                                                                              | Required<sup>1</sup> |
  | `glob`                  | Find files matching a pattern                                                                                                      | -                    |
  | `grep`                  | Search for text patterns across files                                                                                              | -                    |
  | `execute`               | Execute shell commands locally or in a [remote sandbox](/oss/javascript/deepagents/code/remote-sandboxes)                          | Required<sup>1</sup> |
  | `web_search`            | Search the web using Tavily (see [Enable web search](/oss/javascript/deepagents/code/configuration#enable-web-search-with-tavily)) | Required<sup>1</sup> |
  | `fetch_url`             | Fetch and convert web pages to markdown                                                                                            | Required<sup>1</sup> |
  | `task`                  | Delegate work to [subagents](/oss/javascript/deepagents/code/subagents) for parallel execution<sup>3</sup>                         | Required<sup>1</sup> |
  | `ask_user`              | Ask the user free-form or multiple-choice questions                                                                                | -                    |
  | `compact_conversation`  | Summarize older messages, offload originals to backend storage, and replace them in context with the summary                       | Mixed<sup>2</sup>    |
  | `write_todos`           | Create and manage task lists for complex work                                                                                      | -                    |
  | `get_current_thread_id` | Return the current thread ID for LangSmith or MCP tooling                                                                          | -                    |

  <sup>1</sup>: Potentially destructive operations require user approval before execution. To bypass human approval, you can toggle auto-approve (shift+tab) or start with the option:

  ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  dcode --auto-approve
  # shorter alias:
  dcode -y
  ```

  <Note>
    Non-interactive mode disables shell by default. Allowlist commands with `-S`/`--shell-allow-list` (or `DEEPAGENTS_CODE_SHELL_ALLOW_LIST`). Use `recommended` for read-only safe defaults, or `all` to permit anything. See [Non-interactive mode and piping](#non-interactive-mode-and-piping).
  </Note>

  <sup>2</sup>: Deep Agents Code automatically offloads the conversation in the background when token usage exceeds a model-aware threshold. Offloading summarizes older messages via the LLM, and ejects originals to storage (`/conversation_history/{thread_id}.md`), replacing them in context with the summary. The agent can still retrieve the full history from the offloaded file if needed. The `compact_conversation` tool lets the agent (or you) trigger offloading on demand. When called as a tool, it requires user approval by default.

  <sup>3</sup>: When async subagents are configured via the `[async_subagents]` section in `config.toml` (see [Async subagents](/oss/javascript/deepagents/async-subagents)), additional tools become available: `start_async_task`, `update_async_task`, and `cancel_async_task` (all approval-gated), plus `check_async_task` and `list_async_tasks`.
</Accordion>

## Command reference

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# Use a specific agent configuration
dcode --agent mybot

# Use a specific model (provider:model format or auto-detect)
dcode --model anthropic:claude-opus-4-8
dcode --model gpt-5.5

# Auto-approve tool usage (skip human-in-the-loop prompts)
dcode -y

# list directory contents, then summarize directory as first prompt—the command runs first, then the prompt is submitted

# the prompt does NOT have access to the command output
dcode --startup-cmd "ls -la" -m "Summarize what's in this directory"

# Non-interactive with startup command: show git status before the task runs
