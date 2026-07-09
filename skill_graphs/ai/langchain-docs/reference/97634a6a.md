      }),
    },
  );

  const researchSubagent: SubAgent = {
    name: "research-agent",
    description: "Used to research more in depth questions",
    systemPrompt: "You are a great researcher",
    tools: [internetSearch],
    model: "fireworks:accounts/fireworks/models/qwen3p5-397b-a17b", // Optional override, defaults to main agent model
  };
  const subagents = [researchSubagent];

  const agent = createDeepAgent({
    model: "google_genai:gemini-3.5-flash",
    subagents,
  });
  ```

  ```ts Baseten theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { tool } from "langchain";
  import { TavilySearch } from "@langchain/tavily";
  import { createDeepAgent, type SubAgent } from "deepagents";
  import { z } from "zod";

  const internetSearch = tool(
    async ({
      query,
      maxResults = 5,
      topic = "general",
      includeRawContent = false,
    }: {
      query: string;
      maxResults?: number;
      topic?: "general" | "news" | "finance";
      includeRawContent?: boolean;
    }) => {
      const tavilySearch = new TavilySearch({
        maxResults,
        tavilyApiKey: process.env.TAVILY_API_KEY,
        includeRawContent,
        topic,
      });
      return await tavilySearch._call({ query });
    },
    {
      name: "internet_search",
      description: "Run a web search",
      schema: z.object({
        query: z.string().describe("The search query"),
        maxResults: z.number().optional().default(5),
        topic: z
          .enum(["general", "news", "finance"])
          .optional()
          .default("general"),
        includeRawContent: z.boolean().optional().default(false),
      }),
    },
  );

  const researchSubagent: SubAgent = {
    name: "research-agent",
    description: "Used to research more in depth questions",
    systemPrompt: "You are a great researcher",
    tools: [internetSearch],
    model: "baseten:zai-org/GLM-5", // Optional override, defaults to main agent model
  };
  const subagents = [researchSubagent];

  const agent = createDeepAgent({
    model: "google_genai:gemini-3.5-flash",
    subagents,
  });
  ```

  ```ts Ollama theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { tool } from "langchain";
  import { TavilySearch } from "@langchain/tavily";
  import { createDeepAgent, type SubAgent } from "deepagents";
  import { z } from "zod";

  const internetSearch = tool(
    async ({
      query,
      maxResults = 5,
      topic = "general",
      includeRawContent = false,
    }: {
      query: string;
      maxResults?: number;
      topic?: "general" | "news" | "finance";
      includeRawContent?: boolean;
    }) => {
      const tavilySearch = new TavilySearch({
        maxResults,
        tavilyApiKey: process.env.TAVILY_API_KEY,
        includeRawContent,
        topic,
      });
      return await tavilySearch._call({ query });
    },
    {
      name: "internet_search",
      description: "Run a web search",
      schema: z.object({
        query: z.string().describe("The search query"),
        maxResults: z.number().optional().default(5),
        topic: z
          .enum(["general", "news", "finance"])
          .optional()
          .default("general"),
        includeRawContent: z.boolean().optional().default(false),
      }),
    },
  );

  const researchSubagent: SubAgent = {
    name: "research-agent",
    description: "Used to research more in depth questions",
    systemPrompt: "You are a great researcher",
    tools: [internetSearch],
    model: "ollama:devstral-2", // Optional override, defaults to main agent model
  };
  const subagents = [researchSubagent];

  const agent = createDeepAgent({
    model: "google_genai:gemini-3.5-flash",
    subagents,
  });
  ```
</CodeGroup>

## Using CompiledSubAgent

For more complex use cases, you can provide your custom subagents with [`CompiledSubAgent`](https://reference.langchain.com/javascript/deepagents/middleware/CompiledSubAgent).
You can create a custom subagent using LangChain's [`create_agent`](https://reference.langchain.com/javascript/langchain/index/createAgent) or by making a custom LangGraph graph using the [graph API](/oss/javascript/langgraph/graph-api).

If you're creating a custom LangGraph graph, make sure that the graph has a [state key called `"messages"`](/oss/javascript/langgraph/quickstart#2-define-state):

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { createDeepAgent, CompiledSubAgent } from "deepagents";
import { createAgent } from "langchain";

// Create a custom agent graph
const customGraph = createAgent({
  model: yourModel,
  tools: specializedTools,
  prompt: "You are a specialized agent for data analysis...",
});

// Use it as a custom subagent
const customSubagent: CompiledSubAgent = {
  name: "data-analyzer",
  description: "Specialized agent for complex data analysis tasks",
  runnable: customGraph,
};

const subagents = [customSubagent];

const agent = createDeepAgent({
  model: "google_genai:gemini-3.5-flash",
  tools: [internetSearch],
  systemPrompt: researchInstructions,
  subagents: subagents,
});
```

## Streaming

Deep Agents support streaming updates from both the coordinator and every delegated subagent.

Use [`streamEvents`](/oss/javascript/deepagents/event-streaming) to get typed projections—separate iterators for subagents, messages, tool calls, and values—so you can consume each independently.

### Stream subagent progress

The simplest pattern is to iterate `stream.subagents` to track each delegated task as it starts, runs, and completes. Each subagent handle exposes `.name`, `.messages`, `.tool_calls`, and `.output`.

<CodeGroup>
  ```ts Google theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createDeepAgent } from "deepagents";

  const agent = createDeepAgent({
    model: "google-genai:gemini-3.5-flash",
    systemPrompt:
      "You are a project coordinator with no research knowledge. " +
      "For every user request, you must call the task() tool with " +
      "subagent_type set to research-agent. Never answer research " +
      "questions yourself.",
    subagents: [
      {
        name: "research-agent",
        description:
          "Delegate research to this subagent. Give one topic at a time.",
        systemPrompt: "You are a great researcher. Return a brief summary.",
      },
    ],
  });

  async function streamSubagentProgress() {
    const stream = await agent.streamEvents(
      {
        messages: [
          {
            role: "user",
            content: "Research one recent advance in quantum computing.",
          },
        ],
      },
      { version: "v3" },
    );

    const coordinatorMessages: string[] = [];
    const subagentHandles: { name: string }[] = [];

    await Promise.all([
      (async () => {
        for await (const message of stream.messages) {
          console.log("[coordinator]", await message.text);
          coordinatorMessages.push(await message.text);
        }
      })(),
      (async () => {
        for await (const subagent of stream.subagents) {
          console.log(`[${subagent.name}] started`);
          subagentHandles.push({ name: subagent.name });
          for await (const message of subagent.messages) {
            console.log(`[${subagent.name}]`, await message.text);
          }
        }
      })(),
    ]);

    return { coordinatorMessages, subagentHandles };
  }
  ```

  ```ts OpenAI theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createDeepAgent } from "deepagents";

  const agent = createDeepAgent({
    model: "openai:gpt-5.5",
    systemPrompt:
      "You are a project coordinator with no research knowledge. " +
      "For every user request, you must call the task() tool with " +
      "subagent_type set to research-agent. Never answer research " +
      "questions yourself.",
    subagents: [
      {
        name: "research-agent",
        description:
          "Delegate research to this subagent. Give one topic at a time.",
        systemPrompt: "You are a great researcher. Return a brief summary.",
      },
    ],
  });

  async function streamSubagentProgress() {
    const stream = await agent.streamEvents(
      {
        messages: [
          {
            role: "user",
            content: "Research one recent advance in quantum computing.",
          },
        ],
      },
      { version: "v3" },
    );

    const coordinatorMessages: string[] = [];
    const subagentHandles: { name: string }[] = [];

    await Promise.all([
      (async () => {
        for await (const message of stream.messages) {
          console.log("[coordinator]", await message.text);
          coordinatorMessages.push(await message.text);
        }
      })(),
      (async () => {
        for await (const subagent of stream.subagents) {
          console.log(`[${subagent.name}] started`);
          subagentHandles.push({ name: subagent.name });
          for await (const message of subagent.messages) {
            console.log(`[${subagent.name}]`, await message.text);
          }
        }
      })(),
    ]);

    return { coordinatorMessages, subagentHandles };
  }
  ```

  ```ts Anthropic theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createDeepAgent } from "deepagents";

  const agent = createDeepAgent({
    model: "anthropic:claude-sonnet-4-6",
    systemPrompt:
      "You are a project coordinator with no research knowledge. " +
      "For every user request, you must call the task() tool with " +
      "subagent_type set to research-agent. Never answer research " +
      "questions yourself.",
    subagents: [
      {
        name: "research-agent",
        description:
          "Delegate research to this subagent. Give one topic at a time.",
        systemPrompt: "You are a great researcher. Return a brief summary.",
      },
    ],
  });

  async function streamSubagentProgress() {
    const stream = await agent.streamEvents(
      {
        messages: [
          {
            role: "user",
            content: "Research one recent advance in quantum computing.",
          },
        ],
      },
      { version: "v3" },
    );

    const coordinatorMessages: string[] = [];
    const subagentHandles: { name: string }[] = [];

    await Promise.all([
      (async () => {
        for await (const message of stream.messages) {
          console.log("[coordinator]", await message.text);
          coordinatorMessages.push(await message.text);
        }
      })(),
      (async () => {
        for await (const subagent of stream.subagents) {
          console.log(`[${subagent.name}] started`);
          subagentHandles.push({ name: subagent.name });
          for await (const message of subagent.messages) {
            console.log(`[${subagent.name}]`, await message.text);
          }
        }
      })(),
    ]);

    return { coordinatorMessages, subagentHandles };
  }
  ```

  ```ts OpenRouter theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createDeepAgent } from "deepagents";

  const agent = createDeepAgent({
    model: "openrouter:anthropic/claude-sonnet-4-6",
    systemPrompt:
      "You are a project coordinator with no research knowledge. " +
      "For every user request, you must call the task() tool with " +
      "subagent_type set to research-agent. Never answer research " +
      "questions yourself.",
    subagents: [
      {
        name: "research-agent",
        description:
          "Delegate research to this subagent. Give one topic at a time.",
        systemPrompt: "You are a great researcher. Return a brief summary.",
      },
    ],
  });

  async function streamSubagentProgress() {
    const stream = await agent.streamEvents(
      {
        messages: [
          {
            role: "user",
            content: "Research one recent advance in quantum computing.",
          },
        ],
      },
      { version: "v3" },
    );

    const coordinatorMessages: string[] = [];
    const subagentHandles: { name: string }[] = [];

    await Promise.all([
      (async () => {
        for await (const message of stream.messages) {
          console.log("[coordinator]", await message.text);
          coordinatorMessages.push(await message.text);
        }
      })(),
      (async () => {
        for await (const subagent of stream.subagents) {
          console.log(`[${subagent.name}] started`);
          subagentHandles.push({ name: subagent.name });
          for await (const message of subagent.messages) {
            console.log(`[${subagent.name}]`, await message.text);
          }
        }
      })(),
    ]);

    return { coordinatorMessages, subagentHandles };
  }
  ```

  ```ts Fireworks theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createDeepAgent } from "deepagents";

  const agent = createDeepAgent({
    model: "fireworks:accounts/fireworks/models/qwen3p5-397b-a17b",
    systemPrompt:
      "You are a project coordinator with no research knowledge. " +
      "For every user request, you must call the task() tool with " +
      "subagent_type set to research-agent. Never answer research " +
      "questions yourself.",
    subagents: [
      {
        name: "research-agent",
        description:
          "Delegate research to this subagent. Give one topic at a time.",
        systemPrompt: "You are a great researcher. Return a brief summary.",
      },
    ],
  });

  async function streamSubagentProgress() {
    const stream = await agent.streamEvents(
      {
        messages: [
          {
            role: "user",
            content: "Research one recent advance in quantum computing.",
          },
        ],
      },
      { version: "v3" },
    );

    const coordinatorMessages: string[] = [];
    const subagentHandles: { name: string }[] = [];

    await Promise.all([
      (async () => {
        for await (const message of stream.messages) {
          console.log("[coordinator]", await message.text);
          coordinatorMessages.push(await message.text);
        }
      })(),
      (async () => {
        for await (const subagent of stream.subagents) {
          console.log(`[${subagent.name}] started`);
          subagentHandles.push({ name: subagent.name });
          for await (const message of subagent.messages) {
            console.log(`[${subagent.name}]`, await message.text);
          }
        }
      })(),
    ]);

    return { coordinatorMessages, subagentHandles };
  }
  ```

  ```ts Baseten theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createDeepAgent } from "deepagents";

  const agent = createDeepAgent({
    model: "baseten:zai-org/GLM-5",
    systemPrompt:
      "You are a project coordinator with no research knowledge. " +
      "For every user request, you must call the task() tool with " +
      "subagent_type set to research-agent. Never answer research " +
      "questions yourself.",
    subagents: [
      {
        name: "research-agent",
        description:
          "Delegate research to this subagent. Give one topic at a time.",
        systemPrompt: "You are a great researcher. Return a brief summary.",
      },
    ],
  });

  async function streamSubagentProgress() {
    const stream = await agent.streamEvents(
      {
        messages: [
          {
            role: "user",
            content: "Research one recent advance in quantum computing.",
          },
        ],
      },
      { version: "v3" },
    );

    const coordinatorMessages: string[] = [];
    const subagentHandles: { name: string }[] = [];

    await Promise.all([
      (async () => {
        for await (const message of stream.messages) {
          console.log("[coordinator]", await message.text);
          coordinatorMessages.push(await message.text);
        }
      })(),
      (async () => {
        for await (const subagent of stream.subagents) {
          console.log(`[${subagent.name}] started`);
          subagentHandles.push({ name: subagent.name });
          for await (const message of subagent.messages) {
            console.log(`[${subagent.name}]`, await message.text);
          }
        }
      })(),
    ]);

    return { coordinatorMessages, subagentHandles };
  }
  ```

  ```ts Ollama theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createDeepAgent } from "deepagents";

  const agent = createDeepAgent({
    model: "ollama:devstral-2",
    systemPrompt:
      "You are a project coordinator with no research knowledge. " +
      "For every user request, you must call the task() tool with " +
      "subagent_type set to research-agent. Never answer research " +
      "questions yourself.",
    subagents: [
      {
        name: "research-agent",
        description:
          "Delegate research to this subagent. Give one topic at a time.",
        systemPrompt: "You are a great researcher. Return a brief summary.",
      },
    ],
  });

  async function streamSubagentProgress() {
    const stream = await agent.streamEvents(
      {
        messages: [
          {
            role: "user",
            content: "Research one recent advance in quantum computing.",
          },
        ],
      },
      { version: "v3" },
    );

    const coordinatorMessages: string[] = [];
    const subagentHandles: { name: string }[] = [];

    await Promise.all([
      (async () => {
        for await (const message of stream.messages) {
          console.log("[coordinator]", await message.text);
          coordinatorMessages.push(await message.text);
        }
      })(),
      (async () => {
        for await (const subagent of stream.subagents) {
          console.log(`[${subagent.name}] started`);
          subagentHandles.push({ name: subagent.name });
          for await (const message of subagent.messages) {
            console.log(`[${subagent.name}]`, await message.text);
          }
        }
      })(),
    ]);

    return { coordinatorMessages, subagentHandles };
  }
  ```
</CodeGroup>

### LangSmith tracing

As your deep agent runs, all runs executed by a subagent or the coordinator will have the agent name in their metadata under the `lc_agent_name` key—for example, `{'lc_agent_name': 'research-agent'}`. This lets you identify and filter runs by subagent in LangSmith.

<img alt="LangSmith Example trace showing the metadata" />

<Tip>
  Open the run in [LangSmith](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=oss-deepagents-subagents) to compare the coordinator trace with each subagent run. Follow the [observability quickstart](/langsmith/observability-quickstart) to get set up. We recommend you also set up [LangSmith Engine](/langsmith/engine) which monitors your traces, detects issues, and proposes fixes.
</Tip>

## Filter by subagent in LangSmith

Because each subagent's `name` is written to the `lc_agent_name` metadata key on every run it produces, you can use LangSmith's metadata filtering to isolate all runs from a specific subagent — useful for debugging, monitoring, or comparing subagent behavior over time.

### Filter in the LangSmith UI

1. Open your tracing project in [LangSmith](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=oss-deepagents-subagents).
2. Switch the view to **Runs** on the Tracing project page to see individual spans.
3. Click **Add filter** and select **Metadata**.
4. Set the **Key** to `lc_agent_name` and the **Value** to the subagent name (for example, `research-agent`).

This shows only the runs produced by that subagent. You can save the filter as a named view for reuse. For a full reference on filtering options, see [Filter traces](/langsmith/filter-traces-in-application).

### Filter programmatically with the SDK

Use the `has` comparator in the LangSmith filter query language to match runs by metadata key-value pair:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langsmith import Client

client = Client()

runs = client.list_runs(
    project_name="<your-project>",
    filter='has(metadata, \'{"lc_agent_name": "research-agent"}\')',
)

for run in runs:
    print(run.name, run.start_time, run.status)
```

To fetch runs from *any* named subagent (excluding the main agent), filter for runs that have the `lc_agent_name` key at all:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
runs = client.list_runs(
    project_name="<your-project>",
    filter="has(metadata, 'lc_agent_name')",
)
```

For the full filter query language reference, see [Trace query syntax](/langsmith/trace-query-syntax).

## Structured output

Subagents support [structured output](/oss/javascript/langchain/structured-output), so the parent agent receives predictable, parseable JSON instead of free-form text.

<Note>
  Structured output for subagents requires `deepagents>=1.8.4`.
</Note>

Pass `responseFormat` on the subagent config. When the subagent finishes, its structured response is JSON-serialized and returned as the `ToolMessage` content to the parent agent. The schema accepts anything supported by `createAgent`: Zod schemas, JSON schema objects, `toolStrategy(...)`, or `providerStrategy(...)`.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { z } from "zod";
import { createDeepAgent } from "deepagents";

const ResearchFindings = z.object({
  summary: z.string().describe("Summary of findings"),
  confidence: z.number().describe("Confidence score from 0 to 1"),
  sources: z.array(z.string()).describe("List of source URLs"),
});

const researchSubagent = {
  name: "researcher",
  description: "Researches topics and returns structured findings",
  systemPrompt: "Research the given topic thoroughly. Return your findings.",
  tools: [webSearch],
  responseFormat: ResearchFindings,
};

const agent = createDeepAgent({
  model: "claude-sonnet-4-6",
  subagents: [researchSubagent],
});

const result = await agent.invoke({
  messages: [{ role: "user", content: "Research recent advances in quantum computing" }],
});

// The parent's ToolMessage contains JSON-serialized structured data:
// '{"summary": "...", "confidence": 0.87, "sources": ["https://..."]}'
```

Without `response_format`, the parent receives the subagent's last message text as-is. With it, the parent always gets valid JSON matching the schema, which is useful when the parent needs to process the result programmatically or pass it to downstream tools.

For full details on schema types and strategies (tool calling vs. provider-native), see [Structured output](/oss/javascript/langchain/structured-output).

## The general-purpose subagent

In addition to any user-defined subagents, every deep agent has access to a `general-purpose` subagent at all times. This subagent:

* Uses its own [default system prompt with profile overlays applied](/oss/javascript/deepagents/customization#prompt-assembly)
* Has access to all the same tools
* Uses the same model (unless overridden)
* Inherits skills from the main agent (when skills are configured)

### Override the general-purpose subagent

Include a subagent with `name: "general-purpose"` in your `subagents` list to replace the default. Use this to configure a different model, tools, or system prompt for the general-purpose subagent:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { createDeepAgent } from "deepagents";

// Main agent uses Gemini; general-purpose subagent uses GPT
const agent = await createDeepAgent({
  model: "google_genai:gemini-3.5-flash",
  tools: [internetSearch],
  subagents: [
    {
      name: "general-purpose",
      description: "General-purpose agent for research and multi-step tasks",
      systemPrompt: "You are a general-purpose assistant.",
      tools: [internetSearch],
      model: "openai:gpt-5.5",  // Different model for delegated tasks
    },
  ],
});
```

When you provide a subagent with the general-purpose name, the default general-purpose subagent is not added. Your spec fully replaces it.

To remove the built-in general-purpose subagent entirely instead of replacing it, set the active harness profile's general-purpose subagent `enabled` flag to `False`.

### When to use it

The general-purpose subagent is ideal for context isolation without specialized behavior. The main agent can delegate a complex multi-step task to this subagent and get a concise result back without bloat from intermediate tool calls.

<Card title="Example">
  Instead of the main agent making 10 web searches and filling its context with results, it delegates to the general-purpose subagent: `task(name="general-purpose", task="Research quantum computing trends")`. The subagent performs all the searches internally and returns only a summary.
</Card>

### Skills inheritance

When configuring [skills](/oss/javascript/deepagents/skills) with `create_deep_agent`:

* **General-purpose subagent**: Automatically inherits skills from the main agent
* **Custom subagents**: Do NOT inherit skills by default—use the `skills` parameter to give them their own skills

<Note>
  Only subagents configured with skills get a `SkillsMiddleware` instance—custom subagents without a `skills` parameter do not. When present, skill state is fully isolated in both directions: the parent's skills are not visible to the child, and the child's skills are not propagated back to the parent.
