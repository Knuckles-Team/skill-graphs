[Skip to main content](https://gofastmcp.com/v2/servers/context#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v2.14.5
Search...
Navigation
Advanced Features
MCP Context
Search the docs...
Ctrl K
Documentation
##### Get Started
  * [Welcome!](https://gofastmcp.com/v2/getting-started/welcome)
  * [Installation](https://gofastmcp.com/v2/getting-started/installation)
  * [Quickstart](https://gofastmcp.com/v2/getting-started/quickstart)
  * [ Updates NEW ](https://gofastmcp.com/v2/updates)


##### Servers
  * [Overview](https://gofastmcp.com/v2/servers/server)
  * Core Components
  * Advanced Features
    * [Composition](https://gofastmcp.com/v2/servers/composition)
    * [Context](https://gofastmcp.com/v2/servers/context)
    * [ Elicitation NEW ](https://gofastmcp.com/v2/servers/elicitation)
    * [ Icons NEW ](https://gofastmcp.com/v2/servers/icons)
    * [Logging](https://gofastmcp.com/v2/servers/logging)
    * [ Middleware NEW ](https://gofastmcp.com/v2/servers/middleware)
    * [Progress](https://gofastmcp.com/v2/servers/progress)
    * [Proxy Servers](https://gofastmcp.com/v2/servers/proxy)
    * [ Sampling NEW ](https://gofastmcp.com/v2/servers/sampling)
    * [ Storage Backends NEW ](https://gofastmcp.com/v2/servers/storage-backends)
    * [ Background Tasks NEW ](https://gofastmcp.com/v2/servers/tasks)
  * Authentication
  * Deployment


##### Clients
  * Essentials
  * Core Operations
  * Advanced Features
  * Authentication


##### Integrations
  * Authentication
  * Authorization
  * AI Assistants
  * AI SDKs
  * API Integration


##### Patterns
  * [Tool Transformation](https://gofastmcp.com/v2/patterns/tool-transformation)
  * [Decorating Methods](https://gofastmcp.com/v2/patterns/decorating-methods)
  * [CLI](https://gofastmcp.com/v2/patterns/cli)
  * [Contrib Modules](https://gofastmcp.com/v2/patterns/contrib)
  * [Testing](https://gofastmcp.com/v2/patterns/testing)


##### Development
  * [Contributing](https://gofastmcp.com/v2/development/contributing)
  * [Tests](https://gofastmcp.com/v2/development/tests)
  * [Releases](https://gofastmcp.com/v2/development/releases)
  * [ Upgrade Guide NEW ](https://gofastmcp.com/v2/development/upgrade-guide)
  * [Changelog](https://gofastmcp.com/v2/changelog)


These are the docs for FastMCP 2.0. [FastMCP 3.0](https://gofastmcp.com/getting-started/welcome) is now available.
On this page
  * [What Is Context?](https://gofastmcp.com/v2/servers/context#what-is-context)
  * [Accessing the Context](https://gofastmcp.com/v2/servers/context#accessing-the-context)
  * [Legacy Type-Hint Injection](https://gofastmcp.com/v2/servers/context#legacy-type-hint-injection)
  * [Via get_context() Function](https://gofastmcp.com/v2/servers/context#via-get_context-function)
  * [Context Capabilities](https://gofastmcp.com/v2/servers/context#context-capabilities)
  * [Logging](https://gofastmcp.com/v2/servers/context#logging)
  * [Client Elicitation](https://gofastmcp.com/v2/servers/context#client-elicitation)
  * [LLM Sampling](https://gofastmcp.com/v2/servers/context#llm-sampling)
  * [Progress Reporting](https://gofastmcp.com/v2/servers/context#progress-reporting)
  * [Resource Access](https://gofastmcp.com/v2/servers/context#resource-access)
  * [Prompt Access](https://gofastmcp.com/v2/servers/context#prompt-access)
  * [State Management](https://gofastmcp.com/v2/servers/context#state-management)
  * [Change Notifications](https://gofastmcp.com/v2/servers/context#change-notifications)
  * [FastMCP Server](https://gofastmcp.com/v2/servers/context#fastmcp-server)
  * [MCP Request](https://gofastmcp.com/v2/servers/context#mcp-request)
  * [Request Context Availability](https://gofastmcp.com/v2/servers/context#request-context-availability)
  * [Client Metadata](https://gofastmcp.com/v2/servers/context#client-metadata)
  * [Runtime Dependencies](https://gofastmcp.com/v2/servers/context#runtime-dependencies)
  * [HTTP Requests](https://gofastmcp.com/v2/servers/context#http-requests)
  * [HTTP Headers](https://gofastmcp.com/v2/servers/context#http-headers)
  * [Access Tokens](https://gofastmcp.com/v2/servers/context#access-tokens)
  * [Working with Token Claims](https://gofastmcp.com/v2/servers/context#working-with-token-claims)
  * [Custom Dependencies](https://gofastmcp.com/v2/servers/context#custom-dependencies)
  * [Using Depends()](https://gofastmcp.com/v2/servers/context#using-depends)
  * [Resource Management with Context Managers](https://gofastmcp.com/v2/servers/context#resource-management-with-context-managers)
  * [Nested Dependencies](https://gofastmcp.com/v2/servers/context#nested-dependencies)
  * [Advanced: Subclassing Dependency](https://gofastmcp.com/v2/servers/context#advanced-subclassing-dependency)


Advanced Features
# MCP Context
Copy page
Access MCP capabilities like logging, progress, and resources within your MCP objects.
Copy page
When defining FastMCP [tools](https://gofastmcp.com/v2/servers/tools), [resources](https://gofastmcp.com/v2/servers/resources), resource templates, or [prompts](https://gofastmcp.com/v2/servers/prompts), your functions might need to interact with the underlying MCP session or access advanced server capabilities. FastMCP provides the `Context` object for this purpose.
FastMCP uses [Custom Dependencies](https://gofastmcp.com/v2/servers/context#custom-dependencies) for creating your own.
##
[​](https://gofastmcp.com/v2/servers/context#what-is-context)
What Is Context?
The `Context` object provides a clean interface to access MCP features within your functions, including:
  * **Logging** : Send debug, info, warning, and error messages back to the client
  * **Progress Reporting** : Update the client on the progress of long-running operations
  * **Resource Access** : List and read data from resources registered with the server
  * **Prompt Access** : List and retrieve prompts registered with the server
  * **LLM Sampling** : Request the client’s LLM to generate text based on provided messages
  * **User Elicitation** : Request structured input from users during tool execution
  * **State Management** : Store and share data between middleware and the handler within a single request
  * **Request Information** : Access metadata about the current request
  * **Server Access** : When needed, access the underlying FastMCP server instance


##
[​](https://gofastmcp.com/v2/servers/context#accessing-the-context)
Accessing the Context
`2.14` The preferred way to access context is using the `CurrentContext()` dependency:
Copy
```
from fastmcp import FastMCP
from fastmcp.dependencies import CurrentContext
from fastmcp.server.context import Context

mcp = FastMCP(name="Context Demo")

@mcp.tool
async def process_file(file_uri: str, ctx: Context = CurrentContext()) -> str:
    """Processes a file, using context for logging and resource access."""
    await ctx.info(f"Processing {file_uri}")
    return "Processed file"

```

This works with tools, resources, and prompts:
Copy
```
from fastmcp import FastMCP
from fastmcp.dependencies import CurrentContext
from fastmcp.server.context import Context

mcp = FastMCP(name="Context Demo")

@mcp.resource("resource://user-data")
async def get_user_data(ctx: Context = CurrentContext()) -> dict:
    await ctx.debug("Fetching user data")
    return {"user_id": "example"}

@mcp.prompt
async def data_analysis_request(dataset: str, ctx: Context = CurrentContext()) -> str:
    return f"Please analyze the following dataset: {dataset}"

```

**Key Points:**
  * Dependency parameters are automatically excluded from the MCP schema—clients never see them.
  * Context methods are async, so your function usually needs to be async as well.
  * **Each MCP request receives a new context object.** Context is scoped to a single request; state or data set in one request will not be available in subsequent requests.
  * Context is only available during a request; attempting to use context methods outside a request will raise errors.


###
[​](https://gofastmcp.com/v2/servers/context#legacy-type-hint-injection)
Legacy Type-Hint Injection
For backwards compatibility, you can still access context by simply adding a parameter with the `Context` type hint. FastMCP will automatically inject the context instance:
Copy
```
from fastmcp import FastMCP, Context

mcp = FastMCP(name="Context Demo")

@mcp.tool
async def process_file(file_uri: str, ctx: Context) -> str:
    """Processes a file, using context for logging and resource access."""
    # Context is injected automatically based on the type hint
    return "Processed file"

```

This approach still works for tools, resources, and prompts. The parameter name doesn’t matter—only the `Context` type hint is important. The type hint can also be a union (`Context | None`) or use `Annotated[]`.
###
[​](https://gofastmcp.com/v2/servers/context#via-get_context-function)
Via `get_context()` Function
`2.2.11` For code nested deeper within your function calls where passing context through parameters is inconvenient, use `get_context()` to retrieve the active context from anywhere within a request’s execution flow:
Copy
```
from fastmcp import FastMCP
from fastmcp.server.dependencies import get_context

mcp = FastMCP(name="Dependency Demo")

# Utility function that needs context but doesn't receive it as a parameter
async def process_data(data: list[float]) -> dict:
    # Get the active context - only works when called within a request
    ctx = get_context()
    await ctx.info(f"Processing {len(data)} data points")

@mcp.tool
async def analyze_dataset(dataset_name: str) -> dict:
    # Call utility function that uses context internally
    data = load_data(dataset_name)
    await process_data(data)

```

**Important Notes:**
  * The `get_context()` function should only be used within the context of a server request. Calling it outside of a request will raise a `RuntimeError`.
  * The `get_context()` function is server-only and should not be used in client code.


##
[​](https://gofastmcp.com/v2/servers/context#context-capabilities)
Context Capabilities
FastMCP provides several advanced capabilities through the context object. Each capability has dedicated documentation with comprehensive examples and best practices:
###
[​](https://gofastmcp.com/v2/servers/context#logging)
Logging
Send debug, info, warning, and error messages back to the MCP client for visibility into function execution.
Copy
```
await ctx.debug("Starting analysis")
await ctx.info(f"Processing {len(data)} items")
await ctx.warning("Deprecated parameter used")
await ctx.error("Processing failed")

```

See [Server Logging](https://gofastmcp.com/v2/servers/logging) for complete documentation and examples.
###
[​](https://gofastmcp.com/v2/servers/context#client-elicitation)
Client Elicitation
`2.10.0` Request structured input from clients during tool execution, enabling interactive workflows and progressive disclosure. This is a new feature in the 6/18/2025 MCP spec.
Copy
```
result = await ctx.elicit("Enter your name:", response_type=str)
if result.action == "accept":
    name = result.data

```

See [User Elicitation](https://gofastmcp.com/v2/servers/elicitation) for detailed examples and supported response types.
###
[​](https://gofastmcp.com/v2/servers/context#llm-sampling)
LLM Sampling
`2.0.0` Request the client’s LLM to generate text based on provided messages, useful for leveraging AI capabilities within your tools.
Copy
```
response = await ctx.sample("Analyze this data", temperature=0.7)

```

See [LLM Sampling](https://gofastmcp.com/v2/servers/sampling) for comprehensive usage and advanced techniques.
###
[​](https://gofastmcp.com/v2/servers/context#progress-reporting)
Progress Reporting
Update clients on the progress of long-running operations, enabling progress indicators and better user experience.
Copy
```
await ctx.report_progress(progress=50, total=100)  # 50% complete

```

See [Progress Reporting](https://gofastmcp.com/v2/servers/progress) for detailed patterns and examples.
###
[​](https://gofastmcp.com/v2/servers/context#resource-access)
Resource Access
List and read data from resources registered with your FastMCP server, allowing access to files, configuration, or dynamic content.
Copy
```
# List available resources
resources = await ctx.list_resources()

# Read a specific resource
content_list = await ctx.read_resource("resource://config")
content = content_list[0].content

```

**Method signatures:**
  * **`ctx.list_resources() -> list[MCPResource]`**:`2.13.0` Returns list of all available resources
  * **`ctx.read_resource(uri: str | AnyUrl) -> list[ReadResourceContents]`**: Returns a list of resource content parts


###
[​](https://gofastmcp.com/v2/servers/context#prompt-access)
Prompt Access
`2.13.0` List and retrieve prompts registered with your FastMCP server, allowing tools and middleware to discover and use available prompts programmatically.
Copy
```
# List available prompts
prompts = await ctx.list_prompts()

# Get a specific prompt with arguments
result = await ctx.get_prompt("analyze_data", {"dataset": "users"})
messages = result.messages

```

**Method signatures:**
  * **`ctx.list_prompts() -> list[MCPPrompt]`**: Returns list of all available prompts
  * **`ctx.get_prompt(name: str, arguments: dict[str, Any] | None = None) -> GetPromptResult`**: Get a specific prompt with optional arguments


###
[​](https://gofastmcp.com/v2/servers/context#state-management)
State Management
`2.11.0` Store and share data between middleware and handlers within a single MCP request. Each MCP request (such as calling a tool, reading a resource, listing tools, or listing resources) receives its own context object with isolated state. Context state is particularly useful for passing information from [middleware](https://gofastmcp.com/v2/servers/middleware) to your handlers. To store a value in the context state, use `ctx.set_state(key, value)`. To retrieve a value, use `ctx.get_state(key)`.
Context state is scoped to a single MCP request. Each operation (tool call, resource read, list operation, etc.) receives a new context object. State set during one request will not be available in subsequent requests. For persistent data storage across requests, use external storage mechanisms like databases, files, or in-memory caches.
This simplified example shows how to use MCP middleware to store user info in the context state, and how to access that state in a tool:
Copy
```
from fastmcp.server.middleware import Middleware, MiddlewareContext

class UserAuthMiddleware(Middleware):
    async def on_call_tool(self, context: MiddlewareContext, call_next):

        # Middleware stores user info in context state
        context.fastmcp_context.set_state("user_id", "user_123")
        context.fastmcp_context.set_state("permissions", ["read", "write"])

        return await call_next(context)

@mcp.tool
async def secure_operation(data: str, ctx: Context) -> str:
    """Tool can access state set by middleware."""

    user_id = ctx.get_state("user_id")  # "user_123"
    permissions = ctx.get_state("permissions")  # ["read", "write"]

    if "write" not in permissions:
        return "Access denied"

    return f"Processing {data} for user {user_id}"

```

**Method signatures:**
  * **`ctx.set_state(key: str, value: Any) -> None`**: Store a value in the context state
  * **`ctx.get_state(key: str) -> Any`**: Retrieve a value from the context state (returns None if not found)

**State Inheritance:** When a new context is created (nested contexts), it inherits a copy of its parent’s state. This ensures that:
  * State set on a child context never affects the parent context
  * State set on a parent context after the child context is initialized is not propagated to the child context

This makes state management predictable and prevents unexpected side effects between nested operations.
###
[​](https://gofastmcp.com/v2/servers/context#change-notifications)
Change Notifications
`2.9.1` FastMCP automatically sends list change notifications when components (such as tools, resources, or prompts) are added, removed, enabled, or disabled. In rare cases where you need to manually trigger these notifications, you can use the context methods:
Copy
```
@mcp.tool
async def custom_tool_management(ctx: Context) -> str:
    """Example of manual notification after custom tool changes."""
    # After making custom changes to tools
    await ctx.send_tool_list_changed()
    await ctx.send_resource_list_changed()
    await ctx.send_prompt_list_changed()
    return "Notifications sent"

```

These methods are primarily used internally by FastMCP’s automatic notification system and most users will not need to invoke them directly.
###
[​](https://gofastmcp.com/v2/servers/context#fastmcp-server)
FastMCP Server
To access the underlying FastMCP server instance, you can use the `ctx.fastmcp` property:
Copy
```
@mcp.tool
async def my_tool(ctx: Context) -> None:
    # Access the FastMCP server instance
    server_name = ctx.fastmcp.name
    ...

```

###
[​](https://gofastmcp.com/v2/servers/context#mcp-request)
MCP Request
Access metadata about the current request and client.
Copy
```
@mcp.tool
async def request_info(ctx: Context) -> dict:
    """Return information about the current request."""
    return {
        "request_id": ctx.request_id,
        "client_id": ctx.client_id or "Unknown client"
    }

```

**Available Properties:**
  * **`ctx.request_id -> str`**: Get the unique ID for the current MCP request
  * **`ctx.client_id -> str | None`**: Get the ID of the client making the request, if provided during initialization
  * **`ctx.session_id -> str | None`**: Get the MCP session ID for session-based data sharing (HTTP transports only)


####
[​](https://gofastmcp.com/v2/servers/context#request-context-availability)
Request Context Availability
`2.13.1` The `ctx.request_context` property provides access to the underlying MCP request context, but returns `None` when the MCP session has not been established yet. This typically occurs:
  * During middleware execution in the `on_request` hook before the MCP handshake completes
  * During the initialization phase of client connections

The MCP request context is distinct from the HTTP request. For HTTP transports, HTTP request data may be available even when the MCP session is not yet established. To safely access the request context in situations where it may not be available:
Copy
```
from fastmcp import FastMCP, Context
from fastmcp.server.dependencies import get_http_request

mcp = FastMCP(name="Session Aware Demo")

@mcp.tool
async def session_info(ctx: Context) -> dict:
    """Return session information when available."""

    # Check if MCP session is available
    if ctx.request_context:
        # MCP session available - can access MCP-specific attributes
        return {
            "session_id": ctx.session_id,
            "request_id": ctx.request_id,
            "has_meta": ctx.request_context.meta is not None
        }
    else:
        # MCP session not available - use HTTP helpers for request data (if using HTTP transport)
        request = get_http_request()
        return {
            "message": "MCP session not available",
            "user_agent": request.headers.get("user-agent", "Unknown")
        }

```

For HTTP request access that works regardless of MCP session availability (when using HTTP transports), use the [HTTP request helpers](https://gofastmcp.com/v2/servers/context#http-requests) like `get_http_request()` and `get_http_headers()`.
####
[​](https://gofastmcp.com/v2/servers/context#client-metadata)
Client Metadata
`2.13.1` Clients can send contextual information with their requests using the `meta` parameter. This metadata is accessible through `ctx.request_context.meta` and is available for all MCP operations (tools, resources, prompts). The `meta` field is `None` when clients don’t provide metadata. When provided, metadata is accessible via attribute access (e.g., `meta.user_id`) rather than dictionary access. The structure of metadata is determined by the client making the request.
Copy
```
@mcp.tool
def send_email(to: str, subject: str, body: str, ctx: Context) -> str:
    """Send an email, logging metadata about the request."""

    # Access client-provided metadata
    meta = ctx.request_context.meta

    if meta:
        # Meta is accessed as an object with attribute access
        user_id = meta.user_id if hasattr(meta, 'user_id') else None
        trace_id = meta.trace_id if hasattr(meta, 'trace_id') else None

        # Use metadata for logging, observability, etc.
        if trace_id:
            log_with_trace(f"Sending email for user {user_id}", trace_id)

    # Send the email...
    return f"Email sent to {to}"

```

The MCP request is part of the low-level MCP SDK and intended for advanced use cases. Most users will not need to use it directly.
##
[​](https://gofastmcp.com/v2/servers/context#runtime-dependencies)
Runtime Dependencies
###
[​](https://gofastmcp.com/v2/servers/context#http-requests)
HTTP Requests
`2.2.11` The recommended way to access the current HTTP request is through the `get_http_request()` dependency function:
Copy
```
from fastmcp import FastMCP
from fastmcp.server.dependencies import get_http_request
from starlette.requests import Request

mcp = FastMCP(name="HTTP Request Demo")

@mcp.tool
async def user_agent_info() -> dict:
    """Return information about the user agent."""
    # Get the HTTP request
    request: Request = get_http_request()

    # Access request data
    user_agent = request.headers.get("user-agent", "Unknown")
    client_ip = request.client.host if request.client else "Unknown"

    return {
        "user_agent": user_agent,
        "client_ip": client_ip,
        "path": request.url.path,
    }

```

This approach works anywhere within a request’s execution flow, not just within your MCP function. It’s useful when:
  1. You need access to HTTP information in helper functions
  2. You’re calling nested functions that need HTTP request data
  3. You’re working with middleware or other request processing code


###
[​](https://gofastmcp.com/v2/servers/context#http-headers)
HTTP Headers
`2.2.11` If you only need request headers and want to avoid potential errors, you can use the `get_http_headers()` helper:
Copy
```
from fastmcp import FastMCP
from fastmcp.server.dependencies import get_http_headers

mcp = FastMCP(name="Headers Demo")

@mcp.tool
async def safe_header_info() -> dict:
    """Safely get header information without raising errors."""
    # Get headers (returns empty dict if no request context)
    headers = get_http_headers()

    # Get authorization header
    auth_header = headers.get("authorization", "")
    is_bearer = auth_header.startswith("Bearer ")

    return {
        "user_agent": headers.get("user-agent", "Unknown"),
        "content_type": headers.get("content-type", "Unknown"),
        "has_auth": bool(auth_header),
        "auth_type": "Bearer" if is_bearer else "Other" if auth_header else "None",
        "headers_count": len(headers)
    }

```

By default, `get_http_headers()` excludes problematic headers like `host` and `content-length`. To include all headers, use `get_http_headers(include_all=True)`.
###
[​](https://gofastmcp.com/v2/servers/context#access-tokens)
Access Tokens
`2.11.0` When using authentication with your FastMCP server, you can access the authenticated user’s access token information using the `get_access_token()` dependency function:
Copy
```
from fastmcp import FastMCP
from fastmcp.server.dependencies import get_access_token, AccessToken

mcp = FastMCP(name="Auth Token Demo")

@mcp.tool
async def get_user_info() -> dict:
    """Get information about the authenticated user."""
    # Get the access token (None if not authenticated)
    token: AccessToken | None = get_access_token()

    if token is None:
        return {"authenticated": False}

    return {
        "authenticated": True,
        "client_id": token.client_id,
        "scopes": token.scopes,
        "expires_at": token.expires_at,
        "token_claims": token.claims,  # JWT claims or custom token data
    }

```

This is particularly useful when you need to:
  1. **Access user identification** - Get the `client_id` or subject from token claims
  2. **Check permissions** - Verify scopes or custom claims before performing operations
  3. **Multi-tenant applications** - Extract tenant information from token claims
  4. **Audit logging** - Track which user performed which actions


####
[​](https://gofastmcp.com/v2/servers/context#working-with-token-claims)
Working with Token Claims
The `claims` field contains all the data from the original token (JWT claims for JWT tokens, or custom data for other token types):
Copy
```
from fastmcp import FastMCP
from fastmcp.server.dependencies import get_access_token

mcp = FastMCP(name="Multi-tenant Demo")

@mcp.tool
async def get_tenant_data(resource_id: str) -> dict:
    """Get tenant-specific data using token claims."""
    token: AccessToken | None = get_access_token()

    # Extract tenant ID from token claims
    tenant_id = token.claims.get("tenant_id") if token else None

    # Extract user ID from standard JWT subject claim
    user_id = token.claims.get("sub") if token else None

    # Use tenant and user info to authorize and filter data
    if not tenant_id:
        raise ValueError("No tenant information in token")

    return {
        "resource_id": resource_id,
        "tenant_id": tenant_id,
        "user_id": user_id,
        "data": f"Tenant-specific data for {tenant_id}",
    }

```

##
[​](https://gofastmcp.com/v2/servers/context#custom-dependencies)
Custom Dependencies
`2.14` FastMCP’s dependency injection is powered by `CurrentContext()`, you can create your own.
###
[​](https://gofastmcp.com/v2/servers/context#using-depends)
Using `Depends()`
The simplest way to create a custom dependency is with `Depends()`. Pass any callable (sync or async function, or async context manager) and its return value will be injected:
Copy
```
from contextlib import asynccontextmanager
from fastmcp import FastMCP
from fastmcp.dependencies import Depends

mcp = FastMCP(name="Custom Deps Demo")

# Simple function dependency
def get_config() -> dict:
    return {"api_url": "https://api.example.com", "timeout": 30}

# Async function dependency
async def get_user_id() -> int:
    return 42

@mcp.tool
async def fetch_data(
    query: str,
    config: dict = Depends(get_config),
    user_id: int = Depends(get_user_id),
) -> str:
    return f"User {user_id} fetching '{query}' from {config['api_url']}"

```

Dependencies using `Depends()` are automatically excluded from the MCP schema—clients never see them as parameters.
###
[​](https://gofastmcp.com/v2/servers/context#resource-management-with-context-managers)
Resource Management with Context Managers
For dependencies that need cleanup (database connections, file handles, etc.), use an async context manager:
Copy
```
from contextlib import asynccontextmanager
from fastmcp import FastMCP
from fastmcp.dependencies import Depends

mcp = FastMCP(name="Resource Demo")

@asynccontextmanager
async def get_database():
    db = await connect_to_database()
    try:
        yield db
    finally:
        await db.close()

@mcp.tool
async def query_users(sql: str, db = Depends(get_database)) -> list:
    return await db.execute(sql)

```

The context manager’s cleanup code runs after your function completes, even if an error occurs.
###
[​](https://gofastmcp.com/v2/servers/context#nested-dependencies)
Nested Dependencies
Dependencies can depend on other dependencies:
Copy
```
from fastmcp import FastMCP
from fastmcp.dependencies import Depends

mcp = FastMCP(name="Nested Demo")

def get_base_url() -> str:
    return "https://api.example.com"

def get_api_client(base_url: str = Depends(get_base_url)) -> dict:
    return {"base_url": base_url, "version": "v1"}

@mcp.tool
async def call_api(endpoint: str, client: dict = Depends(get_api_client)) -> str:
    return f"Calling {client['base_url']}/{client['version']}/{endpoint}"

```

###
[​](https://gofastmcp.com/v2/servers/context#advanced-subclassing-dependency)
Advanced: Subclassing `Dependency`
For more complex dependency patterns—like dependencies that need access to Docket’s execution context or require custom lifecycle management—you can subclass Docket’s `Dependency` class. See the
[ Server Composition Previous ](https://gofastmcp.com/v2/servers/composition)[ User Elicitation Next ](https://gofastmcp.com/v2/servers/elicitation)
Ctrl+I
