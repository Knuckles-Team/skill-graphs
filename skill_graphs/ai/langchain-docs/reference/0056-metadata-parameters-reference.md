# Metadata parameters reference
Source: https://docs.langchain.com/langsmith/ls-metadata-parameters

When you trace LLM calls with LangSmith, you often want to [track costs](/langsmith/cost-tracking), compare model configurations, and analyze performance across different providers. LangSmith's native integrations (like [LangChain](/langsmith/trace-with-langchain) or the [OpenAI](/langsmith/trace-openai)/[Anthropic](/langsmith/trace-anthropic) wrappers) handle this automatically, but custom model wrappers and self-hosted models require a standardized way to provide this information. LangSmith uses `ls_` metadata parameters for this purpose.

These metadata parameters (all prefixed with `ls_`) let you pass model configuration and identification information through the standard `metadata` field. Once set, LangSmith can automatically calculate costs, display model information in the UI, and enable [filtering](/langsmith/filter-traces-in-application) and analytics across your traces.

Use `ls_` metadata parameters to:

* **Enable automatic cost tracking** for custom or self-hosted models by identifying the provider and model name.
* **Track model configuration** like temperature, max tokens, and other parameters for experiment comparison.
* **Filter and analyze traces** by provider or configuration settings
* **Customize Messages view rendering** for custom agent instrumentation.
* **Mark interrupted errors** so LangSmith can render interrupted runs separately from other errors.
* **Improve debugging** by recording exactly which model settings were used for each run.

## Basic usage example

The most common use case is enabling cost tracking for custom model wrappers. To do this, you need to provide two key pieces of information: the provider name (`ls_provider`) and the model name (`ls_model_name`). These work together to match against LangSmith's pricing database.

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langsmith import traceable

  @traceable(
      run_type="llm",
      metadata={
          "ls_provider": "my_provider",
          "ls_model_name": "my_custom_model"
      }
  )
  def my_custom_llm(prompt: str):
      return call_custom_api(prompt)
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { traceable } from "langsmith/traceable";

  const myCustomLlm = traceable(
    async (prompt: string) => {
      return callCustomApi(prompt);
    },
    {
      run_type: "llm",
      metadata: {
        ls_provider: "my_provider",
        ls_model_name: "my_custom_model"
      }
    }
  );
  ```

  ```java Java theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import com.langchain.smith.tracing.RunType;
  import com.langchain.smith.tracing.TraceConfig;
  import com.langchain.smith.tracing.Tracing;
  import java.util.HashMap;
  import java.util.Map;
  import java.util.function.Function;

  Map<String, Object> metadata = new HashMap<>();
  metadata.put("ls_provider", "my_provider");
  metadata.put("ls_model_name", "my_custom_model");

  Function<String, String> myCustomLlm =
      Tracing.traceFunction(
          prompt -> callCustomApi(prompt),
          TraceConfig.builder()
              .runType(RunType.LLM)
              .metadata(metadata)
              .build());
  ```

  ```kotlin Kotlin theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import com.langchain.smith.tracing.RunType
  import com.langchain.smith.tracing.TraceConfig
  import com.langchain.smith.tracing.traceable

  val myCustomLlm =
      traceable(
          { prompt: String -> callCustomApi(prompt) },
          TraceConfig.builder()
              .runType(RunType.LLM)
              .metadata(
                  mapOf(
                      "ls_provider" to "my_provider",
                      "ls_model_name" to "my_custom_model",
                  ),
              )
              .build(),
      )
  ```
</CodeGroup>

This minimal setup tells LangSmith what model you're using, enabling automatic cost calculation if the model exists in the pricing database or if you've [configured custom pricing](/langsmith/cost-tracking#llm-calls-automatically-track-costs-based-on-token-counts).

For more comprehensive tracking, you can include additional configuration parameters. This is especially useful when [running experiments](/langsmith/evaluation-quickstart) or comparing different model settings:

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  @traceable(
      run_type="llm",
      metadata={
          "ls_provider": "openai",
          "ls_model_name": "gpt-5.5",
          "ls_temperature": 0.7,
          "ls_max_tokens": 4096,
          "ls_stop": ["END"],
          "ls_invocation_params": {
              "top_p": 0.9,
              "frequency_penalty": 0.5
          }
      }
  )
  def my_configured_llm(messages: list):
      return call_llm(messages)
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  const myConfiguredLlm = traceable(
    async (messages: Array<any>) => {
      return callLlm(messages);
    },
    {
      run_type: "llm",
      metadata: {
        ls_provider: "openai",
        ls_model_name: "gpt-5.5",
        ls_temperature: 0.7,
        ls_max_tokens: 4096,
        ls_stop: ["END"],
        ls_invocation_params: {
          top_p: 0.9,
          frequency_penalty: 0.5
        }
      }
    }
  );
  ```

  ```java Java theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import com.langchain.smith.tracing.RunType;
  import com.langchain.smith.tracing.TraceConfig;
  import com.langchain.smith.tracing.Tracing;
  import java.util.Collections;
  import java.util.HashMap;
  import java.util.List;
  import java.util.Map;
  import java.util.function.Function;

  Map<String, Object> metadata = new HashMap<>();
  metadata.put("ls_provider", "openai");
  metadata.put("ls_model_name", "gpt-5.5");
  metadata.put("ls_temperature", 0.7);
  metadata.put("ls_max_tokens", 4096);
  metadata.put("ls_stop", Collections.singletonList("END"));

  Map<String, Object> invocationParams = new HashMap<>();
  invocationParams.put("top_p", 0.9);
  invocationParams.put("frequency_penalty", 0.5);
  metadata.put("ls_invocation_params", invocationParams);

  Function<List<Map<String, String>>, String> myConfiguredLlm =
      Tracing.traceFunction(
          messages -> callLlm(messages),
          TraceConfig.builder()
              .runType(RunType.LLM)
              .metadata(metadata)
              .build());
  ```

  ```kotlin Kotlin theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  val myConfiguredLlm =
      traceable(
          { messages: List<Map<String, String>> -> callLlm(messages) },
          TraceConfig.builder()
              .runType(RunType.LLM)
              .metadata(
                  mapOf(
                      "ls_provider" to "openai",
                      "ls_model_name" to "gpt-5.5",
                      "ls_temperature" to 0.7,
                      "ls_max_tokens" to 4096,
                      "ls_stop" to listOf("END"),
                      "ls_invocation_params" to
                          mapOf(
                              "top_p" to 0.9,
                              "frequency_penalty" to 0.5,
                          ),
                  ),
              )
              .build(),
      )
  ```
</CodeGroup>

With this setup, you can later filter traces by temperature, compare runs with different max token settings, or analyze which configuration parameters produce the best results. All these parameters are optional except for the `ls_provider` and `ls_model_name` pair needed for cost tracking.

## All parameters

### User-configurable parameters

| Parameter                                         | Type       | Required | Description                                                                                    |
| ------------------------------------------------- | ---------- | -------- | ---------------------------------------------------------------------------------------------- |
| [`ls_provider`](#ls_provider)                     | `string`   | Yes\*    | LLM provider name for cost tracking                                                            |
| [`ls_model_name`](#ls_model_name)                 | `string`   | Yes\*    | Model identifier for cost tracking                                                             |
| [`ls_temperature`](#ls_temperature)               | `number`   | No       | Temperature parameter used                                                                     |
| [`ls_max_tokens`](#ls_max_tokens)                 | `number`   | No       | Maximum tokens parameter used                                                                  |
| [`ls_stop`](#ls_stop)                             | `string[]` | No       | Stop sequences used                                                                            |
| [`ls_invocation_params`](#ls_invocation_params)   | `object`   | No       | Additional invocation parameters                                                               |
| [`ls_agent_type`](#ls_agent_type)                 | `string`   | No       | Controls how agent runs appear in the Messages view: `"root"`, `"subagent"`, or `"middleware"` |
| [`ls_is_error_interrupt`](#ls_is_error_interrupt) | `boolean`  | No       | Marks an errored run as interrupted when set to `true`                                         |

\* `ls_provider` and `ls_model_name` must be provided together for cost tracking

### System-generated parameters

| Parameter                       | Type      | Description                                                            |
| ------------------------------- | --------- | ---------------------------------------------------------------------- |
| [`ls_run_depth`](#ls_run_depth) | `integer` | Depth in trace tree (0=root, 1=child, etc.) - automatically calculated |
| [`ls_method`](#ls_method)       | `string`  | Tracing method used (e.g., "traceable") - set by SDK                   |

### Experiment parameters

| Parameter                               | Type            | Description                                                             |
| --------------------------------------- | --------------- | ----------------------------------------------------------------------- |
| [`ls_example_*`](#ls_example_)          | `any`           | Example metadata prefixed with `ls_example_` - added during experiments |
| [`ls_experiment_id`](#ls_experiment_id) | `string` (UUID) | Unique experiment identifier - added during experiments                 |

## Parameter details

### `ls_provider`

* **Type:** `string`
* **Required:** Yes (with [`ls_model_name`](#ls_model_name))

**What it does:**
Identifies the LLM provider. Combined with `ls_model_name`, enables automatic cost calculation by matching against [LangSmith's model pricing database](https://smith.langchain.com/settings/workspaces/models).

**Common values:**

* `"openai"`
* `"anthropic"`
* `"azure"`
* `"bedrock"`
* `"google_vertexai"`
* `"google_genai"`
* `"fireworks"`
* `"mistral"`
* `"groq"`
* Or, any custom string

**When to use:**
When you want [automatic cost tracking](/langsmith/cost-tracking) for custom model wrappers or self-hosted models.

**Example:**

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
@traceable(
    run_type="llm",
    metadata={
        "ls_provider": "openai",
        "ls_model_name": "gpt-5.5"
    }
)
def my_llm_call(prompt: str):
    return call_api(prompt)
```

**Relationships:**

* **Requires** [`ls_model_name`](#ls_model_name) for cost tracking to work.
* Works with token usage data to calculate costs.

### `ls_model_name`

* **Type:** `string`
* **Required:** Yes (with `ls_provider`)

**What it does:**
Identifies the specific model. Combined with `ls_provider`, matches against pricing database for automatic cost calculation.

**Common values:**

* OpenAI: `"gpt-5.5"`, `"gpt-5.4-mini"`, `"gpt-3.5-turbo"`
* Anthropic: `"claude-3-5-sonnet-20241022"`, `"claude-3-opus-20240229"`
* Custom: Any model identifier

**When to use:**
When you want automatic [cost tracking](/langsmith/cost-tracking) and model identification in the [UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-ls-metadata-parameters).

**Example:**

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
@traceable(
    run_type="llm",
    metadata={
        "ls_provider": "anthropic",
        "ls_model_name": "claude-3-5-sonnet-20241022"
    }
)
def my_claude_call(messages: list):
    return call_claude(messages)
```

**Relationships:**

* **Requires** [`ls_provider`](#ls_provider) for cost tracking to work.
* Works with token usage data to calculate costs.

### `ls_temperature`

* **Type:** `number` (nullable)
* **Required:** No

**What it does:**
Records the temperature setting used. This is for tracking only—does not affect LangSmith behavior.

**When to use:**
When you want to track model configuration for experiments or debugging.

**Example:**

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
metadata={
    "ls_provider": "openai",
    "ls_model_name": "gpt-5.5",
    "ls_temperature": 0.7
}
```

**Relationships:**

* Independent; just for tracking.
* Useful alongside other config parameters for experiment comparison.

### `ls_max_tokens`

* **Type:** `number` (nullable)
* **Required:** No

**What it does:**
Records the maximum tokens setting used. This is for tracking only—does not affect LangSmith behavior.

**When to use:**
When you want to track model configuration for experiments or debugging.

**Example:**

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
metadata={
    "ls_provider": "openai",
    "ls_model_name": "gpt-5.5",
    "ls_max_tokens": 4096
}
```

**Relationships:**

* Independent; just for tracking.
* Useful for cost analysis when combined with actual token usage.

### `ls_stop`

* **Type:** `string[]` (nullable)
* **Required:** No

**What it does:**
Records stop sequences used. This is for tracking only—does not affect LangSmith behavior.

**When to use:**
When you want to track model configuration for experiments or debugging.

**Example:**

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
metadata={
    "ls_provider": "openai",
    "ls_model_name": "gpt-5.5",
    "ls_stop": ["END", "STOP", "\n\n"]
}
```

**Relationships:**

* Independent; just for tracking.

### `ls_invocation_params`

* **Type:** `object` (any key-value pairs)
* **Required:** No

**What it does:**
Stores additional model parameters that don't fit the specific `ls_` parameters. Can include provider-specific settings.

**Common parameters:**
`top_p`, `frequency_penalty`, `presence_penalty`, `top_k`, `seed`, or any custom parameters

**When to use:**
When you need to track additional configuration beyond the standard parameters.

**Example:**

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
metadata={
    "ls_provider": "openai",
    "ls_model_name": "gpt-5.5",
    "ls_invocation_params": {
        "top_p": 0.9,
        "frequency_penalty": 0.5,
        "presence_penalty": 0.3,
        "seed": 12345
    }
}
```

**Relationships:**

* Independent; stores arbitrary configuration.

### `ls_agent_type`

* **Type:** `"root" | "subagent" | "middleware"`
* **Required:** No

**What it does:**
Controls how messages from custom agent-like runs appear in the [Messages view](/langsmith/view-traces#messages-view).

Tracing wrapper integrations from the latest versions of the LangSmith SDK set this metadata automatically when needed. For custom instrumentation, set this key on the run that represents the agent or middleware step.

**Values:**

* `"root"`: Messages from this run appear in the main Messages view.
* `"subagent"`: Messages from this run appear in a side thread, separate from the main conversation.
* `"middleware"`: Messages from this run are hidden from the Messages view.

**When to use:**
When you are building custom agent instrumentation and want the Messages view to distinguish root agents, subagents, and middleware.

For more details, see [Customize the Messages view](/langsmith/view-traces#customize-the-messages-view).

**Relationships:**

* Independent of model identification and cost tracking metadata.
* Complements the trace parent-child structure by identifying the role a run plays in an agent trace.

### `ls_is_error_interrupt`

* **Type:** `boolean`
* **Required:** No

**What it does:**
When set to `true` on a run with an error, marks the run status as interrupted instead of error.

**When to use:**
When your instrumentation can identify that an error represents an interrupted run, such as a user interruption or human-in-the-loop interruption, and you want LangSmith to render it separately from other errors.

**Example:**

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
metadata={
    "ls_is_error_interrupt": True
}
```

**Relationships:**

* Only affects runs that include an error.
* Independent of model identification and cost tracking metadata.

### `ls_run_depth`

* **Type:** `integer`
* **Set by:** LangSmith backend (automatic)
* **Cannot be overridden**

**What it does:**
Indicates depth in the trace tree:

* `0` = Root run (top-level)
* `1` = Direct child
* `2` = Grandchild
* etc.

**When it's used:**
Automatically calculated during trace ingestion. Used for filtering (e.g., "show only root runs") and UI visualization.

**Example query:**

```
metadata_key = 'ls_run_depth' AND metadata_value = 0
```

**Relationships:**

* Determined by trace parent-child structure.
* Cannot be set manually.

### `ls_method`

* **Type:** `string`
* **Set by:** SDK (automatic)

**What it does:**
Indicates which SDK method created the trace (commonly `"traceable"` for `@traceable` decorator).

**When it's used:**
Automatically set by the tracing SDK. Used for debugging and analytics.

**Relationships:**

* Set by SDK based on how trace was created.
* Cannot be set manually.

### `ls_example_*`

* **Type:** Any (depends on example metadata)
* **Pattern:** `ls_example_{original_key}`
* **Set by:** LangSmith experiments system (automatic)

**What it does:**
When running [experiments on datasets](/langsmith/evaluation-quickstart), metadata from the example is automatically prefixed with `ls_example_` and added to the trace.

**Special parameter:**

* `ls_example_dataset_split`: Dataset split (e.g., "train", "test", "validation")

**When it's used:**
During dataset experiments. Allows filtering/grouping by example characteristics.

**Example:**
If example has metadata `{"category": "technical", "difficulty": "hard"}`, trace gets:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "metadata": {
    "ls_example_category": "technical",
    "ls_example_difficulty": "hard",
    "ls_example_dataset_split": "test"
  }
}
```

**Relationships:**

* Automatically derived from example metadata.
* Cannot be set manually on traces.

### `ls_experiment_id`

* **Type:** `string` (UUID)
* **Set by:** LangSmith experiments system (automatic)

**What it does:**
Unique identifier for an experiment run.

**When it's used:**
Automatically added when running [experiments/evaluations on datasets](/langsmith/evaluation-quickstart). Used to group all runs from the same experiment.

**Relationships:**

* Links runs to specific experiments.
* Cannot be set manually.

## Parameter relationships

### Cost tracking dependencies

For LangSmith to automatically calculate costs, several parameters must work together. Here's what's required:

**Primary requirement:** [`ls_provider`](#ls_provider) + [`ls_model_name`](#ls_model_name)

* Both should be present for automatic cost calculation.
* If [`ls_model_name`](#ls_model_name) is missing, system will fall back to checking [`ls_invocation_params`](#ls_invocation_params) for model name.
* [`ls_provider`](#ls_provider) must match a provider in the [pricing database](https://smith.langchain.com/settings/workspaces/models) (or use custom pricing).

**Additional requirements:**

* Run must have `run_type="llm"` (or [arbitrary cost tracking](/langsmith/cost-tracking#other-runs-send-costs) must be enabled).
* [Token usage data](/langsmith/log-llm-trace#provide-token-and-cost-information) must be present in the trace (prompt\_tokens, completion\_tokens).
* Model must exist in pricing database or have [custom pricing configured](/langsmith/cost-tracking#llm-calls-automatically-track-costs-based-on-token-counts).

**Fallback behavior:**
If [`ls_model_name`](#ls_model_name) is not in metadata, the system checks [`ls_invocation_params`](#ls_invocation_params) for model identifiers like `"model"` before giving up on cost tracking.

### Configuration tracking group

These parameters help you track model settings but don't affect LangSmith's core functionality:

**Optional, work independently:** [`ls_temperature`](#ls_temperature), [`ls_max_tokens`](#ls_max_tokens), [`ls_stop`](#ls_stop)

* These are for tracking/display.
* Do not affect LangSmith behavior or cost calculation.
* Useful for experiment comparison and debugging.

### Interrupt rendering

Set [`ls_is_error_interrupt`](#ls_is_error_interrupt) to `true` when a run error should be rendered as interrupted instead of error. This parameter only affects runs that include an error.

### Invocation params special case

The `ls_invocation_params` parameter has a dual role as both a tracking field and a fallback mechanism:

**[`ls_invocation_params`](#ls_invocation_params)**; partially independent with fallback role:

* Primarily stores arbitrary configuration for tracking.
* **Can serve as fallback** for cost tracking if [`ls_model_name`](#ls_model_name) is missing.
* Does not directly affect cost calculation when [`ls_model_name`](#ls_model_name) is present.

### System parameters

These parameters are automatically generated by LangSmith and cannot be manually set:

**Cannot be user-set:** [`ls_run_depth`](#ls_run_depth), [`ls_method`](#ls_method), [`ls_example_*`](#ls_example_), [`ls_experiment_id`](#ls_experiment_id)

* Automatically set by system.
* Used for filtering, analytics, and system tracking.

## Filter traces by metadata parameters

Once you've added `ls_` metadata parameters to your traces, you can use them to filter and search traces programmatically via the [API](/langsmith/smith-api/run/query-runs) or interactively in the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-ls-metadata-parameters). This lets you narrow down traces by model, provider, configuration settings, or trace depth.

### Use the API

Use the [`Client`](https://docs.smith.langchain.com/reference/python/client/langsmith.client.Client) class with the [`list_runs()`](https://docs.smith.langchain.com/reference/python/client/langsmith.client.Client#langsmith.client.Client.list_runs) method (Python) or [`listRuns()`](https://docs.smith.langchain.com/reference/js/classes/client.Client#listruns) method (TypeScript) to query traces based on metadata values. The [filter syntax](/langsmith/trace-query-syntax) supports equality checks, comparisons, and logical operators.

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langsmith import Client

  client = Client()

  # Filter runs by provider
  runs = client.list_runs(
      project_name="my-app",
      filter='metadata_key = "ls_provider" AND metadata_value = "openai"'
  )

  # Filter by specific model
  runs = client.list_runs(
      project_name="my-app",
      filter='metadata_key = "ls_model_name" AND metadata_value = "gpt-5.5"'
  )

  # Filter root runs only (top-level traces)
  runs = client.list_runs(
      project_name="my-app",
      filter='metadata_key = "ls_run_depth" AND metadata_value = 0'
  )

  # Filter by temperature threshold
  runs = client.list_runs(
      project_name="my-app",
      filter='metadata_key = "ls_temperature" AND metadata_value > 0.5'
  )
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { Client } from "langsmith";

  const client = new Client();

  // Filter runs by provider
  const runsByProvider: any[] = [];
  for await (const run of client.listRuns({
    projectName: "my-app",
    filter: 'metadata_key = "ls_provider" AND metadata_value = "openai"'
  })) {
    runsByProvider.push(run);
  }

  // Filter by specific model
  const runsByModel: any[] = [];
  for await (const run of client.listRuns({
    projectName: "my-app",
    filter: 'metadata_key = "ls_model_name" AND metadata_value = "gpt-5.5"'
  })) {
    runsByModel.push(run);
  }

  // Filter root runs only (top-level traces)
  const rootRuns: any[] = [];
  for await (const run of client.listRuns({
    projectName: "my-app",
    filter: 'metadata_key = "ls_run_depth" AND metadata_value = 0'
  })) {
    rootRuns.push(run);
  }

  // Filter by temperature threshold
  const highTempRuns: any[] = [];
  for await (const run of client.listRuns({
    projectName: "my-app",
    filter: 'metadata_key = "ls_temperature" AND metadata_value > 0.5'
  })) {
    highTempRuns.push(run);
  }
  ```
</CodeGroup>

These examples show common filtering patterns:

* **Filter by provider or model** to analyze usage patterns or costs for specific models
* **Filter by run depth** to get only root traces (depth 0) or child runs at specific nesting levels
* **Filter by configuration** to compare experiments with different temperature, max tokens, or other settings

### Use the UI

In the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-ls-metadata-parameters), use the filter/search bar with the [filter syntax](/langsmith/trace-query-syntax):

```
metadata_key = 'ls_provider' AND metadata_value = 'openai'
metadata_key = 'ls_model_name' AND metadata_value = 'gpt-5.5'
metadata_key = 'ls_run_depth' AND metadata_value = 0
```

## Related

* [Cost tracking guide](/langsmith/cost-tracking): Learn how to track and analyze LLM costs in LangSmith.
* [Log LLM traces](/langsmith/log-llm-trace): Format requirements for logging LLM calls with proper token tracking.
* [Trace query syntax](/langsmith/trace-query-syntax): Complete reference for filtering and searching traces.
* [Evaluation quickstart](/langsmith/evaluation-quickstart): Run experiments on datasets to compare model configurations.
* [Add metadata and tags](/langsmith/add-metadata-tags): General guide to adding metadata to traces.
* [Filter traces in application](/langsmith/filter-traces-in-application): Programmatically filter traces in your code.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/ls-metadata-parameters.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Manage contexts with the SDK
Source: https://docs.langchain.com/langsmith/manage-contexts-sdk

Use the LangSmith SDK to push, pull, list, and delete agent and skill repos in the Context Hub programmatically.

Use the LangSmith [Python](/langsmith/smith-python-sdk) and [TypeScript](/langsmith/smith-js-ts-sdk) SDKs to manage **agent repos** and **skill repos** in the [Context Hub](/langsmith/use-the-context-hub) programmatically. [Push](#push-an-agent) new versions from CI, [pull](#pull-an-agent) the latest or a pinned commit at runtime to inject context into your agent, and use additional methods to [check existence](#check-whether-a-repo-exists), [list and search](#list-agents-and-skills) repos, and [delete](#delete-an-agent-or-skill) what you no longer need.

<Note>
  Context Hub methods require `langsmith>=0.7.35` (Python) and `langsmith>=0.5.23` (TypeScript).
</Note>

## Setup

1. Install packages:

   <CodeGroup>
     ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
     pip install -U langsmith
     ```

     ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
     uv add langsmith
     ```

     ```bash TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
     yarn add langsmith
     ```
   </CodeGroup>

2. Configure environment variables. If you already have [`LANGSMITH_API_KEY`](/langsmith/create-account-api-key) set in your environment, skip this step. Otherwise, create one in **Settings > API Keys > Create API Key** in LangSmith, then set it as an environment variable:

   ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
   export LANGSMITH_API_KEY="lsv2_..."
   ```

<Note>
  **Python async:** All methods shown on this page are also available on `AsyncClient` (imported from `langsmith`) with identical signatures—just `await` each call. The TypeScript SDK is async by default; there is no separate async client.
</Note>

## Push an agent

Create a new agent repo or commit a new version of an existing one. If
the repo doesn't exist yet, it is created with the metadata you provide
(`description`, `readme`, `tags`, `is_public`). If it already exists,
those fields are patched only when explicitly passed.

The method returns a URL pointing to the new commit in the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-manage-contexts-sdk):

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langsmith import Client
  from langsmith.schemas import FileEntry

  client = Client()

  url = client.push_agent(
      "email-assistant",
      files={
          "AGENTS.md": FileEntry(
              content="You are an email triage assistant.",
          ),
          "tools.json": FileEntry(content='{"tools": []}'),
      },
      description="Triages and drafts replies to incoming email.",
      tags=["email", "productivity"],
      is_public=False,
  )
  print(url)
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { Client } from "langsmith";

  const client = new Client();

  const url = await client.pushAgent("email-assistant", {
    files: {
      "AGENTS.md": {
        type: "file",
        content: "You are an email triage assistant.",
      },
      "tools.json": { type: "file", content: '{"tools": []}' },
    },
    description: "Triages and drafts replies to incoming email.",
    tags: ["email", "productivity"],
    isPublic: false,
  });
  console.log(url);
  ```
</CodeGroup>

## Push a skill

Identical surface to `push_agent`, but commits to a skill repo. Use
this for reusable capabilities that other agents can depend on:

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langsmith import Client
  from langsmith.schemas import FileEntry

  client = Client()

  url = client.push_skill(
      "deep-research",
      files={
          "SKILL.md": FileEntry(content="Conduct deep multi-step research."),
      },
      description="Multi-step web research with citations.",
      tags=["research"],
  )
  print(url)
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { Client } from "langsmith";

  const client = new Client();

  const url = await client.pushSkill("deep-research", {
    files: {
      "SKILL.md": {
        type: "file",
        content: "Conduct deep multi-step research.",
      },
    },
    description: "Multi-step web research with citations.",
    tags: ["research"],
  });
  console.log(url);
  ```
</CodeGroup>

### Link to other repos

Instead of inlining file content, an entry in `files` can be a link to
another agent or skill repo, which lets you compose contexts without duplicating
content across repos. For example, an agent that delegates to a shared skill.

If you omit `commit_id`, LangSmith links to the latest commit of that repo when you push this commit. If the linked repo updates later, LangSmith propagates that update to parent repos that reference it.

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langsmith import Client
  from langsmith.schemas import AgentEntry, FileEntry, SkillEntry

  client = Client()

  url = client.push_agent(
      "email-assistant",
      files={
          "AGENTS.md": FileEntry(content="You are an email triage assistant."),
          # Link to the deep-research skill repo. Omit commit_id to always
          # resolve to the latest version, or pin it for reproducibility.
          "skills/research": SkillEntry(repo_handle="deep-research"),
          # Link to another agent repo.
          "agents/scheduler": AgentEntry(repo_handle="calendar-agent"),
      },
  )
  print(url)
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { Client } from "langsmith";

  const client = new Client();

  const url = await client.pushAgent("email-assistant", {
    files: {
      "AGENTS.md": { type: "file", content: "You are an email triage assistant." },
      // Link to the deep-research skill repo. Omit commit_id to always
      // resolve to the latest version, or pin it for reproducibility.
      "skills/research": { type: "skill", repo_handle: "deep-research" },
      // Link to another agent repo.
      "agents/scheduler": { type: "agent", repo_handle: "calendar-agent" },
    },
  });
  console.log(url);
  ```
</CodeGroup>

## Push parameters

Both `push_agent` / `pushAgent` and `push_skill` / `pushSkill` accept the following parameters:

| Parameter                        | Type                       | Description                                                                                                                                                         |
| -------------------------------- | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `identifier`                     | `string`                   | The repo's identifier.                                                                                                                                              |
| `files`                          | `dict[str, Entry \| None]` | Map of file path to `Entry`. Pass `None` / `null` to delete a path in this commit.                                                                                  |
| `parent_commit` / `parentCommit` | `string` (optional)        | Parent commit hash prefix for optimistic concurrency. Must be 8–64 characters when provided. If it doesn't match the latest commit, the API returns a 409 conflict. |
| `description`                    | `string` (optional)        | Repo description. Set on creation or patched on update.                                                                                                             |
| `readme`                         | `string` (optional)        | Repo readme content.                                                                                                                                                |
| `tags`                           | `string[]` (optional)      | Repo tags.                                                                                                                                                          |
| `is_public` / `isPublic`         | `boolean` (optional)       | Whether the repo is publicly discoverable.                                                                                                                          |

## Pull an agent

Pull a snapshot of an agent repo. By default the latest commit is returned; pass a commit hash or tag via `version` (or embed it in the identifier as `owner/name:version`) to pull a specific version:

<Note>
  **Identifier formats**: the `identifier` argument accepts three forms:

  * `name`: resolves against the current workspace owner.
  * `owner/name`: fully qualified.
  * `owner/name:version`: pinned to a specific commit hash or tag.

  The optional `version` argument overrides any version embedded in the
  identifier. If neither is provided, the latest commit is returned.
</Note>

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langsmith import Client

  client = Client()

  agent = client.pull_agent("email-assistant")
  print(agent.commit_hash)
  print(list(agent.files))

  # Pull a specific commit.
  pinned = client.pull_agent("email-assistant", version="7ca95573")

  # Pull a tagged commit (for example, the production tag).
  prod = client.pull_agent("email-assistant:production")
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { Client } from "langsmith";

  const client = new Client();

  const agent = await client.pullAgent("email-assistant");
  console.log(agent.commit_hash);
  console.log(Object.keys(agent.files));

  // Pull a specific commit.
  const pinned = await client.pullAgent("email-assistant", {
    version: "7ca95573",
  });

  // Pull a tagged commit.
  const prod = await client.pullAgent("email-assistant:production");
  ```
</CodeGroup>

## Pull a skill

Pull a snapshot of a skill repo. Works identically to `pull_agent` but returns a `SkillContext`:

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langsmith import Client

  client = Client()

  skill = client.pull_skill("deep-research")
  print(skill.files["SKILL.md"].content)
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { Client } from "langsmith";

  const client = new Client();

  const skill = await client.pullSkill("deep-research");
  const skillFile = skill.files["SKILL.md"];
  if (skillFile.type === "file") {
    console.log(skillFile.content);
  }
  ```
</CodeGroup>

## Pull parameters

Both `pull_agent` / `pullAgent` and `pull_skill` / `pullSkill` accept the following parameters:

| Parameter    | Type                | Description                                                                   |
| ------------ | ------------------- | ----------------------------------------------------------------------------- |
| `identifier` | `string`            | The repo's identifier. May include an inline version: `owner/name:version`.   |
| `version`    | `string` (optional) | Commit hash or tag to pull. Overrides any version embedded in the identifier. |

`pull_agent` returns an `AgentContext`; `pull_skill` returns a `SkillContext`.

## Check whether a repo exists

Use these methods to check whether an agent or skill repo exists in your
workspace before pushing or pulling:

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langsmith import Client

  client = Client()

  if client.agent_exists("email-assistant"):
      print("agent already exists")

  if not client.skill_exists("deep-research"):
      print("skill not found")
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { Client } from "langsmith";

  const client = new Client();

  if (await client.agentExists("email-assistant")) {
    console.log("agent already exists");
  }

  if (!(await client.skillExists("deep-research"))) {
    console.log("skill not found");
  }
  ```
</CodeGroup>

## List agents and skills

List repos of either type, with optional filters for visibility, archived state, and a search query:

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langsmith import Client

  client = Client()

  # Python returns a paginated response.
  result = client.list_agents(limit=20, query="email")
  for repo in result.repos:
      print(repo.repo_handle)

  skills = client.list_skills(is_public=True)
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { Client } from "langsmith";

  const client = new Client();

  // TypeScript yields one repo at a time, auto-paginating.
  for await (const repo of client.listAgents({ query: "email" })) {
    console.log(repo.repo_handle);
  }

  for await (const skill of client.listSkills({ isPublic: true })) {
    console.log(skill.repo_handle);
  }
  ```
</CodeGroup>

| Parameter                    | Type                 | Description                                                           |
| ---------------------------- | -------------------- | --------------------------------------------------------------------- |
| `limit`                      | `int` (Python only)  | Maximum number of repos to return per page. Defaults to 100.          |
| `offset`                     | `int` (Python only)  | Number of repos to skip. Defaults to 0.                               |
| `is_public` / `isPublic`     | `boolean` (optional) | Filter to only public (or only private) repos.                        |
| `is_archived` / `isArchived` | `boolean` (optional) | Filter by archived state. Defaults to `False`.                        |
| `query`                      | `string` (optional)  | Search query across repo handle, owner handle, description, and tags. |

<Note>
  Python's `list_agents` / `list_skills` return a paginated response object with explicit
  `limit` and `offset` for manual pagination. TypeScript's `listAgents` / `listSkills`
  return an `AsyncIterableIterator` that handles pagination automatically as you
  consume it.
</Note>

## Delete an agent or skill

<Warning>
  This operation is permanent and cannot be undone. Deleting a repo also
  removes its owned child file repos.
</Warning>

Delete an agent or skill repo from your workspace:

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langsmith import Client

  client = Client()

  client.delete_agent("email-assistant")
  client.delete_skill("deep-research")
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { Client } from "langsmith";

  const client = new Client();

  await client.deleteAgent("email-assistant");
  await client.deleteSkill("deep-research");
  ```
</CodeGroup>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/manage-contexts-sdk.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Manage datasets
Source: https://docs.langchain.com/langsmith/manage-datasets

LangSmith provides tools for managing and working with your [*datasets*](/langsmith/evaluation-concepts#datasets). This page describes dataset operations including:

* [Versioning datasets](#version-a-dataset) to track changes over time.
* [Filtering](#evaluate-on-a-filtered-view-of-a-dataset) and [splitting](#evaluate-on-a-dataset-split) datasets for evaluation.
* [Sharing datasets](#share-a-dataset) publicly.
* [Exporting datasets](#export-a-dataset) in various formats.

You'll also learn how to [export filtered traces](#export-filtered-traces-from-experiment-to-dataset) from [experiments](/langsmith/evaluation-concepts#experiment) back to datasets for further analysis and iteration.

<Tip>
  The [LangSmith Engine](/langsmith/engine) can automatically generate ground truth dataset examples from your production traces.
</Tip>

## Version a dataset

In LangSmith, datasets are versioned. This means that every time you add, update, or delete examples in your dataset, a new version of the dataset is created.

### Create a new version of a dataset

Any time you add, update, or delete examples in your dataset, a new [version](/langsmith/evaluation-concepts#dataset-organization) of your dataset is created. This allows you to track changes to your dataset over time and understand how your dataset has evolved.

By default, the version is defined by the timestamp of the change. When you click on a particular version of a dataset (by timestamp) in the **Examples** tab, you will find the state of the dataset at that point in time.

<img alt="Version Datasets" />

Note that examples are read-only when viewing a past version of the dataset. You will also see the operations that were between this version of the dataset and the latest version of the dataset.

<Note>
  By default, the latest version of the dataset is shown in the **Examples** tab and experiments from all versions are shown in the **Tests** tab.
</Note>

In the **Tests** tab, you will find the results of tests run on the dataset at different versions.

<img alt="Version Datasets" />

### Tag a version

You can also tag versions of your dataset to give them a more human-readable name, which can be useful for marking important milestones in your dataset's history.

For example, you might tag a version of your dataset as "prod" and use it to run tests against your LLM pipeline.

You can tag a version of your dataset in the UI by clicking on **+ Tag this version** in the **Examples** tab.

<img alt="Tagging Datasets" />

You can also tag versions of your dataset using the SDK. Here's an example of how to tag a version of a dataset using the [Python SDK](https://docs.smith.langchain.com/reference/python/reference):

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langsmith import Client
from datetime import datetime

client = Client()
initial_time = datetime(2024, 1, 1, 0, 0, 0) # The timestamp of the version you want to tag
