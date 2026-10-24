# Access & oversight
Source: https://docs.langchain.com/langsmith/fleet/access-and-oversight

Control who can access agents, how they authenticate, and audit everything they do.

Fleet gives you the control layer for scaling agents across your organization: tiered permissions, credential management, human-in-the-loop oversight, and an audit trail for agent actions.

## Permissions and sharing

Fleet provides granular control over every agent in two dimensions: **who gets access** and **what they can do**.

* **Who**: Share with individual users or your entire workspace.
* **What**: Three permission levels:
  * **Clone** — copy and customize the agent
  * **Run** — use without modifying
  * **Edit** — full access to change instructions, tools, and settings

You can layer these permissions. Give a core team edit access, share run-only with the broader organization, and revoke at any time.

For setup instructions, see [Change access to the agent](/langsmith/fleet/manage-agent-settings#change-access-to-the-agent).

## Agent identity and credentials

Fleet offers two credential models that control how agents authenticate with external tools:

* **Fixed credentials ("Claws")**: The agent uses a single set of credentials regardless of who runs it. Use for shared-resource agents like a team Slack bot where everyone interacts through the same account.
* **User credentials ("Assistants")**: The agent acts on behalf of the individual user who invokes it. Each user authenticates with their own account via OAuth. Use for tools where users have different access levels, like a personal email assistant.

This is configurable per agent, so you can choose the right model for each use case.

For setup instructions, see [Agent identity](/langsmith/fleet/agent-identity).

## Tool access control

Fleet provides layered access control for tools, covering both **custom MCP servers** (user-added, workspace-scoped) and **built-in integrations** (platform-provided, such as Gmail, Slack, and GitHub):

* **[Role-based access control (RBAC)](#role-based-permissions)**: Controls access at the role level.
* **[Attribute-based access control (ABAC)](#attribute-based-access-control)**: Adds per-resource granularity on top of RBAC.
* **[Workspace integration policy](#workspace-integration-policy)**: Provides an admin-controlled enable/disable gate for built-in integrations.

<Note>
  Tool access control is an Enterprise feature. If you are interested in this feature, [contact our sales team](https://www.langchain.com/contact-sales).
</Note>

### Role-based permissions

Role-based access control (RBAC) grants or denies access to all MCP servers and integrations in a workspace based on a user's role. Configure roles in **Settings > Roles**.

The following permissions are available for MCP servers and integrations:

| Permission           | Description                                                                         |
| -------------------- | ----------------------------------------------------------------------------------- |
| `mcp-servers:read`   | Discover and list MCP servers and integrations                                      |
| `mcp-servers:invoke` | Execute tools from MCP servers and integrations, including OAuth connect/disconnect |
| `mcp-servers:create` | Create new MCP server configurations                                                |
| `mcp-servers:update` | Modify MCP server configurations                                                    |
| `mcp-servers:delete` | Remove MCP server configurations                                                    |

<Note>
  A role with `mcp-servers:read` and `mcp-servers:invoke` can see and use all MCP servers and integrations in the workspace.
</Note>

For more on RBAC, see [Role-based access control](/langsmith/rbac).

#### Create a role with tool permissions

<Steps>
  <Step title="Open role settings">
    Navigate to **Settings > Roles** and click **Create role**.
  </Step>

  <Step title="Configure MCP Servers permissions">
    Expand the **MCP Servers** section and select the permissions to include. For example, grant `Read` and `Invoke` for users who need to use tools but not manage server configurations.
  </Step>

  <Step title="Assign the role">
    Assign the role to users in the workspace in **Settings > Members**.
  </Step>
</Steps>

### Attribute-based access control

Attribute-based access control (ABAC) adds resource-level granularity on top of RBAC. Admins can tag individual MCP servers or integrations and create policies that grant or restrict access based on those tags.

ABAC operates on two resource types for tools:

| Resource type       | Applies to                                         |
| ------------------- | -------------------------------------------------- |
| `mcp_server`        | Custom MCP servers added to the workspace          |
| `fleet_integration` | Built-in integrations (Gmail, Slack, GitHub, etc.) |

<Note>
  A role with no `mcp-servers:*` RBAC permissions can still be granted access to specific tagged resources (e.g. only Notion and Gmail) via an ABAC allow policy. Conversely, a role with broad RBAC access can be restricted from specific resources via an ABAC deny policy.
</Note>

For details on policy structure, operators, and managing policies via the API, see [Attribute-based access control](/langsmith/abac).

### Workspace integration policy

Built-in integrations have an additional control layer: a workspace-level enable/disable toggle managed from **Settings > Integrations > Access control**. This acts as an admin-controlled baseline that runs before per-user RBAC and ABAC.

If an integration is disabled at the workspace level, no user can access it regardless of their role or ABAC policies.

<Note>
  The Access control page is only visible to admin users (requires `workspaces:manage` permission).
</Note>

### Policy evaluation order

The three layers evaluate in sequence. The evaluation order differs slightly between custom MCP servers and built-in integrations:

**Custom MCP servers:**

```
ABAC deny → RBAC → ABAC allow
```

**Built-in integrations:**

```
Workspace policy gate → ABAC deny → RBAC → ABAC allow
```

At each step:

1. **Workspace policy gate** (integrations only): If the integration is disabled, access is denied. No further evaluation.
2. **ABAC deny**: If a deny policy matches, access is denied. Deny always wins.
3. **RBAC**: If the user's role grants the required permission, access is allowed (unless step 4 is needed).
4. **ABAC allow**: If RBAC does not grant access, an allow policy can still grant it for specific tagged resources.

## Observability and audit trail

Agent actions in Fleet are captured in a structured [LangSmith trace](/langsmith/observability), including tool calls, decisions, and outputs. You can inspect, search, and export traces.

Combined with agent identity and permissions, tracing tells you which agent acted, on whose behalf, with what credentials, and what it did at each step.

## Human-in-the-loop oversight

Fleet provides a [central inbox](https://smith.langchain.com/agents/inbox) for reviewing agent actions across all your agents. You can configure agents to pause and request approval before taking specific actions, then review, approve, edit, or reject from one place.

For setup instructions, see [Human-in-the-loop](/langsmith/fleet/essentials#human-in-the-loop).

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/fleet/access-and-oversight.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Agent identity
Source: https://docs.langchain.com/langsmith/fleet/agent-identity

Choose whether your Fleet agent authenticates with its own credentials or with each user's credentials.

Agent identity controls whose [credentials](/langsmith/fleet/workspace-admin) the agent uses when it interacts with apps and services.

<Warning>
  Once an agent identity is set, it cannot be changed.
</Warning>

## Fixed credentials ("Claws")

The agent always authenticates with the same API keys and OAuth tokens, regardless of who is interacting with it.

Use fixed credentials when:

* The agent operates as a shared service (for example, a team Slack bot or a daily briefing agent).
* You want a single set of authenticated accounts for all users.
* The agent needs to run on [channels](/langsmith/fleet/channels) or [schedules](/langsmith/fleet/schedules), which require fixed credentials.

With fixed credentials, all actions the agent takes (sending emails, posting messages, reading calendars) use the account that the agent owner connected during setup.

## User credentials ("Assistants")

The agent authenticates with the API keys and OAuth tokens of the user interacting with it, acting on the user's behalf.

Use user credentials when:

* Each user should act through their own accounts (for example, an email assistant that reads and sends from the user's own inbox).
* You need per-user access control so the agent only sees what that user is authorized to see.
* Audit trails need to reflect which user performed each action.

With user credentials, each user authenticates individually the first time they interact with the agent. The agent uses that user's tokens for all subsequent actions in their threads.

## Set agent identity

To set the identity for an agent:

1. In the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-fleet-agent-identity), navigate to the agent you want to edit.
2. Click <Icon icon="pencil" /> **Edit** in the top right corner.
3. Click **Set identity** and select the identity you want to use.
4. Click **Save**.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/fleet/agent-identity.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Arcade integration
Source: https://docs.langchain.com/langsmith/fleet/arcade

Connect your workspace to Arcade to give agents access to third-party tools like GitHub, Gmail, Slack, and more.

[Arcade](https://arcade.dev) provides managed MCP gateways that give your agents access to thousands of third-party tools behind a single integration. Supported services span email, calendars, code hosting, project management, CRM, messaging, search, and more, including GitHub, Gmail, Google Drive, Slack, Notion, Jira, Salesforce, Linear, and HubSpot.

When you connect Arcade to your workspace, a workspace admin selects an Arcade organization and project, then installs MCP gateways from that project. Each user connects their own Arcade account so that tool calls authenticate with their individual credentials.

## Prerequisites

* A LangSmith workspace with **admin** permissions (to configure the integration)
* An [Arcade](https://arcade.dev) account with at least one organization and project

## Set up Arcade as a workspace admin

Only [workspace admins](/langsmith/rbac#workspace-admin) can configure the Arcade integration, including adding or deleting MCP Gateways. Once configured, the integration is available to all users in the workspace.

<Steps>
  <Step title="Open the Integrations tab">
    Navigate to [**Fleet** > **Integrations**](https://smith.langchain.com/agents/tools). In the left menu under **Apps**, click **Arcade**.
  </Step>

  <Step title="Connect your Arcade account">
    Click **Connect** to authenticate with Arcade via OAuth. This links your Arcade account to the workspace.
  </Step>

  <Step title="Select an organization and project">
    Choose the Arcade **Organization** and **Project** for the workspace. All MCP gateways installed in the workspace come from this project.
  </Step>

  <Step title="Install MCP gateways">
    Browse the available gateways from your Arcade project and click **Add to workspace** to install them. Installed gateways appear as MCP servers available to all agents in the workspace.
  </Step>
</Steps>

## Connect as a workspace member

After an admin configures Arcade, other users must connect their own Arcade account to use the tools. Each user authenticates individually so that tool calls use their own credentials, not the admin's.

<Steps>
  <Step title="Get an invitation to the Arcade project">
    Ask the workspace admin to invite you to their Arcade organization and project. You must be a member of the same project to access its gateways.
  </Step>

  <Step title="Connect your account">
    Navigate to [**Fleet** > **Integrations**](https://smith.langchain.com/agents/tools). In the left menu under **Apps**, click **Arcade**, then click **Connect** to authenticate via OAuth.
  </Step>

  <Step title="Browse available tools">
    After connecting, MCP servers installed by the admin appear automatically. You can add these tools to your agents from the agent editor.
  </Step>
</Steps>

<Note>
  Workspace members cannot change the Arcade organization or project. Only admins can modify the workspace-level configuration.
</Note>

## Use Arcade tools with an agent

After connecting, add Arcade tools to a specific agent:

1. Open your agent in [Fleet](https://smith.langchain.com/agents?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-fleet-arcade) and click the <Icon icon="pencil" /> **Edit Agent** icon.
2. In the **Toolbox** section, click **+ Add**.
3. Select the Arcade tools you want to enable for the agent.
4. Click **Save changes**.

The agent can now call these tools at runtime. When a tool requires authorization, Arcade prompts the user to grant access via OAuth.

## Change the organization or project

Admins can update the workspace-level Arcade organization and project at any time.

<Warning>
  Changing the organization or project **removes all installed MCP servers** from the workspace. You will need to reinstall gateways from the new project afterward.
</Warning>

<Steps>
  <Step title="Open configuration">
    Navigate to [**Fleet** > **Integrations**](https://smith.langchain.com/agents/tools). In the left menu under **Apps**, click **Arcade**. Click the settings icon to open the **Arcade Workspace Configuration** dialog.
  </Step>

  <Step title="Select new organization and project">
    Choose the new organization and project from the dropdowns.
  </Step>

  <Step title="Confirm the change">
    Click **Save Changes**. If the change removes existing MCP servers, confirm in the follow-up dialog. All previously installed gateways are removed and you can install new ones from the updated project.
  </Step>
</Steps>

## Disconnect from Arcade

Navigate to [**Fleet** > **Integrations**](https://smith.langchain.com/agents/tools). In the left menu under **Apps**, click **Arcade**, then click **Disconnect**. This revokes your OAuth token but does not affect the workspace configuration or other users.

Admins can remove the Arcade integration entirely by deleting the workspace configuration, which also removes all installed Arcade MCP servers.

## Next steps

<CardGroup>
  <Card title="Add more tools" icon="puzzle" href="/langsmith/fleet/tools">
    Connect additional services to your agent
  </Card>

  <Card title="Remote MCP servers" icon="server" href="/langsmith/fleet/remote-mcp-servers">
    Connect custom MCP servers to your workspace
  </Card>

  <Card title="Manage agent settings" icon="settings" href="/langsmith/fleet/manage-agent-settings">
    Configure agent behavior and permissions
  </Card>
</CardGroup>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/fleet/arcade.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Auth-aware tool responses
Source: https://docs.langchain.com/langsmith/fleet/auth-format

Format tool responses to trigger OAuth flows and resume execution automatically.

Some [tools](/langsmith/fleet/tools) require user authorization (for example, Google, Slack, GitHub). LangSmith Fleet includes middleware to detect when a tool needs authorization and to pause the run with a clear prompt to the user. After the user completes auth, the same tool call is retried automatically.

## Return shape to request auth

If a tool detects missing authorization, return a JSON string containing the following fields:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "auth_required": true,
  "auth_url": "https://auth.example.com/start",
  "auth_id": "opaque-tracking-id"
}
```

* `auth_required`: set to `true` to signal an interrupt is needed.
* `auth_url`: where the user should be redirected to authorize.
* `auth_id`: optional correlation ID to track the auth session.

When Fleet detects this response, it interrupts the run, displays the authentication UI to the user, and automatically retries the tool call once authorization completes.

If you want your custom tools to reuse the same authentication required interrupt + UI, ensure your tools return the same shape of JSON.

<Note>
  Return only this JSON as the tool's output. Avoid including additional text or content. Fleet parses the response to trigger the authentication flow.
</Note>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/fleet/auth-format.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# LangSmith Fleet changelog
Source: https://docs.langchain.com/langsmith/fleet/changelog

Weekly updates to LangSmith Fleet

Weekly updates to [LangSmith Fleet](/langsmith/fleet).

<Callout icon="rss">
  **Subscribe**: This changelog includes an [RSS feed](https://docs.langchain.com/langsmith/fleet-changelog/rss.xml) that can integrate with [Slack](https://slack.com/help/articles/218688467-Add-RSS-feeds-to-Slack), [email](https://zapier.com/apps/email/integrations/rss/1441/send-new-rss-feed-entries-via-email), Discord bots like [Readybot](https://readybot.io/) or [RSS Feeds to Discord Bot](https://rss.app/en/bots/rssfeeds-discord-bot), and other subscription tools.
</Callout>

<Update label="June 1-5, 2026">
  ## New features

  * [Skills](/langsmith/fleet/skills) load faster: the skills list fetches lightweight metadata first and loads file contents only when you open a skill.
  * The agent creation menu adds a [Templates](/langsmith/fleet/templates) entry.
  * The [remote MCP](/langsmith/fleet/remote-mcp-servers) authorization screen now shows the connecting application's name, logo, and homepage, terms, and privacy links instead of its raw client ID.
  * [Slack integration](/langsmith/fleet/slack-app) available in AWS and APAC regions.

  ## Fixes

  * [Scheduled (cron) execution](/langsmith/fleet/schedules) is restored for enterprise Fleet agents.
  * Long-running agent runs and agent-builder generations are no longer cut off after 60 seconds.
  * The Gmail read-emails [tool](/langsmith/fleet/tools) now returns results when you search sent mail with an `in:sent` query.
  * Scrolling is improved for long toolbox, skill, and sub-agent lists in the agent editor, and webhook dialogs now scroll within the viewport.
</Update>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/fleet/changelog.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Channels
Source: https://docs.langchain.com/langsmith/fleet/channels

Configure channels to trigger your Fleet agents automatically.

Channels define when your agent starts running. Connect your agent to external events so it responds automatically to messages, emails, or other events.

<Tip>
  To trigger an agent on a recurring basis, use [schedules](/langsmith/fleet/schedules).
</Tip>

## Add a channel

To add a channel:

<Steps>
  <Step title="Edit your agent">
    Open your agent in the [Fleet](https://smith.langchain.com/agents?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-fleet-channels) inbox.
    Next to the agent name, click the <Icon icon="pencil" /> **Edit Agent** icon.
  </Step>

  <Step title="Add the channel">
    1. In the **Channels** section, click **+ Add** and select the channel you want to add.
    2. Follow the prompts to add the channel and authenticate.
  </Step>
</Steps>

### Add a Gmail channel

The Gmail channel activates your agent when new emails arrive in your inbox. To let your agent read and respond to emails, add Gmail tools in the **Tools** section. Available Gmail tools include reading emails, sending replies, creating drafts, managing labels, and marking messages as read. See [Tool integrations](/langsmith/fleet/tools) for more information.

<Warning>
  The Gmail channel only monitors your primary inbox. The following emails do not activate the channel:

  * **Alias emails**: Messages sent to an email alias rather than your primary address.
  * **Mailing list emails**: Messages received through a mailing list or group.
  * **Emails outside the inbox**: Messages that skip the inbox due to filters, or that land in spam, trash, or other folders.
</Warning>

### Add a Slack channel

The default Slack bot activates your agent when messages are posted in a connected Slack channel. It triggers on every message in the channel and cannot receive DMs. To let your agent respond in Slack, [add Slack tools](/langsmith/fleet/slack-app#add-slack-tools).

<Tip>
  For tag-only triggering or DM support, [create a custom Slack bot](/langsmith/fleet/slack-app) instead. See [Custom vs. default bot](/langsmith/fleet/slack-app#custom-vs-default-bot) for a comparison.
</Tip>

### Add a Microsoft Teams channel

The Teams channel activates your agent when messages are sent in Microsoft Teams conversations.

For full setup instructions including Azure Bot creation, credential registration, and tool configuration, see [Integrate Teams with an agent](/langsmith/fleet/teams-app).

## Pause and resume channels

You can pause and resume channels without removing them. To pause all channels:

1. In the [Fleet](https://smith.langchain.com/agents?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-fleet-channels) inbox, open your agent.
2. Next to the agent name, click the <Icon icon="pencil" /> **Edit Agent** icon.
3. In the **Channels** section, click <Icon icon="player-pause" /> **Pause channels** button to pause all channels.

To resume all channels, click <Icon icon="player-play" /> **Resume channels** button.

## Thread behavior

How threads are marked depends on whether the agent uses channels:

* **Chat agents (no channel)**: Responses mark the thread as **unread**. Viewing the thread marks it as read.
* **Channel-based agents**: Responses keep the thread as **read** by default.

You can manually mark any thread as read or unread at any time.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/fleet/channels.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Use Fleet agents in code
Source: https://docs.langchain.com/langsmith/fleet/code

Invoke Fleet agents via the LangGraph SDK or REST API, or download and run them locally with the fleet-deepagents-export package.

There are two main ways to use Fleet agents programmatically:

* **[Call from code](#call-from-code)**: Invoke your agent remotely via the LangGraph SDK or REST API, without downloading anything.
* **[Export to code](#export-to-code)**: Download your agent's configuration and run it locally as a self-contained Python project using the `fleet-deepagents-export` package.

## Call from code

You can invoke LangSmith Fleet agents from your applications using the [LangGraph SDK](/langsmith/reference) or the REST API. Fleet agents run on [Agent Server](/langsmith/agent-server), so you can use the same API methods as any other [LangSmith deployment](/langsmith/deployment).

The REST API lets you call your agent from any language or platform that supports HTTP requests.

### Prerequisites

* A LangSmith account with a Fleet agent
* A [Personal Access Token (PAT)](/langsmith/create-account-api-key) for authentication
* (SDK only) The [LangGraph SDK](/langsmith/reference) installed:

<CodeGroup>
  ```bash Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install langgraph-sdk python-dotenv
  ```

  ```bash TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  yarn add @langchain/langgraph-sdk
  ```
</CodeGroup>

### Authentication

To authenticate with your agent's Fleet deployment, provide a LangSmith [Personal Access Token (PAT)](/langsmith/create-account-api-key) to the `api_key` argument when instantiating the LangGraph SDK client, or via the `X-API-Key` header. If using `X-API-Key`, you must also set the `X-Auth-Scheme` header to `langsmith-api-key`.

If the PAT you pass is not tied to the owner of the agent, your request will be rejected with a `404 Not Found` error.

If the agent you're trying to invoke is a <Tooltip href="/langsmith/fleet/manage-agent-settings">workspace agent</Tooltip> and you're not the owner, you can perform all the same operations as you would in the UI (read-only).

### 1. Get the agent ID and URL

To get your agent's `agent_id` and `api_url`:

1. In the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-fleet-code), navigate to your agent's inbox.
2. Next to the agent name, click the <Icon icon="pencil" /> **Edit Agent** icon.
3. Click the <Icon icon="settings" /> **Settings** icon in the top right corner.
4. Click **View code snippets** to see pre-populated values for your agent.

Copy the code below and replace `agent_id` and `api_url` with the values from your agent's code snippets.

Create a `.env` file in your project root with your [Personal Access Token](/langsmith/create-account-api-key):

```bash .env theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
LANGGRAPH_API_KEY=your-personal-access-token
```

### 2. Fetch agent configuration

Verify your connection by fetching your agent's configuration:

<Tabs>
  <Tab title="Python">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import os
    from dotenv import load_dotenv
    from langgraph_sdk.client import get_client

    load_dotenv()

    agent_id = "your-agent-id"

    api_key = os.getenv("LANGGRAPH_API_KEY")
    api_url = "<AGENT-BUILDER-URL>.us.langgraph.app"

    client = get_client(
        url=api_url,
        api_key=api_key,
        headers={
            "X-Auth-Scheme": "langsmith-api-key",
        },
    )

    async def get_assistant(agent_id: str):
        agent = await client.assistants.get(agent_id)
        print(agent)

    if __name__ == "__main__":
        import asyncio
        asyncio.run(get_assistant(agent_id))
    ```
  </Tab>

  <Tab title="TypeScript">
    ```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import "dotenv/config";
    import { Client } from "@langchain/langgraph-sdk";

    const agentId = "your-agent-id";

    const apiKey = process.env.LANGGRAPH_API_KEY;
    const apiUrl = "<AGENT-BUILDER-URL>.us.langgraph.app";

    const client = new Client({
      apiUrl,
      apiKey,
      defaultHeaders: {
        "X-Auth-Scheme": "langsmith-api-key",
      },
    });

    async function main(agentId: string) {
      const agent = await client.assistants.get(agentId);
      console.log(agent);
    }

    main(agentId).catch(console.error);
    ```
  </Tab>

  <Tab title="cURL">
    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    curl --request GET \
        --url "<AGENT-BUILDER-URL>.us.langgraph.app/assistants/your-agent-id" \
        --header 'Content-Type: application/json' \
        --header 'X-Api-Key: your-personal-access-token' \
        --header 'X-Auth-Scheme: langsmith-api-key'
    ```
  </Tab>
</Tabs>

<Callout icon="key">
  Use a [Personal Access Token (PAT)](/langsmith/create-account-api-key) tied to your LangSmith account. Set the `X-Auth-Scheme` header to `langsmith-api-key` for authentication.
</Callout>

### 3. Invoke agent

The examples below show how to send a message to your agent and receive a response. You can use either a **stateless** run (no thread, no conversation history) or a **stateful** run (with a thread to maintain conversation history across multiple turns).

#### Stateless run

A stateless run sends a single request and returns the full response. No conversation history is persisted. This is the simplest way to call your agent:

<Tabs>
  <Tab title="Python">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import os
    from dotenv import load_dotenv
    from langgraph_sdk.client import get_client

    load_dotenv()

    agent_id = "your-agent-id"

    api_key = os.getenv("LANGGRAPH_API_KEY")
    api_url = "https://<AGENT-BUILDER-URL>.us.langgraph.app"

    client = get_client(
        url=api_url,
        api_key=api_key,
        headers={
            "X-Auth-Scheme": "langsmith-api-key",
        },
    )

    result = await client.runs.wait(
        None,
        agent_id,
        input={
            "messages": [
                {"role": "user", "content": "What can you help me with?"}
            ]
        },
    )
    print(result)
    ```
  </Tab>

  <Tab title="TypeScript">
    ```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import "dotenv/config";
    import { Client } from "@langchain/langgraph-sdk";

    const agentId = "your-agent-id";

    const apiKey = process.env.LANGGRAPH_API_KEY;
    const apiUrl = "<AGENT-BUILDER-URL>.us.langgraph.app";

    const client = new Client({
      apiUrl,
      apiKey,
      defaultHeaders: {
        "X-Auth-Scheme": "langsmith-api-key",
      },
    });

    const result = await client.runs.wait(
      null,
      agentId,
      {
        input: {
          messages: [
            { role: "user", content: "What can you help me with?" }
          ]
        }
      }
    );
    console.log(result);
    ```
  </Tab>

  <Tab title="cURL">
    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    curl --request POST \
        --url "<AGENT-BUILDER-URL>.us.langgraph.app/runs/wait" \
        --header 'Content-Type: application/json' \
        --header 'X-Api-Key: your-personal-access-token' \
        --header 'X-Auth-Scheme: langsmith-api-key' \
        --data '{
            "assistant_id": "your-agent-id",
            "input": {
                "messages": [
                    {
                        "role": "user",
                        "content": "What can you help me with?"
                    }
                ]
            }
        }'
    ```
  </Tab>
</Tabs>

#### Stateless streaming run

To stream the response as it is generated rather than waiting for the full result, use the streaming endpoint:

<Tabs>
  <Tab title="Python">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    async for chunk in client.runs.stream(
        None,
        agent_id,
        input={
            "messages": [
                {"role": "user", "content": "What can you help me with?"}
            ]
        },
        stream_mode="updates",
    ):
        if chunk.data and "run_id" not in chunk.data:
            print(chunk.data)
    ```
  </Tab>

  <Tab title="TypeScript">
    ```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    const streamResponse = client.runs.stream(
      null,
      agentId,
      {
        input: {
          messages: [
            { role: "user", content: "What can you help me with?" }
          ]
        },
        streamMode: "updates"
      }
    );
    for await (const chunk of streamResponse) {
      if (chunk.data && !("run_id" in chunk.data)) {
        console.log(chunk.data);
      }
    }
    ```
  </Tab>

  <Tab title="cURL">
    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    curl --request POST \
        --url "<AGENT-BUILDER-URL>.us.langgraph.app/runs/stream" \
        --header 'Content-Type: application/json' \
        --header 'X-Api-Key: your-personal-access-token' \
        --header 'X-Auth-Scheme: langsmith-api-key' \
        --data '{
            "assistant_id": "your-agent-id",
            "input": {
                "messages": [
                    {
                        "role": "user",
                        "content": "What can you help me with?"
                    }
                ]
            },
            "stream_mode": [
                "updates"
            ]
        }'
    ```
  </Tab>
</Tabs>

#### Stateful run with a thread

To maintain conversation history across multiple interactions, first create a thread and then run your agent on it. Each subsequent run on the same thread has access to the full message history:

<Tabs>
  <Tab title="Python">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import os
    from dotenv import load_dotenv
    from langgraph_sdk.client import get_client

    load_dotenv()

    agent_id = "your-agent-id"

    api_key = os.getenv("LANGGRAPH_API_KEY")
    api_url = "<AGENT-BUILDER-URL>.us.langgraph.app"

    client = get_client(
        url=api_url,
        api_key=api_key,
        headers={
            "X-Auth-Scheme": "langsmith-api-key",
        },
    )

    thread = await client.threads.create()

    async for chunk in client.runs.stream(
        thread["thread_id"],
        agent_id,
        input={
            "messages": [
                {"role": "user", "content": "Hi, my name is Alice."}
            ]
        },
        stream_mode="updates",
    ):
        if chunk.data and "run_id" not in chunk.data:
            print(chunk.data)

    async for chunk in client.runs.stream(
        thread["thread_id"],
        agent_id,
        input={
            "messages": [
                {"role": "user", "content": "What is my name?"}
            ]
        },
        stream_mode="updates",
    ):
        if chunk.data and "run_id" not in chunk.data:
            print(chunk.data)
    ```
  </Tab>

  <Tab title="TypeScript">
    ```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import "dotenv/config";
    import { Client } from "@langchain/langgraph-sdk";

    const agentId = "your-agent-id";

    const apiKey = process.env.LANGGRAPH_API_KEY;
    const apiUrl = "<AGENT-BUILDER-URL>.us.langgraph.app";

    const client = new Client({
      apiUrl,
      apiKey,
      defaultHeaders: {
        "X-Auth-Scheme": "langsmith-api-key",
      },
    });

    const thread = await client.threads.create();

    let streamResponse = client.runs.stream(
      thread["thread_id"],
      agentId,
      {
        input: {
          messages: [
            { role: "user", content: "Hi, my name is Alice." }
          ]
        },
        streamMode: "updates"
      }
    );
    for await (const chunk of streamResponse) {
      if (chunk.data && !("run_id" in chunk.data)) {
        console.log(chunk.data);
      }
    }

    streamResponse = client.runs.stream(
      thread["thread_id"],
      agentId,
      {
        input: {
          messages: [
            { role: "user", content: "What is my name?" }
          ]
        },
        streamMode: "updates"
      }
    );
    for await (const chunk of streamResponse) {
      if (chunk.data && !("run_id" in chunk.data)) {
        console.log(chunk.data);
      }
    }
    ```
  </Tab>

  <Tab title="cURL">
    First, create a thread:

    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    curl --request POST \
        --url "<AGENT-BUILDER-URL>.us.langgraph.app/threads" \
        --header 'Content-Type: application/json' \
        --header 'X-Api-Key: your-personal-access-token' \
        --header 'X-Auth-Scheme: langsmith-api-key' \
        --data '{}'
    ```

    Use the `thread_id` from the response to send messages on the thread:

    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    curl --request POST \
        --url "<AGENT-BUILDER-URL>.us.langgraph.app/threads/<THREAD_ID>/runs/stream" \
        --header 'Content-Type: application/json' \
        --header 'X-Api-Key: your-personal-access-token' \
        --header 'X-Auth-Scheme: langsmith-api-key' \
        --data '{
            "assistant_id": "your-agent-id",
            "input": {
                "messages": [
                    {
                        "role": "user",
                        "content": "Hi, my name is Alice."
                    }
                ]
            },
            "stream_mode": [
                "updates"
            ]
        }'
    ```

    Send a follow-up message on the same thread:

    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    curl --request POST \
        --url "<AGENT-BUILDER-URL>.us.langgraph.app/threads/<THREAD_ID>/runs/stream" \
        --header 'Content-Type: application/json' \
        --header 'X-Api-Key: your-personal-access-token' \
        --header 'X-Auth-Scheme: langsmith-api-key' \
        --data '{
            "assistant_id": "your-agent-id",
            "input": {
                "messages": [
                    {
                        "role": "user",
                        "content": "What is my name?"
                    }
                ]
            },
            "stream_mode": [
                "updates"
            ]
        }'
    ```
  </Tab>
</Tabs>

### REST API reference

The table below summarizes the key endpoints. Replace `<API_URL>` with your agent's deployment URL.

| Operation                                                                                                                | Method | Endpoint                                    |
| ------------------------------------------------------------------------------------------------------------------------ | ------ | ------------------------------------------- |
| [Get agent info](/langsmith/agent-server-api/assistants/get-assistant)                                                   | `GET`  | `<API_URL>/assistants/<AGENT_ID>`           |
| [Create a thread](/langsmith/agent-server-api/threads/create-thread)                                                     | `POST` | `<API_URL>/threads`                         |
| [Run (wait for result)](https://docs.langchain.com/langsmith/agent-server-api/stateless-runs/create-run-wait-for-output) | `POST` | `<API_URL>/runs/wait`                       |
| [Run (streaming)](/langsmith/agent-server-api/stateless-runs/create-run-stream-output)                                   | `POST` | `<API_URL>/runs/stream`                     |
| [Run on thread (wait)](/langsmith/agent-server-api/thread-runs/create-run-wait-for-output)                               | `POST` | `<API_URL>/threads/<THREAD_ID>/runs/wait`   |
| /langsmith/agent-server-api/thread-runs/create-run-stream-output                                                         | `POST` | `<API_URL>/threads/<THREAD_ID>/runs/stream` |

All endpoints require the following headers:

* `Content-Type: application/json`
* `X-Api-Key:` your [Personal Access Token](/langsmith/create-account-api-key)
* `X-Auth-Scheme: langsmith-api-key`

For the full API specification, see the [Agent Server API reference](/langsmith/server-api-ref).

## Export to code

The **Export to code** feature lets you download your Fleet agent as a self-contained Python project and run it locally. This is useful when you want to:

* Run your agent in your own infrastructure without calling the Fleet API
* Extend or customize the agent beyond what the Fleet UI supports (add custom tools, middleware, or skills)
* Inspect or version-control the full agent implementation
* Use LangGraph Studio for local development and graph inspection

The [`fleet-deepagents-export`](https://pypi.org/project/fleet-deepagents-export/) package ([GitHub](https://github.com/langchain-ai/fleet-deepagents-export)) handles reading the exported configuration and wiring up your agent with MCP tools, subagents, and skills.

### Prerequisites

* Python 3.11+
* [`uv`](https://docs.astral.sh/uv/getting-started/installation/) (recommended) for dependency management
* A LangSmith Fleet agent to export

### 1. Copy the starter project

The starter project at [`examples/template-agent/`](https://github.com/langchain-ai/fleet-deepagents-export/tree/main/examples/template-agent) is the recommended starting point. Clone the repo and copy the starter:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
git clone https://github.com/langchain-ai/fleet-deepagents-export.git
cp -R fleet-deepagents-export/examples/template-agent my-agent
cd my-agent
```

### 2. Export your agent from Fleet

In the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-fleet-code), open your agent and export it as a `.zip` file.

<img alt="fleet-export-code" />

Then drop the contents into the `fleet/` directory of your starter project:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
unzip path/to/my-export.zip -d fleet/
```

The `fleet/` directory contains everything your agent needs:

* `AGENTS.md` — system prompt
* `config.json` — model configuration and workspace metadata
* `tools.json` — MCP server connections
* `subagents/` (optional) — subagent definitions
* `skills/` (optional) — skill instructions

### 3. Configure your environment

Copy the example env file and fill in the required values:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
cp .env.example .env
```

The three `LANGSMITH_*_ID` values are in `fleet/config.json` under `metadata`. Open that file and copy `tenant_id`, `organization_id`, and `ls_user_id` into your `.env`:

```bash .env theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# Model provider — set the key for whichever provider your agent uses
ANTHROPIC_API_KEY=your-anthropic-api-key

# LangSmith credentials — copy IDs from fleet/config.json → metadata
LANGSMITH_API_KEY=your-langsmith-pat
LANGSMITH_TENANT_ID=your-tenant-id
LANGSMITH_ORGANIZATION_ID=your-organization-id
LANGSMITH_USER_ID=your-user-id       # required if your agent uses OAuth tools

# Built-in MCP tools (Gmail, Calendar, GitHub)
BUILTIN_MCP_URL=https://tools.langchain.com/mcp
```

### 4. Install dependencies and run

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
make setup    # installs dependencies via uv sync
```

Then choose how to interact with your agent:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
make dev    # LangGraph Studio — browser UI for chat and graph inspection
make run    # terminal REPL via cli.py — text-only chat
```

### 5. Customize the agent

The starter separates Fleet-owned files from files you own and can freely edit:

| File / Directory       | Owner | Purpose                                                                                   |
| ---------------------- | ----- | ----------------------------------------------------------------------------------------- |
| `fleet/`               | Fleet | Drop export contents here. Re-unzip to update; nothing else is touched.                   |
| `agent.py`             | You   | Graph wiring. Override the model by replacing the `model = components.pop("model")` line. |
| `custom_tools.py`      | You   | Add code-defined tools; merged with Fleet MCP tools at runtime.                           |
| `custom_middleware.py` | You   | Add `AgentMiddleware` instances for logging, filters, pre/post hooks, etc.                |
| `custom_skills/`       | You   | Drop `<skill-name>/SKILL.md` files; layered on top of `fleet/skills/`.                    |
| `cli.py`               | You   | Terminal REPL; edit freely.                                                               |

Here is the full `agent.py` from the starter:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
"""Standalone deepagent exported from LangSmith Fleet.

LangGraph Studio / dev server:  make dev
Terminal:                        make run  (see cli.py)

Extension points (edit these, not this file):
- ``custom_tools.py``      — add code-defined tools
- ``custom_middleware.py`` — wrap the agent loop with logging, filters, etc.
- ``custom_skills/``       — drop ``<skill-name>/SKILL.md`` files
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from dotenv import load_dotenv

load_dotenv()

from custom_middleware import custom_middleware
from custom_tools import custom_tools
from deepagents import create_deep_agent
from fleet_deepagents_export import StaticSkillsLoader, load_agent_components

PROJECT_DIR = Path(__file__).parent
FLEET_DIR = PROJECT_DIR / "fleet"
CUSTOM_SKILLS_DIR = PROJECT_DIR / "custom_skills"
