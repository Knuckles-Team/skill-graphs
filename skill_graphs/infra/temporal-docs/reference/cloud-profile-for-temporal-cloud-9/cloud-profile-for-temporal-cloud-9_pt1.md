# Cloud profile for Temporal Cloud
[profile.staging]
address = "your-namespace.a1b2c.tmprl.cloud:7233"
namespace = "your-namespace"
api_key = "your-api-key-here"
```

Use the `loadClientConnectConfig` helper from `@temporalio/envconfig` to load the `staging` profile from the
configuration file and create a `NativeConnection` object as follows:

```ts {1,15,17}

async function main() {
  const configFile = resolve(__dirname, '../config.toml');
  const profileName = 'staging'

  // Load the 'staging' profile.
  const config = loadClientConnectConfig({
    profile: profileName,
    configSource: { path: configFile },
  });

  const connection = await NativeConnection.connect(config.connectionOptions);

  const worker = await Worker.create({
    connection,
    namespace: <namespace_id>.<account_id>,
    // ...
});
}
```

</TabItem>

<TabItem value="env-vars" label="Environment Variables">

Ensure you have set the necessary environment variables to connect to Temporal Cloud. For example:

```bash
export TEMPORAL_NAMESPACE="your-namespace.your-account-id"
export TEMPORAL_ADDRESS="your-namespace.a1b2c.tmprl.cloud:7233"
export TEMPORAL_TLS_CLIENT_CERT_PATH="/path/to/your/client/cert.pem"
export TEMPORAL_TLS_CLIENT_KEY_PATH="/path/to/your/client/key.pem"
```

After setting the environment variables, use the following code to create a `NativeConnection` object using the
`loadClientConnectConfig` helper from `@temporalio/envconfig`:

```ts {1,5}

async function main() {
  const config = loadClientConnectConfig();

  const connection = await NativeConnection.connect(config.connectionOptions);

  const worker = await Worker.create({
    connection,
    namespace: process.env.TEMPORAL_NAMESPACE,
    // ...
  });
}
```

</TabItem>

<TabItem value="code" label="Code">

You can also provide connections options in your TypeScript code directly. To create an initial connection, provide the
connections to the ` NativeConnection.connect` method, and then pass the resulting `NativeConnection` object to
`Worker.create()` when creating the Worker:

```ts {1,4,9}

const connection = await NativeConnection.connect({
    address: <endpoint>,
    tls: true,
    apiKey: <APIKey>,
});
const worker = await Worker.create({
    connection,
    namespace: <namespace_id>.<account_id>,
    // ...
});
```

</TabItem>

</Tabs>

## NativeConnection, Connection, and Client

`NativeConnection`, `Connection`, and `Client` are all classes provided by the TypeScript SDK to facilitate
communication with the Temporal Service. This section explains the differences between these classes and their
respective use cases. For detailed information about each class, refer to the
[Temporal TypeScript API documentation](https://typescript.temporal.io/api/namespaces/client).

### NativeConnection vs. Connection {/* #native-connection-vs-connection */}

The TypeScript SDK provides two types of connection classes to connect to the Temporal Service: `NativeConnection` and
`Connection`. The `NativeConnection` class is used to connect from a Worker, while the `Connection` class is used to
connect from a Temporal Application or from within an Activity, typically through a `Client` object. Both connection
classes accept the same set of connection options.

### Connection vs. Client {/* #connection-vs-client */}

A `Client` object is a high-level, lightweight abstraction that simplifies interaction with the Temporal Service. It
internally manages a `Connection` object to handle the low-level communication details. The `Client` class provides
convenient methods for common operations such as starting Workflow Executions, sending Signals and Queries, and
retrieving Workflow results.

A `Connection` object is a lower-level and expensive object that represents a direct connection to the Temporal Service.
You pass in a `Connection` object to the `Client` constructor to create a `Client` instance. Since a `Connection` is
expensive to create, create a single `Connection` object and reuse it across your application whenever possible.

When instantiating a `Connection`, you specify most connection options except for the Namespace, such as the Temporal
Service endpoint, TLS settings, and authentication credentials. When instantiating a `Client`, you provide the
`Connection` object and the Namespace you want to connect to, along with other client options.

## Start Workflow Execution {/* #start-workflow-execution */}

**How to start a Workflow Execution using the Typescript SDK**

[Workflow Execution](/workflow-execution) semantics rely on several parameters—that is, to start a Workflow Execution
you must supply a Task Queue that will be used for the Tasks (one that a Worker is polling), the Workflow Type,
language-specific contextual data, and Workflow Function parameters.

In the examples below, all Workflow Executions are started using a Temporal Client. To spawn Workflow Executions from
within another Workflow Execution, use either the Child Workflow or External Workflow APIs.

See the [Customize Workflow Type](/develop/typescript/workflows/basics#workflow-type) section to see how to customize
the name of the Workflow Type.

A request to spawn a Workflow Execution causes the Temporal Service to create the first Event
([WorkflowExecutionStarted](/references/events#workflowexecutionstarted)) in the Workflow Execution Event History. The
Temporal Service then creates the first Workflow Task, resulting in the first
[WorkflowTaskScheduled](/references/events#workflowtaskscheduled) Event.

When you have a Client, you can schedule the start of a Workflow with `client.workflow.start()`, specifying
`workflowId`, `taskQueue`, and `args` and returning a Workflow handle immediately after the Server acknowledges the
receipt.

```typescript
const handle = await client.workflow.start(example, {
  workflowId: 'your-workflow-id',
  taskQueue: 'your-task-queue',
  args: ['argument01', 'argument02', 'argument03'], // this is typechecked against workflowFn's args
});
const handle = client.getHandle(workflowId);
const result = await handle.result();
```

Calling `client.workflow.start()` and `client.workflow.execute()` send a command to Temporal Server to schedule a new
Workflow Execution on the specified Task Queue. It does not actually start until a Worker that has a matching Workflow
Type, polling that Task Queue, picks it up.

You can test this by executing a Client command without a matching Worker. Temporal Server records the command in Event
History, but does not make progress with the Workflow Execution until a Worker starts polling with a matching Task Queue
and Workflow Definition.

Workflow Execution run in a separate V8 isolate context in order to provide a
[deterministic runtime](/workflow-definition#deterministic-constraints).

### Set a Workflow's Task Queue {/* #set-task-queue */}

In most SDKs, the only Workflow Option that must be set is the name of the [Task Queue](/task-queue).

For any code to execute, a Worker Process must be running that contains a Worker Entity that is polling the same Task
Queue name.

A Task Queue is a dynamic queue in Temporal polled by one or more Workers.

Workers bundle Workflow code and node modules using Webpack v5 and execute them inside V8 isolates. Activities are
directly required and run by Workers in the Node.js environment.

Workers are flexible. You can host any or all of your Workflows and Activities on a Worker, and you can host multiple
Workers on a single machine.

The Worker needs three main things:

- `taskQueue`: The Task Queue to poll. This is the only required argument.
- `activities`: Optional. Imported and supplied directly to the Worker.
- Workflow bundle. Choose one of the following options:
  - Specify `workflowsPath` pointing to your `workflows.ts` file to pass to Webpack; for example,
    `require.resolve('./workflows')`. Workflows are bundled with their dependencies.
  - If you prefer to handle the bundling yourself, pass a prebuilt bundle to `workflowBundle`.

```ts

async function run() {
  // Step 1: Register Workflows and Activities with the Worker and connect to
  // the Temporal server.
  const worker = await Worker.create({
    workflowsPath: require.resolve('./workflows'),
    activities,
    taskQueue: 'hello-world',
  });
  // Worker connects to localhost by default and uses console.error for logging.
  // Customize the Worker by passing more options to create():
  // https://typescript.temporal.io/api/classes/worker.Worker
  // If you need to configure server connection parameters, see docs:
  // /typescript/security#encryption-in-transit-with-mtls

  // Step 2: Start accepting tasks on the `tutorial` queue
  await worker.run();
}

run().catch((err) => {
  console.error(err);
  process.exit(1);
});
```

`taskQueue` is the only required option; however, use `workflowsPath` and `activities` to register Workflows and
Activities with the Worker.

When scheduling a Workflow, you must specify `taskQueue`.

```ts

// This is the code that is used to start a Workflow.
const connection = await Connection.create();
const client = new Client({ connection });
const result = await client.workflow.execute(yourWorkflow, {
  // required
  taskQueue: 'your-task-queue',
  // required
  workflowId: 'your-workflow-id',
});
```

When creating a Worker, you must pass the `taskQueue` option to the `Worker.create()` function.

```ts
const worker = await Worker.create({
  // imported elsewhere
  activities,
  taskQueue: 'your-task-queue',
});
```

Optionally, in Workflow code, when calling an Activity, you can specify the Task Queue by passing the `taskQueue` option
to `proxyActivities()`, `startChild()`, or `executeChild()`. If you do not specify `taskQueue`, the TypeScript SDK
places Activity and Child Workflow Tasks in the same Task Queue as the Workflow Task Queue.

### Set a Workflow Id {/* #workflow-id */}

Although it is not required, we recommend providing your own
[Workflow Id](/workflow-execution/workflowid-runid#workflow-id) that maps to a business process or business entity
identifier, such as an order identifier or customer identifier.

Connect to a Client with `client.workflow.start()` and any arguments. Then specify your `taskQueue` and set your
`workflowId` to a meaningful business identifier.

```typescript
const handle = await client.workflow.start(example, {
  workflowId: 'yourWorkflowId',
  taskQueue: 'yourTaskQueue',
  args: ['your', 'arg', 'uments'],
});
```

This starts a new Client with the given Workflow Id, Task Queue name, and an argument.

### Get the results of a Workflow Execution {/* #get-workflow-results */}

If the call to start a Workflow Execution is successful, you will gain access to the Workflow Execution's Run Id.

The Workflow Id, Run Id, and Namespace may be used to uniquely identify a Workflow Execution in the system and get its
result.

It's possible to both block progress on the result (synchronous execution) or get the result at some other point in time
(asynchronous execution).

In the Temporal Platform, it's also acceptable to use Queries as the preferred method for accessing the state and
results of Workflow Executions.

To return the results of a Workflow Execution:

```typescript
return 'Completed ' + wf.workflowInfo().workflowId + ', Total Charged: ' + totalCharged;
```

`totalCharged` is just a function declared in your code. For a full example, see
[subscription-workflow-project-template-typescript/src/workflows.ts](https://github.com/temporalio/subscription-workflow-project-template-typescript/blob/main/src/workflows.ts).

A Workflow function may return a result. If it doesn’t (in which case the return type is `Promise<void>`), the result
will be `undefined`.

If you started a Workflow with `client.workflow.start()`, you can choose to wait for the result anytime with
`handle.result()`.

```typescript
const handle = client.getHandle(workflowId);
const result = await handle.result();
```

Using a Workflow Handle isn't necessary with `client.workflow.execute()`.

Workflows that prematurely end will throw a `WorkflowFailedError` if you call `result()`.

If you call `result()` on a Workflow that prematurely ended for some reason, it throws a
[`WorkflowFailedError` error](https://typescript.temporal.io/api/classes/client.WorkflowFailedError/) that reflects the
reason. For that reason, it is recommended to catch that error.

```typescript
const handle = client.getHandle(workflowId);
try {
  const result = await handle.result();
} catch (err) {
  if (err instanceof WorkflowFailedError) {
    throw new Error('Temporal workflow failed: ' + workflowId, {
      cause: err,
    });
  } else {
    throw new Error('error from Temporal workflow ' + workflowId, {
      cause: err,
    });
  }
}
```

---

## TypeScript SDK developer guide

![TypeScript SDK Banner](/img/assets/banner-typescript-temporal.png)

## Install and get started

You can find detailed installation instructions for the TypeScript SDK in the [Quickstart](/develop/typescript/set-up-your-local-typescript).

There's also a short walkthrough of how to use the Temporal primitives (Activities, Workflows, and Workers) to build and run a Temporal application to get you up and running.

Once your local Temporal Service is set up, continue building with the following resources:

- [Develop a Workflow](/develop/typescript/workflows/basics)
- [Develop an Activity](/develop/typescript/activities/basics)
- [Start an Activity execution](/develop/typescript/activities/execution)
- [Run Worker processes](/develop/typescript/workers/run-worker-process)

## [Workflows](/develop/typescript/workflows)

- [Workflow basics](/develop/typescript/workflows/basics)
- [Child Workflows](/develop/typescript/workflows/child-workflows)
- [Continue-As-New](/develop/typescript/workflows/continue-as-new)
- [Message passing](/develop/typescript/workflows/message-passing)
- [Cancellation](/develop/typescript/workflows/cancellation)
- [Cancellation scopes](/develop/typescript/workflows/cancellation-scopes)
- [Timeouts](/develop/typescript/workflows/timeouts)
- [Schedules](/develop/typescript/workflows/schedules)
- [Timers](/develop/typescript/workflows/timers)
- [Versioning](/develop/typescript/workflows/versioning)

## [Activities](/develop/typescript/activities)

- [Activity basics](/develop/typescript/activities/basics)
- [Activity execution](/develop/typescript/activities/execution)
- [Timeouts](/develop/typescript/activities/timeouts)
- [Asynchronous Activity](/develop/typescript/activities/asynchronous-activity)
- [Benign exceptions](/develop/typescript/activities/benign-exceptions)

## [Workers](/develop/typescript/workers)

- [Worker processes](/develop/typescript/workers/run-worker-process)
- [Interceptors](/develop/typescript/workers/interceptors)

## [Temporal Client](/develop/typescript/client)

- [Temporal Client](/develop/typescript/client/temporal-client)
- [Namespaces](/develop/typescript/client/namespaces)

## [Temporal Nexus](/develop/typescript/nexus)

- [Quickstart](/develop/typescript/nexus/quickstart)
- [Feature guide](/develop/typescript/nexus/feature-guide)

## [Platform](/develop/typescript/platform)

- [Observability](/develop/typescript/platform/observability)
- [Enriching the UI](/develop/typescript/platform/enriching-ui)

## [Best practices](/develop/typescript/best-practices)

- [Testing](/develop/typescript/best-practices/testing-suite)
- [Debugging](/develop/typescript/best-practices/debugging)
- [Converters and encryption](/develop/typescript/converters-and-encryption)
- [Entity pattern](/develop/typescript/best-practices/entity-pattern)

## [Vercel AI SDK Integration](/develop/typescript/integrations/ai-sdk)

Integrate the Vercel AI SDK with Temporal to build durable AI agents and AI-powered applications.

- [Vercel AI SDK Integration](/develop/typescript/integrations/ai-sdk)

## Temporal TypeScript Technical Resources

- [TypeScript SDK Quickstart - Setup Guide](/develop/typescript/set-up-your-local-typescript)
- [TypeScript API Documentation](https://typescript.temporal.io)
- [TypeScript SDK Code Samples](https://github.com/temporalio/samples-typescript)
- [TypeScript SDK GitHub](https://github.com/temporalio/sdk-typescript)
- [Temporal 101 in TypeScript Free Course](https://learn.temporal.io/courses/temporal_101/typescript/)

### Get Connected with the Temporal TypeScript Community

- [Temporal TypeScript Community Slack](https://temporalio.slack.com/archives/C01DKSMU94L)
- [TypeScript SDK Forum](https://community.temporal.io/tag/typescript-sdk)

## Linting and types in TypeScript {/* #linting-and-types */}

If you started your project with `@temporalio/create`, you already have our recommended TypeScript and ESLint
configurations.

If you incrementally added Temporal to an existing app, we do recommend setting up linting and types because they help catch bugs well before you ship them to production, and they improve your development feedback loop. Take a look at our recommended [.eslintrc](https://github.com/temporalio/samples-typescript/blob/main/.shared/.eslintrc.js) file and tweak to suit your needs.

---

## Install the TypeScript SDK

## How to install a Temporal SDK {/* #install-a-temporal-sdk */}

A [Temporal SDK](/encyclopedia/temporal-sdks) provides a framework for
[Temporal Application](/temporal#temporal-application) development.

An SDK provides you with the following:

- A [Temporal Client](/encyclopedia/temporal-sdks#temporal-client) to communicate with a
  [Temporal Service](/temporal-service).
- APIs to develop [Workflows](/workflows).
- APIs to create and manage [Worker Processes](/workers#worker).
- APIs to author [Activities](/activity-definition).

[![NPM](https://img.shields.io/npm/v/temporalio.svg?style=for-the-badge)](https://www.npmjs.com/search?q=author%3Atemporal-sdk-team)

This project requires Node.js 18 or later.

**Create a project**

```bash
npx @temporalio/create@latest ./your-app
```

**Add to an existing project**

```bash
npm install @temporalio/client @temporalio/worker @temporalio/workflow @temporalio/activity @temporalio/common
```

:::note

The TypeScript SDK is designed with TypeScript-first developer experience in mind, but it works equally well with
JavaScript.

:::

### How to find the TypeScript SDK API reference {/* #api-reference */}

The Temporal TypeScript SDK API reference is published to [typescript.temporal.io](https://typescript.temporal.io).

### Where are SDK-specific code examples? {/* #code-samples */}

You can find a complete list of executable code samples in
[Temporal's GitHub repository](https://github.com/temporalio?q=samples-&type=all&language=&sort=).

Additionally, several of the [Tutorials](https://learn.temporal.io) are backed by a fully executable template
application.

Use the [TypeScript samples library](https://github.com/temporalio/samples-typescript) stored on GitHub to demonstrate
various capabilities of Temporal.

**Where can I find video demos?**

[Temporal TypeScript YouTube playlist](https://www.youtube.com/playlist?list=PLl9kRkvFJrlTavecydpk9r6cF7qBmQJvb).

### How to import an ECMAScript module {/* #ecmascript-modules */}

The JavaScript ecosystem is quickly moving toward publishing ECMAScript modules (ESM) instead of CommonJS modules. For
example, `node-fetch@3` is ESM, but `node-fetch@2` is CommonJS.

For more information about importing a pure ESM dependency, see our
[Fetch ESM](https://github.com/temporalio/samples-typescript/tree/main/fetch-esm) sample for the necessary configuration
changes:

- `package.json` must have include the `"type": "module"` attribute.
- `tsconfig.json` should output in `esnext` format.
- Imports must include the `.js` file extension.

## Linting and types in TypeScript {/* #linting-and-types */}

If you started your project with `@temporalio/create`, you already have our recommended TypeScript and ESLint
configurations.

If you incrementally added Temporal to an existing app, we do recommend setting up linting and types because they help
catch bugs well before you ship them to production, and they improve your development feedback loop. Take a look at our
recommended [.eslintrc](https://github.com/temporalio/samples-typescript/blob/main/.shared/.eslintrc.js) file and tweak
to suit your needs.

---

## AI SDK by Vercel integration

Temporal's integration with [Vercel's AI SDK](https://ai-sdk.dev/) lets you use the AI SDK's API directly in Workflow
code while Temporal handles Durable Execution.

Like all API calls, LLM API calls are non-deterministic. In a [Temporal Application](/glossary#temporal-application),
that means you cannot make LLM calls directly from a [Workflow](/glossary#workflow); they must run as
[Activities](/glossary#activity). The AI SDK plugin handles this automatically: when you call methods in the AI SDK such
as `generateText()`, the plugin wraps those calls in Activities behind the scenes. This preserves the Vercel AI SDK's
developer experience that you are already familiar with while Temporal handles Durable Execution for you.

All code snippets in this guide are taken from the TypeScript SDK
[ai-sdk samples](https://github.com/temporalio/samples-typescript/tree/main/ai-sdk). Refer to the samples for the
complete code and run them locally.

<ReleaseNoteHeader type="publicPreview" />

## Prerequisites

- This guide assumes you are already familiar with the Vercel AI SDK. If you aren't, refer to the
  [Vercel AI SDK documentation](https://ai-sdk.dev/) for more details.
- If you are new to Temporal, we also recommend you read the [Understanding Temporal](/evaluate/understanding-temporal)
  document or take the [Temporal 101](https://learn.temporal.io/courses/temporal_101/) course to understand the basics
  of Temporal.
- Ensure you have set up your local development environment by following the
  [Set up your local with the TypeScript SDK](/develop/typescript/set-up-your-local-typescript) guide. When you are
  done, leave the Temporal Development Server running if you want to test your code locally.

## Configure Workers to use the AI SDK

Workers are the compute layer of a Temporal Application. They are responsible for executing the code that defines your
[Workflows](/glossary#workflow) and [Activities](/glossary#activity). Before you can execute a Workflow or Activity with
the Vercel AI SDK, you need to create a Worker and configure it to use the AI SDK plugin.

Follow the steps below to configure your Worker.

1. Install the `@temporalio/ai-sdk` package.

   ```bash
   npm install @temporalio/ai-sdk
   ```

2. Create a `worker.ts` file and configure the Worker to use the AI SDK plugin.

   ```ts {9-11}

   //... other import statements, initializing a connection
   //  to the Temporal Service to be used by the Worker

   const worker = await Worker.create({
     plugins: [
       new AiSdkPlugin({
         modelProvider: openai,
       }),
     ],
     connection,
     namespace: 'default',
     taskQueue: 'ai-sdk',
     workflowsPath: require.resolve('./workflows'),
     activities,
   });

   // ... code that runs the worker
   ```

   The `modelProvider` specifies which AI provider to use when creating models. Choose the provider that best suits your
   needs. In the Worker options, you are also specifying that the Worker polls the `ai-sdk` Task Queue for work in the
   `default` Namespace. Make sure that you configure your Client application to use the same Task Queue and Namespace.

3. Run the Worker. This Worker will now poll the Temporal Service for work on the `ai-sdk` Task Queue in the `default`
   Namespace until you stop it.

   ```bash
   nodemon worker.ts
   ```

   You must ensure the Worker process has access to your API credentials. Most provider SDKs read credentials from
   environment variables. Refer to the [Vercel AI SDK documentation](https://ai-sdk.dev/providers/ai-sdk-providers) for
   instructions on how to set up your environment variables for the provider you chose.

   :::tip

   You only need to give provider credentials to the Worker process. The client application, meaning the application
   that sends requests to the Temporal Service to start Workflow Executions, doesn't need to know about the credentials.

   :::

See the full example at [ai-sdk samples](https://github.com/temporalio/samples-typescript/tree/main/ai-sdk).

## Develop a Simple Haiku Agent

To help you get started, you can develop a simple Haiku Agent that generates haikus based on a prompt.

If you weren't using Temporal, you would write code like this to generate a haiku:

```ts

async function haikuAgent(prompt: string): Promise<string> {
  const result = await generateText({
    model: openai('gpt-4o-mini'),
    prompt,
    system: 'You only respond in haikus.',
  });
  return result.text;
}
```

To add Durable Execution to your agent, implement the agent as a Temporal Workflow. Use the AI SDK as you normally
would, but pass `temporalProvider.languageModel()` as the model. The string you provide (like `'gpt-4o-mini'`) is passed
to your configured `modelProvider` to create the model.

```ts {2,6}

export async function haikuAgent(prompt: string): Promise<string> {
  const result = await generateText({
    model: temporalProvider.languageModel('gpt-4o-mini'),
    prompt,
    system: 'You only respond in haikus.',
  });
  return result.text;
}
```

With only two line changes, you have added Durable Execution to your agent. Your agent now gets automatic retries,
timeouts, and the ability to run for extended periods without losing state if the process crashes.

## Provide your durable agent with tools

