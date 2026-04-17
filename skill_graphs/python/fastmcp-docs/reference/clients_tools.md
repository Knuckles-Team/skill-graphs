[Skip to main content](https://gofastmcp.com/clients/tools#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
Search...
Navigation
Core Operations
Calling Tools
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
    * [Tools](https://gofastmcp.com/clients/tools)
    * [Resources](https://gofastmcp.com/clients/resources)
    * [Prompts](https://gofastmcp.com/clients/prompts)
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
  * [Basic Execution](https://gofastmcp.com/clients/tools#basic-execution)
  * [Execution Options](https://gofastmcp.com/clients/tools#execution-options)
  * [Structured Results](https://gofastmcp.com/clients/tools#structured-results)
  * [Error Handling](https://gofastmcp.com/clients/tools#error-handling)
  * [Sending Metadata](https://gofastmcp.com/clients/tools#sending-metadata)
  * [Raw Protocol Access](https://gofastmcp.com/clients/tools#raw-protocol-access)


Core Operations
# Calling Tools
Copy page
Execute server-side tools and handle structured results.
Copy page
`2.0.0` Use this when you need to execute server-side functions and process their results. Tools are executable functions exposed by MCP servers. The client’s `call_tool()` method executes a tool by name with arguments and returns structured results.
##
[​](https://gofastmcp.com/clients/tools#basic-execution)
Basic Execution
Copy
```
async with client:
    result = await client.call_tool("add", {"a": 5, "b": 3})
    # result -> CallToolResult with structured and unstructured data

    # Access structured data (automatically deserialized)
    print(result.data)  # 8

    # Access traditional content blocks
    print(result.content[0].text)  # "8"

```

Arguments are passed as a dictionary. For multi-server clients, tool names are automatically prefixed with the server name (e.g., `weather_get_forecast` for a tool named `get_forecast` on the `weather` server).
##
[​](https://gofastmcp.com/clients/tools#execution-options)
Execution Options
The `call_tool()` method supports timeout control and progress monitoring:
Copy
```
async with client:
    # With timeout (aborts if execution takes longer than 2 seconds)
    result = await client.call_tool(
        "long_running_task",
        {"param": "value"},
        timeout=2.0
    )

    # With progress handler
    result = await client.call_tool(
        "long_running_task",
        {"param": "value"},
        progress_handler=my_progress_handler
    )

```

##
[​](https://gofastmcp.com/clients/tools#structured-results)
Structured Results
`2.10.0` Tool execution returns a `CallToolResult` object. The `.data` property provides fully hydrated Python objects including complex types like datetimes and UUIDs, reconstructed from the server’s output schema.
Copy
```
from datetime import datetime
from uuid import UUID

async with client:
    result = await client.call_tool("get_weather", {"city": "London"})

    # FastMCP reconstructs complete Python objects
    weather = result.data
    print(f"Temperature: {weather.temperature}C at {weather.timestamp}")

    # Complex types are properly deserialized
    assert isinstance(weather.timestamp, datetime)
    assert isinstance(weather.station_id, UUID)

    # Raw structured JSON is also available
    print(f"Raw JSON: {result.structured_content}")

```

## CallToolResult Properties
[​](https://gofastmcp.com/clients/tools#param-data)
.data
Any
Fully hydrated Python objects with complex type support (datetimes, UUIDs, custom classes). FastMCP exclusive.
[​](https://gofastmcp.com/clients/tools#param-content)
.content
list[mcp.types.ContentBlock]
Standard MCP content blocks (`TextContent`, `ImageContent`, `AudioContent`, etc.).
[​](https://gofastmcp.com/clients/tools#param-structured-content)
.structured_content
dict[str, Any] | None
Standard MCP structured JSON data as sent by the server.
[​](https://gofastmcp.com/clients/tools#param-is-error)
.is_error
bool
Boolean indicating if the tool execution failed.
For tools without output schemas or when deserialization fails, `.data` will be `None`. Fall back to content blocks in that case:
Copy
```
async with client:
    result = await client.call_tool("legacy_tool", {"param": "value"})

    if result.data is not None:
        print(f"Structured: {result.data}")
    else:
        for content in result.content:
            if hasattr(content, 'text'):
                print(f"Text result: {content.text}")

```

FastMCP servers automatically wrap primitive results (like `int`, `str`, `bool`) in a `{"result": value}` structure. FastMCP clients automatically unwrap this, so you get the original value in `.data`.
##
[​](https://gofastmcp.com/clients/tools#error-handling)
Error Handling
By default, `call_tool()` raises a `ToolError` if the tool execution fails:
Copy
```
from fastmcp.exceptions import ToolError

async with client:
    try:
        result = await client.call_tool("potentially_failing_tool", {"param": "value"})
        print("Tool succeeded:", result.data)
    except ToolError as e:
        print(f"Tool failed: {e}")

```

To handle errors manually instead of catching exceptions, disable automatic error raising:
Copy
```
async with client:
    result = await client.call_tool(
        "potentially_failing_tool",
        {"param": "value"},
        raise_on_error=False
    )

    if result.is_error:
        print(f"Tool failed: {result.content[0].text}")
    else:
        print(f"Tool succeeded: {result.data}")

```

##
[​](https://gofastmcp.com/clients/tools#sending-metadata)
Sending Metadata
`2.13.1` The `meta` parameter sends ancillary information alongside tool calls for observability, debugging, or client identification:
Copy
```
async with client:
    result = await client.call_tool(
        name="send_email",
        arguments={
            "to": "user@example.com",
            "subject": "Hello",
            "body": "Welcome!"
        },
        meta={
            "trace_id": "abc-123",
            "request_source": "mobile_app"
        }
    )

```

See [Client Metadata](https://gofastmcp.com/servers/context#client-metadata) to learn how servers access this data.
##
[​](https://gofastmcp.com/clients/tools#raw-protocol-access)
Raw Protocol Access
For complete control, use `call_tool_mcp()` which returns the raw MCP protocol object:
Copy
```
async with client:
    result = await client.call_tool_mcp("my_tool", {"param": "value"})
    # result -> mcp.types.CallToolResult

    if result.isError:
        print(f"Tool failed: {result.content}")
    else:
        print(f"Tool succeeded: {result.content}")
        # Note: No automatic deserialization with call_tool_mcp()

```

[ Client Transports Previous ](https://gofastmcp.com/clients/transports)[ Reading Resources Next ](https://gofastmcp.com/clients/resources)
Ctrl+I
