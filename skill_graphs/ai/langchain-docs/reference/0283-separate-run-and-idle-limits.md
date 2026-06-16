# Separate run and idle limits
builder.add_node(
    "call_model",
    call_model,
    timeout=TimeoutPolicy(run_timeout=120, idle_timeout=30),
)
```

<Warning>
  Node timeouts only apply to **async** nodes. Sync nodes with a `timeout` are rejected at compile time. To wrap blocking I/O, use `asyncio.to_thread` inside an async node.
</Warning>

### Run timeout

`run_timeout` is a hard wall-clock cap on a single attempt. It is never refreshed, regardless of node activity:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langgraph.types import TimeoutPolicy

builder.add_node(
    "call_model",
    call_model,
    timeout=TimeoutPolicy(run_timeout=120),
)
```

When the limit is exceeded, LangGraph raises [`NodeTimeoutError`](https://reference.langchain.com/python/langgraph/errors/NodeTimeoutError), clears any writes from the failed attempt, and lets the retry policy decide whether to retry.

### Idle timeout

`idle_timeout` is a progress-resetting cap. It fires only when the node stops making observable progress for the specified duration—unlike `run_timeout`, the clock resets whenever the node produces a progress signal:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
builder.add_node(
    "call_model",
    call_model,
    timeout=TimeoutPolicy(idle_timeout=30),
)
```

You can set `run_timeout` and `idle_timeout` together. Whichever fires first cancels the attempt.

#### Progress signals

Under the default `refresh_on="auto"`, the idle clock resets on any of the following:

* State writes via `CONFIG_KEY_SEND`
* Stream output (yielded async stream chunks)
* Child-task scheduling
* Runtime stream-writer calls
* Any LangChain callback event from the node or its descendants (LLM tokens, tool calls, chain start/end, etc.)

#### Heartbeat mode

Set `refresh_on="heartbeat"` to narrow the refresh source to explicit `runtime.heartbeat()` calls only. This is useful when you want a strict idle definition that isn't reset by chatty subordinates:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
builder.add_node(
    "call_model",
    call_model,
    timeout=TimeoutPolicy(idle_timeout=30, refresh_on="heartbeat"),
)
```

#### Manual heartbeats

For long-running work that doesn't naturally emit progress signals, call `runtime.heartbeat()` to manually reset the idle clock:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langgraph.graph import StateGraph, START, END
from langgraph.runtime import Runtime
from langgraph.types import TimeoutPolicy
from typing_extensions import TypedDict

class State(TypedDict):
    result: str

async def long_running_node(state: State, runtime: Runtime) -> State:
    for batch in fetch_batches():
        process(batch)
        runtime.heartbeat()  # [!code highlight]
    return {"result": "done"}

builder = StateGraph(State)
builder.add_node(
    "long_running_node",
    long_running_node,
    timeout=TimeoutPolicy(idle_timeout=30, refresh_on="heartbeat"),
)
builder.add_edge(START, "long_running_node")
builder.add_edge("long_running_node", END)
```

`runtime.heartbeat()` is a no-op outside an idle-timed attempt, so you can call it unconditionally.

### NodeTimeoutError

When a timeout fires, LangGraph raises [`NodeTimeoutError`](https://reference.langchain.com/python/langgraph/errors/NodeTimeoutError) with structured context about which limit was hit:

| Attribute      | Type                     | Description                                    |
| -------------- | ------------------------ | ---------------------------------------------- |
| `node`         | `str`                    | Name of the node whose execution timed out.    |
| `elapsed`      | `float`                  | Seconds elapsed before the timeout fired.      |
| `kind`         | `Literal["idle", "run"]` | Which timeout fired.                           |
| `idle_timeout` | `float \| None`          | The configured idle timeout (seconds), if any. |
| `run_timeout`  | `float \| None`          | The configured run timeout (seconds), if any.  |

`NodeTimeoutError` is retryable by default. Combining `timeout` with a retry policy works out of the box—the timeout clock resets on each new attempt, and writes from a timed-out attempt are cleared before the next retry:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langgraph.types import RetryPolicy, TimeoutPolicy

builder.add_node(
    "call_model",
    call_model,
    timeout=TimeoutPolicy(idle_timeout=30),
    retry_policy=RetryPolicy(max_attempts=3),
)
```

### Dynamic timeouts with Send

When using [`Send`](https://reference.langchain.com/python/langgraph/types/Send) to dispatch nodes dynamically (for example, in map-reduce patterns), you can pass a timeout directly on the `Send` to override the target node's static timeout for that specific push:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langgraph.types import Send, TimeoutPolicy

def fan_out(state: OverallState):
    return [
        Send("process_item", {"item": item}, timeout=TimeoutPolicy(idle_timeout=15))
        for item in state["items"]
    ]
```

If the timeout is omitted on the `Send`, the target node's timeout (set at [`add_node`](https://reference.langchain.com/python/langgraph/graph/state/StateGraph/add_node) time) applies. This lets you set a default timeout on the node and tighten it for individual calls.

## Error handling

<Note>
  Requires `langgraph>=1.2`.
</Note>

An error handler runs after a node fails and all retries are exhausted. It receives the current state and can update it or route to a different node using [`Command`](https://reference.langchain.com/python/langgraph/types/Command). This is useful for compensation flows (Saga patterns) where you want to recover gracefully rather than abort the entire graph.

Pass `error_handler=` to [`add_node`](https://reference.langchain.com/python/langgraph/graph/state/StateGraph/add_node):

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langgraph.errors import NodeError
from langgraph.types import Command, RetryPolicy
from langgraph.graph import StateGraph, START
from typing_extensions import TypedDict

class State(TypedDict):
    status: str

def charge_payment(state: State) -> State:
    raise RuntimeError("payment gateway timeout")

def payment_error_handler(state: State, error: NodeError) -> Command:
    return Command(
        update={"status": f"compensated: {error.error}"},
        goto="finalize",
    )

def finalize(state: State) -> State:
    return state

graph = (
    StateGraph(State)
    .add_node(
        "charge_payment",
        charge_payment,
        retry_policy=RetryPolicy(max_attempts=3, retry_on=ConnectionError),
        error_handler=payment_error_handler,
    )
    .add_node("finalize", finalize)
    .add_edge(START, "charge_payment")
    .compile()
)
```

The handler fires only after the retry policy is exhausted, or immediately if no retry policy is configured. The retry policy and the error handler stay decoupled: configure when to retry and when to compensate independently.

### NodeError

Error handlers receive failure context through a typed `error: NodeError` parameter, injected by type annotation (the same pattern as `runtime: Runtime`):

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langgraph.errors import NodeError

def my_handler(state: State, error: NodeError) -> Command:
    print(f"Node {error.node} failed with: {error.error}")
    return Command(update={"status": "recovered"}, goto="next_step")
```

[`NodeError`](https://reference.langchain.com/python/langgraph/errors/NodeError) is a frozen dataclass with two fields:

| Attribute | Type            | Description                              |
| --------- | --------------- | ---------------------------------------- |
| `node`    | `str`           | Name of the node whose execution failed. |
| `error`   | `BaseException` | The exception raised by the failed node. |

The `error: NodeError` parameter is opt-in. Handlers that don't need failure context can use simpler signatures like `(state)` or `(state, runtime)`.

### Route with Command

Error handlers can return a [`Command`](https://reference.langchain.com/python/langgraph/types/Command) to update state and route to a specific node, enabling Saga / compensation patterns:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langgraph.errors import NodeError
from langgraph.types import Command, RetryPolicy
from langgraph.graph import StateGraph, START
from typing_extensions import TypedDict

class State(TypedDict):
    status: str

def reserve_inventory(state: State) -> State:
    return {"status": "reserved"}

def charge_payment(state: State) -> State:
    raise RuntimeError("payment timeout")

def payment_error_handler(state: State, error: NodeError) -> Command:
    return Command(
        update={"status": f"compensated_after_{error.node}: {error.error}"},
        goto="finalize",
    )

def finalize(state: State) -> State:
    return state

graph = (
    StateGraph(State)
    .add_node("reserve_inventory", reserve_inventory)
    .add_node(
        "charge_payment",
        charge_payment,
        retry_policy=RetryPolicy(max_attempts=3, retry_on=ConnectionError),
        error_handler=payment_error_handler,
    )
    .add_node("finalize", finalize)
    .add_edge(START, "reserve_inventory")
    .add_edge("reserve_inventory", "charge_payment")
    .compile()
)
```

`charge_payment` retries on `ConnectionError` up to 3 times. If retries are exhausted (or the error isn't a `ConnectionError`), the handler compensates by updating state and routing to `finalize` instead of aborting the graph.

### Resume-safe failures

<Note>
  Failure provenance is checkpointed. If the graph is interrupted or the process crashes after a node fails but before the handler completes, the handler sees the same `NodeError` context when the graph resumes from its checkpoint.
</Note>

### Behavior with `interrupt()`

<Warning>
  `interrupt()` raised inside a node is **not** routed to the error handler. Interrupts use the `GraphBubbleUp` mechanism to pause graph execution for human-in-the-loop workflows, bypassing both retry policies and error handlers. The graph pauses as usual.
</Warning>

### Subgraph failures

If a node wraps a subgraph and the subgraph raises an unhandled exception, that exception surfaces to the parent node. If the parent node has an error handler, the handler fires with the subgraph's exception in `error.error`.

## Graph defaults

<Note>
  Requires `langgraph>=1.2`.
</Note>

Instead of repeating the same `retry_policy=`, `error_handler=`, `timeout=`, or `cache_policy=` on every `add_node` call, use `set_node_defaults()` to configure graph-wide defaults in one place:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langgraph.errors import NodeError
from langgraph.types import RetryPolicy, TimeoutPolicy
from langgraph.graph import StateGraph, START
from typing_extensions import TypedDict

class State(TypedDict):
    status: str

def default_error_handler(state: State, error: NodeError) -> State:
    return {"status": f"handled: {error.error}"}

graph = (
    StateGraph(State)
    .set_node_defaults(
        retry_policy=RetryPolicy(max_attempts=3),
        error_handler=default_error_handler,
        timeout=TimeoutPolicy(run_timeout=30),
    )
    .add_node("step_a", step_a)
    .add_node("step_b", step_b)
    .add_edge(START, "step_a")
    .compile()
)
```

Both `step_a` and `step_b` now share the same retry policy, error handler, and timeout without any duplication.

### Precedence

Per-node values passed directly to `add_node()` always override the defaults set by `set_node_defaults()`. Defaults are resolved at `compile()` time, so you can call `set_node_defaults()` before or after `add_node()` in any order:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
graph = (
    StateGraph(State)
    .set_node_defaults(error_handler=default_error_handler)
    .add_node("step_a", step_a)                                     # uses default_error_handler
    .add_node("step_b", step_b, error_handler=custom_error_handler) # uses custom_error_handler
    .add_edge(START, "step_a")
    .compile()
)
```

### Default error handler

The `error_handler` default is particularly valuable when you want a single catch-all recovery function for any node that fails without its own handler. The handler accepts the same `(state, error: NodeError)` signature described in [Error handling](#error-handling):

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langgraph.errors import NodeError
from langgraph.graph import StateGraph, START
from langgraph.types import RetryPolicy
from typing_extensions import TypedDict

class State(TypedDict):
    status: str

def always_failing(state: State) -> State:
    raise ValueError("something went wrong")

def default_handler(state: State, error: NodeError) -> State:
    return {"status": f"recovered from {error.node}: {error.error}"}

graph = (
    StateGraph(State)
    .set_node_defaults(
        retry_policy=RetryPolicy(max_attempts=2),
        error_handler=default_handler,
    )
    .add_node("always_failing", always_failing)
    .add_edge(START, "always_failing")
    .compile()
)
```

The node is retried twice, then `default_handler` runs. The default handler also accepts `RunnableConfig` as an optional third argument if you need access to config values such as `thread_id`:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_core.runnables import RunnableConfig

def default_handler(state: State, error: NodeError, config: RunnableConfig) -> State:
    thread_id = config["configurable"].get("thread_id")
    return {"status": f"handled on thread {thread_id}"}
```

### Applicability matrix

Not all defaults apply to all node types. Error-handler nodes (those registered via `add_node(error_handler=...)`) are excluded from certain defaults to prevent unsafe behavior:

| `set_node_defaults` parameter | Applies to regular nodes | Applies to error-handler nodes | Reason                                                      |
| ----------------------------- | ------------------------ | ------------------------------ | ----------------------------------------------------------- |
| `retry_policy`                | ✅                        | ✅                              | Handlers should be retried on transient failures            |
| `timeout`                     | ✅                        | ✅                              | Stuck handlers should be cancelled like stuck regular nodes |
| `error_handler`               | ✅                        | ❌                              | Handlers must never catch themselves                        |
| `cache_policy`                | ✅                        | ❌                              | Caching handler results is unsafe                           |

### Scope

Defaults set on a parent graph are **not** inherited by subgraphs. Each graph maintains its own defaults.

## Functional API

The same `timeout=` and `retry_policy=` parameters are available on `@task` and `@entrypoint` in the functional API:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langgraph.func import entrypoint, task
from langgraph.types import RetryPolicy, TimeoutPolicy

@task(
    timeout=TimeoutPolicy(idle_timeout=30),
    retry_policy=RetryPolicy(max_attempts=3),
)
async def call_api(url: str) -> str:
    response = await fetch(url)
    return response.text

@entrypoint(timeout=60)
async def my_workflow(inputs: dict) -> str:
    result = await call_api("https://api.example.com/data")
    return result
```

The behavior is identical to `add_node`: `NodeTimeoutError` is raised on timeout, buffered writes are cleared, and the retry policy decides whether to retry.

## Graceful shutdown

Cooperative shutdown lets you stop an in-flight graph run after the current superstep completes and save a resumable checkpoint. This is useful for handling SIGTERM signals or any external supervisor that needs to reclaim resources without losing work.

<Note>
  Requires `langgraph>=1.2`.
</Note>

Create a [`RunControl`](https://reference.langchain.com/python/langgraph/runtime/RunControl) and pass it as `control=` to `invoke` or `stream`. Call `request_drain()` from any thread to signal that the run should stop:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langgraph.runtime import RunControl
from langgraph.errors import GraphDrained

control = RunControl()

# In a signal handler or supervisor:

# control.request_drain("sigterm")

try:
    result = graph.invoke(inputs, config, control=control)
except GraphDrained as e:
    # The graph stopped early and saved a checkpoint.
    # Resume later with the same config.
    print(f"Drained: {e.reason}")
```

### Semantics

Drain is cooperative and operates between supersteps, never preempting work that is already running:

| Scenario                                           | Behavior                                                                                      |
| -------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| Node mid-execution                                 | Runs to completion. Drain takes effect on the next superstep.                                 |
| Node with a retry policy currently retrying        | Retry loop runs to exhaustion or success. Drain takes effect after.                           |
| Graph finishes naturally on the same tick as drain | Returns normally. Inspect `control.drain_requested` to distinguish from a normal run.         |
| More supersteps remain                             | Raises `GraphDrained(reason)`. Checkpoint is saved and resumable.                             |
| Subgraph requests drain                            | `GraphDrained` bubbles up through the parent and stops it at its own next superstep boundary. |

### Resume after drain

Resume a drained run with `invoke(None, config)` using the same `thread_id`:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
result = graph.invoke(None, config)
```

### Read drain state inside a node

Access drain state through the `runtime` parameter to adjust node behavior before the superstep boundary is reached:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langgraph.runtime import Runtime

async def my_node(state: State, runtime: Runtime) -> State:
    if runtime.drain_requested:
        # Skip expensive work and return a minimal result
        return {"status": "skipped", "reason": runtime.drain_reason}
    return {"status": await do_work()}
```

### SIGTERM hook pattern

The recommended pattern for handling process shutdown:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import signal
from langgraph.runtime import RunControl
from langgraph.errors import GraphDrained

control = RunControl()
signal.signal(signal.SIGTERM, lambda *_: control.request_drain("sigterm"))

try:
    result = graph.invoke(inputs, config, control=control)
except GraphDrained as e:
    log.info("graph drained: %s", e.reason)
    # Resume on next startup with the same config
```

<Note>
  `request_drain()` does not cancel running asyncio tasks or kill threads. For a hard upper bound, pair drain with a graceful timeout and task cancellation.
</Note>

## Limitations

* **Timeouts are async-only**: sync nodes with a `timeout` are rejected at compile time.
* **One handler per node**: each node can have at most one `error_handler`.
* **Handler failures bubble up**: if the error handler itself raises, that exception propagates as if the node had no handler.
* **`set_node_defaults` is not inherited by subgraphs**: each graph manages its own defaults independently.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langgraph/fault-tolerance.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Custom stream channels
Source: https://docs.langchain.com/oss/python/langgraph/frontend/custom-stream-channels

Stream custom server-side data to the frontend and read it with useExtension and useChannel

LangGraph agents stream more than messages and tool calls. A server-side
**stream transformer** can inspect or rewrite the protocol as it flows to the
client and publish its own structured data on a named **custom channel**. The
frontend reads that channel with two selectors: [`useExtension`](https://reference.langchain.com/javascript/langchain-react/useExtension) for the latest
payload, and [`useChannel`](https://reference.langchain.com/javascript/langchain-react/useChannel) as a raw-events escape hatch.

The example below is a customer-support agent whose transformer redacts PII
(emails, phone numbers, SSNs, card numbers, IPs) from every event before it
reaches the browser, and publishes running redaction counts on a
`redaction-stats` channel. The side panel renders those counts live.

<PatternEmbed />

## How custom channels work

A custom channel has two ends. On the server, a [`StreamTransformer`](https://reference.langchain.com/python/langgraph/stream/_types/StreamTransformer) opens a
named [`StreamChannel`](https://reference.langchain.com/python/langgraph/stream/stream_channel/StreamChannel) and pushes payloads onto it. On the client, a selector
subscribes to the matching `custom:<name>` channel and exposes the payloads as
reactive state.

The transformer's `process` method runs for every protocol event. It can mutate
the event in place (here, scrubbing PII from `messages`, `tools`, and `values`
data) and push side-channel updates whenever it has something to report.

The client-side selectors (`useExtension`, `useChannel`) ship with the v1
frontend SDK packages (`@langchain/react`, `@langchain/vue`,
`@langchain/svelte`, `@langchain/angular`).

<Note>
  Stream transformers and `StreamChannel` require `langgraph>=1.2`.
</Note>

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import time

from langgraph.stream import ProtocolEvent, StreamChannel, StreamTransformer

class RedactionStatsTransformer(StreamTransformer):
    def __init__(self, scope: tuple[str, ...] = ()) -> None:
        super().__init__(scope)
        # Open a channel named "redaction-stats".
        self.redaction_stats = StreamChannel("redaction-stats")
        self.counts = empty_counts()

    def init(self) -> dict[str, StreamChannel]:
        return {"redactionStats": self.redaction_stats}

    def process(self, event: ProtocolEvent) -> bool:
        # Redact event["params"]["data"] in place and tally what was found.
        delta = redact_in_place(event, self.counts)
        if delta:
            # Publish a payload on the channel.
            self.redaction_stats.push(
                {
                    "kind": "update",
                    "at": int(time.time() * 1000),
                    "delta": delta,
                    "counts": dict(self.counts),
                    "total": sum(self.counts.values()),
                }
            )
        return True  # Keep the (now-redacted) event in the stream.

def create_redaction_stats_transformer() -> RedactionStatsTransformer:
    return RedactionStatsTransformer()
```

Attach the transformer when you build the agent:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain.agents import create_agent

agent = create_agent(
    model="anthropic:claude-haiku-4-5",
    tools=[...],
    transformers=[create_redaction_stats_transformer],
)
```

The payload type is whatever the transformer pushes. The client examples below
read this shape:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
type PiiType = "email" | "phone" | "ssn" | "credit_card" | "ip_address";

type RedactionStatsEvent = {
  kind: "update";
  at: number;
  delta: Partial<Record<PiiType, number>>;
  counts: Record<PiiType, number>;
  total: number;
};
```

## Setting up `useStream`

Wire up [`useStream`](https://reference.langchain.com/javascript/langchain-react/index/useStream) as usual. The custom-channel selectors take the same
`stream` handle returned here.

<Info>
  The code examples use `useStream<typeof myAgent>` for type-safe stream state. See Type inference for [Python](/oss/python/langchain/frontend/overview#type-inference) or [JavaScript](/oss/javascript/langchain/frontend/overview#type-inference) backends.
</Info>

<CodeGroup>
  ```tsx React theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { useStream } from "@langchain/react";

  const AGENT_URL = "http://localhost:2024";

  export function RedactionChat() {
    const stream = useStream<typeof myAgent>({
      apiUrl: AGENT_URL,
      assistantId: "custom_stream_channel",
    });

    return <RedactionStatsPanel stream={stream} />;
  }
  ```

  ```vue Vue theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  <script setup lang="ts">
  import { useStream } from "@langchain/vue";

  const AGENT_URL = "http://localhost:2024";

  const stream = useStream<typeof myAgent>({
    apiUrl: AGENT_URL,
    assistantId: "custom_stream_channel",
  });
  </script>

  <template>
    <RedactionStatsPanel :stream="stream" />
  </template>
  ```

  ```svelte Svelte theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  <script lang="ts">
    import { useStream } from "@langchain/svelte";

    const AGENT_URL = "http://localhost:2024";

    const stream = useStream<typeof myAgent>({
      apiUrl: AGENT_URL,
      assistantId: "custom_stream_channel",
    });
  </script>

  <RedactionStatsPanel {stream} />
  ```

  ```ts Angular theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { Component } from "@angular/core";
  import { injectStream } from "@langchain/angular";

  const AGENT_URL = "http://localhost:2024";

  @Component({
    selector: "app-redaction-chat",
    template: `<app-redaction-stats-panel [stream]="stream" />`,
  })
  export class RedactionChatComponent {
    stream = injectStream<typeof myAgent>({
      apiUrl: AGENT_URL,
      assistantId: "custom_stream_channel",
    });
  }
  ```
</CodeGroup>

## Read the latest payload with `useExtension`

`useExtension` subscribes to a `custom:<name>` channel and returns the most
recent payload the transformer pushed, already unwrapped and typed. It is the
ergonomic choice when the UI only needs the current value, such as a live
counter, progress percentage, or status badge.

Pass the bare channel name (`"redaction-stats"`), not the `custom:` prefix:

<CodeGroup>
  ```tsx React theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { useExtension } from "@langchain/react";

  const latest = useExtension<RedactionStatsEvent>(stream, "redaction-stats");
  // latest?.total, latest?.counts.email, latest?.delta
  ```

  ```vue Vue theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { useExtension } from "@langchain/vue";

  const latest = useExtension<RedactionStatsEvent>(stream, "redaction-stats");
  // latest.value?.total
  ```

  ```svelte Svelte theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { useExtension } from "@langchain/svelte";

  const latest = useExtension<RedactionStatsEvent>(stream, "redaction-stats");
  // latest?.total
  ```

  ```ts Angular theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { injectExtension } from "@langchain/angular";

  const latest = injectExtension<RedactionStatsEvent>(stream, "redaction-stats");
  // latest()?.total
  ```
</CodeGroup>

The return value follows each framework's reactivity model: a plain value in
React and Svelte, a `Ref` in Vue (`latest.value`), and a signal in Angular
(`latest()`). The value is `undefined` until the first payload arrives.

An optional third `target` argument scopes the subscription to a namespace, the
same way `useMessages(stream, node)` scopes messages to a discovered graph node.
See [Graph execution](/oss/python/langgraph/frontend/graph-execution) for namespace
targeting.

## Buffer raw events with `useChannel`

`useChannel` is the raw-events escape hatch. It subscribes to one or more
channels and returns a bounded buffer of the underlying protocol events rather
than a single unwrapped value. Reach for it when you need history instead of the
latest value, such as an event log or audit trail, or when you need a channel
that no higher-level selector covers.

Pass the full channel id (`"custom:redaction-stats"`):

<CodeGroup>
  ```tsx React theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { useChannel } from "@langchain/react";

  const rawEvents = useChannel(stream, ["custom:redaction-stats"]);
  ```

  ```vue Vue theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { useChannel } from "@langchain/vue";

  const rawEvents = useChannel(stream, ["custom:redaction-stats"]);
  // rawEvents.value
  ```

  ```svelte Svelte theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { useChannel } from "@langchain/svelte";

  const rawEvents = useChannel(stream, ["custom:redaction-stats"]);
  ```

  ```ts Angular theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { injectChannel } from "@langchain/angular";

  const rawEvents = injectChannel(stream, ["custom:redaction-stats"]);
  // rawEvents()
  ```
</CodeGroup>

Each entry is a raw protocol event, so the payload sits under
`event.params.data`. Unwrap it yourself:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
function parseRedactionStatsEvents(rawEvents: Event[]): RedactionStatsEvent[] {
  const out: RedactionStatsEvent[] = [];
  for (const event of rawEvents) {
    const data = event.params?.data;
    const payload = data?.payload ?? data;
    if (payload?.kind === "update") out.push(payload);
  }
  return out;
}
```

Control the buffer with the options argument:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const rawEvents = useChannel(
  stream,
  ["custom:redaction-stats"],
  undefined, // target namespace
  { bufferSize: 200, replay: true },
);
```

| Option       | Default     | Effect                                                                                           |
| ------------ | ----------- | ------------------------------------------------------------------------------------------------ |
| `bufferSize` | `"default"` | Maximum number of buffered events. Older events drop once the cap is reached.                    |
| `replay`     | `true`      | Replay events already seen on the channel when the selector mounts, instead of only live events. |

<Note>
  Prefer the higher-level selectors (`useExtension`, `useMessages`,
  `useToolCalls`, `useValues`) for common cases. They return typed, unwrapped
  values and track only what you render. Use `useChannel` when you specifically
  need the raw event stream.
</Note>

## Choosing between `useExtension` and `useChannel`

Both read the same custom channel but differ in what they return:

|                  | `useExtension`                     | `useChannel`                                             |
| ---------------- | ---------------------------------- | -------------------------------------------------------- |
| **Returns**      | Latest payload (`T \| undefined`)  | Bounded buffer of raw events (`Event[]`)                 |
| **Shape**        | Unwrapped, typed payload           | Raw protocol events; unwrap `event.params.data` yourself |
| **Subscribe by** | Channel name (`"redaction-stats"`) | Full channel id (`["custom:redaction-stats"]`)           |
| **Use when**     | You need the current value         | You need history, a log, or multiple channels            |
| **Options**      | —                                  | `bufferSize`, `replay`                                   |

A common pattern is to use both on the same channel: `useExtension` drives a
live summary (current totals), while `useChannel` backs a scrolling event log of
every update across the thread.

## Use cases

Custom channels fit any server-side signal that does not map cleanly to
messages, tool calls, or graph state:

* **Compliance and redaction stats**: counts of scrubbed PII, blocked content,
  or policy hits, as in the example above.
* **Progress reporting**: percentage complete or step labels emitted by a
  long-running tool.
* **Live metrics**: token usage, latency, or cost accumulating during a run.
* **Sources and citations**: retrieved documents pushed to a side panel as the
  agent grounds its answer.
* **Domain events**: any structured update your backend wants to surface
  without changing the message transcript.

## Related

* [Overview](/oss/python/langgraph/frontend/overview) — the LangGraph frontend stream
  API and architecture.
* [Graph execution](/oss/python/langgraph/frontend/graph-execution) — namespace-scoped
  selectors for multi-node pipelines.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langgraph/frontend/custom-stream-channels.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
