# Trace Claude Code applications
Source: https://docs.langchain.com/langsmith/trace-claude-code

This guide shows you how to send conversations automatically from the [Claude Code CLI](https://code.claude.com/docs/en/overview) to LangSmith.

Once configured, each Claude Code project can opt in to sending traces to LangSmith. Each trace includes user messages, tool calls, compaction, subagent runs, and assistant responses. System prompts are not included, because Claude Code does not return them in conversation transcripts.

## Prerequisites

Before setting up tracing, ensure you have:

* [**Claude Code CLI**](https://code.claude.com/docs/en/overview) installed.
* A [**LangSmith API key**](/langsmith/create-account-api-key).
* [**Node.js**](https://nodejs.org/) installed.

## Getting started

From within Claude Code, run:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
/plugin marketplace add langchain-ai/langsmith-claude-code-plugins
/plugin install langsmith-tracing@langsmith-claude-code-plugins
/reload-plugins
```

To update the plugin, run:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
/plugin marketplace update langsmith-claude-code-plugins
/reload-plugins
```

<Note> If you are migrating from the previously recommended version of tracing Claude Code with manually created stop hooks, refer to [Migrating from the manual stop hook](#migrating-from-the-manual-stop-hook). </Note>

### Setting environment variables

**Option 1: Project-level configuration (recommended)**

The plugin requires the following environment variables:

* `TRACE_TO_LANGSMITH: "true"`: Enables tracing for this project. Remove or set to `false` to disable tracing.
* `CC_LANGSMITH_API_KEY`: Your LangSmith API key.
* `CC_LANGSMITH_PROJECT`: The LangSmith project name to which your traces will send.
* (optional) `CC_LANGSMITH_METADATA`: JSON object of custom metadata to attach to all runs (e.g., PR URL, author).
* (optional) `CC_LANGSMITH_DEBUG: "true"`: Enables detailed debug logging. Remove or set to `false` to disable debug logging.

To get set up, create or edit [Claude Code's project settings file](https://code.claude.com/docs/en/settings#:~:text=Project%20settings%20are%20saved%20in%20your%20project%20directory%3A). Create a `.claude/settings.local.json` in your project directory and populate it as follows:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "env": {
    "TRACE_TO_LANGSMITH": "true",
    "CC_LANGSMITH_API_KEY": "<LangSmith API key>",
    "CC_LANGSMITH_PROJECT": "my-project"
  }
}
```

<Note> Alternatively, to enable tracing to LangSmith for all Claude Code sessions, you can add the previous JSON to your [global Claude Code settings.json](https://code.claude.com/docs/en/settings#:~:text=User%20settings%20are%20defined%20in%20~/.claude/settings.json%20and%20apply%20to%20all%20projects.) file. </Note>

**Option 2: Shell environment variables**

Run the following commands in your shell or add them to your shell configuration file (`~/.zshrc`, `~/.bashrc`, or `~/.bash_profile`):

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
export TRACE_TO_LANGSMITH="true"
export CC_LANGSMITH_API_KEY="<LangSmith API key>"
export CC_LANGSMITH_PROJECT="my-project"
```

## Verify setup

Traces will appear complete in your [LangSmith](https://smith.langsmith.com) project after Claude Code responds. If you interrupt a run while it is in progress, the plugin will only flush that run when you send the next message or end the session.

In LangSmith, you'll find:

* Each message to Claude Code appears as a trace.
* All turns from the same Claude Code session are grouped using a shared `thread_id`, which you can view in the **Threads** tab of a project.

## Custom metadata

Set the `CC_LANGSMITH_METADATA` environment variable to a JSON object to attach custom metadata to all traced runs. This is useful for tagging traces with contextual information such as PR URLs, authors, or environment names.

<Tabs>
  <Tab title="Settings file (recommended)">
    ```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    {
      "env": {
        "TRACE_TO_LANGSMITH": "true",
        "CC_LANGSMITH_API_KEY": "<LangSmith API key>",
        "CC_LANGSMITH_PROJECT": "my-project",
        "CC_LANGSMITH_METADATA": "{\"author\":\"jane\",\"environment\":\"development\"}"
      }
    }
    ```
  </Tab>

  <Tab title="Shell environment variable">
    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    export CC_LANGSMITH_METADATA='{"author":"jane","environment":"development"}'
    ```
  </Tab>
</Tabs>

The metadata keys and values will appear on all runs in LangSmith, which you can use to filter and search traces.

## Usage with GitHub Actions

You can use this plugin with [`anthropics/claude-code-action`](https://github.com/anthropics/claude-code-action) to trace Claude Code runs in CI. Add the following to your workflow:

```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
- uses: anthropics/claude-code-action@v1
  env:
    TRACE_TO_LANGSMITH: "true"
    CC_LANGSMITH_API_KEY: ${{ secrets.LANGSMITH_API_KEY }}
    CC_LANGSMITH_PROJECT: "my-project"
    CC_LANGSMITH_METADATA: |
      {
        "pr_url": "${{ github.event.pull_request.html_url || '' }}",
        "pr_number": "${{ github.event.pull_request.number || '' }}",
        "pr_author": "${{ github.event.pull_request.user.login || '' }}",
        "repository": "${{ github.repository }}",
        "commit_sha": "${{ github.sha }}",
        "trigger": "${{ github.event_name }}"
      }
  with:
    anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
    github_token: ${{ secrets.GITHUB_TOKEN }}
    plugin_marketplaces: |
      https://github.com/langchain-ai/langsmith-claude-code-plugins.git
    plugins: |
      langsmith-tracing@langsmith-claude-code-plugins
    prompt: |
      Your prompt here
```

Make sure to add `LANGSMITH_API_KEY` and `ANTHROPIC_API_KEY` as [repository secrets](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions).

This lets you correlate traces back to specific PRs, commits, and authors in LangSmith.

## Nesting traces under an existing run

You can also set an environment variable named `CC_LANGSMITH_PARENT_DOTTED_ORDER` to nest all Claude Code traces as children of an existing LangSmith run. This is useful when Claude Code is invoked programmatically as part of a larger traced workflow.

**Python**

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import subprocess
from langsmith import traceable, get_current_run_tree

os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_API_KEY"] = "<LangSmith API key>"
os.environ["LANGSMITH_PROJECT"] = "claude-code"

@traceable
def run_claude(prompt: str):
    run_tree = get_current_run_tree()
    subprocess.run(
        ["claude", "-p", prompt],
        env={
            **os.environ,
            "TRACE_TO_LANGSMITH": "true",
            "CC_LANGSMITH_API_KEY": "<LangSmith API key>",
            "CC_LANGSMITH_PROJECT": "claude-code",
            "CC_LANGSMITH_PARENT_DOTTED_ORDER": run_tree.dotted_order,
        },
    )
```

**TypeScript**

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { traceable, getCurrentRunTree } from "langsmith/traceable";
import { execSync } from "node:child_process";

process.env.LANGSMITH_TRACING = "true";
process.env.LANGSMITH_API_KEY = "<LangSmith API key>";
process.env.LANGSMITH_PROJECT = "claude-code";

const runClaude = traceable(
  async (prompt: string) => {
    const runTree = getCurrentRunTree();
    const pluginDir = new URL(".", import.meta.url).pathname;
    const res = execSync(`claude -p "${prompt}" --plugin-dir '${pluginDir}'`, {
      env: {
        ...process.env,
        TRACE_TO_LANGSMITH: "true",
        CC_LANGSMITH_API_KEY: "<LangSmith API key>",
        CC_LANGSMITH_PROJECT: "claude-code",
        CC_LANGSMITH_PARENT_DOTTED_ORDER: runTree.dotted_order,
      },
    });
    return res.toString();
  },
  { name: "run_claude" },
);
```

The resulting trace hierarchy looks like:

```
Your outer run (chain)
└── Claude Code Turn (chain)
    ├── Claude (llm)
    ├── Read (tool)
    └── Claude (llm)
```

## Trace to multiple destinations (replicas)

You can trace to multiple LangSmith projects or workspaces simultaneously using the `CC_LANGSMITH_RUNS_ENDPOINTS` environment variable. Set `CC_LANGSMITH_RUNS_ENDPOINTS` to a JSON array of replica configurations. This overrides other client settings.

Tracing to multiple [replicas](/langsmith/log-traces-to-project) is useful for:

* Sending traces to both a production and staging project.
* Tracing to multiple workspaces with different API keys.
* Adding extra metadata to specific replica destinations.

Each replica object supports the following fields:

| Field         | Required | Description                                                                            |
| ------------- | -------- | -------------------------------------------------------------------------------------- |
| `apiUrl`      | Yes      | LangSmith API URL (typically `https://api.smith.langchain.com`)                        |
| `apiKey`      | Yes      | API key for the destination [workspace](/langsmith/administration-overview#workspaces) |
| `projectName` | Yes      | Project name in the destination workspace                                              |
| `updates`     | No       | Optional metadata/fields to override on the replicated runs                            |

There are two ways to set the `CC_LANGSMITH_RUNS_ENDPOINTS` environment variable:

<Tabs>
  <Tab title="Settings file (recommended)">
    In your local `.claude/settings.local.json` or global `~/.claude/settings.json`:

    ```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    {
      "env": {
        "TRACE_TO_LANGSMITH": "true",
        "CC_LANGSMITH_RUNS_ENDPOINTS": "[{\"apiUrl\":\"https://api.smith.langchain.com\",\"apiKey\":\"ls__key_workspace_a\",\"projectName\":\"project-prod\"},{\"apiUrl\":\"https://api.smith.langchain.com\",\"apiKey\":\"ls__key_workspace_b\",\"projectName\":\"project-staging\",\"updates\":{\"metadata\":{\"environment\":\"staging\"}}}]"
      }
    }
    ```

    <Tip>
      To generate the escaped JSON string, use:

      ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      echo '[{"apiUrl":"...","apiKey":"...","projectName":"..."}]' | jq -cR .
      ```
    </Tip>
  </Tab>

  <Tab title="Shell environment variable">
    **Option 2: Shell environment variable**

    Add to your `~/.zshrc`, `~/.bashrc`, or `~/.bash_profile`:

    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    export CC_LANGSMITH_RUNS_ENDPOINTS='[{"apiUrl":"https://api.smith.langchain.com","apiKey":"ls__key_workspace_a","projectName":"project-prod"},{"apiUrl":"https://api.smith.langchain.com","apiKey":"ls__key_workspace_b","projectName":"project-staging","updates":{"metadata":{"environment":"staging"}}}]'
    ```
  </Tab>
</Tabs>

## Troubleshooting

### No traces appearing in LangSmith

1. **Check the hook is running**:
   ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
   tail -f ~/.claude/state/hook.log
   ```
   You should see log entries after each Claude response.

2. **Verify environment variables**:
   * Check that `TRACE_TO_LANGSMITH="true"` in your project's `.claude/settings.local.json`.
   * Verify your Personal Access Token (PAT) is correct (starts with `lsv2_pt_`).
   * Ensure the project name exists in LangSmith.

3. **Enable debug mode** to see detailed API activity:
   ```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
   {
     "env": {
       "CC_LANGSMITH_DEBUG": "true"
     }
   }
   ```
   Then check logs for API calls and HTTP status codes.

### Subagent runs do not appear after user interruption

Subagents are only traced upon completion. This means if you interrupt a conversation turn in the middle of a subagent run, the subagent's child runs will not be traced.

### Managing log file size

The hook logs all activity to `~/.claude/state/hook.log`. With debug mode enabled, this file can grow large:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# View log file size
ls -lh ~/.claude/state/hook.log

# Clear logs if needed
> ~/.claude/state/hook.log
```

## Migrating from the manual stop hook

If you were using the previous version of tracing Claude Code with LangSmith, you will need to remove `~/.claude/hooks/stop_hook.sh` and remove the reference to the hook from any previous `settings.local.json` or `settings.json` files you added it to previously, then follow the [plugin installation instructions](#getting-started).

## Source code

The plugin is open-source under the MIT license and is available in [this GitHub repo](https://github.com/langchain-ai/langsmith-claude-code-plugins).

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-claude-code.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Trace Deep Agents applications
Source: https://docs.langchain.com/langsmith/trace-deep-agents

[`deepagents`](/oss/python/deepagents/overview) is an open-source agent framework built on top of LangGraph, designed for complex, multi-step tasks that require planning, tool usage, and sub-agent delegation. Deep Agents supports native LangSmith tracing.

This guide shows you how to enable LangSmith tracing for Deep Agents, view traces in the LangSmith UI, and (optionally) customize trace configuration for more advanced use cases.

## Installation

Install `deepagents` in your Python environment:

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install deepagents
  ```

  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv add deepagents
  ```
</CodeGroup>

`deepagents` requires:

* Python 3.11+.
* An LLM that supports tool calling (for example, OpenAI or Anthropic models).
* For tracing, a [LangSmith account and API key](/langsmith/create-account-api-key) (free to sign up).

<Note>
  You do not need to install the `langsmith` Python package to trace Deep Agents. `deepagents` is built on LangGraph, which includes native LangSmith tracing support. As long as the LangSmith environment variables are set, traces are sent automatically.

  The `langsmith` package is only required if you want [programmatic control over tracing](#customize-langsmith-tracing) (for example, using `tracing_context`, adding custom metadata, or querying runs from Python).
</Note>

## Setup

You can find your LangSmith API key and project name in the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-trace-deep-agents) under **Settings**:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
export LANGSMITH_API_KEY=<your-langsmith-api-key>
export LANGSMITH_TRACING=true
export LANGSMITH_PROJECT=<your-project-name>
```

## Create a trace

Once tracing is enabled via environment variables, Deep Agents will automatically emit traces to LangSmith. For example:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from typing import Dict, Any, List

from deepagents import create_deep_agent

def compute_compound_interest(
    principal: float,
    annual_rate: float,
    years: int,
    compounds_per_year: int,
) -> Dict[str, Any]:
    """Compute compound interest and return ending balance and interest earned."""
    r = annual_rate
    n = compounds_per_year
    t = years
    amount = principal * (1 + r / n) ** (n * t)
    interest = amount - principal
    return {
        "principal": principal,
        "annual_rate": annual_rate,
        "years": years,
        "compounds_per_year": n,
        "ending_balance": round(amount, 2),
        "interest_earned": round(interest, 2),
    }

def yearly_balance_schedule(
    principal: float,
    annual_rate: float,
    years: int,
    compounds_per_year: int,
) -> List[Dict[str, Any]]:
    """Return a year-by-year balance schedule for the investment."""
    r = annual_rate
    n = compounds_per_year
    schedule: List[Dict[str, Any]] = []

    for year in range(1, years + 1):
        amount = principal * (1 + r / n) ** (n * year)
        schedule.append(
            {
                "year": year,
                "ending_balance": round(amount, 2),
                "interest_earned": round(amount - principal, 2),
            }
        )

    return schedule

agent = create_deep_agent(
    model="google_genai:gemini-3.5-flash",
    tools=[compute_compound_interest, yearly_balance_schedule],
    system_prompt=(
        "You are a careful assistant. "
        "Use tools for calculations and structured outputs. "
        "Return a concise final answer."
    ),
)

result = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": (
                    "I have $2,500 invested at 6% annual interest compounded monthly for 5 years.\n"
                    "1) Compute the ending balance and total interest earned.\n"
                    "2) Generate a year-by-year ending balance schedule.\n"
                    "Then summarize the key takeaways in 3 bullets.\n\n"
                    "Use compounds_per_year=12."
                ),
            }
        ]
    }
)

print(result)
```

## Viewing traces

### Details View

Click on the trace, and toggle to the **Details** view on the top right. Your trace tree in the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-trace-deep-agents) will look like [this](https://smith.langchain.com/public/ec82be64-b158-425e-a959-924be16b8588/r), with the following structure:

* Agent run (top level) representing the full Deep Agents invocation.
* LLM call where the agent analyzes the user request and decides which tools to use.
* Tool run: `compute_compound_interest`:
  * Displays the tool inputs (for example, principal, annual\_rate, years, and compounds\_per\_year).
  * Displays the structured output, including the ending balance and total interest earned.
* LLM call that interprets the calculation results and determines the next step.
* Tool run: `yearly_balance_schedule`:
  * Shows the inputs used to generate the schedule.
  * Returns a year-by-year breakdown of ending balances and interest earned.
* Final LLM response that summarizes the results for the user.

The resulting trace contains multiple nested spans, which allows you to follow the agent’s planning, calculation steps, and interpretation flow in the LangSmith UI.

### Messages View

The **Messages** view in the LangSmith UI shows a simplified conversation history between the user and the agent. This view pulls messages from the top-level trace, (including the user’s initial request, tool calls and the agent’s final response) and represents them in a chat-like format.

### Filter by subagent

Deep Agents automatically writes the subagent's `name` to the `lc_agent_name` metadata key on every run that subagent produces. Use this to isolate all runs from a specific subagent in LangSmith—useful for debugging, monitoring, or comparing subagent behavior.

**Filter in the LangSmith UI:**

1. Open your tracing project in [LangSmith](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-trace-deep-agents).
2. Switch the view to **Runs** to see individual spans.
3. Click **Add filter** and select **Metadata**.
4. Set the **Key** to `lc_agent_name` and the **Value** to the subagent name, for example `research-agent`.

Save the filter as a named view for quick reuse. For a full reference on filter options, see [Filter traces](/langsmith/filter-traces-in-application).

**Filter programmatically with the SDK:**

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langsmith import Client

client = Client()

# Fetch all runs produced by a specific subagent
runs = client.list_runs(
    project_name="<your-project>",
    filter='has(metadata, \'{"lc_agent_name": "research-agent"}\')',
)

for run in runs:
    print(run.name, run.start_time, run.status)
```

For the full filter query language reference, see [Trace query syntax](/langsmith/trace-query-syntax).

## Customize LangSmith tracing

By default, Deep Agents traces are emitted automatically when LangSmith tracing is enabled via environment variables. You can use the [LangSmith SDK](https://reference.langchain.com/python/langsmith/observability/sdk/) directly to customize your tracing, such as scoping traces to part of your code, attaching tags or metadata, or overriding the project name.

Install and use `langsmith` if you want to:

* Trace only specific agent invocations.
* Add custom tags or metadata for filtering in the UI.
* Override the project name at runtime.

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install langsmith
  ```

  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv add langsmith
  ```
</CodeGroup>

This example invokes the same deep agent twice:

* The first invocation is untraced, because it runs outside of `tracing_context`.
* The second invocation is traced, because it runs inside `tracing_context(enabled=True, ...)`.

You can selectively trace only part of your workflow, without enabling global tracing for your entire process with `LANGSMITH_TRACING=true`:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from typing import Dict, Any, List

import langsmith as ls
from deepagents import create_deep_agent

def compute_compound_interest(
    principal: float,
    annual_rate: float,
    years: int,
    compounds_per_year: int,
) -> Dict[str, Any]:
    """Compute compound interest and return ending balance and interest earned."""
    r = annual_rate
    n = compounds_per_year
    t = years
    amount = principal * (1 + r / n) ** (n * t)
    interest = amount - principal
    return {
        "principal": principal,
        "annual_rate": annual_rate,
        "years": years,
        "compounds_per_year": n,
        "ending_balance": round(amount, 2),
        "interest_earned": round(interest, 2),
    }

def yearly_balance_schedule(
    principal: float,
    annual_rate: float,
    years: int,
    compounds_per_year: int,
) -> List[Dict[str, Any]]:
    """Return a year-by-year balance schedule for the investment."""
    r = annual_rate
    n = compounds_per_year
    schedule: List[Dict[str, Any]] = []

    for year in range(1, years + 1):
        amount = principal * (1 + r / n) ** (n * year)
        schedule.append(
            {
                "year": year,
                "ending_balance": round(amount, 2),
                "interest_earned": round(amount - principal, 2),
            }
        )

    return schedule

agent = create_deep_agent(
    model="google_genai:gemini-3.5-flash",
    tools=[compute_compound_interest, yearly_balance_schedule],
    system_prompt=(
        "You are a careful assistant. "
        "Use tools for calculations and structured outputs. "
        "Return a concise final answer."
    ),
)

# ----------------------------

# Untraced invocation

# ----------------------------
agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": (
                    "I have $2,500 invested at 6% annual interest compounded monthly for 5 years. "
                    "Compute the ending balance and total interest earned. "
                    "Use compounds_per_year=12."
                ),
            }
        ]
    }
)

# ----------------------------

# Traced invocation

# ----------------------------
with ls.tracing_context(
    enabled=True,
    project_name="deepagents-demo",
    tags=["deepagents", "scoped-tracing"],
    metadata={"example": "partial-workflow"},
):
    agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": (
                        "I have $2,500 invested at 6% annual interest compounded monthly for 5 years.\n"
                        "1) Compute the ending balance and total interest earned.\n"
                        "2) Generate a year-by-year ending balance schedule.\n"
                        "Then summarize the key takeaways in 3 bullets.\n\n"
                        "Use compounds_per_year=12."
                    ),
                }
            ]
        }
    )
```

The `tracing_context` block enables tracing and also configures how the trace is recorded and organized in LangSmith:

* `enabled=True` explicitly enables tracing for the duration of the block, even if `LANGSMITH_TRACING` is unset or set to `false`.
* `project_name="deepagents-demo"` routes traces from this block to the specified [LangSmith project](/langsmith/log-traces-to-project). This overrides `LANGSMITH_PROJECT` for runs created within the context.
* `tags=[...]` attaches tags to the traced runs. [Tags](/langsmith/add-metadata-tags) appear in the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-trace-deep-agents), which you can use to filter and group traces.
* `metadata={...}` attaches arbitrary structured metadata (for example, environment, experiment name, or feature flag).

In this example, the agent is invoked twice, but only the invocation inside `tracing_context` is recorded. This demonstrates how you can selectively trace specific parts of a Deep Agents workflow without enabling global tracing for the entire process.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-deep-agents.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Trace DeepSeek applications
Source: https://docs.langchain.com/langsmith/trace-deepseek

[DeepSeek](https://deepseek.com/) provides high-performance, OpenAI-compatible language models including `deepseek-chat` (for general conversations) and `deepseek-reasoner` (for advanced reasoning tasks). Using LangSmith allows you to debug, monitor, and evaluate your LLM applications by capturing structured traces of inputs, outputs, and metadata.

This guide shows you how to integrate DeepSeek with LangSmith in both Python and TypeScript, using LangSmith's [`@traceable`](https://reference.langchain.com/python/langsmith/run_helpers/traceable) (Python) and [`traceable(...)`](https://reference.langchain.com/javascript/modules/langsmith.html) (TypeScript) utilities to log LLM calls automatically.

## Installation

Install [OpenAI](https://platform.openai.com/docs/libraries) and LangSmith:

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install openai langsmith
  ```

  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv add openai langsmith
  ```

  ```bash npm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  npm install openai langsmith dotenv
  ```
</CodeGroup>

DeepSeek provides an [OpenAI-compatible API](https://api-docs.deepseek.com/), which means you can use the OpenAI SDK to interact with DeepSeek models. The only difference is that you configure the client to point to DeepSeek's base URL (`https://api.deepseek.com/v1`) instead of OpenAI's endpoint.

## Setup

Set your [API keys](/langsmith/create-account-api-key) and project name:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
export LANGSMITH_API_KEY="your-langsmith-api-key"
export LANGSMITH_TRACING="true"
export LANGSMITH_PROJECT="deepseek-integration"
export DEEPSEEK_API_KEY="your-deepseek-api-key"
```

* Ensure you have a DeepSeek API key from your [DeepSeek account](https://platform.deepseek.com/).
* Set `LANGSMITH_TRACING=true` and provide your LangSmith API key (`LANGSMITH_API_KEY`) activates automatic logging of traces.
* Specify a [`LANGSMITH_PROJECT`](/langsmith/log-traces-to-project) name to organize traces by project; if not set, traces go to the default project (named "default").
* The `LANGSMITH_TRACING` flag must be true for any traces to be recorded.

## Configure tracing

1. Instrument the DeepSeek API call with LangSmith. In your script, create an OpenAI client configured to use DeepSeek's API endpoint and wrap a call in a traced function:

   <CodeGroup>
     ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
     import os
     from openai import OpenAI
     from langsmith import traceable

     # Create a client pointing to DeepSeek
     client = OpenAI(
         api_key=os.environ["DEEPSEEK_API_KEY"],
         base_url="https://api.deepseek.com/v1"
     )

     @traceable(
         run_type="llm",
         name="DeepSeek Chat Completion",
         metadata={"ls_provider": "deepseek", "ls_model_name": "deepseek-chat"},
     )
     def call_deepseek(messages: list[dict]):
         response = client.chat.completions.create(
             model="deepseek-chat",
             messages=messages
         )
         return response.choices[0].message

     if __name__ == "__main__":
         messages = [
             {"role": "system", "content": "You are a helpful assistant that translates English to French."},
             {"role": "user", "content": "I love programming."}
         ]
         result = call_deepseek(messages=messages)
         print("Model reply:", result.content)
     ```

     ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
     import { config } from "dotenv";
     import OpenAI from "openai";
     import { traceable } from "langsmith/traceable";

     config(); // Load env vars from .env

     const openai = new OpenAI({
     apiKey: process.env.DEEPSEEK_API_KEY,
     baseURL: "https://api.deepseek.com/v1"
     });

     type ChatMessage = {
     role: "system" | "user" | "assistant";
     content: string;
     };

     const callDeepSeek = traceable(
     async (messages: ChatMessage[]) => {
         const response = await openai.chat.completions.create({
         model: "deepseek-chat",
         messages
         });

         return response.choices[0].message;
     },
     {
         name: "DeepSeek Chat Completion",
         run_type: "llm",
         metadata: {
         ls_provider: "deepseek",
         ls_model_name: "deepseek-chat"
         }
     }
     );

     (async () => {
     const messages: ChatMessage[] = [
         {
         role: "system",
         content: "You are a helpful assistant that translates English to French."
         },
         {
         role: "user",
         content: "I love programming."
         }
     ];

     const result = await callDeepSeek(messages);
     console.log("Model reply:", result.content);
     })();

     ```
   </CodeGroup>

   In this example, you use the OpenAI SDK to interact with [DeepSeek's API](https://api-docs.deepseek.com/). The OpenAI client is configured with `base_url="https://api.deepseek.com/v1"` to route requests to DeepSeek's endpoint while maintaining OpenAI-compatible syntax.

   The `@traceable` decorator (Python) or `traceable` function (TypeScript) wraps your function so that each invocation is logged as a trace run of type `"llm"`. The `metadata` parameter tags the trace with:

   * `ls_provider`: Identifies the provider (DeepSeek) for filtering traces.
   * `ls_model_name`: Specifies the model used for cost tracking and analytics.

   The function returns the full message object (`response.choices[0].message`), which includes the response content along with metadata like the role and any additional fields. LangSmith automatically captures:

   * Input messages sent to the model.
   * The model's complete response (content, role, etc.).
   * Model name and token usage statistics.
   * Execution timing and any errors.

2. Execute your script to generate a trace:

   <CodeGroup>
     ```bash Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
     python deepseek_trace.py
     ```

     ```bash TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
     node deepseek_trace.js
     ```
   </CodeGroup>

   The function call will reach out to DeepSeek's API, and because of the `@traceable`/`traceable` wrapper, LangSmith will log this call's inputs and outputs as a new trace. You'll find the model's response printed to the console, and a corresponding run appear in the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-trace-deepseek).

## View traces in LangSmith

After running the example, you can inspect the recorded traces in the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-trace-deepseek):

1. Open the LangSmith UI and log in to your account.
2. Select the project you used for this integration (for example, the name set in `LANGSMITH_PROJECT`, or "default" if you didn't set one).
3. Find the trace corresponding to your DeepSeek API call. It will be identified by the function name (`DeepSeek Chat Completion`).
4. Click on the trace to open it. You'll be able to inspect the model input and output, including the prompt messages you sent and the response from DeepSeek, as well as timing information (latency) and token usage.

With LangSmith's tracing, you have full visibility into your DeepSeek calls—allowing you to debug the behavior of DeepSeek's models, monitor performance (response time and token usage), and compare runs with different parameters.

## Cost tracking

Although DeepSeek models are open-weight, using the hosted DeepSeek API may incur usage-based costs depending on your plan.

LangSmith can automatically associate costs with traced LLM calls by estimating token usage and applying model-specific pricing. When tracing DeepSeek API calls, LangSmith uses the recorded prompt and response messages to calculate token counts and attach cost information to each run.

To enable automatic cost tracking for LLM calls, refer to [Automatically track costs based on token counts](/langsmith/cost-tracking#llm-calls:-automatically-track-costs-based-on-token-counts).

Once enabled, costs appear directly in the LangSmith UI alongside each traced DeepSeek run, allowing you to monitor usage and compare experiments over time.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-deepseek.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
