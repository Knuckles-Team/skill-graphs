
Set up the time-skipping test framework in the SDK of your choice.

```bash
npm install @temporalio/testing
```

The `@temporalio/testing` package downloads the test server and exports [`TestWorkflowEnvironment`](https://typescript.temporal.io/api/classes/testing.TestWorkflowEnvironment), which you use to connect the Client and Worker to the test server and interact with the test server.

[`TestWorkflowEnvironment.createTimeSkipping`](https://typescript.temporal.io/api/classes/testing.TestWorkflowEnvironment#createtimeskipping) starts the test server.
A typical test suite should set up a single instance of the test environment to be reused in all tests (for example, in a [Jest](https://jestjs.io/) `beforeAll` hook or a [Mocha](https://mochajs.org/) `before()` hook).

```typescript

let testEnv: TestWorkflowEnvironment;

// beforeAll and afterAll are injected by Jest
beforeAll(async () => {
  testEnv = await TestWorkflowEnvironment.createTimeSkipping();
});

afterAll(async () => {
  await testEnv?.teardown();
});
```

`TestWorkflowEnvironment` has [`client`](https://typescript.temporal.io/api/classes/testing.TestWorkflowEnvironment#client) and [`nativeConnection`](https://typescript.temporal.io/api/classes/testing.TestWorkflowEnvironment#nativeconnection) for creating Workers:

```typescript

test('workflowFoo', async () => {
  const worker = await Worker.create({
    connection: testEnv.nativeConnection,
    taskQueue: 'test',
    ...
  });
  const result = await worker.runUntil(
    testEnv.client.workflow.execute(workflowFoo, {
      workflowId: uuid4(),
      taskQueue: 'test',
    })
  );
  expect(result).toEqual('foo');
});
```

This test uses the test connection to create a Worker, runs the Worker until the Workflow is complete, and then makes an assertion about the Workflow's result.
The Workflow is executed using `testEnv.client.workflow`, which is connected to the test server.

#### Skip time automatically {/* #automatic-method */}

You can skip time automatically in the SDK of your choice.
Start a test server process that skips time as needed.
For example, in the time-skipping mode, Timers, which include sleeps and conditional timeouts, are fast-forwarded except when Activities are running.

The test server starts in "normal" time.
When you use `TestWorkflowEnvironment.client.workflow.execute()` or `.result()`, the test server switches to "skipped" time mode until the Workflow completes.
In "skipped" mode, timers (`sleep()` calls and `condition()` timeouts) are fast-forwarded except when Activities are running.

`workflows.ts`

```ts

export async function sleeperWorkflow() {
  await sleep('1 day');
}
```

`test.ts`

```ts

test('sleep completes almost immediately', async () => {
  const worker = await Worker.create({
    connection: testEnv.nativeConnection,
    taskQueue: 'test',
    workflowsPath: require.resolve('./workflows'),
  });
  // Does not wait an entire day
  await worker.runUntil(
    testEnv.client.workflow.execute(sleeperWorkflow, {
      workflowId: uuid(),
      taskQueue: 'test',
    }),
  );
});
```

#### Skip time manually {/* #manual-method */}

Skip time manually in the SDK of your choice.

You can call `testEnv.sleep()` from your test code to advance the test server's time.
This is useful for testing intermediate states or indefinitely long-running Workflows.
However, to use `testEnv.sleep()`, you need to avoid automatic time skipping by starting the Workflow with `.start()` instead of `.execute()` (and not calling `.result()`).

`workflow.ts`

```ts

export const daysQuery = defineQuery('days');

export async function sleeperWorkflow() {
  let numDays = 0;

  setHandler(daysQuery, () => numDays);

  for (let i = 0; i < 100; i++) {
    await sleep('1 day');
    numDays++;
  }
}
```

`test.ts`

```ts
test('sleeperWorkflow counts days correctly', async () => {
  const worker = await Worker.create({
    connection: testEnv.nativeConnection,
    taskQueue: 'test',
    workflowsPath: require.resolve('./workflows'),
  });

  // `start()` starts the test server in "normal" mode, not skipped time mode.
  // If you don't advance time using `testEnv.sleep()`, then `sleeperWorkflow()`
  // will run for days.
  handle = await testEnv.client.workflow.start(sleeperWorkflow, {
    workflowId: uuid4(),
    taskQueue,
  });

  worker.run();

  let numDays = await handle.query(daysQuery);
  assert.equal(numDays, 0);

  // Advance the test server's time by 25 hours
  await testEnv.sleep('25 hours');
  numDays = await handle.query(daysQuery);
  assert.equal(numDays, 1);

  await testEnv.sleep('25 hours');
  numDays = await handle.query(daysQuery);
  assert.equal(numDays, 2);
});
```

#### Skip time in Activities {/* #skip-time-in-activities */}

Skip time in Activities in the SDK of your choice.

Call [`TestWorkflowEnvironment.sleep`](https://typescript.temporal.io/api/classes/testing.TestWorkflowEnvironment#sleep) from the mock Activity.

In the following test, `processOrderWorkflow` sends a notification to the user after one day.
The `processOrder` mocked Activity calls `testEnv.sleep(‘2 days')`, during which the Workflow sends email (by calling the `sendNotificationEmail` Activity).

Then, after the Workflow completes, we assert that `sendNotificationEmail` was called.

<details>
<summary>
Workflow implementation
</summary>

<!--SNIPSTART typescript-timer-reminder-workflow-->
[timer-examples/src/workflows.ts](https://github.com/temporalio/samples-typescript/blob/main/timer-examples/src/workflows.ts)
```ts
export async function processOrderWorkflow({
  orderProcessingMS,
  sendDelayedEmailTimeoutMS,
}: ProcessOrderOptions): Promise<string> {
  let processing = true;
  // Dynamically define the timeout based on given input
  const { processOrder } = proxyActivities<ReturnType<typeof createActivities>>({
    startToCloseTimeout: orderProcessingMS,
  });

  const processOrderPromise = processOrder().then(() => {
    processing = false;
  });

  await Promise.race([processOrderPromise, sleep(sendDelayedEmailTimeoutMS)]);

  if (processing) {
    await sendNotificationEmail();

    await processOrderPromise;
  }

  return 'Order completed!';
}
```
<!--SNIPEND-->

</details>

<!--SNIPSTART typescript-timer-reminder-test-->
[timer-examples/src/test/workflows.test.ts](https://github.com/temporalio/samples-typescript/blob/main/timer-examples/src/test/workflows.test.ts)
```ts
it('sends reminder email if processOrder does not complete in time', async () => {
  // This test doesn't actually take days to complete: the TestWorkflowEnvironment starts the
  // Test Server, which automatically skips time when there are no running Activities.
  let emailSent = false;
  const mockActivities: ReturnType<typeof createActivities> = {
    async processOrder() {
      // Test server switches to "normal" time while an Activity is executing.
      // Call `env.sleep` to skip ahead 2 days, by which time sendNotificationEmail
      // should have been called.
      await env.sleep('2 days');
    },
    async sendNotificationEmail() {
      emailSent = true;
    },
  };
  const worker = await Worker.create({
    connection: env.nativeConnection,
    taskQueue: 'test',
    workflowsPath: require.resolve('../workflows'),
    activities: mockActivities,
  });
  await worker.runUntil(
    env.client.workflow.execute(processOrderWorkflow, {
      workflowId: uuid(),
      taskQueue: 'test',
      args: [{ orderProcessingMS: ms('3 days'), sendDelayedEmailTimeoutMS: ms('1 day') }],
    }),
  );
  assert.ok(emailSent);
});
```
<!--SNIPEND-->

### Test functions in Workflow context {/* #workflow-context */}

For a function or method to run in the Workflow context (where it's possible to get the current Workflow info, or running inside the sandbox in the case of TypeScript or Python), it needs to be run by the Worker as if it were a Workflow.

:::note

This section is applicable in Python and TypeScript.
In Python, we allow testing of Workflows only and not generic Workflow-related code.

:::

To test a function in your Workflow code that isn't a Workflow, put the file it's exported from in [WorkerOptions.workflowsPath](https://typescript.temporal.io/api/interfaces/worker.WorkerOptions#workflowspath).
Then execute the function as if it were a Workflow:

`workflows/file-with-workflow-function-to-test.ts`

```ts

export async function functionToTest(): Promise<number> {
  await sleep('1 day');
  return 42;
}
```

`test.ts`

```ts
const worker = await Worker.create({
  connection: testEnv.nativeConnection,
  workflowsPath: require.resolve(
    './workflows/file-with-workflow-function-to-test',
  ),
});

const result = await worker.runUntil(
  testEnv.client.workflow.execute(functionToTest, workflowOptions),
);

assert.equal(result, 42);
```

If `functionToTest` starts a Child Workflow, that Workflow must be exported from the same file (so that the Worker knows about it):

```ts

export { someWorkflowToRunAsChild };

export async function functionToTest(): Promise<number> {
  const result = await wf.executeChild(someWorkflowToRunAsChild);
  return result + 42;
}
```

### Assert in Workflow {/* #assert-in-workflow */}

The `assert` statement is a convenient way to insert debugging assertions into the Workflow context.

The `assert` method is available in Python and TypeScript.

The Node.js [`assert`](https://nodejs.org/api/assert.html) module is included in Workflow bundles.

By default, a failed `assert` statement throws `AssertionError`, which causes a [Workflow Task](/tasks#workflow-task) to fail and be indefinitely retried.

To prevent this behavior, use [`workflowInterceptorModules`](https://typescript.temporal.io/api/namespaces/testing/#workflowinterceptormodules) from `@temporalio/testing`.
These interceptors catch an `AssertionError` and turn it into an `ApplicationFailure` that fails the entire Workflow Execution (not just the Workflow Task).

`workflows/file-with-workflow-function-to-test.ts`

```ts

export async function functionToTest() {
  assert.ok(false);
}
```

`test.ts`

```ts

  TestWorkflowEnvironment,
  workflowInterceptorModules,
} from '@temporalio/testing';

const worker = await Worker.create({
  connection: testEnv.nativeConnection,
  interceptors: {
    workflowModules: workflowInterceptorModules,
  },
  workflowsPath: require.resolve(
    './workflows/file-with-workflow-function-to-test',
  ),
});

await worker.runUntil(
  testEnv.client.workflow.execute(functionToTest, workflowOptions), // throws WorkflowFailedError
);
```

## How to Replay a Workflow Execution {/* #replay */}

Replay recreates the exact state of a Workflow Execution.
You can replay a Workflow from the beginning of its Event History.

Replay succeeds only if the [Workflow Definition](/workflow-definition) is compatible with the provided history from a deterministic point of view.

When you test changes to your Workflow Definitions, we recommend doing the following as part of your CI checks:

1. Determine which Workflow Types or Task Queues (or both) will be targeted by the Worker code under test.
2. Download the Event Histories of a representative set of recent open and closed Workflows from each Task Queue, either programmatically using the SDK client or via the Temporal CLI.
3. Run the Event Histories through replay.
4. Fail CI if any error is encountered during replay.

The following are examples of fetching and replaying Event Histories:

To replay a single Event History, use [worker.runReplayHistory](https://typescript.temporal.io/api/classes/worker.Worker#runreplayhistory).

When an Event History is replayed and non-determinism is detected (that is, the Workflow code is incompatible with the History), [DeterminismViolationError](https://typescript.temporal.io/api/classes/workflow.DeterminismViolationError) is thrown.
If replay fails for any other reason, [ReplayError](https://typescript.temporal.io/api/classes/worker.ReplayError) is thrown.

In the following example, a single Event History is loaded from a JSON file on disk (as obtained from the [Web UI](/web-ui) or the [Temporal CLI](/cli/command-reference/workflow#show)):

```ts
const filePath = './history_file.json';
const history = await JSON.parse(fs.promises.readFile(filePath, 'utf8'));
await Worker.runReplayHistory(
  {
    workflowsPath: require.resolve('./your/workflows'),
  },
  history,
);
```

Alternatively, we can download the Event History programmatically using a Client:

```ts
const connection = await Connection.connect({ address });
const client = new Client({ connection, namespace: 'your-namespace' });
const handle = client.workflow.getHandle('your-workflow-id');
const history = await handle.fetchHistory();
await Worker.runReplayHistory(
  {
    workflowsPath: require.resolve('./your/workflows'),
  },
  history,
);
```

To gain confidence that changes to a Workflow are safe to deploy, we recommend that you obtain Event Histories from the relevant Task Queue and replay them in bulk.
You can do so by combining the [Client.workflow.list()](https://typescript.temporal.io/api/classes/client.WorkflowClient#list) and [worker.runReplayHistories()](https://typescript.temporal.io/api/classes/worker.Worker#runreplayhistories) APIs.

In the following example (which, as of server 1.18, requires [Advanced Visibility](/visibility#advanced-visibility) to be enabled), Event Histories are downloaded from the server and then replayed by passing in a client and a set of Workflows Executions.
The [results](https://typescript.temporal.io/api/interfaces/worker.ReplayResult) returned by the async iterator contain information about the Workflow Execution and whether an error occurred during replay.

```ts
const executions = client.workflow.list({
  query: 'TaskQueue=foo and StartTime > "2022-01-01T12:00:00"',
});
const histories = executions.intoHistories();
const results = Worker.runReplayHistories(
  {
    workflowsPath: require.resolve('./your/workflows'),
  },
  histories,
);
for await (const result of results) {
  if (result.error) {
    console.error('Replay failed', result);
  }
}
```

---

## Client - TypeScript SDK

![TypeScript SDK Banner](/img/assets/banner-typescript-temporal.png)

## Temporal Client

- [Temporal Client](/develop/typescript/client/temporal-client)
- [Namespaces](/develop/typescript/client/namespaces)

---

## Manage Namespaces - TypeScript SDK

## How to create and manage Namespaces {/* #namespaces */}

You can create, update, deprecate or delete your [Namespaces](/namespaces) using either the Temporal CLI or SDK APIs.

Use Namespaces to isolate your Workflow Executions according to your needs.
For example, you can use Namespaces to match the development lifecycle by having separate `dev` and `prod` Namespaces.
You could also use them to ensure Workflow Executions between different teams never communicate - such as ensuring that the `teamA` Namespace never impacts the `teamB` Namespace.

On Temporal Cloud, use the [Temporal Cloud UI](/cloud/namespaces#create-a-namespace) to create and manage a Namespace from the UI, or [tcld commands](https://docs.temporal.io/cloud/tcld/namespace/) to manage Namespaces from the command-line interface.

On self-hosted Temporal Service, you can register and manage your Namespaces using the Temporal CLI (recommended) or programmatically using APIs.
Note that these APIs and Temporal CLI commands will not work with Temporal Cloud.

Use a custom [Authorizer](/self-hosted-guide/security#authorizer-plugin) on your Frontend Service in the Temporal Service to set restrictions on who can create, update, or deprecate Namespaces.

You must register a Namespace with the Temporal Service before setting it in the Temporal Client.

### How to register Namespaces {/* #register-namespace */}

Registering a Namespace creates a Namespace on the Temporal Service or Temporal Cloud.

On Temporal Cloud, use the [Temporal Cloud UI](/cloud/namespaces#create-a-namespace) or [tcld commands](https://docs.temporal.io/cloud/tcld/namespace/) to create Namespaces.

On self-hosted Temporal Service, you can register your Namespaces using the Temporal CLI (recommended) or programmatically using APIs.
Note that these APIs and Temporal CLI commands will not work with Temporal Cloud.

Use a custom [Authorizer](/self-hosted-guide/security#authorizer-plugin) on your Frontend Service in the Temporal Service to set restrictions on who can create, update, or deprecate Namespaces.

### How to manage Namespaces {/* #manage-namespaces */}

You can get details for your Namespaces, update Namespace configuration, and deprecate or delete your Namespaces.

On Temporal Cloud, use the [Temporal Cloud UI](/cloud/namespaces#create-a-namespace) or [tcld commands](https://docs.temporal.io/cloud/tcld/namespace/) to manage Namespaces.

On self-hosted Temporal Service, you can manage your registered Namespaces using the Temporal CLI (recommended) or programmatically using APIs.
Note that these APIs and Temporal CLI commands will not work with Temporal Cloud.

Use a custom [Authorizer](/self-hosted-guide/security#authorizer-plugin) on your Frontend Service in the Temporal Service to set restrictions on who can create, update, or deprecate Namespaces.

You must register a Namespace with the Temporal Service before setting it in the Temporal Client.

---

## Temporal Client - Typescript SDK

A [Temporal Client](/encyclopedia/temporal-sdks#temporal-client) enables you to communicate with the Temporal Service.
Communication with a Temporal Service lets you perform actions such as starting Workflow Executions, sending Signals and
Queries to Workflow Executions, getting Workflow results, and more. You cannot initialize a Temporal Client inside a
Workflow. However, they're commonly initialized inside an Activity to communicate with a Temporal Service.

This page shows you how to do the following using the TypeScript SDK with the Temporal Client:

- [Connect to a local development Temporal Service](#connect-to-development-service)
- [Connect to Temporal Cloud](#connect-to-temporal-cloud)
- [Connect to Temporal Service from a Worker](#connect-to-temporal-service-from-a-worker)
- [Start a Workflow Execution](#start-workflow-execution)
- [Get Workflow results](#get-workflow-results)

In the TypeScript SDK, connecting to Temporal Service from a Temporal Application and from within an Activity rely on a
different type of connection than connecting from a Worker. The sections
[Connect to a local development Temporal Service](#connect-to-development-service) and
[Connect to Temporal Cloud](#connect-to-temporal-cloud) apply to connecting from a Temporal Application or from within
an Activity. See [Connect to Temporal Service from a Worker](#connect-to-temporal-service-from-a-worker) for details on
connecting from a Worker.

## Connect to development Temporal Service {/* #connect-to-development-service */}

To connect to a development Temporal service from a Temporal Application or from within an Activity, import the
[`Connection` class](https://typescript.temporal.io/api/classes/client.Connection) from `@temporalio/client` and use
[`Connection.connect`](https://typescript.temporal.io/api/classes/client.Connection#connect) to create a Connection
object to connect to the Temporal Service. Then pass in that connection when you create a new `Client` instance. If you
leave the connection options empty, the SDK defaults to connecting to `127.0.0.1:7233` in the `default` Namespace.

```ts

async function run() {
  const connection = await Connection.connect();

  // your code goes here

  const client = new Client({ connection });
}

run().catch((err) => {
  console.error(err);
  process.exit(1);
});
```

If you need to connect to a Temporal Service with custom options, you can provide connection options directly in code,
load them from **environment variables**, or a **TOML configuration file** using the `@temporalio/envconfig` helpers. We
recommend environment variables or a configuration file for secure, repeatable configuration.

<Tabs groupId="connect-options" defaultValue="config-file" >

<TabItem value="config-file" label="Configuration File">

You can use a TOML configuration file to set connection options for the Temporal Client. The configuration file lets you
configure multiple profiles, each with its own set of connection options. You can then specify which profile to use when
creating the Temporal Client.

You can use the environment variable `TEMPORAL_CONFIG_FILE` to specify the location of the TOML file or provide the path
to the file directly in code. If you don't provide the configuration file path, the SDK looks for it at the path
`~/.config/temporalio/temporal.toml` or the equivalent on your OS. Refer to
[Environment Configuration](/develop/environment-configuration) for more details about configuration files and profiles.

:::info

The connection options set in configuration files have lower precedence than environment variables. This means that if
you set the same option in both the configuration file and as an environment variable, the environment variable value
overrides the option set in the configuration file.

:::

For example, the following TOML configuration file defines two profiles: `default` and `prod`. Each profile has its own
set of connection options.

```toml title="config.toml"
