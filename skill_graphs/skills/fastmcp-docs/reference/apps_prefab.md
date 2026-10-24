[Skip to main content](https://gofastmcp.com/apps/prefab#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
Search...
Navigation
Apps
Prefab Apps
Search the docs...
Ctrl K
Documentation
##### Get Started
  * [Welcome!](https://gofastmcp.com/getting-started/welcome)
  * [Installation](https://gofastmcp.com/getting-started/installation)
  * [Quickstart](https://gofastmcp.com/getting-started/quickstart)


##### Servers
  * [Overview](https://gofastmcp.com/servers/server)
  * Core Components
  * FeaturesUPDATED
  * ProvidersNEW
  * TransformsNEW
  * AuthenticationUPDATED
  * [ Authorization NEW ](https://gofastmcp.com/servers/authorization)
  * Deployment


##### Apps
  * [ Overview NEW ](https://gofastmcp.com/apps/overview)
  * [ Prefab Apps SOON ](https://gofastmcp.com/apps/prefab)
  * [ Patterns SOON ](https://gofastmcp.com/apps/patterns)
  * [ Custom HTML NEW ](https://gofastmcp.com/apps/low-level)


##### Clients
  * [Overview](https://gofastmcp.com/clients/client)
  * [Transports](https://gofastmcp.com/clients/transports)
  * Core Operations
  * HandlersUPDATED
  * AuthenticationUPDATED


##### Integrations
  * Auth
  * Web Frameworks
  * AI Assistants
  * AI SDKs
  * [MCP.json](https://gofastmcp.com/integrations/mcp-json-configuration)


##### CLI
  * [Overview](https://gofastmcp.com/cli/overview)
  * [Running](https://gofastmcp.com/cli/running)
  * [Install MCPs](https://gofastmcp.com/cli/install-mcp)
  * [Inspecting](https://gofastmcp.com/cli/inspecting)
  * [Client](https://gofastmcp.com/cli/client)
  * [Generate CLI](https://gofastmcp.com/cli/generate-cli)
  * [Auth](https://gofastmcp.com/cli/auth)


##### More
  * Upgrading
  * Development
  * What's New


On this page
  * [What You Return](https://gofastmcp.com/apps/prefab#what-you-return)
  * [Components](https://gofastmcp.com/apps/prefab#components)
  * [PrefabApp](https://gofastmcp.com/apps/prefab#prefabapp)
  * [ToolResult](https://gofastmcp.com/apps/prefab#toolresult)
  * [Type Inference](https://gofastmcp.com/apps/prefab#type-inference)
  * [How It Works](https://gofastmcp.com/apps/prefab#how-it-works)
  * [Mixing with Custom HTML Apps](https://gofastmcp.com/apps/prefab#mixing-with-custom-html-apps)
  * [Next Steps](https://gofastmcp.com/apps/prefab#next-steps)


Apps
# Prefab Apps
Copy page
Build interactive tool UIs in pure Python — no HTML or JavaScript required.
Copy page
`3.1.0`
`prefab-ui` to a specific version in your dependencies (see below).
Prefab started as a component library inside FastMCP and grew into a full framework for building interactive applications — with its own state management, reactive expression system, and action model. The
Copy
```
pip install "fastmcp[apps]"

```

Prefab UI is in active early development and its API changes frequently. We strongly recommend pinning `prefab-ui` to a specific version in your project’s dependencies. Installing `fastmcp[apps]` pulls in `prefab-ui` but won’t pin it — so a routine `pip install --upgrade` could introduce breaking changes.
Copy
```
# pyproject.toml
dependencies = [
    "fastmcp[apps]",
    "prefab-ui==0.8.0",  # pin to a known working version
]

```

Here’s the simplest possible Prefab App — a tool that returns a bar chart:
Copy
```
from prefab_ui.components import Column, Heading, BarChart, ChartSeries
from prefab_ui.app import PrefabApp
from fastmcp import FastMCP

mcp = FastMCP("Dashboard")


@mcp.tool(app=True)
def revenue_chart(year: int) -> PrefabApp:
    """Show annual revenue as an interactive bar chart."""
    data = [
        {"quarter": "Q1", "revenue": 42000},
        {"quarter": "Q2", "revenue": 51000},
        {"quarter": "Q3", "revenue": 47000},
        {"quarter": "Q4", "revenue": 63000},
    ]

    with Column(gap=4, css_class="p-6") as view:
        Heading(f"{year} Revenue")
        BarChart(
            data=data,
            series=[ChartSeries(data_key="revenue", label="Revenue")],
            x_axis="quarter",
        )

    return PrefabApp(view=view)

```

That’s it — you declare a layout using Python’s `with` statement, and return it. When the host calls this tool, the user sees an interactive bar chart instead of a JSON blob. The [Patterns](https://gofastmcp.com/apps/patterns) page has more examples: area charts, data tables, forms, status dashboards, and more.
##
[​](https://gofastmcp.com/apps/prefab#what-you-return)
What You Return
###
[​](https://gofastmcp.com/apps/prefab#components)
Components
The simplest way to get started. If you’re returning a visual representation of data and don’t need Prefab’s more advanced features like initial state or stylesheets, just return the components directly. FastMCP wraps them in a `PrefabApp` automatically:
Copy
```
from prefab_ui.components import Column, Heading, Badge
from fastmcp import FastMCP

mcp = FastMCP("Status")


@mcp.tool(app=True)
def status_badge() -> Column:
    """Show system status."""
    with Column(gap=2) as view:
        Heading("All Systems Operational")
        Badge("Healthy", variant="success")
    return view

```

Want a chart? Return a chart. Want a table? Return a table. FastMCP handles the wiring.
###
[​](https://gofastmcp.com/apps/prefab#prefabapp)
PrefabApp
When you need more control — setting initial state values that components can read and react to, or configuring the rendering engine — return a `PrefabApp` explicitly:
Copy
```
from prefab_ui.components import Column, Heading, Text, Button, If, Badge
from prefab_ui.actions import ToggleState
from prefab_ui.app import PrefabApp
from fastmcp import FastMCP

mcp = FastMCP("Demo")


@mcp.tool(app=True)
def toggle_demo() -> PrefabApp:
    """Interactive toggle with state."""
    with Column(gap=4, css_class="p-6") as view:
        Button("Toggle", on_click=ToggleState("show"))
        with If("{{ show }}"):
            Badge("Visible!", variant="success")

    return PrefabApp(view=view, state={"show": False})

```

The `state` dict provides the initial values. Components reference state with `{{ expression }}` templates. State mutations like `ToggleState` happen entirely in the browser — no server round-trip. The
###
[​](https://gofastmcp.com/apps/prefab#toolresult)
ToolResult
Every tool result has two audiences: the renderer (which displays the UI) and the LLM (which reads the text content to understand what happened). By default, Prefab Apps send `"[Rendered Prefab UI]"` as the text content, which tells the LLM almost nothing. If you want the LLM to understand the result — so it can reference the data in conversation, summarize it, or decide what to do next — wrap your return in a `ToolResult` with a meaningful `content` string:
Copy
```
from prefab_ui.components import Column, Heading, BarChart, ChartSeries
from prefab_ui.app import PrefabApp
from fastmcp import FastMCP
from fastmcp.tools import ToolResult

mcp = FastMCP("Sales")


@mcp.tool(app=True)
def sales_overview(year: int) -> ToolResult:
    """Show sales data visually and summarize for the model."""
    data = get_sales_data(year)
    total = sum(row["revenue"] for row in data)

    with Column(gap=4, css_class="p-6") as view:
        Heading("Sales Overview")
        BarChart(data=data, series=[ChartSeries(data_key="revenue")])

    return ToolResult(
        content=f"Total revenue for {year}: ${total:,} across {len(data)} quarters",
        structured_content=view,
    )

```

The user sees the chart. The LLM sees `"Total revenue for 2025: $203,000 across 4 quarters"` and can reason about it.
##
[​](https://gofastmcp.com/apps/prefab#type-inference)
Type Inference
If your tool’s return type annotation is a Prefab type — `PrefabApp`, `Component`, or their `Optional` variants — FastMCP detects this and enables app rendering automatically:
Copy
```
@mcp.tool
def greet(name: str) -> PrefabApp:
    return PrefabApp(view=Heading(f"Hello, {name}!"))

```

This is equivalent to `@mcp.tool(app=True)`. Explicit `app=True` is recommended for clarity, and is required when the return type doesn’t reveal a Prefab type (e.g., `-> ToolResult`).
##
[​](https://gofastmcp.com/apps/prefab#how-it-works)
How It Works
Behind the scenes, when a tool returns a Prefab component or `PrefabApp`, FastMCP:
  1. **Registers a shared renderer** — a `ui://prefab/renderer.html` resource containing the JavaScript rendering engine, fetched once by the host and reused across all your Prefab tools.
  2. **Wires the tool metadata** — so the host knows to load the renderer iframe when displaying the tool result.
  3. **Serializes the component tree** — your Python components become `structuredContent` on the tool result, which the renderer interprets and displays.

None of this requires any configuration. The `app=True` flag (or type inference) is the only thing you need.
##
[​](https://gofastmcp.com/apps/prefab#mixing-with-custom-html-apps)
Mixing with Custom HTML Apps
Prefab tools and [custom HTML tools](https://gofastmcp.com/apps/low-level) coexist in the same server. Prefab tools share a single renderer resource; custom tools point to their own. Both use the same MCP Apps protocol:
Copy
```
from fastmcp.server.apps import AppConfig

@mcp.tool(app=True)
def team_directory() -> PrefabApp:
    ...

@mcp.tool(app=AppConfig(resource_uri="ui://my-app/map.html"))
def map_view() -> str:
    ...

```

##
[​](https://gofastmcp.com/apps/prefab#next-steps)
Next Steps
  * **[Patterns](https://gofastmcp.com/apps/patterns)** — Charts, tables, forms, and other common tool UIs
  * **[Custom HTML Apps](https://gofastmcp.com/apps/low-level)** — When you need your own HTML, CSS, and JavaScript


[ Apps Previous ](https://gofastmcp.com/apps/overview)[ Patterns Next ](https://gofastmcp.com/apps/patterns)
Ctrl+I
