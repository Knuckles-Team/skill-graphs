## How it works[](https://nextjs.org/docs/app/guides/mcp#how-it-works)
Next.js 16+ includes a built-in MCP endpoint at `/_next/mcp` that runs within your development server. The `next-devtools-mcp` package automatically discovers and communicates with these endpoints, allowing it to:
  * Connect to multiple Next.js instances running on different ports
  * Forward tool calls to the appropriate Next.js dev server
  * Provide a unified interface for coding agents


This architecture decouples the agent interface from the internal implementation, enabling `next-devtools-mcp` to work seamlessly across different Next.js projects.
