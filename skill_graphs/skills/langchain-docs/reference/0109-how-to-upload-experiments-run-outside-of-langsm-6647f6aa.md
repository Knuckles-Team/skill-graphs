# How to upload experiments run outside of LangSmith with the REST API
Source: https://docs.langchain.com/langsmith/upload-existing-experiments

Some users prefer to manage their datasets and run their experiments outside of LangSmith, but want to use the LangSmith UI to view the results. This is supported via our endpoint.

This guide will show you how to upload evals using the REST API, using the `requests` library in Python as an example. However, the same principles apply to any language.

## Request body schema

Uploading an experiment requires specifying the relevant high-level information for your experiment and dataset, along with the individual data for your examples and runs within the experiment. Each object in the `results` represents a "row" in the experiment - a single dataset example, along with an associated run. Note that `dataset_id` and `dataset_name` refer to your dataset identifier in your external system and will be used to group external experiments together in a single dataset. They should not refer to an existing dataset in LangSmith (unless that dataset was created via this endpoint).

You may use the following schema to upload experiments to the `/datasets/upload-experiment` endpoint:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "experiment_name": "string (required)",
  "experiment_description": "string (optional)",
  "experiment_start_time": "datetime (required)",
  "experiment_end_time": "datetime (required)",
  "dataset_id": "uuid (optional - an external dataset id, used to group experiments together)",
  "dataset_name": "string (optional - must provide either dataset_id or dataset_name)",
  "dataset_description": "string (optional)",
  "experiment_metadata": { // Object (any shape - optional)
    "key": "value"
  },
  "summary_experiment_scores": [ // List of summary feedback objects (optional)
    {
      "key": "string (required)",
      "score": "number (optional)",
      "value": "string (optional)",
      "comment": "string (optional)",
      "feedback_source": { // Object (optional)
        "type": "string (required)"
      },
      "feedback_config": { // Object (optional)
        "type": "string enum: continuous, categorical, or freeform",
        "min": "number (optional)",
        "max": "number (optional)",
        "categories": [ // List of feedback category objects (optional)
          {
            "value": "number (required)",
            "label": "string (optional)"
          }
        ]
      },
      "created_at": "datetime (optional - defaults to now)",
      "modified_at": "datetime (optional - defaults to now)",
      "correction": "Object or string (optional)"
    }
  ],
  "results": [ // List of experiment row objects (required)
    {
      "row_id": "uuid (required)",
      "inputs": { // Object (required - any shape). This will
        "key": "val" // be the input to both the run and the dataset example.
      },
      "expected_outputs": { // Object (optional - any shape).
        "key": "val" // These will be the outputs of the dataset examples.
      },
      "actual_outputs": { // Object (optional - any shape).
        "key": "val" // These will be the outputs of the runs.
      },
      "evaluation_scores": [ // List of feedback objects for the run (optional)
        {
          "key": "string (required)",
          "score": "number (optional)",
          "value": "string (optional)",
          "comment": "string (optional)",
          "feedback_source": { // Object (optional)
            "type": "string (required)"
          },
          "feedback_config": { // Object (optional)
            "type": "string enum: continuous, categorical, or freeform",
            "min": "number (optional)",
            "max": "number (optional)",
            "categories": [ // List of feedback category objects (optional)
              {
                "value": "number (required)",
                "label": "string (optional)"
              }
            ]
          },
          "created_at": "datetime (optional - defaults to now)",
          "modified_at": "datetime (optional - defaults to now)",
          "correction": "Object or string (optional)"
        }
      ],
      "start_time": "datetime (required)", // The start/end times for the runs will be used to
      "end_time": "datetime (required)", // calculate latency. They must all fall between the
      "run_name": "string (optional)", // start and end times for the experiment.
      "error": "string (optional)",
      "run_metadata": { // Object (any shape - optional)
        "key": "value"
      }
    }
  ]
}
```

The response JSON will be a dict with keys `experiment` and `dataset`, each of which is an object that contains relevant information about the experiment and dataset that was created.

## Considerations

You may upload multiple experiments to the same dataset by providing the same dataset\_id or dataset\_name between multiple calls. Your experiments will be grouped together under a single dataset, and you will be able to [use the comparison view to compare results between experiments](/langsmith/compare-experiment-results).

Ensure that the start and end times of your individual rows are all between the start and end time of your experiment.

You must provide either a dataset\_id or a dataset\_name. If you only provide an ID and the dataset does not yet exist, we will generate a name for you, and vice versa if you only provide a name.

You may not upload experiments to a dataset that was not created via this endpoint. Uploading experiments is only supported for externally-managed datasets.

## Example request

Below is an example of a simple call to the `/datasets/upload-experiment`. This is a basic example that just uses the most important fields as an illustration.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import os
import requests

body = {
    "experiment_name": "My external experiment",
    "experiment_description": "An experiment uploaded to LangSmith",
    "dataset_name": "my-external-dataset",
    "summary_experiment_scores": [
        {
            "key": "summary_accuracy",
            "score": 0.9,
            "comment": "Great job!"
        }
    ],
    "results": [
        {
            "row_id": "<<uuid>>",
            "inputs": {
                "input": "Hello, what is the weather in San Francisco today?"
            },
            "expected_outputs": {
                "output": "Sorry, I am unable to provide information about the current weather."
            },
            "actual_outputs": {
                "output": "The weather is partly cloudy with a high of 65."
            },
            "evaluation_scores": [
                {
                    "key": "hallucination",
                    "score": 1,
                    "comment": "The chatbot made up the weather instead of identifying that "
                               "they don't have enough info to answer the question. This is "
                               "a hallucination."
                }
            ],
            "start_time": "2024-08-03T00:12:39",
            "end_time": "2024-08-03T00:12:41",
            "run_name": "Chatbot"
        },
        {
            "row_id": "<<uuid>>",
            "inputs": {
                "input": "Hello, what is the square root of 49?"
            },
            "expected_outputs": {
                "output": "The square root of 49 is 7."
            },
            "actual_outputs": {
                "output": "7."
            },
            "evaluation_scores": [
                {
                    "key": "hallucination",
                    "score": 0,
                    "comment": "The chatbot correctly identified the answer. This is not a "
                               "hallucination."
                }
            ],
            "start_time": "2024-08-03T00:12:40",
            "end_time": "2024-08-03T00:12:42",
            "run_name": "Chatbot"
        }
    ],
    "experiment_start_time": "2024-08-03T00:12:38",
    "experiment_end_time": "2024-08-03T00:12:43"
}

resp = requests.post(
    "https://api.smith.langchain.com/api/v1/datasets/upload-experiment", # Update appropriately for self-hosted installations or regional SaaS
    json=body,
    headers={"x-api-key": os.environ["LANGSMITH_API_KEY"]}
)

print(resp.json())
```

Below is the response received:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "dataset": {
    "name": "my-external-dataset",
    "description": null,
    "created_at": "2024-08-03T00:36:23.289730+00:00",
    "data_type": "kv",
    "inputs_schema_definition": null,
    "outputs_schema_definition": null,
    "externally_managed": true,
    "id": "<<uuid>>",
    "tenant_id": "<<uuid>>",
    "example_count": 0,
    "session_count": 0,
    "modified_at": "2024-08-03T00:36:23.289730+00:00",
    "last_session_start_time": null
  },
  "experiment": {
    "start_time": "2024-08-03T00:12:38",
    "end_time": "2024-08-03T00:12:43+00:00",
    "extra": null,
    "name": "My external experiment",
    "description": "An experiment uploaded to LangSmith",
    "default_dataset_id": null,
    "reference_dataset_id": "<<uuid>>",
    "trace_tier": "longlived",
    "id": "<<uuid>>",
    "run_count": null,
    "latency_p50": null,
    "latency_p99": null,
    "first_token_p50": null,
    "first_token_p99": null,
    "total_tokens": null,
    "prompt_tokens": null,
    "completion_tokens": null,
    "total_cost": null,
    "prompt_cost": null,
    "completion_cost": null,
    "tenant_id": "<<uuid>>",
    "last_run_start_time": null,
    "last_run_start_time_live": null,
    "feedback_stats": null,
    "session_feedback_stats": null,
    "run_facets": null,
    "error_rate": null,
    "streaming_rate": null,
    "test_run_number": 1
  }
}
```

Note that the latency and feedback stats in the experiment results are null because the runs haven't had a chance to be persisted yet, which may take a few seconds. If you save the experiment id and query again in a few seconds, you will see all the stats (although tokens/cost will still be null, because we don't ask for this information in the request body).

## View the experiment in the UI

Now, login to the UI and click on your newly-created dataset! You should see a single experiment: <img alt="Uploaded experiments table" />

Your examples will have been uploaded: <img alt="Uploaded examples" />

Clicking on your experiment will bring you to the comparison view: <img alt="Uploaded experiment comparison view" />

As you upload more experiments to your dataset, you will be able to compare the results and easily identify regressions in the comparison view.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/upload-existing-experiments.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Upload files with traces
Source: https://docs.langchain.com/langsmith/upload-files-with-traces

When you trace with the [`@traceable` decorator or `traceable` wrapper](/langsmith/annotate-code#use-%40traceable-%2F-traceable), LangSmith supports uploading binary files (such as images, audio, videos, PDFs, and CSVs) alongside your traces. This is particularly useful when working with LLM pipelines using multimodal inputs or outputs.

In both the [Python](#python) and [TypeScript](#typescript) SDKs, you can add attachments to your traces by specifying the MIME type and binary content of each file. This page explains how to define and trace attachments using the `Attachment` type in Python and `Uint8Array` / `ArrayBuffer` in TypeScript.

## Python

In the [Python SDK](/langsmith/smith-python-sdk), you can use the `Attachment` type to add files to your traces. Each `Attachment` requires:

* `mime_type` (str): The MIME type of the file (e.g., `"image/png"`).
* `data` (bytes | Path): The binary content of the file, or the file path.

You can also define an attachment with a tuple of the form `(mime_type, data)` for convenience.

There are two ways to provide file data:

* Load the bytes yourself and pass them directly (works in all environments), or
* Pass a `Path` object and let the SDK read the file by setting `dangerously_allow_filesystem=True` on your `@traceable` decorator.

  <Note>
    The `dangerously_allow_filesystem` flag exists as a safeguard for server and multi-tenant environments, where user-controlled input could influence a file path. In a trusted environment (a local script or a controlled pipeline where you own the file paths), it is safe to enable.
  </Note>

Decorate a function with `@traceable` and include your `Attachment` instances as arguments. The following example demonstrates both approaches: loading file bytes manually into an `Attachment`, and passing a `Path` object with `dangerously_allow_filesystem=True`:

```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langsmith import traceable
from langsmith.schemas import Attachment
from pathlib import Path
import os

# Must set dangerously_allow_filesystem to True if you want to use file paths
@traceable(dangerously_allow_filesystem=True)
def trace_with_attachments(
    val: int,
    text: str,
    image: Attachment,
    audio: Attachment,
    video: Attachment,
    pdf: Attachment,
    csv: Attachment,
):
    return f"Processed: {val}, {text}, {len(image.data)}, {len(audio.data)}, {len(video.data)}, {len(pdf.data), {len(csv.data)}}"

# Helper function to load files as bytes
def load_file(file_path: str) -> bytes:
    with open(file_path, "rb") as f:
        return f.read()

# Load files and create attachments
image_data = load_file("my_image.png")
audio_data = load_file("my_mp3.mp3")
video_data = load_file("my_video.mp4")
pdf_data = load_file("my_document.pdf")

image_attachment = Attachment(mime_type="image/png", data=image_data)
audio_attachment = Attachment(mime_type="audio/mpeg", data=audio_data)
video_attachment = Attachment(mime_type="video/mp4", data=video_data)
pdf_attachment = ("application/pdf", pdf_data) # Can just define as tuple of (mime_type, data)
csv_attachment = Attachment(mime_type="text/csv", data=Path(os.getcwd()) / "my_csv.csv")

# Define other parameters
val = 42
text = "Hello, world!"

# Call the function with traced attachments
result = trace_with_attachments(
    val=val,
    text=text,
    image=image_attachment,
    audio=audio_attachment,
    video=video_attachment,
    pdf=pdf_attachment,
    csv=csv_attachment,
)
```

## TypeScript

In the [TypeScript SDK](/langsmith/smith-js-ts-sdk), you can add attachments to traces by using `Uint8Array` or `ArrayBuffer` as data types. Each attachment's MIME type is specified within `extractAttachments`:

* `Uint8Array`: Useful for handling binary data directly.
* `ArrayBuffer`: Represents fixed-length binary data, which you can convert to `Uint8Array` as needed.

In the TypeScript SDK, the `extractAttachments` function is an optional parameter in the `traceable` configuration. When the traceable-wrapped function is invoked, it extracts binary data (e.g., images, audio files) from your inputs and logs them alongside other trace data, specifying their MIME types.

<Note>
  You cannot directly pass in a file path in the TypeScript SDK, because accessing local files is not supported in all runtime environments.
</Note>

Wrap your function with `traceable` and include your attachments within the `extractAttachments` option. The signature is:

```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
type AttachmentData = Uint8Array | ArrayBuffer;
type Attachments = Record<string, [string, AttachmentData]>;

extractAttachments?: (
    ...args: Parameters<Func>
) => [Attachments | undefined, KVMap];
```

The following example shows a full implementation:

```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { traceable } from "langsmith/traceable";

const traceableWithAttachments = traceable(
    (
        val: number,
        text: string,
        attachment: Uint8Array,
        attachment2: ArrayBuffer,
        attachment3: Uint8Array,
        attachment4: ArrayBuffer,
        attachment5: Uint8Array,
    ) =>
        `Processed: ${val}, ${text}, ${attachment.length}, ${attachment2.byteLength}, ${attachment3.length}, ${attachment4.byteLength}, ${attachment5.byteLength}`,
    {
        name: "traceWithAttachments",
        extractAttachments: (
            val: number,
            text: string,
            attachment: Uint8Array,
            attachment2: ArrayBuffer,
            attachment3: Uint8Array,
            attachment4: ArrayBuffer,
            attachment5: Uint8Array,
        ) => [
            {
                "image inputs": ["image/png", attachment],
                "mp3 inputs": ["audio/mpeg", new Uint8Array(attachment2)],
                "video inputs": ["video/mp4", attachment3],
                "pdf inputs": ["application/pdf", new Uint8Array(attachment4)],
                "csv inputs": ["text/csv", new Uint8Array(attachment5)],
            },
            { val, text },
        ],
    }
);

const fs = Deno // or Node.js fs module
const image = await fs.readFile("my_image.png"); // Uint8Array
const mp3Buffer = await fs.readFile("my_mp3.mp3");
const mp3ArrayBuffer = mp3Buffer.buffer; // Convert to ArrayBuffer
const video = await fs.readFile("my_video.mp4"); // Uint8Array
const pdfBuffer = await fs.readFile("my_document.pdf");
const pdfArrayBuffer = pdfBuffer.buffer; // Convert to ArrayBuffer
const csv = await fs.readFile("test-vals.csv"); // Uint8Array

// Define example parameters
const val = 42;
const text = "Hello, world!";

// Call traceableWithAttachments with the files
const result = await traceableWithAttachments(
    val, text, image, mp3ArrayBuffer, video, pdfArrayBuffer, csv
);
```

## Related

* [Manage datasets](/langsmith/manage-datasets)
* [Set up LLM-as-a-judge online evaluators](/langsmith/online-evaluations-llm-as-judge)

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/upload-files-with-traces.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Usage and billing
Source: https://docs.langchain.com/langsmith/usage-and-billing

Understand LangSmith trace data retention tiers, pricing, rate limits, and usage limits.

## Data retention

This section covers how data retention works and how it's priced in LangSmith.

### Why retention matters

* **Privacy**: Many data privacy regulations, such as GDPR in Europe or CCPA in California, require organizations to delete personal data once it's no longer necessary for the purposes for which it was collected. Setting retention periods aids in compliance with such regulations.
* **Cost**: LangSmith charges less for traces that have low data retention. For more information, learn how to [enforce spend limits](/langsmith/billing#enforce-spend-limits).

<Tip>
  Plan your retention tiers before you start sending traces. Changes apply to new traces only—existing traces keep their original tier. See [Change project-level default retention](/langsmith/billing#change-project-level-default-retention).
</Tip>

### How it works

LangSmith has two tiers of traces based on Data Retention with the following characteristics:

|                      | Base                                                            | Extended                                                        |
| -------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| **Price**            | [See pricing page](https://www.langchain.com/pricing-langsmith) | [See pricing page](https://www.langchain.com/pricing-langsmith) |
| **Retention Period** | 14 days                                                         | 400 days                                                        |

<Note>
  Enterprise customers can customize the extended retention period per workspace. Changes apply to new traces only—existing traces are unaffected. See [Customize extended retention policy](/langsmith/data-purging-compliance#customize-extended-retention-policy).
</Note>

**Data deletion after retention ends**

After the specified retention period, traces are no longer accessible in the tracing project UI or via the API. All user data associated with the trace (e.g. inputs and outputs) is deleted from our internal systems within a day thereafter. Some metadata associated with each trace may be retained indefinitely for analytics and billing purposes.

### Data retention auto-upgrades

<Warning>
  Auto upgrades can have an impact on your bill. Please read this section carefully to fully understand your estimated LangSmith tracing costs.
</Warning>

When you use certain features with `base` tier traces, their data retention will be automatically upgraded to `extended` tier. This will increase both the retention period, and the cost of the trace.

The complete list of scenarios in which a trace will upgrade when:

* **Feedback** is added to any run on the trace (or any trace in the thread), whether through [manual annotation](/langsmith/annotate-traces-inline), automatically with [an online evaluator](/langsmith/online-evaluations-llm-as-judge), or programmatically [via the SDK](/langsmith/attach-user-feedback).
* An **[annotation queue](/langsmith/annotation-queues#assign-runs-to-a-single-run-queue)** receives any run from the trace.
* An **[automation rule](/langsmith/rules#create-a-rule)** matches any run within a trace.

**Why auto-upgrade traces?**

We have two reasons behind the auto-upgrade model for tracing:

1. We think that traces that match any of these conditions are fundamentally more interesting than other traces, and therefore it is good for users to be able to keep them around longer.
2. We philosophically want to charge customers an order of magnitude lower for traces that may not be interacted with meaningfully. We think auto-upgrades align our pricing model with the value that LangSmith brings, where only traces with meaningful interaction are charged at a higher rate.

If you have questions or concerns about our pricing model, please feel free to contact support via [support.langchain.com](https://support.langchain.com) and let us know your thoughts!

**How does data retention affect downstream features?**

* **Annotation Queues, Run Rules, and Feedback**: Traces that use these features will be [auto-upgraded](#data-retention-auto-upgrades).
* **Monitoring**: The monitoring tab will continue to work even after a base tier trace's data retention period ends. It is powered by trace metadata that exists for >30 days, meaning that your monitoring graphs will continue to stay accurate even on `base` tier traces.
* **Datasets**: Datasets have an indefinite data retention period. Restated differently, if you add a trace's inputs and outputs to a dataset, they will never be deleted. We suggest that if you are using LangSmith for data collection, you take advantage of the datasets feature.

### Billing model

**Billable metrics**

On your LangSmith invoice, you will see two metrics that we charge for:

* LangSmith Traces (Base Charge)
* LangSmith Traces (Extended Data Retention Upgrades).

The first metric includes all traces, regardless of tier. The second metric just counts the number of extended retention traces.

**Why measure all traces + upgrades instead of base and extended traces?**

A natural question to ask when considering our pricing is why not just show the number of `base` tier and `extended` tier traces directly on the invoice?

While we understand this would be more straightforward, it doesn't fit trace upgrades properly. Consider a `base` tier trace that was recorded on June 30, and upgraded to `extended` tier on July 3. The `base` tier trace occurred in the June billing period, but the upgrade occurred in the July billing period. Therefore, we need to be able to measure these two events independently to properly bill our customers.

If your trace was recorded as an extended retention trace, then the `base` and `extended` metrics will both be recorded with the same timestamp.

**Cost breakdown**

The Base Charge for a trace is .05¢ per trace. We priced the upgrade such that an `extended` retention trace costs 10x the price of a base tier trace (.50¢ per trace) including both metrics. Thus, each upgrade costs .45¢.

## Rate limits

LangSmith has rate limits which are designed to ensure the stability of the service for all users.

To ensure access and stability, LangSmith will respond with HTTP Status Code 429 indicating that rate or usage limits have been exceeded under the following circumstances:

### Temporary throughput limit over a 1 minute period at our application load balancer

This 429 is the result of exceeding a fixed number of API calls over a 1 minute window on a per service key or PAT basis. The start of the window will vary slightly—it is not guaranteed to start at the start of a clock minute—and may change depending on application deployment events.

After the max events are received we will respond with a 429 until 60 seconds from the start of the evaluation window has been reached and then the process repeats.

This 429 is thrown by our application load balancer and is a mechanism in place for all LangSmith users independent of plan tier to ensure continuity of service for all users.

| Method            | Endpoints     | Limit | Window   |
| ----------------- | ------------- | ----- | -------- |
| `DELETE`          | `/sessions*`  | 30    | 1 minute |
| `POST` OR `PATCH` | `/runs*`      | 5000  | 1 minute |
| `GET`             | `/runs/:id`   | 30    | 1 minute |
| `POST`            | `/feedbacks*` | 5000  | 1 minute |
| `*`               | `*`           | 2000  | 1 minute |

<Note>
  The LangSmith SDK takes steps to minimize the likelihood of reaching these limits on run-related endpoints by batching up to 100 runs from a single session ID into a single API call.
</Note>

### Plan-level hourly trace event limit

This 429 is the result of reaching your maximum hourly events ingested and is evaluated in a fixed window starting at the beginning of each clock hour in UTC and resets at the top of each new hour.

An event in this context is the creation or update of a run. If a run is created and then subsequently updated in the same hourly window, that counts as 2 events against this limit.

This is thrown by our application and varies by plan tier, with organizations on our Startup/Plus and Enterprise plan tiers having higher hourly limits than our Free and Developer Plan Tiers which are designed for personal use.

| Plan                             | Limit          | Window |
| -------------------------------- | -------------- | ------ |
| Developer (no payment on file)   | 50,000 events  | 1 hour |
| Developer (with payment on file) | 250,000 events | 1 hour |
| Startup/Plus                     | 500,000 events | 1 hour |
| Enterprise                       | Custom         | Custom |

### Plan-level hourly trace data ingest limit

This 429 is the result of reaching the maximum amount of data ingested across your trace inputs, outputs, and metadata and is evaluated in a fixed window starting at the beginning of each clock hour in UTC and resets at the top of each new hour.

Typically, inputs, outputs, and metadata are sent on both run creation and update events. If a run is created at 2.0MB and updated to 3.0MB in the same hourly window, that counts as 5.0MB of storage against this limit.

This is thrown by our application and varies by plan tier, with organizations on our Startup/Plus and Enterprise plan tiers having higher hourly limits than our Free and Developer Plan Tiers which are designed for personal use.

| Plan                             | Limit  | Window |
| -------------------------------- | ------ | ------ |
| Developer (no payment on file)   | 500MB  | 1 hour |
| Developer (with payment on file) | 2.5GB  | 1 hour |
| Startup/Plus                     | 5.0GB  | 1 hour |
| Enterprise                       | Custom | Custom |

### Plan-level monthly unique traces limit

This 429 is the result of reaching your maximum monthly traces ingested and is evaluated in a fixed window starting at the beginning of each calendar month in UTC and resets at the beginning of each new month.

This is thrown by our application and applies only to the Developer Plan Tier when there is no payment method on file.

| Plan                           | Limit        | Window  |
| ------------------------------ | ------------ | ------- |
| Developer (no payment on file) | 5,000 traces | 1 month |

### Self-configured monthly usage limits

This 429 is the result of reaching your usage limit as configured by your organization admin and is evaluated in a fixed window starting at the beginning of each calendar month in UTC and resets at the beginning of each new month.

This is thrown by our application and varies by organization based on their configured settings.

### Maximum runs per trace

Each trace is limited to a maximum of 25,000 runs. Once the trace reaches this limit, LangSmith will reject any additional runs that you send for that trace.

### Run query endpoint

The [`POST /runs/query`](/langsmith/smith-api/run/query-runs) endpoint has additional per-tenant rate limits based on query parameters. See [Query traces using the SDK](/langsmith/export-traces#rate-limits) for details.

### Handling 429s responses in your application

Since some 429 responses are temporary and may succeed on a successive call, if you are directly calling the LangSmith API in your application we recommend implementing retry logic with exponential backoff and jitter.

For convenience, LangChain applications built with the LangSmith SDK has this capability built-in.

<Note>
  It is important to note that if you are saturating the endpoints for extended periods of time, retries may not be effective as your application will eventually run large enough backlogs to exhaust all retries.

  If that is the case, we would like to discuss your needs more specifically. Please contact support via [LangSmith Support](https://support.langchain.com) with details about your applications throughput needs and sample code and we can work with you to better understand whether the best approach is fixing a bug, changes to your application code, or a different LangSmith plan.
</Note>

## Usage limits

LangSmith lets you configure usage limits on tracing. Note that these are *usage* limits, not *spend* limits, which mean they let you limit the quantity of occurrences of some event rather than the total amount you will spend.

LangSmith lets you set two different monthly limits, mirroring our Billable Metrics discussed in the aforementioned data retention guide:

* All traces limit
* Extended data retention traces limit

These let you limit the number of total traces, and extended data retention traces respectively.

### Properties of usage limiting

Usage limiting is approximate, meaning that we do not guarantee the exactness of the limit. In rare cases, there may be a small period of time where additional traces are processed above the limit threshold before usage limiting begins to apply.

### Side effects of extended data retention traces limit

The extended data retention traces limit has side effects. If the limit is already reached, any feature that could cause an auto-upgrade of tracing tiers becomes inaccessible. This is because an auto-upgrade of a trace would cause another extended retention trace to be created, which in turn should not be allowed by the limit. Therefore, you can no longer:

1. match run rules
2. add feedback to traces
3. add runs to annotation queues

Each of these features may cause an auto upgrade, so we shut them off when the limit is reached.

### Updating usage limits

Usage limits can be updated from the `Settings` page under `Usage and Billing`. Limit values are cached, so it may take a minute or two before the new limits apply.

## Related content

* Tutorial on how to [enforce spend limits](/langsmith/billing#enforce-spend-limits)

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/usage-and-billing.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# How to interact with a deployment using RemoteGraph
Source: https://docs.langchain.com/langsmith/use-remote-graph

[`RemoteGraph`](https://reference.langchain.com/python/langgraph/pregel/remote/RemoteGraph) is a client-side interface that allows you to interact with your [deployment](/langsmith/deployment) as if it were a local graph. It provides API parity with [`CompiledGraph`](/oss/python/langgraph/graph-api#compiling-your-graph), which means that you can use the same methods (`invoke()`, `stream()`, `get_state()`, etc.) in your development and production environments. This page describes how to initialize a `RemoteGraph` and interact with it.

`RemoteGraph` is useful for the following:

* Separation of development and deployment: Build and test a graph locally with `CompiledGraph`, deploy it to LangSmith, and then [use `RemoteGraph`](#initialize-the-graph) to call it in production while working with the same API interface.
* Thread-level persistence: [Persist and fetch the state](#persist-state-at-the-thread-level) of a conversation across calls with a thread ID.
* Subgraph embedding: Compose modular graphs for a multi-agent workflow by embedding a `RemoteGraph` as a [subgraph](#use-as-a-subgraph) within another graph.
* Reusable workflows: Use deployed graphs as nodes or [tools](https://reference.langchain.com/python/langsmith/deployment/remote_graph/#langgraph.pregel.remote.RemoteGraph.as_tool), so that you can reuse and expose complex logic.

<Warning>
  **Important: Avoid calling the same deployment**

  `RemoteGraph` is designed to call graphs on other deployments. Do not use `RemoteGraph` to call itself or another graph on the same deployment, as this can lead to deadlocks and resource exhaustion. Instead, use local graph composition or [subgraphs](/oss/python/langgraph/use-subgraphs) for graphs within the same deployment.
</Warning>

## Prerequisites

Before getting started with `RemoteGraph`, make sure you have:

* Access to [LangSmith](/langsmith/observability), where your graphs are developed and managed.
* A running [Agent Server](/langsmith/agent-server), which hosts your deployed graphs for remote interaction.

## Initialize the graph

When initializing a `RemoteGraph`, you must always specify:

* `name`: The name of the graph you want to interact with **or** an assistant ID. If you specify a graph name, the default assistant will be used. If you specify an assistant ID, that specific assistant will be used. The graph name is the same name you use in the `langgraph.json` configuration file for your deployment.
* `api_key`: A valid [LangSmith API key](/langsmith/create-account-api-key). You can set as an environment variable (`LANGSMITH_API_KEY`) or pass directly in the `api_key` argument. You can also provide the API key in the `client` / `sync_client` arguments, if `LangGraphClient` / `SyncLangGraphClient` was initialized with the `api_key` argument.

Additionally, you have to provide one of the following:

* [`url`](#use-a-url): The URL of the deployment you want to interact with. If you pass the `url` argument, both sync and async clients will be created using the provided URL, headers (if provided), and default configuration values (e.g., timeout).
* [`client`](#use-a-client): A `LangGraphClient` instance for interacting with the deployment asynchronously (e.g., using `.astream()`, `.ainvoke()`, `.aget_state()`, `.aupdate_state()`).
* `sync_client`: A `SyncLangGraphClient` instance for interacting with the deployment synchronously (e.g., using `.stream()`, `.invoke()`, `.get_state()`, `.update_state()`).

<Note>
  If you pass both `client` or `sync_client` as well as the `url` argument, they will take precedence over the `url` argument. If none of the `client` / `sync_client` / `url` arguments are provided, `RemoteGraph` will raise a `ValueError` at runtime.
</Note>

### Use a URL

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langgraph.pregel.remote import RemoteGraph

  url = "<DEPLOYMENT_URL>"

  # Using graph name (uses default assistant)
  graph_name = "agent"
  remote_graph = RemoteGraph(graph_name, url=url)

  # Using assistant ID
  assistant_id = "<ASSISTANT_ID>"
  remote_graph = RemoteGraph(assistant_id, url=url)
  ```

  ```typescript JavaScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { RemoteGraph } from "@langchain/langgraph/remote";

  const url = "<DEPLOYMENT_URL>";

  // Using graph name (uses default assistant)
  const graphName = "agent";
  const remoteGraph = new RemoteGraph({ graphId: graphName, url });

  // Using assistant ID
  const assistantId = "<ASSISTANT_ID>";
  const remoteGraph = new RemoteGraph({ graphId: assistantId, url });
  ```
</CodeGroup>

### Use a client

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langgraph_sdk import get_client, get_sync_client
  from langgraph.pregel.remote import RemoteGraph

  url = "<DEPLOYMENT_URL>"
  client = get_client(url=url)
  sync_client = get_sync_client(url=url)

  # Using graph name (uses default assistant)
  graph_name = "agent"
  remote_graph = RemoteGraph(graph_name, client=client, sync_client=sync_client)

  # Using assistant ID
  assistant_id = "<ASSISTANT_ID>"
  remote_graph = RemoteGraph(assistant_id, client=client, sync_client=sync_client)
  ```

  ```typescript JavaScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { Client } from "@langchain/langgraph-sdk";
  import { RemoteGraph } from "@langchain/langgraph/remote";

  const client = new Client({ apiUrl: "<DEPLOYMENT_URL>" });

  // Using graph name (uses default assistant)
  const graphName = "agent";
  const remoteGraph = new RemoteGraph({ graphId: graphName, client });

  // Using assistant ID
  const assistantId = "<ASSISTANT_ID>";
  const remoteGraph = new RemoteGraph({ graphId: assistantId, client });
  ```
</CodeGroup>

## Invoke the graph

`RemoteGraph` implements the same Runnable interface as `CompiledGraph`, so you can use it in the same way as a compiled graph. It supports the full set of standard methods, including `.invoke()`, `.stream()`, `.get_state()`, and `.update_state()`, as well as their asynchronous variants.

### Asynchronously

<Note>
  To use the graph asynchronously, you must provide either the `url` or `client` when initializing the `RemoteGraph`.
</Note>

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  # invoke the graph
  result = await remote_graph.ainvoke({
      "messages": [{"role": "user", "content": "what's the weather in sf"}]
  })

  # stream outputs from the graph
  async for chunk in remote_graph.astream({
      "messages": [{"role": "user", "content": "what's the weather in la"}]
  }):
      print(chunk)
  ```

  ```typescript JavaScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  // invoke the graph
  const result = await remoteGraph.invoke({
      messages: [{role: "user", content: "what's the weather in sf"}]
  })

  // stream outputs from the graph
  for await (const chunk of await remoteGraph.stream({
      messages: [{role: "user", content: "what's the weather in la"}]
  })):
      console.log(chunk)
  ```
</CodeGroup>

### Synchronously

<Note>
  To use the graph synchronously, you must provide either the `url` or `sync_client` when initializing the `RemoteGraph`.
</Note>

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  # invoke the graph
  result = remote_graph.invoke({
      "messages": [{"role": "user", "content": "what's the weather in sf"}]
  })

  # stream outputs from the graph
  for chunk in remote_graph.stream({
      "messages": [{"role": "user", "content": "what's the weather in la"}]
  }):
      print(chunk)
  ```
</CodeGroup>

## Persist state at the thread level

By default, graph runs (for example, calls made with `.invoke()` or `.stream()`) are stateless, which means that intermediate checkpoints and the final state are not persisted after a run.

If you want to preserve the outputs of a run—for example, to support human-in-the-loop workflows—you can create a thread and pass its ID through the `config` argument. This works the same way as with a regular compiled graph:

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langgraph_sdk import get_sync_client

  url = "<DEPLOYMENT_URL>"
  graph_name = "agent"
  sync_client = get_sync_client(url=url)
  remote_graph = RemoteGraph(graph_name, url=url)

  # create a thread (or use an existing thread instead)
  thread = sync_client.threads.create()

  # invoke the graph with the thread config
  config = {"configurable": {"thread_id": thread["thread_id"]}}
  result = remote_graph.invoke({
      "messages": [{"role": "user", "content": "what's the weather in sf"}]
  }, config=config)

  # verify that the state was persisted to the thread
  thread_state = remote_graph.get_state(config)
  print(thread_state)
  ```

  ```typescript JavaScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { Client } from "@langchain/langgraph-sdk";
  import { RemoteGraph } from "@langchain/langgraph/remote";

  const url = "<DEPLOYMENT_URL>";
  const graphName = "agent";
  const client = new Client({ apiUrl: url });
  const remoteGraph = new RemoteGraph({ graphId: graphName, url });

  // create a thread (or use an existing thread instead)
  const thread = await client.threads.create();

  // invoke the graph with the thread config
  const config = { configurable: { thread_id: thread.thread_id }};
  const result = await remoteGraph.invoke({
    messages: [{ role: "user", content: "what's the weather in sf" }],
  }, config);

  // verify that the state was persisted to the thread
  const threadState = await remoteGraph.getState(config);
  console.log(threadState);
  ```
</CodeGroup>

## Use as a subgraph

<Note>
  If you need to use a `checkpointer` with a graph that has a `RemoteGraph` subgraph node, make sure to use UUIDs as thread IDs.
</Note>

A graph can also call out to multiple `RemoteGraph` instances as [*subgraph*](/oss/python/langgraph/use-subgraphs) nodes. This allows for modular, scalable workflows where different responsibilities are split across separate graphs.

`RemoteGraph` exposes the same interface as a regular `CompiledGraph`, so you can use it directly as a subgraph inside another graph. For example:

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langgraph_sdk import get_sync_client
  from langgraph.graph import StateGraph, MessagesState, START
  from typing import TypedDict

  url = "<DEPLOYMENT_URL>"
  graph_name = "agent"
  remote_graph = RemoteGraph(graph_name, url=url)

  # define parent graph
  builder = StateGraph(MessagesState)
  # add remote graph directly as a node
  builder.add_node("child", remote_graph)
  builder.add_edge(START, "child")
  graph = builder.compile()

  # invoke the parent graph
  result = graph.invoke({
      "messages": [{"role": "user", "content": "what's the weather in sf"}]
  })
  print(result)

  # stream outputs from both the parent graph and subgraph
  for chunk in graph.stream({
      "messages": [{"role": "user", "content": "what's the weather in sf"}]
  }, subgraphs=True):
      print(chunk)
  ```

  ```typescript JavaScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { MessagesAnnotation, StateGraph, START } from "@langchain/langgraph";
  import { RemoteGraph } from "@langchain/langgraph/remote";

  const url = "<DEPLOYMENT_URL>";
  const graphName = "agent";
  const remoteGraph = new RemoteGraph({ graphId: graphName, url });

  // define parent graph and add remote graph directly as a node
  const graph = new StateGraph(MessagesAnnotation)
    .addNode("child", remoteGraph)
    .addEdge(START, "child")
    .compile()

  // invoke the parent graph
  const result = await graph.invoke({
    messages: [{ role: "user", content: "what's the weather in sf" }]
  });
  console.log(result);

  // stream outputs from both the parent graph and subgraph
  for await (const chunk of await graph.stream({
    messages: [{ role: "user", content: "what's the weather in la" }]
  }, { subgraphs: true })) {
    console.log(chunk);
  }
  ```
</CodeGroup>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/use-remote-graph.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
