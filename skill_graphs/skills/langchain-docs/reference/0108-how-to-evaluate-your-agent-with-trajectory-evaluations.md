# How to evaluate your agent with trajectory evaluations
Source: https://docs.langchain.com/langsmith/trajectory-evals

Many agent behaviors only emerge when using a real LLM, such as which tool the agent decides to call, how it formats responses, or whether a prompt modification affects the entire execution trajectory. LangChain's [`agentevals`](https://github.com/langchain-ai/agentevals) package provides evaluators specifically designed for testing agent trajectories with live models.

<Note>
  This guide covers the open source [LangChain](/oss/python/langchain/overview) `agentevals` package, which integrates with LangSmith for trajectory evaluation.
</Note>

AgentEvals allows you to evaluate the trajectory of your agent (the exact sequence of messages, including tool calls) by performing a *trajectory match* or by using an *LLM judge*:

<Card title="Trajectory match" icon="equal" href="#trajectory-match-evaluator">
  Hard-code a reference trajectory for a given input and validate the run via a step-by-step comparison.

  Ideal for testing well-defined workflows where you know the expected behavior. Use when you have specific expectations about which tools should be called and in what order. This approach is deterministic, fast, and cost-effective since it doesn't require additional LLM calls.
</Card>

<Card title="LLM-as-judge" icon="hammer" href="#llm-as-judge-evaluator">
  Use a LLM to qualitatively validate your agent's execution trajectory. The "judge" LLM reviews the agent's decisions against a prompt rubric (which can include a reference trajectory).

  More flexible and can assess nuanced aspects like efficiency and appropriateness, but requires an LLM call and is less deterministic. Use when you want to evaluate the overall quality and reasonableness of the agent's trajectory without strict tool call or ordering requirements.
</Card>

## Installing AgentEvals

<CodeGroup>
  ```bash Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install agentevals
  ```

  ```bash TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  npm install agentevals @langchain/core
  ```
</CodeGroup>

Or, clone the [AgentEvals repository](https://github.com/langchain-ai/agentevals) directly.

## Trajectory match evaluator

AgentEvals offers the `create_trajectory_match_evaluator` function in Python and `createTrajectoryMatchEvaluator` in TypeScript to match your agent's trajectory against a reference trajectory.

You can use the following modes:

| Mode                                     | Description                                               | Use Case                                                              |
| ---------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------------------- |
| [`strict`](#strict-match)                | Exact match of messages and tool calls in the same order  | Testing specific sequences (e.g., policy lookup before authorization) |
| [`unordered`](#unordered-match)          | Same tool calls allowed in any order                      | Verifying information retrieval when order doesn't matter             |
| [`subset`](#subset-and-superset-match)   | Agent calls only tools from reference (no extras)         | Ensuring agent doesn't exceed expected scope                          |
| [`superset`](#subset-and-superset-match) | Agent calls at least the reference tools (extras allowed) | Verifying minimum required actions are taken                          |

### Strict match

The `strict` mode ensures trajectories contain identical messages in the same order with the same tool calls, though it allows for differences in message content. This is useful when you need to enforce a specific sequence of operations, such as requiring a policy lookup before authorizing an action.

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langchain.agents import create_agent
  from langchain.tools import tool
  from langchain.messages import HumanMessage, AIMessage, ToolMessage
  from agentevals.trajectory.match import create_trajectory_match_evaluator

  @tool
  def get_weather(city: str):
      """Get weather information for a city."""
      return f"It's 75 degrees and sunny in {city}."

  agent = create_agent("gpt-5.5", tools=[get_weather])

  evaluator = create_trajectory_match_evaluator(  # [!code highlight]
      trajectory_match_mode="strict",  # [!code highlight]
  )  # [!code highlight]

  def test_weather_tool_called_strict():
      result = agent.invoke({
          "messages": [HumanMessage(content="What's the weather in San Francisco?")]
      })

      reference_trajectory = [
          HumanMessage(content="What's the weather in San Francisco?"),
          AIMessage(content="", tool_calls=[
              {"id": "call_1", "name": "get_weather", "args": {"city": "San Francisco"}}
          ]),
          ToolMessage(content="It's 75 degrees and sunny in San Francisco.", tool_call_id="call_1"),
          AIMessage(content="The weather in San Francisco is 75 degrees and sunny."),
      ]

      evaluation = evaluator(
          outputs=result["messages"],
          reference_outputs=reference_trajectory
      )
      # {
      #     'key': 'trajectory_strict_match',
      #     'score': True,
      #     'comment': None,
      # }
      assert evaluation["score"] is True
  ```

  ```ts TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createAgent, tool, HumanMessage, AIMessage, ToolMessage } from "langchain"
  import { createTrajectoryMatchEvaluator } from "agentevals";
  import * as z from "zod";

  const getWeather = tool(
    async ({ city }: { city: string }) => {
      return `It's 75 degrees and sunny in ${city}.`;
    },
    {
      name: "get_weather",
      description: "Get weather information for a city.",
      schema: z.object({
        city: z.string(),
      }),
    }
  );

  const agent = createAgent({
    model: "gpt-5.5",
    tools: [getWeather]
  });

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
    // {
    //     'key': 'trajectory_strict_match',
    //     'score': true,
    //     'comment': null,
    // }
    expect(evaluation.score).toBe(true);
  }
  ```
</CodeGroup>

### Unordered match

The `unordered` mode allows the same tool calls in any order, which is helpful when you want to verify that the correct set of tools are being invoked but don't care about the sequence. For example, an agent might need to check both weather and events for a city, but the order doesn't matter.

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langchain.agents import create_agent
  from langchain.tools import tool
  from langchain.messages import HumanMessage, AIMessage, ToolMessage
  from agentevals.trajectory.match import create_trajectory_match_evaluator

  @tool
  def get_weather(city: str):
      """Get weather information for a city."""
      return f"It's 75 degrees and sunny in {city}."

  @tool
  def get_events(city: str):
      """Get events happening in a city."""
      return f"Concert at the park in {city} tonight."

  agent = create_agent("gpt-5.5", tools=[get_weather, get_events])

  evaluator = create_trajectory_match_evaluator(  # [!code highlight]
      trajectory_match_mode="unordered",  # [!code highlight]
  )  # [!code highlight]

  def test_multiple_tools_any_order():
      result = agent.invoke({
          "messages": [HumanMessage(content="What's happening in SF today?")]
      })

      # Reference shows tools called in different order than actual execution
      reference_trajectory = [
          HumanMessage(content="What's happening in SF today?"),
          AIMessage(content="", tool_calls=[
              {"id": "call_1", "name": "get_events", "args": {"city": "SF"}},
              {"id": "call_2", "name": "get_weather", "args": {"city": "SF"}},
          ]),
          ToolMessage(content="Concert at the park in SF tonight.", tool_call_id="call_1"),
          ToolMessage(content="It's 75 degrees and sunny in SF.", tool_call_id="call_2"),
          AIMessage(content="Today in SF: 75 degrees and sunny with a concert at the park tonight."),
      ]

      evaluation = evaluator(
          outputs=result["messages"],
          reference_outputs=reference_trajectory,
      )
      # {
      #     'key': 'trajectory_unordered_match',
      #     'score': True,
      # }
      assert evaluation["score"] is True
  ```

  ```ts TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createAgent, tool, HumanMessage, AIMessage, ToolMessage } from "langchain"
  import { createTrajectoryMatchEvaluator } from "agentevals";
  import * as z from "zod";

  const getWeather = tool(
    async ({ city }: { city: string }) => {
      return `It's 75 degrees and sunny in ${city}.`;
    },
    {
      name: "get_weather",
      description: "Get weather information for a city.",
      schema: z.object({ city: z.string() }),
    }
  );

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
    model: "gpt-5.5",
    tools: [getWeather, getEvents]
  });

  const evaluator = createTrajectoryMatchEvaluator({  // [!code highlight]
    trajectoryMatchMode: "unordered",  // [!code highlight]
  });  // [!code highlight]

  async function testMultipleToolsAnyOrder() {
    const result = await agent.invoke({
      messages: [new HumanMessage("What's happening in SF today?")]
    });

    // Reference shows tools called in different order than actual execution
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
    // {
    //     'key': 'trajectory_unordered_match',
    //     'score': true,
    // }
    expect(evaluation.score).toBe(true);
  }
  ```
</CodeGroup>

### Subset and superset match

The `superset` and `subset` modes focus on which tools are called rather than the order of tool calls, allowing you to control how strictly the agent's tool calls must align with the reference.

* Use `superset` mode when you want to verify that a few key tools are called in the execution, but you're okay with the agent calling additional tools. The agent's trajectory must include at least all the tool calls in the reference trajectory, and may include additional tool calls beyond the reference.
* Use `subset` mode to ensure agent efficiency by verifying that the agent did not call any irrelevant or unnecessary tools beyond those in the reference. The agent's trajectory must include only tool calls that appear in the reference trajectory.

The following example demonstrates `superset` mode, where the reference trajectory only requires the `get_weather` tool, but the agent can call additional tools:

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langchain.agents import create_agent
  from langchain.tools import tool
  from langchain.messages import HumanMessage, AIMessage, ToolMessage
  from agentevals.trajectory.match import create_trajectory_match_evaluator

  @tool
  def get_weather(city: str):
      """Get weather information for a city."""
      return f"It's 75 degrees and sunny in {city}."

  @tool
  def get_detailed_forecast(city: str):
      """Get detailed weather forecast for a city."""
      return f"Detailed forecast for {city}: sunny all week."

  agent = create_agent("gpt-5.5", tools=[get_weather, get_detailed_forecast])

  evaluator = create_trajectory_match_evaluator(  # [!code highlight]
      trajectory_match_mode="superset",  # [!code highlight]
  )  # [!code highlight]

  def test_agent_calls_required_tools_plus_extra():
      result = agent.invoke({
          "messages": [HumanMessage(content="What's the weather in Boston?")]
      })

      # Reference only requires get_weather, but agent may call additional tools
      reference_trajectory = [
          HumanMessage(content="What's the weather in Boston?"),
          AIMessage(content="", tool_calls=[
              {"id": "call_1", "name": "get_weather", "args": {"city": "Boston"}},
          ]),
          ToolMessage(content="It's 75 degrees and sunny in Boston.", tool_call_id="call_1"),
          AIMessage(content="The weather in Boston is 75 degrees and sunny."),
      ]

      evaluation = evaluator(
          outputs=result["messages"],
          reference_outputs=reference_trajectory,
      )
      # {
      #     'key': 'trajectory_superset_match',
      #     'score': True,
      #     'comment': None,
      # }
      assert evaluation["score"] is True
  ```

  ```ts TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createAgent } from "langchain"
  import { tool } from "@langchain/core/tools";
  import { HumanMessage, AIMessage, ToolMessage } from "@langchain/core/messages";
  import { createTrajectoryMatchEvaluator } from "agentevals";
  import * as z from "zod";

  const getWeather = tool(
    async ({ city }: { city: string }) => {
      return `It's 75 degrees and sunny in ${city}.`;
    },
    {
      name: "get_weather",
      description: "Get weather information for a city.",
      schema: z.object({ city: z.string() }),
    }
  );

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
    model: "gpt-5.5",
    tools: [getWeather, getDetailedForecast]
  });

  const evaluator = createTrajectoryMatchEvaluator({  // [!code highlight]
    trajectoryMatchMode: "superset",  // [!code highlight]
  });  // [!code highlight]

  async function testAgentCallsRequiredToolsPlusExtra() {
    const result = await agent.invoke({
      messages: [new HumanMessage("What's the weather in Boston?")]
    });

    // Reference only requires getWeather, but agent may call additional tools
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
    // {
    //     'key': 'trajectory_superset_match',
    //     'score': true,
    //     'comment': null,
    // }
    expect(evaluation.score).toBe(true);
  }
  ```
</CodeGroup>

<Info>
  You can also customize how the evaluator considers equality between tool calls in the actual trajectory vs. the reference by setting the `tool_args_match_mode` (Python) or `toolArgsMatchMode` (TypeScript) property, as well as the `tool_args_match_overrides` (Python) or `toolArgsMatchOverrides` (TypeScript) property. By default, only tool calls with the same arguments to the same tool are considered equal. Visit the [repository](https://github.com/langchain-ai/agentevals?tab=readme-ov-file#tool-args-match-modes) for more details.
</Info>

## LLM-as-judge evaluator

<Note>
  This section covers the trajectory-specific LLM-as-a-judge evaluator from the `agentevals` package. For general-purpose LLM-as-a-judge evaluators in LangSmith, refer to the [LLM-as-a-judge evaluator](/langsmith/llm-as-judge).
</Note>

You can also use an LLM to evaluate the agent's execution path. Unlike the trajectory match evaluators, it doesn't require a reference trajectory, but one can be provided if available.

### Without reference trajectory

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langchain.agents import create_agent
  from langchain.tools import tool
  from langchain.messages import HumanMessage, AIMessage, ToolMessage
  from agentevals.trajectory.llm import create_trajectory_llm_as_judge, TRAJECTORY_ACCURACY_PROMPT

  @tool
  def get_weather(city: str):
      """Get weather information for a city."""
      return f"It's 75 degrees and sunny in {city}."

  agent = create_agent("gpt-5.5", tools=[get_weather])

  evaluator = create_trajectory_llm_as_judge(  # [!code highlight]
      model="openai:o3-mini",  # [!code highlight]
      prompt=TRAJECTORY_ACCURACY_PROMPT,  # [!code highlight]
  )  # [!code highlight]

  def test_trajectory_quality():
      result = agent.invoke({
          "messages": [HumanMessage(content="What's the weather in Seattle?")]
      })

      evaluation = evaluator(
          outputs=result["messages"],
      )
      # {
      #     'key': 'trajectory_accuracy',
      #     'score': True,
      #     'comment': 'The provided agent trajectory is reasonable...'
      # }
      assert evaluation["score"] is True
  ```

  ```ts TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createAgent } from "langchain"
  import { tool } from "@langchain/core/tools";
  import { HumanMessage, AIMessage, ToolMessage } from "@langchain/core/messages";
  import { createTrajectoryLLMAsJudge, TRAJECTORY_ACCURACY_PROMPT } from "agentevals";
  import * as z from "zod";

  const getWeather = tool(
    async ({ city }: { city: string }) => {
      return `It's 75 degrees and sunny in ${city}.`;
    },
    {
      name: "get_weather",
      description: "Get weather information for a city.",
      schema: z.object({ city: z.string() }),
    }
  );

  const agent = createAgent({
    model: "gpt-5.5",
    tools: [getWeather]
  });

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
    // {
    //     'key': 'trajectory_accuracy',
    //     'score': true,
    //     'comment': 'The provided agent trajectory is reasonable...'
    // }
    expect(evaluation.score).toBe(true);
  }
  ```
</CodeGroup>

### With reference trajectory

If you have a reference trajectory, you can add an extra variable to your prompt and pass in the reference trajectory. Below, we use the prebuilt `TRAJECTORY_ACCURACY_PROMPT_WITH_REFERENCE` prompt and configure the `reference_outputs` variable:

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  evaluator = create_trajectory_llm_as_judge(
      model="openai:o3-mini",
      prompt=TRAJECTORY_ACCURACY_PROMPT_WITH_REFERENCE,
  )
  evaluation = evaluator(
      outputs=result["messages"],
      reference_outputs=reference_trajectory,
  )
  ```

  ```ts TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { TRAJECTORY_ACCURACY_PROMPT_WITH_REFERENCE } from "agentevals";

  const evaluator = createTrajectoryLLMAsJudge({
    model: "openai:o3-mini",
    prompt: TRAJECTORY_ACCURACY_PROMPT_WITH_REFERENCE,
  });

  const evaluation = await evaluator({
    outputs: result.messages,
    referenceOutputs: referenceTrajectory,
  });
  ```
</CodeGroup>

<Info>
  For more configurability over how the LLM evaluates the trajectory, visit the [repository](https://github.com/langchain-ai/agentevals?tab=readme-ov-file#trajectory-llm-as-judge).
</Info>

## Async support (Python)

All `agentevals` evaluators support Python asyncio. For evaluators that use factory functions, async versions are available by adding `async` after `create_` in the function name.

Here's an example using the async judge and evaluator:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from agentevals.trajectory.llm import create_async_trajectory_llm_as_judge, TRAJECTORY_ACCURACY_PROMPT
from agentevals.trajectory.match import create_async_trajectory_match_evaluator

async_judge = create_async_trajectory_llm_as_judge(
    model="openai:o3-mini",
    prompt=TRAJECTORY_ACCURACY_PROMPT,
)

async_evaluator = create_async_trajectory_match_evaluator(
    trajectory_match_mode="strict",
)

async def test_async_evaluation():
    result = await agent.ainvoke({
        "messages": [HumanMessage(content="What's the weather?")]
    })

    evaluation = await async_judge(outputs=result["messages"])
    assert evaluation["score"] is True
```

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trajectory-evals.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Troubleshooting
Source: https://docs.langchain.com/langsmith/troubleshooting

This guide will walk you through common issues you may encounter when running a self-hosted instance of LangSmith.

While running LangSmith, you may encounter unexpected 500 errors, slow performance, or other issues. This guide will help you diagnose and resolve these issues.

## Getting helpful information

To diagnose and resolve an issue, you will first need to retrieve some relevant information. The following sections explain how to do this for a Kubernetes or a Docker setup, and how to pull helpful browser information.

Generally, the main services you will want to analyze are the:

* `langsmith-backend`: Handles CRUD API requests, business logic, requests from the frontend and SDK, trace preparation for ingestion, and the hub API.
* `langsmith-platform-backend`: Handles authentication, run ingestion, and other high-volume tasks.
* `langsmith-queue`: Handles incoming traces and feedback, asynchronous ingestion and persistence into the datastore, data integrity checks, and retries during database errors or connection issues.

For more details on these services, refer to the [self-hosted overview](/langsmith/self-hosted).

#### Kubernetes

The first step in troubleshooting is to gather important debugging information about your LangSmith deployment. Service logs, kubernetes events, and resource utilization of containers can help identify the root cause of an issue.

You can run our [k8s troubleshooting script](https://github.com/langchain-ai/helm/blob/main/charts/langsmith/scripts/get_k8s_debugging_info.sh) which will pull all of the relevant kubernetes information and output it to a folder for investigation. The script also compresses this folder into a zip file for sharing. Here is an example of how to run this script, assuming your langsmith deployment was brought up in a `langsmith` namespace:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
bash get_k8s_debugging_info.sh --namespace langsmith
```

You can then inspect the contents of the produced folder for any relevant errors or information. If you would like the LangSmith team to assist in debugging, please share this zip file with the team.

#### Docker

If running on Docker, you can check the logs your deployment by running the following command:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
docker compose logs >> logs.txt
```

#### Browser errors

If you are experiencing an issue that surfaces as a browser error, it may also be helpful to inspect a HAR file which may include key information. To get the HAR file, you can follow [this guide](https://support.langchain.com/articles/9042697994-how-to-generate-a-har-file-for-troubleshooting) which explains the short process for various browsers.

You can then use [Google's HAR analyzer](https://toolbox.googleapps.com/apps/har_analyzer/) to investigate. You can also send your HAR file to the LangSmith team to help with debugging.

## Common issues

### *DB::Exception: Cannot reserve 1.00 MiB, not enough space: While executing WaitForAsyncInsert. (NOT\_ENOUGH\_SPACE)*

This error occurs when ClickHouse runs out of disk space. You will need to increase the disk space available to ClickHouse.

#### Kubernetes

In Kubernetes, you will need to increase the size of the ClickHouse PVC. To achieve this, you can perform the following steps:

1. Get the storage class of the PVC: `kubectl get pvc data-langsmith-clickhouse-0 -n <namespace> -o jsonpath='{.spec.storageClassName}'`

2. Ensure the storage class has AllowVolumeExpansion: true: `kubectl get sc <storage-class-name> -o jsonpath='{.allowVolumeExpansion}'`

   * If it is false, some storage classes can be updated to allow volume expansion.
   * To update the storage class, you can run `kubectl patch sc <storage-class-name> -p '{"allowVolumeExpansion": true}'`
   * If this fails, you may need to create a new storage class with the correct settings.

3. Edit your pvc to have the new size: `kubectl edit pvc data-langsmith-clickhouse-0 -n <namespace>` or `kubectl patch pvc data-langsmith-clickhouse-0 '{"spec":{"resources":{"requests":{"storage":"100Gi"}}}}' -n <namespace>`

4. Update your helm chart `langsmith_config.yaml` to new size(e.g `100 Gi`)

5. Delete the clickhouse statefulset `kubectl delete statefulset langsmith-clickhouse --cascade=orphan -n <namespace>`

6. Apply helm chart with updated size (You can follow the [upgrade guide](/langsmith/self-host-upgrades))

7. Your pvc should now have the new size. Verify by running `kubectl get pvc` and `kubectl exec langsmith-clickhouse-0 -- bash -c "df"`

#### Docker

In Docker, you will need to increase the size of the ClickHouse volume. To achieve this, you can perform the following steps:

1. Stop your instance of LangSmith. `docker compose down`
2. If using bind mount, you will need to increase the size of the mount point.
3. If using a docker `volume`, you will need to allocate more space to the volume/docker.

### *error: Dirty database version 'version'. fix and force version*

This error occurs when the ClickHouse database is in an inconsistent state with our migrations. You will need to reset to an earlier database version and then rerun your upgrade/migrations.

#### Kubernetes

1. Force migration to an earlier version, where version = dirty version - 1.

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
kubectl exec -it deployments/langsmith-backend -- bash -c 'migrate -source "file://clickhouse/migrations" -database "clickhouse://$CLICKHOUSE_HOST:$CLICKHOUSE_NATIVE_PORT?username=$CLICKHOUSE_USER&password=$CLICKHOUSE_PASSWORD&database=$CLICKHOUSE_DB&x-multi-statement=true&x-migrations-table-engine=MergeTree&secure=$CLICKHOUSE_TLS" force <version>'
```

1. Rerun your upgrade/migrations.

#### Docker

1. Force migration to an earlier version, where version = dirty version - 1.

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
docker compose exec langchain-backend migrate -source "file://clickhouse/migrations" -database "clickhouse://$CLICKHOUSE_HOST:$CLICKHOUSE_NATIVE_PORT?username=$CLICKHOUSE_USER&password=$CLICKHOUSE_PASSWORD&database=$CLICKHOUSE_DB&x-multi-statement=true&x-migrations-table-engine=MergeTree&secure=$CLICKHOUSE_TLS" force <version>
```

1. Rerun your upgrade/migrations.

### *413 - request entity too large*

This error occurs when the request size exceeds the maximum allowed size. You will need to increase the maximum request size in your Nginx configuration.

#### Kubernetes

1. Edit your `langsmith_config.yaml` and increase the `frontend.maxBodySize` [value](https://github.com/langchain-ai/helm/blob/main/charts/langsmith/values.yaml#L519). This might look something like this:

```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
frontend:
  maxBodySize: "100M"
```

2. Apply your changes to the cluster.

### *Details: code: 497, message: default: Not enough privileges. to execute this query, it's necessary to have the grant CREATE ROW POLICY ON default.feedbacks\_rmt*

This error occurs when your user does not have the necessary permissions to create row policies in Clickhouse. When deploying the Docker deployment, you need to copy the `users.xml` file from the github repo as well. This adds the `<access_management>` tag to the `users.xml` file, which allows the user to create row policies. Below is the default `users.xml` file that we expect to be used.

```xml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
<clickhouse>
    <users>
        <default>
            <access_management>1</access_management>
            <named_collection_control>1</named_collection_control>
            <show_named_collections>1</show_named_collections>
            <show_named_collections_secrets>1</show_named_collections_secrets>
            <profile>default</profile>
        </default>
    </users>
    <profiles>
        <default>
            <async_insert>1</async_insert>
            <async_insert_max_data_size>2000000</async_insert_max_data_size>
            <wait_for_async_insert>0</wait_for_async_insert>
            <parallel_view_processing>1</parallel_view_processing>
            <allow_simdjson>0</allow_simdjson>
            <lightweight_deletes_sync>0</lightweight_deletes_sync>
        </default>
    </profiles>
</clickhouse>
```

In some environments, your mount point may not be writable by the container. In these cases we suggest building a custom image with the `users.xml` file included.

Example `Dockerfile`:

```dockerfile theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
FROM clickhouse/clickhouse-server:24.8
COPY ./users.xml /etc/clickhouse-server/users.d/users.xml
```

Then take the following steps:

1. Build your custom image.

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
docker build -t <image-name> .
```

2. Update your `docker-compose.yaml` to use the custom image. Make sure to remove the users.xml mount point.

```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
langchain-clickhouse:
  image: <image-name>
```

3. Restart your instance of LangSmith.

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
docker compose down --volumes
docker compose up
```

### *ClickHouse fails to start up when running a cluster with AquaSec*

In some environments, AquaSec may prevent ClickHouse from starting up correctly. This may manifest as the ClickHouse pod not emitting any logs and failing to get marked as ready.
Generally this is due to `LD_PRELOAD` being set by AquaSec, which interferes with ClickHouse. To resolve this, you can add the following environment variable to your ClickHouse deployment:

#### Kubernetes

Edit your `langsmith_config.yaml` (or corresponding config file) and set the `AQUA_SKIP_LD_PRELOAD` environment variable:

```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
clickhouse:
  statefulSet:
    extraEnv:
      - name: AQUA_SKIP_LD_PRELOAD
        value: "true"
```

#### Docker

Edit your `docker-compose.yaml` and set the `AQUA_SKIP_LD_PRELOAD` environment variable:

```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
langchain-clickhouse:
  environment:
    - AQUA_SKIP_LD_PRELOAD=true
```

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/troubleshooting.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Studio troubleshooting
Source: https://docs.langchain.com/langsmith/troubleshooting-studio

## Safari connection issues

Safari blocks plain-HTTP traffic on localhost. When running Studio with `langgraph dev`, you may see "Failed to load assistants" errors.

### Solution 1: Use Cloudflare Tunnel

<Tabs>
  <Tab title="Python">
    ```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    pip install -U langgraph-cli>=0.2.6
    langgraph dev --tunnel
    ```
  </Tab>

  <Tab title="JS">
    ```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    # Requires @langchain/langgraph-cli>=0.0.26
    npx @langchain/langgraph-cli dev --tunnel
    ```
  </Tab>
</Tabs>

The command outputs a tunnel URL. To connect Studio:

1. Copy the tunnel URL (e.g., `https://hamilton-praise-heart-costumes.trycloudflare.com`)
2. Open Studio at `https://smith.langchain.com/studio/`
3. Click **Connect to a local server**
4. Paste the tunnel URL and add it to **Allowed Origins**
5. Click **Connect**

This manual step is required for security - Studio requires explicit user confirmation before connecting to external URLs.

<Note>
  Cloudflare tunnels can be unreliable and may intermittently disconnect.
</Note>

### Solution 2: Use Chromium browser

Chrome and other Chromium browsers allow HTTP on localhost. Use `langgraph dev` without additional configuration.

## Chrome connection issues

Starting with Chrome version 142, you may experience "Failed to initialize Studio" errors with "TypeError: Failed to fetch" when trying to connect [LangSmith Studio](/langsmith/studio) to your local development server via [`langgraph dev`](/langsmith/cli). This occurs even when the API server at `http://127.0.0.1:2024/docs` loads successfully.

**Root Cause:** Chrome 142 fully enforces the Private Network Access (PNA) specification with no fallback, which blocks HTTPS sites (like `https://smith.langchain.com`) from accessing HTTP localhost servers by default.

### Symptoms

* Running `langgraph dev` starts the server successfully.
* Navigating to `http://127.0.0.1:2024/docs` shows the API documentation correctly.
* LangSmith Studio at `https://smith.langchain.com` shows: "Failed to initialize Studio - Please verify if the API server is running or accessible from the browser. TypeError: Failed to fetch".
* Browser console shows errors like: `Permission was denied for this request to access the 'unknown' address space`.

### Solution: Allow local network access in Chrome

1. Open LangSmith Studio at `https://smith.langchain.com` in Chrome.
2. Click the **lock icon** (or site information icon) to the left of the address bar.
3. Look for the **"Local network access"** option in the dropdown.
4. Change the setting from **"Ask (default)"** or **"Block"** to **"Allow"**.
5. Reload the page.

Studio should now connect to your local development server successfully.

### Additional troubleshooting

**Check for browser extension conflicts**

Browser extensions (especially Ollama Chrome extension or AI model extensions) can interfere with localhost connections:

1. Disable all browser extensions temporarily.
2. Restart Chrome.
3. Try connecting to Studio again.
4. If it works, re-enable extensions one by one to identify the culprit.

**Verify dependencies are up to date**

```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
pip install -U "langgraph-cli[inmem]"
```

**Clear browser cache and site data**

1. In Chrome, go to **Settings** > **Privacy and Security** > **Site Settings**.
2. Find `https://smith.langchain.com` in the list.
3. Click **Clear data**.
4. Restart Chrome and try again.

## Brave connection issues

Brave blocks plain-HTTP traffic on localhost when Brave Shields are enabled. When running Studio with `langgraph dev`, you may see "Failed to load assistants" errors.

### Solution 1: Disable Brave shields

Disable Brave Shields for LangSmith using the Brave icon in the URL bar.

### Solution 2: Use Cloudflare Tunnel

<Tabs>
  <Tab title="Python">
    ```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    pip install -U langgraph-cli>=0.2.6
    langgraph dev --tunnel
    ```
  </Tab>

  <Tab title="JS">
    ```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    # Requires @langchain/langgraph-cli>=0.0.26
    npx @langchain/langgraph-cli dev --tunnel
    ```
  </Tab>
</Tabs>

The command outputs a tunnel URL. To connect Studio:

1. Copy the tunnel URL (e.g., `https://hamilton-praise-heart-costumes.trycloudflare.com`)
2. Open Studio at `https://smith.langchain.com/studio/`
3. Click **Connect to a local server**
4. Paste the tunnel URL and add it to **Allowed Origins**
5. Click **Connect**

This manual step is required for security - Studio requires explicit user confirmation before connecting to external URLs.

## Graph edge issues

Undefined conditional edges may show unexpected connections in your graph. This is
because without proper definition, Studio assumes the conditional edge could access all other nodes. To address this, explicitly define the routing paths using one of these methods:

### Solution 1: Path map

Define a mapping between router outputs and target nodes:

<Tabs>
  <Tab title="Python">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    graph.add_conditional_edges("node_a", routing_function, {True: "node_b", False: "node_c"})
    ```
  </Tab>

  <Tab title="Javascript">
    ```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    graph.addConditionalEdges("node_a", routingFunction, { true: "node_b", false: "node_c" });
    ```
  </Tab>
</Tabs>

<a />

### Solution 2: Router type definition

Specify possible routing destinations using Python's `Literal` type:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
def routing_function(state: GraphState) -> Literal["node_b","node_c"]:
    if state['some_condition'] == True:
        return "node_b"
    else:
        return "node_c"
```

## Experiment troubleshooting in Studio

### **Run experiment** button is disabled

Check the following:

* **Deployed application**: If your application is deployed on LangSmith, you may need to create a new revision to enable this feature.
* **Local development server**: If you are running your application locally, make sure you have upgraded to the latest version of the `langgraph-cli` (`pip install -U langgraph-cli`). Additionally, ensure you have tracing enabled by setting the `LANGSMITH_API_KEY` in your project's `.env` file.

### Evaluator results are missing

When you run an experiment, any attached evaluators are scheduled for execution in a queue. If you don't see results immediately, it likely means they are still pending.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/troubleshooting-studio.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Troubleshoot variable caching
Source: https://docs.langchain.com/langsmith/troubleshooting-variable-caching

If you're not seeing traces in your tracing project or notice traces logged to the wrong project/workspace, the issue might be due to LangSmith's default environment variable caching. This is especially common when running LangSmith within a Jupyter notebook. Follow these steps to diagnose and resolve the issue:

## 1. Verify your environment variables

First, check that the environment variables are set correctly by running:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import os
print(os.getenv("LANGSMITH_PROJECT"))
print(os.getenv("LANGSMITH_TRACING"))
print(os.getenv("LANGSMITH_ENDPOINT"))
print(os.getenv("LANGSMITH_API_KEY"))
```

If the output does not match what's defined in your .env file, it's likely due to environment variable caching.

## 2. Clear the cache

Clear the cached environment variables with the following command:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
utils.get_env_var.cache_clear()
```

## 3. Reload the environment variables

Reload your environment variables from the .env file by executing:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from dotenv import load_dotenv
import os
load_dotenv(<path to .env file>, override=True)
```

After reloading, your environment variables should be set correctly.

If you continue to experience issues, please reach out to us via a shared Slack channel or email support (available for Plus and Enterprise plans), or in the [LangChain Forum](https://forum.langchain.com/).

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/troubleshooting-variable-caching.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
