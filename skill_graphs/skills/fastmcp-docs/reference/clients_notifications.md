[Skip to main content](https://gofastmcp.com/clients/notifications#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
Search...
Navigation
Handlers
Notifications
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
  * [Handling Notifications](https://gofastmcp.com/clients/notifications#handling-notifications)
  * [MessageHandler Class](https://gofastmcp.com/clients/notifications#messagehandler-class)
  * [Handler Template](https://gofastmcp.com/clients/notifications#handler-template)
  * [List Change Notifications](https://gofastmcp.com/clients/notifications#list-change-notifications)
  * [Server Requests](https://gofastmcp.com/clients/notifications#server-requests)


Handlers
# Notifications
Copy page
Handle server-sent notifications for list changes and other events.
Copy page
`2.9.1` Use this when you need to react to server-side changes like tool list updates or resource modifications. MCP servers can send notifications to inform clients about state changes. The message handler provides a unified way to process these notifications.
##
[​](https://gofastmcp.com/clients/notifications#handling-notifications)
Handling Notifications
The simplest approach is a function that receives all messages and filters for the notifications you care about:
Copy
```
from fastmcp import Client

async def message_handler(message):
    """Handle MCP notifications from the server."""
    if hasattr(message, 'root'):
        method = message.root.method

        if method == "notifications/tools/list_changed":
            print("Tools have changed - refresh tool cache")
        elif method == "notifications/resources/list_changed":
            print("Resources have changed")
        elif method == "notifications/prompts/list_changed":
            print("Prompts have changed")

client = Client(
    "my_mcp_server.py",
    message_handler=message_handler,
)

```

##
[​](https://gofastmcp.com/clients/notifications#messagehandler-class)
MessageHandler Class
For fine-grained targeting, subclass `MessageHandler` to use specific hooks:
Copy
```
from fastmcp import Client
from fastmcp.client.messages import MessageHandler
import mcp.types

class MyMessageHandler(MessageHandler):
    async def on_tool_list_changed(
        self, notification: mcp.types.ToolListChangedNotification
    ) -> None:
        """Handle tool list changes."""
        print("Tool list changed - refreshing available tools")

    async def on_resource_list_changed(
        self, notification: mcp.types.ResourceListChangedNotification
    ) -> None:
        """Handle resource list changes."""
        print("Resource list changed")

    async def on_prompt_list_changed(
        self, notification: mcp.types.PromptListChangedNotification
    ) -> None:
        """Handle prompt list changes."""
        print("Prompt list changed")

client = Client(
    "my_mcp_server.py",
    message_handler=MyMessageHandler(),
)

```

###
[​](https://gofastmcp.com/clients/notifications#handler-template)
Handler Template
Copy
```
from fastmcp.client.messages import MessageHandler
import mcp.types

class MyMessageHandler(MessageHandler):
    async def on_message(self, message) -> None:
        """Called for ALL messages (requests and notifications)."""
        pass

    async def on_notification(
        self, notification: mcp.types.ServerNotification
    ) -> None:
        """Called for notifications (fire-and-forget)."""
        pass

    async def on_tool_list_changed(
        self, notification: mcp.types.ToolListChangedNotification
    ) -> None:
        """Called when the server's tool list changes."""
        pass

    async def on_resource_list_changed(
        self, notification: mcp.types.ResourceListChangedNotification
    ) -> None:
        """Called when the server's resource list changes."""
        pass

    async def on_prompt_list_changed(
        self, notification: mcp.types.PromptListChangedNotification
    ) -> None:
        """Called when the server's prompt list changes."""
        pass

    async def on_progress(
        self, notification: mcp.types.ProgressNotification
    ) -> None:
        """Called for progress updates during long-running operations."""
        pass

    async def on_logging_message(
        self, notification: mcp.types.LoggingMessageNotification
    ) -> None:
        """Called for log messages from the server."""
        pass

```

##
[​](https://gofastmcp.com/clients/notifications#list-change-notifications)
List Change Notifications
A practical example of maintaining a tool cache that refreshes when tools change:
Copy
```
from fastmcp import Client
from fastmcp.client.messages import MessageHandler
import mcp.types

class ToolCacheHandler(MessageHandler):
    def __init__(self):
        self.cached_tools = []

    async def on_tool_list_changed(
        self, notification: mcp.types.ToolListChangedNotification
    ) -> None:
        """Clear tool cache when tools change."""
        print("Tools changed - clearing cache")
        self.cached_tools = []  # Force refresh on next access

client = Client("server.py", message_handler=ToolCacheHandler())

```

##
[​](https://gofastmcp.com/clients/notifications#server-requests)
Server Requests
While the message handler receives server-initiated requests, you should use dedicated callback parameters for most interactive scenarios:
  * **Sampling requests** : Use [`sampling_handler`](https://gofastmcp.com/clients/sampling)
  * **Elicitation requests** : Use [`elicitation_handler`](https://gofastmcp.com/clients/elicitation)
  * **Progress updates** : Use [`progress_handler`](https://gofastmcp.com/clients/progress)
  * **Log messages** : Use [`log_handler`](https://gofastmcp.com/clients/logging)

The message handler is primarily for monitoring and handling notifications rather than responding to requests.
[ Getting Prompts Previous ](https://gofastmcp.com/clients/prompts)[ LLM Sampling Next ](https://gofastmcp.com/clients/sampling)
Ctrl+I
