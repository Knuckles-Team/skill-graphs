[Skip to main content](https://gofastmcp.com/v2/clients/elicitation#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v2.14.5
Search...
Navigation
Advanced Features
User Elicitation
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
  * [What is Elicitation?](https://gofastmcp.com/v2/clients/elicitation#what-is-elicitation)
  * [How FastMCP Makes Elicitation Easy](https://gofastmcp.com/v2/clients/elicitation#how-fastmcp-makes-elicitation-easy)
  * [Elicitation Handler](https://gofastmcp.com/v2/clients/elicitation#elicitation-handler)
  * [Handler Parameters](https://gofastmcp.com/v2/clients/elicitation#handler-parameters)
  * [Response Actions](https://gofastmcp.com/v2/clients/elicitation#response-actions)
  * [Basic Example](https://gofastmcp.com/v2/clients/elicitation#basic-example)


Advanced Features
# User Elicitation
Copy page
Handle server-initiated user input requests with structured schemas.
Copy page
`2.10.0`
##
[​](https://gofastmcp.com/v2/clients/elicitation#what-is-elicitation)
What is Elicitation?
Elicitation allows MCP servers to request structured input from users during tool execution. Instead of requiring all inputs upfront, servers can interactively ask users for information as needed - like prompting for missing parameters, requesting clarification, or gathering additional context. For example, a file management tool might ask “Which directory should I create?” or a data analysis tool might request “What date range should I analyze?”
##
[​](https://gofastmcp.com/v2/clients/elicitation#how-fastmcp-makes-elicitation-easy)
How FastMCP Makes Elicitation Easy
FastMCP’s client provides a helpful abstraction layer that:
  * **Converts JSON schemas to Python types** : The raw MCP protocol uses JSON schemas, but FastMCP automatically converts these to Python dataclasses
  * **Provides structured constructors** : Instead of manually building dictionaries that match the schema, you get dataclass constructors that ensure correct structure
  * **Handles type conversion** : FastMCP takes care of converting between JSON representations and Python objects
  * **Runtime introspection** : You can inspect the generated dataclass fields to understand the expected structure

When you implement an elicitation handler, FastMCP gives you a dataclass type that matches the server’s schema, making it easy to create properly structured responses without having to manually parse JSON schemas.
##
[​](https://gofastmcp.com/v2/clients/elicitation#elicitation-handler)
Elicitation Handler
Provide an `elicitation_handler` function when creating the client. FastMCP automatically converts the server’s JSON schema into a Python dataclass type, making it easy to construct the response:
Copy
```
from fastmcp import Client
from fastmcp.client.elicitation import ElicitResult

async def elicitation_handler(message: str, response_type: type, params, context):
    # Present the message to the user and collect input
    user_input = input(f"{message}: ")

    # Create response using the provided dataclass type
    # FastMCP converted the JSON schema to this Python type for you
    response_data = response_type(value=user_input)

    # You can return data directly - FastMCP will implicitly accept the elicitation
    return response_data

    # Or explicitly return an ElicitResult for more control
    # return ElicitResult(action="accept", content=response_data)

client = Client(
    "my_mcp_server.py",
    elicitation_handler=elicitation_handler,
)

```

###
[​](https://gofastmcp.com/v2/clients/elicitation#handler-parameters)
Handler Parameters
The elicitation handler receives four parameters:
## Elicitation Handler Parameters
[​](https://gofastmcp.com/v2/clients/elicitation#param-message)
message
str
The prompt message to display to the user
[​](https://gofastmcp.com/v2/clients/elicitation#param-response-type)
response_type
type
A Python dataclass type that FastMCP created from the server’s JSON schema. Use this to construct your response with proper typing and IDE support. If the server requests an empty object (indicating no response), this will be `None`.
[​](https://gofastmcp.com/v2/clients/elicitation#param-params)
params
ElicitRequestParams
The original MCP elicitation request parameters, including the raw JSON schema in `params.requestedSchema` if you need it
[​](https://gofastmcp.com/v2/clients/elicitation#param-context)
context
RequestContext
Request context containing metadata about the elicitation request
###
[​](https://gofastmcp.com/v2/clients/elicitation#response-actions)
Response Actions
The handler can return data directly (which implicitly accepts the elicitation) or an `ElicitResult` object for more control over the response action:
## ElicitResult Structure
[​](https://gofastmcp.com/v2/clients/elicitation#param-action)
action
Literal['accept', 'decline', 'cancel']
How the user responded to the elicitation request
[​](https://gofastmcp.com/v2/clients/elicitation#param-content)
content
dataclass instance | dict | None
The user’s input data (required for “accept”, omitted for “decline”/“cancel”)
**Action Types:**
  * **`accept`**: User provided valid input - include their data in the`content` field
  * **`decline`**: User chose not to provide the requested information - omit`content`
  * **`cancel`**: User cancelled the entire operation - omit`content`


##
[​](https://gofastmcp.com/v2/clients/elicitation#basic-example)
Basic Example
Copy
```
from fastmcp import Client
from fastmcp.client.elicitation import ElicitResult

async def basic_elicitation_handler(message: str, response_type: type, params, context):
    print(f"Server asks: {message}")

    # Simple text input for demonstration
    user_response = input("Your response: ")

    if not user_response:
        # For non-acceptance, use ElicitResult explicitly
        return ElicitResult(action="decline")

    # Use the response_type dataclass to create a properly structured response
    # FastMCP handles the conversion from JSON schema to Python type
    # Return data directly - FastMCP will implicitly accept the elicitation
    return response_type(value=user_response)

client = Client(
    "my_mcp_server.py",
    elicitation_handler=basic_elicitation_handler
)

```

[ Prompts Previous ](https://gofastmcp.com/v2/clients/prompts)[ Server Logging Next ](https://gofastmcp.com/v2/clients/logging)
Ctrl+I
