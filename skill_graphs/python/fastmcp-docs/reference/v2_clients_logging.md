[Skip to main content](https://gofastmcp.com/v2/clients/logging#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v2.14.5
Search...
Navigation
Advanced Features
Server Logging
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
  * Authentication
  * Deployment


##### Clients
  * Essentials
  * Core Operations
  * Advanced Features
    * [Elicitation](https://gofastmcp.com/v2/clients/elicitation)
    * [Logging](https://gofastmcp.com/v2/clients/logging)
    * [Progress](https://gofastmcp.com/v2/clients/progress)
    * [Sampling](https://gofastmcp.com/v2/clients/sampling)
    * [ Background Tasks NEW ](https://gofastmcp.com/v2/clients/tasks)
    * [Messages](https://gofastmcp.com/v2/clients/messages)
    * [Roots](https://gofastmcp.com/v2/clients/roots)
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
  * [Log Handler](https://gofastmcp.com/v2/clients/logging#log-handler)
  * [Handling Structured Logs](https://gofastmcp.com/v2/clients/logging#handling-structured-logs)
  * [Handler Parameters](https://gofastmcp.com/v2/clients/logging#handler-parameters)
  * [Default Log Handling](https://gofastmcp.com/v2/clients/logging#default-log-handling)


Advanced Features
# Server Logging
Copy page
Receive and handle log messages from MCP servers.
Copy page
`2.0.0` MCP servers can emit log messages to clients. The client can handle these logs through a log handler callback.
##
[​](https://gofastmcp.com/v2/clients/logging#log-handler)
Log Handler
Provide a `log_handler` function when creating the client. For robust logging, the log messages can be integrated with Python’s standard `logging` module.
Copy
```
import logging
from fastmcp import Client
from fastmcp.client.logging import LogMessage

# In a real app, you might configure this in your main entry point
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Get a logger for the module where the client is used
logger = logging.getLogger(__name__)

# This mapping is useful for converting MCP level strings to Python's levels
LOGGING_LEVEL_MAP = logging.getLevelNamesMapping()

async def log_handler(message: LogMessage):
    """
    Handles incoming logs from the MCP server and forwards them
    to the standard Python logging system.
    """
    msg = message.data.get('msg')
    extra = message.data.get('extra')

    # Convert the MCP log level to a Python log level
    level = LOGGING_LEVEL_MAP.get(message.level.upper(), logging.INFO)

    # Log the message using the standard logging library
    logger.log(level, msg, extra=extra)


client = Client(
    "my_mcp_server.py",
    log_handler=log_handler,
)

```

##
[​](https://gofastmcp.com/v2/clients/logging#handling-structured-logs)
Handling Structured Logs
The `message.data` attribute is a dictionary that contains the log payload from the server. This enables structured logging, allowing you to receive rich, contextual information. The dictionary contains two keys:
  * `msg`: The string log message.
  * `extra`: A dictionary containing any extra data sent from the server.

This structure is preserved even when logs are forwarded through a FastMCP proxy, making it a powerful tool for debugging complex, multi-server applications.
###
[​](https://gofastmcp.com/v2/clients/logging#handler-parameters)
Handler Parameters
The `log_handler` is called every time a log message is received. It receives a `LogMessage` object:
## Log Handler Parameters
[​](https://gofastmcp.com/v2/clients/logging#param-log-message)
LogMessage
Log Message Object
Show attributes
[​](https://gofastmcp.com/v2/clients/logging#param-level)
level
Literal["debug", "info", "notice", "warning", "error", "critical", "alert", "emergency"]
The log level
[​](https://gofastmcp.com/v2/clients/logging#param-logger)
logger
str | None
The logger name (optional, may be None)
[​](https://gofastmcp.com/v2/clients/logging#param-data)
data
dict
The log payload, containing `msg` and `extra` keys.
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

##
[​](https://gofastmcp.com/v2/clients/logging#default-log-handling)
Default Log Handling
If you don’t provide a custom `log_handler`, FastMCP’s default handler routes server logs to the appropriate Python logging levels. The MCP levels are mapped as follows: `notice` → INFO; `alert` and `emergency` → CRITICAL. If the server includes a logger name, it is prefixed in the message, and any `extra` data is forwarded via the logging `extra` parameter.
Copy
```
client = Client("my_mcp_server.py")

async with client:
    # Server logs are forwarded at their proper severity (DEBUG/INFO/WARNING/ERROR/CRITICAL)
    await client.call_tool("some_tool")

```

[ User Elicitation Previous ](https://gofastmcp.com/v2/clients/elicitation)[ Progress Monitoring Next ](https://gofastmcp.com/v2/clients/progress)
Ctrl+I
