[Skip to main content](https://gofastmcp.com/v2/clients/sampling#content-area)
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
  * [Sampling Handler](https://gofastmcp.com/v2/clients/sampling#sampling-handler)
  * [Handler Parameters](https://gofastmcp.com/v2/clients/sampling#handler-parameters)
  * [Basic Example](https://gofastmcp.com/v2/clients/sampling#basic-example)
  * [Sampling Capabilities](https://gofastmcp.com/v2/clients/sampling#sampling-capabilities)
  * [Built-in Handlers](https://gofastmcp.com/v2/clients/sampling#built-in-handlers)
  * [OpenAI Handler](https://gofastmcp.com/v2/clients/sampling#openai-handler)
  * [Anthropic Handler](https://gofastmcp.com/v2/clients/sampling#anthropic-handler)
  * [Tool Execution](https://gofastmcp.com/v2/clients/sampling#tool-execution)


Advanced Features
# LLM Sampling
Copy page
Handle server-initiated LLM sampling requests.
Copy page
`2.0.0` MCP servers can request LLM completions from clients. The client handles these requests through a sampling handler callback.
##
[​](https://gofastmcp.com/v2/clients/sampling#sampling-handler)
Sampling Handler
Provide a `sampling_handler` function when creating the client:
Copy
```
from fastmcp import Client
from fastmcp.client.sampling import (
    SamplingMessage,
    SamplingParams,
    RequestContext,
)

async def sampling_handler(
    messages: list[SamplingMessage],
    params: SamplingParams,
    context: RequestContext
) -> str:
    # Your LLM integration logic here
    # Extract text from messages and generate a response
    return "Generated response based on the messages"

client = Client(
    "my_mcp_server.py",
    sampling_handler=sampling_handler,
)

```

###
[​](https://gofastmcp.com/v2/clients/sampling#handler-parameters)
Handler Parameters
The sampling handler receives three parameters:
## Sampling Handler Parameters
[​](https://gofastmcp.com/v2/clients/sampling#param-sampling-message)
SamplingMessage
Sampling Message Object
Show attributes
[​](https://gofastmcp.com/v2/clients/sampling#param-role)
role
Literal["user", "assistant"]
The role of the message.
[​](https://gofastmcp.com/v2/clients/sampling#param-content)
content
TextContent | ImageContent | AudioContent
The content of the message.TextContent is most common, and has a `.text` attribute.
[​](https://gofastmcp.com/v2/clients/sampling#param-sampling-params)
SamplingParams
Sampling Parameters Object
Show attributes
[​](https://gofastmcp.com/v2/clients/sampling#param-messages)
messages
list[SamplingMessage]
The messages to sample from
[​](https://gofastmcp.com/v2/clients/sampling#param-model-preferences)
modelPreferences
ModelPreferences | None
The server’s preferences for which model to select. The client MAY ignore these preferences.
Show attributes
[​](https://gofastmcp.com/v2/clients/sampling#param-hints)
hints
list[ModelHint] | None
The hints to use for model selection.
[​](https://gofastmcp.com/v2/clients/sampling#param-cost-priority)
costPriority
float | None
The cost priority for model selection.
[​](https://gofastmcp.com/v2/clients/sampling#param-speed-priority)
speedPriority
float | None
The speed priority for model selection.
[​](https://gofastmcp.com/v2/clients/sampling#param-intelligence-priority)
intelligencePriority
float | None
The intelligence priority for model selection.
[​](https://gofastmcp.com/v2/clients/sampling#param-system-prompt)
systemPrompt
str | None
An optional system prompt the server wants to use for sampling.
[​](https://gofastmcp.com/v2/clients/sampling#param-include-context)
includeContext
IncludeContext | None
A request to include context from one or more MCP servers (including the caller), to be attached to the prompt.
[​](https://gofastmcp.com/v2/clients/sampling#param-temperature)
temperature
float | None
The sampling temperature.
[​](https://gofastmcp.com/v2/clients/sampling#param-max-tokens)
maxTokens
int
The maximum number of tokens to sample.
[​](https://gofastmcp.com/v2/clients/sampling#param-stop-sequences)
stopSequences
list[str] | None
The stop sequences to use for sampling.
[​](https://gofastmcp.com/v2/clients/sampling#param-metadata)
metadata
dict[str, Any] | None
Optional metadata to pass through to the LLM provider.
[​](https://gofastmcp.com/v2/clients/sampling#param-tools)
tools
list[Tool] | None
Optional list of tools the LLM can use during sampling. See [Using the OpenAI Handler](https://gofastmcp.com/v2/clients/sampling#using-the-openai-handler).
[​](https://gofastmcp.com/v2/clients/sampling#param-tool-choice)
toolChoice
ToolChoice | None
Optional control over tool usage behavior (`auto`, `required`, or `none`).
[​](https://gofastmcp.com/v2/clients/sampling#param-request-context)
RequestContext
Request Context Object
Show attributes
[​](https://gofastmcp.com/v2/clients/sampling#param-request-id)
request_id
RequestId
Unique identifier for the MCP request
##
[​](https://gofastmcp.com/v2/clients/sampling#basic-example)
Basic Example
Copy
```
from fastmcp import Client
from fastmcp.client.sampling import SamplingMessage, SamplingParams, RequestContext

async def basic_sampling_handler(
    messages: list[SamplingMessage],
    params: SamplingParams,
    context: RequestContext
) -> str:
    # Extract message content
    conversation = []
    for message in messages:
        content = message.content.text if hasattr(message.content, 'text') else str(message.content)
        conversation.append(f"{message.role}: {content}")

    # Use the system prompt if provided
    system_prompt = params.systemPrompt or "You are a helpful assistant."

    # Here you would integrate with your preferred LLM service
    # This is just a placeholder response
    return f"Response based on conversation: {' | '.join(conversation)}"

client = Client(
    "my_mcp_server.py",
    sampling_handler=basic_sampling_handler
)

```

If the client doesn’t provide a sampling handler, servers can optionally configure a fallback handler. See [Server Sampling](https://gofastmcp.com/v2/servers/sampling#sampling-fallback-handler) for details.
##
[​](https://gofastmcp.com/v2/clients/sampling#sampling-capabilities)
Sampling Capabilities
When you provide a `sampling_handler`, FastMCP automatically advertises full sampling capabilities to the server, including tool support. To disable tool support (for simpler handlers that don’t support tools), pass `sampling_capabilities` explicitly:
Copy
```
from mcp.types import SamplingCapability

client = Client(
    "my_mcp_server.py",
    sampling_handler=basic_handler,
    sampling_capabilities=SamplingCapability(),  # No tool support
)

```

##
[​](https://gofastmcp.com/v2/clients/sampling#built-in-handlers)
Built-in Handlers
FastMCP provides built-in sampling handlers for OpenAI and Anthropic APIs. These handlers support the full sampling API including tool use, handling message conversion and response formatting automatically.
###
[​](https://gofastmcp.com/v2/clients/sampling#openai-handler)
OpenAI Handler
`2.11.0` The OpenAI handler works with OpenAI’s API and any OpenAI-compatible provider:
Copy
```
from fastmcp import Client
from fastmcp.client.sampling.handlers.openai import OpenAISamplingHandler

client = Client(
    "my_mcp_server.py",
    sampling_handler=OpenAISamplingHandler(default_model="gpt-4o"),
)

```

For OpenAI-compatible APIs (like local models), pass a custom client:
Copy
```
from openai import AsyncOpenAI

client = Client(
    "my_mcp_server.py",
    sampling_handler=OpenAISamplingHandler(
        default_model="llama-3.1-70b",
        client=AsyncOpenAI(base_url="http://localhost:8000/v1"),
    ),
)

```

Install the OpenAI handler with `pip install fastmcp[openai]`.
###
[​](https://gofastmcp.com/v2/clients/sampling#anthropic-handler)
Anthropic Handler
`2.14.1` The Anthropic handler uses Claude models via the Anthropic API:
Copy
```
from fastmcp import Client
from fastmcp.client.sampling.handlers.anthropic import AnthropicSamplingHandler

client = Client(
    "my_mcp_server.py",
    sampling_handler=AnthropicSamplingHandler(default_model="claude-sonnet-4-5"),
)

```

You can pass a custom client for advanced configuration:
Copy
```
from anthropic import AsyncAnthropic

client = Client(
    "my_mcp_server.py",
    sampling_handler=AnthropicSamplingHandler(
        default_model="claude-sonnet-4-5",
        client=AsyncAnthropic(),  # Uses ANTHROPIC_API_KEY env var
    ),
)

```

Install the Anthropic handler with `pip install fastmcp[anthropic]`.
###
[​](https://gofastmcp.com/v2/clients/sampling#tool-execution)
Tool Execution
Tool execution happens on the server side. The client’s role is to pass tools to the LLM and return the LLM’s response (which may include tool use requests). The server then executes the tools and may send follow-up sampling requests with tool results.
To implement a custom sampling handler, see the
[ Progress Monitoring Previous ](https://gofastmcp.com/v2/clients/progress)[ Background Tasks Next ](https://gofastmcp.com/v2/clients/tasks)
Ctrl+I
