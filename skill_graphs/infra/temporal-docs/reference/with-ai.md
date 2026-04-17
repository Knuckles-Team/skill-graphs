sessionId: 1773003704193
userId:
deviceId: a7b8e146-8bde-40a2-8f49-9c8771af83e8
Update Reset Update User ID Update Device ID
[Skip to main content](https://docs.temporal.io/with-ai#__docusaurus_skipToContent_fallback)
[![Temporal logo](https://docs.temporal.io/img/assets/temporal-logo-dark.svg)](https://temporal.io)[Home](https://docs.temporal.io/)[Courses](https://learn.temporal.io/getting_started/)[SDKs](https://docs.temporal.io/develop)[AI Cookbook](https://docs.temporal.io/ai-cookbook)[Code Exchange](https://temporal.io/code-exchange)[Temporal Cloud](https://docs.temporal.io/cloud)
Ask AI
Search
  * [Home](https://docs.temporal.io/)
  * [Quickstarts](https://docs.temporal.io/quickstarts)
  * [Evaluate](https://docs.temporal.io/evaluate/)
  * [Develop](https://docs.temporal.io/develop/)
  * [Temporal Cloud](https://docs.temporal.io/cloud)
  * [Deploy to production](https://docs.temporal.io/production-deployment)
  * [CLI (temporal)](https://docs.temporal.io/cli)
  * [References](https://docs.temporal.io/references/)
  * [Troubleshooting](https://docs.temporal.io/troubleshooting/)
  * [Best practices](https://docs.temporal.io/best-practices/)
  * [Encyclopedia](https://docs.temporal.io/encyclopedia/)
  * [Glossary](https://docs.temporal.io/glossary)
  * [Use with AI](https://docs.temporal.io/with-ai)


  * [](https://docs.temporal.io/)
  * Use with AI


On this page
# Use These Docs with AI
Connect Temporal documentation directly to your AI assistant for accurate, up-to-date answers about Temporal. The Temporal docs MCP server gives AI tools real-time access to our documentation, so responses draw from current docs rather than training data.
The server requires anonymous authentication using any Google account to enforce rate limits and prevent abuse. We cannot see nor do we collect any contact information from this.
## Claude Code[​](https://docs.temporal.io/with-ai#claude-code "Direct link to Claude Code")
Add the Temporal docs MCP server to Claude Code with a single command:
```
claude mcp add --scope user --transport http temporal-docs https://temporal.mcp.kapa.ai

```

This adds the server globally so it's available in all your projects.
To add it to a specific project only (stored in `.mcp.json`):
```
claude mcp add --transport http temporal-docs https://temporal.mcp.kapa.ai

```

After adding, restart Claude Code and run `/mcp` to authenticate with your Google account.
## Claude Desktop[​](https://docs.temporal.io/with-ai#claude-desktop "Direct link to Claude Desktop")
  1. Open Claude Desktop settings
  2. Navigate to **Settings > Connectors**
  3. Add a new MCP server with the URL: `https://temporal.mcp.kapa.ai`


## Other MCP-compatible tools[​](https://docs.temporal.io/with-ai#other-mcp-compatible-tools "Direct link to Other MCP-compatible tools")
For any tool that supports the Model Context Protocol, use the following server URL:
```
https://temporal.mcp.kapa.ai

```

Configuration format varies by tool. Here's a generic JSON configuration:
```
{
  "mcpServers": {
    "temporal-docs": {
      "transport": "http",
      "url": "https://temporal.mcp.kapa.ai"
    }
  }
}

```

Help us make Temporal better. Contribute to our
[Previous Glossary](https://docs.temporal.io/glossary)
  * [Claude Code](https://docs.temporal.io/with-ai#claude-code)
  * [Claude Desktop](https://docs.temporal.io/with-ai#claude-desktop)
  * [Other MCP-compatible tools](https://docs.temporal.io/with-ai#other-mcp-compatible-tools)


  * [Temporal Cloud](https://temporal.io/cloud)
  * [Meetups](https://temporal.io/community#events)
  * [Workshops](https://temporal.io/community#workshops)
  * [Support forum](https://community.temporal.io/)
  * [Ask an expert](https://pages.temporal.io/ask-an-expert)


  * [Learn Temporal](https://learn.temporal.io)
  * [Blog](https://temporal.io/blog)
  * [Use cases](https://temporal.io/use-cases)
  * [Newsletter signup](https://pages.temporal.io/newsletter-subscribe)


  * [Security](https://docs.temporal.io/security)
  * [Privacy policy](https://temporal.io/global-privacy-policy)
  * [Terms of service](https://docs.temporal.io/pdf/temporal-tos-2021-07-24.pdf)
  * [We're hiring](https://temporal.io/careers)


[![Temporal logo](https://docs.temporal.io/img/favicon.png)](https://temporal.io)
Copyright © 2026 Temporal Technologies Inc.
Feedback![](https://static.scarf.sh/a.png?x-pxid=6fb132d3-92f6-455f-bf17-eb3d6937bdea)
Recaptcha requires verification.
-
protected by **reCAPTCHA**
-
