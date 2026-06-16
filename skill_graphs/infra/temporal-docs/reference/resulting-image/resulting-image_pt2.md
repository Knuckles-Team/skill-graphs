behaviors you can specify. By default, everything runs in the "root" scope.

Scopes are created using the [CancellationScope](https://typescript.temporal.io/api/classes/workflow.CancellationScope)
constructor or one of three static helpers:

- [cancellable(fn)](https://typescript.temporal.io/api/classes/workflow.CancellationScope#cancellable-1): Children are
  automatically cancelled when their containing scope is cancelled.
  - Equivalent to `new CancellationScope().run(fn)`.
- [nonCancellable(fn)](https://typescript.temporal.io/api/classes/workflow.CancellationScope#noncancellable):
  Cancellation does not propagate to children.
  - Equivalent to `new CancellationScope({ cancellable: false }).run(fn)`.
- [withTimeout(timeoutMs, fn)](https://typescript.temporal.io/api/classes/workflow.CancellationScope#withtimeout): If a
  timeout triggers before `fn` resolves, the scope is cancelled, triggering cancellation of any enclosed operations,
  such as Activities and Timers.
  - Equivalent to `new CancellationScope({ cancellable: true, timeout: timeoutMs }).run(fn)`.

Cancellations are applied to cancellation scopes, which can encompass an entire Workflow or just part of one. Scopes can
be nested, and cancellation propagates from outer scopes to inner ones. A Workflow's `main` function runs in the
outermost scope. Cancellations are handled by catching `CancelledFailure`s thrown by cancelable operations.

`CancellationScope.run()` and the static helpers mentioned earlier return native JavaScript promises, so you can use the
familiar Promise APIs like `Promise.all` and `Promise.race` to model your asynchronous logic. You can also use the
following APIs:

- `CancellationScope.current()`: Get the current scope.
- `scope.cancel()`: Cancel all operations inside a `scope`.
- `scope.run(fn)`: Run an async function within a `scope` and return the result of `fn`.
- `scope.cancelRequested`: A promise that resolves when a scope cancellation is requested, such as when Workflow code
  calls `cancel()` or the entire Workflow is cancelled by an external client.

When a `CancellationScope` is cancelled, it propagates cancellation in any child scopes and of any cancelable operations
created within it, such as the following:

- Activities
- Timers (created with the [sleep](https://typescript.temporal.io/api/namespaces/workflow#sleep) function)
- [Triggers](https://typescript.temporal.io/api/classes/workflow.Trigger)

### CancelledFailure

Timers and triggers throw [CancelledFailure](https://typescript.temporal.io/api/classes/common.CancelledFailure) when
cancelled; Activities and Child Workflows throw `ActivityFailure` and `ChildWorkflowFailure` with cause set to
`CancelledFailure`. One exception is when an Activity or Child Workflow is scheduled in an already cancelled scope (or
Workflow). In this case, they propagate the `CancelledFailure` that was thrown to cancel the scope.

To simplify checking for cancellation, use the
[isCancellation(err)](https://typescript.temporal.io/api/namespaces/workflow#iscancellation) function.

### Internal cancellation example

<!--SNIPSTART typescript-cancel-a-timer-from-workflow-->
[packages/test/src/workflows/cancel-timer-immediately.ts](https://github.com/temporalio/sdk-typescript/blob/main/packages/test/src/workflows/cancel-timer-immediately.ts)
```ts

export async function cancelTimer(): Promise<void> {
  // Timers and Activities are automatically cancelled when their containing scope is cancelled.
  try {
    await CancellationScope.cancellable(async () => {
      const promise = sleep(1); // <-- Will be cancelled because it is attached to this closure's scope
      CancellationScope.current().cancel();
      await promise; // <-- Promise must be awaited in order for `cancellable` to throw
    });
  } catch (e) {
    if (e instanceof CancelledFailure) {
      console.log('Timer cancelled 👍');
    } else {
      throw e; // <-- Fail the workflow
    }
  }
}
```
<!--SNIPEND-->

Alternatively, the preceding can be written as the following.

<!--SNIPSTART typescript-cancel-a-timer-from-workflow-alternative-impl-->
[packages/test/src/workflows/cancel-timer-immediately-alternative-impl.ts](https://github.com/temporalio/sdk-typescript/blob/main/packages/test/src/workflows/cancel-timer-immediately-alternative-impl.ts)
```ts

export async function cancelTimerAltImpl(): Promise<void> {
  try {
    const scope = new CancellationScope();
    const promise = scope.run(() => sleep(1));
    scope.cancel(); // <-- Cancel the timer created in scope
    await promise; // <-- Throws CancelledFailure
  } catch (e) {
    if (e instanceof CancelledFailure) {
      console.log('Timer cancelled 👍');
    } else {
      throw e; // <-- Fail the workflow
    }
  }
}
```
<!--SNIPEND-->

### External cancellation example

The following code shows how to handle Workflow cancellation by an external client while an Activity is running.

{/* TODO: add a sample here of how this Workflow could be cancelled using a WorkflowHandle */}

<!--SNIPSTART typescript-handle-external-workflow-cancellation-while-activity-running-->
[packages/test/src/workflows/handle-external-workflow-cancellation-while-activity-running.ts](https://github.com/temporalio/sdk-typescript/blob/main/packages/test/src/workflows/handle-external-workflow-cancellation-while-activity-running.ts)
```ts

const { httpPostJSON, cleanup } = proxyActivities<typeof activities>({
  startToCloseTimeout: '10m',
});

export async function handleExternalWorkflowCancellationWhileActivityRunning(url: string, data: any): Promise<void> {
  try {
    await httpPostJSON(url, data);
  } catch (err) {
    if (isCancellation(err)) {
      console.log('Workflow cancelled');
      // Cleanup logic must be in a nonCancellable scope
      // If we'd run cleanup outside of a nonCancellable scope it would've been cancelled
      // before being started because the Workflow's root scope is cancelled.
      await CancellationScope.nonCancellable(() => cleanup(url));
    }
    throw err; // <-- Fail the Workflow
  }
}
```
<!--SNIPEND-->

### nonCancellable example

`CancellationScope.nonCancellable` prevents cancellation from propagating to children.

<!--SNIPSTART typescript-non-cancellable-shields-children-->
[activities-cancellation-heartbeating/src/cancellation-scopes.ts](https://github.com/temporalio/samples-typescript/blob/main/activities-cancellation-heartbeating/src/cancellation-scopes.ts)
```ts
export async function nonCancellable(url: string): Promise<any> {
  // Prevent Activity from being cancelled and await completion.
  // Note that the Workflow is completely oblivious and impervious to cancellation in this example.
  return CancellationScope.nonCancellable(() => httpGetJSON(url));
}
```
<!--SNIPEND-->

### withTimeout example

A common operation is to cancel one or more Activities if a deadline elapses. `withTimeout` creates a
`CancellationScope` that is automatically cancelled after a timeout.

<!--SNIPSTART typescript-multiple-activities-single-timeout-workflow-->
[packages/test/src/workflows/multiple-activities-single-timeout.ts](https://github.com/temporalio/sdk-typescript/blob/main/packages/test/src/workflows/multiple-activities-single-timeout.ts)
```ts

export function multipleActivitiesSingleTimeout(urls: string[], timeoutMs: number): Promise<any> {
  const { httpGetJSON } = proxyActivities<typeof activities>({
    startToCloseTimeout: timeoutMs,
  });

  // If timeout triggers before all activities complete
  // the Workflow will fail with a CancelledError.
  return CancellationScope.withTimeout(timeoutMs, () => Promise.all(urls.map((url) => httpGetJSON(url))));
}
```
<!--SNIPEND-->

### scope.cancelRequested

You can await `cancelRequested` to make a Workflow aware of cancellation while waiting on `nonCancellable` scopes.

<!--SNIPSTART typescript-cancel-requested-with-non-cancellable-->
[packages/test/src/workflows/cancel-requested-with-non-cancellable.ts](https://github.com/temporalio/sdk-typescript/blob/main/packages/test/src/workflows/cancel-requested-with-non-cancellable.ts)
```ts

const { httpGetJSON } = proxyActivities<typeof activities>({
  startToCloseTimeout: '10m',
});

export async function resumeAfterCancellation(url: string): Promise<any> {
  let result: any = undefined;
  const scope = new CancellationScope({ cancellable: false });
  const promise = scope.run(() => httpGetJSON(url));
  try {
    result = await Promise.race([scope.cancelRequested, promise]);
  } catch (err) {
    if (!(err instanceof CancelledFailure)) {
      throw err;
    }
    // Prevent Workflow from completing so Activity can complete
    result = await promise;
  }
  return result;
}
```
<!--SNIPEND-->

### Cancellation scopes and callbacks

Callbacks are not particularly useful in Workflows because all meaningful asynchronous operations return promises. In
the rare case that code uses callbacks and needs to handle cancellation, a callback can consume the
`CancellationScope.cancelRequested` promise.

<!--SNIPSTART typescript-cancellation-scopes-with-callbacks-->
[packages/test/src/workflows/cancellation-scopes-with-callbacks.ts](https://github.com/temporalio/sdk-typescript/blob/main/packages/test/src/workflows/cancellation-scopes-with-callbacks.ts)
```ts

function doSomething(callback: () => any) {
  setTimeout(callback, 10);
}

export async function cancellationScopesWithCallbacks(): Promise<void> {
  await new Promise<void>((resolve, reject) => {
    doSomething(resolve);
    CancellationScope.current().cancelRequested.catch(reject);
  });
}
```
<!--SNIPEND-->

### Nesting cancellation scopes

You can achieve complex flows by nesting cancellation scopes.

<!--SNIPSTART typescript-nested-cancellation-scopes-->
[packages/test/src/workflows/nested-cancellation.ts](https://github.com/temporalio/sdk-typescript/blob/main/packages/test/src/workflows/nested-cancellation.ts)
```ts

const { setup, httpPostJSON, cleanup } = proxyActivities<typeof activities>({
  startToCloseTimeout: '10m',
});

export async function nestedCancellation(url: string): Promise<void> {
  await CancellationScope.cancellable(async () => {
    await CancellationScope.nonCancellable(() => setup());
    try {
      await CancellationScope.withTimeout(1000, () => httpPostJSON(url, { some: 'data' }));
    } catch (err) {
      if (isCancellation(err)) {
        await CancellationScope.nonCancellable(() => cleanup(url));
      }
      throw err;
    }
  });
}
```
<!--SNIPEND-->

### Sharing promises between scopes

Operations like Timers and Activities are cancelled by the cancellation scope they were created in. Promises returned by
these operations can be awaited in different scopes.

<!--SNIPSTART typescript-shared-promise-scopes-->
[activities-cancellation-heartbeating/src/cancellation-scopes.ts](https://github.com/temporalio/samples-typescript/blob/main/activities-cancellation-heartbeating/src/cancellation-scopes.ts)
```ts
export async function sharedScopes(): Promise<any> {
  // Start activities in the root scope
  const p1 = httpGetJSON('http://url1.ninja');
  const p2 = httpGetJSON('http://url2.ninja');

  const scopePromise = CancellationScope.cancellable(async () => {
    const first = await Promise.race([p1, p2]);
    // Does not cancel activity1 or activity2 as they're linked to the root scope
    CancellationScope.current().cancel();
    return first;
  });
  return await scopePromise;
  // The Activity that did not complete will effectively be cancelled when
  // Workflow completes unless the Activity is awaited:
  // await Promise.all([p1, p2]);
}
```
<!--SNIPEND-->

<!--SNIPSTART typescript-shield-awaited-in-root-scope-->
[activities-cancellation-heartbeating/src/cancellation-scopes.ts](https://github.com/temporalio/samples-typescript/blob/main/activities-cancellation-heartbeating/src/cancellation-scopes.ts)
```ts
export async function shieldAwaitedInRootScope(): Promise<any> {
  let p: Promise<any> | undefined = undefined;

  await CancellationScope.nonCancellable(async () => {
    p = httpGetJSON('http://example.com'); // <-- Start activity in nonCancellable scope without awaiting completion
  });
  // Activity is shielded from cancellation even though it is awaited in the cancellable root scope
  return p;
}
```
<!--SNIPEND-->

---

## Cancel a Workflow - TypeScript SDK

## Cancel an Activity from a Workflow {/* #cancel-an-activity */}

Canceling an Activity from within a Workflow requires that the Activity Execution sends Heartbeats and sets a Heartbeat
Timeout. If the Heartbeat is not invoked, the Activity cannot receive a cancellation request. When any non-immediate
Activity is executed, the Activity Execution should send Heartbeats and set a
[Heartbeat Timeout](/encyclopedia/detecting-activity-failures#heartbeat-timeout) to ensure that the server knows it is
still working.

When an Activity is canceled, an error is raised in the Activity at the next available opportunity. If cleanup logic
needs to be performed, it can be done in a `finally` clause or inside a caught cancel error. However, for the Activity
to appear canceled the exception needs to be re-thrown.

:::note

Unlike regular Activities, [Local Activities](/local-activity) can be canceled if they don't send Heartbeats. Local
Activities are handled locally, and all the information needed to handle the cancellation logic is available in the same
Worker process.

:::

## Reset a Workflow Execution {/* #reset */}

Resetting a Workflow Execution terminates the current Workflow Execution and starts a new Workflow Execution from a
point you specify in its Event History. Use reset when a Workflow is blocked due to a non-deterministic error or other
issues that prevent it from completing.

When you reset a Workflow, the Event History up to the reset point is copied to the new Workflow Execution, and the
Workflow resumes from that point with the current code. Reset only works if you've fixed the underlying issue, such as
removing non-deterministic code. Any progress made after the reset point will be discarded. Provide a reason when
resetting, as it will be recorded in the Event History.

<Tabs>

<TabItem value="web-ui" label="Web UI">

1. Navigate to the Workflow Execution details page,
2. Click the **Reset** button in the top right dropdown menu,
3. Select the Event ID to reset to,
4. Provide a reason for the reset,
5. Confirm the reset.

The Web UI shows available reset points and creates a link to the new Workflow Execution after the reset completes.

</TabItem>

<TabItem value="cli" label="Temporal CLI">

Use the `temporal workflow reset` command to reset a Workflow Execution:

```bash
temporal workflow reset \
    --workflow-id <workflow-id> \
    --event-id <event-id> \
    --reason "Reason for reset"
```

For example:

```bash
temporal workflow reset \
    --workflow-id my-background-check \
    --event-id 4 \
    --reason "Fixed non-deterministic code"
```

By default, the command resets the latest Workflow Execution in the `default` Namespace. Use `--run-id` to reset a
specific run. Use `--namespace` to specify a different Namespace:

```bash
temporal workflow reset \
    --workflow-id my-background-check \
    --event-id 4 \
    --reason "Fixed non-deterministic code" \
    --namespace my-namespace \
    --tls-cert-path /path/to/cert.pem \
    --tls-key-path /path/to/key.pem
```

Monitor the new Workflow Execution after resetting to ensure it completes successfully.

</TabItem>

</Tabs>

---

## Child Workflows - TypeScript SDK

## How to start a Child Workflow Execution {/* #child-workflows */}

A [Child Workflow Execution](/child-workflows) is a Workflow Execution that is scheduled from within another Workflow using a Child Workflow API.

When using a Child Workflow API, Child Workflow related Events ([StartChildWorkflowExecutionInitiated](/references/events#startchildworkflowexecutioninitiated), [ChildWorkflowExecutionStarted](/references/events#childworkflowexecutionstarted), [ChildWorkflowExecutionCompleted](/references/events#childworkflowexecutioncompleted), etc.) are logged in the Workflow Execution Event History.

The [ChildWorkflowExecutionStarted](/references/events#childworkflowexecutionstarted) Event must be logged to the Event History before the Parent Workflow completes to ensure the Child Workflow has started.
In TypeScript, awaiting `startChild()` or `executeChild()` internally waits for this Event before returning, so the Child Workflow is guaranteed to have started once the call resolves.
If you start a Child Workflow from a non-main context (for example, a Signal or Update handler), make sure the Parent Workflow doesn't complete before that call resolves.

To start a Child Workflow Execution and return a [handle](https://typescript.temporal.io/api/interfaces/workflow.ChildWorkflowHandle/) to it, use [startChild](https://typescript.temporal.io/api/namespaces/workflow/#startchild).

```ts

export async function parentWorkflow(names: string[]) {
  const childHandle = await startChild(childWorkflow, {
    args: [name],
    // workflowId, // add business-meaningful workflow id here
    // // regular workflow options apply here, with two additions (defaults shown):
    // cancellationType: ChildWorkflowCancellationType.WAIT_CANCELLATION_COMPLETED,
    // parentClosePolicy: ParentClosePolicy.PARENT_CLOSE_POLICY_TERMINATE
  });
  // you can use childHandle to signal or get result here
  await childHandle.signal('anySignal');
  const result = childHandle.result();
  // you can use childHandle to signal, query, cancel, terminate, or get result here
}
```

To start a Child Workflow Execution and await its completion, use [executeChild](https://typescript.temporal.io/api/namespaces/workflow/#executechild).

By default, a child is scheduled on the same Task Queue as the parent.

<!--SNIPSTART typescript-child-workflow -->
[child-workflows/src/workflows.ts](https://github.com/temporalio/samples-typescript/blob/main/child-workflows/src/workflows.ts)
```ts

export async function parentWorkflow(...names: string[]): Promise<string> {
  const responseArray = await Promise.all(
    names.map((name) =>
      executeChild(childWorkflow, {
        args: [name],
        // workflowId, // add business-meaningful workflow id here
        // // regular workflow options apply here, with two additions (defaults shown):
        // cancellationType: ChildWorkflowCancellationType.WAIT_CANCELLATION_COMPLETED,
        // parentClosePolicy: ParentClosePolicy.PARENT_CLOSE_POLICY_TERMINATE
      }),
    ),
  );
  return responseArray.join('\n');
}
```
<!--SNIPEND-->

To control any running Workflow from inside a Workflow, use [getExternalWorkflowHandle(workflowId)](https://typescript.temporal.io/api/namespaces/workflow/#getexternalworkflowhandle).

```ts

export async function terminateWorkflow() {
  const { workflowId } = workflowInfo(); // no await needed
  const handle = getExternalWorkflowHandle(workflowId); // sync function, not async
  await handle.cancel();
}
```

If the Child Workflow options aren't explicitly set, they inherit their values from the Parent Workflow options.
Two advanced options are unique to Child Workflows:

- [cancellationType](https://typescript.temporal.io/api/enums/proto.coresdk.child_workflow.ChildWorkflowCancellationType): Controls when to throw the `CanceledFailure` exception when a Child Workflow is canceled.
- `parentClosePolicy`: Explained in the next section.

If you need to cancel a Child Workflow Execution, use [cancellation scopes](/develop/typescript/workflows/cancellation-scopes).
A Child Workflow Execution is automatically cancelled when its containing scope is cancelled.

### How to set a Parent Close Policy {/* #parent-close-policy */}

A [Parent Close Policy](/parent-close-policy) determines what happens to a Child Workflow Execution if its Parent changes to a Closed status (Completed, Failed, or Timed Out).

The default Parent Close Policy option is set to terminate the Child Workflow Execution.

To specify how a Child Workflow reacts to a Parent Workflow reaching a Closed state, use the [`parentClosePolicy`](https://typescript.temporal.io/api/interfaces/workflow.ChildWorkflowOptions#parentclosepolicy) option.

<!--SNIPSTART typescript-child-workflow -->
[child-workflows/src/workflows.ts](https://github.com/temporalio/samples-typescript/blob/main/child-workflows/src/workflows.ts)
```ts

export async function parentWorkflow(...names: string[]): Promise<string> {
  const responseArray = await Promise.all(
    names.map((name) =>
      executeChild(childWorkflow, {
        args: [name],
        // workflowId, // add business-meaningful workflow id here
        // // regular workflow options apply here, with two additions (defaults shown):
        // cancellationType: ChildWorkflowCancellationType.WAIT_CANCELLATION_COMPLETED,
        // parentClosePolicy: ParentClosePolicy.PARENT_CLOSE_POLICY_TERMINATE
      }),
    ),
  );
  return responseArray.join('\n');
}
```
<!--SNIPEND-->

---

## Continue-As-New - Typescript SDK

This page answers the following questions for Typescript developers:

- [What is Continue-As-New?](#what)
- [How to Continue-As-New?](#how)
- [When is it right to Continue-as-New?](#when)
- [How to test Continue-as-New?](#how-to-test)

## What is Continue-As-New? {/* #what */}

[Continue-As-New](/workflow-execution/continue-as-new) lets a Workflow Execution close successfully and creates a new Workflow Execution.
You can think of it as a checkpoint when your Workflow gets too long or approaches certain scaling limits.

The new Workflow Execution is in the same [chain](/workflow-execution#workflow-execution-chain); it keeps the same Workflow Id but gets a new Run Id and a fresh Event History.
It also receives your Workflow's usual parameters.

## How to Continue-As-New using the Typescript SDK {/* #how */}

First, design your Workflow parameters so that you can pass in the "current state" when you Continue-As-New into the next Workflow run.
This state is typically set to `None` for the original caller of the Workflow.

    View the source code
  {' '}
  in the context of the rest of the application code.

```typescript
export interface ClusterManagerInput {
  state?: ClusterManagerState;
}

export async function clusterManagerWorkflow(input: ClusterManagerInput = {}): Promise<ClusterManagerStateSummary> {

````
The test hook in the above snippet is covered [below](#how-to-test).

Inside your Workflow, call the [`continueAsNew()`](https://typescript.temporal.io/api/namespaces/workflow#continueasnew) function with the same type.
This stops the Workflow right away and starts a new one.

    View the source code
  {' '}
  in the context of the rest of the application code.

```typescript
return await wf.continueAsNew<typeof clusterManagerWorkflow>({
  state: manager.getState(),
  testContinueAsNew: input.testContinueAsNew
});
````

### Considerations for Workflows with Message Handlers {/* #with-message-handlers */}

If you use Updates or Signals, don't call Continue-as-New from the handlers.
Instead, wait for your handlers to finish in your main Workflow before you run `ContinueAsNew`.
See the [`allHandlersFinished`](message-passing#wait-for-message-handlers) example for guidance.

## When is it right to Continue-as-New using the Typescript SDK? {/* #when */}

Use Continue-as-New when your Workflow might hit [Event History Limits](/workflow-execution/event#event-history).

Temporal tracks your Workflow's progress against these limits to let you know when you should Continue-as-New.
Call `wf.workflowInfo().continueAsNewSuggested` to check if it's time.

## How to test Continue-as-New using the Typescript SDK {/* #how-to-test */}

Testing Workflows that naturally Continue-as-New may be time-consuming and resource-intensive.
Instead, add a test hook to check your Workflow's Continue-as-New behavior faster in automated tests.

For example, when `testContinueAsNew == true`, this sample creates a test-only variable called `this.maxHistoryLength` and sets it to a small value.
A helper method in the Workflow checks it each time it considers using Continue-as-New:

    View the source code
  {' '}
  in the context of the rest of the application code.

```typescript
shouldContinueAsNew(): boolean {
  if (wf.workflowInfo().continueAsNewSuggested) {
    return true;
  }

  // This is just for ease-of-testing. In production, we trust temporal to tell us when to continue-as-new.
  if (this.maxHistoryLength !== undefined && wf.workflowInfo().historyLength > this.maxHistoryLength) {
    return true;
  }

  return false;
}
```

---

## Workflows - TypeScript SDK(Workflows)

![TypeScript SDK Banner](/img/assets/banner-typescript-temporal.png)

## Workflows

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

---

## Workflow message passing - TypeScript SDK

A Workflow can act like a stateful web service that receives messages: Queries, Signals, and Updates.
The Workflow implementation defines these endpoints via handler methods that can react to incoming messages and return values.
