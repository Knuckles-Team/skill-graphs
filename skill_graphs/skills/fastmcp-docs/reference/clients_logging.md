[Skip to main content](https://gofastmcp.com/clients/logging#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
Search...
Navigation
Handlers
Server Logging
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
    * [Notifications](https://gofastmcp.com/clients/notifications)
    * [Sampling](https://gofastmcp.com/clients/sampling)
    * [Elicitation](https://gofastmcp.com/clients/elicitation)
    * [ Tasks NEW ](https://gofastmcp.com/clients/tasks)
    * [Progress](https://gofastmcp.com/clients/progress)
    * [Logging](https://gofastmcp.com/clients/logging)
    * [Roots](https://gofastmcp.com/clients/roots)
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
  * [Log Handler](https://gofastmcp.com/clients/logging#log-handler)
  * [Structured Logs](https://gofastmcp.com/clients/logging#structured-logs)
  * [Default Behavior](https://gofastmcp.com/clients/logging#default-behavior)


Handlers
# Server Logging
Copy page
Receive and handle log messages from MCP servers.
Copy page
`2.0.0` Use this when you need to capture or process log messages sent by the server. MCP servers can emit log messages to clients. The client handles these through a log handler callback.
##
[​](https://gofastmcp.com/clients/logging#log-handler)
Log Handler
Provide a `log_handler` function when creating the client:
Copy
```
import logging
from fastmcp import Client
from fastmcp.client.logging import LogMessage

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)
LOGGING_LEVEL_MAP = logging.getLevelNamesMapping()

async def log_handler(message: LogMessage):
    """Forward MCP server logs to Python's logging system."""
    msg = message.data.get('msg')
    extra = message.data.get('extra')

    level = LOGGING_LEVEL_MAP.get(message.level.upper(), logging.INFO)
    logger.log(level, msg, extra=extra)

client = Client(
    "my_mcp_server.py",
    log_handler=log_handler,
)

```

The handler receives a `LogMessage` object:
## LogMessage
[​](https://gofastmcp.com/clients/logging#param-level)
level
Literal["debug", "info", "notice", "warning", "error", "critical", "alert", "emergency"]
The log level
[​](https://gofastmcp.com/clients/logging#param-logger)
logger
str | None
The logger name (may be None)
[​](https://gofastmcp.com/clients/logging#param-data)
data
dict
The log payload, containing `msg` and `extra` keys
##
[​](https://gofastmcp.com/clients/logging#structured-logs)
Structured Logs
The `message.data` attribute is a dictionary containing the log payload. This enables structured logging with rich contextual information.
Copy
```
async def detailed_log_handler(message: LogMessage):
    msg = message.data.get('msg')
    extra = message.data.get('extra')

    if message.level == "error":
        print(f"ERROR: {msg} | Details: {extra}")
    elif message.level == "warning":
        print(f"WARNING: {msg} | Details: {extra}")
    else:
        print(f"{message.level.upper()}: {msg}")

```

This structure is preserved even when logs are forwarded through a FastMCP proxy, making it useful for debugging multi-server applications.
##
[​](https://gofastmcp.com/clients/logging#default-behavior)
Default Behavior
If you do not provide a custom `log_handler`, FastMCP’s default handler routes server logs to Python’s logging system at the appropriate severity level. The MCP levels map as follows: `notice` becomes INFO; `alert` and `emergency` become CRITICAL.
Copy
```
client = Client("my_mcp_server.py")

async with client:
    # Server logs are forwarded at proper severity automatically
    await client.call_tool("some_tool")

```

[ Progress Monitoring Previous ](https://gofastmcp.com/clients/progress)[ Client Roots Next ](https://gofastmcp.com/clients/roots)
Ctrl+I
