## Examples[](https://nextjs.org/docs/app/guides/mcp#examples)
### Error detection and diagnosis[](https://nextjs.org/docs/app/guides/mcp#error-detection-and-diagnosis)
Ask your agent about errors in real-time:
```
User: "What errors are currently in my application?"
```

The agent will:
  * Query your running Next.js application via `next-devtools-mcp`
  * Retrieve current build errors, runtime errors, and type errors
  * Analyze the errors and provide actionable fixes

Agent response (click to expand)
```
> fix errors on the page

⏺ I'll help you fix the errors on the page. Let me first check what errors exist by looking at the
  current state of the project.

⏺ next-devtools - nextjs_runtime (MCP)(action: "discover_servers")
⏺ next-devtools - nextjs_runtime (MCP)(action: "call_tool", toolName: "get_errors")

⏺ I found a hydration error on the /about page. The error shows that the server is rendering
  "server" but the client is rendering "client", causing a mismatch. Let me create a todo list and fix
   this issue.

⏺ Perfect! Now let me check for errors on the page.           01:14 PM  claude-sonnet-4-5-20250929

⏺ next-devtools - nextjs_runtime (MCP)(action: "call_tool", toolName: "get_errors")
  ⎿ {
      "success": true,
      "port": 3000,
      "toolName": "get_errors",
      "result": {
        "content": [
          {
            "type": "text",
            "text": "# Found errors in 1 browser session(s)\n\n## Session: /about\n\n**1 error(s)
     found**\n\n### Runtime Errors\n\n#### Error 1 (Type: recoverable)\n\n**Error**: Hydration failed
```

### Upgrading and best practices[](https://nextjs.org/docs/app/guides/mcp#upgrading-and-best-practices)
Get help with Next.js concepts and migrations:
```
User: "Help me upgrade my Next.js app to version 16"
```

The agent will analyze your current version, guide you through automated migrations with codemods, and provide step-by-step instructions for handling breaking changes.
Ask conceptual questions:
```
User: "When should I use 'use client' in App Router?"
```

The agent will query the Next.js knowledge base and provide documentation-backed explanations with examples from your codebase.
