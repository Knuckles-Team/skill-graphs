[Skip to main content](https://gofastmcp.com/clients/prompts#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
Search...
Navigation
Core Operations
Getting Prompts
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
  * [Basic Usage](https://gofastmcp.com/clients/prompts#basic-usage)
  * [Argument Serialization](https://gofastmcp.com/clients/prompts#argument-serialization)
  * [Working with Results](https://gofastmcp.com/clients/prompts#working-with-results)
  * [Version Selection](https://gofastmcp.com/clients/prompts#version-selection)
  * [Multi-Server Clients](https://gofastmcp.com/clients/prompts#multi-server-clients)
  * [Raw Protocol Access](https://gofastmcp.com/clients/prompts#raw-protocol-access)


Core Operations
# Getting Prompts
Copy page
Retrieve rendered message templates with automatic argument serialization.
Copy page
`2.0.0` Use this when you need to retrieve server-defined message templates for LLM interactions. Prompts are reusable message templates exposed by MCP servers. They can accept arguments to generate personalized message sequences for LLM interactions.
##
[​](https://gofastmcp.com/clients/prompts#basic-usage)
Basic Usage
Request a rendered prompt with `get_prompt()`:
Copy
```
async with client:
    # Simple prompt without arguments
    result = await client.get_prompt("welcome_message")
    # result -> mcp.types.GetPromptResult

    # Access the generated messages
    for message in result.messages:
        print(f"Role: {message.role}")
        print(f"Content: {message.content}")

```

Pass arguments to customize the prompt:
Copy
```
async with client:
    result = await client.get_prompt("user_greeting", {
        "name": "Alice",
        "role": "administrator"
    })

    for message in result.messages:
        print(f"Generated message: {message.content}")

```

##
[​](https://gofastmcp.com/clients/prompts#argument-serialization)
Argument Serialization
`2.9.0` FastMCP automatically serializes complex arguments to JSON strings as required by the MCP specification. You can pass typed objects directly:
Copy
```
from dataclasses import dataclass

@dataclass
class UserData:
    name: str
    age: int

async with client:
    result = await client.get_prompt("analyze_user", {
        "user": UserData(name="Alice", age=30),     # Automatically serialized
        "preferences": {"theme": "dark"},           # Dict serialized
        "scores": [85, 92, 78],                     # List serialized
        "simple_name": "Bob"                        # Strings unchanged
    })

```

The client handles serialization using `pydantic_core.to_json()` for consistent formatting. FastMCP servers automatically deserialize these JSON strings back to the expected types.
##
[​](https://gofastmcp.com/clients/prompts#working-with-results)
Working with Results
The `get_prompt()` method returns a `GetPromptResult` containing a list of messages:
Copy
```
async with client:
    result = await client.get_prompt("conversation_starter", {"topic": "climate"})

    for i, message in enumerate(result.messages):
        print(f"Message {i + 1}:")
        print(f"  Role: {message.role}")
        print(f"  Content: {message.content.text if hasattr(message.content, 'text') else message.content}")

```

Prompts can generate different message types. System messages configure LLM behavior:
Copy
```
async with client:
    result = await client.get_prompt("system_configuration", {
        "role": "helpful assistant",
        "expertise": "python programming"
    })

    # Access the returned messages
    message = result.messages[0]
    print(f"Prompt: {message.content}")

```

Conversation templates generate multi-turn flows:
Copy
```
async with client:
    result = await client.get_prompt("interview_template", {
        "candidate_name": "Alice",
        "position": "Senior Developer"
    })

    # Multiple messages for a conversation flow
    for message in result.messages:
        print(f"{message.role}: {message.content}")

```

##
[​](https://gofastmcp.com/clients/prompts#version-selection)
Version Selection
`3.0.0` When a server exposes multiple versions of a prompt, you can request a specific version:
Copy
```
async with client:
    # Get the highest version (default)
    result = await client.get_prompt("summarize", {"text": "..."})

    # Get a specific version
    result_v1 = await client.get_prompt("summarize", {"text": "..."}, version="1.0")

```

See [Metadata](https://gofastmcp.com/servers/versioning#version-discovery) for how to discover available versions.
##
[​](https://gofastmcp.com/clients/prompts#multi-server-clients)
Multi-Server Clients
When using multi-server clients, prompts are accessible directly without prefixing:
Copy
```
async with client:  # Multi-server client
    result1 = await client.get_prompt("weather_prompt", {"city": "London"})
    result2 = await client.get_prompt("assistant_prompt", {"query": "help"})

```

##
[​](https://gofastmcp.com/clients/prompts#raw-protocol-access)
Raw Protocol Access
For complete control, use `get_prompt_mcp()` which returns the full MCP protocol object:
Copy
```
async with client:
    result = await client.get_prompt_mcp("example_prompt", {"arg": "value"})
    # result -> mcp.types.GetPromptResult

```

[ Reading Resources Previous ](https://gofastmcp.com/clients/resources)[ Notifications Next ](https://gofastmcp.com/clients/notifications)
Ctrl+I
