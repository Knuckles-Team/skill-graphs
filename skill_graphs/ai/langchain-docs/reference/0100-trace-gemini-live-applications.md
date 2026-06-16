# Trace Gemini Live applications
Source: https://docs.langchain.com/langsmith/trace-gemini-live

Trace Gemini Live voice agents built with the Google Agent Development Kit (ADK) in LangSmith.

The [Gemini Live API](https://ai.google.dev/gemini-api/docs/live-api) enables low-latency, bidirectional voice interactions with Gemini models over a persistent WebSocket connection. This guide shows how to trace a Gemini Live voice agent built with the [Google Agent Development Kit (ADK)](https://google.github.io/adk-docs/streaming/) to LangSmith.

Gemini Live is a speech-to-speech model: it processes audio natively and exchanges a continuous stream of events with your application over a persistent WebSocket connection, rather than making discrete request/response calls. The following sections show those events and how to turn them into a LangSmith trace. For our high-level principles on getting the most out of your voice agent traces, see [Voice tracing fundamentals](/langsmith/trace-voice-fundamentals).

## The ADK Live event model

As the conversation runs, ADK streams a series of events to your application. Each event reports something that happened in the conversation: a chunk of audio, a transcript fragment, a tool call, a turn boundary, or an interruption. Every event has the same shape, and most of its fields are optional, so you determine what an event represents from **which fields are populated**:

| Populated field                      | Meaning                                                                                                      |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `content.parts[*].inline_data`       | A chunk of agent audio (PCM16 bytes). The agent's voice arrives as a flood of these.                         |
| `input_transcription`                | A fragment of the *user's* speech transcript. A final event repeats the full utterance with `finished=True`. |
| `output_transcription`               | A fragment of the *agent's* speech transcript.                                                               |
| `content.parts[*].function_call`     | The model requested a tool (name and arguments).                                                             |
| `content.parts[*].function_response` | ADK executed the tool and is returning the result to the model.                                              |
| `turn_complete`                      | The server finished its half of the exchange.                                                                |
| `interrupted`                        | The server detected user barge-in over the agent. Flush your speaker buffer.                                 |

## How events map to LangSmith runs

To get the most out of your traces, capture each meaningful event and the data it contains in a single conversation trace, with one span per event:

```text theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
conversation                           ← root run (combined audio recording; ls_modality="audio")
│   metadata: thread_id, model, event_count, duration_s
│
├─ input_transcription                 ← a fragment of the user's speech transcript
├─ output_transcription                ← a fragment of the agent's speech transcript
├─ function_call: get_weather          ← the model requested the tool
├─ function_response: get_weather      ← ADK ran the tool; result heading back
├─ turn_complete                       ← turn boundary
└─ interrupted                         ← barge-in
```

## Installation

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
pip install "google-adk>=2.0" google-genai "langsmith>=0.4"
```

Install `sounddevice` and `numpy` as well if you want to capture local audio and attach the conversation recording.

## Set up your environment

The following steps demonstrate how to trace using the LangSmith SDK. You can also trace using OpenTelemetry directly. See [Trace with OpenTelemetry](/langsmith/trace-with-opentelemetry).

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
export LANGSMITH_API_KEY=...
export LANGSMITH_TRACING=true
export LANGSMITH_PROJECT=my-voice-app
export GOOGLE_API_KEY=...
```

## Quickstart

<Note>
  This guide focuses on the tracing layer. It assumes you already have a working ADK Live app: the `LlmAgent`, `Runner`, and `LiveRequestQueue` that produce the `run_live` event stream, plus your microphone and speaker I/O. For a complete, runnable implementation of all of that, see the [voice demo repository](https://github.com/langchain-ai/voice-demo/tree/main/src/voice_demo/adk).
</Note>

### Step 1: Build the RunConfig

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from google.adk.agents.run_config import RunConfig, StreamingMode
from google.genai import types as genai_types

run_config = RunConfig(
    response_modalities=["AUDIO"],
    streaming_mode=StreamingMode.BIDI,
    input_audio_transcription=genai_types.AudioTranscriptionConfig(),
    output_audio_transcription=genai_types.AudioTranscriptionConfig(),
)
```

<Note>
  **Transcription is opt-in.** You get no transcripts unless you enable input and output transcription in the `RunConfig`. The `finished=True` transcription event carries the complete utterance, so there is no need to accumulate fragments client-side.
</Note>

### Step 2: Open the conversation root run

Open one run for the whole conversation and mark it as a voice trace with `ls_modality="audio"`, following the [single-trace convention](/langsmith/trace-voice-fundamentals#trace-each-conversation-as-a-single-trace). Keep this run open for the lifetime of the session and finalize it when the session ends.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langsmith import RunTree

session = RunTree(
    name="conversation",
    run_type="chain",
    extra={"metadata": {"thread_id": thread_id, "model": MODEL, "ls_modality": "audio"}},
)
session.post()
```

### Step 3: Trace each event

Define a small helper that opens a child run for one event, records its scrubbed payload, and closes it when the block exits. The `scrub` pass replaces raw audio bytes with a placeholder so the spans stay small:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from contextlib import contextmanager

def scrub(obj):
    """Replace raw audio bytes with a placeholder so spans stay small."""
    if isinstance(obj, bytes):
        return f"<{len(obj)} bytes>"
    if isinstance(obj, dict):
        return {k: scrub(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [scrub(v) for v in obj]
    return obj

@contextmanager
def event_span(parent, event, *, name, inbound):
    """Trace one event as a child run under the conversation root.

    User-to-model events land in `inputs`; model-to-user events land in
    `outputs`, so the trace reads in the natural direction of flow.
    """
    payload = scrub(event.raw.model_dump())
    child = parent.create_child(
        name=name,
        run_type="chain",
        inputs=payload if inbound else {},
    )
    child.post()
    try:
        yield child
    finally:
        child.end(outputs={} if inbound else payload)
        child.patch()
```

Then loop over the events from your app's `run_live` stream, skipping the audio-only chunks and spanning the rest. `runner`, `adk_session`, and `queue` come from your ADK Live app (see the [demo agent](https://github.com/langchain-ai/voice-demo/blob/main/src/voice_demo/adk/agent.py)); `LiveEvent` is the wrapper defined in the note below:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
async for raw_event in runner.run_live(
    user_id=USER_ID,
    session_id=adk_session.id,
    live_request_queue=queue,
    run_config=run_config,
):
    event = LiveEvent(raw_event)
    if event.is_audio_only:
        continue  # tracing audio will make your traces very noisy

    with event_span(session, event, name=event.label, inbound=event.is_inbound):
        ...  # handle the event: capture the transcript, run a tool, and so on
```

<Note>
  Skip audio-only events, the chunks of agent speech. They arrive in the thousands over a short conversation and would bury the trace, so play them to the speaker but do not span them.
</Note>

<Note>
  A `LiveEvent` wrapper with helper functions is defined in the [demo repository](https://github.com/langchain-ai/voice-demo/blob/main/src/voice_demo/adk/events.py). Adapt the implementation to your own code.
</Note>

## Attach audio

<Info>
  Audio rates differ by direction: ADK Live expects 16 kHz PCM16 input and produces 24 kHz output. If your microphone capture is not 16 kHz, resample it on the send path.
</Info>

To listen to a conversation alongside its transcript, attach a single combined recording of the whole conversation to the root run. Record both sides into one stereo WAV (the user's mic on the left channel, the agent's audio on the right) so interruptions show up as overlap between the channels. Write the user's mic frames as you send them to ADK, and tap the speaker for the agent's audio so audio flushed on barge-in never reaches the recording and the file reflects what the user actually heard.

For the underlying attachment API, see [Upload files with traces](/langsmith/upload-files-with-traces). For the cross-provider rationale, see [Record a single combined audio file](/langsmith/trace-voice-fundamentals#record-a-single-combined-audio-file).

Finalize the root run when the session ends. Wrap the event loop in a `try`/`finally` so the run always closes, even on error:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
try:
    ...  # the run_live event loop from Step 3
except Exception as exc:
    session.error = f"{type(exc).__name__}: {exc}"  # surface failures on the root run
finally:
    session.end()
    session.patch()
```

The demo repository wraps the full recording flow for each framework, including mic resampling, speaker-tap capture, and stereo WAV reconstruction. For Gemini Live, see the [ADK agent](https://github.com/langchain-ai/voice-demo/blob/main/src/voice_demo/adk/agent.py) and the shared [recording helpers](https://github.com/langchain-ai/voice-demo/blob/main/src/voice_demo/sdk_tracing.py).

## Troubleshooting

* **No transcription configs means empty-looking traces.** This is the most common failure mode. Both `input_audio_transcription` and `output_audio_transcription` must be set on the `RunConfig`.
* **Don't accumulate transcript fragments.** Use the `finished=True` event's full text; fragments are only for live UI display.
* **Don't span audio-only events.** A few minutes of conversation produces thousands of them.
* **Fields co-occur.** Classify by priority, not by assuming one field per event.
* **Tools run inside ADK.** Do not synthesize your own tool runs. Doing so double-counts what `function_call` and `function_response` already record.
* **Resample the mic** if your capture isn't 16 kHz (ADK input is 16 kHz, output is 24 kHz).
* **Mute ADK's startup noise** for a console UI: `logging.getLogger("google_adk").setLevel(logging.ERROR)` suppresses the experimental-feature warning for `run_live` and the MCP-not-installed line.

## Next steps

<CardGroup>
  <Card title="Voice fundamentals" icon="waveform" href="/langsmith/trace-voice-fundamentals">
    Core conventions for tracing voice agents.
  </Card>

  <Card title="Upload files with traces" icon="paperclip" href="/langsmith/upload-files-with-traces">
    Attach the conversation audio recording to your trace.
  </Card>
</CardGroup>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-gemini-live.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Trace generator functions
Source: https://docs.langchain.com/langsmith/trace-generator-functions

In most LLM applications, you will want to stream outputs to minimize the time to the first token seen by the user.

LangSmith's tracing functionality natively supports streamed outputs via `generator` functions. Below is an example.

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langsmith import traceable
  @traceable
  def my_generator():
    for chunk in ["Hello", "World", "!"]:
        yield chunk
  # Stream to the user
  for output in my_generator():
    print(output)
  # It also works with async functions
  import asyncio
  @traceable
  async def my_async_generator():
    for chunk in ["Hello", "World", "!"]:
        yield chunk
  # Stream to the user
  async def main():
    async for output in my_async_generator():
        print(output)
  asyncio.run(main())
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { traceable } from "langsmith/traceable";
  const myGenerator = traceable(function* () {
    for (const chunk of ["Hello", "World", "!"]) {
        yield chunk;
    }
  });
  for (const output of myGenerator()) {
    console.log(output);
  }
  ```
</CodeGroup>

## Aggregate results[ ](#aggregate-results "Direct link to aggregate results")

By default, the `outputs` of the traced function are aggregated into a single array in LangSmith. If you want to customize how it is stored (for instance, concatenating the outputs into a single string), you can use the `aggregate` option (`reduce_fn` in python). This is especially useful for aggregating streamed LLM outputs.

<Note>
  Aggregating outputs **only** impacts the traced representation of the outputs. It doesn not alter the values returned by your function.
</Note>

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langsmith import traceable
  def concatenate_strings(outputs: list):
    return "".join(outputs)
  @traceable(reduce_fn=concatenate_strings)
  def my_generator():
    for chunk in ["Hello", "World", "!"]:
        yield chunk
  # Stream to the user
  for output in my_generator():
    print(output)
  # It also works with async functions
  import asyncio
  @traceable(reduce_fn=concatenate_strings)
  async def my_async_generator():
    for chunk in ["Hello", "World", "!"]:
        yield chunk
  # Stream to the user
  async def main():
    async for output in my_async_generator():
        print(output)
  asyncio.run(main())
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { traceable } from "langsmith/traceable";
  const concatenateStrings = (outputs: string[]) => outputs.join("");
  const myGenerator = traceable(function* () {
    for (const chunk of ["Hello", "World", "!"]) {
        yield chunk;
    }
  }, { aggregator: concatenateStrings });
  for (const output of await myGenerator()) {
    console.log(output);
  }
  ```
</CodeGroup>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-generator-functions.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Trace LiteLLM applications
Source: https://docs.langchain.com/langsmith/trace-litellm

[LiteLLM](https://www.litellm.ai/) provides a unified interface for calling LLM providers using a consistent OpenAI-compatible API. It can be used either as a [Python SDK](https://docs.litellm.ai/docs/#litellm-python-sdk) embedded directly in your application, or as a [proxy server](https://docs.litellm.ai/docs/simple_proxy) that exposes an OpenAI-compatible endpoint for client applications.

This guide shows you how to trace LiteLLM calls with LangSmith using:

* The [LangSmith SDK](#use-langsmith_tracing-and-traceable) (`@traceable`) for application-level tracing.
* [LiteLLM’s built-in langsmith callback](#log-litellm-call-with-the-langsmith-callback) for model-level logging.
* The [LiteLLM Proxy](#use-the-litellm-proxy) for gateway-level tracing.

## Installation

Install the following when using either the LiteLLM Python SDK or LiteLLM Proxy:

<CodeGroup>
  ```bash Python SDK theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install litellm langsmith openai
  ```

  ```bash Proxy usage theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  npm install openai langsmith
  ```
</CodeGroup>

The examples in this guide use OpenAI models, but you can install the necessary provider for your use case.

## Use the LiteLLM Python SDK

LiteLLM supports two ways to send traces to LangSmith, which operate at different layers:

* [LangSmith SDK tracing](#use-langsmith_tracing-and-traceable) with `LANGSMITH_TRACING=true` enables application-level tracing via the LangSmith SDK. This is useful when you want to trace broader business logic, multi-step pipelines, or spans created with `@traceable`.
* LiteLLM’s built-in [`langsmith` callback](#log-litellm-call-with-the-langsmith-callback) logs model calls directly from LiteLLM. This is recommended when you want to trace LiteLLM requests specifically, or run async applications.

<Note>
  Avoid enabling LiteLLM's `langsmith` callback and LangSmith tracing for the same LiteLLM calls, as this can result in duplicate traces.
</Note>

### Use `LANGSMITH_TRACING` and `traceable`

You can use `LANGSMITH_TRACING=true` together with `@traceable` for predictable traces in LangSmith. This approach ensures that the **Input** and **Output** columns reflect your function arguments and return values, allowing you to preserve the full message structure (including `role` and `content`). It also works reliably in simple synchronous scripts, without requiring an asyncio event loop or additional callback configuration.

1. Set the following environment variables to enable LangSmith tracing for LiteLLM Python SDK usage:

   ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
   export LANGSMITH_API_KEY="your_api_key"
   export LANGSMITH_PROJECT="litellm-integration"
   export LANGSMITH_TRACING="true"
   ```

   Create LangSmith [API keys](/langsmith/create-account-api-key) in the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-trace-litellm).

   Depending on what provider you're using, you'll also need to set API keys:

   ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
   export OPENAI_API_KEY="your_openai_key"
   ```

2. Add the following code to your script file:

   ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
   from langsmith import traceable
   from litellm import completion

   @traceable(name="LiteLLM Chat Completion")
   def run(messages):
       response = completion(
           model="gpt-4o",
           messages=messages,
       )
       # Return the assistant message so the LangSmith UI shows role + content
       return response["choices"][0]["message"]

   messages = [
       {"role": "user", "content": "Explain observability in LLM systems."}
   ]

   result = run(messages)
   print(result["content"])
   ```

   `@traceable` instruments your function as a LangSmith run. When `LANGSMITH_TRACING=true` is set, LangSmith automatically:

   * Creates a run when the function is invoked.
   * Records the function arguments as the run inputs.
   * Executes the function body (including the LiteLLM call).
   * Records the function's return value as the run output.
   * Captures timing, errors, and nested spans (if any).

   In this example, the `messages` argument becomes the trace input, and the returned assistant message object becomes the trace output. The LiteLLM call itself runs normally—`@traceable` wraps it with observability rather than modifying its behavior. This approach traces your application logic, not just the model call.

   <Tip>
     For more general examples using `@traceable`, refer to the [Custom instrumentation](/langsmith/annotate-code#use-@traceable-/-traceable) page.
   </Tip>

### Log LiteLLM call with the `langsmith` callback

LiteLLM can send traces directly to LangSmith using its built-in [callback system](https://docs.litellm.ai/docs/observability/callbacks). This is useful when running LiteLLM inside an async Python service and you want LiteLLM itself to emit model-level logs.

LiteLLM callbacks run in an asynchronous environment. When making asynchronous calls with `litellm.acompletion()`, you can enable the `langsmith` callback to log successful model calls.

<Tip>
  This approach is best suited for async applications. For simple synchronous scripts, use the `@traceable` method shown in the [previous section](#use-langsmith_tracing-and-traceable).
</Tip>

1. Set the following environment variables:

   ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
   export LANGSMITH_API_KEY="your_api_key"
   export LANGSMITH_PROJECT="litellm-integration"
   ```

   Create LangSmith [API keys](/langsmith/create-account-api-key) in the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-trace-litellm).

   Depending on what provider you're using, you'll also need to set API keys:

   ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
   export OPENAI_API_KEY="your_openai_key"
   ```

2. To run this in a minimal script:

   * Use `acompletion()` (async API).
   * Run with `asyncio.run(...)` to create an event loop.
   * Set `langsmith_batch_size = 1` to flush immediately.

   ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
   import asyncio
   import litellm
   from litellm import acompletion

   # Enable LiteLLM → LangSmith callback
   litellm.success_callback = ["langsmith"]

   # For short-lived scripts, send immediately instead of waiting for batch flush
   litellm.langsmith_batch_size = 1

   async def main():
       response = await acompletion(
           model="gpt-4o",
           messages=[
               {"role": "user", "content": "Explain observability in LLM systems."}
           ],
       )

       # Print the assistant message content for local verification
       print(response["choices"][0]["message"]["content"])

       # Allow time for background logger to flush before process exit
       await asyncio.sleep(1)

   if __name__ == "__main__":
       asyncio.run(main())
   ```

   The callback sends LiteLLM’s model request and response data directly to LangSmith, including provider metadata and token usage. Because LiteLLM controls the payload, the **Input** and **Output** columns may include additional metadata compared to the `@traceable` example.

## Use the LiteLLM Proxy

The LiteLLM proxy runs as a standalone server and exposes an OpenAI-compatible API.

1. To have the proxy log requests directly to LangSmith, configure the callback in `config.yaml`:

   ```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
   model_list:
     - model_name: gpt-4o
       litellm_params:
         model: openai/gpt-4o

   litellm_settings:
     callbacks: ["langsmith"]
   ```

2. Set environment variables in your proxy environment:

   ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
   export LANGSMITH_API_KEY="your_api_key"
   export LANGSMITH_PROJECT="litellm-proxy"
   export OPENAI_API_KEY="your_openai_key"
   ```

   <Note>
     The LiteLLM proxy runs as a separate service. If you enable LangSmith tracing at the proxy level, you must configure `LANGSMITH_API_KEY` and related environment variables in the proxy’s runtime environment. These settings are not shared with your application process.
   </Note>

3. Start the proxy:

   ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
   litellm --config config.yaml
   ```

   By default, the proxy runs at `http://localhost:4000/v1`. Your application calls it using any OpenAI-compatible client (Python, JavaScript, curl, etc.).

   With `callbacks: ["langsmith"]` enabled, the proxy sends model request and response data directly to LangSmith. No tracing configuration is required in the client application.

4. Call the proxy from another terminal window:

   <CodeGroup>
     ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
     from openai import OpenAI

     client = OpenAI(
         base_url="http://localhost:4000/v1",
         api_key="anything"  # proxy may require a key but doesn't validate it by default
     )

     response = client.chat.completions.create(
         model="gpt-4o",
         messages=[
             {"role": "user", "content": "What is LiteLLM?"}
         ],
     )

     print(response.choices[0].message.content)
     ```

     ```javascript JavaScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
     import OpenAI from "openai";

     const client = new OpenAI({
     apiKey: "anything",
     baseURL: "http://localhost:4000/v1",
     });

     const response = await client.chat.completions.create({
     model: "gpt-4o",
     messages: [
         { role: "user", content: "Explain LiteLLM tracing." }
     ],
     });

     console.log(response.choices[0].message.content);
     ```
   </CodeGroup>

   The client sends a normal chat completion request, and the proxy handles provider routing and response formatting.

## Next steps

* [View traces in LangSmith](/langsmith/filter-traces-in-application)
* [Add custom metadata](/langsmith/ls-metadata-parameters)
* [Filter and sample traces](/langsmith/sample-traces)

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-litellm.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Trace OpenAI applications
Source: https://docs.langchain.com/langsmith/trace-openai

The `wrap_openai`/`wrapOpenAI` methods in Python/TypeScript allow you to wrap your OpenAI client in order to automatically log traces -- no decorator or function wrapping required! Using the wrapper ensures that messages, including tool calls and multimodal content blocks will be rendered nicely in LangSmith. Also note that the wrapper works seamlessly with the `@traceable` decorator or `traceable` function and you can use both in the same application.

<Note>
  The `LANGSMITH_TRACING` environment variable must be set to `'true'` in order for traces to be logged to LangSmith, even when using `wrap_openai` or `wrapOpenAI`. This allows you to toggle tracing on and off without changing your code.

  Additionally, you will need to set the `LANGSMITH_API_KEY` environment variable to your API key (see [Setup](/) for more information).

  If your LangSmith API key is linked to multiple workspaces, set the `LANGSMITH_WORKSPACE_ID` environment variable to specify which workspace to use.

  By default, the traces will be logged to a project named `default`. To log traces to a different project, see [Log traces to a specific project](/langsmith/log-traces-to-project).
</Note>

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import openai
  from langsmith import traceable
  from langsmith.wrappers import wrap_openai

  client = wrap_openai(openai.Client())

  @traceable(run_type="tool", name="Retrieve Context")
  def my_tool(question: str) -> str:
    return "During this morning's meeting, we solved all world conflict."

  @traceable(name="Chat Pipeline")
  def chat_pipeline(question: str):
    context = my_tool(question)
    messages = [
        { "role": "system", "content": "You are a helpful assistant. Please respond to the user's request only based on the given context." },
        { "role": "user", "content": f"Question: {question}\nContext: {context}"}
    ]
    chat_completion = client.chat.completions.create(
        model="gpt-5.5", messages=messages
    )
    return chat_completion.choices[0].message.content

  chat_pipeline("Can you summarize this morning's meetings?")
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import OpenAI from "openai";
  import { traceable } from "langsmith/traceable";
  import { wrapOpenAI } from "langsmith/wrappers";

  const client = wrapOpenAI(new OpenAI());

  const myTool = traceable(async (question: string) => {
    return "During this morning's meeting, we solved all world conflict.";
  }, { name: "Retrieve Context", run_type: "tool" });

  const chatPipeline = traceable(async (question: string) => {
    const context = await myTool(question);
    const messages = [
        {
            role: "system",
            content:
                "You are a helpful assistant. Please respond to the user's request only based on the given context.",
        },
        { role: "user", content: `Question: ${question} Context: ${context}` },
    ];
    const chatCompletion = await client.chat.completions.create({
        model: "gpt-5.5",
        messages: messages,
    });
    return chatCompletion.choices[0].message.content;
  }, { name: "Chat Pipeline" });

  await chatPipeline("Can you summarize this morning's meetings?");
  ```
</CodeGroup>

To trace a provider with an OpenAI-compatible API, refer to [Trace OpenAI-compatible providers](/langsmith/trace-with-openai-compatible).

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-openai.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Trace OpenAI Realtime applications
Source: https://docs.langchain.com/langsmith/trace-openai-realtime

Trace OpenAI Realtime voice agents in LangSmith using the LangSmith SDK.

The [OpenAI Realtime API](https://platform.openai.com/docs/guides/realtime) powers low-latency speech-to-speech voice agents. This guide shows how to trace a Realtime app to LangSmith.

OpenAI Realtime is a speech-to-speech model: it processes audio natively and exchanges a continuous stream of typed JSON events with your application over a persistent WebSocket connection, rather than making discrete request/response calls. The following sections show those events and how to turn them into a LangSmith trace. For our high-level philosophy on getting the most out of your voice agent traces, see [Voice tracing fundamentals](/langsmith/trace-voice-fundamentals).

For a complete implementation, see the [voice demo repository](https://github.com/langchain-ai/voice-demo).

## The event model

Every event has a discriminated `type` string that indicates what it represents: audio, a tool call, and so on.

The client **sends** events to configure the session and stream audio. You do not trace these as spans; they are requests, and their effects come back as server events:

| Client event                | What it does                                                                                                |
| --------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `session.update`            | Configure the session: instructions, voice, audio formats, transcription model, turn detection, tools.      |
| `input_audio_buffer.append` | Stream a base64 PCM16 mic chunk. Sent continuously.                                                         |
| `conversation.item.create`  | Add an item—used to return a `function_call_output` after running a tool.                                   |
| `response.create`           | Ask the model to generate a response (needed explicitly when turn detection uses `create_response: false`). |

The server **sends back** events:

| Server event                                            | What it carries                                                                                     | Traced?                  |
| ------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | ------------------------ |
| `session.created` / `session.updated`                   | Handshake / config acknowledgement.                                                                 | Yes                      |
| `input_audio_buffer.speech_started`                     | Server VAD heard the user start—the **barge-in signal**; flush the speaker buffer.                  | Yes                      |
| `input_audio_buffer.speech_stopped`                     | Server VAD heard the user stop.                                                                     | Yes                      |
| `input_audio_buffer.committed`                          | The audio buffer became a conversation item.                                                        | Yes                      |
| `conversation.item.created`                             | An item was added server-side.                                                                      | Yes                      |
| `conversation.item.input_audio_transcription.completed` | The full user transcript for the turn.                                                              | Yes                      |
| `response.created`                                      | The model started generating.                                                                       | Yes                      |
| `response.output_audio.delta`                           | One chunk of agent speech (base64 PCM16); hundreds per response.                                    | No—played, never spanned |
| `response.output_audio_transcript.delta`                | Streaming fragment of the agent's transcript.                                                       | No                       |
| `response.output_audio_transcript.done`                 | The agent's full transcript for the response.                                                       | Yes                      |
| `response.function_call_arguments.delta` / `.done`      | Streaming / final tool-call arguments.                                                              | `.done` only             |
| `response.output_item.*`, `response.content_part.*`     | Structural progress of the response.                                                                | Yes                      |
| `response.done`                                         | The complete response object: all output items (including every `function_call`), plus token usage. | Yes                      |
| `error`                                                 | Server-reported error.                                                                              | Yes                      |
| `rate_limits.updated`                                   | Quota bookkeeping.                                                                                  | Yes                      |

## How events map to LangSmith runs

We recommend tracing the whole conversation as a single trace, with one span per traced event in arrival order:

```text theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
realtime_session                                 ← root run (chain)
│   metadata: thread_id, model, event_count, duration_s, ls_modality=audio
│   attachments: conversation.wav (stereo: L=user, R=agent)
│
├─ input_audio_buffer.speech_started
├─ input_audio_buffer.speech_stopped
├─ conversation.item.input_audio_transcription.completed
├─ response.created
├─ response.function_call_arguments.done
├─ response.done
│   └─ lookup_weather × N                         ← tool runs, nested under the event that announced them
├─ response.done                                  ← the spoken follow-up after tools
└─ error                                          ← only if the server sent one
```

<Note>
  **The noise rule:** we recommend skipping every event type ending in `.delta`, because the matching `.done` event repeats the complete payload. Tracing both records everything twice. `response.output_audio.delta` in particular is the agent's voice: hundreds of chunks per response that would bury the trace. Play it to the speaker, but never make it a span.
</Note>

## Installation

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
pip install "langsmith>=0.4" "openai>=1.50"
```

The demo also uses `sounddevice` and `numpy` for the mic/speaker and to build the WAV attachment.

## Set up your environment

The following steps demonstrate how to trace using the LangSmith SDK. You can also trace using OpenTelemetry directly. See [Trace with OpenTelemetry](/langsmith/trace-with-opentelemetry).

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
export LANGSMITH_API_KEY=...
export LANGSMITH_TRACING=true
export LANGSMITH_PROJECT=my-voice-app
export OPENAI_API_KEY=...
```

## Quickstart

<Note>
  This guide focuses on the tracing layer. It assumes you already have a working Realtime app: the WebSocket `connection`, the `session.update` configuration, and your microphone and speaker I/O. For a complete, runnable implementation, see the [voice demo repository](https://github.com/langchain-ai/voice-demo/tree/main/src/voice_demo/openai). Enable `input_audio_transcription` (and the agent transcript) in your `session.update`, or the transcription events that make the trace readable never arrive.
</Note>

### Step 1: Open the conversation root at connect time

Use one `RunTree` per conversation:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langsmith import RunTree

root = RunTree(
    name="realtime_session",
    run_type="chain",
    inputs={},
    project_name="my-voice-app",
    extra={"metadata": {"thread_id": thread_id, "model": MODEL, "ls_modality": "audio"}},
)
root.post()
```

A stable `thread_id` you generate per conversation (for example, a UUID) groups the trace into a LangSmith [thread](/langsmith/threads); `ls_modality="audio"` marks it as a voice conversation.

### Step 2: Span each received event, skipping the noise

Define a small helper that opens a child run for one event, records the scrubbed payload as the run's input, and closes it when the block exits:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from contextlib import contextmanager

@contextmanager
def event_span(parent, event, *, name):
    """Trace one event as a child run, with its payload as the run's input."""
    payload = event.model_dump(mode="json")
    child = parent.create_child(name=name, run_type="chain", inputs={"event": payload})
    child.post()
    try:
        yield child
    finally:
        child.end()
        child.patch()
```

Then loop over the events from your open Realtime `connection`, skipping the `.delta` noise and tracing the rest:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
async for event in connection:
    if event.type.endswith(".delta"):
        continue  # the matching .done event repeats the full payload

    with event_span(root, event, name=event.type) as event_run:
        ...  # your handling for this event type
```

### Step 3: Run tools nested under the announcing event

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import json

from langsmith.run_helpers import tracing_context

if event.type == "response.done":
    calls = [i for i in (event.response.output or []) if i.type == "function_call"]
    for call in calls:
        with tracing_context(parent=event_run):
            result = await execute_tool(call.name, call.arguments)  # traced child
        await connection.conversation.item.create(item={
            "type": "function_call_output",
            "call_id": call.call_id,
            "output": json.dumps(result),
        })
    if calls:
        await connection.response.create()   # ask for the spoken follow-up
```

## Attach the conversation audio

To listen to a conversation alongside its transcript, attach a single combined recording of the whole conversation to the root run. Record both the user and the agent in one file (for example, a stereo WAV with the user mic on one channel and the agent on the other), captured from what was played to the client so the recording reflects what was actually heard, including speech cut off by a barge-in. The Realtime API streams agent audio as `response.output_audio.delta` events: decode and write those bytes to your output device, and tap that same output to build the recording.

For the underlying attachment API, see [Upload files with traces](/langsmith/upload-files-with-traces). For the cross-provider rationale, see [Record a single combined audio file](/langsmith/trace-voice-fundamentals#record-a-single-combined-audio-file).

When the conversation ends, finalize the root run:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
root.end()
root.patch()
```

## Next steps

<CardGroup>
  <Card title="Voice fundamentals" icon="waveform" href="/langsmith/trace-voice-fundamentals">
    Core conventions for tracing voice agents.
  </Card>

  <Card title="Upload files with traces" icon="paperclip" href="/langsmith/upload-files-with-traces">
    Attach the conversation audio recording to your trace.
  </Card>
</CardGroup>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-openai-realtime.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
