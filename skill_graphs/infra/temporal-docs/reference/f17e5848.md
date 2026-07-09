}
```

</details>

The Workflow Context Logger tries to avoid reemitting log messages on Workflow Replays.

{/*

#### Customizing Workflow logging using `WorkflowOutboundCallsInterceptor`

FIXME(JWH): Quick introduction to `WorkflowOutboundCallsInterceptor.getLogAttributes()`.
*/}

#### Limitations of Workflow logs

Internally, Workflow logging uses Sinks, and is consequently subject to the same limitations as Sinks.
Notably, logged objects must be serializable using the V8 serialization.

{/* FIXME(JWH): Add more details and link to actual Sinks documentation */}

### What is the Runtime's Logger

A Temporal Worker may emit logs in various ways, including:

- Messages emitted using the [Workflow Context Logger](#logging);
- Messages emitted using the [Activity Context Logger](#logging-from-activities);
- Messages emitted by the TypeScript SDK Worker itself;
- Messages emitted by the underlying Temporal Core SDK (native code).

All of these messages are internally routed to a single logger object, called the Runtime's Logger.
By default, the Runtime's Logger simply writes messages to the console (i.e. the process's `STDOUT`).

#### How to customize the Runtime's Logger

A custom Runtime Logger may be registered when the SDK `Runtime` is instantiated. This is done only once per process.

To register a custom Runtime Logger, you must explicitly instantiate the Runtime, using the [`Runtime.install()`](https://typescript.temporal.io/api/classes/worker.Runtime/#install) function.
For example:

```typescript

  DefaultLogger,
  makeTelemetryFilterString,
  Runtime,
} from '@temporalio/worker';

// This is your custom Logger.
const logger = new DefaultLogger('WARN', ({ level, message }) => {
  console.log(`Custom logger: ${level} — ${message}`);
});

Runtime.install({
  logger,
  // The following block is optional, but generally desired.
  // It allows capturing log messages emitted by the underlying Temporal Core SDK (native code).
  // The Telemetry Filter String determine the desired verboseness of messages emitted by the
  // Temporal Core SDK itself ("core"), and by other native libraries ("other").
  telemetryOptions: {
    logging: {
      filter: makeTelemetryFilterString({ core: 'INFO', other: 'INFO' }),
      forward: {},
    },
  },
});
```

A common use case for this is to write log messages to a file to be picked up by a collector service, such as the [Datadog Agent](https://docs.datadoghq.com/logs/log_collection/nodejs/?tab=winston30).
For example:

```typescript

  DefaultLogger,
  makeTelemetryFilterString,
  Runtime,
} from '@temporalio/worker';

const logger = winston.createLogger({
  level: 'info',
  format: winston.format.json(),
  transports: [new transports.File({ filename: '/path/to/worker.log' })],
});

Runtime.install({
  logger,
  // The following block is optional, but generally desired.
  // It allows capturing log messages emitted by the underlying Temporal Core SDK (native code).
  // The Telemetry Filter String determine the desired verboseness of messages emitted by the
  // Temporal Core SDK itself ("core"), and by other native libraries ("other").
  telemetryOptions: {
    logging: {
      filter: makeTelemetryFilterString({ core: 'INFO', other: 'INFO' }),
      forward: {},
    },
  },
});
```

{/* FIXME(JWH): Everything below this point must be revisited and moved to a distinct section (Sinks). */}

### Implementing custom Logging-like features based on Workflow Sinks

Sinks enable one-way export of logs, metrics, and traces from the Workflow isolate to the Node.js environment.

{/*
Workflows in Temporal may be replayed from the beginning of their history when resumed. In order for Temporal to recreate the exact state Workflow code was in, the code is required to be fully deterministic. To prevent breaking determinism, in the TypeScript SDK, Workflow code runs in an isolated execution environment and may not use any of the Node.js APIs or communicate directly with the outside world. */}

Sinks are written as objects with methods.
Similar to Activities, they are declared in the Worker and then proxied in Workflow code, and it helps to share types between both.

#### Comparing Sinks and Activities

Sinks are similar to Activities in that they are both registered on the Worker and proxied into the Workflow.
However, they differ from Activities in important ways:

- A sink function doesn't return any value back to the Workflow and cannot be awaited.
- A sink call isn't recorded in the Event History of a Workflow Execution (no timeouts or retries).
- A sink function _always_ runs on the same Worker that runs the Workflow Execution it's called from.

#### Declare the sink interface

Explicitly declaring a sink's interface is optional but is useful for ensuring type safety in subsequent steps:

<!--SNIPSTART typescript-logger-sink-interface-->
[packages/test/src/workflows/log-sink-tester.ts](https://github.com/temporalio/sdk-typescript/blob/main/packages/test/src/workflows/log-sink-tester.ts)
```ts

export interface CustomLoggerSinks extends Sinks {
  customLogger: {
    info(message: string): void;
  };
}
```
<!--SNIPEND-->

#### Implement sinks

Implementing sinks is a two-step process.

Implement and inject the Sink function into a Worker

<!--SNIPSTART typescript-logger-sink-worker-->
[sinks/src/worker.ts](https://github.com/temporalio/samples-typescript/blob/main/sinks/src/worker.ts)
```ts

async function main() {
  const sinks: InjectedSinks<MySinks> = {
    alerter: {
      alert: {
        fn(workflowInfo, message) {
          console.log('sending SMS alert!', {
            workflowId: workflowInfo.workflowId,
            workflowRunId: workflowInfo.runId,
            message,
          });
        },
        callDuringReplay: false, // The default
      },
    },
  };
  const worker = await Worker.create({
    workflowsPath: require.resolve('./workflows'),
    taskQueue: 'sinks',
    sinks,
  });
  await worker.run();
  console.log('Worker gracefully shutdown');
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
```
<!--SNIPEND-->

- Sink function implementations are passed as an object into [WorkerOptions](https://typescript.temporal.io/api/interfaces/worker.WorkerOptions/#sinks).
- You can specify whether you want the injected function to be called during Workflow replay by setting the `callDuringReplay` option.

#### Proxy and call a sink function from a Workflow

<!--SNIPSTART typescript-logger-sink-workflow-->
[packages/test/src/workflows/log-sample.ts](https://github.com/temporalio/sdk-typescript/blob/main/packages/test/src/workflows/log-sample.ts)
```ts

export async function logSampleWorkflow(): Promise<void> {
  wf.log.info('Workflow execution started');
}
```
<!--SNIPEND-->

Some important features of the [InjectedSinkFunction](https://typescript.temporal.io/api/interfaces/worker.InjectedSinkFunction) interface:

- **Injected WorkflowInfo argument:** The first argument of a Sink function implementation is a [`workflowInfo` object](https://typescript.temporal.io/api/interfaces/workflow.WorkflowInfo/) that contains useful metadata.
- **Limited arguments types:** The remaining Sink function arguments are copied between the sandbox and the Node.js environment using the [structured clone algorithm](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Structured_clone_algorithm).
- **No return value:** To prevent breaking determinism, Sink functions cannot return values to the Workflow.

**Advanced: Performance considerations and non-blocking Sinks**

The injected sink function contributes to the overall Workflow Task processing duration.

- If you have a long-running sink function, such as one that tries to communicate with external services, you might start seeing Workflow Task timeouts.
- The effect is multiplied when using `callDuringReplay: true` and replaying long Workflow histories because the Workflow Task timer starts when the first history page is delivered to the Worker.

### How to provide a custom logger {/* #custom-logger */}

Use a custom logger for logging.

#### Logging in Workers and Clients

The Worker comes with a default logger, which defaults to log any messages with level `INFO` and higher to `STDERR` using `console.error`.
The following [log levels](https://typescript.temporal.io/api/namespaces/worker#loglevel) are listed in increasing order of severity.

#### Customizing the default logger

Temporal uses a [`DefaultLogger`](https://typescript.temporal.io/api/classes/worker.DefaultLogger/) that implements the basic interface:

```ts

const logger = new DefaultLogger('WARN', ({ level, message }) => {
  console.log(`Custom logger: ${level} — ${message}`);
});
Runtime.install({ logger });
```

The previous code example sets the default logger to log only messages with level `WARN` and higher.

#### Accumulate logs for testing and reporting

```ts

const logs: LogEntry[] = [];
const logger = new DefaultLogger(LogLevel.TRACE, (entry) => logs.push(entry));

logger.debug('hey', { a: 1 });
logger.info('ho');
logger.warn('lets', { a: 1 });
logger.error('go');
```

A common logging use case is logging to a file to be picked up by a collector like the [Datadog Agent](https://docs.datadoghq.com/logs/log_collection/nodejs/?tab=winston30).

```ts

const logger = winston.createLogger({
  level: 'info',
  format: winston.format.json(),
  transports: [new transports.File({ filename: '/path/to/worker.log' })],
});
Runtime.install({ logger });
```

## Visibility APIs {/* #visibility */}

The term Visibility, within the Temporal Platform, refers to the subsystems and APIs that enable an operator to view Workflow Executions that currently exist within a Temporal Service.

### How to use Search Attributes {/* #search-attributes */}

The typical method of retrieving a Workflow Execution is by its Workflow Id.

However, sometimes you'll want to retrieve one or more Workflow Executions based on another property. For example, imagine you want to get all Workflow Executions of a certain type that have failed within a time range, so that you can start new ones with the same arguments.

You can do this with [Search Attributes](/search-attribute).

- [Default Search Attributes](/search-attribute#default-search-attribute) like `WorkflowType`, `StartTime` and `ExecutionStatus` are automatically added to Workflow Executions.
- [Custom Search Attributes](/search-attribute#custom-search-attribute) can contain their own domain-specific data (like `customerId` or `numItems`).

The steps to using custom Search Attributes are:

- Create a new Search Attribute in your Temporal Service using `temporal operator search-attribute create` or the Cloud UI.
- Set the value of the Search Attribute for a Workflow Execution:
  - On the Client by including it as an option when starting the Execution.
  - In the Workflow by calling `UpsertSearchAttributes`.
- Read the value of the Search Attribute:
  - On the Client by calling `DescribeWorkflow`.
  - In the Workflow by looking at `WorkflowInfo`.
- Query Workflow Executions by the Search Attribute using a [List Filter](/list-filter):
  - [With the Temporal CLI](/cli/command-reference/workflow#list).
  - In code by calling `ListWorkflowExecutions`.

Here is how to query Workflow Executions:

Use [`WorkflowService.listWorkflowExecutions`](https://typescript.temporal.io/api/classes/proto.temporal.api.workflowservice.v1.WorkflowService-1#listworkflowexecutions):

```typescript

const connection = await Connection.connect();
const response = await connection.workflowService.listWorkflowExecutions({
  query: `ExecutionStatus = "Running"`,
});
```

where `query` is a [List Filter](/list-filter).

### How to set custom Search Attributes {/* #custom-search-attributes */}

After you've created custom Search Attributes in your Temporal Service (using `temporal operator search-attribute create` or the Cloud UI), you can set the values of the custom Search Attributes when starting a Workflow.

Use [`WorkflowOptions.searchAttributes`](https://typescript.temporal.io/api/interfaces/client.WorkflowOptions#searchattributes).

<!--SNIPSTART typescript-search-attributes-client-->
[search-attributes/src/client.ts](https://github.com/temporalio/samples-typescript/blob/main/search-attributes/src/client.ts)
```ts
const handle = await client.workflow.start(example, {
  taskQueue: 'search-attributes',
  workflowId: 'search-attributes-example-0',
  searchAttributes: {
    CustomIntField: [2],
    CustomKeywordListField: ['keywordA', 'keywordB'],
    CustomBoolField: [true],
    CustomDatetimeField: [new Date()],
    CustomTextField: [
      'String field is for text. When queried, it will be tokenized for partial match. StringTypeField cannot be used in Order By',
    ],
  },
});

const { searchAttributes } = await handle.describe();
```
<!--SNIPEND-->

The type of `searchAttributes` is `Record<string, string[] | number[] | boolean[] | Date[]>`.

### How to upsert Search Attributes {/* #upsert-search-attributes */}

You can upsert Search Attributes to add or update Search Attributes from within Workflow code.

Inside a Workflow, we can read from [`WorkflowInfo.searchAttributes`](https://typescript.temporal.io/api/interfaces/workflow.WorkflowInfo#searchattributes) and call [`upsertSearchAttributes`](https://typescript.temporal.io/api/namespaces/workflow#upsertsearchattributes):

<!--SNIPSTART typescript-search-attributes-workflow -->
[search-attributes/src/workflows.ts](https://github.com/temporalio/samples-typescript/blob/main/search-attributes/src/workflows.ts)
```ts
export async function example(): Promise<SearchAttributes> {
  const customInt = (workflowInfo().searchAttributes.CustomIntField?.[0] as number) || 0;
  upsertSearchAttributes({
    // overwrite the existing CustomIntField: [2]
    CustomIntField: [customInt + 1],

    // delete the existing CustomBoolField: [true]
    CustomBoolField: [],

    // add a new value
    CustomDoubleField: [3.14],
  });
  return workflowInfo().searchAttributes;
}
```
<!--SNIPEND-->

### How to remove a Search Attribute from a Workflow {/* #remove-search-attribute */}

To remove a Search Attribute that was previously set, set it to an empty array: `[]`.

```typescript

async function yourWorkflow() {
  upsertSearchAttributes({ CustomIntField: 1 });

// ... later, to remove:
upsertSearchAttributes({ CustomIntField: null });
}
```

---

## Set up your local with the Typescript SDK
