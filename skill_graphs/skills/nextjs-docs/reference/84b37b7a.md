## Development workflow[](https://nextjs.org/docs/app/guides/mcp#development-workflow)
  1. Start your Next.js development server:


pnpmnpmyarnbun
Terminal
```
pnpm dev
```

  1. Your Coding Agent will automatically connect to the running Next.js instance via `next-devtools-mcp`
  2. Open your application in the browser to view pages
  3. Query your agent for insights and diagnostics (see examples below)


### Available tools[](https://nextjs.org/docs/app/guides/mcp#available-tools)
Through `next-devtools-mcp`, agents can use the following tools:
  * **`get_errors`**: Retrieve current build errors, runtime errors, and type errors from your dev server
  * **`get_logs`**: Get the path to the development log file containing browser console logs and server output
  * **`get_page_metadata`**: Get metadata about specific pages including routes, components, and rendering information
  * **`get_project_metadata`**: Retrieve project structure, configuration, and dev server URL
  * **`get_server_action_by_id`**: Look up Server Actions by their ID to find the source file and function name
