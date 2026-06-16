# LangSmith Observability
Source: https://docs.langchain.com/oss/javascript/langchain/observability

As you build and run agents with LangChain, you need visibility into how they behave: which [tools](/oss/javascript/langchain/tools) they call, what prompts they generate, and how they make decisions. LangChain agents built with [`createAgent`](https://reference.langchain.com/javascript/langchain/index/createAgent) automatically support tracing through [LangSmith](/langsmith/observability), a platform for capturing, debugging, evaluating, and monitoring LLM application behavior.

[*Traces*](/langsmith/observability-concepts#traces) record every step of your agent's execution, from the initial user input to the final response, including all tool calls, model interactions, and decision points. This execution data helps you debug issues, evaluate performance across different inputs, and monitor usage patterns in production.

This guide shows you how to enable tracing for your LangChain agents and use LangSmith to analyze their execution.

## Prerequisites

Before you begin, ensure you have the following:

* **A LangSmith account**: Sign up (for free) or log in at [smith.langchain.com](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=oss-langchain-observability).
* **A LangSmith API key**: Follow the [Create an API key](/langsmith/create-account-api-key) guide.

## Enable tracing

All LangChain agents automatically support LangSmith tracing. To enable it, set the following environment variables:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
export LANGSMITH_TRACING=true
export LANGSMITH_API_KEY=<your-api-key>
```

## Quickstart

No extra code is needed to log a trace to LangSmith. Just run your agent code as you normally would:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { createAgent } from "@langchain/agents";

function sendEmail(to: string, subject: string, body: string): string {
    // ... email sending logic
    return `Email sent to ${to}`;
}

function searchWeb(query: string): string {
    // ... web search logic
    return `Search results for: ${query}`;
}

const agent = createAgent({
    model: "gpt-5.5",
    tools: [sendEmail, searchWeb],
    systemPrompt: "You are a helpful assistant that can send emails and search the web."
});

// Run the agent - all steps will be traced automatically
const response = await agent.invoke({
    messages: [{ role: "user", content: "Search for the latest AI news and email a summary to john@example.com" }]
});
```

By default, the trace will be logged to the project with the name `default`. To configure a custom project name, see [Log to a project](/langsmith/log-traces-to-project).

## Trace selectively

You may opt to trace specific invocations or parts of your application using LangSmith's `tracing_context` context manager:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { LangChainTracer } from "@langchain/core/tracers/tracer_langchain";

// This WILL be traced
const tracer = new LangChainTracer();
await agent.invoke(
  {
    messages: [{role: "user", content: "Send a test email to alice@example.com"}]
  },
  { callbacks: [tracer] }
);

// This will NOT be traced (if LANGSMITH_TRACING is not set)
await agent.invoke(
  {
    messages: [{role: "user", content: "Send another email"}]
  }
);
```

## Log to a project

<Accordion title="Statically">
  You can set a custom project name for your entire application by setting the `LANGSMITH_PROJECT` environment variable:

  ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  export LANGSMITH_PROJECT=my-agent-project
  ```
</Accordion>

<Accordion title="Dynamically">
  You can set the project name programmatically for specific operations:

  ```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { LangChainTracer } from "@langchain/core/tracers/tracer_langchain";

  const tracer = new LangChainTracer({ projectName: "email-agent-test" });
  await agent.invoke(
    {
      messages: [{role: "user", content: "Send a test email to alice@example.com"}]
    },
    { callbacks: [tracer] }
  );
  ```
</Accordion>

## Add metadata to traces

You can annotate your traces with custom metadata and tags:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { LangChainTracer } from "@langchain/core/tracers/tracer_langchain";

const tracer = new LangChainTracer({ projectName: "email-agent-test" });
await agent.invoke(
  {
    messages: [{role: "user", content: "Send a test email to alice@example.com"}]
  },
  {
    tags: ["production", "email-assistant", "v1.0"],
    metadata: {
      userId: "user123",
      sessionId: "session456",
      environment: "production"
    }
  },
);

```

This custom metadata and tags will be attached to the trace in LangSmith.

<Tip>
  To learn more about how to use traces to debug, evaluate, and monitor your agents, see the [LangSmith documentation](/langsmith/observability).
</Tip>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/observability.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# LangChain overview
Source: https://docs.langchain.com/oss/javascript/langchain/overview

LangChain provides create_agent: a minimal, highly configurable agent harness. Compose exactly the agent your use case needs from model, tools, prompt, and middleware.

**Agent = Model + Harness.** LangChain provides `create_agent`: a minimal, highly configurable harness. The harness is everything around the model loop: the prompt, the tools, and any middleware that shapes behavior. Start with the primitives and compose exactly what your use case needs. Supports [OpenAI, Anthropic, Google, and more](/oss/javascript/integrations/providers/overview).

<Tip>
  **LangChain vs. LangGraph vs. Deep Agents**

  Start with [Deep Agents](/oss/javascript/deepagents/overview/) for a "batteries-included" agent with features like automatic context compression, a virtual filesystem, and subagent-spawning. Deep Agents are built on LangChain [agents](/oss/javascript/langchain/agents/) which you can also use directly.

  Use [LangChain](/oss/javascript/langchain/agents) (`create_agent`) for a highly customizable harness, easily tailored to your use case and data.

  Use [LangGraph](/oss/javascript/langgraph/overview), our low-level orchestration framework, for advanced needs combining deterministic and agentic workflows.

  Use [LangSmith](/langsmith/observability) to trace, debug, and evaluate agents built with any of these frameworks. Follow the [tracing quickstart](/langsmith/trace-with-langchain) to get set up. We recommend you also set up [LangSmith Engine](/langsmith/engine) which monitors your traces, detects issues, and proposes fixes.
</Tip>

## <Icon icon="wand" /> Create an agent

This example demonstrates how to create a simple LangChain agent with a custom tool:

<CodeGroup>
  ```ts OpenAI theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  // First install: npm install langchain zod @langchain/openai
  import { createAgent, tool } from "langchain";
  import * as z from "zod";

  const getWeather = tool(
    (input) => `It's always sunny in ${input.city}!`,
    {
      name: "get_weather",
      description: "Get the weather for a given city",
      schema: z.object({
        city: z.string().describe("The city to get the weather for"),
      }),
    }
  );

  const agent = createAgent({
    model: "gpt-5.5",
    tools: [getWeather],
  });

  console.log(
    await agent.invoke({
      messages: [{ role: "user", content: "What's the weather in San Francisco?" }],
    })
  );
  ```

  ```ts Google Gemini theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  // First install: npm install langchain zod @langchain/google-genai
  import { createAgent, tool } from "langchain";
  import * as z from "zod";

  const getWeather = tool(
    (input) => `It's always sunny in ${input.city}!`,
    {
      name: "get_weather",
      description: "Get the weather for a given city",
      schema: z.object({
        city: z.string().describe("The city to get the weather for"),
      }),
    }
  );

  const agent = createAgent({
    model: "google-genai:gemini-2.5-flash-lite",
    tools: [getWeather],
  });

  console.log(
    await agent.invoke({
      messages: [{ role: "user", content: "What's the weather in San Francisco?" }],
    })
  );
  ```

  ```ts Claude (Anthropic) theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  // First install: npm install langchain zod @langchain/anthropic
  import { createAgent, tool } from "langchain";
  import * as z from "zod";

  const getWeather = tool(
    (input) => `It's always sunny in ${input.city}!`,
    {
      name: "get_weather",
      description: "Get the weather for a given city",
      schema: z.object({
        city: z.string().describe("The city to get the weather for"),
      }),
    }
  );

  const agent = createAgent({
    model: "claude-sonnet-4-6",
    tools: [getWeather],
  });

  console.log(
    await agent.invoke({
      messages: [{ role: "user", content: "What's the weather in San Francisco?" }],
    })
  );
  ```

  ```ts OpenRouter theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  // First install: npm install langchain zod @langchain/openrouter
  import { createAgent, tool } from "langchain";
  import * as z from "zod";

  const getWeather = tool(
    (input) => `It's always sunny in ${input.city}!`,
    {
      name: "get_weather",
      description: "Get the weather for a given city",
      schema: z.object({
        city: z.string().describe("The city to get the weather for"),
      }),
    }
  );

  const agent = createAgent({
    model: "openrouter:anthropic/claude-sonnet-4-6",
    tools: [getWeather],
  });

  console.log(
    await agent.invoke({
      messages: [{ role: "user", content: "What's the weather in San Francisco?" }],
    })
  );
  ```

  ```ts Fireworks theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  // First install: npm install langchain zod
  import { createAgent, tool } from "langchain";
  import * as z from "zod";

  const getWeather = tool(
    (input) => `It's always sunny in ${input.city}!`,
    {
      name: "get_weather",
      description: "Get the weather for a given city",
      schema: z.object({
        city: z.string().describe("The city to get the weather for"),
      }),
    }
  );

  const agent = createAgent({
    model: "fireworks:accounts/fireworks/models/qwen3p5-397b-a17b",
    tools: [getWeather],
  });

  console.log(
    await agent.invoke({
      messages: [{ role: "user", content: "What's the weather in San Francisco?" }],
    })
  );
  ```

  ```ts Baseten theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  // First install: npm install langchain zod
  import { createAgent, tool } from "langchain";
  import * as z from "zod";

  const getWeather = tool(
    (input) => `It's always sunny in ${input.city}!`,
    {
      name: "get_weather",
      description: "Get the weather for a given city",
      schema: z.object({
        city: z.string().describe("The city to get the weather for"),
      }),
    }
  );

  const agent = createAgent({
    model: "baseten:zai-org/GLM-5",
    tools: [getWeather],
  });

  console.log(
    await agent.invoke({
      messages: [{ role: "user", content: "What's the weather in San Francisco?" }],
    })
  );
  ```

  ```ts Ollama theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  // First install: npm install langchain zod @langchain/ollama
  import { createAgent, tool } from "langchain";
  import * as z from "zod";

  const getWeather = tool(
    (input) => `It's always sunny in ${input.city}!`,
    {
      name: "get_weather",
      description: "Get the weather for a given city",
      schema: z.object({
        city: z.string().describe("The city to get the weather for"),
      }),
    }
  );

  const agent = createAgent({
    model: "ollama:devstral-2",
    tools: [getWeather],
  });

  console.log(
    await agent.invoke({
      messages: [{ role: "user", content: "What's the weather in San Francisco?" }],
    })
  );
  ```

  ```ts Azure theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  // First install: npm install langchain zod @langchain/openai
  import { createAgent, tool } from "langchain";
  import * as z from "zod";

  const getWeather = tool(
    (input) => `It's always sunny in ${input.city}!`,
    {
      name: "get_weather",
      description: "Get the weather for a given city",
      schema: z.object({
        city: z.string().describe("The city to get the weather for"),
      }),
    }
  );

  const agent = createAgent({
    model: "azure_openai:gpt-5.5",
    tools: [getWeather],
  });

  console.log(
    await agent.invoke({
      messages: [{ role: "user", content: "What's the weather in San Francisco?" }],
    })
  );
  ```

  ```ts AWS Bedrock theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  // First install: npm install langchain zod @langchain/aws
  import { createAgent, tool } from "langchain";
  import * as z from "zod";

  const getWeather = tool(
    (input) => `It's always sunny in ${input.city}!`,
    {
      name: "get_weather",
      description: "Get the weather for a given city",
      schema: z.object({
        city: z.string().describe("The city to get the weather for"),
      }),
    }
  );

  const agent = createAgent({
    model: "bedrock:gpt-5.5",
    tools: [getWeather],
  });

  console.log(
    await agent.invoke({
      messages: [{ role: "user", content: "What's the weather in San Francisco?" }],
    })
  );
  ```
</CodeGroup>

See the [Installation instructions](/oss/javascript/langchain/install) and [Quickstart guide](/oss/javascript/langchain/quickstart) to get started building your own agents and applications with LangChain.

<Tip>
  Use [LangSmith](/langsmith/observability) to trace requests, debug agent behavior, and evaluate outputs. Set `LANGSMITH_TRACING=true` and your API key to get started.
</Tip>

## <Icon icon="star" /> Core benefits

<Columns>
  <Card title="Standard model interface" icon="refresh" href="/oss/javascript/langchain/models">
    Different providers have unique APIs for interacting with models, including the format of responses. LangChain standardizes how you interact with models so that you can seamlessly swap providers and avoid lock-in.
  </Card>

  <Card title="Highly configurable harness" icon="wand" href="/oss/javascript/langchain/agents">
    `create_agent` is a minimal harness: model, tools, prompt, loop. Extend it with middleware: each piece handles one concern and composes freely. Build exactly the agent your use case needs, nothing more.
  </Card>

  <Card title="Built on top of LangGraph" icon="https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/langgraph-icon.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=b997e1a7487d507a36556eedbfd99f81" href="/oss/javascript/langgraph/overview">
    LangChain's agents are built on top of LangGraph. This allows us to take advantage of LangGraph's durable execution, human-in-the-loop support, persistence, and more.
  </Card>

  <Card title="Debug with LangSmith" icon="https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/observability-icon-dark.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=ccbc183bca2a5e4ca78d30149e3836cc" href="/langsmith/observability">
    Gain deep visibility into complex agent behavior with visualization tools that trace execution paths, capture state transitions, and provide detailed runtime metrics.
  </Card>
</Columns>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/overview.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Philosophy
Source: https://docs.langchain.com/oss/javascript/langchain/philosophy

LangChain exists to be the easiest place to start building with LLMs, while also being flexible and production-ready.

LangChain is driven by a few core beliefs:

* Large Language Models (LLMs) are great, powerful new technology.
* LLMs are even better when you combine them with external sources of data.
* LLMs will transform what the applications of the future look like. Specifically, the applications of the future will look more and more agentic.
* It is still very early on in that transformation.
* While it's easy to build a prototype of those agentic applications, it's still really hard to build agents that are reliable enough to put into production.

Today developers can choose how they build agents: use [LangChain](/oss/javascript/langchain/overview) for maximum flexibility and control, or [Deep Agents](/oss/javascript/langchain/overview) which allows for similar flexibility and control but comes with opinionated built-in planning, filesystem tools, subagents, and context management. Both are built on [LangGraph](/oss/javascript/langgraph/overview).

With LangChain, we have two core focuses:

<Steps>
  <Step title="We want to enable developers to build with the best models.">
    Different providers expose different APIs, with different model parameters and different message formats.
    Standardizing these model inputs and outputs is a core focus, making it easy for developer to easily change to the most recent state-of-the-art model, avoiding lock-in.
  </Step>

  <Step title="We want to make it easy to use models to orchestrate more complex flows that interact with other data and computation.">
    Models should be used for more than just *text generation* - they should also be used to orchestrate more complex flows that interact with other data. LangChain makes it easy to define [tools](/oss/javascript/langchain/tools) that LLMs can use dynamically, as well as help with parsing of and access to unstructured data.
  </Step>
</Steps>

## History

Given the constant rate of change in the field, LangChain has also evolved over time. Below is a brief timeline of how LangChain has changed over the years, evolving alongside what it means to build with LLMs:

<Update label="2022-10-24" description="v0.0.1">
  A month before ChatGPT, **LangChain was launched as a Python package**. It consisted of two main components:

  * LLM abstractions
  * "Chains", or predetermined steps of computation to run, for common use cases. For example - RAG: run a retrieval step, then run a generation step.

  The name LangChain comes from "Language" (like Language models) and "Chains".
</Update>

<Update label="2022-12">
  The first general purpose agents were added to LangChain.

  These general purpose agents were based on the [ReAct paper](https://arxiv.org/abs/2210.03629) (ReAct standing for Reasoning and Acting). They used LLMs to generate JSON that represented tool calls, and then parsed that JSON to determine what tools to call.
</Update>

<Update label="2023-01">
  OpenAI releases a 'Chat Completion' API.

  Previously, models took in strings and returned a string. In the ChatCompletions API, they evolved to take in a list of messages and return a message. Other model providers followed suit, and LangChain updated to work with lists of messages.
</Update>

<Update label="2023-01">
  LangChain releases a JavaScript version.

  LLMs and agents will change how applications are built and JavaScript is the language of application developers.
</Update>

<Update label="2023-02">
  **LangChain Inc. was formed as a company** around the open source LangChain project.

  The main goal was to "make intelligent agents ubiquitous". The team recognized that while LangChain was a key part (LangChain made it simple to get started with LLMs), there was also a need for other components.
</Update>

<Update label="2023-03">
  OpenAI releases 'function calling' in their API.

  This allowed the API to explicitly generate payloads that represented tool calls. Other model providers followed suit, and LangChain was updated to use this as the preferred method for tool calling (rather than parsing JSON).
</Update>

<Update label="2023-06">
  **LangSmith is released** as closed source platform by LangChain Inc., providing observability and evals.

  The main issue with building agents is getting them to be reliable, and LangSmith, which provides observability and evals, was built to solve that need. LangChain was updated to integrate seamlessly with LangSmith.
</Update>

<Update label="2024-01" description="v0.1.0">
  **LangChain releases 0.1.0**, its first non-0.0.x.

  The industry matured from prototypes to production, and as such, LangChain increased its focus on stability.
</Update>

<Update label="2024-02">
  **LangGraph is released** as an open-source library.

  The original LangChain had two focuses: LLM abstractions, and high-level interfaces for getting started with common applications; however, it was missing a low-level orchestration layer that allowed developers to control the exact flow of their agent. Enter: LangGraph.

  When building LangGraph, we learned from lessons when building LangChain and added functionality we discovered was needed: streaming, durable execution, short-term memory, human-in-the-loop, and more.
</Update>

<Update label="2024-06">
  **LangChain has over 700 integrations.**

  Integrations were split out of the core LangChain package, and either moved into their own standalone packages (for the core integrations) or `@langchain/community`.
</Update>

<Update label="2024-10">
  LangGraph becomes the preferred way to build any AI application that is more than a single LLM call.

  As developers tried to improve the reliability of their applications, they needed more control than the high-level interfaces provided. LangGraph provided that low-level flexibility. Most chains and agents were marked as deprecated in LangChain with guides on how to migrate them to LangGraph. There is still one high-level abstraction created in LangGraph: an agent abstraction. It is built on top of low-level LangGraph and has the same interface as the ReAct agents from LangChain.
</Update>

<Update label="2025-04">
  Model APIs become more multimodal.

  Models started to accept files, images, videos, and more. We updated the `@langchain/core` message format accordingly to allow developers to specify these multimodal inputs in a standard way.
</Update>

<Update label="2025-10-20" description="v1.0.0">
  **LangChain releases 1.0** with two major changes:

  1. Complete revamp of all chains and agents in `langchain`. All chains and agents are now replaced with only one high level abstraction: an agent abstraction built on top of LangGraph. This was the high-level abstraction that was originally created in LangGraph, but just moved to LangChain.

     For users still using old LangChain chains/agents who do NOT want to upgrade (note: we recommend you do), you can continue using old LangChain by installing the `@langchain/classic` package.

  2. A standard message content format: Model APIs evolved from returning messages with a simple content string to more complex output types - reasoning blocks, citations, server-side tool calls, etc. LangChain evolved its message formats to standardize these across providers.
</Update>

<Update label="2026-03-15" description="v0.5.3">
  **Deep Agents is released** as an open-source agent harness built on LangGraph.

  While LangChain provides flexible building blocks for custom agent architectures, [Deep Agents](/oss/javascript/langchain/overview) offers a batteries-included option for complex, long-running tasks like research and coding. It adds built-in planning tools, a virtual filesystem with pluggable backends (in-memory, disk, LangGraph store, sandboxes), and subagent spawning for context isolation. Use Deep Agents for more autonomous agents with predefined tools; use LangChain for full control over your agent architecture.
</Update>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/philosophy.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
