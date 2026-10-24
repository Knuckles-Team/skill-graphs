# Trace Vercel AI SDK applications (JS/TS only)
Source: https://docs.langchain.com/langsmith/trace-with-vercel-ai-sdk

You can use LangSmith to trace runs from the Vercel AI SDK. This guide will walk through an example.

## Installation

<Note>
  This wrapper requires AI SDK v5 and `langsmith>=0.3.63`. If you are using an older version of the AI SDK or `langsmith`, see the OpenTelemetry (OTEL)
  based approach [on this page](/langsmith/legacy-trace-with-vercel-ai-sdk).
</Note>

Install the Vercel AI SDK. This guide uses Vercel's OpenAI integration for the code snippets below, but you can use any of their other options as well.

<CodeGroup>
  ```bash npm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  npm install ai @ai-sdk/openai zod
  ```

  ```bash yarn theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  yarn add ai @ai-sdk/openai zod
  ```

  ```bash pnpm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pnpm add ai @ai-sdk/openai zod
  ```
</CodeGroup>

## Environment configuration

<CodeGroup>
  ```bash Shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  export LANGSMITH_TRACING=true
  export LANGSMITH_API_KEY=<your-api-key>

  # The examples use OpenAI, but you can use any LLM provider of choice
  export OPENAI_API_KEY=<your-openai-api-key>

  # For LangSmith API keys linked to multiple workspaces, set the LANGSMITH_WORKSPACE_ID environment variable to specify which workspace to use.
  export LANGSMITH_WORKSPACE_ID=<your-workspace-id>
  ```
</CodeGroup>

## Basic setup

Import and wrap AI SDK methods, then use them as you normally would:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { openai } from "@ai-sdk/openai";
import * as ai from "ai";

import { wrapAISDK } from "langsmith/experimental/vercel";

const { generateText, streamText, generateObject, streamObject } =
  wrapAISDK(ai);

await generateText({
  model: openai("gpt-5-nano"),
  prompt: "Write a vegetarian lasagna recipe for 4 people.",
});
```

You should see a trace in your LangSmith dashboard [like this one](https://smith.langchain.com/public/4f0e689e-c801-44d3-8857-93b47ab100cc/r).

You can also trace runs with tool calls:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import * as ai from "ai";
import { tool, stepCountIs } from "ai";
import { openai } from "@ai-sdk/openai";
import { z } from "zod";

import { wrapAISDK } from "langsmith/experimental/vercel";

const { generateText, streamText, generateObject, streamObject } =
  wrapAISDK(ai);

await generateText({
  model: openai("gpt-5-nano"),
  messages: [
    {
      role: "user",
      content: "What are my orders and where are they? My user ID is 123",
    },
  ],
  tools: {
    listOrders: tool({
      description: "list all orders",
      inputSchema: z.object({ userId: z.string() }),
      execute: async ({ userId }) =>
        `User ${userId} has the following orders: 1`,
    }),
    viewTrackingInformation: tool({
      description: "view tracking information for a specific order",
      inputSchema: z.object({ orderId: z.string() }),
      execute: async ({ orderId }) =>
        `Here is the tracking information for ${orderId}`,
    }),
  },
  stopWhen: stepCountIs(5),
});
```

Which results in a trace like [this one](https://smith.langchain.com/public/6075fa2c-d255-4885-a66a-4fc798afaa9f/r).

You can use other AI SDK methods exactly as you usually would.

### With `traceable`

You can wrap `traceable` calls around AI SDK calls or within AI SDK tool calls. This is useful if you
want to group runs together in LangSmith:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import * as ai from "ai";
import { tool, stepCountIs } from "ai";
import { openai } from "@ai-sdk/openai";
import { z } from "zod";

import { traceable } from "langsmith/traceable";
import { wrapAISDK } from "langsmith/experimental/vercel";

const { generateText, streamText, generateObject, streamObject } =
  wrapAISDK(ai);

const wrapper = traceable(async (input: string) => {
  const { text } = await generateText({
    model: openai("gpt-5-nano"),
    messages: [
      {
        role: "user",
        content: input,
      },
    ],
    tools: {
      listOrders: tool({
        description: "list all orders",
        inputSchema: z.object({ userId: z.string() }),
        execute: async ({ userId }) =>
          `User ${userId} has the following orders: 1`,
      }),
      viewTrackingInformation: tool({
        description: "view tracking information for a specific order",
        inputSchema: z.object({ orderId: z.string() }),
        execute: async ({ orderId }) =>
          `Here is the tracking information for ${orderId}`,
      }),
    },
    stopWhen: stepCountIs(5),
  });
  return text;
}, {
  name: "wrapper",
});

await wrapper("What are my orders and where are they? My user ID is 123.");
```

The resulting trace will look [like this](https://smith.langchain.com/public/ff25bc26-9389-4798-8b91-2bdcc95d4a8e/r).

## Tracing in serverless environments

When tracing in serverless environments, you must wait for all runs to flush before your environment
shuts down. To do this, you can pass a LangSmith [`Client`](https://docs.smith.langchain.com/reference/js/classes/client.Client) instance when wrapping the AI SDK method,
then call `await client.awaitPendingTraceBatches()`.
Make sure to also pass it into any `traceable` wrappers you create:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import * as ai from "ai";
import { tool, stepCountIs } from "ai";
import { openai } from "@ai-sdk/openai";
import { z } from "zod";

import { Client } from "langsmith";
import { traceable } from "langsmith/traceable";
import { wrapAISDK } from "langsmith/experimental/vercel";

const client = new Client();

const { generateText, streamText, generateObject, streamObject } =
  wrapAISDK(ai, { client });

const wrapper = traceable(async (input: string) => {
  const { text } = await generateText({
    model: openai("gpt-5-nano"),
    messages: [
      {
        role: "user",
        content: input,
      },
    ],
    tools: {
      listOrders: tool({
        description: "list all orders",
        inputSchema: z.object({ userId: z.string() }),
        execute: async ({ userId }) =>
          `User ${userId} has the following orders: 1`,
      }),
      viewTrackingInformation: tool({
        description: "view tracking information for a specific order",
        inputSchema: z.object({ orderId: z.string() }),
        execute: async ({ orderId }) =>
          `Here is the tracking information for ${orderId}`,
      }),
    },
    stopWhen: stepCountIs(5),
  });
  return text;
}, {
  name: "wrapper",
  client,
});

try {
  await wrapper("What are my orders and where are they? My user ID is 123.");
} finally {
  await client.awaitPendingTraceBatches();
}
```

If you are using `Next.js`, there is a convenient [`after`](https://nextjs.org/docs/app/api-reference/functions/after) hook
where you can put this logic:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { after } from "next/server"
import { Client } from "langsmith";

export async function POST(request: Request) {
  const client = new Client();

  ...

  after(async () => {
    await client.awaitPendingTraceBatches();
  });

  return new Response(JSON.stringify({ ... }), {
    status: 200,
    headers: { "Content-Type": "application/json" },
  });
};
```

See [Trace JS functions in serverless environments](/langsmith/serverless-environments) for more detail, including information
around managing rate limits in serverless environments.

## Passing LangSmith config

You can pass LangSmith-specific config to your wrapper both when initially wrapping your
AI SDK methods and while running them via `providerOptions.langsmith`.
This includes metadata (which you can later use to filter runs in LangSmith), top-level run name,
tags, custom client instances, and more.

Config passed while wrapping will apply to all future calls you make with the wrapped method:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { openai } from "@ai-sdk/openai";
import * as ai from "ai";

import { wrapAISDK } from "langsmith/experimental/vercel";

const { generateText, streamText, generateObject, streamObject } =
  wrapAISDK(ai, {
    metadata: {
      key_for_all_runs: "value",
    },
    tags: ["myrun"],
  });

await generateText({
  model: openai("gpt-5-nano"),
  prompt: "Write a vegetarian lasagna recipe for 4 people.",
});
```

While passing config at runtime via `providerOptions.langsmith` will apply only to that run.
We suggest importing and wrapping your config in `createLangSmithProviderOptions` to ensure
proper typing:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { openai } from "@ai-sdk/openai";
import * as ai from "ai";

import {
  wrapAISDK,
  createLangSmithProviderOptions,
} from "langsmith/experimental/vercel";

const { generateText, streamText, generateObject, streamObject } =
  wrapAISDK(ai);

const lsConfig = createLangSmithProviderOptions({
  metadata: {
    individual_key: "value",
  },
  name: "my_individual_run",
});

await generateText({
  model: openai("gpt-5-nano"),
  prompt: "Write a vegetarian lasagna recipe for 4 people.",
  providerOptions: {
    langsmith: lsConfig,
  },
});
```

## Specify a custom run ID

You can pre-specify a run ID per call using `providerOptions` with [`createLangSmithProviderOptions`](https://reference.langchain.com/javascript/langsmith/experimental/vercel#member-createLangSmithProviderOptions-1). Use `uuid7()` from the LangSmith SDK to generate a valid ID:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import * as ai from "ai";
import { openai } from "@ai-sdk/openai";
import { wrapAISDK, createLangSmithProviderOptions } from "langsmith/experimental/vercel";
import { uuid7 } from "langsmith";

const { generateText } = wrapAISDK(ai);

const runId = uuid7();
const lsConfig = createLangSmithProviderOptions({ id: runId });

await generateText({
  model: openai("gpt-5.4-mini"),
  prompt: "What is the capital of France?",
  providerOptions: {
    langsmith: lsConfig,
  },
});

// runId can now be used to attach feedback, query the run, etc.
```

For more details on specifying a run ID manually, refer to [Specify a custom run ID](/langsmith/annotate-code#specify-a-custom-run-id).

## Redacting data

You can customize what inputs and outputs the AI SDK sends to LangSmith by specifying custom input/output
processing functions. This is useful if you are dealing with sensitive data that you would like to
avoid sending to LangSmith.

Because output formats vary depending on which AI SDK method you are using, we suggest defining and passing config
individually into wrapped methods. You will also need to provide separate functions for child LLM runs within
AI SDK calls, since calling `generateText` at top level calls the LLM internally and can do so multiple times.

We also suggest passing a generic parameter into `createLangSmithProviderOptions` to get proper types for inputs and outputs.
Here's an example for `generateText`:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import {
  wrapAISDK,
  createLangSmithProviderOptions,
} from "langsmith/experimental/vercel";
import * as ai from "ai";
import { openai } from "@ai-sdk/openai";

const { generateText } = wrapAISDK(ai);

const lsConfig = createLangSmithProviderOptions<typeof generateText>({
  processInputs: (inputs) => {
    const { messages } = inputs;
    return {
      messages: messages?.map((message) => ({
        providerMetadata: message.providerOptions,
        role: "assistant",
        content: "REDACTED",
      })),
      prompt: "REDACTED",
    };
  },
  processOutputs: (outputs) => {
    return {
      providerMetadata: outputs.providerMetadata,
      role: "assistant",
      content: "REDACTED",
    };
  },
  processChildLLMRunInputs: (inputs) => {
    const { prompt } = inputs;
    return {
      messages: prompt.map((message) => ({
        ...message,
        content: "REDACTED CHILD INPUTS",
      })),
    };
  },
  processChildLLMRunOutputs: (outputs) => {
    return {
      providerMetadata: outputs.providerMetadata,
      content: "REDACTED CHILD OUTPUTS",
      role: "assistant",
    };
  },
});

const { text } = await generateText({
  model: openai("gpt-5-nano"),
  prompt: "What is the capital of France?",
  providerOptions: {
    langsmith: lsConfig,
  },
});

// Paris.
console.log(text);
```

The actual return value will contain the original, non-redacted result but the trace in LangSmith
will be redacted. [Here's an example](https://smith.langchain.com/public/b4c69c8e-285b-4c0c-8492-e571e2cf562f/r).

For redacting tool input/output, wrap your `execute` method in a `traceable` like this:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import * as ai from "ai";
import { tool, stepCountIs } from "ai";
import { openai } from "@ai-sdk/openai";
import { z } from "zod";

import { Client } from "langsmith";
import { traceable } from "langsmith/traceable";
import { wrapAISDK } from "langsmith/experimental/vercel";

const client = new Client();

const { generateText, streamText, generateObject, streamObject } =
  wrapAISDK(ai, { client });

const { text } = await generateText({
  model: openai("gpt-5-nano"),
  messages: [
    {
      role: "user",
      content: "What are my orders? My user ID is 123.",
    },
  ],
  tools: {
    listOrders: tool({
      description: "list all orders",
      inputSchema: z.object({ userId: z.string() }),
      execute: traceable(
        async ({ userId }) => {
          return `User ${userId} has the following orders: 1`;
        },
        {
          processInputs: (input) => ({ text: "REDACTED" }),
          processOutputs: (outputs) => ({ text: "REDACTED" }),
          run_type: "tool",
          name: "listOrders",
        }
      ) as (input: { userId: string }) => Promise<string>,
    }),
  },
  stopWhen: stepCountIs(5),
});
```

The `traceable` return type is complex, which makes the cast necessary. You may also omit the AI SDK `tool` wrapper function
if you wish to avoid the cast.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-with-vercel-ai-sdk.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Trace Visual Studio Code Copilot Chat sessions
Source: https://docs.langchain.com/langsmith/trace-with-vscode-copilot

Capture VS Code Copilot Chat agent interactions, LLM calls, tool executions, and token usage in LangSmith via OpenTelemetry.

[Visual Studio Code Copilot Chat](https://code.visualstudio.com/docs/copilot/overview) can export traces over [OpenTelemetry](https://opentelemetry.io/) (OTel). LangSmith ingests OTLP directly, so you can point Copilot Chat at LangSmith and inspect agent turns, model metadata, tool calls, and token usage alongside the rest of your LLM traces.

This guide is based on Copilot's [Monitor agent usage with OpenTelemetry](https://code.visualstudio.com/docs/copilot/guides/monitoring-agents) reference.

## Prerequisites

Before setting up tracing, ensure you have:

* A recent version of [Visual Studio Code](https://code.visualstudio.com/) with GitHub Copilot Chat installed and signed in.
* A [LangSmith API key](/langsmith/create-account-api-key).

## Configure tracing

Copilot Chat enables OTel emission when any of `COPILOT_OTEL_ENABLED`, `OTEL_EXPORTER_OTLP_ENDPOINT`, or the `github.copilot.chat.otel.enabled` setting is set. The simplest way to send Copilot Chat traces to LangSmith is to export the following environment variables before launching VS Code:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
export COPILOT_OTEL_ENABLED=true
export COPILOT_OTEL_PROTOCOL=http
export COPILOT_OTEL_ENDPOINT=https://api.smith.langchain.com/otel
export COPILOT_OTEL_CAPTURE_CONTENT=true
export OTEL_EXPORTER_OTLP_HEADERS="x-api-key=<your_langsmith_api_key>,Langsmith-Project=<your_project_name>"
```

| Variable                       | Description                                                                                                                                                                                                              |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `COPILOT_OTEL_ENABLED`         | Set to `true` to enable Copilot Chat OTel export.                                                                                                                                                                        |
| `COPILOT_OTEL_PROTOCOL`        | OTLP protocol. Use `http` to target LangSmith's HTTP OTLP ingestion endpoint.                                                                                                                                            |
| `COPILOT_OTEL_ENDPOINT`        | LangSmith OTLP endpoint. Takes precedence over `OTEL_EXPORTER_OTLP_ENDPOINT`.                                                                                                                                            |
| `COPILOT_OTEL_CAPTURE_CONTENT` | Capture full prompts, responses, tool arguments, and tool results on spans. Off by default.                                                                                                                              |
| `OTEL_EXPORTER_OTLP_HEADERS`   | Authentication headers for the OTLP exporter. Use `x-api-key=<your_langsmith_api_key>` and optionally `Langsmith-Project=<project>` to route traces to a specific [LangSmith project](/langsmith/log-traces-to-project). |

VS Code must inherit these environment variables, so export them in the shell session that launches VS Code (for example, by adding them to `~/.zshrc`, `~/.bashrc`, or a shell profile) before starting the editor.

<Note>
  Update the LangSmith endpoint for self-hosted installations or regional SaaS: GCP EU uses `eu.api.smith.langchain.com`; GCP APAC uses `apac.api.smith.langchain.com`; AWS US uses `aws.api.smith.langchain.com`. For self-hosted LangSmith, append `/api/v1/otel` to your LangSmith API URL—for example, `https://ai-company.com/api/v1/otel`.
</Note>

<Warning>
  `COPILOT_OTEL_CAPTURE_CONTENT=true` records full prompt and response content, system prompts, tool schemas, tool arguments, and tool results. Only enable it in trusted environments where capturing source code, file contents, and user prompts is acceptable.
</Warning>

### Alternative: VS Code settings

If you prefer not to set environment variables, you can enable OTel from VS Code settings instead. Open **Settings** (`⌘,` / `Ctrl+,`), search for `copilot otel`, and configure:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "github.copilot.chat.otel.enabled": true,
  "github.copilot.chat.otel.exporterType": "otlp-http",
  "github.copilot.chat.otel.otlpEndpoint": "https://api.smith.langchain.com/otel",
  "github.copilot.chat.otel.captureContent": true
}
```

Authentication headers must still be provided through the `OTEL_EXPORTER_OTLP_HEADERS` environment variable—VS Code settings do not expose a header field. Environment variables also take precedence over VS Code settings when both are set.

## View traces in LangSmith

Start a Copilot Chat session and send a request. Open your [LangSmith project](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-trace-with-vscode-copilot) to view the resulting traces. Each agent interaction produces a hierarchical span tree following the [OTel GenAI Semantic Conventions](https://github.com/open-telemetry/semantic-conventions/blob/main/docs/gen-ai/):

* `invoke_agent` spans wrap the full agent orchestration, including agent name, conversation ID, turn count, and total token usage.
* `chat` spans capture individual LLM API calls with model, token counts, response time, and finish reason.
* `execute_tool` spans capture tool invocations with tool name, type, duration, and success status.

When an agent invokes a subagent, Copilot Chat propagates trace context automatically, so the subagent's `invoke_agent` span appears as a child of the parent's `execute_tool` span in LangSmith.

## Troubleshooting

* **No traces appear in LangSmith.** Confirm `COPILOT_OTEL_ENABLED=true` and that VS Code was launched from the shell where the variables are exported. Verify `OTEL_EXPORTER_OTLP_HEADERS` includes `x-api-key=<your_langsmith_api_key>` and that the API key belongs to the workspace you want to trace into. Restart VS Code after changing environment variables.
* **Traces land in the wrong project.** Set `Langsmith-Project=<your_project_name>` in `OTEL_EXPORTER_OTLP_HEADERS`. If unset, traces go to the workspace's `default` project.
* **Prompts and responses are missing.** Content capture is opt-in. Set `COPILOT_OTEL_CAPTURE_CONTENT=true` (or enable the `github.copilot.chat.otel.captureContent` setting).

## Related resources

* [VS Code Copilot: Monitor agent usage with OpenTelemetry](https://code.visualstudio.com/docs/copilot/guides/monitoring-agents)
* [Trace with OpenTelemetry](/langsmith/trace-with-opentelemetry)
* [Log traces to a project](/langsmith/log-traces-to-project)

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-with-vscode-copilot.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Trace without setting environment variables
Source: https://docs.langchain.com/langsmith/trace-without-env-vars

The following environment variables allow you to configure tracing enabled, the API endpoint, the API key, and the tracing project:

* `LANGSMITH_TRACING`
* `LANGSMITH_API_KEY`
* `LANGSMITH_ENDPOINT`
* `LANGSMITH_PROJECT`

If you need to trace runs with a custom configuration, are working in an environment that doesn’t support typical environment variables (such as Cloudflare Workers), or prefer not to rely on environment variables, LangSmith allows you to configure tracing programmatically.

<Warning>
  In version **0.1.95** of the [Python SDK](/langsmith/smith-python-sdk), `with trace` honors the `LANGSMITH_TRACING` environment variable. For details, refer to the [release notes](https://github.com/langchain-ai/langsmith-sdk/releases/tag/v0.1.95). To disable or enable tracing without setting environment variables, use the `with tracing_context` context manager, as shown in the following example.
</Warning>

* Python: The recommended way to do this in Python is to use the [`tracing_context`](/langsmith/annotate-code#use-the-trace-context-manager-python-only) context manager. This works for both code annotated with `traceable` and code within the `trace` context manager.
* TypeScript: You can pass in both the client and the `tracingEnabled` flag to the [`traceable`](https://reference.langchain.com/javascript/langsmith/traceable) decorator.

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import openai
  from langsmith import Client, tracing_context, traceable
  from langsmith.wrappers import wrap_openai

  langsmith_client = Client(
    api_key="YOUR_LANGSMITH_API_KEY",  # This can be retrieved from a secrets manager
    api_url="https://api.smith.langchain.com",  # Update appropriately for self-hosted installations or regional SaaS
    workspace_id="YOUR_WORKSPACE_ID", # Must be specified for API keys scoped to multiple workspaces
  )

  client = wrap_openai(openai.Client())

  @traceable(run_type="tool", name="Retrieve Context")
  def my_tool(question: str) -> str:
    return "During this morning's meeting, we solved all world conflict."

  @traceable
  def chat_pipeline(question: str):
    context = my_tool(question)
    messages = [
        { "role": "system", "content": "You are a helpful assistant. Please respond to the user's request only based on the given context." },
        { "role": "user", "content": f"Question: {question}\nContext: {context}"}
    ]
    chat_completion = client.chat.completions.create(
        model="gpt-5.4-mini", messages=messages
    )
    return chat_completion.choices[0].message.content

  # Can set to False to disable tracing here without changing code structure
  with tracing_context(enabled=True):
    # Use langsmith_extra to pass in a custom client
    chat_pipeline("Can you summarize this morning's meetings?", langsmith_extra={"client": langsmith_client})
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { Client } from "langsmith";
  import { traceable } from "langsmith/traceable";
  import { wrapOpenAI } from "langsmith/wrappers";
  import { OpenAI } from "openai";

  const client = new Client({
      apiKey: "YOUR_API_KEY",  // This can be retrieved from a secrets manager
      apiUrl: "https://api.smith.langchain.com",  // Update appropriately for self-hosted installations or regional SaaS
  });

  const openai = wrapOpenAI(new OpenAI());

  const tool = traceable((question: string) => {
      return "During this morning's meeting, we solved all world conflict.";
  }, { name: "Retrieve Context", runType: "tool" });

  const pipeline = traceable(
      async (question: string) => {
          const context = await tool(question);

          const completion = await openai.chat.completions.create({
              model: "gpt-5.4-mini",
              messages: [
                  { role: "system" as const, content: "You are a helpful assistant. Please respond to the user's request only based on the given context." },
                  { role: "user" as const, content: `Question: ${question}\nContext: ${context}`}
              ]
          });

          return completion.choices[0].message.content;
      },
      { name: "Chat", client, tracingEnabled: true }
  );

  await pipeline("Can you summarize this morning's meetings?");
  ```
</CodeGroup>

If you prefer a video tutorial, check out the [Alternative Ways to Trace video](https://academy.langchain.com/pages/intro-to-langsmith-preview) from the Introduction to LangSmith Course.

## Related

If you need to dynamically enable or disable tracing based on runtime conditions (such as client requirements, data sensitivity, or compliance policies), refer to [Conditional tracing](/langsmith/conditional-tracing) for examples.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-without-env-vars.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
