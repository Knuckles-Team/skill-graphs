# Set up composite online evaluators
Source: https://docs.langchain.com/langsmith/online-evaluations-composite

[Online evaluations](/langsmith/evaluation-concepts#online-evaluations) provide real-time feedback on your production [traces](/langsmith/observability-concepts#traces). This is useful to continuously monitor the performance of your application: to identify issues, measure improvements, and ensure consistent quality over time.

[**Composite evaluators**](/langsmith/composite-evaluators-ui) are a way to combine multiple evaluator scores into a single [score](/langsmith/evaluation-concepts#evaluator-outputs). This is useful when you want to evaluate multiple aspects of your application and combine the results into a single result.

<Note>When an online evaluator runs on any run within a trace, the trace will be auto-upgraded to [extended data retention](/langsmith/usage-and-billing#data-retention-auto-upgrades). This upgrade will impact trace pricing, but ensures that traces meeting your evaluation criteria (typically those most valuable for analysis) are preserved for investigation. </Note>

## View online evaluators

Head to the **Tracing Projects** tab and select a tracing project. To view existing online evaluators for that project, click on the **Evaluators** tab.

## Configure composite online evaluators

You can create composite evaluators on a [tracing project](/langsmith/observability-concepts#projects) for [online evaluations](/langsmith/evaluation-concepts#online-evaluations). With composite evaluators in the UI, you can compute a weighted average or weighted sum of multiple evaluator scores, with configurable weights.

### 1. Navigate to the tracing project

To start configuring a composite evaluator, navigate to the **Tracing** page and select a tracing project.

From the tracing project view, navigate to the **Evaluators** tab. Click **+ Evaluator** to open the **Add Evaluator** panel. Click **Composite Score** under **Create from scratch**.

### 2. Configure the composite evaluator

1. Name your evaluator.
2. Select an aggregation method, either **Average** or **Sum**.
   * **Average**: ∑(weight\*score) / ∑(weight).
   * **Sum**: ∑(weight\*score).
3. Add the feedback keys you want to include in the composite score.
4. Add the weights for the feedback keys. By default, the weights are equal for each feedback key. Adjust the weights to increase or decrease the importance of specific feedback keys in the final score.
5. Click **Create** to save the evaluator.

<Tip> If you need to adjust the weights for the composite scores, they can be updated after the evaluator is created. The resulting scores will be updated for all runs that have the evaluator configured. </Tip>

### 3. View composite evaluator results

Composite scores are attached to a run as **feedback**, similarly to feedback from a single evaluator.

**On a tracing project**:

* Composite scores appear as feedback on runs.
* [Filter for runs](/langsmith/filter-traces-in-application) with a composite score, or where the composite score meets a certain threshold.
* [Create a chart](/langsmith/dashboards#custom-dashboards) to visualize trends in the composite score over time.

<Note> If any of the constituent evaluators are not configured on the run, the composite score will not be calculated for that run. </Note>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/online-evaluations-composite.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Set up LLM-as-a-judge online evaluators
Source: https://docs.langchain.com/langsmith/online-evaluations-llm-as-judge

[Online evaluations](/langsmith/evaluation-concepts#online-evaluations) provide real-time feedback on your production traces. This is useful to monitor the performance of your application continuously—to identify issues, measure improvements, and ensure consistent quality over time.

**[LLM-as-a-judge](/langsmith/evaluation-concepts#llm-as-judge)** evaluators use an LLM to evaluate traces as a scalable substitute for human-like judgment. This guide covers **run-level** evaluators that evaluate a single run. For evaluating entire conversation threads, see [multi-turn online evaluators](/langsmith/online-evaluations-multi-turn).

<Note>When an online evaluator runs on any run within a trace, the trace will be auto-upgraded to [extended data retention](/langsmith/usage-and-billing#data-retention-auto-upgrades). This upgrade will impact trace pricing, but ensures that traces meeting your evaluation criteria (typically those most valuable for analysis) are preserved for investigation. </Note>

## View online evaluators

In the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-online-evaluations-llm-as-judge), head to the **Tracing Projects** tab and select a tracing project. To view existing online evaluators for that project, click on the **Evaluators** tab.

## Add an online evaluator

1. In the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-online-evaluations-llm-as-judge), navigate to the **Tracing** page and select a tracing project.
2. Click the **Evaluators** tab.
3. Click **+ Evaluator** to open the **Add Evaluator** panel.
4. Choose one of the following:
   * **Create from scratch**: Select **LLM-as-a-Judge Evaluator**.
   * **Attach an existing evaluator**: Select an evaluator already in your workspace to reuse it.
   * **Create from a template**: Start from a ready-made evaluator.
5. Name your evaluator.

## Apply a filter to runs that trigger the evaluator

You can apply a filter to the runs that trigger the evaluator. You may want to apply an evaluator based on:

* Runs where a [user left feedback](/langsmith/attach-user-feedback) indicating the response was unsatisfactory.
* Runs that invoke a specific tool call. See [filtering for tool calls](/langsmith/filter-traces-in-application#example-filtering-for-tool-calls) for more information.
* Runs that match a particular piece of metadata (e.g. if you log traces with a `plan_type` and only want to run evaluations on traces from your enterprise customers). See [adding metadata to your traces](/langsmith/add-metadata-tags) for more information.

[Filters on evaluators](/langsmith/filter-traces-in-application) work the same way as when you're filtering traces in a project.

<Tip>
  It's often helpful to inspect runs as you're creating a filter for your evaluator. With the evaluator configuration panel open, you can inspect runs and apply filters to them. Any filters you apply to the runs table will automatically be reflected in filters on your evaluator.
</Tip>

<Tip>
  If you also have a webhook automation rule on this project and want the webhook payload to include this evaluator's scores, add a feedback filter to the webhook rule rather than relying on rule ordering. For example, filter on `has(feedback_key, "answer_usefulness")` so the webhook only fires after the score exists. See [Ensuring evaluations complete before the webhook fires](/langsmith/webhooks#ensuring-evaluations-complete-before-the-webhook-fires) for details.
</Tip>

## Configure a sampling rate

Configure a sampling rate to control the percentage of filtered runs that trigger the automation action. For example, to control costs, you may want to set a filter to only apply the evaluator to 10% of traces. In order to do this, you would set the sampling rate to 0.1.

## Apply a rule to past runs

Apply a rule to past runs by toggling the **Apply to past runs** and entering a "Backfill from" date. This is only possible upon rule creation.

<Note>
  The backfill is processed as a background job, so you will not see the results immediately.
</Note>

In order to track progress of the backfill, you can view logs for your evaluator by heading to the **Evaluators** tab within a tracing project and clicking the Logs button for the evaluator you created. Online evaluator logs are similar to [automation rule logs](/langsmith/rules#view-logs-for-your-automations).

1. Add an evaluator name.
2. Optionally filter runs that you would like to apply your evaluator on or configure a sampling rate.
3. Select **Apply Evaluator**.

## Configure the LLM-as-a-judge evaluator

View [LLM-as-a-judge evaluators](/langsmith/llm-as-judge#evaluator-templates) for more information.

## Map multimodal content to evaluator

If your traces contain multimodal content like images, audio, or documents, you can include this content in your evaluator prompts. There are two approaches:

* **Using base64-encoded content from traces**: If your application logs multimodal content as base64-encoded data in the trace (for example, in the input or output of a run), you can reference this content directly in your evaluator prompt using template variables. The evaluator will extract the base64 data from the trace and pass it to the LLM.
* **Using attachments from traces**: Similar to [offline evaluations with attachments](/langsmith/evaluate-with-attachments), you can use attachments from your traces in online evaluations. Since your traces already include attachments logged via the SDK, you can reference them directly in your evaluator.

  1. Select **+ Evaluator** from the dataset page.
  2. In the **Template variables** editor, add a variable for the attachment(s) to include:
     * If you want to include a specific attachment, you can use the suggested variable name, such as `{{attachment.file_name}}`, this will map the file with `file_name` in the attachment list to pass it to the evaluator.
     * If you want to include all attachments, use the `{{attachments}`}\` variable.

  <img alt="Edit evaluator modal with an image attachment selected for the input." />

  <img alt="Edit evaluator modal with an image attachment selected for the input." />

The evaluator can then access these attachments when evaluating the trace. This is useful for evaluators that need to:

* Verify if an image description matches the actual image in the trace.
* Check if a transcription accurately reflects the audio input.
* Validate if extracted text from a document is correct.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/online-evaluations-llm-as-judge.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Set up multi-turn online evaluators
Source: https://docs.langchain.com/langsmith/online-evaluations-multi-turn

Multi-turn online evaluators allow you to evaluate entire conversations between a human and an agent—not just individual exchanges. They measure end-to-end interaction quality across all turns in a thread.

You can use multi-turn evaluations to measure:

1. Semantic Intent: What the user was trying to do.
2. Semantic Outcome: What actually happened, did the task succeed.
3. Trajectory: How the conversation unfolded, including trajectory of tool calls.

<Note> Running multi-turn online evals will auto-upgrade each trace within a thread to [extended data retention](/langsmith/usage-and-billing#data-retention-auto-upgrades). This upgrade will impact trace pricing, but ensures that traces meeting your evaluation criteria (typically those most valuable for analysis) are preserved for investigation. </Note>

## How it works

Multi-turn online evaluators follow this evaluation lifecycle:

1. **Trace ingestion**: Each turn in a conversation is traced as a separate run and associated with a thread using a shared thread ID.
2. **Idle time detection**: After the last trace in a thread is ingested, LangSmith waits for the configured idle time to elapse. This idle period signals that the conversation is complete and ready for evaluation.
3. **Message assembly**: LangSmith collects the `messages` from each trace in the thread and assembles them into a single conversation history. If each trace contains only the latest message, LangSmith stitches messages together across turns. If each trace contains the full history, LangSmith uses that directly. Because consecutive traces in a thread often resend prior history, LangSmith deduplicates overlapping messages so each one appears only once. The result is a single list of messages in OpenAI chat format (`{"role": ..., "content": ...}`), which is what the `all_messages` variable in your prompt resolves to.
4. **LLM-as-a-judge evaluation**: The assembled conversation is passed to your configured LLM-as-a-judge prompt. The evaluator scores the full thread based on your criteria: semantic intent, outcome, or trajectory.
5. **Feedback recording**: The evaluator writes feedback to LangSmith using the feedback key you configured, associated with the thread.

This lifecycle means that multi-turn evaluators run once per completed thread, not once per trace. Use [run-level online evaluators](/langsmith/online-evaluations-llm-as-judge) if you want per-trace evaluation.

## Prerequisites

* Your tracing project must be using [threads](/langsmith/threads).
* The top-level inputs and outputs of each trace in a thread must have a `messages` key that contains a list of messages. We support messages in [LangChain](/langsmith/log-llm-trace#messages-format), [OpenAI Chat Completions](https://platform.openai.com/docs/api-reference/chat/create), and [Anthropic Messages](https://platform.claude.com/docs/en/api/messages) formats.
  * If the top-level inputs and outputs of each trace only contain the latest message in the conversation, LangSmith will automatically combine messages across turns into a thread.
  * If the top-level inputs and outputs of each trace contain the full conversation history, LangSmith will use that directly.

<Note>
  If your traces don't follow the format above, thread level evaluators won't work. You'll need to update how you trace to LangSmith to ensure each trace's top-level inputs and outputs contain a list of `messages`.

  Please refer to the [troubleshooting](/langsmith/online-evaluations-multi-turn#troubleshooting) section for more information.
</Note>

## Configuration

1. Navigate to the **Tracing** page and select a tracing project.
2. Click the **Evaluators** tab, then click **+ Evaluator**. Select **LLM-as-a-Judge Evaluator** under **Create from scratch**. Under **Source**, select **Threads**.
3. **Name your evaluator**.
4. Apply **Filters** or a **Sampling Rate**. <br />
   Use filters or sampling to control evaluator cost. For example, evaluate only threads under *N* turns or sample 10% of all threads.
5. **Configure an idle time**. <br />
   The first time you configure a thread level evaluator, you'll define the idle time—the amount of time after the last trace in a thread before it's considered complete and ready for evaluation. This value should reflect the expected length of user interactions in your app. It applies across all evaluators in the project.

<Tip>
  When first testing your evaluator, use a short idle time so you can see results quickly. Once validated, increase it to match the expected length of user interactions.
</Tip>

6. **Configure your model.**<br />
   Select the provider and model you want to use for your evaluator. Threads tend to get long, so you should use a model with a higher context window in order to avoid running into limits. For example, OpenAI's GPT-5.4 mini or Gemini 2.5 Flash are good options as they both have 1M+ token context windows.

7. **Configure your LLM-as-a-judge prompt.**<br />
   Define what you want to evaluate. This prompt will be used to evaluate the thread. You can also configure which parts of the assembled conversation are passed to the evaluator through the `all_messages` variable to control the content it receives:
   * All messages: Send the full conversation as a list of JSON message objects in OpenAI chat format (`{"role": ..., "content": ...}`), with each message rendered as indented JSON and separated by a blank line.
   * Human and AI pairs: Send only user and assistant messages, formatted as `<user>...</user>` and `<assistant>...</assistant>` and excluding system messages, tool calls, and other roles.
   * First human and last AI: Send only the first user message and the last assistant reply.

8. **Set up your feedback configuration**.<br />
   Configure a name for the feedback key, the format for the feedback you want to collect and optionally enable reasoning on the feedback.

<Warning>
  We don't recommend using the same feedback key for a thread-level evaluator and a run-level evaluator as it can be hard to distinguish between the two.
</Warning>

8. **Save your evaluator.**

After saving, your evaluator will appear in the **Evaluators** tab. You can test it once the idle time has passed for any new threads created after saving.

## Limits

These are the current limits for multi-turn online evaluators (subject to change). Please reach out if you are running into any of these limits.

* **Runs must be less than one week old**: When a thread becomes idle, only runs within the past 7 days are eligible for evaluation.
* **Maximum of 500 threads evaluated at once**: If you have more than 500 threads marked as idle in a five minute period, we will automatically sample beyond 500.
* **Maximum of 10 multi-turn online evaluators per workspace**

## Troubleshooting

**Checking the status of your evaluator** <br />
You can check when your evaluator was last run by heading to the **Evaluators** tab within a tracing project and clicking the **Logs** button for the evaluator you created to view its run history.

**Inspect the data sent to the evaluator** <br />
Inspect the data sent to the evaluator by heading to the **Evaluators** tab within a tracing project, clicking on the evaluator you created and clicking the **Evaluator traces** tab.

In this tab, you can see the inputs passed into the LLM-as-a-judge evaluator. If your messages are not being passed in correctly, you will see blank values in the inputs. This can happen if your messages are not formatted in one of [the expected formats](/langsmith/online-evaluations-multi-turn#prerequisites).

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/online-evaluations-multi-turn.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Document API authentication in OpenAPI
Source: https://docs.langchain.com/langsmith/openapi-security

This guide shows how to customize the OpenAPI security schema for your LangSmith API documentation. A well-documented security schema helps API consumers understand how to authenticate with your API and even enables automatic client generation. See the [Authentication & Access Control conceptual guide](/langsmith/auth) for more details about LangGraph's authentication system.

<Note>
  **Implementation vs Documentation**
  This guide only covers how to document your security requirements in OpenAPI. To implement the actual authentication logic, see [How to add custom authentication](/langsmith/custom-auth).
</Note>

This guide applies to all LangSmith deployments (Cloud and self-hosted). It does not apply to usage of the LangGraph open source library if you are not using LangSmith.

## Default schema

The default security scheme varies by deployment type:

<Tabs>
  <Tab title="LangSmith" />
</Tabs>

By default, LangSmith requires a LangSmith API key in the `x-api-key` header:

```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
components:
  securitySchemes:
    apiKeyAuth:
      type: apiKey
      in: header
      name: x-api-key
security:
  - apiKeyAuth: []
```

When using one of the LangGraph SDK's, this can be inferred from environment variables.

<Tabs>
  <Tab title="Self-hosted" />
</Tabs>

By default, self-hosted deployments have no security scheme. This means they are to be deployed only on a secured network or with authentication. To add custom authentication, see [How to add custom authentication](/langsmith/custom-auth).

## Custom security schema

To customize the security schema in your OpenAPI documentation, add an `openapi` field to your `auth` configuration in `langgraph.json`. Remember that this only updates the API documentation - you must also implement the corresponding authentication logic as shown in [How to add custom authentication](/langsmith/custom-auth).

Note that LangSmith does not provide authentication endpoints - you'll need to handle user authentication in your client application and pass the resulting credentials to the LangGraph API.

<Tabs>
  <Tab title="OAuth2 with Bearer Token">
    ```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    {
      "auth": {
        "path": "./auth.py:my_auth",  // Implement auth logic here
        "openapi": {
          "securitySchemes": {
            "OAuth2": {
              "type": "oauth2",
              "flows": {
                "implicit": {
                  "authorizationUrl": "https://your-auth-server.com/oauth/authorize",
                  "scopes": {
                    "me": "Read information about the current user",
                    "threads": "Access to create and manage threads"
                  }
                }
              }
            }
          },
          "security": [
            {"OAuth2": ["me", "threads"]}
          ]
        }
      }
    }
    ```
  </Tab>

  <Tab title="API Key">
    ```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    {
      "auth": {
        "path": "./auth.py:my_auth",  // Implement auth logic here
        "openapi": {
          "securitySchemes": {
            "apiKeyAuth": {
              "type": "apiKey",
              "in": "header",
              "name": "X-API-Key"
            }
          },
          "security": [
            {"apiKeyAuth": []}
          ]
        }
      }
    }
    ```
  </Tab>
</Tabs>

## Testing

After updating your configuration:

1. Deploy your application
2. Visit `/docs` to see the updated OpenAPI documentation
3. Try out the endpoints using credentials from your authentication server (make sure you've implemented the authentication logic first)

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/openapi-security.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Run evals with openevals package
Source: https://docs.langchain.com/langsmith/openevals

Run evaluations using the open-source openevals and agentevals packages with LangSmith.

LangSmith integrates with the open-source `openevals` package to provide a suite of evaluation utilities and prompts that you can use as starting points for evaluation.

<Note>
  This how-to guide will demonstrate how to set up and run one type of evaluator (LLM-as-a-judge). For a complete list of evaluation utilities and prompts with usage examples, refer to the [openevals](https://github.com/langchain-ai/openevals) and [agentevals](https://github.com/langchain-ai/agentevals) repos.
</Note>

## Setup

You'll need to install the `openevals` package to use the LLM-as-a-judge evaluator.

<CodeGroup>
  ```bash Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install -U openevals
  ```

  ```bash TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  yarn add openevals @langchain/core
  ```
</CodeGroup>

You'll also need to set your OpenAI API key as an environment variable, though you can choose different providers too:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
export OPENAI_API_KEY="your_openai_api_key"
```

We'll also use LangSmith's [pytest](/langsmith/pytest) integration for Python and [Vitest/Jest](/langsmith/vitest-jest) for TypeScript to run our evals. `openevals` also integrates seamlessly with the [`evaluate`](https://docs.smith.langchain.com/reference/python/evaluation/langsmith.evaluation._runner.evaluate) method. See the [appropriate guides](/langsmith/pytest) for setup instructions.

## Running an evaluator

The general flow is simple: import the evaluator or factory function from `openevals`, then run it within your test file with inputs, outputs, and reference outputs. LangSmith will automatically log the evaluator's results as feedback.

Note that not all evaluators will require each parameter (the exact match evaluator only requires outputs and reference outputs, for example). Additionally, if your LLM-as-a-judge prompt requires additional variables, passing them in as kwargs will format them into the prompt.

Set up your test file like this:

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import pytest
  from langsmith import testing as t
  from openevals.llm import create_llm_as_judge
  from openevals.prompts import CORRECTNESS_PROMPT

  correctness_evaluator = create_llm_as_judge(
      prompt=CORRECTNESS_PROMPT,
      feedback_key="correctness",
      model="openai:o3-mini",
  )

  # Mock standin for your application
  def my_llm_app(inputs: dict) -> str:
      return "Doodads have increased in price by 10% in the past year."

  @pytest.mark.langsmith
  def test_correctness():
      inputs = "How much has the price of doodads changed in the past year?"
      reference_outputs = "The price of doodads has decreased by 50% in the past year."
      outputs = my_llm_app(inputs)

      t.log_inputs({"question": inputs})
      t.log_outputs({"answer": outputs})
      t.log_reference_outputs({"answer": reference_outputs})

      correctness_evaluator(
          inputs=inputs,
          outputs=outputs,
          reference_outputs=reference_outputs
      )
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import * as ls from "langsmith/vitest";
  // import * as ls from "langsmith/jest";
  import { createLLMAsJudge, CORRECTNESS_PROMPT } from "openevals";

  const correctnessEvaluator = createLLMAsJudge({
      prompt: CORRECTNESS_PROMPT,
      feedbackKey: "correctness",
      model: "openai:o3-mini",
  });

  // Mock standin for your application
  const myLLMApp = async (_inputs: Record<string, unknown>) => {
      return "Doodads have increased in price by 10% in the past year.";
  };

  ls.describe("Correctness", () => {
      ls.test("incorrect answer", {
          inputs: {
              question: "How much has the price of doodads changed in the past year?"
          },
          referenceOutputs: {
              answer: "The price of doodads has decreased by 50% in the past year."
          }
      }, async ({ inputs, referenceOutputs }) => {
          const outputs = await myLLMApp(inputs);
          ls.logOutputs({ answer: outputs });
          await correctnessEvaluator({
              inputs,
              outputs,
              referenceOutputs,
          });
      });
  });
  ```
</CodeGroup>

The `feedback_key`/`feedbackKey` parameter will be used as the name of the feedback in your experiment.

Running the eval in your terminal will result in something like the following:

<img alt="Prebuilt evaluator terminal result" />

You can also pass evaluators directly into the `evaluate` method if you have already created a dataset in LangSmith. If using Python, this requires `langsmith>=0.3.11`:

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langsmith import Client
  from openevals.llm import create_llm_as_judge
  from openevals.prompts import CONCISENESS_PROMPT

  client = Client()
  conciseness_evaluator = create_llm_as_judge(
      prompt=CONCISENESS_PROMPT,
      feedback_key="conciseness",
      model="openai:o3-mini",
  )

  experiment_results = client.evaluate(
      # This is a dummy target function, replace with your actual LLM-based system
      lambda inputs: "What color is the sky?",
      data="Sample dataset",
      evaluators=[
          conciseness_evaluator
      ]
  )
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { evaluate } from "langsmith/evaluation";
  import { createLLMAsJudge, CONCISENESS_PROMPT } from "openevals";

  const concisenessEvaluator = createLLMAsJudge({
      prompt: CONCISENESS_PROMPT,
      feedbackKey: "conciseness",
      model: "openai:o3-mini",
  });

  await evaluate((inputs) => "What color is the sky?", {
      data: datasetName,
      evaluators: [concisenessEvaluator],
  });
  ```
</CodeGroup>

For a complete list of available evaluation utilities and prompts, see the [openevals](https://github.com/langchain-ai/openevals) and [agentevals](https://github.com/langchain-ai/agentevals) repos.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/openevals.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Optimize a classifier
Source: https://docs.langchain.com/langsmith/optimize-classifier

This tutorial walks through optimizing a classifier based on user a feedback. Classifiers are great to optimize because its generally pretty simple to collect the desired output, which makes it easy to create few shot examples based on user feedback. That is exactly what we will do in this example.

## The objective

In this example, we will build a bot that classify GitHub issues based on their title. It will take in a title and classify it into one of many different classes. Then, we will start to collect user feedback and use that to shape how this classifier performs.

## Getting started

To get started, we will first set it up so that we send all traces to a specific project. We can do this by setting an environment variable:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import os
os.environ["LANGSMITH_PROJECT"] = "classifier"
```

We can then create our initial application. This will be a really simple function that just takes in a GitHub issue title and tries to label it.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import openai
from langsmith import traceable, Client
import uuid

client = openai.Client()

available_topics = [
    "bug",
    "improvement",
    "new_feature",
    "documentation",
    "integration",
]

prompt_template = """Classify the type of the issue as one of {topics}.
Issue: {text}"""

@traceable(
    run_type="chain",
    name="Classifier",
)
def topic_classifier(
    topic: str):
    return client.chat.completions.create(
        model="gpt-5.4-mini",
        temperature=0,
        messages=[
            {
                "role": "user",
                "content": prompt_template.format(
                    topics=','.join(available_topics),
                    text=topic,
                )
            }
        ],
    ).choices[0].message.content
```

We can then start to interact with it. When interacting with it, we will generate the LangSmith run id ahead of time and pass that into this function. We do this so we can attach feedback later on.

Here's how we can invoke the application:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langsmith import uuid7

run_id = uuid7()
topic_classifier(
    "fix bug in LCEL",
    langsmith_extra={"run_id": run_id})
```

Here's how we can attach feedback after. We can collect feedback in two forms.

First, we can collect "positive" feedback - this is for examples that the model got right.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
ls_client = Client()
run_id = uuid7()
topic_classifier(
    "fix bug in LCEL",
    langsmith_extra={"run_id": run_id})
ls_client.create_feedback(
    run_id,
    key="user-score",
    score=1.0,
)
```

Next, we can focus on collecting feedback that corresponds to a "correction" to the generation. In this example the model will classify it as a bug, whereas I really want this to be classified as documentation.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
ls_client = Client()
run_id = uuid7()
topic_classifier(
    "fix bug in documentation",
    langsmith_extra={"run_id": run_id})
ls_client.create_feedback(
    run_id,
    key="correction",
    correction="documentation")
```

## Set up automations

We can now set up automations to move examples with feedback of some form into a dataset. We will set up two automations, one for positive feedback and the other for negative feedback.

The first will take all runs with positive feedback and automatically add them to a dataset. The logic behind this is that any run with positive feedback we can use as a good example in future iterations. Let's create a dataset called `classifier-github-issues` to add this data to.

<img alt="Optimization Negative" />

The second will take all runs with a correction and use a webhook to add them to a dataset. When creating this webhook, we will select the option to "Use Corrections". This option will make it so that when creating a dataset from a run, rather than using the output of the run as the gold-truth output of the datapoint, it will use the correction.

<img alt="Optimization Positive" />

## Update the application

We can now update our code to pull down the dataset we are sending runs to. Once we pull it down, we can create a string with the examples in it. We can then put this string as part of the prompt!

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
### NEW CODE ###

# Initialize the LangSmith Client so we can use to get the dataset
ls_client = Client()

# Create a function that will take in a list of examples and format them into a string
def create_example_string(examples):
    final_strings = []
    for e in examples:
        final_strings.append(f"Input: {e.inputs['topic']}\n> {e.outputs['output']}")
    return "\n\n".join(final_strings)
### NEW CODE ###

client = openai.Client()

available_topics = [
    "bug",
    "improvement",
    "new_feature",
    "documentation",
    "integration",
]

prompt_template = """Classify the type of the issue as one of {topics}.

Here are some examples:
{examples}

Begin!
Issue: {text}
>"""

@traceable(
    run_type="chain",
    name="Classifier",
)
def topic_classifier(
    topic: str):
    # We can now pull down the examples from the dataset
    # We do this inside the function so it always get the most up-to-date examples,
    # But this can be done outside and cached for speed if desired
    examples = list(ls_client.list_examples(dataset_name="classifier-github-issues"))  # <- New Code
    example_string = create_example_string(examples)
    return client.chat.completions.create(
        model="gpt-5.4-mini",
        temperature=0,
        messages=[
            {
                "role": "user",
                "content": prompt_template.format(
                    topics=','.join(available_topics),
                    text=topic,
                    examples=example_string,
                )
            }
        ],
    ).choices[0].message.content
```

If now run the application with a similar input as before, we can see that it correctly learns that anything related to docs (even if a bug) should be classified as `documentation`

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
ls_client = Client()
run_id = uuid7()
topic_classifier(
    "address bug in documentation",
    langsmith_extra={"run_id": run_id})
```

## Semantic search over examples

One additional thing we can do is only use the most semantically similar examples. This is useful when you start to build up a lot of examples.

In order to do this, we can first define an example to find the `k` most similar examples:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import numpy as np

def find_similar(examples, topic, k=5):
    inputs = [e.inputs['topic'] for e in examples] + [topic]
    vectors = client.embeddings.create(input=inputs, model="text-embedding-3-small")
    vectors = [e.embedding for e in vectors.data]
    vectors = np.array(vectors)
    args = np.argsort(-vectors.dot(vectors[-1])[:-1])[:5]
    examples = [examples[i] for i in args]
    return examples
```

We can then use that in the application

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
ls_client = Client()

def create_example_string(examples):
    final_strings = []
    for e in examples:
        final_strings.append(f"Input: {e.inputs['topic']}\n> {e.outputs['output']}")
    return "\n\n".join(final_strings)

client = openai.Client()

available_topics = [
    "bug",
    "improvement",
    "new_feature",
    "documentation",
    "integration",
]

prompt_template = """Classify the type of the issue as one of {topics}.

Here are some examples:
{examples}

Begin!
Issue: {text}
>"""

@traceable(
    run_type="chain",
    name="Classifier",
)
def topic_classifier(
    topic: str):
    examples = list(ls_client.list_examples(dataset_name="classifier-github-issues"))
    examples = find_similar(examples, topic)
    example_string = create_example_string(examples)
    return client.chat.completions.create(
        model="gpt-5.4-mini",
        temperature=0,
        messages=[
            {
                "role": "user",
                "content": prompt_template.format(
                    topics=','.join(available_topics),
                    text=topic,
                    examples=example_string,
                )
            }
        ],
    ).choices[0].message.content
```

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/optimize-classifier.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
