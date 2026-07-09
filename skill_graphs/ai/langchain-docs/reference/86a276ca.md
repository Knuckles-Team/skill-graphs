    end

    M->>M: Process results & generate response
    M->>U: "SF: 72°F sunny, NYC: 68°F cloudy"
```

To make tools that you have defined available for use by a model, you must bind them using [`bindTools`](https://reference.langchain.com/javascript/classes/_langchain_core.language_models_chat_models.BaseChatModel.html#bindTools). In subsequent invocations, the model can choose to call any of the bound tools as needed.

Some model providers offer <Tooltip>built-in tools</Tooltip> that can be enabled via model or invocation parameters (e.g. [`ChatOpenAI`](/oss/javascript/integrations/chat/openai), [`ChatAnthropic`](/oss/javascript/integrations/chat/anthropic)). Check the respective [provider reference](/oss/javascript/integrations/providers/overview) for details.

<Tip>
  See the [tools guide](/oss/javascript/langchain/tools) for details and other options for creating tools.
</Tip>

```typescript Binding user tools theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { tool } from "langchain";
import * as z from "zod";
import { ChatOpenAI } from "@langchain/openai";

const getWeather = tool(
  (input) => `It's sunny in ${input.location}.`,
  {
    name: "get_weather",
    description: "Get the weather at a location.",
    schema: z.object({
      location: z.string().describe("The location to get the weather for"),
    }),
  },
);

const model = new ChatOpenAI({ model: "gpt-5.5" });
const modelWithTools = model.bindTools([getWeather]);  // [!code highlight]

const response = await modelWithTools.invoke("What's the weather like in Boston?");
const toolCalls = response.tool_calls || [];
for (const tool_call of toolCalls) {
  // View tool calls made by the model
  console.log(`Tool: ${tool_call.name}`);
  console.log(`Args: ${tool_call.args}`);
}
```

When binding user-defined tools, the model's response includes a **request** to execute a tool. When using a model separately from an [agent](/oss/javascript/langchain/agents), it is up to you to execute the requested tool and return the result back to the model for use in subsequent reasoning. When using an [agent](/oss/javascript/langchain/agents), the agent loop will handle the tool execution loop for you.

Below, we show some common ways you can use tool calling.

<AccordionGroup>
  <Accordion title="Tool execution loop" icon="refresh">
    When a model returns tool calls, you need to execute the tools and pass the results back to the model. This creates a conversation loop where the model can use tool results to generate its final response. LangChain includes [agent](/oss/javascript/langchain/agents) abstractions that handle this orchestration for you.

    Here's a simple example of how to do this:

    ```typescript Tool execution loop theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    // Bind (potentially multiple) tools to the model
    const modelWithTools = model.bindTools([get_weather])

    // Step 1: Model generates tool calls
    const messages = [{"role": "user", "content": "What's the weather in Boston?"}]
    const ai_msg = await modelWithTools.invoke(messages)
    messages.push(ai_msg)

    // Step 2: Execute tools and collect results
    for (const tool_call of ai_msg.tool_calls) {
        // Execute the tool with the generated arguments
        const tool_result = await get_weather.invoke(tool_call)
        messages.push(tool_result)
    }

    // Step 3: Pass results back to model for final response
    const final_response = await modelWithTools.invoke(messages)
    console.log(final_response.text)
    // "The current weather in Boston is 72°F and sunny."
    ```

    Each [`ToolMessage`](https://reference.langchain.com/javascript/langchain-core/messages/ToolMessage) returned by the tool includes a `tool_call_id` that matches the original tool call, helping the model correlate results with requests.
  </Accordion>

  <Accordion title="Forcing tool calls" icon="asterisk">
    By default, the model has the freedom to choose which bound tool to use based on the user's input. However, you might want to force choosing a tool, ensuring the model uses either a particular tool or **any** tool from a given list:

    <CodeGroup>
      ```typescript Force use of any tool theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      const modelWithTools = model.bindTools([tool_1], { toolChoice: "any" })
      ```

      ```typescript Force use of specific tools theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      const modelWithTools = model.bindTools([tool_1], { toolChoice: "tool_1" })
      ```
    </CodeGroup>
  </Accordion>

  <Accordion title="Parallel tool calls" icon="stack-2">
    Many models support calling multiple tools in parallel when appropriate. This allows the model to gather information from different sources simultaneously.

    ```typescript Parallel tool calls theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    const modelWithTools = model.bind_tools([get_weather])

    const response = await modelWithTools.invoke(
        "What's the weather in Boston and Tokyo?"
    )

    // The model may generate multiple tool calls
    console.log(response.tool_calls)
    // [
    //   { name: 'get_weather', args: { location: 'Boston' }, id: 'call_1' },
    //   { name: 'get_time', args: { location: 'Tokyo' }, id: 'call_2' }
    // ]

    // Execute all tools (can be done in parallel with async)
    const results = []
    for (const tool_call of response.tool_calls || []) {
        if (tool_call.name === 'get_weather') {
            const result = await get_weather.invoke(tool_call)
            results.push(result)
        }
    }
    ```

    The model intelligently determines when parallel execution is appropriate based on the independence of the requested operations.

    <Tip>
      Most models supporting tool calling enable parallel tool calls by default. Some (including [OpenAI](/oss/javascript/integrations/chat/openai) and [Anthropic](/oss/javascript/integrations/chat/anthropic)) allow you to disable this feature. To do this, set `parallel_tool_calls=False`:

      ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      model.bind_tools([get_weather], parallel_tool_calls=False)
      ```
    </Tip>
  </Accordion>

  <Accordion title="Streaming tool calls" icon="rss">
    When streaming responses, tool calls are progressively built through [`ToolCallChunk`](https://reference.langchain.com/javascript/langchain-core/messages/ContentBlock/Tools/ToolCallChunk). This allows you to see tool calls as they're being generated rather than waiting for the complete response.

    ```typescript Streaming tool calls theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    const stream = await modelWithTools.stream(
        "What's the weather in Boston and Tokyo?"
    )
    for await (const chunk of stream) {
        // Tool call chunks arrive progressively
        if (chunk.tool_call_chunks) {
            for (const tool_chunk of chunk.tool_call_chunks) {
            console.log(`Tool: ${tool_chunk.get('name', '')}`)
            console.log(`Args: ${tool_chunk.get('args', '')}`)
            }
        }
    }

    // Output:
    // Tool: get_weather
    // Args:
    // Tool:
    // Args: {"loc
    // Tool:
    // Args: ation": "BOS"}
    // Tool: get_time
    // Args:
    // Tool:
    // Args: {"timezone": "Tokyo"}
    ```

    You can accumulate chunks to build complete tool calls:

    ```typescript Accumulate tool calls theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    let full: AIMessageChunk | null = null
    const stream = await modelWithTools.stream("What's the weather in Boston?")
    for await (const chunk of stream) {
        full = full ? full.concat(chunk) : chunk
        console.log(full.contentBlocks)
    }
    ```
  </Accordion>
</AccordionGroup>

***

## Structured output

Models can be requested to provide their response in a format matching a given schema. This is useful for ensuring the output can be easily parsed and used in subsequent processing. LangChain supports multiple schema types and methods for enforcing structured output.

<Tip>
  To learn about structured output, see [Structured output](/oss/javascript/langchain/structured-output).
</Tip>

<Tabs>
  <Tab title="Zod">
    A [zod schema](https://zod.dev/) is the preferred method of defining an output schema. Note that when a zod schema is provided, the model output will also be validated against the schema using zod's parse methods.

    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import * as z from "zod";

    const Movie = z.object({
      title: z.string().describe("The title of the movie"),
      year: z.number().describe("The year the movie was released"),
      director: z.string().describe("The director of the movie"),
      rating: z.number().describe("The movie's rating out of 10"),
    });

    const modelWithStructure = model.withStructuredOutput(Movie);

    const response = await modelWithStructure.invoke("Provide details about the movie Inception");
    console.log(response);
    // {
    //   title: "Inception",
    //   year: 2010,
    //   director: "Christopher Nolan",
    //   rating: 8.8,
    // }
    ```
  </Tab>

  <Tab title="JSON Schema">
    For maximum control or interoperability, you can provide a raw JSON Schema.

    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    const jsonSchema = {
      "title": "Movie",
      "description": "A movie with details",
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the movie",
        },
        "year": {
          "type": "integer",
          "description": "The year the movie was released",
        },
        "director": {
          "type": "string",
          "description": "The director of the movie",
        },
        "rating": {
          "type": "number",
          "description": "The movie's rating out of 10",
        },
      },
      "required": ["title", "year", "director", "rating"],
    }

    const modelWithStructure = model.withStructuredOutput(
      jsonSchema,
      { method: "jsonSchema" },
    )

    const response = await modelWithStructure.invoke("Provide details about the movie Inception")
    console.log(response)  // {'title': 'Inception', 'year': 2010, ...}
    ```
  </Tab>

  <Tab title="Standard Schema">
    Any schema from a library implementing the [Standard Schema](https://standardschema.dev/) specification is also supported. Standard Schema objects are validated at runtime via the schema's `~standard.validate()` method.

    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import * as v from "valibot";
    import { toStandardJsonSchema } from "@valibot/to-json-schema";

    const Movie = toStandardJsonSchema(
      v.object({
        title: v.pipe(v.string(), v.description("The title of the movie")),
        year: v.pipe(v.number(), v.description("The year the movie was released")),
        director: v.pipe(v.string(), v.description("The director of the movie")),
        rating: v.pipe(v.number(), v.description("The movie's rating out of 10")),
      })
    );

    const modelWithStructure = model.withStructuredOutput(Movie);

    const response = await modelWithStructure.invoke("Provide details about the movie Inception");
    console.log(response);
    // {
    //   title: "Inception",
    //   year: 2010,
    //   director: "Christopher Nolan",
    //   rating: 8.8,
    // }
    ```
  </Tab>
</Tabs>

<Note>
  **Key considerations for structured output:**

  * **Method parameter**: Some providers support different methods (`'jsonSchema'`, `'functionCalling'`, `'jsonMode'`)
  * **Include raw**: Use [`includeRaw: true`](https://reference.langchain.com/javascript/classes/_langchain_core.language_models_chat_models.BaseChatModel.html#withStructuredOutput) to get both the parsed output and the raw [`AIMessage`](https://reference.langchain.com/javascript/langchain-core/messages/AIMessage)
  * **Validation**: Zod and Standard Schema objects provide automatic validation, while JSON Schema requires manual validation
  * **Standard Schema**: Any schema library implementing the [Standard Schema](https://standardschema.dev/) spec is supported and validated at runtime

  See your [provider's integration page](/oss/javascript/integrations/providers/overview) for supported methods and configuration options.
</Note>

<Accordion title="Example: Message output alongside parsed structure">
  It can be useful to return the raw [`AIMessage`](https://reference.langchain.com/javascript/langchain-core/messages/AIMessage) object alongside the parsed representation to access response metadata such as [token counts](#token-usage). To do this, set [`include_raw=True`](https://reference.langchain.com/javascript/classes/_langchain_core.language_models_chat_models.BaseChatModel.html#withStructuredOutput) when calling [`with_structured_output`](https://reference.langchain.com/javascript/classes/_langchain_core.language_models_chat_models.BaseChatModel.html#withStructuredOutput):

  ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import * as z from "zod";

  const Movie = z.object({
    title: z.string().describe("The title of the movie"),
    year: z.number().describe("The year the movie was released"),
    director: z.string().describe("The director of the movie"),
    rating: z.number().describe("The movie's rating out of 10"),
    title: z.string().describe("The title of the movie"),
    year: z.number().describe("The year the movie was released"),
    director: z.string().describe("The director of the movie"),  // [!code highlight]
    rating: z.number().describe("The movie's rating out of 10"),
  });

  const modelWithStructure = model.withStructuredOutput(Movie, { includeRaw: true });

  const response = await modelWithStructure.invoke("Provide details about the movie Inception");
  console.log(response);
  // {
  //   raw: AIMessage { ... },
  //   parsed: { title: "Inception", ... }
  // }
  ```
</Accordion>

<Accordion title="Example: Nested structures">
  Schemas can be nested:

  ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import * as z from "zod";

  const Actor = z.object({
    name: z.string(),
    role: z.string(),
  });

  const MovieDetails = z.object({
    title: z.string(),
    year: z.number(),
    cast: z.array(Actor),
    genres: z.array(z.string()),
    budget: z.number().nullable().describe("Budget in millions USD"),
  });

  const modelWithStructure = model.withStructuredOutput(MovieDetails);
  ```
</Accordion>

***

## Advanced topics

### Model profiles

<Info>
  Model profiles require `langchain>=1.1`.
</Info>

LangChain chat models can expose a dictionary of supported features and capabilities through a `profile` property:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
model.profile;
// {
//   maxInputTokens: 400000,
//   imageInputs: true,
//   reasoningOutput: true,
//   toolCalling: true,
//   ...
// }
```

Refer to the full set of fields in the [API reference](https://reference.langchain.com/javascript/langchain-core/language_models/profile/ModelProfile).

Much of the model profile data is powered by the [models.dev](https://github.com/sst/models.dev) project, an open source initiative that provides model capability data. This data is augmented with additional fields for purposes of use with LangChain. These augmentations are kept aligned with the upstream project as it evolves.

Model profile data allow applications to work around model capabilities dynamically. For example:

1. [Summarization middleware](/oss/javascript/langchain/middleware/built-in#summarization) can trigger summarization based on a model's context window size.
2. [Structured output](/oss/javascript/langchain/structured-output) strategies in `createAgent` can be inferred automatically (e.g., by checking support for native structured output features).
3. Model inputs can be gated based on supported [modalities](#multimodal) and maximum input tokens.
4. [Deep Agents Code](/oss/javascript/deepagents/code) filters the [interactive model switcher](/oss/javascript/deepagents/code/providers#which-models-appear-in-the-switcher) to models whose profiles report `tool_calling` support and text I/O, and displays context window sizes and capability flags in the selector detail view.

<Accordion title="Modify profile data">
  Model profile data can be changed if it is missing, stale, or incorrect.

  **Option 1 (quick fix)**

  You can instantiate a chat model with any valid profile:

  ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  const customProfile = {
  maxInputTokens: 100_000,
  toolCalling: true,
  structuredOutput: true,
  // ...
  };
  const model = initChatModel("...", { profile: customProfile });
  ```

  **Option 2 (fix data upstream)**

  The primary source for the data is the [models.dev](https://models.dev/) project. These data are merged with additional fields and overrides in LangChain [integration packages](/oss/javascript/integrations/providers/overview) and are shipped with those packages.

  Model profile data can be updated through the following process:

  1. (If needed) update the source data at [models.dev](https://models.dev/) through a pull request to its [repository on GitHub](https://github.com/sst/models.dev).
  2. (If needed) update additional fields and overrides in `langchain-<package>/profiles.toml` through a pull request to the LangChain [integration package](/oss/javascript/integrations/providers/overview).
</Accordion>

<Warning>
  Model profiles are a beta feature. The format of a profile is subject to change.
</Warning>

### Multimodal

Certain models can process and return non-textual data such as images, audio, and video. You can pass non-textual data to a model by providing [content blocks](/oss/javascript/langchain/messages#message-content).

<Tip>
  All LangChain chat models with underlying multimodal capabilities support:

  1. Data in the cross-provider standard format (see [our messages guide](/oss/javascript/langchain/messages))
  2. OpenAI [chat completions](https://platform.openai.com/docs/api-reference/chat) format
  3. Any format that is native to that specific provider (e.g., Anthropic models accept Anthropic native format)
</Tip>

See the [multimodal section](/oss/javascript/langchain/messages#multimodal) of the messages guide for details.

<Tooltip href="https://models.dev/">Some models</Tooltip> can return multimodal data as part of their response. If invoked to do so, the resulting [`AIMessage`](https://reference.langchain.com/javascript/langchain-core/messages/AIMessage) will have content blocks with multimodal types.

```typescript Multimodal output theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const response = await model.invoke("Create a picture of a cat");
console.log(response.contentBlocks);
// [
//   { type: "text", text: "Here's a picture of a cat" },
//   { type: "image", data: "...", mimeType: "image/jpeg" },
// ]
```

See the [integrations page](/oss/javascript/integrations/providers/overview) for details on specific providers.

### Reasoning

Many models are capable of performing multi-step reasoning to arrive at a conclusion. This involves breaking down complex problems into smaller, more manageable steps.

**If supported by the underlying model,** you can surface this reasoning process to better understand how the model arrived at its final answer.

<CodeGroup>
  ```typescript Stream reasoning output theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  const stream = model.stream("Why do parrots have colorful feathers?");
  for await (const chunk of stream) {
      const reasoningSteps = chunk.contentBlocks.filter(b => b.type === "reasoning");
      console.log(reasoningSteps.length > 0 ? reasoningSteps : chunk.text);
  }
  ```

  ```typescript Complete reasoning output theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  const response = await model.invoke("Why do parrots have colorful feathers?");
  const reasoningSteps = response.contentBlocks.filter(b => b.type === "reasoning");
  console.log(reasoningSteps.map(step => step.reasoning).join(" "));
  ```
</CodeGroup>

Depending on the model, you can sometimes specify the level of effort it should put into reasoning. Similarly, you can request that the model turn off reasoning entirely. This may take the form of categorical "tiers" of reasoning (e.g., `'low'` or `'high'`) or integer token budgets.

For details, see the [integrations page](/oss/javascript/integrations/providers/overview) or [reference](https://reference.langchain.com/python/integrations/) for your respective chat model.

### Local models

LangChain supports running models locally on your own hardware. This is useful for scenarios where either data privacy is critical, you want to invoke a custom model, or when you want to avoid the costs incurred when using a cloud-based model.

[Ollama](/oss/javascript/integrations/chat/ollama) is one of the easiest ways to run chat and embedding models locally.

### Prompt caching

Many providers offer prompt caching features to reduce latency and cost on repeat processing of the same tokens. These features can be **implicit** or **explicit**:

* **Implicit prompt caching:** providers will automatically pass on cost savings if a request hits a cache. Examples: [OpenAI](/oss/javascript/integrations/chat/openai) and [Gemini](/oss/javascript/integrations/chat/google_generative_ai).
* **Explicit caching:** providers allow you to manually indicate cache points for greater control or to guarantee cost savings. Examples:
  * [`ChatOpenAI`](https://reference.langchain.com/javascript/langchain-openai/ChatOpenAI) (via `prompt_cache_key`)
  * Anthropic's [`AnthropicPromptCachingMiddleware`](/oss/javascript/integrations/chat/anthropic#prompt-caching)
  * [Gemini](https://reference.langchain.com/python/integrations/langchain_google_genai/).

<Warning>
  Prompt caching is often only engaged above a minimum input token threshold. See [provider pages](/oss/javascript/integrations/chat) for details.
</Warning>

Cache usage will be reflected in the [usage metadata](/oss/javascript/langchain/messages#token-usage) of the model response.

### Server-side tool use

Some providers support server-side [tool-calling](#tool-calling) loops: models can interact with web search, code interpreters, and other tools and analyze the results in a single conversational turn.

If a model invokes a tool server-side, the content of the response message will include content representing the invocation and result of the tool. Accessing the [content blocks](/oss/javascript/langchain/messages#standard-content-blocks) of the response will return the server-side tool calls and results in a provider-agnostic format:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { initChatModel } from "langchain";

const model = await initChatModel("gpt-5.4-mini");
const modelWithTools = model.bindTools([{ type: "web_search" }])

const message = await modelWithTools.invoke("What was a positive news story from today?");
console.log(message.contentBlocks);
```

This represents a single conversational turn; there are no associated [ToolMessage](/oss/javascript/langchain/messages#tool-message) objects that need to be passed in as in client-side [tool-calling](#tool-calling).

See the [integration page](/oss/javascript/integrations/chat) for your given provider for available tools and usage details.

### Base URL and proxy settings

You can configure a custom base URL for providers that implement the OpenAI Chat Completions API.

<Warning>
  `model_provider="openai"` (or direct `ChatOpenAI` usage) targets the official OpenAI API specification. Provider-specific fields from routers and proxies may not be extracted or preserved.

  For OpenRouter and LiteLLM, prefer the dedicated integrations:

  * [OpenRouter via `ChatOpenRouter`](/oss/javascript/integrations/chat/openrouter) (`langchain-openrouter`)
  * [LiteLLM via `ChatLiteLLM` / `ChatLiteLLMRouter`](/oss/javascript/integrations/chat) (`langchain-litellm`)
</Warning>

<Accordion title="Custom base URL" icon="link">
  Many model providers offer OpenAI-compatible APIs (e.g., [Together AI](https://www.together.ai/), [vLLM](https://github.com/vllm-project/vllm)). You can use `initChatModel` with these providers by specifying the appropriate `base_url` parameter:

  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  model = initChatModel(
      "MODEL_NAME",
      {
          modelProvider: "openai",
          baseUrl: "BASE_URL",
          apiKey: "YOUR_API_KEY",
      }
  )
  ```

  <Note>
    When using direct chat model class instantiation, the parameter name may vary by provider. Check the respective [reference](/oss/javascript/integrations/providers/overview) for details.
  </Note>
</Accordion>

### Log probabilities

Certain models can be configured to return token-level log probabilities representing the likelihood of a given token by setting the `logprobs` parameter when initializing the model:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
