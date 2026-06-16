# Build a deep research agent
Source: https://docs.langchain.com/oss/javascript/deepagents/deep-research

Build a multi-step web research agent with subagent delegation

## Overview

This guide demonstrates how to build a multi-step web research agent from scratch using [Deep Agents](/oss/javascript/deepagents). The agent decomposes research questions into focused tasks, delegates them to specialized sub-agents, and synthesizes findings into a comprehensive report.

The agent you build will:

1. Plan research using a todo list
2. Delegate focused research tasks to sub-agents with isolated context
3. Assess search results and plan next steps as you gather information
4. Synthesize findings with proper citations into a final report

The spawned sub-agents will conduct web searches with Tavily, fetching full webpage content for analysis.

### Key concepts

This tutorial covers:

* [Subagents](/oss/javascript/deepagents/subagents) for parallel, context-isolated research
* Custom [tools](/oss/javascript/langchain/tools) for web search
* Multi-step planning with the [built-in planning tool](/oss/javascript/deepagents/harness#task-planning)

## Prerequisites

API keys for:

* Anthropic (Claude) or Google (Gemini)
* [Tavily](https://www.tavily.com/) for web search (optional - free tier sufficient)
* [LangSmith](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=oss-deepagents-deep-research) for tracing (optional)

## Setup

<Steps>
  <Step title="Create project directory">
    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    mkdir deep-research-agent
    cd deep-research-agent
    ```
  </Step>

  <Step title="Install dependencies">
    <Tabs>
      <Tab title="Claude">
        ```bash npm wrap theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
        npm install deepagents @langchain/anthropic @langchain/core
        ```
      </Tab>

      <Tab title="Gemini">
        ```bash npm wrap theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
        npm install deepagents @langchain/google-genai @langchain/core
        ```
      </Tab>
    </Tabs>
  </Step>

  <Step title="Set API keys">
    <Tabs>
      <Tab title="Claude">
        ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
        export ANTHROPIC_API_KEY="your_anthropic_api_key"
        export TAVILY_API_KEY="your_tavily_api_key"
        export LANGSMITH_API_KEY="your_langsmith_api_key"   # Optional
        ```
      </Tab>

      <Tab title="Gemini">
        ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
        export GOOGLE_API_KEY="your_google_api_key"
        export TAVILY_API_KEY="your_tavily_api_key"
        export LANGSMITH_API_KEY="your_langsmith_api_key"   # Optional
        ```
      </Tab>
    </Tabs>
  </Step>
</Steps>

## Build the agent

Create `agent.ts` in your project directory:

<Steps>
  <Step title="Add tools">
    Add the custom search tool. The `tavily_search` tool uses Tavily for URL discovery, then fetches full webpage content so the agent can analyze complete sources instead of summaries.

    ```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { tool } from "langchain";
    import { z } from "zod";

    async function fetchWebpageContent(
      url: string,
      timeout = 10_000,
    ): Promise<string> {
      try {
        const controller = new AbortController();
        const id = setTimeout(() => controller.abort(), timeout);
        const response = await fetch(url, {
          headers: {
            "User-Agent":
              "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
          },
          signal: controller.signal,
        });
        clearTimeout(id);
        if (!response.ok) {
          return `Error fetching ${url}: HTTP ${response.status}`;
        }
        return await response.text();
      } catch (e) {
        return `Error fetching ${url}: ${e}`;
      }
    }

    const tavilySearch = tool(
      async ({
        query,
        maxResults = 1,
        topic = "general",
      }: {
        query: string;
        maxResults?: number;
        topic?: "general" | "news" | "finance";
      }) => {
        const response = await fetch("https://api.tavily.com/search", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${process.env.TAVILY_API_KEY}`,
          },
          body: JSON.stringify({ query, max_results: maxResults, topic }),
        });
        const data = (await response.json()) as {
          results: Array<{ url: string; title: string }>;
        };
        const results = data.results ?? [];
        const resultTexts: string[] = [];
        for (const result of results) {
          const content = await fetchWebpageContent(result.url);
          resultTexts.push(
            `## ${result.title}\n**URL:** ${result.url}\n\n${content}\n---`,
          );
        }
        return (
          `Found ${resultTexts.length} result(s) for '${query}':\n\n` +
          resultTexts.join("\n")
        );
      },
      {
        name: "tavily_search",
        description:
          "Search the web for information on a given query. Uses Tavily to discover relevant URLs, then fetches and returns full webpage content.",
        schema: z.object({
          query: z.string().describe("Search query to execute"),
          maxResults: z
            .number()
            .optional()
            .default(1)
            .describe("Maximum number of results to return (default: 1)"),
          topic: z
            .enum(["general", "news", "finance"])
            .optional()
            .default("general")
            .describe(
              "Topic filter - 'general', 'news', or 'finance' (default: 'general')",
            ),
        }),
      },
    );
    ```
  </Step>

  <Step title="Add prompts">
    Add the orchestrator workflow and sub-agent prompt templates to `agent.ts`:

    ```ts expandable wrap theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    const RESEARCH_WORKFLOW_INSTRUCTIONS = `# Research Workflow

    Follow this workflow for all research requests:

    1. **Plan**: Create a todo list with write_todos to break down the research into focused tasks
    2. **Save the request**: Use write_file() to save the user's research question to \`/research_request.md\`
    3. **Research**: Delegate research tasks to sub-agents using the task() tool - ALWAYS use sub-agents for research, never conduct research yourself
    4. **Synthesize**: Review all sub-agent findings and consolidate citations (each unique URL gets one number across all findings)
    5. **Write Report**: Write a comprehensive final report to \`/final_report.md\` (see Report Writing Guidelines below)
    6. **Verify**: Read \`/research_request.md\` and confirm you've addressed all aspects with proper citations and structure

    ## Research Planning Guidelines
    - Batch similar research tasks into a single TODO to minimize overhead
    - For simple fact-finding questions, use 1 sub-agent
    - For comparisons or multi-faceted topics, delegate to multiple parallel sub-agents
    - Each sub-agent should research one specific aspect and return findings

    ## Report Writing Guidelines

    When writing the final report to \`/final_report.md\`, follow these structure patterns:

    **For comparisons:**
    1. Introduction
    2. Overview of topic A
    3. Overview of topic B
    4. Detailed comparison
    5. Conclusion

    **For lists/rankings:**
    Simply list items with details - no introduction needed:
    1. Item 1 with explanation
    2. Item 2 with explanation
    3. Item 3 with explanation

    **For summaries/overviews:**
    1. Overview of topic
    2. Key concept 1
    3. Key concept 2
    4. Key concept 3
    5. Conclusion

    **General guidelines:**
    - Use clear section headings (## for sections, ### for subsections)
    - Write in paragraph form by default - be text-heavy, not just bullet points
    - Do NOT use self-referential language ("I found...", "I researched...")
    - Write as a professional report without meta-commentary
    - Each section should be comprehensive and detailed
    - Use bullet points only when listing is more appropriate than prose

    **Citation format:**
    - Cite sources inline using [1], [2], [3] format
    - Assign each unique URL a single citation number across ALL sub-agent findings
    - End report with ### Sources section listing each numbered source
    - Number sources sequentially without gaps (1,2,3,4...)
    - Format: [1] Source Title: URL (each on separate line for proper list rendering)
    - Example:

     Some important finding [1]. Another key insight [2].

     ### Sources
     [1] AI Research Paper: https://example.com/paper
     [2] Industry Analysis: https://example.com/analysis
    `;
    ```

    ```ts expandable wrap theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    const RESEARCHER_INSTRUCTIONS = `You are a research assistant conducting research on the user's input topic. For context, today's date is {date}.

    Your job is to use tools to gather information about the user's input topic.
    You can use the tavily_search tool to find resources that can help answer the research question.
    You can call it in series or in parallel, your research is conducted in a tool-calling loop.

    You have access to the tavily_search tool for conducting web searches.

    Think like a human researcher with limited time. Follow these steps:

    1. **Read the question carefully** - What specific information does the user need?
    2. **Start with broader searches** - Use broad, comprehensive queries first
    3. **After each search, pause and assess** - Do I have enough to answer? What's still missing?
    4. **Execute narrower searches as you gather information** - Fill in the gaps
    5. **Stop when you can answer confidently** - Don't keep searching for perfection

    **Tool Call Budgets** (Prevent excessive searching):
    - **Simple queries**: Use 2-3 search tool calls maximum
    - **Complex queries**: Use up to 5 search tool calls maximum
    - **Always stop**: After 5 search tool calls if you cannot find the right sources

    **Stop Immediately When**:
    - You can answer the user's question comprehensively
    - You have 3+ relevant examples/sources for the question
    - Your last 2 searches returned similar information

    After each search, assess results before continuing: What key information did I find? What's missing? Do I have enough to answer? Should I search more or provide my answer?

    When providing your findings back to the orchestrator:

    1. **Structure your response**: Organize findings with clear headings and detailed explanations
    2. **Cite sources inline**: Use [1], [2], [3] format when referencing information from your searches
    3. **Include Sources section**: End with ### Sources listing each numbered source with title and URL

    Example:
    ## Key Findings
    Context engineering is a critical technique for AI agents [1]. Studies show that proper context management can improve performance by 40% [2].

    ### Sources
    [1] Context Engineering Guide: https://example.com/context-guide
    [2] AI Performance Study: https://example.com/study

    The orchestrator will consolidate citations from all sub-agents into the final report.
    `;
    ```

    ```ts expandable wrap theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    const SUBAGENT_DELEGATION_INSTRUCTIONS = `# Sub-Agent Research Coordination

    Your role is to coordinate research by delegating tasks from your TODO list to specialized research sub-agents.

    ## Delegation Strategy

    **DEFAULT: Start with 1 sub-agent** for most queries:
    - "What is quantum computing?" -> 1 sub-agent (general overview)
    - "List the top 10 coffee shops in San Francisco" -> 1 sub-agent
    - "Summarize the history of the internet" -> 1 sub-agent
    - "Research context engineering for AI agents" -> 1 sub-agent (covers all aspects)

    **ONLY parallelize when the query EXPLICITLY requires comparison or has clearly independent aspects:**

    **Explicit comparisons** -> 1 sub-agent per element:
    - "Compare OpenAI vs Anthropic vs DeepMind AI safety approaches" -> 3 parallel sub-agents
    - "Compare Python vs JavaScript for web development" -> 2 parallel sub-agents

    **Clearly separated aspects** -> 1 sub-agent per aspect (use sparingly):
    - "Research renewable energy adoption in Europe, Asia, and North America" -> 3 parallel sub-agents (geographic separation)
    - Only use this pattern when aspects cannot be covered efficiently by a single comprehensive search

    ## Key Principles
    - **Bias towards single sub-agent**: One comprehensive research task is more token-efficient than multiple narrow ones
    - **Avoid premature decomposition**: Don't break "research X" into "research X overview", "research X techniques", "research X applications" - just use 1 sub-agent for all of X
    - **Parallelize only for clear comparisons**: Use multiple sub-agents when comparing distinct entities or geographically separated data

    ## Parallel Execution Limits
    - Use at most {maxConcurrentResearchUnits} parallel sub-agents per iteration
    - Make multiple task() calls in a single response to enable parallel execution
    - Each sub-agent returns findings independently

    ## Research Limits
    - Stop after {maxResearcherIterations} delegation rounds if you haven't found adequate sources
    - Stop when you have sufficient information to answer comprehensively
    - Bias towards focused research over exhaustive exploration`;
    ```
  </Step>

  <Step title="Create the agent">
    Add the model initialization and agent creation to `agent.ts`:

    <CodeGroup>
      ```ts Google theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { createDeepAgent } from "deepagents";
      import { ChatAnthropic } from "@langchain/anthropic";

      const maxConcurrentResearchUnits = 3;
      const maxResearcherIterations = 3;

      const currentDate = new Date().toISOString().split("T")[0];

      const INSTRUCTIONS =
        RESEARCH_WORKFLOW_INSTRUCTIONS +
        "\n\n" +
        "=".repeat(80) +
        "\n\n" +
        SUBAGENT_DELEGATION_INSTRUCTIONS.replace(
          "{maxConcurrentResearchUnits}",
          String(maxConcurrentResearchUnits),
        ).replace("{maxResearcherIterations}", String(maxResearcherIterations));

      const researchSubAgent = {
        name: "research-agent",
        description: "Delegate research to the sub-agent. Give one topic at a time.",
        systemPrompt: RESEARCHER_INSTRUCTIONS.replace("{date}", currentDate),
        tools: [tavilySearch],
      };

      const model = new ChatAnthropic({
        model: "google-genai:gemini-3.5-flash",
        temperature: 0,
      });

      const agent = createDeepAgent({
        model,
        tools: [tavilySearch],
        systemPrompt: INSTRUCTIONS,
        subagents: [researchSubAgent],
      });
      ```

      ```ts OpenAI theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { createDeepAgent } from "deepagents";
      import { ChatAnthropic } from "@langchain/anthropic";

      const maxConcurrentResearchUnits = 3;
      const maxResearcherIterations = 3;

      const currentDate = new Date().toISOString().split("T")[0];

      const INSTRUCTIONS =
        RESEARCH_WORKFLOW_INSTRUCTIONS +
        "\n\n" +
        "=".repeat(80) +
        "\n\n" +
        SUBAGENT_DELEGATION_INSTRUCTIONS.replace(
          "{maxConcurrentResearchUnits}",
          String(maxConcurrentResearchUnits),
        ).replace("{maxResearcherIterations}", String(maxResearcherIterations));

      const researchSubAgent = {
        name: "research-agent",
        description: "Delegate research to the sub-agent. Give one topic at a time.",
        systemPrompt: RESEARCHER_INSTRUCTIONS.replace("{date}", currentDate),
        tools: [tavilySearch],
      };

      const model = new ChatAnthropic({
        model: "openai:gpt-5.5",
        temperature: 0,
      });

      const agent = createDeepAgent({
        model,
        tools: [tavilySearch],
        systemPrompt: INSTRUCTIONS,
        subagents: [researchSubAgent],
      });
      ```

      ```ts Anthropic theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { createDeepAgent } from "deepagents";
      import { ChatAnthropic } from "@langchain/anthropic";

      const maxConcurrentResearchUnits = 3;
      const maxResearcherIterations = 3;

      const currentDate = new Date().toISOString().split("T")[0];

      const INSTRUCTIONS =
        RESEARCH_WORKFLOW_INSTRUCTIONS +
        "\n\n" +
        "=".repeat(80) +
        "\n\n" +
        SUBAGENT_DELEGATION_INSTRUCTIONS.replace(
          "{maxConcurrentResearchUnits}",
          String(maxConcurrentResearchUnits),
        ).replace("{maxResearcherIterations}", String(maxResearcherIterations));

      const researchSubAgent = {
        name: "research-agent",
        description: "Delegate research to the sub-agent. Give one topic at a time.",
        systemPrompt: RESEARCHER_INSTRUCTIONS.replace("{date}", currentDate),
        tools: [tavilySearch],
      };

      const model = new ChatAnthropic({
        model: "anthropic:claude-sonnet-4-6",
        temperature: 0,
      });

      const agent = createDeepAgent({
        model,
        tools: [tavilySearch],
        systemPrompt: INSTRUCTIONS,
        subagents: [researchSubAgent],
      });
      ```

      ```ts OpenRouter theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { createDeepAgent } from "deepagents";
      import { ChatAnthropic } from "@langchain/anthropic";

      const maxConcurrentResearchUnits = 3;
      const maxResearcherIterations = 3;

      const currentDate = new Date().toISOString().split("T")[0];

      const INSTRUCTIONS =
        RESEARCH_WORKFLOW_INSTRUCTIONS +
        "\n\n" +
        "=".repeat(80) +
        "\n\n" +
        SUBAGENT_DELEGATION_INSTRUCTIONS.replace(
          "{maxConcurrentResearchUnits}",
          String(maxConcurrentResearchUnits),
        ).replace("{maxResearcherIterations}", String(maxResearcherIterations));

      const researchSubAgent = {
        name: "research-agent",
        description: "Delegate research to the sub-agent. Give one topic at a time.",
        systemPrompt: RESEARCHER_INSTRUCTIONS.replace("{date}", currentDate),
        tools: [tavilySearch],
      };

      const model = new ChatAnthropic({
        model: "openrouter:anthropic/claude-sonnet-4-6",
        temperature: 0,
      });

      const agent = createDeepAgent({
        model,
        tools: [tavilySearch],
        systemPrompt: INSTRUCTIONS,
        subagents: [researchSubAgent],
      });
      ```

      ```ts Fireworks theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { createDeepAgent } from "deepagents";
      import { ChatAnthropic } from "@langchain/anthropic";

      const maxConcurrentResearchUnits = 3;
      const maxResearcherIterations = 3;

      const currentDate = new Date().toISOString().split("T")[0];

      const INSTRUCTIONS =
        RESEARCH_WORKFLOW_INSTRUCTIONS +
        "\n\n" +
        "=".repeat(80) +
        "\n\n" +
        SUBAGENT_DELEGATION_INSTRUCTIONS.replace(
          "{maxConcurrentResearchUnits}",
          String(maxConcurrentResearchUnits),
        ).replace("{maxResearcherIterations}", String(maxResearcherIterations));

      const researchSubAgent = {
        name: "research-agent",
        description: "Delegate research to the sub-agent. Give one topic at a time.",
        systemPrompt: RESEARCHER_INSTRUCTIONS.replace("{date}", currentDate),
        tools: [tavilySearch],
      };

      const model = new ChatAnthropic({
        model: "fireworks:accounts/fireworks/models/qwen3p5-397b-a17b",
        temperature: 0,
      });

      const agent = createDeepAgent({
        model,
        tools: [tavilySearch],
        systemPrompt: INSTRUCTIONS,
        subagents: [researchSubAgent],
      });
      ```

      ```ts Baseten theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { createDeepAgent } from "deepagents";
      import { ChatAnthropic } from "@langchain/anthropic";

      const maxConcurrentResearchUnits = 3;
      const maxResearcherIterations = 3;

      const currentDate = new Date().toISOString().split("T")[0];

      const INSTRUCTIONS =
        RESEARCH_WORKFLOW_INSTRUCTIONS +
        "\n\n" +
        "=".repeat(80) +
        "\n\n" +
        SUBAGENT_DELEGATION_INSTRUCTIONS.replace(
          "{maxConcurrentResearchUnits}",
          String(maxConcurrentResearchUnits),
        ).replace("{maxResearcherIterations}", String(maxResearcherIterations));

      const researchSubAgent = {
        name: "research-agent",
        description: "Delegate research to the sub-agent. Give one topic at a time.",
        systemPrompt: RESEARCHER_INSTRUCTIONS.replace("{date}", currentDate),
        tools: [tavilySearch],
      };

      const model = new ChatAnthropic({
        model: "baseten:zai-org/GLM-5",
        temperature: 0,
      });

      const agent = createDeepAgent({
        model,
        tools: [tavilySearch],
        systemPrompt: INSTRUCTIONS,
        subagents: [researchSubAgent],
      });
      ```

      ```ts Ollama theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { createDeepAgent } from "deepagents";
      import { ChatAnthropic } from "@langchain/anthropic";

      const maxConcurrentResearchUnits = 3;
      const maxResearcherIterations = 3;

      const currentDate = new Date().toISOString().split("T")[0];

      const INSTRUCTIONS =
        RESEARCH_WORKFLOW_INSTRUCTIONS +
        "\n\n" +
        "=".repeat(80) +
        "\n\n" +
        SUBAGENT_DELEGATION_INSTRUCTIONS.replace(
          "{maxConcurrentResearchUnits}",
          String(maxConcurrentResearchUnits),
        ).replace("{maxResearcherIterations}", String(maxResearcherIterations));

      const researchSubAgent = {
        name: "research-agent",
        description: "Delegate research to the sub-agent. Give one topic at a time.",
        systemPrompt: RESEARCHER_INSTRUCTIONS.replace("{date}", currentDate),
        tools: [tavilySearch],
      };

      const model = new ChatAnthropic({
        model: "ollama:devstral-2",
        temperature: 0,
      });

      const agent = createDeepAgent({
        model,
        tools: [tavilySearch],
        systemPrompt: INSTRUCTIONS,
        subagents: [researchSubAgent],
      });
      ```
    </CodeGroup>
  </Step>
</Steps>

## Run the agent

You can run the agent synchronously, meaning it will wait for the full result and then print it, or you can stream updates as they come in.

Add the code from the respective tab at the bottom of `agent.ts`:

<Tabs>
  <Tab title="Run synchronously">
    ```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    {
      async function main() {
        const result = await agent.invoke({
          messages: [
            {
              role: "user",
              content:
                "What are the main differences between RAG and fine-tuning for LLM applications?",
            },
          ],
        });

        for (const msg of result.messages ?? []) {
          if (msg.content) {
            console.log(msg.content);
          }
        }
      }

      main().catch((err) => {
        console.error(err);
        process.exitCode = 1;
      });
    }
    ```
  </Tab>

  <Tab title="Stream updates">
    ```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    {
      async function main() {
        for await (const chunk of await agent.stream(
          {
            messages: [
              {
                role: "user",
                content: "Compare Python vs JavaScript for web development",
              },
            ],
          },
          { streamMode: "updates" },
        )) {
          for (const [, update] of Object.entries(chunk)) {
            const messages = (update as any)?.messages;
            if (!messages) continue;
            const msgList = Array.isArray(messages) ? messages : [messages];
            for (const msg of msgList) {
              if (msg.content) {
                console.log(msg.content);
              }
            }
          }
        }
      }

      main().catch((err) => {
        console.error(err);
        process.exitCode = 1;
      });
    }
    ```
  </Tab>
</Tabs>

Run the agent from the project root:

```sh theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
npx tsx agent.ts
```

If you set the `LANGSMITH_API_KEY` environment variable before running, you can view the agent's traces in [LangSmith](/langsmith/observability) to debug and monitor multi-step behavior.

## Full code

View the complete [Deep Research example](https://github.com/langchain-ai/deepagents/tree/main/examples/deep_research) on GitHub.

## Next steps

Now that you've built the agent, customize it by changing the prompt constants in your agent file to adjust the workflow, delegation strategy, or researcher behavior.
You can also tune the delegation limits to allow for more parallel sub-agents or delegation rounds.

For more information on the concepts in this tutorial, check out the following resources:

* [Subagents](/oss/javascript/deepagents/subagents): Learn how to configure subagents with different tools and prompts
* [Customization](/oss/javascript/deepagents/customization): Customize models, tools, system prompts, and planning behavior
* [LangSmith](/langsmith/observability): Trace research runs and debug multi-step behavior
* [Deep Research Course](https://academy.langchain.com/courses/deep-research-with-langgraph): Full course on deep research with LangGraph

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/deepagents/deep-research.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Event streaming
Source: https://docs.langchain.com/oss/javascript/deepagents/event-streaming

Stream subagents, messages, tool calls, and final output from Deep Agents.

This page covers streaming concerns specific to Deep Agents—most importantly, streaming from delegated subagents via `stream.subagents`. For general agent streaming (`stream.messages`, `stream.values`, tool calls, custom updates), see [LangChain Event Streaming](/oss/javascript/langchain/event-streaming).

## Stream subagents

Deep Agents add a subagent projection on top of LangGraph streaming. Use `stream.subagents` when you want one stream handle per delegated `task` call. The projection is lightweight: it discovers subagent tasks first, and message, tool-call, and value streams are opened only when you access them on a subagent handle.

Each handle's `name` is the sub-agent's configured name: the `subagent_type` the coordinator passes when it calls the `task` tool. Deep Agents binds that name to the delegated run, so the same label you defined in your subagent specs is what you filter and route on in the stream.

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const stream = await agent.streamEvents(
  { messages: [{ role: "user", content: "Write me a haiku about the sea" }] },
  { version: "v3" }
);

for await (const subagent of stream.subagents) {
  console.log(subagent.name);
  console.log(await subagent.taskInput);

  for await (const message of subagent.messages) {
    console.log(await message.text);
  }
}
```

## Subagent stream fields

Each subagent stream exposes the same kinds of projections as the parent run, such as messages, tool calls, nested subagents, and final output. For the general parent-run streaming model, see [LangChain Event Streaming](/oss/javascript/langchain/event-streaming).

TypeScript uses camelCase projection names such as `toolCalls` and `taskInput`. Each subagent stream can expose `.messages`, `.toolCalls`, `.values`, `.subagents`, and `.output`.

| Field       | Description                                                                                |
| ----------- | ------------------------------------------------------------------------------------------ |
| `name`      | Sub-agent name, taken from the `subagent_type` the coordinator selects in its `task` call. |
| `messages`  | Messages emitted by the subagent.                                                          |
| `subagents` | Nested subagent invocations.                                                               |
| `output`    | Final subagent state, or completion signal for the delegated task.                         |
| `taskInput` | Promise for the prompt passed to the task tool.                                            |
| `toolCalls` | Tool calls scoped to the subagent.                                                         |

## Track subagent lifecycle

Use `stream.subagents` when you only need to show which subagents started and finished. You do not need to subscribe to message or value streams unless you access those projections on an individual subagent.

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const stream = await agent.streamEvents(input, { version: "v3" });

let running = 0;
let completed = 0;
let failed = 0;
const watchers: Promise<void>[] = [];

for await (const subagent of stream.subagents) {
  running += 1;
  console.log(`${subagent.name}: started`);

  watchers.push(
    subagent.output.then(
      () => {
        running -= 1;
        completed += 1;
        console.log(`${subagent.name}: completed`);
      },
      () => {
        running -= 1;
        failed += 1;
        console.log(`${subagent.name}: failed`);
      }
    )
  );
}

await Promise.all(watchers);
console.log({ running, completed, failed });
```

## Stream messages

Deep Agents can emit messages from the coordinator agent and from delegated subagents. Use `stream.messages` for top-level messages and `subagent.messages` for each delegated subagent.

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const stream = await agent.streamEvents(input, { version: "v3" });

for await (const message of stream.messages) {
  console.log("[coordinator]", await message.text);
}

for await (const subagent of stream.subagents) {
  for await (const message of subagent.messages) {
    console.log(`[${subagent.name}]`, await message.text);
  }
}
```

## Stream tool calls

Deep Agents expose tool calls at each level of the agent tree. Use the top-level `stream.tool_calls` for coordinator tools and each `subagent.tool_calls` for delegated work.

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const stream = await agent.streamEvents(input, { version: "v3" });

for await (const call of stream.toolCalls) {
  console.log("[coordinator tool]", call.name, call.input);
  console.log(await call.status);
}

for await (const subagent of stream.subagents) {
  for await (const call of subagent.toolCalls) {
    console.log(`[${subagent.name} tool]`, call.name, call.input);

    const status = await call.status;
    if (status === "finished") {
      console.log(await call.output);
    } else if (status === "error") {
      console.error(await call.error);
    }
  }
}
```

## Stream nested work

You can recurse into a subagent stream to observe nested subagents, messages, and tool calls.

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const stream = await agent.streamEvents(input, { version: "v3" });

for await (const subagent of stream.subagents) {
  console.log(`subagent ${subagent.name}: started`);

  for await (const toolCall of subagent.toolCalls) {
    console.log(`${toolCall.name}(${JSON.stringify(toolCall.input)})`);

    const status = await toolCall.status;
    if (status === "finished") {
      console.log(await toolCall.output);
    } else if (status === "error") {
      console.error(await toolCall.error);
    }
  }

  for await (const nested of subagent.subagents) {
    console.log(`nested subagent ${nested.name}: started`);
  }
}
```

## Consume concurrently

Coordinator and subagent output often interleave. Consume projections concurrently when you need live UI updates.

Use concurrent consumers in JavaScript:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const stream = await agent.streamEvents(input, { version: "v3" });

await Promise.all([
  (async () => {
    for await (const message of stream.messages) {
      console.log("[coordinator]", await message.text);
    }
  })(),
  (async () => {
    for await (const subagent of stream.subagents) {
      void (async () => {
        for await (const message of subagent.messages) {
          console.log(`[${subagent.name}]`, await message.text);
        }
      })();
    }
  })(),
]);
```

When you need exact arrival order across the coordinator and all subagents, iterate raw protocol events and use `namespace` to identify the source:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const stream = await agent.streamEvents(input, { version: "v3" });

for await (const event of stream) {
  if (event.method !== "messages") continue;

  const data = event.params.data;
  if (data.event !== "content-block-delta") continue;

  const block = data.delta ?? {};
  if (block.type === "text-delta") {
    const isSubagent = event.params.namespace.some((seg) => seg.startsWith("tools:"));
    const source = isSubagent ? "subagent" : "coordinator";
    console.log(`[${source}] ${block.text}`);
  }
}
```

## Subagents versus subgraphs

`stream.subgraphs` shows graph execution structure. `stream.subagents` shows product-level Deep Agents task delegations. Use `stream.subagents` for user-facing UI because it hides internal graph nodes and exposes the subagent concept directly.

## Related

* [LangChain Event Streaming](/oss/javascript/langchain/event-streaming) covers general agent message and tool-call streaming concepts.
* [Subagent frontend streaming](/oss/javascript/deepagents/frontend/subagent-streaming) shows UI patterns that separate coordinator messages from subagent cards.
* [LangGraph Event Streaming](/oss/javascript/langgraph/event-streaming) covers the underlying graph streaming model.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/deepagents/event-streaming.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Overview
Source: https://docs.langchain.com/oss/javascript/deepagents/frontend/overview

Build UIs that display real-time subagent streams, task progress, and sandbox for Deep Agents

Build frontends that visualize deep agent workflows in real time. These patterns
show how to render subagent progress, task planning, streaming content, and
IDE-like sandbox experiences from agents created with `createDeepAgent`.

Deep agents are most useful when the UI makes delegation visible. Instead of
showing a single opaque assistant bubble, the LangChain SDKs expose the
coordinator, subagent discovery, custom state, and sandbox-backed artifacts so
users can inspect how a long-running task is being decomposed and completed.

<Note>
  These patterns use the v1 frontend SDK packages. If you are using earlier versions, see the migration guides for [React](https://github.com/langchain-ai/langgraphjs/blob/main/libs/sdk-react/docs/v1-migration.md), [Vue](https://github.com/langchain-ai/langgraphjs/blob/main/libs/sdk-vue/docs/v1-migration.md), [Svelte](https://github.com/langchain-ai/langgraphjs/blob/main/libs/sdk-svelte/docs/v1-migration.md), and [Angular](https://github.com/langchain-ai/langgraphjs/blob/main/libs/sdk-angular/docs/v1-migration.md).
</Note>

## Architecture

Deep Agents use a coordinator-worker architecture. The main agent plans tasks and delegates to specialized subagents, each running in isolation. On the frontend, the v1 stream handle surfaces coordinator messages on the root stream and exposes subagent discovery snapshots for scoped subagent views.

```mermaid theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
%%{
  init: {
    "fontFamily": "monospace",
    "flowchart": {
      "curve": "curve"
    }
  }
}%%
graph LR
  FRONTEND["useStream()"]
  SELECTORS["selector helpers"]
  BACKEND["createDeepAgent()"]
  SUB1["Subagent A"]
  SUB2["Subagent B"]

  BACKEND --"stream"--> FRONTEND
  FRONTEND --"scope by subagent"--> SELECTORS
  SELECTORS --> SUB1
  SELECTORS --> SUB2
  FRONTEND --"submit"--> BACKEND
  BACKEND --"delegate"--> SUB1
  BACKEND --"delegate"--> SUB2
  SUB1 --"result"--> BACKEND
  SUB2 --"result"--> BACKEND

  classDef blueHighlight fill:#E5F4FF,stroke:#006DDD,color:#030710;
  classDef greenHighlight fill:#F6FFDB,stroke:#6E8900,color:#2E3900;
  classDef purpleHighlight fill:#EBD0F0,stroke:#885270,color:#441E33;
  class FRONTEND,SELECTORS blueHighlight;
  class BACKEND greenHighlight;
  class SUB1,SUB2 purpleHighlight;
```

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { createDeepAgent } from "deepagents";

const agent = createDeepAgent({
  tools: [getWeather],
  systemPrompt: "You are a helpful assistant",
  subagents: [
    {
      name: "researcher",
      description: "Research assistant",
    },
  ],
});
```

On the frontend, connect with [`useStream`](https://reference.langchain.com/javascript/langchain-react/index/useStream) the same way as with `createAgent`. Pass a [type parameter](/oss/javascript/langchain/frontend/overview) for type-safe stream state. Deep agent patterns use `stream.subagents`, selector helpers such as `useMessages(stream, subagent)`, and custom state values like `stream.values.todos` to render subagent-specific UIs.

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { useStream } from "@langchain/react";

function App() {
  const stream = useStream<typeof agent>({
    apiUrl: "http://localhost:2024",
    assistantId: "agent",
  });

  // Deep agent state beyond messages
  const todos = stream.values?.todos;
  const subagents = [...stream.subagents.values()];
}
```

## What the SDK exposes

Deep agent UIs usually need more than the final answer. The frontend SDK gives
you structured projections for the parts of the run users care about:

| Projection         | Use it for                                                                                                 |
| ------------------ | ---------------------------------------------------------------------------------------------------------- |
| `stream.messages`  | The coordinator conversation and final synthesis.                                                          |
| `stream.subagents` | Live discovery of specialist workers, including status and task metadata.                                  |
| `stream.values`    | Shared state such as todos, plans, report sections, sandbox metadata, or any custom key your agent writes. |
| Tool-call state    | Rendering filesystem, search, browser, or domain tools as cards with progress and results.                 |
| Interrupts         | Pausing delegated work for user approval or missing input without losing the run state.                    |

This lets you build interfaces that feel closer to an IDE, task board, or
workflow monitor than a plain chat transcript.

## Patterns

<CardGroup>
  <Card title="Subagent streaming" icon="arrows-split" href="/oss/javascript/deepagents/frontend/subagent-streaming">
    Display specialist subagents with streaming content, progress tracking, and collapsible cards.
  </Card>

  <Card title="Todo list" icon="list-check" href="/oss/javascript/deepagents/frontend/todo-list">
    Track agent progress with a real-time todo list synced from agent state.
  </Card>

  <Card title="Sandbox" icon="code" href="/oss/javascript/deepagents/frontend/sandbox">
    Build an IDE-like UI with a file browser, code viewer, and diff panel backed by a sandbox.
  </Card>
</CardGroup>

## Related patterns

The [LangChain frontend patterns](/oss/javascript/langchain/frontend/overview), including
markdown messages, tool calling, and human-in-the-loop, all work with deep
agents too. Deep Agents are built on the same LangGraph runtime, so
`useStream` provides the same core API.

For lower-level graph visualizations, see the
[LangGraph frontend patterns](/oss/javascript/langgraph/frontend/overview). They show how
to map graph nodes and state keys directly to UI components.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/deepagents/frontend/overview.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
