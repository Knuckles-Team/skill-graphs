# The trace produced will not have anonymized inputs and outputs
response_without_anonymization = openai_client.chat.completions.create(
  model="gpt-5.4-mini",
  messages=[
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "My name is Slim Shady, call me at 313-666-7440 or email me at real.slim.shady@gmail.com"},
  ],
)
```

The anonymized run will look like this in LangSmith: <img alt="Anonymized run" />

The non-anonymized run will look like this in LangSmith: <img alt="Non-anonymized run" />

### Batch processing for high-throughput masking

<Info>
  [`process_buffered_run_ops`](https://reference.langchain.com/python/langsmith/client/Client) is available in the [Python SDK only](/langsmith/smith-python-sdk).
</Info>

The previous approaches on this page process each run individually. If your masking logic involves a rate-limited API or model inference—such as the Presidio or Amazon Comprehend examples—processing runs one at a time can create a bottleneck. [`process_buffered_run_ops`](https://reference.langchain.com/python/langsmith/client/Client) lets you intercept a batch of raw run dicts before they are serialized and sent to the API, so you can amortize the cost across multiple runs at once. LangSmith processes these runs in a background thread, which does not block your application.

LangSmith holds runs in an in-memory buffer and flushes them as a batch when either:

* `run_ops_buffer_size` run operations have accumulated, or
* `run_ops_buffer_timeout_ms` milliseconds have elapsed since the last run was added (default: 5000 ms).

Your function receives the batch as a list of raw run dicts and must return a list of the **same length**, in the **same order**, with **run IDs unchanged**. Breaking either constraint raises a `ValueError`.

<Note>
  `run_ops_buffer_size` counts individual run *operations*, not unique runs. Each traced call typically produces two operations: a create (when the run starts) and an update (when it ends with outputs). Set your buffer size accordingly. For example, `run_ops_buffer_size=1000` will buffer approximately 500 traced calls. Because of this, the same run ID may appear twice in a single batch: once with inputs and once with outputs.
</Note>

<Warning>
  The buffer only flushes automatically when the size limit is reached or the timeout elapses. Always call `client.flush()` before your program exits to avoid dropping buffered runs.
</Warning>

Each run dict in the batch is either a create operation (with `inputs`, sent when the run starts) or an update operation (with `outputs`, sent when it ends). Here's what a typical pair looks like for a single traced call:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# Create op — sent when the run starts
{
    "id": "018f1b2c-...",
    "name": "my_llm_call",
    "run_type": "llm",
    "inputs": {"messages": [{"role": "user", "content": "My name is Jane Smith..."}]},
    "start_time": "2024-01-01T00:00:00.000Z",
    "trace_id": "018f1b2c-...",
    "dotted_order": "20240101T000000000000Z018f1b2c-...",
    "extra": {"metadata": {}, "runtime": {...}},
    "session_name": "default",
}

# Update op — sent when the run ends (same id, adds outputs)
{
    "id": "018f1b2c-...",
    "outputs": {"choices": [{"message": {"role": "assistant", "content": "Hello Jane..."}}]},
    "end_time": "2024-01-01T00:00:01.000Z",
    "trace_id": "018f1b2c-...",
    "dotted_order": "20240101T000000000000Z018f1b2c-...",
}
```

The following example uses Comprehend's [`batch_detect_entities` endpoint](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_BatchDetectEntities.html), which accepts up to 25 texts per call. With the per-run approach (`hide_inputs`) you would make one API call per run. Here, all message texts across the entire buffer are gathered first, then sent to Comprehend in chunks of 25, which results in significantly fewer API calls at high throughput.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import boto3
from langsmith import Client, traceable

comprehend = boto3.client("comprehend", region_name="us-east-1")

def redact_entities(text: str, entities: list) -> str:
    for entity in sorted(entities, key=lambda e: e["BeginOffset"], reverse=True):
        placeholder = f"[{entity['Type']}]"
        text = text[:entity["BeginOffset"]] + placeholder + text[entity["EndOffset"]:]
    return text

def comprehend_anonymize_batch(runs: list[dict]) -> list[dict]:
    # Collect all message texts and remember where they came from.
    # Note: the same run ID may appear twice — once as a create (with inputs)
    # and once as an update (with outputs).
    locations = []  # (run_idx, field, msg_idx)
    texts = []
    for run_idx, run in enumerate(runs):
        for field in ("inputs", "outputs"):
            data = run.get(field)
            if not isinstance(data, dict):
                continue
            for msg_idx, message in enumerate(data.get("messages") or []):
                content = message.get("content", "")
                if content.strip():
                    locations.append((run_idx, field, msg_idx))
                    texts.append(content)

    # Send all texts to Comprehend in batches of 25 (API limit).
    # For 1000 ops (~500 runs) with 2 messages each: 40 API calls instead of 1000.
    redacted_texts = []
    for i in range(0, len(texts), 25):
        chunk = texts[i : i + 25]
        response = comprehend.batch_detect_entities(
            TextList=chunk, LanguageCode="en"
        )
        for text, result in zip(chunk, response["ResultList"]):
            redacted_texts.append(redact_entities(text, result.get("Entities", [])))

    # Write redacted text back into the run dicts
    for (run_idx, field, msg_idx), redacted in zip(locations, redacted_texts):
        runs[run_idx][field]["messages"][msg_idx]["content"] = redacted

    return runs

client = Client(
    process_buffered_run_ops=comprehend_anonymize_batch,
    run_ops_buffer_size=1000,        # ~500 traced calls (2 ops each: create + update)
    run_ops_buffer_timeout_ms=3000,  # or after 3 seconds, whichever comes first
)

@traceable(client=client)
def my_llm_call(messages: list) -> dict:
    # ... your LLM call ...
    pass

try:
    my_llm_call([{"role": "user", "content": "My name is Jane Smith, call me at 555-867-5309"}])
finally:
    client.flush()  # always flush before exit
```

[`process_buffered_run_ops`](https://reference.langchain.com/python/langsmith/client/Client) and `run_ops_buffer_size` must always be set together—providing one without the other raises a `ValueError`.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/mask-inputs-outputs.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Messages view integrations
Source: https://docs.langchain.com/langsmith/messages-view-integrations

Frameworks and SDKs that render in the LangSmith Messages view.

The [Messages view](/langsmith/view-traces#messages-view) renders an agent's trace as a chat-style conversation: user prompts, model responses, tool calls, and tool results, in order. It works automatically with any of the integrations listed in the table on this page. A couple of integrations (`wrap_anthropic` alone, and the JavaScript Claude Agent SDK) need a single metadata key set manually, which are listed in the table and in [Known limitations](#known-limitations).

## Supported integrations

| Integration                           | Tracing SDK                   | Setup required                                               |
| ------------------------------------- | ----------------------------- | ------------------------------------------------------------ |
| LangChain chat models                 | langchain-core                | None                                                         |
| LangGraph                             | langgraph                     | None                                                         |
| `langchain.create_agent`              | langchain                     | None (see caveat in [Known limitations](#known-limitations)) |
| Deep Agents                           | deepagents                    | None                                                         |
| OpenAI Chat Completions               | `wrap_openai`                 | None                                                         |
| OpenAI Responses                      | `wrap_openai` (responses API) | None                                                         |
| OpenAI Agents SDK                     | Python tracing processor      | None                                                         |
| Vercel AI SDK                         | `wrapAISDK`                   | None                                                         |
| Anthropic Messages (`wrap_anthropic`) | `wrap_anthropic`              | Set `ls_message_format: "anthropic"`                         |
| Claude Agent SDK (Python)             | claude-agent-sdk              | None                                                         |
| Claude Agent SDK (JS)                 | claude-agent-sdk-js           | Set `ls_message_format: "anthropic"`                         |
| Claude Code                           | claude-code                   | None                                                         |

For the full detection rules, expected payload shape, and worked JSON examples for each integration, see [Trace format reference](/langsmith/messages-view-trace-format).

## Known limitations

A few integrations need a metadata override to be picked up:

* **`wrap_anthropic` alone:** the wrapper does not set `ls_message_format`, so detection doesn't match today. Set `metadata={"ls_message_format": "anthropic"}` on the call (or via `RunnableConfig`) for the run to be claimed.
* **Claude Agent SDK (JS):** auto-detection currently allowlists only `"claude-agent-sdk"` and `"claude-code"`, not the JS-emitted `"claude-agent-sdk-js"`. Set `ls_message_format: "anthropic"` explicitly on JS traces.
* **`langchain.create_agent`:** not in the explicit detection allowlist. It's claimed today via `ls_provider`/`ls_message_format` fallthroughs in the matching OpenAI/Anthropic detection, or via `graph_id` / `langgraph_node` when the agent runs inside LangGraph. If routing is unreliable, set `metadata.ls_message_format: "langchain"` explicitly.

## Exclude runs from the Messages view

Setting `ls_message_view_exclude` on a run's metadata tells the Messages view to skip that run. The key's presence is what matters; `True` is the conventional value. The filter runs before any extraction strategy sees the trace, so an excluded LLM or tool run never affects detection, message extraction, or tool-call pairing.

Use it for LLM subspans that aren't conversational turns, such as classification calls, embedding lookups, safety filters, or routing/guardrail decisions, that you still want visible elsewhere in LangSmith but don't want cluttering the conversation transcript.

### Python

**1. On a `@traceable` decorator**: exclude a whole function's run.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langsmith import traceable

@traceable(run_type="llm", metadata={"ls_message_view_exclude": True})
def classify_intent(query: str) -> str:
    # This LLM call is internal routing, not part of the chat
    return llm.predict(f"Classify the intent of: {query}")
```

**2. Via the `trace` context manager**: exclude an ad-hoc span.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langsmith import trace

with trace(
    "safety_check",
    run_type="llm",
    metadata={"ls_message_view_exclude": True},
) as run:
    result = safety_model.score(text)
    run.end(outputs={"score": result})
```

**3. From inside a running function**: set the key on the current run tree at any point before the run is patched.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langsmith import get_current_run_tree, traceable

@traceable(run_type="llm")
def maybe_internal(query: str) -> str:
    result = llm.predict(query)
    if _looks_like_routing(query):
        rt = get_current_run_tree()
        if rt is not None:
            rt.add_metadata({"ls_message_view_exclude": True})
    return result
```

**4. Per-call when using `wrap_openai` / `wrap_anthropic`**: pass `langsmith_extra` through to the wrapped client call.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import openai
from langsmith.wrappers import wrap_openai

client = wrap_openai(openai.Client())

resp = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Classify: ..."}],
    langsmith_extra={"metadata": {"ls_message_view_exclude": True}},
)
```

**5. LangChain `RunnableConfig`**: exclude a single invocation of a chain or chat model.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o")
result = llm.invoke(
    "Classify this query",
    config={"metadata": {"ls_message_view_exclude": True}},
)
```

### TypeScript

**1. On a `traceable` wrapper**: exclude a whole function's run.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { traceable } from "langsmith/traceable";

const classifyIntent = traceable(
  async (query: string) => {
    return await llm.predict(`Classify the intent of: ${query}`);
  },
  {
    name: "classify_intent",
    run_type: "llm",
    metadata: { ls_message_view_exclude: true },
  },
);
```

**2. From inside a running function**: mutate the current run tree.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { traceable, getCurrentRunTree } from "langsmith/traceable";

const maybeInternal = traceable(
  async (query: string) => {
    const result = await llm.predict(query);
    if (looksLikeRouting(query)) {
      const rt = getCurrentRunTree();
      rt.extra = rt.extra ?? {};
      rt.extra.metadata = { ...rt.extra.metadata, ls_message_view_exclude: true };
    }
    return result;
  },
  { run_type: "llm" },
);
```

**3. Per-call with `wrapOpenAI`**: pass `langsmithExtra` on the call.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { wrapOpenAI } from "langsmith/wrappers";
import OpenAI from "openai";

const client = wrapOpenAI(new OpenAI());

const resp = await client.chat.completions.create(
  {
    model: "gpt-4o-mini",
    messages: [{ role: "user", content: "Classify: ..." }],
  },
  { langsmithExtra: { metadata: { ls_message_view_exclude: true } } },
);
```

**4. Vercel AI SDK middleware**: pass the key via `lsConfig.metadata` on `wrapAISDK`. The middleware merges this onto every emitted LLM run.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { wrapAISDK } from "langsmith/experimental/vercel";
import * as ai from "ai";

const { generateText } = wrapAISDK(ai, {
  metadata: { ls_message_view_exclude: true },
});
```

To exclude only some calls and not others, wrap with `wrapAISDK` normally and instead mutate `getCurrentRunTree()` from inside a parent `traceable` that calls into the AI SDK, or use a child `RunTree` with `createChild({ extra: { metadata: { ls_message_view_exclude: true } } })`.

**5. Manual `RunTree.createChild`**: when you're building runs by hand.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { RunTree } from "langsmith/run_trees";

const parent = new RunTree({ name: "agent", run_type: "chain" });
const child = parent.createChild({
  name: "safety_check",
  run_type: "llm",
  extra: { metadata: { ls_message_view_exclude: true } },
});
```

### Notes

* The filter checks for the **presence of the key**, not truthiness. `ls_message_view_exclude: false` still excludes the run. Omit the key entirely to include the run.
* Exclusion applies to that run only: child runs are not implicitly excluded. To drop a whole subtree, set the key on each run.
* Excluded runs still appear in the regular trace view, runs explorer, and metrics. Only the Messages view filters them out.

## Manual instrumentation

If you trace without one of the wrappers in [Supported integrations](#supported-integrations)—for example, emitting runs through `RunTree`, the REST API, or a custom wrapper around a provider SDK—set `ls_message_format` on each LLM run's metadata to route the trace to the correct extractor:

| Trace shape                               | Set on metadata                    |
| ----------------------------------------- | ---------------------------------- |
| LangChain messages (constructor envelope) | `ls_message_format: "langchain"`   |
| OpenAI Chat Completions                   | `ls_message_format: "completions"` |
| OpenAI Responses API                      | `ls_message_format: "responses"`   |
| Anthropic Messages API                    | `ls_message_format: "anthropic"`   |

For the JSON shape each extractor expects, see the [Trace format reference](/langsmith/messages-view-trace-format).

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/messages-view-integrations.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Messages view trace format reference
Source: https://docs.langchain.com/langsmith/messages-view-trace-format

Detection rules, payload shapes, and examples for how the LangSmith Messages view extracts conversations from traces.

<Note>
  If you trace with a [supported integration](/langsmith/messages-view-integrations), your traces render in the [Messages view](/langsmith/view-traces#messages-view) automatically.
</Note>

Use this reference when you're tracing an agent framework or LLM client that isn't on the supported list, emitting runs manually through `RunTree` or the REST API, or diagnosing a trace that does not render correctly in the [Messages view](/langsmith/view-traces#messages-view).

[*Extraction strategy*](#extraction-strategy-resolution) refers to the per-integration logic that reads the LLM and tool runs in a trace and produces the ordered conversation the Messages view renders. For each supported integration, this page documents the metadata keys that determine which strategy LangSmith applies, the JSON shape the strategy expects on `inputs` and `outputs`, and how tool calls are paired with their results.

<Note>
  **Tracing default** on this page means the LangSmith SDK sets the relevant metadata key automatically when you use the documented entry point. Anything else is the integration vendor's own instrumentation or a user override.
</Note>

## Extraction strategy resolution

For each trace, the first matching extraction strategy wins. Each strategy's detection explicitly defers to others when it sees markers from another integration. The most common collision: `ls_provider: "openai"` paired with a LangChain-shaped payload; the OpenAI strategy defers to LangChain in that case. If no strategy matches the first run of the trace, the messages API returns `400 no adapter pair found for trace format`.

| Integration                                                                 | Strategy  | Primary metadata signal                                                     | Tracing default (LangSmith SDK)             |
| --------------------------------------------------------------------------- | --------- | --------------------------------------------------------------------------- | ------------------------------------------- |
| [Vercel AI SDK](#vercel-ai-sdk)                                             | vercel    | `ls_integration: "vercel-ai-sdk"` or `ai_sdk_method`                        | Yes (`wrapAISDK`)                           |
| [OpenAI Chat Completions](#openai-wrap_openai)                              | openai    | `ls_provider: "openai"` or `"azure"` (no `use_responses_api`)               | Yes (`wrap_openai`)                         |
| [OpenAI Responses](#openai-wrap_openai)                                     | openai    | `ls_provider` plus `ls_invocation_params.use_responses_api: true`           | Yes (`wrap_openai` responses)               |
| [OpenAI Agents SDK](#openai-wrap_openai)                                    | openai    | `ls_integration: "openai-agents-sdk"`                                       | Yes (Python tracing processor)              |
| [Anthropic Messages (`wrap_anthropic`)](#anthropic-messages-wrap_anthropic) | anthropic | `ls_message_format: "anthropic"` (must be set explicitly today)             | Partial: provider set, format key is opt-in |
| [Claude Agent SDK (Python)](#anthropic-messages-wrap_anthropic)             | anthropic | `ls_integration: "claude-agent-sdk"`                                        | Yes                                         |
| [Claude Code](#anthropic-messages-wrap_anthropic)                           | anthropic | `ls_integration: "claude-code"`                                             | Set by claude-code itself                   |
| [Claude Agent SDK (JS)](#anthropic-messages-wrap_anthropic)                 | anthropic | Currently does **not** auto-match (emits `"claude-agent-sdk-js"`)           | Provider yes, format no (gap)               |
| [LangChain chat models](#langchain-and-langgraph)                           | langchain | `ls_integration: "langchain_chat_model"`                                    | Yes (langchain-core)                        |
| [LangGraph](#langchain-and-langgraph)                                       | langchain | `graph_id` or `langgraph_node`                                              | Yes (langgraph)                             |
| [`langchain.create_agent`](#langchain-and-langgraph)                        | langchain | `ls_integration: "langchain_create_agent"` (falls through to other signals) | Yes (langchain)                             |
| [Deep Agents](#langchain-and-langgraph)                                     | langchain | `ls_integration: "deepagents"` or `"deepagents-cli"`                        | Yes (deepagents)                            |

## LangChain and LangGraph

Covers `BaseChatModel`-derived LLM runs, LangGraph graphs, `deepagents`, and `langchain.create_agent`.

### Detection

Any of the following on metadata triggers extraction:

* `ls_message_format` is `"langchain"` (explicit override)
* `ls_integration` is `"langchain_chat_model"`, `"deepagents"`, or `"deepagents-cli"`
* `graph_id` is present (LangGraph root)
* `langgraph_node` is present (LangGraph sub-run; sub-runs carry this even when `graph_id` is only on the root)

OpenAI detection explicitly defers to LangChain when these markers are present, so LangChain extraction wins even when `ls_provider: "openai"`.

### Tracing defaults

**`langchain-core`** `BaseChatModel` sets the following on every chat-model run:

* `metadata.ls_integration`: `"langchain_chat_model"`
* Plus the provider-specific `_get_ls_params()` output (`ls_provider`, `ls_model_name`, `ls_model_type`, `ls_temperature`, `ls_max_tokens`, `ls_stop`)

**`langchain.create_agent`** sets `metadata.ls_integration: "langchain_create_agent"` on the agent config.

<Note>
  `langchain_create_agent` is not in the explicit detection allowlist. It's claimed today via the `ls_provider`/`ls_message_format` fallthroughs in the matching OpenAI/Anthropic detection, or via `graph_id` / `langgraph_node` when the agent runs inside LangGraph. If routing is unreliable, set `metadata.ls_message_format: "langchain"` explicitly.
</Note>

**LangGraph** sets `graph_id` (root) and `langgraph_node` (every sub-run).

**Deep Agents** sets `metadata.ls_integration: "deepagents"` on the root chain run; the CLI variant uses `"deepagents-cli"`.

### Run shape

LangChain serializes messages with its constructor format. The `id` array's last element identifies the class:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "lc": 1,
  "type": "constructor",
  "id": ["langchain", "schema", "messages", "AIMessage"],
  "kwargs": {
    "content": "...",
    "id": "run-abc-123",
    "type": "ai",
    "tool_calls": [
      {"name": "search", "args": {}, "id": "call_1", "type": "tool_call"}
    ],
    "tool_call_id": "call_1"
  }
}
```

Role mapping (last element of `id` → canonical role):

* `SystemMessage` → system
* `HumanMessage` → human
* `AIMessage` → ai
* `ToolMessage`, `FunctionMessage` → tool
* `ChatMessage` → human

**Inputs:**

* `inputs.messages` is `[[msg, msg, ...]]`. LangChain wraps in an extra array for batched generations; the outer array is unwrapped during extraction.

**Outputs** (multiple paths, tried in order):

1. `outputs.generations[0][*].message`: standard chat-model output
2. `outputs.messages[]`: direct messages (e.g., LangGraph state outputs)
3. `outputs.output.update.messages[]`: deepagents-cli subagent outputs; the inner messages carry `tool_call_id` linking to the subagent invocation
4. `outputs.output` (object): fallback for tool runs

### Tool-call matching

`tool_calls[*].id` on the assistant message matches either `kwargs.tool_call_id` (constructor format) or top-level `tool_call_id` (flat format) on the tool-result message.

### Dedup

Prefer `kwargs.id` (constructor format), then top-level `id` (flat format), then fall back to a `role + content` hash. Stable LangChain run IDs make dedup cheap across re-emissions.

### Example trace

A LangChain chat-model run that issues a tool call, the tool run, and the follow-up. Note the double-nesting on `inputs.messages` (`[[ ... ]]`) and the `generations` envelope on outputs.

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
[
  {
    "id": "0001",
    "trace_id": "trace-0005",
    "run_type": "llm",
    "name": "ChatOpenAI",
    "metadata": {
      "ls_integration": "langchain_chat_model",
      "ls_provider": "openai",
      "ls_model_name": "gpt-4o"
    },
    "inputs": {
      "messages": [[
        {"lc": 1, "type": "constructor", "id": ["langchain","schema","messages","SystemMessage"],
         "kwargs": {"content": "You are a helpful assistant.", "id": "sys-1"}},
        {"lc": 1, "type": "constructor", "id": ["langchain","schema","messages","HumanMessage"],
         "kwargs": {"content": "what is the weather in paris?", "id": "hu-1"}}
      ]]
    },
    "outputs": {
      "generations": [[{
        "message": {
          "lc": 1, "type": "constructor",
          "id": ["langchain","schema","messages","AIMessage"],
          "kwargs": {
            "content": "",
            "id": "ai-1",
            "tool_calls": [
              {"name": "get_weather", "args": {"city": "Paris"}, "id": "call_abc", "type": "tool_call"}
            ]
          }
        }
      }]]
    }
  },
  {
    "id": "0002",
    "trace_id": "trace-0005",
    "parent_run_id": "0001",
    "run_type": "tool",
    "name": "get_weather",
    "metadata": {"ls_integration": "langchain_chat_model"},
    "inputs": {"city": "Paris"},
    "outputs": {
      "output": {
        "lc": 1, "type": "constructor",
        "id": ["langchain","schema","messages","ToolMessage"],
        "kwargs": {"content": "Sunny, 22C", "tool_call_id": "call_abc", "id": "tool-1"}
      }
    }
  },
  {
    "id": "0003",
    "trace_id": "trace-0005",
    "run_type": "llm",
    "name": "ChatOpenAI",
    "metadata": {
      "ls_integration": "langchain_chat_model",
      "ls_provider": "openai",
      "ls_model_name": "gpt-4o"
    },
    "inputs": {
      "messages": [[
        {"lc": 1, "type": "constructor", "id": ["langchain","schema","messages","SystemMessage"],
         "kwargs": {"content": "You are a helpful assistant.", "id": "sys-1"}},
        {"lc": 1, "type": "constructor", "id": ["langchain","schema","messages","HumanMessage"],
         "kwargs": {"content": "what is the weather in paris?", "id": "hu-1"}},
        {"lc": 1, "type": "constructor", "id": ["langchain","schema","messages","AIMessage"],
         "kwargs": {"content": "", "id": "ai-1",
                    "tool_calls": [{"name": "get_weather", "args": {"city": "Paris"}, "id": "call_abc", "type": "tool_call"}]}},
        {"lc": 1, "type": "constructor", "id": ["langchain","schema","messages","ToolMessage"],
         "kwargs": {"content": "Sunny, 22C", "tool_call_id": "call_abc", "id": "tool-1"}}
      ]]
    },
    "outputs": {
      "generations": [[{
        "message": {
          "lc": 1, "type": "constructor",
          "id": ["langchain","schema","messages","AIMessage"],
          "kwargs": {"content": "It's sunny and 22°C in Paris.", "id": "ai-2"}
        }
      }]]
    }
  }
]
```

LangGraph traces look the same but add `graph_id` / `langgraph_node` to the metadata, and may use `outputs.messages[]` directly instead of `outputs.generations`.

## OpenAI (`wrap_openai`)

One extraction strategy covers both OpenAI API shapes (Chat Completions and Responses) and the OpenAI Agents SDK (Responses shape). Detection picks the API shape from metadata.

### Detection

Decision tree, in order. The first rule that matches wins.

1. `metadata.ls_integration`:
   * `"openai-agents-sdk"` → Responses
   * `"langchain_chat_model"`, `"deepagents"`, `"deepagents-cli"` → not claimed (these emit LangChain-shaped payloads with `ls_provider: "openai"`; LangChain extraction takes them)
2. `metadata.ls_message_format` (explicit override, wins over the `ls_provider` heuristic):
   * `"responses"` → Responses
   * `"completions"` → Completions
   * `"langchain"`, `"anthropic"` → not claimed
   * Unknown values fall through to rule 3 so future format strings keep working
3. `metadata.graph_id` or `metadata.langgraph_node` present → not claimed (LangGraph subtree; LangChain extraction takes it even when `ls_provider: "openai"`)
4. `metadata.ls_provider` is `"openai"` or `"azure"`:
   * If `metadata.ls_invocation_params.use_responses_api == true` → Responses
   * Otherwise → Completions

### Tracing defaults

**`wrap_openai`** sets the following on every LLM run:

* `metadata.ls_provider`: `"openai"` (or `"azure"` if the client is `AzureOpenAI` / `AsyncAzureOpenAI`)
* `metadata.ls_model_type`: `"chat"` or `"llm"`
* `metadata.ls_model_name`, `ls_temperature`, `ls_max_tokens`, `ls_stop`
* `metadata.ls_invocation_params`: an allowlisted subset of the SDK call kwargs. When the call goes through `client.responses.create` or `client.responses.parse`, this dict contains `use_responses_api: true`.
* `run_type`: `"llm"`
* `name`: `"ChatOpenAI"`, `"OpenAI"`, `"AzureChatOpenAI"`, or `"AzureOpenAI"` (overridable)

`wrap_openai` does **not** emit `ls_integration` or `ls_message_format`. Detection falls through to rule 4 (`ls_provider`).

**OpenAI Agents SDK** uses a tracing processor (not a wrapper). On every span it sets:

* `metadata.ls_integration`: `"openai-agents-sdk"`
* `metadata.ls_integration_version`: package version
* `metadata.ls_agent_type`: `"root"` on the root span
* LLM spans also carry `metadata.openai_trace_id` and `openai_span_id`

The Agents SDK emits Responses-API-shaped payloads but with `outputs = {"output": [...]}` only. The rest of the Response envelope (`id`, `model`, `tools`, `usage`) lives in `extra.metadata`, not in `outputs`.

### Run shape

**Completions:**

* `inputs.messages` is an array of `{role, content, tool_calls?, tool_call_id?, refusal?, name?, id?}`
* `outputs.choices[*].message` has the same shape (typically `role: "assistant"`)
* Tool call IDs live on `tool_calls[*].id`; tool-result messages link back via top-level `tool_call_id`

**Responses:**

* Optional top-level `inputs.instructions` (string) is promoted to a synthetic system message and prepended.
* `inputs.input` is an array of items where each item is one of:
  * A simple `{role, content}` message
  * A typed `{type: "message", role, content}`
  * `{type: "function_call", call_id, name, arguments}` (assistant role)
  * `{type: "function_call_output", call_id, output}` (tool role)
  * `{type: "reasoning", ...}` (assistant role)
* `outputs.output` has the same array shape for LLM runs. For tool runs it can be a string, an object, or a bare top-level object (Agents SDK case); each is wrapped as a tool-role message with `content` set to the JSON text.

### Tool-call matching

* Completions: `tool_call_id` on the tool-result message matches `tool_calls[*].id` on the prior assistant message.
* Responses: `call_id` on `function_call` matches `call_id` on `function_call_output`. Bare-object tool-run outputs may carry `call_id` at the top level of `outputs`.

### Dedup

Responses items dedup by `id` when present, else by item-type-specific content: `call_id|arguments` for `function_call`, `call_id|output` for `function_call_output`, and `content` for messages.

### Example traces

**Chat Completions (`wrap_openai`):** three runs: a tool-calling assistant turn, the tool run, and the follow-up assistant turn with the final answer.

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
[
  {
    "id": "0001",
    "trace_id": "trace-0002",
    "run_type": "llm",
    "name": "ChatOpenAI",
    "metadata": {"ls_provider": "openai", "ls_model_name": "gpt-4o"},
    "inputs": {
      "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "what is the weather in paris?"}
      ]
    },
    "outputs": {
      "choices": [{
        "index": 0,
        "finish_reason": "tool_calls",
        "message": {
          "role": "assistant",
          "content": null,
          "tool_calls": [{
            "id": "call_abc123",
            "type": "function",
            "function": {"name": "get_weather", "arguments": "{\"city\":\"Paris\"}"}
          }]
        }
      }]
    }
  },
  {
    "id": "0002",
    "trace_id": "trace-0002",
    "parent_run_id": "0001",
    "run_type": "tool",
    "name": "get_weather",
    "inputs": {"city": "Paris"},
    "outputs": {"tool_call_id": "call_abc123", "role": "tool", "content": "Sunny, 22C"}
  },
  {
    "id": "0003",
    "trace_id": "trace-0002",
    "run_type": "llm",
    "name": "ChatOpenAI",
    "metadata": {"ls_provider": "openai", "ls_model_name": "gpt-4o"},
    "inputs": {
      "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "what is the weather in paris?"},
        {"role": "assistant", "content": null, "tool_calls": [
          {"id": "call_abc123", "type": "function", "function": {"name": "get_weather", "arguments": "{\"city\":\"Paris\"}"}}
        ]},
        {"role": "tool", "tool_call_id": "call_abc123", "content": "Sunny, 22C"}
      ]
    },
    "outputs": {
      "choices": [{
        "index": 0,
        "finish_reason": "stop",
        "message": {"role": "assistant", "content": "It's sunny and 22°C in Paris."}
      }]
    }
  }
]
```

**Responses API (OpenAI Agents SDK):** items are typed (`function_call`, `function_call_output`, `message`) rather than role-keyed. `inputs.instructions` is promoted to a synthetic system message.

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
[
  {
    "id": "0001",
    "trace_id": "trace-0003",
    "run_type": "llm",
    "name": "Helpful Assistant Response",
    "metadata": {"ls_integration": "openai-agents-sdk", "ls_model_name": "gpt-4.1"},
    "inputs": {
      "instructions": "You are a helpful assistant.",
      "input": [{"role": "user", "content": "what time is it in san francisco?"}]
    },
    "outputs": {
      "output": [{
        "type": "function_call",
        "call_id": "call_LVsl",
        "name": "get_time",
        "arguments": "{\"timezone\":\"America/Los_Angeles\"}",
        "id": "fc_0ed8"
      }]
    }
  },
  {
    "id": "0002",
    "trace_id": "trace-0003",
    "parent_run_id": "0001",
    "run_type": "tool",
    "name": "get_time",
    "metadata": {"ls_integration": "openai-agents-sdk"},
    "inputs": {"timezone": "America/Los_Angeles"},
    "outputs": {"output": "12:00 PM (America/Los_Angeles)", "call_id": "call_LVsl"}
  },
  {
    "id": "0003",
    "trace_id": "trace-0003",
    "run_type": "llm",
    "name": "Helpful Assistant Response",
    "metadata": {"ls_integration": "openai-agents-sdk", "ls_model_name": "gpt-4.1"},
    "inputs": {
      "instructions": "You are a helpful assistant.",
      "input": [
        {"role": "user", "content": "what time is it in san francisco?"},
        {"type": "function_call", "call_id": "call_LVsl", "name": "get_time", "arguments": "{\"timezone\":\"America/Los_Angeles\"}", "id": "fc_0ed8"},
        {"type": "function_call_output", "call_id": "call_LVsl", "output": "12:00 PM (America/Los_Angeles)"}
      ]
    },
    "outputs": {
      "output": [{
        "type": "message",
        "role": "assistant",
        "status": "completed",
        "content": [{"type": "output_text", "text": "It is currently 12:00 PM in San Francisco.", "annotations": []}]
      }]
    }
  }
]
```

## Vercel AI SDK

### Detection

Either of the following on `extra.metadata` of any LLM run triggers extraction:

* `ai_sdk_method` key is present (any value), or
* `ls_integration` is `"vercel-ai-sdk"`

Both are set automatically by the LangSmith Vercel AI SDK wrapper. The underlying language-model provider (OpenAI, Anthropic, Google, etc.) is irrelevant; the wrapper normalizes all of them into a single message envelope.

### Tracing defaults

When the Vercel AI SDK wrapper is in use, the SDK sets on every LLM run:

* `metadata.ls_integration`: `"vercel-ai-sdk"`
* `metadata.ai_sdk_method`: `"ai.doGenerate"` or `"ai.doStream"`
* `metadata.ls_model_name`: the model id
* `run_type`: `"llm"`
* `name`: `"ai.doGenerate"` or `"ai.doStream"` (overridable)

### Run shape

LLM runs:

* `run_type: "llm"`
* `inputs.messages` or `inputs.prompt` contains the conversation
* `outputs.role` is one of `assistant`, `tool`, `user`
* `outputs.content` contains the emitted content. Tool calls are blocks within `content` carrying `toolCallId` and `toolName`.

Tool runs:

* `run_type: "tool"`
* `inputs.toolCallId` matches the LLM output's `toolCallId`
* `inputs.toolName` or `name` identifies the tool
* `outputs.output` or `outputs.result` holds the tool result

### Tool-call matching

Prefer matching by `toolCallId`; fall back to tool name when the ID is unavailable.

### Example trace

A two-run trace: one LLM run that asks for a tool call, one tool run that returns the result. Each entry is one LangSmith run; `inputs`, `outputs`, and `metadata` are JSON-encoded strings on the wire (shown unescaped here for readability).

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
[
  {
    "id": "0001",
    "trace_id": "trace-0001",
    "run_type": "llm",
    "name": "ai.doGenerate",
    "metadata": {
      "ls_integration": "vercel-ai-sdk",
      "ai_sdk_method": "ai.doGenerate",
      "ls_model_name": "gpt-4o"
    },
    "inputs": {
      "prompt": [
        {"role": "user", "content": [{"type": "text", "text": "what's the weather in paris?"}]}
      ]
    },
    "outputs": {
      "role": "assistant",
      "content": [
        {"type": "tool-call", "toolCallId": "call_abc", "toolName": "get_weather", "input": {"city": "Paris"}}
      ]
    }
  },
  {
    "id": "0002",
    "trace_id": "trace-0001",
    "parent_run_id": "0001",
    "run_type": "tool",
    "name": "get_weather",
    "inputs": {"toolCallId": "call_abc", "toolName": "get_weather", "args": {"city": "Paris"}},
    "outputs": {"result": "Sunny, 22C"}
  }
]
```

## Anthropic Messages (`wrap_anthropic`)

Covers `wrap_anthropic` (the Messages-API wrapper) and the Claude Agent SDK / Claude Code integrations.

### Detection

Any of the following on metadata triggers extraction:

* `ls_message_format` is `"anthropic"`
* `ls_integration` is `"claude-agent-sdk"` or `"claude-code"`

### Tracing defaults

**`wrap_anthropic`** sets the following on every LLM run:

* `metadata.ls_provider`: `"anthropic"`
* `metadata.ls_model_type`: `"chat"`
* `metadata.ls_model_name`, `ls_temperature`, `ls_max_tokens`, `ls_stop`
* `metadata.ls_invocation_params`: an allowlisted subset (`mcp_servers`, `service_tier`, `tool_choice`, `top_k`, `top_p`, `stream`, `thinking`)
* `run_type`: `"llm"`, `name`: `"ChatAnthropic"` (overridable)

`wrap_anthropic` does **not** emit `ls_integration` or `ls_message_format`.

<Warning>
  **Known limitation:** with only the wrapper, detection does not match today. Set `ls_message_format: "anthropic"` explicitly for the run to be claimed.
</Warning>

**Claude Agent SDK (Python)** sets the following on the root chain run:

* `metadata.ls_integration`: `"claude-agent-sdk"`
* `metadata.ls_integration_version`: package version
* Optional `metadata.model`, `permission_mode`, `max_turns`

Its synthetic LLM child runs get `metadata.ls_provider: "anthropic"` and optionally `ls_model_name`, but no `ls_integration`. They ride along on the parent chain's claim (the first run of the trace drives the choice).

**Claude Agent SDK (JS)** sets `metadata.ls_integration: "claude-agent-sdk-js"` and `ls_agent_type: "root"`.

<Warning>
  **Known limitation:** only `"claude-agent-sdk"` and `"claude-code"` are auto-detected today, not `"claude-agent-sdk-js"`. JS traces need `ls_message_format: "anthropic"` set explicitly to be picked up.
</Warning>

### Run shape

**`wrap_anthropic`** Messages API:

* `inputs.messages`: `[{role, content}, ...]`
* Optional `inputs.system`: string OR array of content blocks; becomes a prepended system message
* `content` may be a string or an array of `{type, ...}` content blocks (`text`, `tool_use`, `tool_result`, `image`, `thinking`, `redacted_thinking`)
* Outputs preserve the full Anthropic `Message` object. Content is found at one of:
  * `outputs.message.content` (most common, wrapped)
  * `outputs.content` when `outputs.type == "message"` (bare)
  * `outputs.content` when `outputs.role == "assistant"` (Agents SDK bare)
  * `outputs.output.messages[0].content` (JS SDK)
  * `outputs.messages[0].content` (Claude Code)

**Claude Agent SDK / Claude Code:**

* `inputs.input` (array of messages, same Anthropic message shape). `inputs.messages` takes precedence when both are present and non-empty.
* Tool-run outputs use either `outputs.output` (object) or `outputs.content` (top-level array, subagent-style).

### Tool-call matching

`tool_use_id` on the assistant `tool_use` block matches `tool_result.tool_use_id` on the corresponding result block within the next user message.

### Example trace

`wrap_anthropic` Messages API with a tool call and follow-up. The assistant turn returns a content array containing a `tool_use` block; the tool result is sent back as a `tool_result` block inside the next user message.

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
[
  {
    "id": "0001",
    "trace_id": "trace-0004",
    "run_type": "llm",
    "name": "ChatAnthropic",
    "metadata": {
      "ls_provider": "anthropic",
      "ls_model_name": "claude-opus-4-7",
      "ls_message_format": "anthropic"
    },
    "inputs": {
      "system": "You are a helpful assistant.",
      "messages": [
        {"role": "user", "content": "what is the weather in paris?"}
      ]
    },
    "outputs": {
      "message": {
        "id": "msg_01",
        "role": "assistant",
        "type": "message",
        "content": [
          {"type": "text", "text": "Let me check."},
          {"type": "tool_use", "id": "toolu_01", "name": "get_weather", "input": {"city": "Paris"}}
        ]
      }
    }
  },
  {
    "id": "0002",
    "trace_id": "trace-0004",
    "parent_run_id": "0001",
    "run_type": "tool",
    "name": "get_weather",
    "inputs": {"city": "Paris"},
    "outputs": {"output": {"temperature": 22, "condition": "Sunny"}}
  },
  {
    "id": "0003",
    "trace_id": "trace-0004",
    "run_type": "llm",
    "name": "ChatAnthropic",
    "metadata": {
      "ls_provider": "anthropic",
      "ls_model_name": "claude-opus-4-7",
      "ls_message_format": "anthropic"
    },
    "inputs": {
      "system": "You are a helpful assistant.",
      "messages": [
        {"role": "user", "content": "what is the weather in paris?"},
        {"role": "assistant", "content": [
          {"type": "text", "text": "Let me check."},
          {"type": "tool_use", "id": "toolu_01", "name": "get_weather", "input": {"city": "Paris"}}
        ]},
        {"role": "user", "content": [
          {"type": "tool_result", "tool_use_id": "toolu_01", "content": "Sunny, 22C"}
        ]}
      ]
    },
    "outputs": {
      "message": {
        "id": "msg_02",
        "role": "assistant",
        "type": "message",
        "content": [{"type": "text", "text": "It's sunny and 22°C in Paris."}]
      }
    }
  }
]
```

Claude Agent SDK / Claude Code traces look similar but use `inputs.input` instead of `inputs.messages` and set `ls_integration: "claude-agent-sdk"` (or `"claude-code"`) on the root chain run.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/messages-view-trace-format.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
