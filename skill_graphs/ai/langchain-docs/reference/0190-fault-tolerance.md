# Fault tolerance
Source: https://docs.langchain.com/oss/javascript/langgraph/fault-tolerance

Configure per-node timeouts, retries, and error handlers in LangGraph.

When a node fails—from a slow external API, a transient network error, or an unhandled exception—LangGraph gives you three composable mechanisms to respond:

* [**Retries**](#retries) — automatically re-run failed attempts based on exception type and backoff settings
* [**Timeouts**](#timeouts) — cap how long a single attempt may run
* [**Error handling**](#error-handling) — run a recovery function after all retries are exhausted

Use [**`setNodeDefaults`**](#graph-defaults) to configure these mechanisms once for all nodes instead of repeating them on every `addNode` call.

These compose in a fixed order: when a node attempt raises any exception (including [`NodeTimeoutError`](https://reference.langchain.com/javascript/langchain-langgraph/index/NodeTimeoutError) from a timeout), the retry policy decides whether to retry. Only after retries are exhausted does the error handler run.

For stopping a run cleanly at a superstep boundary and resuming later, see [Graceful shutdown](#graceful-shutdown).

<Note>
  Per-node timeouts and node-level error handlers require `@langchain/langgraph>=1.4.0`.
</Note>

```mermaid theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
%%{init:{'theme':'base','themeVariables':{'lineColor':'#40668D','primaryColor':'#E5F4FF','primaryTextColor':'#030710','primaryBorderColor':'#006DDD'}}}%%
flowchart LR
    start([Attempt starts]) --> exec[Run node]
    exec -->|"success"| done([Continue graph])
    exec -->|"any exception<br/>including NodeTimeoutError"| retry{retry_policy<br/>matches?}
    retry -->|"yes, attempts left"| exec
    retry -->|"exhausted or absent"| handler{error_handler?}
    handler -->|"yes"| run_handler["Invoke handler<br/>with NodeError"]
    run_handler --> route([Update state +<br/>Command goto])
    handler -->|"no"| bubble([Exception<br/>bubbles up])

    classDef process fill:#E5F4FF,stroke:#006DDD,stroke-width:2px,color:#030710
    classDef decision fill:#FDF3FF,stroke:#7E65AE,stroke-width:2px,color:#504B5F
    classDef alert fill:#F8E8E6,stroke:#B27D75,stroke-width:2px,color:#634643
    classDef output fill:#EBD0F0,stroke:#885270,stroke-width:2px,color:#441E33

    class exec,run_handler process
    class retry,handler decision
    class bubble alert
    class done,route,start output
```

## Retries

A retry policy automatically re-runs a failed node attempt based on exception type and backoff settings.

Pass `retryPolicy` to [`addNode`](https://reference.langchain.com/javascript/classes/_langchain_langgraph.index.StateGraph.html#addNode):

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { StateGraph } from "@langchain/langgraph";

const graph = new StateGraph(State)
  .addNode("callApi", callApi, { retryPolicy: { maxAttempts: 3 } })
  .compile();
```

### Default behavior

Retries are opt-in. A node retries only when it has a `retryPolicy` configured, either directly or through graph defaults with [`setNodeDefaults`](#graph-defaults). An empty policy (`{}`) is enough. Without a policy, the first failure ends the attempt and LangGraph does not call `retryOn`.

If the policy omits `retryOn`, LangGraph uses a built-in handler that retries thrown errors except:

* Abort and cancellation errors: `error.name === "AbortError"`, or `error.message` starts with `"Cancel"` or `"AbortError"`
* `GraphValueError`, matched by `error.name`
* Aborted connections: `error.code === "ECONNABORTED"`
* HTTP client errors with status 400, 401, 402, 403, 404, 405, 406, 407, or 409, read from `error.response?.status` or `error.status` for clients such as `fetch`, Axios, and similar clients
* OpenAI-style quota errors: `error.error?.code === "insufficient_quota"`

Other HTTP statuses, including 408 and 5xx responses, are retryable unless you override `retryOn`. [`NodeTimeoutError`](https://reference.langchain.com/javascript/langchain-langgraph/index/NodeTimeoutError) is not on this blocklist, so it is retryable when a retry policy is configured.

Some failures bypass `retryOn`. Graph control-flow errors, such as `GraphInterrupt` and `Command` routing, bubble up without retrying. An aborted run signal also stops the retry loop, even if `retryOn` would return `true`.

### Parameters

| Parameter         | Type                          | Default                               | Description                                                                                     |
| ----------------- | ----------------------------- | ------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `maxAttempts`     | `number`                      | `3`                                   | Maximum number of attempts, including the first.                                                |
| `initialInterval` | `number`                      | `500`                                 | Milliseconds before the first retry.                                                            |
| `backoffFactor`   | `number`                      | `2.0`                                 | Multiplier applied to the interval after each retry.                                            |
| `maxInterval`     | `number`                      | `128000`                              | Maximum milliseconds between retries.                                                           |
| `jitter`          | `boolean`                     | `true`                                | Add random jitter to the interval.                                                              |
| `retryOn`         | `(error: unknown) => boolean` | built-in handler (when policy is set) | Callable returning `true` for retryable exceptions. Only used when `retryPolicy` is configured. |
| `logWarning`      | `boolean`                     | `true`                                | Whether to log a warning when a retry is attempted.                                             |

### Custom retry logic

Pass a callable to `retryOn`. Unlike Python, there is no exported `defaultRetryOn` helper—implement your own predicate:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { StateGraph } from "@langchain/langgraph";

class MyCustomError extends Error {}

const graph = new StateGraph(State)
  .addNode("callApi", callApi, {
    retryPolicy: {
      maxAttempts: 3,
      retryOn: (error: unknown) => {
        if (error instanceof MyCustomError) return false;
        // Retry on other errors
        return true;
      },
    },
  })
  .compile();
```

### Inspect retry state

Use execution info inside a node to inspect the current attempt number. This is useful for switching to a fallback when the primary call keeps failing:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { StateGraph, StateSchema, START, END, type Runtime } from "@langchain/langgraph";
import * as z from "zod";

const State = new StateSchema({
  result: z.string(),
});

const myNode = async (state: typeof State.State, runtime: Runtime<typeof State>) => {
  if ((runtime.executionInfo?.nodeAttempt ?? 1) > 1) {  // [!code highlight]
    return { result: await callFallbackApi() };
  }
  return { result: await callPrimaryApi() };
};

const graph = new StateGraph(State)
  .addNode("myNode", myNode, { retryPolicy: { maxAttempts: 3 } })
  .addEdge(START, "myNode")
  .addEdge("myNode", END)
  .compile();
```

`executionInfo` exposes the following fields:

| Attribute              | Type                  | Description                                                                            |
| ---------------------- | --------------------- | -------------------------------------------------------------------------------------- |
| `nodeAttempt`          | `number`              | Current attempt number (1-indexed). `1` on the first try, `2` on the first retry, etc. |
| `nodeFirstAttemptTime` | `number \| undefined` | Unix timestamp (ms) of when the first attempt started. Constant across retries.        |
| `threadId`             | `string \| undefined` | Thread ID for the current execution. `undefined` without a checkpointer.               |
| `runId`                | `string \| undefined` | Run ID for the current execution. `undefined` when not provided in config.             |
| `checkpointId`         | `string`              | Checkpoint ID for the current execution.                                               |
| `checkpointNs`         | `string`              | Checkpoint namespace for the current execution.                                        |
| `taskId`               | `string`              | Task ID for the current execution.                                                     |

`executionInfo` is available even without a retry policy—`nodeAttempt` defaults to `1`.

## Timeouts

<Note>
  Requires `@langchain/langgraph>=1.4.0`.
</Note>

The `timeout` parameter on [`addNode`](https://reference.langchain.com/javascript/classes/_langchain_langgraph.index.StateGraph.html#addNode) caps how long a single node attempt may run. Pass a number (milliseconds) or a [`TimeoutPolicy`](https://reference.langchain.com/javascript/langchain-langgraph/index/TimeoutPolicy) for separate run and idle limits:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { StateGraph, type TimeoutPolicy } from "@langchain/langgraph";

// Simple wall-clock cap (60 seconds)
new StateGraph(State).addNode("callModel", callModel, { timeout: 60_000 });

// Separate run and idle limits
new StateGraph(State).addNode("callModel", callModel, {
  timeout: { runTimeout: 120_000, idleTimeout: 30_000 },
});
```

### Run timeout

`runTimeout` is a hard wall-clock cap on a single attempt. It is never refreshed, regardless of node activity:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const graph = new StateGraph(State)
  .addNode("callModel", callModel, {
    timeout: { runTimeout: 120_000 },
  })
  .compile();
```

When the limit is exceeded, LangGraph raises [`NodeTimeoutError`](https://reference.langchain.com/javascript/langchain-langgraph/index/NodeTimeoutError), clears any writes from the failed attempt, and lets the retry policy decide whether to retry.

### Idle timeout

`idleTimeout` is a progress-resetting cap. It fires only when the node stops making observable progress for the specified duration—unlike `runTimeout`, the clock resets whenever the node produces a progress signal:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const graph = new StateGraph(State)
  .addNode("callModel", callModel, {
    timeout: { idleTimeout: 30_000 },
  })
  .compile();
```

You can set `runTimeout` and `idleTimeout` together. Whichever fires first cancels the attempt.

#### Progress signals

Under the default `refreshOn: "auto"`, the idle clock resets on any of the following:

* State writes through the graph write path
* Custom stream output via `runtime.writer`
* Child-task scheduling
* Any LangChain callback event from the node or its descendants (LLM tokens, tool calls, chain start/end, etc.)

#### Heartbeat mode

Set `refreshOn: "heartbeat"` to narrow the refresh source to explicit `runtime.heartbeat()` calls only. This is useful when you want a strict idle definition that isn't reset by chatty subordinates:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const graph = new StateGraph(State)
  .addNode("callModel", callModel, {
    timeout: { idleTimeout: 30_000, refreshOn: "heartbeat" },
  })
  .compile();
```

#### Manual heartbeats

For long-running work that doesn't naturally emit progress signals, call `runtime.heartbeat()` to manually reset the idle clock:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import {
  StateGraph,
  StateSchema,
  START,
  END,
  type Runtime,
} from "@langchain/langgraph";
import * as z from "zod";

const State = new StateSchema({
  result: z.string(),
});

const longRunningNode = async (
  state: typeof State.State,
  runtime: Runtime<typeof State>
) => {
  for (const batch of fetchBatches()) {
    process(batch);
    runtime.heartbeat?.(); // [!code highlight]
  }
  return { result: "done" };
};

const graph = new StateGraph(State)
  .addNode("longRunningNode", longRunningNode, {
    timeout: { idleTimeout: 30_000, refreshOn: "heartbeat" },
  })
  .addEdge(START, "longRunningNode")
  .addEdge("longRunningNode", END)
  .compile();
```

`runtime.heartbeat()` is a no-op outside an idle-timed attempt, so you can call it unconditionally.

### NodeTimeoutError

When a timeout fires, LangGraph raises [`NodeTimeoutError`](https://reference.langchain.com/javascript/langchain-langgraph/index/NodeTimeoutError) with structured context about which limit was hit:

| Attribute     | Type                  | Description                                         |
| ------------- | --------------------- | --------------------------------------------------- |
| `node`        | `string`              | Name of the node whose execution timed out.         |
| `elapsed`     | `number`              | Milliseconds elapsed before the timeout fired.      |
| `kind`        | `"idle" \| "run"`     | Which timeout fired.                                |
| `timeout`     | `number`              | The value (ms) of the timeout that fired.           |
| `idleTimeout` | `number \| undefined` | The configured idle timeout (milliseconds), if any. |
| `runTimeout`  | `number \| undefined` | The configured run timeout (milliseconds), if any.  |

Use `isNodeTimeoutError(error)` to narrow caught errors in TypeScript.

`NodeTimeoutError` is retryable by default. Combining `timeout` with a retry policy works out of the box—the timeout clock resets on each new attempt, and writes from a timed-out attempt are cleared before the next retry:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const graph = new StateGraph(State)
  .addNode("callModel", callModel, {
    timeout: { idleTimeout: 30_000 },
    retryPolicy: { maxAttempts: 3 },
  })
  .compile();
```

### Dynamic timeouts with Send

When using [`Send`](https://reference.langchain.com/javascript/langchain-langgraph/index/Send) to dispatch nodes dynamically (for example, in map-reduce patterns), you can pass a timeout directly on the `Send` to override the target node's static timeout for that specific push:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { Send } from "@langchain/langgraph";

const fanOut = (state: typeof State.State) =>
  state.items.map(
    (item) =>
      new Send("processItem", { item }, { timeout: { idleTimeout: 15_000 } })
  );
```

If the timeout is omitted on the `Send`, the target node's timeout (set at [`addNode`](https://reference.langchain.com/javascript/classes/_langchain_langgraph.index.StateGraph.html#addNode) time) applies. This lets you set a default timeout on the node and tighten it for individual calls.

## Error handling

<Note>
  Requires `@langchain/langgraph>=1.4.0`.
</Note>

An error handler runs after a node fails and all retries are exhausted. It receives the current state and can update it or route to a different node using [`Command`](https://reference.langchain.com/javascript/langchain-langgraph/index/Command). This is useful for compensation flows (Saga patterns) where you want to recover gracefully rather than abort the entire graph.

Pass `errorHandler` to [`addNode`](https://reference.langchain.com/javascript/classes/_langchain_langgraph.index.StateGraph.html#addNode) on [`StateGraph`](https://reference.langchain.com/javascript/langchain-langgraph/index/StateGraph) only (not the base `Graph` class):

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import {
  StateGraph,
  StateSchema,
  START,
  Command,
  NodeError,
} from "@langchain/langgraph";
import * as z from "zod";

class ConnectionError extends Error {}

const State = new StateSchema({
  status: z.string(),
});

const chargePayment = () => {
  throw new Error("payment gateway timeout");
};

const paymentErrorHandler = (
  state: typeof State.State,
  error: NodeError
) =>
  new Command({
    update: { status: `compensated: ${error.error.message}` },
    goto: "finalize",
  });

const finalize = (state: typeof State.State) => state;

const graph = new StateGraph(State)
  .addNode("chargePayment", chargePayment, {
    retryPolicy: {
      maxAttempts: 3,
      retryOn: (err) => err instanceof ConnectionError,
    },
    errorHandler: paymentErrorHandler,
  })
  .addNode("finalize", finalize)
  .addEdge(START, "chargePayment")
  .compile();
```

The handler fires only after the retry policy is exhausted, or immediately if no retry policy is configured. The retry policy and the error handler stay decoupled: configure when to retry and when to compensate independently.

### NodeError

Error handlers receive failure context through a typed `error: NodeError` parameter:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { Command, NodeError } from "@langchain/langgraph";

const myHandler = (state: typeof State.State, error: NodeError) => {
  console.log(`Node ${error.node} failed with: ${error.error.message}`);
  return new Command({
    update: { status: "recovered" },
    goto: "nextStep",
  });
};
```

[`NodeError`](https://reference.langchain.com/javascript/langchain-langgraph/index/NodeError) is a class with two fields:

| Attribute | Type     | Description                              |
| --------- | -------- | ---------------------------------------- |
| `node`    | `string` | Name of the node whose execution failed. |
| `error`   | `Error`  | The exception thrown by the failed node. |

The `error: NodeError` parameter is opt-in. Handlers that don't need failure context can omit the second argument and accept only `state`.

### Route with Command

Error handlers can return a [`Command`](https://reference.langchain.com/javascript/langchain-langgraph/index/Command) to update state and route to a specific node, enabling Saga / compensation patterns:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import {
  StateGraph,
  StateSchema,
  START,
  Command,
  NodeError,
} from "@langchain/langgraph";
import * as z from "zod";

class ConnectionError extends Error {}

const State = new StateSchema({
  status: z.string(),
});

const reserveInventory = () => ({ status: "reserved" });

const chargePayment = () => {
  throw new Error("payment timeout");
};

const paymentErrorHandler = (
  state: typeof State.State,
  error: NodeError
) =>
  new Command({
    update: {
      status: `compensated_after_${error.node}: ${error.error.message}`,
    },
    goto: "finalize",
  });

const finalize = (state: typeof State.State) => state;

const graph = new StateGraph(State)
  .addNode("reserveInventory", reserveInventory)
  .addNode("chargePayment", chargePayment, {
    retryPolicy: {
      maxAttempts: 3,
      retryOn: (err) => err instanceof ConnectionError,
    },
    errorHandler: paymentErrorHandler,
  })
  .addNode("finalize", finalize)
  .addEdge(START, "reserveInventory")
  .addEdge("reserveInventory", "chargePayment")
  .compile();
```

`chargePayment` retries on `ConnectionError` up to 3 times. If retries are exhausted (or the error isn't a `ConnectionError`), the handler compensates by updating state and routing to `finalize` instead of aborting the graph.

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
  Requires `@langchain/langgraph>=1.4.0`.
</Note>

Instead of repeating the same `retryPolicy`, `errorHandler`, `timeout`, or `cachePolicy` on every `addNode` call, use [`setNodeDefaults`](https://reference.langchain.com/javascript/langchain-langgraph/index/StateGraph#member-setNodeDefaults) to configure graph-wide defaults in one place:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { StateGraph, START, NodeError } from "@langchain/langgraph";

const defaultErrorHandler = (
  state: typeof State.State,
  error: NodeError
) => ({ status: `handled: ${error.error.message}` });

const graph = new StateGraph(State)
  .setNodeDefaults({
    retryPolicy: { maxAttempts: 3 },
    errorHandler: defaultErrorHandler,
    timeout: { runTimeout: 30_000 },
    cachePolicy: { ttl: 60 },
  })
  .addNode("stepA", stepA)
  .addNode("stepB", stepB)
  .addEdge(START, "stepA")
  .compile();
```

Both `stepA` and `stepB` now share the same retry policy, error handler, timeout, and cache policy without any duplication.

### Precedence

Per-node values passed directly to `addNode()` always override defaults set by `setNodeDefaults()`. Defaults are resolved at `compile()` time, so you can call `setNodeDefaults()` before or after `addNode()` in any order:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { StateGraph, START } from "@langchain/langgraph";

const graph = new StateGraph(State)
  .setNodeDefaults({ errorHandler: defaultErrorHandler })
  .addNode("stepA", stepA) // uses defaultErrorHandler
  .addNode("stepB", stepB, { errorHandler: customErrorHandler }) // overrides default
  .addEdge(START, "stepA")
  .compile();
```

### Applicability matrix

Not all defaults apply to all node types. Error-handler nodes (those registered via `addNode(..., { errorHandler })`) are excluded from certain defaults to prevent unsafe behavior:

| `setNodeDefaults` parameter | Applies to regular nodes | Applies to error-handler nodes | Reason                                                      |
| --------------------------- | ------------------------ | ------------------------------ | ----------------------------------------------------------- |
| `retryPolicy`               | ✅                        | ✅                              | Handlers should be retried on transient failures            |
| `timeout`                   | ✅                        | ✅                              | Stuck handlers should be cancelled like stuck regular nodes |
| `errorHandler`              | ✅                        | ❌                              | Handlers must never catch themselves                        |
| `cachePolicy`               | ✅                        | ❌                              | Caching handler results is unsafe                           |

### Scope

Defaults set on a parent graph are **not** inherited by subgraphs. Each graph maintains its own defaults.

## Functional API

The `timeout` option is available on `task` and `entrypoint`; `task` also accepts a `retry` option (not `retryPolicy`):

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { entrypoint, task } from "@langchain/langgraph";

const callApi = task(
  {
    name: "callApi",
    timeout: { idleTimeout: 30_000 },
    retry: { maxAttempts: 3 },
  },
  async (url: string) => {
    const response = await fetch(url);
    return response.text();
  }
);

const myWorkflow = entrypoint(
  { name: "myWorkflow", timeout: 60_000 },
  async (inputs: { url: string }) => {
    return await callApi(inputs.url);
  }
);
```

The behavior matches `addNode`: `NodeTimeoutError` is raised on timeout, buffered writes are cleared, and the retry policy decides whether to retry. Error handlers are not available on `task` / `entrypoint` in the JavaScript/TypeScript SDK—use `StateGraph.addNode(..., { errorHandler })` instead.

## Graceful shutdown

Cooperative shutdown lets you stop an in-flight graph run after the current superstep completes and save a resumable checkpoint. This is useful for handling SIGTERM signals or any external supervisor that needs to reclaim resources without losing work.

<Note>
  Requires `@langchain/langgraph>=1.4.0`.
</Note>

Create a [`RunControl`](https://reference.langchain.com/javascript/langchain-langgraph/index/RunControl) and pass it as `control` to `invoke` or `stream`. Call `requestDrain()` from any context to signal that the run should stop:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { RunControl, GraphDrained } from "@langchain/langgraph";

const control = new RunControl();

// In a signal handler or supervisor:
// control.requestDrain("sigterm");

try {
  const result = await graph.invoke(inputs, { ...config, control });
} catch (e) {
  if (e instanceof GraphDrained) {
    // The graph stopped early and saved a checkpoint.
    // Resume later with the same config.
    console.log(`Drained: ${e.reason}`);
  } else {
    throw e;
  }
}
```

### Semantics

Drain is cooperative and operates between supersteps, never preempting work that is already running:

| Scenario                                           | Behavior                                                                                      |
| -------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| Node mid-execution                                 | Runs to completion. Drain takes effect on the next superstep.                                 |
| Node with a retry policy currently retrying        | Retry loop runs to exhaustion or success. Drain takes effect after.                           |
| Graph finishes naturally on the same tick as drain | Returns normally. Inspect `control.drainRequested` to distinguish from a normal run.          |
| More supersteps remain                             | Raises `GraphDrained(reason)`. Checkpoint is saved and resumable.                             |
| Subgraph requests drain                            | `GraphDrained` bubbles up through the parent and stops it at its own next superstep boundary. |

### Resume after drain

Resume a drained run with `invoke(null, config)` using the same `thread_id`:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const result = await graph.invoke(null, config);
```

### Read drain state inside a node

Access drain state through the `runtime` parameter to adjust node behavior before the superstep boundary is reached:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { type Runtime } from "@langchain/langgraph";

const myNode = async (state: typeof State.State, runtime: Runtime<typeof State>) => {
  if (runtime.control?.drainRequested) {
    // Skip expensive work and return a minimal result
    return { status: "skipped", reason: runtime.control.drainReason };
  }
  return { status: await doWork() };
};
```

### SIGTERM hook pattern

The recommended pattern for handling process shutdown:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import process from "node:process";
import { RunControl, GraphDrained } from "@langchain/langgraph";

const control = new RunControl();
process.on("SIGTERM", () => control.requestDrain("sigterm"));

try {
  const result = await graph.invoke(inputs, { ...config, control });
} catch (e) {
  if (e instanceof GraphDrained) {
    console.log(`graph drained: ${e.reason}`);
    // Resume on next startup with the same config
  } else {
    throw e;
  }
}
```

<Note>
  `requestDrain()` does not cancel in-flight async work. For a hard upper bound, pair drain with a graceful timeout and an `AbortSignal`.
</Note>

## Limitations

* **`setNodeDefaults` is not inherited by subgraphs**: each graph manages its own defaults independently.
* **Error handlers are `StateGraph`-only**: pass `errorHandler` to `StateGraph.addNode`, not the base `Graph` class. Error handlers are not available on `task` / `entrypoint`.
* **One handler per node**: each node can have at most one `errorHandler`.
* **Handler failures bubble up**: if the error handler itself throws, that exception propagates as if the node had no handler.

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
Source: https://docs.langchain.com/oss/javascript/langgraph/frontend/custom-stream-channels

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

A custom channel has two ends. On the server, a [`StreamTransformer`](https://reference.langchain.com/javascript/langchain-langgraph/index/StreamTransformer) opens a
named [`StreamChannel`](https://reference.langchain.com/javascript/langchain-langgraph/index/StreamChannel) and pushes payloads onto it. On the client, a selector
subscribes to the matching `custom:<name>` channel and exposes the payloads as
reactive state.

The transformer's `process` method runs for every protocol event. It can mutate
the event in place (here, scrubbing PII from `messages`, `tools`, and `values`
data) and push side-channel updates whenever it has something to report.

The client-side selectors (`useExtension`, `useChannel`) ship with the v1
frontend SDK packages (`@langchain/react`, `@langchain/vue`,
`@langchain/svelte`, `@langchain/angular`).

<Note>
  Stream transformers and `StreamChannel` require `@langchain/langgraph>=1.3.1`.
</Note>

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { StreamChannel } from "@langchain/langgraph";
import type { ProtocolEvent, StreamTransformer } from "@langchain/langgraph";

export const createRedactionStatsTransformer = (): StreamTransformer<{
  redactionStats: StreamChannel<RedactionStatsEvent>;
}> => {
  // Open a remote channel named "redaction-stats".
  const redactionStats = StreamChannel.remote<RedactionStatsEvent>("redaction-stats");
  const counts = emptyCounts();

  return {
    init: () => ({ redactionStats }),

    process(event: ProtocolEvent): boolean {
      // Redact event.params.data in place and tally what was found.
      const delta = redactInPlace(event, counts);
      if (Object.keys(delta).length > 0) {
        // Publish a payload on the channel.
        redactionStats.push({
          kind: "update",
          at: Date.now(),
          delta,
          counts: { ...counts },
          total: totalRedactions(counts),
        });
      }
      return true; // Keep the (now-redacted) event in the stream.
    },
  };
};
```

Attach the transformer when you build the agent:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { createAgent } from "langchain";

const agent = createAgent({
  model: "anthropic:claude-haiku-4-5",
  tools: [...],
  streamTransformers: [createRedactionStatsTransformer],
});
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
See [Graph execution](/oss/javascript/langgraph/frontend/graph-execution) for namespace
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

* [Overview](/oss/javascript/langgraph/frontend/overview) — the LangGraph frontend stream
  API and architecture.
* [Graph execution](/oss/javascript/langgraph/frontend/graph-execution) — namespace-scoped
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
