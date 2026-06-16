# MCP endpoint in Agent Server
Source: https://docs.langchain.com/langsmith/server-mcp

The Model Context Protocol (MCP) is an open protocol for describing tools and data sources in a model-agnostic format, enabling LLMs to discover and use them via a structured API.

[Agent Server](/langsmith/agent-server) implements MCP using the [Streamable HTTP transport](https://spec.modelcontextprotocol.io/specification/2025-03-26/basic/transports/#streamable-http). This allows LangGraph **agents** to be exposed as **MCP tools**, making them usable with any MCP-compliant client supporting Streamable HTTP.

The MCP endpoint is available at `/mcp` on [Agent Server](/langsmith/agent-server).

You can set up [custom authentication middleware](/langsmith/custom-auth) to authenticate a user with an MCP server to get access to user-scoped tools within your LangSmith deployment.

An example architecture for this flow:

```mermaid theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
sequenceDiagram
  %% Actors
  participant ClientApp as Client
  participant AuthProv  as Auth Provider
  participant LangGraph as Agent Server
  participant SecretStore as Secret Store
  participant MCPServer as MCP Server

  %% Platform login / AuthN
  ClientApp  ->> AuthProv: 1. Login (username / password)
  AuthProv   -->> ClientApp: 2. Return token
  ClientApp  ->> LangGraph: 3. Request with token

  Note over LangGraph: 4. Validate token (@auth.authenticate)
  LangGraph  -->> AuthProv: 5. Fetch user info
  AuthProv   -->> LangGraph: 6. Confirm validity

  %% Fetch user tokens from secret store
  LangGraph  ->> SecretStore: 6a. Fetch user tokens
  SecretStore -->> LangGraph: 6b. Return tokens

  Note over LangGraph: 7. Apply access control (@auth.on.*)

  %% MCP round-trip
  Note over LangGraph: 8. Build MCP client with user token
  LangGraph  ->> MCPServer: 9. Call MCP tool (with header)
  Note over MCPServer: 10. MCP validates header and runs tool
  MCPServer  -->> LangGraph: 11. Tool response

  %% Return to caller
  LangGraph  -->> ClientApp: 12. Return resources / tool output
```

## Requirements

To use MCP, ensure you have the following dependencies installed:

* `langgraph-api >= 0.2.3`
* `langgraph-sdk >= 0.1.61`

Install them with:

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install "langgraph-api>=0.2.3" "langgraph-sdk>=0.1.61"
  ```

  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv add "langgraph-api>=0.2.3" "langgraph-sdk>=0.1.61"
  ```
</CodeGroup>

## Usage overview

To enable MCP:

* Upgrade to use langgraph-api>=0.2.3. If you are deploying LangSmith, this will be done for you automatically if you create a new revision.
* MCP tools (agents) will be automatically exposed.
* Connect with any MCP-compliant client that supports Streamable HTTP.

### Client

Use an MCP-compliant client to connect to the Agent Server. The following examples show how to connect using different programming languages.

<Tabs>
  <Tab title="JavaScript/TypeScript">
    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    npm install @modelcontextprotocol/sdk
    ```

    > **Note**
    > Replace `serverUrl` with your Agent Server URL and configure authentication headers as needed.

    ```js theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { Client } from "@modelcontextprotocol/sdk/client/index.js";
    import { StreamableHTTPClientTransport } from "@modelcontextprotocol/sdk/client/streamableHttp.js";

    // Connects to the LangGraph MCP endpoint
    async function connectClient(url) {
        const baseUrl = new URL(url);
        const client = new Client({
            name: 'streamable-http-client',
            version: '1.0.0'
        });

        const transport = new StreamableHTTPClientTransport(baseUrl);
        await client.connect(transport);

        console.log("Connected using Streamable HTTP transport");
        console.log(JSON.stringify(await client.listTools(), null, 2));
        return client;
    }

    const serverUrl = "http://localhost:2024/mcp";

    connectClient(serverUrl)
        .then(() => {
            console.log("Client connected successfully");
        })
        .catch(error => {
            console.error("Failed to connect client:", error);
        });
    ```
  </Tab>

  <Tab title="Python">
    Install the adapter with:

    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    pip install langchain-mcp-adapters
    ```

    Here is an example of how to connect to a remote MCP endpoint and use an agent as a tool:

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    # Create server parameters for stdio connection
    from mcp import ClientSession
    from mcp.client.streamable_http import streamablehttp_client
    import asyncio

    from langchain_mcp_adapters.tools import load_mcp_tools
    from langchain.agents import create_agent

    server_params = {
        "url": "https://mcp-finance-agent.xxx.us.langgraph.app/mcp",
        "headers": {
            "X-Api-Key":"lsv2_pt_your_api_key"
        }
    }

    async def main():
        async with streamablehttp_client(**server_params) as (read, write, _):
            async with ClientSession(read, write) as session:
                # Initialize the connection
                await session.initialize()

                # Load the remote graph as if it was a tool
                tools = await load_mcp_tools(session)

                # Create and run a react agent with the tools
                agent = create_agent("gpt-5.5", tools)

                # Invoke the agent with a message
                agent_response = await agent.ainvoke({"messages": "What can the finance agent do for me?"})
                print(agent_response)

    if __name__ == "__main__":
        asyncio.run(main())
    ```
  </Tab>
</Tabs>

## Expose an agent as MCP tool

When deployed, your agent will appear as a tool in the MCP endpoint
with this configuration:

* **Tool name**: The agent's name.
* **Tool description**: The agent's description.
* **Tool input schema**: The agent's input schema.

### Setting name and description

You can set the name and description of your agent in `langgraph.json`:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
    "graphs": {
        "my_agent": {
            "path": "./my_agent/agent.py:graph",
            "description": "A description of what the agent does"
        }
    },
    "env": ".env"
}
```

After deployment, you can update the name and description using the LangGraph SDK.

### Schema

Define clear, minimal input and output schemas to avoid exposing unnecessary internal complexity to the LLM.

The default [MessagesState](/oss/python/langgraph/graph-api#messagesstate) uses `AnyMessage`, which supports many message types but is too general for direct LLM exposure.

Instead, define **custom agents or workflows** that use explicitly typed input and output structures.

For example, a workflow answering documentation questions might look like this:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langgraph.graph import StateGraph, START, END
from typing_extensions import TypedDict

# Define input schema
class InputState(TypedDict):
    question: str

# Define output schema
class OutputState(TypedDict):
    answer: str

# Combine input and output
class OverallState(InputState, OutputState):
    pass

# Define the processing node
def answer_node(state: InputState):
    # Replace with actual logic and do something useful
    return {"answer": "bye", "question": state["question"]}

# Build the graph with explicit schemas
builder = StateGraph(OverallState, input_schema=InputState, output_schema=OutputState)
builder.add_node(answer_node)
builder.add_edge(START, "answer_node")
builder.add_edge("answer_node", END)
graph = builder.compile()

# Run the graph
print(graph.invoke({"question": "hi"}))
```

For more details, see the [low-level concepts guide](/oss/python/langgraph/graph-api#state).

## Use user-scoped MCP tools in your deployment

<Tip>
  **Prerequisites**
  You have added your own [custom auth middleware](/langsmith/custom-auth) that populates the `langgraph_auth_user` object, making it accessible through configurable context for every node in your graph.
</Tip>

To make user-scoped tools available to your LangSmith deployment, start with implementing a snippet like the following:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_mcp_adapters.client import MultiServerMCPClient

def mcp_tools_node(state, config):
    user = config["configurable"].get("langgraph_auth_user")
         , user["github_token"], user["email"], etc.

    client = MultiServerMCPClient({
        "github": {
            "transport": "streamable_http", # (1)
            "url": "https://my-github-mcp-server/mcp", # (2)
            "headers": {
                "Authorization": f"Bearer {user['github_token']}"
            }
        }
    })
    tools = await client.get_tools() # (3)

    # Your tool-calling logic here

    tool_messages = ...
    return {"messages": tool_messages}
```

1. MCP only supports adding headers to requests made to `streamable_http` and `sse` `transport` servers.
2. Your MCP server URL.
3. Get available tools from your MCP server.

*This can also be done by [rebuilding your graph at runtime](/langsmith/graph-rebuild) to have a different configuration for a new run*

## Session behavior

The current LangGraph MCP implementation does not support sessions. Each `/mcp` request is stateless and independent.

## Authentication

The `/mcp` endpoint uses the same authentication as the rest of the LangGraph API. Refer to the [authentication guide](/langsmith/auth) for setup details.

## Disable MCP

To disable the MCP endpoint, set `disable_mcp` to `true` in your `langgraph.json` configuration file:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "$schema": "https://langgra.ph/schema.json",
  "http": {
    "disable_mcp": true
  }
}
```

This will prevent the server from exposing the `/mcp` endpoint.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/server-mcp.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Trace JS functions in serverless environments
Source: https://docs.langchain.com/langsmith/serverless-environments

<Note>
  This section is relevant for those using the LangSmith JS SDK version 0.2.0 and higher. If you are tracing using LangChain.js or LangGraph.js in serverless environments, see [this guide](https://js.langchain.com/docs/how_to/callbacks_serverless).
</Note>

When tracing JavaScript functions, LangSmith will trace runs in the background by default to avoid adding latency. In serverless environments where the execution context may be terminated abruptly, it's important to ensure that all tracing data is properly flushed before the function completes.

To make sure this occurs, you can either:

* Set an environment variable named `LANGSMITH_TRACING_BACKGROUND` to `"false"`. This will cause your traced functions to wait for tracing to complete before returning.
  * Note that this is named differently from the [environment variable](https://js.langchain.com/docs/how_to/callbacks_serverless) in LangChain.js because LangSmith can be used without LangChain.
* Pass a custom client into your traced runs and `await` the `client.awaitPendingTraceBatches();` method.

Here's an example of using `awaitPendingTraceBatches` alongside the [`traceable`](/langsmith/annotate-code) method:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { Client } from "langsmith";
import { traceable } from "langsmith/traceable";
const langsmithClient = new Client({});
const tracedFn = traceable(
  async () => {
    return "Some return value";
  },
  {
    client: langsmithClient,
  }
);
const res = await tracedFn();
await langsmithClient.awaitPendingTraceBatches();
```

## Rate limits at high concurrency[ ](#rate-limits-at-high-concurrency "Direct link to rate limits at high concurrency")

By default, the LangSmith client will batch operations as your traced run executions, sending a new batch every few milliseconds.

This works well in most situations, but if your traced function is long-running and you have very high concurrency, you may also hit rate limits related to overall request count.

If you are seeing rate limit errors related to this, you can try setting `manualFlushMode: true` in your client like this:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { Client } from "langsmith";
const langsmithClient = new Client({  manualFlushMode: true,});
const myTracedFunc = traceable(
  async () => {
    // Your logic here...
  },
  { client: langsmithClient }
);
```

And then manually calling `client.flush()` like this before your serverless function closes:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
try {
  await myTracedFunc();
} finally {
  await langsmithClient.flush();
}
```

Note that this will prevent runs from appearing in the LangSmith UI until you call `.flush()`.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/serverless-environments.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Set up custom authentication
Source: https://docs.langchain.com/langsmith/set-up-custom-auth

In this tutorial, we will build a chatbot that only lets specific users access it. We'll start with the LangGraph template and add token-based security step by step. By the end, you'll have a working chatbot that checks for valid tokens before allowing access.

This is part 1 of our authentication series:

1. Set up custom authentication (you are here) - Control who can access your bot
2. [Make conversations private](/langsmith/resource-auth) - Let users have private conversations
3. [Connect an authentication provider](/langsmith/add-auth-server) - Add real user accounts and validate using OAuth2 for production

This guide assumes basic familiarity with the following concepts:

* [**Authentication & Access Control**](/langsmith/auth)
* [**LangSmith**](/langsmith/observability)

<Note>
  Custom auth is only available for LangSmith SaaS deployments or Enterprise Self-Hosted deployments.
</Note>

## 1. Create your app

Create a new chatbot using the LangGraph starter template:

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install -U "langgraph-cli[inmem]"
  langgraph new --template=new-langgraph-project-python custom-auth
  cd custom-auth
  ```

  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv add "langgraph-cli[inmem]"
  langgraph new --template=new-langgraph-project-python custom-auth
  cd custom-auth
  ```
</CodeGroup>

The template gives us a placeholder LangGraph app. Try it out by installing the local dependencies and running the development server:

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install -e .
  langgraph dev
  ```

  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv add .
  langgraph dev
  ```

  ```bash npm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  npx @langchain/langgraph-cli dev
  ```
</CodeGroup>

The server will start and open [Studio](/langsmith/studio) in your browser:

```
> - 🚀 API: http://127.0.0.1:2024
> - 🎨 Studio UI: https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024
> - 📚 API Docs: http://127.0.0.1:2024/docs
>
> This in-memory server is designed for development and testing.
> For production use, please use LangSmith.
```

If you were to self-host this on the public internet, anyone could access it.

<img alt="No authentication: the dev server is publicly reachable, anyone can access the bot if exposed to the internet." />

## 2. Add authentication

Now that you have a base LangGraph app, add authentication to it.

<Note>
  In this tutorial, you will start with a hard-coded token for example purposes. You will get to a "production-ready" authentication scheme in the third tutorial.
</Note>

The [Auth](https://reference.langchain.com/python/langgraph-sdk/auth/Auth) object lets you register an authentication function that the LangSmith deployment will run on every request. This function receives each request and decides whether to accept or reject.

Create a new file `src/security/auth.py`. This is where your code will live to check if users are allowed to access your bot:

```python {highlight={10,15-16}} title="src/security/auth.py" theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langgraph_sdk import Auth

# This is our toy user database. Do not do this in production
VALID_TOKENS = {
    "user1-token": {"id": "user1", "name": "Alice"},
    "user2-token": {"id": "user2", "name": "Bob"},
}

# The "Auth" object is a container that LangGraph will use to mark our authentication function
auth = Auth()

# The `authenticate` decorator tells LangGraph to call this function as middleware

# for every request. This will determine whether the request is allowed or not
@auth.authenticate
async def get_current_user(authorization: str | None) -> Auth.types.MinimalUserDict:
    """Check if the user's token is valid."""
    assert authorization
    scheme, token = authorization.split()
    assert scheme.lower() == "bearer"
    # Check if token is valid
    if token not in VALID_TOKENS:
        raise Auth.exceptions.HTTPException(status_code=401, detail="Invalid token")

    # Return user info if valid
    user_data = VALID_TOKENS[token]
    return {
        "identity": user_data["id"],
    }
```

Notice that your [Auth.authenticate](https://reference.langchain.com/python/langgraph-sdk/auth/Auth/authenticate) handler does two important things:

1. Checks if a valid token is provided in the request's [Authorization header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization)
2. Returns the user's [MinimalUserDict](https://reference.langchain.com/python/langgraph-sdk/auth/types/MinimalUserDict)

Now tell LangGraph to use authentication by adding the following to the [langgraph.json](https://reference.langchain.com/python/cloud/reference/cli/#configuration-file) configuration:

```json {highlight={7-9}} title="langgraph.json" theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "dependencies": ["."],
  "graphs": {
    "agent": "./src/agent/graph.py:graph"
  },
  "env": ".env",
  "auth": {
    "path": "src/security/auth.py:auth"
  }
}
```

## 3. Test your bot

Start the server again to test everything out:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
langgraph dev --no-browser
```

If you didn't add the `--no-browser`, the Studio UI will open in the browser. By default, we also permit access from Studio, even when using custom auth. This makes it easier to develop and test your bot in Studio. You can remove this alternative authentication option by setting `disable_studio_auth: true` in your auth configuration:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
    "auth": {
        "path": "src/security/auth.py:auth",
        "disable_studio_auth": true
    }
}
```

## 4. Chat with your bot

You should now only be able to access the bot if you provide a valid token in the request header. Users will still, however, be able to access each other's resources until you add [resource authorization handlers](/langsmith/auth#resource-specific-handlers) in the next section of the tutorial.

<img alt="Auth gate passes requests with a valid token, but no per-resource filters are applied yet—so users share visibility until authorization handlers are added in the next step." />

Run the following code in a file or notebook:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langgraph_sdk import get_client

# Try without a token (should fail)
client = get_client(url="http://localhost:2024")
try:
    thread = await client.threads.create()
    print("❌ Should have failed without token!")
except Exception as e:
    print("✅ Correctly blocked access:", e)

# Try with a valid token
client = get_client(
    url="http://localhost:2024", headers={"Authorization": "Bearer user1-token"}
)

# Create a thread and chat
thread = await client.threads.create()
print(f"✅ Created thread as Alice: {thread['thread_id']}")

response = await client.runs.create(
    thread_id=thread["thread_id"],
    assistant_id="agent",
    input={"messages": [{"role": "user", "content": "Hello!"}]},
)
print("✅ Bot responded:")
print(response)
```

You should see that:

1. Without a valid token, we can't access the bot
2. With a valid token, we can create threads and chat

Congratulations! You've built a chatbot that only lets "authenticated" users access it. While this system doesn't (yet) implement a production-ready security scheme, we've learned the basic mechanics of how to control access to our bot. In the next tutorial, we'll learn how to give each user their own private conversations.

## Next steps

Now that you can control who accesses your bot, you might want to:

1. Continue the tutorial by going to [Make conversations private](/langsmith/resource-auth) to learn about resource authorization.
2. Read more about [authentication concepts](/langsmith/auth).
3. Check out the API reference for [Auth](https://reference.langchain.com/python/langgraph-sdk/auth/Auth), [Auth.authenticate](https://reference.langchain.com/python/langgraph-sdk/auth/Auth/authenticate), and [MinimalUserDict](https://reference.langchain.com/python/langgraph-sdk/auth/types/MinimalUserDict) for more authentication details.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/set-up-custom-auth.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Set up feedback criteria
Source: https://docs.langchain.com/langsmith/set-up-feedback-criteria

<Tip>
  **Recommended Reading**

  Before diving into this content, it might be helpful to read the following:

  * [Conceptual guide on tracing and feedback](/langsmith/observability-concepts)
  * [Reference guide on feedback data format](/langsmith/feedback-data-format)
</Tip>

Feedback criteria are represented in the application as feedback tags. For human feedback, you can set up new feedback criteria as continuous feedback or categorical feedback.

<Info>
  You can also manage feedback configs programmatically with the SDK. Refer to [Manage feedback & annotation queues programmatically](/langsmith/annotation-queues-sdk).
</Info>

<Tip>
  For free-form acceptance criteria a reviewer writes per-run (rather than a fixed set of rubric scores), refer to [Use assertions](/langsmith/assertions).
</Tip>

To set up a new feedback criteria, follow [this link](https://smith.langchain.com/settings/workspaces/feedbacks) to view all existing tags for your workspace, then click **New Tag**.

## Continuous feedback

For continuous feedback, you can enter a feedback tag name, then select a minimum and maximum value. Every value, including floating-point numbers, within this range will be accepted as feedback scores.

<img alt="Cont feedback" />

## Categorical feedback

For categorical feedback, you can enter a feedback tag name, then add a list of categories, each category mapping to a score. When you provide feedback, you can select one of these categories as the feedback score.
Both the category label and the score will be logged as feedback in `value` and `score` fields, respectively.

<img alt="Cat feedback" />

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/set-up-feedback-criteria.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Set up hierarchy
Source: https://docs.langchain.com/langsmith/set-up-hierarchy

This page describes setting up and managing your LangSmith [*organization*](/langsmith/administration-overview#organizations) and [*workspaces*](/langsmith/administration-overview#workspaces):

* [Set up an organization](#set-up-an-organization): Create and manage organizations for team collaboration, including user management and role assignments.
* [Set up a workspace](#set-up-a-workspace): Set up and configure workspaces to organize your LangSmith resources, manage workspace members, and configure settings for team collaboration.
* [Set up applications](#set-up-applications): Set up applications within a workspace to further organize LangSmith resources, and take advantage of ABAC permissioning.

<Check>
  You may find it helpful to refer to the [overview on LangSmith resource hierarchy](/langsmith/administration-overview) before you read this setup page.
</Check>

## Set up an organization

<Note>
  If you're interested in managing your organization and workspaces programmatically, refer to [Manage organizations using the API](/langsmith/manage-organization-by-api).
</Note>

### Create an organization

When you log into the [UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-set-up-hierarchy) for the first time, LangSmith will create a personal organization for you automatically. If you'd like to collaborate with others, you can create a separate organization and invite your team members to join.

1. Open the **Organizations** drawer by clicking your profile icon in the bottom left
2. Select the organization profile dropdown at the top of the menu.
3. Click **+ Create organization**.

Shared organizations require a credit card before you can use them. You will need to [set up billing](/langsmith/billing#set-up-billing-for-your-account) to proceed.

### Manage and navigate workspaces

Once you've subscribed to a [plan](/langsmith/pricing-plans) that allows for multiple users per organization, you can set up [workspaces](/langsmith/administration-overview#workspaces) to collaborate more effectively and isolate LangSmith resources between different groups of users. To navigate between workspaces and access the resources within each workspace (trace projects, annotation queues, etc.), select the desired workspace from the picker in the bottom left of the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-set-up-hierarchy).

### Manage users

Manage membership in your shared organization in the **Members and roles** tabs on the [Settings page](https://smith.langchain.com/settings). Here you can:

* Invite new users to your organization, selecting workspace membership and (if [RBAC](/langsmith/rbac) is enabled) workspace role.
* Edit a user's organization role.
* Remove users from your organization.

Organizations on the [Enterprise plan](/langsmith/pricing-plans) may set up custom workspace roles in the **Roles** tab. For more details, refer to the [access control setup guide](/langsmith/user-management).

#### Organization roles

Organization-scoped roles are used to determine access to organization settings. The role selected also has an impact on workspace membership:

* **Organization Admin** grants full access to manage all organization configuration, users, billing, and workspaces. Any Organization Admin has `Admin` access to all workspaces in an organization.
* **Organization User** may read organization information, but cannot execute any write actions at the organization level. You can add an Organization User to a subset of workspaces and assigned workspace roles as usual (if [RBAC](/langsmith/rbac) is enabled), which specify permissions at the workspace level.

<Info>
  The [Organization User](/langsmith/rbac#organization-user) and [Organization Viewer](/langsmith/rbac#organization-viewer) roles are only available in organizations on [Plus and Enterprise plans](https://langchain.com/pricing). In Developer organizations (single workspace), all users are assigned the [Organization Admin](/langsmith/rbac#organization-admin) role by default. Custom organization-scoped roles are not available.
</Info>

For a full list of permissions associated with each role, refer to the [Administration overview](/langsmith/administration-overview#organization-roles) page.

## Set up a workspace

When you log in for the first time, LangSmith will create a default [workspace](/langsmith/administration-overview#workspaces) for you in your personal organization. You can use workspaces to separate resources between different teams or business units to establish clear trust boundaries between them. Within each workspace, [Role-Based Access Control (RBAC)](/langsmith/rbac) manages permissions and access levels, which ensures that users only have access to the resources and settings necessary for their role. Most LangSmith activity happens in the context of a workspace, each of which has its own settings and access controls.

For guidance on choosing the right workspace organization model for your team (single workspace per team, multiple teams per workspace, or multiple workspaces per team), refer to [Workload isolation](/langsmith/workload-isolation).

### Create a workspace

To create a new workspace, navigate to the [**Settings** page](https://smith.langchain.com/settings) **Workspaces** tab in your shared organization and click **Add Workspace**.

Once you have created your workspace, you can manage its members and other configuration by selecting the workspace on the **Settings** page.

<Note>
  Different plans have different limits placed on the number of workspaces that you can use in an organization. For more information, refer to the [pricing page](https://www.langchain.com/pricing-langsmith).
</Note>

### Manage users

<Info>
  Only [workspace admins](/langsmith/rbac#workspace-admin) can manage workspace membership and, if RBAC is enabled, change a user's workspace role.
</Info>

For users that are already members of an organization, a workspace admin may add them to a workspace in the **Workspace members** tab on the [**Workspaces settings** page](https://smith.langchain.com/settings/workspaces). Users may also be invited directly to one or more workspaces when they are invited to an organization.

### Configure workspace settings

Workspace configuration exists in the [**Workspaces settings** page](https://smith.langchain.com/settings/workspaces) tab. Select the workspace to configure and then the desired configuration sub-tab.
Configuration options include:

* **Workspace members**
* **API keys**
* **Secrets**
* **Feedback config**
* **Models**
* **Rules**
* **Shared URLs**

### Delete a workspace

<Warning>
  Deleting a workspace will permanently delete the workspace and all associated data. This action cannot be undone.
</Warning>

You can delete a workspace through the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-set-up-hierarchy) or via [API](/langsmith/smith-api/workspaces/delete-workspace). You must be a [workspace admin](/langsmith/rbac#workspace-admin) in order to delete a workspace.

In the LangSmith UI:

1. Navigate to **Settings**.
2. Select the workspace you want to delete.
3. Click the delete icon <Icon icon="trash" /> in the top-right corner of the screen.

## Set up applications

You can create applications within a workspace to further organize resources, such as tracing projects and datasets. A workspace may have zero or more applications.

You can view all resources within a workspace by selecting **All applications** from the LangSmith UI home page. You may tag resources to multiple applications by adding them to the `Application` tag under **Resource Tags** on the **Settings** page.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/set-up-hierarchy.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Set up resource tags
Source: https://docs.langchain.com/langsmith/set-up-resource-tags

Create and manage resource tags to organize projects, datasets, prompts, and other resources within a LangSmith workspace.

<Info>
  Resource tags are available for [Plus and Enterprise plans](/langsmith/pricing-plans).
</Info>

While [workspaces](/langsmith/administration-overview#workspaces) help separate trust boundaries and access control, tags help you organize resources within a workspace. Tags are key-value pairs that you can attach to resources.

<Note>
  **Not to be confused with commit tags**: Resource tags are key-value pairs used to organize and filter workspace resources (projects, datasets, prompts, etc.). [Commit tags](/langsmith/manage-prompts#commit-tags) are labels that reference specific versions in a prompt's commit history. While both types of tags can use similar terminology (like `prod` or `staging`), resource tags help you *organize resources* across your workspace, while commit tags control *which version* of a prompt is used in your code.
</Note>

You can manage resource tags through the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-set-up-resource-tags) or programmatically via the [REST API](/langsmith/smith-api-ref):

<Tabs>
  <Tab title="UI" icon="browser">
    ## Create a tag

    <Note>
      To create resource tags, you must have the [`workspaces:manage` permission](/langsmith/organization-workspace-operations) (granted to the [workspace admin](/langsmith/rbac#workspace-admin) role by default). Editors can apply **Application** tags to resources they have update access to, but creating tag keys or applying other tag types requires this permission. For more on applying tags to resources, refer to the workspace operations [Tags section](/langsmith/organization-workspace-operations#tags).
    </Note>

    To create a tag:

    1. Navigate to the workspace **Settings** page and click on **Resource tags** in the left-hand sidebar.
    2. Here, you'll find the existing tag values, grouped by key. LangSmith creates the **Application** and **Environment** keys by default. You can use the **Application** key to filter resources shown in the UI.
    3. Select <Icon icon="tag" /> **New Tag** at the top of the page. You'll be prompted to enter a key and a value for the tag. Note that you can use an existing key or create a new one.

       <img alt="Create resource tag modal accessed from the Settings menu in the LangSmith UI." />

       <img alt="Create resource tag modal accessed from the Settings menu in the LangSmith UI." />

    ## Assign a tag to a resource

    Within the same side panel for creating a new tag, you can also assign resources to tags. Search for corresponding resources in the **Assign resources** section and select the resources you want to tag.

    <Note>
      You can only tag workspace-scoped resources with resource tags. This includes Tracing Projects, Annotation Queues, Deployments, Experiments, Datasets, and Prompts.
    </Note>

    To un-assign a tag from a resource, click the <Icon icon="trash" /> trash icon next to the tag, both in the tag panel and the resource tag panel.

    ## Delete a tag

    You can delete either a key or a value of a tag from the [**Settings** page > **Resource tags** page](https://smith.langchain.com/settings/workspaces/resource_tags). To delete a key, click the <Icon icon="trash" /> trash icon next to the key. To delete a value, click the <Icon icon="trash" /> trash icon next to the value.

    If you delete a key, LangSmith will delete all values associated with that key. When you delete a value, you will lose all associations between that value and resources.
  </Tab>

  <Tab title="API" icon="terminal">
    ## Manage tags via API

    You can create, assign, and query resource tags programmatically using the LangSmith REST API. All tag endpoints live under `/api/v1/workspaces/current/` and require an [API key](/langsmith/create-account-api-key).

    ### Set up

    Import the `requests` library and configure your API key and headers. All the following examples assume these variables are in scope:

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import os
    import requests

    LANGSMITH_API_URL = "https://api.smith.langchain.com"
    LANGSMITH_API_KEY = os.environ["LANGSMITH_API_KEY"]
    headers = {"x-api-key": LANGSMITH_API_KEY, "Content-Type": "application/json"}
    ```

    ### Create a tag key

    <Note>
      Creating tag keys requires the [`workspaces:manage`](/langsmith/organization-workspace-operations) permission.
      If you want to apply the default **Application** key, skip this step and list existing keys instead.
    </Note>

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    response = requests.post(
        f"{LANGSMITH_API_URL}/api/v1/workspaces/current/tag-keys",
        headers=headers,
        json={"key": "Environment", "description": "Deployment environment"},
    )
    response.raise_for_status()
    tag_key = response.json()
    tag_key_id = tag_key["id"]
    ```

    ### Create a tag value

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    response = requests.post(
        f"{LANGSMITH_API_URL}/api/v1/workspaces/current/tag-keys/{tag_key_id}/tag-values",
        headers=headers,
        json={"value": "production"},
    )
    response.raise_for_status()
    tag_value = response.json()
    tag_value_id = tag_value["id"]
    ```

    ### Assign a tag to a resource

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    response = requests.post(
        f"{LANGSMITH_API_URL}/api/v1/workspaces/current/taggings",
        headers=headers,
        json={
            "tag_value_id": tag_value_id,
            "resource_type": "project",
            "resource_id": "<project-uuid>",
        },
    )
    response.raise_for_status()
    tagging_id = response.json()["id"]
    ```

    Valid `resource_type` values: `project`, `dataset`, `prompt`, `experiment`, `queue`,
    `deployment`, `dashboard`, `evaluator`, `mcp_server`, `fleet_integration`.

    <Note>
      **Permissions**: Assigning the **Application** tag only requires update access to the target resource,
      so editors can do this without `workspaces:manage`. Assigning any other tag key requires `workspaces:manage`.
    </Note>

    **Applying existing tags**: If the key and value already exist (for example, the default **Application** key), retrieve their IDs first and go straight to the assign step:

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    tags = requests.get(
        f"{LANGSMITH_API_URL}/api/v1/workspaces/current/tags",
        headers=headers,
    ).json()
    # tags is a list of {id, key, values: [{id, value}, ...]}
    ```

    ### Query tags

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    # All tag keys and values in the workspace
    tags = requests.get(
        f"{LANGSMITH_API_URL}/api/v1/workspaces/current/tags",
        headers=headers,
    ).json()

    # Tags on a specific resource
    resource_tags = requests.get(
        f"{LANGSMITH_API_URL}/api/v1/workspaces/current/tags/resource",
        headers=headers,
        params={"resource_type": "project", "resource_id": "<project-uuid>"},
    ).json()

    # All resources tagged with a specific value
    taggings = requests.get(
        f"{LANGSMITH_API_URL}/api/v1/workspaces/current/taggings",
        headers=headers,
        params={"tag_value_id": tag_value_id},
    ).json()
    ```

    ### Remove a tag from a resource

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    requests.delete(
        f"{LANGSMITH_API_URL}/api/v1/workspaces/current/taggings/{tagging_id}",
        headers=headers,
    )
    ```

    ### Delete a tag key or value

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    # Delete a value (removes all resource assignments for that value)
    requests.delete(
        f"{LANGSMITH_API_URL}/api/v1/workspaces/current/tag-keys/{tag_key_id}/tag-values/{tag_value_id}",
        headers=headers,
    )

    # Delete a key (also deletes all its values)
    requests.delete(
        f"{LANGSMITH_API_URL}/api/v1/workspaces/current/tag-keys/{tag_key_id}",
        headers=headers,
    )
    ```

    For a full list of request/response fields, refer to the [API reference](/langsmith/smith-api-ref).
  </Tab>
</Tabs>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/set-up-resource-tags.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# How to set up an application with requirements.txt
Source: https://docs.langchain.com/langsmith/setup-app-requirements-txt

An application must be configured with a [configuration file](/langsmith/cli#configuration-file) in order to be deployed to LangSmith (or to be self-hosted). This how-to guide discusses the basic steps to set up an application for deployment using `requirements.txt` to specify project dependencies.

This example is based on [this repository](https://github.com/langchain-ai/langgraph-example), which uses the LangGraph framework.

The final repository structure will look something like this:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
my-app/
├── my_agent # all project code lies within here
│   ├── utils # utilities for your graph
│   │   ├── __init__.py
│   │   ├── tools.py # tools for your graph
│   │   ├── nodes.py # node functions for your graph
│   │   └── state.py # state definition of your graph
│   ├── requirements.txt # package dependencies
│   ├── __init__.py
│   └── agent.py # code for constructing your graph
├── .env # environment variables
└── langgraph.json # configuration file for LangGraph
```

<Tip>
  LangSmith Deployment supports deploying a [LangGraph](/oss/python/langgraph/overview) *graph*. However, the implementation of a *node* of a graph can contain arbitrary code. This means any framework can be implemented within a node and deployed on LangSmith Deployment. This lets you implement your core application logic without using additional LangGraph OSS APIs while still using LangSmith for [deployment](/langsmith/deployment), scaling, and [observability](/langsmith/observability). For more details, refer to [Use any framework with LangSmith Deployment](/langsmith/application-structure#use-any-framework-with-langsmith-deployment).
</Tip>

You can also set up with:

* `pyproject.toml`: If you prefer using poetry for dependency management, check out [this how-to guide](/langsmith/setup-app-requirements-txt) on using `pyproject.toml` for LangSmith.
* a monorepo: If you are interested in deploying a graph located inside a monorepo, take a look at [this repository](https://github.com/langchain-ai/langgraph-example-monorepo) for an example of how to do so.

After each step, an example file directory is provided to demonstrate how code can be organized.

## Specify dependencies

Dependencies can optionally be specified in one of the following files: `pyproject.toml`, `setup.py`, or `requirements.txt`. If none of these files is created, then dependencies can be specified later in the [configuration file](#create-the-configuration-file).

The dependencies below will be included in the image, you can also use them in your code, as long as with a compatible version range:

```
langgraph>=0.4.10,<2
langgraph-sdk>=0.3.5
langgraph-checkpoint>=3.0.1,<5
langchain-core>=0.3.66
langsmith>=0.7.31
orjson>=3.9.7
httpx>=0.25.0
tenacity>=8.0.0
uvicorn>=0.26.0
sse-starlette>=2.1.3,<3.4.0
uvloop>=0.18.0
httptools>=0.5.0
jsonschema-rs>=0.20.0
structlog>=24.1.0
cloudpickle>=3.0.0
truststore>=0.1
protobuf>=6.32.1,<7.0.0
grpcio>=1.80.0,<1.81.0
grpcio-tools>=1.80.0,<1.81.0
grpcio-health-checking>=1.80.0,<1.81.0
opentelemetry-api>=0.0.1
opentelemetry-sdk>=0.0.1
opentelemetry-exporter-otlp-proto-http>=0.0.1
```

Example `requirements.txt` file:

```
langgraph
langchain_anthropic
tavily-python
langchain_openai

```

Example file directory:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
my-app/
├── my_agent # all project code lies within here
│   └── requirements.txt # package dependencies
```

## Specify environment variables

Environment variables can optionally be specified in a file (e.g. `.env`). See the [Environment Variables reference](/langsmith/env-var) to configure additional variables for a deployment.

Example `.env` file:

```
MY_ENV_VAR_1=foo
MY_ENV_VAR_2=bar
OPENAI_API_KEY=key
```

Example file directory:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
my-app/
├── my_agent # all project code lies within here
│   └── requirements.txt # package dependencies
└── .env # environment variables
```

<Tip>
  By default, LangSmith follows the `uv`/`pip` behavior of **not** installing prerelease versions unless explicitly allowed. If want to use prereleases, you have the following options:

  * With `pyproject.toml`: add `allow-prereleases = true` to your `[tool.uv]` section.
  * With `requirements.txt` or `setup.py`: you must explicitly specify every prerelease dependency, including transitive ones. For example, if you declare `a==0.0.1a1` and `a` depends on `b==0.0.1a1`, then you must also explicitly include `b==0.0.1a1` in your dependencies.
</Tip>

## Define graphs

Implement your graphs. Graphs can be defined in a single file or multiple files. Make note of the variable names of each [CompiledStateGraph](https://reference.langchain.com/python/langgraph/graph/state/CompiledStateGraph) to be included in the application. The variable names will be used later when creating the [LangGraph configuration file](/langsmith/cli#configuration-file).

Example `agent.py` file, which shows how to import from other modules you define (code for the modules is not shown here, please see [this repository](https://github.com/langchain-ai/langgraph-example) to see their implementation):

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
