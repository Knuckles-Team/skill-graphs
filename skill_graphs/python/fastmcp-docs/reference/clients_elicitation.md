[Skip to main content](https://gofastmcp.com/clients/elicitation#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
Search...
Navigation
Handlers
User Elicitation
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
  * [Handler Template](https://gofastmcp.com/clients/elicitation#handler-template)
  * [How It Works](https://gofastmcp.com/clients/elicitation#how-it-works)
  * [Response Actions](https://gofastmcp.com/clients/elicitation#response-actions)
  * [Example](https://gofastmcp.com/clients/elicitation#example)


Handlers
# User Elicitation
Copy page
Handle server requests for structured user input.
Copy page
`2.10.0` Use this when you need to respond to server requests for user input during tool execution. Elicitation allows MCP servers to request structured input from users during operations. Instead of requiring all inputs upfront, servers can interactively ask for missing parameters, request clarification, or gather additional context.
##
[​](https://gofastmcp.com/clients/elicitation#handler-template)
Handler Template
Copy
```
from fastmcp import Client
from fastmcp.client.elicitation import ElicitResult, ElicitRequestParams, RequestContext

async def elicitation_handler(
    message: str,
    response_type: type | None,
    params: ElicitRequestParams,
    context: RequestContext
) -> ElicitResult | object:
    """
    Handle server requests for user input.

    Args:
        message: The prompt to display to the user
        response_type: Python dataclass type for the response (None if no data expected)
        params: Original MCP elicitation parameters including raw JSON schema
        context: Request context with metadata

    Returns:
        - Data directly (implicitly accepts the elicitation)
        - ElicitResult for explicit control over the action
    """
    # Present the message and collect input
    user_input = input(f"{message}: ")

    if not user_input:
        return ElicitResult(action="decline")

    # Create response using the provided dataclass type
    return response_type(value=user_input)

client = Client(
    "my_mcp_server.py",
    elicitation_handler=elicitation_handler,
)

```

##
[​](https://gofastmcp.com/clients/elicitation#how-it-works)
How It Works
When a server needs user input, it sends an elicitation request with a message prompt and a JSON schema describing the expected response structure. FastMCP automatically converts this schema into a Python dataclass type, making it easy to construct properly typed responses without manually parsing JSON schemas. The handler receives four parameters:
## Handler Parameters
[​](https://gofastmcp.com/clients/elicitation#param-message)
message
str
The prompt message to display to the user
[​](https://gofastmcp.com/clients/elicitation#param-response-type)
response_type
type | None
A Python dataclass type that FastMCP created from the server’s JSON schema. Use this to construct your response with proper typing. If the server requests an empty object, this will be `None`.
[​](https://gofastmcp.com/clients/elicitation#param-params)
params
ElicitRequestParams
The original MCP elicitation parameters, including the raw JSON schema in `params.requestedSchema`
[​](https://gofastmcp.com/clients/elicitation#param-context)
context
RequestContext
Request context containing metadata about the elicitation request
##
[​](https://gofastmcp.com/clients/elicitation#response-actions)
Response Actions
You can return data directly, which implicitly accepts the elicitation:
Copy
```
async def elicitation_handler(message, response_type, params, context):
    user_input = input(f"{message}: ")
    return response_type(value=user_input)  # Implicit accept

```

Or return an `ElicitResult` for explicit control over the action:
Copy
```
from fastmcp.client.elicitation import ElicitResult

async def elicitation_handler(message, response_type, params, context):
    user_input = input(f"{message}: ")

    if not user_input:
        return ElicitResult(action="decline")  # User declined

    if user_input == "cancel":
        return ElicitResult(action="cancel")   # Cancel entire operation

    return ElicitResult(
        action="accept",
        content=response_type(value=user_input)
    )

```

**Action types:**
  * **`accept`**: User provided valid input. Include the data in the`content` field.
  * **`decline`**: User chose not to provide the requested information. Omit`content`.
  * **`cancel`**: User cancelled the entire operation. Omit`content`.


##
[​](https://gofastmcp.com/clients/elicitation#example)
Example
A file management tool might ask which directory to create:
Copy
```
from fastmcp import Client
from fastmcp.client.elicitation import ElicitResult

async def elicitation_handler(message, response_type, params, context):
    print(f"Server asks: {message}")

    user_response = input("Your response: ")

    if not user_response:
        return ElicitResult(action="decline")

    # Use the response_type dataclass to create a properly structured response
    return response_type(value=user_response)

client = Client(
    "my_mcp_server.py",
    elicitation_handler=elicitation_handler
)

```

[ LLM Sampling Previous ](https://gofastmcp.com/clients/sampling)[ Background Tasks Next ](https://gofastmcp.com/clients/tasks)
Ctrl+I
