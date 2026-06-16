# OpenAI integration
Source: https://docs.langchain.com/oss/javascript/integrations/tools/openai

Integrate with the OpenAI tool using LangChain JavaScript.

The `@langchain/openai` package provides LangChain-compatible wrappers for OpenAI's built-in tools. These tools can be bound to `ChatOpenAI` using `bindTools()` or [`createAgent`](https://reference.langchain.com/javascript/langchain/index/createAgent).

### Web search tool

The web search tool allows OpenAI models to search the web for up-to-date information before generating a response. Web search supports three main types:

1. **Non-reasoning web search**: Quick lookups where the model passes queries directly to the search tool
2. **Agentic search with reasoning models**: The model actively manages the search process, analyzing results and deciding whether to keep searching
3. **Deep research**: Extended investigations using models like `o3-deep-research` or `gpt-5` with high reasoning effort

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { ChatOpenAI, tools } from "@langchain/openai";

const model = new ChatOpenAI({
  model: "gpt-5.5",
});

// Basic usage
const response = await model.invoke(
  "What was a positive news story from today?",
  {
    tools: [tools.webSearch()],
  }
);
```

**Domain filtering** - Limit search results to specific domains (up to 100):

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const response = await model.invoke("Latest AI research news", {
  tools: [
    tools.webSearch({
      filters: {
        allowedDomains: ["arxiv.org", "nature.com", "science.org"],
      },
    }),
  ],
});
```

**User location** - Refine search results based on geography:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const response = await model.invoke("What are the best restaurants near me?", {
  tools: [
    tools.webSearch({
      userLocation: {
        type: "approximate",
        country: "US",
        city: "San Francisco",
        region: "California",
        timezone: "America/Los_Angeles",
      },
    }),
  ],
});
```

**Cache-only mode** - Disable live internet access:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const response = await model.invoke("Find information about OpenAI", {
  tools: [
    tools.webSearch({
      externalWebAccess: false,
    }),
  ],
});
```

For more information, see [OpenAI's Web Search Documentation](https://platform.openai.com/docs/guides/tools-web-search).

### MCP tool (Model context protocol)

The MCP tool allows OpenAI models to connect to remote MCP servers and OpenAI-maintained service connectors, giving models access to external tools and services.

There are two ways to use MCP tools:

1. **Remote MCP servers**: Connect to any public MCP server via URL
2. **Connectors**: Use OpenAI-maintained wrappers for popular services like Google Workspace or Dropbox

**Remote MCP server** - Connect to any MCP-compatible server:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { ChatOpenAI, tools } from "@langchain/openai";

const model = new ChatOpenAI({ model: "gpt-5.5" });

const response = await model.invoke("Roll 2d4+1", {
  tools: [
    tools.mcp({
      serverLabel: "dmcp",
      serverDescription: "A D&D MCP server for dice rolling",
      serverUrl: "https://dmcp-server.deno.dev/sse",
      requireApproval: "never",
    }),
  ],
});
```

**Service connectors** - Use OpenAI-maintained connectors for popular services:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const response = await model.invoke("What's on my calendar today?", {
  tools: [
    tools.mcp({
      serverLabel: "google_calendar",
      connectorId: "connector_googlecalendar",
      authorization: "<oauth-access-token>",
      requireApproval: "never",
    }),
  ],
});
```

For more information, see [OpenAI's MCP Documentation](https://platform.openai.com/docs/guides/tools-remote-mcp).

### Code interpreter tool

The Code Interpreter tool allows models to write and run Python code in a sandboxed environment to solve complex problems.

Use Code Interpreter for:

* **Data analysis**: Processing files with diverse data and formatting
* **File generation**: Creating files with data and images of graphs
* **Iterative coding**: Writing and running code iteratively to solve problems
* **Visual intelligence**: Cropping, zooming, rotating, and transforming images

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { ChatOpenAI, tools } from "@langchain/openai";

const model = new ChatOpenAI({ model: "gpt-5.5" });

// Basic usage with auto container (default 1GB memory)
const response = await model.invoke("Solve the equation 3x + 11 = 14", {
  tools: [tools.codeInterpreter()],
});
```

**Memory configuration** - Choose from 1GB (default), 4GB, 16GB, or 64GB:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const response = await model.invoke(
  "Analyze this large dataset and create visualizations",
  {
    tools: [
      tools.codeInterpreter({
        container: { memoryLimit: "4g" },
      }),
    ],
  }
);
```

**With files** - Make uploaded files available to the code:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const response = await model.invoke("Process the uploaded CSV file", {
  tools: [
    tools.codeInterpreter({
      container: {
        memoryLimit: "4g",
        fileIds: ["file-abc123", "file-def456"],
      },
    }),
  ],
});
```

**Explicit container** - Use a pre-created container ID:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const response = await model.invoke("Continue working with the data", {
  tools: [
    tools.codeInterpreter({
      container: "cntr_abc123",
    }),
  ],
});
```

> **Note**: Containers expire after 20 minutes of inactivity. While called "Code Interpreter", the model knows it as the "python tool" - for explicit prompting, ask for "the python tool" in your prompts.

For more information, see [OpenAI's Code Interpreter Documentation](https://platform.openai.com/docs/guides/tools-code-interpreter).

### File search tool

The File Search tool allows models to search your files for relevant information using semantic and keyword search. It enables retrieval from a knowledge base of previously uploaded files stored in vector stores.

**Prerequisites**: Before using File Search, you must:

1. Upload files to the File API with `purpose: "assistants"`
2. Create a vector store
3. Add files to the vector store

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { ChatOpenAI, tools } from "@langchain/openai";

const model = new ChatOpenAI({ model: "gpt-5.5" });

const response = await model.invoke("What is deep research by OpenAI?", {
  tools: [
    tools.fileSearch({
      vectorStoreIds: ["vs_abc123"],
      // maxNumResults: 5, // Limit results for lower latency
      // filters: { type: "eq", key: "category", value: "blog" }, // Metadata filtering
      // filters: { type: "and", filters: [                       // Compound filters (AND/OR)
      //   { type: "eq", key: "category", value: "technical" },
      //   { type: "gte", key: "year", value: 2024 },
      // ]},
      // rankingOptions: { scoreThreshold: 0.8, ranker: "auto" }, // Customize scoring
    }),
  ],
});
```

Filter operators: `eq` (equals), `ne` (not equal), `gt` (greater than), `gte` (greater than or equal), `lt` (less than), `lte` (less than or equal).

For more information, see [OpenAI's File Search Documentation](https://platform.openai.com/docs/guides/tools-file-search).

### Image generation tool

The Image Generation tool allows models to generate or edit images using text prompts and optional image inputs. It leverages the GPT Image model and automatically optimizes text inputs for improved performance.

Use Image Generation for:

* **Creating images from text**: Generate images from detailed text descriptions
* **Editing existing images**: Modify images based on text instructions
* **Multi-turn image editing**: Iteratively refine images across conversation turns
* **Various output formats**: Support for PNG, JPEG, and WebP formats

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { ChatOpenAI, tools } from "@langchain/openai";

const model = new ChatOpenAI({ model: "gpt-5.5" });

// Basic usage - generate an image
const response = await model.invoke(
  "Generate an image of a gray tabby cat hugging an otter with an orange scarf",
  { tools: [tools.imageGeneration()] }
);

// Access the generated image (base64-encoded)
const imageOutput = response.additional_kwargs.tool_outputs?.find(
  (output) => output.type === "image_generation_call"
);
if (imageOutput?.result) {
  const fs = await import("fs");
  fs.writeFileSync("output.png", Buffer.from(imageOutput.result, "base64"));
}
```

**Custom size and quality** - Configure output dimensions and quality:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const response = await model.invoke("Draw a beautiful sunset over mountains", {
  tools: [
    tools.imageGeneration({
      size: "1536x1024", // Landscape format (also: "1024x1024", "1024x1536", "auto")
      quality: "high", // Quality level (also: "low", "medium", "auto")
    }),
  ],
});
```

**Output format and compression** - Choose format and compression level:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const response = await model.invoke("Create a product photo", {
  tools: [
    tools.imageGeneration({
      outputFormat: "jpeg", // Format (also: "png", "webp")
      outputCompression: 90, // Compression 0-100 (for JPEG/WebP)
    }),
  ],
});
```

**Transparent background** - Generate images with transparency:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const response = await model.invoke(
  "Create a logo with transparent background",
  {
    tools: [
      tools.imageGeneration({
        background: "transparent", // Background type (also: "opaque", "auto")
        outputFormat: "png",
      }),
    ],
  }
);
```

**Streaming with partial images** - Get visual feedback during generation:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const response = await model.invoke("Draw a detailed fantasy castle", {
  tools: [
    tools.imageGeneration({
      partialImages: 2, // Number of partial images (0-3)
    }),
  ],
});
```

**Force image generation** - Ensure the model uses the image generation tool:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const response = await model.invoke("A serene lake at dawn", {
  tools: [tools.imageGeneration()],
  tool_choice: { type: "image_generation" },
});
```

**Multi-turn editing** - Refine images across conversation turns:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
// First turn: generate initial image
const response1 = await model.invoke("Draw a red car", {
  tools: [tools.imageGeneration()],
});

// Second turn: edit the image
const response2 = await model.invoke(
  [response1, new HumanMessage("Now change the car color to blue")],
  { tools: [tools.imageGeneration()] }
);
```

> **Prompting tips**: Use terms like "draw" or "edit" for best results. For combining images, say "edit the first image by adding this element" instead of "combine" or "merge".

Supported models: `gpt-4o`, `gpt-4o-mini`, `gpt-5.5`, `gpt-5.4-mini`, `gpt-5.4-nano`, `o3`

For more information, see [OpenAI's Image Generation Documentation](https://platform.openai.com/docs/guides/tools-image-generation).

### Computer use tool

The Computer Use tool allows models to control computer interfaces by simulating mouse clicks, keyboard input, scrolling, and more. It uses OpenAI's Computer-Using Agent (CUA) model to understand screenshots and suggest actions.

> **Beta**: Computer use is in beta. Use in sandboxed environments only and do not use for high-stakes or authenticated tasks. Always implement human-in-the-loop for important decisions.

**How it works**: The tool operates in a continuous loop:

1. Model sends computer actions (click, type, scroll, etc.)
2. Your code executes these actions in a controlled environment
3. You capture a screenshot of the result
4. Send the screenshot back to the model
5. Repeat until the task is complete

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { ChatOpenAI, tools } from "@langchain/openai";

const model = new ChatOpenAI({ model: "computer-use-preview" });

// With execute callback for automatic action handling
const computer = tools.computerUse({
  displayWidth: 1024,
  displayHeight: 768,
  environment: "browser",
  execute: async (action) => {
    if (action.type === "screenshot") {
      return captureScreenshot();
    }
    if (action.type === "click") {
      await page.mouse.click(action.x, action.y, { button: action.button });
      return captureScreenshot();
    }
    if (action.type === "type") {
      await page.keyboard.type(action.text);
      return captureScreenshot();
    }
    if (action.type === "scroll") {
      await page.mouse.move(action.x, action.y);
      await page.evaluate(
        `window.scrollBy(${action.scroll_x}, ${action.scroll_y})`
      );
      return captureScreenshot();
    }
    // Handle other actions...
    return captureScreenshot();
  },
});

const llmWithComputer = model.bindTools([computer]);
const response = await llmWithComputer.invoke(
  "Check the latest news on bing.com"
);
```

For more information, see [OpenAI's Computer Use Documentation](https://platform.openai.com/docs/guides/tools-computer-use).

### Local shell tool

The Local Shell tool allows models to run shell commands locally on a machine you provide. Commands are executed inside your own runtime—the API only returns the instructions.

> **Security Warning**: Running arbitrary shell commands can be dangerous. Always sandbox execution or add strict allow/deny-lists before forwarding commands to the system shell.
> **Note**: This tool is designed to work with [Codex CLI](https://github.com/openai/codex) and the `codex-mini-latest` model.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { ChatOpenAI, tools } from "@langchain/openai";
import { exec } from "child_process";
import { promisify } from "util";

const execAsync = promisify(exec);
const model = new ChatOpenAI({ model: "codex-mini-latest" });

// With execute callback for automatic command handling
const shell = tools.localShell({
  execute: async (action) => {
    const { command, env, working_directory, timeout_ms } = action;
    const result = await execAsync(command.join(" "), {
      cwd: working_directory ?? process.cwd(),
      env: { ...process.env, ...env },
      timeout: timeout_ms ?? undefined,
    });
    return result.stdout + result.stderr;
  },
});

const llmWithShell = model.bindTools([shell]);
const response = await llmWithShell.invoke(
  "List files in the current directory"
);
```

**Action properties**: The model returns actions with these properties:

* `command` - Array of argv tokens to execute
* `env` - Environment variables to set
* `working_directory` - Directory to run the command in
* `timeout_ms` - Suggested timeout (enforce your own limits)
* `user` - Optional user to run the command as

For more information, see [OpenAI's Local Shell Documentation](https://platform.openai.com/docs/guides/tools-local-shell).

### Shell tool

The Shell tool allows models to run shell commands through your integration. Unlike Local Shell, this tool supports executing multiple commands concurrently and is designed for `gpt-5.1`.

> **Security Warning**: Running arbitrary shell commands can be dangerous. Always sandbox execution or add strict allow/deny-lists before forwarding commands to the system shell.

**Use cases**:

* **Automating filesystem or process diagnostics** – e.g., "find the largest PDF under \~/Documents"
* **Extending model capabilities** – Using built-in UNIX utilities, Python runtime, and other CLIs
* **Running multi-step build and test flows** – Chaining commands like `pip install` and `pytest`
* **Complex agentic coding workflows** – Using with `apply_patch` for file operations

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { ChatOpenAI, tools } from "@langchain/openai";
import { exec } from "node:child_process/promises";

const model = new ChatOpenAI({ model: "gpt-5.1" });

// With execute callback for automatic command handling
const shellTool = tools.shell({
  execute: async (action) => {
    const outputs = await Promise.all(
      action.commands.map(async (cmd) => {
        try {
          const { stdout, stderr } = await exec(cmd, {
            timeout: action.timeout_ms ?? undefined,
          });
          return {
            stdout,
            stderr,
            outcome: { type: "exit" as const, exit_code: 0 },
          };
        } catch (error) {
          const timedOut = error.killed && error.signal === "SIGTERM";
          return {
            stdout: error.stdout ?? "",
            stderr: error.stderr ?? String(error),
            outcome: timedOut
              ? { type: "timeout" as const }
              : { type: "exit" as const, exit_code: error.code ?? 1 },
          };
        }
      })
    );
    return {
      output: outputs,
      maxOutputLength: action.max_output_length,
    };
  },
});

const llmWithShell = model.bindTools([shellTool]);
const response = await llmWithShell.invoke(
  "Find the largest PDF file in ~/Documents"
);
```

**Action properties**: The model returns actions with these properties:

* `commands` - Array of shell commands to execute (can run concurrently)
* `timeout_ms` - Optional timeout in milliseconds (enforce your own limits)
* `max_output_length` - Optional maximum characters to return per command

**Return format**: Your execute function should return a `ShellResult`:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
interface ShellResult {
  output: Array<{
    stdout: string;
    stderr: string;
    outcome: { type: "exit"; exit_code: number } | { type: "timeout" };
  }>;
  maxOutputLength?: number | null; // Pass back from action if provided
}
```

> **Note**: Only available through the Responses API with `gpt-5.1`. The `timeout_ms` from the model is only a hint—always enforce your own limits.

For more information, see [OpenAI's Shell Documentation](https://platform.openai.com/docs/guides/tools-shell).

### Apply patch tool

The Apply Patch tool allows models to propose structured diffs that your integration applies. This enables iterative, multi-step code editing workflows where the model can create, update, and delete files in your codebase.

**When to use**:

* **Multi-file refactors** – Rename symbols, extract helpers, or reorganize modules
* **Bug fixes** – Have the model both diagnose issues and emit precise patches
* **Tests & docs generation** – Create new test files, fixtures, and documentation
* **Migrations & mechanical edits** – Apply repetitive, structured updates

> **Security Warning**: Applying patches can modify files in your codebase. Always validate paths, implement backups, and consider sandboxing.
> **Note**: This tool is designed to work with `gpt-5.1` model.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { ChatOpenAI, tools } from "@langchain/openai";
import { applyDiff } from "@openai/agents";
import * as fs from "fs/promises";

const model = new ChatOpenAI({ model: "gpt-5.1" });

// With execute callback for automatic patch handling
const patchTool = tools.applyPatch({
  execute: async (operation) => {
    if (operation.type === "create_file") {
      const content = applyDiff("", operation.diff, "create");
      await fs.writeFile(operation.path, content);
      return `Created ${operation.path}`;
    }
    if (operation.type === "update_file") {
      const current = await fs.readFile(operation.path, "utf-8");
      const newContent = applyDiff(current, operation.diff);
      await fs.writeFile(operation.path, newContent);
      return `Updated ${operation.path}`;
    }
    if (operation.type === "delete_file") {
      await fs.unlink(operation.path);
      return `Deleted ${operation.path}`;
    }
    return "Unknown operation type";
  },
});

const llmWithPatch = model.bindTools([patchTool]);
const response = await llmWithPatch.invoke(
  "Rename the fib() function to fibonacci() in lib/fib.py"
);
```

**Operation types**: The model returns operations with these properties:

* `create_file` – Create a new file at `path` with content from `diff`
* `update_file` – Modify an existing file at `path` using V4A diff format in `diff`
* `delete_file` – Remove a file at `path`

**Best practices**:

* **Path validation**: Prevent directory traversal and restrict edits to allowed directories
* **Backups**: Consider backing up files before applying patches
* **Error handling**: Return descriptive error messages so the model can recover
* **Atomicity**: Decide whether you want "all-or-nothing" semantics (rollback if any patch fails)

For more information, see [OpenAI's Apply Patch Documentation](https://platform.openai.com/docs/guides/tools-apply-patch).

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/javascript/integrations/tools/openai.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Vector store integrations
Source: https://docs.langchain.com/oss/javascript/integrations/vectorstores/index

Integrate with vector stores using LangChain JavaScript.

## Overview

A [vector store](/oss/javascript/integrations/vectorstores) stores [embedded](/oss/javascript/integrations/embeddings) data and performs similarity search.

```mermaid theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
flowchart LR

    subgraph "📥 Indexing phase (store)"
        A[📄 Documents] --> B[🔢 Embedding model]
        B --> C[🔘 Embedding vectors]
        C --> D[(Vector store)]
    end

    subgraph "📤 Query phase (retrieval)"
        E[❓ Query text] --> F[🔢 Embedding model]
        F --> G[🔘 Query vector]
        G --> H[🔍 Similarity search]
        H --> D
        D --> I[📄 Top-k results]
    end

    classDef process fill:#E5F4FF,stroke:#006DDD,stroke-width:2px,color:#030710
    class A,B,C,D,E,F,G,H,I process
```

### Interface

LangChain provides a unified interface for vector stores, allowing you to:

* `addDocuments` - Add documents to the store.
* `delete` - Remove stored documents by ID.
* `similaritySearch` - Query for semantically similar documents.

This abstraction lets you switch between different implementations without altering your application logic.

### Initialization

Most vectorstores in LangChain accept an embedding model as an argument when initializing the vector store.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { OpenAIEmbeddings } from "@langchain/openai";
import { MemoryVectorStore } from "@langchain/classic/vectorstores/memory";

const embeddings = new OpenAIEmbeddings({
  model: "text-embedding-3-small",
});
const vectorStore = new MemoryVectorStore(embeddings);
```

### Adding documents

You can add documents to the vector store by using the `addDocuments` function.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { Document } from "@langchain/core/documents";
const document = new Document({
  pageContent: "Hello world",
});
await vectorStore.addDocuments([document]);
```

### Deleting documents

You can delete documents from the vector store by using the `delete` function.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
await vectorStore.delete({
  filter: {
    pageContent: "Hello world",
  },
});
```

### Similarity search

Issue a semantic query using `similaritySearch`, which returns the closest embedded documents:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const results = await vectorStore.similaritySearch("Hello world", 10);
```

Many vector stores support parameters like:

* `k` — number of results to return
* `filter` — conditional filtering based on metadata

### Similarity metrics & indexing

Embedding similarity may be computed using:

* **Cosine similarity**
* **Euclidean distance**
* **Dot product**

Efficient search often employs indexing methods such as HNSW (Hierarchical Navigable Small World), though specifics depend on the vector store.

### Metadata filtering

Filtering by metadata (e.g., source, date) can refine search results:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
vectorStore.similaritySearch("query", 2, { source: "tweets" });
```

<important>
  Support for metadata-based filtering varies between implementations.
  Check the documentation of your chosen vector store for details.
</important>

## Top integrations

**Select embedding model:**

<AccordionGroup>
  <Accordion title="OpenAI">
    Install dependencies:

    <CodeGroup>
      ```bash npm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      npm install @langchain/openai @langchain/core
      ```

      ```bash yarn theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      yarn add @langchain/openai @langchain/core
      ```

      ```bash pnpm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      pnpm add @langchain/openai @langchain/core
      ```
    </CodeGroup>

    Add environment variables:

    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    OPENAI_API_KEY=your-api-key
    ```

    Instantiate the model:

    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { OpenAIEmbeddings } from "@langchain/openai";

    const embeddings = new OpenAIEmbeddings({
      model: "text-embedding-3-large"
    });
    ```
  </Accordion>

  <Accordion title="Azure">
    Install dependencies

    <CodeGroup>
      ```bash npm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      npm install @langchain/openai @langchain/core
      ```

      ```bash yarn theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      yarn add @langchain/openai @langchain/core
      ```

      ```bash pnpm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      pnpm add @langchain/openai @langchain/core
      ```
    </CodeGroup>

    Add environment variables:

    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    AZURE_OPENAI_API_INSTANCE_NAME=<YOUR_INSTANCE_NAME>
    AZURE_OPENAI_API_KEY=<YOUR_KEY>
    AZURE_OPENAI_API_VERSION="2024-02-01"
    ```

    Instantiate the model:

    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { AzureOpenAIEmbeddings } from "@langchain/openai";

    const embeddings = new AzureOpenAIEmbeddings({
      azureOpenAIApiEmbeddingsDeploymentName: "text-embedding-ada-002"
    });
    ```
  </Accordion>

  <Accordion title="AWS">
    Install dependencies:

    <CodeGroup>
      ```bash npm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      npm i @langchain/aws
      ```

      ```bash yarn theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      yarn add @langchain/aws
      ```

      ```bash pnpm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      pnpm add @langchain/aws
      ```
    </CodeGroup>

    Add environment variables:

    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    BEDROCK_AWS_REGION=your-region
    ```

    Instantiate the model:

    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { BedrockEmbeddings } from "@langchain/aws";

    const embeddings = new BedrockEmbeddings({
      model: "amazon.titan-embed-text-v1"
    });
    ```
  </Accordion>

  <Accordion title="Google Gemini">
    Install dependencies:

    <CodeGroup>
      ```bash npm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      npm i @langchain/google-genai
      ```

      ```bash yarn theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      yarn add @langchain/google-genai
      ```

      ```bash pnpm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      pnpm add @langchain/google-genai
      ```
    </CodeGroup>

    Add environment variables:

    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    GOOGLE_API_KEY=your-api-key
    ```

    Instantiate the model:

    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { GoogleGenerativeAIEmbeddings } from "@langchain/google-genai";

    const embeddings = new GoogleGenerativeAIEmbeddings({
      model: "text-embedding-004"
    });
    ```
  </Accordion>

  <Accordion title="Google Vertex">
    Install dependencies:

    <CodeGroup>
      ```bash npm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      npm i @langchain/google-vertexai
      ```

      ```bash yarn theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      yarn add @langchain/google-vertexai
      ```

      ```bash pnpm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      pnpm add @langchain/google-vertexai
      ```
    </CodeGroup>

    Add environment variables:

    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    GOOGLE_APPLICATION_CREDENTIALS=credentials.json
    ```

    Instantiate the model:

    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { VertexAIEmbeddings } from "@langchain/google-vertexai";

    const embeddings = new VertexAIEmbeddings({
      model: "gemini-embedding-001"
    });
    ```
  </Accordion>

  <Accordion title="MistralAI">
    Install dependencies:

    <CodeGroup>
      ```bash npm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      npm install @langchain/mistralai @langchain/core
      ```

      ```bash yarn theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      yarn add @langchain/mistralai @langchain/core
      ```

      ```bash pnpm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      pnpm add @langchain/mistralai @langchain/core
      ```
    </CodeGroup>

    Add environment variables:

    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    MISTRAL_API_KEY=your-api-key
    ```

    Instantiate the model:

    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { MistralAIEmbeddings } from "@langchain/mistralai";

    const embeddings = new MistralAIEmbeddings({
      model: "mistral-embed"
    });
    ```
  </Accordion>

  <Accordion title="Cohere">
    Install dependencies:

    <CodeGroup>
      ```bash npm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      npm i @langchain/cohere
      ```

      ```bash yarn theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      yarn add @langchain/cohere
      ```

      ```bash pnpm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      pnpm add @langchain/cohere
      ```
    </CodeGroup>

    Add environment variables:

    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    COHERE_API_KEY=your-api-key
    ```

    Instantiate the model:

    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { CohereEmbeddings } from "@langchain/cohere";

    const embeddings = new CohereEmbeddings({
      model: "embed-english-v3.0"
    });
    ```
  </Accordion>

  <Accordion title="Ollama">
    Install dependencies:

    <CodeGroup>
      ```bash npm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      npm install @langchain/ollama @langchain/core
      ```

      ```bash yarn theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      yarn add @langchain/ollama @langchain/core
      ```

      ```bash pnpm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      pnpm add @langchain/ollama @langchain/core
      ```
    </CodeGroup>

    Instantiate the model:

    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { OllamaEmbeddings } from "@langchain/ollama";

    const embeddings = new OllamaEmbeddings({
      model: "llama2",
      baseUrl: "http://localhost:11434", // Default value
    });
    ```
  </Accordion>
</AccordionGroup>

**Select vector store:**

<AccordionGroup>
  <Accordion title="Memory">
    <CodeGroup>
      ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      npm i langchain
      ```

      ```bash yarn theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      yarn add langchain
      ```

      ```bash pnpm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      pnpm add langchain
      ```
    </CodeGroup>

    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { MemoryVectorStore } from "@langchain/classic/vectorstores/memory";

    const vectorStore = new MemoryVectorStore(embeddings);
    ```
  </Accordion>

  <Accordion title="MongoDB">
    <Tabs>
      <Tab title="Manual embedding">
        <CodeGroup>
          ```bash npm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
          npm install @langchain/mongodb mongodb @langchain/core
          ```

          ```bash yarn theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
          yarn add @langchain/mongodb mongodb @langchain/core
          ```

          ```bash pnpm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
          pnpm add @langchain/mongodb mongodb @langchain/core
          ```
        </CodeGroup>

        ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
        import { MongoDBAtlasVectorSearch } from "@langchain/mongodb"
        import { MongoClient } from "mongodb";

        const client = new MongoClient(process.env.MONGODB_ATLAS_URI!);
        const collection = client
          .db(process.env.MONGODB_ATLAS_DB_NAME)
          .collection(process.env.MONGODB_ATLAS_COLLECTION_NAME);

        const vectorStore = new MongoDBAtlasVectorSearch(embeddings, {
          collection,
          indexName: "vector_index",
          textKey: "text",
          embeddingKey: "embedding",
        });
        ```
      </Tab>

      <Tab title="Automated embedding">
        <CodeGroup>
          ```bash npm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
          npm install @langchain/mongodb mongodb @langchain/core
          ```

          ```bash yarn theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
          yarn add @langchain/mongodb mongodb @langchain/core
          ```

          ```bash pnpm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
          pnpm add @langchain/mongodb mongodb @langchain/core
          ```
        </CodeGroup>

        ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
        import { MongoDBAtlasVectorSearch } from "@langchain/mongodb"
        import { MongoClient } from "mongodb";

        const client = new MongoClient(process.env.MONGODB_ATLAS_URI!);
        const collection = client
          .db(process.env.MONGODB_ATLAS_DB_NAME)
          .collection(process.env.MONGODB_ATLAS_COLLECTION_NAME);

        const vectorStore = new MongoDBAtlasVectorSearch({ collection });
        ```
      </Tab>
    </Tabs>
  </Accordion>

  <Accordion title="Pinecone">
    <CodeGroup>
      ```bash npm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      npm install @langchain/pinecone @langchain/core @pinecone-database/pinecone
      ```

      ```bash yarn theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      yarn add @langchain/pinecone @langchain/core @pinecone-database/pinecone
      ```

      ```bash pnpm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      pnpm add @langchain/pinecone @langchain/core @pinecone-database/pinecone
      ```
    </CodeGroup>

    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { PineconeStore } from "@langchain/pinecone";
    import { Pinecone as PineconeClient } from "@pinecone-database/pinecone";

    const pinecone = new PineconeClient();
    const vectorStore = new PineconeStore(embeddings, {
      pineconeIndex,
      maxConcurrency: 5,
    });
    ```
  </Accordion>

  <Accordion title="Redis">
    <CodeGroup>
      ```bash npm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      npm install @langchain/redis @langchain/core redis
      ```

      ```bash yarn theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      yarn add @langchain/redis @langchain/core redis
      ```

      ```bash pnpm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      pnpm add @langchain/redis @langchain/core redis
      ```
    </CodeGroup>

    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { RedisVectorStore } from "@langchain/redis";

    const vectorStore = new RedisVectorStore(embeddings, {
      redisClient: client,
      indexName: "langchainjs-testing",
    });
    ```
  </Accordion>

  <Accordion title="Qdrant">
    <CodeGroup>
      ```bash npm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      npm install @langchain/qdrant @langchain/core
      ```

      ```bash yarn theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      yarn add @langchain/qdrant @langchain/core
      ```

      ```bash pnpm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      pnpm add @langchain/qdrant @langchain/core
      ```
    </CodeGroup>

    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { QdrantVectorStore } from "@langchain/qdrant";

    const vectorStore = await QdrantVectorStore.fromExistingCollection(embeddings, {
      url: process.env.QDRANT_URL,
      collectionName: "langchainjs-testing",
    });
    ```
  </Accordion>

  <Accordion title="Oracle AI Database">
    <CodeGroup>
      ```bash npm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      npm i @oracle/langchain-oracledb @langchain/core
      ```

      ```bash yarn theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      yarn add @oracle/langchain-oracledb @langchain/core
      ```

      ```bash pnpm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      pnpm add @oracle/langchain-oracledb @langchain/core
      ```
    </CodeGroup>

    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import oracledb from "oracledb";
    import { OracleEmbeddings, OracleVS } from "@oracle/langchain-oracledb";

    const connection = await oracledb.getConnection({
      user: process.env.ORACLE_USER,
      password: process.env.ORACLE_PASSWORD,
      connectionString: process.env.ORACLE_DSN,
    });

    const embeddings = new OracleEmbeddings(connection, {
      provider: "database",
      model: process.env.DEMO_ONNX_MODEL ?? "DEMO_MODEL",
    });

    const vectorStore = new OracleVS(embeddings, {
      client: connection,
      tableName: "DEMO_VECTORS",
      query: "Find support tickets mentioning service outages.",
      distanceStrategy: "DOT",
    });
    await vectorStore.initialize();
    ```
  </Accordion>

  <Accordion title="Weaviate">
    <CodeGroup>
      ```bash npm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      npm install @langchain/weaviate @langchain/core weaviate-client
      ```

      ```bash yarn theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      yarn add @langchain/weaviate @langchain/core weaviate-client
      ```

      ```bash pnpm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      pnpm add @langchain/weaviate @langchain/core weaviate-client
      ```
    </CodeGroup>

    <CodeGroup>
      ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { WeaviateStore } from "@langchain/weaviate";

      const vectorStore = new WeaviateStore(embeddings, {
          client: weaviateClient,
          indexName: "Langchainjs_test",
      });
      ```
    </CodeGroup>
  </Accordion>
</AccordionGroup>

LangChain.js integrates with a variety of vector stores. You can check out a full list below:

## All vector stores

<Columns>
  <Card title="Azure DocumentDB" icon="link" href="/oss/javascript/integrations/vectorstores/azure_documentdb" />

  <Card title="Azure Cosmos DB for NoSQL" icon="link" href="/oss/javascript/integrations/vectorstores/azure_cosmosdb_nosql" />

  <Card title="Cloudflare Vectorize" icon="link" href="/oss/javascript/integrations/vectorstores/cloudflare_vectorize" />

  <Card title="Google Cloud SQL for PostgreSQL" icon="link" href="/oss/javascript/integrations/vectorstores/google_cloudsql_pg" />

  <Card title="In-memory" icon="link" href="/oss/javascript/integrations/vectorstores/memory" />

  <Card title="Milvus" icon="link" href="/oss/javascript/integrations/vectorstores/milvus" />

  <Card title="MongoDB Atlas" icon="link" href="/oss/javascript/integrations/vectorstores/mongodb_atlas" />

  <Card title="Oracle AI Database" icon="link" href="/oss/javascript/integrations/vectorstores/oracleai" />

  <Card title="Pinecone" icon="link" href="/oss/javascript/integrations/vectorstores/pinecone" />

  <Card title="Qdrant" icon="link" href="/oss/javascript/integrations/vectorstores/qdrant" />

  <Card title="Redis" icon="link" href="/oss/javascript/integrations/vectorstores/redis" />

  <Card title="Weaviate" icon="link" href="/oss/javascript/integrations/vectorstores/weaviate" />

  <Card title="Neo4j Vector Index" icon="link" href="/oss/javascript/integrations/vectorstores/neo4jvector" />

  <Card title="PGVector" icon="link" href="/oss/javascript/integrations/vectorstores/pgvector" />

  <Card title="Turbopuffer" icon="link" href="/oss/javascript/integrations/vectorstores/turbopuffer" />

  <Card title="YDB" icon="link" href="/oss/javascript/integrations/vectorstores/ydb" />
</Columns>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/javascript/integrations/vectorstores/index.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# LangChain Academy
Source: https://docs.langchain.com/oss/javascript/langchain/academy

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/academy.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
