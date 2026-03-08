[Skip to main content](https://gofastmcp.com/deployment/prefect-horizon#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
Search...
Navigation
Deployment
Prefect Horizon
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
    * [Running Your Server](https://gofastmcp.com/deployment/running-server)
    * [HTTP Deployment](https://gofastmcp.com/deployment/http)
    * [Prefect Horizon](https://gofastmcp.com/deployment/prefect-horizon)
    * [Project Configuration](https://gofastmcp.com/deployment/server-configuration)


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
  * [The Platform](https://gofastmcp.com/deployment/prefect-horizon#the-platform)
  * [Prerequisites](https://gofastmcp.com/deployment/prefect-horizon#prerequisites)
  * [Getting Started](https://gofastmcp.com/deployment/prefect-horizon#getting-started)
  * [Step 1: Select a Repository](https://gofastmcp.com/deployment/prefect-horizon#step-1-select-a-repository)
  * [Step 2: Configure Your Server](https://gofastmcp.com/deployment/prefect-horizon#step-2-configure-your-server)
  * [Step 3: Deploy and Connect](https://gofastmcp.com/deployment/prefect-horizon#step-3-deploy-and-connect)
  * [Testing Your Server](https://gofastmcp.com/deployment/prefect-horizon#testing-your-server)
  * [Inspector](https://gofastmcp.com/deployment/prefect-horizon#inspector)
  * [ChatMCP](https://gofastmcp.com/deployment/prefect-horizon#chatmcp)
  * [Horizon Agents](https://gofastmcp.com/deployment/prefect-horizon#horizon-agents)


Deployment
# Prefect Horizon
Copy page
The MCP platform from the FastMCP team
Copy page
Horizon includes a **free personal tier for FastMCP users** , making it the fastest way to get a secure, production-ready server URL with built-in OAuth authentication.
Horizon is free for personal projects. Enterprise governance features are available for teams deploying to thousands of users.
##
[​](https://gofastmcp.com/deployment/prefect-horizon#the-platform)
The Platform
Horizon is organized into four integrated pillars:
  * **Deploy** : Managed hosting with CI/CD, scaling, monitoring, and rollbacks. Push code and get a live, governed endpoint in 60 seconds.
  * **Registry** : A central catalog of MCP servers across your organization—first-party, third-party, and curated remix servers composed from multiple sources.
  * **Gateway** : Role-based access control, authentication, and audit logs. Define what agents can see and do at the tool level.
  * **Agents** : A permissioned chat interface for interacting with any MCP server or curated combination of servers.

This guide focuses on **Horizon Deploy** , the managed hosting layer that gives you the fastest path from a FastMCP server to a production URL.
##
[​](https://gofastmcp.com/deployment/prefect-horizon#prerequisites)
Prerequisites
To use Horizon, you’ll need a  Your repo can be public or private, but must include at least a Python file containing a FastMCP server instance.
To verify your file is compatible with Horizon, run `fastmcp inspect <file.py:server_object>` to see what Horizon will see when it runs your server.
If you have a `requirements.txt` or `pyproject.toml` in the repo, Horizon will automatically detect your server’s dependencies and install them. Your file _can_ have an `if __name__ == "__main__"` block, but it will be ignored by Horizon. For example, a minimal server file might look like:
Copy
```
from fastmcp import FastMCP

mcp = FastMCP("MyServer")

@mcp.tool
def hello(name: str) -> str:
    return f"Hello, {name}!"

```

##
[​](https://gofastmcp.com/deployment/prefect-horizon#getting-started)
Getting Started
There are just three steps to deploying a server to Horizon:
###
[​](https://gofastmcp.com/deployment/prefect-horizon#step-1-select-a-repository)
Step 1: Select a Repository
Visit  ![Horizon repository selection](https://mintcdn.com/fastmcp/kmZMfDguWt_dAKty/assets/images/horizon/select-repo.png?fit=max&auto=format&n=kmZMfDguWt_dAKty&q=85&s=0261c7638aad85d04a4fee5598e8a662)
###
[​](https://gofastmcp.com/deployment/prefect-horizon#step-2-configure-your-server)
Step 2: Configure Your Server
Next, you’ll configure how Horizon should build and deploy your server. ![Horizon server configuration](https://mintcdn.com/fastmcp/kmZMfDguWt_dAKty/assets/images/horizon/configure-server.png?fit=max&auto=format&n=kmZMfDguWt_dAKty&q=85&s=65f08feefd47d66fc73a296246bbf1b1) The configuration screen lets you specify:
  * **Server name** : A unique name for your server. This determines your server’s URL.
  * **Description** : A brief description of what your server does.
  * **Entrypoint** : The Python file containing your FastMCP server (e.g., `main.py`). This field has the same syntax as the `fastmcp run` command—use `main.py:mcp` to specify a specific object in the file.
  * **Authentication** : When enabled, only authenticated users in your organization can connect. Horizon handles all the OAuth complexity for you.

Horizon will automatically detect your server’s Python dependencies from either a `requirements.txt` or `pyproject.toml` file.
###
[​](https://gofastmcp.com/deployment/prefect-horizon#step-3-deploy-and-connect)
Step 3: Deploy and Connect
Click **Deploy Server** and Horizon will clone your repository, build your server, and deploy it to a unique URL—typically in under 60 seconds. ![Horizon deployment view showing live server](https://mintcdn.com/fastmcp/kmZMfDguWt_dAKty/assets/images/horizon/deployment-live.png?fit=max&auto=format&n=kmZMfDguWt_dAKty&q=85&s=9df5871545f94c370ae1758f4de3b185) Once deployed, your server is accessible at a URL like:
Copy
```
https://your-server-name.fastmcp.app/mcp

```

Horizon monitors your repo and redeploys automatically whenever you push to `main`. It also builds preview deployments for every PR, so you can test changes before they go live.
##
[​](https://gofastmcp.com/deployment/prefect-horizon#testing-your-server)
Testing Your Server
Horizon provides two ways to verify your server is working before connecting external clients.
###
[​](https://gofastmcp.com/deployment/prefect-horizon#inspector)
Inspector
The Inspector gives you a structured view of everything your server exposes—tools, resources, and prompts. You can click any tool, fill in the inputs, execute it, and see the output. This is useful for systematically validating each capability and debugging specific behaviors.
###
[​](https://gofastmcp.com/deployment/prefect-horizon#chatmcp)
ChatMCP
For quick end-to-end testing, ChatMCP lets you interact with your server conversationally. It uses a fast model optimized for rapid iteration—you can verify the server works, test tool calls in context, and confirm the overall behavior before sharing it with others. ![Horizon ChatMCP interface](https://mintcdn.com/fastmcp/kmZMfDguWt_dAKty/assets/images/horizon/chat.png?fit=max&auto=format&n=kmZMfDguWt_dAKty&q=85&s=819c704307a796a29c9b08b5eca31881) ChatMCP is designed for testing, not as a daily work environment. Once you’ve confirmed your server works, you can copy connection snippets for Claude Desktop, Cursor, Claude Code, and other MCP clients—or use the FastMCP client library to connect programmatically.
##
[​](https://gofastmcp.com/deployment/prefect-horizon#horizon-agents)
Horizon Agents
Beyond testing individual servers, Horizon lets you create **Agents** —chat interfaces backed by one or more MCP servers. While ChatMCP tests a single server, Agents let you compose capabilities from multiple servers into a unified experience. ![Horizon Agent configuration](https://mintcdn.com/fastmcp/kmZMfDguWt_dAKty/assets/images/horizon/agent-detail.png?fit=max&auto=format&n=kmZMfDguWt_dAKty&q=85&s=bb4fe7f77cd4a560d02f9f7865c8840f) To create an agent:
  1. Navigate to **Agents** in the sidebar
  2. Click **Create Agent** and give it a name and description
  3. Add MCP servers to the agent—these can be servers you’ve deployed to Horizon or external servers in the registry

Once configured, you can chat with your agent directly in Horizon: ![Chatting with a Horizon Agent](https://mintcdn.com/fastmcp/kmZMfDguWt_dAKty/assets/images/horizon/agent-chat.png?fit=max&auto=format&n=kmZMfDguWt_dAKty&q=85&s=63371310b14c6224de18f0cc0a0af123) Agents are useful for creating purpose-built interfaces that combine tools from different servers. For example, you might create an agent that has access to both your company’s internal data server and a general-purpose utilities server.
[ HTTP Deployment Previous ](https://gofastmcp.com/deployment/http)[ Project Configuration Next ](https://gofastmcp.com/deployment/server-configuration)
Ctrl+I
![Horizon repository selection](https://mintcdn.com/fastmcp/kmZMfDguWt_dAKty/assets/images/horizon/select-repo.png?w=840&fit=max&auto=format&n=kmZMfDguWt_dAKty&q=85&s=dfb39f7ec4b32f592fab3330149aec53)
![Horizon server configuration](https://mintcdn.com/fastmcp/kmZMfDguWt_dAKty/assets/images/horizon/configure-server.png?w=840&fit=max&auto=format&n=kmZMfDguWt_dAKty&q=85&s=1d040da9300d5ec48524cab93c085539)
![Horizon deployment view showing live server](https://mintcdn.com/fastmcp/kmZMfDguWt_dAKty/assets/images/horizon/deployment-live.png?w=840&fit=max&auto=format&n=kmZMfDguWt_dAKty&q=85&s=f2c1d00412ac38d44a5bac972b41c8b7)
![Horizon ChatMCP interface](https://mintcdn.com/fastmcp/kmZMfDguWt_dAKty/assets/images/horizon/chat.png?w=840&fit=max&auto=format&n=kmZMfDguWt_dAKty&q=85&s=e5b543184fd0415dbcf20e293397d4a8)
![Horizon Agent configuration](https://mintcdn.com/fastmcp/kmZMfDguWt_dAKty/assets/images/horizon/agent-detail.png?w=840&fit=max&auto=format&n=kmZMfDguWt_dAKty&q=85&s=a8b1a430eccafb8e783cadf029a3d3db)
![Chatting with a Horizon Agent](https://mintcdn.com/fastmcp/kmZMfDguWt_dAKty/assets/images/horizon/agent-chat.png?w=840&fit=max&auto=format&n=kmZMfDguWt_dAKty&q=85&s=a9d6f44e4ea7a8be4814659fcd46a8f0)
