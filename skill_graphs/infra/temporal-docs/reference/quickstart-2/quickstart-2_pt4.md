If you supply only the Workflow Id (and provide an empty string as the Run Id param), the running Workflow Execution receives the Update.

You must provide a `WaitForStage` when calling `UpdateWorkflow()`.
This parameter controls the stage the update must reach before returning a handle to the caller:

- If `WaitForStage` is set to `WorkflowUpdateStageCompleted`, the handle is returned after the Update completes.
- If `WaitForStage` is set to `WorkflowUpdateStageAccepted`, the handle is returned after the Update is accepted (i.e. after the validator has run, if there is a validator).

You can't send Updates directly from one Workflow to another. If you need to send Updates across Workflows, like to Child Workflows, use an Activity.

```go
ctxWithTimeout, cancel := context.WithTimeout(context.Background(), 15*time.Second)
defer cancel()

updateHandle, err := temporalClient.UpdateWorkflow(ctxWithTimeout, client.UpdateWorkflowOptions{
    WorkflowID:   we.GetID(),
    RunID:        we.GetRunID(),
    UpdateName:   message.SetLanguageUpdate,
    WaitForStage: client.WorkflowUpdateStageAccepted,
    Args:         []interface{}{message.Chinese},
})
if err != nil {
    log.Fatalf("Unable to update workflow: %v", err)
}

var previousLang message.Language
err = updateHandle.Get(ctxWithTimeout, &previousLang)
if err != nil {
    log.Fatalf("Unable to get update result: %v", err)
}
```

#### Update-With-Start {/* #update-with-start */}

:::tip

For open source server users, Temporal Server version [Temporal Server version 1.28](https://github.com/temporalio/temporal/releases/tag/v1.28.0) is recommended.

:::

[Update-with-Start](/sending-messages#update-with-start) lets you
[send an Update](/develop/go/workflows/message-passing#send-update-from-client) that checks whether an already-running Workflow with that ID exists:

- If the Workflow exists, the Update is processed.
- If the Workflow does not exist, a new Workflow Execution is started with the given ID, and the Update is processed before the main Workflow method starts to execute.

Use the [`Client.UpdateWithStartWorkflow`](https://pkg.go.dev/go.temporal.io/sdk/client#Client.UpdateWithStartWorkflow) API call.
It returns once the requested Update wait stage has been reached; or when a provided context times out.
Use [`WorkflowUpdateHandle`](https://pkg.go.dev/go.temporal.io/sdk/client#WorkflowUpdateHandle) to retrieve a result from the Update.

You will need to provide:

- [`StartWorkflowOptions`](https://pkg.go.dev/go.temporal.io/sdk/internal#StartWorkflowOptions).
  The [Workflow Id Conflict Policy](/workflow-execution/workflowid-runid#workflow-id-conflict-policy) is required.
  Choose "Use Existing" and use an idempotent Update handler to ensure your code can be executed again in case of a Client failure.
  Not all `StartWorkflowOptions` are allowed.
  For example, specifying a Cron Schedule will result in an error.
  Refer to the [API documentation](https://pkg.go.dev/go.temporal.io/sdk/internal#StartWorkflowOptions) for further details.

- [`UpdateWorkflowOptions`](https://pkg.go.dev/go.temporal.io/sdk/internal#UpdateWorkflowOptions).
  Same as for [Update Workflow](/develop/go/workflows/message-passing#send-update-from-client), the update name and an update wait stage must be specified.
  For Update-with-Start, the Workflow Id is optional.
  When specified, the Id must match the one used in `StartWorkflowOptions`.
  Since a running Workflow Execution may not already exist, you can't set a Run Id.

- [`Client.NewWithStartWorkflowOperation`](https://pkg.go.dev/go.temporal.io/sdk/client#Client.NewWithStartWorkflowOperation).
  Specify the workflow options, method and arguments.
  Note that a `WithStartWorkflowOperation` can only be used once.
  Re-using a previously used operation returns an error from `UpdateWithStartWorkflow`.

The following example shows the creation, configuration, and use of UpdateWithStart:

```go
ctxWithTimeout, cancel := context.WithTimeout(context.Background(), 15*time.Second)
defer cancel()

workflowOptions := client.StartWorkflowOptions{
    ID:                       "some-workflow-id",
    TaskQueue:                "some-task-queue",
    WorkflowIDConflictPolicy: enumspb.WORKFLOW_ID_CONFLICT_POLICY_USE_EXISTING,
}

updateOptions := client.UpdateWorkflowOptions{
    UpdateName:   message.SetLanguageUpdate,
    WaitForStage: client.WorkflowUpdateStageCompleted,
}

startWorkflowOp := temporalClient.NewWithStartWorkflowOperation(workflowOptions, MyWorkflow)
updateHandle, err := temporalClient.UpdateWithStartWorkflow(
	ctxWithTimeout,
	client.UpdateWithStartWorkflowOptions{
        StartWorkflowOperation: startWorkflowOp,
        UpdateOptions:          updateOptions,
    })
if err != nil {
    log.Fatalf("Unable to execute update-with-start: %v", err)
}

var previousLang message.Language
err = updateHandle.Get(ctxWithTimeout, &previousLang)
if err != nil {
    log.Fatalf("Unable to obtain update result: %v", err)
}

workflowRun, err := startWorkflowOp.Get(ctxWithTimeout)
if err != nil {
    log.Fatalf("Unable to obtain workflow run: %v", err)
}
```

For more examples, see the [Go sample for early-return pattern](https://github.com/temporalio/samples-go/tree/main/early-return).

## Message handler patterns {/* #message-handler-patterns */}

This section covers common write operations, such as Signal and Update handlers.
It doesn't apply to pure read operations, like Queries or Update Validators.

:::tip

For additional information, see [Inject work into the main Workflow](/handling-messages#injecting-work-into-main-workflow), [Ensuring your messages are processed exactly once](/handling-messages#exactly-once-message-processing), and [this sample](https://github.com/temporalio/samples-go/blob/main/safe_message_handler/README.md) demonstrating safe blocking message handling.

:::

### Blocking handlers {/* #blocking-handlers */}

Signal and Update handlers can block.
This allows you to use Activities, Child Workflows, durable [workflow.Sleep](https://pkg.go.dev/go.temporal.io/sdk/workflow#Sleep) Timers, [`workflow.Await`](https://pkg.go.dev/go.temporal.io/sdk/workflow#Await) conditions, etc.
This expands the possibilities for what can be done by a handler but it also means that handler executions and your main Workflow method are all running concurrently, with switching occurring between them at await calls.

It's essential to understand the things that could go wrong in order to use blocking handlers safely.
See [Workflow message passing](/encyclopedia/workflow-message-passing) for guidance on safe usage of blocking Signal and Update handlers, and the [Controlling handler concurrency](#control-handler-concurrency) and [Waiting for message handlers to finish](#wait-for-message-handlers) sections below.

The following code modifies the Update handler from earlier on in this page.
The Update handler now makes a blocking call to execute an Activity:

```go
func GreetingWorkflow(ctx workflow.Context) error {
	language := English

	err = workflow.SetUpdateHandler(ctx, SetLanguageUpdate, func(ctx workflow.Context, newLanguage Language) (Language, error) {
        if _, ok := greeting[newLanguage]; !ok {
            ao := workflow.ActivityOptions{
                StartToCloseTimeout: 10 * time.Second,
            }
            ctx = workflow.WithActivityOptions(ctx, ao)

            var greeting string
            err := workflow.ExecuteActivity(ctx, CallGreetingService, newLanguage).Get(ctx, &greeting)
            if err != nil {
                return nil, err
            }
            greeting[newLanguage] = greeting
        }
		var previousLanguage Language
		previousLanguage, language = language, newLanguage
		return previousLanguage, nil
	})
  ...
}
```

### Add blocking wait conditions {/* #block-with-wait */}

Sometimes, blocking Signal or Update handlers need to meet certain conditions before they should continue.
You can use [`workflow.Await`](https://pkg.go.dev/go.temporal.io/sdk/workflow#Await) to prevent the code from proceeding until a condition is true.
You specify the condition by passing a function that returns `true` or `false`.
This is an important feature that helps you control your handler logic.

Here are three important use cases for `Workflow.await`:

- Waiting until a specific Update has arrived.
- Waiting in a handler until it is appropriate to continue.
- Waiting in the main Workflow until all active handlers have finished.

```go
err = workflow.SetUpdateHandler(ctx, "UpdateHandler", func(ctx workflow.Context, input UpdateInput) error {
    workflow.Await(ctx, updateUnblockedFunc)
    ...
})
```

This is necessary if your Update handlers require something in the main Workflow function to be done first, since an Update handler can execute concurrently with the main Workflow function.

You can also use `Workflow.await` anywhere else in the handler to wait for a specific condition to become true.
This allows you to write handlers that pause at multiple points, each time waiting for a required condition to become true.

#### Ensure your handlers finish before the Workflow completes {/* #wait-for-message-handlers */}

`Workflow.await` can ensure your handler completes before a Workflow finishes.
When your Workflow uses blocking Update handlers, your main Workflow method can return or Continue-as-New while a handler is still waiting on an async task, such as an Activity.
The Workflow completing may interrupt the handler before it finishes crucial work and cause client errors when trying to retrieve Update results.
Use [`workflow.Await`](https://pkg.go.dev/go.temporal.io/sdk/workflow#Await) to wait for [`AllHandlersFinished`](https://pkg.go.dev/go.temporal.io/sdk/workflow#AllHandlersFinished) to return `true` to address this problem and allow your Workflow to end smoothly:

```go
func YourWorkflowDefinition(ctx workflow.Context, param YourWorkflowParam) error {
    ...
	err = workflow.Await(ctx, func() bool {
		return workflow.AllHandlersFinished(ctx)
	})
    return nil
}
```

By default, your Worker will log a warning if you allow your Workflow Execution to finish with unfinished Update handler executions.
You can silence these warnings on a per-handler basis by setting `UnfinishedPolicy` field on [`workflow.UpdateHandlerOptions`](https://pkg.go.dev/go.temporal.io/sdk/workflow#UpdateHandlerOptions) struct:

```go
err = workflow.SetUpdateHandlerWithOptions(ctx, UpdateHandlerName, UpdateFunc, workflow.UpdateHandlerOptions{
       UnfinishedPolicy: workflow.HandlerUnfinishedPolicyAbandon,
})
```

See [Finishing handlers before the Workflow completes](/handling-messages#finishing-message-handlers) for more information.

#### Use `workflow.Mutex` to prevent concurrent handler execution {/* #control-handler-concurrency */}

See [Message handler concurrency](/handling-messages#message-handler-concurrency).

Concurrent processes can interact in unpredictable ways.
Incorrectly written [concurrent message-passing](/handling-messages#message-handler-concurrency) code may not work correctly when multiple handler instances run simultaneously.
Here's an example of a pathological case:

```go
// ...
func YourWorkflowDefinition(ctx workflow.Context, param YourWorkflowParam) error {
    ...
    err := workflow.SetUpdateHandler(ctx, "BadUpdateHandler", func(ctx workflow.Context) error {
        ao := workflow.ActivityOptions{
            StartToCloseTimeout: 10 * time.Second,
        }
        ctx = workflow.WithActivityOptions(ctx, ao)

        var result Data
        err := workflow.ExecuteActivity(ctx, FetchData, name).Get(ctx, &result)
        x = result.x
        // 🐛🐛 Bug!! If multiple instances of this handler are executing concurrently, then
        // there may be times when the Workflow has self.x from one Activity execution and self.y from another.
        err = workflow.Sleep(ctx, time.Second)
        if err != nil {
            return err
        }
        y = result.y
    })
    ...
}
```

Coordinating access with `workflow.Mutex` corrects this code.
Locking makes sure that only one handler instance can execute a specific section of code at any given time:

```go
func YourWorkflowDefinition(ctx workflow.Context, param YourWorkflowParam) error {
    ...
    err := workflow.SetUpdateHandler(ctx, "SafeUpdateHandler", func(ctx workflow.Context) error {
        err := mutex.Lock(ctx)
        if err != nil {
            return err
        }
        defer mutex.Unlock()
        ao := workflow.ActivityOptions{
            StartToCloseTimeout: 10 * time.Second,
        }
        ctx = workflow.WithActivityOptions(ctx, ao)

        var result Data
        err := workflow.ExecuteActivity(ctx, FetchData, name).Get(ctx, &result)
        x = data.x
        // ✅ OK: the scheduler may switch now to a different handler execution, or to the main workflow
        // method, but no other execution of this handler can run until this execution finishes.
        err = workflow.Sleep(ctx, time.Second)
        if err != nil {
            return err
        }
        self.y = data.y
    })
    ...
}
```

## Troubleshooting

See [Exceptions in message handlers](/handling-messages#exceptions) for a non–Go-specific discussion of this topic.

When sending a Signal, Update, or Query to a Workflow, your Client might encounter the following errors:

- **The Client can't contact the server**

- **The Workflow does not exist**

Unlike Signals, for Queries and Updates, the Client waits for a response from the Worker.
If an issue occurs during the handler execution by the Worker, the Client may receive an exception.

### Problems when sending an Update

- **There is no Workflow Worker polling the Task Queue**

  Your request will be retried by the SDK Client until the calling context is cancelled.

- **Update failed.**

  Update failures are like [Workflow failures](/references/failures).
  Issues that cause a Workflow failure in the main method also cause Update failures in the Update handler.
  These might include:

  - A failed Child Workflow
  - A failed Activity if the activity retries have been set to a finite number
  - The Workflow author returning an `error`
  - A panic in the handler, depending on the `WorkflowPanicPolicy`

- **The handler caused the Workflow Task to fail**
  A [Workflow Task Failure](/references/failures) causes the server to retry Workflow Tasks indefinitely. What happens to your Update request depends on its stage:
  - If the request hasn't been accepted by the server, you receive a [`FAILED_PRECONDITION`](https://pkg.go.dev/go.temporal.io/api/serviceerror#FailedPrecondition) error.
  - If the request has been accepted, it is durable.
    Once the Workflow is healthy again after a code deploy, use a [`WorkflowUpdateHandle`](https://pkg.go.dev/go.temporal.io/sdk/client#WorkflowUpdateHandle) to fetch the Update result.

- **The Workflow finished while the Update handler execution was in progress**:
  You'll receive a [`ServiceError`](https://pkg.go.dev/go.temporal.io/api/serviceerror#ServiceError) "workflow execution already completed"`.

  This will happen if the Workflow finished while the Update handler execution was in progress, for example because

  - The Workflow was canceled or failed.

  - The Workflow completed normally or continued-as-new and the Workflow author did not [wait for handlers to be finished](/handling-messages#finishing-message-handlers).

### Problems when sending a Query

- **There is no Workflow Worker polling the Task Queue**

  You'll receive a [`ServiceError`](https://pkg.go.dev/go.temporal.io/api/serviceerror#ServiceError) on which the `status` is `FAILED_PRECONDITION`.

- **Query failed.**
  You'll receive a [`QueryFailed`](https://pkg.go.dev/go.temporal.io/api/serviceerror#QueryFailed) error.
  Any panic in a Query handler will trigger this error.
  This differs from Signal and Update, where panics can lead to Workflow Task Failure instead.

- **The handler caused the Workflow Task to fail.**
  This would happen, for example, if the Query handler blocks the thread for too long without yielding.

---

## Schedules - Go SDK

This page shows how to do the following:

- [Scheduled Workflows](#schedule-a-workflow)
  - [Create a Schedule](#create-schedule)
  - [Backfill a Schedule](#backfill-schedule)
  - [Delete a Schedule](#delete-schedule)
  - [Describe a Schedule](#describe-schedule)
  - [List Schedules](#list-schedules)
  - [Pause a Schedule](#pause-schedule)
  - [Trigger a Schedule](#trigger-schedule)
  - [Update a Schedule](#update-schedule)
- [Start delay](#start-delay)
- [Temporal Cron Jobs](#temporal-cron-jobs)

## Scheduled Workflows {/* #schedule-a-workflow */}

Scheduling Workflows is a crucial aspect of any automation process, especially when dealing with time-sensitive tasks. By scheduling a Workflow, you can automate repetitive tasks, reduce the need for manual intervention, and ensure timely execution of your business processes.

Use any of the following actions to help Schedule a Workflow Execution and take control over your automation process.

### Create a Schedule {/* #create-schedule */}

Schedules are initiated with the `create` call.
The user generates a unique Schedule ID for each new Schedule.

To create a Schedule in Go, use `Create()` on the [Client](/encyclopedia/temporal-sdks#temporal-client).
Schedules must be initialized with a Schedule ID, [Spec](/schedule), and [Action](/schedule) in `client.ScheduleOptions{}`.

    View the source code
  {' '}
  in the context of the rest of the application code.

```go
func main() {
// ...
	scheduleID := "schedule_id"
	workflowID := "schedule_workflow_id"
	// Create the schedule.
	scheduleHandle, err := temporalClient.ScheduleClient().Create(ctx, client.ScheduleOptions{
		ID:   scheduleID,
		Spec: client.ScheduleSpec{},
		Action: &client.ScheduleWorkflowAction{
			ID:        workflowID,
			Workflow:  schedule.ScheduleWorkflow,
			TaskQueue: "schedule",
		},
	})
// ...
}
// ...
```

:::tip Schedule Auto-Deletion

Once a Schedule has completed creating all its Workflow Executions, the Temporal Service deletes it since it won’t fire again.
The Temporal Service doesn't guarantee when this removal will happen.

:::

### Backfill a Schedule {/* #backfill-schedule */}

Backfilling a Schedule executes [Workflow Tasks](/tasks#workflow-task) ahead of the Schedule's specified time range.
This is useful for executing a missed or delayed Action, or for testing the Workflow ahead of time.

To backfill a Schedule in Go, use `Backfill()` on `ScheduleHandle`.
Specify the start and end times to execute the Workflow, along with the overlap policy.

    View the source code
  {' '}
  in the context of the rest of the application code.

```go
func main() {
// ...
	err = scheduleHandle.Backfill(ctx, client.ScheduleBackfillOptions{
		Backfill: []client.ScheduleBackfill{
			{
				Start:   now.Add(-4 * time.Minute),
				End:     now.Add(-2 * time.Minute),
				Overlap: enums.SCHEDULE_OVERLAP_POLICY_ALLOW_ALL,
			},
			{
				Start:   now.Add(-2 * time.Minute),
				End:     now,
				Overlap: enums.SCHEDULE_OVERLAP_POLICY_ALLOW_ALL,
			},
		},
	})
	if err != nil {
		log.Fatalln("Unable to Backfill Schedule", err)
	}
// ...
}
// ...
```

### Delete a Schedule {/* #delete-schedule */}

Deleting a Schedule erases a Schedule.
Deletion does not affect any Workflows started by the Schedule.

To delete a Schedule, use `Delete()` on the `ScheduleHandle`.

    View the source code
  {' '}
  in the context of the rest of the application code.

```go
func main() {
// ...
	defer func() {
		log.Println("Deleting schedule", "ScheduleID", scheduleHandle.GetID())
		err = scheduleHandle.Delete(ctx)
		if err != nil {
			log.Fatalln("Unable to delete schedule", err)
		}
	}()
// ...
```

### Describe a Schedule {/* #describe-schedule */}

`Describe` retrieves information about the current Schedule configuration.
This can include details about the Schedule Spec (such as Intervals), CronExpressions, and Schedule State.

To describe a Schedule, use `Describe()` on the ScheduleHandle.

    View the source code
  {' '}
  in the context of the rest of the application code.

```go
func main() {
// ...
	scheduleHandle.Describe(ctx)
// ...
```

### List Schedules {/* #list-schedules */}

The `List` action returns all available Schedules and their respective Schedule IDs.

To return information on all Schedules, use `ScheduleClient.List()`.

    View the source code
  {' '}
  in the context of the rest of the application code.

```go
func main() {
// ...
	listView, _ := temporalClient.ScheduleClient().List(ctx, client.ScheduleListOptions{
		PageSize: 1,
	})

	for listView.HasNext() {
		log.Println(listView.Next())
	}
// ...
```

### Pause a Schedule {/* #pause-schedule */}

`Pause` and `Unpause` enable the start or stop of all future Workflow Runs on a given Schedule.

Pausing a Schedule halts all future Workflow Runs.
Pausing can be enabled by setting `State.Paused` to `true`, or by using `Pause()` on the ScheduleHandle.

Unpausing a Schedule allows the Workflow to execute as planned.
To unpause a Schedule, use `Unpause()` on `ScheduleHandle`.

    View the source code
  {' '}
  in the context of the rest of the application code.

```go
func main() {
// ...
	err = scheduleHandle.Pause(ctx, client.SchedulePauseOptions{
		Note: "The Schedule has been paused.",
	})
// ...
	err = scheduleHandle.Unpause(ctx, client.ScheduleUnpauseOptions{
		Note: "The Schedule has been unpaused.",
	})
```

### Trigger a Schedule {/* #trigger-schedule */}

Triggering a Schedule immediately executes an Action defined in that Schedule.
By default, `trigger` is subject to the Overlap Policy.

To trigger a Scheduled Workflow Execution, use `trigger()` on `ScheduleHandle`.

    View the source code
  {' '}
  in the context of the rest of the application code.

```go
func main() {
// ...
	for i := 0; i < 5; i++ {
		scheduleHandle.Trigger(ctx, client.ScheduleTriggerOptions{
			Overlap: enums.SCHEDULE_OVERLAP_POLICY_ALLOW_ALL,
		})
		time.Sleep(2 * time.Second)
	}
// ...
```

### Update a Schedule {/* #update-schedule */}

Updating a Schedule changes the configuration of an existing Schedule.
These changes can be made to Workflow Actions, Action parameters, Memos, and the Workflow's Cancellation Policy.

Use `Update()` on the ScheduleHandle to modify a Schedule.

    View the source code
  {' '}
  in the context of the rest of the application code.

```go
func main() {
// ...
	updateSchedule := func(input client.ScheduleUpdateInput) (*client.ScheduleUpdate, error) {
		return &client.ScheduleUpdate{
			Schedule: &input.Description.Schedule,
		}, nil
	}

	_ = scheduleHandle.Update(ctx, client.ScheduleUpdateOptions{
		DoUpdate: updateSchedule,
	})
}
// ...
```

## Start Delay {/* #start-delay */}

Use `StartDelay` to schedule a Workflow Execution at a specific one-time future point rather than on a recurring schedule.

Create an instance of [`StartWorkflowOptions`](https://pkg.go.dev/go.temporal.io/sdk/client#StartWorkflowOptions) from the `go.temporal.io/sdk/client` package, set the `StartDelay` field, and pass the instance to the `ExecuteWorkflow` call.

```go
workflowOptions := client.StartWorkflowOptions{
  // ...
  // Start the workflow in 12 hours
  StartDelay: time.Hours * 12,
  // ...
}
workflowRun, err := c.ExecuteWorkflow(context.Background(), workflowOptions, YourWorkflowDefinition)
if err != nil {
  // ...
}
```

## Temporal Cron Jobs {/* #temporal-cron-jobs */}

:::caution Cron support is not recommended

We recommend using [Schedules](https://docs.temporal.io/schedule) instead of Cron Jobs.
Schedules were built to provide a better developer experience, including more configuration options and the ability to update or pause running Schedules.

:::

A [Temporal Cron Job](/cron-job) is the series of Workflow Executions that occur when a Cron Schedule is provided in the call to spawn a Workflow Execution.

A Cron Schedule is provided as an option when the call to spawn a Workflow Execution is made.

Create an instance of [`StartWorkflowOptions`](https://pkg.go.dev/go.temporal.io/sdk/client#StartWorkflowOptions) from the `go.temporal.io/sdk/client` package, set the `CronSchedule` field, and pass the instance to the `ExecuteWorkflow` call.

- Type: `string`
- Default: None

```go
workflowOptions := client.StartWorkflowOptions{
  CronSchedule: "15 8 * * *",
  // ...
}
workflowRun, err := c.ExecuteWorkflow(context.Background(), workflowOptions, YourWorkflowDefinition)
if err != nil {
  // ...
}
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

---

## Selectors - Go SDK

This page shows how to do the following:

- [Use Selectors with Futures](#use-selectors-with-futures)
- [Use Selectors with Timers](#use-selectors-with-timers)
- [Use Selectors with Channels](#use-selectors-with-channels)

In Go, the `select` statement lets a goroutine wait on multiple communication operations.
A `select` **blocks until one of its cases can run**, then it executes that case.
It chooses one at random if multiple are ready.

However, a normal Go select statement can not be used inside of Workflows directly because of the random nature.
