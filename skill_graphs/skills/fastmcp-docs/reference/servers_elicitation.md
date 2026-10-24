[Skip to main content](https://gofastmcp.com/servers/elicitation#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
Search...
Navigation
Features
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
  * [Overview](https://gofastmcp.com/servers/elicitation#overview)
  * [Multi-Turn Elicitation](https://gofastmcp.com/servers/elicitation#multi-turn-elicitation)
  * [Client Requirements](https://gofastmcp.com/servers/elicitation#client-requirements)
  * [Schema and Response Types](https://gofastmcp.com/servers/elicitation#schema-and-response-types)
  * [Scalar Types](https://gofastmcp.com/servers/elicitation#scalar-types)
  * [No Response](https://gofastmcp.com/servers/elicitation#no-response)
  * [Constrained Options](https://gofastmcp.com/servers/elicitation#constrained-options)
  * [Multi-Select](https://gofastmcp.com/servers/elicitation#multi-select)
  * [Titled Options](https://gofastmcp.com/servers/elicitation#titled-options)
  * [Structured Responses](https://gofastmcp.com/servers/elicitation#structured-responses)
  * [Default Values](https://gofastmcp.com/servers/elicitation#default-values)


Features
# User Elicitation
Copy page
Request structured input from users during tool execution through the MCP context.
Copy page
`2.10.0` User elicitation allows MCP servers to request structured input from users during tool execution. Instead of requiring all inputs upfront, tools can interactively ask for missing parameters, clarification, or additional context as needed. Elicitation enables tools to pause execution and request specific information from users:
  * **Missing parameters** : Ask for required information not provided initially
  * **Clarification requests** : Get user confirmation or choices for ambiguous scenarios
  * **Progressive disclosure** : Collect complex information step-by-step
  * **Dynamic workflows** : Adapt tool behavior based on user responses

For example, a file management tool might ask “Which directory should I create?” or a data analysis tool might request “What date range should I analyze?”
##
[​](https://gofastmcp.com/servers/elicitation#overview)
Overview
Use the `ctx.elicit()` method within any tool function to request user input. Specify the message to display and the type of response you expect.
Copy
```
from fastmcp import FastMCP, Context
from dataclasses import dataclass

mcp = FastMCP("Elicitation Server")

@dataclass
class UserInfo:
    name: str
    age: int

@mcp.tool
async def collect_user_info(ctx: Context) -> str:
    """Collect user information through interactive prompts."""
    result = await ctx.elicit(
        message="Please provide your information",
        response_type=UserInfo
    )

    if result.action == "accept":
        user = result.data
        return f"Hello {user.name}, you are {user.age} years old"
    elif result.action == "decline":
        return "Information not provided"
    else:  # cancel
        return "Operation cancelled"

```

The elicitation result contains an `action` field indicating how the user responded:
Action | Description
---|---
`accept` | User provided valid input—data is available in the `data` field
`decline` | User chose not to provide the requested information
`cancel` | User cancelled the entire operation
FastMCP also provides typed result classes for pattern matching:
Copy
```
from fastmcp.server.elicitation import (
    AcceptedElicitation,
    DeclinedElicitation,
    CancelledElicitation,
)

@mcp.tool
async def pattern_example(ctx: Context) -> str:
    result = await ctx.elicit("Enter your name:", response_type=str)

    match result:
        case AcceptedElicitation(data=name):
            return f"Hello {name}!"
        case DeclinedElicitation():
            return "No name provided"
        case CancelledElicitation():
            return "Operation cancelled"

```

###
[​](https://gofastmcp.com/servers/elicitation#multi-turn-elicitation)
Multi-Turn Elicitation
Tools can make multiple elicitation calls to gather information progressively:
Copy
```
@mcp.tool
async def plan_meeting(ctx: Context) -> str:
    """Plan a meeting by gathering details step by step."""

    title_result = await ctx.elicit("What's the meeting title?", response_type=str)
    if title_result.action != "accept":
        return "Meeting planning cancelled"

    duration_result = await ctx.elicit("Duration in minutes?", response_type=int)
    if duration_result.action != "accept":
        return "Meeting planning cancelled"

    priority_result = await ctx.elicit(
        "Is this urgent?",
        response_type=["yes", "no"]
    )
    if priority_result.action != "accept":
        return "Meeting planning cancelled"

    urgent = priority_result.data == "yes"
    return f"Meeting '{title_result.data}' for {duration_result.data} minutes (Urgent: {urgent})"

```

###
[​](https://gofastmcp.com/servers/elicitation#client-requirements)
Client Requirements
Elicitation requires the client to implement an elicitation handler. If a client doesn’t support elicitation, calls to `ctx.elicit()` will raise an error indicating that elicitation is not supported. See [Client Elicitation](https://gofastmcp.com/clients/elicitation) for details on how clients handle these requests.
##
[​](https://gofastmcp.com/servers/elicitation#schema-and-response-types)
Schema and Response Types
The server must send a schema to the client indicating the type of data it expects in response to the elicitation request. The MCP spec only supports a limited subset of JSON Schema types for elicitation responses—specifically JSON **objects** with **primitive** properties including `string`, `number` (or `integer`), `boolean`, and `enum` fields. FastMCP makes it easy to request a broader range of types, including scalars (e.g. `str`) or no response at all, by automatically wrapping them in MCP-compatible object schemas.
###
[​](https://gofastmcp.com/servers/elicitation#scalar-types)
Scalar Types
You can request simple scalar data types for basic input, such as a string, integer, or boolean. When you request a scalar type, FastMCP automatically wraps it in an object schema for MCP spec compatibility. Clients will see a schema requesting a single “value” field of the requested type. Once clients respond, the provided object is “unwrapped” and the scalar value is returned directly in the `data` field.
String
Integer
Boolean
Copy
```
@mcp.tool
async def get_user_name(ctx: Context) -> str:
    result = await ctx.elicit("What's your name?", response_type=str)

    if result.action == "accept":
        return f"Hello, {result.data}!"
    return "No name provided"

```

###
[​](https://gofastmcp.com/servers/elicitation#no-response)
No Response
Sometimes, the goal of an elicitation is to simply get a user to approve or reject an action. Pass `None` as the response type to indicate that no data is expected. The `data` field will be `None` when the user accepts.
Copy
```
@mcp.tool
async def approve_action(ctx: Context) -> str:
    result = await ctx.elicit("Approve this action?", response_type=None)

    if result.action == "accept":
        return do_action()
    else:
        raise ValueError("Action rejected")

```

###
[​](https://gofastmcp.com/servers/elicitation#constrained-options)
Constrained Options
Constrain the user’s response to a specific set of values using a `Literal` type, Python enum, or a list of strings as a convenient shortcut.
List of strings
Literal type
Python enum
Copy
```
@mcp.tool
async def set_priority(ctx: Context) -> str:
    result = await ctx.elicit(
        "What priority level?",
        response_type=["low", "medium", "high"],
    )

    if result.action == "accept":
        return f"Priority set to: {result.data}"

```

###
[​](https://gofastmcp.com/servers/elicitation#multi-select)
Multi-Select
`2.14.0` Enable multi-select by wrapping your choices in an additional list level. This allows users to select multiple values from the available options.
List of strings
list[Enum] type
Copy
```
@mcp.tool
async def select_tags(ctx: Context) -> str:
    result = await ctx.elicit(
        "Choose tags",
        response_type=[["bug", "feature", "documentation"]]  # Note: list of a list
    )

    if result.action == "accept":
        tags = result.data
        return f"Selected tags: {', '.join(tags)}"

```

###
[​](https://gofastmcp.com/servers/elicitation#titled-options)
Titled Options
`2.14.0` For better UI display, provide human-readable titles for enum options. FastMCP generates SEP-1330 compliant schemas using the `oneOf` pattern with `const` and `title` fields.
Copy
```
@mcp.tool
async def set_priority(ctx: Context) -> str:
    result = await ctx.elicit(
        "What priority level?",
        response_type={
            "low": {"title": "Low Priority"},
            "medium": {"title": "Medium Priority"},
            "high": {"title": "High Priority"}
        }
    )

    if result.action == "accept":
        return f"Priority set to: {result.data}"

```

For multi-select with titles, wrap the dict in a list:
Copy
```
@mcp.tool
async def select_priorities(ctx: Context) -> str:
    result = await ctx.elicit(
        "Choose priorities",
        response_type=[{
            "low": {"title": "Low Priority"},
            "medium": {"title": "Medium Priority"},
            "high": {"title": "High Priority"}
        }]
    )

    if result.action == "accept":
        return f"Selected: {', '.join(result.data)}"

```

###
[​](https://gofastmcp.com/servers/elicitation#structured-responses)
Structured Responses
Request structured data with multiple fields by using a dataclass, typed dict, or Pydantic model as the response type. Note that the MCP spec only supports shallow objects with scalar (string, number, boolean) or enum properties.
Copy
```
from dataclasses import dataclass
from typing import Literal

@dataclass
class TaskDetails:
    title: str
    description: str
    priority: Literal["low", "medium", "high"]
    due_date: str

@mcp.tool
async def create_task(ctx: Context) -> str:
    result = await ctx.elicit(
        "Please provide task details",
        response_type=TaskDetails
    )

    if result.action == "accept":
        task = result.data
        return f"Created task: {task.title} (Priority: {task.priority})"
    return "Task creation cancelled"

```

###
[​](https://gofastmcp.com/servers/elicitation#default-values)
Default Values
`2.14.0` Provide default values for elicitation fields using Pydantic’s `Field(default=...)`. Clients will pre-populate form fields with these defaults. Fields with default values are automatically marked as optional.
Copy
```
from pydantic import BaseModel, Field
from enum import Enum

class Priority(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class TaskDetails(BaseModel):
    title: str = Field(description="Task title")
    description: str = Field(default="", description="Task description")
    priority: Priority = Field(default=Priority.MEDIUM, description="Task priority")

@mcp.tool
async def create_task(ctx: Context) -> str:
    result = await ctx.elicit("Please provide task details", response_type=TaskDetails)
    if result.action == "accept":
        return f"Created: {result.data.title}"
    return "Task creation cancelled"

```

Default values are supported for strings, integers, numbers, booleans, and enums.
[ Dependency Injection Previous ](https://gofastmcp.com/servers/dependency-injection)[ Icons Next ](https://gofastmcp.com/servers/icons)
Ctrl+I
