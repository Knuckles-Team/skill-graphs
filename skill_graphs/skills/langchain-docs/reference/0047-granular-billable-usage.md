# Granular billable usage
Source: https://docs.langchain.com/langsmith/granular-usage

Retrieve detailed trace and LangSmith Deployment usage data broken down by workspace, project, user, or API key.

<Note>
  **Trace usage:** For LangSmith Cloud, granular billable trace data collection started on January 5, 2026. Data is not available for traces ingested before this date.

  For self-hosted instances, trace data collection begins when the feature is enabled via the following environment variables, or after [upgrading to a version with it enabled by default](/langsmith/self-hosted-changelog#langsmith-0-13-12).

  ```env theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  DEFAULT_ORG_FEATURE_ENABLE_GRANULAR_USAGE_REPORTING=true
  GRANULAR_USAGE_TABLE_ENABLED=true
  ```

  **LangSmith Deployment usage** uses a separate data source. For more details, refer to the [LangSmith Deployment section](/langsmith/granular-usage#langsmith-deployment-usage-kind%3Dlangsmith_deployments).
</Note>

LangSmith provides granular billable usage APIs that let you retrieve detailed usage data broken down by workspace, project, user, or API key. Two billable domains are supported by the same endpoint, selected via a `kind` query parameter:

* **Trace usage** (`kind=traces`, default): number of traces ingested.
* **LangSmith Deployment usage** (`kind=langsmith_deployments`): nodes executed, agent runs, and agent uptime for [LangSmith Deployment](/langsmith/billing).

Both kinds share the same query parameters (time range, workspace filter, grouping dimension) and return the same time-bucketed shape. The data sources are separate, so a record returned by one kind will not appear in the other.

These APIs enable you to:

* Track usage across different teams or workspaces
* Identify which users or API keys are consuming the most traces or running the most agents
* Analyze usage patterns over time
* Export usage data for internal reporting

## Prerequisites

* You must have the [`organization:read` permission](/langsmith/organization-workspace-operations) to access granular usage data.
* You can only view usage for workspaces you have read access to.

## View in the UI

You can also view granular usage data in the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-granular-usage):

1. Navigate to **Settings** > **Billing and Usage**
2. Select the **Granular Usage** tab
3. Switch between the **LangSmith Traces** and **LangSmith Deployments** sub-tabs to view each domain. The active sub-tab is reflected in the URL (`?tab=traces` or `?tab=deployments`) so you can bookmark the page to land on the same view.
4. Use the controls to:
   * Select a time range (Last 7 days, 30 days, 3 months, 6 months, 1 year, or custom)
   * Group by workspace, project, user, or API key
   * Filter to specific workspaces
   * On the **LangSmith Traces** tab, optionally filter by retention tier (`All Retention` / `Long-lived only` / `Short-lived only`)
5. Click **Export CSV** to download the data for the active tab.

Time range and workspace filters are shared across both sub-tabs, switching tabs preserves what you've selected. The **LangSmith Deployments** tab shows three stat cards (Total Nodes Executed / Total Agent Runs / Total Agent Uptime (seconds)) and one chart per metric stacked vertically, since the three metrics use different units.

## Query parameters

The granular usage endpoint accepts the following query parameters:

| Parameter       | Type           | Required | Description                                                                                                                  |
| --------------- | -------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `start_time`    | datetime       | Yes      | Start of the time range (ISO 8601 format).                                                                                   |
| `end_time`      | datetime       | Yes      | End of the time range. Must be after `start_time`.                                                                           |
| `workspace_ids` | array of UUIDs | Yes      | Filter results to specific workspaces.                                                                                       |
| `kind`          | string         | No       | `traces` (default) or `langsmith_deployments`. Selects the billable domain.                                                  |
| `group_by`      | string         | No       | Dimension to group by. One of: `workspace`, `project`, `user`, `api_key`. Default: `workspace`.                              |
| `trace_tier`    | string         | No       | Trace-only retention filter: `longlived` or `shortlived`. Omit for all retention. Ignored when `kind=langsmith_deployments`. |

### Day-granular contract

Usage data is aggregated at day granularity. The endpoint normalizes the window to whole days at the API layer:

* `start_time` is rounded down to its day's UTC midnight.
* `end_time` is rounded up to the next UTC midnight (no-op when already at midnight).
* Any day overlapping the requested window is included in full.

A 24-hour window from `2026-01-01T12:00:00Z` to `2026-01-02T12:00:00Z` therefore returns usage for the full Jan 1 and Jan 2 buckets.

### Stride

The `stride` field in each response indicates the time bucket size used for aggregation, calculated from the requested time range. Daily is the minimum. Sub-day windows still bucket at one day.

| Time range              | Aggregation | Stride      |
| ----------------------- | ----------- | ----------- |
| Up to 31 days           | Daily       | `days: 1`   |
| 32–93 days (\~3 months) | Weekly      | `days: 7`   |
| 94–366 days (\~1 year)  | Monthly     | `days: 30`  |
| More than 366 days      | Yearly      | `days: 365` |

### Compatibility

`kind=langsmith_deployments` combined with `group_by=trace_tier` returns `400 Bad Request`. Retention tiers only apply to traces.

## API endpoint

```
GET /api/v1/orgs/current/billing/granular-usage
```

Existing callers that omit `kind` continue to get trace usage with the same response shape they always did.

### Trace usage (`kind=traces`)

#### Response

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "stride": {
    "days": 1,
    "hours": 0
  },
  "usage": [
    {
      "time_bucket": "2026-01-15T00:00:00Z",
      "dimensions": {
        "workspace_id": "uuid",
        "workspace_name": "My Workspace"
      },
      "traces": 1500
    }
  ]
}
```

#### Example: Get trace usage by workspace

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import httpx
  from datetime import datetime, timedelta, timezone

  client = httpx.Client(
      base_url="https://api.smith.langchain.com",
      headers={"x-api-key": "<your-api-key>"}
  )

  end_time = datetime.now(timezone.utc)
  start_time = end_time - timedelta(days=30)

  response = client.get(
      "/api/v1/orgs/current/billing/granular-usage",
      params={
          "start_time": start_time.isoformat(),
          "end_time": end_time.isoformat(),
          "workspace_ids": ["<workspace-id>"],
          "group_by": "workspace",
      },
  )

  data = response.json()
  for record in data["usage"]:
      print(f"{record['time_bucket']}: {record['traces']} traces")
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  const response = await fetch(
    `https://api.smith.langchain.com/api/v1/orgs/current/billing/granular-usage?` +
    new URLSearchParams({
      start_time: new Date(Date.now() - 30 * 24 * 60 * 60 * 1000).toISOString(),
      end_time: new Date().toISOString(),
      workspace_ids: "<workspace-id>",
      group_by: "workspace",
    }),
    {
      headers: {
        "x-api-key": "<your-api-key>",
      },
    }
  );

  const data = await response.json();
  for (const record of data.usage) {
    console.log(`${record.time_bucket}: ${record.traces} traces`);
  }
  ```

  ```bash cURL theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  curl -X GET "https://api.smith.langchain.com/api/v1/orgs/current/billing/granular-usage?\
  start_time=2026-01-01T00:00:00Z&\
  end_time=2026-01-15T00:00:00Z&\
  workspace_ids=<workspace-id>&\
  group_by=workspace" \
    -H "x-api-key: <your-api-key>"
  ```
</CodeGroup>

#### Example: Get trace usage by user, filtered to long-lived retention only

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  response = client.get(
      "/api/v1/orgs/current/billing/granular-usage",
      params={
          "start_time": start_time.isoformat(),
          "end_time": end_time.isoformat(),
          "workspace_ids": ["<workspace-id>"],
          "group_by": "user",
          "trace_tier": "longlived",
      },
  )

  data = response.json()
  for record in data["usage"]:
      user_email = record["dimensions"].get("user_email", "Unknown")
      print(f"{user_email}: {record['traces']} long-lived traces")
  ```
</CodeGroup>

### LangSmith Deployment usage (`kind=langsmith_deployments`)

Each record carries three metrics together so a single fetch powers the whole Deployment view.

<Note>
  **LangSmith Deployment usage** is sourced separately from trace usage and is available for the full retention window of your deployment usage.

  For self-hosted instances, the Deployment usage endpoint is opt-in. Enable it via:

  ```env theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  REMOTE_METRICS_ROLLUP_ENABLED=true
  ```

  Or upgrade to a LangSmith version that enables it by default (see [self-hosted changelog](/langsmith/self-hosted-changelog)).
</Note>

#### Response

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "stride": {
    "days": 1,
    "hours": 0
  },
  "usage": [
    {
      "time_bucket": "2026-01-15T00:00:00Z",
      "dimensions": {
        "workspace_id": "uuid",
        "workspace_name": "My Workspace"
      },
      "nodes_executed": 12500,
      "agent_runs": 320,
      "agent_uptime_seconds": 86400
    }
  ]
}
```

| Field                  | Description                                                                                                                                                                                                                             |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `nodes_executed`       | Total LangGraph nodes executed in the time bucket.                                                                                                                                                                                      |
| `agent_runs`           | Total agent runs (graph invocations) in the time bucket.                                                                                                                                                                                |
| `agent_uptime_seconds` | Total replica uptime, in seconds, summed across deployment replicas. The deduplicated standby minutes used for invoicing is computed separately by the billing pipeline; this field is the raw sum surfaced for breakdown and analysis. |

#### Example: Get Deployment usage by workspace

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  response = client.get(
      "/api/v1/orgs/current/billing/granular-usage",
      params={
          "kind": "langsmith_deployments",
          "start_time": start_time.isoformat(),
          "end_time": end_time.isoformat(),
          "workspace_ids": ["<workspace-id>"],
          "group_by": "workspace",
      },
  )

  data = response.json()
  for record in data["usage"]:
      print(
          f"{record['time_bucket']}: "
          f"{record['nodes_executed']} nodes, "
          f"{record['agent_runs']} runs, "
          f"{record['agent_uptime_seconds']}s uptime"
      )
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  const response = await fetch(
    `https://api.smith.langchain.com/api/v1/orgs/current/billing/granular-usage?` +
    new URLSearchParams({
      kind: "langsmith_deployments",
      start_time: new Date(Date.now() - 30 * 24 * 60 * 60 * 1000).toISOString(),
      end_time: new Date().toISOString(),
      workspace_ids: "<workspace-id>",
      group_by: "workspace",
    }),
    {
      headers: {
        "x-api-key": "<your-api-key>",
      },
    }
  );

  const data = await response.json();
  for (const record of data.usage) {
    console.log(
      `${record.time_bucket}: ${record.nodes_executed} nodes, ` +
      `${record.agent_runs} runs, ${record.agent_uptime_seconds}s uptime`
    );
  }
  ```

  ```bash cURL theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  curl -X GET "https://api.smith.langchain.com/api/v1/orgs/current/billing/granular-usage?\
  kind=langsmith_deployments&\
  start_time=2026-01-01T00:00:00Z&\
  end_time=2026-01-15T00:00:00Z&\
  workspace_ids=<workspace-id>&\
  group_by=workspace" \
    -H "x-api-key: <your-api-key>"
  ```
</CodeGroup>

## CSV export

```
GET /api/v1/orgs/current/billing/granular-usage/export
```

Same query parameters as the data endpoint, including `kind`. Returns a CSV file with one row per (time bucket, dimension) tuple. All dimension columns are always present; only the columns matching the selected `group_by` are populated.

For `kind=traces`, the value column is `Traces`. For `kind=langsmith_deployments`, the value columns are `Nodes Executed`, `Agent Runs`, and `Agent Uptime (seconds)`.

| Column                                               | Present when                                 |
| ---------------------------------------------------- | -------------------------------------------- |
| Time Bucket Start                                    | Always                                       |
| Time Bucket End                                      | Always                                       |
| Workspace ID / Name                                  | Always (populated when `group_by=workspace`) |
| Project ID / Name                                    | Always (populated when `group_by=project`)   |
| User ID / Email                                      | Always (populated when `group_by=user`)      |
| API Key Short Key                                    | Always (populated when `group_by=api_key`)   |
| Traces                                               | `kind=traces`                                |
| Nodes Executed / Agent Runs / Agent Uptime (seconds) | `kind=langsmith_deployments`                 |

Cells whose value would start with `=`, `+`, `-`, `@`, tab, or carriage-return are tab-prefixed to neutralize spreadsheet formula evaluation in Excel / Google Sheets / LibreOffice.

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  response = client.get(
      "/api/v1/orgs/current/billing/granular-usage/export",
      params={
          "kind": "langsmith_deployments",
          "start_time": start_time.isoformat(),
          "end_time": end_time.isoformat(),
          "workspace_ids": ["<workspace-id>"],
          "group_by": "workspace",
      },
  )

  with open("deployment_usage_report.csv", "wb") as f:
      f.write(response.content)
  ```

  ```bash cURL theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  curl -X GET "https://api.smith.langchain.com/api/v1/orgs/current/billing/granular-usage/export?\
  kind=langsmith_deployments&\
  start_time=2026-01-01T00:00:00Z&\
  end_time=2026-01-15T00:00:00Z&\
  workspace_ids=<workspace-id>&\
  group_by=workspace" \
    -H "x-api-key: <your-api-key>" \
    -o deployment_usage_report.csv
  ```
</CodeGroup>

## Grouping options

The `group_by` parameter determines how usage data is aggregated:

| Value       | Description        | Dimensions returned              | Available for |
| ----------- | ------------------ | -------------------------------- | ------------- |
| `workspace` | Group by workspace | `workspace_id`, `workspace_name` | Both kinds    |
| `project`   | Group by project   | `project_id`, `project_name`     | Both kinds    |
| `user`      | Group by user      | `user_id`, `user_email`          | Both kinds    |
| `api_key`   | Group by API key   | `api_key_short_key`              | Both kinds    |

For trace usage, "project" refers to the [LangSmith tracer session](/langsmith/observability-concepts). For Deployment usage, "project" refers to the LangSmith Deployment project (a deployed agent).

## Related resources

* [Manage billing in your account](/langsmith/billing)
* [Organization and workspace operations](/langsmith/organization-workspace-operations)

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/granular-usage.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Rebuild graph at runtime
Source: https://docs.langchain.com/langsmith/graph-rebuild

Rebuild your graph with different configurations for each run using ServerRuntime.

You might need to rebuild your graph with a different configuration for a new run. For example, you might want to load different tools depending on the user's credentials. This guide shows how you can do this using `ServerRuntime`.

<Note>
  In most cases, customization is best handled by conditioning on the config within individual nodes rather than dynamically changing the whole graph structure. This makes it easier to test and manage.
</Note>

## Prerequisites

* Make sure to check out [this how-to guide](/langsmith/setup-app-requirements-txt) on setting up your app for deployment first.
* `ServerRuntime` requires `langgraph-api >= 0.7.31` and `langgraph-sdk >= 0.3.5`. Prior to that, graph factories only accepted a single `config: RunnableConfig` argument.

## Define graphs

Let's say you have an app with a simple graph that calls an LLM and returns the response to the user. The app file directory looks like the following:

```
my-app/
|-- langgraph.json
|-- my_project/
|   |-- __init__.py
|   |-- agents.py     # code for your graph
|-- pyproject.toml
```

where the graph is defined in `agents.py`.

### No rebuild

The most common way to deploy your Agent Server is to reference a compiled graph instance that's defined at the top level of your file. An example is below:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# my_project/agents.py
from langgraph.graph import StateGraph, MessagesState, START

async def model(state: MessagesState):
    return {"messages": [{"role": "assistant", "content": "Hi, there!"}]}

graph_workflow = StateGraph(MessagesState)
graph_workflow.add_node("model", model)
graph_workflow.add_edge(START, "model")
agent = graph_workflow.compile()
```

To make the server aware of your graph, you need to specify a path to the variable that contains the [`CompiledStateGraph`](https://reference.langchain.com/python/langgraph/graph/state/CompiledStateGraph) instance in your LangGraph API configuration (`langgraph.json`), e.g.:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
    "$schema": "https://langgra.ph/schema.json",
    "dependencies": ["."],
    "graphs": {
        "chat_agent": "my_project.agents:agent",
    }
}
```

### Rebuild

To rebuild your graph on each new run, provide a **factory function** that returns (or yields) a graph. The factory can optionally accept a `ServerRuntime` parameter or a `RunnableConfig`. The server inspects your function's type annotations to determine which arguments to inject, so make sure to include the correct type hints. The server's queue workers will call your factory function any time they need to process a run. The function will also be called for certain other endpoints to update state, read state, or to fetch assistant schemas. The `ServerRuntime` tells you which context triggered the call.

<Note>
  `ServerRuntime` is in beta and may change in future releases.
</Note>

#### Simple factory

The simplest form is a plain `async def` that returns a compiled graph:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_openai import ChatOpenAI
from langgraph.graph import START, StateGraph
from langchain_core.runnables import RunnableConfig
from langgraph_sdk.runtime import ServerRuntime

from my_agent.utils.state import AgentState

model = ChatOpenAI(model="gpt-5.5")

def make_graph_for_user(user_id: str):
    """Build a graph customized per user."""
    graph_workflow = StateGraph(AgentState)

    async def call_model(state):
        return {"messages": [await model.ainvoke(state["messages"])]}

    graph_workflow.add_node("agent", call_model)
    graph_workflow.add_edge(START, "agent")
    return graph_workflow.compile()

async def make_graph(config: RunnableConfig, runtime: ServerRuntime):
    user = runtime.ensure_user()
    return make_graph_for_user(user.identity)
```

#### Context manager factory

If you need to set up and tear down resources (database connections, load MCP tools, etc.), use an async context manager. Use `runtime.execution_runtime` to check whether the graph is being called for actual execution or just for introspection (schemas, visualization):

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import contextlib

from langchain_openai import ChatOpenAI
from langgraph.graph import START, StateGraph
from langchain_core.runnables import RunnableConfig
from langgraph_sdk.runtime import ServerRuntime

from my_agent.utils.state import AgentState

model = ChatOpenAI(model="gpt-5.5")

def make_agent_graph(tools: list):
    """Make a simple LLM agent."""
    graph_workflow = StateGraph(AgentState)
    bound = model.bind_tools(tools)

    async def call_model(state):
        return {"messages": [await bound.ainvoke(state["messages"])]}

    graph_workflow.add_node("agent", call_model)
    graph_workflow.add_edge(START, "agent")
    return graph_workflow.compile()

@contextlib.asynccontextmanager
async def make_graph(runtime: ServerRuntime):
    if ert := runtime.execution_runtime:
        # Only set up expensive resources during actual execution.
        # Introspection calls (get_schema, get_graph, ...) skip this.
        mcp_tools = await connect_mcp(ert.ensure_user())  # your setup logic
        yield make_agent_graph(tools=mcp_tools)
        await disconnect_mcp()  # your teardown logic
    else:
        # For schema/state reads, return a graph with the same
        # topology but no expensive resource setup.
        yield make_agent_graph(tools=[])
```

Finally, specify the path to your factory in `langgraph.json`:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
    "$schema": "https://langgra.ph/schema.json",
    "dependencies": ["."],
    "graphs": {
        "chat_agent": "my_project.agents:make_graph",
    }
}
```

## ServerRuntime reference

Your factory function receives a `ServerRuntime` instance with the following attributes:

| Attribute        | Type               | Description                                                                                                       |
| ---------------- | ------------------ | ----------------------------------------------------------------------------------------------------------------- |
| `access_context` | `str`              | Why the factory was called: `"threads.create_run"`, `"threads.update"`, `"threads.read"`, or `"assistants.read"`. |
| `user`           | `BaseUser \| None` | The authenticated user, or `None` if no [custom auth](/langsmith/custom-auth) is configured.                      |
| `store`          | `BaseStore`        | The store instance for persistence and memory.                                                                    |

**Methods:**

| Method              | Description                                                                                                                                                                     |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ensure_user()`     | Returns the authenticated user. Raises `PermissionError` if no user is provided.                                                                                                |
| `execution_runtime` | Returns the execution runtime when `access_context` is `"threads.create_run"`, or `None` otherwise. Use this to conditionally set up expensive resources only during execution. |

### Access contexts

The server calls your factory in several contexts beyond just executing runs. In all contexts, the returned graph should have the **same topology** (nodes, edges, state schema). A mismatched topology in write contexts (`threads.create_run`, `threads.update`) can cause incorrect state updates. In read contexts (`threads.read`, `assistants.read`), a mismatch affects reported pending tasks, schemas, and visualizations but won't corrupt data. Use `execution_runtime` to conditionally set up expensive resources without changing the graph structure.

| Context              | Description                                                                                             |
| -------------------- | ------------------------------------------------------------------------------------------------------- |
| `threads.create_run` | Full graph execution. `execution_runtime` is available.                                                 |
| `threads.update`     | State update via `aupdate_state`. Does not execute node functions, but it can change the pending tasks. |
| `threads.read`       | State reads via `aget_state` / `aget_state_history`.                                                    |
| `assistants.read`    | Schema and graph introspection for visualization, MCP, A2A, etc.                                        |

## Customize tracing per graph

You can use the factory function to customize or disable tracing for a specific graph. See [Conditional tracing: Customize tracing in deployed agents](/langsmith/conditional-tracing#customize-tracing-in-deployed-agents) for examples.

See more info on the [LangGraph API configuration file](/langsmith/cli#configuration-file).

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/graph-rebuild.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Time travel using the server API
Source: https://docs.langchain.com/langsmith/human-in-the-loop-time-travel

LangGraph provides the [**time travel**](/oss/python/langgraph/use-time-travel) functionality to resume execution from a prior checkpoint, either replaying the same state or modifying it to explore alternatives. In all cases, resuming past execution produces a new fork in the history.

To time travel using the LangSmith Deployment API (via the LangGraph SDK):

1. **Run the graph** with initial inputs using [LangGraph SDK](/langsmith/langgraph-python-sdk)'s [client.runs.wait](https://reference.langchain.com/python/langsmith/deployment/sdk/#langgraph_sdk.client.RunsClient.wait) or [client.runs.stream](https://reference.langchain.com/python/langsmith/deployment/sdk/#langgraph_sdk.client.RunsClient.stream) APIs.
2. **Identify a checkpoint in an existing thread**: Use [client.threads.get\_history](https://reference.langchain.com/python/langsmith/deployment/sdk/#langgraph_sdk.client.ThreadsClient.get_history) method to retrieve the execution history for a specific `thread_id` and locate the desired `checkpoint_id`.
   Alternatively, set a [breakpoint](/oss/python/langgraph/interrupts) before the node(s) where you want execution to pause. You can then find the most recent checkpoint recorded up to that breakpoint.
3. **(Optional) modify the graph state**: Use the [client.threads.update\_state](https://reference.langchain.com/python/langsmith/deployment/sdk/#langgraph_sdk.client.ThreadsClient.update_state) method to modify the graph’s state at the checkpoint and resume execution from alternative state.
4. **Resume execution from the checkpoint**: Use the [client.runs.wait](https://reference.langchain.com/python/langsmith/deployment/sdk/#langgraph_sdk.client.RunsClient.wait) or [client.runs.stream](https://reference.langchain.com/python/langsmith/deployment/sdk/#langgraph_sdk.client.RunsClient.stream) APIs with an input of `None` and the appropriate `thread_id` and `checkpoint_id`.

## Use time travel in a workflow

<Accordion title="Example graph">
  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from typing_extensions import TypedDict, NotRequired
  from langgraph.graph import StateGraph, START, END
  from langchain.chat_models import init_chat_model
  from langgraph.checkpoint.memory import InMemorySaver

  class State(TypedDict):
      topic: NotRequired[str]
      joke: NotRequired[str]

  model = init_chat_model(
      "claude-sonnet-4-6",
      temperature=0,
  )

  def generate_topic(state: State):
      """LLM call to generate a topic for the joke"""
      msg = model.invoke("Give me a funny topic for a joke")
      return {"topic": msg.content}

  def write_joke(state: State):
      """LLM call to write a joke based on the topic"""
      msg = model.invoke(f"Write a short joke about {state['topic']}")
      return {"joke": msg.content}

  # Build workflow
  builder = StateGraph(State)

  # Add nodes
  builder.add_node("generate_topic", generate_topic)
  builder.add_node("write_joke", write_joke)

  # Add edges to connect nodes
  builder.add_edge(START, "generate_topic")
  builder.add_edge("generate_topic", "write_joke")

  # Compile
  graph = builder.compile()
  ```
</Accordion>

### 1. Run the graph

<Tabs>
  <Tab title="Python">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from langgraph_sdk import get_client
    client = get_client(url=<DEPLOYMENT_URL>)

    # Using the graph deployed with the name "agent"
    assistant_id = "agent"

    # create a thread
    thread = await client.threads.create()
    thread_id = thread["thread_id"]

    # Run the graph
    result = await client.runs.wait(
        thread_id,
        assistant_id,
        input={}
    )
    ```
  </Tab>

  <Tab title="JavaScript">
    ```js theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { Client } from "@langchain/langgraph-sdk";
    const client = new Client({ apiUrl: <DEPLOYMENT_URL> });

    // Using the graph deployed with the name "agent"
    const assistantID = "agent";

    // create a thread
    const thread = await client.threads.create();
    const threadID = thread["thread_id"];

    // Run the graph
    const result = await client.runs.wait(
      threadID,
      assistantID,
      { input: {}}
    );
    ```
  </Tab>

  <Tab title="cURL">
    Create a thread:

    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    curl --request POST \
    --url <DEPLOYMENT_URL>/threads \
    --header 'Content-Type: application/json' \
    --data '{}'
    ```

    Run the graph:

    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    curl --request POST \
    --url <DEPLOYMENT_URL>/threads/<THREAD_ID>/runs/wait \
    --header 'Content-Type: application/json' \
    --data "{
      \"assistant_id\": \"agent\",
      \"input\": {}
    }"
    ```
  </Tab>
</Tabs>

### 2. Identify a checkpoint

<Tabs>
  <Tab title="Python">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    # The states are returned in reverse chronological order.
    states = await client.threads.get_history(thread_id)
    selected_state = states[1]
    print(selected_state)
    ```
  </Tab>

  <Tab title="JavaScript">
    ```js theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    // The states are returned in reverse chronological order.
    const states = await client.threads.getHistory(threadID);
    const selectedState = states[1];
    console.log(selectedState);
    ```
  </Tab>

  <Tab title="cURL">
    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    curl --request GET \
    --url <DEPLOYMENT_URL>/threads/<THREAD_ID>/history \
    --header 'Content-Type: application/json'
    ```
  </Tab>
</Tabs>

<a />

### 3. Update the state

[`update_state`](https://reference.langchain.com/python/langgraph/graphs/#langgraph.graph.state.CompiledStateGraph.update_state) will create a new checkpoint. The new checkpoint will be associated with the same thread, but a new checkpoint ID.

<Tabs>
  <Tab title="Python">
    ```python {highlight={4}} theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    new_config = await client.threads.update_state(
        thread_id,
        {"topic": "chickens"},
        checkpoint_id=selected_state["checkpoint_id"]
    )
    print(new_config)
    ```
  </Tab>

  <Tab title="JavaScript">
    ```js theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    const newConfig = await client.threads.updateState(
      threadID,
      {
        values: { "topic": "chickens" },
        checkpointId: selectedState["checkpoint_id"]
      }
    );
    console.log(newConfig);
    ```
  </Tab>

  <Tab title="cURL">
    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    curl --request POST \
    --url <DEPLOYMENT_URL>/threads/<THREAD_ID>/state \
    --header 'Content-Type: application/json' \
    --data "{
      \"assistant_id\": \"agent\",
      \"checkpoint_id\": <CHECKPOINT_ID>,
      \"values\": {\"topic\": \"chickens\"}
    }"
    ```
  </Tab>
</Tabs>

### 4. Resume execution from the checkpoint

<Tabs>
  <Tab title="Python">
    ```python {highlight={4,5}} theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    await client.runs.wait(
        thread_id,
        assistant_id,
        input=None,
        checkpoint_id=new_config["checkpoint_id"]
    )
    ```
  </Tab>

  <Tab title="JavaScript">
    ```javascript {highlight={5,6}} theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    await client.runs.wait(
      threadID,
      assistantID,
      {
        input: null,
        checkpointId: newConfig["checkpoint_id"]
      }
    );
    ```
  </Tab>

  <Tab title="cURL">
    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    curl --request POST \
    --url <DEPLOYMENT_URL>/threads/<THREAD_ID>/runs/wait \
    --header 'Content-Type: application/json' \
    --data "{
      \"assistant_id\": \"agent\",
      \"checkpoint_id\": <CHECKPOINT_ID>
    }"
    ```
  </Tab>
</Tabs>

## Learn more

* [**LangGraph time travel guide**](/oss/python/langgraph/use-time-travel): learn more about using time travel in LangGraph.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/human-in-the-loop-time-travel.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Hybrid
Source: https://docs.langchain.com/langsmith/hybrid

Self-host your Agent Servers and send traces to either a self-hosted LangSmith instance or LangSmith SaaS.

In the **hybrid** model, you self-host your <Tooltip>Agent Servers</Tooltip> in your own infrastructure and send traces to LangSmith, where LangSmith can be either a self-hosted instance or LangSmith SaaS.

This gives you control over where your agent workloads run while letting you choose the LangSmith deployment that best fits your observability and compliance requirements.

## Components

| Component                                | Where it runs                                         | Who manages it                        |
| ---------------------------------------- | ----------------------------------------------------- | ------------------------------------- |
| <Tooltip>Agent Servers</Tooltip>         | Your infrastructure                                   | You                                   |
| LangSmith (tracing, evaluation, prompts) | Self-hosted in your infrastructure, or LangSmith SaaS | You (self-hosted) or LangChain (SaaS) |

## Self-host your Agent Servers

Deploy standalone Agent Servers using Docker, Docker Compose, or Kubernetes. See the [standalone server guide](/langsmith/deploy-standalone-server) for prerequisites, environment variables, and platform-specific instructions.

## Choose where traces are sent

Agent Servers send traces to LangSmith based on the `LANGSMITH_ENDPOINT` environment variable:

* **LangSmith SaaS**: Omit `LANGSMITH_ENDPOINT` to use the default (GCP US), or set it to the endpoint for your region:

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

* **Self-hosted LangSmith**: Set `LANGSMITH_ENDPOINT` to the hostname of your [self-hosted LangSmith](/langsmith/self-hosted) instance.

In both cases, authenticate with a [LangSmith API key](/langsmith/create-account-api-key) issued by the LangSmith instance you are tracing to.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/hybrid.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
