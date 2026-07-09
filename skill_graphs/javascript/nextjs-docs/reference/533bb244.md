## Getting started[](https://nextjs.org/docs/app/guides/mcp#getting-started)
**Requirements:** Next.js 16 or above
Add `next-devtools-mcp` to the `.mcp.json` file at the root of your project:
.mcp.json
```
{
  "mcpServers": {
    "next-devtools": {
      "command": "npx",
      "args": ["-y", "next-devtools-mcp@latest"]
    }
  }
}
```

That's it! When you start your development server, `next-devtools-mcp` will automatically discover and connect to your running Next.js instance.
For more configuration options, see the
