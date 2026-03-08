[Skip to main content](https://gofastmcp.com/v2/servers/sampling#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v2.14.5
Search...
Navigation
Advanced Features
LLM Sampling
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
  * [Method Reference](https://gofastmcp.com/v2/servers/sampling#method-reference)
  * [Basic Sampling](https://gofastmcp.com/v2/servers/sampling#basic-sampling)
  * [System Prompts](https://gofastmcp.com/v2/servers/sampling#system-prompts)
  * [Model Preferences](https://gofastmcp.com/v2/servers/sampling#model-preferences)
  * [Multi-Turn Conversations](https://gofastmcp.com/v2/servers/sampling#multi-turn-conversations)
  * [Structured Output](https://gofastmcp.com/v2/servers/sampling#structured-output)
  * [Sampling with Tools](https://gofastmcp.com/v2/servers/sampling#sampling-with-tools)
  * [Defining Tools](https://gofastmcp.com/v2/servers/sampling#defining-tools)
  * [Tool Error Handling](https://gofastmcp.com/v2/servers/sampling#tool-error-handling)
  * [Combining with Structured Output](https://gofastmcp.com/v2/servers/sampling#combining-with-structured-output)
  * [Loop Control](https://gofastmcp.com/v2/servers/sampling#loop-control)
  * [Using sample_step()](https://gofastmcp.com/v2/servers/sampling#using-sample_step)
  * [SampleStep Properties](https://gofastmcp.com/v2/servers/sampling#samplestep-properties)
  * [Manual Tool Execution](https://gofastmcp.com/v2/servers/sampling#manual-tool-execution)
  * [Error Handling](https://gofastmcp.com/v2/servers/sampling#error-handling)
  * [Fallback Handlers](https://gofastmcp.com/v2/servers/sampling#fallback-handlers)
  * [Behavior Modes](https://gofastmcp.com/v2/servers/sampling#behavior-modes)


Advanced Features
# LLM Sampling
Copy page
Request LLM text generation from the client or a configured provider through the MCP context.
Copy page
`2.0.0` LLM sampling allows your MCP tools to request text generation from an LLM during execution. This enables tools to leverage AI capabilities for analysis, generation, reasoning, and more—without the client needing to orchestrate multiple calls. By default, sampling requests are routed to the client’s LLM. You can also configure a fallback handler to use a specific provider (like OpenAI) when the client doesn’t support sampling, or to always use your own LLM regardless of client capabilities.
##
[​](https://gofastmcp.com/v2/servers/sampling#method-reference)
Method Reference
## ctx.sample()
[​](https://gofastmcp.com/v2/servers/sampling#param-ctx-sample)
ctx.sample
async method
Request text generation from the LLM, running to completion automatically.
Show Parameters
[​](https://gofastmcp.com/v2/servers/sampling#param-messages)
messages
str | list[str | SamplingMessage]
The prompt to send. Can be a simple string or a list of messages for multi-turn conversations.
[​](https://gofastmcp.com/v2/servers/sampling#param-system-prompt)
system_prompt
str | None
default:"None"
Instructions that establish the LLM’s role and behavior.
[​](https://gofastmcp.com/v2/servers/sampling#param-temperature)
temperature
float | None
default:"None"
Controls randomness (0.0 = deterministic, 1.0 = creative).
[​](https://gofastmcp.com/v2/servers/sampling#param-max-tokens)
max_tokens
int | None
default:"512"
Maximum tokens to generate.
[​](https://gofastmcp.com/v2/servers/sampling#param-model-preferences)
model_preferences
str | list[str] | None
default:"None"
Hints for which model the client should use.
[​](https://gofastmcp.com/v2/servers/sampling#param-tools)
tools
list[Callable] | None
default:"None"
Functions the LLM can call during sampling.
[​](https://gofastmcp.com/v2/servers/sampling#param-result-type)
result_type
type[T] | None
default:"None"
A type for validated structured output. Supports Pydantic models, dataclasses, and basic types like `int`, `list[str]`, or `dict[str, int]`.
[​](https://gofastmcp.com/v2/servers/sampling#param-mask-error-details)
mask_error_details
bool | None
default:"None"
If True, mask detailed error messages from tool execution. When None (default), uses the global `settings.mask_error_details` value. Tools can raise `ToolError` to bypass masking and provide specific error messages to the LLM.
Show Response
[​](https://gofastmcp.com/v2/servers/sampling#param-sampling-resultt)
SamplingResult[T]
dataclass
  * `.text`: The raw text response (or JSON for structured output)
  * `.result`: The typed result—same as `.text` for plain text, or a validated Pydantic object for structured output
  * `.history`: All messages exchanged during sampling


## ctx.sample_step()
[​](https://gofastmcp.com/v2/servers/sampling#param-ctx-sample-step)
ctx.sample_step
async method
Make a single LLM sampling call. Use this for fine-grained control over the sampling loop.
Show Parameters
Same as `sample()`, plus:
[​](https://gofastmcp.com/v2/servers/sampling#param-tool-choice)
tool_choice
str | None
default:"None"
Controls tool usage: `"auto"`, `"required"`, or `"none"`.
[​](https://gofastmcp.com/v2/servers/sampling#param-execute-tools)
execute_tools
bool
default:"True"
If True, execute tool calls and append results to history. If False, return immediately with tool calls available for manual execution.
[​](https://gofastmcp.com/v2/servers/sampling#param-mask-error-details-1)
mask_error_details
bool | None
default:"None"
If True, mask detailed error messages from tool execution. When None (default), uses the global `settings.mask_error_details` value. Tools can raise `ToolError` to bypass masking.
Show Response
[​](https://gofastmcp.com/v2/servers/sampling#param-sample-step)
SampleStep
dataclass
  * `.response`: The raw LLM response
  * `.history`: Messages including input, assistant response, and tool results
  * `.is_tool_use`: True if the LLM requested tool execution
  * `.tool_calls`: List of tool calls (if any)
  * `.text`: The text content (if any)


##
[​](https://gofastmcp.com/v2/servers/sampling#basic-sampling)
Basic Sampling
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
[​](https://gofastmcp.com/v2/servers/sampling#system-prompts)
System Prompts
System prompts let you establish the LLM’s role and behavioral guidelines before it processes your request. This is useful for controlling tone, enforcing constraints, or providing context that shouldn’t clutter the user-facing prompt.
Copy
```
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
[​](https://gofastmcp.com/v2/servers/sampling#model-preferences)
Model Preferences
Model preferences let you hint at which LLM the client should use for a request. You can pass a single model name or a list of preferences in priority order. These are hints rather than requirements—the actual model used depends on what the client has available.
Copy
```
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
[​](https://gofastmcp.com/v2/servers/sampling#multi-turn-conversations)
Multi-Turn Conversations
For requests that need conversational context, construct a list of `SamplingMessage` objects representing the conversation history. Each message has a `role` (“user” or “assistant”) and `content` (a `TextContent` object).
Copy
```
from mcp.types import SamplingMessage, TextContent

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
##
[​](https://gofastmcp.com/v2/servers/sampling#structured-output)
Structured Output
`2.14.1` When you need validated, typed data instead of free-form text, use the `result_type` parameter. FastMCP ensures the LLM returns data matching your type, handling validation and retries automatically. The `result_type` parameter accepts Pydantic models, dataclasses, and basic types like `int`, `list[str]`, or `dict[str, int]`.
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
When you pass `result_type`, `sample()` automatically creates a `final_response` tool that the LLM calls to provide its response. If validation fails, the error is sent back to the LLM for retry. This automatic handling only applies to `sample()`—with `sample_step()`, you must manage structured output yourself.
##
[​](https://gofastmcp.com/v2/servers/sampling#sampling-with-tools)
Sampling with Tools
`2.14.1` Sampling with tools enables agentic workflows where the LLM can call functions to gather information before responding. This implements  Pass Python functions to the `tools` parameter, and FastMCP handles the execution loop automatically—calling tools, returning results to the LLM, and continuing until the LLM provides a final response.
###
[​](https://gofastmcp.com/v2/servers/sampling#defining-tools)
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
[​](https://gofastmcp.com/v2/servers/sampling#tool-error-handling)
Tool Error Handling
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

`ToolError` messages always pass through to the LLM, making it the escape hatch for errors you want the LLM to see and handle. For custom names or descriptions, use `SamplingTool.from_function()`:
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
[​](https://gofastmcp.com/v2/servers/sampling#combining-with-structured-output)
Combining with Structured Output
Combine tools with `result_type` for agentic workflows that return validated, structured data. The LLM uses your tools to gather information, then returns a response matching your type.
Copy
```
result = await ctx.sample(
    messages="Research Python async patterns",
    tools=[search, fetch_url],
    result_type=ResearchResult,
)

```

##
[​](https://gofastmcp.com/v2/servers/sampling#loop-control)
Loop Control
`2.14.1` While `sample()` handles the tool execution loop automatically, some scenarios require fine-grained control over each step. The `sample_step()` method makes a single LLM call and returns a `SampleStep` containing the response and updated history. Unlike `sample()`, `sample_step()` is stateless—it doesn’t remember previous calls. You control the conversation by passing the full message history each time. The returned `step.history` includes all messages up through the current response, making it easy to continue the loop. Use `sample_step()` when you need to:
  * Inspect tool calls before they execute
  * Implement custom termination conditions
  * Add logging, metrics, or checkpointing between steps
  * Build custom agentic loops with domain-specific logic


###
[​](https://gofastmcp.com/v2/servers/sampling#using-sample_step)
Using sample_step()
By default, `sample_step()` executes any tool calls and includes the results in the history. Call it in a loop, passing the updated history each time, until a stop condition is met.
Copy
```
from mcp.types import SamplingMessage

@mcp.tool
async def controlled_agent(question: str, ctx: Context) -> str:
    """Agent with manual loop control."""
    messages: list[str | SamplingMessage] = [question]  # strings auto-convert

    while True:
        step = await ctx.sample_step(
            messages=messages,
            tools=[search, get_time],
        )

        if step.is_tool_use:
            # Tools already executed (execute_tools=True by default)
            # Log what was called before continuing
            for call in step.tool_calls:
                print(f"Called tool: {call.name}")

        if not step.is_tool_use:
            return step.text or ""

        # Continue with updated history
        messages = step.history

```

###
[​](https://gofastmcp.com/v2/servers/sampling#samplestep-properties)
SampleStep Properties
Each `SampleStep` provides information about what the LLM returned:
  * `step.is_tool_use` — True if the LLM requested tool calls
  * `step.tool_calls` — List of tool calls requested (if any)
  * `step.text` — The text content (if any)
  * `step.history` — All messages exchanged so far

The contents of `step.history` depend on `execute_tools`:
  * **`execute_tools=True`**(default): Includes tool results, ready for the next iteration
  * **`execute_tools=False`**: Includes the assistant’s tool request, but you add results yourself


###
[​](https://gofastmcp.com/v2/servers/sampling#manual-tool-execution)
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

    # Map tool names to functions
    tools = {"search": search, "get_time": get_time}

    messages: list[SamplingMessage] = [question]  # strings are converted automatically

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

####
[​](https://gofastmcp.com/v2/servers/sampling#error-handling)
Error Handling
To report an error, set `isError=True`. The LLM will see the error and can decide how to proceed:
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
[​](https://gofastmcp.com/v2/servers/sampling#fallback-handlers)
Fallback Handlers
Client support for sampling is optional—some clients may not implement it. To ensure your tools work regardless of client capabilities, configure a `sampling_handler` that sends requests directly to an LLM provider. FastMCP provides built-in handlers for [OpenAI and Anthropic APIs](https://gofastmcp.com/v2/clients/sampling#built-in-handlers). These handlers support the full sampling API including tools, automatically converting your Python functions to each provider’s format.
Install handlers with `pip install fastmcp[openai]` or `pip install fastmcp[anthropic]`.
Copy
```
from fastmcp import FastMCP
from fastmcp.client.sampling.handlers.openai import OpenAISamplingHandler

server = FastMCP(
    name="My Server",
    sampling_handler=OpenAISamplingHandler(default_model="gpt-4o-mini"),
    sampling_handler_behavior="fallback",
)

```

Or with Anthropic:
Copy
```
from fastmcp import FastMCP
from fastmcp.client.sampling.handlers.anthropic import AnthropicSamplingHandler

server = FastMCP(
    name="My Server",
    sampling_handler=AnthropicSamplingHandler(default_model="claude-sonnet-4-5"),
    sampling_handler_behavior="fallback",
)

```

###
[​](https://gofastmcp.com/v2/servers/sampling#behavior-modes)
Behavior Modes
The `sampling_handler_behavior` parameter controls when the handler is used:
  * **`"fallback"`**(default): Use the handler only when the client doesn’t support sampling. This lets capable clients use their own LLM while ensuring your tools still work with clients that lack sampling support.
  * **`"always"`**: Always use the handler, bypassing the client entirely. Use this when you need guaranteed control over which LLM processes requests—for cost control, compliance requirements, or when specific model characteristics are essential.


Sampling with tools requires the client to advertise the `sampling.tools` capability. FastMCP clients do this automatically. For external clients that don’t support tool-enabled sampling, configure a fallback handler with `sampling_handler_behavior="always"`.
[ Proxy Servers Previous ](https://gofastmcp.com/v2/servers/proxy)[ Storage Backends Next ](https://gofastmcp.com/v2/servers/storage-backends)
Ctrl+I
