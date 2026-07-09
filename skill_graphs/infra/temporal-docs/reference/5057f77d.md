    return Promise.all(
      payloads.map(async (payload) => {
        if (!payload.metadata || decode(payload.metadata[METADATA_ENCODING_KEY]) !== ENCODING) {
          return payload;
        }
        if (!payload.data) {
          throw new ValueError('Payload data is missing');
        }

        const keyIdBytes = payload.metadata[METADATA_ENCRYPTION_KEY_ID];
        if (!keyIdBytes) {
          throw new ValueError('Unable to decrypt Payload without encryption key id');
        }

        const keyId = decode(keyIdBytes);
        let key = this.keys.get(keyId);
        if (!key) {
          key = await fetchKey(keyId);
          this.keys.set(keyId, key);
        }
        const decryptedPayloadBytes = await decrypt(payload.data, key);
        console.log('Decrypting payload.data:', payload.data);
        return temporal.api.common.v1.Payload.decode(decryptedPayloadBytes);
      }),
    );
  }
}

async function fetchKey(_keyId: string): Promise<crypto.CryptoKey> {
  // In production, fetch key from a key management system (KMS). You may want to memoize requests if you'll be decoding
  // Payloads that were encrypted using keys other than defaultKeyId.
  const key = Buffer.from('test-key-test-key-test-key-test!');
  const cryptoKey = await crypto.subtle.importKey(
    'raw',
    key,
    {
      name: 'AES-GCM',
    },
    true,
    ['encrypt', 'decrypt'],
  );

  return cryptoKey;
}
```
<!--SNIPEND-->

The encryption and decryption code is in [src/crypto.ts](https://github.com/temporalio/samples-typescript/tree/main/encryption/src/crypto.ts).
Because encryption is CPU intensive, and doing AES with the crypto module built into Node.js blocks the main thread, we use `@ronomon/crypto-async`, which uses the Node.js thread pool.

As before, we provide a custom Data Converter to the Client and Worker:

<!--SNIPSTART typescript-encryption-client -->
[encryption/src/client.ts](https://github.com/temporalio/samples-typescript/blob/main/encryption/src/client.ts)
```ts
const client = new Client({
  connection,
  dataConverter: await getDataConverter(),
});

const handle = await client.workflow.start(example, {
  args: ['Alice: Private message for Bob.'],
  taskQueue: 'encryption',
  workflowId: `my-business-id-${uuid()}`,
});

console.log(`Started workflow ${handle.workflowId}`);
console.log(await handle.result());
```
<!--SNIPEND-->

<!--SNIPSTART typescript-encryption-worker -->
[encryption/src/worker.ts](https://github.com/temporalio/samples-typescript/blob/main/encryption/src/worker.ts)
```ts
const worker = await Worker.create({
  workflowsPath: require.resolve('./workflows'),
  taskQueue: 'encryption',
  dataConverter: await getDataConverter(),
});
```
<!--SNIPEND-->

When the Client sends `'Alice: Private message for Bob.'` to the Workflow, it gets encrypted on the Client and decrypted in the Worker.
The Workflow receives the decrypted message and appends another message.
When it returns that longer string, the string gets encrypted by the Worker and decrypted by the Client.

<!--SNIPSTART typescript-encryption-workflow -->
[encryption/src/workflows.ts](https://github.com/temporalio/samples-typescript/blob/main/encryption/src/workflows.ts)
```ts
export async function example(message: string): Promise<string> {
  return `${message}\nBob: Hi Alice, I'm Workflow Bob.`;
}
```
<!--SNIPEND-->

---

## Debugging - TypeScript SDK

The Debugging section of the Temporal TypeScript SDK developer's guide covers tools for debugging and how to troubleshoot common issues.

## How to debug in a development environment {/* #debug-in-a-development-environment */}

In addition to the normal development tools of logging and a debugger, you can also see what's happening in your Workflow by using the [Web UI](/web-ui) or [Temporal CLI](/cli).

## How to debug in a production environment {/* #debug-in-a-production-environment */}

You can debug production Workflows using:

- [Web UI](/web-ui)
- [Temporal CLI](/cli)
- [Replay](/develop/typescript/best-practices/testing-suite#replay)
- [Tracing](/develop/typescript/platform/observability#tracing)
- [Logging](/develop/typescript/platform/observability#logging)

You can debug and tune Worker performance with metrics and the [Worker performance guide](/develop/worker-performance).
For information on setting up SDK metrics, see [Metrics](/develop/typescript/platform/observability#metrics) in the Observability section of the TypeScript SDK developer's guide.

Debug Server performance with [Cloud metrics](/cloud/metrics/) or [self-hosted Server metrics](/self-hosted-guide/production-checklist#scaling-and-metrics).

## How to troubleshoot common issues in the TypeScript SDK {/* #troubleshoot-common-issues */}

{/* The following was ported from \docs-src\typescript\troubleshooting.md */}

### Two locations to watch

- Workflow Errors are reflected in Temporal Web.
- Worker errors and logs are reflected in the terminal.

If something isn't behaving the way you expect, make sure to check both locations for helpful error messages.

### Stale Workflows

If you are developing Workflows and finding that code isn't executing as expected, the first place to look is whether old Workflows are still running.

If those old Workflows have the same name and are on the same Task Queue, Temporal will try to continue executing them on your new code by design. You may get errors that make no sense to you because:

- Temporal is trying to execute old Workflow code that no longer exists in your codebase.
- Your new Client code is expecting Temporal to execute old Workflow/Activity code it doesn't yet know about.

Stale Workflows are usually a non-issue because the errors generated are just noise from code you no longer want to run. If you need to terminate old stale Workflows, you can do so with Temporal Web or the Temporal CLI.

### Workflow/Activity registration errors

**If your Workflows or Activities are not imported or spelled correctly**, here are some errors we've seen:

- `ApplicationFailure: 'MyFunction' is not a function`
- `Workflow did not register a handler for MyQuery`

Double check that your Workers are registering the right Workflow and Activity Definitions (function names) on the right Task Queues.

**If you are running Temporal in a monorepo**, then your `node_modules` may be in a different location than where Temporal expects to find it by default, which results in errors like:

```bash
[ERROR] Module not found: Error: Can't resolve '@temporalio/workflow/lib/worker-interface.js' in '/src'
```

Our [Next.js tutorial](https://learn.temporal.io/tutorials/typescript/nextjs) is written for people setting up Temporal **within an existing monorepo**, which may be of use here.

When you pass a `workflowsPath`, our Webpack config expects to find `node_modules` in the same or a parent/ancestor directory.

**If you are custom bundling your own Workflows** you may get errors like these:

```bash
[ERROR] Failed to activate workflow {
  runId: 'aaf84a83-51ce-462a-9ab7-6a641a703bff',
  error: ReferenceError: exports is not defined,
  workflowExists: false
}
```

Temporal Workflow Bundles need to [export a set of methods that fit the compiled `worker-interface.ts` from `@temporalio/workflow`](https://github.com/temporalio/sdk-typescript/blob/eaa2d205c9bc5ff4a3b17c0b34f2dcf6b1e0264a/packages/worker/src/workflow/bundler.ts#L81) as an entry point.
We do offer a `bundleWorkflowCode` method to assist you with this, though it uses our Webpack settings.
For more information, see the [Register types](/develop/typescript/workers/run-worker-process#register-types) section.

### Webpack errors

The TypeScript SDK's Worker bundles Workflows based on `workflowsPath` with [Webpack](https://webpack.js.org/) and run them inside v8 isolates.

If Webpack fails to create the bundle, the SDK will throw an error and emit webpack logs using the SDK's [logger](/develop/typescript/platform/observability#logging).

If you do not see Webpack output in your terminal make sure that you have not disabled SDK logging (see reference to `Runtime.install()` in the link above).

**A common mistake for newcomers to the TypeScript SDK is trying to use Node.js built-ins and modules in their Workflow code.** Usually, the best thing to do is move that code to an Activity.

Some common examples that will **not** work in the Workflow isolate:

<details>
    <summary>
    Importing node built-in modules
    </summary>

:::danger Antipattern

```ts

const config = fs.readFileSync('config.json', 'utf8');
```

:::

This is invalid because reading from the filesystem is a non-deterministic operation: the file may change from the time of the original Workflow Execution to when the Workflow is replayed.

You'll typically see an error in this form in the Webpack output:

```
2021-10-14T19:22:00.606Z [INFO] Module not found: Error: Can't resolve 'fs' in '/Users/you/your-project/src'
2021-10-14T19:22:00.606Z [INFO] resolve 'fs' in '/Users/you/your-project/src'
2021-10-14T19:22:00.606Z [INFO]   Parsed request is a module
2021-10-14T19:22:00.606Z [INFO]   using description file: /Users/you/your-project/package.json (relative path: ./src)
2021-10-14T19:22:00.606Z [INFO]     Field 'browser' doesn't contain a valid alias configuration
```

</details>

<details>
    <summary>
    Importing and calling Activities directly from Workflow code
    </summary>

:::danger Antipattern

```ts

export async function yourWorkflow(): Promise<string> {
  return await makeHTTPRequest('https://temporal.io');
}
```

:::

This is invalid because activity implementations should not be directly referenced by Workflow code.
Activities are used by Workflows in order to make network calls and read from the filesystem, operations which are non-deterministic by nature because they rely on external state.
Temporal records Activity results in the Event history and in case your Workflow is replayed, completed Activities will not be rerun, instead their recorded result will be delivered to the Workflow.

You'll typically see an error in this form in the Webpack output:

```
2021-10-14T19:46:52.731Z [INFO] ERROR in ./src/activities.ts 8:31-46
2021-10-14T19:46:52.731Z [INFO] Module not found: Error: Can't resolve 'http' in '/Users/you/your-project/src'
2021-10-14T19:46:52.731Z [INFO]
2021-10-14T19:46:52.731Z [INFO] BREAKING CHANGE: webpack < 5 used to include polyfills for node.js core modules by default.
2021-10-14T19:46:52.731Z [INFO] This is no longer the case. Verify if you need this module and configure a polyfill for it.
2021-10-14T19:46:52.731Z [INFO]
2021-10-14T19:46:52.731Z [INFO] If you want to include a polyfill, you need to:
2021-10-14T19:46:52.731Z [INFO]         - add a fallback 'resolve.fallback: { "http": require.resolve("stream-http") }'
2021-10-14T19:46:52.731Z [INFO]         - install 'stream-http'
2021-10-14T19:46:52.731Z [INFO] If you don't want to include a polyfill, you can use an empty module like this:
2021-10-14T19:46:52.731Z [INFO]         resolve.fallback: { "http": false }
```

To properly call your Activities from Workflow code use `proxyActivities` and make sure to only import the Activity types.

```ts

const { makeHTTPRequest } = proxyActivities<typeof activities>();

export async function yourWorkflow(): Promise<string> {
  return await makeHTTPRequest('https://temporal.io');
}
```

</details>

### Works in Dev but not in Prod

The two main sources of dev-prod discrepancies are in bundling and connecting.

#### Production bundling

You may experience your Client sending stripped names as the Workflow "Type" when scheduling a Workflow.
Webpack can change the Workflow's function name to something shorter.
Temporal won't know how to handle the mismatch between the shorter name and the expected Workflow type.

You may experience errors like this:

```
Error: 3 INVALID_ARGUMENT: WorkflowType is not set on request.
```

Or you may see shorter names in the Temporal Service's Web UI when Webpack changed the Workflow's function name to something shorter, in this case the single letter 's':

<CaptionedImage
    src="/img/webui/stripped_workflow_types_in_webui.png"
    title="Temporal Web UI showing stripped 'Workflow Type' entries, in this case the single letter 's'"
/>

This issue can happen when your bundler strips out Workflow function names.
Temporal relies on those names to set the "Workflow Type" in the Service Web UI.
To prevent the build process from shortening Workflow function names, modify the webpack configuration file ( `webpack.config.js`) to set the Boolean that retains the original names in the `TerserPlugin` configuration section.
Setting the option (`keep_fnames`) to `true` prevents name stripping.

<Tabs
defaultValue="webpackterser"
values={[
{label: 'Webpack with Terser', value: 'webpackterser'},
{label: 'ESbuild', value: 'esbuild'},
]
}>

<TabItem value="webpackterser">

```js
// webpack.config.js
module.exports = {
  optimization: {
    minimize: true,
    minimizer: [
      new TerserPlugin({
        terserOptions: {
          keep_fnames: true, // don't strip function names in production
        },
      }),
    ],
  },
};
```

</TabItem>
<TabItem value="esbuild">

```js
require('esbuild').buildSync({
  entryPoints: ['app.js'],
  minify: true,
  keepNames: true,
  outfile: 'out.js',
});
```

See the [esbuild docs](https://esbuild.github.io/api/#keep-names) for more information.
</TabItem>
</Tabs>

#### Connecting to Temporal Server

If you are trying to connect in production and getting this:

```bash
[TransportError: transport error]
```

It is a sign that something is wrong with your Cert/Key pair.
Log it out and make sure it is an exact match with what is expected (often, the issue can be whitespace when injecting from your production secrets management environment).

### Resetting Workflows to deal with logical bugs

You can "rewind time" using the Temporal CLI, resetting Event History to some previous point in time. You can read the Temporal CLI docs on:

- [Restarting and resetting Workflows by ID](/cli)
- [Resetting all Workflows by binary checksum identifier](/cli)

If you need to reset programmatically, the TS SDK does not have any high level APIs for this, but you can make raw gRPC calls to [resetWorkflowExecution](https://typescript.temporal.io/api/classes/proto.temporal.api.workflowservice.v1.WorkflowService-1/#resetworkflowexecution).

Resetting should only be used to deal with serious logical bugs in your code: it's not for handling transient failures, like a downstream service being unreachable. It should not be used in the course of normal application flows.

### gRPC call timeouts (context deadline exceeded)

The opaque `context deadline exceeded` error comes from `gRPC`:

```
Error: 4 DEADLINE_EXCEEDED: context deadline exceeded
    at Object.callErrorFromStatus (/Users/swyx/Work/Temporal/samples-typescript/nextjs-oneclick/node_modules/@grpc/grpc-js/build/src/call.js:31:26)
    at Object.onReceiveStatus (/Users/swyx/Work/Temporal/samples-typescript/nextjs-oneclick/node_modules/@grpc/grpc-js/build/src/client.js:179:52)
    at Object.onReceiveStatus (/Users/swyx/Work/Temporal/samples-typescript/nextjs-oneclick/node_modules/@grpc/grpc-js/build/src/client-interceptors.js:336:141)
    at Object.onReceiveStatus (/Users/swyx/Work/Temporal/samples-typescript/nextjs-oneclick/node_modules/@grpc/grpc-js/build/src/client-interceptors.js:299:181)
    at /Users/swyx/Work/Temporal/samples-typescript/nextjs-oneclick/node_modules/@grpc/grpc-js/build/src/call-stream.js:145:78
    at processTicksAndRejections (node:internal/process/task_queues:78:11) {
  code: 4,
  details: 'context deadline exceeded',
  metadata: Metadata {
    internalRepr: Map(1) { 'content-type' => [Array] },
    options: {}
  },
  page: '/api/getBuyState'
}
```

Several conditions can cause this error, including network hiccups, timeouts that are too short, and an overloaded server.
Querying a Workflow Execution whose query handler causes an error can result in the query call timing out.

Some troubleshooting actions you can take:

- Verify the connection from your Worker to the Temporal Server is working and doesn't have unusually high latency.
- If you are running Temporal Server yourself, check your [server metrics](/self-hosted-guide/production-checklist#scaling-and-metrics) to ensure it's not overloaded.
- If what's timing out is a query, check the logs of your Workers to see if they are having issues handling the query.

If none of the preceding actions help you discover why timeouts are occurring, please try to produce a minimal repro and we'll be glad to help.

---

## Entity pattern - TypeScript SDK

### Single-entity design pattern in TypeScript {/* #single-entity-pattern */}

The following is a simple pattern that represents a single entity.
It tracks the number of iterations regardless of frequency, and calls `continueAsNew` while properly handling pending updates from Signals.

```ts
interface Input {
  /* Define your Workflow input type here */
}
interface Update {
  /* Define your Workflow update type here */
}

const MAX_ITERATIONS = 1;

export async function entityWorkflow(
  input: Input,
  isNew = true,
): Promise<void> {
  try {
    const pendingUpdates = Array<Update>();
    setHandler(updateSignal, (updateCommand) => {
      pendingUpdates.push(updateCommand);
    });

    if (isNew) {
      await setup(input);
    }

    for (let iteration = 1; iteration <= MAX_ITERATIONS; ++iteration) {
      // Ensure that we don't block the Workflow Execution forever waiting
      // for updates, which means that it will eventually Continue-As-New
      // even if it does not receive updates.
      await condition(() => pendingUpdates.length > 0, '1 day');

      while (pendingUpdates.length) {
        const update = pendingUpdates.shift();
        await runAnActivityOrChildWorkflow(update);
      }
    }
  } catch (err) {
    if (isCancellation(err)) {
      await CancellationScope.nonCancellable(async () => {
        await cleanup();
      });
    }
    throw err;
  }
  await continueAsNew<typeof entityWorkflow>(input, false);
}
```

---

## Best Practices - TypeScript SDK

![TypeScript SDK Banner](/img/assets/banner-typescript-temporal.png)

## Best practices

- [Testing](/develop/typescript/best-practices/testing-suite)
- [Debugging](/develop/typescript/best-practices/debugging)
- [Converters and encryption](/develop/typescript/converters-and-encryption)
- [Entity pattern](/develop/typescript/best-practices/entity-pattern)

---

## Testing - TypeScript SDK

The Testing section of the Temporal Application development guide describes the frameworks that facilitate Workflow and integration testing.

In the context of Temporal, you can create these types of automated tests:

- **End-to-end:** Running a Temporal Server and Worker with all its Workflows and Activities; starting and interacting with Workflows from a Client.
- **Integration:** Anything between end-to-end and unit testing.
  - Running Activities with mocked Context and other SDK imports (and usually network requests).
  - Running Workers with mock Activities, and using a Client to start Workflows.
  - Running Workflows with mocked SDK imports.
- **Unit:** Running a piece of Workflow or Activity code (a function or method) and mocking any code it calls.

We generally recommend writing the majority of your tests as integration tests.

Because the test server supports skipping time, use the test server for both end-to-end and integration tests with Workers.

## Test frameworks {/* #test-frameworks */}

Some SDKs have support or examples for popular test frameworks, runners, or libraries.

TypeScript has sample tests for [Jest](https://jestjs.io/) and [Mocha](https://mochajs.org/).

**Jest**

- Minimum Jest version: `27.0.0`
- [Sample test file](https://github.com/temporalio/samples-typescript/blob/main/activities-examples/src/workflows.test.ts)
- [`jest.config.js`](https://github.com/temporalio/samples-typescript/blob/main/activities-examples/jest.config.js) (must use [`testEnvironment: 'node'`](https://jestjs.io/docs/configuration#testenvironment-string); `testEnvironment: 'jsdom'` is not supported)

**Mocha**

- [Sample test file](https://github.com/temporalio/samples-typescript/blob/main/activities-examples/src/mocha/workflows.test.ts)
- Test coverage library: [`@temporalio/nyc-test-coverage`](https://github.com/temporalio/sdk-typescript/tree/main/packages/nyc-test-coverage)

## Testing Activities {/* #test-activities */}

An Activity can be tested with a mock Activity environment, which provides a way to mock the Activity context, listen to Heartbeats, and cancel the Activity.
This behavior allows you to test the Activity in isolation by calling it directly, without needing to create a Worker to run the Activity.

### Run an Activity {/* #run-an-activity */}

If an Activity references its context, you need to mock that context when testing in isolation.

First, create a [`MockActivityEnvironment`](https://typescript.temporal.io/api/classes/testing.MockActivityEnvironment).
The constructor accepts an optional partial Activity [`Info`](https://typescript.temporal.io/api/interfaces/activity.Info) object in case any info fields are needed for the test.

Then use [`MockActivityEnvironment.run()`](https://typescript.temporal.io/api/classes/testing.MockActivityEnvironment#run) to run a function in an Activity [Context](https://typescript.temporal.io/api/classes/activity.Context).

```ts

// A function that takes two numbers and returns a promise that resolves to the sum of the two numbers
// and the current attempt.
async function activityFoo(a: number, b: number): Promise<number> {
  return a + b + activityInfo().attempt;
}

// Create a MockActivityEnvironment with attempt set to 2. Run the activityFoo
// function with parameters 5 and 35. Assert that the result is 42.
const env = new MockActivityEnvironment({ attempt: 2 });
const result = await env.run(activityFoo, 5, 35);
assert.equal(result, 42);
```

### Listen to Heartbeats {/* #listen-to-heartbeats */}

When an Activity sends a Heartbeat, be sure that you can see the Heartbeats in your test code so that you can verify them.

[`MockActivityEnvironment`](https://typescript.temporal.io/api/classes/testing.MockActivityEnvironment) is an [`EventEmitter`](https://nodejs.org/api/events.html#class-eventemitter) that emits a `heartbeat` event that you can use to listen for Heartbeats emitted by the Activity.

When an Activity is run by a Worker, Heartbeats are throttled to avoid overloading the server.
`MockActivityEnvironment`, however, does not throttle Heartbeats.

```ts

async function activityFoo(): Promise<void> {
  heartbeat(6);
}

const env = new MockActivityEnvironment();

env.on('heartbeat', (d: unknown) => {
  assert(d === 6);
});

await env.run(activityFoo);
```

### Cancel an Activity {/* #cancel-an-activity */}

If an Activity is supposed to react to a Cancellation, you can test whether it reacts correctly by canceling it.

[`MockActivityEnvironment`](https://typescript.temporal.io/api/classes/testing.MockActivityEnvironment) exposes a [`.cancel()`](https://typescript.temporal.io/api/classes/testing.MockActivityEnvironment#cancel) method that cancels the Activity Context.

```ts

async function activityFoo(): Promise<void> {
  heartbeat(6);
  // @temporalio/activity's sleep() is Cancellation-aware, which means that on Cancellation,
  // CancelledFailure will be thrown from it.
  await sleep(100);
}

const env = new MockActivityEnvironment();

env.on('heartbeat', (d: unknown) => {
  assert(d === 6);
});

await assert.rejects(env.run(activityFoo), (err) => {
  assert.ok(err instanceof CancelledFailure);
});
```

## Testing Workflows {/* #test-workflows */}

### How to mock Activities {/* #mock-activities */}

Mock the Activity invocation when unit testing your Workflows.

When integration testing Workflows with a Worker, you can mock Activities by providing mock Activity implementations to the Worker.

Implement only the relevant Activities for the Workflow being tested.

```ts

// Creating a mock object of the activities.
const mockActivities: Partial<typeof activities> = {
  makeHTTPRequest: async () => '99',
};

// Creating a worker with the mocked activities.
const worker = await Worker.create({
  activities: mockActivities,
  // ...
});
```

### How to skip time {/* #skip-time */}

Some long-running Workflows can persist for months or even years.
Implementing the test framework allows your Workflow code to skip time and complete your tests in seconds rather than the Workflow's specified amount.

For example, if you have a Workflow sleep for a day, or have an Activity failure with a long retry interval, you don't need to wait the entire length of the sleep period to test whether the sleep function works.
Instead, test the logic that happens after the sleep by skipping forward in time and complete your tests in a timely manner.

The test framework included in most SDKs is an in-memory implementation of Temporal Server that supports skipping time.
Time is a global property of an instance of `TestWorkflowEnvironment`: skipping time (either automatically or manually) applies to all currently running tests.
If you need different time behaviors for different tests, run your tests in a series or with separate instances of the test server.
For example, you could run all tests with automatic time skipping in parallel, and then all tests with manual time skipping in series, and then all tests without time skipping in parallel.

#### Set up time skipping {/* #setting-up */}
