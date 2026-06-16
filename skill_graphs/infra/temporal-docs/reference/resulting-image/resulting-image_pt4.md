The Workflow completing may interrupt the handler before it finishes crucial work and cause client errors when trying retrieve Update results.
Use [`workflow.condition`](https://typescript.temporal.io/api/namespaces/workflow#condition) and [`allHandlersFinished`](https://typescript.temporal.io/api/namespaces/workflow#condition#allhandlersfinished) to address this problem and allow your Workflow to end smoothly:

```typescript
export async function myWorkflow(): Promise<MyWorkflowOutput> {
  await wf.condition(wf.allHandlersFinished);
  return workflowOutput;
}
```

By default, your Worker will log a warning when you allow a Workflow Execution to finish with unfinished handler executions.
You can silence these warnings on a per-handler basis by setting the `unfinishedPolicy` in `SignalHandlerOptions` or `UpdateHandlerOptions` when calling [`workflow.setHandler`](https://typescript.temporal.io/api/namespaces/workflow#sethandler)

See [Finishing handlers before the Workflow completes](/handling-messages#finishing-message-handlers) for more information.

### Use a lock to prevent concurrent handler execution {/* #control-handler-concurrency */}

Concurrent processes can interact in unpredictable ways.
Incorrectly written [concurrent message-passing](/handling-messages#message-handler-concurrency) code may not work correctly when multiple handler instances run simultaneously.
Here's an example of a pathological case:

```typescript
export async function myWorkflow(): Promise<MyWorkflowOutput> {
  let x = 0;
  let y = 0;
  wf.setHandler(mySignal, async () => {
    const data = await myActivity();
    x = data.x;

    // 🐛🐛 Bug!! If multiple instances of this handler are executing
    // concurrently, then there may be times when the Workflow has x from one
    // Activity execution and y from another.
    await wf.sleep(500); // or await anything else

    y = data.y;
  });
  ...
}
```

Coordinating access using a lock (also known as a mutex) corrects this code.
Locking makes sure that only one handler instance can execute a specific section of code at any given time:

```typescript

...

export async function myWorkflow(): Promise<MyWorkflowOutput> {
  let x = 0;
  let y = 0;
  const lock = new Mutex();

  wf.setHandler(mySignal, async () => {
    await lock.runExclusive(async () => {
      const data = await myActivity();
      x = data.x;

      // ✅ OK: node's event loop may switch now to a different handler
      // execution, or to the main workflow function, but no other execution of
      // this handler can run until this execution finishes.
      await wf.sleep(500); // or await anything else

      y = data.y;
    });
  });
  return {
    name: 'hello',
  };
}
```

## Message handler troubleshooting {/* #message-handler-troubleshooting */}

When sending a Signal, Update, or Query to a Workflow, your Client might encounter the following errors:

- **The client can't contact the server**:
  You'll receive a [`client.ServiceError`](https://typescript.temporal.io/api/classes/client.ServiceError) on which the `cause.code` attribute is [gRPC status code](https://grpc.io/docs/guides/status-codes/) 14 `UNAVAILABLE` (after some retries).

- **The workflow does not exist**:
  You'll receive an [`common.WorkflowNotFoundError`](https://typescript.temporal.io/api/classes/common.WorkflowNotFoundError) error.

### Problems when sending a Signal {/* #signal-problems */}

When using Signal, the two errors described above are the only errors that will result from your requests.

For Queries and Updates, the client waits for a response from the Worker and therefore additional errors may occur during the handler Execution by the Worker.

### Problems when sending an Update {/* #update-problems */}

When working with Updates, you may encounter these problems:

- **No Workflow Workers are polling the Task Queue**:
  Your request will be retried by the SDK Client indefinitely.

- **Update failed**: You'll receive a [`client.WorkflowUpdateFailedError`](https://typescript.temporal.io/api/classes/client.WorkflowUpdateFailedError) exception.
  There are two ways this can happen:

  - The Update was rejected by an Update validator defined in the Workflow alongside the Update handler.

  - The Update failed after having been accepted.

  Update failures are like [Workflow failures](/references/failures#errors-in-workflows).
  Issues that cause a Workflow failure in the main method also cause Update failures in the Update handler.
  These might include:

      - A failed Child Workflow
      - A failed Activity (if the Activity retries have been set to a finite number)
      - The Workflow author raising `ApplicationFailure`

- **The handler caused the Workflow Task to fail**:
  A [Workflow Task Failure](/references/failures#errors-in-workflows) causes the server to retry Workflow Tasks indefinitely. What happens to your Update request depends on its stage:
  - If the request hasn't been accepted by the server, you receive a [`client.ServiceError`](https://typescript.temporal.io/api/classes/client.ServiceError) on which the `cause.code` attribute is [gRPC status code](https://grpc.io/docs/guides/status-codes/) 9 `FAILED_PRECONDITION` (after some retries).
  - If the request has been accepted, it is durable.
    Once the Workflow is healthy again after a code deploy, use an [`WorkflowUpdateHandle`](https://typescript.temporal.io/api/interfaces/client.WorkflowUpdateHandle) to fetch the Update result.

- **The Workflow finished while the Update handler execution was in progress**:
  You'll receive a [`client.ServiceError`](https://typescript.temporal.io/api/classes/client.ServiceError) on which the `cause.code` attribute is [gRPC status code](https://grpc.io/docs/guides/status-codes/) 5 `NOT_FOUND`.
  This happens if the Workflow finished while the Update handler execution was in progress, for example because

  - The Workflow was canceled or failed.

  - The Workflow completed normally or continued-as-new and the Workflow author did not [wait for handlers to be finished](/handling-messages#finishing-message-handlers).

### Problems when sending a Query {/* #query-problems */}

When working with Queries, you may encounter these errors:

- **There is no Workflow Worker polling the Task Queue**:
  You'll receive a [`client.ServiceError`](https://typescript.temporal.io/api/classes/client.ServiceError) on which the `cause.code` attribute is [gRPC status code](https://grpc.io/docs/guides/status-codes/) 9 `FAILED_PRECONDITION`.

- **Query failed**:
  You'll receive a [`client.QueryNotRegisteredError`](https://typescript.temporal.io/api/classes/client.QueryNotRegisteredError) exception if something goes wrong during a Query.
  Any error in a Query handler will trigger this error.
  This differs from Signal and Update requests, where errors can lead to Workflow Task Failure instead.

- **The handler caused the Workflow Task to fail.**
  This would happen, for example, if the Query handler blocks the thread for too long without yielding.

## Define Signals and Queries statically or dynamically {/* #dynamic-handler */}

- Handlers for both Signals and Queries can take arguments, which can be used inside `setHandler` logic.
- Only Signal Handlers can mutate state, and only Query Handlers can return values.

* [Define Signals and Queries statically](#static-signals-and-queries)
* [Define Signals and Queries dynamically](#dynamic-signals-and-queries)

### Define Signals and Queries statically {/* #static-signals-and-queries */}

If you know the name of your Signals and Queries upfront, we recommend declaring them outside the Workflow Definition.

<!--SNIPSTART typescript-blocked-workflow-->
[signals-queries/src/workflows.ts](https://github.com/temporalio/samples-typescript/blob/main/signals-queries/src/workflows.ts)
```ts

export const unblockSignal = wf.defineSignal('unblock');
export const isBlockedQuery = wf.defineQuery<boolean>('isBlocked');

export async function unblockOrCancel(): Promise<void> {
  let isBlocked = true;
  wf.setHandler(unblockSignal, () => void (isBlocked = false));
  wf.setHandler(isBlockedQuery, () => isBlocked);
  wf.log.info('Blocked');
  try {
    await wf.condition(() => !isBlocked);
    wf.log.info('Unblocked');
  } catch (err) {
    if (err instanceof wf.CancelledFailure) {
      wf.log.info('Cancelled');
    }
    throw err;
  }
}
```
<!--SNIPEND-->

This technique helps provide type safety because you can export the type signature of the Signal or Query to be called by the Client.

### Define Signals and Queries dynamically {/* #dynamic-signals-and-queries */}

For more flexible use cases, you might want a dynamic Signal (such as a generated ID).
You can handle it in two ways:

- Avoid making it dynamic by collapsing all Signals into one handler and move the ID to the payload.
- Actually make the Signal name dynamic by inlining the Signal definition per handler.

```ts

// "fat handler" solution
wf.setHandler(`genericSignal`, (payload) => {
  switch (payload.taskId) {
    case taskAId:
      // do task A things
      break;
    case taskBId:
      // do task B things
      break;
    default:
      throw new Error('Unexpected task.');
  }
});

// "inline definition" solution
wf.setHandler(wf.defineSignal(`task-${taskAId}`), (payload) => {
  /* do task A things */
});
wf.setHandler(wf.defineSignal(`task-${taskBId}`), (payload) => {
  /* do task B things */
});

// utility "inline definition" helper
const inlineSignal = (signalName, handler) =>
  wf.setHandler(wf.defineSignal(signalName), handler);
inlineSignal(`task-${taskBId}`, (payload) => {
  /* do task B things */
});
```

<details>
  <summary>
    API Design FAQs
  </summary>

**Why not "new Signal" and "new Query"?**

The semantic of `defineSignal` and `defineQuery` is intentional.
They return Signal and Query **definitions**, not unique instances of Signals and Queries themselves
The following is their [entire source code](https://github.com/temporalio/sdk-typescript/blob/fc658d3760e6653aec47732ab17a0062b7dd23fc/packages/workflow/src/workflow.ts#L883-L907):

```ts
/**
 * Define a signal method for a Workflow.
 */
export function defineSignal<Args extends any[] = []>(
  name: string,
): SignalDefinition<Args> {
  return {
    type: 'signal',
    name,
  };
}

/**
 * Define a query method for a Workflow.
 */
export function defineQuery<Ret, Args extends any[] = []>(
  name: string,
): QueryDefinition<Ret, Args> {
  return {
    type: 'query',
    name,
  };
}
```

Signals and Queries are instantiated only in `setHandler` and are specific to particular Workflow Executions.

These distinctions might seem minor, but they model how Temporal works under the hood, because Signals and Queries are messages identified by "just strings" and don't have meaning independent of the Workflow having a listener to handle them.
This will be clearer if you refer to the Client-side APIs.

**Why setHandler and not OTHER_API?**

We named it `setHandler` instead of `subscribe` because a Signal or Query can have only one "handler" at a time, whereas `subscribe` could imply an Observable with multiple consumers and is a higher-level construct.

```ts
wf.setHandler(MySignal, handlerFn1);
wf.setHandler(MySignal, handlerFn2); // replaces handlerFn1
```

If you are familiar with [RxJS](https://rxjs.dev/), you are free to wrap your Signals and Queries into Observables if you want, or you could dynamically reassign the listener based on your business logic or Workflow state.

</details>

---

## Schedules - TypeScript SDK

This page shows how to do the following:

- [Schedule a Workflow](#schedule-a-workflow)
  - [Create a Schedule](#create-schedule)
  - [Backfill a Schedule](#backfill-schedule)
  - [Delete a Schedule](#delete-schedule)
  - [Describe a Schedule](#describe-schedule)
  - [List a Schedule](#list-schedule)
  - [Pause a Schedule](#pause-schedule)
  - [Trigger a Schedule](#trigger-schedule)
  - [Update a Schedule](#update-schedule)
- [Temporal Cron Jobs](#temporal-cron-jobs)
- [Start Delay](#start-delay)

## How to Schedule a Workflow {/* #schedule-a-workflow */}

Scheduling Workflows is a crucial aspect of any automation process, especially when dealing with time-sensitive tasks. By scheduling a Workflow, you can automate repetitive tasks, reduce the need for manual intervention, and ensure timely execution of your business processes.

Use any of the following actions to help Schedule a Workflow Execution and take control over your automation process.

### Create a Schedule {/* #create-schedule */}

The create action enables you to create a new Schedule. When you create a new Schedule, a unique Schedule ID is generated, which you can use to reference the Schedule in other Schedule commands.

:::tip Schedule Auto-Deletion

Once a Schedule has completed creating all its Workflow Executions, the Temporal Service deletes it since it won’t fire again.
The Temporal Service doesn't guarantee when this removal will happen.

:::

<!--SNIPSTART typescript-create-a-scheduled-workflow-->
[schedules/src/start-schedule.ts](https://github.com/temporalio/samples-typescript/blob/main/schedules/src/start-schedule.ts)
```ts
async function run() {
  const config = loadClientConnectConfig();
  const connection = await Connection.connect(config.connectionOptions);
  const client = new Client({ connection });

  // https://typescript.temporal.io/api/classes/client.ScheduleClient#create
  const schedule = await client.schedule.create({
    action: {
      type: 'startWorkflow',
      workflowType: reminder,
      args: ['♻️ Dear future self, please take out the recycling tonight. Sincerely, past you ❤️'],
      taskQueue: 'schedules',
    },
    scheduleId: 'sample-schedule',
    policies: {
      catchupWindow: '1 day',
      overlap: ScheduleOverlapPolicy.ALLOW_ALL,
    },
    spec: {
      intervals: [{ every: '10s' }],
      // or periodic calendar times:
      // calendars: [
      //   {
      //     comment: 'every wednesday at 8:30pm',
      //     dayOfWeek: 'WEDNESDAY',
      //     hour: 20,
      //     minute: 30,
      //   },
      // ],
      // or a single datetime:
      // calendars: [
      //   {
      //     comment: '1/1/23 at 9am',
      //     year: 2023,
      //     month: 1,
      //     dayOfMonth: 1,
      //     hour: 9,
      //   },
      // ],
    },
  });
```
<!--SNIPEND-->

### Backfill a Schedule {/* #backfill-schedule */}

The backfill action executes Actions ahead of their specified time range. This command is useful when you need to execute a missed or delayed Action, or when you want to test the Workflow before its scheduled time.

<!--SNIPSTART typescript-backfill-a-scheduled-workflow-->
[schedules/src/backfill-schedule.ts](https://github.com/temporalio/samples-typescript/blob/main/schedules/src/backfill-schedule.ts)
```ts
function subtractMinutes(minutes: number): Date {
  const now = new Date();
  return new Date(now.getTime() - minutes * 60 * 1000);
}

async function run() {
  const client = new Client({
    connection: await Connection.connect(),
  });

  const backfillOptions: Backfill = {
    start: subtractMinutes(10),
    end: subtractMinutes(9),
    overlap: ScheduleOverlapPolicy.ALLOW_ALL,
  };

  const handle = client.schedule.getHandle('sample-schedule');
  await handle.backfill(backfillOptions);

  console.log(`Schedule is now backfilled.`);
}
```
<!--SNIPEND-->

### Delete a Schedule {/* #delete-schedule */}

The delete action enables you to delete a Schedule. When you delete a Schedule, it does not affect any Workflows that were started by the Schedule.

<!--SNIPSTART typescript-delete-a-scheduled-workflow-->
[schedules/src/delete-schedule.ts](https://github.com/temporalio/samples-typescript/blob/main/schedules/src/delete-schedule.ts)
```ts
async function run() {
  const client = new Client({
    connection: await Connection.connect(),
  });

  const handle = client.schedule.getHandle('sample-schedule');
  await handle.delete();

  console.log(`Schedule is now deleted.`);
}
```
<!--SNIPEND-->

### Describe a Schedule {/* #describe-schedule */}

The describe action shows the current Schedule configuration, including information about past, current, and future Workflow Runs. This command is helpful when you want to get a detailed view of the Schedule and its associated Workflow Runs.

<!--SNIPSTART typescript-describe-a-scheduled-workflow-->
[schedules/src/describe-schedule.ts](https://github.com/temporalio/samples-typescript/blob/main/schedules/src/describe-schedule.ts)
```ts
async function run() {
  const client = new Client({
    connection: await Connection.connect(),
  });

  const handle = client.schedule.getHandle('sample-schedule');

  const result = await handle.describe();

  console.log(`Schedule description: ${JSON.stringify(result)}`);
}
```
<!--SNIPEND-->

### List a Schedule {/* #list-schedule */}

The list action lists all the available Schedules. This command is useful when you want to view a list of all the Schedules and their respective Schedule IDs.

<!--SNIPSTART typescript-list-a-scheduled-workflow-->
[schedules/src/list-schedule.ts](https://github.com/temporalio/samples-typescript/blob/main/schedules/src/list-schedule.ts)
```ts
async function run() {
  const client = new Client({
    connection: await Connection.connect(),
  });

  const schedules = [];

  const scheduleList = client.schedule.list();

  for await (const schedule of scheduleList) {
    schedules.push(schedule);
  }

  console.log(`Schedules are now listed: ${JSON.stringify(schedules)}`);
}
```
<!--SNIPEND-->

### Pause a Schedule {/* #pause-schedule */}

The pause action enables you to pause and unpause a Schedule. When you pause a Schedule, all the future Workflow Runs associated with the Schedule are temporarily stopped. This command is useful when you want to temporarily halt a Workflow due to maintenance or any other reason.

<!--SNIPSTART typescript-pause-a-scheduled-workflow-->
[schedules/src/pause-schedule.ts](https://github.com/temporalio/samples-typescript/blob/main/schedules/src/pause-schedule.ts)
```ts
async function run() {
  const client = new Client({
    connection: await Connection.connect(),
  });

  const handle = client.schedule.getHandle('sample-schedule');
  await handle.pause();

  console.log(`Schedule is now paused.`);
}
```
<!--SNIPEND-->

### Trigger a Schedule {/* #trigger-schedule */}

The trigger action triggers an immediate action with a given Schedule. By default, this action is subject to the Overlap Policy of the Schedule. This command is helpful when you want to execute a Workflow outside of its scheduled time.

<!--SNIPSTART typescript-trigger-a-scheduled-workflow-->
[schedules/src/trigger-schedule.ts](https://github.com/temporalio/samples-typescript/blob/main/schedules/src/trigger-schedule.ts)
```ts
async function run() {
  const client = new Client({
    connection: await Connection.connect(),
  });

  const handle = client.schedule.getHandle('sample-schedule');

  await handle.trigger();

  console.log(`Schedule is now triggered.`);
}
```
<!--SNIPEND-->

### Update a Schedule {/* #update-schedule */}

The update action enables you to update an existing Schedule. This command is useful when you need to modify the Schedule's configuration, such as changing the start time, end time, or interval.

<!--SNIPSTART typescript-update-a-scheduled-workflow-->
[schedules/src/update-schedule.ts](https://github.com/temporalio/samples-typescript/blob/main/schedules/src/update-schedule.ts)
```ts
const updateSchedule = (
  input: ScheduleDescription,
): ScheduleUpdateOptions<ScheduleOptionsStartWorkflowAction<Workflow>> => {
  const scheduleAction = input.action;

  scheduleAction.args = ['my updated schedule arg'];

  return { ...input, ...scheduleAction };
};

async function run() {
  const client = new Client({
    connection: await Connection.connect(),
  });

  const handle = client.schedule.getHandle('sample-schedule');

  await handle.update(updateSchedule);

  console.log(`Schedule is now updated.`);
}
```
<!--SNIPEND-->

## Temporal Cron Jobs {/* #temporal-cron-jobs */}

:::caution Cron support is not recommended

We recommend using [Schedules](https://docs.temporal.io/schedule) instead of Cron Jobs.
Schedules were built to provide a better developer experience, including more configuration options and the ability to update or pause running Schedules.

:::

A [Temporal Cron Job](/cron-job) is the series of Workflow Executions that occur when a Cron Schedule is provided in the call to spawn a Workflow Execution.

A Cron Schedule is provided as an option when the call to spawn a Workflow Execution is made.

You can set each Workflow to repeat on a schedule with the `cronSchedule` option:

```typescript
const handle = await client.workflow.start(scheduledWorkflow, {
  // ...
  cronSchedule: '* * * * *', // start every minute
});
```

Temporal Workflow Schedule Cron strings follow this format:

```
┌───────────── minute (0 - 59)
│ ┌───────────── hour (0 - 23)
│ │ ┌───────────── day of the month (1 - 31)
│ │ │ ┌───────────── month (1 - 12)
│ │ │ │ ┌───────────── day of the week (0 - 6) (Sunday to Saturday)
│ │ │ │ │
* * * * *
```

## Start Delay {/* #start-delay */}

**How to use Start Delay**

Use the `startDelay` to schedule a Workflow Execution at a specific one-time future point rather than on a recurring schedule.

You may specify the `startDelay` option on either the [`client.workflow.start()`](https://typescript.temporal.io/api/classes/client.WorkflowClient#start) or [`client.workflow.execute()`](https://typescript.temporal.io/api/classes/client.WorkflowClient#execute) methods of a Workflow Client.
For example:

```typescript
const handle = await client.workflow.start(someWorkflow, {
  // ...
  startDelay: '2 hours',
});
```

---

## Workflow Timeouts - TypeScript SDK

This page shows how to do the following:

- [Raise and Handle Exceptions](#exception-handling)
- [Deliberately Fail Workflows](#workflow-failure)
- [Workflow Timeouts](#workflow-timeouts)
- [Workflow retries](#workflow-retries)

## Raise and Handle Exceptions {/* #exception-handling */}

In each Temporal SDK, error handling is implemented idiomatically, following the conventions of the language.
Temporal uses several different error classes internally — for example, [`CancelledFailure`](https://typescript.temporal.io/api/classes/common.CancelledFailure) in the Typescript SDK, to handle a Workflow cancellation.
You should not raise or otherwise implement these manually, as they are tied to Temporal platform logic.

The one Temporal error class that you will typically raise deliberately is [`ApplicationFailure`](https://typescript.temporal.io/api/classes/common.ApplicationFailure).
In fact, *any* other exceptions that are raised from your Typescript code in a Temporal Activity will be converted to an `ApplicationError` internally.
This way, an error's type, severity, and any additional details can be sent to the Temporal Service, indexed by the Web UI, and even serialized across language boundaries.

In other words, these two code samples do the same thing:

```typescript
class InvalidChargeError extends Error {
    constructor(message: string) {
        super(message);
        this.name = "InvalidChargeError";
        Object.setPrototypeOf(this, CustomError.prototype);
    }
}

if (chargeAmount < 0) {
  throw new InvalidChargeError(`Invalid charge amount: ${chargeAmount} (must be above zero)`);
}
```

```typescript
if (chargeAmount < 0) {
  throw ApplicationFailure.create({
    message: `Invalid charge amount: ${chargeAmount} (must be above zero)`,
    type: 'InvalidChargeError',
  });
}
```

Depending on your implementation, you may decide to use either method.
One reason to use the Temporal `ApplicationFailure` class is because it allows you to set an additional `non_retryable` parameter.
This way, you can decide whether an error should not be retried automatically by Temporal.
This can be useful for deliberately failing a Workflow due to bad input data, rather than waiting for a timeout to elapse:

```typescript
if (chargeAmount < 0) {
  throw ApplicationFailure.create({
    message: `Invalid charge amount: ${chargeAmount} (must be above zero)`,
    nonRetryable: true
  });
}
```

You can alternately specify a list of errors that are non-retryable in your Activity [Retry Policy](/develop/typescript/activities/timeouts#activity-retries).

## Failing Workflows {/* #workflow-failure */}

One of the core design principles of Temporal is that an Activity Failure will never directly cause a Workflow Failure — a Workflow should never return as Failed unless deliberately.
The default retry policy associated with Temporal Activities is to retry them until reaching a certain timeout threshold.
Activities will not actually *return* a failure to your Workflow until this condition or another non-retryable condition is met.
At this point, you can decide how to handle an error returned by your Activity the way you would in any other program.
For example, you could implement a [Saga Pattern](https://github.com/temporalio/samples-typescript/tree/main/saga) that uses `try` and `catch` blocks to "unwind" some of the steps your Workflow has performed up to the point of Activity Failure.

**You will only fail a Workflow by manually raising an `ApplicationFailure` from the Workflow code.**
You could do this in response to an Activity Failure, if the failure of that Activity means that your Workflow should not continue:
