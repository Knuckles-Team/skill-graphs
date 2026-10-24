# Read SKILL.md from disk once; middleware injects into state on first turn.
_SKILL_LOADER = StaticSkillsLoader(
    [
        (FLEET_DIR / "skills", "/skills/fleet"),
        (CUSTOM_SKILLS_DIR, "/skills/custom"),
    ]
)

async def graph(runtime: Any):
    """Build and return the agent graph."""
    components = await load_agent_components(FLEET_DIR)
    model = components.pop("model")  # from fleet/config.json; replace to override
    components["tools"] = list(components["tools"]) + list(custom_tools)

    if _SKILL_LOADER.files:
        components["skills"] = _SKILL_LOADER.skill_paths

    return create_deep_agent(
        model=model,
        middleware=[_SKILL_LOADER, *custom_middleware],
        **components,
    ).with_config({"recursion_limit": 1000})
```

### Re-exporting

When you export a new version of your agent from Fleet, simply wipe and re-unzip — your customizations are untouched:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
rm -rf fleet && unzip path/to/my-new-export.zip -d fleet/
```

### Supported model providers

The starter ships with `langchain-anthropic`, `langchain-openai`, and `langchain-google-genai`. For any other provider (e.g. `bedrock`, `fireworks`), add the matching `langchain-<provider>` package to `pyproject.toml`.

### MCP authentication

At startup, each tool's `mcp_server_url` is resolved against LangSmith's MCP server registry:

* **Built-in LangSmith tools** (Gmail, Calendar, GitHub) — authenticated via your `LANGSMITH_API_KEY`.
* **Static-credential servers** (`auth_type: "headers"`) — credentials come from the registry record. Requires `mcp-servers:invoke` permission.
* **OAuth servers** (`auth_type: "oauth"`) — bearer token fetched from LangSmith's OAuth broker. A browser window opens on first run for any per-user server that hasn't been authorized yet.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/fleet/code.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Agent platform comparison
Source: https://docs.langchain.com/langsmith/fleet/comparison

Compare LangSmith Fleet with Claude Cowork, Amazon Quick, Google Workspace Studio, and Microsoft Copilot to choose the right enterprise agent platform for your team

[**LangSmith Fleet**](/langsmith/fleet/index) is an enterprise agent platform for building, sharing, and governing agents across your organization. This page compares it with similar platforms to help you choose the right one for your team.

<div>
  | **Platform**                              | **Choose if...**                                                                                                                                                                                                                                                                                        |
  | ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | [LangSmith Fleet](/langsmith/fleet/index) | You want to build and share purpose-built agents across your organization, stay model-agnostic, and keep full observability via LangSmith. **Fleet** is the only option with a self-hosted deployment path and the ability to export agents to code via [Deep Agents](/oss/python/deepagents/overview). |
  | Claude Cowork                             | You want to delegate open-ended tasks to Claude from the desktop for personal knowledge work, and on-device data storage meets your privacy requirements.                                                                                                                                               |
  | Amazon Quick                              | You are already on AWS and want an AI assistant with direct access to your AWS data sources and enterprise integrations.                                                                                                                                                                                |
  | Google Workspace Studio                   | Your organization runs on Google Workspace and you want no-code agents that work natively inside Gmail, Drive, and Sheets without leaving the Google ecosystem.                                                                                                                                         |
  | Microsoft Copilot                         | Your organization runs on Microsoft 365 and you want low-code agents (via Copilot Studio) that publish natively to Teams and Microsoft 365 Copilot, governed through the Power Platform admin center.                                                                                                   |
</div>

## Compare capabilities

* ❌ Not available
* ⚠️ Partial or limited
* — Not confirmed from public documentation

<div>
  | **Aspect**              | **LangSmith Fleet**                                                                                                                                                                            | **Claude Cowork**                           | **Amazon Quick**                               | **Google Workspace Studio**         | **Microsoft Copilot**                                                  |
  | ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- | ---------------------------------------------- | ----------------------------------- | ---------------------------------------------------------------------- |
  | **Primary use case**    | Teams building purpose-built agents to share across an organization, with no-code creation and code export for custom deployments; individuals using a general-purpose chat agent for any task | Individual desktop knowledge work           | Enterprise AI with AWS data integration        | No-code agents for Google Workspace | Low-code agents for Microsoft 365                                      |
  | **Model support**       | Model-agnostic: any LLM with an OpenAI-compatible or Anthropic-compatible API                                                                                                                  | Claude only                                 | —                                              | Gemini 3                            | Curated OpenAI + Anthropic models; bring-your-own via Azure AI Foundry |
  | **Interface**           | Web app, Slack app, Teams app, API                                                                                                                                                             | Desktop, mobile, Slack, M365 connectors     | Web, desktop, browser extensions, Slack, Teams | Web app, Gmail and Chat sidebars    | Teams, M365 apps, web, mobile, Windows, Copilot Studio                 |
  | **Deployment**          | Cloud (LangSmith) or self-hosted                                                                                                                                                               | Local by default; remote on Anthropic cloud | Cloud (AWS)                                    | Cloud (Google)                      | Cloud (Microsoft)                                                      |
  | **Self-hosting**        | ✅ [Beta](/langsmith/deploy-self-hosted-full-platform#enable-fleet-insights-and-chat), [contact sales](https://www.langchain.com/contact-sales) for production readiness details                | ❌                                           | ❌                                              | ❌                                   | ❌                                                                      |
  | **Code export**         | ✅ [Export to Deep Agents](/langsmith/fleet/code)                                                                                                                                               | ❌                                           | ❌                                              | ❌                                   | ❌                                                                      |
  | **Observability**       | LangSmith tracing and evaluations at scale                                                                                                                                                     | OpenTelemetry to SIEM                       | CloudTrail + run logs                          | Activity tab + audit logs           | App Insights + Purview                                                 |
  | **Platform license**    | Proprietary                                                                                                                                                                                    | Proprietary                                 | Proprietary                                    | Proprietary                         | Proprietary                                                            |
  | **Code export license** | MIT ([Deep Agents](/oss/python/deepagents/overview))                                                                                                                                           | N/A                                         | N/A                                            | N/A                                 | N/A                                                                    |
</div>

### Target users

**Fleet** covers both org-wide and personal use cases. Teams can build purpose-built agents to share across an organization (for example, a vendor intake agent that serves an entire ops org, or a weekly report agent that saves every account manager thirty minutes on Monday morning), and any user can get help with any task using any tool via Fleet's general-purpose default chat. Other platforms focus on individual productivity, ecosystem-specific automation, or both, but none combine no-code agent building with org-wide sharing and code export.

**Fleet** also lets you set tool-level approval requirements so agents check with you before executing sensitive steps, with a [centralized inbox](https://smith.langchain.com/agents/inbox) for reviewing, editing, and approving actions. No other platform in this comparison offers a single centralized approvals inbox spanning all agents.

<div>
  | Feature                     | **Fleet**                                                                                                                                                 | **Claude Cowork** | **Amazon Quick** | **Google Workspace Studio** | **Microsoft Copilot**       |
  | --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | ---------------- | --------------------------- | --------------------------- |
  | General-purpose chat agent  | ✅ [Fleet chat](https://smith.langchain.com/agents?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-fleet-comparison) | ✅                 | ✅                | ❌                           | ✅                           |
  | No-code agent builder       | ✅                                                                                                                                                         | ❌                 | ✅                | ✅                           | ✅                           |
  | Slack-native integration    | ✅ [Native Slack app](/langsmith/fleet/slack-app)                                                                                                          | ✅                 | ✅                | ⚠️                          | ⚠️  (via Azure Bot Service) |
  | Microsoft Teams integration | ✅ [Teams app](/langsmith/fleet/teams-app)                                                                                                                 | ✅                 | ✅                | ❌                           | ✅                           |
  | Scheduled runs              | ✅ [Schedules](/langsmith/fleet/schedules)                                                                                                                 | ✅                 | ✅                | ✅                           | ✅                           |
  | Sub-agents                  | ✅ [Sub-agents](/langsmith/fleet/essentials#sub-agents)                                                                                                    | ✅                 | ✅                | ❌                           | ✅                           |
  | Skills system               | ✅ [Skills](/langsmith/fleet/skills)                                                                                                                       | ✅                 | ❌                | ❌                           | —                           |
  | Human-in-the-loop           | ✅ [Central approvals inbox](/langsmith/fleet/essentials#human-in-the-loop)                                                                                | ✅                 | ✅                | ⚠️                          | ⚠️                          |
  | MCP client                  | ✅ [Remote MCP servers](/langsmith/fleet/remote-mcp-servers)                                                                                               | ✅                 | ✅                | ❌                           | ✅                           |
  | Web search                  | ✅ (via Exa, Tavily)                                                                                                                                       | ✅                 | ✅                | ✅                           | ✅                           |
</div>

### Enterprise controls and access

**Fleet** provides RBAC, attribute-based access control, and per-agent sharing permissions (Clone, Run, and Edit). Among the platforms compared here, only Fleet documents per-MCP-server attribute-based access control. All platforms offer some form of RBAC, but granularity varies.

**Fleet** manages spending at the workspace level. For enterprise billing options, [contact sales](https://www.langchain.com/contact-sales).

<div>
  | Feature                              | **Fleet**                                                                                                | **Claude Cowork** | **Amazon Quick** | **Google Workspace Studio** | **Microsoft Copilot** |
  | ------------------------------------ | -------------------------------------------------------------------------------------------------------- | ----------------- | ---------------- | --------------------------- | --------------------- |
  | Role-based access control            | ✅ [RBAC with per-tool permissions](/langsmith/rbac)                                                      | ✅                 | ✅                | ✅                           | ✅                     |
  | Attribute-based access control       | ✅ [Per MCP server and integration](/langsmith/fleet/access-and-oversight#attribute-based-access-control) | ❌                 | ❌                | ❌                           | —                     |
  | Per-agent sharing and permissions    | ✅ [Clone, Run, and Edit access per agent](/langsmith/fleet/access-and-oversight#permissions-and-sharing) | ⚠️                | ✅                | ⚠️                          | ✅                     |
  | Credential model (fixed or per-user) | ✅ [Configurable per agent](/langsmith/fleet/access-and-oversight#agent-identity-and-credentials)         | ✅                 | ✅                | ✅                           | ✅                     |
  | Spend limits                         | ⚠️ Managed at workspace level                                                                            | ✅                 | ⚠️               | ⚠️                          | ✅                     |
  | SCIM provisioning                    | ✅                                                                                                        | ✅                 | ✅                | —                           | ✅                     |
  | Audit trail                          | ✅ [Structured LangSmith traces](/langsmith/fleet/access-and-oversight#observability-and-audit-trail)     | ✅                 | ✅                | ✅                           | ✅                     |
</div>

### Model flexibility

**Fleet** supports any LLM via the OpenAI or Anthropic chat spec, including self-hosted providers, with no ecosystem dependency. Microsoft Copilot offers curated multi-vendor models and a bring-your-own path via Azure AI Foundry, but full flexibility requires Azure infrastructure. Google Workspace Studio and Amazon Quick are more constrained to their respective vendor ecosystems.

Of the platforms compared here, only Fleet works with any OpenAI- or Anthropic-compatible API endpoint regardless of cloud provider.

### Memory, self-updates, and learning

**Fleet** agents can persist context across conversations using a dedicated memory system, and can update their own instructions, add tools, or remove tools as they learn from interactions. Of the platforms compared here, only Fleet documents agent self-modification at runtime.

<div>
  | Feature                         | **Fleet**                                                                                                           | **Claude Cowork** | **Amazon Quick** | **Google Workspace Studio** | **Microsoft Copilot** |
  | ------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ----------------- | ---------------- | --------------------------- | --------------------- |
  | Long-term memory                | ✅ [Persistent memory files across sessions](/langsmith/fleet/essentials#memory)                                     | ✅                 | ✅                | ❌                           | —                     |
  | Thread-scoped context           | ✅                                                                                                                   | ✅                 | ✅                | ✅                           | ✅                     |
  | Self-updating agents            | ✅ [Agents can add tools, remove tools, and update their own instructions](/langsmith/fleet/essentials#self-updates) | ❌                 | ❌                | ❌                           | ❌                     |
  | Approval gate for memory writes | ✅ [Configurable per agent](/langsmith/fleet/manage-agent-settings)                                                  | ❌                 | ❌                | ❌                           | —                     |
</div>

### Observability and governance

**Fleet's** clearest advantage is its native connection to LangSmith. Every agent run is traced in LangSmith, making it easy to debug performance and run evaluations at scale. Other platforms offer basic logging and audit trails, but none match Fleet's depth of LLM-aware tracing, evaluations, and debugging through a dedicated observability platform.

<div>
  | Feature        | **Fleet**                                                    | **Claude Cowork** | **Amazon Quick** | **Google Workspace Studio** | **Microsoft Copilot** |
  | -------------- | ------------------------------------------------------------ | ----------------- | ---------------- | --------------------------- | --------------------- |
  | Native tracing | ✅ [LangSmith traces for every run](/langsmith/observability) | ✅                 | ⚠️               | ⚠️                          | ⚠️                    |
  | Evaluations    | ✅ [LangSmith evaluations](/langsmith/evaluation-concepts)    | ❌                 | ❌                | ❌                           | ⚠️                    |
</div>

### Code export and hosting

**Fleet** lets you export any agent you build to code via [Deep Agents](/oss/python/deepagents/overview), the open-source agent runtime that Fleet runs on. Exported agents are MIT-licensed and can be deployed independently of Fleet, modified in code, or integrated directly into your own applications via the [API](/langsmith/fleet/code). None of the other platforms in this comparison offer a code export path.

**Fleet** is the only platform in this comparison with a self-hosted deployment option. For teams with compliance requirements, self-hosted and BYOC (bring your own cloud) configurations let you run Fleet entirely within your own infrastructure. All other platforms are cloud-only managed services.

<div>
  | Feature                   | **Fleet**                                                                                                                                                                       | **Claude Cowork** | **Amazon Quick** | **Google Workspace Studio** | **Microsoft Copilot** |
  | ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | ---------------- | --------------------------- | --------------------- |
  | Cloud-hosted              | ✅                                                                                                                                                                               | ⚠️                | ✅                | ✅                           | ✅                     |
  | Self-hosted               | ✅ [Beta](/langsmith/deploy-self-hosted-full-platform#enable-fleet-insights-and-chat), [contact sales](https://www.langchain.com/contact-sales) for production readiness details | ❌                 | ❌                | ❌                           | ❌                     |
  | Custom models             | ✅ [Any OpenAI- or Anthropic-compatible API](/langsmith/fleet/essentials#custom-models)                                                                                          | ❌                 | ❌                | ⚠️                          | ⚠️                    |
  | Call agents from your app | ✅ [API access](/langsmith/fleet/code)                                                                                                                                           | ✅                 | ⚠️               | ❌                           | ✅                     |
  | Export to code            | ✅ [Export to Deep Agents](/langsmith/fleet/code)                                                                                                                                | ❌                 | ❌                | ❌                           | ❌                     |
</div>

### Integrations and tools

A ✅ indicates the integration is available; supported actions and depth vary by platform. See [Fleet tool integrations](/langsmith/fleet/tools) for the full list of Fleet's built-in integrations and what each one can do.

<div>
  | Feature                                           | **Fleet**                               | **Claude Cowork** | **Amazon Quick** | **Google Workspace Studio** | **Microsoft Copilot** |
  | ------------------------------------------------- | --------------------------------------- | ----------------- | ---------------- | --------------------------- | --------------------- |
  | Google Workspace (Gmail, Drive, Sheets, Docs)     | ✅                                       | ✅                 | ⚠️               | ✅                           | ⚠️                    |
  | Microsoft 365 (Outlook, Teams, SharePoint, Excel) | ✅                                       | ✅                 | ✅                | ❌                           | ✅                     |
  | GitHub                                            | ✅                                       | ✅                 | ✅                | —                           | —                     |
  | Slack                                             | ✅ [Native](/langsmith/fleet/slack-app)  | ✅                 | ✅                | ⚠️                          | ❌                     |
  | CRM (Salesforce, HubSpot)                         | ✅                                       | —                 | ✅                | ⚠️                          | ✅                     |
  | Project management (Linear, Jira, Notion)         | ✅                                       | ✅                 | ✅                | ⚠️                          | ⚠️                    |
  | Custom tools via MCP                              | ✅                                       | ✅                 | ✅                | ❌                           | ✅                     |
  | Webhooks                                          | ✅ [Webhooks](/langsmith/fleet/webhooks) | ❌                 | ❌                | ⚠️                          | ✅                     |
</div>

For pricing and SLA information, [contact sales](https://www.langchain.com/contact-sales).

<Note>
  Last updated May 5, 2026. These products evolve quickly. If something has changed, please [file an issue](https://github.com/langchain-ai/docs/issues) to help us keep this page current.
</Note>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/fleet/comparison.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Computer use
Source: https://docs.langchain.com/langsmith/fleet/computer-use

Run code, manage files, and call authenticated APIs from a persistent virtual computer attached to your Fleet agent.

Computer use gives your Fleet agent access to an isolated virtual computer. The agent can write and execute code, manage files, install packages, and call authenticated external APIs without exposing credentials to the language model.

<Note>
  Computer use is available on the [Plus and Enterprise plans](https://langchain.com/pricing).
</Note>

## Computer modes

Choose how the virtual computer is shared across an agent's conversation threads:

| Mode                    | Description                                                                                                                                                                                                                                                                         |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Shared computer**     | All threads share a single computer. The filesystem, installed packages, and running processes persist across threads. Choose this mode when you want files, dependencies, or environment setup to accumulate across conversations. Shared computers are not deleted automatically. |
| **Computer per thread** | Each thread gets its own isolated computer that starts fresh and is archived when it goes idle. Choose this mode for software-engineering agents and other workloads that run many parallel, write-heavy tasks, or for any case where threads should not see each other's state.    |

## Configure computer use

<Warning>
  The computer mode is set when the agent is created and cannot be changed afterward. To switch modes, create a new agent.
</Warning>

<Steps>
  <Step title="Open the Create agent dialog">
    In the [Fleet](https://smith.langchain.com/agents?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-fleet-computer-use) left navigation, under **My Agents**, click <Icon icon="plus" /> and select either **Create with AI** or **Blank agent**. Enter a name for your agent.
  </Step>

  <Step title="Enable computer use">
    Under **Should your agent use a computer?**, select **Yes**, then choose **Shared computer** or **Computer per thread**. If you select **No** (the default), the agent is created with no computer access.
  </Step>

  <Step title="Set the base snapshot (optional)">
    Expand **Advanced** to choose a **Snapshot** for new computers.
  </Step>

  <Step title="Create the agent">
    Click **Create Agent**.
  </Step>
</Steps>

## Access profiles

Use access profiles to let your agent call authenticated external APIs without putting credentials in the prompt or exposing them to the language model. Outbound HTTP requests to matching hosts are routed through a proxy that injects the configured headers before forwarding.

A profile contains one or more **Custom rules**. Each rule specifies:

* **Match Hosts**: The target hostnames the rule applies to. Use `*` as a wildcard (for example, `*.example.com` matches `api.example.com`).
* **Source Type and Provider**: The credential source. Choose **Connection** for user-delegated OAuth, or **Workspace Secret** for static API keys.
* **Inject Headers**: The HTTP headers the proxy adds to matched requests. Use template values such as `{access_token}` to reference the credential (for example, `Authorization: Bearer {access_token}`).

A profile also has a **Network scope** that controls outbound traffic for the agent's computer. The default is **None (all traffic allowed)**.

### Add an access profile

<Steps>
  <Step title="Create the access profile">
    Go to the [Fleet Integrations tab](https://smith.langchain.com/agents/tools) and navigate to the **Computer** section. Click **+ Create profile** and follow the prompts to configure the host patterns and credentials.
  </Step>

  <Step title="Attach the profile to an agent">
    In the agent editor, click the **Computer** node. Click **+ Add** next to **Access profiles** and select the profile you created.
  </Step>

  <Step title="Save changes">
    Click **Save changes**.
  </Step>
</Steps>

## Computer lifecycle

Each agent has two lifecycle settings that control how long a computer stays active and how long it is kept after it stops. [Configure both in the settings popover](#configure-lifecycle-and-snapshot).

* **Idle timeout**: When the computer has not received any commands for this duration, it pauses and the disk is archived. The agent can resume the same computer later without losing data. Default: **15 minutes**.
* **Stopped computer cleanup**: After a computer has been stopped for this duration, it is permanently deleted along with all disk data. Default: **14 days**.

<Note>
  **Stopped computer cleanup** applies only to **Computer per thread** mode. Shared computers are not deleted automatically.
</Note>

## Base snapshot

A snapshot is the disk image used to boot the computer. By default, all Fleet agents use the workspace default snapshot. To build, capture, or configure custom snapshots, see [Sandbox snapshots](/langsmith/sandbox-snapshots). [Change the snapshot for an agent](#configure-lifecycle-and-snapshot) in the settings popover.

<Note>
  Snapshot changes apply only to new computers for the agent. The single shared computer in **Shared computer** mode keeps its original snapshot for its lifetime.
</Note>

## Configure lifecycle and snapshot

The snapshot, idle timeout, and stopped computer cleanup for an agent are all set in the **Computer lifecycle** section of the settings popover.

<Steps>
  <Step title="Open the settings popover">
    In [Fleet](https://smith.langchain.com/agents?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-fleet-computer-use), open the agent and click the <Icon icon="settings" /> settings icon in the agent editor.
  </Step>

  <Step title="Set the lifecycle fields">
    Scroll to the **Computer lifecycle** section. Set the **Snapshot**, **Idle timeout**, and, for **Computer per thread** mode, **Stopped computer cleanup**.
  </Step>

  <Step title="Save changes">
    Click **Save changes**.
  </Step>
</Steps>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/fleet/computer-use.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Essentials
Source: https://docs.langchain.com/langsmith/fleet/essentials

Fleet's core features

LangSmith Fleet essentials are the core features that make up the foundation of your agents. They include tools, channels, memory, sub-agents, and approvals.

## Agent identity

Agent identity controls whose [credentials](/langsmith/fleet/workspace-admin) the agent uses when it interacts with apps and services.

See [Agent identity](/langsmith/fleet/agent-identity) for more information.

## Channels

<Anchor />

Channels define when your agent should start running. You can connect your agent to external tools or time-based schedules, letting it respond automatically to messages, emails, or recurring events.

See [Channels](/langsmith/fleet/channels) for setup instructions and supported channel types.

## Custom models

Fleet supports custom models. You can connect any LLM API that supports the **OpenAI chat completions spec** or **Anthropic chat spec**.

Common use cases include:

* **LLM proxies**: Route requests through services like LiteLLM, Portkey, or your own proxy.
* **Self-hosted models**: Connect to models running on your own infrastructure.
* **Alternative providers**: Use any provider with a compatible API.

To add a custom model:

1. In the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-fleet-essentials), navigate to the agent you want to edit.
2. Click on the <Icon icon="settings" /> settings icon in the top right corner.
3. In the **Model** section, select **+ Add custom model**.
4. Enter the model ID, display name, base URL, and API key name and value.
5. Click **Save**.

<Note>
  Custom models must be accessible through a public API endpoint. LangSmith cannot connect to models hosted on private networks, behind VPNs, or on machines that are not exposed to the internet.
</Note>

## Human-in-the-loop

Stay in control of important decisions. You can set up your agent to pause and ask for your approval before taking certain actions. This ensures your agent handles most tasks automatically, while you retain oversight.

### Setting up approval steps

<Steps>
  <Step title="Select a tool">
    When setting up your agent, choose the tool or action you want to review before it runs.
  </Step>

  <Step title="Turn on approval">
    Find the approval option for that tool and switch it on.
  </Step>

  <Step title="Agent waits for you">
    When your agent reaches that step, it will pause and wait for your approval before continuing.
  </Step>
</Steps>

### What you can do when your agent pauses

When your agent stops to ask for approval, you have three options:

<CardGroup>
  <Card title="Accept" icon="check">
    Give the green light and let your agent proceed with its plan.
  </Card>

  <Card title="Edit" icon="edit">
    Modify the agent's message or parameters before allowing it to continue.
  </Card>

  <Card title="Send feedback" icon="message">
    Share feedback to help your agent learn and improve.
  </Card>
</CardGroup>

## Instructions

Instructions are the system prompt that defines your agent's behavior, personality, and capabilities. They guide how the agent interprets requests, uses its tools, and responds to users.

To edit instructions:

1. In the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-fleet-essentials), navigate to the agent you want to edit.
2. Click <Icon icon="pencil" /> **Edit** in the top right corner.
3. In the **Instructions** panel, click <Icon icon="pencil" /> **Edit**.
4. Edit the instructions.
5. Click **Done** and then **Save changes**.

<Tip>
  You can also update instructions by prompting the agent directly in the chat. For example: "Update your instructions to always respond in bullet points."
</Tip>

## Memory

Agents remember important information from previous conversations and can update themselves to work better. Fleet agents use two sources of memory:

* **Thread-scoped memory**: Context from the current conversation thread, including messages and actions in that thread.
* **Long-term memory**: Persistent files in the agent workspace, such as `AGENTS.md`, `tools.json` (tool configuration), `subagents/*`, and `skills/*`. These are loaded at runtime and available from the start of each run. `AGENTS.md` is inserted into the system prompt automatically. Other long-term files are not added to the prompt automatically; the agent must read them on demand (for example, using the `read_file` tool).

Agents persist relevant details from past interactions by writing files to a **memories folder** (using `write_file` and `edit_file` tool calls). This helps them make better decisions in future conversations.

<Note>
  By default, agents require approval before saving to the memories folder. You can disable this in the agent's settings.

  For agents that run on automated [schedules](/langsmith/fleet/schedules#add-a-schedule), we recommend [disabling the approval requirement](/langsmith/fleet/manage-agent-settings#disable-required-approval-for-memory-updates) so the agent can persist information without manual intervention.
</Note>

For more information, see [How we built the memory system for Fleet (formerly known as Agent Builder)](https://www.langchain.com/conceptual-guides/how-we-built-agent-builders-memory).

## Self-updates

Agents can update themselves: they can add new tools, remove ones they don't need, or adjust their instructions. However, agents can't change their name, description, or the channels that start them.

## Skills

Skills are a way to bundle capabilities and provide more specific information in situations where the context is not universally relevant.

Using skills can help:

* Save on token usage by only providing the context that is relevant to the current task.
* Prevent the agent from having too much context in the system prompt, which can lead to hallucinations and incorrect responses.

For more information, see [Skills](/langsmith/fleet/skills).

## Sub-agents

Build complex agents by breaking big tasks into smaller, specialized helpers. Think of sub-agents as a team of specialists—each one handles a specific part of the job while working together with your main agent.

This approach makes it easier to build sophisticated systems. Instead of one agent trying to do everything, you can have specialized helpers that each excel at their part of the task.

Here are some ways you might use sub-agents:

* Split into sub-tasks: Have one agent fetch data, another summarize it, and a third format the results.
* Specialized tools: Give different agents access to different tools based on what they need to do.
* Independent work: Let sub-agents work on their own, then bring their results back to the main agent.

## Threads

Threads are conversations between you and your agent. Each thread contains messages, agent responses, and any actions the agent takes.

To view threads, navigate to your agent in the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-fleet-essentials). The inbox shows all threads for that agent. Click on a thread to view the conversation.

### Read and unread status

How threads are marked depends on whether the agent uses channels:

* **Chat agents (no channel):** Responses mark the thread as **unread**. Viewing the thread marks it as read.
* **Channel-based agents:** Responses keep the thread as **read** by default.

You can manually mark any thread as read or unread at any time.

## Tools

Tools let your agents interact with your apps and services. Your agents can send emails, create calendar events, post messages, search the web, and more. Choose from built-in tools for Gmail, Slack, Google Calendar, GitHub, and many others.

Tools work regardless of how the agent was triggered. For example, you can start a task in the Fleet chat UI and have the agent send you a [Slack message](/langsmith/fleet/slack-app#add-slack-tools) when it's done.

See [Tool integrations](/langsmith/fleet/tools) for more information.

## Traces

Traces are a series of steps that your agent takes to go from input to output. You can use [LangSmith](/langsmith/observability) to visualize these execution steps.

To view all traces for your agent:

1. In the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-fleet-essentials), navigate to your agent's inbox.
2. Next to the agent name, click the **View Agent Traces** icon.

To view a trace for a specific thread:

1. In the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-fleet-essentials), navigate to your agent's inbox.
2. Right-click on the thread you want to trace and select **View trace**.

For more information, see [LangSmith Observability](/langsmith/observability).

<Note>
  Fleet traces all agent runs and stores them in LangSmith. LLM providers do not retain your data. On LangSmith Cloud, trace data is stored with a 14-day retention period by default.
</Note>

## Next steps

* [Set up your workspace](/langsmith/fleet/workspace-admin)
* [Connect apps and services](/langsmith/fleet/tools)
* [Use remote servers for tools](/langsmith/fleet/remote-mcp-servers)
* [Choose between workspace and private agents](/langsmith/fleet/manage-agent-settings)
* [Call agents from your app](/langsmith/fleet/code)

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/fleet/essentials.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# No-code agents with LangSmith Fleet
Source: https://docs.langchain.com/langsmith/fleet/index

Create helpful AI agents without code. Start from a template, connect your accounts, and let the agent handle routine work while you stay in control.

<Callout icon="speakerphone">
  **Agent Builder is now LangSmith Fleet.** All existing agents, configurations, and integrations continue to work. No action is required.
</Callout>

LangSmith Fleet is a no-code platform for creating and managing AI agents. It allows you to create agents from templates, connect your accounts, and let the agent handle routine work while you stay in control.

Use Fleet to:

* Automate everyday tasks like drafting emails, summarizing updates, and organizing information.
* Connect your favorite apps to bring context into your agent's work.
* Use in chat or where you work (e.g., Slack) to get help in the flow.
* Stay in control with simple approvals for important actions.

## Start building

<CardGroup>
  <Card title="Create with a template" icon="layout-grid" href="/langsmith/fleet/quickstart">
    Pick a ready-made starter (e.g., email assistant or team updates) and customize.
  </Card>

  <Card title="Create with AI" icon="wand">
    Describe your goal in plain English and let AI draft your agent's configuration. Review and edit before running.
  </Card>
</CardGroup>

## Get started

<Steps>
  <Step title="Sign up" icon="login">
    Sign up for a [LangSmith account](https://smith.langchain.com/agents?skipOnboarding=true\&utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-fleet-index).
  </Step>

  <Step title="Create an agent" icon="circle-plus">
    Start from a ready-to-use template, or describe your goal and let AI draft your agent's instructions. You can edit details before running. [Browse templates](https://www.langchain.com/templates).
  </Step>

  <Step title="Connect your accounts" icon="link">
    Securely sign in to the services you want the agent to use.
  </Step>

  <Step title="Try it out" icon="rocket">
    Run the agent and iterate on its instructions in a few clicks.
  </Step>
</Steps>

## Privacy policy and disclaimers

The LangSmith Fleet App for Slack collects, manages, and stores third-party data in accordance with our privacy policy. For full details on how your data is handled, please see [our privacy policy](https://www.langchain.com/privacy-policy).

Fleet uses the following approach to AI:

* **Model**: Uses LLMs provided through the LangSmith platform
* **Data retention**: User data is retained according to LangSmith's data retention policies
* **Data tenancy**: Data is handled according to your LangSmith organization settings
* **Data residency**: Data residency follows your LangSmith configuration

<Warning>
  Disclaimers:

  * **AI-generated content**: All responses from agents are generated by AI and may contain errors or inaccuracies. Always verify important information.
  * **Data usage**: Slack data is not used to train LLMs. Your workspace data remains private and is only used to provide agent functionality.
  * **Transparency**: Fleet is transparent about the actions it will take once added to your workspace, as outlined in the permissions section above.
</Warning>

## Learn more

* [Essentials: connections, automation, memory, approvals](/langsmith/fleet/essentials)
* [Create from a template](/langsmith/fleet/templates)
* [Set up your workspace](/langsmith/fleet/workspace-admin)
* [Connect apps and services](/langsmith/fleet/tools) and [use remote connections](/langsmith/fleet/mcp-framework)
* [Choose between workspace and private agents](/langsmith/fleet/manage-agent-settings)
* [Authorize accounts when prompted](/langsmith/fleet/auth-format)
* [Call agents from your app](/langsmith/fleet/code)

<Note>
  **Self-hosting for Fleet is available in Beta.** For more information, see [Enable Fleet](/langsmith/deploy-self-hosted-full-platform#enable-fleet-insights-and-chat).
</Note>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/fleet/index.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
