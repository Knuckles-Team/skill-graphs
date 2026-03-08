## Upgrading from 15 to 16[](https://nextjs.org/docs/app/guides/upgrading/version-16#upgrading-from-15-to-16)
### Using AI Agents with Next.js DevTools MCP[](https://nextjs.org/docs/app/guides/upgrading/version-16#using-ai-agents-with-nextjs-devtools-mcp)
If you're using an AI coding assistant that supports the **Next.js DevTools MCP** to automate the upgrade process and migration tasks.
#### Setup[](https://nextjs.org/docs/app/guides/upgrading/version-16#setup)
Add the following configuration to your MCP client, for each coding agent you can read
**example:**
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

For more information, visit the
> **Note:** Using `next-devtools-mcp@latest` ensures that your MCP client will always use the latest version of the Next.js DevTools MCP server.
#### Example Prompts[](https://nextjs.org/docs/app/guides/upgrading/version-16#example-prompts)
Once configured, you can use natural language prompts to upgrade your Next.js app:
**To upgrade to Next.js 16:**
Connect to your coding agent and then prompt:
```
Next Devtools, help me upgrade my Next.js app to version 16
```

**To migrate to Cache Components (after upgrading to v16):**
Connect to your coding agent and then prompt:
```
Next Devtools, migrate my Next.js app to cache components
```

Learn more in the documentation [here](https://nextjs.org/docs/app/guides/mcp).
### Using the Codemod[](https://nextjs.org/docs/app/guides/upgrading/version-16#using-the-codemod)
To update to Next.js version 16, you can use the `upgrade` [codemod](https://nextjs.org/docs/app/guides/upgrading/codemods#160):
pnpmnpmyarnbun
Terminal
```
pnpm dlx @next/codemod@canary upgrade latest
```

The [codemod](https://nextjs.org/docs/app/guides/upgrading/codemods#160) is able to:
  * Update `next.config.js` to use the new `turbopack` configuration
  * Migrate from `next lint` to the ESLint CLI
  * Migrate from deprecated `middleware` convention to `proxy`
  * Remove `unstable_` prefix from stabilized APIs
  * Remove `experimental_ppr` Route Segment Config from pages and layouts


If you prefer to do it manually, install the latest Next.js and React versions:
pnpmnpmyarnbun
Terminal
```
pnpm add next@latest react@latest react-dom@latest
```

If you are using TypeScript, ensure you also upgrade `@types/react` and `@types/react-dom` to their latest versions.
