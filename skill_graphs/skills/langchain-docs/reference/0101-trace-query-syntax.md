# Trace query syntax
Source: https://docs.langchain.com/langsmith/trace-query-syntax

Using the method in the SDK or endpoint in the API, you can filter runs to analyze and export.

## Filter arguments

| Keys                          | Description                                                                                                                                                                                                                    |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `project_id` / `project_name` | The project(s) to fetch runs from - can be a single project or a list of projects.                                                                                                                                             |
| `trace_id`                    | Fetch runs that are part of a specific trace.                                                                                                                                                                                  |
| `run_type`                    | The [type of run](/langsmith/run-data-format#run-types) to get, for example, `llm`, `chain`, `tool`, `retriever`.                                                                                                              |
| `dataset_name` / `dataset_id` | Fetch runs that are associated with an example row in the specified dataset. This is useful for comparing prompts or models over a given dataset.                                                                              |
| `reference_example_id`        | Fetch runs that are associated with a specific example row. This is useful for comparing prompts or models on a given input.                                                                                                   |
| `parent_run_id`               | Fetch runs that are children of a given run. This is useful for fetching runs grouped together using the context manager or for fetching an agent trajectory.                                                                  |
| `error`                       | Fetch runs that errored or did not error.                                                                                                                                                                                      |
| `run_ids`                     | Fetch runs with a given list of run ids. Note: **This will ignore all other filtering arguments.**                                                                                                                             |
| `filter`                      | Fetch runs that match a given structured filter statement. See the guide below for more information.                                                                                                                           |
| `trace_filter`                | Filter to apply to the ROOT run in the trace tree. This is meant to be used in conjunction with the regular `filter` parameter to let you filter runs by attributes of the root run within a trace.                            |
| `tree_filter`                 | Filter to apply to OTHER runs in the trace tree, including sibling and child runs. This is meant to be used in conjunction with the regular `filter` parameter to let you filter runs by attributes of any run within a trace. |
| `is_root`                     | Only return root runs.                                                                                                                                                                                                         |
| `select`                      | Select the fields to return in the response. By default, all fields are returned. See [run data format](/langsmith/run-data-format) for available fields.                                                                      |
| `query` (*experimental*)      | Natural language query, which translates your query into a filter statement.                                                                                                                                                   |

<Note>
  **Performance tip**: Passing the `select` parameter and excluding `inputs` and `outputs` from the list can significantly improve query performance and reduce response sizes, especially for large runs.
</Note>

## Filter query language

LangSmith supports powerful filtering capabilities with a filter query language to permit complex filtering operations when fetching runs.

The filtering grammar is based on common comparators on fields in the run object. Supported comparators include:

* `gte` (greater than or equal to)
* `gt` (greater than)
* `lte` (less than or equal to)
* `lt` (less than)
* `eq` (equal to)
* `neq` (not equal to)
* `has` (check if run contains a tag or metadata json blob)
* `search` (search for a substring in a string field)

Additionally, you can combine multiple comparisons through the `and` operator.

These can be applied on fields of the run object, such as its `id`, `name`, `run_type`, `start_time` / `end_time`, `latency`, `total_tokens`, `error`, `execution_order`, `tags`, and any associated feedback through `feedback_key` and `feedback_score`.

<Note>
  `tree_filter` applies the same query syntax to runs anywhere in the trace tree. For predicates over arbitrary nested child-run fields, such as returned `inputs`, `outputs`, or `extra` payload paths, first narrow candidates with server-side filters, then hydrate root traces with child runs and traverse them locally. See [Query trace trees with child-run predicates](/langsmith/export-traces#query-trace-trees-with-child-run-predicates).
</Note>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-query-syntax.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Voice tracing fundamentals
Source: https://docs.langchain.com/langsmith/trace-voice-fundamentals

Best practices for tracing voice and audio agents in LangSmith, including conversation audio, single-trace conversations, and the audio modality flag.

[Tracing](/langsmith/observability-concepts#traces) a voice agent is different from tracing a text agent. A conversation is continuous, bidirectional, and interruptible: users talk over the agent, change topics mid-sentence, and expect sub-second responses. To debug and evaluate these systems, your traces need to capture the conversation as a single, audio-aware unit rather than a series of disconnected text exchanges.

This page covers the core conventions for tracing voice applications in LangSmith. Follow these patterns regardless of which framework or model provider you use ([OpenAI Realtime](/langsmith/trace-openai-realtime), [Gemini Live](/langsmith/trace-gemini-live), [LiveKit](/langsmith/trace-with-livekit), [Pipecat](/langsmith/trace-with-pipecat), or your own).

<Note>
  These conventions assume you are exporting traces to LangSmith through one of the supported [tracing setups](/langsmith/observability). For audio rendering and playback in the UI, see [Log multimodal traces](/langsmith/log-multimodal-traces) and [Upload files with traces](/langsmith/upload-files-with-traces).
</Note>

## Two architectures, two trace shapes

How you build a voice agent determines what the trace looks like. There are two common architectures, and they produce fundamentally different traces.

### Cascade

A cascade chains together separate, single-purpose models: speech-to-text (STT) transcribes the user's audio, a language model (LLM) reasons over the text and decides what to do, and text-to-speech (TTS) synthesizes the reply. Middleware, tool calls, and retrieval steps sit in between.

Because each stage is a discrete model call with a clear input and output, a cascade traces like any other agent pipeline. The trace is a tree of `STT`, `LLM`, `TTS`, tool, and middleware runs: stages can run in parallel, and a new STT → LLM → TTS cycle repeats for each turn of the conversation. These runs have meaningful input/output pairs (audio in → transcript out, prompt in → completion out).

The two most common frameworks for building cascade voice agents are [LiveKit](/langsmith/trace-with-livekit) and [Pipecat](/langsmith/trace-with-pipecat).

### Speech-to-speech (S2S)

A speech-to-speech model (such as the [OpenAI Realtime API](/langsmith/trace-openai-realtime) or [Gemini Live](/langsmith/trace-gemini-live)) processes audio natively and replies with audio over a single persistent connection, typically a WebSocket. There is no STT/LLM/TTS decomposition to trace.

Instead, the model server and your client exchange a stream of **events** over the wire: audio chunks, transcription fragments, tool-call requests, turn boundaries, interruptions, and errors. The natural unit to trace is the **event payload**, not a request/response pair. Each event you record becomes one span whose content is the payload that crossed the wire.

The rest of this page describes conventions that apply to both architectures. The provider guides cover the event-stream specifics for [OpenAI Realtime](/langsmith/trace-openai-realtime) and [Gemini Live](/langsmith/trace-gemini-live).

## Core conventions

These are the practices we recommend for getting the most out of voice traces in LangSmith. You should trace your voice applications however best suits your infrastructure and implementations, but following the structure we suggest here will help to make your traces consistent and easy to debug and evaluate.

We recommend three high-level conventions:

1. [**Trace each conversation as a single trace**](#trace-each-conversation-as-a-single-trace) instead of splitting it into multiple traces.
2. [**Record a single combined audio file**](#record-a-single-combined-audio-file) and attach it to the root run.
3. [**Mark the trace as audio**](#mark-the-trace-as-audio) with `ls_modality` so it renders and filters as a voice trace.

### Trace each conversation as a single trace

A conversation is a single interaction, so we recommend keeping it in a single trace, with the individual model calls or events nested underneath one root run that represents the whole conversation.

Do not split a conversation into multiple traces. If you start a new trace for each exchange, you lose the information that lives **between** exchanges:

* **Interruptions**: when the user talks over the agent and the agent stops (barge-in).
* **Timing and latency**: gaps between speakers, and how long the agent took to respond.
* **Context**: references back to earlier parts of the conversation.
* **Conversation-level outcomes**: whether the user's goal was ultimately resolved.

What hangs under the root run depends on your [architecture](#two-architectures-two-trace-shapes). For a [cascade](#cascade), the children are the model calls and middleware:

```text theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
conversation                      ← root run (whole conversation; combined audio; ls_modality="audio")
│
├─ stt                            ← a transcription call
├─ llm                            ← a model call (may include middleware and tool runs)
├─ tts                            ← a synthesis call
└─ ...                            ← the pattern repeats as the conversation continues
```

For a [speech-to-speech](#speech-to-speech-s2s) agent, the children are the **events** that crossed the socket:

```text theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
conversation                      ← root run (whole conversation; combined audio; ls_modality="audio")
│
├─ input_transcription            ← a fragment of the user's speech transcript
├─ output_transcription           ← a fragment of the agent's speech transcript
├─ function_call: get_weather     ← the model requested a tool
├─ function_response: get_weather ← the tool result heading back to the model
├─ turn_complete                  ← a turn boundary reported by the server
└─ interrupted                    ← the server detected user barge-in
```

<Note>
  A voice agent has no reliable notion of a "turn". Speakers overlap, interrupt, and trail off. Do not group runs into synthetic turns. Trace the real units instead: the model calls in a cascade, or the event payloads in a speech-to-speech stream.
</Note>

For background on grouping related runs, see [Nest traces](/langsmith/nest-traces). To group several separate sessions for one user, use [Threads](/langsmith/threads).

### Record a single combined audio file

Attach **one** audio file to the root run that contains **both** the user and the agent, recorded from **what was actually played to the client**, not the audio the model generated.

Record at the client. A common approach is a stereo WAV with the user's microphone on one channel and the agent's speech, captured at the speaker, on the other. This matters because the generated audio and the heard audio are not the same thing: network delay, dropped or reordered packets, and barge-in all change what the user actually experiences. A barge-in that cuts the agent off mid-sentence should appear truncated in the recording, because that is what happened. Recording what was played, rather than what was generated but possibly never heard, is what makes the trace faithful to the real interaction.

Attach the file using the [attachments API](/langsmith/upload-files-with-traces):

```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langsmith import traceable
from langsmith.schemas import Attachment

@traceable(name="conversation", metadata={"ls_modality": "audio"})
def run_conversation(session_id: str, conversation_audio: bytes):
    # conversation_audio: a single recording of what was played to the client
    # (e.g. stereo WAV: user mic on L, agent speech at the speaker on R)
    ...
    return {"conversation": Attachment(mime_type="audio/wav", data=conversation_audio)}
```

<Tip>
  Audio files can be large. For high-volume production workloads, consider downsampling, using a compressed format (such as MP3 or Opus), or sampling which conversations you record in full.
</Tip>

### Mark the trace as audio

Set the `ls_modality` metadata field to `"audio"` on the root run. This flags the trace as a voice trace so LangSmith can render it appropriately and so you can [filter](/langsmith/filter-traces-in-application) for voice traces in your project.

```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langsmith import traceable

@traceable(
    name="conversation",
    metadata={"ls_modality": "audio"},
)
def run_conversation(session_id: str):
    ...
```

<Note>
  For other `ls_` metadata fields, refer to [Metadata parameters reference](/langsmith/ls-metadata-parameters).
</Note>

## Next steps

<CardGroup>
  <Card title="Trace OpenAI Realtime" icon="microphone" href="/langsmith/trace-openai-realtime">
    Trace voice agents built on the OpenAI Realtime API.
  </Card>

  <Card title="Trace Gemini Live" icon="microphone" href="/langsmith/trace-gemini-live">
    Trace voice agents built on the Gemini Live API.
  </Card>

  <Card title="Trace LiveKit" icon="microphone" href="/langsmith/trace-with-livekit">
    Trace voice agents built with LiveKit Agents.
  </Card>

  <Card title="Trace Pipecat" icon="microphone" href="/langsmith/trace-with-pipecat">
    Trace voice agents built with Pipecat.
  </Card>

  <Card title="Upload files with traces" icon="paperclip" href="/langsmith/upload-files-with-traces">
    Attach the conversation audio recording to your trace.
  </Card>

  <Card title="Log multimodal traces" icon="photo" href="/langsmith/log-multimodal-traces">
    Render audio and other media in the LangSmith UI.
  </Card>
</CardGroup>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-voice-fundamentals.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Trace with API
Source: https://docs.langchain.com/langsmith/trace-with-api

Learn how to trace LLM applications using the LangSmith REST API directly.

This guide covers two approaches to tracing with the [REST API](/langsmith/smith-api-ref): basic tracing using the `POST /runs` and `PATCH /runs` endpoints, and batch ingestion using `POST /runs/multipart` for higher throughput.

For a full list of endpoints and request/response schemas, refer to the [API reference](/langsmith/smith-api-ref).

<Warning>
  We strongly recommend using the [Python](/langsmith/smith-python-sdk) or [TypeScript](/langsmith/smith-js-ts-sdk) SDK to send traces to LangSmith instead of the REST API directly. The SDKs include batching and background sending optimizations that prevent tracing from affecting your application's performance.

  If you cannot use an SDK, note that sending traces synchronously may impact application performance.
</Warning>

<Note>
  We recommend using **UUID v7** for run IDs. UUIDv7 embeds a timestamp, which preserves correct time-ordering of runs in a trace. Use `uuid7()` from the LangSmith SDK to generate them, or see [Specify a custom run ID](/langsmith/annotate-code#specify-a-custom-run-id) for more details.
</Note>

## Basic tracing

The simplest way to log runs is via the `POST /runs` and `PATCH /runs` endpoints. This approach requires minimal information to establish the trace hierarchy.

<Note>
  When using the LangSmith REST API, provide your [API key](/langsmith/create-account-api-key) in the request headers as `"x-api-key"`.

  If your API key is linked to multiple workspaces, specify the workspace in the header with `"x-tenant-id"`.

  In this approach, you do not need to set the `dotted_order` or `trace_id` fields—the system generates them automatically. Though simpler, it is slower and subject to lower rate limits than batch ingestion.
</Note>

The following example traces a chat completion with a parent chain run and a child LLM run. Set [`parent_run_id`](/langsmith/run-data-format) on a child run to attach it to its parent:

```python expandable wrap theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import openai
import os
import requests
from datetime import datetime, timezone
from langsmith import uuid7

# Send your API Key in the request headers
headers = {
    "x-api-key": os.environ["LANGSMITH_API_KEY"],
    "x-tenant-id": os.environ["LANGSMITH_WORKSPACE_ID"]
}

def post_run(run_id, name, run_type, inputs, parent_id=None):
    """Function to post a new run to the API."""
    data = {
        "id": run_id.hex,
        "name": name,
        "run_type": run_type,
        "inputs": inputs,
        "start_time": datetime.utcnow().isoformat(),
        # "session_name": "project-name",  # the name of the project to trace to
        # "session_id": "project-id",  # the ID of the project to trace to. specify one of session_name or session_id
    }
    if parent_id:
        data["parent_run_id"] = parent_id.hex

    requests.post(
        "https://api.smith.langchain.com/runs",  # Update for self-hosted, GCP EU (`eu.api...`), GCP APAC (`apac.api...`), or AWS US (`aws.api...`)
        json=data,
        headers=headers
    )

def patch_run(run_id, outputs):
    """Function to patch a run with outputs."""
    requests.patch(
        f"https://api.smith.langchain.com/runs/{run_id}",
        json={
            "outputs": outputs,
            "end_time": datetime.now(timezone.utc).isoformat(),
        },
        headers=headers,
    )

# This can be a user input to your app
question = "Can you summarize this morning's meetings?"

# This can be retrieved in a retrieval step
context = "During this morning's meeting, we solved all world conflict."

messages = [
    {"role": "system", "content": "You are a helpful assistant. Please respond to the user's request only based on the given context."},
    {"role": "user", "content": f"Question: {question}\nContext: {context}"}
]

# Create parent run
parent_run_id = uuid7()
post_run(parent_run_id, "Chat Pipeline", "chain", {"question": question})

# Create child run
child_run_id = uuid7()
post_run(child_run_id, "OpenAI Call", "llm", {"messages": messages}, parent_run_id)

# Generate a completion
client = openai.Client()
chat_completion = client.chat.completions.create(
    model="gpt-5.4-mini",
    messages=messages
)

# End runs
patch_run(child_run_id, chat_completion.dict())
patch_run(parent_run_id, {"answer": chat_completion.choices[0].message.content})
```

For more information, refer to [Run (span) data format](/langsmith/run-data-format).

## Batch ingestion

For faster ingestion and higher rate limits, use the [`POST /runs/multipart`](/langsmith/smith-api/runs/ingest-runs-multipart) endpoint. This requires the [`requests-toolbelt`](https://pypi.org/project/requests-toolbelt/) and [`uuid-utils`](https://pypi.org/project/uuid-utils/) packages.

Unlike basic tracing, this endpoint requires you to compute and set [`dotted_order`](/langsmith/run-data-format#what-is-dotted_order) and [`trace_id`](/langsmith/run-data-format) yourself. `dotted_order` encodes each run's timestamp and UUID with parent and child entries joined by dots (e.g., `20240101T000000Z<parent-uuid>.20240101T000001Z<child-uuid>`), telling LangSmith how runs relate and in what order they occurred. `trace_id` is the UUID of the root run.

The following example creates a parent run and a child run, sends them in a single batch request, then patches both with their outputs:

```python expandable theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import json
import os
import uuid
from datetime import datetime, timezone
from typing import Dict, List
import requests
from requests_toolbelt import MultipartEncoder
from uuid_utils.compat import uuid7

def create_dotted_order(
    start_time: datetime | None = None,
    run_id: uuid.UUID | None = None
) -> str:
    """Create a dotted order string for run ordering and hierarchy.

    The dotted order is used to establish the sequence and relationships between runs.
    It combines a timestamp with a unique identifier to ensure proper ordering and tracing.
    """
    st = start_time or datetime.now(timezone.utc)
    id_ = run_id or uuid7()
    return f"{st.strftime('%Y%m%dT%H%M%S%fZ')}{id_}"

def create_run_base(
    name: str,
    run_type: str,
    inputs: dict,
    start_time: datetime
) -> dict:
    """Create the base structure for a run."""
    run_id = uuid7()
    return {
        "id": str(run_id),
        "trace_id": str(run_id),
        "name": name,
        "start_time": start_time.isoformat(),
        "inputs": inputs,
        "run_type": run_type,
    }

def construct_run(
    name: str,
    run_type: str,
    inputs: dict,
    parent_dotted_order: str | None = None,
) -> dict:
    """Construct a run dictionary with the given parameters.

    This function creates a run with a unique ID and dotted order, establishing its place
    in the trace hierarchy if it's a child run.
    """
    start_time = datetime.now(timezone.utc)
    run = create_run_base(name, run_type, inputs, start_time)
    current_dotted_order = create_dotted_order(start_time, uuid.UUID(run["id"]))

    if parent_dotted_order:
        current_dotted_order = f"{parent_dotted_order}.{current_dotted_order}"
        run["trace_id"] = parent_dotted_order.split(".")[0].split("Z")[1]
        run["parent_run_id"] = parent_dotted_order.split(".")[-1].split("Z")[1]

    run["dotted_order"] = current_dotted_order
    return run

def serialize_run(operation: str, run_data: dict) -> List[tuple]:
    """Serialize a run for the multipart request.

    This function separates the run data into parts for efficient transmission and storage.
    The main run data and optional fields (inputs, outputs, events) are serialized separately.
    """
    run_id = run_data.get("id", str(uuid7()))

    # Separate optional fields
    inputs = run_data.pop("inputs", None)
    outputs = run_data.pop("outputs", None)
    events = run_data.pop("events", None)

    parts = []

    # Serialize main run data
    run_data_json = json.dumps(run_data).encode("utf-8")
    parts.append(
        (
            f"{operation}.{run_id}",
            (
                None,
                run_data_json,
                "application/json",
                {"Content-Length": str(len(run_data_json))},
            ),
        )
    )

    # Serialize optional fields
    for key, value in [("inputs", inputs), ("outputs", outputs), ("events", events)]:
        if value:
            serialized_value = json.dumps(value).encode("utf-8")
            parts.append(
                (
                    f"{operation}.{run_id}.{key}",
                    (
                        None,
                        serialized_value,
                        "application/json",
                        {"Content-Length": str(len(serialized_value))},
                    ),
                )
            )

    return parts

def batch_ingest_runs(
    api_url: str,
    api_key: str,
    posts: list[dict] | None = None,
    patches: list[dict] | None = None,
) -> None:
    """Ingest multiple runs in a single batch request.

    This function handles both creating new runs (posts) and updating existing runs (patches).
    It's more efficient for ingesting multiple runs compared to individual API calls.
    """
    boundary = uuid.uuid4().hex
    all_parts = []

    for operation, runs in zip(("post", "patch"), (posts, patches)):
        if runs:
            all_parts.extend(
                [part for run in runs for part in serialize_run(operation, run)]
            )

    encoder = MultipartEncoder(fields=all_parts, boundary=boundary)
    headers = {"Content-Type": encoder.content_type, "x-api-key": api_key}

    try:
        response = requests.post(
            f"{api_url}/runs/multipart",
            data=encoder,
            headers=headers
        )
        response.raise_for_status()
        print("Successfully ingested runs.")
    except requests.RequestException as e:
        print(f"Error ingesting runs: {e}")
        # In a production environment, you might want to log this error or handle it more robustly

# Configure API URL and key

# For production use, consider using a configuration file or environment variables
api_url = "https://api.smith.langchain.com"  # GCP EU: eu.api...; GCP APAC: apac.api...; AWS US: aws.api... for regional SaaS
api_key = os.environ.get("LANGSMITH_API_KEY")

if not api_key:
    raise ValueError("LANGSMITH_API_KEY environment variable is not set")

# Create a parent run
parent_run = construct_run(
    name="Parent Run",
    run_type="chain",
    inputs={"main_question": "Tell me about France"},
)

# Create a child run, linked to the parent
child_run = construct_run(
    name="Child Run",
    run_type="llm",
    inputs={"question": "What is the capital of France?"},
    parent_dotted_order=parent_run["dotted_order"],
)

# First, post the runs to create them
posts = [parent_run, child_run]
batch_ingest_runs(api_url, api_key, posts=posts)

# Then, update the runs with their end times and any outputs
child_run_update = {
    **child_run,
    "end_time": datetime.now(timezone.utc).isoformat(),
    "outputs": {"answer": "Paris is the capital of France."},
}

parent_run_update = {
    **parent_run,
    "end_time": datetime.now(timezone.utc).isoformat(),
    "outputs": {"summary": "Discussion about France, including its capital."},
}

patches = [parent_run_update, child_run_update]
batch_ingest_runs(api_url, api_key, patches=patches)

# Note: This example requires the `requests` and `requests_toolbelt` libraries.

# You can install them using pip:

# pip install requests requests_toolbelt
```

## Related

* [Run (span) data format](/langsmith/run-data-format)
* [Specify a custom run ID](/langsmith/annotate-code#specify-a-custom-run-id)
* [Custom instrumentation](/langsmith/annotate-code)

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-with-api.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Trace AutoGen applications
Source: https://docs.langchain.com/langsmith/trace-with-autogen

LangSmith can capture traces generated by [AutoGen](https://microsoft.github.io/autogen/stable/) using OpenTelemetry instrumentation. This guide shows you how to automatically capture traces from your AutoGen multi-agent conversations and send them to LangSmith for monitoring and analysis.

## Installation

Install the required packages using your preferred package manager:

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install langsmith autogen-agentchat autogen-ext opentelemetry-instrumentation-openai
  ```

  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv add langsmith autogen-agentchat autogen-ext opentelemetry-instrumentation-openai
  ```
</CodeGroup>

## Setup

### 1. Configure environment variables

Set your [API keys](/langsmith/create-account-api-key) and project name:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
export LANGSMITH_API_KEY=<your_langsmith_api_key>
export LANGSMITH_PROJECT=<your_project_name>
export OPENAI_API_KEY=<your_openai_api_key>
```

### 2. Configure OpenTelemetry integration

In your AutoGen application, configure the LangSmith OpenTelemetry integration along with the OpenAI instrumentor:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langsmith.integrations.otel import OtelSpanProcessor
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.instrumentation.openai import OpenAIInstrumentor

# Set up tracer provider
tracer_provider = TracerProvider()
tracer_provider.add_span_processor(OtelSpanProcessor())
trace.set_tracer_provider(tracer_provider)

# Instrument OpenAI calls
OpenAIInstrumentor().instrument()
```

### 3. Create and run your AutoGen application

Once configured, your AutoGen application will automatically send traces to LangSmith. Pass the tracer provider to the runtime for full tracing coverage:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.conditions import MaxMessageTermination, TextMentionTermination
from autogen_agentchat.teams import SelectorGroupChat
from autogen_agentchat.ui import Console
from autogen_core import SingleThreadedAgentRuntime
from autogen_ext.models.openai import OpenAIChatCompletionClient
from langsmith.integrations.otel import OtelSpanProcessor
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.instrumentation.openai import OpenAIInstrumentor

# Set up tracing
tracer_provider = TracerProvider()
tracer_provider.add_span_processor(OtelSpanProcessor())
trace.set_tracer_provider(tracer_provider)
OpenAIInstrumentor().instrument()

# Define a tool
def percentage_change(start: float, end: float) -> float:
    """Calculate percentage change between two values."""
    if start == 0:
        return float("inf")
    return ((end - start) / start) * 100

async def main():
    model_client = OpenAIChatCompletionClient(model="gpt-4o")
    tracer = trace.get_tracer("autogen-demo")

    with tracer.start_as_current_span("run_team"):
        planning_agent = AssistantAgent(
            "PlanningAgent",
            description="Plans tasks and delegates.",
            model_client=model_client,
            system_message=(
                "You are a planning agent. Plan and delegate tasks.\n"
                "When assigning tasks, use: 1. <agent> : <task>\n"
                'After tasks complete, summarize and end with "TERMINATE".'
            ),
        )

        data_analyst = AssistantAgent(
            "DataAnalystAgent",
            description="Performs calculations.",
            model_client=model_client,
            tools=[percentage_change],
            system_message="You are a data analyst. Use tools to compute results.",
        )

        termination = TextMentionTermination("TERMINATE") | MaxMessageTermination(max_messages=25)

        # Pass tracer_provider to the runtime
        runtime = SingleThreadedAgentRuntime(tracer_provider=trace.get_tracer_provider())
        runtime.start()

        team = SelectorGroupChat(
            [planning_agent, data_analyst],
            model_client=model_client,
            termination_condition=termination,
            allow_repeated_speaker=True,
            runtime=runtime,
        )

        task = "You started with 100 apples, now you have 120 apples. What is the percentage change?"
        await Console(team.run_stream(task=task))

        await runtime.stop()

    await model_client.close()

if __name__ == "__main__":
    asyncio.run(main())
```

## Advanced usage

### Custom metadata and tags

You can add custom metadata to your traces by setting span attributes:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from opentelemetry import trace

tracer = trace.get_tracer(__name__)

async def run_with_metadata():
    with tracer.start_as_current_span("autogen_workflow") as span:
        span.set_attribute("langsmith.metadata.session_type", "multi_agent")
        span.set_attribute("langsmith.metadata.agent_count", "2")
        span.set_attribute("langsmith.span.tags", "autogen,planning")

        # Your AutoGen code here
        await Console(team.run_stream(task=task))
```

### Combining with other instrumentors

You can combine AutoGen tracing with other OpenTelemetry instrumentors:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from opentelemetry.instrumentation.openai import OpenAIInstrumentor
from opentelemetry.instrumentation.httpx import HTTPXClientInstrumentor

# Initialize multiple instrumentors
OpenAIInstrumentor().instrument()
HTTPXClientInstrumentor().instrument()
```

## Resources

* [AutoGen documentation](https://microsoft.github.io/autogen/stable/)
* [LangSmith OpenTelemetry guide](/langsmith/trace-with-opentelemetry)

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-with-autogen.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Trace OpenAI Codex sessions
Source: https://docs.langchain.com/langsmith/trace-with-codex

Capture OpenAI Codex agent turns, tool calls, model metadata, and subagent threads in LangSmith.

The [`langsmith-codex-plugins`](https://github.com/langchain-ai/langsmith-codex-plugins) marketplace ships a tracing plugin that sends [OpenAI Codex](https://developers.openai.com/codex) session data to LangSmith. Use it to inspect agent turns, model metadata, token usage, tool calls, and subagent threads from your Codex workflows.

## Prerequisites

Before setting up tracing, ensure you have:

* [Codex CLI](https://developers.openai.com/codex/quickstart?setup=cli) v0.128 or later.
* A [LangSmith API key](/langsmith/create-account-api-key).

## Install and enable the plugin

Add the marketplace using the Codex CLI:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
codex plugin marketplace add langchain-ai/langsmith-codex-plugins
```

Enable plugin hooks and the tracing plugin globally in `~/.codex/config.toml`, or only for a specific project in `.codex/config.toml`:

```toml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
[features]
plugin_hooks = true

[plugins."tracing@langsmith-codex-plugins"]
enabled = true
```

## Configure tracing

Tracing is disabled until either `TRACE_TO_LANGSMITH` is `"true"` or `enabled` is `true` in a config file. Configure credentials with environment variables, a JSON config file, or both.

### Environment variables

The plugin reads Codex-specific variables first, then falls back to the generic LangSmith SDK variables.

| Variable                         | Required    | Default                           | Description                                                                                                   |
| -------------------------------- | ----------- | --------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `TRACE_TO_LANGSMITH`             | Yes         | -                                 | Set to `"true"` to enable tracing.                                                                            |
| `LANGSMITH_CODEX_API_KEY`        | Conditional | -                                 | LangSmith API key. Falls back to `LANGSMITH_API_KEY`. Required unless every replica provides its own API key. |
| `LANGSMITH_CODEX_ENDPOINT`       | No          | `https://api.smith.langchain.com` | LangSmith API URL. Falls back to `LANGSMITH_ENDPOINT`.                                                        |
| `LANGSMITH_CODEX_PROJECT`        | No          | `codex`                           | LangSmith project name. Falls back to `LANGSMITH_PROJECT`.                                                    |
| `LANGSMITH_CODEX_METADATA`       | No          | -                                 | JSON object merged into root trace metadata. Falls back to `LANGSMITH_METADATA`.                              |
| `LANGSMITH_CODEX_RUNS_ENDPOINTS` | No          | -                                 | JSON array of replica destinations. Falls back to `LANGSMITH_RUNS_ENDPOINTS`.                                 |

Add the variables to your shell configuration file (`~/.zshrc`, `~/.bashrc`, or `~/.bash_profile`):

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
export TRACE_TO_LANGSMITH="true"
export LANGSMITH_CODEX_API_KEY="<your-langsmith-api-key>"
export LANGSMITH_CODEX_PROJECT="codex"
```

### Config file

Use `<project>/.codex/langsmith.json` for project-level settings or `~/.codex/langsmith.json` for global defaults. The global file loads first, the project file overrides it, and matching environment variables take precedence over both.

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "enabled": true,
  "api_key": "<your-langsmith-api-key>",
  "api_url": "https://api.smith.langchain.com",
  "project": "codex",
  "metadata": {
    "team": "agents",
    "environment": "dev"
  }
}
```

| Field      | Environment variable                                         | Default           | Description                                               |
| ---------- | ------------------------------------------------------------ | ----------------- | --------------------------------------------------------- |
| `enabled`  | `TRACE_TO_LANGSMITH`                                         | `false`           | Set to `true` to enable tracing.                          |
| `api_key`  | `LANGSMITH_CODEX_API_KEY`, `LANGSMITH_API_KEY`               | -                 | LangSmith API key.                                        |
| `api_url`  | `LANGSMITH_CODEX_ENDPOINT`, `LANGSMITH_ENDPOINT`             | LangSmith default | LangSmith API URL.                                        |
| `project`  | `LANGSMITH_CODEX_PROJECT`, `LANGSMITH_PROJECT`               | `codex`           | LangSmith project name.                                   |
| `metadata` | `LANGSMITH_CODEX_METADATA`, `LANGSMITH_METADATA`             | -                 | Object merged into root trace metadata.                   |
| `replicas` | `LANGSMITH_CODEX_RUNS_ENDPOINTS`, `LANGSMITH_RUNS_ENDPOINTS` | -                 | Additional LangSmith destinations to replicate traces to. |

Keep config files that include API keys out of version control.

## Trace to multiple destinations

Set `replicas` in `langsmith.json` or `LANGSMITH_CODEX_RUNS_ENDPOINTS` to send the same trace data to additional LangSmith workspaces or projects. When set, the replica list overrides the other client settings.

Tracing to multiple [replicas](/langsmith/log-traces-to-project) is useful for:

* Sending traces to both a production and staging project.
* Tracing to multiple workspaces with different API keys.
* Adding extra metadata to specific replica destinations.

<Tabs>
  <Tab title="Config file (recommended)">
    In `<project>/.codex/langsmith.json` or `~/.codex/langsmith.json`:

    ```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    {
      "enabled": true,
      "replicas": [
        {
          "apiUrl": "https://api.smith.langchain.com",
          "apiKey": "lsv2_pt_workspace_a",
          "projectName": "project-prod"
        },
        {
          "apiUrl": "https://api.smith.langchain.com",
          "apiKey": "lsv2_pt_workspace_b",
          "projectName": "project-staging",
          "updates": { "metadata": { "environment": "staging" } }
        }
      ]
    }
    ```
  </Tab>

  <Tab title="Shell environment variable">
    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    export LANGSMITH_CODEX_RUNS_ENDPOINTS='[{"apiUrl":"https://api.smith.langchain.com","apiKey":"lsv2_pt_workspace_a","projectName":"project-prod"},{"apiUrl":"https://api.smith.langchain.com","apiKey":"lsv2_pt_workspace_b","projectName":"project-staging","updates":{"metadata":{"environment":"staging"}}}]'
    ```

    To generate the escaped JSON string, use:

    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    echo '[{"apiUrl":"...","apiKey":"...","projectName":"..."}]' | jq -c .
    ```
  </Tab>
</Tabs>

Each replica object supports the following fields:

| Field         | Required | Description                                                                 |
| ------------- | -------- | --------------------------------------------------------------------------- |
| `apiUrl`      | Yes      | LangSmith API URL (typically `https://api.smith.langchain.com`).            |
| `apiKey`      | Yes      | API key for the destination workspace.                                      |
| `projectName` | Yes      | Project name in the destination workspace.                                  |
| `updates`     | No       | Optional run fields to override on replicated runs, such as extra metadata. |

## What gets traced

Each LLM run includes:

* **Inputs**: accumulated conversation messages.
* **Outputs**: assistant response content.
* **Metadata**: model provider, model name, stop reason, and token usage.

Tool calls (function calls, shell calls, computer calls, file reads, web searches) are included with their inputs and outputs. Subagent threads are resolved and uploaded as nested child runs under the parent turn.

Interrupted turns where the user cancels mid-response are still uploaded once the session completes.

## View traces in LangSmith

Open the configured LangSmith project and complete a Codex turn. By default traces appear in the `codex` project. The plugin uploads completed Codex transcript data, including messages, tool call inputs and outputs, model metadata, token usage, and subagent thread structure.

<Warning>
  The plugin uploads full Codex transcript data to LangSmith. Do not enable tracing for sessions that contain data you do not want stored in LangSmith.
</Warning>

## Troubleshooting

If traces do not appear in LangSmith:

* Confirm `plugin_hooks = true` and the tracing plugin is enabled in `config.toml`.
* Confirm `TRACE_TO_LANGSMITH=true` is visible to the Codex process.
* Confirm `LANGSMITH_CODEX_API_KEY` or `LANGSMITH_API_KEY` is set and valid.
* If runs land in the wrong project, set `LANGSMITH_CODEX_PROJECT` or the `project` config key.
* If a custom endpoint is not used, set `LANGSMITH_CODEX_ENDPOINT` or the `api_url` config key.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-with-codex.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Trace CrewAI applications
Source: https://docs.langchain.com/langsmith/trace-with-crewai

LangSmith can capture traces generated by [CrewAI](https://github.com/crewAIInc/crewAI) using OpenTelemetry instrumentation. This guide shows you how to automatically capture traces from your CrewAI multi-agent workflows and send them to LangSmith for monitoring and analysis.

## Installation

Install the required packages using your preferred package manager:

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install langsmith crewai opentelemetry-instrumentation-crewai opentelemetry-instrumentation-openai
  ```

  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv add langsmith crewai opentelemetry-instrumentation-crewai opentelemetry-instrumentation-openai
  ```
</CodeGroup>

## Setup

### 1. Configure environment variables

Set your [API keys](/langsmith/create-account-api-key) and project name:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
export LANGSMITH_API_KEY=<your_langsmith_api_key>
export LANGSMITH_PROJECT=<your_project_name>
export OPENAI_API_KEY=<your_openai_api_key>
```

### 2. Configure OpenTelemetry integration

In your CrewAI application, configure the LangSmith OpenTelemetry integration along with the CrewAI and OpenAI instrumentors:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langsmith.integrations.otel import OtelSpanProcessor
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.instrumentation.crewai import CrewAIInstrumentor
from opentelemetry.instrumentation.openai import OpenAIInstrumentor

# Get or create tracer provider
current_provider = trace.get_tracer_provider()
if isinstance(current_provider, TracerProvider):
    tracer_provider = current_provider
else:
    tracer_provider = TracerProvider()
    trace.set_tracer_provider(tracer_provider)

# Add OtelSpanProcessor to the tracer provider
tracer_provider.add_span_processor(OtelSpanProcessor())
