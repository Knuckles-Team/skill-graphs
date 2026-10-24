# Integrate Slack with an agent
Source: https://docs.langchain.com/langsmith/fleet/slack-app

Connect LangSmith Fleet to your Slack workspace to let your agents communicate with users in Slack.

With LangSmith Fleet, you can securely connect your agents to your Slack workspace to let your agents communicate with users in Slack.

After integrating, your agents will be able to:

* Receive messages directly from your Slack bot, starting a new run with the message content.
* Communicate back to your Slack workspace after processing the message.
* Obtain relevant context from Slack by reading thread messages and conversation history.

LangSmith Fleet offers two ways to connect an agent to Slack: a **custom Slack bot** (recommended) and the **default Slack bot**.

## Custom vs. default bot

|               | [Custom Slack bot](#set-up-a-custom-slack-bot)  | [Default Slack bot](#set-up-the-default-slack-bot)                |
| ------------- | ----------------------------------------------- | ----------------------------------------------------------------- |
| **Slack app** | Your own app, created through LangSmith         | LangSmith's Slack account                                         |
| **Trigger**   | Tag the bot directly with `@Bot_Name`           | Every message in the channel                                      |
| **DMs**       | ✅                                               | ❌                                                                 |
| **Best for**  | Direct back-and-forth communication from Slack. | Starting a run every time a message is sent in a specific channel |

<Info>
  The Slack integration with Fleet does not have any direct pricing. However, agent runs and traces are billed through the [LangSmith platform](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-fleet-slack-app) according to your organization's plan.

  For current pricing information, see the [LangSmith pricing page](https://www.langchain.com/pricing).
</Info>

## Set up a custom Slack bot

A custom Slack bot gives you full bidirectional communication between your agent and Slack.

### Prerequisites

* An existing agent in Fleet (see [Quickstart](/langsmith/fleet/quickstart) to create one)
* Admin access to a Slack workspace or permission to install apps

### Create the Slack app

<Steps>
  <Step title="Create a new Slack app">
    1. Navigate to the **Integrations** page in Fleet and go to the **Apps** section.
    2. Click **Add Slack App**.
    3. Enter a name for the bot.
    4. Click **Create Slack App**. You will be redirected to the Slack API site with a popup asking you to pick a workspace.

    <Warning>
      Do not create a separate Slack app outside of this flow. The app must be created through this popup.
    </Warning>
  </Step>

  <Step title="Select your workspace">
    1. Choose the workspace where you want to install the bot.
    2. Click **Next**.
    3. Click **Create Bot**.
  </Step>

  <Step title="Enter your app credentials">
    After creating the bot, you will receive your app credentials. Enter the following credentials in Fleet:

    * App ID
    * Client ID
    * Client secret
    * Signing secret

    <Note>
      Copy the full client secret and signing secret carefully to ensure a successful connection.
    </Note>
  </Step>

  <Step title="Connect OAuth">
    1. Click **Connect OAuth**.
    2. Click **Allow** to give Fleet access to your app.
  </Step>

  <Step title="Finish setup">
    Link your Slack bot to an existing agent, or click **Finish** to link later.
  </Step>
</Steps>

### Link the Slack bot to an agent

You can link a Slack bot to an agent from the integrations page or from the agent editor. Each agent can only have one Slack app, and each Slack app can only be linked to one agent.

<Tabs>
  <Tab title="From the Integrations page">
    1. Navigate to the **Slack Apps** section on the **Integrations** page in Fleet.
    2. Select the bot you want to link.
    3. From the dropdown menu, choose the agent you want to link to.
    4. Verify that **\<Agent Name>** appears next to the bot name.
  </Tab>

  <Tab title="From the agent editor">
    1. Select your agent from **My Agents** in the left-hand navigation.

    2. Click <Icon icon="pencil" /> **Edit Agent**.

    3. Scroll to the **Channels** section.

       <Note>
         You may need to set the agent identity first. Click **Set Identity** in the top right corner.
       </Note>

    4. Click **Slack**.

    5. From the dropdown menu, select the Slack app you want to link.
  </Tab>
</Tabs>

### Invite the bot to your channel

1. In Slack, go to the channel where you want to use the bot.
2. Type `/invite @YourSlackBotName` to invite the bot.
3. Send a message mentioning the bot to verify it responds.

### Configure agent behavior (optional)

Your agent needs to know how to handle incoming Slack messages. Update its instructions by prompting it directly in the agent chat:

```
Update your instructions to handle the Slack Trigger and Slack Tools
for bidirectional communication
```

Adjust the instructions based on your use case—for example, you might want the agent to only respond to certain types of questions, or to pull information from specific sources before replying.

## Set up the default Slack bot

The default Slack bot uses LangSmith's Slack account and triggers your agent on every message posted in a connected channel. It cannot receive DMs.

<Steps>
  <Step title="Authenticate with Slack and get the channel ID">
    1. On the [Fleet > Integrations page](https://smith.langchain.com/agents/tools), authenticate with Slack.
    2. In Slack, invite the default app (`@LangSmith Fleet`) to a channel.
    3. Copy the channel ID.
  </Step>

  <Step title="Open the agent editor">
    In [Fleet](https://smith.langchain.com/agents?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-fleet-slack-app), select your agent and click the <Icon icon="pencil" /> **Edit Agent** icon.
  </Step>

  <Step title="Add a Slack channel">
    1.In the **Channels** section, click **Slack**.

    1. Navigate to **LangSmith Bot** and click **Add Channel**.
    2. Paste the channel ID and channel name.
  </Step>

  <Step title="Start a run">
    Send any message in the channel to start a run.
  </Step>
</Steps>

## Add Slack tools

Slack tools let your agent send messages, reply in threads, and read channel history. They work regardless of how the agent was triggered, whether through Slack, the Fleet UI, a schedule, or a webhook.

For example, you could start a long-running research task in the Fleet chat UI and instruct the agent to send you a Slack message when it's done.

<Tip>
  You can also ask your agent to add these tools itself. In the agent chat, try: "Add the Slack tools so you can respond to messages."
</Tip>

1. In the agent editor, scroll to the **Tools** section.
2. Click **+ Add**.
3. Search for "Slack" and add the tools you need, if not already added:
   * **slack\_send\_channel\_message**—Post messages to a channel
   * **slack\_reply\_to\_message**—Reply in a thread
   * **slack\_write\_private\_message**—Send direct messages
   * **slack\_read\_channel\_history**—Read recent messages
   * **slack\_read\_thread\_messages**—Read thread replies
4. If prompted, click **Connect** to authorize the Slack tools.
5. Click **Save changes**.

## Troubleshooting

### Agent does not respond

If your agent is not responding, you can try the following:

* Check the thread in Fleet for any approvals that need human input.
* Verify the bot was invited to the channel.
* Check the **Feed** tab for errors.
* Ensure the channel is not paused in the **Channels** section.
* Try reauthenticating with Slack to make sure Fleet has your most up-to-date Slack user ID stored.

### Not allowed to tag the bot

If you receive a private message saying you are not allowed to tag the bot, your Slack ID is not authorized for that agent. The agent's owner needs to share the agent with you—either by sharing run access with the whole workspace or with you individually.

## Next steps

<CardGroup>
  <Card title="Add more tools" icon="puzzle" href="/langsmith/fleet/tools">
    Connect additional services to your agent
  </Card>

  <Card title="Add more channels" icon="bolt" href="/langsmith/fleet/channels">
    Set up email, schedule, or webhook channels
  </Card>

  <Card title="Use templates" icon="layout-grid" href="/langsmith/fleet/templates">
    Start from a prebuilt agent template
  </Card>
</CardGroup>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/fleet/slack-app.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Integrate Teams with an agent
Source: https://docs.langchain.com/langsmith/fleet/teams-app

Connect LangSmith Fleet to Microsoft Teams by bringing your own Azure Bot to let agents communicate with users in Teams.

With LangSmith Fleet, you can connect your agents to Microsoft Teams by registering a custom Azure Bot. Once connected, your agents can:

* Receive messages from Teams users, starting a new run with the message content.
* Respond directly in Teams conversations using the Bot Framework.
* Access Teams channels and messages through Microsoft Graph API tools.

<Note>
  In channel conversations, the bot only responds when explicitly mentioned. In direct messages and group chats, the bot responds to all messages.
</Note>

## Prerequisites

* An existing agent in Fleet (see [Quickstart](/langsmith/fleet/quickstart) to create one)
* An [Azure account](https://portal.azure.com) with permission to create resources
* Admin access to a Microsoft Teams workspace, or permission to install apps

## Create an Azure Bot

Before registering in Fleet, you need to create an Azure Bot resource and obtain its credentials.

<Steps>
  <Step title="Create an Azure Bot resource">
    1. Go to the [Azure Portal](https://portal.azure.com).
    2. Search for **Azure Bot** and click **Create**.
    3. Fill in the required fields:
       * **Bot handle**: A unique identifier for your bot.
       * **Subscription**: Select your Azure subscription.
       * **Resource group**: Create a new one or select an existing one.
       * **Type of App**: Select **Multi Tenant**.
       * **Creation type**: Select **Create new Microsoft App ID**.
    4. Click **Review + create**, then **Create**.
  </Step>

  <Step title="Get your app credentials">
    After the resource is created:

    1. Navigate to your bot resource and click **Configuration** in the left sidebar.
    2. Copy the **Microsoft App ID**. You will need this later.
    3. Click **Manage Password** next to the App ID.
    4. Click **New client secret**, add a description, and click **Add**.
    5. Copy the **Value** of the new secret immediately — it is only shown once.

    <Warning>
      Copy the client secret value immediately after creation. You cannot retrieve it later. If you lose it, you must create a new one.
    </Warning>
  </Step>

  <Step title="Configure the messaging endpoint">
    You will set the messaging endpoint after registering the bot in Fleet. Skip this field for now—you will return to this step later.
  </Step>
</Steps>

## Register the bot in Fleet

<Steps>
  <Step title="Open the integrations page">
    1. Navigate to **Fleet** in the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-fleet-teams-app).
    2. Go to the **Integrations** page.
    3. Click **Add Teams App**.
  </Step>

  <Step title="Enter your credentials">
    Fill in the following fields:

    * **App Name**: A display name for the bot in Fleet.
    * **Azure App ID**: The Microsoft App ID from the Azure Bot resource.
    * **Azure App Password**: The client secret value you copied earlier.
    * **Azure Tenant ID** (optional): Your Azure AD tenant ID. Leave as default for multi-tenant bots.

    Click **Create** to register the bot.
  </Step>

  <Step title="Copy the webhook URL">
    After registration, Fleet displays a **webhook URL**. Copy this URL—you need it to complete the Azure Bot configuration.
  </Step>

  <Step title="Set the messaging endpoint in Azure">
    1. Return to your Azure Bot resource in the [Azure Portal](https://portal.azure.com).
    2. Go to **Configuration**.
    3. Paste the webhook URL from Fleet into the **Messaging endpoint** field.
    4. Click **Apply**.
  </Step>
</Steps>

## Add the bot to Teams

<Steps>
  <Step title="Open the Teams channel">
    1. In the Azure Portal, go to your bot resource.
    2. Click **Channels** in the left sidebar.
    3. Select **Microsoft Teams** and click **Apply**.
    4. Agree to the terms of service.
  </Step>

  <Step title="Install the bot in Teams">
    1. In Teams, click **Apps** in the left sidebar.
    2. Click **Manage your apps** then **Upload an app**.
    3. Upload a [Teams app manifest](https://learn.microsoft.com/en-us/microsoftteams/platform/resources/schema/manifest-schema) that references your Azure App ID, or use the **Open in Teams** link from the Azure Bot Channels page.
    4. Add the bot to the desired team or chat.
  </Step>
</Steps>

## Link the bot to an agent

You can link a Teams bot to an agent from the integrations page or from the agent editor.

### Link from the integrations page

1. Navigate to the **Teams Apps** section on the **Integrations** page in Fleet.
2. Select the bot you want to link.
3. From the dropdown menu, choose the agent you want to link to.

### Link from the agent editor

1. Select your agent from **My Agents** in the left-hand navigation.
2. Click <Icon icon="pencil" /> **Edit Agent**.
3. Scroll to the **Channels** section.
4. Click **Teams**.
5. From the dropdown menu, select the Teams app you want to link.

## Add Teams tools

Tools let your agent take actions in Teams. To respond to messages and interact with Teams, add the relevant tools.

<Tip>
  You can also ask your agent to add these tools itself. In the agent chat, try: "Add the Teams tools so you can respond to messages."
</Tip>

1. In the agent editor, scroll to the **Tools** section.
2. Click **+ Add**.
3. Search for "Teams" and add the tools you need:
   * **teams\_bot\_send\_proactive\_message** — Send messages back to the Teams conversation
   * **microsoft\_teams\_list\_my\_teams** — List teams the authenticated user belongs to
   * **microsoft\_teams\_list\_channels** — List channels in a team
   * **microsoft\_teams\_post\_channel\_message** — Post a message to a channel
   * **microsoft\_teams\_read\_channel\_messages** — Read recent messages from a channel
4. If prompted, click **Connect** to authorize the Microsoft Graph tools.
5. Click **Save changes**.

<Note>
  The `teams_bot_send_proactive_message` tool uses Bot Framework credentials and does not require separate OAuth authorization. The other Teams tools use Microsoft Graph API and may require OAuth consent.
</Note>

## Configure agent behavior (optional)

Your agent needs to know how to handle incoming Teams messages. Update its instructions by prompting it directly in the agent chat:

```
Update your instructions to handle the Teams Trigger and Teams Tools
for bidirectional communication
```

Adjust the instructions based on your use case—for example, you might want the agent to only respond to certain types of questions, or to pull information from specific sources before replying.

## Troubleshooting

### Agent does not respond

* Check the thread in Fleet for any approvals that need human input.
* In channel conversations, make sure you **@mention** the bot. Channel messages without a mention are ignored.
* Check the **Feed** tab for errors.
* Verify the messaging endpoint in the Azure Bot resource matches the webhook URL from Fleet.
* Ensure the bot registration is not paused in Fleet.

### Invalid credentials error during registration

* Verify that the **Azure App ID** and **App Password** (client secret) are correct.
* Make sure the client secret has not expired. Create a new secret in Azure if needed.
* Check that the bot type is set to **Multi Tenant** in Azure.

### Bot works in direct messages but not in channels

* The bot must be explicitly **@mentioned** in channel conversations.
* Make sure the bot has been added to the team and has permission to read messages in the channel.

## Next steps

<CardGroup>
  <Card title="Add more tools" icon="puzzle" href="/langsmith/fleet/tools">
    Connect additional services to your agent
  </Card>

  <Card title="Add more channels" icon="bolt" href="/langsmith/fleet/channels">
    Set up email, schedule, or webhook channels
  </Card>

  <Card title="Use templates" icon="layout-grid" href="/langsmith/fleet/templates">
    Start from a prebuilt agent template
  </Card>
</CardGroup>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/fleet/teams-app.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Templates
Source: https://docs.langchain.com/langsmith/fleet/templates

Start faster with curated Fleet templates and customize tools, prompts, and channels.

LangSmith Fleet includes [starter templates](https://www.langchain.com/templates) to help you create agents quickly. Templates include predefined instructions, [tools](/langsmith/fleet/tools), and [channels](/langsmith/fleet/essentials#channels) (if applicable) for common use cases. You can use templates as-is, or as a baseline to customize.

<Tip>
  If you're new to Fleet, start with the step-by-step [quickstart](/langsmith/fleet/quickstart) to build your first agent using a template.
</Tip>

## Features

Templates are pre-configured agents designed for specific use cases. Each template includes the following components:

### Pre-configured tools

Templates come with a curated set of [tools](/langsmith/fleet/essentials#tools) that enable the agent to perform specific actions. For example, an email assistant template includes tools for reading, sending, and organizing emails. Tools connect to external services through OAuth authentication, allowing your agent to interact with apps like Gmail, Slack, or Linear. For a complete list, refer to [Supported tools](/langsmith/fleet/tools).

### System instructions

Each template includes a *system prompt* (also called *instructions*) that defines the agent's behavior, personality, and capabilities. The system prompt guides how the agent interprets user requests and uses its available tools. You can customize these instructions to match your specific needs.

### Channels (optional)

Some templates include [channels](/langsmith/fleet/essentials#channels) that allow agents to respond to external events automatically. For example, a Slack bot template might include a channel that activates when someone mentions the agent in a Slack conversation. Channels enable proactive agent behavior beyond chat-based interactions.

### Cloning and customization

Templates serve as starting points that you clone to create your own agent. When you clone a template, you create an independent copy that you can customize without affecting the original. You can modify prompts, add or remove tools, attach different channels, and switch models to tailor the agent to your requirements.

## Available templates

<CardGroup>
  <Card title="Daily calendar brief" icon="calendar">
    A daily agent that scans your calendar and delivers a concise briefing with meeting details and important context.
  </Card>

  <Card title="Email assistant" icon="mail">
    Automate email triage with an agent that flags important emails, drafts and sends replies, and schedules meetings.
  </Card>

  <Card title="LinkedIn recruiter" icon="users">
    Automate recruiting with an agent that digests candidate requirements, adapts to feedback, and outputs a candidate list.
  </Card>

  <Card title="Social media AI monitor" icon="news">
    An agent that tracks top AI discussions from X lists and Hacker News, and delivers a daily Slack message with important updates.
  </Card>
</CardGroup>

<Info>
  For more information, see [Templates](https://www.langchain.com/templates).
</Info>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/fleet/templates.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Tool integrations
Source: https://docs.langchain.com/langsmith/fleet/tools

Give your agents access to a wide range of tools and services.

You can access a variety of tools in LangSmith Fleet. Use tool integrations and [MCP servers](/langsmith/fleet/remote-mcp-servers) to give your agents access to email, calendars, chat, project management, code hosting, spreadsheets/BI, search, social, and general web utilities.

## Add a tool

You can add a tool from the [Fleet > Integrations tab](https://smith.langchain.com/agents/tools) to make it available to all agents in the workspace or from the agent editor to add it to a specific agent.

<Tabs>
  <Tab title="From Fleet > Integrations">
    To add a tool to all agents in the workspace:

    1. On the [Fleet > Integrations tab](https://smith.langchain.com/agents/tools), find the tool you want to add.
    2. Click the **Connect**.
    3. Follow the prompts to connect the tool to your agent.
  </Tab>

  <Tab title="From the agent editor">
    To add a tool to a specific agent:

    1. In [Fleet](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-fleet-tools), select the agent to which you want to add the tool.
    2. In the graph view, navigate to the **Toolbox** section and click **+ Add**.
    3. Select the tool you want to add.
    4. Click **Save Changes**.
  </Tab>
</Tabs>

## Disconnect a tool

To remove a tool from your agent:

<Steps>
  <Step title="Select the agent">
    In [Fleet](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-fleet-tools), select the agent from which you want to remove the tool.
  </Step>

  <Step title="Remove the tool">
    1. In the graph view, navigate to the **Toolbox** section and find the tool you want to remove.
    2. Click the <Icon icon="trash" /> **Remove** icon for the tool.
    3. Click **Save Changes**.
  </Step>
</Steps>

## Built-in tools

The following tools are a subset of the tools available in LangSmith Fleet. For the full up-to-date list, visit the [Fleet > Integrations tab](https://smith.langchain.com/agents/tools).

<CardGroup>
  <Card title="Gmail" icon="brand-google">
    Read, compose, and organize emails in your Gmail inbox.
  </Card>

  <Card title="Google BigQuery" icon="brand-google">
    Run queries and analyze large datasets stored in Google BigQuery.
  </Card>

  <Card title="Google Calendar" icon="brand-google">
    View, create, and manage calendar events and meeting schedules.
  </Card>

  <Card title="Google Docs" icon="brand-google">
    Create, read, and edit documents in Google Docs.
  </Card>

  <Card title="Google Sheets" icon="brand-google">
    Read, update, and analyze data in Google Sheets spreadsheets.
  </Card>
</CardGroup>

<CardGroup>
  <Card title="Excel" icon="brand-windows">
    Read, write, and analyze data in Microsoft Excel workbooks.
  </Card>

  <Card title="Outlook" icon="brand-windows">
    Read, draft, and organize Outlook emails, meetings, and calendar events.
  </Card>

  <Card title="PowerPoint" icon="brand-windows">
    Search, read, and create Microsoft PowerPoint presentations.
  </Card>

  <Card title="SharePoint" icon="brand-windows">
    Browse, read, and manage documents and sites in Microsoft SharePoint.
  </Card>

  <Card title="Teams" icon="brand-windows">
    Send and read messages, channels, and collaboration updates in Microsoft Teams.
  </Card>

  <Card title="Word" icon="brand-windows">
    Search, read, and manage Microsoft Word documents.
  </Card>
</CardGroup>

<CardGroup>
  <Card title="Exa" icon="search">
    Search the web using AI-powered semantic search for highly relevant results.
  </Card>

  <Card title="GitHub" icon="brand-github">
    Browse repositories, manage issues and pull requests, and review code on GitHub.
  </Card>

  <Card title="Linear" icon="list-check">
    Track issues, plan sprints, and coordinate team projects in Linear.
  </Card>

  <Card title="LinkedIn" icon="brand-linkedin">
    Create posts, manage your company page, and engage with your professional network.
  </Card>

  <Card title="Pylon" icon="messages">
    View and respond to customer support conversations across channels.
  </Card>

  <Card title="Slack" icon="brand-slack">
    Send messages, manage channels, and automate notifications in Slack.
  </Card>

  <Card title="Tavily" icon="world-search">
    Search the web and extract structured content from web pages.
  </Card>

  <Card title="X" icon="brand-x">
    Publish posts, monitor mentions, and engage with your audience on X.
  </Card>
</CardGroup>

<Tip>
  You can also connect to remote MCP servers to give your agents access to additional tools. See [Remote MCP servers](/langsmith/fleet/remote-mcp-servers) for more information.
</Tip>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/fleet/tools.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Fleet webhooks
Source: https://docs.langchain.com/langsmith/fleet/webhooks

Integrate agent publishing with external systems, CI/CD pipelines, or custom deployment workflows.

When triggered, a webhook sends a complete package of your agent's configuration and files to the specified endpoint.

<Callout icon="lock">
  **Security notes:**

  * Webhook URLs must use HTTPS.
  * Custom headers (e.g., API keys) are stored encrypted.
  * Publisher identity is included for audit trails.
  * Webhooks are only visible to agent owners.
</Callout>

## Add a webhook

1. Navigate to [Settings > Fleet webhooks](https://smith.langchain.com/settings/workspaces/agent-builder-webhooks).
2. Click **Add webhook**.
3. Configure:
   * **Name**: A descriptive name (e.g., "Publish Agent", "Deploy to Production").
   * **URL**: Your HTTPS endpoint that will receive the webhook.
   * **Headers** (optional): Custom headers for authentication (stored encrypted).
   * **Form Schema** (optional): Define custom input fields users must fill when triggering.
4. Click **Save**.

## Trigger a webhook

1. Open your agent in the Fleet editor.
2. Click the **Settings** menu (gear icon).
3. Under **Webhooks**, click the webhook name.
4. Fill in any custom fields defined in the form schema.
5. Click **Run Webhook**.

## Edit a webhook

1. Navigate to [Settings > Fleet webhooks](https://smith.langchain.com/settings/workspaces/agent-builder-webhooks).
2. For the webhook you want to edit, click **Edit**.
3. Make your changes and click **Save**.

## Delete a webhook

1. Navigate to [Settings > Fleet webhooks](https://smith.langchain.com/settings/workspaces/agent-builder-webhooks).
2. For the webhook you want to delete, click **Delete**.
3. To confirm the deletion, click **Delete**.

## Webhook payload

The webhook payload is a JSON object with the following fields:

| Field                                               | Description                                                        |
| --------------------------------------------------- | ------------------------------------------------------------------ |
| `action`                                            | The name of the webhook.                                           |
| `input`                                             | Values from custom form fields (empty object if no custom fields). |
| `publisher`                                         | User ID and email of the person triggering the webhook.            |
| `agent`                                             | Agent name and description.                                        |
| [`tool_auth_requirements`](#tool-auth-requirements) | Authentication requirements for each tool the agent uses.          |
| [`files`](#zip-file-structure)                      | Base64-encoded ZIP containing all agent files.                     |
| [`fields`](#custom-input-fields)                    | Custom input fields.                                               |

For example:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "action": "Webhook Name",
  "input": {
    "notes": "User-provided value",
    "environment": "prod",
    "dry_run": true
  },
  "publisher": {
    "user_id": "uuid-of-publishing-user",
    "email": "user@example.com"
  },
  "agent": {
    "name": "My Agent",
    "description": "Agent description text"
  },
  "tool_auth_requirements": [
    {
      "tool_name": "tavily_web_search",
      "auth_type": "api_key",
      "required_env_vars": ["TAVILY_API_KEY"]
    },
    {
      "tool_name": "google_calendar",
      "auth_type": "oauth",
      "auth_provider": "google",
      "scopes": ["calendar.readonly"]
    }
  ],
  "files": {
    "type": "zip",
    "filename": "My_Agent.zip",
    "content_base64": "<base64-encoded-zip>"
  },
  "fields": [
    {
      "name": "notes",
      "label": "Deployment Notes",
      "type": "textarea"
    }
  ]
}
```

### Tool auth requirements

The `tool_auth_requirements` array describes authentication needed for each tool:

| Auth Type | Fields                    | Description                                      |
| --------- | ------------------------- | ------------------------------------------------ |
| `none`    | -                         | Tool requires no authentication                  |
| `api_key` | `required_env_vars`       | Tool needs API key(s) in environment variables   |
| `oauth`   | `auth_provider`, `scopes` | Tool requires OAuth tokens with specified scopes |

Use this information to configure your deployment environment with the necessary credentials.

### ZIP file structure

The `files.content_base64` field contains a ZIP archive with the following structure:

```
.
├── AGENTS.md           # Agent system prompt and instructions
├── config.json         # Agent metadata (name, description, visibility)
├── tools.json          # Tool configurations and interrupt settings
├── skills/             # Optional skill definitions
│   └── skill-name/
│       └── SKILL.md
└── subagents/          # Optional subagent configurations
    └── research_worker/
        ├── AGENTS.md
        └── tools.json
```

The `config.json` file and `tools.json` files are structured as follows:

<Tabs>
  <Tab title="`config.json`">
    ```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    {
      "name": "My Agent",
      "description": "Agent description",
      "visibility_scope": "tenant",
      "triggers_paused": false
    }
    ```
  </Tab>

  <Tab title="`tools.json`">
    ```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    {
      "tools": [
        {
          "name": "tavily_web_search",
          "mcp_server_url": "http://localhost:8084",
          "mcp_server_name": "Fleet",
          "display_name": "tavily_web_search"
        }
      ],
      "interrupt_config": {
        "http://localhost:8084::tavily_web_search::Fleet": false
      }
    }
    ```
  </Tab>
</Tabs>

### Custom input fields

You can define custom input fields to collect information when the webhook is triggered. Supported field types are as follows:

| Type       | Description                       |
| ---------- | --------------------------------- |
| `string`   | Single-line text input (default). |
| `number`   | Numeric input.                    |
| `boolean`  | Checkbox (true/false).            |
| `textarea` | Multi-line text input.            |
| `json`     | JSON editor.                      |
| `select`   | Dropdown with predefined options. |

For example:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "fields": [
    {
      "name": "notes",
      "label": "Deployment Notes",
      "type": "textarea"
    },
    {
      "name": "environment",
      "label": "Environment",
      "type": "select",
      "options": [
        { "label": "Development", "value": "dev" },
        { "label": "Staging", "value": "staging" },
        { "label": "Production", "value": "prod" }
      ]
    },
    {
      "name": "dry_run",
      "label": "Dry Run",
      "type": "boolean",
      "default": true
    }
  ]
}
```

## Example: Webhook server

The following is an example webhook server in Python:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import base64
import zipfile
import io

class WebhookHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = json.loads(self.rfile.read(content_length))

        action = body.get("action")
        input_data = body.get("input", {})
        publisher = body.get("publisher", {})
        agent = body.get("agent", {})
        tool_auth = body.get("tool_auth_requirements", [])
        files = body.get("files", {})

        print(f"Webhook: {action}")
        print(f"Publisher: {publisher.get('email')}")
        print(f"Agent: {agent.get('name')}")
        print(f"Custom Input: {input_data}")

        # Extract ZIP contents
        if files.get("content_base64"):
            zip_bytes = base64.b64decode(files["content_base64"])
            with zipfile.ZipFile(io.BytesIO(zip_bytes)) as zf:
                print(f"Files: {zf.namelist()}")

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({"status": "ok"}).encode())

HTTPServer(("", 8000), WebhookHandler).serve_forever()
```

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/fleet/webhooks.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Manage workspace administration
Source: https://docs.langchain.com/langsmith/fleet/workspace-admin

Configure workspace-level settings for Fleet.

Configure workspace secrets and manage spend limits for Fleet agents and users.

## Workspace secrets

Fleet uses [workspace secrets](/langsmith/set-up-hierarchy#configure-workspace-settings) to store API keys for models and tools. The following secret types are available:

* **Required model key**: An OpenAI or Anthropic API key is required for Fleet to make LLM API calls. The agent graphs load this key from workspace secrets for inference.
* **Fleet-specific secrets**: Secrets prefixed with `FLEET_` are prioritized over workspace secrets within Fleet. This way, you can better track the usage of Fleet vs other parts of LangSmith that use the same secrets. If you have both `OPENAI_API_KEY` and `FLEET_OPENAI_API_KEY`, the `FLEET_OPENAI_API_KEY` secret will be used.
* **Optional tool keys**: Add keys for any tools you enable. These are read from workspace secrets at runtime.
  * `EXA_API_KEY`: Required for Exa search tools (general web and LinkedIn profile search).
  * `TAVILY_API_KEY`: Required for Tavily web search.
  * `TWITTER_API_KEY` and `TWITTER_API_KEY_SECRET`: Required for Twitter/X read operations (app-only bearer). Posting/media upload is not enabled.
* **MCP server configuration**: Fleet can pull tools from one or more remote [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) servers. Configure MCP servers and headers in your [workspace](/langsmith/administration-overview#workspaces) settings. Fleet automatically discovers tools and applies the configured headers when calling them. For more information, refer to the [Remote MCP servers](/langsmith/fleet/remote-mcp-servers) page.

<Note icon="wand">
  Fleet supports custom models per agent. See [Custom models](/langsmith/fleet/essentials#custom-models) for more information.
</Note>

### Add a secret

To add a secret:

1. In the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-fleet-workspace-admin), navigate to <Icon icon="settings" /> **Settings** and then move to the **Secrets** tab.

2. Select **Add secret** and enter the secret **name** (for example, `OPENAI_API_KEY` or `ANTHROPIC_API_KEY`) and your key as the **value**.

   <Note>
     Ensure that the secret keys match the environment variable names expected by your model provider.
   </Note>

3. Select **Save secret**.

## Usage and spend limits

The **Usage** page gives workspace admins visibility into Fleet spend and the ability to set spend limits for agents and users. This page will only be visible to users with the `fleet:read-admin-config` permission.

### View current spend

The **Usage** page shows your workspace's total spend over a selected time period (**Last 7 days** or **Last 14 days**), along with total threads and total runs.

A daily spend chart provides a visual breakdown of costs over the selected period. The **Breakdown** section lets you view spend details in two ways:

* **By agent**: See each agent's total cost, number of runs, first and last used dates, owner, and weekly limit.
* **By user**: See each user's spend and activity.

### Set spend limits

Spend limits let you control how much agents and users can spend. Managing spend limits requires the `fleet:write-admin-config` permission.

#### Default weekly spend limits

In the **Default Weekly Spend Limits** section, you can configure:

* **Per-Agent Default Limit (USD)**: Set a default weekly spend limit that applies to all agents in the workspace.
* **Per-User Default Limit (USD)**: Set a default weekly spend limit that applies to all users in the workspace.

Limits are week-to-date and reset on Mondays.

#### Override limits for individual agents and users

You can override the default spend limit for individual agents or users to set a custom weekly limit.

#### Spend limit behavior

* Changes to spend limits may take a few minutes to propagate across all running agents.
* Spend limits are checked at the start of each run. If a run begins while usage is under the limit, it will be allowed to complete even if the final cost exceeds the limit.
* Spend calculations are based on traces. Deleting traces will affect reported usage and spend enforcement.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/fleet/workspace-admin.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
