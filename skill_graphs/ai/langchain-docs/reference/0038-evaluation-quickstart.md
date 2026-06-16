# Evaluation quickstart
Source: https://docs.langchain.com/langsmith/evaluation-quickstart

[*Evaluations*](/langsmith/evaluation-concepts) are a quantitative way to measure the performance of LLM applications. LLMs can behave unpredictably, even small changes to prompts, models, or inputs can significantly affect results. Evaluations provide a structured way to identify failures, compare versions, and build more reliable AI applications.

Running an evaluation in LangSmith requires three key components:

* [*Dataset*](/langsmith/evaluation-concepts#datasets): A set of test inputs (and optionally, expected outputs).
* [*Target function*](/langsmith/define-target-function): The part of your application you want to test—this might be a single LLM call with a new prompt, one module, or your entire workflow.
* [*Evaluators*](/langsmith/evaluation-concepts#evaluators): Functions that score your target function’s outputs.

This quickstart guides you through running a starter evaluation that checks the correctness of LLM responses, using either the LangSmith SDK or UI.

## Prerequisites

Before you begin, make sure you have:

* **A LangSmith account**: Sign up or log in at [smith.langchain.com](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-evaluation-quickstart).
* **A LangSmith API key**: Follow the [Create an API key](/langsmith/create-account-api-key) guide.
* **An OpenAI API key**: Generate this from the [OpenAI dashboard](https://platform.openai.com/account/api-keys).

**Select the UI or SDK filter for instructions:**

<Tabs>
  <Tab title="UI" icon="window">
    ## 1. Set workspace secrets

    In the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=snippets-langsmith-set-workspace-secrets), ensure that your API key is set as a [workspace secret](/langsmith/set-up-hierarchy#configure-workspace-settings).

    1. Navigate to <Icon icon="settings" /> **Settings** and then move to the **Secrets** tab.
    2. Select **Add secret** and enter the key environment variable (e.g.,`OPENAI_API_KEY` or `ANTHROPIC_API_KEY`) and your API key as the **Value**.
    3. Select **Save secret**.

    <Note> When adding workspace secrets in the LangSmith UI, make sure the secret keys match the environment variable names expected by your model provider.</Note>

    ## 2. Create a prompt

    The [Playground](/langsmith/prompt-engineering-concepts#playground) makes it possible to run evaluations over different prompts, new models, or test different model configurations.

    1. In the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-evaluation-quickstart), click **Playground** in the sidebar.
    2. Under the **Prompts** panel, modify the **system** prompt to:

       ```
       Answer the following question accurately:
       ```

       Leave the **Human** message as is: `{question}`.

    ## 3. Create a dataset

    1. Click **Set up Evaluation**, which will open a **New Experiment** table at the bottom of the page.

    2. In the **Select or create a new dataset** dropdown, click the **+ New** button to create a new dataset.

       <div>
         <img alt="Playground with the edited system prompt and new experiment with the dropdown for creating a new dataset." />

         <img alt="Playground with the edited system prompt and new experiment with the dropdown for creating a new dataset." />
       </div>

    3. Add the following examples to the dataset:

       | Inputs                                                   | Reference Outputs                                 |
       | -------------------------------------------------------- | ------------------------------------------------- |
       | question: Which country is Mount Kilimanjaro located in? | output: Mount Kilimanjaro is located in Tanzania. |
       | question: What is Earth's lowest point?                  | output: Earth's lowest point is The Dead Sea.     |

    4. Click **Save** and enter a name to save your newly created dataset.

    ## 4. Add an evaluator

    1. Click **+ Evaluator** and select **Correctness** from the **Prebuilt Evaluator** options.
    2. In the **Correctness** panel, click **Save**.

    ## 5. Run your evaluation

    1. Select <Icon icon="player-play" /> **Start** on the top right to run your evaluation. This will create an [*experiment*](/langsmith/evaluation-concepts#experiment) with a preview in the **New Experiment** table. You can view in full by clicking the experiment name.

       <div>
         <img alt="Full experiment view of the results that used the example dataset." />

         <img alt="Full experiment view of the results that used the example dataset." />
       </div>

    ## Next steps

    <Tip>
      To learn more about running experiments in LangSmith, read the [evaluation conceptual guide](/langsmith/evaluation-concepts).
    </Tip>

    * For more details on evaluations, refer to the [Evaluation documentation](/langsmith/evaluation).
    * Learn how to [create and manage datasets in the UI](/langsmith/manage-datasets-in-application#create-a-dataset-and-add-examples).
    * Learn how to [run an evaluation from the Playground](/langsmith/run-evaluation-from-playground).
  </Tab>

  <Tab title="SDK" icon="code">
    <Tip>
      This guide uses prebuilt LLM-as-judge evaluators from the open-source [`openevals`](https://github.com/langchain-ai/openevals) package. OpenEvals includes a set of commonly used evaluators and is a great starting point if you're new to evaluations. If you want greater flexibility in how you evaluate your apps, you can also [define completely custom evaluators](/langsmith/code-evaluator-ui).
    </Tip>

    ## 1. Install dependencies

    In your terminal, create a directory for your project and install the dependencies in your environment:

    <CodeGroup>
      ```bash Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      mkdir ls-evaluation-quickstart && cd ls-evaluation-quickstart
      python -m venv .venv && source .venv/bin/activate
      python -m pip install --upgrade pip
      pip install -U langsmith openevals openai
      ```

      ```bash TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      mkdir ls-evaluation-quickstart-ts && cd ls-evaluation-quickstart-ts
      npm init -y
      npm install langsmith openevals openai
      npx tsc --init
      ```
    </CodeGroup>

    <Info>
      If you are using `yarn` as your package manager, you will also need to manually install `@langchain/core` as a peer dependency of `openevals`. This is not required for LangSmith evals in general, you may define evaluators [using arbitrary custom code](/langsmith/code-evaluator-ui).
    </Info>

    ## 2. Set up environment variables

    Set the following environment variables:

    * `LANGSMITH_TRACING`
    * `LANGSMITH_API_KEY`
    * `OPENAI_API_KEY` (or your LLM provider's API key)
    * (optional) `LANGSMITH_WORKSPACE_ID`: If your LangSmith API key is linked to multiple [workspaces](/langsmith/administration-overview#workspaces), set this variable to specify which workspace to use.

    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    export LANGSMITH_TRACING=true
    export LANGSMITH_API_KEY="<your-langsmith-api-key>"
    export OPENAI_API_KEY="<your-openai-api-key>"
    export LANGSMITH_WORKSPACE_ID="<your-workspace-id>"
    ```

    <Note>
      If you're using Anthropic, use the [Anthropic wrapper](/langsmith/trace-anthropic) to trace your calls. For other providers, use [the traceable wrapper](/langsmith/annotate-code#use-%40traceable-%2F-traceable).
    </Note>

    ## 3. Create a dataset

    1. Create a file and add the following code, which will:

       * Import the `Client` to connect to LangSmith.
       * Create a dataset.
       * Define example [*inputs* and *outputs*](/langsmith/evaluation-concepts#examples).
       * Associate the input and output pairs with that dataset in LangSmith so they can be used in evaluations.

       <CodeGroup>
         ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
         # dataset.py
         from langsmith import Client

         def main():
             client = Client()

             # Programmatically create a dataset in LangSmith
             dataset = client.create_dataset(
                 dataset_name="Sample dataset",
                 description="A sample dataset in LangSmith."
             )

             # Create examples
             examples = [
                 {
                     "inputs": {"question": "Which country is Mount Kilimanjaro located in?"},
                     "outputs": {"answer": "Mount Kilimanjaro is located in Tanzania."},
                 },
                 {
                     "inputs": {"question": "What is Earth's lowest point?"},
                     "outputs": {"answer": "Earth's lowest point is The Dead Sea."},
                 },
             ]

             # Add examples to the dataset
             client.create_examples(dataset_id=dataset.id, examples=examples)
             print("Created dataset:", dataset.name)

         if __name__ == "__main__":
             main()

         ```

         ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
         // dataset.ts
         import { Client } from "langsmith";

         async function main() {
         const client = new Client();

         const dataset = await client.createDataset(
             "Sample dataset",
             { description: "A sample dataset in LangSmith." }
         );

         // Define examples
         const inputs = [
             { question: "Which country is Mount Kilimanjaro located in?" },
             { question: "What is Earth's lowest point?" },
         ];
         const outputs = [
             { answer: "Mount Kilimanjaro is located in Tanzania." },
             { answer: "Earth's lowest point is The Dead Sea." },
         ];

         await client.createExamples({
             datasetId: dataset.id,
             inputs,
             outputs,
         });

         console.log("Created dataset:", dataset.name);
         }

         if (require.main === module) {
         main().catch((e) => {
             console.error(e);
             process.exit(1);
         });
         }
         ```
       </CodeGroup>

    2. In your terminal, run the `dataset` file to create the datasets you'll use to evaluate your app:

       <CodeGroup>
         ```bash Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
         python dataset.py
         ```

         ```bash TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
         npx ts-node dataset.ts
         ```
       </CodeGroup>

       You'll see the following output:

       ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
       Created dataset: Sample dataset
       ```

    ## 4. Create your target function

    Define a [target function](/langsmith/define-target-function) that contains what you're evaluating. In this guide, you'll define a target function that contains a single LLM call to answer a question.

    Add the following to an `eval` file:

    <CodeGroup>
      ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      # eval.py
      from langsmith import Client, wrappers
      from openai import OpenAI

      # Wrap the OpenAI client for LangSmith tracing
      openai_client = wrappers.wrap_openai(OpenAI())

      # Define the application logic you want to evaluate inside a target function
      # The SDK will automatically send the inputs from the dataset to your target function
      def target(inputs: dict) -> dict:
          response = openai_client.chat.completions.create(
              model="gpt-5-mini",
              messages=[
                  {"role": "system", "content": "Answer the following question accurately"},
                  {"role": "user", "content": inputs["question"]},
              ],
          )
          return {"answer": response.choices[0].message.content.strip()}
      ```

      ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      // eval.ts
      import { evaluate } from "langsmith/evaluation";
      import { wrapOpenAI } from "langsmith/wrappers/openai";
      import OpenAI from "openai";

      const openaiClient = wrapOpenAI(new OpenAI());

      async function target(inputs: Record<string, any>): Promise<Record<string, any>> {
        const question = String(inputs.question ?? "");
        const resp = await openaiClient.chat.completions.create({
          model: "gpt-5-mini",
          messages: [
            { role: "system", content: "Answer the following question accurately" },
            { role: "user", content: question },
          ],
        });
        return { answer: resp.choices[0].message.content?.trim() ?? "" };
      }
      ```
    </CodeGroup>

    ## 5. Define an evaluator

    In this step, you’re telling LangSmith how to grade the answers your app produces.

    Import a prebuilt evaluation prompt (`CORRECTNESS_PROMPT`) from [`openevals`](https://github.com/langchain-ai/openevals) and a helper that wraps it into an [*LLM-as-judge evaluator*](/langsmith/evaluation-concepts#llm-as-judge), which will score the application's output.

    <Info>
      `CORRECTNESS_PROMPT` is just an f-string with variables for `"inputs"`, `"outputs"`, and `"reference_outputs"`. See [customizing OpenEvals prompts](https://github.com/langchain-ai/openevals#customizing-prompts) for more information.
    </Info>

    The evaluator compares:

    * `inputs`: what was passed into your target function (e.g., the question text).
    * `outputs`: what your target function returned (e.g., the model’s answer).
    * `reference_outputs`: the ground truth answers you attached to each dataset example in [Step 3](#3-create-a-dataset).

    Add the following highlighted code to your `eval` file:

    <CodeGroup>
      ```python Python highlight={3,4,21-31} theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from langsmith import Client, wrappers
      from openai import OpenAI
      from openevals.llm import create_llm_as_judge
      from openevals.prompts import CORRECTNESS_PROMPT

      # Wrap the OpenAI client for LangSmith tracing
      openai_client = wrappers.wrap_openai(OpenAI())

      # Define the application logic you want to evaluate inside a target function
      # The SDK will automatically send the inputs from the dataset to your target function
      def target(inputs: dict) -> dict:
          response = openai_client.chat.completions.create(
              model="gpt-5-mini",
              messages=[
                  {"role": "system", "content": "Answer the following question accurately"},
                  {"role": "user", "content": inputs["question"]},
              ],
          )
          return {"answer": response.choices[0].message.content.strip()}

      def correctness_evaluator(inputs: dict, outputs: dict, reference_outputs: dict):
          evaluator = create_llm_as_judge(
              prompt=CORRECTNESS_PROMPT,
              model="openai:o3-mini",
              feedback_key="correctness",
          )
          return evaluator(
              inputs=inputs,
              outputs=outputs,
              reference_outputs=reference_outputs
          )
      ```

      ```typescript TypeScript highlight={4,20-37} theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { evaluate } from "langsmith/evaluation";
      import { wrapOpenAI } from "langsmith/wrappers/openai";
      import OpenAI from "openai";
      import { createLLMAsJudge, CORRECTNESS_PROMPT } from "openevals";

      const openaiClient = wrapOpenAI(new OpenAI());

      async function target(inputs: Record<string, any>): Promise<Record<string, any>> {
        const question = String(inputs.question ?? "");
        const resp = await openaiClient.chat.completions.create({
          model: "gpt-5-mini",
          messages: [
            { role: "system", content: "Answer the following question accurately" },
            { role: "user", content: question },
          ],
        });
        return { answer: resp.choices[0].message.content?.trim() ?? "" };
      }

      const judge = createLLMAsJudge({
        prompt: CORRECTNESS_PROMPT,
        model: "openai:o3-mini",
        feedbackKey: "correctness",
      });

      async function correctnessEvaluator(run: {
        inputs: Record<string, any>;
        outputs: Record<string, any>;
        referenceOutputs?: Record<string, any>;
      }) {
        return judge({
          inputs: run.inputs,
          outputs: run.outputs,
          // OpenEvals expects snake_case here:
          reference_outputs: run.referenceOutputs,
        });
      }
      ```
    </CodeGroup>

    ## 6. Run and view results

    To run the evaluation experiment, you'll call `evaluate(...)`, which:

    * Pulls example from the dataset you created in [Step 3](#3-create-a-dataset).
    * Sends each example's inputs to your target function from [Step 4](#4-add-an-evaluator).
    * Collects the outputs (the model's answers).
    * Passes the outputs along with the `reference_outputs` to your evaluator from [Step 5](#5-define-an-evaluator).
    * Records all results in LangSmith as an experiment, so you can view them in the UI.

    1. Add the highlighted code to your `eval` file:

       <CodeGroup>
         ```python Python highlight={33-49} theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
         from langsmith import Client, wrappers
         from openai import OpenAI
         from openevals.llm import create_llm_as_judge
         from openevals.prompts import CORRECTNESS_PROMPT

         # Wrap the OpenAI client for LangSmith tracing
         openai_client = wrappers.wrap_openai(OpenAI())

         # Define the application logic you want to evaluate inside a target function
         # The SDK will automatically send the inputs from the dataset to your target function
         def target(inputs: dict) -> dict:
             response = openai_client.chat.completions.create(
                 model="gpt-5-mini",
                 messages=[
                     {"role": "system", "content": "Answer the following question accurately"},
                     {"role": "user", "content": inputs["question"]},
                 ],
             )
             return {"answer": response.choices[0].message.content.strip()}

         def correctness_evaluator(inputs: dict, outputs: dict, reference_outputs: dict):
             evaluator = create_llm_as_judge(
                 prompt=CORRECTNESS_PROMPT,
                 model="openai:o3-mini",
                 feedback_key="correctness",
             )
             return evaluator(
                 inputs=inputs,
                 outputs=outputs,
                 reference_outputs=reference_outputs
             )

         # After running the evaluation, a link will be provided to view the results in langsmith
         def main():
             client = Client()
             experiment_results = client.evaluate(
                 target,
                 data="Sample dataset",
                 evaluators=[
                     correctness_evaluator,
                     # can add multiple evaluators here
                 ],
                 experiment_prefix="first-eval-in-langsmith",
                 max_concurrency=2,
             )
             print(experiment_results)

         if __name__ == "__main__":
             main()
         ```

         ```typescript TypeScript highlight={39-57} theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
         import { evaluate } from "langsmith/evaluation";
         import { wrapOpenAI } from "langsmith/wrappers/openai";   // helper to wrap OpenAI client
         import OpenAI from "openai";                              // model provider
         import { createLLMAsJudge, CORRECTNESS_PROMPT } from "openevals"; // evaluator tools

         const openaiClient = wrapOpenAI(new OpenAI());

         async function target(inputs: Record<string, any>): Promise<Record<string, any>> {
         const question = String(inputs.question ?? "");
         const resp = await openaiClient.chat.completions.create({
             model: "gpt-5-mini",
             messages: [
             { role: "system", content: "Answer the following question accurately" },
             { role: "user", content: question },
             ],
         });
         return { answer: resp.choices[0].message.content?.trim() ?? "" };
         }

         const judge = createLLMAsJudge({
         prompt: CORRECTNESS_PROMPT,
         model: "openai:o3-mini",
         feedbackKey: "correctness",
         });

         async function correctnessEvaluator(run: {
         inputs: Record<string, any>;
         outputs: Record<string, any>;
         referenceOutputs?: Record<string, any>;
         }) {
         return judge({
             inputs: run.inputs,
             outputs: run.outputs,
             // OpenEvals expects snake_case here:
             reference_outputs: run.referenceOutputs,
         });
         }

         async function main() {
         const datasetName = process.env.DATASET_NAME ?? "Sample dataset";

         const results = await evaluate(target, {
             data: datasetName,
             evaluators: [correctnessEvaluator],
             experimentPrefix: "first-eval-in-langsmith",
             maxConcurrency: 2,
         });

         console.log(results);
         }

         if (require.main === module) {
         main().catch((e) => {
             console.error(e);
             process.exit(1);
         });
         }
         ```
       </CodeGroup>

    2. Run your evaluator:

       <CodeGroup>
         ```bash Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
         python eval.py
         ```

         ```bash TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
         npx ts-node eval.ts
         ```
       </CodeGroup>

    3. You'll receive a link to view the evaluation results and metadata for the experiment results:

       ```
       View the evaluation results for experiment: 'first-eval-in-langsmith-00000000' at: https://smith.langchain.com/o/6551f9c4-2685-4a08-86b9-1b29643deb3d/datasets/e5fde557-c274-4e49-b39d-000000000000/compare?selectedSessions=70b11778-6a28-4cdb-be81-000000000000

       <ExperimentResults first-eval-in-langsmith-00000000>
       ```

    4. Follow the link in the output of your evaluation run to access the **Datasets & Experiments** page in the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-evaluation-quickstart), and explore the results of the experiment. This will direct you to the created experiment with a table showing the **Inputs**, **Reference Output**, and **Outputs**. You can select a dataset to open an expanded view of the results.

       <div>
         <img alt="Experiment results in the UI after following the link." />

         <img alt="Experiment results in the UI after following the link." />
       </div>

    ## Next steps

    Here are some topics you might want to explore next:

    * [Evaluation concepts](/langsmith/evaluation-concepts) provides descriptions of the key terminology for evaluations in LangSmith.
    * [OpenEvals README](https://github.com/langchain-ai/openevals) to see all available prebuilt evaluators and how to customize them.
    * [Define custom evaluators](/langsmith/code-evaluator-ui).
    * [Python](https://docs.smith.langchain.com/reference/python/reference) or [TypeScript](https://docs.smith.langchain.com/reference/js) SDK references for comprehensive descriptions of every class and function.
  </Tab>
</Tabs>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/evaluation-quickstart.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Evaluation types
Source: https://docs.langchain.com/langsmith/evaluation-types

This page covers two aspects of evaluation in LangSmith:

1. **[Evaluation types](#offline-evaluation-types)**: *When and why* to evaluate. Offline evaluation types (benchmarking, unit tests, regression tests) for pre-deployment testing, and online evaluation types (monitoring, anomaly detection) for production.
2. **[Evaluator implementations](#implement-evaluators)**: *How* to evaluate. The available evaluator approaches (LLM-as-judge, code, composite, summary, pairwise) and where to configure them (UI or SDK, offline or online).

Understanding both aspects helps you build a comprehensive evaluation strategy that validates functionality before deployment and monitors quality in production.

## Offline evaluation types

Offline evaluation tests applications on curated datasets before deployment. By running evaluations on examples with reference outputs, teams can compare versions, validate functionality, and build confidence before exposing changes to users.

Run offline evaluations client-side using the LangSmith SDK ([Python](https://reference.langchain.com/python/langsmith/observability/sdk/) or [TypeScript](https://reference.langchain.com/javascript/modules/langsmith.html)) or server-side via the [Playground](/langsmith/prompt-engineering-concepts#playground) or by [binding evaluators to a dataset](/langsmith/bind-evaluator-to-dataset).

<img alt="Offline" />

### Benchmarking

*Benchmarking* compares multiple application versions on a curated dataset to identify the best performer. This process involves creating a dataset of representative inputs, defining performance metrics, and testing each version.

Benchmarking requires dataset curation with gold-standard reference outputs and well-designed comparison metrics. Examples:

* **RAG Q\&A bot**: Dataset of questions and reference answers, with an LLM-as-judge evaluator checking semantic equivalence between actual and reference answers.
* **ReACT agent**: Dataset of user requests and reference tool calls, with a heuristic evaluator verifying all expected tool calls were made.

### Unit tests

*Unit tests* verify the correctness of individual system components. In LLM contexts, [unit tests are often rule-based assertions](https://hamel.dev/blog/posts/evals/#level-1-unit-tests) on inputs or outputs (e.g., verifying LLM-generated code compiles, JSON loads successfully) that validate basic functionality.

Unit tests typically expect consistent passing results, making them suitable for CI pipelines. When running in CI, configure caching to minimize LLM API calls and associated costs.

For more details, refer to the [Pytest](/langsmith/pytest) and [Vitest/Jest](/langsmith/vitest-jest) pages.

### Regression tests

*Regression tests* measure performance consistency across application versions over time. They ensure new versions do not degrade performance on cases the current version handles correctly, and ideally demonstrate improvements over the baseline. These tests typically run when making updates expected to affect user experience (e.g., model or architecture changes).

LangSmith's comparison view highlights regressions (red) and improvements (green) relative to the baseline, enabling quick identification of changes.

<img alt="Comparison view" />

### Backtesting

*Backtesting* evaluates new application versions against historical production data. Production logs are converted into a dataset, then newer versions process these examples to assess performance on past, realistic user inputs.

This approach is commonly used for evaluating new model releases. For example, when a new model becomes available, test it on the most recent production runs and compare results to actual production outcomes.

### Pairwise evaluation

*Pairwise evaluation* compares outputs from two versions by determining relative quality rather than assigning absolute scores. For some tasks, [determining "version A is better than B"](https://www.oreilly.com/radar/what-we-learned-from-a-year-of-building-with-llms-part-i/) is easier than scoring each version independently.

This approach proves particularly useful for LLM-as-judge evaluations on subjective tasks. For example, in summarization, determining "Which summary is clearer and more concise?" is often simpler than assigning numeric clarity scores.

Learn [how run pairwise evaluations](/langsmith/evaluate-pairwise).

## Online evaluation types

Online evaluation assesses production application outputs in near real-time. Without reference outputs, these evaluations focus on detecting issues, monitoring quality trends, and identifying edge cases that inform future offline testing.

Online evaluators typically run server-side. LangSmith provides built-in [LLM-as-judge evaluators](/langsmith/llm-as-judge) for configuration, and supports custom code evaluators that run within LangSmith.

<img alt="Online" />

### Real-time monitoring

Monitor application quality continuously as users interact with the system. Online evaluations run automatically on production traffic, providing immediate feedback on each interaction. This enables detection of quality degradation, unusual patterns, or unexpected behaviors before they impact significant user populations.

### Anomaly detection

Identify outliers and edge cases that deviate from expected patterns. Online evaluators can flag runs with unusual characteristics—extremely long or short responses, unexpected error rates, or outputs that fail safety checks—for human review and potential addition to offline datasets.

### Production feedback loop

Use insights from production to improve offline evaluation. Online evaluations surface real-world issues and usage patterns that may not appear in curated datasets. Failed production runs become candidates for dataset examples, creating an iterative cycle where production experience continuously refines testing coverage.

## Implement evaluators

The evaluation types above describe *when* to evaluate. LangSmith provides several approaches for *how* to implement evaluators that work across these evaluation types.

### LLM-as-a-judge

Use an LLM to score outputs based on criteria defined in a prompt. This approach works well for subjective qualities like tone, clarity, or semantic correctness that are difficult to capture with deterministic rules.

Common use cases include assessing factual accuracy against reference outputs (offline) or checking for toxicity in production responses (online). For example, benchmarking a RAG system might use an LLM-as-judge evaluator to check semantic equivalence between generated and reference answers.

Configure LLM-as-a-judge evaluators for:

* Programmatic offline evaluation: [With the SDK](/langsmith/llm-as-judge-sdk)
* Offline evaluation on datasets: [In the UI](/langsmith/llm-as-judge)
* Online evaluation on production traces: [In the UI](/langsmith/online-evaluations-llm-as-judge)

### Code evaluators

Write deterministic, rule-based functions that check specific conditions. These evaluators execute custom logic to validate structure, check for patterns, or apply business rules.

Code evaluators are particularly useful for unit tests—verifying generated code compiles, JSON parses correctly, or required fields are present. In regression testing, they can track consistency of structured outputs. For online monitoring, they catch format violations in real-time.

Define code evaluators for:

* Offline evaluation on datasets: [In the UI](/langsmith/code-evaluator-ui)
* Programmatic offline evaluation: [With the SDK](/langsmith/code-evaluator-sdk)
* Online evaluation on production traces: [In the UI](/langsmith/online-evaluations-code)

### Composite evaluators

Combine multiple evaluator scores into a single metric using weighted averages or sums. This creates aggregate quality scores that reflect multiple evaluation criteria simultaneously.

For benchmarking, composite scores help compare versions on multiple dimensions (e.g., 70% accuracy + 20% clarity + 10% conciseness). In online monitoring, they provide single metrics for dashboards and alerts. For example, track overall chatbot quality as a weighted combination of helpfulness, correctness, and tone scores.

Set up composite evaluators for:

* Offline evaluation with predefined aggregation: [In the UI](/langsmith/composite-evaluators-ui)
* Offline evaluation with custom aggregation logic: [With the SDK](/langsmith/composite-evaluators-sdk)
* Online evaluation on production traces: [In the UI](/langsmith/online-evaluations-composite)

### Summary evaluators

Compute metrics across an entire experiment rather than individual examples. These evaluators receive all outputs from a dataset and calculate aggregate statistics like precision, recall, F1 scores, or distribution analysis.

Summary evaluators are essential for benchmarking when you need dataset-level metrics—comparing overall performance across versions rather than example-by-example scores. They work exclusively with offline evaluation because they require processing complete datasets.

Implement summary evaluators for:

* Custom aggregation functions for offline evaluation: [With the SDK](/langsmith/summary)

### Pairwise evaluators

Compare outputs from two versions to determine relative quality. This approach, covered earlier under [pairwise evaluation](#pairwise-evaluation), helps when absolute scoring is difficult but determining "which is better" is straightforward.

Run pairwise evaluations for:

* Compare existing experiments: [With the SDK](/langsmith/evaluate-pairwise)

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/evaluation-types.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Manage evaluators
Source: https://docs.langchain.com/langsmith/evaluators

View and manage evaluators at the workspace level in LangSmith.

[Evaluators](/langsmith/evaluation-concepts#evaluators) in LangSmith are [workspace-level](/langsmith/administration-overview#workspaces) resources. You can attach a single evaluator to multiple [tracing projects](/langsmith/observability-concepts#projects) and [datasets](/langsmith/evaluation-concepts#datasets), so you can apply consistent evaluation logic across your work without recreating it each time.

<Tip>
  The [LangSmith Engine](/langsmith/engine) suggests custom evaluators for detected issues and can deploy them with one click.
</Tip>

## View evaluators

In the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-evaluators), select **Evaluators** in the left sidebar to view all evaluators in your workspace.

The evaluators table shows the following columns:

| Column                            | Description                                                                                                                                                                     |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Name                              | The evaluator name                                                                                                                                                              |
| Type                              | **LLM as a judge** or **Code**. Composite score evaluators are scoped to individual tracing projects and datasets and do not appear here.                                       |
| Feedback Key                      | The feedback key the evaluator produces                                                                                                                                         |
| Projects & Datasets               | Tracing projects and datasets this evaluator is attached to                                                                                                                     |
| Evaluator Trace Count (this week) | Number of traces this evaluator ran on in the past week. Only shown when spend tracking is enabled; **–** for Code evaluators or evaluators with no attached rules.             |
| Spend (this week)                 | Estimated USD spend for this evaluator in the past week. Only shown when spend tracking is enabled; **–** for Code evaluators or evaluators with no attached rules.             |
| Spend Status                      | Whether the evaluator is **Under limits**, **Unlimited**, or has hit one or more configured spend limits. Only shown when spend tracking is enabled; **–** for Code evaluators. |
| Created By                        | The workspace member who created the evaluator                                                                                                                                  |
| Updated At                        | When the evaluator was last modified                                                                                                                                            |
| Created At                        | When the evaluator was created                                                                                                                                                  |

## Create an evaluator

1. In the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-evaluators), select **Evaluators** in the left sidebar.
2. Click **+ Evaluator** to open the new evaluator panel.
3. The panel lets you:
   * **Create from scratch**: Build a new [LLM-as-a-Judge](/langsmith/llm-as-judge) or [Code](/langsmith/online-evaluations-code) evaluator.
   * **Create from a template**: Start from a ready-made evaluator (also known as a prebuilt evaluator) for common evaluation patterns. A **Recommended** section surfaces popular templates first, followed by templates organized by the following categories:

     | Category          | Description                                          |
     | ----------------- | ---------------------------------------------------- |
     | Security          | Detect leaks, injections, and adversarial inputs.    |
     | Safety            | Evaluate content safety and moderation.              |
     | Quality           | Measure output quality and accuracy.                 |
     | Conversation      | Evaluate conversational quality and user experience. |
     | Trajectory        | Evaluate agent tool use and decision paths.          |
     | Image Evaluations | Evaluate image content quality and safety.           |
     | Voice Evaluation  | Evaluate voice and audio interaction quality.        |

You can also add an evaluator directly from a [tracing project](/langsmith/observability-concepts#projects) or [dataset](/langsmith/evaluation-concepts#datasets). In that flow, you can additionally **attach an existing evaluator** from your workspace, or create a [Composite](/langsmith/composite-evaluators-ui) evaluator. Refer to [Set up LLM-as-a-judge online evaluators](/langsmith/online-evaluations-llm-as-judge) and [Automatically run evaluators on experiments](/langsmith/bind-evaluator-to-dataset).

## View evaluator details

Click any evaluator in the table to open its detail view. The detail view has four tabs:

* **Overview**: The evaluator's feedback configuration and prompt or code definition.
* **Traces**: Traces processed by this evaluator across all attached resources.
* **Logs**: Execution logs for this evaluator across all attached resources.
* **Resources**: The tracing projects and datasets this evaluator is attached to.

## Edit an evaluator

Open an evaluator. In the **Overview** tab, click the **Edit evaluator** <Icon icon="pencil" /> icon to open the **Configure Evaluator** panel. Update the evaluator's configuration. Click **Save**.

Because the evaluator is shared, changes apply across all tracing projects and datasets it is attached to.

## Delete an evaluator

An evaluator cannot be deleted while it is attached to a tracing project or dataset. To delete an evaluator, first remove it from all resources via the **Resources** tab, then delete it.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/evaluators.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
