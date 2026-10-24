# Run a local server
Source: https://docs.langchain.com/oss/javascript/langgraph/local-server

This guide shows you how to run a LangGraph application locally.

## Prerequisites

Before you begin, ensure you have the following:

* An API key for [LangSmith](https://smith.langchain.com/settings) - free to sign up

## 1. Install the LangGraph CLI

```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
npm install --save-dev @langchain/langgraph-cli
```

## 2. Create a LangGraph app

Create a new app from the [`new-langgraph-project-js` template](https://github.com/langchain-ai/new-langgraphjs-project). This template demonstrates a single-node application you can extend with your own logic.

```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
npm create langgraph
```

<Accordion title="Adding LangGraph to an existing project">
  If you have an existing project with LangGraph agents, you can automatically generate a `langgraph.json` configuration file using the `config` command:

  ```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  npm create langgraph config
  ```

  This command scans your project for LangGraph agents (such as `createAgent()`, `StateGraph.compile()`, or `workflow.compile()` patterns) and generates a configuration file with all exported agents.

  Example output:

  ```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  {
    "node_version": "24",
    "graphs": {
      "agent": "./src/agent.ts:agent",
      "searchAgent": "./src/search.ts:searchAgent"
    },
    "env": ".env"
  }
  ```

  <Tip>
    Only **exported** agents are included in the configuration. If an agent is not exported, the command will warn you so you can add the `export` keyword.
  </Tip>
</Accordion>

## 3. Install dependencies

In the root of your new LangGraph app, install the dependencies in `edit` mode so your local changes are used by the server:

```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
cd path/to/your/app
npm install
```

## 4. Create a `.env` file

You will find a `.env.example` in the root of your new LangGraph app. Create a `.env` file in the root of your new LangGraph app and copy the contents of the `.env.example` file into it, filling in the necessary API keys:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
LANGSMITH_API_KEY=lsv2...
```

## 5. Launch Agent server

Start the LangGraph API server locally:

```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
npx @langchain/langgraph-cli dev
```

Sample output:

```
INFO:langgraph_api.cli:

        Welcome to

╦  ┌─┐┌┐┌┌─┐╔═╗┬─┐┌─┐┌─┐┬ ┬
║  ├─┤││││ ┬║ ╦├┬┘├─┤├─┘├─┤
╩═╝┴ ┴┘└┘└─┘╚═╝┴└─┴ ┴┴  ┴ ┴

- 🚀 API: http://127.0.0.1:2024
- 🎨 Studio UI: https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024
- 📚 API Docs: http://127.0.0.1:2024/docs

This in-memory server is designed for development and testing.
For production use, please use LangSmith Deployment.
```

The `langgraph dev` command starts Agent Server in an in-memory mode. This mode is suitable for development and testing purposes. For production use, deploy Agent Server with access to a persistent storage backend. For more information, see the [Platform setup overview](/langsmith/platform-setup).

## 6. Test your application in Studio

[Studio](/langsmith/studio) is a specialized UI that you can connect to LangGraph API server to visualize, interact with, and debug your application locally. Test your graph in Studio by visiting the URL provided in the output of the `langgraph dev` command:

```
>    - LangGraph Studio Web UI: https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024
```

For an Agent Server running on a custom host/port, update the `baseUrl` query parameter in the URL. For example, if your server is running on `http://myhost:3000`:

```
https://smith.langchain.com/studio/?baseUrl=http://myhost:3000
```

<Accordion title="Safari compatibility">
  Use the `--tunnel` flag with your command to create a secure tunnel, as Safari has limitations when connecting to localhost servers:

  ```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  langgraph dev --tunnel
  ```
</Accordion>

## 7. Test the API

<Tabs>
  <Tab title="Javascript SDK">
    1. Install the LangGraph JS SDK:
       ```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
       npm install @langchain/langgraph-sdk
       ```
    2. Send a message to the assistant (threadless run):

    ```js theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { Client } from "@langchain/langgraph-sdk";

    // only set the apiUrl if you changed the default port when calling langgraph dev
    const client = new Client({ apiUrl: "http://localhost:2024"});

    const streamResponse = client.runs.stream(
      null, // Threadless run
      "agent", // Assistant ID
      {
        input: {
          "messages": [
            { "role": "user", "content": "What is LangGraph?"}
          ]
        },
        streamMode: "messages-tuple",
      }
    );

    for await (const chunk of streamResponse) {
      console.log(`Receiving new event of type: ${chunk.event}...`);
      console.log(JSON.stringify(chunk.data));
      console.log("\n\n");
    }
    ```
  </Tab>

  <Tab title="Rest API">
    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    curl -s --request POST \
        --url "http://localhost:2024/runs/stream" \
        --header 'Content-Type: application/json' \
        --data "{
            \"assistant_id\": \"agent\",
            \"input\": {
                \"messages\": [
                    {
                        \"role\": \"human\",
                        \"content\": \"What is LangGraph?\"
                    }
                ]
            },
            \"stream_mode\": \"messages-tuple\"
        }"
    ```
  </Tab>
</Tabs>

## Next steps

Now that you have a LangGraph app running locally, take your journey further by exploring deployment and advanced features:

* [Deployment quickstart](/langsmith/deployment-quickstart): Deploy your LangGraph app using LangSmith.

* [LangSmith](/langsmith/observability): Learn about foundational LangSmith concepts.

* [SDK Reference](https://reference.langchain.com/javascript/modules/_langchain_langgraph-sdk.html): Explore the SDK API Reference.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langgraph/local-server.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# LangSmith Observability
Source: https://docs.langchain.com/oss/javascript/langgraph/observability

Traces are a series of steps that your application takes to go from input to output. Each of these individual steps is represented by a run. You can use [LangSmith](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=oss-langgraph-observability) to visualize these execution steps. To use it, [enable tracing for your application](/langsmith/trace-with-langgraph). This enables you to do the following:

* [Debug a locally running application](/langsmith/observability-studio#debug-langsmith-traces).
* [Evaluate the application performance](/oss/javascript/langchain/test/evals).
* [Monitor the application](/langsmith/dashboards).

## Prerequisites

Before you begin, ensure you have the following:

* **A LangSmith account**: Sign up (for free) or log in at [smith.langchain.com](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=oss-langgraph-observability).
* **A LangSmith API key**: Follow the [Create an API key](/langsmith/create-account-api-key) guide.

## Enable tracing

To enable tracing for your application, set the following environment variables:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
export LANGSMITH_TRACING=true
export LANGSMITH_API_KEY=<your-api-key>
```

By default, the trace will be logged to the project with the name `default`. To configure a custom project name, see [Log to a project](#log-to-a-project).

For more information, see [Trace with LangGraph](/langsmith/trace-with-langgraph).

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
  config: {
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

## Use anonymizers to prevent logging of sensitive data in traces

You may want to mask sensitive data to prevent it from being logged to LangSmith. You can create [anonymizers](/langsmith/mask-inputs-outputs#rule-based-masking-of-inputs-and-outputs) and apply them to
your graph using configuration. This example will redact anything matching the Social Security Number format XXX-XX-XXXX from traces sent to LangSmith.

```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { StateGraph } from "@langchain/langgraph";
import { LangChainTracer } from "@langchain/core/tracers/tracer_langchain";
import { StateAnnotation } from "./state.js";
import { createAnonymizer } from "langsmith/anonymizer"
import { Client } from "langsmith"

const anonymizer = createAnonymizer([
  // Matches SSNs
  { pattern: /\b\d{3}-?\d{2}-?\d{4}\b/, replace: "<ssn>" }
])

const langsmithClient = new Client({ anonymizer })
const tracer = new LangChainTracer({
  client: langsmithClient,
});

export const graph = new StateGraph(StateAnnotation)
  .compile()
  .withConfig({ callbacks: [tracer] });
```

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langgraph/observability.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# LangGraph overview
Source: https://docs.langchain.com/oss/javascript/langgraph/overview

Gain control with LangGraph to design agents that reliably handle complex tasks

Trusted by companies shaping the future of agents-- including Klarna, Uber, J.P. Morgan, and more-- LangGraph is a low-level orchestration framework and runtime for building, managing, and deploying long-running, stateful agents.

LangGraph is very low-level, and focused entirely on agent **orchestration**. Before using LangGraph, we recommend you familiarize yourself with some of the components used to build agents, starting with [models](/oss/javascript/langchain/models) and [tools](/oss/javascript/langchain/tools).

We will commonly use [LangChain](/oss/javascript/langchain/overview) components throughout the documentation to integrate models and tools, but you don't need to use LangChain to use LangGraph. If you are just getting started with agents or want a higher-level abstraction, we recommend you use LangChain's [agents](/oss/javascript/langchain/agents) that provide prebuilt architectures for common LLM and tool-calling loops.

LangGraph is focused on the underlying capabilities important for agent orchestration: durable execution, streaming, human-in-the-loop, and more.

<Expandable title="how LangChain products fit together">
  * [Deep Agents](/oss/javascript/deepagents/overview) is an [agent harness](/oss/javascript/concepts/products#agent-harnesses-like-the-deep-agents-sdk): planning, subagents, filesystem tools, and context management on top of LangGraph.
  * [LangChain](/oss/javascript/langchain/overview) is the agent framework: abstractions and integrations for models, tools, and agent loops.
  * [LangGraph](/oss/javascript/langgraph/overview) is the orchestration runtime: durable execution, streaming, human-in-the-loop, and persistence.
  * [LangSmith](/langsmith/observability) is the platform for tracing, evaluation, prompts, and deployment across frameworks.
  * [LangSmith Engine](/langsmith/engine) detects issues in your LangGraph agent traces and proposes fixes. You can open a pull request with the proposed fix directly from the Engine tab.
  * [LangSmith Fleet](/langsmith/fleet/index) is the no-code agent builder for templates, integrations, and routine automation.

  Read [Frameworks, runtimes, and harnesses](/oss/javascript/concepts/products) for a comparison of the open source stack.
</Expandable>

## <Icon icon="download" /> Install

<CodeGroup>
  ```bash npm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  npm install @langchain/langgraph @langchain/core
  ```

  ```bash pnpm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pnpm add @langchain/langgraph @langchain/core
  ```

  ```bash yarn theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  yarn add @langchain/langgraph @langchain/core
  ```

  ```bash bun theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  bun add @langchain/langgraph @langchain/core
  ```
</CodeGroup>

Then, create a simple hello world example:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { StateSchema, MessagesValue, type GraphNode, StateGraph, START, END } from "@langchain/langgraph";

const State = new StateSchema({
  messages: MessagesValue,
});

const mockLlm: GraphNode<typeof State> = (state) => {
  return { messages: [{ role: "ai", content: "hello world" }] };
};

const graph = new StateGraph(State)
  .addNode("mock_llm", mockLlm)
  .addEdge(START, "mock_llm")
  .addEdge("mock_llm", END)
  .compile();

await graph.invoke({ messages: [{ role: "user", content: "hi!" }] });
```

<Tip>
  Use [LangSmith](/langsmith/observability) to trace requests, debug agent behavior, and evaluate outputs. Set `LANGSMITH_TRACING=true` and your API key to get started. Follow the [tracing quickstart](/langsmith/trace-with-langchain) to get set up.  We recommend you also set up [LangSmith Engine](/langsmith/engine) which monitors your traces, detects issues, and proposes fixes.
</Tip>

## Core benefits

LangGraph provides low-level supporting infrastructure for *any* long-running, stateful workflow or agent. LangGraph does not abstract prompts or architecture, and provides the following central benefits:

* [Persistence](/oss/javascript/langgraph/persistence): Build agents that persist through failures and can run for extended periods, resuming from where they left off.
* [Human-in-the-loop](/oss/javascript/langgraph/interrupts): Incorporate human oversight by inspecting and modifying agent state at any point.
* [Comprehensive memory](/oss/javascript/concepts/memory): Create stateful agents with both short-term working memory for ongoing reasoning and long-term memory across sessions.
* [Debugging with LangSmith](/langsmith/observability): Gain deep visibility into complex agent behavior with visualization tools that trace execution paths, capture state transitions, and provide detailed runtime metrics.
* [Production-ready deployment](/langsmith/deployment): Deploy sophisticated agent systems confidently with scalable infrastructure designed to handle the unique challenges of stateful, long-running workflows.

## LangGraph ecosystem

While LangGraph can be used standalone, it also integrates seamlessly with any LangChain product, giving developers a full suite of tools for building agents. To improve your LLM application development, pair LangGraph with:

<Columns>
  <Card title="LangSmith Observability" icon="https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/observability-icon-dark.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=ccbc183bca2a5e4ca78d30149e3836cc" href="/langsmith/observability">
    Trace requests, evaluate outputs, and monitor deployments in one place. Prototype locally with LangGraph, then move to production with integrated observability and evaluation to build more reliable agent systems.
  </Card>

  <Card title="LangSmith Deployment" icon="https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/deployment-icon-dark.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=024e3712d388bfa55f4f160cc9d6a85b" href="/langsmith/deployment">
    Deploy and scale agents effortlessly with a purpose-built deployment platform for long running, stateful workflows. Discover, reuse, configure, and share agents across teams — and iterate quickly with visual prototyping in Studio.
  </Card>

  <Card title="LangChain" icon="https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/langchain-icon.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=663b30f85baf99ad708b97e05da2a5a4" href="/oss/javascript/langchain/overview">
    Provides integrations and composable components to streamline LLM application development. Contains agent abstractions built on top of LangGraph.
  </Card>
</Columns>

## Acknowledgements

LangGraph is inspired by [Pregel](https://research.google/pubs/pub37252/) and [Apache Beam](https://beam.apache.org/). The public interface draws inspiration from [NetworkX](https://networkx.org/documentation/latest/). LangGraph is built by LangChain Inc, the creators of LangChain, but can be used without LangChain.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langgraph/overview.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Persistence
Source: https://docs.langchain.com/oss/javascript/langgraph/persistence

LangGraph's persistence layer gives agents short-term memory through checkpointers and long-term memory through stores.

<a />

<a />

<a />

<a />

<a />

<a />

Persistence lets LangGraph applications keep useful information beyond a single graph run. It matters when an agent needs to continue a conversation, resume after an interruption, recover from a failure, or remember information across interactions.

LangGraph provides two complementary persistence systems:

* **[Checkpointers](/oss/javascript/langgraph/checkpointers)** persist a thread's graph state as checkpoints. Use them for short-term, thread-scoped memory, including conversation continuity, human-in-the-loop workflows, time travel, and fault tolerance.
* **[Stores](/oss/javascript/langgraph/stores)** persist application-defined data outside the graph state. Use them for long-term, cross-thread memory, including user preferences, facts, and shared knowledge.

Most applications can use both: a [checkpointer](/oss/javascript/langgraph/checkpointers) tracks the current thread, and a [store](/oss/javascript/langgraph/stores) tracks durable information across threads.

## Quickstart

Compile your graph with a checkpointer, a store, or both:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { MemorySaver, MemoryStore } from "@langchain/langgraph";

const checkpointer = new MemorySaver();
const store = new MemoryStore();

const graph = builder.compile({ checkpointer, store });

const result = await graph.invoke(
  { messages: [{ role: "user", content: "Hi, my name is Bob." }] },
  { configurable: { thread_id: "thread-1" } }
);
```

<Info>
  **Agent Server handles persistence automatically**
  When using the [Agent Server](/langsmith/agent-server), you do not need to implement or configure checkpointers or stores manually. The server handles persistence infrastructure behind the scenes.
</Info>

## Checkpointer vs. store

|                | Checkpointer                                                                 | Store                                               |
| -------------- | ---------------------------------------------------------------------------- | --------------------------------------------------- |
| Persists       | Graph state snapshots                                                        | Application-defined key-value data                  |
| Scope          | A single thread                                                              | Across threads                                      |
| Memory type    | Short-term, thread-scoped memory                                             | Long-term, cross-thread memory                      |
| Use for        | Conversation continuity, human-in-the-loop, time travel, and fault tolerance | User preferences, facts, and shared knowledge       |
| Access pattern | Pass a `thread_id` in graph config                                           | Read and write items from nodes or application code |
| Full guide     | [Checkpointers](/oss/javascript/langgraph/checkpointers)                     | [Stores](/oss/javascript/langgraph/stores)          |

## Next steps

* [Use checkpointers](/oss/javascript/langgraph/checkpointers) to persist and inspect thread state.
* [Use stores](/oss/javascript/langgraph/stores) to persist durable data across threads.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langgraph/persistence.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# LangGraph runtime
Source: https://docs.langchain.com/oss/javascript/langgraph/pregel

[`Pregel`](https://reference.langchain.com/javascript/langchain-langgraph/index/Pregel) implements LangGraph's runtime, managing the execution of LangGraph applications.

Compiling a [StateGraph](https://reference.langchain.com/javascript/langchain-langgraph/index/StateGraph) or creating an [entrypoint](https://reference.langchain.com/javascript/langchain-langgraph/index/entrypoint) produces a [`Pregel`](https://reference.langchain.com/javascript/langchain-langgraph/index/Pregel) instance that can be invoked with input.

This guide explains the runtime at a high level and provides instructions for directly implementing applications with Pregel.

> **Note:** The [`Pregel`](https://reference.langchain.com/javascript/langchain-langgraph/index/Pregel) runtime is named after [Google's Pregel algorithm](https://research.google/pubs/pub37252/), which describes an efficient method for large-scale parallel computation using graphs.

## Overview

In LangGraph, Pregel combines [**actors**](https://en.wikipedia.org/wiki/Actor_model) and **channels** into a single application. **Actors** read data from channels and write data to channels. Pregel organizes the execution of the application into multiple steps, following the **Pregel Algorithm**/**Bulk Synchronous Parallel** model.

Each step consists of three phases:

* **Plan**: Determine which **actors** to execute in this step. For example, in the first step, select the **actors** that subscribe to the special **input** channels; in subsequent steps, select the **actors** that subscribe to channels updated in the previous step.
* **Execution**: Execute all selected **actors** in parallel, until all complete, or one fails, or a timeout is reached. During this phase, channel updates are invisible to actors until the next step.
* **Update**: Update the channels with the values written by the **actors** in this step.

Repeat until no **actors** are selected for execution, or a maximum number of steps is reached.

## Actors

An **actor** is a `PregelNode`. It subscribes to channels, reads data from them, and writes data to them. It can be thought of as an **actor** in the Pregel algorithm. `PregelNodes` implement LangChain's Runnable interface.

## Channels

Channels are used to communicate between actors (PregelNodes). Each channel has a value type, an update type, and an update function—which takes a sequence of updates and modifies the stored value. Channels can be used to send data from one chain to another, or to send data from a chain to itself in a future step.

### LastValue

[`LastValue`](https://reference.langchain.com/javascript/classes/_langchain_langgraph.channels.LastValue.html) is the default channel type. It stores the last value written to it, overwriting any previous value. Use it for input and output values, or for passing data from one step to the next.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { LastValue } from "@langchain/langgraph/channels";

const channel = new LastValue<number>();
```

### Topic

[`Topic`](https://reference.langchain.com/javascript/langchain-langgraph/channels/Topic) is a configurable PubSub channel useful for sending multiple values between actors or accumulating output across steps. It can be configured to deduplicate values or to accumulate all values written during a run.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { Topic } from "@langchain/langgraph/channels";

// Accumulate all values written across steps
const channel = new Topic<string>({ accumulate: true });
```

### BinaryOperatorAggregate

[`BinaryOperatorAggregate`](https://reference.langchain.com/javascript/langchain-langgraph/channels/BinaryOperatorAggregate) stores a persistent value that is updated by applying a binary operator to the current value and each new update. Use it to compute running aggregates across steps.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { BinaryOperatorAggregate } from "@langchain/langgraph/channels";

// Running total: each write adds to the current value
const total = new BinaryOperatorAggregate<number>({ operator: (a, b) => a + b });
```

## Examples

While most users will interact with Pregel through the [StateGraph](https://reference.langchain.com/javascript/langchain-langgraph/index/StateGraph) API or the [entrypoint](https://reference.langchain.com/javascript/langchain-langgraph/index/entrypoint) decorator, it is possible to interact with Pregel directly.

Below are a few different examples to give you a sense of the Pregel API.

<Tabs>
  <Tab title="Single node">
    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { EphemeralValue } from "@langchain/langgraph/channels";
    import { Pregel, NodeBuilder } from "@langchain/langgraph/pregel";

    const node1 = new NodeBuilder()
      .subscribeOnly("a")
      .do((x: string) => x + x)
      .writeTo("b");

    const app = new Pregel({
      nodes: { node1 },
      channels: {
        a: new EphemeralValue<string>(),
        b: new EphemeralValue<string>(),
      },
      inputChannels: ["a"],
      outputChannels: ["b"],
    });

    await app.invoke({ a: "foo" });
    ```

    ```console theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    { b: 'foofoo' }
    ```
  </Tab>

  <Tab title="Multiple nodes">
    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { LastValue, EphemeralValue } from "@langchain/langgraph/channels";
    import { Pregel, NodeBuilder } from "@langchain/langgraph/pregel";

    const node1 = new NodeBuilder()
      .subscribeOnly("a")
      .do((x: string) => x + x)
      .writeTo("b");

    const node2 = new NodeBuilder()
      .subscribeOnly("b")
      .do((x: string) => x + x)
      .writeTo("c");

    const app = new Pregel({
      nodes: { node1, node2 },
      channels: {
        a: new EphemeralValue<string>(),
        b: new LastValue<string>(),
        c: new EphemeralValue<string>(),
      },
      inputChannels: ["a"],
      outputChannels: ["b", "c"],
    });

    await app.invoke({ a: "foo" });
    ```

    ```console theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    { b: 'foofoo', c: 'foofoofoofoo' }
    ```
  </Tab>

  <Tab title="Topic">
    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { EphemeralValue, Topic } from "@langchain/langgraph/channels";
    import { Pregel, NodeBuilder } from "@langchain/langgraph/pregel";

    const node1 = new NodeBuilder()
      .subscribeOnly("a")
      .do((x: string) => x + x)
      .writeTo("b", "c");

    const node2 = new NodeBuilder()
      .subscribeTo("b")
      .do((x: { b: string }) => x.b + x.b)
      .writeTo("c");

    const app = new Pregel({
      nodes: { node1, node2 },
      channels: {
        a: new EphemeralValue<string>(),
        b: new EphemeralValue<string>(),
        c: new Topic<string>({ accumulate: true }),
      },
      inputChannels: ["a"],
      outputChannels: ["c"],
    });

    await app.invoke({ a: "foo" });
    ```

    ```console theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    { c: ['foofoo', 'foofoofoofoo'] }
    ```
  </Tab>

  <Tab title="BinaryOperatorAggregate">
    This example demonstrates how to use the [`BinaryOperatorAggregate`](https://reference.langchain.com/javascript/langchain-langgraph/channels/BinaryOperatorAggregate) channel to implement a reducer.

    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { EphemeralValue, BinaryOperatorAggregate } from "@langchain/langgraph/channels";
    import { Pregel, NodeBuilder } from "@langchain/langgraph/pregel";

    const node1 = new NodeBuilder()
      .subscribeOnly("a")
      .do((x: string) => x + x)
      .writeTo("b", "c");

    const node2 = new NodeBuilder()
      .subscribeOnly("b")
      .do((x: string) => x + x)
      .writeTo("c");

    const reducer = (current: string, update: string) => {
      if (current) {
        return current + " | " + update;
      } else {
        return update;
      }
    };

    const app = new Pregel({
      nodes: { node1, node2 },
      channels: {
        a: new EphemeralValue<string>(),
        b: new EphemeralValue<string>(),
        c: new BinaryOperatorAggregate<string>({ operator: reducer }),
      },
      inputChannels: ["a"],
      outputChannels: ["c"],
    });

    await app.invoke({ a: "foo" });
    ```
  </Tab>

  <Tab title="Cycle">
    This example demonstrates how to introduce a cycle in the graph, by having
    a chain write to a channel it subscribes to. Execution will continue
    until a `null` value is written to the channel.

    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { EphemeralValue } from "@langchain/langgraph/channels";
    import { Pregel, NodeBuilder, ChannelWriteEntry } from "@langchain/langgraph/pregel";

    const exampleNode = new NodeBuilder()
      .subscribeOnly("value")
      .do((x: string) => x.length < 10 ? x + x : null)
      .writeTo(new ChannelWriteEntry("value", { skipNone: true }));

    const app = new Pregel({
      nodes: { exampleNode },
      channels: {
        value: new EphemeralValue<string>(),
      },
      inputChannels: ["value"],
      outputChannels: ["value"],
    });

    await app.invoke({ value: "a" });
    ```

    ```console theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    { value: 'aaaaaaaaaaaaaaaa' }
    ```
  </Tab>
</Tabs>

## High-level API

LangGraph provides two high-level APIs for creating a Pregel application: the [StateGraph (Graph API)](/oss/javascript/langgraph/graph-api) and the [Functional API](/oss/javascript/langgraph/functional-api).

<Tabs>
  <Tab title="StateGraph (Graph API)">
    The [StateGraph (Graph API)](https://reference.langchain.com/javascript/langchain-langgraph/index/StateGraph) is a higher-level abstraction that simplifies the creation of Pregel applications. It allows you to define a graph of nodes and edges. When you compile the graph, the StateGraph API automatically creates the Pregel application for you.

    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { START, StateGraph } from "@langchain/langgraph";

    interface Essay {
      topic: string;
      content?: string;
      score?: number;
    }

    const writeEssay = (essay: Essay) => {
      return {
        content: `Essay about ${essay.topic}`,
      };
    };

    const scoreEssay = (essay: Essay) => {
      return {
        score: 10
      };
    };

    const builder = new StateGraph<Essay>({
      channels: {
        topic: null,
        content: null,
        score: null,
      }
    })
      .addNode("writeEssay", writeEssay)
      .addNode("scoreEssay", scoreEssay)
      .addEdge(START, "writeEssay")
      .addEdge("writeEssay", "scoreEssay");

    // Compile the graph.
    // This will return a Pregel instance.
    const graph = builder.compile();
    ```

    The compiled Pregel instance will be associated with a list of nodes and channels. You can inspect the nodes and channels by printing them.

    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    console.log(graph.nodes);
    ```

    You will see something like this:

    ```console theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    {
      __start__: PregelNode { ... },
      writeEssay: PregelNode { ... },
      scoreEssay: PregelNode { ... }
    }
    ```

    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    console.log(graph.channels);
    ```

    You should see something like this

    ```console theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    {
      topic: LastValue { ... },
      content: LastValue { ... },
      score: LastValue { ... },
      __start__: EphemeralValue { ... },
      writeEssay: EphemeralValue { ... },
      scoreEssay: EphemeralValue { ... },
      'branch:__start__:__self__:writeEssay': EphemeralValue { ... },
      'branch:__start__:__self__:scoreEssay': EphemeralValue { ... },
      'branch:writeEssay:__self__:writeEssay': EphemeralValue { ... },
      'branch:writeEssay:__self__:scoreEssay': EphemeralValue { ... },
      'branch:scoreEssay:__self__:writeEssay': EphemeralValue { ... },
      'branch:scoreEssay:__self__:scoreEssay': EphemeralValue { ... },
      'start:writeEssay': EphemeralValue { ... }
    }
    ```
  </Tab>

  <Tab title="Functional API">
    In the [Functional API](/oss/javascript/langgraph/functional-api), you can use an [`entrypoint`](https://reference.langchain.com/javascript/langchain-langgraph/index/entrypoint) to create a Pregel application. The `entrypoint` decorator allows you to define a function that takes input and returns output.

    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { MemorySaver } from "@langchain/langgraph";
    import { entrypoint } from "@langchain/langgraph/func";

    interface Essay {
      topic: string;
      content?: string;
      score?: number;
    }

    const checkpointer = new MemorySaver();

    const writeEssay = entrypoint(
      { checkpointer, name: "writeEssay" },
      async (essay: Essay) => {
        return {
          content: `Essay about ${essay.topic}`,
        };
      }
    );

    console.log("Nodes: ");
    console.log(writeEssay.nodes);
    console.log("Channels: ");
    console.log(writeEssay.channels);
    ```

    ```console theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    Nodes:
    { writeEssay: PregelNode { ... } }
    Channels:
    {
      __start__: EphemeralValue { ... },
      __end__: LastValue { ... },
      __previous__: LastValue { ... }
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
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langgraph/pregel.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
