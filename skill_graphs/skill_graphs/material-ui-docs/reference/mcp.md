[Skip to content](https://mui.com/material-ui/getting-started/mcp/#main-content)
[](https://mui.com/)
Search…`Ctrl+K`3
# Model Context Protocol (MCP) for MUI
Access the official Material UI docs and code examples in your AI client.
![ads via Carbon](https://ad.double-click.net/ddm/trackimp/N718679.452584BUYSELLADS.COM/B29332811.421611897;dc_trk_aid=613858979;dc_trk_cid=235700574;ord=177300366;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;gdpr=$;gdpr_consent=$;ltd=;dc_tdv=1)
## [What is MCP?](https://mui.com/material-ui/getting-started/mcp/#what-is-mcp)
The Model Context Protocol (MCP) is an open standard for connecting AI assistants to real, trusted sources of documentation and code. For Material UI users, this means you get answers that are accurate, up-to-date, and directly reference the official docs.
To learn more about MCP, see the
## [Why use MCP?](https://mui.com/material-ui/getting-started/mcp/#why-use-mcp)
Popular AI coding assistants are excellent at providing answers, especially to straightforward questions. But when faced with deeper, more complex questions that require understanding concepts from multiple parts of the documentation, they often hallucinate links, cite non-existent documentation, or provide answers that are hard to verify. MCP solves these problems by:
  * Quoting real, direct sources in answers
  * Linking to actual documentation—no imaginary links that lead to 404s
  * Using component code from officially published registries


## [Installation and setup](https://mui.com/material-ui/getting-started/mcp/#installation-and-setup)
The sections below detail how to set up the Material UI MCP in popular agentic coding environments.
### [VS Code, Cursor, Windsurf](https://mui.com/material-ui/getting-started/mcp/#vs-code-cursor-windsurf)
Open the MCP configuration (**Settings** -> **MCP** -> **Add Server**) and add the following:
```
"mcpServers": {
  "mui-mcp": {
    "type": "stdio",
    "command": "npx",
    "args": ["-y", "@mui/mcp@latest"]
  }
}

```
CopyCopied(or Ctrl + C)
VS Code users must also enable Agent mode (for Copilot Chat) and add the following to `settings.json`:
```
  "chat.mcp.enabled": true,
  "chat.mcp.discovery.enabled": true

```
CopyCopied(or Ctrl + C)
### [JetBrains IDEs](https://mui.com/material-ui/getting-started/mcp/#jetbrains-ides)
Open the MCP configuration (**Settings** -> **Tools** -> **AI Assistant** -> **Model Context Protocol (MCP)**) and add the following:
  * Name: MUI MCP
  * Command: `npx`
  * Arguments: `-y @mui/mcp@latest`


Click **OK** and **Apply**.
### [Zed](https://mui.com/material-ui/getting-started/mcp/#zed)
You can add the Material UI MCP server to Zed as an extension or as a custom server:
#### As an extension
Go to the Extensions page through the keybinding `cmd-shift-x`/`ctrl-shift-x` (macOS/Linux), or via the Command Palette by searching for `zed: extensions`.
Search for "MUI MCP" and install the extension. No additional configuration is required, but you can optionally add the `preferred_theme` and `component_filter` fields.
#### As a custom server
Search for `agent: add context server` in the Command Palette and add the following:
```
{
  "mui-mcp-server": {
    "command": {
      "path": "npx",
      "args": ["-y", "@mui/mcp@latest"]
      "env": {}
    }
  }
}

```
CopyCopied(or Ctrl + C)
### [Claude Code](https://mui.com/material-ui/getting-started/mcp/#claude-code)
Claude Code is Anthropic's agentic coding tool that runs in your terminal.
You can add the Material UI MCP server to Claude Code via the command line:
```
claude mcp add mui-mcp -- npx -y @mui/mcp@latest

```
CopyCopied(or Ctrl + C)
By default, this installs the MCP server to local-scope of the project you are working on.
If you want the MCP server to always be available to all projects on your machine, you would install it to user-scope:
```
claude mcp add mui-mcp -s user -- npx -y @mui/mcp@latest

```
CopyCopied(or Ctrl + C)
To better understand MCP server scope hierarchy and precedence in Claude Code, see their
## [Common issues](https://mui.com/material-ui/getting-started/mcp/#common-issues)
### [I've installed the MCP but there are errors in connection](https://mui.com/material-ui/getting-started/mcp/#ive-installed-the-mcp-but-there-are-errors-in-connection)
Try using the MCP inspector to debug the connection. To do so, run:
```
 npx @modelcontextprotocol/inspector

```
CopyCopied(or Ctrl + C)
Wait for the terminal to print "🔍 MCP Inspector is up and running at
  * **Transport type: Stdio**
  * **Command:**`npx`
  * **Arguments:** `-y @mui/mcp@latest`


Click **Connect** and wait for the connection to be established.
Once connected, you'll see a list of available tools. If you're not able to connect, check the logs in the terminal where you ran the MCP inspector for more details.
### [I've installed the MCP but it's not being used when I ask questions](https://mui.com/material-ui/getting-started/mcp/#ive-installed-the-mcp-but-its-not-being-used-when-i-ask-questions)
If you've installed the MCP and enabled all the necessary settings but it's not being used when you ask questions, you might need to supply rules to your AI client to tell it to use the MCP.
Most editors allow you to specify rules for AI assistants to follow. In VS Code, for instance, you can create a new rule at `.github/instructions/mui.md` and add the following:
```
## Use the mui-mcp server to answer any MUI questions --

- 1. call the "useMuiDocs" tool to fetch the docs of the package relevant in the question
- 2. call the "fetchDocs" tool to fetch any additional docs if needed using ONLY the URLs present in the returned content.
- 3. repeat steps 1-2 until you have fetched all relevant docs for the given question
- 4. use the fetched content to answer the question

```
CopyCopied(or Ctrl + C)
You can use this same text as a rule for any other IDE, but the preferred location for rules may differ.
## [Troubleshooting](https://mui.com/material-ui/getting-started/mcp/#troubleshooting)
The MCP is available as a separate package that runs locally and communicates via your AI client using the `stdio` transport. Use the following command to test the MCP in the
```
npx -y @mui/mcp@latest

```
CopyCopied(or Ctrl + C)
Was this page helpful?
* * *
[](https://mui.com/material-ui/getting-started/usage/)[llms.txt](https://mui.com/material-ui/llms.txt)
* * *
[](https://mui.com/)
•
[Blog ](https://mui.com/blog/)
•
[Store ](https://mui.com/store/)
[](https://mui.com/r/discord/ "Discord")[](https://mui.com/feed/blog/rss.xml "RSS Feed")
Contents
  * [What is MCP?](https://mui.com/material-ui/getting-started/mcp/#what-is-mcp)
  * [Why use MCP?](https://mui.com/material-ui/getting-started/mcp/#why-use-mcp)
  * [Installation and setup](https://mui.com/material-ui/getting-started/mcp/#installation-and-setup)
    * [VS Code, Cursor, Windsurf](https://mui.com/material-ui/getting-started/mcp/#vs-code-cursor-windsurf)
    * [JetBrains IDEs](https://mui.com/material-ui/getting-started/mcp/#jetbrains-ides)
    * [Zed](https://mui.com/material-ui/getting-started/mcp/#zed)
    * [Claude Code](https://mui.com/material-ui/getting-started/mcp/#claude-code)
  * [Common issues](https://mui.com/material-ui/getting-started/mcp/#common-issues)
    * [I've installed the MCP but there are errors in connection](https://mui.com/material-ui/getting-started/mcp/#ive-installed-the-mcp-but-there-are-errors-in-connection)
    * [I've installed the MCP but it's not being used when I ask questions](https://mui.com/material-ui/getting-started/mcp/#ive-installed-the-mcp-but-its-not-being-used-when-i-ask-questions)
  * [Troubleshooting](https://mui.com/material-ui/getting-started/mcp/#troubleshooting)


[Become a Diamond sponsor](https://mui.com/material-ui/discover-more/backers/#diamond-sponsors)
###### Cookie Preferences
We use cookies to understand site usage and improve our content. This includes third-party analytics.
Allow analyticsEssential only
[](https://mui.com/)
Material UIv7.3.9
  * [](https://mui.com/material-ui/getting-started/)
    * [Overview](https://mui.com/material-ui/getting-started/)
    * [Installation](https://mui.com/material-ui/getting-started/installation/)
    * [Usage](https://mui.com/material-ui/getting-started/usage/)
    * [MCPNew](https://mui.com/material-ui/getting-started/mcp/)
    * [llms.txtNew](https://mui.com/material-ui/llms.txt)
    * [Example projects](https://mui.com/material-ui/getting-started/example-projects/)
    * [Templates](https://mui.com/material-ui/getting-started/templates/)
    * [Learn](https://mui.com/material-ui/getting-started/learn/)
    * [Design resources](https://mui.com/material-ui/getting-started/design-resources/)
    * [FAQs](https://mui.com/material-ui/getting-started/faq/)
    * [Supported components](https://mui.com/material-ui/getting-started/supported-components/)
    * [Supported platforms](https://mui.com/material-ui/getting-started/supported-platforms/)
    * [Support](https://mui.com/material-ui/getting-started/support/)
  * [](https://mui.com/material-ui/all-components/)
  * [](https://mui.com/material-ui/api/accordion/)
  * [](https://mui.com/material-ui/customization/how-to-customize/)
  * [](https://mui.com/material-ui/guides/building-extensible-themes/)
  * [](https://mui.com/material-ui/integrations/tailwindcss/tailwindcss-v4/)
  * [](https://mui.com/material-ui/experimental-api/classname-generator/)
  * [](https://mui.com/material-ui/migration/upgrade-to-grid-v2/)
  * [](https://mui.com/material-ui/discover-more/showcase/)
  * [](https://mui.com/material-ui/design-resources/material-ui-for-figma/)
  * [](https://mui.com/store/%3Futm_source=docs&utm_medium=referral&utm_campaign=sidenav/)
