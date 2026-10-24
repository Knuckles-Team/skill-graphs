[Skip to main content](https://gofastmcp.com/servers/lifespan#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
Search...
Navigation
Features
Lifespans
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
    * [ Background Tasks NEW ](https://gofastmcp.com/servers/tasks)
    * [Composition](https://gofastmcp.com/servers/composition)
    * [ Dependencies NEW ](https://gofastmcp.com/servers/dependency-injection)
    * [Elicitation](https://gofastmcp.com/servers/elicitation)
    * [Icons](https://gofastmcp.com/servers/icons)
    * [ Lifespan NEW ](https://gofastmcp.com/servers/lifespan)
    * [Logging](https://gofastmcp.com/servers/logging)
    * [Middleware](https://gofastmcp.com/servers/middleware)
    * [ Pagination NEW ](https://gofastmcp.com/servers/pagination)
    * [Progress](https://gofastmcp.com/servers/progress)
    * [Sampling](https://gofastmcp.com/servers/sampling)
    * [ Storage Backends NEW ](https://gofastmcp.com/servers/storage-backends)
    * [ Telemetry NEW ](https://gofastmcp.com/servers/telemetry)
    * [Testing](https://gofastmcp.com/servers/testing)
    * [ Versioning NEW ](https://gofastmcp.com/servers/versioning)
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
  * [Basic Usage](https://gofastmcp.com/servers/lifespan#basic-usage)
  * [Accessing Lifespan Context](https://gofastmcp.com/servers/lifespan#accessing-lifespan-context)
  * [Composing Lifespans](https://gofastmcp.com/servers/lifespan#composing-lifespans)
  * [Backwards Compatibility](https://gofastmcp.com/servers/lifespan#backwards-compatibility)
  * [With FastAPI](https://gofastmcp.com/servers/lifespan#with-fastapi)


Features
# Lifespans
Copy page
Server-level setup and teardown with composable lifespans
Copy page
`3.0.0` Lifespans let you run code once when the server starts and clean up when it stops. Unlike per-session handlers, lifespans run exactly once regardless of how many clients connect.
##
[​](https://gofastmcp.com/servers/lifespan#basic-usage)
Basic Usage
Use the `@lifespan` decorator to define a lifespan:
Copy
```
from fastmcp import FastMCP
from fastmcp.server.lifespan import lifespan

@lifespan
async def app_lifespan(server):
    # Setup: runs once when server starts
    print("Starting up...")
    try:
        yield {"started_at": "2024-01-01"}
    finally:
        # Teardown: runs when server stops
        print("Shutting down...")

mcp = FastMCP("MyServer", lifespan=app_lifespan)

```

The dict you yield becomes the **lifespan context** , accessible from tools.
Always use `try/finally` for cleanup code to ensure it runs even if the server is cancelled.
##
[​](https://gofastmcp.com/servers/lifespan#accessing-lifespan-context)
Accessing Lifespan Context
Access the lifespan context in tools via `ctx.lifespan_context`:
Copy
```
from fastmcp import FastMCP, Context
from fastmcp.server.lifespan import lifespan

@lifespan
async def app_lifespan(server):
    # Initialize shared state
    data = {"users": ["alice", "bob"]}
    yield {"data": data}

mcp = FastMCP("MyServer", lifespan=app_lifespan)

@mcp.tool
def list_users(ctx: Context) -> list[str]:
    data = ctx.lifespan_context["data"]
    return data["users"]

```

##
[​](https://gofastmcp.com/servers/lifespan#composing-lifespans)
Composing Lifespans
Compose multiple lifespans with the `|` operator:
Copy
```
from fastmcp import FastMCP
from fastmcp.server.lifespan import lifespan

@lifespan
async def config_lifespan(server):
    config = {"debug": True, "version": "1.0"}
    yield {"config": config}

@lifespan
async def data_lifespan(server):
    data = {"items": []}
    yield {"data": data}

# Compose with |
mcp = FastMCP("MyServer", lifespan=config_lifespan | data_lifespan)

```

Composed lifespans:
  * Enter in order (left to right)
  * Exit in reverse order (right to left)
  * Merge their context dicts (later values overwrite earlier on conflict)


##
[​](https://gofastmcp.com/servers/lifespan#backwards-compatibility)
Backwards Compatibility
Existing `@asynccontextmanager` lifespans still work when passed directly to FastMCP:
Copy
```
from contextlib import asynccontextmanager
from fastmcp import FastMCP

@asynccontextmanager
async def legacy_lifespan(server):
    yield {"key": "value"}

mcp = FastMCP("MyServer", lifespan=legacy_lifespan)

```

To compose an `@asynccontextmanager` function with `@lifespan` functions, wrap it with `ContextManagerLifespan`:
Copy
```
from contextlib import asynccontextmanager
from fastmcp.server.lifespan import lifespan, ContextManagerLifespan

@asynccontextmanager
async def legacy_lifespan(server):
    yield {"legacy": True}

@lifespan
async def new_lifespan(server):
    yield {"new": True}

# Wrap the legacy lifespan explicitly for composition
combined = ContextManagerLifespan(legacy_lifespan) | new_lifespan

```

##
[​](https://gofastmcp.com/servers/lifespan#with-fastapi)
With FastAPI
When mounting FastMCP into FastAPI, use `combine_lifespans` to run both your app’s lifespan and the MCP server’s lifespan:
Copy
```
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastmcp import FastMCP
from fastmcp.utilities.lifespan import combine_lifespans

@asynccontextmanager
async def app_lifespan(app):
    print("FastAPI starting...")
    yield
    print("FastAPI shutting down...")

mcp = FastMCP("Tools")
mcp_app = mcp.http_app()

app = FastAPI(lifespan=combine_lifespans(app_lifespan, mcp_app.lifespan))
app.mount("/mcp", mcp_app)

```

See the [FastAPI integration guide](https://gofastmcp.com/integrations/fastapi#combining-lifespans) for full details.
[ Icons Previous ](https://gofastmcp.com/servers/icons)[ Client Logging Next ](https://gofastmcp.com/servers/logging)
Ctrl+I
