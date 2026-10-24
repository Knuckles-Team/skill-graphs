# How to return categorical vs numerical metrics
Source: https://docs.langchain.com/langsmith/metric-type

LangSmith supports both categorical and numerical metrics, and you can return either when writing a custom evaluator.

For an evaluator result to be logged as a numerical metric, it must returned as:

* (Python only) an `int`, `float`, or `bool`
* a dict of the form `{"key": "metric_name", "score": int | float | bool}`

For an evaluator result to be logged as a categorical metric, it must be returned as:

* (Python only) a `str`
* a dict of the form `{"key": "metric_name", "value": str | int | float | bool}`

Here are some examples:

* Python: Requires `langsmith>=0.2.0`
* TypeScript: Support for multiple scores is available in `langsmith@0.1.32` and higher

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  def numerical_metric(inputs: dict, outputs: dict, reference_outputs: dict) -> float:
      # Evaluation logic...
      return 0.8
      # Equivalently
      # return {"score": 0.8}
      # Or
      # return {"key": "numerical_metric", "score": 0.8}

  def categorical_metric(inputs: dict, outputs: dict, reference_outputs: dict) -> str:
      # Evaluation logic...
      return "english"
      # Equivalently
      # return {"key": "categorical_metric", "score": "english"}
      # Or
      # return {"score": "english"}
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import type { Run, Example } from "langsmith/schemas";

  function numericalMetric(run: Run, example: Example) {
    // Your evaluation logic here
    return { key: "numerical_metric", score: 0.8};
  }

  function categoricalMetric(run: Run, example: Example) {
    // Your evaluation logic here
    return { key: "categorical_metric", value: "english"};
  }
  ```
</CodeGroup>

## Related

* [Return multiple metrics in one evaluator](/langsmith/multiple-scores)

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/metric-type.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Manage model configurations
Source: https://docs.langchain.com/langsmith/model-configurations

Manage model configurations and control their availability across LangSmith features.

Model configurations define the model and parameters that LangSmith features use when calling an AI provider. A single shared library of configurations spans your entire [workspace](/langsmith/administration-overview#workspaces), so any configuration you create is available across the following features without duplication:

* [**Playground**](/langsmith/prompt-engineering-concepts)
* [**Evaluators**](/langsmith/evaluation)
* [**Fleet**](/langsmith/fleet/index)
* [**Chat**](/langsmith/chat)
* [**Insights**](/langsmith/insights)

[Workspace admins](/langsmith/rbac#workspace-admin) can create, edit, and delete configurations and control which providers and models are available per feature. Non-admin members can view configurations but cannot modify them.

## Feature Access

The **Feature Access** table controls provider and model availability independently for each LangSmith feature.

| **Feature**              | **Model selection experience**                                                                                                                                   |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Playground               | Full model controls—view and adjust all parameters. No built-in models; relies on workspace configurations.                                                      |
| Evaluators               | Full model controls—view and adjust all parameters. No built-in models; relies on workspace configurations.                                                      |
| Fleet                    | Choose from a curated list by default. You can also add custom workspace configurations.                                                                         |
| Chat                     | Choose from a curated list by default. You can also add custom workspace configurations.                                                                         |
| Insights (Thinking)      | Model used for deep analysis. Choose from a curated list with provider recommendations by default. You can also add custom workspace configurations.             |
| Insights (Summarization) | Model used for lightweight summarization. Choose from a curated list with provider recommendations by default. You can also add custom workspace configurations. |

All features support custom workspace configurations, so you can use any provider or model—even for features that show a curated list by default.

<Note>
  **Insights** uses two separate rows—one for analysis and one for summarization. The UI displays a warning if you select incompatible providers or non-recommended models for either row.
</Note>

### Configure feature access

To configure feature access in the [UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-model-configurations):

1. Navigate to **Settings** > **Model configurations**.
2. In the **Feature Access** table, find the feature you want to configure.
3. Click **Enabled Providers** and toggle providers on or off for that feature.
4. Click **Available Models** and select which models users can choose from.
5. Use the **Default Model** dropdown to set the model preselected when users open the feature.

## Configurations

The **Configurations** table is a shared library of named model configurations for your workspace. Configurations you create in LangSmith (including from the [Playground](/langsmith/managing-model-configurations)) appear here and you can reuse them across all features.

### Create a configuration

1. Navigate to **Settings** > **Model configurations**.
2. Under **Configurations**, click **+ Create**.
3. Select a **Provider** and **Model**.
4. Enter the **API Key Name**—the name of the secret in your workspace that stores the provider API key.
5. Adjust parameters as needed. Parameters are grouped into sections for:

   * **Standard sampling settings**: temperature, top P, top K, presence penalty, frequency penalty, max output tokens
   * **Reasoning**: reasoning effort, service tier
   * **Provider config**: provider API, base URL
   * **Options**: stop sequences, seed, JSON mode, extra headers, requests per second, extra parameters

   Available parameters vary by provider—refer to your provider's documentation for details.
6. Click **Save**.

### Edit a configuration

1. In the **Configurations** table, click the overflow menu <Icon icon="dots-vertical" /> next to the configuration.
2. Select **Edit**.
3. Update the configuration and click **Save**.

### Delete a configuration

1. In the **Configurations** table, click the overflow menu <Icon icon="dots-vertical" /> next to the configuration.
2. Select <Icon icon="trash" /> **Delete** and confirm.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/model-configurations.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Monorepo support
Source: https://docs.langchain.com/langsmith/monorepo-support

LangSmith supports deploying agents from monorepo setups where your agent code may depend on shared packages located elsewhere in the repository. This guide shows how to structure your monorepo and configure your `langgraph.json` file to work with shared dependencies.

## Repository structure

For complete working examples, see:

* [Python monorepo example](https://github.com/langchain-ai/python-langraph-monorepo-example)
* [JS monorepo example](https://github.com/langchain-ai/js-langgraph-monorepo-example)

<CodeGroup>
  ```plaintext Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  my-monorepo/
  ├── shared-utils/           # Shared Python package
  │   ├── __init__.py
  │   ├── common.py
  │   └── pyproject.toml      # Or setup.py
  ├── agents/
  │   └── customer-support/   # Agent directory
  │       ├── agent/
  │       │   ├── __init__.py
  │       │   └── graph.py
  │       ├── langgraph.json  # Config file in agent directory
  │       ├── .env
  │       └── pyproject.toml  # Agent dependencies
  └── other-service/
      └── ...
  ```

  ```plaintext JS theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  my-monorepo/
  ├── package.json            # Root package.json with workspaces
  ├── shared-utils/           # Shared TypeScript package
  │   ├── package.json
  │   ├── src/
  │   │   └── index.ts
  │   └── tsconfig.json
  ├── agents/
  │   └── customer-support/   # Agent directory
  │       ├── src/
  │       │   └── agent.ts
  │       ├── langgraph.json  # Config file in agent directory
  │       ├── package.json    # Agent dependencies
  │       ├── .env
  │       └── tsconfig.json
  └── other-service/
      └── ...
  ```
</CodeGroup>

## LangGraph.json configuration

Place the langgraph.json file in your agent’s directory (not in the monorepo root). Ensure the file follows the required structure:

<CodeGroup>
  ```json Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  {
    "dependencies": [
      ".",                    # Current agent package
      "../../shared-utils"    # Relative path to shared package
    ],
    "graphs": {
      "customer_support": "./agent/graph.py:graph"
    },
    "env": ".env"
  }
  ```

  ```json JS theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  {
    "node_version": "20",
    "graphs": {
      "customer_support": "./src/agent.ts:graph"
    },
    "env": ".env"
  }
  ```
</CodeGroup>

The Python implementation automatically handles packages in parent directories by:

* Detecting relative paths that start with `"."`.
* Adding parent directories to the Docker build context as needed.
* Supporting both real packages (with `pyproject.toml`/`setup.py`) and simple Python modules.

For JavaScript monorepos:

* Shared workspace dependencies are resolved automatically by your package manager.
* Your `package.json` should reference shared packages using workspace syntax.

Example `package.json` in the agent directory:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "name": "customer-support-agent",
  "dependencies": {
    "@company/shared-utils": "workspace:*",
    "@langchain/langgraph": "^0.2.0"
  }
}
```

## Building the application

Run `langgraph build`:

<CodeGroup>
  ```bash Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  cd agents/customer-support
  langgraph build -t my-customer-support-agent
  ```

  ```bash JS theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  # Run from the root of the monorepo
  langgraph build -t my-customer-support-agent -c agents/customer-support/langgraph.json --build-command "yarn run turbo build" --install-command "yarn install"
  ```
</CodeGroup>

The Python build process:

1. Automatically detects relative dependency paths.
2. Copies shared packages into the Docker build context.
3. Installs all dependencies in the correct order.
4. No special flags or commands required.

The JavaScript build process:

1. Uses the directory you called `langgraph build` from (the monorepo root in this case) as the build context.
2. Automatically detects your package manager (yarn, npm, pnpm, bun)
3. Runs the appropriate install command.
   * If you have one or both of a custom build/install command it will run from the directory you called `langgraph build` from.
   * Otherwise, it will run from the directory where the `langgraph.json` file is located.
4. Optionally runs a custom build command from the directory where the `langgraph.json` file is located (only if you pass the `--build-command` flag).

## Tips and best practices

1. **Keep agent configs in agent directories**: Place `langgraph.json` files in the specific agent directories, not at the monorepo root. This allows you to support multiple agents in the same monorepo, without having to deploy them all in the same LangSmith deployment.

2. **Use relative paths for Python**: For Python monorepos, use relative paths like `"../../shared-package"` in the `dependencies` array.

3. **Leverage workspace features for JS**: For JavaScript/TypeScript, use your package manager's workspace features to manage dependencies between packages.

4. **Test locally first**: Always test your build locally before deploying to ensure all dependencies are correctly resolved.

5. **Environment variables**: Keep environment files (`.env`) in your agent directories for environment-specific configuration.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/monorepo-support.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# How to simulate multi-turn interactions
Source: https://docs.langchain.com/langsmith/multi-turn-simulation

AI applications with conversational interfaces, like chatbots, operate over multiple interactions with a user, also called conversation *turns*. When evaluating the performance of such applications, core concepts such as [building a dataset](/langsmith/evaluation-concepts#datasets) and defining [evaluators](/langsmith/evaluation-concepts#evaluators) and metrics to judge your app outputs remain useful. However, you may also find it useful to run a *simulation* between your app and a user, then evaluate this dynamically created trajectory.

Some advantages of doing this are:

* Ease of getting started vs. an evaluation over a full dataset of pre-existing trajectories
* End-to-end coverage from an initial query until a successful or unsuccessful resolution
* The ability to detect repetitive behavior or context loss over several iterations of your app

The downside is that because you are broadening your evaluation surface area to contain multiple turns, there is less consistency than evaluating a single output from your app given a static input from a dataset.

<img alt="Multi turn trace" />

This guide will show you how to simulate multi-turn interactions and evaluate them using the open-source [`openevals`](https://github.com/langchain-ai/openevals) package, which contains prebuilt evaluators and other convenient resources for evaluating your AI apps. It will also use OpenAI models, though you can use other providers as well.

## Setup

First, ensure you have the required dependencies installed:

<CodeGroup>
  ```bash Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install -U langsmith openevals
  ```

  ```bash TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  npm install langsmith openevals
  ```
</CodeGroup>

<Info>
  If you are using `yarn` as your package manager, you will also need to manually install `@langchain/core` as a peer dependency of `openevals`. This is not required for LangSmith evals in general.
</Info>

And set up your environment variables:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
export LANGSMITH_TRACING="true"
export LANGSMITH_API_KEY="<Your LangSmith API key>"
export OPENAI_API_KEY="<Your OpenAI API key>"
```

## Running a simulation

There are two primary components you'll need to get started:

* `app`: Your application, or a function wrapping it. Must accept a single chat message (dict with "role" and "content" keys) as an input arg and a `thread_id` as a kwarg. Should accept other kwargs as more may be added in future releases. Returns a chat message as output with at least role and content keys.
* `user`: The simulated user. In this guide, we will use an imported prebuilt function named `create_llm_simulated_user` which uses an LLM to generate user responses, though you can [create your own too](https://github.com/langchain-ai/openevals?tab=readme-ov-file#custom-simulated-users).

The simulator in `openevals` passes a single chat message to your `app` from the `user` for each turn. Therefore you should statefully track the current history internally based on `thread_id` if needed.

Here's an example that simulates a multi-turn customer support interaction. This guide uses a simple chat app that wraps a single call to the OpenAI chat completions API, however this is where you would call your application or agent. In this example, our simulated user is playing the role of a particularly aggressive customer:

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from openevals.simulators import run_multiturn_simulation, create_llm_simulated_user
  from openevals.types import ChatCompletionMessage
  from langsmith.wrappers import wrap_openai
  from openai import OpenAI

  # Wrap OpenAI client for tracing
  client = wrap_openai(OpenAI())
  history = {}

  # Your application logic
  def app(inputs: ChatCompletionMessage, *, thread_id: str, **kwargs):
      if thread_id not in history:
          history[thread_id] = []
      history[thread_id].append(inputs)
      # inputs is a message object with role and content
      res = client.chat.completions.create(
          model="gpt-5.4-mini",
          messages=[
              {
                  "role": "system",
                  "content": "You are a patient and understanding customer service agent.",
              },
          ] + history[thread_id],
      )
      response_message = res.choices[0].message
      history[thread_id].append(response_message)
      return response_message

  user = create_llm_simulated_user(
      system="You are an aggressive and hostile customer who wants a refund for their car.",
      model="openai:gpt-5.4-mini",
  )

  # Run the simulation directly with the new function
  simulator_result = run_multiturn_simulation(
      app=app,
      user=user,
      max_turns=5,
  )
  print(simulator_result)
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { OpenAI } from "openai";
  import { wrapOpenAI } from "langsmith/wrappers/openai";
  import {
    createLLMSimulatedUser,
    runMultiturnSimulation,
    type ChatCompletionMessage,
  } from "openevals";

  // Wrap OpenAI client for tracing
  const client = wrapOpenAI(new OpenAI());
  const history = {};

  // Your application logic
  const app = async ({ inputs, threadId }: { inputs: ChatCompletionMessage, threadId: string }) => {
    if (history[threadId] === undefined) {
      history[threadId] = [];
    }
    history[threadId].push(inputs);
    const res = await client.chat.completions.create({
      model: "gpt-5.4-mini",
      messages: [
        {
          role: "system",
          content:
            "You are a patient and understanding customer service agent.",
        },
        inputs,
      ],
    });
    const responseMessage = res.choices[0].message;
    history[threadId].push(responseMessage);
    return res.choices[0].message;
  };

  const user = createLLMSimulatedUser({
    system: "You are an aggressive and hostile customer who wants a refund for their car.",
    model: "openai:gpt-5.4-mini",
  });

  const result = await runMultiturnSimulation({
    app,
    user,
    maxTurns: 5,
  });
  console.log(result);
  ```
</CodeGroup>

The response looks like this:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "trajectory": [
    {
      "role": "user",
      "content": "This piece of junk car is a complete disaster! I demand a full refund immediately. How dare you sell me such a worthless vehicle!",
      "id": "chatcmpl-BUpXa07LaM7wXbyaNnng1Gtn5Dsbh"
    },
    {
      "role": "assistant",
      "content": "I'm really sorry to hear about your experience and understand how frustrating this must be. I'd like to help resolve this issue as smoothly as possible. Could you please provide some details about the problem with the vehicle? Once I have more information, I'll do my best to assist you with a solution, whether it's a refund or other options. Thank you for your patience.",
      "refusal": null,
      "annotations": [],
      "id": "d7520f6a-7cf8-46f8-abe4-7df04f134482"
    },
    "...",
    {
      "role": "assistant",
      "content": "I truly understand your frustration and sincerely apologize for the inconvenience you've experienced.\n\nPlease allow me a moment to review your case, and I will do everything I can to expedite your refund. Your patience is greatly appreciated, and I am committed to resolving this matter to your satisfaction.",
      "refusal": null,
      "annotations": [],
      "id": "a0536d4f-9353-4cfa-84df-51c8d29e076d"
    }
  ]
}
```

The simulation first generates an initial query from the simulated `user`, then passes response chat messages back and forth until it reaches `max_turns` (you can alternatively pass a `stopping_condition` that takes the current trajectory and returns `True` or `False` - [see the OpenEvals README for more information](https://github.com/langchain-ai/openevals?tab=readme-ov-file#multiturn-simulation)). The return value is the final list of chat messages that make up the converation's **trajectory**.

<Info>
  There are several ways to configure the simulated user, such as having it return fixed responses for the first turns of your simulation, as well as the simulation as a whole. For full details, check out [the OpenEvals README](https://github.com/langchain-ai/openevals?tab=readme-ov-file#multiturn-simulation).
</Info>

The final trace will look something [like this](https://smith.langchain.com/public/648ca37d-1c4d-4f7b-9b6a-89e35dc5d4f0/r) with responses from your `app` and `user` interleaved:

<img alt="Multi turn trace" />

Congrats! You just ran your first multi-turn simulation. Next, we'll cover how to run it in a LangSmith experiment.

## Running in LangSmith experiments

You can use the results of multi-turn simulations as part of a LangSmith experiment to track performance and progress over time. For these sections, it helps to be familiar with at least one of LangSmith's [`pytest`](/langsmith/pytest) (Python-only), [`Vitest`/`Jest`](/langsmith/vitest-jest) (JS only), or [`evaluate`](/langsmith/evaluate-llm-application) runners.

### Using `pytest` or `Vitest/Jest`

<Check>
  See the following guides to learn how to set up evals using LangSmith's integrations with test frameworks:

  * [`pytest`](https://docs.smith.langchain.com/langsmith/pytest)
  * [`Vitest` or `Jest`](https://docs.smith.langchain.com/langsmith/vitest-jest)
</Check>

If you are using one of the [LangSmith test framework integrations](/langsmith/pytest), you can pass in an array of OpenEvals evaluators as a `trajectory_evaluators` param when running the simulation. These evaluators will run at the end of the simulation, taking the final list of chat messages as an `outputs` kwarg. Your passed `trajectory_evaluator` must therefore accept this kwarg.

<img alt="Multi turn vitest" />

Here's an example:

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from openevals.simulators import run_multiturn_simulation, create_llm_simulated_user
  from openevals.llm import create_llm_as_judge
  from openevals.types import ChatCompletionMessage
  from langsmith import testing as t
  from langsmith.wrappers import wrap_openai
  from openai import OpenAI
  import pytest

  @pytest.mark.langsmith
  def test_multiturn_message_with_openai():
      inputs = {"role": "user", "content": "I want a refund for my car!"}
      t.log_inputs(inputs)
      # Wrap OpenAI client for tracing
      client = wrap_openai(OpenAI())
      history = {}

      def app(inputs: ChatCompletionMessage, *, thread_id: str):
          if thread_id not in history:
              history[thread_id] = []
          history[thread_id] = history[thread_id] + [inputs]
          res = client.chat.completions.create(
              model="gpt-5.4-nano",
              messages=[
                  {
                      "role": "system",
                      "content": "You are a patient and understanding customer service agent.",
                  }
              ]
              + history[thread_id],
          )
          response = res.choices[0].message
          history[thread_id].append(response)
          return response

      user = create_llm_simulated_user(
          system="You are a nice customer who wants a refund for their car.",
          model="openai:gpt-5.4-nano",
          fixed_responses=[
              inputs,
          ],
      )
      trajectory_evaluator = create_llm_as_judge(
          model="openai:o3-mini",
          prompt="Based on the below conversation, was the user satisfied?\n{outputs}",
          feedback_key="satisfaction",
      )
      res = run_multiturn_simulation(
          app=app,
          user=user,
          trajectory_evaluators=[trajectory_evaluator],
          max_turns=5,
      )
      t.log_outputs(res)
      # Optionally, assert that the evaluator scored the interaction as satisfactory.
      # This will cause the overall test case to fail if "score" is False.
      assert res["evaluator_results"][0]["score"]
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { OpenAI } from "openai";
  import { wrapOpenAI } from "langsmith/wrappers/openai";
  import * as ls from "langsmith/vitest";
  import { expect } from "vitest";
  // import * as ls from "langsmith/jest";
  // import { expect } from "@jest/globals";
  import {
    createLLMSimulatedUser,
    runMultiturnSimulation,
    createLLMAsJudge,
    type ChatCompletionMessage,
  } from "openevals";

  const client = wrapOpenAI(new OpenAI());

  ls.describe("Multiturn demo", () => {
    ls.test(
      "Should have a satisfactory interaction with a nice user",
      {
        inputs: {
          messages: [{ role: "user" as const, content: "I want a refund for my car!" }],
        },
      },
      async ({ inputs }) => {
        const history = {};
        // Create a custom app function
        const app = async (
          { inputs, threadId }: { inputs: ChatCompletionMessage, threadId: string }
        ) => {
          if (history[threadId] === undefined) {
            history[threadId] = [];
          }
          history[threadId].push(inputs);
          const res = await client.chat.completions.create({
            model: "gpt-5.4-nano",
            messages: [
              {
                role: "system",
                content:
                  "You are a patient and understanding customer service agent",
              },
              inputs,
            ],
          });
          const responseMessage = res.choices[0].message;
          history[threadId].push(responseMessage);
          return responseMessage;
        };

        const user = createLLMSimulatedUser({
          system:
            "You are a nice customer who wants a refund for their car.",
          model: "openai:gpt-5.4-nano",
          fixedResponses: inputs.messages,
        });

        const trajectoryEvaluator = createLLMAsJudge({
          model: "openai:o3-mini",
          prompt:
            "Based on the below conversation, was the user satisfied?\n{outputs}",
          feedbackKey: "satisfaction",
        });

        const result = await runMultiturnSimulation({
          app,
          user,
          trajectoryEvaluators: [trajectoryEvaluator],
          maxTurns: 5,
        });

        ls.logOutputs(result);
        // Optionally, assert that the evaluator scored the interaction as satisfactory.
        // This will cause the overall test case to fail if "score" is false.
        expect(result.evaluatorResults[0].score).toBe(true);
      }
    );
  });
  ```
</CodeGroup>

LangSmith will automatically detect and log the feedback returned from the passed `trajectory_evaluators`, adding it to the experiment. Note also that the test case uses the `fixed_responses` param on the simulated user to start the conversation with a specific input, which you can log and make part of your stored dataset.

You may also find it convenient to have the simulated user's system prompt be part of your logged dataset.

### Using `evaluate`

You can also use the [`evaluate`](/langsmith/evaluate-llm-application) runner to evaluate simulated multi-turn interactions. This will be a little bit different from the `pytest`/`Vitest`/`Jest` example in the following ways:

* The simulation should be part of your `target` function, and your target function should return the final trajectory.
  * This will make the trajectory the `outputs` that LangSmith will pass to your evaluators.
* Instead of using the `trajectory_evaluators` param, you should pass your evaluators as a param into the `evaluate()` method.
* You will need an existing dataset of inputs and (optionally) reference trajectories.

Here's an example:

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from openevals.simulators import run_multiturn_simulation, create_llm_simulated_user
  from openevals.llm import create_llm_as_judge
  from openevals.types import ChatCompletionMessage
  from langsmith.wrappers import wrap_openai
  from langsmith import Client
  from openai import OpenAI

  ls_client = Client()
  examples = [
      {
          "inputs": {
              "messages": [{ "role": "user", "content": "I want a refund for my car!" }]
          },
      },
  ]
  dataset = ls_client.create_dataset(dataset_name="multiturn-starter")
  ls_client.create_examples(
      dataset_id=dataset.id,
      examples=examples,
  )
  trajectory_evaluator = create_llm_as_judge(
      model="openai:o3-mini",
      prompt="Based on the below conversation, was the user satisfied?\n{outputs}",
      feedback_key="satisfaction",
  )

  def target(inputs: dict):
      # Wrap OpenAI client for tracing
      client = wrap_openai(OpenAI())
      history = {}

      def app(next_message: ChatCompletionMessage, *, thread_id: str):
          if thread_id not in history:
              history[thread_id] = []
          history[thread_id] = history[thread_id] + [next_message]
          res = client.chat.completions.create(
              model="gpt-5.4-nano",
              messages=[
                  {
                      "role": "system",
                      "content": "You are a patient and understanding customer service agent.",
                  }
              ]
              + history[thread_id],
          )
          response = res.choices[0].message
          history[thread_id].append(response)
          return response

      user = create_llm_simulated_user(
          system="You are a nice customer who wants a refund for their car.",
          model="openai:gpt-5.4-nano",
          fixed_responses=inputs["messages"],
      )
      res = run_multiturn_simulation(
          app=app,
          user=user,
          max_turns=5,
      )
      return res["trajectory"]

  results = ls_client.evaluate(
      target,
      data=dataset.name,
      evaluators=[trajectory_evaluator],
  )
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { OpenAI } from "openai";
  import { Client } from "langsmith";
  import { wrapOpenAI } from "langsmith/wrappers/openai";
  import { evaluate } from "langsmith/evaluation";
  import {
    createLLMSimulatedUser,
    runMultiturnSimulation,
    createLLMAsJudge,
    type ChatCompletionMessage,
  } from "openevals";

  const lsClient = new Client();
  const inputs = {
    messages: [
      {
        role: "user",
        content: "I want a refund for my car!",
      },
    ],
  };
  const datasetName = "Multiturn";
  const dataset = await lsClient.createDataset(datasetName);
  await lsClient.createExamples([{ inputs, dataset_id: dataset.id }]);

  const trajectoryEvaluator = createLLMAsJudge({
    model: "openai:o3-mini",
    prompt:
      "Based on the below conversation, was the user satisfied?\n{outputs}",
    feedbackKey: "satisfaction",
  });

  const client = wrapOpenAI(new OpenAI());

  const target = async (inputs: { messages: ChatCompletionMessage[]}) => {
    const history = {};
    // Create a custom app function
    const app = async (
      { inputs: nextMessage, threadId }: { inputs: ChatCompletionMessage, threadId: string }
    ) => {
      if (history[threadId] === undefined) {
        history[threadId] = [];
      }
      history[threadId].push(nextMessage);
      const res = await client.chat.completions.create({
        model: "gpt-5.4-nano",
        messages: [
          {
            role: "system",
            content:
              "You are a patient and understanding customer service agent",
          },
          nextMessage,
        ],
      });
      const responseMessage = res.choices[0].message;
      history[threadId].push(responseMessage);
      return responseMessage;
    };

    const user = createLLMSimulatedUser({
      system:
        "You are a nice customer who wants a refund for their car.",
      model: "openai:gpt-5.4-nano",
      fixedResponses: inputs.messages,
    });

    const result = await runMultiturnSimulation({
      app,
      user,
      maxTurns: 5,
    });
    return result.trajectory;
  };

  await evaluate(target, {
    data: datasetName,
    evaluators: [trajectoryEvaluator],
  });
  ```
</CodeGroup>

## Modifying the simulated user persona

The above examples run using the same simulated user persona for all input examples, defined by the `system` parameter passed into `create_llm_simulated_user`. If you would like to use a different persona for specific items in your dataset, you can update your dataset examples to also contain an extra field with the desired `system` prompt, then pass that field in when creating your simulated user like this:

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from openevals.simulators import run_multiturn_simulation, create_llm_simulated_user
  from openevals.llm import create_llm_as_judge
  from openevals.types import ChatCompletionMessage
  from langsmith.wrappers import wrap_openai
  from langsmith import Client
  from openai import OpenAI

  ls_client = Client()
  examples = [
      {
          "inputs": {
              "messages": [{ "role": "user", "content": "I want a refund for my car!" }],
              "simulated_user_prompt": "You are an angry and belligerent customer who wants a refund for their car."
          },
      },
      {
          "inputs": {
              "messages": [{ "role": "user", "content": "Please give me a refund for my car." }],
              "simulated_user_prompt": "You are a nice customer who wants a refund for their car.",
          },
      }
  ]
  dataset = ls_client.create_dataset(dataset_name="multiturn-with-personas")
  ls_client.create_examples(
      dataset_id=dataset.id,
      examples=examples,
  )
  trajectory_evaluator = create_llm_as_judge(
      model="openai:o3-mini",
      prompt="Based on the below conversation, was the user satisfied?\n{outputs}",
      feedback_key="satisfaction",
  )

  def target(inputs: dict):
      # Wrap OpenAI client for tracing
      client = wrap_openai(OpenAI())
      history = {}

      def app(next_message: ChatCompletionMessage, *, thread_id: str):
          if thread_id not in history:
              history[thread_id] = []
          history[thread_id] = history[thread_id] + [next_message]
          res = client.chat.completions.create(
              model="gpt-5.4-nano",
              messages=[
                  {
                      "role": "system",
                      "content": "You are a patient and understanding customer service agent.",
                  }
              ]
              + history[thread_id],
          )
          response = res.choices[0].message
          history[thread_id].append(response)
          return response

      user = create_llm_simulated_user(
          system=inputs["simulated_user_prompt"],
          model="openai:gpt-5.4-nano",
          fixed_responses=inputs["messages"],
      )
      res = run_multiturn_simulation(
          app=app,
          user=user,
          max_turns=5,
      )
      return res["trajectory"]

  results = ls_client.evaluate(
      target,
      data=dataset.name,
      evaluators=[trajectory_evaluator],
  )
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { OpenAI } from "openai";
  import { Client } from "langsmith";
  import { wrapOpenAI } from "langsmith/wrappers/openai";
  import { evaluate } from "langsmith/evaluation";
  import {
    createLLMSimulatedUser,
    runMultiturnSimulation,
    createLLMAsJudge,
    type ChatCompletionMessage,
  } from "openevals";

  const lsClient = new Client();
  const datasetName = "Multiturn with personas";
  const dataset = await lsClient.createDataset(datasetName);
  const examples = [{
    inputs: {
      messages: [
        {
          role: "user",
          content: "I want a refund for my car!",
        },
      ],
      simulated_user_prompt: "You are an angry and belligerent customer who wants a refund for their car.",
    },
    dataset_id: dataset.id,
  }, {
    inputs: {
      messages: [
        {
          role: "user",
          content: "Please give me a refund for my car."
        }
      ],
      simulated_user_prompt: "You are a nice customer who wants a refund for their car.",
    },
    dataset_id: dataset.id,
  }];
  await lsClient.createExamples(examples);

  const trajectoryEvaluator = createLLMAsJudge({
    model: "openai:o3-mini",
    prompt:
      "Based on the below conversation, was the user satisfied?\n{outputs}",
    feedbackKey: "satisfaction",
  });

  const client = wrapOpenAI(new OpenAI());

  const target = async (inputs: {
    messages: ChatCompletionMessage[],
    simulated_user_prompt: string,
  }) => {
    const history = {};
    // Create a custom app function
    const app = async (
      { inputs: nextMessage, threadId }: { inputs: ChatCompletionMessage, threadId: string }
    ) => {
      if (history[threadId] === undefined) {
        history[threadId] = [];
      }
      history[threadId].push(nextMessage);
      const res = await client.chat.completions.create({
        model: "gpt-5.4-nano",
        messages: [
          {
            role: "system",
            content:
              "You are a patient and understanding customer service agent",
          },
          nextMessage,
        ],
      });
      const responseMessage = res.choices[0].message;
      history[threadId].push(responseMessage);
      return responseMessage;
    };

    const user = createLLMSimulatedUser({
      system: inputs.simulated_user_prompt,
      model: "openai:gpt-5.4-nano",
      fixedResponses: inputs.messages,
    });

    const result = await runMultiturnSimulation({
      app,
      user,
      maxTurns: 5,
    });
    return result.trajectory;
  };

  await evaluate(target, {
    data: datasetName,
    evaluators: [trajectoryEvaluator],
  });
  ```
</CodeGroup>

## Next steps

You've just seen some techniques for simulating multi-turn interactions and running them in LangSmith evals.

Here are some topics you might want to explore next:

* [Trace multiturn conversations across different traces](/langsmith/threads)
* [Use multiple messages in the playground UI](/langsmith/multiple-messages)
* [Return multiple metrics in one evaluator](/langsmith/multiple-scores)

You can also explore the [OpenEvals readme](https://github.com/langchain-ai/openevals) for more on prebuilt evaluators.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/multi-turn-simulation.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Include multimodal content in a prompt
Source: https://docs.langchain.com/langsmith/multimodal-content

Some applications are based around multimodal content, like a chatbot that can answer questions about a PDF or image. In these cases, you'll want to include multimodal content in your prompt and test the model's ability to answer questions about the content.

The Playground supports two methods for incorporating multimodal content in your prompts:

1. Inline content: Embed static files (images, PDFs, audio) directly in your prompt. This is ideal when you want to consistently include the same multimodal content across all uses of the prompt. For example, you might include a reference image that helps ground the model's responses.

2. Template variables: Create dynamic placeholders for attachments that can be populated with different content each time. This approach offers more flexibility, allowing you to:

   * Test how the model handles different inputs
   * Create reusable prompts that work with varying content

<Note>
  Not all models support multimodal content. Before using multimodal features in the Playground, make sure your selected model supports the file types you want to use.
</Note>

## Inline content

Click the file icon in the message where you want to add multimodal content. Under the `Upload content` tab, you can upload a file and include it inline in the prompt.

<img alt="Upload inline multimodal content" />

## Template variables

Click the file icon in the message where you want to add multimodal content. Under the `Template variables` tab, you can create a template variable for a specific attachment type. Currently, only images, PDFs, and audio files (.wav, .mp3) are supported.

<img alt="Template variable multimodal content" />

## Populate the template variable

Once you've added a template variable, you can provide content for it using the panel on the right side of the screen. Simply click the `+` button to upload or select content that will be used to populate the template variable.

<img alt="Manual prompt multimodal" />

## Run an evaluation

After testing out your prompt manually, you can [run an evaluation](/langsmith/evaluate-with-attachments?mode=ui) to see how the prompt performs over a golden dataset of examples.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/multimodal-content.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Test multi-turn conversations
Source: https://docs.langchain.com/langsmith/multiple-messages

This how-to guide walks you through the various ways you can set up the Playground for multi-turn conversations, which will allow you to test different tool configurations and system prompts against longer threads of messages.

<img alt="Multiturn diagram" />

## From an existing run

First, ensure you have properly [traced](/langsmith/observability) a multi-turn conversation, and then navigate to your tracing project. Once you get to your tracing project simply open the run, select the LLM call, and open it in the Playground as follows:

<img alt="Multiturn from run" />

You can then edit the system prompt, tweak the tools and/or output schema and observe how the output of the multi-turn conversation changes.

## From a dataset

Before starting, make sure you have [set up your dataset](/langsmith/manage-datasets-in-application). Since you want to evaluate multi-turn conversations, make sure there is a key in your inputs that contains a list of messages.

Once you have created your dataset, head to the Playground and [load your dataset](/langsmith/manage-datasets-in-application#from-the-playground) to evaluate.

Then, add a messages list variable to your prompt, making sure to name it the same as the key in your inputs that contains the list of messages:

<img alt="Multiturn from dataset" />

When you run your prompt, the messages from each example will be added as a list in place of the 'Messages List' variable.

## Manually

There are two ways to manually create multi-turn conversations. The first way is by simply appending messages to the prompt:

<img alt="Multiturn manual" />

This is helpful for quick iteration, but is rigid since the multi-turn conversation is hardcoded. Instead, if you want your prompt to work with any multi-turn conversation you can add a 'Messages List' variable and add your multi-turn conversation there:

<img alt="Multiturn manual list" />

This allows you to just tweak the system prompt or the tools, while allowing any multi-turn conversation to take the place of the `Messages List` variable, allowing you to reuse this prompt across various runs.

## Next steps

Now that you know how to set up the Playground for multi-turn interactions, you can either manually inspect and judge the outputs, or you can [add evaluators](/langsmith/code-evaluator-ui) to classify results.

You can also read [these how-to guides](/langsmith/create-a-prompt) to learn more about how to use the Playground to run evaluations.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/multiple-messages.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
