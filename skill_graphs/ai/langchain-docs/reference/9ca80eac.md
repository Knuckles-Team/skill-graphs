const model = new ChatOpenAI({
    model: "gpt-5.5",
    logprobs: true,
});

const responseMessage = await model.invoke("Why do parrots talk?");

responseMessage.response_metadata.logprobs.content.slice(0, 5);
```

### Token usage

A number of model providers return token usage information as part of the invocation response. When available, this information will be included on the [`AIMessage`](https://reference.langchain.com/javascript/langchain-core/messages/AIMessage) objects produced by the corresponding model. For more details, see the [messages](/oss/javascript/langchain/messages) guide.

### Invocation config

When invoking a model, you can pass additional configuration through the `config` parameter using a [`RunnableConfig`](https://reference.langchain.com/javascript/langchain-core/runnables/RunnableConfig) object. This provides run-time control over execution behavior, callbacks, and metadata tracking.

Common configuration options include:

```typescript Invocation with config theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const response = await model.invoke(
    "Tell me a joke",
    {
        runName: "joke_generation",      // Custom name for this run
        tags: ["humor", "demo"],          // Tags for categorization
        metadata: {"user_id": "123"},     // Custom metadata
        callbacks: [my_callback_handler], // Callback handlers
    }
)
```

These configuration values are particularly useful when:

* Debugging with [LangSmith](/langsmith/observability) tracing
* Implementing custom logging or monitoring
* Controlling resource usage in production
* Tracking invocations across complex pipelines

<Accordion title="Key configuration attributes">
  <ParamField type="string">
    Identifies this specific invocation in logs and traces. Not inherited by sub-calls.
  </ParamField>

  <ParamField type="string[]">
    Labels inherited by all sub-calls for filtering and organization in debugging tools.
  </ParamField>

  <ParamField type="object">
    Custom key-value pairs for tracking additional context, inherited by all sub-calls.
  </ParamField>

  <ParamField type="number">
    Controls the maximum number of parallel calls when using `batch()`.
  </ParamField>

  <ParamField type="CallbackHandler[]">
    Handlers for monitoring and responding to events during execution.
  </ParamField>

  <ParamField type="number">
    Maximum recursion depth for chains to prevent infinite loops in complex pipelines.
  </ParamField>
</Accordion>

<Tip>
  See full [`RunnableConfig`](https://reference.langchain.com/javascript/langchain-core/runnables/RunnableConfig) reference for all supported attributes.
</Tip>

### Dynamic model selection

Dynamic models are selected at <Tooltip>runtime</Tooltip> based on the current <Tooltip>state</Tooltip> and context. This enables sophisticated routing logic and cost optimization.

To use a dynamic model, create middleware with `wrapModelCall` that modifies the model in the request:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { ChatOpenAI } from "@langchain/openai";
import { createAgent, createMiddleware } from "langchain";

const basicModel = new ChatOpenAI({ model: "gpt-5.4-mini" });
const advancedModel = new ChatOpenAI({ model: "gpt-5.5" });

const dynamicModelSelection = createMiddleware({
  name: "DynamicModelSelection",
  wrapModelCall: (request, handler) => {
    // Choose model based on conversation complexity
    const messageCount = request.messages.length;

    return handler({
        ...request,
        model: messageCount > 10 ? advancedModel : basicModel,
    });
  },
});

const agent = createAgent({
  model: "gpt-5.4-mini", // Base model (used when messageCount ≤ 10)
  tools,
  middleware: [dynamicModelSelection],
});
```

For more details on middleware and advanced patterns, see the [middleware documentation](/oss/javascript/langchain/middleware).

<Tip>
  For model configuration details, see [Models](/oss/javascript/langchain/models). For dynamic model selection patterns, see [Dynamic model in middleware](/oss/javascript/langchain/middleware#dynamic-model).
</Tip>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/models.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
