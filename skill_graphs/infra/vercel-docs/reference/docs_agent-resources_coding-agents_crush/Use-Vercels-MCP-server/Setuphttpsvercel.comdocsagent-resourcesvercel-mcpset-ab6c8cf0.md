##  [Setup](https://vercel.com/docs/agent-resources/vercel-mcp#setup)[](https://vercel.com/docs/agent-resources/vercel-mcp#setup)
Connect your AI client to Vercel MCP and authorize access to manage your Vercel projects.
###  [Install with add-mcp](https://vercel.com/docs/agent-resources/vercel-mcp#install-with-add-mcp)[](https://vercel.com/docs/agent-resources/vercel-mcp#install-with-add-mcp)
Install the MCP server for all your coding agents:
```
npx add-mcp https://mcp.vercel.com
```

The `add-mcp` tool automatically detects your installed AI clients and configures Vercel MCP for each one.
Add `-y` to skip the confirmation prompt and install to all detected agents already in use in the project directory. Add `-g` to install globally across all projects.
###  [Claude Code](https://vercel.com/docs/agent-resources/vercel-mcp#claude-code)[](https://vercel.com/docs/agent-resources/vercel-mcp#claude-code)
```
# Install Claude Code
npm install -g @anthropic-ai/claude-code

# Navigate to your project
cd your-awesome-project

# Add Vercel MCP
claude mcp add --transport http vercel https://mcp.vercel.com

# Start coding with Claude
claude

# Authenticate the MCP tools by typing /mcp
/mcp
```

###  [Claude.ai and Claude for desktop](https://vercel.com/docs/agent-resources/vercel-mcp#claude.ai-and-claude-for-desktop)[](https://vercel.com/docs/agent-resources/vercel-mcp#claude.ai-and-claude-for-desktop)
Custom connectors using remote MCP are available on Claude and Claude Desktop for users on
  1. Open Settings in the sidebar
  2. Navigate to Connectors and select Add custom connector
  3. Configure the connector:
     * Name: `Vercel`
     * URL: `https://mcp.vercel.com`


###  [ChatGPT](https://vercel.com/docs/agent-resources/vercel-mcp#chatgpt)[](https://vercel.com/docs/agent-resources/vercel-mcp#chatgpt)
Custom connectors using MCP are available on ChatGPT for
Follow these steps to set up Vercel as a connector within ChatGPT:
  1. Enable
     * Go to
  2. Open
  3. In the Connectors tab, `Create` a new connector:
     * Give it a name: `Vercel`
     * MCP server URL: `https://mcp.vercel.com`
     * Authentication: `OAuth`
  4. Click Create


The Vercel connector will appear in the composer's
###  [Codex CLI](https://vercel.com/docs/agent-resources/vercel-mcp#codex-cli)[](https://vercel.com/docs/agent-resources/vercel-mcp#codex-cli)
```
# Install Codex
npm i -g @openai/codex

# Add Vercel MCP
codex mcp add vercel --url https://mcp.vercel.com

# Start Codex
codex
```

When adding the MCP server, Codex will detect OAuth support and open your browser to authorize the connection.
###  [Cursor](https://vercel.com/docs/agent-resources/vercel-mcp#cursor)[](https://vercel.com/docs/agent-resources/vercel-mcp#cursor)
Click the button above to open Cursor and automatically add Vercel MCP. You can also add the snippet below to your project-specific or global `.cursor/mcp.json` file manually. For more details, see the
```
{
  "mcpServers": {
    "vercel": {
      "url": "https://mcp.vercel.com"
    }
  }
}
```

Once the server is added, Cursor will attempt to connect and display a `Needs login` prompt. Click on this prompt to authorize Cursor to access your Vercel account.
###  [VS Code with Copilot](https://vercel.com/docs/agent-resources/vercel-mcp#vs-code-with-copilot)[](https://vercel.com/docs/agent-resources/vercel-mcp#vs-code-with-copilot)
####  [Installation](https://vercel.com/docs/agent-resources/vercel-mcp#installation)[](https://vercel.com/docs/agent-resources/vercel-mcp#installation)
[Add to VS Code](vscode:mcp/install?%7B%22name%22%3A%22Vercel%22%2C%22url%22%3A%22https%3A%2F%2Fmcp.vercel.com%22%7D)
Use the one-click installation by clicking the button above to add Vercel MCP, or follow the steps below to do it manually:
  1. Open the Command Palette (``Ctrl+Shift+P`` on Windows/Linux or ``Cmd+Shift+P`` on macOS)
  2. Run MCP: Add Server
  3. Select HTTP
  4. Enter the following details:
     * URL: `https://mcp.vercel.com`
     * Name: `Vercel`
  5. Select Global or Workspace depending on your needs
  6. Click Add


####  [Authorization](https://vercel.com/docs/agent-resources/vercel-mcp#authorization)[](https://vercel.com/docs/agent-resources/vercel-mcp#authorization)
Now that you've added Vercel MCP, let's start the server and authorize:
  1. Open the Command Palette (``Ctrl+Shift+P`` on Windows/Linux or ``Cmd+Shift+P`` on macOS)
  2. Run MCP: List Servers
  3. Select Vercel
  4. Click Start Server
  5. When the dialog appears saying `The MCP Server Definition 'Vercel' wants to authenticate to Vercel MCP`, click Allow
  6. A popup will ask `Do you want Code to open the external website?` — click Cancel
  7. You'll see a message: `Having trouble authenticating to 'Vercel MCP'? Would you like to try a different way? (URL Handler)`
  8. Click Yes
  9. Click Open and complete the Vercel sign-in flow to connect to Vercel MCP


###  [Devin](https://vercel.com/docs/agent-resources/vercel-mcp#devin)[](https://vercel.com/docs/agent-resources/vercel-mcp#devin)
  1. Navigate to
  2. Search for "Vercel" and select the MCP
  3. Click Install


###  [Raycast](https://vercel.com/docs/agent-resources/vercel-mcp#raycast)[](https://vercel.com/docs/agent-resources/vercel-mcp#raycast)
  1. Run the Install Server command
  2. Enter the following details:
     * Name: `Vercel`
     * Transport: HTTP
     * URL: `https://mcp.vercel.com`
  3. Click Install


###  [Goose](https://vercel.com/docs/agent-resources/vercel-mcp#goose)[](https://vercel.com/docs/agent-resources/vercel-mcp#goose)
Use the one-click installation by clicking the button below to add Vercel MCP. For more details, see the
###  [Windsurf](https://vercel.com/docs/agent-resources/vercel-mcp#windsurf)[](https://vercel.com/docs/agent-resources/vercel-mcp#windsurf)
Add the snippet below to your `mcp_config.json` file. For more details, see the
```
{
  "mcpServers": {
    "vercel": {
      "serverUrl": "https://mcp.vercel.com"
    }
  }
}
```

###  [Gemini Code Assist](https://vercel.com/docs/agent-resources/vercel-mcp#gemini-code-assist)[](https://vercel.com/docs/agent-resources/vercel-mcp#gemini-code-assist)
Gemini Code Assist is an IDE extension that supports MCP integration. To set up Vercel MCP with Gemini Code Assist:
  1. Ensure you have Gemini Code Assist installed in your IDE
  2. Add the following configuration to your `~/.gemini/settings.json` file:


```
{
  "mcpServers": {
    "vercel": {
      "command": "npx",
      "args": ["mcp-remote", "https://mcp.vercel.com"]
    }
  }
}
```

  1. Restart your IDE to apply the configuration
  2. When prompted, authenticate with Vercel to grant access


###  [Gemini CLI](https://vercel.com/docs/agent-resources/vercel-mcp#gemini-cli)[](https://vercel.com/docs/agent-resources/vercel-mcp#gemini-cli)
Gemini CLI shares the same configuration as [Gemini Code Assist](https://vercel.com/docs/agent-resources/vercel-mcp#gemini-code-assist). To set up Vercel MCP with Gemini CLI:
  1. Ensure you have the Gemini CLI installed
  2. Add the following configuration to your `~/.gemini/settings.json` file:


```
{
  "mcpServers": {
    "vercel": {
      "command": "npx",
      "args": ["mcp-remote", "https://mcp.vercel.com"]
    }
  }
}
```

  1. Run the Gemini CLI and use the `/mcp list` command to see available MCP servers
  2. When prompted, authenticate with Vercel to grant access


For more details on configuring MCP servers with Gemini tools, see the
Setup steps may vary based on your MCP client version. Always check your client's documentation for the latest instructions.
