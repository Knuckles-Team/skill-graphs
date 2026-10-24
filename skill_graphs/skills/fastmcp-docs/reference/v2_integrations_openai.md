[Skip to main content](https://gofastmcp.com/v2/integrations/openai#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v2.14.5
Search...
Navigation
AI SDKs
OpenAI API 🤝 FastMCP
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
  * Authentication


##### Integrations
  * Authentication
  * Authorization
  * AI Assistants
  * AI SDKs
    * [Anthropic API](https://gofastmcp.com/v2/integrations/anthropic)
    * [Gemini SDK](https://gofastmcp.com/v2/integrations/gemini)
    * [OpenAI API](https://gofastmcp.com/v2/integrations/openai)
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
  * [Responses API](https://gofastmcp.com/v2/integrations/openai#responses-api)
  * [Create a Server](https://gofastmcp.com/v2/integrations/openai#create-a-server)
  * [Deploy the Server](https://gofastmcp.com/v2/integrations/openai#deploy-the-server)
  * [Call the Server](https://gofastmcp.com/v2/integrations/openai#call-the-server)
  * [Authentication](https://gofastmcp.com/v2/integrations/openai#authentication)
  * [Server Authentication](https://gofastmcp.com/v2/integrations/openai#server-authentication)
  * [Client Authentication](https://gofastmcp.com/v2/integrations/openai#client-authentication)


AI SDKs
# OpenAI API 🤝 FastMCP
Copy page
Connect FastMCP servers to the OpenAI API
Copy page
##
[​](https://gofastmcp.com/v2/integrations/openai#responses-api)
Responses API
OpenAI’s
The Responses API is a distinct API from OpenAI’s Completions API or Assistants API. At this time, only the Responses API supports MCP.
Currently, the Responses API only accesses **tools** from MCP servers—it queries the `list_tools` endpoint and exposes those functions to the AI agent. Other MCP features like resources and prompts are not currently supported.
###
[​](https://gofastmcp.com/v2/integrations/openai#create-a-server)
Create a Server
First, create a FastMCP server with the tools you want to expose. For this example, we’ll create a server with a single tool that rolls dice.
server.py
Copy
```
import random
from fastmcp import FastMCP

mcp = FastMCP(name="Dice Roller")

@mcp.tool
def roll_dice(n_dice: int) -> list[int]:
    """Roll `n_dice` 6-sided dice and return the results."""
    return [random.randint(1, 6) for _ in range(n_dice)]

if __name__ == "__main__":
    mcp.run(transport="http", port=8000)

```

###
[​](https://gofastmcp.com/v2/integrations/openai#deploy-the-server)
Deploy the Server
Your server must be deployed to a public URL in order for OpenAI to access it. For development, you can use tools like `ngrok` to temporarily expose a locally-running server to the internet. We’ll do that for this example (you may need to install `ngrok` and create a free account), but you can use any other method to deploy your server. Assuming you saved the above code as `server.py`, you can run the following two commands in two separate terminals to deploy your server and expose it to the internet:
FastMCP server
ngrok
Copy
```
python server.py

```

This exposes your unauthenticated server to the internet. Only run this command in a safe environment if you understand the risks.
###
[​](https://gofastmcp.com/v2/integrations/openai#call-the-server)
Call the Server
To use the Responses API, you’ll need to install the OpenAI Python SDK (not included with FastMCP):
Copy
```
pip install openai

```

You’ll also need to authenticate with OpenAI. You can do this by setting the `OPENAI_API_KEY` environment variable. Consult the OpenAI SDK documentation for more information.
Copy
```
export OPENAI_API_KEY="your-api-key"

```

Here is an example of how to call your server from Python. Note that you’ll need to replace `https://your-server-url.com` with the actual URL of your server. In addition, we use `/mcp/` as the endpoint because we deployed a streamable-HTTP server with the default path; you may need to use a different endpoint if you customized your server’s deployment.
Copy
```
from openai import OpenAI

# Your server URL (replace with your actual URL)
url = 'https://your-server-url.com'

client = OpenAI()

resp = client.responses.create(
    model="gpt-4.1",
    tools=[
        {
            "type": "mcp",
            "server_label": "dice_server",
            "server_url": f"{url}/mcp/",
            "require_approval": "never",
        },
    ],
    input="Roll a few dice!",
)

print(resp.output_text)

```

If you run this code, you’ll see something like the following output:
Copy
```
You rolled 3 dice and got the following results: 6, 4, and 2!

```

###
[​](https://gofastmcp.com/v2/integrations/openai#authentication)
Authentication
`2.6.0` The Responses API can include headers to authenticate the request, which means you don’t have to worry about your server being publicly accessible.
####
[​](https://gofastmcp.com/v2/integrations/openai#server-authentication)
Server Authentication
The simplest way to add authentication to the server is to use a bearer token scheme. For this example, we’ll quickly generate our own tokens with FastMCP’s `RSAKeyPair` utility, but this may not be appropriate for production use. For more details, see the complete server-side [Token Verification](https://gofastmcp.com/v2/servers/auth/token-verification) documentation. We’ll start by creating an RSA key pair to sign and verify tokens.
Copy
```
from fastmcp.server.auth.providers.jwt import RSAKeyPair

key_pair = RSAKeyPair.generate()
access_token = key_pair.create_token(audience="dice-server")

```

FastMCP’s `RSAKeyPair` utility is for development and testing only.
Next, we’ll create a `JWTVerifier` to authenticate the server.
Copy
```
from fastmcp import FastMCP
from fastmcp.server.auth import JWTVerifier

auth = JWTVerifier(
    public_key=key_pair.public_key,
    audience="dice-server",
)

mcp = FastMCP(name="Dice Roller", auth=auth)

```

Here is a complete example that you can copy/paste. For simplicity and the purposes of this example only, it will print the token to the console. **Do NOT do this in production!**
server.py
Copy
```
from fastmcp import FastMCP
from fastmcp.server.auth import JWTVerifier
from fastmcp.server.auth.providers.jwt import RSAKeyPair
import random

key_pair = RSAKeyPair.generate()
access_token = key_pair.create_token(audience="dice-server")

auth = JWTVerifier(
    public_key=key_pair.public_key,
    audience="dice-server",
)

mcp = FastMCP(name="Dice Roller", auth=auth)

@mcp.tool
def roll_dice(n_dice: int) -> list[int]:
    """Roll `n_dice` 6-sided dice and return the results."""
    return [random.randint(1, 6) for _ in range(n_dice)]

if __name__ == "__main__":
    print(f"\n---\n\n🔑 Dice Roller access token:\n\n{access_token}\n\n---\n")
    mcp.run(transport="http", port=8000)

```

####
[​](https://gofastmcp.com/v2/integrations/openai#client-authentication)
Client Authentication
If you try to call the authenticated server with the same OpenAI code we wrote earlier, you’ll get an error like this:
Copy
```
pythonAPIStatusError: Error code: 424 - {
    "error": {
        "message": "Error retrieving tool list from MCP server: 'dice_server'. Http status code: 401 (Unauthorized)",
        "type": "external_connector_error",
        "param": "tools",
        "code": "http_error"
    }
}

```

As expected, the server is rejecting the request because it’s not authenticated. To authenticate the client, you can pass the token in the `Authorization` header with the `Bearer` scheme:
Copy
```
from openai import OpenAI

# Your server URL (replace with your actual URL)
url = 'https://your-server-url.com'

# Your access token (replace with your actual token)
access_token = 'your-access-token'

client = OpenAI()

resp = client.responses.create(
    model="gpt-4.1",
    tools=[
        {
            "type": "mcp",
            "server_label": "dice_server",
            "server_url": f"{url}/mcp/",
            "require_approval": "never",
            "headers": {
                "Authorization": f"Bearer {access_token}"
            }
        },
    ],
    input="Roll a few dice!",
)

print(resp.output_text)

```

You should now see the dice roll results in the output.
[ Gemini SDK 🤝 FastMCP Previous ](https://gofastmcp.com/v2/integrations/gemini)[ FastAPI 🤝 FastMCP Next ](https://gofastmcp.com/v2/integrations/fastapi)
Ctrl+I
