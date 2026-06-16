# consumer.py: accumulates the model's output and resets on retry
async def stream_chat(chat_id: str) -> str:
    # Subscribe-only; no `async with` needed because the flusher only runs for publishers.
    stream = WorkflowStreamClient.create(temporal_client, workflow_id=chat_id)
    converter = temporal_client.data_converter.payload_converter
    output: list[str] = []

    def render() -> None:
        ...  # display the accumulated output (terminal redraw, UI update, etc.)

    async for item in stream.subscribe(
        ["delta", "retry", "close"], result_type=RawValue
    ):
        if item.topic == "retry":
            # Earlier attempt's deltas are stale; drop what we've shown.
            output.clear()
            render()
        elif item.topic == "delta":
            delta = converter.from_payload(item.data.payload, TextDelta)
            output.append(delta.text)
            render()
        elif item.topic == "close":
            # Acknowledge so the Workflow can return without a sleep.
            await temporal_client.get_workflow_handle(chat_id).signal(
                ChatWorkflow.subscriber_acknowledged_terminator
            )
            break

    return "".join(output)
```

A few choices in this shape are deliberate:

- The Activity is the publisher because it owns the non-deterministic LLM call. The Workflow processes only the Activity's return value, never reading its own stream — see [Publish from a client](#publish-from-a-client) for why.
- The Activity publishes a `RETRY` event when `activity.info().attempt > 1`. This lets the UI respond appropriately to the failure, typically by clearing accumulated deltas before the next attempt's deltas arrive (see [Delivery semantics](#delivery-semantics)).
- Termination uses an *ack handshake*: the consumer signals the Workflow once it has received the `close` event, so the Workflow can return as soon as the subscriber confirms. The `wait_condition` timeout is the fallback when no subscriber is attached (see [Closing the stream](#closing-the-stream) for the simpler fixed-sleep alternative).
- `force_flush=True` is used only on the first delta and on the `RETRY` sentinel, where latency matters. Subsequent deltas batch at the 200 ms `batch_interval`; per-delta `force_flush=True` would generate one Signal per token (see [Tuning](#tuning) for the trade-off).

## See also

- [Workflow Streams samples (samples-python)](https://github.com/temporalio/samples-python/tree/main/workflow_streams): four runnable scenarios covering basic publish/subscribe, reconnecting subscribers, external publishers, and bounded logs.
- [`temporalio.contrib.workflow_streams` API reference](https://python.temporal.io/temporalio.contrib.workflow_streams.html).
- [Workflow message passing](/develop/python/workflows/message-passing): Signals, Updates, and Queries that Workflow Streams is built on.
- [Payload conversion](/develop/python/data-handling/data-conversion): converters and codecs.

---

## Asynchronous Activity completion - Ruby SDK

## How to asynchronously complete an Activity {/* #asynchronous-activity-completion */}

This page describes how to asynchronously complete an Activity.

[Asynchronous Activity Completion](/activity-execution#asynchronous-activity-completion) enables the Activity Function to return without the Activity Execution completing.

There are three steps to follow:

1. The Activity provides the external system with identifying information needed to complete the Activity Execution.
   Identifying information can be a [Task Token](/activity-execution#task-token), or a combination of Namespace, Workflow Id, and Activity Id.
2. The Activity Function completes in a way that identifies it as waiting to be completed by an external system.
3. The Temporal Client is used to Heartbeat and complete the Activity.

To mark an Activity as completing asynchronously, do the following inside the Activity.

```ruby
