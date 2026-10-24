#         + <Claude-specific guidance>
```

<Note>
  Passing a `SystemMessage` (rather than a string) triggers a different concatenation path: the right-hand assembly (`BASE`-or-`CUSTOM` plus any `SUFFIX`) is appended as an additional text content block onto the message's existing `content_blocks`. The same logical ordering applies (caller blocks first), and any `cache_control` markers on the caller's blocks are preserved—useful for placing explicit Anthropic prompt-cache breakpoints.
</Note>

<AccordionGroup>
  <Accordion title="Subagent prompts">
    The [prompt assembly](#prompt-assembly) overlay rules also apply to declarative [subagents](/oss/javascript/deepagents/subagents): each subagent re-runs profile resolution against **its own model**, then applies the resolved profile's `base_system_prompt` / `system_prompt_suffix` to its authored `system_prompt`. The subagent's `system_prompt` plays the `BASE` role; `CUSTOM` and `SUFFIX` come from the profile that matches the subagent's model (which may differ from the main agent's profile).

    | `spec["system_prompt"]` | profile `base_system_prompt` (`CUSTOM`) | profile `system_prompt_suffix` (`SUFFIX`) | Final subagent system prompt |
    | ----------------------- | :-------------------------------------: | :---------------------------------------: | ---------------------------- |
    | authored                |                    -                    |                     -                     | authored                     |
    | authored                |                    -                    |                     ✓                     | authored + `SUFFIX`          |
    | authored                |                    ✓                    |                     -                     | `CUSTOM`                     |
    | authored                |                    ✓                    |                     ✓                     | `CUSTOM` + `SUFFIX`          |

    There is no `USER` segment for subagents. The spec's authored `system_prompt` is the closest analog and stays in the `BASE` slot. A profile that ships only a `system_prompt_suffix` (the common case for built-in Anthropic / OpenAI profiles) just appends to whatever the subagent author wrote. A profile that sets `base_system_prompt` will *replace* the authored prompt outright.
  </Accordion>

  <Accordion title="General-purpose subagent prompt">
    The auto-added [general-purpose subagent](/oss/javascript/deepagents/subagents#the-general-purpose-subagent) follows the [prompt assembly](#prompt-assembly) overlay rules with one extra layer: the GP base prompt is resolved as **`general_purpose_subagent.system_prompt` (if set) -> `HarnessProfile.base_system_prompt` (if set) -> SDK general-purpose default**. The profile suffix layers on top either way.

    The two override fields can both carry a base-prompt replacement, but they are not interchangeable. `general_purpose_subagent.system_prompt` is general-purpose-specific configuration; `base_system_prompt` is a global override that primarily targets the main agent. When both are set, the **general-purpose-specific intent wins for the general-purpose subagent** so a user tuning both fields never sees their GP override silently dropped:

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    register_harness_profile(
        "anthropic",
        HarnessProfile(
            base_system_prompt="You are ACME's support orchestrator.",  # main agent
            general_purpose_subagent=GeneralPurposeSubagentProfile(
                system_prompt="You are a research subagent. Cite sources.",  # GP subagent
            ),
            system_prompt_suffix="Always think step by step.",
        ),
    )
    ```

    | Stack       | Final system prompt                                     |
    | ----------- | ------------------------------------------------------- |
    | Main agent  | `"You are ACME's support orchestrator." + SUFFIX`       |
    | GP subagent | `"You are a research subagent. Cite sources." + SUFFIX` |

    If `general_purpose_subagent.system_prompt` is unset, the GP subagent falls back to `base_system_prompt` (when set) and finally to the SDK general-purpose default.
  </Accordion>
</AccordionGroup>

## Middleware

Deep Agents support any [middleware](/oss/javascript/langchain/middleware/overview), including the built-in middleware listed below, prebuilt middleware from LangChain, provider-specific middleware, and custom middleware you write yourself.

Pass middleware to the `middleware` argument of `createDeepAgent`. Custom middleware is appended after [`PatchToolCallsMiddleware`](https://reference.langchain.com/javascript/deepagents/middleware/createPatchToolCallsMiddleware) in the [default stack](#default-stack-main-agent).

By default, Deep Agents have access to the following middleware:

### Default stack (main agent)

From first to last:

1. [`TodoListMiddleware`](https://reference.langchain.com/javascript/langchain/index/todoListMiddleware): Tracks and manages todo lists for organizing agent tasks and work.

2. [`SkillsMiddleware`](https://reference.langchain.com/javascript/deepagents/middleware/createSkillsMiddleware): Only when you pass `skills`. Injected **immediately after** the todo middleware and **before** filesystem middleware so skill metadata is available before file tools run.

3. [`FilesystemMiddleware`](https://reference.langchain.com/javascript/deepagents/middleware/createFilesystemMiddleware): Handles file system operations such as reading, writing, and navigating directories. When you pass `permissions`, filesystem permissions enforcement is included here so it can evaluate every tool the agent might call.

4. [`SubAgentMiddleware`](https://reference.langchain.com/javascript/deepagents/middleware/createSubAgentMiddleware): Spawns and coordinates subagents for delegating tasks to specialized agents.

5. [`SummarizationMiddleware`](https://reference.langchain.com/javascript/langchain/index/summarizationMiddleware): Condenses message history to stay within context limits when conversations grow long (via [createSummarizationMiddleware](https://reference.langchain.com/javascript/deepagents/middleware/createSummarizationMiddleware)).

6. [`PatchToolCallsMiddleware`](https://reference.langchain.com/javascript/deepagents/middleware/createPatchToolCallsMiddleware): Repairs dangling tool calls in message history when a run resumes after an interruption or receives malformed tool-call arguments. Runs **before** Anthropic prompt caching and the tail stack below.

7. [`AsyncSubAgentMiddleware`](https://reference.langchain.com/javascript/deepagents/agent/createDeepAgent): Only when you configure async subagents.

8. **Your middleware argument**: Optional middleware you pass as the `middleware` argument is appended here (after Patch, before the tail stack).

9. **Harness profile extras**: Provider-specific middleware from the resolved model profile, if any.

10. **Excluded-tool filtering**: When the harness profile lists excluded tools, middleware removes those tools from the agent.

11. [`AnthropicPromptCachingMiddleware`](https://reference.langchain.com/javascript/langchain/index/anthropicPromptCachingMiddleware): Automatically added when you are using an Anthropic model. Runs **after** Patch and after your middleware so the cached prefix matches what is actually sent to the model.

12. [`MemoryMiddleware`](https://reference.langchain.com/javascript/deepagents/middleware/createMemoryMiddleware): Only when you pass `memory`.

    <Note>
      `MemoryMiddleware` is placed **after** profile extras and Anthropic prompt caching so updates to injected memory are less likely to invalidate the Anthropic cache prefix. The same ordering concern is called out in the `createDeepAgent` implementation comments.
    </Note>

13. `HumanInTheLoopMiddleware`: Only when you pass `interruptOn`. Pauses for human approval or input at configured tool calls.

### Default stack (synchronous subagents)

The built-in **general-purpose** subagent and each declarative synchronous `SubAgent` graph use a stack that `createDeepAgent` builds in code. It matches the main agent in broad shape (todo list, filesystem, summarization, Patch, profile extras, Anthropic caching, optional permissions) but differs in two ways:

* **Skills run after** [`PatchToolCallsMiddleware`](https://reference.langchain.com/javascript/deepagents/middleware/createPatchToolCallsMiddleware) on these inner agents (on the main agent, skills run **before** filesystem middleware when `skills` is set).
* There is **no** [`SubAgentMiddleware`](https://reference.langchain.com/javascript/deepagents/middleware/createSubAgentMiddleware) inside a subagent graph (only the parent agent exposes the `task` tool).

When a declarative subagent sets `interruptOn`, that value is forwarded to `createAgent` for the subagent, which wires up human-in-the-loop handling for the configured tool calls.

### Prebuilt middleware

LangChain exposes additional prebuilt middleware that let you add-on various features, such as retries, fallbacks, or PII detection. See [Prebuilt middleware](/oss/javascript/langchain/middleware/built-in) for more.

The `deepagents` package also exposes [`createSummarizationMiddleware`](https://reference.langchain.com/javascript/deepagents/middleware/createSummarizationMiddleware) for the same workflow. For more detail, see [Summarization](/oss/javascript/deepagents/context-engineering#summarization).

### Provider-specific middleware

For provider-specific middleware that is optimized for specific LLM providers, see [Official integrations](/oss/javascript/integrations/middleware#official-integrations) and [Community integrations](/oss/javascript/integrations/middleware#community-integrations).

### Custom middleware

You can provide additional middleware to extend functionality, add tools, or implement custom hooks:

<CodeGroup>
  ```ts Google theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { tool, createMiddleware } from "langchain";
  import { createDeepAgent } from "deepagents";
  import * as z from "zod";

  const getWeather = tool(
    ({ city }: { city: string }) => {
      return `The weather in ${city} is sunny.`;
    },
    {
      name: "get_weather",
      description: "Get the weather in a city.",
      schema: z.object({
        city: z.string(),
      }),
    },
  );

  let callCount = 0;

  const logToolCallsMiddleware = createMiddleware({
    name: "LogToolCallsMiddleware",
    wrapToolCall: async (request, handler) => {
      // Intercept and log every tool call - demonstrates cross-cutting concern
      callCount += 1;
      const toolName = request.toolCall.name;

      console.log(`[Middleware] Tool call #${callCount}: ${toolName}`);
      console.log(
        `[Middleware] Arguments: ${JSON.stringify(request.toolCall.args)}`,
      );

      // Execute the tool call
      const result = await handler(request);

      // Log the result
      console.log(`[Middleware] Tool call #${callCount} completed`);

      return result;
    },
  });

  const agent = await createDeepAgent({
    model: "google-genai:gemini-3.5-flash",
    tools: [getWeather] as any,
    middleware: [logToolCallsMiddleware] as any,
  });
  ```

  ```ts OpenAI theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { tool, createMiddleware } from "langchain";
  import { createDeepAgent } from "deepagents";
  import * as z from "zod";

  const getWeather = tool(
    ({ city }: { city: string }) => {
      return `The weather in ${city} is sunny.`;
    },
    {
      name: "get_weather",
      description: "Get the weather in a city.",
      schema: z.object({
        city: z.string(),
      }),
    },
  );

  let callCount = 0;

  const logToolCallsMiddleware = createMiddleware({
    name: "LogToolCallsMiddleware",
    wrapToolCall: async (request, handler) => {
      // Intercept and log every tool call - demonstrates cross-cutting concern
      callCount += 1;
      const toolName = request.toolCall.name;

      console.log(`[Middleware] Tool call #${callCount}: ${toolName}`);
      console.log(
        `[Middleware] Arguments: ${JSON.stringify(request.toolCall.args)}`,
      );

      // Execute the tool call
      const result = await handler(request);

      // Log the result
      console.log(`[Middleware] Tool call #${callCount} completed`);

      return result;
    },
  });

  const agent = await createDeepAgent({
    model: "openai:gpt-5.5",
    tools: [getWeather] as any,
    middleware: [logToolCallsMiddleware] as any,
  });
  ```

  ```ts Anthropic theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { tool, createMiddleware } from "langchain";
  import { createDeepAgent } from "deepagents";
  import * as z from "zod";

  const getWeather = tool(
    ({ city }: { city: string }) => {
      return `The weather in ${city} is sunny.`;
    },
    {
      name: "get_weather",
      description: "Get the weather in a city.",
      schema: z.object({
        city: z.string(),
      }),
    },
  );

  let callCount = 0;

  const logToolCallsMiddleware = createMiddleware({
    name: "LogToolCallsMiddleware",
    wrapToolCall: async (request, handler) => {
      // Intercept and log every tool call - demonstrates cross-cutting concern
      callCount += 1;
      const toolName = request.toolCall.name;

      console.log(`[Middleware] Tool call #${callCount}: ${toolName}`);
      console.log(
        `[Middleware] Arguments: ${JSON.stringify(request.toolCall.args)}`,
      );

      // Execute the tool call
      const result = await handler(request);

      // Log the result
      console.log(`[Middleware] Tool call #${callCount} completed`);

      return result;
    },
  });

  const agent = await createDeepAgent({
    model: "anthropic:claude-sonnet-4-6",
    tools: [getWeather] as any,
    middleware: [logToolCallsMiddleware] as any,
  });
  ```

  ```ts OpenRouter theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { tool, createMiddleware } from "langchain";
  import { createDeepAgent } from "deepagents";
  import * as z from "zod";

  const getWeather = tool(
    ({ city }: { city: string }) => {
      return `The weather in ${city} is sunny.`;
    },
    {
      name: "get_weather",
      description: "Get the weather in a city.",
      schema: z.object({
        city: z.string(),
      }),
    },
  );

  let callCount = 0;

  const logToolCallsMiddleware = createMiddleware({
    name: "LogToolCallsMiddleware",
    wrapToolCall: async (request, handler) => {
      // Intercept and log every tool call - demonstrates cross-cutting concern
      callCount += 1;
      const toolName = request.toolCall.name;

      console.log(`[Middleware] Tool call #${callCount}: ${toolName}`);
      console.log(
        `[Middleware] Arguments: ${JSON.stringify(request.toolCall.args)}`,
      );

      // Execute the tool call
      const result = await handler(request);

      // Log the result
      console.log(`[Middleware] Tool call #${callCount} completed`);

      return result;
    },
  });

  const agent = await createDeepAgent({
    model: "openrouter:anthropic/claude-sonnet-4-6",
    tools: [getWeather] as any,
    middleware: [logToolCallsMiddleware] as any,
  });
  ```

  ```ts Fireworks theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { tool, createMiddleware } from "langchain";
  import { createDeepAgent } from "deepagents";
  import * as z from "zod";

  const getWeather = tool(
    ({ city }: { city: string }) => {
      return `The weather in ${city} is sunny.`;
    },
    {
      name: "get_weather",
      description: "Get the weather in a city.",
      schema: z.object({
        city: z.string(),
      }),
    },
  );

  let callCount = 0;

  const logToolCallsMiddleware = createMiddleware({
    name: "LogToolCallsMiddleware",
    wrapToolCall: async (request, handler) => {
      // Intercept and log every tool call - demonstrates cross-cutting concern
      callCount += 1;
      const toolName = request.toolCall.name;

      console.log(`[Middleware] Tool call #${callCount}: ${toolName}`);
      console.log(
        `[Middleware] Arguments: ${JSON.stringify(request.toolCall.args)}`,
      );

      // Execute the tool call
      const result = await handler(request);

      // Log the result
      console.log(`[Middleware] Tool call #${callCount} completed`);

      return result;
    },
  });

  const agent = await createDeepAgent({
    model: "fireworks:accounts/fireworks/models/qwen3p5-397b-a17b",
    tools: [getWeather] as any,
    middleware: [logToolCallsMiddleware] as any,
  });
  ```

  ```ts Baseten theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { tool, createMiddleware } from "langchain";
  import { createDeepAgent } from "deepagents";
  import * as z from "zod";

  const getWeather = tool(
    ({ city }: { city: string }) => {
      return `The weather in ${city} is sunny.`;
    },
    {
      name: "get_weather",
      description: "Get the weather in a city.",
      schema: z.object({
        city: z.string(),
      }),
    },
  );

  let callCount = 0;

  const logToolCallsMiddleware = createMiddleware({
    name: "LogToolCallsMiddleware",
    wrapToolCall: async (request, handler) => {
      // Intercept and log every tool call - demonstrates cross-cutting concern
      callCount += 1;
      const toolName = request.toolCall.name;

      console.log(`[Middleware] Tool call #${callCount}: ${toolName}`);
      console.log(
        `[Middleware] Arguments: ${JSON.stringify(request.toolCall.args)}`,
      );

      // Execute the tool call
      const result = await handler(request);

      // Log the result
      console.log(`[Middleware] Tool call #${callCount} completed`);

      return result;
    },
  });

  const agent = await createDeepAgent({
    model: "baseten:zai-org/GLM-5",
    tools: [getWeather] as any,
    middleware: [logToolCallsMiddleware] as any,
  });
  ```

  ```ts Ollama theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { tool, createMiddleware } from "langchain";
  import { createDeepAgent } from "deepagents";
  import * as z from "zod";

  const getWeather = tool(
    ({ city }: { city: string }) => {
      return `The weather in ${city} is sunny.`;
    },
    {
      name: "get_weather",
      description: "Get the weather in a city.",
      schema: z.object({
        city: z.string(),
      }),
    },
  );

  let callCount = 0;

  const logToolCallsMiddleware = createMiddleware({
    name: "LogToolCallsMiddleware",
    wrapToolCall: async (request, handler) => {
      // Intercept and log every tool call - demonstrates cross-cutting concern
      callCount += 1;
      const toolName = request.toolCall.name;

      console.log(`[Middleware] Tool call #${callCount}: ${toolName}`);
      console.log(
        `[Middleware] Arguments: ${JSON.stringify(request.toolCall.args)}`,
      );

      // Execute the tool call
      const result = await handler(request);

      // Log the result
      console.log(`[Middleware] Tool call #${callCount} completed`);

      return result;
    },
  });

  const agent = await createDeepAgent({
    model: "ollama:devstral-2",
    tools: [getWeather] as any,
    middleware: [logToolCallsMiddleware] as any,
  });
  ```
</CodeGroup>

<Warning>
  **Do not mutate attributes after initialization**

  If you need to track values across hook invocations (for example, counters or accumulated data), use graph state.
  Graph state is scoped to a thread by design, so updates are safe under concurrency.

  **Do this:**

  ```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  const customMiddleware = createMiddleware({
    name: "CustomMiddleware",
    beforeAgent: async (state) => {
      return { x: (state.x ?? 0) + 1 }; // Update graph state instead
    },
  });
  ```

  Do **not** do this:

  ```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  let x = 1;

  const customMiddlewareBad = createMiddleware({
    name: "CustomMiddleware",
    beforeAgent: async () => {
      x += 1; // Mutation causes race conditions
    },
  });
  ```

  Mutation in place, such as modifying `state.x` in `beforeAgent`, mutating a shared variable in `beforeAgent`, or changing other shared values in hooks, can lead to subtle bugs and race conditions because many operations run concurrently (subagents, parallel tools, and parallel invocations on different threads).

  If you must use mutation in custom middleware, consider what happens when subagents, parallel tools, or concurrent agent invocations run at the same time.
</Warning>

### Interpreters

Use [interpreters](/oss/javascript/deepagents/interpreters) to add an `eval` tool that runs JavaScript in a scoped QuickJS runtime. Interpreters are useful when the agent needs to compose tools programmatically, batch work, handle errors in code, or transform structured data without a full shell environment.

<CodeGroup>
  ```ts Google theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createDeepAgent } from "deepagents";
  import { createCodeInterpreterMiddleware } from "@langchain/quickjs";

  const agent = createDeepAgent({
    model: "google-genai:gemini-3.5-flash",
    middleware: [createCodeInterpreterMiddleware()],
  });
  ```

  ```ts OpenAI theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createDeepAgent } from "deepagents";
  import { createCodeInterpreterMiddleware } from "@langchain/quickjs";

  const agent = createDeepAgent({
    model: "openai:gpt-5.5",
    middleware: [createCodeInterpreterMiddleware()],
  });
  ```

  ```ts Anthropic theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createDeepAgent } from "deepagents";
  import { createCodeInterpreterMiddleware } from "@langchain/quickjs";

  const agent = createDeepAgent({
    model: "anthropic:claude-sonnet-4-6",
    middleware: [createCodeInterpreterMiddleware()],
  });
  ```

  ```ts OpenRouter theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createDeepAgent } from "deepagents";
  import { createCodeInterpreterMiddleware } from "@langchain/quickjs";

  const agent = createDeepAgent({
    model: "openrouter:anthropic/claude-sonnet-4-6",
    middleware: [createCodeInterpreterMiddleware()],
  });
  ```

  ```ts Fireworks theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createDeepAgent } from "deepagents";
  import { createCodeInterpreterMiddleware } from "@langchain/quickjs";

  const agent = createDeepAgent({
    model: "fireworks:accounts/fireworks/models/qwen3p5-397b-a17b",
    middleware: [createCodeInterpreterMiddleware()],
  });
  ```

  ```ts Baseten theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createDeepAgent } from "deepagents";
  import { createCodeInterpreterMiddleware } from "@langchain/quickjs";

  const agent = createDeepAgent({
    model: "baseten:zai-org/GLM-5",
    middleware: [createCodeInterpreterMiddleware()],
  });
  ```

  ```ts Ollama theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createDeepAgent } from "deepagents";
  import { createCodeInterpreterMiddleware } from "@langchain/quickjs";

  const agent = createDeepAgent({
    model: "ollama:devstral-2",
    middleware: [createCodeInterpreterMiddleware()],
  });
  ```
</CodeGroup>

For setup, programmatic tool calling, subagent orchestration, and limits, see [Interpreters](/oss/javascript/deepagents/interpreters).

## Subagents

To isolate detailed work and avoid context bloat, use subagents:

<CodeGroup>
  ```ts Google theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
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
    model: "google-genai:gemini-3.5-flash", // Optional override, defaults to main agent model
  };
  const subagents = [researchSubagent];

  const agent = createDeepAgent({
    model: "google_genai:gemini-3.5-flash",
    subagents,
  });
  ```

  ```ts OpenAI theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
