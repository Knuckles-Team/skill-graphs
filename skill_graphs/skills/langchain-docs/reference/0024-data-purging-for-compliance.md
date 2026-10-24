# Data purging for compliance
Source: https://docs.langchain.com/langsmith/data-purging-compliance

This guide covers the various features available after data reaches LangSmith Cloud servers to help you achieve your privacy goals.

## Data retention

LangSmith provides automatic data retention capabilities to help with compliance and storage management. Data retention policies can be configured at two levels:

* **Workspace level**: Enterprise customers with the required permissions can set extended retention as the workspace default and customize the retention duration (up to 400 days). See [Customize extended retention policy](#customize-extended-retention-policy).
* **Project level**: Customers with the required permissions can set the default retention tier per tracing project, choosing between base (14 days) or extended retention (400 days). See [Change project-level default retention](/langsmith/billing#change-project-level-default-retention).

For detailed information about data retention configuration and management, please refer to the [Data Retention concepts](/langsmith/usage-and-billing#data-retention) documentation.

## Customize extended retention policy

<Note>
  This feature is available for [Enterprise](/langsmith/pricing-plans) plan customers. For [self-hosted](/langsmith/self-hosted) Enterprise customers, refer to the [workspace-level configuration section](#workspace-level-extended-retention-for-self-hosted).
</Note>

[Enterprise](/langsmith/pricing-plans) customers can customize the extended data retention period for traces at the [workspace](/langsmith/administration-overview#workspaces) level to meet specific compliance requirements. By default, extended retention is set to 400 days, but you can adjust this based on your organization's needs. Changes to the retention period apply to new traces only.

<Note>
  Changes to the retention period apply to new traces only. Existing traces are not affected.
</Note>

### Configure extended retention

Organization Admins and Operators (`organization:manage`) can configure retention for any workspace. Workspace Admins can configure their own workspace (`workspaces:manage`). For a full permissions reference, see [Organization and workspace operations](/langsmith/organization-workspace-operations).

<Tabs>
  <Tab title="UI">
    In the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-data-purging-compliance):

    1. Navigate to **Settings** at the bottom of the page.
    2. Select **Usage configuration** from the left-hand menu.
    3. Find the workspace in the list that you would like to configure.
    4. Click on the value under the **Data retention policy** column for that workspace.
    5. On the **workspace usage configurations** modal, customize the extended policy using the dropdown for **Extended - All traces are retained for** option. Available durations are: 30d, 60d, 90d, 120d, 150d, 180d, 240d, 300d, 365d, and 400d.
    6. Select **Save**.
  </Tab>

  <Tab title="API">
    To read current settings:

    **Organization level** (`organization:manage`)

    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    curl -X GET "https://api.smith.langchain.com/api/v1/orgs/ttl-settings" \
      -H "x-api-key: YOUR_API_KEY"
    ```

    **Workspace level** (`workspaces:manage`)

    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    curl -X GET "https://api.smith.langchain.com/api/v1/ttl-settings" \
      -H "x-api-key: YOUR_API_KEY"
    ```

    To update the retention period, set `resource_type` to `"run"` for traces and `ttl_days` to your desired duration. Available durations are: 30, 60, 90, 120, 150, 180, 240, 300, 365, and 400 days.

    **Organization level** (`organization:manage`)

    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    curl -X PUT "https://api.smith.langchain.com/api/v1/orgs/ttl-settings" \
      -H "x-api-key: YOUR_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{"resource_type": "run", "ttl_days": 90}'
    ```

    **Workspace level** (`workspaces:manage`)

    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    curl -X PUT "https://api.smith.langchain.com/api/v1/ttl-settings" \
      -H "x-api-key: YOUR_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{"resource_type": "run", "ttl_days": 90}'
    ```
  </Tab>
</Tabs>

### Workspace-level extended retention for self-hosted

Self-hosted [Enterprise](/langsmith/pricing-plans) customers can also use workspace-level extended retention configuration instead of system-wide TTL settings. This provides more granular control over data retention for different workspaces without requiring environment variable changes.

<Warning>
  If you use blob storage, you **must** add a lifecycle rule for each custom retention period you configure. For example, setting a workspace to 90-day retention means blob data is written to the `ttl_90d/` prefix, which requires a matching lifecycle rule to be cleaned up automatically. See [blob storage TTL configuration](/langsmith/self-host-blob-storage#custom-workspace-level-retention-prefixes) for details and examples.
</Warning>

To configure this for self-hosted deployments, refer to the [self-hosted TTL documentation](/langsmith/self-host-ttl) for the legacy system-wide approach or contact [support](https://support.langchain.com).

## Trace deletes

You can use the API to complete trace deletes. The API supports two methods for deleting traces:

1. **By trace IDs and session ID**: Delete specific traces by providing a list of trace IDs and their corresponding session ID (up to 1000 traces per request)
2. **By metadata**: Delete traces across a workspace that match any of the specified metadata key-value pairs

For more details, refer to the [API spec](/langsmith/smith-api/run/delete-runs).

<Warning>
  All trace deletions will delete related entities like feedbacks, aggregations, and stats across all data storages.
</Warning>

### Deletion timeline

Trace deletions are processed during non-peak usage times and are not instant. LangChain runs the delete job on the weekend. There is no confirmation of deletion - you'll need to query the data again to verify it has been removed.

### Delete specific traces

To delete specific traces by their trace IDs from a single session:

<Note>
  The `session_id` is the project ID for the trace you are trying to delete. You can find it on the tracing project page in the LangSmith UI.
</Note>

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
curl -X POST "https://api.smith.langchain.com/api/v1/runs/delete" \
  -H "x-api-key: YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "trace_ids": ["trace-id-1", "trace-id-2", "trace-id-3"],
    "session_id": "session-id-1"
  }'
```

### Delete by metadata

When deleting by metadata:

* Accepts a `metadata` object of key/value pairs. KV pair matching uses an **or** condition. A trace will match if it has **any** of the key-value pairs specified in metadata (not all)
* You don't need to specify a session id when deleting by metadata. Deletes will apply across the workspace.

To delete traces based on metadata across a workspace (matches **any** of the metadata key-value pairs):

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
curl -X POST "https://api.smith.langchain.com/api/v1/runs/delete" \
  -H "x-api-key: YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "metadata": {
      "user_id": "user123",
      "environment": "staging"
    }
  }'
```

This will delete traces that have either `user_id: "user123"` **or** `environment: "staging"` in their metadata.

<Warning>
  Remember that you can only schedule up to 1000 traces per session per request. For larger deletions, you'll need to make multiple requests.
</Warning>

## Example deletes

You can delete dataset examples self-serve via our API, which supports both soft and hard deletion methods depending on your data retention needs.

<Warning>
  Hard deletes will permanently remove inputs, outputs, and metadata from ALL versions of the specified examples across the entire dataset history.
</Warning>

### Deleting examples is a two-step process

For bulk operations, example deletion follows a two-step process:

#### 1. Search for examples by metadata

Find all examples with matching metadata across all datasets in a workspace.

[GET /examples](/langsmith/smith-api/examples/read-examples)

* `as_of` must be explicitly specified as a timestamp. Only examples created before the `as_of` date will be returned

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
curl -X GET "https://api.smith.langchain.com/api/v1/examples?as_of=2024-01-01T00:00:00Z" \
  -H "x-api-key: YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "metadata": {
      "user_id": "user123",
      "environment": "staging"
    }
  }'
```

This will return examples that have either `user_id: "user123"` **or** `environment: "staging"` in their metadata across all datasets in your workspace.

#### 2. Hard delete examples

Once you have the example IDs, send a delete request. This will zero-out the inputs, outputs, and metadata from all versions of the dataset for that example.

[POST /v1/platform/datasets/examples/delete/](/langsmith/smith-api/examples/hard-delete-examples)

* Specify `example_ids` (list of example IDs) and `hard_delete` (boolean) in the request body

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
curl -X POST "https://api.smith.langchain.com/v1/platform/datasets/examples/delete/" \
  -H "x-api-key: YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "example_ids": ["example-id-1", "example-id-2", "example-id-3"],
    "hard_delete": true
  }'
```

### Deletion types

#### Soft delete (default)

* Creates tombstoned entries with NULL inputs/outputs in the dataset
* Preserves historical data and maintains dataset versioning
* Only affects the current version of the dataset

#### Hard delete

* Permanently removes inputs, outputs, and metadata from ALL dataset versions
* Complete data removal when compliance requires zero-out across all versions
* Set `"hard_delete": true` in the request body

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/data-purging-compliance.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Data storage and privacy
Source: https://docs.langchain.com/langsmith/data-storage-and-privacy

This document describes how data is processed in the LangGraph CLI and the Agent Server for both the in-memory server (`langgraph dev`) and the local Docker server (`langgraph up`). It also describes what data is tracked when interacting with the hosted Studio frontend.

## CLI

LangGraph **CLI** is the command-line interface for building and running LangGraph applications; see the [CLI guide](/langsmith/cli) to learn more.

By default, calls to most CLI commands log a single analytics event upon invocation. This helps us better prioritize improvements to the CLI experience. Each telemetry event contains the calling process's OS, OS version, Python version, the CLI version, the command name (`dev`, `up`, `run`, etc.), and booleans representing whether a flag was passed to the command. For more information, see the [full analytics logic](https://github.com/langchain-ai/langgraph/blob/main/libs/cli/langgraph-cli/analytics.py).

You can disable all CLI telemetry by setting `LANGGRAPH_CLI_NO_ANALYTICS=1`.

<a />

## Agent Server

The [Agent Server](/langsmith/agent-server) provides a durable execution runtime that relies on persisting checkpoints of your application state, long-term memories, thread metadata, assistants, and similar resources to the local file system or a database. Unless you have deliberately customized the storage location, this information is either written to local disk (for `langgraph dev`) or a PostgreSQL database (for `langgraph up` and in all deployments).

### LangSmith tracing

When running the Agent server (either in-memory or in Docker), LangSmith tracing may be enabled to facilitate faster debugging and offer observability of graph state and LLM prompts in production. You can always disable tracing by setting `LANGSMITH_TRACING=false` in your server's runtime environment.

<Note>
  For more granular control, you can use [conditional tracing](/langsmith/conditional-tracing) to selectively enable or disable tracing based on runtime conditions, such as client requirements or data sensitivity.
</Note>

<a />

### In-memory development server

`langgraph dev` runs an [in-memory development server](/langsmith/local-dev-testing) as a single Python process, designed for quick development and testing. It saves all checkpointing and memory data to disk within a `.langgraph_api` directory in the current working directory. Apart from the telemetry data described in the [CLI](#cli) section, no data leaves the machine unless you have enabled tracing or your graph code explicitly contacts an external service.

<a />

### Standalone Server

`langgraph up` builds your local package into a Docker image and runs the server as the [data plane](/langsmith/self-hosted) consisting of three containers: the API server, a PostgreSQL container, and a Redis container. All persistent data (checkpoints, assistants, etc.) are stored in the PostgreSQL database. Redis is used as a pubsub connection for real-time streaming of events. You can encrypt all checkpoints before saving to the database by setting a valid `LANGGRAPH_AES_KEY` environment variable. You can also specify [TTLs](/langsmith/configure-ttl) for checkpoints and cross-thread memories in `langgraph.json` to control how long data is stored. All persisted threads, memories, and other data can be deleted via the relevant API endpoints.

Additional API calls are made to confirm that the server has a valid license and to track the number of executed runs and tasks. Periodically, the API server validates the provided license key (or API key).

If you've disabled [tracing](#langsmith-tracing), no user data is persisted externally unless your graph code explicitly contacts an external service.

## Studio

[Studio](/langsmith/studio) is a graphical interface for interacting with your Agent Server. It does not persist any private data (the data you send to your server is not sent to LangSmith). Though the Studio interface is served at [smith.langchain.com](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-data-storage-and-privacy), it is run in your browser and connects directly to your local Agent Server so that no data needs to be sent to LangSmith.

If you are logged in, LangSmith does collect some usage analytics to help improve the debugging user experience. This includes:

* Page visits and navigation patterns
* User actions (button clicks)
* Browser type and version
* Screen resolution and viewport size

Importantly, no application data or code (or other sensitive configuration details) are collected. All of that is stored in the persistence layer of your Agent Server. When using Studio anonymously, no account creation is required and usage analytics are not collected.

## Quick reference

In summary, you can opt-out of server-side telemetry by turning off CLI analytics and disabling tracing.

| Variable                       | Purpose                   | Default                |
| ------------------------------ | ------------------------- | ---------------------- |
| `LANGGRAPH_CLI_NO_ANALYTICS=1` | Disable CLI analytics     | Analytics enabled      |
| `LANGSMITH_API_KEY`            | Enable LangSmith tracing  | Tracing disabled       |
| `LANGSMITH_TRACING=false`      | Disable LangSmith tracing | Depends on environment |

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/data-storage-and-privacy.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Dataset prebuilt JSON schema types
Source: https://docs.langchain.com/langsmith/dataset-json-types

LangSmith recommends that you set a schema on the inputs and outputs of your dataset schemas to ensure data consistency and that your examples are in the right format for downstream processing, like running evals.

In order to better support LLM workflows, LangSmith has support for a few different predefined prebuilt types. These schemas are hosted publicly by the LangSmith API, and can be defined in your dataset schemas using [JSON Schema references](https://json-schema.org/understanding-json-schema/structuring#dollarref). The table of available schemas can be seen below

| Type    | JSON Schema Reference Link                                                                                                       | Usage                                                                                                                     |
| ------- | -------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| Message | [https://api.smith.langchain.com/public/schemas/v1/message.json](https://api.smith.langchain.com/public/schemas/v1/message.json) | Represents messages sent to a chat model, following the OpenAI standard format.                                           |
| Tool    | [https://api.smith.langchain.com/public/schemas/v1/tooldef.json](https://api.smith.langchain.com/public/schemas/v1/tooldef.json) | Tool definitions available to chat models for function calling, defined in OpenAI's JSON Schema inspired function format. |

LangSmith lets you define a series of transformations that collect the above prebuilt types from your traces and add them to your dataset. For more info on available transformations, see our [reference](/langsmith/dataset-transformations)

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/dataset-json-types.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Dataset transformations
Source: https://docs.langchain.com/langsmith/dataset-transformations

LangSmith allows you to attach transformations to fields in your dataset's schema that apply to your data before it is added to your dataset, whether that be from UI, API, or run rules.

Coupled with [LangSmith's prebuilt JSON schema types](/langsmith/dataset-json-types), these allow you to do easy preprocessing of your data before saving it into your datasets.

## Transformation types

| Transformation Type         | Target Types                                                               | Functionality                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| --------------------------- | -------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `remove_system_messages`    | `Array[Message]`                                                           | Filters a list of messages to remove any system messages.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `convert_to_openai_message` | Message `Array[Message]`                                                   | Converts any incoming data from LangChain's internal serialization format to OpenAI's standard message format using langchain's [`convert_to_openai_messages`](https://reference.langchain.com/python/langchain_core/utils/#langchain_core.utils.function_calling.convert_to_openai_messages). If the target field is marked as required, and no matching message is found upon entry, it will attempt to extract a message (or list of messages) from several well-known LangSmith tracing formats (e.g., any traced LangChain [`BaseChatModel`](https://reference.langchain.com/python/langchain-core/language_models/chat_models/BaseChatModel) run or traced run from the [LangSmith OpenAI wrapper](/langsmith/annotate-code#use-%40traceable-%2F-traceable)), and remove the original key containing the message. |
| `convert_to_openai_tool`    | `Array[Tool]` Only available on top level fields in the inputs dictionary. | Converts any incoming data into OpenAI standard tool formats here using langchain's [`convert_to_openai_tool`](https://reference.langchain.com/python/langchain-core/utils/function_calling/convert_to_openai_tool) Will extract tool definitions from a run's invocation parameters if present / no tools are found at the specified key. This is useful because LangChain chat models trace tool definitions to the `extra.invocation_params` field of the run rather than inputs.                                                                                                                                                                                                                                                                                                                                    |
| `remove_extra_fields`       | `Object`                                                                   | Removes any field not defined in the schema for this target object.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

## Chat model prebuilt schema

The main use case for transformations is to simplify collecting production traces into datasets in a format that can be standardized across model providers for usage in evaluations / few shot prompting / etc downstream.

To simplify setup of transformations for our end users, LangSmith offers a pre-defined schema that will do the following:

* Extract messages from your collected runs and transform them into the openai standard format, which makes them compatible all LangChain ChatModels and most model providers' SDK for downstream evaluation and experimentation
* Extract any tools used by your LLM and add them to your example's input to be used for reproducibility in downstream evaluation

<Check>
  Users who want to iterate on their system prompts often also add the Remove System Messages transformation on their input messages when using our Chat Model schema, which will prevent you from saving the system prompt to your dataset.
</Check>

### Compatibility

The LLM run collection schema is built to collect data from LangChain [`BaseChatModel`](https://reference.langchain.com/python/langchain-core/language_models/chat_models/BaseChatModel) runs or traced runs from the [LangSmith OpenAI wrapper](/langsmith/annotate-code#use-%40traceable-%2F-traceable).

Please contact support via [support.langchain.com](https://support.langchain.com) if you have an LLM run you are tracing that is not compatible and we can extend support.

If you want to apply transformations to other sorts of runs (for example, representing LangGraph state with message history), please define your schema directly and manually add the relevant transformations.

### Enablement

When adding a run from a tracing project or annotation queue to a dataset, if it has the LLM run type, we will apply the Chat Model schema by default.

For enablement on new datasets, see our [dataset management how-to guide](/langsmith/manage-datasets-in-application).

### Specs

For the full API specs of the prebuilt schema, see the below sections:

#### Input schema

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "type": "object",
  "properties": {
    "messages": {
      "type": "array",
      "items": {
        "$ref": "https://api.smith.langchain.com/public/schemas/v1/message.json"
      }
    },
    "tools": {
      "type": "array",
      "items": {
        "$ref": "https://api.smith.langchain.com/public/schemas/v1/tooldef.json"
      }
    }
  },
  "required": ["messages"]
}
```

#### Output schema

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "type": "object",
  "properties": {
    "message": {
      "$ref": "https://api.smith.langchain.com/public/schemas/v1/message.json"
    }
  },
  "required": ["message"]
}
```

#### Transformations

And the transformations look as follows:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
[
  {
    "path": ["inputs"],
    "transformation_type": "remove_extra_fields"
  },
  {
    "path": ["inputs", "messages"],
    "transformation_type": "convert_to_openai_message"
  },
  {
    "path": ["inputs", "tools"],
    "transformation_type": "convert_to_openai_tool"
  },
  {
    "path": ["outputs"],
    "transformation_type": "remove_extra_fields"
  },
  {
    "path": ["outputs", "message"],
    "transformation_type": "convert_to_openai_message"
  }
]
```

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/dataset-transformations.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# How to define a target function to evaluate
Source: https://docs.langchain.com/langsmith/define-target-function

There are three main pieces need to run an evaluation:

1. A [dataset](/langsmith/evaluation-concepts#datasets) of test inputs and expected outputs.
2. A target function which is what you're evaluating.
3. [Evaluators](/langsmith/evaluation-concepts#evaluators) that score your target function's outputs.

This guide shows you how to define the target function depending on the part of your application you are evaluating. See here for [how to create a dataset](/langsmith/manage-datasets-programmatically) and [how to define evaluators](/langsmith/code-evaluator-ui), and here for an [end-to-end example of running an evaluation](/langsmith/evaluate-llm-application).

## Target function signature

In order to evaluate an application in code, we need a way to run the application. When using `evaluate()` ([Python](https://reference.langchain.com/python/langsmith/client/Client/evaluate) / [JavaScript](https://reference.langchain.com/javascript/functions/langsmith.evaluation.evaluate.html)) we'll do this by passing in a *target function* argument. This is a function that takes in a dataset [Example's](/langsmith/evaluation-concepts#examples) inputs and returns the application output as a dict. Within this function we can call our application however we'd like. We can also format the output however we'd like. The key is that any evaluator functions we define should work with the output format we return in our target function.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langsmith import Client

# 'inputs' will come from your dataset.
def dummy_target(inputs: dict) -> dict:
    return {"foo": 1, "bar": "two"}

# 'inputs' will come from your dataset.

# 'outputs' will come from your target function.
def evaluator_one(inputs: dict, outputs: dict) -> bool:
    return outputs["foo"] == 2

def evaluator_two(inputs: dict, outputs: dict) -> bool:
    return len(outputs["bar"]) < 3

client = Client()
results = client.evaluate(
    dummy_target,  # <-- target function
    data="your-dataset-name",
    evaluators=[evaluator_one, evaluator_two],
    ...
)
```

<Check>
  `evaluate()` will automatically trace your target function. This means that if you run any traceable code within your target function, this will also be traced as child runs of the target trace.
</Check>

## Example: Single LLM call

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langsmith import wrappers
  from openai import OpenAI

  # Optionally wrap the OpenAI client to automatically
  # trace all model calls.
  oai_client = wrappers.wrap_openai(OpenAI())

  def target(inputs: dict) -> dict:
    # This assumes your dataset has inputs with a 'messages' key.
    # You can update to match your dataset schema.
    messages = inputs["messages"]
    response = oai_client.chat.completions.create(
        messages=messages,
        model="gpt-5.4-mini",
    )
    return {"answer": response.choices[0].message.content}
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import OpenAI from 'openai';
  import { wrapOpenAI } from "langsmith/wrappers";

  const client = wrapOpenAI(new OpenAI());

  // This is the function you will evaluate.
  const target = async(inputs) => {
    // This assumes your dataset has inputs with a `messages` key
    const messages = inputs.messages;
    const response = await client.chat.completions.create({
        messages: messages,
        model: 'gpt-5.4-mini',
    });
    return { answer: response.choices[0].message.content };
  }
  ```

  ```python Python (LangChain) theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langchain.chat_models import init_chat_model

  model = init_chat_model("gpt-5.4-mini")

  def target(inputs: dict) -> dict:
    # This assumes your dataset has inputs with a `messages` key
    messages = inputs["messages"]
    response = model.invoke(messages)
    return {"answer": response.content}
  ```

  ```typescript TypeScript (LangChain) theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { ChatOpenAI } from '@langchain/openai';

  // This is the function you will evaluate.
  const target = async(inputs) => {
    // This assumes your dataset has inputs with a `messages` key
    const messages = inputs.messages;
    const model = new ChatOpenAI({ model: "gpt-5.4-mini" });
    const response = await model.invoke(messages);
    return {"answer": response.content};
  }
  ```
</CodeGroup>

## Example: Non-LLM component

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langsmith import traceable

  # Optionally decorate with '@traceable' to trace all invocations of this function.
  @traceable
  def calculator_tool(operation: str, number1: float, number2: float) -> str:
    if operation == "add":
        return str(number1 + number2)
    elif operation == "subtract":
        return str(number1 - number2)
    elif operation == "multiply":
        return str(number1 * number2)
    elif operation == "divide":
        return str(number1 / number2)
    else:
        raise ValueError(f"Unrecognized operation: {operation}.")

  # This is the function you will evaluate.
  def target(inputs: dict) -> dict:
    # This assumes your dataset has inputs with `operation`, `num1`, and `num2` keys.
    operation = inputs["operation"]
    number1 = inputs["num1"]
    number2 = inputs["num2"]
    result = calculator_tool(operation, number1, number2)
    return {"result": result}
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { traceable } from "langsmith/traceable";

  // Optionally wrap in 'traceable' to trace all invocations of this function.
  const calculatorTool = traceable(async ({ operation, number1, number2 }) => {
  // Functions must return strings
  if (operation === "add") {
    return (number1 + number2).toString();
  } else if (operation === "subtract") {
    return (number1 - number2).toString();
  } else if (operation === "multiply") {
    return (number1 * number2).toString();
  } else if (operation === "divide") {
    return (number1 / number2).toString();
  } else {
    throw new Error("Invalid operation.");
  }
  });

  // This is the function you will evaluate.
  const target = async (inputs) => {
  // This assumes your dataset has inputs with `operation`, `num1`, and `num2` keys
  const result = await calculatorTool.invoke({
    operation: inputs.operation,
    number1: inputs.num1,
    number2: inputs.num2,
  });
  return { result };
  }
  ```
</CodeGroup>

## Example: Application or agent

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from my_agent import agent

        # This is the function you will evaluate.
  def target(inputs: dict) -> dict:
    # This assumes your dataset has inputs with a `messages` key
    messages = inputs["messages"]
    # Replace `invoke` with whatever you use to call your agent
    response = agent.invoke({"messages": messages})
    # This assumes your agent output is in the right format
    return response
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { agent } from 'my_agent';

  // This is the function you will evaluate.
  const target = async(inputs) => {
  // This assumes your dataset has inputs with a `messages` key
  const messages = inputs.messages;
  // Replace `invoke` with whatever you use to call your agent
  const response = await agent.invoke({ messages });
  // This assumes your agent output is in the right format
  return response;
  }
  ```
</CodeGroup>

<Check>
  If you have a LangGraph/LangChain agent that accepts the inputs defined in your dataset and that returns the output format you want to use in your evaluators, you can pass that object in as the target directly:

  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from my_agent import agent
  from langsmith import Client
  client = Client()
  client.evaluate(agent, ...)
  ```
</Check>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/define-target-function.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Deploy Google ADK agents
Source: https://docs.langchain.com/langsmith/deploy-google-adk

Deploy Google Agent Development Kit (ADK) agents to LangSmith Agent Server using the deployments-wrap-sdk package.

This guide shows you how to deploy a [Google Agent Development Kit (ADK)](https://github.com/google/adk-python) agent on [LangSmith Agent Server](/langsmith/agent-server) using the [`deployments-wrap-sdk`](https://pypi.org/project/deployments-wrap-sdk/) package.

`deployments-wrap-sdk` provides a thin wrapper that turns a configured ADK `Runner` into a LangGraph-compatible graph, so you can deploy ADK agents without writing the [Functional API](/oss/python/langgraph/functional-api) glue yourself. The wrapper:

* Bridges ADK sessions to Agent Server's [checkpoint persistence](/langsmith/agent-server#persistence), so session state survives restarts and resumes across runs.
* Forwards ADK token events through LangGraph's streaming pipeline, so partial tokens show up in [`stream_mode="messages"`](/langsmith/streaming) and in [LangSmith Studio](/langsmith/studio).
* Automatically enables [LangSmith tracing](/langsmith/trace-with-google-adk) for ADK when `LANGSMITH_TRACING` is set.

## Prerequisites

* Python 3.11+
* [LangGraph CLI](/langsmith/cli) for local dev and deployment
* A LangSmith API key, refer to [Create an account and API key](https://docs.langchain.com/langsmith/create-account-api-key)
* A Google AI API key if you use Gemini models, refer to [Google AI Studio](https://aistudio.google.com/api-keys)

## Installation

Install the package with the `google-adk` extra. The extra pulls in `google-adk` and other dependencies needed for the wrapper:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
pip install "deployments-wrap-sdk[google-adk]"
```

<Note>
  The PyPI distribution name is `deployments-wrap-sdk`, but the Python import path is `saf_sdk`. Both refer to the same package.
</Note>

## Quickstart

This minimal example builds an agent that returns the input as its response and does not require a model API key. The agent bypasses the LLM call so you can verify that the deployment works correctly before connecting a real model.

Create `agent.py`:

```python agent.py theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from google.adk.agents import Agent
from google.adk.models.llm_response import LlmResponse
from google.adk.runners import Runner
from google.genai.types import Content, Part
from saf_sdk.adk import LangsmithSessionService, wrap

def echo_callback(callback_context, llm_request):
    """Return the user's message instead of calling a real model."""
    user_text = ""
    if callback_context.user_content and callback_context.user_content.parts:
        for part in callback_context.user_content.parts:
            if part.text:
                user_text += part.text
    return LlmResponse(
        content=Content(role="model", parts=[Part(text=f"echo: {user_text}")])
    )

agent = wrap(
    Runner(
        agent=Agent(
            name="echo_agent",
            model="gemini-2.0-flash",
            instruction="Echo the user message.",
            before_model_callback=echo_callback,
        ),
        app_name="adk_echo",
        session_service=LangsmithSessionService(),
    )
)
```

Two things are essential:

1. **Pass `LangsmithSessionService()`** as the runner's `session_service`. `wrap()` raises a `TypeError` if you forget. Agent Server needs this hook to load and save ADK session state through its checkpointer.
2. **Export the wrapped `agent`** as a module-level variable. Agent Server imports this symbol when serving the graph.

For a real agent, drop the `before_model_callback` and configure a model directly. For example, use Gemini by setting `model="gemini-2.0-flash"` with `GOOGLE_API_KEY` set, or use Claude/OpenAI via ADK's LiteLLM adapter (`google.adk.models.lite_llm.LiteLlm`, available through `google-adk[extensions]`).

## Capabilities and limitations

`wrap()` bridges a defined subset of ADK's runtime to Agent Server. Review the boundaries below before porting an existing ADK agent, since some ADK features are passed through unchanged while others are intentionally not supported.

### Supported

* **Agent primitives**: `Agent`, `SequentialAgent`, and `ParallelAgent`, including nested sub-agent delegation through the `sub_agents` parameter.
* **Tools**: Python function tools and `LongRunningFunctionTool`.
* **Models**: Gemini models directly, and any model supported by ADK's LiteLLM adapter (`google.adk.models.lite_llm.LiteLlm`, available through `google-adk[extensions]`). Set the provider's API key on the deployment.
* **Token streaming**: ADK partial events are forwarded through LangGraph's async callback manager, so token chunks reach clients consuming `stream_mode="messages"` and the Studio chat view.
* **Structured output**: agents configured with `output_schema` and `output_key` expose the typed value on the graph's response in addition to `messages`.
* **Session persistence**: `LangsmithSessionService` stores ADK session state in the deployment's checkpoint store. State survives restarts and is loaded on each subsequent turn of the same thread.
* **Tracing**: when `LANGSMITH_TRACING=true`, the wrapper calls `configure_google_adk()` automatically (see [Enable tracing](#enable-tracing)).
* **Authentication**: if Agent Server [authentication](/langsmith/auth) is enabled, the authenticated user id becomes ADK's `user_id`. Otherwise the user id is `"anonymous"`.

### Not supported

* **Multimodal input**: the wrapper forwards only `messages[-1].content` as a single text part. Inbound images, files, audio, or inline binary blocks are not passed to the ADK runner.
* **Multiple new messages per turn**: only the last item in `messages` is treated as the new user message. Conversation history is reconstructed from ADK session state, not from the LangGraph message list.
* **Bidirectional / live streaming**: the wrapper hard-codes `RunConfig(streaming_mode=StreamingMode.SSE)`. ADK's `Runner.run_live()` and the bidirectional streaming mode used for audio or voice agents are not invoked, so live audio and voice agents cannot be deployed through `wrap()`.
* **Non-text output parts**: only `part.text` values are collected from ADK events. Inline images, audio, or files produced by the agent are not surfaced on the graph's `messages` output.
* **Intermediate events as messages**: the response is emitted as one `AIMessage` containing the concatenated text. Tool calls, tool results, and intermediate sub-agent turns are not exposed as separate items in the graph's `messages` field. Inspect them in [LangSmith traces](/langsmith/observability) instead.
* **Alternative ADK session services**: `runner.session_service` must be a `LangsmithSessionService`. ADK's `InMemorySessionService`, `DatabaseSessionService`, and `VertexAiSessionService` are rejected with a `TypeError`, because session state is held in the LangGraph checkpoint.
* **Native LangGraph interrupts**: the wrapper does not expose LangGraph's `interrupt` or `Command(resume=...)` mechanism. Human-in-the-loop flows built on `LongRunningFunctionTool` follow ADK's own pattern: the tool returns a status such as `pending_approval`, the agent replies, and a follow-up turn resolves the pending call.

## Project layout

A deployable project needs three files:

```
my-adk-agent/
├── agent.py              # exports the wrapped agent
├── langgraph.json        # Agent Server config
└── pyproject.toml        # Python dependencies
```

[`langgraph.json`](/langsmith/application-structure#configuration-file-concepts) points Agent Server at the exported symbol:

```json langgraph.json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "$schema": "https://langgra.ph/schema.json",
  "dependencies": ["."],
  "graphs": {
    "adk_echo": "./agent.py:agent"
  },
  "env": ".env"
}
```

`pyproject.toml` declares dependencies:

```toml pyproject.toml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
[project]
name = "my-adk-agent"
version = "0.0.1"
requires-python = ">=3.11"
dependencies = [
    "deployments-wrap-sdk[google-adk]>=0.0.1",
]
```

## Install dependencies

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
pip install -e .
```

## Run locally

Start the local Agent Server with the [LangGraph CLI](/langsmith/cli):

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
langgraph dev
```

This serves the agent at `http://127.0.0.1:2024` and opens [LangSmith Studio](/langsmith/studio) so you can chat with the agent. Send a request directly with `curl`:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# Create a thread
THREAD=$(curl -s -X POST http://127.0.0.1:2024/threads \
  -H "Content-Type: application/json" -d '{}' | python -c "import sys, json; print(json.load(sys.stdin)['thread_id'])")
