[Skip to main content](https://gofastmcp.com/clients/sampling#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
Search...
Navigation
Handlers
LLM Sampling
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
  * [Handler Template](https://gofastmcp.com/clients/sampling#handler-template)
  * [Handler Parameters](https://gofastmcp.com/clients/sampling#handler-parameters)
  * [Built-in Handlers](https://gofastmcp.com/clients/sampling#built-in-handlers)
  * [OpenAI Handler](https://gofastmcp.com/clients/sampling#openai-handler)
  * [Anthropic Handler](https://gofastmcp.com/clients/sampling#anthropic-handler)
  * [Google Gemini Handler](https://gofastmcp.com/clients/sampling#google-gemini-handler)
  * [Sampling Capabilities](https://gofastmcp.com/clients/sampling#sampling-capabilities)
  * [Tool Execution](https://gofastmcp.com/clients/sampling#tool-execution)


Handlers
# LLM Sampling
Copy page
Handle server-initiated LLM completion requests.
Copy page
`2.0.0` Use this when you need to respond to server requests for LLM completions. MCP servers can request LLM completions from clients during tool execution. This enables servers to delegate AI reasoning to the client, which controls which LLM is used and how requests are made.
##
[​](https://gofastmcp.com/clients/sampling#handler-template)
Handler Template
Copy
```
from fastmcp import Client
from fastmcp.client.sampling import SamplingMessage, SamplingParams, RequestContext

async def sampling_handler(
    messages: list[SamplingMessage],
    params: SamplingParams,
    context: RequestContext
) -> str:
    """
    Handle server requests for LLM completions.

    Args:
        messages: Conversation messages to send to the LLM
        params: Sampling parameters (temperature, max_tokens, etc.)
        context: Request context with metadata

    Returns:
        Generated text response from your LLM
    """
    # Extract message content
    conversation = []
    for message in messages:
        content = message.content.text if hasattr(message.content, 'text') else str(message.content)
        conversation.append(f"{message.role}: {content}")

    # Use the system prompt if provided
    system_prompt = params.systemPrompt or "You are a helpful assistant."

    # Integrate with your LLM service here
    return "Generated response based on the messages"

client = Client(
    "my_mcp_server.py",
    sampling_handler=sampling_handler,
)

```

##
[​](https://gofastmcp.com/clients/sampling#handler-parameters)
Handler Parameters
## SamplingMessage
[​](https://gofastmcp.com/clients/sampling#param-role)
role
Literal["user", "assistant"]
The role of the message
[​](https://gofastmcp.com/clients/sampling#param-content)
content
TextContent | ImageContent | AudioContent
The content of the message. TextContent has a `.text` attribute.
## SamplingParams
[​](https://gofastmcp.com/clients/sampling#param-system-prompt)
systemPrompt
str | None
Optional system prompt the server wants to use
[​](https://gofastmcp.com/clients/sampling#param-model-preferences)
modelPreferences
ModelPreferences | None
Server preferences for model selection (hints, cost/speed/intelligence priorities)
[​](https://gofastmcp.com/clients/sampling#param-temperature)
temperature
float | None
Sampling temperature
[​](https://gofastmcp.com/clients/sampling#param-max-tokens)
maxTokens
int
Maximum tokens to generate
[​](https://gofastmcp.com/clients/sampling#param-stop-sequences)
stopSequences
list[str] | None
Stop sequences for sampling
[​](https://gofastmcp.com/clients/sampling#param-tools)
tools
list[Tool] | None
Tools the LLM can use during sampling
[​](https://gofastmcp.com/clients/sampling#param-tool-choice)
toolChoice
ToolChoice | None
Tool usage behavior (`auto`, `required`, or `none`)
##
[​](https://gofastmcp.com/clients/sampling#built-in-handlers)
Built-in Handlers
FastMCP provides built-in handlers for OpenAI, Anthropic, and Google Gemini APIs that support the full sampling API including tool use.
###
[​](https://gofastmcp.com/clients/sampling#openai-handler)
OpenAI Handler
`2.11.0`
Copy
```
from fastmcp import Client
from fastmcp.client.sampling.handlers.openai import OpenAISamplingHandler

client = Client(
    "my_mcp_server.py",
    sampling_handler=OpenAISamplingHandler(default_model="gpt-4o"),
)

```

For OpenAI-compatible APIs (like local models):
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
[​](https://gofastmcp.com/clients/sampling#anthropic-handler)
Anthropic Handler
`2.14.1`
Copy
```
from fastmcp import Client
from fastmcp.client.sampling.handlers.anthropic import AnthropicSamplingHandler

client = Client(
    "my_mcp_server.py",
    sampling_handler=AnthropicSamplingHandler(default_model="claude-sonnet-4-5"),
)

```

Install the Anthropic handler with `pip install fastmcp[anthropic]`.
###
[​](https://gofastmcp.com/clients/sampling#google-gemini-handler)
Google Gemini Handler
`3.1.0`
Copy
```
from fastmcp import Client
from fastmcp.client.sampling.handlers.google_genai import GoogleGenAISamplingHandler

client = Client(
    "my_mcp_server.py",
    sampling_handler=GoogleGenAISamplingHandler(default_model="gemini-2.0-flash"),
)

```

Install the Google Gemini handler with `pip install fastmcp[gemini]`.
##
[​](https://gofastmcp.com/clients/sampling#sampling-capabilities)
Sampling Capabilities
When you provide a `sampling_handler`, FastMCP automatically advertises full sampling capabilities to the server, including tool support. To disable tool support for simpler handlers:
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
[​](https://gofastmcp.com/clients/sampling#tool-execution)
Tool Execution
Tool execution happens on the server side. The client’s role is to pass tools to the LLM and return the LLM’s response (which may include tool use requests). The server then executes the tools and may send follow-up sampling requests with tool results.
To implement a custom sampling handler, see the
[ Notifications Previous ](https://gofastmcp.com/clients/notifications)[ User Elicitation Next ](https://gofastmcp.com/clients/elicitation)
Ctrl+I
