[Skip to main content](https://gofastmcp.com/servers/providers/custom#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
Search...
Navigation
Providers
Custom Providers
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
    * [ Overview NEW ](https://gofastmcp.com/servers/providers/overview)
    * [ Local NEW ](https://gofastmcp.com/servers/providers/local)
    * [ Filesystem NEW ](https://gofastmcp.com/servers/providers/filesystem)
    * [MCP Proxy](https://gofastmcp.com/servers/providers/proxy)
    * [ Skills NEW ](https://gofastmcp.com/servers/providers/skills)
    * [ Custom NEW ](https://gofastmcp.com/servers/providers/custom)
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
  * [When to Build Custom](https://gofastmcp.com/servers/providers/custom#when-to-build-custom)
  * [Providers vs Middleware](https://gofastmcp.com/servers/providers/custom#providers-vs-middleware)
  * [The Provider Interface](https://gofastmcp.com/servers/providers/custom#the-provider-interface)
  * [What Providers Return](https://gofastmcp.com/servers/providers/custom#what-providers-return)
  * [Registering Providers](https://gofastmcp.com/servers/providers/custom#registering-providers)
  * [A Simple Provider](https://gofastmcp.com/servers/providers/custom#a-simple-provider)
  * [Lifecycle Management](https://gofastmcp.com/servers/providers/custom#lifecycle-management)
  * [Full Example: API-Backed Resources](https://gofastmcp.com/servers/providers/custom#full-example-api-backed-resources)


Providers
# Custom Providers
Copy page
Build providers that source components from any data source
Copy page
`3.0.0` Custom providers let you source components from anywhere - databases, APIs, configuration systems, or dynamic runtime logic. If you can write Python code to fetch or generate a component, you can wrap it in a provider.
##
[​](https://gofastmcp.com/servers/providers/custom#when-to-build-custom)
When to Build Custom
The built-in providers handle common cases: decorators (`LocalProvider`), composition (`FastMCPProvider`), and proxying (`ProxyProvider`). Build a custom provider when your components come from somewhere else:
  * **Database-backed tools** : Admin users define tools in a database, and your server exposes them dynamically
  * **API-backed resources** : Resources that fetch content from external services on demand
  * **Configuration-driven components** : Components loaded from YAML/JSON config files at startup
  * **Multi-tenant systems** : Different users see different tools based on their permissions
  * **Plugin systems** : Third-party code registers components at runtime


##
[​](https://gofastmcp.com/servers/providers/custom#providers-vs-middleware)
Providers vs Middleware
Both providers and [middleware](https://gofastmcp.com/servers/middleware) can influence what components a client sees, but they work at different levels. **Providers** are objects that source components. They make it easy to reason about where tools, resources, and prompts come from - a database, another server, an API. **Middleware** intercepts individual requests. It’s well-suited for request-specific decisions like logging, rate limiting, or authentication. You _could_ use middleware to dynamically add tools based on request context. But it’s often cleaner to have a provider source all possible tools, then use middleware or [visibility controls](https://gofastmcp.com/servers/visibility) to filter what each request can see. This separation makes it easier to reason about how components are sourced and how they interact with other server machinery.
##
[​](https://gofastmcp.com/servers/providers/custom#the-provider-interface)
The Provider Interface
A provider implements protected `_list_*` methods that return available components. The public `list_*` methods handle transforms automatically - you override the underscore-prefixed versions:
Copy
```
from collections.abc import Sequence
from fastmcp.server.providers import Provider
from fastmcp.tools import Tool
from fastmcp.resources import Resource
from fastmcp.prompts import Prompt

class MyProvider(Provider):
    async def _list_tools(self) -> Sequence[Tool]:
        """Return all tools this provider offers."""
        return []

    async def _list_resources(self) -> Sequence[Resource]:
        """Return all resources this provider offers."""
        return []

    async def _list_prompts(self) -> Sequence[Prompt]:
        """Return all prompts this provider offers."""
        return []

```

You only need to implement the methods for component types you provide. The base class returns empty sequences by default. The `_get_*` methods (`_get_tool`, `_get_resource`, `_get_prompt`) have default implementations that search through the list results. Override them only if you can fetch individual components more efficiently than iterating the full list.
##
[​](https://gofastmcp.com/servers/providers/custom#what-providers-return)
What Providers Return
Providers return component objects that are ready to use. When a client calls a tool, FastMCP invokes the tool’s function - your provider isn’t involved in execution. This means the `Tool`, `Resource`, or `Prompt` you return must actually work. The easiest way to create components is from functions:
Copy
```
from fastmcp.tools import Tool

def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

tool = Tool.from_function(add)

```

The function’s type hints become the input schema, and the docstring becomes the description. You can override these:
Copy
```
tool = Tool.from_function(
    add,
    name="calculator_add",
    description="Add two integers together"
)

```

Similar `from_function` methods exist for `Resource` and `Prompt`.
##
[​](https://gofastmcp.com/servers/providers/custom#registering-providers)
Registering Providers
Add providers when creating the server:
Copy
```
mcp = FastMCP(
    "MyServer",
    providers=[
        DatabaseProvider(db_url),
        ConfigProvider(config_path),
    ]
)

```

Or add them after creation:
Copy
```
mcp = FastMCP("MyServer")
mcp.add_provider(DatabaseProvider(db_url))

```

##
[​](https://gofastmcp.com/servers/providers/custom#a-simple-provider)
A Simple Provider
Here’s a minimal provider that serves tools from a dictionary:
Copy
```
from collections.abc import Callable, Sequence
from fastmcp import FastMCP
from fastmcp.server.providers import Provider
from fastmcp.tools import Tool

class DictProvider(Provider):
    def __init__(self, tools: dict[str, Callable]):
        super().__init__()
        self._tools = [
            Tool.from_function(fn, name=name)
            for name, fn in tools.items()
        ]

    async def _list_tools(self) -> Sequence[Tool]:
        return self._tools

```

Use it like this:
Copy
```
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b

mcp = FastMCP("Calculator", providers=[
    DictProvider({"add": add, "multiply": multiply})
])

```

##
[​](https://gofastmcp.com/servers/providers/custom#lifecycle-management)
Lifecycle Management
Providers often need to set up connections when the server starts and clean them up when it stops. Override the `lifespan` method:
Copy
```
from contextlib import asynccontextmanager
from collections.abc import AsyncIterator, Sequence

class DatabaseProvider(Provider):
    def __init__(self, db_url: str):
        super().__init__()
        self.db_url = db_url
        self.db = None

    @asynccontextmanager
    async def lifespan(self) -> AsyncIterator[None]:
        self.db = await connect_database(self.db_url)
        try:
            yield
        finally:
            await self.db.close()

    async def _list_tools(self) -> Sequence[Tool]:
        rows = await self.db.fetch("SELECT * FROM tools")
        return [self._make_tool(row) for row in rows]

```

FastMCP calls your provider’s `lifespan` during server startup and shutdown. The connection is available to your methods while the server runs.
##
[​](https://gofastmcp.com/servers/providers/custom#full-example-api-backed-resources)
Full Example: API-Backed Resources
Here’s a complete provider that fetches resources from an external REST API:
Copy
```
from contextlib import asynccontextmanager
from collections.abc import AsyncIterator, Sequence
from fastmcp.server.providers import Provider
from fastmcp.resources import Resource
import httpx

class ApiResourceProvider(Provider):
    """Provides resources backed by an external API."""

    def __init__(self, base_url: str, api_key: str):
        super().__init__()
        self.base_url = base_url
        self.api_key = api_key
        self.client = None

    @asynccontextmanager
    async def lifespan(self) -> AsyncIterator[None]:
        self.client = httpx.AsyncClient(
            base_url=self.base_url,
            headers={"Authorization": f"Bearer {self.api_key}"}
        )
        try:
            yield
        finally:
            await self.client.aclose()

    async def _list_resources(self) -> Sequence[Resource]:
        response = await self.client.get("/resources")
        response.raise_for_status()
        return [
            self._make_resource(item)
            for item in response.json()["items"]
        ]

    def _make_resource(self, data: dict) -> Resource:
        resource_id = data["id"]

        async def read_content() -> str:
            response = await self.client.get(
                f"/resources/{resource_id}/content"
            )
            return response.text

        return Resource.from_function(
            read_content,
            uri=f"api://resources/{resource_id}",
            name=data["name"],
            description=data.get("description", ""),
            mime_type=data.get("mime_type", "text/plain")
        )

```

Register it like any other provider:
Copy
```
from fastmcp import FastMCP

mcp = FastMCP("API Resources", providers=[
    ApiResourceProvider("https://api.example.com", "my-api-key")
])

```

[ Skills Provider Previous ](https://gofastmcp.com/servers/providers/skills)[ Transforms Overview Next ](https://gofastmcp.com/servers/transforms/transforms)
Ctrl+I
