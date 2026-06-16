# Quickstart

Configure your local development environment to get started developing with Temporal.

<SetupSteps>
<SetupStep code={
  <>
    The TypeScript SDK requires Node.js 20 or later.
    Install Node.js via your package manager by following the official Node.js instructions.
  </>
}>
## Install Node.js

The TypeScript SDK requires Node.js 20 or later. Install Node.js via your package manager by following the official
Node.js instructions.

</SetupStep>

<SetupStep code={
<>
<CodeSnippet language="bash">
npx @temporalio/create@latest ./my-app
</CodeSnippet>

When prompted to select a sample, choose the hello-world sample.
</>
}>

## Install the Temporal TypeScript SDK

You can create a new project with the Temporal SDK:

If you're creating a new project using `npx @temporalio/create`, the required SDK packages will be installed
automatically.

To add Temporal to an existing project, install the required packages manually with
`npm install @temporalio/client @temporalio/worker @temporalio/workflow`.

Next, you'll configure a local Temporal Service for development.

</SetupStep>

<SetupStep code={
<>
<Tabs>
<TabItem value="macos" label="macOS" default>

        Install the Temporal CLI using Homebrew:
        <CodeSnippet language="bash">
        brew install temporal
        </CodeSnippet>
      </TabItem>

      <TabItem value="windows" label="Windows">
        Download the Temporal CLI archive for your architecture:

          Windows amd64
          Windows arm64

        Extract it and add <code>temporal.exe</code> to your PATH.
      </TabItem>

      <TabItem value="linux" label="Linux">
        Download the Temporal CLI for your architecture:

          Linux amd64
          Linux arm64

        Extract the archive and move the <code>temporal</code> binary into your PATH, for example:
        <CodeSnippet language="bash">
        sudo mv temporal /usr/local/bin
        </CodeSnippet>
      </TabItem>
    </Tabs>

</>
}>

## Install Temporal CLI

The fastest way to get a development version of the Temporal Service running on your local machine is to use
[Temporal CLI](https://docs.temporal.io/cli).

Choose your operating system to install Temporal CLI.

</SetupStep>

<SetupStep code={
<>

After installing, open a new Terminal window and start the development server:

<CodeSnippet language="bash">temporal server start-dev</CodeSnippet>

Change the Web UI port
The Temporal Web UI may be on a different port in some examples or tutorials. To change the port for the Web UI, use the <code>--ui-port</code> option when starting the server:
<CodeSnippet language="bash">
temporal server start-dev --ui-port 8080
</CodeSnippet>
The Temporal Web UI will now be available at http://localhost:8080.

</>
}>

## Start the development server

Once you've installed Temporal CLI and added it to your PATH, open a new Terminal window and run the following command.

This command starts a local Temporal Service. It starts the Web UI, creates the default Namespace, and uses an in-memory
database.

The Temporal Service will be available on localhost:7233. The Temporal Web UI will be available at
http://localhost:8233.

Leave the local Temporal Service running as you work through tutorials and other projects. You can stop the Temporal
Service at any time by pressing CTRL+C.

Once you have everything installed, you're ready to build apps with Temporal on your local machine.

</SetupStep>
</SetupSteps>

## Run Hello World: Test Your Installation

Now let's verify your setup is working by creating and running a complete Temporal application with both a Workflow and
Activity.

This test will confirm that:

- The Temporal TypeScript SDK is properly installed
- Your local Temporal Service is running
- You can successfully create and execute Workflows and Activities
- The communication between components is functioning correctly

### 1. Create the Activity

Create an Activity file (activities.ts):

```ts
export async function greet(name: string): Promise<string> {
  return `Hello, ${name}!`;
}
```

An Activity is a normal function or method that executes a single, well-defined action (either short or long running),
which often involve interacting with the outside world, such as sending emails, making network requests, writing to a
database, or calling an API, which are prone to failure. If an Activity fails, Temporal automatically retries it based
on your configuration.

### 2. Create the Workflow

Create a Workflow file (workflows.ts):

```ts

// Only import the activity types

const { greet } = proxyActivities<typeof activities>({
  startToCloseTimeout: '1 minute',
});

/** A workflow that simply calls an activity */
export async function example(name: string): Promise<string> {
  return await greet(name);
}
```

Workflows orchestrate Activities and contain the application logic. Temporal Workflows are resilient. They can run and
keep running for years, even if the underlying infrastructure fails. If the application itself crashes, Temporal will
automatically recreate its pre-failure state so it can continue right where it left off.

### 3. Create and Run the Worker

Create a Worker file (worker.ts):

```ts

async function run() {
  // Step 1: Establish a connection with Temporal server.
  //
  // Worker code uses `@temporalio/worker.NativeConnection`.
  // (But in your application code it's `@temporalio/client.Connection`.)
  const connection = await NativeConnection.connect({
    address: 'localhost:7233',
    // TLS and gRPC metadata configuration goes here.
  });
  try {
    // Step 2: Register Workflows and Activities with the Worker.
    const worker = await Worker.create({
      connection,
      namespace: 'default',
      taskQueue: 'hello-world',
      // Workflows are registered using a path as they run in a separate JS context.
      workflowsPath: require.resolve('./workflows'),
      activities,
    });

    // Step 3: Start accepting tasks on the `hello-world` queue
    //
    // The worker runs until it encounters an unexpected error or the process receives a shutdown signal registered on
    // the SDK Runtime object.
    //
    // By default, worker logs are written via the Runtime logger to STDERR at INFO level.
    //
    // See https://typescript.temporal.io/api/classes/worker.Runtime#install to customize these defaults.
    await worker.run();
  } finally {
    // Close the connection once the worker has stopped
    await connection.close();
  }
}

run().catch((err) => {
  console.error(err);
  process.exit(1);
});
```

Run the Worker and keep this terminal running:

```bash
npm run start
```

With your Activity and Workflow defined, you need a Worker to execute them. A Worker polls a Task Queue, that you
configure it to poll, looking for work to do. Once the Worker dequeues a Workflow or Activity task from the Task Queue,
it then executes that task.

Workers are a crucial part of your Temporal application as they're what actually execute the tasks defined in your
Workflows and Activities. For more information on Workers, see
[Understanding Temporal](/evaluate/understanding-temporal#workers) and a [deep dive into Workers](/workers).

### 4. Execute the Workflow

Now that your Worker is running, it's time to start a Workflow Execution.

This final step will validate that everything is working correctly with your file labeled `client.ts`.

Create a separate file called `client.ts`.

```ts

async function run() {
  // Connect to the default Server location
  const connection = await Connection.connect({ address: 'localhost:7233' });
  // In production, pass options to configure TLS and other settings:
  // {
  //   address: 'foo.bar.tmprl.cloud',
  //   tls: {}
  // }

  const client = new Client({
    connection,
    // namespace: 'foo.bar', // connects to 'default' namespace if not specified
  });

  const handle = await client.workflow.start(example, {
    taskQueue: 'hello-world',
    // type inference works! args: [name: string]
    args: ['Temporal'],
    // in practice, use a meaningful business ID, like customerId or transactionId
    workflowId: 'workflow-' + nanoid(),
  });
  console.log(`Started workflow ${handle.workflowId}`);

  // optional: wait for client result
  console.log(await handle.result()); // Hello, Temporal!
}

run().catch((err) => {
  console.error(err);
  process.exit(1);
});
```

Then run:

```bash
npm run workflow
```

### Verify Success

If everything is working correctly, you should see:

- Worker processing the workflow and activity
- Output: `Workflow result: Hello, Temporal!`
- Workflow Execution details in the [Temporal Web UI](http://localhost:8233)

<details>
<summary>Additional details about Workflow Execution</summary>

- Temporal clients are not explicitly closed.
- To enable TLS, set the `tls` option to `true` for default settings or pass a [`TLSConfig`](https://typescript.temporal.io/api/interfaces/worker.TLSConfig) for custom configuration.
- Calling `client.workflow.start()` and `client.workflow.execute()` send a command to Temporal Server to schedule a new
  Workflow Execution on the specified Task Queue.
- If you started a Workflow with `client.workflow.start()`, you can choose to wait for the result anytime with
  handle.result().
- Using a Workflow Handle isn't necessary with `client.workflow.execute()`.

</details>

<CallToAction href="https://learn.temporal.io/getting_started/typescript/first_program_in_typescript/">
  Run your first Temporal Application
  Create a basic Workflow and run it with the Temporal TypeScript SDK
</CallToAction>

<CallToAction href="https://learn.temporal.io/courses/">
  Take a Temporal 101 course
  Learn Temporal concepts and build your first application with a guided course
</CallToAction>

---

## Worker Versioning (Legacy) - Typescript SDK

## How to use Worker Versioning in TypeScript (Deprecated) {/* #worker-versioning */}

:::caution

This section is for a deprecated Worker Versioning API. Please redirect your attention to [Worker Versioning](/production-deployment/worker-deployments/worker-versioning).

See the [Pre-release README](https://github.com/temporalio/temporal/blob/main/docs/worker-versioning.md) for more information.

:::

A Build ID corresponds to a deployment. If you don't already have one, we recommend a hash of the code--such as a Git SHA--combined with a human-readable timestamp.
To use Worker Versioning, you need to pass a Build ID to your Typescript Worker and opt in to Worker Versioning.

### Assign a Build ID to your Worker and opt in to Worker Versioning

You should understand assignment rules before completing this step.
See the [Worker Versioning Pre-release README](https://github.com/temporalio/temporal/blob/main/docs/worker-versioning.md) for more information.

To enable Worker Versioning for your Worker, assign the Build ID--perhaps from an environment variable--and turn it on.

```typescript
// ...
const worker = await Worker.create({
  taskQueue: 'your_task_queue_name',
  buildId: buildId,
  useVersioning: true,
  // ...
});
// ...
```

:::warning

Importantly, when you start this Worker, it won't receive any tasks until you set up assignment rules.

:::

### Specify versions for Activities, Child Workflows, and Continue-as-New Workflows

:::caution

This section is for a deprecated Worker Versioning API. Please redirect your attention to [Worker Versioning](/production-deployment/worker-deployments/worker-versioning).

:::

By default, Activities, Child Workflows, and Continue-as-New Workflows are run on the build of the Workflow that created them if they are also configured to run on the same Task Queue.
When configured to run on a separate task queue, they will default to using the current assignment rules.

If you want to override this behavior, you can specify your intent via the `versioningIntent`
field available on the options object for each of these commands.

For example, if you want an Activity to use the latest assignment rules rather than inheriting from its parent:

```typescript
// ...
const { echo } = proxyActivities<typeof activities>({
  startToCloseTimeout: '20s',
  versioningIntent: 'USE_ASSIGNMENT_RULES',
});
// ...
```

### Tell the Task Queue about your Worker's Build ID (Deprecated)

:::caution

This section is for a deprecated Worker Versioning API. Please redirect your attention to [Worker Versioning](/production-deployment/worker-deployments/worker-versioning).

:::

Now you can use the SDK (or the Temporal CLI) to tell the Task Queue about your Worker's Build ID.
You might want to do this as part of your CI deployment process.

```typescript
// ...
await client.taskQueue.updateBuildIdCompatibility('your_task_queue_name', {
  operation: 'addNewIdInNewDefaultSet',
  buildId: 'deadbeef',
});
```

This code adds the `deadbeef` Build ID to the Task Queue as the sole version in a new version set, which becomes the default for the queue.
New Workflows execute on Workers with this Build ID, and existing ones will continue to process by appropriately compatible Workers.

If, instead, you want to add the Build ID to an existing compatible set, you can do this:

```typescript
// ...
await client.taskQueue.updateBuildIdCompatibility('your_task_queue_name', {
  operation: 'addNewCompatibleVersion',
  buildId: 'deadbeef',
  existingCompatibleBuildId: 'some-existing-build-id',
});
```

This code adds `deadbeef` to the existing compatible set containing `some-existing-build-id` and marks it as the new default Build ID for that set.

You can promote an existing Build ID in a set to be the default for that set:

```typescript
// ...
await client.taskQueue.updateBuildIdCompatibility('your_task_queue_name', {
  operation: 'promoteBuildIdWithinSet',
  buildId: 'deadbeef',
});
```

You can promote an entire set to become the default set for the queue. New Workflows will start using that set's default build.

```typescript
// ...
await client.taskQueue.updateBuildIdCompatibility('your_task_queue_name', {
  operation: 'promoteSetByBuildId',
  buildId: 'deadbeef',
});
```

You can merge two sets into one, preserving the primary set's default Build ID as the default
for the merged set.

```typescript
// ...
await client.taskQueue.updateBuildIdCompatibility('your_task_queue_name', {
  operation: 'mergeSets',
  primaryBuildId: 'deadbeef',
  secondaryBuildId: 'some-existing-build-id',
});
```

---

## Workers - TypeScript SDK

![TypeScript SDK Banner](/img/assets/banner-typescript-temporal.png)

## Workers

- [Worker processes](/develop/typescript/workers/run-worker-process)
- [Interceptors](/develop/typescript/workers/interceptors)

---

## Manage Interceptors - TypeScript SDK

Interceptors are SDK hooks that let you intercept inbound and outbound Temporal calls. You use them to apply shared
behavior across many calls, such as tracing and authorization, before calls reach the application code and after they return.
This is similar to middleware in other frameworks.

There are two main types of interceptors--inbound and outbound.

* Outbound interceptors wrap network calls, running before they reach the network and after they return.
* Inbound interceptors run after the network hop, wrapping application code and running before it starts and after it returns.

Those further break down into concrete Interceptor types--see below.

## How to implement interceptors in TypeScript {/* #interceptors */}

Interceptors run as a chain.  Each interceptor wraps the entire inner call: your code runs before the call, invokes `next` to execute the rest of the chain, and then runs after the call completes. This means you can inspect or modify both the `input` and the result, handle errors, and perform side effects at either stage.

The TypeScript SDK comes with an optional interceptor package that adds tracing with
[OpenTelemetry](https://www.npmjs.com/package/@temporalio/interceptors-opentelemetry). See how to use it in the
[interceptors-opentelemetry](https://github.com/temporalio/samples-typescript/tree/main/interceptors-opentelemetry) code
sample.

- [WorkflowInboundCallsInterceptor](https://typescript.temporal.io/api/interfaces/workflow.WorkflowInboundCallsInterceptor/):
  Intercept Workflow inbound calls like execution, Signals, and Queries.
- [WorkflowOutboundCallsInterceptor](https://typescript.temporal.io/api/interfaces/workflow.WorkflowOutboundCallsInterceptor/):
  Intercept Workflow outbound calls to Temporal APIs like scheduling Activities and starting Timers.
- [ActivityInboundCallsInterceptor](https://typescript.temporal.io/api/interfaces/worker.ActivityInboundCallsInterceptor):
  Intercept inbound calls to an Activity (such as `execute`).
- [WorkflowClientInterceptor](https://typescript.temporal.io/api/interfaces/client.WorkflowClientInterceptor/):
  Intercept workflow-related methods of [`Client`](https://typescript.temporal.io/api/classes/client.Client/) and
  [`WorkflowHandle`](https://typescript.temporal.io/api/interfaces/client.WorkflowHandle) like starting or signaling a
  Workflow.
- [NexusInboundCallsInterceptor](https://typescript.temporal.io/api/interfaces/worker.NexusInboundCallsInterceptor):
  Intercept inbound Nexus Operation calls like `startOperation` and `cancelOperation`.
- [NexusOutboundCallsInterceptor](https://typescript.temporal.io/api/interfaces/worker.NexusOutboundCallsInterceptor):
  Intercept outbound calls from Nexus Operations, such as enriching log attributes and metric tags.

All interceptor methods are optional—it's up to the implementor to choose which methods to intercept.

## Interceptor examples

**Log start and completion of Activities**

```ts

export class ActivityLogInterceptor implements WorkflowOutboundCallsInterceptor {
  constructor(public readonly workflowType: string) {}

  async scheduleActivity(
    input: ActivityInput,
    next: Next<WorkflowOutboundCallsInterceptor, 'scheduleActivity'>
  ): Promise<unknown> {
    console.log('Starting activity', { activityType: input.activityType });
    try {
      return await next(input);
    } finally {
      console.log('Completed activity', {
        workflow: this.workflowType,
        activityType: input.activityType,
      });
    }
  }
}
```

**Log Nexus Operations**

```ts

  NexusInboundCallsInterceptor,
  NexusStartOperationInput,
  NexusStartOperationOutput,
  Next,
} from '@temporalio/worker';

export class NexusOperationLogInterceptor implements NexusInboundCallsInterceptor {
  async startOperation(
    input: NexusStartOperationInput,
    next: Next<NexusInboundCallsInterceptor, 'startOperation'>
  ): Promise<NexusStartOperationOutput> {
    console.log('Starting Nexus operation', {
      service: input.ctx.service,
      operation: input.ctx.operation,
    });
    const output = await next(input);
    console.log('Nexus operation started', {
      service: input.ctx.service,
      operation: input.ctx.operation,
      async: output.result.isAsync,
    });
    return output;
  }
}
```

## Register an Interceptor {/* #register-interceptor */}

Registering an interceptor means providing it to the SDK so Temporal can invoke it when matching Client or Worker calls occur. Once registered, it runs in the call path and can observe or modify request and response data.

### Register via a Plugin

If you're building a reusable library or want to bundle interceptors with other primitives, you can register them
through a [Plugin](/develop/plugins-guide#interceptors).

### Activity and client interceptors registration

- Activity interceptors are registered on Worker creation by passing an array of
  [ActivityInboundCallsInterceptor factory functions](https://typescript.temporal.io/api/interfaces/worker.ActivityInboundCallsInterceptorFactory)
  through [WorkerOptions](https://typescript.temporal.io/api/interfaces/worker.WorkerOptions#interceptors).

- Client interceptors are registered on `Client` construction by passing an array of
  [WorkflowClientInterceptor](https://typescript.temporal.io/api/interfaces/client.WorkflowClientInterceptor) via
  [ClientOptions.interceptors](https://typescript.temporal.io/api/interfaces/client.ClientOptions#interceptors).

### Workflow interceptors registration

Workflow interceptor registration is different from the other interceptors because they run in the Workflow isolate. To
register Workflow interceptors, export an `interceptors` function from a file located in the `workflows` directory and
provide the name of that file to the Worker on creation via
[WorkerOptions](https://typescript.temporal.io/api/interfaces/worker.WorkerOptions#interceptors).

At the time of construction, the Workflow context is already initialized for the current Workflow. You may call the
[`workflowInfo()`](https://typescript.temporal.io/api/namespaces/workflow#workflowinfo) function to access
Workflow-specific information from an interceptor.

`src/workflows/your-interceptors.ts`

```ts

export const interceptors = () => ({
  outbound: [new ActivityLogInterceptor(workflowInfo().workflowType)],
  inbound: [],
});
```

`src/worker/index.ts`

```ts
const worker = await Worker.create({
  workflowsPath: require.resolve('./workflows'),
  interceptors: {
    workflowModules: [require.resolve('./workflows/your-interceptors')],
  },
});
```

### Nexus interceptor registration

Nexus interceptors are registered on Worker creation via
[WorkerOptions](https://typescript.temporal.io/api/interfaces/worker.WorkerOptions#interceptors).
Pass an array of factory functions to `interceptors.nexus`.
Each factory receives an [`OperationContext`](https://typescript.temporal.io/api/classes/nexus.OperationContext) and returns an object with optional `inbound` and `outbound` interceptors.

`src/worker/index.ts`

```ts

const worker = await Worker.create({
  // ...
  nexusServices: [/* your Nexus services */],
  interceptors: {
    nexus: [
      (_ctx) => ({
        inbound: new NexusOperationLogInterceptor(),
      }),
    ],
  },
});
```

---

## Worker processes - TypeScript SDK

## How to run Worker Processes {/* #run-a-dev-worker */}

The [Worker Process](/workers#worker-process) is where Workflow Functions and Activity Functions are executed.

- Each [Worker Entity](/workers#worker-entity) in the Worker Process must register the exact Workflow Types and Activity
  Types it may execute.
- Each Worker Entity must also associate itself with exactly one [Task Queue](/task-queue).
- Each Worker Entity polling the same Task Queue must be registered with the same Workflow Types and Activity Types.

A [Worker Entity](/workers#worker-entity) is the component within a Worker Process that listens to a specific Task
Queue.

Although multiple Worker Entities can be in a single Worker Process, a single Worker Entity Worker Process may be
perfectly sufficient. For more information, see the [Worker tuning guide](/develop/worker-performance).

A Worker Entity contains a Workflow Worker and/or an Activity Worker, which makes progress on Workflow Executions and
Activity Executions, respectively.

## How to run a Worker on Docker in TypeScript {/* #run-a-worker-on-docker */}

:::note

To improve worker startup time, we recommend preparing workflow bundles ahead-of-time. See our
[productionsample](https://github.com/temporalio/samples-typescript/tree/main/production) for details.

:::

Workers based on the TypeScript SDK can be deployed and run as Docker containers.

We recommend an LTS Node.js release such as 18, 20, 22, or 24. Both `amd64` and `arm64` architectures are supported. A
glibc-based image is required; musl-based images are _not_ supported (see below).

The easiest way to deploy a TypeScript SDK Worker on Docker is to start with the `node:20-bullseye` image. For example:

```dockerfile
FROM node:20-bullseye
