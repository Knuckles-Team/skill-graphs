
<CaptionedImage src="/img/cloud/nexus/go-sdk-observability-sync.png" title="Observability Sync" />

An asynchronous Nexus Operation will surface in the caller Workflow as follows, with `NexusOperationScheduled`, `NexusOperationStarted`, and `NexusOperationCompleted`, in the caller's Event history:

<CaptionedImage src="/img/cloud/nexus/go-sdk-observability-async.png" title="Observability Async" />

### Temporal CLI

Use the `workflow describe` command to show pending Nexus Operations in the caller Workflow and any attached callbacks on the handler Workflow:

```
temporal workflow describe -w <ID>
```

Nexus events are included in the caller's Event history:

```
temporal workflow show -w <ID>
```

For **asynchronous Nexus Operations** the following are reported in the caller's history:

- `NexusOperationScheduled`
- `NexusOperationStarted`
- `NexusOperationCompleted`

For **synchronous Nexus Operations** the following are reported in the caller's history:

- `NexusOperationScheduled`
- `NexusOperationCompleted`

:::note

`NexusOperationStarted` isn't reported in the caller's history for synchronous operations.

:::

### OpenTelemetry

The `@temporalio/interceptors-opentelemetry` package supports Nexus Operations, providing automatic trace context propagation across Nexus boundaries from the caller Workflow to the handler.

The easiest way to enable it is with the `OpenTelemetryPlugin`, which auto-registers Nexus interceptors alongside Activity and Workflow interceptors:

```ts

const plugin = new OpenTelemetryPlugin({
  resource: myResource,
  spanProcessor: mySpanProcessor,
});

const worker = await Worker.create({
  // ...
  plugins: [plugin],
  nexusServices: [myServiceHandler],
});
```

The plugin creates the following spans:

- **Caller side:** `StartNexusOperation:service/operation` — created when the caller Workflow starts a Nexus Operation.
- **Handler side:** `RunStartNexusOperation:service/operation` and `RunCancelNexusOperation:service/operation` — created when the handler processes the operation. These spans are children of the caller span, linked via trace context propagated in Nexus request headers.

See the [interceptors-opentelemetry sample](https://github.com/temporalio/samples-typescript/tree/main/interceptors-opentelemetry) for a complete example.

For custom interceptor logic beyond tracing (e.g., logging, authorization), see [Nexus interceptor registration](/develop/typescript/workers/interceptors#nexus-interceptor-registration).

## Learn more

- Read the high-level description of the [Temporal Nexus feature](/evaluate/nexus) and watch the [Nexus keynote and demo](https://youtu.be/qqc2vsv1mrU?feature=shared&t=2082).
- Learn how Nexus works in the [Nexus deep dive talk](https://www.youtube.com/watch?v=izR9dQ_eIe4) and [Encyclopedia](/nexus).
- Deploy Nexus Endpoints in production with [Temporal Cloud](/cloud/nexus).

---

## Nexus - TypeScript SDK

<ReleaseNoteHeader
  featureName="nexus"
/>

![TypeScript SDK Banner](/img/assets/banner-typescript-temporal.png)

## Temporal Nexus

- [Quickstart](/develop/typescript/nexus/quickstart)
- [Feature guide](/develop/typescript/nexus/feature-guide)

---

## Nexus TypeScript Quickstart

<ReleaseNoteHeader
  featureName="nexus"
/>

[Temporal Nexus](/evaluate/nexus) connects Temporal Applications within and across Namespaces using a Nexus Endpoint, a Nexus Service contract, and Nexus Operations. Build a Nexus Service that wraps an existing Temporal Workflow, then invoke it from a caller Workflow.

:::info NEW TO NEXUS?
This page will help you get a working sample running in TypeScript.
To evaluate whether Nexus fits your use case, see the [evaluation guide](/evaluate/nexus) and to learn more about Nexus features, click [here](/nexus).
:::

**Prerequisites:** Complete the [TypeScript SDK Quickstart](/develop/typescript/set-up-your-local-typescript) first.
You should have `activities.ts`, `workflows.ts`, `worker.ts`, and `client.ts` from that guide.

## What you'll build

You have `example` running in the `default` Namespace.
By the end of this guide:

1. A Nexus Service will expose `example` as an Operation.
2. A second Namespace will contain a Workflow that calls that Operation.
3. The caller Workflow will get back `"Hello, Temporal!"` — the same result, but across Namespaces.

<SetupSteps>

<SetupStep code={
<>

<CodeSnippet language="typescript">
{`import * as nexus from 'nexus-rpc';

export interface MyInput {
    name: string;
}

export const sayHelloService = nexus.service('say-hello', {
    sayHello: nexus.operation<MyInput, string>(),
});`}
</CodeSnippet>

</>
}>

## 1. Define the Nexus Service

Create a file called `service.ts` that defines the Nexus Service contract.

Creating a Nexus Service establishes the contract between your implementation and any callers.
It provides type safety when invoking Nexus Operations and ensures that Operation Handlers fulfill the contract.

`nexus.service()` declares a named service, and `nexus.operation()` defines a typed operation.
The `example` Workflow returns `string`, so the operation output type is `string`.

</SetupStep>

<SetupStep code={
<>

<CodeSnippet language="typescript">
{`import { randomUUID } from 'crypto';

export const sayHelloHandler = nexus.serviceHandler(sayHelloService, {
    sayHello: new temporalNexus.WorkflowRunOperationHandler<MyInput, string>(
      async (ctx, input: MyInput) => {
        return await temporalNexus.startWorkflow(ctx, example, {
          args: [input.name],
          workflowId: "say-hello-nexus-" + randomUUID(),

          // Task queue defaults to the task queue this Operation is handled on.
        });
      },
    ),
});`}
</CodeSnippet>

</>
}>

## 2. Define the Nexus Operation handlers

Create a file called `handler.ts` that implements the Nexus Operation handler.

Operation handlers contain the logic that runs when a caller invokes a Nexus Operation.

`WorkflowRunOperationHandler` creates an asynchronous Nexus Operation that starts a Workflow.
The handler bridges the Nexus `MyInput` interface to the `example` Workflow's `string` parameter by extracting `input.name`.

</SetupStep>

<SetupStep code={
<>

<CodeSnippet language="typescript">
{`import { NativeConnection, Worker } from '@temporalio/worker';

async function run() {
    const connection = await NativeConnection.connect({
      address: 'localhost:7233',
    });
    try {
      const worker = await Worker.create({
        connection,
        namespace: 'default',
        taskQueue: 'hello-world',
        workflowsPath: require.resolve('./workflows'),
        activities,
        nexusServices: [sayHelloHandler],
      });
      await worker.run();
    } finally {
      await connection.close();
    }
}

run().catch((err) => {
    console.error(err);
    process.exit(1);
});`}
</CodeSnippet>

</>
}>

## 3. Register the Nexus Service handler in a Worker

Update your existing `worker.ts` to register the Nexus Service Handler.

A Worker will only poll for and process incoming Nexus requests if the Nexus Service Handlers are registered.
This is the same Worker concept used for Workflows and Activities.

The `nexusServices` parameter registers the handler so it can receive Nexus Operation requests.

</SetupStep>

<SetupStep code={
<>

<CodeSnippet language="typescript">
{`import { proxyActivities, createNexusServiceClient } from '@temporalio/workflow';
// Only import the activity types

const { greet } = proxyActivities<typeof activities>({
    startToCloseTimeout: '1 minute',
});

/** A workflow that simply calls an activity */
export async function example(name: string): Promise<string> {
    return await greet(name);
}

const NEXUS_ENDPOINT = 'my-nexus-endpoint-name';

export async function callerWorkflow(name: string): Promise<string> {
    const nexusClient = createNexusServiceClient({
      service: sayHelloService,
      endpoint: NEXUS_ENDPOINT,
    });
    return await nexusClient.executeOperation('sayHello', { name }, { scheduleToCloseTimeout: '10s' });
}
`}
</CodeSnippet>

</>
}>

## 4. Develop the caller Workflow

Update your existing `workflows.ts` file with a Workflow which invokes the Nexus Operation.

The caller Workflow demonstrates the consumer side of Nexus.
Instead of importing handler code directly, the caller only depends on the Service contract.
This keeps the caller and handler decoupled so they can live in separate Namespaces, repositories, or even teams.

The `wf.createNexusServiceClient()` method creates a client bound to your Nexus Service and Endpoint.
`executeOperation` starts the operation and waits for the result.

</SetupStep>

<SetupStep code={
<>

<CodeSnippet language="bash">
temporal operator namespace create --namespace my-caller-namespace
</CodeSnippet>

<CodeSnippet language="bash">
{`temporal operator nexus endpoint create \\
  --name my-nexus-endpoint-name \\
  --target-namespace default \\
  --target-task-queue hello-world`}
</CodeSnippet>

</>
}>

## 5. Create the caller Namespace and Nexus Endpoint

Before running the application, create a caller Namespace and a Nexus Endpoint to route requests from the caller to the handler.
The handler uses the `default` Namespace that was created when you started the dev server.

Namespaces provide isolation between the caller and handler sides.
The Nexus Endpoint acts as a routing layer that connects the caller Namespace to the handler's target Namespace and Task Queue.
The endpoint name must match the variable defined in `caller.ts` from step 4.

Make sure your local Temporal dev server is running (`temporal server start-dev`).

</SetupStep>

<SetupStep code={
<>

<CodeSnippet language="typescript">
{`import { randomUUID } from 'crypto';

const CALLER_TASK_QUEUE = 'my-caller-task-queue';
const NAMESPACE = 'my-caller-namespace';

async function main() {
    const clientConnection = await Connection.connect({
      address: 'localhost:7233',
    });
    const client = new Client({
      connection: clientConnection,
      namespace: NAMESPACE,
    });

    const workerConnection = await NativeConnection.connect({
      address: 'localhost:7233',
    });
    try {
      const worker = await Worker.create({
        connection: workerConnection,
        namespace: NAMESPACE,
        taskQueue: CALLER_TASK_QUEUE,
        workflowsPath: require.resolve('./workflows'),
      });

      await worker.runUntil(async () => {
        const result = await client.workflow.execute(callerWorkflow, {
          args: ['Temporal'],
          workflowId: \`caller-workflow-\${randomUUID()}\`,
          taskQueue: CALLER_TASK_QUEUE,
        });
        console.log('Workflow result:', result);
      });
    } finally {
      await workerConnection.close();
    }
}

main().catch((err) => {
    console.error(err);
    process.exit(1);
});`}
</CodeSnippet>

</>
}>

## 6. Run and Verify

Create a file called `caller-starter.ts` to start the caller Worker and execute the Workflow.

This step brings everything together: the caller Worker hosts `callerWorkflow`, which uses the Nexus client to invoke `sayHello` on the handler side.
The full request flows from the caller Workflow, through the Nexus Endpoint, to the handler Worker running the `example` Workflow, and back to the caller.

**Run the application:**

1. Start the handler Worker in one terminal:

```bash
npx ts-node src/worker.ts
```

2. Run the caller in another terminal:

```bash
npx ts-node src/caller-starter.ts
```

You should see:

```
Workflow result: Hello, Temporal!
```

Open the [Temporal Web UI](http://localhost:8233) and find the `callerWorkflow` execution.
You should see `NexusOperationScheduled`, `NexusOperationStarted`, and `NexusOperationCompleted` events in the Event history.

</SetupStep>
</SetupSteps>

## Next Steps

Now that you have a working Nexus Service, here are some resources to deepen your understanding:

- **[TypeScript Nexus Feature Guide](/develop/typescript/nexus)**: Covers synchronous and asynchronous Operations, error handling, cancellation, and cross-Namespace calls.
- **[Nexus Operations](/nexus/operations)**: The full Operation lifecycle, including retries, timeouts, and execution semantics.
- **[Nexus Services](/nexus/services)**: Designing Service contracts and registering multiple Services per Worker.
- **[Nexus Patterns](/nexus/patterns)**: Comparing the collocated and router-queue deployment patterns.
- **[Error Handling in Nexus](/nexus/error-handling)**: Handling retryable and non-retryable errors across caller and handler boundaries.
- **[Execution Debugging](/nexus/execution-debugging)**: Bi-directional linking and OpenTelemetry tracing for debugging Nexus calls.
- **[Nexus Endpoints](/nexus/endpoints)**: Managing Endpoints and understanding how they route requests.
- **[Temporal Nexus on Temporal Cloud](/cloud/nexus)**: Deploying Nexus in a production Temporal Cloud environment with built-in access controls and multi-region connectivity.

---

## Enriching the user interface - TypeScript SDK

Temporal supports adding context to Workflows and Events with metadata.
This helps users identify and understand Workflows and their operations.

## Adding Summary and Details to Workflows

### Starting a Workflow

When starting a Workflow, you can provide a static summary and details to help identify the workflow in the UI:

```typescript

const client = new Client();

// Start a workflow with static summary and details
const handle = await client.workflow.start(yourWorkflow, {
  args: ['workflow input'],
  taskQueue: 'your-task-queue',
  workflowId: 'your-workflow-id',
  staticSummary: 'Order processing for customer #12345',
  staticDetails: 'Processing premium order with expedited shipping'
});
```

`staticSummary` is a single-line description that appears in the workflow list view, limited to 200 bytes.
`staticDetails` can be multi-line and provides more comprehensive information that appears in the workflow details view, with a larger limit of 20K bytes.

The input format is standard Markdown excluding images, HTML, and scripts.

You can also use the `execute` method with the same parameters:

```typescript
const result = await client.workflow.execute(yourWorkflow, {
  args: ['workflow input'],
  taskQueue: 'your-task-queue',
  workflowId: 'your-workflow-id',
  staticSummary: 'Order processing for customer #12345',
  staticDetails: 'Processing premium order with expedited shipping'
});
```

### Inside the Workflow

Within a Workflow, you can get and set the _current workflow details_.
Unlike static summary/details set at Workflow start, this value can be updated throughout the life of the Workflow.
Current Workflow details also takes Markdown format (excluding images, HTML, and scripts) and can span multiple lines.

```typescript

export async function yourWorkflow(input: string): Promise<string> {
  // Get the current details
  const currentDetails = getCurrentDetails();
  console.log(`Current details: ${currentDetails}`);

  // Set/update the current details
  setCurrentDetails('Updated workflow details with new status');

  return 'Workflow completed';
}
```

### Adding Summary to Activities and Timers

You can attach a `summary` to activities by using `executeWithOptions` when calling them:

```typescript

const { yourActivity } = proxyActivities<typeof activities>({
  startToCloseTimeout: '10 seconds'
});

export async function yourWorkflow(input: string): Promise<string> {
  // Execute an activity with a summary using executeWithOptions
  const result = await yourActivity.executeWithOptions(
    {
      staticSummary: 'Processing user data'
    },
    [input] // Note: arguments must be passed as an array
  );

  return result;
}
```

Similarly, you can attach a `summary` to timers within a workflow:

```typescript

export async function yourWorkflow(input: string): Promise<string> {
  // Create a timer with a summary
  await sleep('5 minutes', { summary: 'Waiting for payment confirmation' });

  return 'Timer completed';
}
```

The input format for `summary` is a string, and limited to 200 bytes.

## Viewing Summary and Details in the UI

Once you've added summaries and details to your Workflows, Activities, and Timers, you can view this enriched information in the Temporal Web UI.
Navigate to your Workflow's details page to see the metadata displayed in two key locations:

### Workflow Overview Section

At the top of the workflow details page, you'll find the workflow-level metadata:

- **Summary & Details** - Displays the static summary and static details set when starting the workflow
- **Current Details** - Displays the dynamic details that can be updated during workflow execution

All Workflow details support standard Markdown formatting (excluding images, HTML, and scripts), allowing you to create rich, structured information displays.

### Event History

Individual events in the Workflow's Event History display their associated summaries when available.

Workflow, Activity and Timer summaries appear in purple text next to their corresponding Events, providing immediate context without requiring you to expand the event details.
When you do expand an Event, the summary is also prominently displayed in the detailed view.

---

## Client - TypeScript SDK(Platform)

![TypeScript SDK Banner](/img/assets/banner-typescript-temporal.png)

## Platform

- [Observability](/develop/typescript/platform/observability)
- [Enriching the UI](/develop/typescript/platform/enriching-ui)

---

## Observability - TypeScript SDK

The observability section of the TypeScript developer guide covers the many ways to view the current state of your [Temporal Application](/temporal#temporal-application)—that is, ways to view which [Workflow Executions](/workflow-execution) are tracked by the [Temporal Platform](/temporal#temporal-platform) and the state of any specified Workflow Execution, either currently or at points of an execution.

This section covers features related to viewing the state of the application, including:

- [Emit metrics](#metrics)
- [Set up tracing](#tracing)
- [Log from a Workflow](#logging)
- [Visibility APIs](#visibility)

## Emit metrics {/* #metrics */}

Each Temporal SDK is capable of emitting an optional set of metrics from either the Client or the Worker process.
For a complete list of metrics capable of being emitted, see the [SDK metrics reference](/references/sdk-metrics).

- For an overview of Prometheus and Grafana integration, refer to the [Monitoring](/self-hosted-guide/monitoring) guide.
- For a list of metrics, see the [SDK metrics reference](/references/sdk-metrics).
- For an end-to-end example that exposes metrics with the TypeScript SDK, refer to the [samples-typescript](https://github.com/temporalio/samples-typescript/tree/main/interceptors-opentelemetry) repo.

Workers can emit metrics and traces. There are a few [telemetry options](https://typescript.temporal.io/api/interfaces/worker.TelemetryOptions) that can be provided to [`Runtime.install`](https://typescript.temporal.io/api/classes/worker.Runtime/#install). The common options are:

- `metrics: { otel: { url } }`: The URL of a gRPC [OpenTelemetry collector](https://opentelemetry.io/docs/collector/).
- `metrics: { prometheus: { bindAddress } }`: Address on the Worker host that will have metrics for [Prometheus](https://prometheus.io/) to scrape.

To set up tracing of Workflows and Activities, use our `opentelemetry-interceptors` package.
(For details, see the next section.)

```typescript
telemetryOptions: {
    metrics: {
      prometheus: { bindAddress: '0.0.0.0:9464' },
    },
    logging: { forward: { level: 'DEBUG' } },
  },
```

## Set up tracing {/* #tracing */}

Tracing allows you to view the call graph of a Workflow along with its Activities and any Child Workflows.

Temporal Web's tracing capabilities mainly track Activity Execution within a Temporal context. If you need custom tracing specific for your use case, you should make use of context propagation to add tracing logic accordingly.

The [`interceptors-opentelemetry`](https://github.com/temporalio/samples-typescript/tree/main/interceptors-opentelemetry) sample shows how to use the SDK's built-in OpenTelemetry tracing to trace everything from starting a Workflow to Workflow Execution to running an Activity from that Workflow.

The built-in tracing uses protobuf message headers (like [this one](https://github.com/temporalio/api/blob/b2b8ae6592a8730dd5be6d90569d1aea84e1712f/temporal/api/workflowservice/v1/request_response.proto#L161) when starting a Workflow) to propagate the tracing information from the client to the Workflow and from the Workflow to its successors (when Continued As New), children, and Activities.
All of these executions are linked with a single trace identifier and have the proper `parent -> child` span relation.

Tracing is compatible between different Temporal SDKs as long as compatible [context propagators](https://opentelemetry.io/docs/concepts/context-propagation/) are used.

**Context propagation**

The TypeScript SDK uses the global OpenTelemetry propagator.

To extend the default ([Trace Context](https://github.com/open-telemetry/opentelemetry-js/blob/main/packages/opentelemetry-core/README.md#w3ctracecontextpropagator-propagator) and [Baggage](https://github.com/open-telemetry/opentelemetry-js/blob/main/packages/opentelemetry-core/README.md#baggage-propagator) propagators) to also include the [Jaeger propagator](https://www.npmjs.com/package/@opentelemetry/propagator-jaeger), follow these steps:

- `npm i @opentelemetry/propagator-jaeger`

- At the top level of your Workflow code, add the following lines:

  ```js

    CompositePropagator,
    W3CBaggagePropagator,
    W3CTraceContextPropagator,
  } from '@opentelemetry/core';

  propagation.setGlobalPropagator(
    new CompositePropagator({
      propagators: [
        new W3CTraceContextPropagator(),
        new W3CBaggagePropagator(),
        new JaegerPropagator(),
      ],
    }),
  );
  ```

Similarly, you can customize the OpenTelemetry `NodeSDK` propagators by following the instructions in the [Initialize the SDK](https://github.com/open-telemetry/opentelemetry-js/tree/main/experimental/packages/opentelemetry-sdk-node#initialize-the-sdk) section of the `README.md` file.

## Log from a Workflow {/* #logging */}

Logging enables you to record critical information during code execution.
Loggers create an audit trail and capture information about your Workflow's operation.
An appropriate logging level depends on your specific needs.
During development or troubleshooting, you might use debug or even trace.
In production, you might use info or warn to avoid excessive log volume.

The logger supports the following logging levels:

| Level   | Use                                                                                                       |
| ------- | --------------------------------------------------------------------------------------------------------- |
| `TRACE` | The most detailed level of logging, used for very fine-grained information.                               |
| `DEBUG` | Detailed information, typically useful for debugging purposes.                                            |
| `INFO`  | General information about the application's operation.                                                    |
| `WARN`  | Indicates potentially harmful situations or minor issues that don't prevent the application from working. |
| `ERROR` | Indicates error conditions that might still allow the application to continue running.                    |

The Temporal SDK core normally uses `WARN` as its default logging level.

### Logging from Activities

Activities run in the standard Node.js environment and may therefore use any Node.js logger directly.

The Temporal SDK however provides a convenient Activity Context logger, which funnels log messages to the [Runtime's logger](/develop/typescript/platform/observability#customizing-the-default-logger). Attributes from the current Activity context are automatically included as metadata on every log entries emitted using the Activity context logger, and some key events of the Activity's lifecycle are automatically logged (at DEBUG level for most messages; WARN for failures).

<details>
<summary>
Using the Activity Context logger
</summary>

```ts

export async function greet(name: string): Promise<string> {
  log.info('Log from activity', { name });
  return `Hello, ${name}!`;
}
```

</details>

{/*

#### Customizing Activity logging with `ActivityOutboundCallsInterceptor`

FIXME(JWH): Quick introduction to `ActivityOutboundCallsInterceptor.getLogAttributes()`.
*/}

### Logging from Workflows

Workflows may not use regular Node.js loggers because:

1. Workflows run in a sandboxed environment and cannot do any I/O.
1. Workflow code might get replayed at any time, which would result in duplicated log messages.

The Temporal SDK however provides a Workflow Context logger, which funnels log messages to the [Runtime's logger](/develop/typescript/platform/observability#customizing-the-default-logger). Attributes from the current Workflow context are automatically included as metadata on every log entries emitted using the Workflow context logger, and some key events of the Workflow's lifecycle are automatically logged (at DEBUG level for most messages; WARN for failures).

<details>
<summary>
Using the Workflow Context logger
</summary>

```ts

export async function myWorkflow(name: string): Promise<string> {
  log.info('Log from workflow', { name });
  return `Hello, ${name}!`;
