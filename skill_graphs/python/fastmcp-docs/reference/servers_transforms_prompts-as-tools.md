[Skip to main content](https://gofastmcp.com/servers/transforms/prompts-as-tools#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
Search...
Navigation
Transforms
Prompts as Tools
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
    * [ Overview NEW ](https://gofastmcp.com/servers/transforms/transforms)
    * [ Namespace NEW ](https://gofastmcp.com/servers/transforms/namespace)
    * [ Tool Transformation NEW ](https://gofastmcp.com/servers/transforms/tool-transformation)
    * [ Visibility NEW ](https://gofastmcp.com/servers/visibility)
    * [ Code Mode NEW ](https://gofastmcp.com/servers/transforms/code-mode)
    * [ Tool Search NEW ](https://gofastmcp.com/servers/transforms/tool-search)
    * [ Resources as Tools NEW ](https://gofastmcp.com/servers/transforms/resources-as-tools)
    * [ Prompts as Tools NEW ](https://gofastmcp.com/servers/transforms/prompts-as-tools)
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
  * [Basic Usage](https://gofastmcp.com/servers/transforms/prompts-as-tools#basic-usage)
  * [Listing Prompts](https://gofastmcp.com/servers/transforms/prompts-as-tools#listing-prompts)
  * [Getting Prompts](https://gofastmcp.com/servers/transforms/prompts-as-tools#getting-prompts)
  * [Message Format](https://gofastmcp.com/servers/transforms/prompts-as-tools#message-format)
  * [Binary Content](https://gofastmcp.com/servers/transforms/prompts-as-tools#binary-content)


Transforms
# Prompts as Tools
Copy page
Expose prompts to tool-only clients
Copy page
`3.0.0` Some MCP clients only support tools. They cannot list or get prompts directly because they lack prompt protocol support. The `PromptsAsTools` transform bridges this gap by generating tools that provide access to your server’s prompts. When you add `PromptsAsTools` to a server, it creates two tools that clients can call instead of using the prompt protocol:
  * **`list_prompts`**returns JSON describing all available prompts and their arguments
  * **`get_prompt`**renders a specific prompt with provided arguments

This means any client that can call tools can now access prompts, even if the client has no native prompt support.
##
[​](https://gofastmcp.com/servers/transforms/prompts-as-tools#basic-usage)
Basic Usage
Pass your server to `PromptsAsTools` when adding the transform. The transform queries that server for prompts whenever the generated tools are called.
Copy
```
from fastmcp import FastMCP
from fastmcp.server.transforms import PromptsAsTools

mcp = FastMCP("My Server")

@mcp.prompt
def analyze_code(code: str, language: str = "python") -> str:
    """Analyze code for potential issues."""
    return f"Analyze this {language} code:\n{code}"

@mcp.prompt
def explain_concept(concept: str) -> str:
    """Explain a programming concept."""
    return f"Explain: {concept}"

# Add the transform - creates list_prompts and get_prompt tools
mcp.add_transform(PromptsAsTools(mcp))

```

Clients now see three items: whatever tools you defined directly, plus `list_prompts` and `get_prompt`.
##
[​](https://gofastmcp.com/servers/transforms/prompts-as-tools#listing-prompts)
Listing Prompts
The `list_prompts` tool returns JSON with metadata for each prompt, including its arguments.
Copy
```
result = await client.call_tool("list_prompts", {})
prompts = json.loads(result.data)
# [
#   {
#     "name": "analyze_code",
#     "description": "Analyze code for potential issues.",
#     "arguments": [
#       {"name": "code", "description": null, "required": true},
#       {"name": "language", "description": null, "required": false}
#     ]
#   },
#   {
#     "name": "explain_concept",
#     "description": "Explain a programming concept.",
#     "arguments": [
#       {"name": "concept", "description": null, "required": true}
#     ]
#   }
#]

```

Each argument includes:
  * `name`: The argument name
  * `description`: Optional description from type hints or docstrings
  * `required`: Whether the argument must be provided


##
[​](https://gofastmcp.com/servers/transforms/prompts-as-tools#getting-prompts)
Getting Prompts
The `get_prompt` tool accepts a prompt name and optional arguments dict. It returns the rendered prompt as JSON with a messages array.
Copy
```
# Prompt with required and optional arguments
result = await client.call_tool(
    "get_prompt",
    {
        "name": "analyze_code",
        "arguments": {
            "code": "x = 1\nprint(x)",
            "language": "python"
        }
    }
)

response = json.loads(result.data)
# {
#   "messages": [
#     {
#       "role": "user",
#       "content": "Analyze this python code:\nx = 1\nprint(x)"
#     }
#   ]
# }

```

If a prompt has no arguments, you can omit the `arguments` field or pass an empty dict:
Copy
```
result = await client.call_tool(
    "get_prompt",
    {"name": "simple_prompt"}
)

```

##
[​](https://gofastmcp.com/servers/transforms/prompts-as-tools#message-format)
Message Format
Rendered prompts return a messages array following the standard MCP format. Each message includes:
  * `role`: The message role (“user” or “assistant”)
  * `content`: The message text content

Multi-message prompts are supported - the array will contain all messages in order.
##
[​](https://gofastmcp.com/servers/transforms/prompts-as-tools#binary-content)
Binary Content
Unlike resources, prompts always return text content. There is no binary encoding needed.
[ Resources as Tools Previous ](https://gofastmcp.com/servers/transforms/resources-as-tools)[ Authentication Next ](https://gofastmcp.com/servers/auth/authentication)
Ctrl+I
