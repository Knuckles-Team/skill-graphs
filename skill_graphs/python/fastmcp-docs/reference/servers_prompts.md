[Skip to main content](https://gofastmcp.com/servers/prompts#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
Search...
Navigation
Core Components
Prompts
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
    * [Tools](https://gofastmcp.com/servers/tools)
    * [Resources](https://gofastmcp.com/servers/resources)
    * [Prompts](https://gofastmcp.com/servers/prompts)
    * [ Context NEW ](https://gofastmcp.com/servers/context)
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
  * [What Are Prompts?](https://gofastmcp.com/servers/prompts#what-are-prompts)
  * [Prompts](https://gofastmcp.com/servers/prompts#prompts)
  * [The @prompt Decorator](https://gofastmcp.com/servers/prompts#the-%40prompt-decorator)
  * [Decorator Arguments](https://gofastmcp.com/servers/prompts#decorator-arguments)
  * [Using with Methods](https://gofastmcp.com/servers/prompts#using-with-methods)
  * [Argument Types](https://gofastmcp.com/servers/prompts#argument-types)
  * [Return Values](https://gofastmcp.com/servers/prompts#return-values)
  * [Message](https://gofastmcp.com/servers/prompts#message)
  * [PromptResult](https://gofastmcp.com/servers/prompts#promptresult)
  * [Required vs. Optional Parameters](https://gofastmcp.com/servers/prompts#required-vs-optional-parameters)
  * [Component Visibility](https://gofastmcp.com/servers/prompts#component-visibility)
  * [Async Prompts](https://gofastmcp.com/servers/prompts#async-prompts)
  * [Accessing MCP Context](https://gofastmcp.com/servers/prompts#accessing-mcp-context)
  * [Notifications](https://gofastmcp.com/servers/prompts#notifications)
  * [Server Behavior](https://gofastmcp.com/servers/prompts#server-behavior)
  * [Duplicate Prompts](https://gofastmcp.com/servers/prompts#duplicate-prompts)
  * [Versioning](https://gofastmcp.com/servers/prompts#versioning)


Core Components
# Prompts
Copy page
Create reusable, parameterized prompt templates for MCP clients.
Copy page
Prompts are reusable message templates that help LLMs generate structured, purposeful responses. FastMCP simplifies defining these templates, primarily using the `@mcp.prompt` decorator.
##
[​](https://gofastmcp.com/servers/prompts#what-are-prompts)
What Are Prompts?
Prompts provide parameterized message templates for LLMs. When a client requests a prompt:
  1. FastMCP finds the corresponding prompt definition.
  2. If it has parameters, they are validated against your function signature.
  3. Your function executes with the validated inputs.
  4. The generated message(s) are returned to the LLM to guide its response.

This allows you to define consistent, reusable templates that LLMs can use across different clients and contexts.
##
[​](https://gofastmcp.com/servers/prompts#prompts)
Prompts
###
[​](https://gofastmcp.com/servers/prompts#the-@prompt-decorator)
The `@prompt` Decorator
The most common way to define a prompt is by decorating a Python function. The decorator uses the function name as the prompt’s identifier.
Copy
```
from fastmcp import FastMCP
from fastmcp.prompts import Message

mcp = FastMCP(name="PromptServer")

# Basic prompt returning a string (converted to user message automatically)
@mcp.prompt
def ask_about_topic(topic: str) -> str:
    """Generates a user message asking for an explanation of a topic."""
    return f"Can you please explain the concept of '{topic}'?"

# Prompt returning multiple messages
@mcp.prompt
def generate_code_request(language: str, task_description: str) -> list[Message]:
    """Generates a conversation for code generation."""
    return [
        Message(f"Write a {language} function that performs the following task: {task_description}"),
        Message("I'll help you write that function.", role="assistant"),
    ]

```

**Key Concepts:**
  * **Name:** By default, the prompt name is taken from the function name.
  * **Parameters:** The function parameters define the inputs needed to generate the prompt.
  * **Inferred Metadata:** By default:
    * Prompt Name: Taken from the function name (`ask_about_topic`).
    * Prompt Description: Taken from the function’s docstring.


Functions with `*args` or `**kwargs` are not supported as prompts. This restriction exists because FastMCP needs to generate a complete parameter schema for the MCP protocol, which isn’t possible with variable argument lists.
####
[​](https://gofastmcp.com/servers/prompts#decorator-arguments)
Decorator Arguments
While FastMCP infers the name and description from your function, you can override these and add additional metadata using arguments to the `@mcp.prompt` decorator:
Copy
```
@mcp.prompt(
    name="analyze_data_request",          # Custom prompt name
    description="Creates a request to analyze data with specific parameters",  # Custom description
    tags={"analysis", "data"},            # Optional categorization tags
    meta={"version": "1.1", "author": "data-team"}  # Custom metadata
)
def data_analysis_prompt(
    data_uri: str = Field(description="The URI of the resource containing the data."),
    analysis_type: str = Field(default="summary", description="Type of analysis.")
) -> str:
    """This docstring is ignored when description is provided."""
    return f"Please perform a '{analysis_type}' analysis on the data found at {data_uri}."

```

## @prompt Decorator Arguments
[​](https://gofastmcp.com/servers/prompts#param-name)
name
str | None
Sets the explicit prompt name exposed via MCP. If not provided, uses the function name
[​](https://gofastmcp.com/servers/prompts#param-title)
title
str | None
A human-readable title for the prompt
[​](https://gofastmcp.com/servers/prompts#param-description)
description
str | None
Provides the description exposed via MCP. If set, the function’s docstring is ignored for this purpose
[​](https://gofastmcp.com/servers/prompts#param-tags)
tags
set[str] | None
A set of strings used to categorize the prompt. These can be used by the server and, in some cases, by clients to filter or group available prompts.
[​](https://gofastmcp.com/servers/prompts#param-enabled)
enabled
bool
default:"True"
Deprecated in v3.0.0. Use `mcp.enable()` / `mcp.disable()` at the server level instead.
A boolean to enable or disable the prompt. See [Component Visibility](https://gofastmcp.com/servers/prompts#component-visibility) for the recommended approach.
[​](https://gofastmcp.com/servers/prompts#param-icons)
icons
list[Icon] | None
`2.13.0`Optional list of icon representations for this prompt. See [Icons](https://gofastmcp.com/servers/icons) for detailed examples
[​](https://gofastmcp.com/servers/prompts#param-meta)
meta
dict[str, Any] | None
`2.11.0`Optional meta information about the prompt. This data is passed through to the MCP client as the `meta` field of the client-side prompt object and can be used for custom metadata, versioning, or other application-specific purposes.
[​](https://gofastmcp.com/servers/prompts#param-version)
version
str | int | None
`3.0.0`Optional version identifier for this prompt. See [Versioning](https://gofastmcp.com/servers/versioning) for details.
####
[​](https://gofastmcp.com/servers/prompts#using-with-methods)
Using with Methods
For decorating instance or class methods, use the standalone `@prompt` decorator and register the bound method. See [Tools: Using with Methods](https://gofastmcp.com/servers/tools#using-with-methods) for the pattern.
###
[​](https://gofastmcp.com/servers/prompts#argument-types)
Argument Types
`2.9.0` The MCP specification requires that all prompt arguments be passed as strings, but FastMCP allows you to use typed annotations for better developer experience. When you use complex types like `list[int]` or `dict[str, str]`, FastMCP:
  1. **Automatically converts** string arguments from MCP clients to the expected types
  2. **Generates helpful descriptions** showing the exact JSON string format needed
  3. **Preserves direct usage** - you can still call prompts with properly typed arguments

Since the MCP specification only allows string arguments, clients need to know what string format to use for complex types. FastMCP solves this by automatically enhancing the argument descriptions with JSON schema information, making it clear to both humans and LLMs how to format their arguments.
Python Code
Resulting MCP Prompt
Copy
```
@mcp.prompt
def analyze_data(
    numbers: list[int],
    metadata: dict[str, str],
    threshold: float
) -> str:
    """Analyze numerical data."""
    avg = sum(numbers) / len(numbers)
    return f"Average: {avg}, above threshold: {avg > threshold}"

```

**MCP clients will call this prompt with string arguments:**
Copy
```
{
  "numbers": "[1, 2, 3, 4, 5]",
  "metadata": "{\"source\": \"api\", \"version\": \"1.0\"}",
  "threshold": "2.5"
}

```

**But you can still call it directly with proper types:**
Copy
```
# This also works for direct calls
result = await prompt.render({
    "numbers": [1, 2, 3, 4, 5],
    "metadata": {"source": "api", "version": "1.0"},
    "threshold": 2.5
})

```

Keep your type annotations simple when using this feature. Complex nested types or custom classes may not convert reliably from JSON strings. The automatically generated schema descriptions are the only guidance users receive about the expected format.Good choices: `list[int]`, `dict[str, str]`, `float`, `bool` Avoid: Complex Pydantic models, deeply nested structures, custom classes
###
[​](https://gofastmcp.com/servers/prompts#return-values)
Return Values
Prompt functions must return one of these types:
  * **`str`**: Sent as a single user message.
  * **`list[Message | str]`**: A sequence of messages (a conversation). Strings are auto-converted to user Messages.
  * **`PromptResult`**: Full control over messages, description, and metadata. See[PromptResult](https://gofastmcp.com/servers/prompts#promptresult) below.


Copy
```
from fastmcp.prompts import Message

@mcp.prompt
def roleplay_scenario(character: str, situation: str) -> list[Message]:
    """Sets up a roleplaying scenario with initial messages."""
    return [
        Message(f"Let's roleplay. You are {character}. The situation is: {situation}"),
        Message("Okay, I understand. I am ready. What happens next?", role="assistant")
    ]

```

####
[​](https://gofastmcp.com/servers/prompts#message)
Message
`3.0.0` `Message` provides a user-friendly wrapper for prompt messages with automatic serialization.
Copy
```
from fastmcp.prompts import Message

# String content (user role by default)
Message("Hello, world!")

# Explicit role
Message("I can help with that.", role="assistant")

# Auto-serialized to JSON text
Message({"key": "value"})
Message(["item1", "item2"])

```

`Message` accepts two fields: **`content`**- The message content. Strings pass through directly. Other types (dict, list, BaseModel) are automatically JSON-serialized to text. **`role`**- The message role, either`"user"` (default) or `"assistant"`.
## Message
[​](https://gofastmcp.com/servers/prompts#param-content)
content
Any
required
The content data. Strings pass through directly. Other types (dict, list, BaseModel) are automatically JSON-serialized.
[​](https://gofastmcp.com/servers/prompts#param-role)
role
Literal['user', 'assistant']
default:"user"
The message role.
####
[​](https://gofastmcp.com/servers/prompts#promptresult)
PromptResult
`3.0.0` `PromptResult` gives you explicit control over prompt responses: multiple messages, roles, and metadata at both the message and result level.
Copy
```
from fastmcp import FastMCP
from fastmcp.prompts import PromptResult, Message

mcp = FastMCP(name="PromptServer")

@mcp.prompt
def code_review(code: str) -> PromptResult:
    """Returns a code review prompt with metadata."""
    return PromptResult(
        messages=[
            Message(f"Please review this code:\n\n```\n{code}\n```"),
            Message("I'll analyze this code for issues.", role="assistant"),
        ],
        description="Code review prompt",
        meta={"review_type": "security", "priority": "high"}
    )

```

For simple cases, you can pass a string directly to `PromptResult`:
Copy
```
return PromptResult("Please help me with this task")  # auto-converts to single Message

```

## PromptResult
[​](https://gofastmcp.com/servers/prompts#param-messages)
messages
str | list[Message]
required
Messages to return. Strings are wrapped as a single user Message.
[​](https://gofastmcp.com/servers/prompts#param-description-1)
description
str | None
Optional description of the prompt result. If not provided, defaults to the prompt’s docstring.
[​](https://gofastmcp.com/servers/prompts#param-meta-1)
meta
dict[str, Any] | None
Result-level metadata, included in the MCP response’s `_meta` field. Use this for runtime metadata like categorization, priority, or other client-specific data.
The `meta` field in `PromptResult` is for runtime metadata specific to this render response. This is separate from the `meta` parameter in `@mcp.prompt(meta={...})`, which provides static metadata about the prompt definition itself (returned when listing prompts).
You can still return plain `str` or `list[Message | str]` from your prompt functions—`PromptResult` is opt-in for when you need to include metadata.
###
[​](https://gofastmcp.com/servers/prompts#required-vs-optional-parameters)
Required vs. Optional Parameters
Parameters in your function signature are considered **required** unless they have a default value.
Copy
```
@mcp.prompt
def data_analysis_prompt(
    data_uri: str,                        # Required - no default value
    analysis_type: str = "summary",       # Optional - has default value
    include_charts: bool = False          # Optional - has default value
) -> str:
    """Creates a request to analyze data with specific parameters."""
    prompt = f"Please perform a '{analysis_type}' analysis on the data found at {data_uri}."
    if include_charts:
        prompt += " Include relevant charts and visualizations."
    return prompt

```

In this example, the client _must_ provide `data_uri`. If `analysis_type` or `include_charts` are omitted, their default values will be used.
###
[​](https://gofastmcp.com/servers/prompts#component-visibility)
Component Visibility
`3.0.0` You can control which prompts are enabled for clients using server-level enabled control. Disabled prompts don’t appear in `list_prompts` and can’t be called.
Copy
```
from fastmcp import FastMCP

mcp = FastMCP("MyServer")

@mcp.prompt(tags={"public"})
def public_prompt(topic: str) -> str:
    return f"Discuss: {topic}"

@mcp.prompt(tags={"internal"})
def internal_prompt() -> str:
    return "Internal system prompt"

# Disable specific prompts by key
mcp.disable(keys={"prompt:internal_prompt"})

# Disable prompts by tag
mcp.disable(tags={"internal"})

# Or use allowlist mode - only enable prompts with specific tags
mcp.enable(tags={"public"}, only=True)

```

See [Visibility](https://gofastmcp.com/servers/visibility) for the complete visibility control API including key formats, tag-based filtering, and provider-level control.
###
[​](https://gofastmcp.com/servers/prompts#async-prompts)
Async Prompts
FastMCP supports both standard (`def`) and asynchronous (`async def`) functions as prompts. Synchronous functions automatically run in a threadpool to avoid blocking the event loop.
Copy
```
# Synchronous prompt (runs in threadpool)
@mcp.prompt
def simple_question(question: str) -> str:
    """Generates a simple question to ask the LLM."""
    return f"Question: {question}"

# Asynchronous prompt
@mcp.prompt
async def data_based_prompt(data_id: str) -> str:
    """Generates a prompt based on data that needs to be fetched."""
    # In a real scenario, you might fetch data from a database or API
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://api.example.com/data/{data_id}") as response:
            data = await response.json()
            return f"Analyze this data: {data['content']}"

```

Use `async def` when your prompt function performs I/O operations like network requests or database queries, since async is more efficient than threadpool dispatch.
###
[​](https://gofastmcp.com/servers/prompts#accessing-mcp-context)
Accessing MCP Context
`2.2.5` Prompts can access additional MCP information and features through the `Context` object. To access it, add a parameter to your prompt function with a type annotation of `Context`:
Copy
```
from fastmcp import FastMCP, Context

mcp = FastMCP(name="PromptServer")

@mcp.prompt
async def generate_report_request(report_type: str, ctx: Context) -> str:
    """Generates a request for a report."""
    return f"Please create a {report_type} report. Request ID: {ctx.request_id}"

```

For full documentation on the Context object and all its capabilities, see the [Context documentation](https://gofastmcp.com/servers/context).
###
[​](https://gofastmcp.com/servers/prompts#notifications)
Notifications
`2.9.1` FastMCP automatically sends `notifications/prompts/list_changed` notifications to connected clients when prompts are added, enabled, or disabled. This allows clients to stay up-to-date with the current prompt set without manually polling for changes.
Copy
```
@mcp.prompt
def example_prompt() -> str:
    return "Hello!"

# These operations trigger notifications:
mcp.add_prompt(example_prompt)               # Sends prompts/list_changed notification
mcp.disable(keys={"prompt:example_prompt"})  # Sends prompts/list_changed notification
mcp.enable(keys={"prompt:example_prompt"})   # Sends prompts/list_changed notification

```

Notifications are only sent when these operations occur within an active MCP request context (e.g., when called from within a tool or other MCP operation). Operations performed during server initialization do not trigger notifications. Clients can handle these notifications using a [message handler](https://gofastmcp.com/clients/notifications) to automatically refresh their prompt lists or update their interfaces.
##
[​](https://gofastmcp.com/servers/prompts#server-behavior)
Server Behavior
###
[​](https://gofastmcp.com/servers/prompts#duplicate-prompts)
Duplicate Prompts
`2.1.0` You can configure how the FastMCP server handles attempts to register multiple prompts with the same name. Use the `on_duplicate_prompts` setting during `FastMCP` initialization.
Copy
```
from fastmcp import FastMCP

mcp = FastMCP(
    name="PromptServer",
    on_duplicate_prompts="error"  # Raise an error if a prompt name is duplicated
)

@mcp.prompt
def greeting(): return "Hello, how can I help you today?"

# This registration attempt will raise a ValueError because
# "greeting" is already registered and the behavior is "error".
# @mcp.prompt
# def greeting(): return "Hi there! What can I do for you?"

```

The duplicate behavior options are:
  * `"warn"` (default): Logs a warning, and the new prompt replaces the old one.
  * `"error"`: Raises a `ValueError`, preventing the duplicate registration.
  * `"replace"`: Silently replaces the existing prompt with the new one.
  * `"ignore"`: Keeps the original prompt and ignores the new registration attempt.


##
[​](https://gofastmcp.com/servers/prompts#versioning)
Versioning
`3.0.0` Prompts support versioning, allowing you to maintain multiple implementations under the same name while clients automatically receive the highest version. See [Versioning](https://gofastmcp.com/servers/versioning) for complete documentation on version comparison, retrieval, and migration patterns.
[ Resources & Templates Previous ](https://gofastmcp.com/servers/resources)[ MCP Context Next ](https://gofastmcp.com/servers/context)
Ctrl+I
