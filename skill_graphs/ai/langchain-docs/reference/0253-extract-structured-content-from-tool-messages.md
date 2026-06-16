# Extract structured content from tool messages
for message in result["messages"]:
    if isinstance(message, ToolMessage) and message.artifact:
        structured_content = message.artifact["structured_content"]
```

**Appending structured content via interceptor**

If you want structured content to be visible in the conversation history (visible to the model), you can use an [interceptor](#tool-interceptors) to automatically append structured content to the tool result:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import json

from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_mcp_adapters.interceptors import MCPToolCallRequest
from mcp.types import TextContent

async def append_structured_content(request: MCPToolCallRequest, handler):
    """Append structured content from artifact to tool message."""
    result = await handler(request)
    if result.structuredContent:
        result.content += [
            TextContent(type="text", text=json.dumps(result.structuredContent)),
        ]
    return result

client = MultiServerMCPClient({...}, tool_interceptors=[append_structured_content])
```

#### Multimodal tool content

MCP tools can return [multimodal content](https://modelcontextprotocol.io/specification/2025-03-26/server/tools#tool-result) (images, text, etc.) in their responses. When an MCP server returns content with multiple parts (e.g., text and images), the adapter converts them to LangChain's [standard content blocks](/oss/python/langchain/messages#standard-content-blocks). You can access the standardized representation via the `content_blocks` property on the `ToolMessage`:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent

client = MultiServerMCPClient({...})
tools = await client.get_tools()
agent = create_agent("claude-sonnet-4-6", tools)

result = await agent.ainvoke(
    {"messages": [{"role": "user", "content": "Take a screenshot of the current page"}]}
)

# Access multimodal content from tool messages
for message in result["messages"]:
    if message.type == "tool":
        # Raw content in provider-native format
        print(f"Raw content: {message.content}")

        # Standardized content blocks  # [!code highlight]
        for block in message.content_blocks:  # [!code highlight]
            if block["type"] == "text":  # [!code highlight]
                print(f"Text: {block['text']}")  # [!code highlight]
            elif block["type"] == "image":  # [!code highlight]
                print(f"Image URL: {block.get('url')}")  # [!code highlight]
                print(f"Image base64: {block.get('base64', '')[:50]}...")  # [!code highlight]
```

This allows you to handle multimodal tool responses in a provider-agnostic way, regardless of how the underlying MCP server formats its content.

### Resources

[Resources](https://modelcontextprotocol.io/docs/concepts/resources) allow MCP servers to expose data—such as files, database records, or API responses—that can be read by clients. LangChain converts MCP resources into [Blob](https://reference.langchain.com/python/langchain_core/documents/#langchain_core.documents.base.Blob) objects, which provide a unified interface for handling both text and binary content.

#### Loading resources

Use `client.get_resources()` to load resources from an MCP server:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_mcp_adapters.client import MultiServerMCPClient

client = MultiServerMCPClient({...})

# Load all resources from a server
blobs = await client.get_resources("server_name")  # [!code highlight]

# Or load specific resources by URI
blobs = await client.get_resources("server_name", uris=["file:///path/to/file.txt"])  # [!code highlight]

for blob in blobs:
    print(f"URI: {blob.metadata['uri']}, MIME type: {blob.mimetype}")
    print(blob.as_string())  # For text content
```

You can also use [`load_mcp_resources`](https://reference.langchain.com/python/langchain_mcp_adapters/#langchain_mcp_adapters.resources.load_mcp_resources) directly with a session for more control:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_mcp_adapters.resources import load_mcp_resources

client = MultiServerMCPClient({...})

async with client.session("server_name") as session:
    # Load all resources
    blobs = await load_mcp_resources(session)

    # Or load specific resources by URI
    blobs = await load_mcp_resources(session, uris=["file:///path/to/file.txt"])
```

### Prompts

[Prompts](https://modelcontextprotocol.io/docs/concepts/prompts) allow MCP servers to expose reusable prompt templates that can be retrieved and used by clients. LangChain converts MCP prompts into [messages](/oss/python/langchain/messages), making them easy to integrate into chat-based workflows.

#### Loading prompts

Use `client.get_prompt()` to load a prompt from an MCP server:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_mcp_adapters.client import MultiServerMCPClient

client = MultiServerMCPClient({...})

# Load a prompt by name
messages = await client.get_prompt("server_name", "summarize")  # [!code highlight]

# Load a prompt with arguments
messages = await client.get_prompt(  # [!code highlight]
    "server_name",  # [!code highlight]
    "code_review",  # [!code highlight]
    arguments={"language": "python", "focus": "security"}  # [!code highlight]
)  # [!code highlight]

# Use the messages in your workflow
for message in messages:
    print(f"{message.type}: {message.content}")
```

You can also use [`load_mcp_prompt`](https://reference.langchain.com/python/langchain_mcp_adapters/#langchain_mcp_adapters.prompts.load_mcp_prompt) directly with a session for more control:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_mcp_adapters.prompts import load_mcp_prompt

client = MultiServerMCPClient({...})

async with client.session("server_name") as session:
    # Load a prompt by name
    messages = await load_mcp_prompt(session, "summarize")

    # Load a prompt with arguments
    messages = await load_mcp_prompt(
        session,
        "code_review",
        arguments={"language": "python", "focus": "security"}
    )
```

## Advanced features

### Tool interceptors

MCP servers run as separate processes—they can't access LangGraph runtime information like the [store](/oss/python/langgraph/stores), [context](/oss/python/langchain/context-engineering), or agent state. **Interceptors bridge this gap** by giving you access to this runtime context during MCP tool execution.

Interceptors also provide middleware-like control over tool calls: you can modify requests, implement retries, add headers dynamically, or short-circuit execution entirely.

| Section                                                   | Description                                                                 |
| --------------------------------------------------------- | --------------------------------------------------------------------------- |
| [Accessing runtime context](#accessing-runtime-context)   | Read user IDs, API keys, store data, and agent state                        |
| [State updates and commands](#state-updates-and-commands) | Update agent state or control graph flow with `Command`                     |
| [Writing interceptors](#custom-interceptors)              | Patterns for modifying requests, composing interceptors, and error handling |

#### Accessing runtime context

When MCP tools are used within a LangChain agent (via `create_agent`), interceptors receive access to the `ToolRuntime` context. This provides access to the tool call ID, state, config, and store—enabling powerful patterns for accessing user data, persisting information, and controlling agent behavior.

<Tabs>
  <Tab title="Runtime context">
    Access user-specific configuration like user IDs, API keys, or permissions that are passed at invocation time:

    ```python Inject user context into MCP tool calls theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from dataclasses import dataclass
    from langchain_mcp_adapters.client import MultiServerMCPClient
    from langchain_mcp_adapters.interceptors import MCPToolCallRequest
    from langchain.agents import create_agent

    @dataclass
    class Context:
        user_id: str
        api_key: str

    async def inject_user_context(
        request: MCPToolCallRequest,
        handler,
    ):
        """Inject user credentials into MCP tool calls."""
        runtime = request.runtime
        user_id = runtime.context.user_id  # [!code highlight]
        api_key = runtime.context.api_key  # [!code highlight]

        # Add user context to tool arguments
        modified_request = request.override(
            args={**request.args, "user_id": user_id}
        )
        return await handler(modified_request)

    client = MultiServerMCPClient(
        {...},
        tool_interceptors=[inject_user_context],
    )
    tools = await client.get_tools()
    agent = create_agent("gpt-5.5", tools, context_schema=Context)

    # Invoke with user context
    result = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "Search my orders"}]},
        context={"user_id": "user_123", "api_key": "sk-..."}
    )
    ```
  </Tab>

  <Tab title="Store">
    Access long-term memory to retrieve user preferences or persist data across conversations:

    ```python Access user preferences from store theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from dataclasses import dataclass
    from langchain_mcp_adapters.client import MultiServerMCPClient
    from langchain_mcp_adapters.interceptors import MCPToolCallRequest
    from langchain.agents import create_agent
    from langgraph.store.memory import InMemoryStore

    @dataclass
    class Context:
        user_id: str

    async def personalize_search(
        request: MCPToolCallRequest,
        handler,
    ):
        """Personalize MCP tool calls using stored preferences."""
        runtime = request.runtime
        user_id = runtime.context.user_id
        store = runtime.store  # [!code highlight]

        # Read user preferences from store
        prefs = store.get(("preferences",), user_id)  # [!code highlight]

        if prefs and request.name == "search":
            # Apply user's preferred language and result limit
            modified_args = {
                **request.args,
                "language": prefs.value.get("language", "en"),
                "limit": prefs.value.get("result_limit", 10),
            }
            request = request.override(args=modified_args)

        return await handler(request)

    client = MultiServerMCPClient(
        {...},
        tool_interceptors=[personalize_search],
    )
    tools = await client.get_tools()
    agent = create_agent(
        "gpt-5.5",
        tools,
        context_schema=Context,
        store=InMemoryStore()
    )
    ```
  </Tab>

  <Tab title="State">
    Access conversation state to make decisions based on the current session:

    ```python Filter tools based on authentication state theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from langchain_mcp_adapters.client import MultiServerMCPClient
    from langchain_mcp_adapters.interceptors import MCPToolCallRequest
    from langchain.messages import ToolMessage

    async def require_authentication(
        request: MCPToolCallRequest,
        handler,
    ):
        """Block sensitive MCP tools if user is not authenticated."""
        runtime = request.runtime
        state = runtime.state  # [!code highlight]
        is_authenticated = state.get("authenticated", False)  # [!code highlight]

        sensitive_tools = ["delete_file", "update_settings", "export_data"]

        if request.name in sensitive_tools and not is_authenticated:
            # Return error instead of calling tool
            return ToolMessage(
                content="Authentication required. Please log in first.",
                tool_call_id=runtime.tool_call_id,
            )

        return await handler(request)

    client = MultiServerMCPClient(
        {...},
        tool_interceptors=[require_authentication],
    )
    ```
  </Tab>

  <Tab title="Tool call ID">
    Access the tool call ID to return properly formatted responses or track tool executions:

    ```python Return custom responses with tool call ID theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from langchain_mcp_adapters.client import MultiServerMCPClient
    from langchain_mcp_adapters.interceptors import MCPToolCallRequest
    from langchain.messages import ToolMessage

    async def rate_limit_interceptor(
        request: MCPToolCallRequest,
        handler,
    ):
        """Rate limit expensive MCP tool calls."""
        runtime = request.runtime
        tool_call_id = runtime.tool_call_id  # [!code highlight]

        # Check rate limit (simplified example)
        if is_rate_limited(request.name):
            return ToolMessage(
                content="Rate limit exceeded. Please try again later.",
                tool_call_id=tool_call_id,  # [!code highlight]
            )

        result = await handler(request)

        # Log successful tool call
        log_tool_execution(tool_call_id, request.name, success=True)

        return result

    client = MultiServerMCPClient(
        {...},
        tool_interceptors=[rate_limit_interceptor],
    )
    ```
  </Tab>
</Tabs>

For more context engineering patterns, see [Context engineering](/oss/python/langchain/context-engineering) and [Tools](/oss/python/langchain/tools).

#### State updates and commands

Interceptors can return `Command` objects to update agent state or control graph execution flow. This is useful for tracking task progress, switching between agents, or ending execution early.

```python Mark task complete and switch agents theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain.agents import AgentState, create_agent
from langchain_mcp_adapters.interceptors import MCPToolCallRequest
from langchain.messages import ToolMessage
from langgraph.types import Command

async def handle_task_completion(
    request: MCPToolCallRequest,
    handler,
):
    """Mark task complete and hand off to summary agent."""
    result = await handler(request)

    if request.name == "submit_order":
        return Command(
            update={
                "messages": [result] if isinstance(result, ToolMessage) else [],
                "task_status": "completed",  # [!code highlight]
            },
            goto="summary_agent",  # [!code highlight]
        )

    return result
```

Use `Command` with `goto="__end__"` to end execution early:

```python End agent run on completion theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
async def end_on_success(
    request: MCPToolCallRequest,
    handler,
):
    """End agent run when task is marked complete."""
    result = await handler(request)

    if request.name == "mark_complete":
        return Command(
            update={"messages": [result], "status": "done"},
            goto="__end__",  # [!code highlight]
        )

    return result
```

#### Custom interceptors

Interceptors are async functions that wrap tool execution, enabling request/response modification, retry logic, and other cross-cutting concerns. They follow an "onion" pattern where the first interceptor in the list is the outermost layer.

**Basic pattern**

An interceptor is an async function that receives a request and a handler. You can modify the request before calling the handler, modify the response after, or skip the handler entirely.

```python Basic interceptor pattern theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_mcp_adapters.interceptors import MCPToolCallRequest

async def logging_interceptor(
    request: MCPToolCallRequest,
    handler,
):
    """Log tool calls before and after execution."""
    print(f"Calling tool: {request.name} with args: {request.args}")
    result = await handler(request)
    print(f"Tool {request.name} returned: {result}")
    return result

client = MultiServerMCPClient(
    {"math": {"transport": "stdio", "command": "python", "args": ["/path/to/server.py"]}},
    tool_interceptors=[logging_interceptor],  # [!code highlight]
)
```

**Modifying requests**

Use `request.override()` to create a modified request. This follows an immutable pattern, leaving the original request unchanged.

```python Modifying tool arguments theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
async def double_args_interceptor(
    request: MCPToolCallRequest,
    handler,
):
    """Double all numeric arguments before execution."""
    modified_args = {k: v * 2 for k, v in request.args.items()}
    modified_request = request.override(args=modified_args)  # [!code highlight]
    return await handler(modified_request)

# Original call: add(a=2, b=3) becomes add(a=4, b=6)
```

**Modifying headers at runtime**

Interceptors can modify HTTP headers dynamically based on the request context:

```python Dynamic header modification theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
async def auth_header_interceptor(
    request: MCPToolCallRequest,
    handler,
):
    """Add authentication headers based on the tool being called."""
    token = get_token_for_tool(request.name)
    modified_request = request.override(
        headers={"Authorization": f"Bearer {token}"}  # [!code highlight]
    )
    return await handler(modified_request)
```

**Composing interceptors**

Multiple interceptors compose in "onion" order—the first interceptor in the list is the outermost layer:

```python Composing multiple interceptors theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
async def outer_interceptor(request, handler):
    print("outer: before")
    result = await handler(request)
    print("outer: after")
    return result

async def inner_interceptor(request, handler):
    print("inner: before")
    result = await handler(request)
    print("inner: after")
    return result

client = MultiServerMCPClient(
    {...},
    tool_interceptors=[outer_interceptor, inner_interceptor],  # [!code highlight]
)

# Execution order:

# outer: before -> inner: before -> tool execution -> inner: after -> outer: after
```

**Error handling**

Use interceptors to catch exceptions from tool execution, such as transport or runtime failures, and add retry logic. Tool execution errors (`CallToolResult(isError=True)`) do not raise by default, so exception-catching interceptors never trigger on them. To catch those as exceptions here, set `handle_tool_errors=False`.

```python Retry on error theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import asyncio

async def retry_interceptor(
    request: MCPToolCallRequest,
    handler,
    max_retries: int = 3,
    delay: float = 1.0,
):
    """Retry failed tool calls with exponential backoff."""
    last_error = None
    for attempt in range(max_retries):
        try:
            return await handler(request)
        except Exception as e:
            last_error = e
            if attempt < max_retries - 1:
                wait_time = delay * (2 ** attempt)  # Exponential backoff
                print(f"Tool {request.name} failed (attempt {attempt + 1}), retrying in {wait_time}s...")
                await asyncio.sleep(wait_time)
    raise last_error

client = MultiServerMCPClient(
    {...},
    tool_interceptors=[retry_interceptor],  # [!code highlight]
)
```

You can also catch specific error types and return fallback values:

```python Error handling with fallback theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
async def fallback_interceptor(
    request: MCPToolCallRequest,
    handler,
):
    """Return a fallback value if tool execution fails."""
    try:
        return await handler(request)
    except TimeoutError:
        return f"Tool {request.name} timed out. Please try again later."
    except ConnectionError:
        return f"Could not connect to {request.name} service. Using cached data."
```

### Progress notifications

Subscribe to progress updates for long-running tool executions:

```python Progress callback theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_mcp_adapters.callbacks import Callbacks, CallbackContext

async def on_progress(
    progress: float,
    total: float | None,
    message: str | None,
    context: CallbackContext,
):
    """Handle progress updates from MCP servers."""
    percent = (progress / total * 100) if total else progress
    tool_info = f" ({context.tool_name})" if context.tool_name else ""
    print(f"[{context.server_name}{tool_info}] Progress: {percent:.1f}% - {message}")

client = MultiServerMCPClient(
    {...},
    callbacks=Callbacks(on_progress=on_progress),  # [!code highlight]
)
```

The `CallbackContext` provides:

* `server_name`: Name of the MCP server
* `tool_name`: Name of the tool being executed (available during tool calls)

### Logging

The MCP protocol supports [logging](https://modelcontextprotocol.io/specification/2025-03-26/server/utilities/logging#log-levels) notifications from servers. Use the `Callbacks` class to subscribe to these events.

```python Logging callback theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_mcp_adapters.callbacks import Callbacks, CallbackContext
from mcp.types import LoggingMessageNotificationParams

async def on_logging_message(
    params: LoggingMessageNotificationParams,
    context: CallbackContext,
):
    """Handle log messages from MCP servers."""
    print(f"[{context.server_name}] {params.level}: {params.data}")

client = MultiServerMCPClient(
    {...},
    callbacks=Callbacks(on_logging_message=on_logging_message),  # [!code highlight]
)
```

### Elicitation

[Elicitation](https://modelcontextprotocol.io/specification/2025-11-25/client/elicitation#elicitation) allows MCP servers to request additional input from users during tool execution. Instead of requiring all inputs upfront, servers can interactively ask for information as needed.

#### Server setup

Define a tool that uses `ctx.elicit()` to request user input with a schema:

```python MCP server with elicitation theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from pydantic import BaseModel
from mcp.server.fastmcp import Context, FastMCP

server = FastMCP("Profile")

class UserDetails(BaseModel):
    email: str
    age: int

@server.tool()
async def create_profile(name: str, ctx: Context) -> str:
    """Create a user profile, requesting details via elicitation."""
    result = await ctx.elicit(  # [!code highlight]
        message=f"Please provide details for {name}'s profile:",  # [!code highlight]
        schema=UserDetails,  # [!code highlight]
    )  # [!code highlight]
    if result.action == "accept" and result.data:
        return f"Created profile for {name}: email={result.data.email}, age={result.data.age}"
    if result.action == "decline":
        return f"User declined. Created minimal profile for {name}."
    return "Profile creation cancelled."

if __name__ == "__main__":
    server.run(transport="http")
```

#### Client setup

Handle elicitation requests by providing a callback to `MultiServerMCPClient`:

```python Handling elicitation requests theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_mcp_adapters.callbacks import Callbacks, CallbackContext
from mcp.shared.context import RequestContext
from mcp.types import ElicitRequestParams, ElicitResult

async def on_elicitation(
    mcp_context: RequestContext,
    params: ElicitRequestParams,
    context: CallbackContext,
) -> ElicitResult:
    """Handle elicitation requests from MCP servers."""
    # In a real application, you would prompt the user for input
    # based on params.message and params.requestedSchema
    return ElicitResult(  # [!code highlight]
        action="accept",  # [!code highlight]
        content={"email": "user@example.com", "age": 25},  # [!code highlight]
    )  # [!code highlight]

client = MultiServerMCPClient(
    {
        "profile": {
            "url": "http://localhost:8000/mcp",
            "transport": "http",
        }
    },
    callbacks=Callbacks(on_elicitation=on_elicitation),  # [!code highlight]
)
```

#### Response actions

The elicitation callback can return one of three actions:

| Action    | Description                                                         |
| --------- | ------------------------------------------------------------------- |
| `accept`  | User provided valid input. Include the data in the `content` field. |
| `decline` | User chose not to provide the requested information.                |
| `cancel`  | User cancelled the operation entirely.                              |

```python Response action examples theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# Accept with data
ElicitResult(action="accept", content={"email": "user@example.com", "age": 25})

# Decline (user doesn't want to provide info)
ElicitResult(action="decline")

# Cancel (abort the operation)
ElicitResult(action="cancel")
```

## Additional resources

* [MCP documentation](https://modelcontextprotocol.io/introduction)
* [MCP Transport documentation](https://modelcontextprotocol.io/docs/concepts/transports)
* [`langchain-mcp-adapters`](https://github.com/langchain-ai/langchain-mcp-adapters)

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/mcp.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Messages
Source: https://docs.langchain.com/oss/python/langchain/messages

Messages are the fundamental unit of context for models in LangChain. They represent the input and output of models, carrying both the content and metadata needed to represent the state of a conversation when interacting with an LLM.

Messages are objects that contain:

* <Icon icon="user" /> [**Role**](#message-types) - Identifies the message type (e.g. `system`, `user`)
* <Icon icon="folder" /> [**Content**](#message-content) - Represents the actual content of the message (like text, images, audio, documents, etc.)
* <Icon icon="tag" /> [**Metadata**](#message-metadata) - Optional fields such as response information, message IDs, and token usage

LangChain provides a standard message type that works across all model providers, ensuring consistent behavior regardless of the model being called.

## Basic usage

The simplest way to use messages is to create message objects and pass them to a model when [invoking](/oss/python/langchain/models#invocation).

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage, AIMessage, SystemMessage

model = init_chat_model("gpt-5-nano")

system_msg = SystemMessage("You are a helpful assistant.")
human_msg = HumanMessage("Hello, how are you?")

# Use with chat models
messages = [system_msg, human_msg]
response = model.invoke(messages)  # Returns AIMessage
```

<Tip>
  Multi-turn [agents](/oss/python/langchain/agents) accumulate long message histories. [LangSmith](/langsmith/observability) records each turn, tool result, and model response so you can inspect the full conversation. Follow the [tracing quickstart](/langsmith/trace-with-langchain) to enable tracing.

  We recommend you also set up [LangSmith Engine](/langsmith/engine) which monitors your traces, detects issues, and proposes fixes.
</Tip>

### Text prompts

Text prompts are strings - ideal for straightforward generation tasks where you don't need to retain conversation history.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
response = model.invoke("Write a haiku about spring")
```

**Use text prompts when:**

* You have a single, standalone request
* You don't need conversation history
* You want minimal code complexity

### Message prompts

Alternatively, you can pass in a list of messages to the model by providing a list of message objects.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain.messages import SystemMessage, HumanMessage, AIMessage

messages = [
    SystemMessage("You are a poetry expert"),
    HumanMessage("Write a haiku about spring"),
    AIMessage("Cherry blossoms bloom...")
]
response = model.invoke(messages)
```

**Use message prompts when:**

* Managing multi-turn conversations
* Working with multimodal content (images, audio, files)
* Including system instructions

### Dictionary format

You can also specify messages directly in OpenAI chat completions format.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
messages = [
    {"role": "system", "content": "You are a poetry expert"},
    {"role": "user", "content": "Write a haiku about spring"},
    {"role": "assistant", "content": "Cherry blossoms bloom..."}
]
response = model.invoke(messages)
```

## Message types

* <Icon icon="settings" /> [System message](#system-message) - Tells the model how to behave and provide context for interactions
* <Icon icon="user" /> [Human message](#human-message) - Represents user input and interactions with the model
* <Icon icon="robot" /> [AI message](#ai-message) - Responses generated by the model, including text content, tool calls, and metadata
* <Icon icon="tool" /> [Tool message](#tool-message) - Represents the outputs of [tool calls](/oss/python/langchain/models#tool-calling)

### System message

A [`SystemMessage`](https://reference.langchain.com/python/langchain-core/messages/system/SystemMessage) represent an initial set of instructions that primes the model's behavior. You can use a system message to set the tone, define the model's role, and establish guidelines for responses.

```python Basic instructions theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
system_msg = SystemMessage("You are a helpful coding assistant.")

messages = [
    system_msg,
    HumanMessage("How do I create a REST API?")
]
response = model.invoke(messages)
```

```python Detailed persona theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain.messages import SystemMessage, HumanMessage

system_msg = SystemMessage("""
You are a senior Python developer with expertise in web frameworks.
Always provide code examples and explain your reasoning.
Be concise but thorough in your explanations.
""")

messages = [
    system_msg,
    HumanMessage("How do I create a REST API?")
]
response = model.invoke(messages)
```

***

### Human message

A [`HumanMessage`](https://reference.langchain.com/python/langchain-core/messages/human/HumanMessage) represents user input and interactions. They can contain text, images, audio, files, and any other amount of multimodal [content](#message-content).

#### Text content

<CodeGroup>
  ```python Message object theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  response = model.invoke([
    HumanMessage("What is machine learning?")
  ])
  ```

  ```python String shortcut theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  # Using a string is a shortcut for a single HumanMessage
  response = model.invoke("What is machine learning?")
  ```
</CodeGroup>

#### Message metadata

```python Add metadata theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
human_msg = HumanMessage(
    content="Hello!",
    name="alice",  # Optional: identify different users
    id="msg_123",  # Optional: unique identifier for tracing
)
```

<Note>
  The `name` field behavior varies by provider—some use it for user identification, others ignore it. To check, refer to the model provider's [reference](https://reference.langchain.com/python/integrations/).
</Note>

***

### AI message

An [`AIMessage`](https://reference.langchain.com/python/langchain-core/messages/ai/AIMessage) represents the output of a model invocation. They can include multimodal data, tool calls, and provider-specific metadata that you can later access.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
response = model.invoke("Explain AI")
print(type(response))  # <class 'langchain.messages.AIMessage'>
```

[`AIMessage`](https://reference.langchain.com/python/langchain-core/messages/ai/AIMessage) objects are returned by the model when calling it, which contains all of the associated metadata in the response.

Providers weigh/contextualize types of messages differently, which means it is sometimes helpful to manually create a new [`AIMessage`](https://reference.langchain.com/python/langchain-core/messages/ai/AIMessage) object and insert it into the message history as if it came from the model.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain.messages import AIMessage, SystemMessage, HumanMessage

# Create an AI message manually (e.g., for conversation history)
ai_msg = AIMessage("I'd be happy to help you with that question!")

# Add to conversation history
messages = [
    SystemMessage("You are a helpful assistant"),
    HumanMessage("Can you help me?"),
    ai_msg,  # Insert as if it came from the model
    HumanMessage("Great! What's 2+2?")
]

response = model.invoke(messages)
```

<Accordion title="Attributes">
  <ParamField type="string">
    The text content of the message.
  </ParamField>

  <ParamField type="string | dict[]">
    The raw content of the message.
  </ParamField>

  <ParamField type="ContentBlock[]">
    The standardized [content blocks](#message-content) of the message.
  </ParamField>

  <ParamField type="dict[] | None">
    The tool calls made by the model.

    Empty if no tools are called.
  </ParamField>

  <ParamField type="string">
    A unique identifier for the message (either automatically generated by LangChain or returned in the provider response)
  </ParamField>

  <ParamField type="dict | None">
    The usage metadata of the message, which can contain token counts when available.
  </ParamField>

  <ParamField type="ResponseMetadata | None">
    The response metadata of the message.
  </ParamField>
</Accordion>

#### Tool calls

When models make [tool calls](/oss/python/langchain/models#tool-calling), they're included in the [`AIMessage`](https://reference.langchain.com/python/langchain-core/messages/ai/AIMessage):

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain.chat_models import init_chat_model

model = init_chat_model("gpt-5-nano")

def get_weather(location: str) -> str:
    """Get the weather at a location."""
    ...

model_with_tools = model.bind_tools([get_weather])
response = model_with_tools.invoke("What's the weather in Paris?")

for tool_call in response.tool_calls:
    print(f"Tool: {tool_call['name']}")
    print(f"Args: {tool_call['args']}")
    print(f"ID: {tool_call['id']}")
```

Other structured data, such as reasoning or citations, can also appear in message [content](/oss/python/langchain/messages#message-content).

#### Token usage

An [`AIMessage`](https://reference.langchain.com/python/langchain-core/messages/ai/AIMessage) can hold token counts and other usage metadata in its [`usage_metadata`](https://reference.langchain.com/python/langchain-core/messages/ai/UsageMetadata) field:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain.chat_models import init_chat_model

model = init_chat_model("gpt-5-nano")

response = model.invoke("Hello!")
response.usage_metadata
```

```
{'input_tokens': 8,
 'output_tokens': 304,
 'total_tokens': 312,
 'input_token_details': {'audio': 0, 'cache_read': 0},
 'output_token_details': {'audio': 0, 'reasoning': 256}}
```

See [`UsageMetadata`](https://reference.langchain.com/python/langchain-core/messages/ai/UsageMetadata) for details.

#### Streaming and chunks

During streaming, you'll receive [`AIMessageChunk`](https://reference.langchain.com/python/langchain-core/messages/ai/AIMessageChunk) objects that can be combined into a full message object:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
chunks = []
full_message = None
for chunk in model.stream("Hi"):
    chunks.append(chunk)
    print(chunk.text)
    full_message = chunk if full_message is None else full_message + chunk
```

<Note>
  Learn more:

  * [Streaming tokens from chat models](/oss/python/langchain/models#stream)
  * [Streaming tokens and/or steps from agents](/oss/python/langchain/streaming)
</Note>

***

### Tool message

For models that support [tool calling](/oss/python/langchain/models#tool-calling), AI messages can contain tool calls. Tool messages are used to pass the results of a single tool execution back to the model.

[Tools](/oss/python/langchain/tools) can generate [`ToolMessage`](https://reference.langchain.com/python/langchain-core/messages/tool/ToolMessage) objects directly. Below, we show a simple example. Read more in the [tools guide](/oss/python/langchain/tools).

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain.messages import AIMessage
from langchain.messages import ToolMessage

# After a model makes a tool call

# (Here, we demonstrate manually creating the messages for brevity)
ai_message = AIMessage(
    content=[],
    tool_calls=[{
        "name": "get_weather",
        "args": {"location": "San Francisco"},
        "id": "call_123"
    }]
)

# Execute tool and create result message
weather_result = "Sunny, 72°F"
tool_message = ToolMessage(
    content=weather_result,
    tool_call_id="call_123"  # Must match the call ID
)

# Continue conversation
messages = [
    HumanMessage("What's the weather in San Francisco?"),
    ai_message,  # Model's tool call
    tool_message,  # Tool execution result
]
response = model.invoke(messages)  # Model processes the result
```

<Accordion title="Attributes">
  <ParamField type="string">
    The stringified output of the tool call.
  </ParamField>

  <ParamField type="string">
    The ID of the tool call that this message is responding to. Must match the ID of the tool call in the [`AIMessage`](https://reference.langchain.com/python/langchain-core/messages/ai/AIMessage).
  </ParamField>

  <ParamField type="string">
    The name of the tool that was called.
  </ParamField>

  <ParamField type="dict">
    Additional data not sent to the model but can be accessed programmatically.
  </ParamField>
</Accordion>

<Note>
  The `artifact` field stores supplementary data that won't be sent to the model but can be accessed programmatically. This is useful for storing raw results, debugging information, or data for downstream processing without cluttering the model's context.

  <Accordion title="Example: Using artifact for retrieval metadata">
    For example, a [retrieval](/oss/python/langchain/retrieval) tool could retrieve a passage from a document for reference by a model. Where message `content` contains text that the model will reference, an `artifact` can contain document identifiers or other metadata that an application can use (e.g., to render a page). See example below:

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from langchain.messages import ToolMessage

    # Sent to model
    message_content = "It was the best of times, it was the worst of times."

    # Artifact available downstream
    artifact = {"document_id": "doc_123", "page": 0}

    tool_message = ToolMessage(
        content=message_content,
        tool_call_id="call_123",
        name="search_books",
        artifact=artifact,
    )
    ```

    See the [RAG tutorial](/oss/python/langchain/rag) for an end-to-end example of building retrieval [agents](/oss/python/langchain/agents) with LangChain.
  </Accordion>
</Note>

***

## Message content

You can think of a message's content as the payload of data that gets sent to the model. Messages have a `content` attribute that is loosely-typed, supporting strings and lists of untyped objects (e.g., dictionaries). This allows support for provider-native structures directly in LangChain chat models, such as [multimodal](#multimodal) content and other data.

Separately, LangChain provides dedicated content types for text, reasoning, citations, multi-modal data, server-side tool calls, and other message content. See [content blocks](#standard-content-blocks) below.

LangChain chat models accept message content in the `content` attribute.

This may contain either:

1. A string
2. A list of content blocks in a provider-native format
3. A list of [LangChain's standard content blocks](#standard-content-blocks)

See below for an example using [multimodal](#multimodal) inputs:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain.messages import HumanMessage

# String content
human_message = HumanMessage("Hello, how are you?")

# Provider-native format (e.g., OpenAI)
human_message = HumanMessage(content=[
    {"type": "text", "text": "Hello, how are you?"},
    {"type": "image_url", "image_url": {"url": "https://example.com/image.jpg"}}
])
