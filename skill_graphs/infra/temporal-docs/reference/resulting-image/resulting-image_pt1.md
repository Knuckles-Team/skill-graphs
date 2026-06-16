# -- RESULTING IMAGE --

FROM gcr.io/distroless/nodejs20-debian11

COPY --from=builder /app /app
WORKDIR /app

CMD ["node", "build/worker.js"]
```

### Properly configure Node.js memory in Docker

By default, `node` configures its maximum old-gen memory to 25% of the _physical memory_ of the machine on which it is
executing, with a maximum of 4 GB. This is likely inappropriate when running Node.js in a Docker environment and can
result in either underusage of available memory (`node` only uses a fraction of the memory allocated to the container)
or overusage (`node` tries to use more memory than what is allocated to the container, which will eventually lead to the
process being killed by the operating system).

Therefore we recommended that you always explicitly set the `--max-old-space-size` `node` argument to approximately 80%
of the maximum size (in megabytes) that you want to allocate the `node` process. You might need some experimentation and
adjustment to find the most appropriate value based on your specific application.

In practice, it is generally easier to provide this argument through the
[`NODE_OPTIONS` environment variable](https://nodejs.org/api/cli.html#node_optionsoptions).

### Do not use Alpine

Alpine replaces glibc with musl, which is incompatible with the Rust core of the TypeScript SDK. If you receive errors
like the following, it's probably because you are using Alpine.

```sh
Error: Error loading shared library ld-linux-x86-64.so.2: No such file or directory (needed by /opt/app/node_modules/@temporalio/core-bridge/index.node)
```

Or like this:

```sh
Error: Error relocating /opt/app/node_modules/@temporalio/core-bridge/index.node: __register_atfork: symbol not found
```

## How to run a Temporal Cloud Worker {/* #run-a-temporal-cloud-worker */}

To run a Worker that uses [Temporal Cloud](/cloud), you need to provide additional connection and client options that
include the following:

- An address that includes your [Cloud Namespace Name](/namespaces) and a port number:
  `<Namespace>.<ID>.tmprl.cloud:<port>`.
- mTLS CA certificate.
- mTLS private key.

For more information about managing and generating client certificates for Temporal Cloud, see
[How to manage certificates in Temporal Cloud](/cloud/certificates).

For more information about configuring TLS to secure inter- and intra-network communication for a Temporal Service, see
[Temporal Customization Samples](https://github.com/temporalio/samples-server).

### How to register types {/* #register-types */}

All Workers listening to the same Task Queue name must be registered to handle the exact same Workflows Types and
Activity Types.

If a Worker polls a Task for a Workflow Type or Activity Type it does not know about, it fails that Task. However, the
failure of the Task does not cause the associated Workflow Execution to fail.

In development, use
[`workflowsPath`](https://typescript.temporal.io/api/interfaces/worker.WorkerOptions/#workflowspath):

<!--SNIPSTART typescript-worker-create -->
[snippets/src/worker.ts](https://github.com/temporalio/samples-typescript/blob/main/snippets/src/worker.ts)
```ts

async function run() {
  const worker = await Worker.create({
    workflowsPath: require.resolve('./workflows'),
    taskQueue: 'snippets',
    activities,
  });

  await worker.run();
}
```
<!--SNIPEND-->

In this snippet, the Worker bundles the Workflow code at runtime.

In production, you can improve your Worker's startup time by bundling in advance: as part of your production build, call
`bundleWorkflowCode`:

<!--SNIPSTART typescript-bundle-workflow -->
[production/src/scripts/build-workflow-bundle.ts](https://github.com/temporalio/samples-typescript/blob/main/production/src/scripts/build-workflow-bundle.ts)
```ts

async function bundle() {
  const { code } = await bundleWorkflowCode({
    workflowsPath: require.resolve('../workflows'),
  });
  const codePath = path.join(__dirname, '../../workflow-bundle.js');

  await writeFile(codePath, code);
  console.log(`Bundle written to ${codePath}`);
}
```
<!--SNIPEND-->

Then the bundle can be passed to the Worker:

<!--SNIPSTART typescript-production-worker-->
[production/src/worker.ts](https://github.com/temporalio/samples-typescript/blob/main/production/src/worker.ts)
```ts
const workflowOption = () =>
  process.env.NODE_ENV === 'production'
    ? {
        workflowBundle: {
          codePath: require.resolve('../workflow-bundle.js'),
        },
      }
    : { workflowsPath: require.resolve('./workflows') };

async function run() {
  const worker = await Worker.create({
    ...workflowOption(),
    activities,
    taskQueue: 'production-sample',
  });

  await worker.run();
}
```
<!--SNIPEND-->

## How to shut down a Worker and track its state {/* #shut-down-a-worker */}

Workers shut down if they receive any of the Signals enumerated in
[shutdownSignals](https://typescript.temporal.io/api/interfaces/worker.RuntimeOptions#shutdownsignals): `'SIGINT'`,
`'SIGTERM'`, `'SIGQUIT'`, and `'SIGUSR2'`.

In development, we shut down Workers with `Ctrl+C` (`SIGINT`) or
[nodemon](https://github.com/temporalio/samples-typescript/blob/c37bae3ea235d1b6956fcbe805478aa46af973ce/hello-world/package.json#L10)
(`SIGUSR2`). In production, you usually want to give Workers time to finish any in-progress Activities by setting
[shutdownGraceTime](https://typescript.temporal.io/api/interfaces/worker.WorkerOptions#shutdowngracetime).

As soon as a Worker receives a shutdown Signal or request, the Worker stops polling for new Tasks and allows in-flight
Tasks to complete until `shutdownGraceTime` is reached. Any Activities that are still running at that time will stop
running and will be rescheduled by Temporal Server when an Activity timeout occurs.

If you must guarantee that the Worker eventually shuts down, you can set
[shutdownForceTime](https://typescript.temporal.io/api/interfaces/worker.WorkerOptions#shutdownforcetime).

You might want to programmatically shut down Workers (with
[Worker.shutdown()](https://typescript.temporal.io/api/classes/worker.Worker#shutdown)) in integration tests or when
automating a fleet of Workers.

### Worker states

At any time, you can Query Worker state with
[Worker.getState()](https://typescript.temporal.io/api/classes/worker.Worker#getstate). A Worker is always in one of
seven states:

- `INITIALIZED`: The initial state of the Worker after calling
  [Worker.create()](https://typescript.temporal.io/api/classes/worker.Worker#create) and successfully connecting to the
  server.
- `RUNNING`: [Worker.run()](https://typescript.temporal.io/api/classes/worker.Worker#run) was called and the Worker is
  polling Task Queues.
- `FAILED`: The Worker encountered an unrecoverable error; `Worker.run()` should reject with the error.
- The last four states are related to the Worker shutdown process:
  - `STOPPING`: The Worker received a shutdown Signal or `Worker.shutdown()` was called. The Worker will forcefully shut
    down after `shutdownGraceTime` expires.
  - `DRAINING`: All Workflow Tasks have been drained; waiting for Activities and cached Workflows eviction.
  - `DRAINED`: All Activities and Workflows have completed; ready to shut down.
  - `STOPPED`: Shutdown complete; `worker.run()` resolves.

If you need more visibility into internal Worker state, see the
[Worker class](https://typescript.temporal.io/api/classes/worker.Worker) in the API reference.

---

## Serverless Workers on AWS Lambda - TypeScript SDK

<ReleaseNoteHeader featureName="serverlessWorkers">
  To request access during Pre-release, create a [support ticket](/cloud/support#support-ticket) or contact your account team.
  APIs are experimental and may be subject to backwards-incompatible changes.
  [Sign up for updates](https://temporal.io/pages/serverless-workers-updates) to be notified when Serverless Workers reach Public Preview.
</ReleaseNoteHeader>

The `@temporalio/lambda-worker` package lets you run a Temporal Serverless Worker on AWS Lambda.
Deploy your Worker code as a Lambda function, and Temporal Cloud invokes it when Tasks arrive.
Each invocation starts a Worker, polls for Tasks, then gracefully shuts down before a configurable invocation deadline.
You register Workflows and Activities the same way you would with a standard Worker.

For a full end-to-end deployment guide covering AWS IAM setup, compute configuration, and verification, see [Deploy a Serverless Worker on AWS Lambda](/production-deployment/worker-deployments/serverless-workers/aws-lambda).

## Create and run a Worker in Lambda {/* #create-and-run */}

Use the `runWorker` function to create a Lambda handler that runs a Temporal Worker.
Pass a deployment version and a configure callback that sets up your Workflows and Activities.

<!--SNIPSTART typescript-lambda-worker {"selectedLines": ["1", "3-11", "13"]}-->
[lambda-worker/src/index.ts](https://github.com/temporalio/samples-typescript/blob/main/lambda-worker/src/index.ts)
```ts

// ...

export const handler = runWorker({ deploymentName: 'sdk-demo', buildId: 'v1' }, (config) => {
  config.workerOptions.taskQueue = TASK_QUEUE;
  config.workerOptions.workflowBundle = {
    codePath: require.resolve('./workflow-bundle.js'),
  };
  config.workerOptions.activities = activities;
// ...
});
```
<!--SNIPEND-->

The deployment version is required.
Worker Deployment Versioning is always enabled for Serverless Workers.
Each Workflow must declare a [versioning behavior](/worker-versioning#versioning-behaviors), either `AutoUpgrade` or `Pinned`.
The default versioning behavior is `PINNED`. To change it, set `workerDeploymentOptions.defaultVersioningBehavior` in the configure callback.

### Pre-bundle Workflow code {/* #pre-bundle */}

Use `workflowBundle` with pre-bundled code instead of `workflowsPath`.
Pre-bundling avoids webpack bundling overhead on every Lambda cold start.

Build the bundle as a separate build step:

```typescript

const { code } = await bundleWorkflowCode({
  workflowsPath: require.resolve('./workflows'),
});
await writeFile('./workflow-bundle.js', code);
```

Then reference the bundle in your handler with `workflowBundle: { codePath: require.resolve('./workflow-bundle.js') }`.

## Configure the Temporal connection {/* #configure-connection */}

The `@temporalio/lambda-worker` package automatically loads Temporal client configuration from a TOML config file and environment variables. Refer to [Environment Configuration](/develop/environment-configuration) for more details.

The config file is resolved in order:

1. `TEMPORAL_CONFIG_FILE` environment variable, if set.
2. `temporal.toml` in `$LAMBDA_TASK_ROOT` (typically `/var/task`).
3. `temporal.toml` in the current working directory.

The file is optional. If absent, only environment variables are used.

Encrypt sensitive values like TLS keys or API keys. Refer to [AWS documentation](https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars-encryption.html) for options.

## Adjust Worker defaults for Lambda {/* #lambda-tuned-defaults */}

The `@temporalio/lambda-worker` package applies conservative defaults suited to short-lived Lambda invocations.
These differ from standard Worker defaults to avoid overcommitting resources in a constrained environment.

| Setting | Lambda default |
|---|---|
| `maxConcurrentActivityTaskExecutions` | 2 |
| `maxConcurrentWorkflowTaskExecutions` | 10 |
| `maxConcurrentLocalActivityExecutions` | 2 |
| `maxConcurrentNexusTaskExecutions` | 5 |
| `workflowTaskPollerBehavior` | `SimpleMaximum(2)` |
| `activityTaskPollerBehavior` | `SimpleMaximum(1)` |
| `nexusTaskPollerBehavior` | `SimpleMaximum(1)` |
| `shutdownGraceTime` | 5 seconds |
| `maxCachedWorkflows` | 30 |
| `shutdownDeadlineBufferMs` | 7000 |

Eager Activities are not supported. Lambda invocations don't maintain persistent connections.

`shutdownDeadlineBufferMs` is specific to the `@temporalio/lambda-worker` package.
It controls how much time before the Lambda deadline the Worker begins its graceful shutdown.
The default is `shutdownGraceTime` (5s) + 2s.

If your Worker handles long-running Activities, increase `shutdownGraceTime`, `shutdownDeadlineBufferMs`, and the Lambda invocation deadline (`--timeout`) together.
For guidance on how these values relate, see [Tuning for long-running Activities](/serverless-workers#tuning-for-long-running-activities).

## Add observability with OpenTelemetry {/* #add-observability */}

The `@temporalio/lambda-worker/otel` module provides OpenTelemetry integration with defaults configured for the [AWS Distro for OpenTelemetry (ADOT)](https://aws-otel.github.io/docs/getting-started/lambda) Lambda layers.
With this enabled, the Worker emits SDK metrics and distributed traces for Workflow and Activity executions.

The underlying metrics and traces are the same ones the TypeScript SDK emits in any environment.
For general observability concepts and the full list of available metrics, see [Observability - TypeScript SDK](/develop/typescript/platform/observability) and the [SDK metrics reference](/references/sdk-metrics).

<!--SNIPSTART typescript-lambda-worker-->
[lambda-worker/src/index.ts](https://github.com/temporalio/samples-typescript/blob/main/lambda-worker/src/index.ts)
```ts

export const handler = runWorker({ deploymentName: 'sdk-demo', buildId: 'v1' }, (config) => {
  config.workerOptions.taskQueue = TASK_QUEUE;
  config.workerOptions.workflowBundle = {
    codePath: require.resolve('./workflow-bundle.js'),
  };
  config.workerOptions.activities = activities;
  applyDefaults(config);
});
```
<!--SNIPEND-->

`applyDefaults` registers Temporal SDK interceptors for tracing and configures the Core SDK to export metrics via OpenTelemetry Protocol (OTLP).
By default, telemetry is sent to `localhost:4317`, which is the ADOT Lambda layer's default collector endpoint.

To collect this telemetry, attach two ADOT Lambda layers:

1. The [ADOT JavaScript layer](https://aws-otel.github.io/docs/getting-started/lambda/lambda-js) for Node.js-side auto-instrumentation and trace export.
2. The [ADOT Collector layer](https://aws-otel.github.io/docs/getting-started/lambda) (`aws-otel-collector-amd64`) to run the OTel Collector as a Lambda extension, receiving telemetry via OTLP on `localhost:4317` and forwarding traces to X-Ray and metrics to CloudWatch.

The default Collector configuration does not route OTLP data to the traces pipeline.
You must provide a custom Collector configuration that wires the OTLP receiver to both the traces and metrics pipelines.
Bundle the following `otel-collector-config.yaml` in your Lambda deployment package:

<!--SNIPSTART typescript-lambda-worker-otel-collector-config-->
[lambda-worker/otel-collector-config.yaml](https://github.com/temporalio/samples-typescript/blob/main/lambda-worker/otel-collector-config.yaml)
```yaml
receivers:
  otlp:
    protocols:
      grpc:
        endpoint: 'localhost:4317'
      http:
        endpoint: 'localhost:4318'

exporters:
  debug:
  awsxray:
    region: us-west-2
  awsemf:
    # AWS EMF exporter for metrics
    # These are example configurations
    namespace: TemporalWorkerMetrics
    log_group_name: /aws/lambda/<your-function-name>
    region: us-west-2
    dimension_rollup_option: NoDimensionRollup
    resource_to_telemetry_conversion:
      enabled: true

service:
  pipelines:
    traces:
      receivers: [otlp]
      exporters: [awsxray, debug]
    metrics:
      receivers: [otlp]
      exporters: [awsemf]
  telemetry:
    logs:
      level: info
    metrics:
      address: localhost:8888
```
<!--SNIPEND-->

Set the following environment variable on the Lambda function:

- `OPENTELEMETRY_COLLECTOR_CONFIG_URI=/var/task/otel-collector-config.yaml`

Enable X-Ray active tracing on the Lambda function:

```bash
aws lambda update-function-configuration \
  --function-name <your-function-name> \
  --tracing-config Mode=Active
```

The Lambda execution role must have permissions to write to X-Ray and CloudWatch.
Add `xray:PutTraceSegments`, `xray:PutTelemetryRecords`, and `cloudwatch:PutMetricData` permissions to the execution role.
Without these permissions, the Collector fails silently and no telemetry appears.

When pre-bundling Workflow code, pass the plugin from `makeOtelPlugin()` so that Workflow interceptor modules are included in the bundle:

```typescript

const { plugin } = makeOtelPlugin();
const { code } = await bundleWorkflowCode({
  workflowsPath: require.resolve('./workflows'),
  plugins: [plugin],
});
```

---

## Serverless Workers - TypeScript SDK

Serverless Workers run on ephemeral, on-demand compute rather than long-lived processes.
Temporal invokes the Worker when Tasks arrive, and the Worker shuts down when the work is done.

For a general overview of how Serverless Workers work, see [Serverless Workers](/serverless-workers).
For the end-to-end deployment guide, see [Deploy a Serverless Worker](/production-deployment/worker-deployments/serverless-workers).

## Supported providers

- [**AWS Lambda**](/develop/typescript/workers/serverless-workers/aws-lambda) - Use the `@temporalio/lambda-worker` package to run a Worker as a Lambda function. Covers setup, configuration, Lambda-tuned defaults, and observability.

---

## Workflow basics - TypeScript SDK

## How to develop a Workflow {/* #develop-workflows */}

Workflows are the fundamental unit of a Temporal Application, and it all starts with the development of a [Workflow Definition](/workflow-definition).

In the Temporal TypeScript SDK programming model, Workflow Definitions are _just functions_, which can store state and orchestrate Activity Functions. The following code snippet uses `example` to schedule a `greet` Activity in the system to say hello.

A Workflow Definition can have multiple parameters; however, we recommend using a single object parameter.

```typescript
type ExampleArgs = {
  name: string;
};

export async function example(args: ExampleArgs): Promise<{ greeting: string }> {
  const greeting = await greet(args.name);
  return { greeting };
}
```

## How to define Workflow parameters {/* #workflow-parameters */}

Temporal Workflows may have any number of custom parameters. However, we strongly recommend that objects are used as
parameters, so that the object's individual fields may be altered without breaking the signature of the Workflow. All
Workflow Definition parameters must be serializable.

You can define and pass parameters in your Workflow. In this example, you define your arguments in your `client.ts` file
and pass those parameters to `workflow.ts` through your Workflow function.

Start a Workflow with the parameters that are in the `client.ts` file. In this example we set the `name` parameter to
`Temporal` and `born` to `2019`. Then set the Task Queue and Workflow Id.

`client.ts`

```typescript

...
await client.workflow.start(example, {
  args: [{ name: 'Temporal', born: 2019 }],
  taskQueue: 'your-queue',
  workflowId: 'business-meaningful-id',
});
```

In `workflows.ts` define the type of the parameter that the Workflow function takes in. The interface `ExampleParam` is
a name we can now use to describe the requirement in the previous example. It still represents having the two properties
called `name` and `born` that is of the type `string`. Then define a function that takes in a parameter of the type
`ExampleParam` and return a `Promise<string>`. The `Promise` object represents the eventual completion, or failure, of
`await client.workflow.start()` and its resulting value.

```ts
interface ExampleParam {
  name: string;
  born: number;
}
export async function example({ name, born }: ExampleParam): Promise<string> {
  return `Hello ${name}, you were born in ${born}.`;
}
```

## How to define Workflow return parameters {/* #workflow-return-values */}

Workflow return values must also be serializable. Returning results, returning errors, or throwing exceptions is fairly
idiomatic in each language that is supported. However, Temporal APIs that must be used to get the result of a Workflow
Execution will only ever receive one of either the result or the error.

To return a value of the Workflow function, use `Promise<something>`. The `Promise` is used to make asynchronous calls
and comes with guarantees.

The following example uses a `Promise<string>` to eventually return a `name` and `born` parameter.

```typescript
interface ExampleParam {
  name: string;
  born: number;
}
export async function example({ name, born }: ExampleParam): Promise<string> {
  return `Hello ${name}, you were born in ${born}.`;
}
```

## How to customize your Workflow Type {/* #workflow-type */}

Workflows have a Type that are referred to as the Workflow name.

The following examples demonstrate how to set a custom name for your Workflow Type.

In TypeScript, the Workflow Type is the Workflow function name and there isn't a mechanism to customize the Workflow
Type.

In the following example, the Workflow Type is the name of the function, `helloWorld`.

<!--SNIPSTART typescript-workflow-type -->
[snippets/src/workflows.ts](https://github.com/temporalio/samples-typescript/blob/main/snippets/src/workflows.ts)
```ts
export async function helloWorld(): Promise<string> {
  return '👋 Hello World!';
}
```
<!--SNIPEND-->

## How to develop Workflow logic {/* #workflow-logic-requirements */}

Workflow logic is constrained by [deterministic execution requirements](/workflow-definition#deterministic-constraints).
Each Temporal SDK provides a
set of APIs that can be used inside your Workflow to interact with external (to the Workflow) application code.

In the Temporal TypeScript SDK, Workflows run in a deterministic sandboxed environment. The code is bundled on Worker
creation using Webpack, and can import any package as long as it does not reference Node.js or DOM APIs.

:::note

If you **must** use a library that references a Node.js or DOM API and you are certain that those APIs are not used at
runtime, add that module to the
[ignoreModules](https://typescript.temporal.io/api/interfaces/worker.BundleOptions#ignoremodules) list.

:::

The Workflow sandbox can run only deterministic code, so side effects and access to external state must be done through Activities because Activity outputs are recorded in the Event History and can read be deterministically by the Workflow.

This limitation also means that Workflow code cannot directly import the [Activity Definition](/activity-definition).
[Activity Types](/activity-definition#activity-type) can be imported, so they can be invoked in a type-safe manner.

To make the Workflow runtime deterministic, functions like `Math.random()`, `Date`, and `setTimeout()` are replaced by deterministic versions.

[FinalizationRegistry](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/FinalizationRegistry)
and [WeakRef](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakRef) are removed because v8's garbage collector is not deterministic.

The following sections describe the replay-safe APIs available in the sandbox.

#### Logging

Use [`log`](https://typescript.temporal.io/api/namespaces/workflow#log) from `@temporalio/workflow` instead of `console.log`. The SDK logger automatically suppresses messages during replay to avoid duplicates:

```ts

export async function myWorkflow(name: string): Promise<string> {
  log.info('Starting workflow', { name });
  // ...
}
```

For logger configuration, see [Observability: Log from a Workflow](/develop/typescript/platform/observability#logging).

#### Random numbers and UUIDs

`Math.random()` is replaced by a deterministic version in the sandbox, so you can use it directly. It produces the same sequence of values on replay. UUID libraries that rely on `Math.random()` (such as the `uuid` package) are also safe to use. Avoid `crypto.randomUUID()`, which is not available in the sandbox:

```ts

// Safe - Math.random() is deterministic in the Workflow sandbox
const value = Math.random();
const id = uuid4();
```

#### Current time

`Date.now()` and `new Date()` are replaced by deterministic versions that return the time of the last Workflow Task completion. The value only advances when you `await` something (like `sleep()`):

```ts

// Prints the *exact* same timestamp on every iteration
for (let x = 0; x < 10; ++x) {
  console.log(Date.now());
}

// Prints timestamps increasing roughly 1s each iteration
for (let x = 0; x < 10; ++x) {
  await sleep('1 second');
  console.log(Date.now());
}
```

#### Detecting replay (advanced)

Use [`workflowInfo().unsafe.isReplaying`](https://typescript.temporal.io/api/interfaces/workflow.UnsafeWorkflowInfo#isreplaying) to guard code that should only run on the first execution, such as emitting metrics or sending external notifications from an [Interceptor](/develop/typescript/workers/interceptors).
:::caution

Never use this to affect Workflow business logic — branching on replay status breaks determinism.

:::

```ts

if (!workflowInfo().unsafe.isReplaying) {
  metrics.emit('workflow_started', 1);
}
```

If your goal is to always take action when something new is happening, check that `workflowInfo().unsafe.isReplayingHistoryEvents` is false instead. This will be false during read-only operations like queries and update validators. This is what the SDK's built-in logger uses internally.

---

## Cancellation scopes - TypeScript SDK

## Cancellation scopes in Typescript {/* #cancellation-scopes */}

In the TypeScript SDK, Workflows are represented internally by a tree of cancellation scopes, each with cancellation
