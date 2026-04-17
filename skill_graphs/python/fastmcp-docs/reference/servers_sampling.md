[Skip to main content](https://gofastmcp.com/servers/sampling#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
Search...
Navigation
Features
Sampling
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
  * [Overview](https://gofastmcp.com/servers/sampling#overview)
  * [System Prompts](https://gofastmcp.com/servers/sampling#system-prompts)
  * [Model Preferences](https://gofastmcp.com/servers/sampling#model-preferences)
  * [Multi-Turn Conversations](https://gofastmcp.com/servers/sampling#multi-turn-conversations)
  * [Fallback Handlers](https://gofastmcp.com/servers/sampling#fallback-handlers)
  * [Structured Output](https://gofastmcp.com/servers/sampling#structured-output)
  * [Structured Output with Tools](https://gofastmcp.com/servers/sampling#structured-output-with-tools)
  * [Tool Use](https://gofastmcp.com/servers/sampling#tool-use)
  * [Defining Tools](https://gofastmcp.com/servers/sampling#defining-tools)
  * [Custom Tool Definitions](https://gofastmcp.com/servers/sampling#custom-tool-definitions)
  * [Error Handling](https://gofastmcp.com/servers/sampling#error-handling)
  * [Concurrent Tool Execution](https://gofastmcp.com/servers/sampling#concurrent-tool-execution)
  * [Client Requirements](https://gofastmcp.com/servers/sampling#client-requirements)
  * [Advanced Control](https://gofastmcp.com/servers/sampling#advanced-control)
  * [Basic Loop](https://gofastmcp.com/servers/sampling#basic-loop)
  * [SampleStep Properties](https://gofastmcp.com/servers/sampling#samplestep-properties)
  * [Manual Tool Execution](https://gofastmcp.com/servers/sampling#manual-tool-execution)
  * [Method Reference](https://gofastmcp.com/servers/sampling#method-reference)


Features
# Sampling
Copy page
Request LLM text generation from the client or a configured provider through the MCP context.
Copy page
`2.0.0` LLM sampling allows your MCP tools to request text generation from an LLM during execution. This enables tools to leverage AI capabilities for analysis, generation, reasoning, and more—without the client needing to orchestrate multiple calls. By default, sampling requests are routed to the client’s LLM. You can also configure a fallback handler to use a specific provider (like OpenAI) when the client doesn’t support sampling, or to always use your own LLM regardless of client capabilities.
##
[​](https://gofastmcp.com/servers/sampling#overview)
Overview
The simplest use of sampling is passing a prompt string to `ctx.sample()`. The method sends the prompt to the LLM, waits for the complete response, and returns a `SamplingResult`. You can access the generated text through the `.text` attribute.
Copy
```
from fastmcp import FastMCP, Context

mcp = FastMCP()

@mcp.tool
async def summarize(content: str, ctx: Context) -> str:
    """Generate a summary of the provided content."""
    result = await ctx.sample(f"Please summarize this:\n\n{content}")
    return result.text or ""

```

The `SamplingResult` also provides `.result` (identical to `.text` for plain text responses) and `.history` containing the full message exchange—useful if you need to continue the conversation or debug the interaction.
###
[​](https://gofastmcp.com/servers/sampling#system-prompts)
System Prompts
System prompts let you establish the LLM’s role and behavioral guidelines before it processes your request. This is useful for controlling tone, enforcing constraints, or providing context that shouldn’t clutter the user-facing prompt.
Copy
```
from fastmcp import FastMCP, Context

mcp = FastMCP()

@mcp.tool
async def generate_code(concept: str, ctx: Context) -> str:
    """Generate a Python code example for a concept."""
    result = await ctx.sample(
        messages=f"Write a Python example demonstrating '{concept}'.",
        system_prompt=(
            "You are an expert Python programmer. "
            "Provide concise, working code without explanations."
        ),
        temperature=0.7,
        max_tokens=300
    )
    return f"```python\n{result.text}\n```"

```

The `temperature` parameter controls randomness—higher values (up to 1.0) produce more varied outputs, while lower values make responses more deterministic. The `max_tokens` parameter limits response length.
###
[​](https://gofastmcp.com/servers/sampling#model-preferences)
Model Preferences
Model preferences let you hint at which LLM the client should use for a request. You can pass a single model name or a list of preferences in priority order. These are hints rather than requirements—the actual model used depends on what the client has available.
Copy
```
from fastmcp import FastMCP, Context

mcp = FastMCP()

@mcp.tool
async def technical_analysis(data: str, ctx: Context) -> str:
    """Analyze data using a reasoning-focused model."""
    result = await ctx.sample(
        messages=f"Analyze this data:\n\n{data}",
        model_preferences=["claude-opus-4-5", "gpt-5-2"],
        temperature=0.2,
    )
    return result.text or ""

```

Use model preferences when different tasks benefit from different model characteristics. Creative writing might prefer faster models with higher temperature, while complex analysis might benefit from larger reasoning-focused models.
###
[​](https://gofastmcp.com/servers/sampling#multi-turn-conversations)
Multi-Turn Conversations
For requests that need conversational context, construct a list of `SamplingMessage` objects representing the conversation history. Each message has a `role` (“user” or “assistant”) and `content` (a `TextContent` object).
Copy
```
from mcp.types import SamplingMessage, TextContent
from fastmcp import FastMCP, Context

mcp = FastMCP()

@mcp.tool
async def contextual_analysis(query: str, data: str, ctx: Context) -> str:
    """Analyze data with conversational context."""
    messages = [
        SamplingMessage(
            role="user",
            content=TextContent(type="text", text=f"Here's my data: {data}"),
        ),
        SamplingMessage(
            role="assistant",
            content=TextContent(type="text", text="I see the data. What would you like to know?"),
        ),
        SamplingMessage(
            role="user",
            content=TextContent(type="text", text=query),
        ),
    ]
    result = await ctx.sample(messages=messages)
    return result.text or ""

```

The LLM receives the full conversation thread and responds with awareness of the preceding context.
###
[​](https://gofastmcp.com/servers/sampling#fallback-handlers)
Fallback Handlers
Client support for sampling is optional—some clients may not implement it. To ensure your tools work regardless of client capabilities, configure a `sampling_handler` that sends requests directly to an LLM provider. FastMCP provides built-in handlers for [OpenAI and Anthropic APIs](https://gofastmcp.com/clients/sampling#built-in-handlers). These handlers support the full sampling API including tools, automatically converting your Python functions to each provider’s format.
Install handlers with `pip install fastmcp[openai]` or `pip install fastmcp[anthropic]`.
Copy
```
from fastmcp import FastMCP
from fastmcp.client.sampling.handlers.openai import OpenAISamplingHandler

server = FastMCP(
    name="My Server",
    sampling_handler=OpenAISamplingHandler(default_model="nvidia/nemotron-3-super"),
    sampling_handler_behavior="fallback",
)

```

The `sampling_handler_behavior` parameter controls when the handler is used:
  * **`"fallback"`**(default): Use the handler only when the client doesn’t support sampling. This lets capable clients use their own LLM while ensuring your tools still work with clients that lack sampling support.
  * **`"always"`**: Always use the handler, bypassing the client entirely. Use this when you need guaranteed control over which LLM processes requests—for cost control, compliance requirements, or when specific model characteristics are essential.


##
[​](https://gofastmcp.com/servers/sampling#structured-output)
Structured Output
`2.14.1` When you need validated, typed data instead of free-form text, use the `result_type` parameter. FastMCP ensures the LLM returns data matching your type, handling validation and retries automatically. The `result_type` parameter accepts Pydantic models, dataclasses, and basic types like `int`, `list[str]`, or `dict[str, int]`. When you specify a result type, FastMCP automatically creates a `final_response` tool that the LLM calls to provide its response. If validation fails, the error is sent back to the LLM for retry.
Copy
```
from pydantic import BaseModel
from fastmcp import FastMCP, Context

mcp = FastMCP()

class SentimentResult(BaseModel):
    sentiment: str
    confidence: float
    reasoning: str

@mcp.tool
async def analyze_sentiment(text: str, ctx: Context) -> SentimentResult:
    """Analyze text sentiment with structured output."""
    result = await ctx.sample(
        messages=f"Analyze the sentiment of: {text}",
        result_type=SentimentResult,
    )
    return result.result  # A validated SentimentResult object

```

When you call this tool, the LLM returns a structured response that FastMCP validates against your Pydantic model. You access the validated object through `result.result`, while `result.text` contains the JSON representation.
###
[​](https://gofastmcp.com/servers/sampling#structured-output-with-tools)
Structured Output with Tools
Combine structured output with tools for agentic workflows that return validated data. The LLM uses your tools to gather information, then returns a response matching your type.
Copy
```
from pydantic import BaseModel
from fastmcp import FastMCP, Context

mcp = FastMCP()

def search(query: str) -> str:
    """Search the web for information."""
    return f"Results for: {query}"

def fetch_url(url: str) -> str:
    """Fetch content from a URL."""
    return f"Content from: {url}"

class ResearchResult(BaseModel):
    summary: str
    sources: list[str]
    confidence: float

@mcp.tool
async def research(topic: str, ctx: Context) -> ResearchResult:
    """Research a topic and return structured findings."""
    result = await ctx.sample(
        messages=f"Research: {topic}",
        tools=[search, fetch_url],
        result_type=ResearchResult,
    )
    return result.result

```

Structured output with automatic validation only applies to `sample()`. With `sample_step()`, you must manage structured output yourself.
##
[​](https://gofastmcp.com/servers/sampling#tool-use)
Tool Use
`2.14.1` Sampling with tools enables agentic workflows where the LLM can call functions to gather information before responding. This implements  Pass Python functions to the `tools` parameter, and FastMCP handles the execution loop automatically—calling tools, returning results to the LLM, and continuing until the LLM provides a final response.
###
[​](https://gofastmcp.com/servers/sampling#defining-tools)
Defining Tools
Define regular Python functions with type hints and docstrings. FastMCP extracts the function’s name, docstring, and parameter types to create tool schemas that the LLM can understand.
Copy
```
from fastmcp import FastMCP, Context

def search(query: str) -> str:
    """Search the web for information."""
    return f"Results for: {query}"

def get_time() -> str:
    """Get the current time."""
    from datetime import datetime
    return datetime.now().strftime("%H:%M:%S")

mcp = FastMCP()

@mcp.tool
async def research(question: str, ctx: Context) -> str:
    """Answer questions using available tools."""
    result = await ctx.sample(
        messages=question,
        tools=[search, get_time],
    )
    return result.text or ""

```

The LLM sees each function’s signature and docstring, using this information to decide when and how to call them. Tool errors are caught and sent back to the LLM, allowing it to recover gracefully. An internal safety limit prevents infinite loops.
###
[​](https://gofastmcp.com/servers/sampling#custom-tool-definitions)
Custom Tool Definitions
For custom names or descriptions, use `SamplingTool.from_function()`:
Copy
```
from fastmcp.server.sampling import SamplingTool

tool = SamplingTool.from_function(
    my_func,
    name="custom_name",
    description="Custom description"
)

result = await ctx.sample(messages="...", tools=[tool])

```

###
[​](https://gofastmcp.com/servers/sampling#error-handling)
Error Handling
By default, when a sampling tool raises an exception, the error message (including details) is sent back to the LLM so it can attempt recovery. To prevent sensitive information from leaking to the LLM, use the `mask_error_details` parameter:
Copy
```
result = await ctx.sample(
    messages=question,
    tools=[search],
    mask_error_details=True,  # Generic error messages only
)

```

When `mask_error_details=True`, tool errors become generic messages like `"Error executing tool 'search'"` instead of exposing stack traces or internal details. To intentionally provide specific error messages to the LLM regardless of masking, raise `ToolError`:
Copy
```
from fastmcp.exceptions import ToolError

def search(query: str) -> str:
    """Search for information."""
    if not query.strip():
        raise ToolError("Search query cannot be empty")
    return f"Results for: {query}"

```

`ToolError` messages always pass through to the LLM, making it the escape hatch for errors you want the LLM to see and handle.
###
[​](https://gofastmcp.com/servers/sampling#concurrent-tool-execution)
Concurrent Tool Execution
By default, tools execute sequentially — one at a time, in order. When your tools are independent (no shared state between them), you can execute them in parallel with `tool_concurrency`:
Copy
```
result = await ctx.sample(
    messages="Research these three topics",
    tools=[search, fetch_url],
    tool_concurrency=0,  # Unlimited parallel execution
)

```

The `tool_concurrency` parameter controls how many tools run at once:
  * **`None`**(default): Sequential execution
  * **`0`**: Unlimited parallel execution
  * **`N > 0`**: Execute at most N tools concurrently

For tools that must not run concurrently (file writes, shared state mutations, etc.), mark them as `sequential` when creating the `SamplingTool`:
Copy
```
from fastmcp.server.sampling import SamplingTool

db_writer = SamplingTool.from_function(
    write_to_db,
    sequential=True,  # Forces all tools in the batch to run sequentially
)

result = await ctx.sample(
    messages="Process this data",
    tools=[search, db_writer],
    tool_concurrency=0,  # Would be parallel, but db_writer forces sequential
)

```

When any tool in a batch has `sequential=True`, the entire batch executes sequentially regardless of `tool_concurrency`. This is a conservative guarantee — if one tool needs ordering, all tools in that batch respect it.
###
[​](https://gofastmcp.com/servers/sampling#client-requirements)
Client Requirements
Sampling with tools requires the client to advertise the `sampling.tools` capability. FastMCP clients do this automatically. For external clients that don’t support tool-enabled sampling, configure a fallback handler with `sampling_handler_behavior="always"`.
##
[​](https://gofastmcp.com/servers/sampling#advanced-control)
Advanced Control
`2.14.1` While `sample()` handles the tool execution loop automatically, some scenarios require fine-grained control over each step. The `sample_step()` method makes a single LLM call and returns a `SampleStep` containing the response and updated history. Unlike `sample()`, `sample_step()` is stateless—it doesn’t remember previous calls. You control the conversation by passing the full message history each time. The returned `step.history` includes all messages up through the current response, making it easy to continue the loop. Use `sample_step()` when you need to:
  * Inspect tool calls before they execute
  * Implement custom termination conditions
  * Add logging, metrics, or checkpointing between steps
  * Build custom agentic loops with domain-specific logic


###
[​](https://gofastmcp.com/servers/sampling#basic-loop)
Basic Loop
By default, `sample_step()` executes any tool calls and includes the results in the history. Call it in a loop, passing the updated history each time, until a stop condition is met.
Copy
```
from mcp.types import SamplingMessage
from fastmcp import FastMCP, Context

mcp = FastMCP()

def search(query: str) -> str:
    return f"Results for: {query}"

def get_time() -> str:
    return "12:00 PM"

@mcp.tool
async def controlled_agent(question: str, ctx: Context) -> str:
    """Agent with manual loop control."""
    messages: list[str | SamplingMessage] = [question]

    while True:
        step = await ctx.sample_step(
            messages=messages,
            tools=[search, get_time],
        )

        if step.is_tool_use:
            # Tools already executed (execute_tools=True by default)
            for call in step.tool_calls:
                print(f"Called tool: {call.name}")

        if not step.is_tool_use:
            return step.text or ""

        messages = step.history

```

###
[​](https://gofastmcp.com/servers/sampling#samplestep-properties)
SampleStep Properties
Each `SampleStep` provides information about what the LLM returned:
Property | Description
---|---
`step.is_tool_use` | True if the LLM requested tool calls
`step.tool_calls` | List of tool calls requested (if any)
`step.text` | The text content (if any)
`step.history` | All messages exchanged so far
The contents of `step.history` depend on `execute_tools`:
  * **`execute_tools=True`**(default): Includes tool results, ready for the next iteration
  * **`execute_tools=False`**: Includes the assistant’s tool request, but you add results yourself


###
[​](https://gofastmcp.com/servers/sampling#manual-tool-execution)
Manual Tool Execution
Set `execute_tools=False` to handle tool execution yourself. When disabled, `step.history` contains the user message and the assistant’s response with tool calls—but no tool results. You execute the tools and append the results as a user message.
Copy
```
from mcp.types import SamplingMessage, ToolResultContent, TextContent
from fastmcp import FastMCP, Context

mcp = FastMCP()

@mcp.tool
async def research(question: str, ctx: Context) -> str:
    """Research with manual tool handling."""

    def search(query: str) -> str:
        return f"Results for: {query}"

    def get_time() -> str:
        return "12:00 PM"

    tools = {"search": search, "get_time": get_time}
    messages: list[SamplingMessage] = [question]

    while True:
        step = await ctx.sample_step(
            messages=messages,
            tools=list(tools.values()),
            execute_tools=False,
        )

        if not step.is_tool_use:
            return step.text or ""

        # Execute tools and collect results
        tool_results = []
        for call in step.tool_calls:
            fn = tools[call.name]
            result = fn(**call.input)
            tool_results.append(
                ToolResultContent(
                    type="tool_result",
                    toolUseId=call.id,
                    content=[TextContent(type="text", text=result)],
                )
            )

        messages = list(step.history)
        messages.append(SamplingMessage(role="user", content=tool_results))

```

To report an error to the LLM, set `isError=True` on the tool result:
Copy
```
tool_result = ToolResultContent(
    type="tool_result",
    toolUseId=call.id,
    content=[TextContent(type="text", text="Permission denied")],
    isError=True,
)

```

##
[​](https://gofastmcp.com/servers/sampling#method-reference)
Method Reference
## ctx.sample()
[​](https://gofastmcp.com/servers/sampling#param-ctx-sample)
ctx.sample
async method
Request text generation from the LLM, running to completion automatically.
Show Parameters
[​](https://gofastmcp.com/servers/sampling#param-messages)
messages
str | list[str | SamplingMessage]
The prompt to send. Can be a simple string or a list of messages for multi-turn conversations.
[​](https://gofastmcp.com/servers/sampling#param-system-prompt)
system_prompt
str | None
default:"None"
Instructions that establish the LLM’s role and behavior.
[​](https://gofastmcp.com/servers/sampling#param-temperature)
temperature
float | None
default:"None"
Controls randomness (0.0 = deterministic, 1.0 = creative).
[​](https://gofastmcp.com/servers/sampling#param-max-tokens)
max_tokens
int | None
default:"512"
Maximum tokens to generate.
[​](https://gofastmcp.com/servers/sampling#param-model-preferences)
model_preferences
str | list[str] | None
default:"None"
Hints for which model the client should use.
[​](https://gofastmcp.com/servers/sampling#param-tools)
tools
list[Callable] | None
default:"None"
Functions the LLM can call during sampling.
[​](https://gofastmcp.com/servers/sampling#param-result-type)
result_type
type[T] | None
default:"None"
A type for validated structured output. Supports Pydantic models, dataclasses, and basic types like `int`, `list[str]`, or `dict[str, int]`.
[​](https://gofastmcp.com/servers/sampling#param-mask-error-details)
mask_error_details
bool | None
default:"None"
If True, mask detailed error messages from tool execution. When None (default), uses the global `settings.mask_error_details` value. Tools can raise `ToolError` to bypass masking and provide specific error messages to the LLM.
[​](https://gofastmcp.com/servers/sampling#param-tool-concurrency)
tool_concurrency
int | None
default:"None"
Controls parallel execution of tools. `None` (default) for sequential, `0` for unlimited parallel, or a positive integer for bounded concurrency. If any tool has `sequential=True`, all tools execute sequentially regardless.
Show Response
[​](https://gofastmcp.com/servers/sampling#param-sampling-resultt)
SamplingResult[T]
dataclass
  * `.text`: The raw text response (or JSON for structured output)
  * `.result`: The typed result—same as `.text` for plain text, or a validated Pydantic object for structured output
  * `.history`: All messages exchanged during sampling


## ctx.sample_step()
[​](https://gofastmcp.com/servers/sampling#param-ctx-sample-step)
ctx.sample_step
async method
Make a single LLM sampling call. Use this for fine-grained control over the sampling loop.
Show Parameters
[​](https://gofastmcp.com/servers/sampling#param-messages-1)
messages
str | list[str | SamplingMessage]
The prompt or conversation history.
[​](https://gofastmcp.com/servers/sampling#param-system-prompt-1)
system_prompt
str | None
default:"None"
Instructions that establish the LLM’s role and behavior.
[​](https://gofastmcp.com/servers/sampling#param-temperature-1)
temperature
float | None
default:"None"
Controls randomness (0.0 = deterministic, 1.0 = creative).
[​](https://gofastmcp.com/servers/sampling#param-max-tokens-1)
max_tokens
int | None
default:"512"
Maximum tokens to generate.
[​](https://gofastmcp.com/servers/sampling#param-tools-1)
tools
list[Callable] | None
default:"None"
Functions the LLM can call during sampling.
[​](https://gofastmcp.com/servers/sampling#param-tool-choice)
tool_choice
str | None
default:"None"
Controls tool usage: `"auto"`, `"required"`, or `"none"`.
[​](https://gofastmcp.com/servers/sampling#param-execute-tools)
execute_tools
bool
default:"True"
If True, execute tool calls and append results to history. If False, return immediately with tool calls available for manual execution.
[​](https://gofastmcp.com/servers/sampling#param-mask-error-details-1)
mask_error_details
bool | None
default:"None"
If True, mask detailed error messages from tool execution.
[​](https://gofastmcp.com/servers/sampling#param-tool-concurrency-1)
tool_concurrency
int | None
default:"None"
Controls parallel execution of tools. `None` (default) for sequential, `0` for unlimited parallel, or a positive integer for bounded concurrency.
Show Response
[​](https://gofastmcp.com/servers/sampling#param-sample-step)
SampleStep
dataclass
  * `.response`: The raw LLM response
  * `.history`: Messages including input, assistant response, and tool results
  * `.is_tool_use`: True if the LLM requested tool execution
  * `.tool_calls`: List of tool calls (if any)
  * `.text`: The text content (if any)


[ Progress Reporting Previous ](https://gofastmcp.com/servers/progress)[ Storage Backends Next ](https://gofastmcp.com/servers/storage-backends)
Ctrl+I
