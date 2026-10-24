# The above chain will be traced as a child run of the traceable function
@traceable(
    tags=["openai", "chat"],
    metadata={"foo": "bar"}
)
def invoke_runnnable(question, context):
    result = chain.invoke({"question": question, "context": context})
    return "The response is: " + result

invoke_runnnable("Can you summarize this morning's meetings?", "During this morning's meeting, we solved all world conflict.")
```

This will produce the following trace tree: <img alt="Trace tree python interop" />

## Interoperability between LangChain.JS and LangSmith SDK

### Tracing LangChain objects inside `traceable` (JS only)

Starting with `langchain@0.2.x`, LangChain objects are traced automatically when used inside `@traceable` functions, inheriting the client, tags, metadata and project name of the traceable function.

For older versions of LangChain below `0.2.x`, you will need to manually pass an instance `LangChainTracer` created from the tracing context found in `@traceable`.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { ChatOpenAI } from "@langchain/openai";
import { ChatPromptTemplate } from "@langchain/core/prompts";
import { StringOutputParser } from "@langchain/core/output_parsers";
import { getLangchainCallbacks } from "langsmith/langchain";

const prompt = ChatPromptTemplate.fromMessages([
  [
    "system",
    "You are a helpful assistant. Please respond to the user's request only based on the given context.",
  ],
  ["user", "Question: {question}\nContext: {context}"],
]);

const model = new ChatOpenAI({ modelName: "gpt-5.4-mini" });
const outputParser = new StringOutputParser();
const chain = prompt.pipe(model).pipe(outputParser);

const main = traceable(
  async (input: { question: string; context: string }) => {
    const callbacks = await getLangchainCallbacks();
    const response = await chain.invoke(input, { callbacks });
    return response;
  },
  { name: "main" }
);
```

### Tracing LangChain child runs via `traceable` / RunTree API (JS only)

<Note>
  We're working on improving the interoperability between `traceable` and LangChain. The following limitations are present when using combining LangChain with `traceable`:

  1. Mutating RunTree obtained from `getCurrentRunTree()` of the RunnableLambda context will result in a no-op.
  2. It's discouraged to traverse the RunTree obtained from RunnableLambda via `getCurrentRunTree()` as it may not contain all the RunTree nodes.
  3. Different child runs may have the same `execution_order` and `child_execution_order` value. Thus in extreme circumstances, some runs may end up in a different order, depending on the `start_time`.
</Note>

In some uses cases, you might want to run `traceable` functions as part of the RunnableSequence or trace child runs of LangChain run imperatively via the `RunTree` API. Starting with LangSmith 0.1.39 and @langchain/core 0.2.18, you can directly invoke `traceable`-wrapped functions within RunnableLambda.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { traceable } from "langsmith/traceable";
import { RunnableLambda } from "@langchain/core/runnables";
import { RunnableConfig } from "@langchain/core/runnables";

const tracedChild = traceable((input: string) => `Child Run: ${input}`, {
  name: "Child Run",
});

const parrot = new RunnableLambda({
  func: async (input: { text: string }, config?: RunnableConfig) => {
    return await tracedChild(input.text);
  },
});
```

<img alt="Trace Tree" />

Alternatively, you can convert LangChain's [`RunnableConfig`](https://reference.langchain.com/python/langchain-core/runnables/config/RunnableConfig) to a equivalent RunTree object by using `RunTree.fromRunnableConfig` or pass the [`RunnableConfig`](https://reference.langchain.com/python/langchain-core/runnables/config/RunnableConfig) as the first argument of `traceable`-wrapped function.

<CodeGroup>
  ```typescript Traceable theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { traceable } from "langsmith/traceable";
  import { RunnableLambda } from "@langchain/core/runnables";
  import { RunnableConfig } from "@langchain/core/runnables";

  const tracedChild = traceable((input: string) => `Child Run: ${input}`, {
    name: "Child Run",
  });

  const parrot = new RunnableLambda({
    func: async (input: { text: string }, config?: RunnableConfig) => {
      // Pass the config to existing traceable function
      await tracedChild(config, input.text);
      return input.text;
    },
  });
  ```

  ```typescript Run Tree theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { RunTree } from "langsmith/run_trees";
  import { RunnableLambda } from "@langchain/core/runnables";
  import { RunnableConfig } from "@langchain/core/runnables";

  const parrot = new RunnableLambda({
    func: async (input: { text: string }, config?: RunnableConfig) => {
      // create the RunTree from the RunnableConfig of the RunnableLambda
      const childRunTree = RunTree.fromRunnableConfig(config, {
        name: "Child Run",
      });

      childRunTree.inputs = { input: input.text };
      await childRunTree.postRun();

      childRunTree.outputs = { output: `Child Run: ${input.text}` };
      await childRunTree.patchRun();

      return input.text;
    },
  });
  ```
</CodeGroup>

If you prefer a video tutorial, check out the [Alternative Ways to Trace video](https://academy.langchain.com/pages/intro-to-langsmith-preview) from the Introduction to LangSmith Course.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-with-langchain.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Trace LangGraph applications
Source: https://docs.langchain.com/langsmith/trace-with-langgraph

LangSmith smoothly integrates with LangGraph (Python and JS) to help you trace agents, whether you're using LangChain modules or other SDKs.

## With LangChain

If you are using LangChain modules within LangGraph, you only need to set a few environment variables to enable tracing.

This guide will walk through a basic example. For more detailed information on configuration, see the [Trace With LangChain](/langsmith/trace-with-langchain) guide.

### 1. Installation

Install the LangGraph library and the OpenAI integration for Python and JS (we use the OpenAI integration for the code snippets below).

For a full list of packages available, see the [LangChain Python docs](https://docs.langchain.com/oss/python/integrations/providers/overview) and [LangChain JS docs](https://docs.langchain.com/oss/javascript/integrations/providers/overview).

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install langchain_openai langgraph
  ```

  ```bash yarn theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  yarn add @langchain/openai @langchain/langgraph
  ```

  ```bash npm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  npm install @langchain/openai @langchain/langgraph
  ```

  ```bash pnpm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pnpm add @langchain/openai @langchain/langgraph
  ```
</CodeGroup>

### 2. Configure your environment

```bash wrap theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
export LANGSMITH_TRACING=true
export LANGSMITH_API_KEY=<your-api-key>

# This example uses OpenAI, but you can use any LLM provider of choice
export OPENAI_API_KEY=<your-openai-api-key>

# For LangSmith API keys linked to multiple workspaces, set the LANGSMITH_WORKSPACE_ID environment variable to specify which workspace to use.
export LANGSMITH_WORKSPACE_ID=<your-workspace-id>
```

<Note>
  If your account is in a region other than US (the default), also set `LANGSMITH_ENDPOINT` to the API URL for your region. Without this, your API key won't be recognized and requests will fail to authenticate.

  <table>
    <thead>
      <tr>
        <th>Region</th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <td>GCP US</td>
      </tr>

      <tr>
        <td>GCP EU</td>
      </tr>

      <tr>
        <td>GCP APAC</td>
      </tr>

      <tr>
        <td>AWS US</td>
      </tr>
    </tbody>
  </table>

  For example, EU accounts: `export LANGSMITH_ENDPOINT="https://eu.api.smith.langchain.com"`.
</Note>

<Info>
  If you are using LangChain.js with LangSmith and are not in a serverless environment, we also recommend setting the following explicitly to reduce latency:

  `export LANGCHAIN_CALLBACKS_BACKGROUND=true`

  If you are in a serverless environment, we recommend setting the reverse to allow tracing to finish before your function ends:

  `export LANGCHAIN_CALLBACKS_BACKGROUND=false`

  See [this LangChain.js guide](https://js.langchain.com/docs/how_to/callbacks_serverless) for more information.
</Info>

### 3. Log a trace

Once you've set up your environment, you can call LangChain runnables as normal. LangSmith will infer the proper tracing config:

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from typing import Literal
  from langchain.messages import HumanMessage
  from langchain_openai import ChatOpenAI
  from langchain.tools import tool
  from langgraph.prebuilt import ToolNode
  from langgraph.graph import StateGraph, MessagesState

  @tool
  def search(query: str):
      """Call to surf the web."""
      if "sf" in query.lower() or "san francisco" in query.lower():
          return "It's 60 degrees and foggy."
      return "It's 90 degrees and sunny."

  tools = [search]
  tool_node = ToolNode(tools)

  model = ChatOpenAI(model="gpt-5.5", temperature=0).bind_tools(tools)

  def should_continue(state: MessagesState) -> Literal["tools", "__end__"]:
      messages = state['messages']
      last_message = messages[-1]
      if last_message.tool_calls:
          return "tools"
      return "__end__"

  def call_model(state: MessagesState):
      messages = state['messages']
      # Invoking `model` will automatically infer the correct tracing context
      response = model.invoke(messages)
      return {"messages": [response]}

  workflow = StateGraph(MessagesState)
  workflow.add_node("agent", call_model)
  workflow.add_node("tools", tool_node)
  workflow.add_edge("__start__", "agent")
  workflow.add_conditional_edges(
      "agent",
      should_continue,
  )
  workflow.add_edge("tools", 'agent')

  app = workflow.compile()

  final_state = app.invoke(
      {"messages": [HumanMessage(content="what is the weather in sf")]},
      config={"configurable": {"thread_id": 42}}
  )

  final_state["messages"][-1].content
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { HumanMessage, AIMessage } from "@langchain/core/messages";
  import { tool } from "@langchain/core/tools";
  import { z } from "zod";
  import { ChatOpenAI } from "@langchain/openai";
  import { StateGraph, StateGraphArgs } from "@langchain/langgraph";
  import { ToolNode } from "@langchain/langgraph/prebuilt";

  interface AgentState {
    messages: HumanMessage[];
  }

  const graphState: StateGraphArgs<AgentState>["channels"] = {
    messages: {
      reducer: (x: HumanMessage[], y: HumanMessage[]) => x.concat(y),
    },
  };

  const searchTool = tool(async ({ query }: { query: string }) => {
    if (query.toLowerCase().includes("sf") || query.toLowerCase().includes("san francisco")) {
      return "It's 60 degrees and foggy."
    }
    return "It's 90 degrees and sunny."
  }, {
    name: "search",
    description:
      "Call to surf the web.",
    schema: z.object({
      query: z.string().describe("The query to use in your search."),
    }),
  });

  const tools = [searchTool];
  const toolNode = new ToolNode<AgentState>(tools);

  const model = new ChatOpenAI({
    model: "gpt-5.5",
    temperature: 0,
  }).bindTools(tools);

  function shouldContinue(state: AgentState) {
    const messages = state.messages;
    const lastMessage = messages[messages.length - 1] as AIMessage;
    if (lastMessage.tool_calls?.length) {
      return "tools";
    }
    return "__end__";
  }

  async function callModel(state: AgentState) {
    const messages = state.messages;
    // Invoking `model` will automatically infer the correct tracing context
    const response = await model.invoke(messages);
    return { messages: [response] };
  }

  const workflow = new StateGraph<AgentState>({ channels: graphState })
    .addNode("agent", callModel)
    .addNode("tools", toolNode)
    .addEdge("__start__", "agent")
    .addConditionalEdges("agent", shouldContinue)
    .addEdge("tools", "agent");

  const app = workflow.compile();

  const finalState = await app.invoke(
    { messages: [new HumanMessage("what is the weather in sf")] },
    { configurable: { thread_id: "42" } }
  );

  finalState.messages[finalState.messages.length - 1].content;
  ```
</CodeGroup>

### Viewing the trace

**Details view**

Click on the trace, and toggle to the **Details** view on the top right. Your trace in LangSmith should [look like this](https://smith.langchain.com/public/79061a0f-c602-4012-b022-03fd46bce89e/r).

**Messages view**

The **Messages** view in the LangSmith UI shows a simplified conversation history between the user and the agent. This view pulls messages from the top-level trace (including the user’s initial request, tool calls, and the agent’s final response) and represents them in a chat-like format.

## Without LangChain

If you are using other SDKs or custom functions within LangGraph, you will need to [wrap or decorate them appropriately](/langsmith/annotate-code#use-%40traceable-%2F-traceable) (with the `@traceable` decorator in Python or the `traceable` function in JS, or something like e.g. `wrap_openai` for SDKs). If you do so, LangSmith will automatically nest traces from those wrapped methods.

Here's an example. You can also see this page for more information.

### 1. Installation

Install the LangGraph library and the OpenAI SDK for Python and JS (we use the OpenAI integration for the code snippets below).

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install openai langsmith langgraph
  ```

  ```bash yarn theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  yarn add openai langsmith @langchain/langgraph
  ```

  ```bash npm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  npm install openai langsmith @langchain/langgraph
  ```

  ```bash pnpm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pnpm add openai langsmith @langchain/langgraph
  ```
</CodeGroup>

### 2. Configure your environment

```bash wrap theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
export LANGSMITH_TRACING=true
export LANGSMITH_API_KEY=<your-api-key>

# This example uses OpenAI, but you can use any LLM provider of choice
export OPENAI_API_KEY=<your-openai-api-key>
```

<Note>
  If your account is in a region other than US (the default), also set `LANGSMITH_ENDPOINT` to the API URL for your region. Without this, your API key won't be recognized and requests will fail to authenticate.

  <table>
    <thead>
      <tr>
        <th>Region</th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <td>GCP US</td>
      </tr>

      <tr>
        <td>GCP EU</td>
      </tr>

      <tr>
        <td>GCP APAC</td>
      </tr>

      <tr>
        <td>AWS US</td>
      </tr>
    </tbody>
  </table>

  For example, EU accounts: `export LANGSMITH_ENDPOINT="https://eu.api.smith.langchain.com"`.
</Note>

<Info>
  If you are using LangChain.js with LangSmith and are not in a serverless environment, we also recommend setting the following explicitly to reduce latency:

  `export LANGCHAIN_CALLBACKS_BACKGROUND=true`

  If you are in a serverless environment, we recommend setting the reverse to allow tracing to finish before your function ends:

  `export LANGCHAIN_CALLBACKS_BACKGROUND=false`

  See [this LangChain.js guide](https://js.langchain.com/docs/how_to/callbacks_serverless) for more information.
</Info>

### 3. Log a trace

Once you've set up your environment, [wrap or decorate the custom functions/SDKs](/langsmith/annotate-code#use-%40traceable-%2F-traceable) you want to trace. LangSmith will then infer the proper tracing config:

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import json
  import openai
  import operator
  from langsmith import traceable
  from langsmith.wrappers import wrap_openai
  from typing import Annotated, Literal, TypedDict
  from langgraph.graph import StateGraph

  class State(TypedDict):
      messages: Annotated[list, operator.add]

  tool_schema = {
      "type": "function",
      "function": {
          "name": "search",
          "description": "Call to surf the web.",
          "parameters": {
              "type": "object",
              "properties": {"query": {"type": "string"}},
              "required": ["query"],
          },
      },
  }

  # Decorating the tool function will automatically trace it with the correct context
  @traceable(run_type="tool", name="Search Tool")
  def search(query: str):
      """Call to surf the web."""
      if "sf" in query.lower() or "san francisco" in query.lower():
          return "It's 60 degrees and foggy."
      return "It's 90 degrees and sunny."

  tools = [search]

  def call_tools(state):
      function_name_to_function = {"search": search}
      messages = state["messages"]
      tool_call = messages[-1]["tool_calls"][0]
      function_name = tool_call["function"]["name"]
      function_arguments = tool_call["function"]["arguments"]
      arguments = json.loads(function_arguments)
      function_response = function_name_to_function[function_name](**arguments)
      tool_message = {
          "tool_call_id": tool_call["id"],
          "role": "tool",
          "name": function_name,
          "content": function_response,
      }
      return {"messages": [tool_message]}

  wrapped_client = wrap_openai(openai.Client())

  def should_continue(state: State) -> Literal["tools", "__end__"]:
      messages = state["messages"]
      last_message = messages[-1]
      if last_message["tool_calls"]:
          return "tools"
      return "__end__"

  def call_model(state: State):
      messages = state["messages"]
      # Calling the wrapped client will automatically infer the correct tracing context
      response = wrapped_client.chat.completions.create(
          messages=messages, model="gpt-5.4-mini", tools=[tool_schema]
      )
      raw_tool_calls = response.choices[0].message.tool_calls
      tool_calls = [tool_call.to_dict() for tool_call in raw_tool_calls] if raw_tool_calls else []
      response_message = {
          "role": "assistant",
          "content": response.choices[0].message.content,
          "tool_calls": tool_calls,
      }
      return {"messages": [response_message]}

  workflow = StateGraph(State)
  workflow.add_node("agent", call_model)
  workflow.add_node("tools", call_tools)
  workflow.add_edge("__start__", "agent")
  workflow.add_conditional_edges(
      "agent",
      should_continue,
  )
  workflow.add_edge("tools", 'agent')

  app = workflow.compile()

  final_state = app.invoke(
      {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
  )

  final_state["messages"][-1]["content"]
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  **Note:** The below example requires `langsmith>=0.1.39` and `@langchain/langgraph>=0.0.31`

  import OpenAI from "openai";
  import { StateGraph } from "@langchain/langgraph";
  import { wrapOpenAI } from "langsmith/wrappers/openai";
  import { traceable } from "langsmith/traceable";

  type GraphState = {
    messages: OpenAI.ChatCompletionMessageParam[];
  };

  const wrappedClient = wrapOpenAI(new OpenAI({}));

  const toolSchema: OpenAI.ChatCompletionTool = {
    type: "function",
    function: {
      name: "search",
      description: "Use this tool to query the web.",
      parameters: {
        type: "object",
        properties: {
          query: {
            type: "string",
          },
        },
        required: ["query"],
      }
    }
  };

  // Wrapping the tool function will automatically trace it with the correct context
  const search = traceable(async ({ query }: { query: string }) => {
    if (
      query.toLowerCase().includes("sf") ||
      query.toLowerCase().includes("san francisco")
    ) {
      return "It's 60 degrees and foggy.";
    }
    return "It's 90 degrees and sunny.";
  }, { run_type: "tool", name: "Search Tool" });

  const callTools = async ({ messages }: GraphState) => {
    const mostRecentMessage = messages[messages.length - 1];
    const toolCalls = (mostRecentMessage as OpenAI.ChatCompletionAssistantMessageParam).tool_calls;
    if (toolCalls === undefined || toolCalls.length === 0) {
      throw new Error("No tool calls passed to node.");
    }
    const toolNameMap = {
      search,
    };
    const functionName = toolCalls[0].function.name;
    const functionArguments = JSON.parse(toolCalls[0].function.arguments);
    const response = await toolNameMap[functionName](functionArguments);
    const toolMessage = {
      tool_call_id: toolCalls[0].id,
      role: "tool",
      name: functionName,
      content: response,
    }
    return { messages: [toolMessage] };
  };

  const callModel = async ({ messages }: GraphState) => {
    // Calling the wrapped client will automatically infer the correct tracing context
    const response = await wrappedClient.chat.completions.create({
      messages,
      model: "gpt-5.4-mini",
      tools: [toolSchema],
    });
    const responseMessage = {
      role: "assistant",
      content: response.choices[0].message.content,
      tool_calls: response.choices[0].message.tool_calls ?? [],
    };
    return { messages: [responseMessage] };
  };

  const shouldContinue = ({ messages }: GraphState) => {
    const lastMessage =
      messages[messages.length - 1] as OpenAI.ChatCompletionAssistantMessageParam;
    if (
      lastMessage?.tool_calls !== undefined &&
      lastMessage?.tool_calls.length > 0
    ) {
      return "tools";
    }
    return "__end__";
  }

  const workflow = new StateGraph<GraphState>({
    channels: {
      messages: {
        reducer: (a: any, b: any) => a.concat(b),
      }
    }
  });

  const graph = workflow
    .addNode("model", callModel)
    .addNode("tools", callTools)
    .addEdge("__start__", "model")
    .addConditionalEdges("model", shouldContinue, {
      tools: "tools",
      __end__: "__end__",
    })
    .addEdge("tools", "model")
    .compile();

  await graph.invoke({
    messages: [{ role: "user", content: "what is the weather in sf" }]
  });
  ```
</CodeGroup>

### Viewing the trace

**Details view**

Click on the trace, and toggle to the **Details** view on the top right. Your trace in LangSmith should [look like this](https://smith.langchain.com/public/c3d128fa-c618-4b0e-b9d0-ccbb619440d8/r).

**Messages view**

The **Messages** view in the LangSmith UI shows a simplified conversation history between the user and the agent. This view pulls messages from the top-level trace (including the user’s initial request, tool calls, and the agent’s final response) and represents them in a chat-like format.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-with-langgraph.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Trace LiveKit applications
Source: https://docs.langchain.com/langsmith/trace-with-livekit

LangSmith can capture traces generated by [LiveKit Agents](https://docs.livekit.io/agents/) using OpenTelemetry instrumentation. This guide shows you how to automatically capture traces from your LiveKit voice AI agents and send them to LangSmith for monitoring and analysis.

For our high-level guiding principles on tracing voice agents, see [Voice tracing fundamentals](/langsmith/trace-voice-fundamentals).

For a complete implementation, see the [voice demo repository](https://github.com/langchain-ai/voice-demo).

## Installation

Install the required packages:

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install langsmith livekit livekit-agents livekit-plugins-openai livekit-plugins-silero livekit-plugins-turn-detector opentelemetry-exporter-otlp python-dotenv
  ```

  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv add langsmith livekit livekit-agents livekit-plugins-openai livekit-plugins-silero livekit-plugins-turn-detector opentelemetry-exporter-otlp python-dotenv
  ```
</CodeGroup>

## Quickstart tutorial

Follow this step-by-step tutorial to create a voice AI agent with LiveKit and LangSmith tracing. You'll build a complete working example by copying and pasting code snippets.

### Step 1: Set up your environment

Create a `.env` file in your project directory:

```bash .env theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
OTEL_EXPORTER_OTLP_ENDPOINT=https://api.smith.langchain.com/otel
OTEL_EXPORTER_OTLP_HEADERS=x-api-key=<your-langsmith-api-key>, Langsmith-Project=livekit-voice
LIVEKIT_URL=<your-livekit-url>
LIVEKIT_API_KEY=<your-livekit-api-key>
LIVEKIT_API_SECRET=<your-livekit-api-secret>
OPENAI_API_KEY=<your-openai-api-key>
```

### Step 2: Download the span processor

LiveKit emits OpenTelemetry spans, but most of the useful data rides in LiveKit-specific attributes that LangSmith doesn't recognize by default. A custom span processor translates those attributes so your traces render properly in LangSmith.

Add the [custom span processor file](https://github.com/langchain-ai/voice-demo/blob/main/src/voice_demo/livekit/processor.py) and save it as `langsmith_processor.py` in your project directory.

<Accordion title="What does the span processor do?">
  The span processor enriches LiveKit Agents' OpenTelemetry spans with LangSmith-compatible attributes so your traces display properly in LangSmith.

  **Key functions:**

  * Converts LiveKit span types (stt, llm, tts, agent, session, job) to LangSmith format.
  * Adds `gen_ai.prompt.*` and `gen_ai.completion.*` attributes for message visualization.
  * Surfaces LiveKit's metrics (time-to-first-token, time-to-first-byte, end-to-end latency, and other `lk.*` analysis data) as run metadata.
  * Tracks and aggregates conversation messages across the conversation.
  * Renders the whole-conversation transcript and attaches the call recording to the root run.

  It only reshapes spans it recognizes as LiveKit's; any other span (for example, a nested LangChain or LangGraph run) passes through untouched. The processor activates when you import it in your code.
</Accordion>

### Step 3: Create your voice agent file

Create a new file called `agent.py` and add the following code. We'll build it section by section so you can copy and paste each part.

#### Part 1: Import dependencies and set up tracing

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import sys
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import LiveKit components
from livekit import agents
from livekit.agents import AgentServer, AgentSession, Agent
from livekit.agents.telemetry import set_tracer_provider
from livekit.plugins import openai, silero
from livekit.plugins.turn_detector.multilingual import MultilingualModel
from opentelemetry.sdk.trace import TracerProvider

# Import span processor to enable LangSmith tracing
from langsmith_processor import LangSmithSpanProcessor

# Set up LangSmith tracing
def setup_langsmith():
    """Setup OpenTelemetry tracing to export spans to LangSmith."""
    endpoint = os.getenv("OTEL_EXPORTER_OTLP_ENDPOINT")
    headers = os.getenv("OTEL_EXPORTER_OTLP_HEADERS")

    if not endpoint or not headers:
        print("⚠️  Warning: OTEL environment variables not set. Tracing disabled.")
        return

    # Create tracer provider with custom span processor
    trace_provider = TracerProvider()
    trace_provider.add_span_processor(LangSmithSpanProcessor())

    # Set as LiveKit's tracer provider
    set_tracer_provider(trace_provider)
    print("✅ LangSmith tracing enabled")

# Enable tracing before creating agents
setup_langsmith()
```

#### Part 2: Define your agent

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(
            instructions="""You are a helpful voice AI assistant.
            You eagerly assist users with their questions.
            Keep responses concise and conversational.""",
        )
```

#### Part 3: Set up the agent server

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
server = AgentServer()

@server.rtc_session()
async def my_agent(ctx: agents.JobContext):
    # Create agent session with STT, LLM, TTS, and VAD
    session = AgentSession(
        stt="deepgram/nova-2:en",
        llm="openai/gpt-5.4-mini",
        tts=openai.TTS(model="tts-1", voice="alloy"),
        vad=silero.VAD.load(),
        turn_detection=MultilingualModel(),
    )

    # Start the session
    await session.start(
        room=ctx.room,
        agent=Assistant(),
    )

if __name__ == "__main__":
    # Run in console mode for local testing
    sys.argv = [sys.argv[0], "console"]
    agents.cli.run_app(server)
```

### Step 4: Run your agent

Run your voice agent in console mode for local testing:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
python agent.py console
```

Your agent will start and connect to LiveKit. Speak through your microphone, and all traces will automatically appear in LangSmith.

View the complete [agent.py code](https://github.com/langchain-ai/voice-demo/blob/main/src/voice_demo/livekit/agent.py).

## Advanced usage

### Trace speech-to-speech models

The previous example uses a cascade pipeline (separate STT, LLM, and TTS services). LiveKit also supports speech-to-speech models, where a single realtime model handles audio in and out. To trace one, build the session with a realtime model instead of the STT/LLM/TTS stack. The tracing setup is identical and the span processor is unchanged:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from livekit.plugins import openai as lk_openai

session = AgentSession(llm=lk_openai.realtime.RealtimeModel(voice="marin"))
```

### Attach the conversation audio

To listen to a conversation alongside its transcript, record the call and attach the audio file to the root run. Record what was played to the client so the recording reflects what was actually heard, including any speech cut off by an interruption. For the underlying attachment API, see [Upload files with traces](/langsmith/upload-files-with-traces).

### Custom metadata and tags

You can add custom metadata to your traces using span attributes:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from opentelemetry import trace

class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(
            instructions="You are a helpful assistant.",
        )

        # Get current span and add custom attributes
        tracer = trace.get_tracer(__name__)
        span = trace.get_current_span()
        if span:
            span.set_attribute("langsmith.metadata.agent_type", "voice_assistant")
            span.set_attribute("langsmith.metadata.version", "1.0")
            span.set_attribute("langsmith.span.tags", "livekit,voice-ai,production")
```

## Troubleshooting

### Spans not appearing in LangSmith

If traces aren't showing up in LangSmith:

1. **Verify environment variables**: Ensure `OTEL_EXPORTER_OTLP_ENDPOINT` and `OTEL_EXPORTER_OTLP_HEADERS` are set correctly in your `.env` file.
2. **Check setup order**: Make sure `setup_langsmith()` is called **before** creating `AgentServer`.
3. **Check API key**: Confirm your LangSmith API key has write permissions.
4. **Look for confirmation**: You should see "✅ LangSmith tracing enabled" in the console when starting.

### Messages not showing correctly

If conversation messages aren't displaying properly:

1. **Check span processor**: Verify `langsmith_processor.py` is in your project directory and imported correctly.
2. **Verify imports**: Ensure `LangSmithSpanProcessor` is imported in your agent.py.
3. **Enable debug logging**: Set `LANGSMITH_PROCESSOR_DEBUG=true` in your environment to see detailed logs.

### Connection issues

If your agent can't connect to LiveKit:

1. **Verify LiveKit URL**: Check `LIVEKIT_URL` is set correctly in your `.env` file.
2. **Check credentials**: Ensure `LIVEKIT_API_KEY` and `LIVEKIT_API_SECRET` are correct.
3. **Test connection**: Try connecting to your LiveKit server with the LiveKit CLI first.
4. **Console mode**: For local testing, always use: `python agent.py console`.

### Import errors

If you're getting import errors:

1. **Install dependencies**: Run the complete pip install command from Step 1.
2. **Check Python version**: Ensure you're using Python 3.9 or higher.
3. **Verify langsmith\_processor**: Make sure `langsmith_processor.py` is downloaded and in the same directory as `agent.py`.
4. **Check LiveKit plugins**: Ensure you have the correct LiveKit plugins installed for your STT/LLM/TTS providers.

### Agent not responding

If your agent connects but doesn't respond:

1. **Check API keys**: Verify your OpenAI API key (or other provider keys) are correct.
2. **Test services**: Ensure your STT, LLM, and TTS services are accessible.
3. **Check instructions**: Make sure your Agent has proper instructions.
4. **Review logs**: Look for errors in the console output.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-with-livekit.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Trace Mastra applications
Source: https://docs.langchain.com/langsmith/trace-with-mastra

[Mastra](https://mastra.ai/docs) is a TypeScript framework for building AI-powered applications and agents. Using Mastra’s [LangSmith exporter](https://mastra.ai/docs/observability/ai-tracing/exporters/langsmith), you can send traces from your Mastra agents and workflows to LangSmith for debugging, evaluation, and observability.

This guide shows you how to integrate Mastra with LangSmith using Mastra’s AI tracing system.

## Installation

Install Mastra and the LangSmith exporter:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
npm install @mastra/core @mastra/langsmith @mastra/observability @mastra/libsql
```

## Setup

1. Set your LangSmith API key and (optionally) a LangSmith project name:

   ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
   export LANGSMITH_API_KEY=<your_langsmith_api_key>
   export LANGCHAIN_PROJECT=<your_project_name> # optional
   ```

   <Tip>
     If [`LANGCHAIN_PROJECT`](/langsmith/log-traces-to-project) is not set, traces will be sent to the default project.
   </Tip>

2. If you plan to use OpenAI models, also ensure you have an OpenAI API key available at runtime:

   ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
   export OPENAI_API_KEY=<your_openai_api_key>
   ```

3. In your project directory, create the following project structure and files:

   ```
   src/
       mastra.ts
       agent.ts
       index.ts
   ```

## Configure Mastra with the LangSmith exporter

Mastra tracing is configured directly on the `Mastra` constructor. Add the following to a `mastra.ts` file:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { Mastra } from "@mastra/core";
import { LibSQLStore } from "@mastra/libsql";
import { LangSmithExporter } from "@mastra/langsmith";

import { echoAgent } from "./agent";

export const mastra = new Mastra({
  agents: { echoAgent },

  storage: new LibSQLStore({
    url: "file:./mastra.db",
  }),

  observability: {
    configs: {
      langsmith: {
        serviceName: "mastra-langsmith-demo",
        exporters: [
          new LangSmithExporter({
            apiKey: process.env.LANGSMITH_API_KEY,
          }),
        ],
      },
    },
  },

  // Disable deprecated telemetry system
  telemetry: {
    enabled: false,
  },
});
```

* [Storage is required for tracing](https://mastra.ai/docs/observability/ai-tracing/overview#basic-config) (even when exporting traces externally).
* The LangSmith exporter reads credentials from environment variables.
* The [deprecated telemetry system](https://mastra.ai/docs/observability/overview#otel-tracing-deprecated) is disabled to avoid warnings.
* No separate instrumentation file is required when running Mastra outside of the Mastra server.
  For more details, refer to the [Mastra docs](https://mastra.ai/docs/observability/ai-tracing/overview).

### Define an agent

For compatibility, use [string-based model identifiers](https://mastra.ai/models#basic-usage). Add the following code to an `agent.ts` file:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { Agent } from "@mastra/core/agent";

export const echoAgent = new Agent({
  name: "echoAgent",
  instructions: "You are a helpful assistant.",
  model: "openai/gpt-4o-mini",
});
```

Mastra will automatically route the model call using your configured API keys and capture traces for each invocation.

### Run the agent

1. Add the following to an `index.ts` file:

   ```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
   import { mastra } from "./mastra";

   async function main() {
   const agent = mastra.getAgent("echoAgent");
   const result = await agent.generate("Say hello and explain what Mastra is.");
   console.log(result.text);
   }

   main();
   ```

2. Run your application:

   ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
   npx ts-node src/index.ts
   ```

## View traces in LangSmith

After running the agent:

1. Open the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-trace-with-mastra).
2. Select your project. For example, the value of `LANGCHAIN_PROJECT`.
3. Locate the trace corresponding to `echoAgent.generate`.

You’ll be able to inspect:

* Model inputs and outputs
* Agent execution steps
* Timing and error information

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-with-mastra.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Trace Microsoft Agent Framework applications
Source: https://docs.langchain.com/langsmith/trace-with-microsoft-agent-framework

LangSmith can capture traces generated by [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/overview/agent-framework-overview) using its built-in OpenTelemetry instrumentation. This guide shows you how to automatically capture traces from your Microsoft Agent Framework agents and send them to LangSmith for monitoring and analysis.

## Installation

Install the required packages:

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install agent-framework opentelemetry-exporter-otlp-proto-http
  ```

  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv add agent-framework opentelemetry-exporter-otlp-proto-http
  ```
</CodeGroup>

## Setup

### 1. Configure environment variables

Enable OpenTelemetry instrumentation of the agent and set the OpenTelemetry environment variables to point to the LangSmith OTEL endpoint:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
export ENABLE_INSTRUMENTATION=true
export OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf
export OTEL_EXPORTER_OTLP_ENDPOINT=https://api.smith.langchain.com/otel/v1/traces
export OTEL_EXPORTER_OTLP_HEADERS="x-api-key=<your_langsmith_api_key>,Langsmith-Project=<your_project_name>"
```

### 2. Enable OpenTelemetry in your application

In your Microsoft Agent Framework application, enable OpenTelemetry tracing using the built-in `configure_otel_providers` function:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from agent_framework.observability import configure_otel_providers

# Enable OpenTelemetry tracing
configure_otel_providers(enable_sensitive_data=True)
```

<Note>
  Setting `enable_sensitive_data=True` allows capturing input and output content in traces. Set to `False` if you want to exclude sensitive data from traces.
</Note>

### 3. Create and run your agent

Once configured, your Microsoft Agent Framework agents will automatically send traces to LangSmith:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from agent_framework import ChatAgent
from agent_framework.observability import configure_otel_providers
from agent_framework.openai import OpenAIChatClient

# Enable OpenTelemetry tracing
configure_otel_providers(enable_sensitive_data=True)

agent = ChatAgent(
    chat_client=OpenAIChatClient(model_id="gpt-4o"),
)

result = await agent.run("What's the the capital of Bavaria?")
print(result.text)
```

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-with-microsoft-agent-framework.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
