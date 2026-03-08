[Skip to main content](https://gofastmcp.com/v2/servers/elicitation#content-area)
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
  * [What is Elicitation?](https://gofastmcp.com/v2/servers/elicitation#what-is-elicitation)
  * [Basic Usage](https://gofastmcp.com/v2/servers/elicitation#basic-usage)
  * [Method Signature](https://gofastmcp.com/v2/servers/elicitation#method-signature)
  * [Elicitation Actions](https://gofastmcp.com/v2/servers/elicitation#elicitation-actions)
  * [Response Types](https://gofastmcp.com/v2/servers/elicitation#response-types)
  * [Scalar Types](https://gofastmcp.com/v2/servers/elicitation#scalar-types)
  * [No Response](https://gofastmcp.com/v2/servers/elicitation#no-response)
  * [Constrained Options](https://gofastmcp.com/v2/servers/elicitation#constrained-options)
  * [Multi-Select](https://gofastmcp.com/v2/servers/elicitation#multi-select)
  * [Titled Options](https://gofastmcp.com/v2/servers/elicitation#titled-options)
  * [Structured Responses](https://gofastmcp.com/v2/servers/elicitation#structured-responses)
  * [Default Values](https://gofastmcp.com/v2/servers/elicitation#default-values)
  * [Multi-Turn Elicitation](https://gofastmcp.com/v2/servers/elicitation#multi-turn-elicitation)
  * [Client Requirements](https://gofastmcp.com/v2/servers/elicitation#client-requirements)


Advanced Features
# User Elicitation
Copy page
Request structured input from users during tool execution through the MCP context.
Copy page
`2.10.0` User elicitation allows MCP servers to request structured input from users during tool execution. Instead of requiring all inputs upfront, tools can interactively ask for missing parameters, clarification, or additional context as needed.
Most of the examples in this document assume you have a FastMCP server instance named `mcp` and show how to use the `ctx.elicit` method to request user input from an `@mcp.tool`-decorated function.
##
[​](https://gofastmcp.com/v2/servers/elicitation#what-is-elicitation)
What is Elicitation?
Elicitation enables tools to pause execution and request specific information from users. This is particularly useful for:
  * **Missing parameters** : Ask for required information not provided initially
  * **Clarification requests** : Get user confirmation or choices for ambiguous scenarios
  * **Progressive disclosure** : Collect complex information step-by-step
  * **Dynamic workflows** : Adapt tool behavior based on user responses

For example, a file management tool might ask “Which directory should I create?” or a data analysis tool might request “What date range should I analyze?”
###
[​](https://gofastmcp.com/v2/servers/elicitation#basic-usage)
Basic Usage
Use the `ctx.elicit()` method within any tool function to request user input:
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

##
[​](https://gofastmcp.com/v2/servers/elicitation#method-signature)
Method Signature
## Context Elicitation Method
[​](https://gofastmcp.com/v2/servers/elicitation#param-ctx-elicit)
ctx.elicit
async method
Show Parameters
[​](https://gofastmcp.com/v2/servers/elicitation#param-message)
message
str
The prompt message to display to the user
[​](https://gofastmcp.com/v2/servers/elicitation#param-response-type)
response_type
type
default:"None"
The Python type defining the expected response structure (dataclass, primitive type, etc.) Note that elicitation responses are subject to a restricted subset of JSON Schema types. See [Supported Response Types](https://gofastmcp.com/v2/servers/elicitation#supported-response-types) for more details.
Show Response
[​](https://gofastmcp.com/v2/servers/elicitation#param-elicitation-result)
ElicitationResult
object
Result object containing the user’s response
Show properties
[​](https://gofastmcp.com/v2/servers/elicitation#param-action)
action
Literal['accept', 'decline', 'cancel']
How the user responded to the request
[​](https://gofastmcp.com/v2/servers/elicitation#param-data)
data
response_type | None
The user’s input data (only present when action is “accept”)
##
[​](https://gofastmcp.com/v2/servers/elicitation#elicitation-actions)
Elicitation Actions
The elicitation result contains an `action` field indicating how the user responded:
  * **`accept`**: User provided valid input - data is available in the`data` field
  * **`decline`**: User chose not to provide the requested information and the data field is`None`
  * **`cancel`**: User cancelled the entire operation and the data field is`None`


Copy
```
@mcp.tool
async def my_tool(ctx: Context) -> str:
    result = await ctx.elicit("Choose an action")

    if result.action == "accept":
        return "Accepted!"
    elif result.action == "decline":
        return "Declined!"
    else:
        return "Cancelled!"

```

FastMCP also provides typed result classes for pattern matching on the `action` field:
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

##
[​](https://gofastmcp.com/v2/servers/elicitation#response-types)
Response Types
The server must send a schema to the client indicating the type of data it expects in response to the elicitation request. If the request is `accept`-ed, the client must send a response that matches the schema. The MCP spec only supports a limited subset of JSON Schema types for elicitation responses. Specifically, it only supports JSON **objects** with **primitive** properties including `string`, `number` (or `integer`), `boolean` and `enum` fields. FastMCP makes it easy to request a broader range of types, including scalars (e.g. `str`) or no response at all, by automatically wrapping them in MCP-compatible object schemas.
###
[​](https://gofastmcp.com/v2/servers/elicitation#scalar-types)
Scalar Types
You can request simple scalar data types for basic input, such as a string, integer, or boolean. When you request a scalar type, FastMCP automatically wraps it in an object schema for MCP spec compatibility. Clients will see a corresponding schema requesting a single “value” field of the requested type. Once clients respond, the provided object is “unwrapped” and the scalar value is returned to your tool function as the `data` field of the `ElicitationResult` object. As a developer, this means you do not have to worry about creating or accessing a structured object when you only need a scalar value.
Request a string
Request an integer
Request a boolean
Copy
```
@mcp.tool
async def get_user_name(ctx: Context) -> str:
    """Get the user's name."""
    result = await ctx.elicit("What's your name?", response_type=str)

    if result.action == "accept":
        return f"Hello, {result.data}!"
    return "No name provided"

```

###
[​](https://gofastmcp.com/v2/servers/elicitation#no-response)
No Response
Sometimes, the goal of an elicitation is to simply get a user to approve or reject an action. In this case, you can pass `None` as the response type to indicate that no response is expected. In order to comply with the MCP spec, the client will see a schema requesting an empty object in response. In this case, the `data` field of the `ElicitationResult` object will be `None` when the user accepts the elicitation.
No response
Copy
```
@mcp.tool
async def approve_action(ctx: Context) -> str:
    """Approve an action."""
    result = await ctx.elicit("Approve this action?", response_type=None)

    if result.action == "accept":
        return do_action()
    else:
        raise ValueError("Action rejected")

```

###
[​](https://gofastmcp.com/v2/servers/elicitation#constrained-options)
Constrained Options
Often you’ll want to constrain the user’s response to a specific set of values. You can do this by using a `Literal` type or a Python enum as the response type, or by passing a list of strings to the `response_type` parameter as a convenient shortcut.
Using a list of strings
Using a Literal type
Using a Python enum
Copy
```
@mcp.tool
async def set_priority(ctx: Context) -> str:
    """Set task priority level."""
    result = await ctx.elicit(
        "What priority level?",
        response_type=["low", "medium", "high"],
    )

    if result.action == "accept":
        return f"Priority set to: {result.data}"

```

####
[​](https://gofastmcp.com/v2/servers/elicitation#multi-select)
Multi-Select
`2.14.0` Enable multi-select by wrapping your choices in an additional list level. This allows users to select multiple values from the available options.
List of a list of strings
list[Enum] type annotation
Copy
```
@mcp.tool
async def select_tags(ctx: Context) -> str:
    """Select multiple tags."""
    result = await ctx.elicit(
        "Choose tags",
        response_type=[["bug", "feature", "documentation"]]  # Note: list of a list
    )

    if result.action == "accept":
        tags = result.data  # List of selected strings
        return f"Selected tags: {', '.join(tags)}"

```

For titled multi-select, wrap a dict in a list (see [Titled Options](https://gofastmcp.com/v2/servers/elicitation#titled-options) for dict syntax):
Copy
```
@mcp.tool
async def select_priorities(ctx: Context) -> str:
    """Select multiple priorities."""
    result = await ctx.elicit(
        "Choose priorities",
        response_type=[{  # Note: list containing a dict
            "low": {"title": "Low Priority"},
            "medium": {"title": "Medium Priority"},
            "high": {"title": "High Priority"}
        }]
    )

    if result.action == "accept":
        priorities = result.data  # List of selected strings
        return f"Selected: {', '.join(priorities)}"

```

####
[​](https://gofastmcp.com/v2/servers/elicitation#titled-options)
Titled Options
`2.14.0` For better UI display, you can provide human-readable titles for enum options. FastMCP generates SEP-1330 compliant schemas using the `oneOf` pattern with `const` and `title` fields. Use a dict to specify titles for enum values:
Copy
```
@mcp.tool
async def set_priority(ctx: Context) -> str:
    """Set task priority level."""
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
    """Select multiple priorities."""
    result = await ctx.elicit(
        "Choose priorities",
        response_type=[{  # List containing a dict for multi-select
            "low": {"title": "Low Priority"},
            "medium": {"title": "Medium Priority"},
            "high": {"title": "High Priority"}
        }]
    )

    if result.action == "accept":
        priorities = result.data  # List of selected strings
        return f"Selected: {', '.join(priorities)}"

```

###
[​](https://gofastmcp.com/v2/servers/elicitation#structured-responses)
Structured Responses
You can request structured data with multiple fields by using a dataclass, typed dict, or Pydantic model as the response type. Note that the MCP spec only supports shallow objects with scalar (string, number, boolean) or enum properties.
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
    """Create a new task with user-provided details."""
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
[​](https://gofastmcp.com/v2/servers/elicitation#default-values)
Default Values
`2.14.0` You can provide default values for elicitation fields using Pydantic’s `Field(default=...)`. Clients will pre-populate form fields with these defaults, making it easier for users to provide input. Default values are supported for all primitive types:
  * Strings: `Field(default="[email protected]")`
  * Integers: `Field(default=50)`
  * Numbers: `Field(default=3.14)`
  * Booleans: `Field(default=False)`
  * Enums: `Field(default=EnumValue.A)`

Fields with default values are automatically marked as optional (not included in the `required` list), so users can accept the default or provide their own value.
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

##
[​](https://gofastmcp.com/v2/servers/elicitation#multi-turn-elicitation)
Multi-Turn Elicitation
Tools can make multiple elicitation calls to gather information progressively:
Copy
```
@mcp.tool
async def plan_meeting(ctx: Context) -> str:
    """Plan a meeting by gathering details step by step."""

    # Get meeting title
    title_result = await ctx.elicit("What's the meeting title?", response_type=str)
    if title_result.action != "accept":
        return "Meeting planning cancelled"

    # Get duration
    duration_result = await ctx.elicit("Duration in minutes?", response_type=int)
    if duration_result.action != "accept":
        return "Meeting planning cancelled"

    # Get priority
    priority_result = await ctx.elicit(
        "Is this urgent?",
        response_type=Literal["yes", "no"]
    )
    if priority_result.action != "accept":
        return "Meeting planning cancelled"

    urgent = priority_result.data == "yes"
    return f"Meeting '{title_result.data}' planned for {duration_result.data} minutes (Urgent: {urgent})"

```

##
[​](https://gofastmcp.com/v2/servers/elicitation#client-requirements)
Client Requirements
Elicitation requires the client to implement an elicitation handler. See [Client Elicitation](https://gofastmcp.com/v2/clients/elicitation) for details on how clients can handle these requests. If a client doesn’t support elicitation, calls to `ctx.elicit()` will raise an error indicating that elicitation is not supported.
[ MCP Context Previous ](https://gofastmcp.com/v2/servers/context)[ Icons Next ](https://gofastmcp.com/v2/servers/icons)
Ctrl+I
