# console.log(result);
/**
 * {
 *   messages: [
 *     ...
 *     { role: "tool", content: "Returning structured response: {'task': 'update the project timeline', 'assignee': 'Sarah', 'priority': 'high'}", tool_call_id: "call_456", name: "MeetingAction" }
 *   ],
 *   structuredResponse: { task: "update the project timeline", assignee: "Sarah", priority: "high" }
 * }
 */
```

### Error handling

Models can make mistakes when generating structured output via tool calling. LangChain provides intelligent retry mechanisms to handle these errors automatically.

#### Multiple structured outputs error

When a model incorrectly calls multiple structured output tools, the agent provides error feedback in a [`ToolMessage`](https://reference.langchain.com/javascript/langchain-core/messages/ToolMessage) and prompts the model to retry:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import * as z from "zod";
import { createAgent, toolStrategy } from "langchain";

const ContactInfo = z.object({
    name: z.string().describe("Person's name"),
    email: z.string().describe("Email address"),
});

const EventDetails = z.object({
    event_name: z.string().describe("Name of the event"),
    date: z.string().describe("Event date"),
});

const agent = createAgent({
    model: "gpt-5.5",
    tools: [],
    responseFormat: toolStrategy([ContactInfo, EventDetails]),
});

const result = await agent.invoke({
    messages: [
        {
        role: "user",
        content:
            "Extract info: John Doe (john@email.com) is organizing Tech Conference on March 15th",
        },
    ],
});

console.log(result);

/**
 * {
 *   messages: [
 *     { role: "user", content: "Extract info: John Doe (john@email.com) is organizing Tech Conference on March 15th" },
 *     { role: "assistant", content: "", tool_calls: [ { name: "ContactInfo", args: { name: "John Doe", email: "john@email.com" }, id: "call_1" }, { name: "EventDetails", args: { event_name: "Tech Conference", date: "March 15th" }, id: "call_2" } ] },
 *     { role: "tool", content: "Error: Model incorrectly returned multiple structured responses (ContactInfo, EventDetails) when only one is expected.\n Please fix your mistakes.", tool_call_id: "call_1", name: "ContactInfo" },
 *     { role: "tool", content: "Error: Model incorrectly returned multiple structured responses (ContactInfo, EventDetails) when only one is expected.\n Please fix your mistakes.", tool_call_id: "call_2", name: "EventDetails" },
 *     { role: "assistant", content: "", tool_calls: [ { name: "ContactInfo", args: { name: "John Doe", email: "john@email.com" }, id: "call_3" } ] },
 *     { role: "tool", content: "Returning structured response: {'name': 'John Doe', 'email': 'john@email.com'}", tool_call_id: "call_3", name: "ContactInfo" }
 *   ],
 *   structuredResponse: { name: "John Doe", email: "john@email.com" }
 * }
 */
```

#### Schema validation error

When structured output doesn't match the expected schema, the agent provides specific error feedback:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import * as z from "zod";
import { createAgent, toolStrategy } from "langchain";

const ProductRating = z.object({
    rating: z.number().min(1).max(5).describe("Rating from 1-5"),
    comment: z.string().describe("Review comment"),
});

const agent = createAgent({
    model: "gpt-5.5",
    tools: [],
    responseFormat: toolStrategy(ProductRating),
});

const result = await agent.invoke({
    messages: [
        {
        role: "user",
        content: "Parse this: Amazing product, 10/10!",
        },
    ],
});

console.log(result);

/**
 * {
 *   messages: [
 *     { role: "user", content: "Parse this: Amazing product, 10/10!" },
 *     { role: "assistant", content: "", tool_calls: [ { name: "ProductRating", args: { rating: 10, comment: "Amazing product" }, id: "call_1" } ] },
 *     { role: "tool", content: "Error: Failed to parse structured output for tool 'ProductRating': 1 validation error for ProductRating\nrating\n  Input should be less than or equal to 5 [type=less_than_equal, input_value=10, input_type=int].\n Please fix your mistakes.", tool_call_id: "call_1", name: "ProductRating" },
 *     { role: "assistant", content: "", tool_calls: [ { name: "ProductRating", args: { rating: 5, comment: "Amazing product" }, id: "call_2" } ] },
 *     { role: "tool", content: "Returning structured response: {'rating': 5, 'comment': 'Amazing product'}", tool_call_id: "call_2", name: "ProductRating" }
 *   ],
 *   structuredResponse: { rating: 5, comment: "Amazing product" }
 * }
 */
```

#### Error handling strategies

You can customize how errors are handled using the `handleErrors` parameter:

**Custom error message:**

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const responseFormat = toolStrategy(ProductRating, {
    handleError: "Please provide a valid rating between 1-5 and include a comment."
)

// Error message becomes:
// { role: "tool", content: "Please provide a valid rating between 1-5 and include a comment." }
```

**Handle specific exceptions only:**

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { ToolInputParsingException } from "@langchain/core/tools";

const responseFormat = toolStrategy(ProductRating, {
    handleError: (error: ToolStrategyError) => {
        if (error instanceof ToolInputParsingException) {
        return "Please provide a valid rating between 1-5 and include a comment.";
        }
        return error.message;
    }
)

// Only validation errors get retried with default message:
// { role: "tool", content: "Error: Failed to parse structured output for tool 'ProductRating': ...\n Please fix your mistakes." }
```

**Handle multiple exception types:**

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const responseFormat = toolStrategy(ProductRating, {
    handleError: (error: ToolStrategyError) => {
        if (error instanceof ToolInputParsingException) {
        return "Please provide a valid rating between 1-5 and include a comment.";
        }
        if (error instanceof CustomUserError) {
        return "This is a custom user error.";
        }
        return error.message;
    }
)
```

**No error handling:**

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const responseFormat = toolStrategy(ProductRating, {
    handleError: false  // All errors raised
)
```

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/structured-output.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# LangSmith Studio
Source: https://docs.langchain.com/oss/javascript/langchain/studio

When building agents with LangChain locally, it's helpful to visualize what's happening inside your agent, interact with it in real-time, and debug issues as they occur. **LangSmith Studio** is a free visual interface for developing and testing your LangChain agents from your local machine.

Studio connects to your locally running agent to show you each step your agent takes: the prompts sent to the model, tool calls and their results, and the final output. You can test different inputs, inspect intermediate states, and iterate on your agent's behavior without additional code or deployment.

This pages describes how to set up Studio with your local LangChain agent.

## Prerequisites

Before you begin, ensure you have the following:

* **A LangSmith account**: Sign up (for free) or log in at [smith.langchain.com](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=snippets-oss-studio-js).
* **A LangSmith API key**: Follow the [Create an API key](/langsmith/create-account-api-key) guide.
* If you don't want data [traced](/langsmith/observability-concepts#traces) to LangSmith, set `LANGSMITH_TRACING=false` in your application's `.env` file. With tracing disabled, no data leaves your local server.

## Set up local Agent server

### 1. Install the LangGraph CLI

The [LangGraph CLI](/langsmith/cli) provides a local development server (also called [Agent Server](/langsmith/agent-server)) that connects your agent to Studio.

```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
npx @langchain/langgraph-cli
```

### 2. Prepare your agent

If you already have a LangChain agent, you can use it directly. This example uses a simple email agent:

```typescript title="agent.ts" theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { createAgent } from "@langchain/agents";

function sendEmail(to: string, subject: string, body: string): string {
  const email = {
    to,
    subject,
    body,
  };
  // ... email sending logic

  return `Email sent to ${to}`;
}

const agent = createAgent({
  model: "gpt-5.5",
  tools: [sendEmail],
  systemPrompt: "You are an email assistant. Always use the send_email tool.",
});
```

### 3. Environment variables

Studio requires a LangSmith API key to connect your local agent. Create a `.env` file in the root of your project and add your API key from [LangSmith](https://smith.langchain.com/settings).

<Warning>
  Ensure your `.env` file is not committed to version control, such as Git.
</Warning>

```bash .env theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
LANGSMITH_API_KEY=lsv2...
```

### 4. Create a LangGraph config file

The LangGraph CLI uses a configuration file to locate your agent and manage dependencies. Create a `langgraph.json` file in your app's directory:

```json title="langgraph.json" theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "dependencies": ["."],
  "graphs": {
    "agent": "./src/agent.ts:agent"
  },
  "env": ".env"
}
```

The [`createAgent`](https://reference.langchain.com/javascript/langchain/index/createAgent) function automatically returns a compiled LangGraph graph, which is what the `graphs` key expects in the configuration file.

<Info>
  For detailed explanations of each key in the JSON object of the configuration file, refer to the [LangGraph configuration file reference](/langsmith/cli#configuration-file).
</Info>

At this point, the project structure will look like this:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
my-app/
├── src
│   └── agent.ts
├── .env
└── langgraph.json
```

### 5. Install dependencies

```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
yarn install
```

### 6. View your agent in Studio

Start the development server to connect your agent to Studio:

```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
npx @langchain/langgraph-cli dev
```

<Warning>
  Safari blocks `localhost` connections to Studio. To work around this, run the above command with `--tunnel` to access Studio via a secure tunnel.
</Warning>

Once the server is running, your agent is accessible both via API at `http://127.0.0.1:2024` and through the Studio UI at `https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024`:

<Frame>
  <img alt="Agent view in the Studio UI" />
</Frame>

With Studio connected to your local agent, you can iterate quickly on your agent's behavior. Run a test input, inspect the full execution trace including prompts, tool arguments, return values, and token/latency metrics. When something goes wrong, Studio captures exceptions with the surrounding state to help you understand what happened.

The development server supports hot-reloading—make changes to prompts or tool signatures in your code, and Studio reflects them immediately. Re-run conversation threads from any step to test your changes without starting over. This workflow scales from simple single-tool agents to complex multi-node graphs.

For more information on how to run Studio, refer to the following guides in the [LangSmith docs](/langsmith/observability):

* [Run application](/langsmith/use-studio#run-application)
* [Manage assistants](/langsmith/use-studio#manage-assistants)
* [Manage threads](/langsmith/use-studio#manage-threads)
* [Iterate on prompts](/langsmith/observability-studio)
* [Debug LangSmith traces](/langsmith/observability-studio#debug-langsmith-traces)
* [Add node to dataset](/langsmith/observability-studio#add-node-to-dataset)

## Video guide

<Frame>
  <iframe title="Studio" />
</Frame>

<Tip>
  For more information about deployed agents, see [Deploy](/oss/javascript/langchain/deploy).
</Tip>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/studio.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Agent Evals
Source: https://docs.langchain.com/oss/javascript/langchain/test/evals

Evaluate agent trajectories using deterministic matching or LLM-as-judge evaluators with AgentEvals and LangSmith.

Evaluations ("evals") measure how well your agent performs by assessing its execution trajectory, the sequence of messages and tool calls it produces. Unlike [integration tests](/oss/javascript/langchain/test/integration-testing) that verify basic correctness, evals score agent behavior against a reference or rubric, making them useful for catching regressions when you change prompts, tools, or models.

An evaluator is a function that takes agent outputs (and optionally reference outputs) and returns a score:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
function evaluator({ outputs, referenceOutputs }: {
  outputs: Record<string, any>;
  referenceOutputs: Record<string, any>;
}) {
  const outputMessages = outputs.messages;
  const referenceMessages = referenceOutputs.messages;
  const score = compareMessages(outputMessages, referenceMessages);
  return { key: "evaluator_score", score: score };
}
```

The [`agentevals`](https://github.com/langchain-ai/agentevals) package provides prebuilt evaluators for agent trajectories. You can evaluate by performing a **trajectory match** (deterministic comparison) or by using an **LLM judge** (qualitative assessment):

| Approach                                        | When to use                                                                     |
| ----------------------------------------------- | ------------------------------------------------------------------------------- |
| [Trajectory match](#trajectory-match-evaluator) | You know the expected tool calls and want fast, deterministic, cost-free checks |
| [LLM-as-judge](#llm-as-judge-evaluator)         | You want to assess overall quality and reasoning without strict expectations    |

## Install AgentEvals

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
npm install agentevals @langchain/core
```

Or, clone the [AgentEvals repository](https://github.com/langchain-ai/agentevals) directly.

## Trajectory match evaluator

AgentEvals offers the `createTrajectoryMatchEvaluator` function to match your agent's trajectory against a reference. There are four modes:

| Mode        | Description                                                                                    | Use case                                                              |
| ----------- | ---------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `strict`    | Exact match of message structure and tool calls in the same order (message content can differ) | Testing specific sequences (e.g., policy lookup before authorization) |
| `unordered` | Same message structure and tool calls as reference, but tool calls can happen in any order     | Verifying information retrieval when order doesn't matter             |
| `subset`    | Agent calls only tools from reference (no extras)                                              | Ensuring agent doesn't exceed expected scope                          |
| `superset`  | Agent calls at least the reference tools (extras allowed)                                      | Verifying minimum required actions are taken                          |

The examples below share a common setup, an agent with a `get_weather` tool:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { createAgent } from "langchain";
import { tool } from "@langchain/core/tools";
import { HumanMessage, AIMessage, ToolMessage } from "@langchain/core/messages";
import { createTrajectoryMatchEvaluator } from "agentevals";
import * as z from "zod";

const getWeather = tool(
  async ({ city }) => {
    return `It's 75 degrees and sunny in ${city}.`;
  },
  {
    name: "get_weather",
    description: "Get weather information for a city.",
    schema: z.object({ city: z.string() }),
  }
);

const agent = createAgent({
  model: "claude-sonnet-4-6",
  tools: [getWeather],
});
```

<Accordion title="Strict match">
  The `strict` mode ensures trajectories contain identical messages in the same order with the same tool calls, though it allows for differences in message content. This is useful when you need to enforce a specific sequence of operations, such as requiring a policy lookup before authorizing an action.

  ```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  const evaluator = createTrajectoryMatchEvaluator({  // [!code highlight]
    trajectoryMatchMode: "strict",  // [!code highlight]
  });  // [!code highlight]

  async function testWeatherToolCalledStrict() {
    const result = await agent.invoke({
      messages: [new HumanMessage("What's the weather in San Francisco?")]
    });

    const referenceTrajectory = [
      new HumanMessage("What's the weather in San Francisco?"),
      new AIMessage({
        content: "",
        tool_calls: [
          { id: "call_1", name: "get_weather", args: { city: "San Francisco" } }
        ]
      }),
      new ToolMessage({
        content: "It's 75 degrees and sunny in San Francisco.",
        tool_call_id: "call_1"
      }),
      new AIMessage("The weather in San Francisco is 75 degrees and sunny."),
    ];

    const evaluation = await evaluator({
      outputs: result.messages,
      referenceOutputs: referenceTrajectory
    });
    expect(evaluation.score).toBe(true);
  }
  ```
</Accordion>

<Accordion title="Unordered match">
  The `unordered` mode allows the same tool calls in any order. This is helpful when you want to verify that specific information was retrieved but don't care about the sequence. For example, an agent that checks both weather and events for a city with different tool calls.

  ```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  const getEvents = tool(
    async ({ city }: { city: string }) => {
      return `Concert at the park in ${city} tonight.`;
    },
    {
      name: "get_events",
      description: "Get events happening in a city.",
      schema: z.object({ city: z.string() }),
    }
  );

  const agent = createAgent({
    model: "claude-sonnet-4-6",
    tools: [getWeather, getEvents],
  });

  const evaluator = createTrajectoryMatchEvaluator({  // [!code highlight]
    trajectoryMatchMode: "unordered",  // [!code highlight]
  });  // [!code highlight]

  async function testMultipleToolsAnyOrder() {
    const result = await agent.invoke({
      messages: [new HumanMessage("What's happening in SF today?")]
    });

    const referenceTrajectory = [
      new HumanMessage("What's happening in SF today?"),
      new AIMessage({
        content: "",
        tool_calls: [
          { id: "call_1", name: "get_events", args: { city: "SF" } },
          { id: "call_2", name: "get_weather", args: { city: "SF" } },
        ]
      }),
      new ToolMessage({
        content: "Concert at the park in SF tonight.",
        tool_call_id: "call_1"
      }),
      new ToolMessage({
        content: "It's 75 degrees and sunny in SF.",
        tool_call_id: "call_2"
      }),
      new AIMessage("Today in SF: 75 degrees and sunny with a concert at the park tonight."),
    ];

    const evaluation = await evaluator({
      outputs: result.messages,
      referenceOutputs: referenceTrajectory,
    });
    expect(evaluation.score).toBe(true);
  }
  ```
</Accordion>

<Accordion title="Subset and superset match">
  The `superset` and `subset` modes match partial trajectories. The `superset` mode verifies that the agent called at least the tools in the reference trajectory, allowing additional tool calls. The `subset` mode ensures the agent did not call any tools beyond those in the reference.

  ```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  const getDetailedForecast = tool(
    async ({ city }: { city: string }) => {
      return `Detailed forecast for ${city}: sunny all week.`;
    },
    {
      name: "get_detailed_forecast",
      description: "Get detailed weather forecast for a city.",
      schema: z.object({ city: z.string() }),
    }
  );

  const agent = createAgent({
    model: "claude-sonnet-4-6",
    tools: [getWeather, getDetailedForecast],
  });

  const evaluator = createTrajectoryMatchEvaluator({  // [!code highlight]
    trajectoryMatchMode: "superset",  // [!code highlight]
  });  // [!code highlight]

  async function testAgentCallsRequiredToolsPlusExtra() {
    const result = await agent.invoke({
      messages: [new HumanMessage("What's the weather in Boston?")]
    });

    const referenceTrajectory = [
      new HumanMessage("What's the weather in Boston?"),
      new AIMessage({
        content: "",
        tool_calls: [
          { id: "call_1", name: "get_weather", args: { city: "Boston" } },
        ]
      }),
      new ToolMessage({
        content: "It's 75 degrees and sunny in Boston.",
        tool_call_id: "call_1"
      }),
      new AIMessage("The weather in Boston is 75 degrees and sunny."),
    ];

    const evaluation = await evaluator({
      outputs: result.messages,
      referenceOutputs: referenceTrajectory,
    });
    expect(evaluation.score).toBe(true);
  }
  ```
</Accordion>

<Info>
  You can also set the `toolArgsMatchMode` property and/or `toolArgsMatchOverrides` to customize how the evaluator considers equality between tool calls in the actual trajectory vs. the reference. By default, only tool calls with the same arguments to the same tool are considered equal. Visit the [repository](https://github.com/langchain-ai/agentevals?tab=readme-ov-file#tool-args-match-modes) for more details.
</Info>

## LLM-as-judge evaluator

You can use an LLM to evaluate the agent's execution path with the `createTrajectoryLLMAsJudge` function. Unlike trajectory match evaluators, it doesn't require a reference trajectory, but one can be provided if available.

<Accordion title="Without reference trajectory">
  ```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createTrajectoryLLMAsJudge, TRAJECTORY_ACCURACY_PROMPT } from "agentevals";

  const evaluator = createTrajectoryLLMAsJudge({  // [!code highlight]
    model: "openai:o3-mini",  // [!code highlight]
    prompt: TRAJECTORY_ACCURACY_PROMPT,  // [!code highlight]
  });  // [!code highlight]

  async function testTrajectoryQuality() {
    const result = await agent.invoke({
      messages: [new HumanMessage("What's the weather in Seattle?")]
    });

    const evaluation = await evaluator({
      outputs: result.messages,
    });
    expect(evaluation.score).toBe(true);
  }
  ```
</Accordion>

<Accordion title="With reference trajectory">
  If you have a reference trajectory, use the prebuilt `TRAJECTORY_ACCURACY_PROMPT_WITH_REFERENCE` prompt:

  ```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createTrajectoryLLMAsJudge, TRAJECTORY_ACCURACY_PROMPT_WITH_REFERENCE } from "agentevals";

  const evaluator = createTrajectoryLLMAsJudge({
    model: "openai:o3-mini",
    prompt: TRAJECTORY_ACCURACY_PROMPT_WITH_REFERENCE,
  });

  const evaluation = await evaluator({
    outputs: result.messages,
    referenceOutputs: referenceTrajectory,
  });
  ```
</Accordion>

<Info>
  For more configurability over how the LLM evaluates the trajectory, visit the [repository](https://github.com/langchain-ai/agentevals?tab=readme-ov-file#trajectory-llm-as-judge).
</Info>

## Run evals in LangSmith

For tracking experiments over time, log evaluator results to [LangSmith](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=oss-langchain-test-evals). First, set the required environment variables:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
export LANGSMITH_API_KEY="your_langsmith_api_key"
export LANGSMITH_TRACING="true"
```

LangSmith offers two main approaches for running evaluations: [Vitest/Jest](/langsmith/vitest-jest) integration and the `evaluate` function.

<Accordion title="Use vitest/jest integration">
  ```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import * as ls from "langsmith/vitest";
  // import * as ls from "langsmith/jest";

  import { createTrajectoryLLMAsJudge, TRAJECTORY_ACCURACY_PROMPT } from "agentevals";

  const trajectoryEvaluator = createTrajectoryLLMAsJudge({
    model: "openai:o3-mini",
    prompt: TRAJECTORY_ACCURACY_PROMPT,
  });

  ls.describe("trajectory accuracy", () => {
    ls.test("accurate trajectory", {
      inputs: {
        messages: [
          { role: "user", content: "What is the weather in SF?" }
        ]
      },
      referenceOutputs: {
        messages: [
          new HumanMessage("What is the weather in SF?"),
          new AIMessage({
            content: "",
            tool_calls: [
              { id: "call_1", name: "get_weather", args: { city: "SF" } }
            ]
          }),
          new ToolMessage({
            content: "It's 75 degrees and sunny in SF.",
            tool_call_id: "call_1"
          }),
          new AIMessage("The weather in SF is 75 degrees and sunny."),
        ],
      },
    }, async ({ inputs, referenceOutputs }) => {
      const result = await agent.invoke({
        messages: [new HumanMessage("What is the weather in SF?")]
      });

      ls.logOutputs({ messages: result.messages });

      await trajectoryEvaluator({
        inputs,
        outputs: result.messages,
        referenceOutputs,
      });
    });
  });
  ```

  Run the evaluation with your test runner:

  ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  vitest run test_trajectory.eval.ts
  # or
  jest test_trajectory.eval.ts
  ```
</Accordion>

<Accordion title="Use the evaluate function">
  Create a [LangSmith dataset](/langsmith/manage-datasets) and use the `evaluate` function. The dataset must have the following schema:

  * **input**: `{"messages": [...]}` input messages to call the agent with.
  * **output**: `{"messages": [...]}` expected message history in the agent output. For trajectory evaluation, you can choose to keep only assistant messages.

  ```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { evaluate } from "langsmith/evaluation";
  import { createTrajectoryLLMAsJudge, TRAJECTORY_ACCURACY_PROMPT } from "agentevals";

  const trajectoryEvaluator = createTrajectoryLLMAsJudge({
    model: "openai:o3-mini",
    prompt: TRAJECTORY_ACCURACY_PROMPT,
  });

  async function runAgent(inputs: any) {
    const result = await agent.invoke(inputs);
    return result.messages;
  }

  await evaluate(
    runAgent,
    {
      data: "your_dataset_name",
      evaluators: [trajectoryEvaluator],
    }
  );
  ```
</Accordion>

<Tip>
  To learn more about evaluating your agent, see the [LangSmith docs](/langsmith/vitest-jest).
</Tip>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/test/evals.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Test
Source: https://docs.langchain.com/oss/javascript/langchain/test/index

Strategies for testing LangChain agents, including unit tests, integration tests, and trajectory evaluations.

Agentic applications let an LLM decide its own next steps to solve a problem. That flexibility is powerful, but the model's black-box nature makes it hard to predict how a tweak in one part of your agent will affect the whole. To build production-ready agents, thorough testing is essential.

There are a few approaches to testing your agents:

* **Unit tests** exercise small, deterministic pieces of your agent in isolation using in-memory fakes so you can assert exact behavior quickly and deterministically.
* **Integration tests** test the agent using real network calls to confirm that components work together, credentials and schemas line up, and latency is acceptable.
* **Evals** use evaluators to assess your agent's execution trajectory, either via deterministic matching or an LLM judge.

Agentic applications tend to lean more on integration because they chain multiple components together and must deal with flakiness due to the nondeterministic nature of LLMs.

<Tip>
  Run evaluations at scale, track results over time, and compare experiments with [LangSmith](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=oss-langchain-test-index). See [Evaluate an LLM application](/langsmith/evaluate-llm-application) to get started.
</Tip>

<CardGroup>
  <Card title="Unit testing" icon="flask" href="/oss/javascript/langchain/test/unit-testing">
    Mock chat models and use in-memory persistence to test agent logic without API calls.
  </Card>

  <Card title="Integration testing" icon="plug" href="/oss/javascript/langchain/test/integration-testing">
    Test your agent with real LLM APIs. Organize tests, manage keys, handle flakiness, and control costs.
  </Card>

  <Card title="Evals" icon="scale" href="/oss/javascript/langchain/test/evals">
    Evaluate agent trajectories with deterministic matching or LLM-as-judge evaluators.
  </Card>
</CardGroup>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/test/index.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Integration testing
Source: https://docs.langchain.com/oss/javascript/langchain/test/integration-testing

Test agents with real LLM APIs by organizing tests, managing keys, handling flakiness, and controlling costs.

Integration tests verify that your agent works correctly with model APIs and external services. Unlike [unit tests](/oss/javascript/langchain/test/unit-testing) that use fakes and mocks, integration tests make actual network calls to confirm that components work together, credentials are valid, and latency is acceptable.

Because LLM responses are nondeterministic, integration tests require different strategies than traditional software tests. This guide covers how to organize, write, and run integration tests for your agents. For general test infrastructure when contributing to LangChain itself, see [Contributing to code](/oss/javascript/contributing/code#running-tests).

## Separate unit and integration tests

Integration tests are slower and require API credentials, so keep them separate from unit tests. This lets you run fast unit tests on every change and reserve integration tests for CI or pre-deploy checks.

Use a file naming convention to separate integration tests. Name integration test files `*.int.test.ts` and configure vitest to exclude them from default runs:

```ts vitest.config.ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { configDefaults, defineConfig } from "vitest/config";

export default defineConfig((env) => {
  if (env.mode === "int") {
    return {
      test: {
        testTimeout: 100_000,
        include: ["**/*.int.test.ts"],
        setupFiles: ["dotenv/config"],
      },
    };
  }

  return {
    test: {
      testTimeout: 30_000,
      exclude: ["**/*.int.test.ts", ...configDefaults.exclude],
    },
  };
});
```

Add scripts to `package.json`:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "scripts": {
    "test": "vitest",
    "test:integration": "vitest --mode int"
  }
}
```

Run integration tests explicitly:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
npm run test:integration
```

## Manage API keys

Integration tests require real API credentials. Load them from environment variables so keys stay out of source control.

Add `dotenv/config` as a vitest setup file so environment variables load automatically from `.env`:

```ts vitest.config.ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
export default defineConfig({
  test: {
    setupFiles: ["dotenv/config"],
  },
});
```

```bash .env theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
OPENAI_API_KEY=sk-...
```

Skip tests when keys are missing:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { test } from "vitest";

test.skipIf(!process.env.OPENAI_API_KEY)(
  "agent responds with tool call",
  async () => {
    // ...
  }
);
```

<Warning>
  Add `.env` to your `.gitignore` to avoid committing credentials. In CI, inject secrets through your provider's secrets management (e.g., GitHub Actions secrets).
</Warning>

## Assert on structure, not content

LLM responses vary between runs. Instead of asserting on exact output strings, verify the structural properties of the response: message types, tool call names, argument shapes, and message count.

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
test("agent calls weather tool", async () => {
  const agent = createAgent({ model: "claude-sonnet-4-6", tools: [getWeather] });
  const result = await agent.invoke({
    messages: [new HumanMessage("What's the weather in SF?")]
  });

  const aiMsg = result.messages.find(
    (m) => AIMessage.isInstance(m) && m.tool_calls?.length
  );
  expect(aiMsg).toContainToolCall({ name: "get_weather" });
  expect(result.messages.at(-1)).toBeAIMessage();
});
```

This example uses [custom test matchers](#use-custom-test-matchers). See the section below for setup and the full matcher reference.

<Tip>
  For more rigorous trajectory assertions, use the [AgentEvals](/oss/javascript/langchain/test/evals) evaluators which support fuzzy matching modes like `unordered` and `superset`.
</Tip>

## Use custom test matchers

`langchain` ships [custom vitest matchers](https://vitest.dev/guide/extending-matchers.html) that make structural assertions more readable and produce clear error messages on failure. Register them once in a setup file and they become available on every `expect()` call.

### Set up

Add a vitest setup file that extends `expect` with the LangChain matchers:

```ts vitest.setup.ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { langchainMatchers } from "@langchain/core/testing";

expect.extend(langchainMatchers);
```

Reference it in your vitest config:

```ts vitest.config.ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
export default defineConfig({
  test: {
    setupFiles: ["vitest.setup.ts"],
  },
});
```

TypeScript types are included automatically, so no extra configuration is needed for autocomplete.

### Check message types

Each message class has a corresponding matcher: `toBeHumanMessage()`, `toBeAIMessage()`, `toBeSystemMessage()`, and `toBeToolMessage()`. Call without arguments to check only the type, or pass a string to also match content:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const response = await agent.invoke({
  messages: [new HumanMessage("What's the weather?")]
});
const lastMessage = response.messages.at(-1);

expect(lastMessage).toBeAIMessage();
expect(lastMessage).toBeAIMessage("It's 72°F and sunny.");
```

Pass an object to match specific fields:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
expect(lastMessage).toBeAIMessage({ name: "weather-bot" });
expect(toolMsg).toBeToolMessage({ tool_call_id: "call_1" });
```

### Assert on tool calls

Three matchers cover tool call assertions on an [`AIMessage`](https://reference.langchain.com/javascript/langchain-core/messages/AIMessage):

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const response = await agent.invoke({
  messages: [new HumanMessage("Weather in SF and NYC?")]
});
const aiMsg = response.messages.find(
  (m) => AIMessage.isInstance(m) && m.tool_calls?.length
);

// Check that specific tool calls are present (order-independent)
expect(aiMsg).toHaveToolCalls([
  { name: "get_weather", args: { city: "San Francisco" } },
  { name: "get_weather", args: { city: "New York" } },
]);

// Check only the count
expect(aiMsg).toHaveToolCallCount(2);

// Check that at least one tool call matches (supports .not)
expect(aiMsg).toContainToolCall({ name: "get_weather" });
expect(aiMsg).not.toContainToolCall({ name: "send_email" });
```

### Assert on tool messages

`toHaveToolMessages()` takes the full message array and checks the [`ToolMessage`](https://reference.langchain.com/javascript/langchain-core/messages/ToolMessage) instances within it, in order:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
expect(response.messages).toHaveToolMessages([
  { content: "72°F and sunny in San Francisco" },
  { content: "68°F and cloudy in New York" },
]);
```

### Assert on interrupts and structured responses

`toHaveBeenInterrupted()` checks for a `__interrupt__` field in a [LangGraph interrupt](/oss/javascript/langchain/human-in-the-loop) result. Pass a value to match the interrupt payload:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const result = await graph.invoke(input);

expect(result).toHaveBeenInterrupted();
expect(result).toHaveBeenInterrupted("confirm_action");
```

`toHaveStructuredResponse()` checks for a `structuredResponse` field on the result. Pass an object to match specific fields:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
expect(result).toHaveStructuredResponse();
expect(result).toHaveStructuredResponse({ name: "Alice", age: 30 });
```

### Matcher reference

| Matcher                               | Description                                                                                      |
| ------------------------------------- | ------------------------------------------------------------------------------------------------ |
| `toBeHumanMessage(expected?)`         | Check that the value is a `HumanMessage`. Optionally match content (string) or fields (object).  |
| `toBeAIMessage(expected?)`            | Check that the value is an `AIMessage`. Optionally match content or fields.                      |
| `toBeSystemMessage(expected?)`        | Check that the value is a `SystemMessage`. Optionally match content or fields.                   |
| `toBeToolMessage(expected?)`          | Check that the value is a `ToolMessage`. Optionally match content or fields like `tool_call_id`. |
| `toHaveToolCalls(expected)`           | Check that an `AIMessage` has exactly the given tool calls (order-independent).                  |
| `toHaveToolCallCount(n)`              | Check that an `AIMessage` has exactly `n` tool calls.                                            |
| `toContainToolCall(expected)`         | Check that an `AIMessage` contains at least one matching tool call. Supports `.not`.             |
| `toHaveToolMessages(expected)`        | Check that a message array contains the given `ToolMessage` instances, in order.                 |
| `toHaveBeenInterrupted(value?)`       | Check that a result has an `__interrupt__`. Optionally match the interrupt value.                |
| `toHaveStructuredResponse(expected?)` | Check that a result has a `structuredResponse`. Optionally match specific fields.                |

## Reduce cost and latency

Integration tests that call LLM APIs incur real costs. A few practices help keep test suites fast and affordable:

* **Use smaller models**: `gemini-3.1-flash-lite` or equivalent for tests that only need to verify tool calling and response structure.
* **Set `maxTokens`**: Cap response length to avoid long, expensive completions.
* **Limit test scope**: Test one behavior per test. Avoid end-to-end scenarios that chain many LLM calls when a single-turn test suffices.
* **Run selectively**: Use the test separation from [above](#separate-unit-and-integration-tests) to run integration tests only in CI or before deploy, not on every file save.

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const agent = createAgent({
  model: "gemini-3.1-flash-lite",
  tools: [getWeather],
  modelArgs: { maxTokens: 256 },
});
```

## Next steps

Learn how to evaluate agent trajectories with deterministic matching or LLM-as-judge evaluators in [Evals](/oss/javascript/langchain/test/evals).

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/test/integration-testing.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
