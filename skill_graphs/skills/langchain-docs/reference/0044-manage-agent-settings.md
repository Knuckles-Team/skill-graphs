# Manage agent settings
Source: https://docs.langchain.com/langsmith/fleet/manage-agent-settings

Manage your agents in Fleet.

This page explains how to manage the settings for your agents in LangSmith Fleet.

## Change the model

To change the model for your agent:

1. In the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-fleet-manage-agent-settings), navigate to your agent's inbox.
2. Next to the agent name, click the <Icon icon="pencil" /> **Edit Agent** icon.
3. In the top right corner, click the <Icon icon="settings" /> **Settings** icon.
4. Select the **Model** you want to use.
5. Enter the API key for the model.

For information on how to add a custom model, see [Custom models](/langsmith/fleet/essentials#custom-models).

## Reconnect tool integrations

To reconnect a tool integration to an agent:

1. In the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-fleet-manage-agent-settings), navigate to your agent's inbox.
2. Next to the agent name, click the <Icon icon="pencil" /> **Edit Agent** icon.
3. In the top right corner, click the <Icon icon="settings" /> **Settings** icon.
4. In the **Connected Integrations** section, click the **Connect** button next to the tool you want to reconnect.

## Download agent files

To download the files for your agent, click the <Icon icon="settings" /> **Settings** icon in the top right corner of the agent and select **Download ZIP**. This will export the agent configuration as a ZIP file.

## Change access to the agent

Agents can either be private to the creator or shared within a LangSmith workspace.

| Feature                  | Private agents                          | [Workspace agents](#workspace-scoped-agent-details)                                                                    |
| ------------------------ | --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **Ownership and access** | Only visible to creator                 | Visible to anyone within the same LangSmith workspace                                                                  |
| **OAuth authentication** | OAuth credentials are scoped to creator | OAuth credentials are scoped to each user; new users cloning workspace agents must re-authenticate with selected tools |
| **Secrets**              | Uses workspace-scoped LangSmith secrets | Uses workspace-scoped LangSmith secrets (same as private agents)                                                       |

To change the agent visibility, click the <Icon icon="lock" /> **Visibility settings** icon in the top right corner of the agent and select either **Only me** or **Workspace**.

### Workspace-scoped agent details

While workspace-scoped agents are shared, some details are public, while others are private:

* **Threads are always user-scoped**, so even if an agent is workspace-scoped, the chat history created within that agent will always be private and only accessible to the specific user who created them.
* **The system prompt, selected tools, and sub-agents will be public on workspace-scoped agents.** Users will not be able to modify these fields on the original workspace-scoped agent, but can make changes once they've cloned the agent.
* **The channel type on workspace-scoped agents is public** (for example, Slack message received), but the specific connection with the channel (for example, the Slack channel, or Gmail address) is not shared. This way, users know what channel to use when cloning an agent, but can't gain unauthorized access to any connections the original user has set up.

## Update memory

Your agent can remember information from previous conversations and use it to make better decisions in future conversations. Agents persist memories by writing files to a **memories folder** using `write_file` and `edit_file` tool calls.

By default, your agent requires approval before saving to the memories folder. When this setting is enabled, the agent pauses and waits for you to accept, edit, or reject each memory update in the Fleet UI before continuing.

<Tip>
  If your agent runs on a [schedule](/langsmith/fleet/schedules#add-a-schedule) or other automated schedule, disable the memory approval requirement. Otherwise, the agent will pause on every scheduled run that involves a memory update and wait indefinitely for manual approval.
</Tip>

### Disable required approval for memory updates

To disable the memory approval requirement:

1. In the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-fleet-manage-agent-settings), navigate to your agent's inbox.
2. Next to the agent name, click the <Icon icon="pencil" /> **Edit Agent** icon.
3. In the top right corner, click the <Icon icon="settings" /> **Settings** icon.
4. In the **Memory** section, toggle **Require approval to update memories** to off.

## Use the agent programmatically

You can use the [LangGraph SDK](/langsmith/reference) to connect to your agent through code. To view the code snippets needed to call your agent programmatically:

1. In the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-fleet-manage-agent-settings), navigate to your agent's inbox.
2. Next to the agent name, click the <Icon icon="pencil" /> **Edit Agent** icon.
3. In the top right corner, click the <Icon icon="settings" /> **Settings** icon.
4. Click the **View code snippets** button.
5. Copy the pre-populated code snippets for your agent.

For more information, see [Call agents from code](/langsmith/fleet/code).

## Pause agent

To pause an agent, pause its channels:

1. In the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-fleet-manage-agent-settings), navigate to your agent's inbox.
2. Next to the agent name, click the <Icon icon="pencil" /> **Edit Agent** icon.
3. In the graph view, click the **Pause** button in the **Channels** box.
4. Click **Save Changes**.

<Tip>
  To resume, click the **Resume channels** button in the **Channels** box.
</Tip>

## Delete agent

To permanently delete an agent:

1. In the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-fleet-manage-agent-settings), navigate to your agent's inbox.
2. Next to the agent name, click the <Icon icon="pencil" /> **Edit Agent** icon.
3. In the top right corner, click the <Icon icon="settings" /> **Settings** icon.
4. Click the **Delete Agent** button.
5. To confirm the deletion, click the **Delete** button.

<Warning>
  This action cannot be undone. It will permanently delete the agent, all threads linked to the agent, and unlink any attached channels.
</Warning>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/fleet/manage-agent-settings.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# LangSmith Tool Server
Source: https://docs.langchain.com/langsmith/fleet/mcp-framework

The LangSmith Tool Server is a standalone MCP framework for building and deploying tools with built-in authentication and authorization. Use the Tool Server when you want to:

* [Create custom tools](#create-a-custom-toolkit) that integrate with LangSmith's [Agent Auth](/langsmith/agent-auth) for OAuth authentication
* [Build an MCP gateway](#use-as-an-mcp-gateway) for agents you're building yourself (outside of Fleet)

<Note>
  If you're using [Fleet](/langsmith/fleet/index), you don't need to interact with the Tool Server directly. Fleet provides [built-in tools](/langsmith/fleet/tools) and supports [remote MCP servers](/langsmith/fleet/remote-mcp-servers) without requiring Tool Server setup.

  However, you can configure the associated tool server instance as an MCP server, which will allow you to use your custom MCP servers in your agent.
</Note>

Download the [PyPI package](https://pypi.org/project/langsmith-tool-server/) to get started.

## Create a custom toolkit

Install the LangSmith Tool Server and LangChain CLI:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
pip install langsmith-tool-server
pip install langchain-cli-v2
```

Create a new toolkit:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
langchain tools new my-toolkit
cd my-toolkit
```

This creates a toolkit with the following structure:

```
my-toolkit/
├── pyproject.toml
├── toolkit.toml
└── my_toolkit/
    ├── __init__.py
    ├── auth.py
    └── tools/
        ├── __init__.py
        └── ...
```

Define your tools using the `@tool` decorator. For more on tool schemas, return values, error handling, and `ToolRuntime`, see the [Tools guide](/oss/python/langchain/tools).

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langsmith_tool_server import tool

@tool
def hello(name: str) -> str:
    """Greet someone by name."""
    return f"Hello, {name}!"

@tool
def add(x: int, y: int) -> int:
    """Add two numbers."""
    return x + y

TOOLS = [hello, add]
```

Run the server:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
langchain tools serve
```

Your tool server will start on `http://localhost:8000`.

## Call tools via MCP protocol

Below is an example that lists available tools and calls the `add` tool:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import asyncio
import aiohttp

async def mcp_request(url: str, method: str, params: dict = None):
    async with aiohttp.ClientSession() as session:
        payload = {"jsonrpc": "2.0", "method": method, "params": params or {}, "id": 1}
        async with session.post(f"{url}/mcp", json=payload) as response:
            return await response.json()

async def main():
    url = "http://localhost:8000"

    tools = await mcp_request(url, "tools/list")
    print(f"Tools: {tools}")

    result = await mcp_request(url, "tools/call", {"name": "add", "arguments": {"a": 5, "b": 3}})
    print(f"Result: {result}")

asyncio.run(main())
```

## Use as an MCP gateway

The LangSmith Tool Server can act as an MCP gateway, aggregating tools from multiple MCP servers into a single endpoint. Configure MCP servers in your `toolkit.toml`:

```toml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
[toolkit]
name = "my-toolkit"
tools = "./my_toolkit/__init__.py:TOOLS"

[[mcp_servers]]
name = "weather"
transport = "streamable_http"
url = "http://localhost:8001/mcp/"

[[mcp_servers]]
name = "math"
transport = "stdio"
command = "python"
args = ["-m", "mcp_server_math"]
```

All tools from connected MCP servers are exposed through your server's `/mcp` endpoint. MCP tools are prefixed with their server name to avoid conflicts (e.g., `weather_get_forecast`, `math_add`).

## Authenticate

### OAuth for third-party APIs

For tools that need to access third-party APIs (like Google, GitHub, Slack, etc.), you can use OAuth authentication with [Agent Auth](/langsmith/agent-auth).

Before using OAuth in your tools, you'll need to configure an OAuth provider in your LangSmith workspace settings. See the [Agent Auth documentation](/langsmith/agent-auth) for setup instructions.

Once configured, specify the `auth_provider` in your tool decorator:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langsmith_tool_server import tool, Context
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

@tool(
    auth_provider="google",
    scopes=["https://www.googleapis.com/auth/gmail.readonly"],
    integration="gmail"
)
async def read_emails(context: Context, max_results: int = 10) -> str:
    """Read recent emails from Gmail."""
    credentials = Credentials(token=context.token)
    service = build('gmail', 'v1', credentials=credentials)
    # ... Gmail API calls
    return f"Retrieved {max_results} emails"
```

Tools with `auth_provider` must:

* Have `context: Context` as the first parameter
* Specify at least one scope
* Use `context.token` to make authenticated API calls

### Custom request authentication

Custom authentication allows you to validate requests and integrate with your identity provider. Define an authentication handler in your `auth.py` file:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langsmith_tool_server import Auth

auth = Auth()

@auth.authenticate
async def authenticate(authorization: str = None) -> dict:
    """Validate requests and return user identity."""
    if not authorization or not authorization.startswith("Bearer "):
        raise auth.exceptions.HTTPException(
            status_code=401,
            detail="Unauthorized"
        )

    token = authorization.replace("Bearer ", "")
    # Validate token with your identity provider
    user = await verify_token_with_idp(token)

    return {"identity": user.id}
```

The handler runs on every request and must return a dict with `identity` (and optionally `permissions`).

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/fleet/mcp-framework.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Quickstart
Source: https://docs.langchain.com/langsmith/fleet/quickstart

Build an agent from a template

In this quickstart, you'll use the pre-defined **Email Assistant** [template](/langsmith/fleet/templates) that organizes and manages your inbox for you.

* Select a different template.

<Callout icon="message">
  You'll interact with your agent through chat, just like texting a helpful assistant.
</Callout>

## Before you start

You'll need:

* A LangSmith account ([sign up here](https://smith.langchain.com/agents?skipOnboarding=true\&utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-fleet-quickstart)).
* A Gmail account.
* A Google calendar.
* An OpenAI or Anthropic API key (Step 1 will show you how to get one).

## 1. Get your model API key

Your agent needs an API key to connect to an AI model. The AI model is what allows your agent to understand and respond to your requests.

<Tabs>
  <Tab title="OpenAI (ChatGPT)">
    1. Go to [platform.openai.com/api-keys](https://platform.openai.com/api-keys).
    2. Click **Create new secret key**.
    3. Give it a name like "Fleet".
    4. Copy the key (it starts with `sk-`).
    5. Save it somewhere safe, you'll need it in Step 2.
  </Tab>

  <Tab title="Anthropic (Claude)">
    1. Go to [console.anthropic.com/settings/keys](https://console.anthropic.com/settings/keys).
    2. Click **Create Key**.
    3. Give it a name like "Fleet".
    4. Copy the key (it starts with `sk-ant-`).
    5. Save it somewhere safe, you'll need it in Step 2.
  </Tab>
</Tabs>

<Warning>
  Both services charge based on usage.
</Warning>

## 2. Add your API key to LangSmith

Now you'll add your API key to LangSmith so your agents can use it:

<Steps>
  <Step title="Open Settings">
    1. Go to [smith.langchain.com](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-fleet-quickstart).
    2. Click the <Icon icon="settings" /> **Settings** icon in the bottom left.
  </Step>

  <Step title="Go to Secrets">
    Click the **Secrets** tab at the top.
  </Step>

  <Step title="Add your key">
    1. Click **Add secret**.
    2. For **Key**, enter:
       * `OPENAI_API_KEY` (if using OpenAI)
       * `ANTHROPIC_API_KEY` (if using Anthropic)
    3. For **Value**, paste the API key you copied in Step 1.
    4. Click **Save secret**.
  </Step>
</Steps>

<Callout type="success" icon="check">
  Your agent now has access to an AI model to understand and respond to your requests. Next, you'll create your agent.
</Callout>

## 3. Create your agent

<Steps>
  <Step title="Navigate to Fleet">
    1. In the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-fleet-quickstart), click <Icon icon="pointer" /> **Switch to Fleet** at the top of the left-hand navigation.
  </Step>

  <Step title="Choose a template">
    1. Select **Templates** in the left-hand navigation.
    2. Select **Email Assistant** template.
    3. Click **Use this template**.

    <Tip>
      If you don't want to start with a template, you have two other options. From the **+ New Agent** page:

      * **Chat**: Use the chat interface to describe your agent, and it will help you create it step-by-step.
      * **Manually**: Select **Create manually instead** to build your agent without any pre-filled responses on the configuration page.
    </Tip>
  </Step>

  <Step title="Authorize accounts">
    Your agent will ask you to connect your Google accounts:

    1. Click **Connect**.
    2. Sign in with your Google account.
    3. Review permissions and click **Allow**.
    4. You'll be redirected back to LangSmith where your agent will be created.
  </Step>
</Steps>

<Info>
  Your agent only accesses your accounts when working on tasks you give it. You can revoke access anytime in your Google account settings.
</Info>

## 4. View the agent template

<Steps>
  <Step title="View and customize the template">
    At this point, you can review the template instructions for the email assistant. If needed, you can make adjustments to the instructions.

    If you made any changes, click **Save changes**.
  </Step>

  <Step title="Start a test chat">
    1. In the right-hand panel of the configuration page, select the **Test Chat** tab.
    2. Try out the email assistant in the chat interface, for example:

       > *Apply a "Review" label to emails that I receive, which require some kind of review from me*
  </Step>

  <Step title="Agent starts working">
    Your agent will start work and provide a **Continue** option for each step that requires your approval.

    <img alt="Test chat output view with response including approvals for Gmail tool." />

    <img alt="Test chat output view with response including approvals for Gmail tool." />

    3. As you test out the agent, you can make edits to the instructions, or add tools that you may need. Click **Save changes** when you're happy with the results.
  </Step>
</Steps>

## Edit your agent

You may want to update your agent's instructions or include more tools. You can directly chat with your agent to ask for updates, or you can:

1. From **My Agents** in the left-hand navigation, select the agent you want to edit.
2. Select <Icon icon="pencil" /> **Edit Agent**.

From the agent's edit page, you can:

* Add tools with **+ Add tool** to connect more apps and services like Slack, GitHub, or Linear.
* Add further helpers with **+ Add sub-agent** to break complex tasks into specialized sub-tasks.
* Request pauses for reviews on existing tools.
* Modify existing tools.
* Explore channels that can start your agent automatically.

## Next steps

Now that you've created your first agent, here's what to explore:

<CardGroup>
  <Card title="Try more templates" icon="layout-grid" href="/langsmith/fleet/templates">
    Explore prebuilt agents for common tasks
  </Card>

  <Card title="Add automation" icon="bolt" href="/langsmith/fleet/essentials#channels">
    Run your agent automatically with channels (Slack, email, schedules)
  </Card>

  <Card title="Connect more tools" icon="puzzle" href="/langsmith/fleet/tools">
    Add Slack, GitHub, Linear, and more
  </Card>

  <Card title="Build complex agents" icon="sitemap" href="/langsmith/fleet/essentials#sub-agents">
    Use sub-agents to break down big tasks
  </Card>
</CardGroup>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/fleet/quickstart.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Remote MCP servers
Source: https://docs.langchain.com/langsmith/fleet/remote-mcp-servers

Connect Fleet to popular remote MCP servers

You can connect LangSmith Fleet to remote MCP servers to extend your agents with additional tools and integrations. This page covers how to add custom MCP servers and provides configuration details for popular remote servers.

An [MCP (Model Context Protocol) server](https://modelcontextprotocol.io/docs/getting-started/intro) exposes tools that an agent can call at runtime.

A remote MCP server:

* Runs outside of LangSmith (usually over HTTPS).
* Owns its own authentication and authorization.
* Acts as a bridge between your agent and an external system.

LangSmith Fleet doesn't execute these tools itself, it forwards requests to the MCP server and returns the results to the agent.

### How it works

* Fleet discovers tools from remote MCP servers via the standard MCP protocol.
* Headers configured in your workspace are automatically attached when fetching tools or calling them. Headers are key-value pairs sent with every HTTP request to your MCP server. They're commonly used for authentication (like API keys or bearer tokens), but can also provide configuration information, content types, or custom metadata.
* Tools from remote servers are available alongside built-in tools in Fleet.

**Runtime**: Fleet automatically connects to your MCP server and uses its tools.

```mermaid theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
sequenceDiagram
    participant Agent as Fleet
    participant MCP as Remote MCP Server

    Agent->>MCP: Discover available tools<br/>(with configured headers)
    MCP-->>Agent: Return tool list

    Note over Agent,MCP: Later, when agent needs a tool...

    Agent->>MCP: Call tool<br/>(with configured headers)
    MCP-->>Agent: Return result
```

## Add a remote MCP server

You can add MCP servers directly from your agent or from workspace settings.

<Note>
  Adding MCP servers requires the **MCP Server Create** permission. Workspace admins can grant this permission to users from workspace settings.
</Note>

### Add to a specific agent

To add a remote MCP server to a specific agent:

<Steps>
  <Step title="Open the agent editor">
    Open your agent in the [Fleet](https://smith.langchain.com/agents?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-fleet-remote-mcp-servers) inbox. Next to the agent name, click the <Icon icon="pencil" /> **Edit Agent** icon.
  </Step>

  <Step title="Add the MCP server">
    In the **Toolbox** section, click **MCP**. Enter the server name and URL, then configure authentication (see [authentication types](#authentication-types)).
  </Step>

  <Step title="Save your agent">
    Click **Save changes**. Fleet will discover available tools from your MCP server and make them available in this agent.
  </Step>
</Steps>

### Add to all agents in the workspace

To add a remote MCP server to all agents in the workspace:

<Tabs>
  <Tab title="From Fleet > Integrations">
    <Steps>
      <Step title="Navigate to Fleet > Integrations">
        In the LangSmith UI, navigate to the [**Fleet** > **Integrations**](https://smith.langchain.com/agents/tools) tab.
      </Step>

      <Step title="Add the server">
        1. Click **+ Custom MCP** at the bottom of the left sidebar.
        2. Add a **Name** for the MCP server.
        3. Add the MCP **URL** (e.g., `https://api.example.com/mcp`)
        4. Select the **Authentication** type. See [Authentication types](#authentication-types) for more details.
      </Step>

      <Step title="Save the server">
        Click **Save server**. Fleet will automatically discover available tools from your MCP server and make them available in your agents. The configured headers are applied to both tool discovery requests and tool execution requests.
      </Step>
    </Steps>
  </Tab>

  <Tab title="From workspace settings">
    <Steps>
      <Step title="Navigate to MCP server settings">
        In the LangSmith UI, navigate to the [Settings > MCP servers](https://smith.langchain.com/settings/workspaces/mcp-servers) tab.
      </Step>

      <Step title="Add the server">
        Click **Add server** and enter the server name and URL, then configure authentication (see [authentication types](#authentication-types)).
      </Step>

      <Step title="Save the server">
        Click **Save server**. Fleet will automatically discover available tools from your MCP server and make them available in your agents. The configured headers are applied to both tool discovery requests and tool execution requests.
      </Step>
    </Steps>
  </Tab>
</Tabs>

### Authentication types

Select an authentication type based on the server's requirements:

* **Headers**: Add key-value pairs sent with every request. The most common pattern is using an Authorization bearer token:

  * **Key**: `Authorization`
  * **Value**: `Bearer API_KEY`

  <Info>
    You can add multiple headers if your MCP server requires additional authentication or configuration parameters. Each header key-value pair is sent with every request to the server.
  </Info>

* **OAuth 2.1 (Auto)**: Select this for servers that support OAuth via dynamic client registration. You'll be prompted to log in with your account for that service.

* **OAuth 2.1 (Manual)**: Select this for servers that support OAuth, but require specifying the client ID/secret beforehand. OAuth providers used in this flow must have **PKCE** enabled.

## Update your MCP server URL

<Warning>
  Changing the URL of a custom MCP server will break any agents that use tools from that server.
</Warning>

Fleet stores tool references by MCP server URL. If you update the URL of a custom MCP server, existing agents will fail when attempting to call those tools because the stored URL no longer matches.

To update an MCP server URL:

1. Update your MCP server URL in the workspace settings.
2. For each agent using tools from that server:
   * Remove the affected tools from the agent configuration.
   * Re-add the tools (they will now reference the new URL).
3. Test the agent to confirm tools work correctly.

## Supported servers

To view all available MCP servers and configuration details, navigate to the [Fleet > Integrations tab](https://smith.langchain.com/agents/tools).

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/fleet/remote-mcp-servers.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Salesforce integration
Source: https://docs.langchain.com/langsmith/fleet/salesforce

Connect LangSmith Fleet to Salesforce so your agents can query records, navigate schemas, and read custom fields.

The Salesforce integration gives your agents read-only access to data in your Salesforce org. Once connected, an agent can:

* Query records across standard and custom objects.
* Navigate your Salesforce data schema, including relationships and custom fields.
* Pull live context from Salesforce into any thread or scheduled run.

<Note>
  Connecting Salesforce is a one-time setup per Salesforce org. A Salesforce System Administrator (or a user with the **Approve Uninstalled Connected Apps** permission) must install the connector before other users can authenticate.
</Note>

## Prerequisites

* A LangSmith workspace with access to [Fleet](https://smith.langchain.com/agents?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-fleet-salesforce).
* A Salesforce org and user account.
* A Salesforce System Administrator to complete the install (or the **Approve Uninstalled Connected Apps** permission on your own user).

## Register the connector

The first connection attempt registers the **LangChain Fleet Connector** in your Salesforce org so that an administrator can install it. This initial attempt is expected to fail with an authentication error.

<Steps>
  <Step title="Open the Integrations page">
    In the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-fleet-salesforce), navigate to the [**Fleet** > **Integrations**](https://smith.langchain.com/agents/tools) tab.
  </Step>

  <Step title="Start the Salesforce connection">
    Find the **Salesforce** tool and click **Connect**.
  </Step>

  <Step title="Sign in to Salesforce">
    Sign in with your Salesforce credentials. If your org requires a custom domain or SSO, click **Use Custom Domain** and enter your org's My Domain before signing in. Then click **Allow** to authorize the connection.
  </Step>
</Steps>

<Info>
  The first attempt fails by design. The failed request registers the **LangChain Fleet Connector** in your Salesforce org so an administrator can install it in the next step.
</Info>

<Tip>
  If you are not a Salesforce administrator, stop here and send your admin the link to this page. They need to follow the **Install the connector** and **Grant user access** steps below before you can complete the connection.
</Tip>

## Install the connector

<Note>
  This step must be completed by a Salesforce System Administrator.
</Note>

<Steps>
  <Step title="Open Salesforce Setup">
    In Salesforce, click the <Icon icon="settings" /> gear icon and select **Setup**.
  </Step>

  <Step title="Open Connected Apps OAuth Usage">
    In the **Quick Find** box, type `Connected Apps OAuth Usage` and open the page.
  </Step>

  <Step title="Install the connector">
    1. Find **LangChain Fleet Connector** in the list.
    2. Click **Install**.
    3. Confirm the installation on the next page.
  </Step>
</Steps>

## Grant user access

Granting access through a permission set is the recommended way to control which users can authenticate with Fleet.

<Note>
  This step must be completed by a Salesforce System Administrator.
</Note>

<Steps>
  <Step title="Open the app policies">
    From **Connected Apps OAuth Usage**, click **Manage App Policies** next to **LangChain Fleet Connector**.
  </Step>

  <Step title="Pre-authorize admin-approved users">
    Under **OAuth Policies** > **Permitted Users**, select **Admin approved users are pre-authorized**, then click **Save**.
  </Step>

  <Step title="Assign a permission set">
    Use **Manage Permission Sets** to grant access to the users who need to connect the Salesforce tool in Fleet.
  </Step>
</Steps>

## Connect from Fleet

Once your administrator has installed the connector and granted access, return to Fleet to complete the connection.

1. In the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-fleet-salesforce), navigate to the [**Fleet** > **Integrations**](https://smith.langchain.com/agents/tools) tab.
2. Find the **Salesforce** tool and click **Connect**.
3. Sign in with your Salesforce credentials and click **Allow**.

The connection now succeeds and Salesforce tools become available to agents in your workspace.

## Use Salesforce with an agent

After connecting, add Salesforce tools to a specific agent:

1. Open your agent in [Fleet](https://smith.langchain.com/agents?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-fleet-salesforce) and click the <Icon icon="pencil" /> **Edit Agent** icon.
2. In the **Toolbox** section, click **+ Add**.
3. Search for **Salesforce Query** and add it to the agent.
4. Click **Save changes**.

## Troubleshooting

### Connection fails with an authentication error

The first connection attempt is expected to fail. It registers the **LangChain Fleet Connector** in your Salesforce org so an administrator can install it. If the connection still fails after the connector is installed, confirm that:

* The administrator completed both **Install the connector** and **Grant user access**.
* Your Salesforce user is assigned to a permission set that grants access to the connector.
* You signed in through **Use Custom Domain** with the correct Salesforce domain.

### Agent cannot see an object or field

Salesforce tools run with the permissions of the connected user. If an agent cannot read an object or custom field, verify that the user's Salesforce profile and permission sets grant read access to that object.

## Next steps

<CardGroup>
  <Card title="Add more tools" icon="puzzle" href="/langsmith/fleet/tools">
    Connect additional services to your agent
  </Card>

  <Card title="Agent identity" icon="user" href="/langsmith/fleet/agent-identity">
    Choose whether the agent uses shared or per-user credentials
  </Card>

  <Card title="Human-in-the-loop" icon="check" href="/langsmith/fleet/essentials#human-in-the-loop">
    Require approval before the agent takes sensitive actions
  </Card>
</CardGroup>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/fleet/salesforce.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Schedules
Source: https://docs.langchain.com/langsmith/fleet/schedules

Configure schedules to run your Fleet agents on a recurring basis.

Schedules run your agent on a recurring time-based schedule. Use schedules when your agent needs to do work proactively, not just in response to a message or event.

Common use cases include:

* **Daily briefings**: Summarize emails, calendar events, or Slack activity each morning.
* **Memory synthesis**: Periodically review and consolidate the agent's memory files to keep context clean and relevant.
* **Proactive outreach**: Draft weekly status updates, follow-up reminders, or recurring reports.
* **Data monitoring**: Check dashboards, metrics, or feeds on a set cadence and surface anything noteworthy.

<Tip>
  To start an agent based on an event (such as a Slack message or email), use [channels](/langsmith/fleet/channels) instead.
</Tip>

## Add a schedule

To add a schedule:

1. In the **Schedules** section, click **+ Add**.

2. Select when the schedule should run.

   <Note>
     Schedules are in UTC. Convert your desired execution time to UTC when configuring the schedule.
   </Note>

3. (Optional) Add a **Prompt**. With a custom prompt, you can tell the agent what to do on each scheduled run. For example:

   * "Summarize my unread emails from the last 24 hours and post a digest to #team-updates in Slack."
   * "Review your memory files and consolidate any redundant or outdated entries."

4. Click **Create schedule**.

5. Click **Save changes**.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/fleet/schedules.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Self-hosted
Source: https://docs.langchain.com/langsmith/fleet/self-hosted-link

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/fleet/self-hosted-link.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Skills
Source: https://docs.langchain.com/langsmith/fleet/skills

Use skills to give your agents access to specific capabilities.

Skills are reusable capabilities that provide specialized workflows and domain knowledge to your agent. Each skill is stored in the agent's long-term memory at `memories/skills/<skill-name>`. The skill's name and description is loaded when the agent starts. Based on this info the agent can decide to use the skill. The full skill file is only loaded when the agent determines it is relevant to the current task. Any referenced additional resources may be loaded by the agent if they become relevant.

Using skills can help:

* Save on token usage by only providing context relevant to the current task.
* Prevent the agent from having too much context in the system prompt, which can lead to hallucinations and incorrect responses.

<Info>
  Fleet skills are built on [Deep Agents](/oss/python/deepagents/skills) and follow the [Agent Skills specification](https://agentskills.io/specification). For details on skill structure, the `SKILL.md` format, and authoring best practices, see the [Deep Agents skills documentation](/oss/python/deepagents/skills).
</Info>

## Private vs. shared skills

Skills can be **private** to a single agent or **shared** across a workspace:

* **Private skills**: Private to the agent they belong to and are stored in the agent's long-term memory.
* **Shared skills**: Shared with the workspace and listed on the [**Skills**](https://smith.langchain.com/agents/skills) page.
  * Visible to all agents in the workspace.
  * Only the user who created the skill can edit or delete it.
  * Can be added to any agent in the workspace and stay in sync as skill is updated.
  * Accessed automatically by the general-purpose chat.

## Write effective skill descriptions

Write the description as instructions for when to use the skill, not as a label for what it does. The agent routes tasks based on the description alone. It reads the full skill file only after deciding to use it.

For example, instead of "Helps with email," write: "Use when drafting, replying to, or summarizing emails. Covers tone adjustments, follow-up scheduling, and inbox triage."

A description that is too broad means the agent may not use the skill even when it would handle the task correctly. A description that overlaps with another skill means the agent may route to the wrong one or fail to choose. As your skill library grows, review descriptions for overlap and narrow any that are ambiguous.

## Create a skill

You can create a skill two ways:

* **With AI**: Use natural language to describe the skill and the agent will create it for you. You can also add additional resources. Any additional files must be referenced in `SKILL.md` for the agent to be aware of them.
* **Manually**: Create a skill with a `SKILL.md` file.

<Note>
  By default, skills are **private** to the agent they belong to and are stored in the agent's long-term memory. You can [share a skill with the workspace](#share-a-skill).
</Note>

<Tabs>
  <Tab title="With AI">
    In [Fleet](https://smith.langchain.com/agents?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-fleet-skills), select an agent and prompt it to create a skill:

    <Prompt description="Create a skill that helps the agent use the web to research a topic.">
      Create a skill that helps the agent use the web to research a topic. Use when asked to research a topic, person, company, technology, event, or any question that requires gathering and synthesizing information from the web. Covers news lookups, competitive analysis, background research, and fact-finding tasks. Prefer `tavily_web_search` for most queries.
    </Prompt>

    You can also turn a previous conversation into a reusable skill at any time. After completing a task, ask the agent to capture the workflow:

    <Prompt description="Turn this conversation into a reusable skill.">
      Turn what we just did into a skill so you can repeat it in the future.
    </Prompt>
  </Tab>

  <Tab title="From a template">
    1. Navigate to [**Fleet > Skills**](https://smith.langchain.com/agents/skills).
    2. Browse available templates and select one to add to your agent.
  </Tab>

  <Tab title="Manually">
    1. Select an agent in [Fleet](https://smith.langchain.com/agents?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-fleet-skills).
    2. Click <Icon icon="pencil" /> **Edit Agent**.
    3. In the **Skills** section, click **Create**.
    4. Enter the skill name, description, and instructions.
    5. Click **Save Changes**.
  </Tab>
</Tabs>

<Tip>
  When you create a new agent, Fleet automatically generates relevant skills if the agent would benefit from them. These skills are private by default. You can [share them to your workspace](#share-a-skill) from the agent editor.
</Tip>

## Fix recurring mistakes

The default response to an agent mistake is to correct it in the moment. A skill changes this: it gives the agent explicit rules to follow every time it encounters that class of task, so the same mistake cannot happen again.

When an agent handles a task incorrectly, correct it, then ask it to capture the fix:

<Prompt description="Capture this fix as a skill.">
  Turn this correction into a skill so you always handle it this way.
</Prompt>

The agent creates a `SKILL.md` encoding the correct behavior. On future sessions, it reads the skill before handling that task rather than reasoning from scratch.

## Edit a private skill

1. Select an agent in [Fleet](https://smith.langchain.com/agents?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-fleet-skills).
2. Click <Icon icon="pencil" /> **Edit Agent**.
3. In the **Skills** section, select the skill to edit.
4. Update the skill name, description, or instructions.
5. Click **Save Changes**.

## Edit a shared skill

<Note>
  Only the user who created the shared skill can edit it.
</Note>

1. Navigate to [**Fleet > Skills**](https://smith.langchain.com/agents/skills).
2. Select the skill to edit.
3. Update the skill name, description, or instructions.
4. Click **Save Changes**.

## Share a skill

1. Select an agent in [Fleet](https://smith.langchain.com/agents?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-fleet-skills).
2. Click <Icon icon="pencil" /> **Edit Agent**.
3. In the **Skills** section of the graph view, select the skill to share.
4. Click <Icon icon="share" />**Share**.

Once shared, the skill appears on the [**Skills**](https://smith.langchain.com/agents/skills) page. You can add shared skills to any agent in the workspace from the agent editor, and the general-purpose chat picks them up automatically.

<Note>
  Only the creator of a shared skill can edit or delete it.
</Note>

## Delete a private skill

Deleting a private skill removes it permanently, since it is stored in that agent's memory.

1. Select the agent in [Fleet](https://smith.langchain.com/agents?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-fleet-skills).
2. Click <Icon icon="pencil" /> **Edit Agent**.
3. In the **Skills** section, click the <Icon icon="trash" /> icon for the skill to delete.

## Delete a shared skill

Only the user who created the shared skill can delete it.

<Warning>
  Deleting a skill removes it from the workspace and from all agents that use it. This action cannot be undone.
</Warning>

1. Navigate to [**Fleet > Skills**](https://smith.langchain.com/agents/skills).
2. Select the skill to delete.
3. Click the <Icon icon="trash" /> **Delete skill** icon.

## Use Fleet skills in local development

Download skills from your Fleet workspace with the LangSmith CLI and install them locally for use in coding agents like Claude Code, Cursor, or Codex.

By default, files are saved to `~/.agents/skills/[skill-name]/` and symlinked into `~/.claude/skills/[skill-name]/`.

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
langsmith fleet skills pull [skill-name] [flags]
```

| Flag              | Description                                                                                     |
| ----------------- | ----------------------------------------------------------------------------------------------- |
| `--global=false`  | Install to project-level directories (`.agents/` and `.claude/`) instead of the home directory. |
| `--agent`         | Target a specific agent (`claude`, `cursor`, `codex`).                                          |
| `--copy`          | Copy files instead of symlinking.                                                               |
| `--format pretty` | Display the installed skill's file tree.                                                        |

For example:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
$ langsmith fleet skills pull web-research --format pretty
Installed skill "web-research" to ~/.agents/skills/web-research
  Linked: ~/.claude/skills/web-research

web-research/
├── SKILL.md
└── references/
    └── search-tips.md
```

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/fleet/skills.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
