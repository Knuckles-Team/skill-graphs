# LangSmith MCP Server
Source: https://docs.langchain.com/langsmith/langsmith-mcp-server

Use the Model Context Protocol (MCP) server to let language models fetch conversation history, prompts, runs, datasets, experiments, and billing from LangSmith.

<Warning>
  **Deprecated—use the [LangSmith Remote MCP](/langsmith/langsmith-remote-mcp) instead.**

  LangSmith now hosts an OAuth-authenticated remote MCP server on LangSmith Cloud and on [self-hosted LangSmith](/langsmith/self-hosted) v0.15 or later. Cloud endpoints:

  <table>
    <thead>
      <tr>
        <th>Region</th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <td>GCP US</td>
      </tr>

      <tr>
        <td>GCP EU</td>
      </tr>

      <tr>
        <td>GCP APAC</td>
      </tr>

      <tr>
        <td>AWS US</td>
      </tr>
    </tbody>
  </table>

  Self-hosted endpoint: `https://<your-langsmith-host>/api/mcp`.

  It exposes the same tool surface as the standalone server documented on this page, but authenticates via OAuth 2.1 with dynamic client registration—no API key, no separate deployment, no header configuration.

  The standalone server documented below remains the supported path for self-hosted deployments on versions earlier than v0.15 and for users who prefer running the server themselves.
</Warning>

The LangSmith MCP Server is a [Model Context Protocol](https://modelcontextprotocol.io/introduction) (MCP) server that integrates with [LangSmith](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-langsmith-mcp-server). It lets MCP-compatible clients (for example, AI coding assistants) read [conversation history](/langsmith/observability-concepts#threads), [prompts](/langsmith/manage-prompts-programmatically), [runs and traces](/langsmith/observability-concepts#runs), [datasets](/langsmith/evaluation-concepts#datasets), [experiments](/langsmith/evaluation-concepts#experiment), and billing usage from your LangSmith workspace.

## Example use cases

* **Conversation history**: "Fetch the history of my conversation from thread 'thread-123' in project 'my-chatbot'"
* **Prompt management**: "Get all public prompts" or "Pull the template for the 'legal-case-summarizer' prompt"
* **Traces and runs**: "Fetch the latest 10 root runs from project 'alpha'" or "Get all runs for a trace by UUID"
* **Datasets**: "List datasets of type chat" or "Read examples from dataset 'customer-support-qa'"
* **Experiments**: "List experiments for dataset 'my-eval-set' with latency and cost metrics"
* **Billing**: "Get billing usage for September 2025"

<Tip>
  **Use the server in code or Fleet**

  * To connect and use remote MCP servers (including this one) in your Python application, see [MCP (Model Context Protocol)](/oss/python/langchain/mcp).
  * To connect and use this server in Fleet, see [Remote MCP servers](/langsmith/fleet/remote-mcp-servers).
</Tip>

## Quickstart (hosted)

A hosted version of the LangSmith MCP Server is available over HTTP, so you can connect without running the server yourself.

* **URL:** `https://langsmith-mcp-server.onrender.com/mcp`
* **Authentication:** Send your [LangSmith API key](/langsmith/create-account-api-key) in the `LANGSMITH-API-KEY` header.

<Note>
  The hosted instance is for [LangSmith Cloud](/langsmith/deploy-to-cloud). For a [self-hosted LangSmith](/langsmith/self-hosted) instance, run the server yourself and point it at your endpoint (see [Docker deployment](#docker-deployment-http-streamable)).
</Note>

**Example (Cursor `mcp.json`):**

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "mcpServers": {
    "LangSmith MCP (Hosted)": {
      "url": "https://langsmith-mcp-server.onrender.com/mcp",
      "headers": {
        "LANGSMITH-API-KEY": "lsv2_pt_your_api_key_here"
      }
    }
  }
}
```

Optional headers: `LANGSMITH-WORKSPACE-ID`, `LANGSMITH-ENDPOINT` (same as in [Environment variables](#environment-variables)).

## Available tools

### Conversation and threads

| Tool                 | Description                                                                                                                                                                                                             |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `get_thread_history` | Get message history for a conversation thread. Uses character-based pagination: pass `page_number` (1-based) and use the returned `total_pages` to request more pages. Optional: `max_chars_per_page`, `preview_chars`. |

### Prompt management

| Tool                 | Description                                                                    |
| -------------------- | ------------------------------------------------------------------------------ |
| `list_prompts`       | List prompts with optional filtering by visibility (public/private) and limit. |
| `get_prompt_by_name` | Get a single prompt by exact name (details and template).                      |
| `push_prompt`        | Documentation-only: how to create and push prompts to LangSmith.               |

### Traces and runs

| Tool            | Description                                                                                                                                                                                                                                                                                                                  |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `fetch_runs`    | Fetch runs (traces, tools, chains, etc.) from one or more projects. Supports filters (`run_type`, `error`, `is_root`), FQL (`filter`, `trace_filter`, `tree_filter`), and ordering. When `trace_id` is set, results are character-based paginated; otherwise one batch up to `limit`. Always pass `limit` and `page_number`. |
| `list_projects` | List projects with optional filtering by name, dataset, and detail level.                                                                                                                                                                                                                                                    |

### Datasets and examples

| Tool              | Description                                                                                                                      |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `list_datasets`   | List datasets with filtering by ID, type, name, or metadata.                                                                     |
| `list_examples`   | List examples from a dataset by dataset ID/name or example IDs; supports filter, metadata, splits, and optional `as_of` version. |
| `read_dataset`    | Read one dataset by ID or name.                                                                                                  |
| `read_example`    | Read one example by ID, with optional `as_of` version.                                                                           |
| `create_dataset`  | Documentation-only: how to create datasets.                                                                                      |
| `update_examples` | Documentation-only: how to update dataset examples.                                                                              |

### Experiments and evaluations

| Tool               | Description                                                                                                                                                 |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `list_experiments` | List experiment (reference) projects for a dataset. Requires `reference_dataset_id` or `reference_dataset_name`. Returns metrics (latency, cost, feedback). |
| `run_experiment`   | Documentation-only: how to run experiments and evaluations.                                                                                                 |

### Billing

| Tool                | Description                                                                                     |
| ------------------- | ----------------------------------------------------------------------------------------------- |
| `get_billing_usage` | Get organization billing usage (e.g. trace counts) for a date range. Optional workspace filter. |

### Pagination (character-based)

Tools that return large payloads use **character-budget pagination** so responses stay within a size limit:

* **Used by:** `get_thread_history` and `fetch_runs` (when `trace_id` is set).
* **Parameters:** Send `page_number` (1-based) on each request. Optional: `max_chars_per_page` (default 25000, max 30000), `preview_chars` (truncate long strings with "... (+N chars)").
* **Response:** Includes `page_number`, `total_pages`, and the page payload. Request more by calling again with `page_number = 2`, then `3`, up to `total_pages`.
* **Benefits:** Pages are built by character count, not item count; no cursor or server-side state—just page numbers.

## Installation (run locally)

If you prefer to run the server locally (or use a self-hosted LangSmith endpoint), install it and configure your MCP client.

### Prerequisites

1. Install [uv](https://github.com/astral-sh/uv) (Python package installer):
   ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. Install the package:
   ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
   uv run pip install --upgrade langsmith-mcp-server
   ```

### MCP client configuration

Add the server to your MCP client config. Use the path from `which uvx` for the `command` value.

**PyPI / uvx:**

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "mcpServers": {
    "LangSmith API MCP Server": {
      "command": "/path/to/uvx",
      "args": ["langsmith-mcp-server"],
      "env": {
        "LANGSMITH_API_KEY": "your_langsmith_api_key",
        "LANGSMITH_WORKSPACE_ID": "your_workspace_id",
        "LANGSMITH_ENDPOINT": "https://api.smith.langchain.com"
      }
    }
  }
}
```

**From source** (clone [langsmith-mcp-server](https://github.com/langchain-ai/langsmith-mcp-server) first):

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "mcpServers": {
    "LangSmith API MCP Server": {
      "command": "/path/to/uv",
      "args": [
        "--directory",
        "/path/to/langsmith-mcp-server",
        "run",
        "langsmith_mcp_server/server.py"
      ],
      "env": {
        "LANGSMITH_API_KEY": "your_langsmith_api_key",
        "LANGSMITH_WORKSPACE_ID": "your_workspace_id",
        "LANGSMITH_ENDPOINT": "https://api.smith.langchain.com"
      }
    }
  }
}
```

Replace `/path/to/uv`, `/path/to/uvx`, and `/path/to/langsmith-mcp-server` with your actual paths.

## Docker deployment (HTTP-streamable)

You can run the server as an HTTP service with Docker so clients connect via the HTTP-streamable protocol.

1. Build and run:
   ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
   docker build -t langsmith-mcp-server .
   docker run -p 8000:8000 langsmith-mcp-server
   ```
   Use the [langsmith-mcp-server](https://github.com/langchain-ai/langsmith-mcp-server) repository for the Dockerfile and context.

2. Connect your MCP client to `http://localhost:8000/mcp` with the `LANGSMITH-API-KEY` header (and optional `LANGSMITH-WORKSPACE-ID`, `LANGSMITH-ENDPOINT`).

3. Health check (no auth):
   ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
   curl http://localhost:8000/health
   ```

For full Docker and HTTP-streamable details, see the [LangSmith MCP Server repository](https://github.com/langchain-ai/langsmith-mcp-server).

## Deployment overview

Use the **hosted** MCP server to connect to [LangSmith Cloud](/langsmith/cloud) (`smith.langchain.com`, `eu.smith.langchain.com`, `apac.smith.langchain.com`, or `aws.smith.langchain.com`). To connect to Cloud or [self-hosted LangSmith](/langsmith/self-hosted), run the server [locally](#installation-run-locally) and set `LANGSMITH_ENDPOINT`. For self-hosted deployments, you can also run the server via the [Docker image](#docker-deployment-http-streamable) inside your VPC.

```mermaid actions={false} theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
flowchart LR
  subgraph Client["MCP client"]
    C[Cursor / Claude Code / etc.]
  end

  subgraph CloudPath["Cloud"]
    H[Hosted MCP server]
    LSCloud[LangSmith Cloud]
  end

  subgraph LocalPath["Local"]
    LocalServer[Local MCP server]
  end

  subgraph SelfHostedPath["Self-hosted"]
    D[Docker MCP server]
    LSSelf[Self-hosted LangSmith]
  end

  C --> H
  H --> LSCloud
  C --> LocalServer
  LocalServer --> LSCloud
  LocalServer --> LSSelf
  C --> D
  D --> LSSelf
```

## Environment variables

| Variable                 | Required | Description                                                                                                                 |
| ------------------------ | -------- | --------------------------------------------------------------------------------------------------------------------------- |
| `LANGSMITH_API_KEY`      | Yes      | Your [LangSmith API key](/langsmith/create-account-api-key) for authentication.                                             |
| `LANGSMITH_WORKSPACE_ID` | No       | Workspace ID when your API key has access to multiple workspaces.                                                           |
| `LANGSMITH_ENDPOINT`     | No       | API endpoint URL (for [self-hosted](/langsmith/self-hosted) or custom regions). Default: `https://api.smith.langchain.com`. |

For the **hosted** server, use the same names as **headers**: `LANGSMITH-API-KEY`, `LANGSMITH-WORKSPACE-ID`, `LANGSMITH-ENDPOINT`.

## TypeScript implementation

A community-maintained TypeScript/Node.js port of the official Python server is available. To run it: `LANGSMITH_API_KEY=your-key npx langsmith-mcp-server`.

Source and package: [GitHub](https://github.com/amitrechavia/langsmith-mcp-server-js) · [npm](https://www.npmjs.com/package/langsmith-mcp-server). Maintained by [amitrechavia](https://github.com/amitrechavia).

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/langsmith-mcp-server.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# LangSmith Remote MCP
Source: https://docs.langchain.com/langsmith/langsmith-remote-mcp

Connect MCP-compatible clients to LangSmith over OAuth, no API key or header configuration required.

The LangSmith Remote MCP is a [Model Context Protocol](https://modelcontextprotocol.io/introduction) (MCP) server hosted by LangSmith. It exposes the same tools as the [standalone LangSmith MCP Server](/langsmith/langsmith-mcp-server) (conversation history, prompts, runs and traces, datasets, experiments, billing) but with OAuth-based authentication, so MCP-compatible clients connect directly without an API key, a separate deployment, or any header configuration.

The Remote MCP is available on all LangSmith Cloud regions and on [self-hosted LangSmith](/langsmith/self-hosted) deployments running v0.15 or later. Self-hosted deployments on earlier versions should continue to use the [standalone LangSmith MCP Server](/langsmith/langsmith-mcp-server).

## Endpoints

**LangSmith Cloud:**

<table>
  <thead>
    <tr>
      <th>Region</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>GCP US</td>
    </tr>

    <tr>
      <td>GCP EU</td>
    </tr>

    <tr>
      <td>GCP APAC</td>
    </tr>

    <tr>
      <td>AWS US</td>
    </tr>
  </tbody>
</table>

The server discovers the rest of its OAuth metadata via [RFC 8414](https://datatracker.ietf.org/doc/html/rfc8414) at `/.well-known/oauth-authorization-server` on the same host, so a compliant MCP client only needs the URL above.

**Self-hosted LangSmith:**

`https://<your-langsmith-host>/api/mcp`, where `<your-langsmith-host>` is the hostname of your LangSmith instance.

## Authentication

Authentication uses OAuth 2.1 with [Dynamic Client Registration (RFC 7591)](https://datatracker.ietf.org/doc/html/rfc7591). Compatible MCP clients register themselves automatically on first use—there is no client ID to provision and no API key to manage.

After registration:

1. The client opens an authorization URL in your browser.
2. You log in to LangSmith (or use an existing session) and consent.
3. The client receives an access token and refresh token.
4. The access token is automatically refreshed by the client when it expires.

The session is scoped to your LangSmith user and workspace permissions—calls through the MCP server can only view what your account is permitted to view.

## Quickstart

### Claude Code

Add the server to your project's `.mcp.json` (or run `claude mcp add --transport http -s user langsmith https://api.smith.langchain.com/mcp` to install it user-wide):

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "mcpServers": {
    "langsmith": {
      "type": "http",
      "url": "https://api.smith.langchain.com/mcp"
    }
  }
}
```

Then run `/mcp` and select **langsmith** to complete the OAuth flow. Tools become available as `mcp__langsmith__<tool_name>`.

### Deep Agents Code (`dcode`)

Add the server to your user-level `~/.deepagents/.mcp.json` file to make it available in every Deep Agents Code project, or add it to a project-level `.mcp.json` file for only that project. See the [Deep Agents Code MCP tools docs](/oss/python/deepagents/code/mcp-tools) for discovery locations and precedence rules.

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "mcpServers": {
    "langsmith": {
      "url": "https://api.smith.langchain.com/mcp",
      "transport": "http",
      "auth": "oauth"
    }
  }
}
```

Then complete the OAuth login flow in one of two ways:

* In the Deep Agents Code TUI, run `/mcp`, select **langsmith**, and follow the login prompt.
* From your shell, run:

  ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  dcode mcp login langsmith
  ```

Launch `dcode`, or restart an active session, to load the LangSmith MCP tools. In an interactive session, run `/mcp` to inspect server status and loaded tools.

### Cursor

Add to your Cursor `mcp.json`:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "mcpServers": {
    "LangSmith": {
      "url": "https://api.smith.langchain.com/mcp"
    }
  }
}
```

Cursor will prompt you to complete the OAuth flow on first use.

### Other clients

Any MCP client supporting the [Streamable HTTP transport](https://spec.modelcontextprotocol.io/specification/2025-03-26/basic/transports/#streamable-http) and OAuth 2.1 with dynamic client registration can connect with just the URL above.

## Known client incompatibilities

<Note>
  **OpenAI Codex CLI** does not work with the LangSmith Remote MCP. Codex omits the [RFC 8707](https://datatracker.ietf.org/doc/html/rfc8707) `resource` parameter required by the [MCP authorization spec](https://modelcontextprotocol.io/specification/draft/basic/authorization) during the OAuth flow, so login appears to succeed but the issued token is not bound to the LangSmith MCP and `initialize` fails with an auth-required error. Two upstream issues affect token exchange and authorize requests in Codex (refer to [openai/codex#20729](https://github.com/openai/codex/issues/20729) and [openai/codex#13891](https://github.com/openai/codex/issues/13891)). In the meantime, use the [LangSmith CLI](vscode-webview://10gvgke5c00vonuvk2psr9q89hcqv6q2583jm92ucepld5716i57/langsmith/langsmith-cli) from Codex—it supports the same projects, traces, runs, datasets, experiments, and threads as the MCP server, with native OAuth login.
</Note>

## Available tools

The Remote MCP exposes the same tool surface as the [standalone server](/langsmith/langsmith-mcp-server#available-tools):

* **Conversation and threads:** `get_thread_history`
* **Prompt management:** `list_prompts`, `get_prompt_by_name`, `push_prompt`
* **Traces and runs:** `fetch_runs`, `list_projects`
* **Datasets and examples:** `list_datasets`, `list_examples`, `read_dataset`, `read_example`, `create_dataset`, `update_examples`
* **Experiments and evaluations:** `list_experiments`, `run_experiment`
* **Billing:** `get_billing_usage`

See the [standalone server reference](/langsmith/langsmith-mcp-server#available-tools) for parameter and pagination details—both servers share the same tool implementations.

## Re-authenticating

If a client loses its session (for example, after revoking access in your LangSmith account, or if the refresh token is invalidated), trigger re-auth from the client:

* **Claude Code:** run `/mcp`, select **langsmith**, choose re-authenticate.
* **Cursor:** disable and re-enable the server in MCP settings.
* **Other clients:** consult the client's MCP settings UI.

## Self-hosted LangSmith

[Self-hosted LangSmith](/langsmith/self-hosted) deployments on v0.15 or later expose the Remote MCP at `https://<your-langsmith-host>/api/mcp`. Configuration, authentication, and tool surface are identical to LangSmith Cloud.

For deployments on earlier versions, run the [standalone LangSmith MCP Server](/langsmith/langsmith-mcp-server) in your own environment and point its `LANGSMITH_ENDPOINT` at your self-hosted instance.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/langsmith-remote-mcp.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# How to define an LLM-as-a-judge evaluator
Source: https://docs.langchain.com/langsmith/llm-as-judge

LLM applications can be challenging to evaluate since they often generate conversational text with no single correct answer.

This guide shows you how to define an [LLM-as-a-judge evaluator](/langsmith/evaluation-concepts#llm-as-judge) for [offline evaluation](/langsmith/evaluation-concepts#offline-evaluations) using the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-llm-as-judge).

<Note>
  To run evaluations in real-time on your production traces, refer to [setting up online evaluations](/langsmith/online-evaluations-llm-as-judge).
</Note>

<Tip>
  If your dataset examples were built with [assertions written in an annotation queue](/langsmith/assertions), an LLM-as-a-judge evaluator can read `example.outputs["assertions"]` and grade each one against your application's output.
</Tip>

## Step 1. Create the evaluator

1. In the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-llm-as-judge), click **+ Evaluator** from the [Evaluators](/langsmith/evaluators) page, or from the **Evaluators** tab within a dataset or tracing project.
2. In the **Add Evaluator** panel, select **LLM-as-a-Judge Evaluator** under **Create from scratch**. Alternatively, select **Create from a template** to start from a ready-made evaluator and edit it.

### Evaluator templates

Evaluator templates are a useful starting point when setting up evaluations. Select **Create from a template** in the **Add Evaluator** panel to browse templates organized by category, such as Security, Safety, and Quality.

You can configure an LLM-as-a-Judge evaluator:

* From the [Evaluators](/langsmith/evaluators) page
* As part of a dataset to [automatically run evaluations on experiments](/langsmith/bind-evaluator-to-dataset)
* When running an [online evaluation](/langsmith/online-evaluations-llm-as-judge)

### Customize your LLM-as-a-judge evaluator

Add specific instructions for your LLM-as-a-judge evaluator prompt and configure which parts of the input/output/reference output should be passed to the evaluator.

## Step 2. Configure the evaluator

### Prompt

Create a new prompt, or choose an existing prompt from the [prompt hub](/langsmith/prompt-engineering-quickstart).

* **Create your own prompt**: Create a custom prompt inline.

* **Pull a prompt from the prompt hub**: Use the **Select a prompt** dropdown to select from an existing prompt. You can't edit these prompts directly within the prompt editor, but you can view the prompt and the schema it uses. To make changes, edit the prompt in the Playground and commit the version, and then pull in your new prompt in the evaluator.

### Model

Select the desired model from the provided options.

### Mapping variables

Use variable mapping to indicate the variables that are passed into your evaluator prompt from your run or example. To aid with variable mapping, an example (or run) is provided for reference. Click on the variables in your prompt and use the dropdown to map them to the relevant parts of the input, output, or reference output.

To add prompt variables type the variable with double curly brackets `{{prompt_var}}` if using mustache formatting (the default) or single curly brackets `{prompt_var}` if using f-string formatting.

You may remove variables as needed. For example if you are evaluating a metric such as conciseness, you typically don't need a reference output so you may remove that variable.

### Preview

Previewing the prompt will show you of what the formatted prompt will look like using the reference run and dataset example shown on the right.

### Improve your evaluator with few-shot examples

To better align the LLM-as-a-judge evaluator to human preferences, LangSmith allows you to collect [human corrections](/langsmith/create-few-shot-evaluators#make-corrections) on evaluator scores. With this selection enabled, corrections are then inserted automatically as few-shot examples into your prompt.

Learn [how to set up few-shot examples and make corrections](/langsmith/create-few-shot-evaluators).

### Feedback configuration

Feedback configuration is the scoring criteria that your LLM-as-a-judge evaluator will use. Think of this as the rubric that your evaluator will grade based on. Scores will be added as [feedback](/langsmith/observability-concepts#feedback) to a run or example. Defining feedback for your evaluator:

1. **Name the feedback key**: This is the name that will appear when viewing evaluation results. Names should be unique across experiments.

2. **Add a description**: Describe what the feedback represents.

3. **Choose a feedback type**:

   * **Boolean**: True/false feedback.
   * **Categorical**: Select from predefined categories.
   * **Continuous**: Numerical scoring within a specified range.

Behind the scenes, feedback configuration is added as [structured output](/oss/python/langchain/structured-output) to the LLM-as-a-judge prompt. If you're using an existing prompt from the hub, you must add an output schema to the prompt before configuring an evaluator to use it. Each top-level key in the output schema will be treated as a separate piece of feedback.

## Step 3. Save the evaluator

Once you are finished configuring, save your changes.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/llm-as-judge.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# How to define an LLM-as-a-judge evaluator
Source: https://docs.langchain.com/langsmith/llm-as-judge-sdk

LLM applications can be challenging to evaluate since they often generate conversational text with no single correct answer.

This guide shows you how to define an [LLM-as-a-judge evaluator](/langsmith/evaluation-concepts#llm-as-judge) for [offline evaluation](/langsmith/evaluation-concepts#offline-evaluations) using the [LangSmith SDK](https://reference.langchain.com/python/langsmith/observability/sdk).

<Tip>
  For a quick start, use [openevals](/langsmith/openevals), which provides ready-to-use LLM-as-a-judge evaluators.
</Tip>

## Create your own LLM-as-a-judge evaluator

For complete control of evaluator logic, create your own LLM-as-a-judge evaluator and run it using the LangSmith SDK ([Python](https://docs.smith.langchain.com/reference/python/reference) / [TypeScript](https://docs.smith.langchain.com/reference/js)).

Requires `langsmith>=0.2.0`

An LLM-as-a-judge evaluator consists of three key components:

1. **Evaluator function**: A function that receives the example inputs and application outputs, then uses an LLM to score the quality. The function should return a boolean, number, string, or dictionary with score information.
2. **Target function**: Your application logic being evaluated (wrapped with [`@traceable`](https://reference.langchain.com/python/langsmith/run_helpers/traceable) for observability).
3. **Dataset and evaluation**: A dataset of test examples and the `evaluate()` function that runs your target function on each example and applies your evaluators.

### Example

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langsmith import evaluate, traceable, wrappers, Client
from openai import OpenAI
from pydantic import BaseModel

# Wrap the OpenAI client to automatically trace all LLM calls
oai_client = wrappers.wrap_openai(OpenAI())

# 1. Define your evaluator function

# This function receives the inputs and outputs from each test example
def valid_reasoning(inputs: dict, outputs: dict) -> bool:
    """Use an LLM to judge if the reasoning and the answer are consistent."""
    # Define the evaluation criteria
    instructions = """
Given the following question, answer, and reasoning, determine if the reasoning
for the answer is logically valid and consistent with the question and the answer."""

    # Use structured output to get a boolean score
    class Response(BaseModel):
        reasoning_is_valid: bool

    # Construct the prompt with the actual inputs and outputs
    msg = f"Question: {inputs['question']}\nAnswer: {outputs['answer']}\nReasoning: {outputs['reasoning']}"

    # Call the LLM to judge the output
    response = oai_client.beta.chat.completions.parse(
        model="gpt-4o",
        messages=[{"role": "system", "content": instructions}, {"role": "user", "content": msg}],
        response_format=Response
    )

    # Return the boolean score
    return response.choices[0].message.parsed.reasoning_is_valid

# 2. Define your target function (the application being evaluated)

# The @traceable decorator logs traces to LangSmith for debugging
@traceable
def dummy_app(inputs: dict) -> dict:
    return {"answer": "hmm i'm not sure", "reasoning": "i didn't understand the question"}

# 3. Create a dataset with test examples
ls_client = Client()
dataset = ls_client.create_dataset("big questions")
examples = [
    {"inputs": {"question": "how will the universe end"}},
    {"inputs": {"question": "are we alone"}},
]
ls_client.create_examples(dataset_id=dataset.id, examples=examples)

# 4. Run the evaluation

# This runs dummy_app on each example and applies the valid_reasoning evaluator
results = evaluate(
    dummy_app,              # Your application function
    data=dataset,           # Dataset to evaluate on
    evaluators=[valid_reasoning]  # List of evaluator functions
)
```

For more information on how to write a custom evaluator, refer to [How to define a code evaluator (SDK)](/langsmith/code-evaluator-sdk).

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/llm-as-judge-sdk.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
