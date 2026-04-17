##  [Advanced Usage](https://vercel.com/docs/agent-resources/vercel-mcp#advanced-usage)[](https://vercel.com/docs/agent-resources/vercel-mcp#advanced-usage)
###  [Project-specific MCP access](https://vercel.com/docs/agent-resources/vercel-mcp#project-specific-mcp-access)[](https://vercel.com/docs/agent-resources/vercel-mcp#project-specific-mcp-access)
For enhanced functionality and better tool performance, you can use project-specific MCP URLs that automatically provide the necessary project and team context:
`https://mcp.vercel.com/<teamSlug>/<projectSlug>`
####  [Benefits of project-specific URLs](https://vercel.com/docs/agent-resources/vercel-mcp#benefits-of-project-specific-urls)[](https://vercel.com/docs/agent-resources/vercel-mcp#benefits-of-project-specific-urls)
  * Automatic context: The MCP server automatically knows which project and team you're working with
  * Improved tool performance: Tools can execute without requiring manual parameter input
  * Better error handling: Reduces errors from missing project slug or team slug parameters
  * Streamlined workflow: No need to manually specify project context in each tool call


####  [When to use project-specific URLs](https://vercel.com/docs/agent-resources/vercel-mcp#when-to-use-project-specific-urls)[](https://vercel.com/docs/agent-resources/vercel-mcp#when-to-use-project-specific-urls)
Use project-specific URLs when:
  * You're working on a specific Vercel project
  * You want to avoid manually providing project and team slugs
  * You're experiencing errors like "Project slug and Team slug are required"


####  [Finding your team slug and project slug](https://vercel.com/docs/agent-resources/vercel-mcp#finding-your-team-slug-and-project-slug)[](https://vercel.com/docs/agent-resources/vercel-mcp#finding-your-team-slug-and-project-slug)
You can find your team slug and project slug in several ways:
  1. From the Vercel [dashboard](https://vercel.com/dashboard):
     * Project slug: Navigate to your project → Settings → General (sidebar tab)
     * Team slug: Navigate to your team → Settings → General (sidebar tab)
  2. From the Vercel CLI: Use `vercel projects ls` to list your projects


####  [Example usage](https://vercel.com/docs/agent-resources/vercel-mcp#example-usage)[](https://vercel.com/docs/agent-resources/vercel-mcp#example-usage)
Instead of using the general MCP endpoint and manually providing parameters, you can use:
`https://mcp.vercel.com/my-team/my-awesome-project `
This automatically provides the context for team `my-team` and project `my-awesome-project`, allowing tools to execute without additional parameter input.
* * *
[ Previous Markdown Access ](https://vercel.com/docs/agent-resources/markdown-access)[ Next Tools ](https://vercel.com/docs/agent-resources/vercel-mcp/tools)
Was this helpful?
Send
On this page
  * [What is Vercel MCP?](https://vercel.com/docs/agent-resources/vercel-mcp#what-is-vercel-mcp)
  * [Available tools](https://vercel.com/docs/agent-resources/vercel-mcp#available-tools)
  * [Connecting to Vercel MCP](https://vercel.com/docs/agent-resources/vercel-mcp#connecting-to-vercel-mcp)
  * [Supported clients](https://vercel.com/docs/agent-resources/vercel-mcp#supported-clients)
  * [Setup](https://vercel.com/docs/agent-resources/vercel-mcp#setup)
  * [Install with add-mcp](https://vercel.com/docs/agent-resources/vercel-mcp#install-with-add-mcp)
  * [Claude Code](https://vercel.com/docs/agent-resources/vercel-mcp#claude-code)
  * [Claude.ai and Claude for desktop](https://vercel.com/docs/agent-resources/vercel-mcp#claude.ai-and-claude-for-desktop)
  * [ChatGPT](https://vercel.com/docs/agent-resources/vercel-mcp#chatgpt)
  * [Codex CLI](https://vercel.com/docs/agent-resources/vercel-mcp#codex-cli)
  * [Cursor](https://vercel.com/docs/agent-resources/vercel-mcp#cursor)
  * [VS Code with Copilot](https://vercel.com/docs/agent-resources/vercel-mcp#vs-code-with-copilot)
  * [Installation](https://vercel.com/docs/agent-resources/vercel-mcp#installation)
  * [Authorization](https://vercel.com/docs/agent-resources/vercel-mcp#authorization)
  * [Devin](https://vercel.com/docs/agent-resources/vercel-mcp#devin)
  * [Raycast](https://vercel.com/docs/agent-resources/vercel-mcp#raycast)
  * [Goose](https://vercel.com/docs/agent-resources/vercel-mcp#goose)
  * [Windsurf](https://vercel.com/docs/agent-resources/vercel-mcp#windsurf)
  * [Gemini Code Assist](https://vercel.com/docs/agent-resources/vercel-mcp#gemini-code-assist)
  * [Gemini CLI](https://vercel.com/docs/agent-resources/vercel-mcp#gemini-cli)
  * [Security best practices](https://vercel.com/docs/agent-resources/vercel-mcp#security-best-practices)
  * [Advanced Usage](https://vercel.com/docs/agent-resources/vercel-mcp#advanced-usage)
  * [Project-specific MCP access](https://vercel.com/docs/agent-resources/vercel-mcp#project-specific-mcp-access)
  * [Benefits of project-specific URLs](https://vercel.com/docs/agent-resources/vercel-mcp#benefits-of-project-specific-urls)
  * [When to use project-specific URLs](https://vercel.com/docs/agent-resources/vercel-mcp#when-to-use-project-specific-urls)
  * [Finding your team slug and project slug](https://vercel.com/docs/agent-resources/vercel-mcp#finding-your-team-slug-and-project-slug)
  * [Example usage](https://vercel.com/docs/agent-resources/vercel-mcp#example-usage)


Copy as MarkdownGive feedbackAsk AI about this page
[Agent Resources](https://vercel.com/docs/agent-resources)
Vercel MCP server
