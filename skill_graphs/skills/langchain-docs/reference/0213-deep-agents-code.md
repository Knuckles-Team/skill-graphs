# Deep Agents Code
Source: https://docs.langchain.com/oss/python/deepagents/code/overview

Terminal coding agent built on the Deep Agents SDK

Deep Agents Code (`dcode`) is an open source coding agent built on the [Deep Agents SDK](/oss/python/deepagents/quickstart).
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

    Use the `/auth` command to connect with a provider. See [Providers](/oss/python/deepagents/code/providers) for the full list and credential details.

    <Note>
      Web search uses [Tavily](https://tavily.com) and requires `TAVILY_API_KEY`. See [Enable web search](/oss/python/deepagents/code/configuration#enable-web-search-with-tavily).
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

    See [Model providers](/oss/python/deepagents/code/providers) for the full provider list, open weights options, and credential details.
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
* <Icon icon="cloud" /> **[Remote sandboxes](/oss/python/deepagents/code/remote-sandboxes)** - run agent tools remotely instead of on your local machine.
* <Icon icon="search" /> **Web search** - search the web for up-to-date information and documentation. Requires a [Tavily API key](/oss/python/deepagents/code/configuration#enable-web-search-with-tavily).
* <Icon icon="list-check" /> **Task planning and tracking** - break down complex tasks into discrete steps and track progress.
* <Icon icon="users" /> **[Subagents](/oss/python/deepagents/code/subagents)** - delegate work to task-specific subagents.
* <Icon icon="brain" /> **[Memory storage and retrieval](/oss/python/deepagents/code/memory-and-skills#memory)** - store and retrieve information across sessions, enabling agents to remember project conventions and learned patterns.
* <Icon icon="arrows-minimize" /> **Context compaction & offloading** - summarize older conversation messages and offload originals to storage.
* <Icon icon="user" /> **Human-in-the-loop** - require human approval for sensitive tool operations.
* <Icon icon="puzzle" /> **[Skills](/oss/python/deepagents/code/memory-and-skills#skills)** - extend agent capabilities with custom expertise and instructions.
* <Icon icon="plug" /> **[MCP tools](/oss/python/deepagents/code/mcp-tools)** - load external tools from [Model Context Protocol](https://modelcontextprotocol.io/) servers.
* <Icon icon="chart-dots" /> **[Tracing](/oss/python/deepagents/code/overview#trace-with-langsmith)** - trace agent operations in LangSmith for observability and debugging.

<Accordion title="Full list of built-in tools">
  ## Built-in tools

  The agent comes with the following built-in tools which are available without configuration:

  | Tool                    | Description                                                                                                                    | Human-in-the-Loop    |
  | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------ | -------------------- |
  | `ls`                    | List files and directories                                                                                                     | -                    |
  | `read_file`             | Read contents of a file; returns multimodal blocks for images, audio, video, and PDFs                                          | -                    |
  | `write_file`            | Create or overwrite a file                                                                                                     | Required<sup>1</sup> |
  | `edit_file`             | Make targeted edits to existing files                                                                                          | Required<sup>1</sup> |
  | `glob`                  | Find files matching a pattern                                                                                                  | -                    |
  | `grep`                  | Search for text patterns across files                                                                                          | -                    |
  | `execute`               | Execute shell commands locally or in a [remote sandbox](/oss/python/deepagents/code/remote-sandboxes)                          | Required<sup>1</sup> |
  | `web_search`            | Search the web using Tavily (see [Enable web search](/oss/python/deepagents/code/configuration#enable-web-search-with-tavily)) | Required<sup>1</sup> |
  | `fetch_url`             | Fetch and convert web pages to markdown                                                                                        | Required<sup>1</sup> |
  | `task`                  | Delegate work to [subagents](/oss/python/deepagents/code/subagents) for parallel execution<sup>3</sup>                         | Required<sup>1</sup> |
  | `ask_user`              | Ask the user free-form or multiple-choice questions                                                                            | -                    |
  | `compact_conversation`  | Summarize older messages, offload originals to backend storage, and replace them in context with the summary                   | Mixed<sup>2</sup>    |
  | `write_todos`           | Create and manage task lists for complex work                                                                                  | -                    |
  | `get_current_thread_id` | Return the current thread ID for LangSmith or MCP tooling                                                                      | -                    |

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

  <sup>3</sup>: When async subagents are configured via the `[async_subagents]` section in `config.toml` (see [Async subagents](/oss/python/deepagents/async-subagents)), additional tools become available: `start_async_task`, `update_async_task`, and `cancel_async_task` (all approval-gated), plus `check_async_task` and `list_async_tasks`.
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
