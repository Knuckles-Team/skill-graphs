# Trace Mistral applications
Source: https://docs.langchain.com/langsmith/trace-with-mistral

[Mistral](https://mistral.ai/) provides hosted access to open-weight language models via a simple API.

This guide shows you how to trace Mistral API calls with LangSmith, allowing you to record prompts, responses, and metadata for debugging and observability. Traces are sent directly to LangSmith using the [LangSmith SDK](https://reference.langchain.com/python/langsmith/) and standard span instrumentation.

## Installation

Install Mistral’s official library and LangSmith:

<CodeGroup>
  ```bash Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install mistralai langsmith
  ```

  ```bash JavaScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  npm install @mistralai/mistralai langsmith dotenv
  ```
</CodeGroup>

[`mistralai`](https://docs.mistral.ai/getting-started/clients) provides a Mistral client for interacting with Mistral’s API.

## Setup

Set your [API keys](/langsmith/create-account-api-key) and project name:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
export MISTRAL_API_KEY="<your_mistral_api_key>"
export LANGSMITH_TRACING="true"
export LANGSMITH_API_KEY="<your_langsmith_api_key>"
export LANGSMITH_PROJECT="<your_project_name>"  # optional
```

* Ensure you have a Mistral API key from your [Mistral AI account](https://v2.auth.mistral.ai/login) (set this as `MISTRAL_API_KEY`).
* Set `LANGSMITH_TRACING=true` and provide your LangSmith API key (`LANGSMITH_API_KEY`) activates automatic logging of traces.
* Specify a [`LANGSMITH_PROJECT`](/langsmith/log-traces-to-project) name to organize traces by project; if not set, traces go to the default project (named "default").
* The `LANGSMITH_TRACING` flag must be true for any traces to be recorded.

## Configure tracing

1. Instrument the Mistral API call with LangSmith. In your script, create a Mistral client and wrap a call in a traced function:

   <CodeGroup>
     ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
     import os
     from mistralai import Mistral
     from langsmith import traceable

     # Initialize Mistral API client with your API key
     client = Mistral(api_key=os.environ["MISTRAL_API_KEY"])

     @traceable(
         run_type="llm",
         metadata={"ls_provider": "mistral", "ls_model_name": "mistral-medium-latest"},
     )
     def query_mistral(prompt: str):
         response = client.chat.complete(
             model="mistral-medium-latest",
             messages=[{"role": "user", "content": prompt}],
         )
         return response.choices[0].message

     # Example usage
     result = query_mistral("Hello, how are you?")
     print("Mistral response:", result.content)
     ```

     ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
     import { Client } from "langsmith";
     import { traceable } from "langsmith/traceable";
     import { Mistral } from "@mistralai/mistralai";
     import "dotenv/config";

     const mistral = new Mistral({
       apiKey: process.env.MISTRAL_API_KEY,
     });

     const langsmith = new Client();

     const tracedChatCompletion = traceable(
       async (params: {
         model: string;
         messages: Array<{ role: string; content: string }>;
       }) => {
         const response = await mistral.chat.complete(params);
         // Return the message content so LangSmith captures it correctly
         return response.choices[0].message.content;
       },
       {
         name: "Mistral Chat Completion",
         run_type: "llm",
         metadata: {
           ls_provider: "mistral",
           ls_model_name: "mistral-small-latest",
         },
       }
     );

     async function main() {
       const response = await tracedChatCompletion({
         model: "mistral-small-latest",
         messages: [
           { role: "user", content: "Say hello in one short sentence." },
         ],
       });

       console.log(response);
     }

     main();
     ```
   </CodeGroup>

   In this example, you use the [Mistral SDK](https://docs.mistral.ai/getting-started/clients) to send a chat completion request (with a user prompt) and retrieve the model’s answer.

   The [`@traceable`](https://reference.langchain.com/python/langsmith/run_helpers/traceable) decorator (from the [LangSmith Python SDK](https://reference.langchain.com/python/langsmith/observability/sdk/)) wraps the `query_mistral` function so that each invocation is logged as a trace run of type `"llm"`. The `metadata={"ls_provider": "mistral", "ls_model_name": "mistral-medium-latest"}` tags the trace with the provider (Mistral) and model name.

   You can also refer to the [LangSmith JavaScript SDK](https://reference.langchain.com/javascript/modules/langsmith.html).

2. Execute your script to generate a trace. For example:

   <CodeGroup>
     ```bash Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
     python mistral_trace.py
     ```

     ```bash JavaScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
     node index.js
     ```
   </CodeGroup>

   The `query_mistral("Hello, how are you?")` call will reach out to the Mistral API, and because of the `@traceable`/`traceable` wrapper, LangSmith will log this call’s inputs and outputs as a new trace. You'll find the model’s response printed to the console, and a corresponding run appear in [LangSmith](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-trace-with-mistral).

## View traces in LangSmith

After running the example, you can inspect the recorded traces in the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-trace-with-mistral):

1. Open the LangSmith UI and log in to your account.
2. Select the project you used for this integration (for example, the name set in `LANGSMITH_PROJECT`, or default if you didn’t set one).
3. Find the trace corresponding to your Mistral API call. It will be identified by the function name (`query_mistral`) or a custom name if provided.
4. Click on the trace to open it. You’ll be able to inspect the model input and output, including the prompt messages you sent and the response from Mistral, as well as timing information (latency) and any error details if the call failed.

With LangSmith’s tracing, you have full visibility into your Mistral calls—allowing you to debug the behavior of Mistral’s models, monitor performance (e.g., response time and token usage), and compare runs with different parameters using the metadata tags.

## Cost tracking

Although Mistral models are open-weight, using the hosted Mistral API may incur usage-based costs depending on your plan.

LangSmith can automatically associate costs with traced LLM calls by estimating token usage and applying model-specific pricing. When tracing Mistral API calls, LangSmith uses the recorded prompt and response messages to calculate token counts and attach cost information to each run.

To enable automatic cost tracking for LLM calls, refer to [Automatically track costs based on token counts](/langsmith/cost-tracking#llm-calls:-automatically-track-costs-based-on-token-counts).

Once enabled, costs appear directly in the LangSmith UI alongside each traced Mistral run, so that you can monitor usage and compare experiments over time.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-with-mistral.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Trace n8n workflows
Source: https://docs.langchain.com/langsmith/trace-with-n8n

Learn how to trace n8n AI workflows in LangSmith.

[n8n](https://n8n.io/) is a workflow automation platform that includes advanced AI capabilities built on LangChain. You can connect your n8n instance to LangSmith to record and monitor AI workflow runs.

<Note>
  LangSmith tracing is available for **self-hosted n8n instances** only.
</Note>

## Prerequisites

* A [LangSmith account](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-trace-with-n8n) and [API key](/langsmith/create-account-api-key)
* A self-hosted n8n instance

## Set up tracing

1. Set the following environment variables in the environment where you host your n8n instance, in the same way as the rest of your [n8n configuration](https://docs.n8n.io/hosting/configuration/configuration-methods/).

   Required environment variables:

   * `LANGCHAIN_TRACING_V2` — Set to `true` to enable tracing.
   * `LANGCHAIN_API_KEY` — Your LangSmith API key.

   Optional environment variables:

   * `LANGCHAIN_ENDPOINT` — LangSmith API endpoint. Defaults to `https://api.smith.langchain.com`. Set this if using self-hosted LangSmith, GCP EU (`https://eu.api.smith.langchain.com`), GCP APAC (`https://apac.api.smith.langchain.com`), or AWS US (`https://aws.api.smith.langchain.com`).
   * `LANGCHAIN_PROJECT` — Project name for traces. Defaults to `"default"`.
   * `LANGCHAIN_CALLBACKS_BACKGROUND` — Set to `true` for asynchronous trace upload (default), or `false` for synchronous uploads. (default: `true`)

2. Restart your n8n instance for the environment variables to take effect.

## View traces in LangSmith

After running an AI workflow:

1. Open [LangSmith](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-trace-with-n8n).
2. Select your project. If you just created your account, the `"default"` project appears after the first trace is sent.
3. Locate the trace corresponding to your workflow execution.

## Additional resources

* [n8n LangSmith integration guide](https://docs.n8n.io/advanced-ai/langchain/langsmith/)
* [n8n Advanced AI documentation](https://docs.n8n.io/advanced-ai/)

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-with-n8n.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Trace OpenAI Agents SDK applications
Source: https://docs.langchain.com/langsmith/trace-with-openai-agents-sdk

Trace OpenAI Agents SDK Python and JavaScript applications with LangSmith.

The OpenAI Agents SDK lets you build agentic applications powered by OpenAI models.

Use LangSmith to trace OpenAI Agents SDK runs, including agent steps, model calls, tool calls, and handoffs.

<Tabs>
  <Tab title="Python">
    ## Installation

    <Info>
      Requires Python SDK version `langsmith>=0.3.15`.
    </Info>

    Install LangSmith with OpenAI Agents support:

    <CodeGroup>
      ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      pip install "langsmith[openai-agents]"
      ```

      ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      uv add "langsmith[openai-agents]"
      ```
    </CodeGroup>

    This installs both the LangSmith library and the OpenAI Agents SDK.

    ## Environment configuration

    ```bash Shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    export LANGSMITH_API_KEY=<your-api-key>
    export OPENAI_API_KEY=<your-openai-api-key>

    # Optional: set a project for your traces
    export LANGSMITH_PROJECT=<your-project-name>

    # For LangSmith API keys linked to multiple workspaces, set the LANGSMITH_WORKSPACE_ID environment variable to specify which workspace to use.
    export LANGSMITH_WORKSPACE_ID=<your-workspace-id>
    ```

    ## Quick start

    Integrate LangSmith tracing with the OpenAI Agents SDK by using the `OpenAIAgentsTracingProcessor` class.

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import asyncio

    from agents import Agent, Runner, set_trace_processors
    from langsmith.integrations.openai_agents_sdk import OpenAIAgentsTracingProcessor

    async def main():
        agent = Agent(
            name="Captain Obvious",
            instructions="You are Captain Obvious, the world's most literal technical support agent.",
        )

        question = "Why is my code failing when I try to divide by zero? I keep getting this error message."
        result = await Runner.run(agent, question)
        print(result.final_output)

    if __name__ == "__main__":
        set_trace_processors([OpenAIAgentsTracingProcessor()])
        asyncio.run(main())
    ```

    The agent's execution flow, including spans and their details, is logged to LangSmith.
  </Tab>

  <Tab title="JavaScript">
    ## Installation

    <Info>
      Requires JS SDK version `langsmith>=0.5.25`.
    </Info>

    Install LangSmith and the OpenAI Agents SDK:

    <CodeGroup>
      ```bash npm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      npm install langsmith @openai/agents zod
      ```

      ```bash yarn theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      yarn add langsmith @openai/agents zod
      ```

      ```bash pnpm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      pnpm add langsmith @openai/agents zod
      ```
    </CodeGroup>

    ## Environment configuration

    ```bash Shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    export LANGSMITH_API_KEY=<your-api-key>
    export OPENAI_API_KEY=<your-openai-api-key>

    # Optional: set a project for your traces
    export LANGSMITH_PROJECT=<your-project-name>

    # For LangSmith API keys linked to multiple workspaces, set the LANGSMITH_WORKSPACE_ID environment variable to specify which workspace to use.
    export LANGSMITH_WORKSPACE_ID=<your-workspace-id>
    ```

    <Note>
      Installing `OpenAIAgentsTracingProcessor` is an explicit opt-in to tracing. The processor posts traces even when `LANGSMITH_TRACING` is not set, and nested `traceable` calls inside agent tools inherit the active trace context.
    </Note>

    ## Quick start

    Register `OpenAIAgentsTracingProcessor` with the OpenAI Agents SDK before running agents.

    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { Agent, run, setTraceProcessors, tool } from "@openai/agents";
    import { z } from "zod";

    import { OpenAIAgentsTracingProcessor } from "langsmith/wrappers/openai_agents";

    setTraceProcessors([new OpenAIAgentsTracingProcessor()]);

    const getWeather = tool({
      name: "get_weather",
      description: "Get the current weather for a city",
      parameters: z.object({
        city: z.string().describe("The city to get weather for"),
      }),
      execute: async ({ city }: { city: string }) => {
        return `The weather in ${city} is sunny.`;
      },
    });

    const agent = new Agent({
      name: "WeatherAgent",
      instructions: "You are a helpful assistant. Use the get_weather tool when asked about weather.",
      model: "gpt-5-nano",
      tools: [getWeather],
    });

    const result = await run(agent, "What's the weather in San Francisco?");
    console.log(result.finalOutput);
    ```

    The resulting trace contains the root agent run, response spans, and nested tool call spans.

    ## Configure the processor

    Pass options to the processor to set a LangSmith client, project, tags, metadata, or root trace name.

    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { Agent, run, setTraceProcessors } from "@openai/agents";

    import { Client } from "langsmith";
    import { OpenAIAgentsTracingProcessor } from "langsmith/wrappers/openai_agents";

    const client = new Client();
    const processor = new OpenAIAgentsTracingProcessor({
      client,
      projectName: "openai-agents-demo",
      name: "Support agent workflow",
      tags: ["openai-agents"],
      metadata: {
        environment: "development",
      },
    });

    setTraceProcessors([processor]);

    const agent = new Agent({
      name: "SupportAgent",
      instructions: "You are a concise support agent.",
      model: "gpt-5-nano",
    });

    const result = await run(agent, "Help me reset my password.");
    console.log(result.finalOutput);
    ```

    ## Nest `traceable` calls in tools

    You can use `traceable` inside OpenAI Agents SDK tool handlers. LangSmith nests those runs under the active tool span.

    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { Agent, run, setTraceProcessors, tool } from "@openai/agents";
    import { z } from "zod";

    import { traceable } from "langsmith/traceable";
    import { OpenAIAgentsTracingProcessor } from "langsmith/wrappers/openai_agents";

    setTraceProcessors([new OpenAIAgentsTracingProcessor()]);

    const lookupOrder = traceable(
      async (orderId: string) => {
        return { orderId, status: "shipped" };
      },
      { name: "lookup_order" }
    );

    const orderStatus = tool({
      name: "order_status",
      description: "Look up the status of an order",
      parameters: z.object({
        orderId: z.string().describe("The order ID to look up"),
      }),
      execute: async ({ orderId }: { orderId: string }) => {
        return JSON.stringify(await lookupOrder(orderId));
      },
    });

    const agent = new Agent({
      name: "OrdersAgent",
      instructions: "Use the order_status tool to answer order questions.",
      model: "gpt-5-nano",
      tools: [orderStatus],
    });

    await run(agent, "Where is order 123?");
    ```

    ## Flush traces in serverless environments

    When tracing in serverless environments, flush pending traces before the process exits.

    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { Agent, run, setTraceProcessors } from "@openai/agents";

    import { Client } from "langsmith";
    import { OpenAIAgentsTracingProcessor } from "langsmith/wrappers/openai_agents";

    const client = new Client();
    const processor = new OpenAIAgentsTracingProcessor({ client });
    setTraceProcessors([processor]);

    try {
      const agent = new Agent({
        name: "SupportAgent",
        instructions: "You are a concise support agent.",
        model: "gpt-5-nano",
      });

      const result = await run(agent, "Help me reset my password.");
      console.log(result.finalOutput);
    } finally {
      await processor.forceFlush();
    }
    ```
  </Tab>
</Tabs>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-with-openai-agents-sdk.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Trace OpenAI-compatible providers
Source: https://docs.langchain.com/langsmith/trace-with-openai-compatible

Trace LLM calls from any OpenAI-compatible provider to LangSmith.

Many LLM providers accept requests in the same format as the OpenAI API. To trace calls from these providers to LangSmith, construct an OpenAI client pointed at the provider's base URL, then wrap it with [`wrap_openai`](https://reference.langchain.com/python/langsmith/wrappers/_openai/wrap_openai) / [`wrapOpenAI`](https://reference.langchain.com/javascript/modules/langsmith.html).

Use `wrap_openai` / `wrapOpenAI` for direct API calls. Use [`@traceable`](https://reference.langchain.com/python/langsmith/run_helpers/traceable) when you need to trace application logic around the call or set metadata per invocation.

|                | `wrap_openai` / `wrapOpenAI`                                      | `@traceable` / `traceable`                                                                                            |
| -------------- | ----------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| Token tracking | Automatic                                                         | Requires `run_type="llm"`                                                                                             |
| Run type       | LLM (set automatically)                                           | Chain by default                                                                                                      |
| Traces         | The API call                                                      | The function wrapping it                                                                                              |
| Metadata       | Client-level only (Python); client-level or per-call (TypeScript) | Per-call via [`langsmith_extra`](https://reference.langchain.com/python/langsmith/run_helpers/SupportsLangsmithExtra) |

<Note>To trace OpenAI directly, refer to [Trace OpenAI applications](/langsmith/trace-openai).</Note>

## Setup

<CodeGroup>
  ```bash Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install langsmith openai
  ```

  ```bash npm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  npm install langsmith openai
  ```
</CodeGroup>

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
export LANGSMITH_API_KEY=<your-api-key>
export LANGSMITH_TRACING=true
```

## Trace API calls

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import os

  import openai
  from langsmith import wrappers

  client = wrappers.wrap_openai(
      openai.OpenAI(
          base_url="https://<provider-base-url>/v1",
          api_key=os.environ["PROVIDER_API_KEY"],
      )
  )

  completion = client.chat.completions.create(
      model="<provider-model-name>",
      messages=[{"role": "user", "content": "Hello!"}],
  )
  print(completion.choices[0].message.content)
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import OpenAI from "openai";
  import { wrapOpenAI } from "langsmith/wrappers/openai";

  const client = wrapOpenAI(
    new OpenAI({
      baseURL: "https://<provider-base-url>/v1",
      apiKey: process.env.PROVIDER_API_KEY!,
    })
  );

  const completion = await client.chat.completions.create({
    model: "<provider-model-name>",
    messages: [{ role: "user", content: "Hello!" }],
  });
  console.log(completion.choices[0].message.content);
  ```
</CodeGroup>

## Add metadata

<Tabs>
  <Tab title="Python">
    Pass `tracing_extra` when wrapping the client. The metadata applies to all calls made with that client.

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import os

    import openai

    from langsmith import wrappers

    client = wrappers.wrap_openai(
        openai.OpenAI(
            base_url="https://<provider-base-url>/v1",
            api_key=os.environ["PROVIDER_API_KEY"],
        ),
        tracing_extra={"metadata": {"environment": "production"}},
    )
    ```
  </Tab>

  <Tab title="TypeScript">
    Pass options as the second argument to `wrapOpenAI` for client-level metadata, or pass [`langsmithExtra`](https://reference.langchain.com/javascript/modules/langsmith.html) per call.

    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import OpenAI from "openai";
    import { wrapOpenAI } from "langsmith/wrappers/openai";

    const client = wrapOpenAI(
      new OpenAI({
        baseURL: "https://<provider-base-url>/v1",
        apiKey: process.env.PROVIDER_API_KEY!,
      }),
      { metadata: { environment: "production" } }
    );

    // Per-call metadata
    const completion = await client.chat.completions.create(
      {
        model: "<provider-model-name>",
        messages: [{ role: "user", content: "Hello!" }],
      },
      { langsmithExtra: { metadata: { request_id: "abc123" } } }
    );
    ```
  </Tab>
</Tabs>

## Related guides

Some providers have dedicated setup guides that use `@traceable` or a native callback. These approaches trace at the function level rather than wrapping the client directly, or integrate with the provider's own SDK and routing layer.

* [DeepSeek](/langsmith/trace-deepseek): OpenAI-compatible API; guide uses `@traceable` with custom provider metadata
* [LiteLLM](/langsmith/trace-litellm): proxy that exposes an OpenAI-compatible endpoint; guide covers `@traceable` and LiteLLM's built-in LangSmith callback

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-with-openai-compatible.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Trace OpenCode sessions
Source: https://docs.langchain.com/langsmith/trace-with-opencode

Capture OpenCode sessions, assistant turns, tool calls, and subagent activity in LangSmith.

The `@langchain/langsmith-opencode` plugin sends [OpenCode](https://opencode.ai/) session traces to LangSmith. Use it to inspect agent turns, model metadata, token usage, tool calls, tool errors, attachments, and subagent activity from your OpenCode workflows.

## Prerequisites

Before setting up tracing, ensure you have:

* [OpenCode](https://opencode.ai/) installed and configured.
* A [LangSmith API key](/langsmith/create-account-api-key).
* Access to configure the OpenCode `plugin` key in `opencode.json` or `~/.config/opencode/opencode.json`.

## Install and enable the plugin

Add the plugin to your OpenCode configuration file. You can configure it locally in `opencode.json` or globally in `~/.config/opencode/opencode.json`:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "$schema": "https://opencode.ai/config.json",
  "plugin": ["@langchain/langsmith-opencode"]
}
```

Enable tracing and provide your LangSmith API key before starting OpenCode:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
export TRACE_TO_LANGSMITH="true"
export LANGSMITH_API_KEY="<your-langsmith-api-key>"
export LANGSMITH_PROJECT="opencode"
```

Run OpenCode as usual. The plugin sends completed user turns to the configured LangSmith project.

## Configure tracing

Tracing is disabled by default. With `TRACE_TO_LANGSMITH=true` set, the plugin sends traces to LangSmith. You can also enable tracing with a LangSmith config file.

### Environment variables

The plugin reads OpenCode-specific variables first, then falls back to the generic LangSmith SDK variables when available.

| Variable                            | Required    | Default               | Description                                                                                                   |
| ----------------------------------- | ----------- | --------------------- | ------------------------------------------------------------------------------------------------------------- |
| `TRACE_TO_LANGSMITH`                | Yes         | `false`               | Set to `"true"` to enable tracing.                                                                            |
| `LANGSMITH_OPENCODE_API_KEY`        | Conditional | -                     | LangSmith API key. Falls back to `LANGSMITH_API_KEY`. Required unless every replica provides its own API key. |
| `LANGSMITH_OPENCODE_ENDPOINT`       | No          | LangSmith SDK default | LangSmith API URL. Falls back to `LANGSMITH_ENDPOINT`.                                                        |
| `LANGSMITH_OPENCODE_PROJECT`        | No          | `opencode`            | LangSmith project name. Falls back to `LANGSMITH_PROJECT`.                                                    |
| `LANGSMITH_OPENCODE_METADATA`       | No          | -                     | JSON object merged into root trace metadata.                                                                  |
| `LANGSMITH_OPENCODE_RUNS_ENDPOINTS` | No          | -                     | JSON array of replica destinations.                                                                           |

For example:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
export TRACE_TO_LANGSMITH="true"
export LANGSMITH_API_KEY="<your-langsmith-api-key>"
export LANGSMITH_PROJECT="opencode"
export LANGSMITH_OPENCODE_METADATA='{"team":"agents","environment":"dev"}'
```

### Config files

Use `.opencode/langsmith.json` for project-level settings or `~/.config/opencode/langsmith.json` for global defaults.

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "enabled": true,
  "api_key": "<your-langsmith-api-key>",
  "api_url": "https://api.smith.langchain.com",
  "project": "opencode",
  "metadata": {
    "team": "agents",
    "environment": "dev"
  }
}
```

| Field      | Required    | Default               | Description                                                                      |
| ---------- | ----------- | --------------------- | -------------------------------------------------------------------------------- |
| `enabled`  | Yes         | `false`               | Set to `true` to enable tracing from the config file.                            |
| `api_key`  | Conditional | -                     | LangSmith API key. Required unless provided by environment variable or replicas. |
| `api_url`  | No          | LangSmith SDK default | LangSmith API URL, usually `https://api.smith.langchain.com`.                    |
| `project`  | No          | `opencode`            | LangSmith project name.                                                          |
| `metadata` | No          | -                     | Object merged into root trace metadata.                                          |
| `replicas` | No          | -                     | Additional LangSmith destinations to replicate traces to.                        |

Keep config files that include API keys out of version control.

## Trace to multiple destinations

Set `replicas` in `langsmith.json` or `LANGSMITH_OPENCODE_RUNS_ENDPOINTS` to send the same trace data to additional LangSmith workspaces or projects.

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "enabled": true,
  "api_key": "<your-langsmith-api-key>",
  "project": "opencode",
  "replicas": [
    {
      "api_url": "https://api.smith.langchain.com",
      "api_key": "<your-replica-langsmith-api-key>",
      "project": "opencode-replica",
      "updates": {
        "metadata": {
          "replica": true
        }
      }
    }
  ]
}
```

Replica objects support both snake\_case and LangSmith SDK-style camelCase field names. snake\_case is recommended in config files.

| Field                     | Description                                                                 |
| ------------------------- | --------------------------------------------------------------------------- |
| `api_url` / `apiUrl`      | LangSmith API URL for the replica destination.                              |
| `api_key` / `apiKey`      | API key for the destination workspace.                                      |
| `project` / `projectName` | Project name in the destination workspace.                                  |
| `updates`                 | Optional run fields to override on replicated runs, such as extra metadata. |

## What gets traced

The plugin listens to OpenCode chat and event hooks, aggregates each completed user turn, and submits it to LangSmith as a run tree.

* `opencode.session` root runs for completed user turns.
* `opencode.assistant.turn` child runs for assistant and model responses.
* Nested tool runs for tool calls, including inputs, outputs, errors, timing, and attachments when available.
* Subagent sessions nested under the parent tool call.
* Model name, provider, invocation parameters, token usage, and thread or session ID metadata.
* User messages, assistant messages, reasoning blocks, file parts, and system prompts associated with assistant turns.

Trace completion is based on OpenCode `step-finish` events. The plugin also flushes pending trace batches when the OpenCode server shuts down.

## View traces in LangSmith

Open the configured LangSmith project and look for root runs named `opencode.session`. Each trace contains the user turn as the root input and assistant responses, tool calls, and subagent traces as child runs. The plugin stores the OpenCode session ID as `thread_id` metadata, so you can filter or group related OpenCode turns in LangSmith.

## Troubleshooting

If traces do not appear in LangSmith:

* Confirm tracing is enabled with `TRACE_TO_LANGSMITH=true` or `"enabled": true` in config.
* Confirm the LangSmith API key is set in the same shell, project config, or global config used by OpenCode.
* Confirm the plugin package is installed where OpenCode can resolve it.
* Check the selected LangSmith project. If no project is configured, traces go to `opencode`.
* Restart OpenCode after changing `opencode.json`, `langsmith.json`, or environment variables.
* Make sure a user turn completes. The plugin does not send incomplete turns.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-with-opencode.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Trace with OpenTelemetry
Source: https://docs.langchain.com/langsmith/trace-with-opentelemetry

Configure OpenTelemetry tracing in LangSmith, including LANGSMITH_OTEL_ENABLED and OTEL fanout with the OpenTelemetry Collector.

LangSmith supports OpenTelemetry-based tracing, allowing you to send traces from any OpenTelemetry-compatible application. This guide covers both automatic instrumentation for LangChain applications and manual instrumentation for other frameworks.

Learn how to trace your LLM applications using OpenTelemetry with LangSmith.

<Note>
  Update the LangSmith URL appropriately for self-hosted installations or regional SaaS in the requests below: GCP EU uses `eu.api.smith.langchain.com`; GCP APAC uses `apac.api.smith.langchain.com`; AWS US uses `aws.api.smith.langchain.com`.
</Note>

## Trace a LangChain application

If you're using LangChain or LangGraph, use the built-in integration to trace your application:

1. Install the LangSmith package with OpenTelemetry support:

   <CodeGroup>
     ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
     pip install "langsmith[otel]"
     pip install langchain
     ```
   </CodeGroup>

   <Info>
     Requires Python SDK version `langsmith>=0.3.18`. We recommend `langsmith>=0.4.25` to benefit from important OpenTelemetry fixes.
   </Info>

2. In your LangChain/LangGraph App, enable the OpenTelemetry integration by setting the `LANGSMITH_OTEL_ENABLED` environment variable:

   <CodeGroup>
     ```bash Shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
     LANGSMITH_OTEL_ENABLED=true
     LANGSMITH_TRACING=true
     LANGSMITH_ENDPOINT=https://api.smith.langchain.com
     LANGSMITH_API_KEY=<your_langsmith_api_key>
     # For LangSmith API keys linked to multiple workspaces, set the LANGSMITH_WORKSPACE_ID environment variable to specify which workspace to use.
     ```
   </CodeGroup>

3. Create a LangChain application with tracing. For example:

   ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
   import os
   from langchain_openai import ChatOpenAI
   from langchain_core.prompts import ChatPromptTemplate

   # Create a chain
   prompt = ChatPromptTemplate.from_template("Tell me a joke about {topic}")
   model = ChatOpenAI()
   chain = prompt | model

   # Run the chain
   result = chain.invoke({"topic": "programming"})
   print(result.content)
   ```

4. View the traces in your LangSmith dashboard ([example](https://smith.langchain.com/public/a762af6c-b67d-4f22-90a0-728df16baeba/r)) once your application runs.

## Trace a non-LangChain application

For non-LangChain applications or custom instrumentation, you can trace your application in LangSmith with a standard OpenTelemetry client. (We recommend **langsmith ≥ 0.4.25**.)

1. Install the OpenTelemetry SDK, OpenTelemetry exporter packages, as well as the OpenAI package:

   <CodeGroup>
     ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
     pip install openai
     pip install opentelemetry-sdk
     pip install opentelemetry-exporter-otlp
     ```
   </CodeGroup>

2. Setup environment variables for the endpoint, substitute your specific values:

   <CodeGroup>
     ```bash Shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
     OTEL_EXPORTER_OTLP_ENDPOINT=https://api.smith.langchain.com/otel
     OTEL_EXPORTER_OTLP_HEADERS="x-api-key=<your langsmith api key>"
     ```
   </CodeGroup>

   <Note>
     Depending on how your otel exporter is configured, you may need to append `/v1/traces` to the endpoint if you are only sending traces.
   </Note>

   <Note>
     If you're self-hosting LangSmith, replace the base endpoint with your LangSmith api endpoint and append `/api/v1`. For example: `OTEL_EXPORTER_OTLP_ENDPOINT=https://ai-company.com/api/v1/otel`
   </Note>

   Optional: Specify a custom project name other than "default":

   <CodeGroup>
     ```bash Shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
     OTEL_EXPORTER_OTLP_ENDPOINT=https://api.smith.langchain.com/otel
     OTEL_EXPORTER_OTLP_HEADERS="x-api-key=<your langsmith api key>,Langsmith-Project=<project name>"
     ```
   </CodeGroup>

3. Log a trace.

   This code sets up an OTEL tracer and exporter that will send traces to LangSmith. It then calls OpenAI and sends the required OpenTelemetry attributes.

   ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
   from openai import OpenAI
   from opentelemetry import trace
   from opentelemetry.sdk.trace import TracerProvider
   from opentelemetry.sdk.trace.export import (
       BatchSpanProcessor,
   )
   from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter

   client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

   otlp_exporter = OTLPSpanExporter(
       timeout=10,
   )

   trace.set_tracer_provider(TracerProvider())
   trace.get_tracer_provider().add_span_processor(
       BatchSpanProcessor(otlp_exporter)
   )

   tracer = trace.get_tracer(__name__)

   def call_openai():
       model = "gpt-5.4-mini"
       with tracer.start_as_current_span("call_open_ai") as span:
           span.set_attribute("langsmith.span.kind", "LLM")
           span.set_attribute("langsmith.metadata.user_id", "user_123")
           span.set_attribute("gen_ai.system", "OpenAI")
           span.set_attribute("gen_ai.request.model", model)
           span.set_attribute("llm.request.type", "chat")

           messages = [
               {"role": "system", "content": "You are a helpful assistant."},
               {
                   "role": "user",
                   "content": "Write a haiku about recursion in programming."
               }
           ]

           for i, message in enumerate(messages):
               span.set_attribute(f"gen_ai.prompt.{i}.content", str(message["content"]))
               span.set_attribute(f"gen_ai.prompt.{i}.role", str(message["role"]))

           completion = client.chat.completions.create(
               model=model,
               messages=messages
           )

           span.set_attribute("gen_ai.response.model", completion.model)
           span.set_attribute("gen_ai.completion.0.content", str(completion.choices[0].message.content))
           span.set_attribute("gen_ai.completion.0.role", "assistant")
           span.set_attribute("gen_ai.usage.prompt_tokens", completion.usage.prompt_tokens)
           span.set_attribute("gen_ai.usage.completion_tokens", completion.usage.completion_tokens)
           span.set_attribute("gen_ai.usage.total_tokens", completion.usage.total_tokens)

           return completion.choices[0].message

   if __name__ == "__main__":
       call_openai()
   ```

4. View the trace in your LangSmith dashboard ([example](https://smith.langchain.com/public/4f2890b1-f105-44aa-a6cf-c777dcc27a37/r)).

## Send traces to an alternate provider

While LangSmith is the default destination for OpenTelemetry traces, you can also configure OpenTelemetry to send traces to other observability platforms.

<Info>
  Available in LangSmith Python SDK **≥ 0.4.1**. We recommend **≥ 0.4.25** for fixes that improve OTEL export and hybrid fan-out stability.
</Info>

### Use environment variables for global configuration

By default, the LangSmith OpenTelemetry exporter will send data to the LangSmith API OTEL endpoint, but this can be customized by setting standard OTEL environment variables:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
OTEL_EXPORTER_OTLP_ENDPOINT: Override the endpoint URL
OTEL_EXPORTER_OTLP_HEADERS: Add custom headers (LangSmith API keys and Project are added automatically)
OTEL_SERVICE_NAME: Set a custom service name (defaults to "langsmith")
```

LangSmith uses the HTTP trace exporter by default. If you'd like to use your own tracing provider, you can either:

1. Set the OTEL environment variables as shown above, or
2. Set a global trace provider before initializing LangChain components, which LangSmith will detect and use instead of creating its own.

### Configure alternate OTLP endpoints

To send traces to a different provider, configure the OTLP exporter with your provider's endpoint:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import os

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

# Set environment variables for LangChain
os.environ["LANGSMITH_OTEL_ENABLED"] = "true"
os.environ["LANGSMITH_TRACING"] = "true"

# Configure the OTLP exporter for your custom endpoint
provider = TracerProvider()
otlp_exporter = OTLPSpanExporter(
    # Change to your provider's endpoint
    endpoint="https://otel.your-provider.com/v1/traces",
    # Add any required headers for authentication
    headers={"api-key": "your-api-key"},
)
processor = BatchSpanProcessor(otlp_exporter)
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)
