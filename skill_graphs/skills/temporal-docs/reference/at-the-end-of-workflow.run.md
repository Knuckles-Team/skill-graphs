# at the end of @workflow.run
self.status.publish(StatusEvent(state="completed", progress=100))
await workflow.sleep(timedelta(seconds=30))
return result
```

The sleep needs to be long enough to cover the time between when the terminator becomes visible and when the subscriber's next poll reaches the server, including any client-side cooldown and network round-trips. A few hundred milliseconds is tight under realistic conditions; thirty seconds is a generous default. The cost is small: the Workflow Run stays open for that duration but does no other work.

**Acknowledgment handshake.** The subscriber sends a Signal once it has the terminator; the Workflow waits up to a timeout, returning as soon as the ack arrives:

```python
@workflow.signal
async def subscriber_acknowledged_terminator(self) -> None:
    self.subscriber_done = True

@workflow.run
async def run(self, input: ChatInput) -> str:
    ...
    try:
        await workflow.wait_condition(
            lambda: self.subscriber_done,
            timeout=timedelta(seconds=30),
        )
    except TimeoutError:
        pass  # No subscriber attached; the run still completes cleanly.
    return result
```

The timeout is still required because the subscriber may not be attached, or may have gone away. With the ack on top, the typical case (subscriber online) exits as soon as the subscriber confirms receipt, regardless of how long the fallback timeout is. The full pattern is wired into the [Stream LLM output](#stream-llm-output) example below.

**Inspecting terminal status.** `subscribe()` exits cleanly when the Workflow reaches `COMPLETED`, `FAILED`, `CANCELED`, `TERMINATED`, or `TIMED_OUT`, but does not distinguish among them. If your application needs to know which (to display success or failure to the user, log the outcome, or decide whether to retry), call `await temporal_client.get_workflow_handle(workflow_id).describe()` after the loop returns to inspect the Workflow's status.

## Continue-As-New {/* #continue-as-new */}

If your Workflow runs for minutes and finishes (a single chat completion, an order pipeline, a one-shot agent), you can skip this section. Continue-As-New becomes relevant for streams that run for hours or accumulate thousands of events, where you need to roll the run over to keep history bounded.

Subscribers automatically follow Continue-As-New chains, so a long-running Workflow can roll over without disrupting active consumers. Workflow Ids are stable across Continue-As-New, so the iterator simply fetches a fresh handle for the same Workflow Id and continues polling from the carried offset. CAN-following requires the client retained from `WorkflowStreamClient.create()` or `from_within_activity()`; clients constructed directly with a single handle cannot re-target the new run.

To roll a long-running streaming Workflow over without subscribers seeing a gap, carry both your application state and the stream state across the boundary. Add a `WorkflowStreamState | None` field to your Workflow input, pass it to the constructor, and call `WorkflowStream.continue_as_new(build_args)` to invoke the rollover. The helper drains waiting subscribers, waits for in-flight handlers to finish, then calls `workflow.continue_as_new` with the args produced by `build_args(post_drain_state)`:

```python
from dataclasses import dataclass, field

from temporalio import workflow
from temporalio.contrib.workflow_streams import WorkflowStream, WorkflowStreamState

@dataclass
class AppState:
    items_processed: int = 0

@dataclass
class WorkflowInput:
    app_state: AppState = field(default_factory=AppState)
    stream_state: WorkflowStreamState | None = None

@workflow.defn
class LongRunningWorkflow:
    @workflow.init
    def __init__(self, input: WorkflowInput) -> None:
        self.app_state = input.app_state
        self.stream = WorkflowStream(prior_state=input.stream_state)

    @workflow.run
    async def run(self, input: WorkflowInput) -> None:
        while True:
            await do_one_iteration(self)
            if workflow.info().is_continue_as_new_suggested():
                await self.stream.continue_as_new(
                    lambda stream_state: [
                        WorkflowInput(
                            app_state=self.app_state,
                            stream_state=stream_state,
                        )
                    ]
                )
```

The `| None` on the `stream_state` field type is required: `prior_state` is `None` on a fresh start and a `WorkflowStreamState` instance after a rollover. Always use the concrete type, not `Any`. With `Any`, the data converter rebuilds the field as a plain `dict` and `WorkflowStream(prior_state=...)` raises `AttributeError` accessing `.log` / `.base_offset` / `.publishers` on the dict.

To pass other Continue-As-New parameters such as `task_queue`, `retry_policy`, `run_timeout`, use the explicit recipe instead:

```python
self.stream.detach_pollers()
await workflow.wait_condition(workflow.all_handlers_finished)
workflow.continue_as_new(
    args=[WorkflowInput(app_state=self.app_state, stream_state=self.stream.get_state())],
    task_queue="other-tq",
)
```

The carried `WorkflowStreamState` includes the entire in-memory log of the previous run, so streams that carry large items can hit Temporal's per-payload size limit at the rollover. (Individual publish Signals and subscribe Update responses can also exceed the limit, but the carried state is the most acute case because it accumulates the full log window.) Offload the bytes via [External Storage](/external-storage) so each item is a small reference rather than the full payload, and combine that with `truncate()` to keep the carried log itself small.

## Tuning

The most important question when tuning is: how often do you want to update your UI? That answer drives the trade-off between user-perceived latency and the number of history events your Workflow accumulates. The library defaults assume a slow-moving UI; LLM token streaming and other interactive cases need lower latency, which means tuning.

The trade-off is direct. Each batched publish is one Signal, and each subscriber poll is one Update. Each Signal and each Update accumulates against the Workflow's history. A more responsive UI means more messages and more history per second; messages drive workload (and on metered deployments, billing), while history accumulates against Temporal's per-run limits. For long-running streams, plan a [Continue-As-New](#continue-as-new) policy from the start.

### Settings that matter most

- **`batch_interval`** (default 2 seconds). Maximum time between automatic flushes from the client. Lower it to make the stream feel live; raise it to amortize Signal cost. For an LLM token stream feeding a chat UI, 200 ms is a good starting point: the user perceives it as live, and a 30-second response generates roughly 150 publish Signals rather than several hundred. Below 100 ms the per-Signal RPC overhead starts to dominate.

For per-publish overrides where one specific event needs lower latency than the batch interval (for example, the first delta of a response so the user sees something fast, or punctuated events like `RETRY` and `STATUS_CHANGE`), pass `force_flush=True` on that publish. Don't make this the default mode: per-token `force_flush=True` on a 500-token completion produces 500 publish Signals, which is meaningful but tractable; per-character `force_flush=True` is not.

### Other settings

You usually do not need to touch these, but they are available when the basic settings are not enough:

- **`max_batch_size`** (default unbounded). Caps the number of items per batch. With the default, only `batch_interval` bounds batch size, so a hot publisher can accumulate enough items between intervals that the resulting Signal exceeds Temporal's per-message gRPC payload limit. Set `max_batch_size` to bound by item count, or call `force_flush=True` after each logical chunk to bound by application boundaries (for example, publish per generated sentence in a TTS Activity so each Signal carries one audio chunk). For large items, offload via [External Storage](/external-storage) so each item is a small reference.
- **`poll_cooldown`** (subscriber-side, default 100 ms). The subscriber sleeps for this interval between polls. The cooldown is skipped only when a poll response was capped at the ~1 MB gRPC limit and more items remain (a `more_ready` flag in the response), so the next poll can drain the rest immediately. That path is an optimization for bursty producers; in the steady state, every poll waits the cooldown before the next. Hold a single iterator and consume from it rather than opening and closing subscriptions in a loop.
- **`max_retry_duration`** (default 10 minutes). How long the client retries a failed publish batch before giving up and raising `TimeoutError`. Tune higher if your application can tolerate longer outages while a publisher retries through transient failures; lower if you want failures to surface quickly.
- **`publisher_ttl`** (default 15 minutes). How long the Workflow retains per-publisher deduplicate state. At each Continue-As-New, entries older than this are dropped. Tune higher if your publishers can be silent for extended windows.

The last two settings are related. Keep `max_retry_duration < publisher_ttl` so a long-running retry cannot outlast its dedup record and produce a duplicate when it finally succeeds. If you tune one, tune the other. See [Delivery semantics](#delivery-semantics) for the full failure model.

## Delivery semantics

**Exactly-once at the execution layer.** Each `(publisher_id, sequence)` batch lands in the Workflow's event log at most once, even if the publisher's underlying Signal is retried by the SDK or the network. Once an event is in the log, every subscriber that polls past its offset will see it, and deduplicate state is carried across Continue-As-New so a retried publish that arrives after a rollover still lands at most once.

**Ordering.** The log imposes a single total order on all events, fixed once written: an event at offset N stays at offset N on every read. Within one publisher (one `WorkflowStreamClient` instance, or the Workflow itself), events appear in publish order. Across concurrent publishers, the interleaving is whatever the Workflow saw when serializing inbound Signals; the order is stable once recorded but not under application control. If event A must precede event B, publish them from the same publisher.

**Activity retries surface to subscribers.** When an Activity that publishes events fails partway through and Temporal retries it, *both* attempts' events appear in the stream. Concretely: an Activity that publishes three `TEXT_DELTA` events and then errors, then retries and publishes its full output, will deliver three partial events followed by the complete sequence. The Workflow itself sees only the successful attempt's return value (that's what durable execution hides), but a UI subscribed to the stream will see the partial output unless it dedupes. Consumers must reset or annotate on retry events; the library does not do this automatically.

The conventional pattern is for an Activity that detects it's on a retry attempt to publish a `RETRY` event with `force_flush=True`, and for the consumer to clear or annotate prior-attempt output when it sees one. Treat the stream as an append-only log of attempts and let an idempotent consumer reducer reconcile them: overwrite on terminal events like `STATUS_CHANGE` or `TEXT_COMPLETE`, or reset an accumulator on a sentinel like `AGENT_START` before deltas resume. Because the Workflow processes only Activity return values rather than reading the stream itself, its own state stays independent of these retried events.

This is the price of streaming events as they happen rather than waiting for the Workflow's durable view to settle. If the library waited for a successful Activity return before surfacing anything, there would be nothing to stream.

**Other failure modes.** Events still in a publisher's in-memory client buffer are lost if the process crashes before they ship. Subscribers that handle an item and crash before persisting their next offset will reprocess that item on resume. Build consumer state with both in mind.

Two limits on the deduplication window are worth understanding:

- **`publisher_ttl`** (default 15 minutes). Retention for the per-publisher deduplicate state. At each Continue-As-New, deduplicate entries whose `last_seen` is older than this are dropped. `last_seen` is updated on each *successful* publish (not on each retry attempt), so a publisher that retries through a long partition without success can still age out. A publisher that returns after a longer pause may produce a duplicate. Tune upward via `WorkflowStream.continue_as_new(publisher_ttl=...)` if your publishers can be silent for extended windows.
- **`max_retry_duration`** (default 10 minutes). A `WorkflowStreamClient` retries a failed batch for up to this long. If the duration elapses with the batch still pending (for example, during a sustained network partition), the client gives up, the pending batch is dropped, and a `TimeoutError` is raised.

    On timeout, the dropped batch is at-most-once: it may or may not have reached the Workflow. Subsequent publishes resume cleanly with the next sequence. One operational caveat: the `TimeoutError` raises from inside the background flusher task and terminates it. Until you call `await client.flush()` or exit the `async with` block, subsequent publishes accumulate in the buffer with no flusher to ship them.

**The two limits must satisfy `max_retry_duration < publisher_ttl`.** If a publisher's retry window exceeds the dedup retention, the dedup state for that publisher can age out (at the next Continue-As-New) before the retry lands. A retry that arrives after its dedup record has been pruned is treated as a fresh publish, and if the original delivery had also succeeded, the same logical batch lands twice. The defaults (10 minutes < 15 minutes) satisfy this; if you tune one, tune the other to preserve the relationship.

## Architecture

The user-facing API hides three pieces of machinery worth understanding when you tune throughput, debug delivery, or reason about history size.

**Append-only log inside the Workflow.** `WorkflowStream` keeps an in-memory list of `(topic, data)` entries inside the Workflow's state, each with a monotonically increasing global offset. Subscribers maintain their own cursor and on each long-poll receive the next range past it. Because the log lives in Workflow state, it is replay-safe and is carried across Continue-As-New via `WorkflowStreamState`.

Two mechanisms bound log growth, and they do different jobs:

- **`truncate(up_to_offset)`** drops entries from the in-memory log (and therefore from the carried Continue-As-New payload). It does not remove publish Signals already recorded in history.
- **Continue-As-New** starts a fresh history. This is the only way to shrink history; truncate alone cannot.

A subscriber whose offset falls below the new base after a `truncate()` is silently advanced. Internally, the poll raises `ApplicationError("TruncatedOffset")`; the Python client catches it and resets to offset 0, which the Workflow reads as "from the current base." The iterator does not raise, but the subscriber may re-receive items already in the log past the new base. Applications that depend on seeing every event exactly once must keep subscribers ahead of truncation or implement their own gap and re-delivery handling using `item.offset`.

**Wire-level handlers.** The three handlers registered when you construct a `WorkflowStream` are `__temporal_workflow_stream_publish` (the Signal that receives batched publishes), `__temporal_workflow_stream_poll` (the long-poll Update that subscribers use), and `__temporal_workflow_stream_offset` (the Query that reports the current head offset). Poll responses are capped at roughly 1 MB by accumulating items until the next would exceed the budget, so high-throughput producers see a steady stream of small batches. A single item that exceeds 1 MB on its own is admitted unconditionally; offload large items via [External Storage](/external-storage) so each item is a small reference.

**Batching and deduplicating.** Every batch carries a unique identifier (the client's id paired with a monotonic batch sequence number), so a Signal retried by the SDK or the network deduplicates to a single landing in the Workflow's event log. Deduplicate state is part of the Workflow's carried state, so the guarantee survives Continue-As-New (subject to `publisher_ttl`).

This dedup applies at the Signal layer, not the Activity layer. An *Activity retry* is a different concept from a *publish retry*: when Temporal retries the Activity, the retried execution constructs a new `WorkflowStreamClient` with its own client id, so from the stream's perspective every attempt is a fresh publisher whose batches will not deduplicate against the prior attempt's. That is why retried-attempt events appear in the stream alongside the successful attempt's output.

### Gotchas

A few details worth knowing about, mostly relevant if you're writing custom message handlers or pushing the library to its limits.

- **`WorkflowStreamClient` is asyncio-only.** The client buffer is mutated on the publish path and read from the flusher inside a single event loop. Don't call `publish()` from a worker thread.
- **Custom handlers reading stream state on the first activation.** `WorkflowStream` registers its publish-Signal handler dynamically from `__init__`, so on the very first activation a publish Signal can be queued before class-level `@workflow.signal` or `@workflow.update` handlers have run. A handler that observes state set by stream initialization in that same activation can see pre-publish state. The fix is to make the handler `async def` and `await` once before reading state. `asyncio.sleep(0)` is a no-op yield that suffices and adds no history events. (Don't substitute `workflow.sleep(0)`, which records a timer event.) Once the first activation completes, the handler is permanent and the race does not recur.
- **Type bindings aren't shared across publishers.** Each `WorkflowStream` and each `WorkflowStreamClient` records topic types only for its own instance. If two publishers bind the same topic name to different types, the mismatch is not caught at publish, and the subscriber gets a decode error when it processes events from the mismatched publisher.

## Application: Stream LLM output {/* #stream-llm-output */}

The headline use case fits the publish/subscribe shapes documented above. An Activity calls the model and publishes deltas as they arrive; the Workflow kicks off the Activity and waits for the consumer to acknowledge end-of-stream; the consumer subscribes, accumulates the deltas, and clears its accumulated state on `RETRY` before continuing. The shape works for a terminal client, a desktop UI, or a Server-Sent Events (SSE) endpoint forwarding to a browser; whatever holds the displayed state calls `render()` to display it.

If your Activity can retry, the consumer side has to account for it: a retried attempt is a fresh publisher, so its output appears in the stream alongside the previous attempt's. In the LLM streaming pattern below, that means the failed attempt's partial deltas and the retried attempt's full output both reach a subscribed UI unless the UI resets on a `RETRY` event. The example wires up that pattern; see [Delivery semantics](#delivery-semantics) for the precise guarantees.

```python
