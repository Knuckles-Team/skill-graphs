[Skip to main content](https://gofastmcp.com/apps/overview#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
Search...
Navigation
Apps
Apps
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
  * [Prefab Apps (Recommended)](https://gofastmcp.com/apps/overview#prefab-apps-recommended)
  * [Custom HTML Apps](https://gofastmcp.com/apps/overview#custom-html-apps)


Apps
# Apps
Copy page
Give your tools interactive UIs rendered directly in the conversation.
Copy page
`3.0.0` MCP Apps let your tools return interactive UIs — rendered in a sandboxed iframe right inside the host client’s conversation. Instead of returning plain text, a tool can show a chart, a sortable table, a form, or anything you can build with HTML. FastMCP implements the
##
[​](https://gofastmcp.com/apps/overview#prefab-apps-recommended)
Prefab Apps (Recommended)
`3.1.0`
[pin `prefab-ui` to a specific version](https://gofastmcp.com/apps/prefab#getting-started) in your dependencies.
Copy
```
from prefab_ui.components import Column, Heading, BarChart, ChartSeries
from prefab_ui.app import PrefabApp
from fastmcp import FastMCP

mcp = FastMCP("Dashboard")

@mcp.tool(app=True)
def sales_chart(year: int) -> PrefabApp:
    """Show sales data as an interactive chart."""
    data = get_sales_data(year)

    with Column(gap=4, css_class="p-6") as view:
        Heading(f"{year} Sales")
        BarChart(
            data=data,
            series=[ChartSeries(data_key="revenue", label="Revenue")],
            x_axis="month",
        )

    return PrefabApp(view=view)

```

Install with `pip install "fastmcp[apps]"` and see [Prefab Apps](https://gofastmcp.com/apps/prefab) for the integration guide.
##
[​](https://gofastmcp.com/apps/overview#custom-html-apps)
Custom HTML Apps
The  This is the right choice for custom rendering (maps, 3D, video), specific JavaScript frameworks, or capabilities beyond what the component library offers.
Copy
```
from fastmcp import FastMCP
from fastmcp.server.apps import AppConfig, ResourceCSP

mcp = FastMCP("Custom App")

@mcp.tool(app=AppConfig(resource_uri="ui://my-app/view.html"))
def my_tool() -> str:
    return '{"values": [1, 2, 3]}'

@mcp.resource(
    "ui://my-app/view.html",
    app=AppConfig(csp=ResourceCSP(resource_domains=["https://unpkg.com"])),
)
def view() -> str:
    return "<html>...</html>"

```

See [Custom HTML Apps](https://gofastmcp.com/apps/low-level) for the full reference.
[ Project Configuration Previous ](https://gofastmcp.com/deployment/server-configuration)[ Prefab Apps Next ](https://gofastmcp.com/apps/prefab)
Ctrl+I
