# Anthropic integration
Source: https://docs.langchain.com/oss/javascript/integrations/tools/anthropic

Integrate with the Anthropic tool using LangChain JavaScript.

The `@langchain/anthropic` package provides LangChain-compatible wrappers for Anthropic's built-in tools. These tools can be bound to `ChatAnthropic` using `bindTools()` or [`createAgent`](https://reference.langchain.com/javascript/langchain/index/createAgent).

### Memory tool

The memory tool (`memory_20250818`) enables Claude to store and retrieve information across conversations through a memory file directory. Claude can create, read, update, and delete files that persist between sessions, allowing it to build knowledge over time without keeping everything in the context window.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { ChatAnthropic, tools } from "@langchain/anthropic";

// Create a simple in-memory file store (or use your own persistence layer)
const files = new Map<string, string>();

const memory = tools.memory_20250818({
  execute: async (command) => {
    switch (command.command) {
      case "view":
        if (!command.path || command.path === "/") {
          return Array.from(files.keys()).join("\n") || "Directory is empty.";
        }
        return (
          files.get(command.path) ?? `Error: File not found: ${command.path}`
        );
      case "create":
        files.set(command.path!, command.file_text ?? "");
        return `Successfully created file: ${command.path}`;
      case "str_replace":
        const content = files.get(command.path!);
        if (content && command.old_str) {
          files.set(
            command.path!,
            content.replace(command.old_str, command.new_str ?? "")
          );
        }
        return `Successfully replaced text in: ${command.path}`;
      case "delete":
        files.delete(command.path!);
        return `Successfully deleted: ${command.path}`;
      // Handle other commands: insert, rename
      default:
        return `Unknown command`;
    }
  },
});

const llm = new ChatAnthropic({
  model: "claude-sonnet-4-6",
});

const llmWithMemory = llm.bindTools([memory]);

const response = await llmWithMemory.invoke(
  "Remember that my favorite programming language is TypeScript"
);
```

For more information, see [Anthropic's Memory Tool documentation](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/memory-tool).

### Web search tool

The web search tool (`webSearch_20250305`) gives Claude direct access to real-time web content, allowing it to answer questions with up-to-date information beyond its knowledge cutoff. Claude automatically cites sources from search results as part of its answer.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { ChatAnthropic, tools } from "@langchain/anthropic";

const llm = new ChatAnthropic({
  model: "claude-sonnet-4-6",
});

// Basic usage
const response = await llm.invoke("What is the weather in NYC?", {
  tools: [tools.webSearch_20250305()],
});
```

The web search tool supports several configuration options:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const response = await llm.invoke("Latest news about AI?", {
  tools: [
    tools.webSearch_20250305({
      // Maximum number of times the tool can be used in the API request
      maxUses: 5,
      // Only include results from these domains
      allowedDomains: ["reuters.com", "bbc.com"],
      // Or block specific domains (cannot be used with allowedDomains)
      // blockedDomains: ["example.com"],
      // Provide user location for more relevant results
      userLocation: {
        type: "approximate",
        city: "San Francisco",
        region: "California",
        country: "US",
        timezone: "America/Los_Angeles",
      },
    }),
  ],
});
```

For more information, see [Anthropic's Web Search Tool documentation](https://docs.anthropic.com/en/docs/build-with-claude/tool-use/web-search-tool).

### Web fetch tool

The web fetch tool (`webFetch_20250910`) allows Claude to retrieve full content from specified web pages and PDF documents. Claude can only fetch URLs that have been explicitly provided by the user or that come from previous web search or web fetch results.

> **⚠️ Security Warning:** Enabling the web fetch tool in environments where Claude processes untrusted input alongside sensitive data poses data exfiltration risks. We recommend only using this tool in trusted environments or when handling non-sensitive data.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { ChatAnthropic, tools } from "@langchain/anthropic";

const llm = new ChatAnthropic({
  model: "claude-sonnet-4-6",
});

// Basic usage - fetch content from a URL
const response = await llm.invoke(
  "Please analyze the content at https://example.com/article",
  { tools: [tools.webFetch_20250910()] }
);
```

The web fetch tool supports several configuration options:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const response = await llm.invoke(
  "Summarize this research paper: https://arxiv.org/abs/2024.12345",
  {
    tools: [
      tools.webFetch_20250910({
        // Maximum number of times the tool can be used in the API request
        maxUses: 5,
        // Only fetch from these domains
        allowedDomains: ["arxiv.org", "example.com"],
        // Or block specific domains (cannot be used with allowedDomains)
        // blockedDomains: ["example.com"],
        // Enable citations for fetched content (optional, unlike web search)
        citations: { enabled: true },
        // Maximum content length in tokens (helps control token usage)
        maxContentTokens: 50000,
      }),
    ],
  }
);
```

You can combine web fetch with web search for comprehensive information gathering:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { tools } from "@langchain/anthropic";

const response = await llm.invoke(
  "Find recent articles about quantum computing and analyze the most relevant one",
  {
    tools: [
      tools.webSearch_20250305({ maxUses: 3 }),
      tools.webFetch_20250910({ maxUses: 5, citations: { enabled: true } }),
    ],
  }
);
```

For more information, see [Anthropic's Web Fetch Tool documentation](https://docs.anthropic.com/en/docs/build-with-claude/tool-use/web-fetch-tool).

### Tool search tools

The tool search tools enable Claude to work with hundreds or thousands of tools by dynamically discovering and loading them on-demand. This is useful when you have a large number of tools but don't want to load them all into the context window at once.

There are two variants:

* **`toolSearchRegex_20251119`** - Claude constructs regex patterns (using Python's `re.search()` syntax) to search for tools
* **`toolSearchBM25_20251119`** - Claude uses natural language queries to search for tools using the BM25 algorithm

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { ChatAnthropic, tools } from "@langchain/anthropic";
import { tool } from "langchain";
import { z } from "zod";

const llm = new ChatAnthropic({
  model: "claude-sonnet-4-6",
});

// Create tools with defer_loading to make them discoverable via search
const getWeather = tool(
  async (input: { location: string }) => {
    return `Weather in ${input.location}: Sunny, 72°F`;
  },
  {
    name: "get_weather",
    description: "Get the weather at a specific location",
    schema: z.object({
      location: z.string(),
    }),
    extras: { defer_loading: true },
  }
);

const getNews = tool(
  async (input: { topic: string }) => {
    return `Latest news about ${input.topic}...`;
  },
  {
    name: "get_news",
    description: "Get the latest news about a topic",
    schema: z.object({
      topic: z.string(),
    }),
    extras: { defer_loading: true },
  }
);

// Claude will search and discover tools as needed
const response = await llm.invoke("What is the weather in San Francisco?", {
  tools: [tools.toolSearchRegex_20251119(), getWeather, getNews],
});
```

Using the BM25 variant for natural language search:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { tools } from "@langchain/anthropic";

const response = await llm.invoke("What is the weather in San Francisco?", {
  tools: [tools.toolSearchBM25_20251119(), getWeather, getNews],
});
```

For more information, see [Anthropic's Tool Search documentation](https://docs.anthropic.com/en/docs/build-with-claude/tool-use/tool-search-tool).

### Text editor tool

The text editor tool (`textEditor_20250728`) enables Claude to view and modify text files, helping debug, fix, and improve code or other text documents. Claude can directly interact with files, providing hands-on assistance rather than just suggesting changes.

Available commands:

* `view` - Examine file contents or list directory contents
* `str_replace` - Replace specific text in a file
* `create` - Create a new file with specified content
* `insert` - Insert text at a specific line number

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import fs from "node:fs";
import { ChatAnthropic, tools } from "@langchain/anthropic";

const llm = new ChatAnthropic({
  model: "claude-sonnet-4-6",
});

const textEditor = tools.textEditor_20250728({
  async execute(args) {
    switch (args.command) {
      case "view":
        const content = fs.readFileSync(args.path, "utf-8");
        // Return with line numbers for Claude to reference
        return content
          .split("\n")
          .map((line, i) => `${i + 1}: ${line}`)
          .join("\n");
      case "str_replace":
        let fileContent = fs.readFileSync(args.path, "utf-8");
        fileContent = fileContent.replace(args.old_str, args.new_str);
        fs.writeFileSync(args.path, fileContent);
        return "Successfully replaced text.";
      case "create":
        fs.writeFileSync(args.path, args.file_text);
        return `Successfully created file: ${args.path}`;
      case "insert":
        const lines = fs.readFileSync(args.path, "utf-8").split("\n");
        lines.splice(args.insert_line, 0, args.new_str);
        fs.writeFileSync(args.path, lines.join("\n"));
        return `Successfully inserted text at line ${args.insert_line}`;
      default:
        return "Unknown command";
    }
  },
  // Optional: limit file content length when viewing
  maxCharacters: 10000,
});

const llmWithEditor = llm.bindTools([textEditor]);

const response = await llmWithEditor.invoke(
  "There's a syntax error in my primes.py file. Can you help me fix it?"
);
```

For more information, see [Anthropic's Text Editor Tool documentation](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/text-editor-tool).

### Computer use tool

The computer use tools enable Claude to interact with desktop environments through screenshot capture, mouse control, and keyboard input for autonomous desktop interaction.

> **⚠️ Security Warning:** Computer use is a beta feature with unique risks. Use a dedicated virtual machine or container with minimal privileges. Avoid giving access to sensitive data.

There are two variants:

* **`computer_20251124`** - For Claude Opus 4.5 (includes zoom capability)
* **`computer_20250124`** - For Claude 4 and Claude 3.7 models

Available actions:

* `screenshot` - Capture the current screen
* `left_click`, `right_click`, `middle_click` - Mouse clicks at coordinates
* `double_click`, `triple_click` - Multi-click actions
* `left_click_drag` - Click and drag operations
* `left_mouse_down`, `left_mouse_up` - Granular mouse control
* `scroll` - Scroll the screen
* `type` - Type text
* `key` - Press keyboard keys/shortcuts
* `mouse_move` - Move the cursor
* `hold_key` - Hold a key while performing other actions
* `wait` - Wait for a specified duration
* `zoom` - View specific screen regions at full resolution (Claude Opus 4.5 only)

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { ChatAnthropic, tools } from "@langchain/anthropic";

const llm = new ChatAnthropic({
  model: "claude-sonnet-4-6",
});

const computer = tools.computer_20250124({
  // Required: specify display dimensions
  displayWidthPx: 1024,
  displayHeightPx: 768,
  // Optional: X11 display number
  displayNumber: 1,
  execute: async (action) => {
    switch (action.action) {
      case "screenshot":
      // Capture and return base64-encoded screenshot
      // ...
      case "left_click":
      // Click at the specified coordinates
      // ...
      // ...
    }
  },
});

const llmWithComputer = llm.bindTools([computer]);

const response = await llmWithComputer.invoke(
  "Save a picture of a cat to my desktop."
);
```

For Claude Opus 4.5 with zoom support:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { tools } from "@langchain/anthropic";

const computer = tools.computer_20251124({
  displayWidthPx: 1920,
  displayHeightPx: 1080,
  // Enable zoom for detailed screen region inspection
  enableZoom: true,
  execute: async (action) => {
    // Handle actions including "zoom" for Claude Opus 4.5
    // ...
  },
});
```

For more information, see [Anthropic's Computer Use documentation](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/computer-use).

### Code execution tool

The code execution tool (`codeExecution_20250825`) allows Claude to run Bash commands and manipulate files in a secure, sandboxed environment. Claude can analyze data, create visualizations, perform calculations, and process files.

When this tool is provided, Claude automatically gains access to:

* **Bash commands** - Execute shell commands for system operations
* **File operations** - Create, view, and edit files directly

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { ChatAnthropic, tools } from "@langchain/anthropic";

const llm = new ChatAnthropic({
  model: "claude-sonnet-4-6",
});

// Basic usage - calculations and data analysis
const response = await llm.invoke(
  "Calculate the mean and standard deviation of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]",
  { tools: [tools.codeExecution_20250825()] }
);

// File operations and visualization
const response2 = await llm.invoke(
  "Create a matplotlib visualization of sales data and save it as chart.png",
  { tools: [tools.codeExecution_20250825()] }
);
```

Container reuse for multi-step workflows:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
// First request - creates a container
const response1 = await llm.invoke("Write a random number to /tmp/number.txt", {
  tools: [tools.codeExecution_20250825()],
});

// Extract container ID from response for reuse
const containerId = response1.response_metadata?.container?.id;

// Second request - reuse container to access the file
const response2 = await llm.invoke(
  "Read /tmp/number.txt and calculate its square",
  {
    tools: [tools.codeExecution_20250825()],
    container: containerId,
  }
);
```

For more information, see [Anthropic's Code Execution Tool documentation](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/code-execution-tool).

### Bash tool

The bash tool (`bash_20250124`) enables shell command execution in a persistent bash session. Unlike the sandboxed code execution tool, this tool requires you to provide your own execution environment.

> **⚠️ Security Warning:** The bash tool provides direct system access. Implement safety measures such as running in isolated environments (Docker/VM), command filtering, and resource limits.

The bash tool provides:

* **Persistent bash session** - Maintains state between commands
* **Shell command execution** - Run any shell command
* **Environment access** - Access to environment variables and working directory
* **Command chaining** - Support for pipes, redirects, and scripting

Available commands:

* Execute a command: `{ command: "ls -la" }`
* Restart the session: `{ restart: true }`

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { ChatAnthropic, tools } from "@langchain/anthropic";
import { execSync } from "child_process";

const llm = new ChatAnthropic({
  model: "claude-sonnet-4-6",
});

const bash = tools.bash_20250124({
  execute: async (args) => {
    if (args.restart) {
      // Reset session state
      return "Bash session restarted";
    }
    try {
      const output = execSync(args.command, {
        encoding: "utf-8",
        timeout: 30000,
      });
      return output;
    } catch (error) {
      return `Error: ${(error as Error).message}`;
    }
  },
});

const llmWithBash = llm.bindTools([bash]);

const response = await llmWithBash.invoke(
  "List all Python files in the current directory"
);

// Process tool calls and execute commands
console.log(response.tool_calls?.[0].name); // "bash"
console.log(response.tool_calls?.[0].args.command); // "ls -la *.py"
```

For more information, see [Anthropic's Bash Tool documentation](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/bash-tool).

### MCP toolset

The MCP toolset (`mcpToolset_20251120`) enables Claude to connect to remote MCP (Model Context Protocol) servers directly from the Messages API without implementing a separate MCP client. This allows Claude to use tools provided by MCP servers.

Key features:

* **Direct API integration** - Connect to MCP servers without implementing an MCP client
* **Tool calling support** - Access MCP tools through the Messages API
* **Flexible tool configuration** - Enable all tools, allowlist specific tools, or denylist unwanted tools
* **Per-tool configuration** - Configure individual tools with custom settings
* **OAuth authentication** - Support for OAuth Bearer tokens for authenticated servers
* **Multiple servers** - Connect to multiple MCP servers in a single request

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { ChatAnthropic, tools } from "@langchain/anthropic";

const llm = new ChatAnthropic({
  model: "claude-sonnet-4-6",
});

// Basic usage - enable all tools from an MCP server
const response = await llm.invoke("What tools do you have available?", {
  mcp_servers: [
    {
      type: "url",
      url: "https://example-server.modelcontextprotocol.io/sse",
      name: "example-mcp",
      authorization_token: "YOUR_TOKEN",
    },
  ],
  tools: [tools.mcpToolset_20251120({ serverName: "example-mcp" })],
});
```

**Allowlist pattern** - Enable only specific tools:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const response = await llm.invoke("Search for events", {
  mcp_servers: [
    {
      type: "url",
      url: "https://calendar.example.com/sse",
      name: "google-calendar-mcp",
      authorization_token: "YOUR_TOKEN",
    },
  ],
  tools: [
    tools.mcpToolset_20251120({
      serverName: "google-calendar-mcp",
      // Disable all tools by default
      defaultConfig: { enabled: false },
      // Explicitly enable only these tools
      configs: {
        search_events: { enabled: true },
        create_event: { enabled: true },
      },
    }),
  ],
});
```

**Denylist pattern** - Disable specific tools:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const response = await llm.invoke("List my events", {
  mcp_servers: [
    {
      type: "url",
      url: "https://calendar.example.com/sse",
      name: "google-calendar-mcp",
      authorization_token: "YOUR_TOKEN",
    },
  ],
  tools: [
    tools.mcpToolset_20251120({
      serverName: "google-calendar-mcp",
      // All tools enabled by default, just disable dangerous ones
      configs: {
        delete_all_events: { enabled: false },
        share_calendar_publicly: { enabled: false },
      },
    }),
  ],
});
```

**Multiple MCP servers**:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const response = await llm.invoke("Use tools from both servers", {
  mcp_servers: [
    {
      type: "url",
      url: "https://mcp.example1.com/sse",
      name: "mcp-server-1",
      authorization_token: "TOKEN1",
    },
    {
      type: "url",
      url: "https://mcp.example2.com/sse",
      name: "mcp-server-2",
      authorization_token: "TOKEN2",
    },
  ],
  tools: [
    tools.mcpToolset_20251120({ serverName: "mcp-server-1" }),
    tools.mcpToolset_20251120({
      serverName: "mcp-server-2",
      defaultConfig: { deferLoading: true },
    }),
  ],
});
```

**With Tool Search** - Use deferred loading for on-demand tool discovery:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const response = await llm.invoke("Find and use the right tool", {
  mcp_servers: [
    {
      type: "url",
      url: "https://example.com/sse",
      name: "example-mcp",
    },
  ],
  tools: [
    tools.toolSearchRegex_20251119(),
    tools.mcpToolset_20251120({
      serverName: "example-mcp",
      defaultConfig: { deferLoading: true },
    }),
  ],
});
```

For more information, see [Anthropic's MCP Connector documentation](https://docs.anthropic.com/en/docs/agents-and-tools/mcp-connector).

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/javascript/integrations/tools/anthropic.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Google integration
Source: https://docs.langchain.com/oss/javascript/integrations/tools/google

Integrate with Google Gemini tools using LangChain JavaScript.

The `@langchain/google` package supports Gemini's built-in tools, which provide capabilities like web search grounding, code execution, URL context retrieval, and more. These tools are passed as Gemini-native objects to `ChatGoogle` via `bindTools()` or the `tools` call option.

<Warning>
  You cannot mix Gemini native tools (Google Search, Code Execution, etc.) with standard LangChain tools (Zod-based function tools) in the same request. See the [ChatGoogle](/oss/javascript/integrations/chat/google) page for standard tool calling usage.
</Warning>

### Google Search

The `googleSearch` tool grounds model responses with real-time Google Search results. This is useful for questions about current events or specific facts.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { ChatGoogle } from "@langchain/google";

const llm = new ChatGoogle("gemini-2.5-flash")
  .bindTools([
    {
      googleSearch: {},
    },
  ]);

const res = await llm.invoke("Who won the latest World Series?");
console.log(res.text);
```

You can optionally filter search results to a specific time range:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const llm = new ChatGoogle("gemini-2.5-flash")
  .bindTools([
  {
    googleSearch: {
      timeRangeFilter: {
        startTime: "2025-01-01T00:00:00Z",
        endTime: "2025-12-31T23:59:59Z",
      },
    },
  },
]);
```

<Note>
  The `googleSearchRetrieval` tool is maintained for backwards compatibility, but `googleSearch` is preferred.
</Note>

For more information, see [Google's Grounding with Google Search documentation](https://ai.google.dev/gemini-api/docs/grounding).

### Code execution

The `codeExecution` tool allows Gemini to generate and run Python code to solve complex problems. The model writes the code, executes it, and returns the results.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { ChatGoogle } from "@langchain/google";

const llm = new ChatGoogle("gemini-2.5-flash")
  .bindTools([
    {
      codeExecution: {},
    },
  ]);

const res = await llm.invoke("Calculate the 100th Fibonacci number.");
console.log(res.contentBlocks);
```

The response includes both the generated code and its execution result in the `contentBlocks` field:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
for (const block of res.contentBlocks) {
  if (block.type === "tool_code") {
    console.log("Code:", block.toolCode);
  } else if (block.type === "tool_result") {
    console.log("Result:", block.toolResult);
  }
}
```

For more information, see [Google's Code Execution documentation](https://ai.google.dev/gemini-api/docs/code-execution).

### URL context

The `urlContext` tool allows Gemini to fetch and use content from URLs to ground its responses.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { ChatGoogle } from "@langchain/google";

const llm = new ChatGoogle("gemini-2.5-flash")
  .bindTools([
    {
      urlContext: {},
    },
  ]);

const res = await llm.invoke("Summarize this page: https://js.langchain.com/");
console.log(res.text);
```

For more information, see [Google's URL Context documentation](https://ai.google.dev/gemini-api/docs/url-context).

### Google Maps

The `googleMaps` tool grounds responses with geospatial context from Google Maps. This is useful for place-related queries.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { ChatGoogle } from "@langchain/google";

const llm = new ChatGoogle("gemini-2.5-flash")
  .bindTools([
    {
      googleMaps: {},
    },
  ]);

const res = await llm.invoke("What are the best coffee shops near Times Square?");
console.log(res.text);
```

You can enable a widget context token for rendering a Google Maps widget:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const llm = new ChatGoogle("gemini-2.5-flash")
  .bindTools([
    {
      googleMaps: {
        enableWidget: true,
    },
  },
]);

const res = await llm.invoke("Find Italian restaurants in downtown Chicago");

// Access the widget context token from grounding metadata
const groundingMetadata = res.response_metadata?.groundingMetadata;
console.log(groundingMetadata?.googleMapsWidgetContextToken);
```

For more information, see [Google's Google Maps grounding documentation](https://ai.google.dev/gemini-api/docs/grounding/google-maps).

### File search

The `fileSearch` tool performs semantic retrieval from file search stores. Files must first be imported using the Gemini File API.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { ChatGoogle } from "@langchain/google";

const llm = new ChatGoogle("gemini-2.5-flash")
  .bindTools([
    {
      fileSearch: {
      fileSearchStoreNames: ["fileSearchStores/my-store-123"],
    },
  },
]);

const res = await llm.invoke("What does the report say about Q4 revenue?");
console.log(res.text);
```

Configuration options:

* `fileSearchStoreNames` (required) -- the names of the file search stores to retrieve from
* `metadataFilter` (optional) -- metadata filter to apply to the retrieval
* `topK` (optional) -- the number of semantic retrieval chunks to return

For more information, see [Google's File Search documentation](https://ai.google.dev/gemini-api/docs/file-search).

### Computer use

The `computerUse` tool enables Gemini to interact with a browser environment. The model can view screenshots and perform actions like clicking, typing, and scrolling.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { ChatGoogle } from "@langchain/google";

const llm = new ChatGoogle("gemini-2.5-flash")
  .bindTools([
    {
      computerUse: {
      environment: "ENVIRONMENT_BROWSER",
    },
  },
]);
```

Configuration options:

* `environment` (required) -- the environment being operated (e.g. `"ENVIRONMENT_BROWSER"`)
* `excludedPredefinedFunctions` (optional) -- predefined functions to exclude from the action space

For more information, see [Google's Computer Use documentation](https://ai.google.dev/gemini-api/docs/computer-use).

### MCP servers

The `mcpServers` field allows Gemini to connect to remote MCP (Model Context Protocol) servers. Unlike other native tools, MCP servers are specified as an array on the tool object.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { ChatGoogle } from "@langchain/google";

const llm = new ChatGoogle("gemini-2.5-flash")
  .bindTools([
    {
      mcpServers: [
      {
        name: "my-mcp-server",
        streamableHttpTransport: {
          url: "https://my-mcp-server.example.com/mcp",
        },
      },
    ],
  },
]);

const res = await llm.invoke("Use the tools from the MCP server to help me.");
console.log(res.text);
```

For more information, see [Google's MCP documentation](https://ai.google.dev/gemini-api/docs/mcp).

### Vertex AI Search data store

If you are using Vertex AI (`platformType: "gcp"`), you can ground responses using a Vertex AI Search data store.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { ChatGoogle } from "@langchain/google";

const projectId = "YOUR_PROJECT_ID";
const datastoreId = "YOUR_DATASTORE_ID";

const llm = new ChatGoogle({
  model: "gemini-2.5-pro",
  platformType: "gcp",
}).bindTools([
  {
    retrieval: {
      vertexAiSearch: {
        datastore: `projects/${projectId}/locations/global/collections/default_collection/dataStores/${datastoreId}`,
      },
      disableAttribution: false,
    },
  },
]);

const res = await llm.invoke(
  "What is the score of Argentina vs Bolivia football game?"
);
console.log(res.text);
```

For more information, see [Google's Vertex AI Search grounding documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/grounding/ground-with-vertex-ai-search).

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/javascript/integrations/tools/google.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Tool integrations
Source: https://docs.langchain.com/oss/javascript/integrations/tools/index

Integrate with tools using LangChain JavaScript.

[Tools](/oss/javascript/langchain/tools) are utilities designed to be called by a model: their inputs are designed to be generated by models, and their outputs are designed to be passed back to models.

A [toolkit](/oss/javascript/langchain/tools#prebuilt-tools) is a collection of tools meant to be used together.

## Integration platforms

The following platforms provide access to multiple tools and services through a unified interface:

| Tool/Toolkit                                              | Number of Integrations | Pricing             | Key Features                                               |
| --------------------------------------------------------- | ---------------------- | ------------------- | ---------------------------------------------------------- |
| [`Composio`](/oss/javascript/integrations/tools/composio) | 500+                   | Free tier available | OAuth handling, event-driven workflows, multi-user support |

## All tools and toolkits

<Columns>
  <Card title="Azure Container Apps Dynamic Sessions" icon="link" href="/oss/javascript/integrations/tools/azure_dynamic_sessions" />

  <Card title="ClickSend" icon="link" href="/oss/javascript/integrations/tools/clicksend" />

  <Card title="Composio" icon="link" href="/oss/javascript/integrations/tools/composio" />

  <Card title="Dall-E Tool" icon="link" href="/oss/javascript/integrations/tools/dalle" />

  <Card title="Decodo Tools" icon="link" href="/oss/javascript/integrations/tools/decodo" />

  <Card title="ExaSearchResults" icon="link" href="/oss/javascript/integrations/tools/exa_search" />

  <Card title="FalkorDB" icon="link" href="/oss/javascript/integrations/tools/falkordb" />

  <Card title="Google (Gemini Native Tools)" icon="link" href="/oss/javascript/integrations/tools/google" />

  <Card title="GOAT" icon="link" href="/oss/javascript/integrations/tools/goat" />

  <Card title="JigsawStack Tool" icon="link" href="/oss/javascript/integrations/tools/jigsawstack" />

  <Card title="Agent with AWS Lambda" icon="link" href="/oss/javascript/integrations/tools/lambda_agent" />

  <Card title="Oracle AI Database" icon="link" href="/oss/javascript/integrations/tools/oracleai" />

  <Card title="Nia Toolkit" icon="link" href="/oss/javascript/integrations/tools/nia" />

  <Card title="Tavily Search" icon="link" href="/oss/javascript/integrations/tools/tavily_search" />

  <Card title="Tavily Extract" icon="link" href="/oss/javascript/integrations/tools/tavily_extract" />

  <Card title="Tavily Crawl" icon="link" href="/oss/javascript/integrations/tools/tavily_crawl" />

  <Card title="Tavily Map" icon="link" href="/oss/javascript/integrations/tools/tavily_map" />

  <Card title="Web Browser Tool" icon="link" href="/oss/javascript/integrations/tools/webbrowser" />

  <Card title="You.com Search" icon="link" href="/oss/javascript/integrations/tools/youdotcom" />
</Columns>

<Info>
  If you'd like to write your own tool, see [Create tools](/oss/javascript/langchain/tools#create-tools). If you'd like to contribute an integration, see [Build a new integration](/oss/javascript/contributing/integrations-langchain).
</Info>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/javascript/integrations/tools/index.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
