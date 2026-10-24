
## How to develop an Activity Definition in Go {/* #activity-definition */}

In the Temporal Go SDK programming model, an Activity Definition is an exportable function or a `struct` method.
Below is an example of both a basic Activity Definition and of an Activity defined as a Struct method.
An _Activity struct_ can have more than one method, with each method acting as a separate Activity Type.
Activities written as struct methods can use shared struct variables, such as:

- an application level DB pool
- client connection to another service
- reusable utilities
- any other expensive resources that you only want to initialize once per process

Because this is such a common need, the rest of this guide shows Activities written as `struct` methods.

:::note

While it is possible to register struct methods as Workflows, this is strongly discouraged.
In some cases, struct methods as Workflows may cause non-deterministic errors. We recommend
only using struct methods for Activities.

:::

    View the source code
  {' '}
  in the context of the rest of the application code.

```go
package yourapp

    "context"

    "go.temporal.io/sdk/activity"
)
// ...

// YourSimpleActivityDefinition is a basic Activity Definition.
func YourSimpleActivityDefinition(ctx context.Context) error {
    return nil
}

// YourActivityObject is the struct that maintains shared state across Activities.
// If the Worker crashes this Activity object loses its state.
type YourActivityObject struct {
    Message *string
    Number  *int
}

// YourActivityDefinition is your custom Activity Definition.
// An Activity Definition is an exportable function.
func (a *YourActivityObject) YourActivityDefinition(ctx context.Context, param YourActivityParam) (*YourActivityResultObject, error) {
// ...
}
```

### How to develop Activity Parameters {/* #activity-parameters */}

There is no explicit limit to the total number of parameters that an [Activity Definition](/activity-definition) may support.
However, there is a limit to the total size of the data that ends up encoded into a gRPC message Payload.

A single argument is limited to a maximum size of 2 MB.
And the total size of a gRPC message, which includes all the arguments, is limited to a maximum of 4 MB.

Also, keep in mind that all Payload data is recorded in the [Workflow Execution Event History](/workflow-execution/event#event-history) and large Event Histories can affect Worker performance.
This is because the entire Event History could be transferred to a Worker Process with a [Workflow Task](/tasks#workflow-task).

{/* TODO link to gRPC limit section when available */}

Some SDKs require that you pass context objects, others do not.
When it comes to your application data—that is, data that is serialized and encoded into a Payload—we recommend that you use a single object as an argument that wraps the application data passed to Activities.
This is so that you can change what data is passed to the Activity without breaking a function or method signature.

The first parameter of an Activity Definition is `context.Context`.
This parameter is optional for an Activity Definition, though it is recommended, especially if the Activity is expected to use other Go SDK APIs.

An Activity Definition can support as many other custom parameters as needed.
However, all parameters must be serializable (parameters can't be channels, functions, variadic, or unsafe pointers), and it is recommended to pass a single struct that can be updated later.

    View the source code
  {' '}
  in the context of the rest of the application code.

```go
// YourActivityParam is the struct passed to your Activity.
// Use a struct so that your function signature remains compatible if fields change.
type YourActivityParam struct {
    ActivityParamX string
    ActivityParamY int
}
// ...
func (a *YourActivityObject) YourActivityDefinition(ctx context.Context, param YourActivityParam) (*YourActivityResultObject, error) {
// ...
}
```

### How to define Activity return values {/* #activity-return-values */}

All data returned from an Activity must be serializable.

Activity return values are subject to payload size limits in Temporal. The default payload size limit is 2MB, and there is a hard limit of 4MB for any gRPC message size in the Event History transaction ([see Cloud limits here](https://docs.temporal.io/cloud/limits#per-message-grpc-limit)). Keep in mind that all return values are recorded in a [Workflow Execution Event History](/workflow-execution/event#event-history).

A Go-based Activity Definition can return either just an `error` or a `customValue, error` combination (same as a Workflow Definition).
You may wish to use a `struct` type to hold all custom values, just keep in mind they must all be serializable.

    View the source code
  {' '}
  in the context of the rest of the application code.

```go
// YourActivityResultObject is the struct returned from your Activity.
// Use a struct so that you can return multiple values of different types.
// Additionally, your function signature remains compatible if the fields change.
type YourActivityResultObject struct {
    ResultFieldX string
    ResultFieldY int
}
// ...
func (a *YourActivityObject) YourActivityDefinition(ctx context.Context, param YourActivityParam) (*YourActivityResultObject, error) {
// ...
    result := &YourActivityResultObject{
        ResultFieldX: "Success",
        ResultFieldY: 1,
    }
    // Return the results back to the Workflow Execution.
    // The results persist within the Event History of the Workflow Execution.
    return result, nil
}
```

### How to customize Activity Type in Go {/* #customize-activity-type */}

To customize the Activity Type, set the `Name` parameter with `RegisterOptions` when registering your Activity with a Worker.

    View the source code
  {' '}
  in the context of the rest of the application code.

```go
func main() {
// ...
    yourWorker := worker.New(temporalClient, "your-custom-task-queue-name", worker.Options{})
// ...
    // Use RegisterOptions to change the name of the Activity Type for example.
    registerAOptions := activity.RegisterOptions{
        Name: "JustAnotherActivity",
    }
    yourWorker.RegisterActivityWithOptions(yourapp.YourSimpleActivityDefinition, registerAOptions)
    // Run the Worker
    err = yourWorker.Run(worker.InterruptCh())
// ...
}
// ...
```

---

## Benign exceptions - Go SDK

When Activities return errors that are expected or not severe, they can create noise in your logs, metrics, and OpenTelemetry traces, making it harder to identify real issues.
By marking these errors as benign, you can exclude them from your observability data while still handling them in your Workflow logic.

To mark an error as benign, use [`temporal.NewApplicationErrorWithOptions`](https://pkg.go.dev/go.temporal.io/sdk/temporal#NewApplicationErrorWithOptions) and set the `Category` field to `temporal.ApplicationErrorCategoryBenign` in the `ApplicationErrorOptions`.

Benign errors:
- Have Activity failure logs downgraded to DEBUG level
- Do not emit Activity failure metrics
- Do not set the OpenTelemetry failure status to ERROR

```go

	"go.temporal.io/sdk/activity"
	"go.temporal.io/sdk/temporal"
)

func MyActivity(ctx context.Context) (string, error) {
	result, err := callExternalService()
	if err != nil {
		// Mark this error as benign since it's expected
		return "", temporal.NewApplicationErrorWithOptions(
			err.Error(),
			"",
			temporal.ApplicationErrorOptions{
				Category: temporal.ApplicationErrorCategoryBenign,
			},
		)
	}
	return result, nil
}
```

Use benign exceptions for Activity errors that occur regularly as part of normal operations, such as polling an external service that isn't ready yet, or handling expected transient failures that will be retried.

---

## Dynamic Activity - Go SDK

## Set a Dynamic Activity {/* #set-a-dynamic-activity */}

A Dynamic Activity in Temporal is an Activity that is invoked dynamically at runtime if no other Activity with the same name is registered.
An Activity can be registered as dynamic by using `worker.RegisterDynamicActivity()`.
You must register the Activity with the Worker before it can be invoked.
Only one Dynamic Activity can be present on a Worker.

The Activity Definition must then accept a single argument of type `converter.EncodedValues`.
This code snippet is taken from the [Dynamic Workflow example from samples-go](https://github.com/temporalio/samples-go/tree/main/dynamic-workflows).

```go
func DynamicActivity(ctx context.Context, args converter.EncodedValues) (string, error) {
	var arg1, arg2 string
	err := args.Get(&arg1, &arg2)
	if err != nil {
		return "", fmt.Errorf("failed to decode arguments: %w", err)
	}

	info := activity.GetInfo(ctx)
	result := fmt.Sprintf("%s - %s - %s", info.WorkflowType.Name, arg1, arg2)

	return result, nil
}
```

---

## Activity execution - Go SDK

## How to start an Activity Execution {/* #activity-execution */}

Calls to spawn [Activity Executions](/activity-execution) are written within a [Workflow Definition](/workflow-definition).
The call to spawn an Activity Execution generates the [ScheduleActivityTask](/references/commands#scheduleactivitytask) Command.
This results in the set of three [Activity Task](/tasks#activity-task) related Events ([ActivityTaskScheduled](/references/events#activitytaskscheduled), [ActivityTaskStarted](/references/events#activitytaskstarted), and ActivityTask[Closed]) in your Workflow Execution Event History.

A single instance of the Activities implementation is shared across multiple simultaneous Activity invocations.
Activity implementation code should be _idempotent_.

The values passed to Activities through invocation parameters or returned through a result value are recorded in the Execution history.
The entire Execution history is transferred from the Temporal Service to Workflow Workers when a Workflow state needs to recover.
A large Execution history can thus adversely impact the performance of your Workflow.

Therefore, be mindful of the amount of data you transfer through Activity invocation parameters or Return Values.
Otherwise, no additional limitations exist on Activity implementations.

    To spawn an [Activity Execution](/activity-execution), call [`ExecuteActivity()`](https://pkg.go.dev/go.temporal.io/sdk/workflow#ExecuteActivity) inside your Workflow Definition.
    The API is available from the [`go.temporal.io/sdk/workflow`](https://pkg.go.dev/go.temporal.io/sdk/workflow) package.
    The `ExecuteActivity()` API call requires an instance of `workflow.Context`, the Activity function name, and any variables to be passed to the Activity Execution.
        The Activity function name can be provided as a variable object (no quotations) or as a string.
        The benefit of passing the actual function object is that the framework can validate the parameters against the Activity Definition.
        The `ExecuteActivity` call returns a Future, which can be used to get the result of the Activity Execution.

    View the source code
  {' '}
  in the context of the rest of the application code.

```go
func YourWorkflowDefinition(ctx workflow.Context, param YourWorkflowParam) (*YourWorkflowResultObject, error) {
    // Set the options for the Activity Execution.
    // Either StartToClose Timeout OR ScheduleToClose is required.
    // Not specifying a Task Queue will default to the parent Workflow Task Queue.
    activityOptions := workflow.ActivityOptions{
        StartToCloseTimeout: 10 * time.Second,
    }
    ctx = workflow.WithActivityOptions(ctx, activityOptions)
    activityParam := YourActivityParam{
        ActivityParamX: param.WorkflowParamX,
        ActivityParamY: param.WorkflowParamY,
    }
    // Use a nil struct pointer to call Activities that are part of a struct.
    var a *YourActivityObject
    // Execute the Activity and wait for the result.
    var activityResult YourActivityResultObject
    err := workflow.ExecuteActivity(ctx, a.YourActivityDefinition, activityParam).Get(ctx, &activityResult)
    if err != nil {
        return nil, err
    }
// ...
}
```

### How to set the required Activity Timeouts {/* #required-timeout */}

Activity Execution semantics rely on several parameters.
The only required value that needs to be set is either a [Schedule-To-Close Timeout](/encyclopedia/detecting-activity-failures#schedule-to-close-timeout) or a [Start-To-Close Timeout](/encyclopedia/detecting-activity-failures#start-to-close-timeout).
These values are set in the Activity Options.

To set an Activity Timeout in Go, create an instance of `ActivityOptions` from the `go.temporal.io/sdk/workflow` package, set the Activity Timeout field, and then use the `WithActivityOptions()` API to apply the options to the instance of `workflow.Context`.

Available timeouts are:

- `StartToCloseTimeout`
- `ScheduleToClose`
- `ScheduleToStartTimeout`

```go
activityOptions := workflow.ActivityOptions{
  // Set Activity Timeout duration
  ScheduleToCloseTimeout: 10 * time.Second,
  // StartToCloseTimeout: 10 * time.Second,
  // ScheduleToStartTimeout: 10 * time.Second,
}
ctx = workflow.WithActivityOptions(ctx, activityOptions)
var yourActivityResult YourActivityResult
err = workflow.ExecuteActivity(ctx, YourActivityDefinition, yourActivityParam).Get(ctx, &yourActivityResult)
if err != nil {
  // ...
}
```

### Go ActivityOptions reference {/* #activity-options-reference */}

Create an instance of [`ActivityOptions`](https://pkg.go.dev/go.temporal.io/sdk/workflow#ActivityOptions) from the `go.temporal.io/sdk/workflow` package and use [`WithActivityOptions()`](https://pkg.go.dev/go.temporal.io/sdk/workflow#WithActivityOptions) to apply it to the instance of `workflow.Context`.

The instance of `workflow.Context` is then passed to the `ExecuteActivity()` call.

| Field                                               | Required                          | Type                                                                        |
| --------------------------------------------------- | --------------------------------- | --------------------------------------------------------------------------- |
| [`ActivityID`](#activityid)                         | No                                | `string`                                                                    |
| [`TaskQueueName`](#taskqueuename)                   | No                                | `string`                                                                    |
| [`ScheduleToCloseTimeout`](#scheduletoclosetimeout) | Yes (or `StartToCloseTimeout`)    | `time.Duration`                                                             |
| [`ScheduleToStartTimeout`](#scheduletostarttimeout) | No                                | `time.Duration`                                                             |
| [`StartToCloseTimeout`](#scheduletoclosetimeout)    | Yes (or `ScheduleToCloseTimeout`) | `time.Duration`                                                             |
| [`HeartbeatTimeout`](#heartbeattimeout)             | No                                | `time.Duration`                                                             |
| [`WaitForCancellation`](#waitforcancellation)       | No                                | `bool`                                                                      |
| [`OriginalTaskQueueName`](#originaltaskqueuename)   | No                                | `string`                                                                    |
| [`RetryPolicy`](#retrypolicy)                       | No                                | [`RetryPolicy`](https://pkg.go.dev/go.temporal.io/sdk/temporal#RetryPolicy) |

#### ActivityID

- Type: `string`
- Default: None

```go
activityOptions := workflow.ActivityOptions{
  ActivityID: "your-activity-id",
}
ctx = workflow.WithActivityOptions(ctx, activityOptions)
var yourActivityResult YourActivityResult
err = workflow.ExecuteActivity(ctx, YourActivityDefinition, yourActivityParam).Get(ctx, &yourActivityResult)
if err != nil {
  // ...
}
```

- [What is an Activity Id](/activity-execution#activity-id)

#### TaskQueueName

- Type: `string`
- Default: Inherits the TaskQueue name from the Workflow.

```go
activityOptions := workflow.ActivityOptions{
  TaskQueueName: "your-task-queue-name",
}
ctx = workflow.WithActivityOptions(ctx, activityOptions)
var yourActivityResult YourActivityResult
err = workflow.ExecuteActivity(ctx, YourActivityDefinition, yourActivityParam).Get(ctx, &yourActivityResult)
if err != nil {
  // ...
}
```

- [What is a Task Queue](/task-queue)

#### ScheduleToCloseTimeout

To set a [Schedule-To-Close Timeout](/encyclopedia/detecting-activity-failures#schedule-to-close-timeout), create an instance of `ActivityOptions` from the `go.temporal.io/sdk/workflow` package, set the `ScheduleToCloseTimeout` field, and then use the `WithActivityOptions()` API to apply the options to the instance of `workflow.Context`.

This or `StartToCloseTimeout` must be set.

- Type: `time.Duration`
- Default: ∞ (infinity - no limit)

```go
activityOptions := workflow.ActivityOptions{
  ScheduleToCloseTimeout: 10 * time.Second,
}
ctx = workflow.WithActivityOptions(ctx, activityOptions)
var yourActivityResult YourActivityResult
err = workflow.ExecuteActivity(ctx, YourActivityDefinition, yourActivityParam).Get(ctx, &yourActivityResult)
if err != nil {
  // ...
}
```

#### ScheduleToStartTimeout

To set a [Schedule-To-Start Timeout](/encyclopedia/detecting-activity-failures#schedule-to-start-timeout), create an instance of `ActivityOptions` from the `go.temporal.io/sdk/workflow` package, set the `ScheduleToStartTimeout` field, and then use the `WithActivityOptions()` API to apply the options to the instance of `workflow.Context`.

- Type: `time.Duration`
- Default: ∞ (infinity - no limit)

```go
activityOptions := workflow.ActivityOptions{
  ScheduleToStartTimeout: 10 * time.Second,
}
ctx = workflow.WithActivityOptions(ctx, activityOptions)
var yourActivityResult YourActivityResult
err = workflow.ExecuteActivity(ctx, YourActivityDefinition, yourActivityParam).Get(ctx, &yourActivityResult)
if err != nil {
  // ...
}
```

#### StartToCloseTimeout

To set a [Start-To-Close Timeout](/encyclopedia/detecting-activity-failures#start-to-close-timeout), create an instance of `ActivityOptions` from the `go.temporal.io/sdk/workflow` package, set the `StartToCloseTimeout` field, and then use the `WithActivityOptions()` API to apply the options to the instance of `workflow.Context`.

This or `ScheduleToCloseTimeout` must be set.

- Type: `time.Duration`
- Default: Same as the `ScheduleToCloseTimeout`

```go
activityOptions := workflow.ActivityOptions{
  StartToCloseTimeout: 10 * time.Second,
}
ctx = workflow.WithActivityOptions(ctx, activityOptions)
var yourActivityResult YourActivityResult
err = workflow.ExecuteActivity(ctx, YourActivityDefinition, yourActivityParam).Get(ctx, &yourActivityResult)
if err != nil {
  // ...
}
```

#### HeartbeatTimeout

To set a [Heartbeat Timeout](/encyclopedia/detecting-activity-failures#heartbeat-timeout), create an instance of `ActivityOptions` from the `go.temporal.io/sdk/workflow` package, set the `HeartbeatTimeout` field, and then use the `WithActivityOptions()` API to apply the options to the instance of `workflow.Context`.

```go
activityOptions := workflow.ActivityOptions{
  HeartbeatTimeout: 10 * time.Second,
}
ctx = workflow.WithActivityOptions(ctx, activityOptions)
var yourActivityResult YourActivityResult
err = workflow.ExecuteActivity(ctx, YourActivityDefinition, yourActivityParam).Get(ctx, &yourActivityResult)
if err != nil {
  // ...
}
```

#### WaitForCancellation

If `true` the Activity Execution will finish executing should there be a Cancellation request.

- Type: `bool`
- Default: `false`

```go
activityOptions := workflow.ActivityOptions{
  WaitForCancellation: false,
}
ctx = workflow.WithActivityOptions(ctx, activityOptions)
var yourActivityResult YourActivityResult
err = workflow.ExecuteActivity(ctx, YourActivityDefinition, yourActivityParam).Get(ctx, &yourActivityResult)
if err != nil {
  // ...
}
```

#### OriginalTaskQueueName

```go
activityOptions := workflow.ActivityOptions{
  OriginalTaskQueueName: "your-original-task-queue-name",
}
ctx = workflow.WithActivityOptions(ctx, activityOptions)
var yourActivityResult YourActivityResult
err = workflow.ExecuteActivity(ctx, YourActivityDefinition, yourActivityParam).Get(ctx, &yourActivityResult)
if err != nil {
  // ...
}
```

#### RetryPolicy

To set a [RetryPolicy](/encyclopedia/retry-policies), create an instance of `ActivityOptions` from the `go.temporal.io/sdk/workflow` package, set the `RetryPolicy` field, and then use the `WithActivityOptions()` API to apply the options to the instance of `workflow.Context`.

- Type: [`RetryPolicy`](https://pkg.go.dev/go.temporal.io/sdk/temporal#RetryPolicy)
- Default:

```go
retryPolicy := &temporal.RetryPolicy{
  InitialInterval:    time.Second,
  BackoffCoefficient: 2.0,
  MaximumInterval:    time.Second * 100, // 100 * InitialInterval
  MaximumAttempts:    0, // Unlimited
  NonRetryableErrorTypes: []string, // empty
}
```

Providing a Retry Policy here is a customization that overwrites individual Field defaults.

```go
retryPolicy := &temporal.RetryPolicy{
  InitialInterval:    time.Second,
  BackoffCoefficient: 2.0,
  MaximumInterval:    time.Second * 100,
}

activityOptions := workflow.ActivityOptions{
  RetryPolicy: retryPolicy,
}
ctx = workflow.WithActivityOptions(ctx, activityOptions)
var yourActivityResult YourActivityResult
err = workflow.ExecuteActivity(ctx, YourActivityDefinition, yourActivityParam).Get(ctx, &yourActivityResult)
if err != nil {
  // ...
}
```

### How to get the results of an Activity Execution {/* #get-activity-results */}

The call to spawn an [Activity Execution](/activity-execution) generates the [ScheduleActivityTask](/references/commands#scheduleactivitytask) Command and provides the Workflow with an Awaitable.
Workflow Executions can either block progress until the result is available through the Awaitable or continue progressing, making use of the result when it becomes available.

The `ExecuteActivity` API call returns an instance of [`workflow.Future`](https://pkg.go.dev/go.temporal.io/sdk/workflow#Futures) which has the following two methods:

- `Get()`: Takes an instance of the `workflow.Context`, that was passed to the Activity Execution, and a pointer as parameters.
  The variable associated with the pointer is populated with the Activity Execution result.
  This call blocks until the results are available.
- `IsReady()`: Returns `true` when the result of the Activity Execution is ready.

Call the `Get()` method on the instance of `workflow.Future` to get the result of the Activity Execution.
The type of the result parameter must match the type of the return value declared by the Activity function.

```go
func YourWorkflowDefinition(ctx workflow.Context, param YourWorkflowParam) (YourWorkflowResponse, error) {
 // ...
 future := workflow.ExecuteActivity(ctx, YourActivityDefinition, yourActivityParam)
 var yourActivityResult YourActivityResult
 if err := future.Get(ctx, &yourActivityResult); err != nil {
   // ...
 }
 // ...
}
```

Use the `IsReady()` method first to make sure the `Get()` call doesn't cause the Workflow Execution to wait on the result.

```go
func YourWorkflowDefinition(ctx workflow.Context, param YourWorkflowParam) (YourWorkflowResponse, error) {
 // ...
 future := workflow.ExecuteActivity(ctx, YourActivityDefinition, yourActivityParam)
 // ...
 if(future.IsReady()) {
   var yourActivityResult YourActivityResult
   if err := future.Get(ctx, &yourActivityResult); err != nil {
     // ...
   }
 }
 // ...
}
```

It is idiomatic to invoke multiple Activity Executions from within a Workflow.
Therefore, it is also idiomatic to either block on the results of the Activity Executions or continue on to execute additional logic, checking for the Activity Execution results at a later time.

---

## Activities - Go SDK

![Go SDK Banner](/img/assets/banner-go-temporal.png)

## Activities

- [Activity basics](/develop/go/activities/basics)
- [Activity execution](/develop/go/activities/execution)
- [Standalone Activities](/develop/go/activities/standalone-activities)
- [Timeouts](/develop/go/activities/timeouts)
- [Asynchronous Activity completion](/develop/go/activities/asynchronous-activity)
- [Dynamic Activity](/develop/go/activities/dynamic-activity)
- [Benign exceptions](/develop/go/activities/benign-exceptions)

---

## Standalone Activities - Go SDK

<ReleaseNoteHeader
  featureName="standaloneActivity"
/>

Standalone Activities are Activity Executions that run independently, without being orchestrated by a Workflow. Instead
of starting an Activity from within a Workflow Definition using `workflow.ExecuteActivity()`, you start a Standalone
Activity directly from a Temporal Client using `client.ExecuteActivity()`.

The Activity definition and Worker registration are identical to regular Activities, and only the execution path
differs.

This page covers the following:

- [Get Started with Standalone Activities](#get-started)
- [Define your Activity](#define-activity)
- [Run a Worker with the Activity registered](#run-worker)
- [Execute a Standalone Activity](#execute-activity)
- [Get the result of a Standalone Activity](#get-activity-result)
- [Get a handle to an existing Standalone Activity](#get-activity-handle)
- [List Standalone Activities](#list-activities)
