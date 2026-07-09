Temporal Clients use messages to read Workflow state and control its execution.
See [Workflow message passing](/encyclopedia/workflow-message-passing) for a general overview of this topic.
This page introduces these features for the Temporal Typescript SDK.

## Write message handlers {/* #writing-message-handlers */}

:::info
The code that follows is part of a working [message-passing sample](https://github.com/temporalio/samples-typescript/tree/main/message-passing/introduction).
:::

Follow these guidelines when writing your message handlers:

- Define a message type as a global variable using [`defineQuery`](https://typescript.temporal.io/api/namespaces/workflow#definequery), [`defineSignal`](https://typescript.temporal.io/api/namespaces/workflow#definesignal), or [`defineUpdate`](https://typescript.temporal.io/api/namespaces/workflow#defineupdate).
  This is what your client code will use to send a message to the workflow.
- Message handlers are defined by calling [`workflow.setHandler`](https://typescript.temporal.io/api/namespaces/workflow#sethandler) in your Workflow function.
- The parameters and return values of handlers and the main Workflow function must be [serializable](/dataconversion).
- Prefer using a single object over multiple input parameters.
  A single object allows you to add fields without changing the signature.

### Query handlers {/* #queries */}

A [Query](/sending-messages#sending-queries) is a synchronous operation that retrieves state from a Workflow Execution:

```typescript
export enum Language {
  ARABIC = 'ARABIC',
  CHINESE = 'CHINESE',
  ENGLISH = 'ENGLISH',
  FRENCH = 'FRENCH',
  HINDI = 'HINDI',
  PORTUGUESE = 'PORTUGUESE',
  SPANISH = 'SPANISH',
}

interface GetLanguagesInput {
  includeUnsupported: boolean;
}

// 👉 Use the object returned by defineQuery to set the query handler in
// Workflow code, and when sending the Query in Client code.
export const getLanguages = wf.defineQuery<Language[], [GetLanguagesInput]>('getLanguages');

export async function greetingWorkflow(): Promise<string> {
  const greetings: Partial<Record<Language, string>> = {
    [Language.CHINESE]: '你好，世界',
    [Language.ENGLISH]: 'Hello, world',
  };

  wf.setHandler(getLanguages, (input: GetLanguagesInput): Language[] => {
    // 👉 A Query handler returns a value: it must not mutate the Workflow state
    // and can't perform async operations.
    if (input.includeUnsupported) {
      return Object.values(Language);
    } else {
      return Object.keys(greetings) as Language[];
    }
  });

  ...
}
```

- A Query handler cannot be `async`.
  You can't perform async operations like executing an Activity in a Query handler.

- `setHandler` can take `QueryHandlerOptions` (such as `description`) as described in the API reference docs for [`workflow.setHandler`](https://typescript.temporal.io/api/namespaces/workflow#sethandler).

### Signal handlers {/* #signals */}

A [Signal](/sending-messages#sending-signals) is an asynchronous message sent to a running Workflow Execution to change its state and control its flow:

```typescript
// 👉 Use the object returned by defineSignal to set the Signal handler in
// Workflow code, and to send the Signal from Client code.
export const approve = wf.defineSignal<[ApproveInput]>('approve');

export async function greetingWorkflow(): Promise<string> {
  let approvedForRelease = false;
  let approverName: string | undefined;

  wf.setHandler(approve, (input) => {
    // 👉 A Signal handler mutates the Workflow state but cannot return a value.
    approvedForRelease = true;
    approverName = input.name;
  });

  ...
}
...
```

- The handler cannot return a value.
  The response is sent immediately from the server, without waiting for the Workflow to process the Signal.

- Signal and Update handlers can be `async`.
  This allows you to use Activities, Child Workflows, durable [`workflow.sleep`](https://typescript.temporal.io/api/namespaces/workflow#sleep) Timers, [`workflow.condition`](https://typescript.temporal.io/api/namespaces/workflow#condition) conditions, and more.
  See [Async handlers](#async-handlers) and [Workflow message passing](/encyclopedia/workflow-message-passing) for guidelines on safely using async Signal and Update handlers.

- If your Workflow needs to do some async initialization before handling a Signal or Update, use [`workflow.condition`](https://typescript.temporal.io/api/namespaces/workflow#condition) inside your handler to wait until initialization has completed.

- `setHandler` can take `SignalHandlerOptions` (such as `description` and `unfinishedPolicy`) as described in the API reference docs for [`workflow.setHandler`](https://typescript.temporal.io/api/namespaces/workflow#sethandler).

### Update handlers and validators {/* #updates */}

An [Update](/sending-messages#sending-updates) is a trackable synchronous request sent to a running Workflow Execution.
It can change the Workflow state, control its flow, and return a result.
The sender must wait until the Worker accepts or rejects the Update.
The sender may wait further to receive a returned value or an exception if something goes wrong:

```typescript
// 👉 Use the object returned by defineUpdate to set the Update handler in
// Workflow code, and to send Updates from Client code.
export const setLanguage = wf.defineUpdate<Language, [Language]>('setLanguage');

export async function greetingWorkflow(): Promise<string> {
  const greetings: Partial<Record<Language, string>> = {
    [Language.CHINESE]: '你好，世界',
    [Language.ENGLISH]: 'Hello, world',
  };

  let language = Language.ENGLISH;

wf.setHandler(
    setLanguage,
    (newLanguage: Language) => {
      // 👉 An Update handler can mutate the Workflow state and return a value.
      const previousLanguage = language;
      language = newLanguage;
      return previousLanguage;
    },
    {
      validator: (newLanguage: Language) => {
        // 👉 Update validators are optional
        if (!(newLanguage in greetings)) {
          throw new Error(`${newLanguage} is not supported`);
        }
      },
    }
  );

  ...
}
```

- `setHandler` can take `UpdateHandlerOptions` (such as `validator`, `description` and `unfinishedPolicy`) as described in the API reference docs for [`workflow.setHandler`](https://typescript.temporal.io/api/namespaces/workflow#sethandler).

- About validators:
  - Use validators to reject an Update before it is written to History.
    Validators are always optional.
    If you don't need to reject Updates, you don't need a validator.
  - To set a validator, pass the validator function in `UpdateHandlerOptions` when calling [`workflow.setHandler`](https://typescript.temporal.io/api/namespaces/workflow#sethandler).
    The validator must be a non-async function that accepts the same argument types as the handler and returns `void`.

- Accepting and rejecting Updates with validators:
  - To reject an Update, throw an error of any type in the validator.
  - Without a validator, Updates are always accepted.
- Validators and Event History:
  - The `WorkflowExecutionUpdateAccepted` event is written into History whether the acceptance was automatic or due to a validator function not throwing an error.
  - When a Validator throws an error, the Update is rejected and `WorkflowExecutionUpdateAccepted` _won't_ be added to the Event History.
    The caller receives an "Update failed" error.

- Use [`workflow.currentUpdateInfo`](https://typescript.temporal.io/api/namespaces/workflow#current_update_info) to obtain information about the current Update.
  This includes the Update ID, which can be useful for deduplication when using Continue-As-New: see [Ensuring your messages are processed exactly once](/handling-messages#exactly-once-message-processing).
- Update and Signal handlers can be `async`, letting them use Activities, Child Workflows, durable [`workflow.sleep`](https://typescript.temporal.io/api/namespaces/workflow#sleep) Timers, [`workflow.condition`](https://typescript.temporal.io/api/namespaces/workflow#condition) conditions, and more.
  See [Async handlers](#async-handlers) and [Workflow message passing](/encyclopedia/workflow-message-passing) for safe usage guidelines.
- If your Workflow needs to do some async initialization before handling an Update or Signal, use [`workflow.condition`](https://typescript.temporal.io/api/namespaces/workflow#condition) inside your handler to wait until initialization has completed.

## Send messages {/* #send-messages */}

To send Queries, Signals, or Updates, you call methods on a [WorkflowHandle](https://typescript.temporal.io/api/namespaces/client#workflowhandle) object:

- Use [`client.workflow.start`](https://typescript.temporal.io/api/classes/client.WorkflowClient#start) and return its handle.

- Use [`client.workflow.getHandle`](https://typescript.temporal.io/api/classes/client.WorkflowClient#gethandle) to retrieve a Workflow handle by its Workflow Id.

For example:

```typescript
const handle = await client.workflow.start(greetingWorkflow, {
  taskQueue: 'my-task-queue',
  args: [myArg],
  workflowId: 'my-workflow-id',
});
```

To check the argument types required when sending messages -- and the return type for Queries and Updates -- refer to the corresponding handler method in the Workflow Definition.

:::warning Using Continue-as-New and Updates

- Temporal _does not_ support Continue-as-New functionality within Update handlers.
- Complete all handlers _before_ using Continue-as-New.
- Use Continue-as-New from your main Workflow Definition method, just as you would complete or fail a Workflow Execution.

:::

### Send a Query {/* #send-query */}

Use [`WorkflowHandle.query`](https://typescript.temporal.io/api/interfaces/client.WorkflowHandle/#query) to send a Query to a Workflow Execution:

```typescript
const supportedLanguages = await handle.query(getLanguages, {
  includeUnsupported: false,
});
```

- Sending a Query doesn’t add events to a Workflow's Event History.

- You can send Queries to closed Workflow Executions within a Namespace's Workflow retention period.
  This includes Workflows that have completed, failed, or timed out.
  Querying terminated Workflows is not safe and, therefore, not supported.

- A Worker must be online and polling the Task Queue to process a Query.

### Send a Signal {/* #send-signal */}

You can send a Signal to a Workflow Execution from a Temporal Client or from another Workflow Execution.
However, you can only send Signals to Workflow Executions that haven’t closed.

#### Send a Signal from a Client {/* #send-signal-from-client */}

Use [WorkflowHandle.signal](https://typescript.temporal.io/api/interfaces/client.WorkflowHandle#signal) to send a Signal:

```typescript
await handle.signal(greetingWorkflow.approve, { name: 'me' });
```

- The call returns when the server accepts the Signal; it does _not_ wait for the Signal to be delivered to the Workflow Execution.

- The [WorkflowExecutionSignaled](/references/events#workflowexecutionsignaled) Event appears in the Workflow's Event History.

### Send a Signal from a Workflow {/* #send-signal-from-workflow */}

A Workflow can send a Signal to another Workflow, in which case it's called an _External Signal_.
Use [`getExternalWorkflowHandle`](https://typescript.temporal.io/api/namespaces/workflow#getExternalWorkflowHandle):

```typescript

export async function yourWorkflowThatSignals() {
  const handle = getExternalWorkflowHandle('workflow-id-123');
  await handle.signal(joinSignal, { userId: 'user-1', groupId: 'group-1' });
}
```

When an External Signal is sent:

- A [SignalExternalWorkflowExecutionInitiated](/references/events#signalexternalworkflowexecutioninitiated) Event appears in the sender's Event History.
- A [WorkflowExecutionSignaled](/references/events#workflowexecutionsignaled) Event appears in the recipient's Event History.

The `getExternalWorkflowHandle` method helps ensure that Workflows remain deterministic.
Recall that one aspect of deterministic Workflows means not directly making network calls from the Workflow.
This means that developers cannot use a Temporal Client directly within the Workflow code to send Signals or start other Workflows.
Instead, to communicate between Workflows, we use `getExternalWorkflowHandle` to both ensure that Workflows remain deterministic and also that these interactions are recorded as Events in the Workflow's Event History.

### Signal-With-Start {/* #signal-with-start */}

Signal-With-Start allows a Client to send a Signal to a Workflow Execution, starting the Execution if it is not already running.
Use [`Client.workflow.signalWithStart`](https://typescript.temporal.io/api/classes/client.WorkflowClient#signalwithstart):

```typescript

const client = new Client();

await client.workflow.signalWithStart(yourWorkflow, {
  workflowId: 'workflow-id-123',
  taskQueue: 'my-taskqueue',
  args: [{ foo: 1 }],
  signal: joinSignal,
  signalArgs: [{ userId: 'user-1', groupId: 'group-1' }],
});
```

Signal-With-Start is limited to Client use.
It cannot be called from a Workflow.

### Send an Update {/* #send-update-from-client */}

An Update is a synchronous, blocking call that can change Workflow state, control its flow, and return a result.

A client sending an Update must wait until the Server delivers the Update to a Worker.
Workers must be available and responsive.
If you need a response as soon as the Server receives the request, use a Signal instead.
You can't send Updates directly from one Workflow to another or perform an Update equivalent of Signal-With-Start. If you need to send Updates across Workflows, like to Child Workflows, use an Activity.

- `WorkflowExecutionUpdateAccepted` is added to the Event History when the Worker confirms that the Update passed validation.
- `WorkflowExecutionUpdateCompleted` is added to the Event History when the Worker confirms that the Update has finished.

To send an Update to a Workflow Execution, you can:

- Call [`WorkflowHandle.executeUpdate`](https://typescript.temporal.io/api/interfaces/client.WorkflowHandle/#executeUpdate) and wait for the Update to complete.
  This code fetches an Update result:

  ```typescript
  let previousLanguage = await handle.executeUpdate(setLanguage, {
    args: [Language.CHINESE],
  });
  ```

- Send [`WorkflowHandle.startUpdate`](https://typescript.temporal.io/api/interfaces/client.WorkflowHandle/#startUpdate) to receive an [`WorkflowUpdateHandle`](https://typescript.temporal.io/api/interfaces/client.WorkflowUpdateHandle) as soon as the Update is accepted or rejected.

  - Use this `UpdateHandle` later to fetch your results.
  - `async` Update handlers normally perform long-running asynchronous operations, such as calling an Activity.
  - `startUpdate` only waits until the Worker has accepted or rejected the Update, not until all asynchronous operations are complete.

  For example:

  ```typescript
  const updateHandle = await handle.startUpdate(setLanguage, {
    args: [Language.ENGLISH],
    waitForStage: WorkflowUpdateStage.ACCEPTED,
  });
  previousLanguage = await updateHandle.result();
  ```

  For more details, see the "Async handlers" section.

To obtain an Update handle, you can:

- Use [`WorkflowHandle.startUpdate`](https://typescript.temporal.io/api/interfaces/client.WorkflowHandle/#startUpdate) to start an Update and return the handle, as shown in the preceding example.
- Use [`getUpdateHandle`](https://typescript.temporal.io/api/interfaces/client.WorkflowHandle/#getupdatehandle) to fetch a handle for an in-progress Update using the Update ID.

#### Update-With-Start {/* #update-with-start */}

:::tip

For open source server users, Temporal Server version [Temporal Server version 1.28](https://github.com/temporalio/temporal/releases/tag/v1.28.0) is recommended.

:::

[Update-with-Start](/sending-messages#update-with-start) lets you
[send an Update](/develop/typescript/workflows/message-passing#send-update-from-client) that checks whether an already-running Workflow with that ID exists:

- If the Workflow exists, the Update is processed.
- If the Workflow does not exist, a new Workflow Execution is started with the given ID, and the Update is processed before the main Workflow method starts to execute.

Use [`executeUpdateWithStart`](https://typescript.temporal.io/api/classes/client.WorkflowClient#executeUpdateWithStart) to start an Update and wait for the result in one go.

Alternatively, use [`startUpdateWithStart`](https://typescript.temporal.io/api/classes/client.WorkflowClient#startUpdateWithStart) to start an Update and receive a [`WorkflowUpdateHandle`](https://typescript.temporal.io/api/interfaces/client.WorkflowUpdateHandle), and then use `await updateHandle.result()` to retrieve the result from the Update.

These calls return once the requested Update wait stage has been reached, or when the request times out.

You will need to provide a [`WithStartWorkflowOperation`](https://typescript.temporal.io/api/classes/client.WithStartWorkflowOperation) to define the Workflow that will be started if necessary, and its arguments.
You must specify a [WorkflowIdConflictPolicy](/workflow-execution/workflowid-runid#workflow-id-conflict-policy) when creating the `WithStartWorkflowOperation`.
Note that a `WithStartWorkflowOperation` can only be used once.

Here's an example taken from the [early-return](https://github.com/temporalio/samples-typescript/tree/main/early-return) sample:

```typescript
const startWorkflowOperation = new WithStartWorkflowOperation.create(
  transactionWorkflow,
  {
    workflowId,
    args: [transactionID],
    taskQueue: 'early-return',
    workflowIdConflictPolicy: 'FAIL',
  },
);

const earlyConfirmation = await client.workflow.executeUpdateWithStart(
  getTransactionConfirmation,
  {
    startWorkflowOperation,
  },
);

const wfHandle = await startWorkflowOperation.workflowHandle();
const finalReport = await wfHandle.result();
```

:::info SEND MESSAGES WITHOUT TYPE SAFETY

In real-world development, sometimes you may be unable to import message type objects defined by `defineQuery`, `defineSignal`, or `defineUpdate`.
When you don't have access to the Workflow Definition or it isn't written in Typescript, you can still use APIs that aren't type-safe, and dynamic method invocation.
Pass message type names instead of message type objects to:

- [`client.workflow.start`](https://typescript.temporal.io/api/classes/client.WorkflowClient#start)
- [`WorkflowHandle.query`](https://typescript.temporal.io/api/interfaces/client.WorkflowHandle/#query)
- [WorkflowHandle.signal](https://typescript.temporal.io/api/interfaces/client.WorkflowHandle#signal)
- [`WorkflowHandle.executeUpdate`](https://typescript.temporal.io/api/interfaces/client.WorkflowHandle/#executeUpdate)
- [`WorkflowHandle.startUpdate`](https://typescript.temporal.io/api/interfaces/client.WorkflowHandle/#startUpdate)

Pass Workflow IDs to these APIs to get Workflow handles:

- [`client.workflow.getHandle`](https://typescript.temporal.io/api/classes/client.WorkflowClient#gethandle)
- [`getExternalWorkflowHandle`](https://typescript.temporal.io/api/namespaces/workflow#getExternalWorkflowHandle).

:::

## Message handler patterns {/* #message-handler-patterns */}

This section covers common write operations, such as Signal and Update handlers.
It doesn't apply to pure read operations, like Queries or Update Validators.

:::tip

For additional information, see [Inject work into the main Workflow](/handling-messages#injecting-work-into-main-workflow), [Ensuring your messages are processed exactly once](/handling-messages#exactly-once-message-processing), and [this sample](https://github.com/temporalio/samples-typescript/blob/main/message-passing/safe-message-handlers/README.md) demonstrating safe `async` message handling.

:::

### Use async handlers {/* #async-handlers */}

Signal and Update handlers can be `async` functions.
Using `async` allows you to use `await` with Activities, Child Workflows, durable [`workflow.sleep`](https://typescript.temporal.io/api/namespaces/workflow#sleep) Timers, [`workflow.condition`](https://typescript.temporal.io/api/namespaces/workflow#condition) conditions, etc.
This expands the possibilities for what can be done by a handler but it also means that handler executions and your main Workflow method are all running concurrently, with switching occurring between them at `await` calls.
It's essential to understand the things that could go wrong in order to use `async` handlers safely.
See [Workflow message passing](/encyclopedia/workflow-message-passing) for guidance on safe usage of async Signal and Update handlers, the [Safe message handlers](https://github.com/temporalio/samples-typescript/blob/main/message-passing/safe-message-handlers/README.md) sample, and the [Controlling handler concurrency](#control-handler-concurrency) and [Waiting for message handlers to finish](#wait-for-message-handlers) sections below.

The following code executes an Activity that makes a network call to a remote service.
It modifies the Update handler from earlier on this page, turning it into an `async` function:

```typescript
// 👉 Use the objects returned by defineUpdate to set the Update handler in
// Workflow code, and to send Updates from Client code.
export const setLanguageUsingActivity = wf.defineUpdate<Language, [Language]>('setLanguageUsingActivity');

export async function greetingWorkflow(): Promise<string> {
  const greetings: Partial<Record<Language, string>> = {
    [Language.CHINESE]: '你好，世界',
    [Language.ENGLISH]: 'Hello, world',
  };

  let language = Language.ENGLISH;

  const lock = new Mutex();
  wf.setHandler(setLanguageUsingActivity, async (newLanguage) => {
    // 👉 An Update handler can mutate the Workflow state and return a value.
    // 👉 Since this update handler is async, it can execute an activity.
    if (!(newLanguage in greetings)) {
      // 👉 Do the following with the lock held to ensure that multiple calls to set_language are processed in order.
      await lock.runExclusive(async () => {
        if (!(newLanguage in greetings)) {
          const greeting = await callGreetingService(newLanguage);
          if (!greeting) {
            // 👉 An update validator cannot be async, so cannot be used to check that the remote
            // call_greeting_service supports the requested language. Raising ApplicationError
            // will fail the Update, but the WorkflowExecutionUpdateAccepted event will still be
            // added to history.
            throw new wf.ApplicationFailure(`${newLanguage} is not supported by the greeting service`);
          }
          greetings[newLanguage] = greeting;
        }
      });
    }
    const previousLanguage = language;
    language = newLanguage;
    return previousLanguage;
  });
  ...
}
```

After updating the code to use `async`, your Update handler can schedule an Activity and await the result.
Although an `async` Signal handler can also execute an Activity, using an Update handler allows the client to receive a result or error once the Activity completes.
This lets your client track the progress of asynchronous work performed by the Update's Activities, Child Workflows, etc.

### Add wait conditions to block

Sometimes, `async` Signal or Update handlers need to meet certain conditions before they should continue.
You can use [`workflow.condition`](https://typescript.temporal.io/api/namespaces/workflow#condition) to prevent the code from proceeding until a condition is true.
You specify the condition by passing a function that returns `true` or `false`.
This is an important feature that helps you control your handler logic.

Here are three important use cases for `workflow.condition`:

- Waiting for a Signal or Update to arrive
- Waiting in a handler until it is appropriate to continue.
- Waiting in the main Workflow until all active handlers have finished.

#### Wait for a Signal or Update to arrive

It's common to use `workflow.condition` to wait for a particular Signal or Update to be sent by a Client:

```typescript
export async function greetingWorkflow(): Promise<string> {
  let approvedForRelease = false;
  let approverName: string | undefined;

  wf.setHandler(approve, (input) => {
    approvedForRelease = true;
    approverName = input.name;
  });
  ...

  await wf.condition(() => approvedForRelease);
  ...
}
```

#### Use wait conditions in handlers

It's common to use a Workflow wait condition in a handler.
For example, suppose your Workflow has a mutable variable `readyForUpdateToExecute` that indicates whether your Update handler should be allowed to start executing.
You can use `workflow.condition` in the handler to make the handler pause until the condition is met:

```typescript
let readyForUpdateToExecute = false;

wf.setHandler(myUpdate, async (input: MyUpdateInput): Promise<MyUpdateOutput> => {
  await wf.condition(() => readyForUpdateToExecute);
  ...
});
```

Remember: handlers can execute before the main Workflow method starts.

You can also use wait conditions anywhere else in the handler to wait for a specific condition to become true.
This allows you to write handlers that pause at multiple points, each time waiting for a required condition to become true.

#### Ensure your handlers finish before the Workflow completes {/* #wait-for-message-handlers */}

Workflow wait conditions can ensure your handler completes before a Workflow finishes.
When your Workflow uses `async` Signal or Update handlers, your main Workflow method can return or Continue-as-New while a handler is still waiting on an async task, such as an Activity result.
