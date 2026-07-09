
Enable X-Ray active tracing on the Lambda function:

```bash
aws lambda update-function-configuration \
  --function-name <your-function-name> \
  --tracing-config Mode=Active
```

The Lambda execution role must have permissions to write to X-Ray and CloudWatch.
Add `xray:PutTraceSegments`, `xray:PutTelemetryRecords`, and `cloudwatch:PutMetricData` permissions to the execution role.
Without these permissions, the Collector fails silently and no telemetry appears.

If you only need metrics or tracing, use `otel.ApplyMetrics` or `otel.ApplyTracing` individually.

---

## Serverless Workers - Go SDK

Serverless Workers run on ephemeral, on-demand compute rather than long-lived processes.
Temporal invokes the Worker when Tasks arrive, and the Worker shuts down when the work is done.

For a general overview of how Serverless Workers work, see [Serverless Workers](/serverless-workers).
For the end-to-end deployment guide, see [Deploy a Serverless Worker](/production-deployment/worker-deployments/serverless-workers).

## Supported providers

- [**AWS Lambda**](/develop/go/workers/serverless-workers/aws-lambda) - Use the `lambdaworker` package to run a Worker as a Lambda function. Covers setup, configuration, Lambda-tuned defaults, observability, and the invocation lifecycle.

---

## Worker Sessions - Go SDK

This page shows how to do the following:

- [Enable Worker Sessions](#enable-sessions)
- [Change the maximum concurrent Sessions of a Worker](#max-concurrent-sessions)
- [Create a Worker Session](#create-a-session)

:::tip

This feature is currently available only in the Go SDK.

:::

A Worker Session is a feature that provides a straightforward API for [Task Routing](/task-routing) to ensure that Activity Tasks are executed with the same Worker without requiring you to manually specify Task Queue names.

## Enable Worker Sessions {/* #enable-sessions */}

Set `EnableSessionWorker` to `true` in the Worker options.

    View the source code
  {' '}
  in the context of the rest of the application code.

```go
// ...
func main() {
// ...
	// Enable Sessions for this Worker.
	workerOptions := worker.Options{
		EnableSessionWorker: true,
// ...
	}
	w := worker.New(temporalClient, "fileprocessing", workerOptions)
	w.RegisterWorkflow(sessions.SomeFileProcessingWorkflow)
	w.RegisterActivity(&sessions.FileActivities{})
	err = w.Run(worker.InterruptCh())
// ...
}
```

### Change the maximum concurrent Sessions of a Worker. {/* #max-concurrent-sessions */}

You can adjust the maximum concurrent Sessions of a Worker.

To limit the number of concurrent Sessions running on a Worker, set the `MaxConcurrentSessionExecutionSize` field of `worker.Options` to the desired value.
By default, this field is set to a very large value, so there's no need to manually set it if no limitation is needed.

If a Worker hits this limitation, it won't accept any new `CreateSession()` requests until one of the existing sessions is completed.
If the session can't be created within `CreationTimeout`, `CreateSession()` returns an error .

    View the source code
  {' '}
  in the context of the rest of the application code.

```go
func main() {
// ...
	workerOptions := worker.Options{
// ...
		// This configures the maximum allowed concurrent sessions.
		// Customize this value only if you need to.
		MaxConcurrentSessionExecutionSize: 1000,
// ...
}
// ...
```

## Create a Worker Session {/* #create-a-session */}

Within the Workflow code use the Workflow APIs to create a Session with whichever Worker picks up the first Activity Task.

Use the [`CreateSession`](https://pkg.go.dev/go.temporal.io/sdk/workflow#CreateSession) API to create a Context object that can be passed to calls to spawn Activity Executions.

Pass an instance of `workflow.Context` and [`SessionOptions`](https://pkg.go.dev/go.temporal.io/sdk/workflow#SessionOptions) to the `CreateSession` API call and get a Session Context that contains metadata information of the Session.

Use the Session Context to spawn all Activity Executions that should belong to the Session.
All associated Activity Tasks are then processed by the same Worker Entity.
When the `CreateSession` API is called, the Task Queue name that is specified in `ActivityOptions` (or in `StartWorkflowOptions` if the Task Queue name is not specified in `ActivityOptions`) is used, and a Session is created with one of the Workers polling that Task Queue.

The Session Context is cancelled if the Worker executing this Session dies or `CompleteSession()` is called.
When using the returned Session Context to spawn Activity Executions, a `workflow.ErrSessionFailed` error is returned if the Session framework detects that the Worker executing this Session has died.
The failure of Activity Executions won't affect the state of the Session, so you still need to handle the errors returned from your Activities and call `CompleteSession()` if necessary.

If the context passed in already contains an open Session, `CreateSession()` returns an error.
If all the Workers are currently busy and unable to handle a new Session, the framework keeps retrying until the `CreationTimeout` period you specified in `SessionOptions` has passed before returning an error.
(For more details, check the "Concurrent Session Limitation" section.)

`CompleteSession()` releases the resources reserved on the Worker, so it's important to call it as soon as you no longer need the Session.
It cancels the session context and therefore all the Activity Executions using that Session Context.
It is safe to call `CompleteSession()` on a failed Session, meaning that you can call it from a `defer` function after the Session is successfully created.

If the Worker goes down between Activities, any scheduled Activities meant for the Session Worker are canceled.
If not, you get a `workflow.ErrSessionFailed` error when the next call of `workflow.ExecuteActivity()` is made from that Workflow.

    View the source code
  {' '}
  in the context of the rest of the application code.

```go
package sessions

	"time"

	"go.temporal.io/sdk/workflow"
)

// ...
// SomeFileProcessingWorkflow is a Workflow Definition.
func SomeFileProcessingWorkflow(ctx workflow.Context, param FileProcessingWFParam) error {
	activityOptions := workflow.ActivityOptions{
		StartToCloseTimeout: time.Minute,
	}
	ctx = workflow.WithActivityOptions(ctx, activityOptions)
// ...
	sessionOptions := &workflow.SessionOptions{
		CreationTimeout:  time.Minute,
		ExecutionTimeout: time.Minute,
	}
	// Create a Session with the Worker so that all Activities execute with the same Worker.
	sessionCtx, err := workflow.CreateSession(ctx, sessionOptions)
	if err != nil {
		return err
	}
	defer workflow.CompleteSession(sessionCtx)
// ...
	err = workflow.ExecuteActivity(sessionCtx, a.DownloadFile, param).Get(sessionCtx, &downloadResult)
// ...
	err = workflow.ExecuteActivity(sessionCtx, a.ProcessFile, processParam).Get(sessionCtx, &processResult)
// ...
	err = workflow.ExecuteActivity(sessionCtx, a.UploadFile, uploadParam).Get(sessionCtx, nil)
// ...
}
```

## Additional Session usage information {/* #session-metadata */}

```go
type SessionInfo struct {
 // A unique Id for the session
 SessionID         string
 // The hostname of the worker that is executing the session
 HostName          string
 // ... other unexported fields
}

func GetSessionInfo(ctx Context) *SessionInfo
```

The Session Context also stores some Session metadata, which can be retrieved by the `GetSessionInfo()` API.
If the Context passed in doesn't contain any Session metadata, this API will return a `nil` pointer.

### Recreate Session

For long-running Sessions, you may want to use the `ContinueAsNew` feature to split the Workflow into multiple runs when all Activities need to be executed by the same Worker.
The `RecreateSession()` API is designed for such a use case.

```go
func RecreateSession(ctx Context, recreateToken []byte, sessionOptions *SessionOptions) (Context, error)
```

Its usage is the same as `CreateSession()` except that it also takes in a `recreateToken`, which is needed to create a new Session on the same Worker as the previous one.
You can get the token by calling the `GetRecreateToken()` method of the `SessionInfo` object.

```go
token := workflow.GetSessionInfo(sessionCtx).GetRecreateToken()
```

**Is there a complete example?**

Yes, the [file processing example](https://github.com/temporalio/samples-go/tree/main/fileprocessing) in the [temporalio/samples-go](https://github.com/temporalio/samples-go) repo has been updated to use the session framework.

**What happens to my Activity if the Worker dies?**

If your Activity has already been scheduled, it will be canceled.
If not, you will get a `workflow.ErrSessionFailed` error when you call `workflow.ExecuteActivity()`.

**Is the concurrent session limitation per process or per host?**

It's per Worker Process, so make sure there's only one Worker Process running on the host if you plan to use this feature.

**Future Work**

- Right now, a Session is considered failed if the Worker Process dies.
  However, for some use cases, you may only care whether the Worker host is alive or not.
  For these use cases, the Session should be automatically re-established if the Worker Process is restarted.

- The current implementation assumes that all Sessions are consuming the same type of resource and there's only one global limitation.
  Our plan is to allow you to specify what type of resource your Session will consume and enforce different limitations on different types of resources.

---

## Workflow basics - Go SDK

## How to develop a basic Workflow {/* #develop-workflows */}

Workflows are the fundamental unit of a Temporal Application, and it all starts with the development of a [Workflow Definition](/workflow-definition).

In the Temporal Go SDK programming model, a [Workflow Definition](/workflow-definition) is an exportable function.
Below is an example of a basic Workflow Definition.

    View the source code
  {' '}
  in the context of the rest of the application code.

```go
package yourapp

    "time"

    "go.temporal.io/sdk/workflow"
)
// ...

// YourSimpleWorkflowDefinition is the most basic Workflow Definition.
func YourSimpleWorkflowDefinition(ctx workflow.Context) error {
    // ...
    return nil
}
```

### How to define Workflow parameters {/* #workflow-parameters */}

Temporal Workflows may have any number of custom parameters.
However, we strongly recommend that objects are used as parameters, so that the object's individual fields may be altered without breaking the signature of the Workflow.
All Workflow Definition parameters must be serializable.

The first parameter of a Go-based Workflow Definition must be of the [`workflow.Context`](https://pkg.go.dev/go.temporal.io/sdk/workflow#Context) type.
It is used by the Temporal Go SDK to pass around Workflow Execution context, and virtually all the Go SDK APIs that are callable from the Workflow require it.
It is acquired from the [`go.temporal.io/sdk/workflow`](https://pkg.go.dev/go.temporal.io/sdk/workflow) package.

The `workflow.Context` entity operates similarly to the standard `context.Context` entity provided by Go.
The only difference between `workflow.Context` and `context.Context` is that the `Done()` function, provided by `workflow.Context`, returns `workflow.Channel` instead of the standard Go `chan`.

Additional parameters can be passed to the Workflow when it is invoked.
A Workflow Definition may support multiple custom parameters, or none.
These parameters can be regular type variables or safe pointers.
However, the best practice is to pass a single parameter that is of a `struct` type, so there can be some backward compatibility if new parameters are added.

All Workflow Definition parameters must be serializable and can't be channels, functions, variadic, or unsafe pointers.

    View the source code
  {' '}
  in the context of the rest of the application code.

```go
package yourapp

    "time"

    "go.temporal.io/sdk/workflow"
)

// YourWorkflowParam is the object passed to the Workflow.
type YourWorkflowParam struct {
    WorkflowParamX string
    WorkflowParamY int
}
// ...
// YourWorkflowDefinition is your custom Workflow Definition.
func YourWorkflowDefinition(ctx workflow.Context, param YourWorkflowParam) (*YourWorkflowResultObject, error) {
// ...
}
```

### How to define Workflow return parameters {/* #workflow-return-values */}

Workflow return values must also be serializable.
Returning results, returning errors, or throwing exceptions is fairly idiomatic in each language that is supported.
However, Temporal APIs that must be used to get the result of a Workflow Execution will only ever receive one of either the result or the error.

A Go-based Workflow Definition can return either just an `error` or a `customValue, error` combination.
Again, the best practice here is to use a `struct` type to hold all custom values.
A Workflow Definition written in Go can return both a custom value and an error.
However, it's not possible to receive both a custom value and an error in the calling process, as is normal in Go.
The caller will receive either one or the other.
Returning a non-nil `error` from a Workflow indicates that an error was encountered during its execution and the Workflow Execution should be terminated, and any custom return values will be ignored by the system.

    View the source code
  {' '}
  in the context of the rest of the application code.

```go
package yourapp

    "time"

    "go.temporal.io/sdk/workflow"
)
// ...

// YourWorkflowResultObject is the object returned by the Workflow.
type YourWorkflowResultObject struct {
    WFResultFieldX string
    WFResultFieldY int
}
// ...
// YourWorkflowDefinition is your custom Workflow Definition.
func YourWorkflowDefinition(ctx workflow.Context, param YourWorkflowParam) (*YourWorkflowResultObject, error) {
// ...
    if err != nil {
        return nil, err
    }
    // Make the results of the Workflow Execution available.
    workflowResult := &YourWorkflowResultObject{
        WFResultFieldX: activityResult.ResultFieldX,
        WFResultFieldY: activityResult.ResultFieldY,
    }
    return workflowResult, nil
}
```

### How to customize Workflow Type in Go {/* #customize-workflow-type */}

In Go, by default, the Workflow Type name is the same as the function name.

To customize the Workflow Type, set the `Name` parameter with `RegisterOptions` when registering your Workflow with a Worker.

    View the source code
  {' '}
  in the context of the rest of the application code.

```go
package main

    "log"

    "go.temporal.io/sdk/activity"
    "go.temporal.io/sdk/client"
    "go.temporal.io/sdk/worker"
    "go.temporal.io/sdk/workflow"

    "documentation-samples-go/yourapp"
)
// ...
func main() {
// ...
    yourWorker := worker.New(temporalClient, "your-custom-task-queue-name", worker.Options{})
// ...
    // Use RegisterOptions to set the name of the Workflow Type for example.
    registerWFOptions := workflow.RegisterOptions{
        Name: "JustAnotherWorkflow",
    }
    yourWorker.RegisterWorkflowWithOptions(yourapp.YourSimpleWorkflowDefinition, registerWFOptions)
// ...
}
```

### How to develop Workflow logic {/* #workflow-logic-requirements */}

Workflow logic is constrained by [deterministic execution requirements](/workflow-definition#deterministic-constraints). Each Temporal SDK provides a set of APIs that can be used inside your Workflow to interact with application code outside the Workflow.

In Go, Workflow Definition code cannot directly do the following:

- Iterate over maps using `range`, because with `range` the order of the map's iteration is randomized.
  Instead you can collect the keys of the map, sort them, and then iterate over the sorted keys to access the map.
  This technique provides deterministic results.
  You can also use a Side Effect or an Activity to process the map instead.
- Call an external API, conduct a file I/O operation, talk to another service, etc. (Use an Activity for these.)

The Temporal Go SDK has APIs to handle equivalent Go constructs:

- `workflow.Now()` This is a replacement for `time.Now()`.
- `workflow.Sleep()` This is a replacement for `time.Sleep()`.
- `workflow.GetLogger()` This ensures that the provided logger does not duplicate logs during a replay.
- `workflow.Go()` This is a replacement for the `go` statement.
- `workflow.Channel` This is a replacement for the native `chan` type.
  Temporal provides support for both buffered and unbuffered channels.
- `workflow.Selector` This is a replacement for the `select` statement.
  Learn more on the [Go SDK Selectors](https://legacy-documentation-sdks.temporal.io/go/selectors) page.
- `workflow.Context` This is a replacement for `context.Context`.
  See [Tracing](/develop/go/platform/observability#tracing) for more information about context propagation.

---

## Cancel a Workflow - Go SDK

This page shows the following:

- How to handle a Cancellation request within a Workflow.
- How to set an Activity Heartbeat Timeout.
- How to listen for and handle a Cancellation request within an Activity.
- How to send a Cancellation request from a Temporal Client.
- Heartbeating after a Cancellation.

## Handle Cancellation in Workflow {/* #handle-cancellation-in-workflow */}

Workflow Definitions can be written to handle execution cancellation requests with Go's `defer` and the
`workflow.NewDisconnectedContext` API. In the Workflow Definition, there is a special Activity that handles clean up
should the execution be cancelled.

If the Workflow receives a Cancellation Request, but all Activities gracefully handle the Cancellation, and/or no
Activities are skipped then the Workflow status will be Complete. It is completely up to the needs of the business
process and your use case which determines whether you want to return the Cancellation error to show a Canceled status
or Complete status regardless of whether a Cancellation has propagated to and/or skipped Activities.

<!--SNIPSTART go-features-cancellation-workflow {"selectedLines": ["14-15", "18", "20-38", "41", "43-45", "47-50"]}-->
[sample-apps/go/features/cancellation/workflow.go](https://github.com/temporalio/documentation/blob/main/sample-apps/go/features/cancellation/workflow.go)
```go
// ...
// YourWorkflow is a Workflow Definition that shows how it can be canceled.
func YourWorkflow(ctx workflow.Context) error {
// ...
	activityOptions := workflow.ActivityOptions{
// ...
		HeartbeatTimeout:    5 * time.Second,
		// Set WaitForCancellation to true to have the Workflow wait to return
		// until all in progress Activities have completed, failed, or accepted the Cancellation.
		WaitForCancellation: true,
	}
	defer func() {
		// This logic ensures cleanup only happens if there is a Cancelation error
		if !errors.Is(ctx.Err(), workflow.ErrCanceled) {
			return
		}
		// For the Workflow to execute an Activity after it receives a Cancellation Request
		// It has to get a new disconnected context
		newCtx, _ := workflow.NewDisconnectedContext(ctx)
		// This Activity is only executed if
		err := workflow.ExecuteActivity(newCtx, a.CleanupActivity).Get(ctx, nil)
		if err != nil {
			logger.Error("CleanupActivity failed", "Error", err)
		}
	}()
// ...
	err := workflow.ExecuteActivity(ctx, a.ActivityToBeCanceled).Get(ctx, &result)
// ...
	// This call to execute the Activity is expected to return an error "canceled".
	// And the Activity Execution is skipped.
	err = workflow.ExecuteActivity(ctx, a.ActivityToBeSkipped).Get(ctx, nil)
// ...
	// Return any errors.
	// If a CanceledError is returned, the Workflow changes to a Canceled state.
	return err
}
```
<!--SNIPEND-->

## Handle Cancellation in an Activity {/* #handle-cancellation-in-an-activity */}

**How to handle a Cancellation in an Activity in Go.**

Ensure that the Activity is Heartbeating to receive the Cancellation request and stop execution.

    View the source code
  {' '}
  in the context of the rest of the application code.

```go
// ActivityToBeCanceled is the Activity that will respond to the Cancellation Request
func (a *Activities) ActivityToBeCanceled(ctx context.Context) (string, error) {
// ...
	// A for select statement is a common approach to listening for a Cancellation in an Activity
	for {
		select {
		case <-time.After(1 * time.Second):
			logger.Info("Heartbeating...")
			activity.RecordHeartbeat(ctx, "")
		// Listen for ctx.Done() to know if a Cancellation Request has propagated to the Activity.
		case <-ctx.Done():
			logger.Info("This Activity is canceled!")
			return "I am canceled by Done", nil
		}
	}
}
// ...
```

## Request Cancellation {/* #request-cancellation */}

**How to request Cancellation of a Workflow and Activities in Go.**

Use the `CancelWorkflow` API to cancel a Workflow Execution using its Id.

    View the source code
  {' '}
  in the context of the rest of the application code.

```go
func main() {
// ...
	// Call the CancelWorkflow API to cancel a Workflow
	// In this call we are relying on the Workflow Id only.
	// But a Run Id can also be supplied to ensure the correct Workflow is Canceled.
	err = temporalClient.CancelWorkflow(context.Background(), cancellation.WorkflowId, "")
	if err != nil {
		log.Fatalln("Unable to cancel Workflow Execution", err)
	}
// ...
}
```

## Heartbeating after a Cancellation

Sometimes you may want to continue running your Activity, even after a Cancellation has been issued. You may want to
completely ignore the cancellation and continue Activity execution, including Heartbeating, or you may want to send one
final Heartbeat after Cancellation. Even though the context is cancelled when the Workflow is Cancelled, you are still
able to send Activity Heartbeats.

When you call `activity.RecordHeartbeat` after Cancellation has occurred, a
`WARN RecordActivityHeartbeat with error Error context canceled` message will be logged, and a `context canceled` error
will be returned from the call. However, the Heartbeat **has** still been sent.

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

## Child Workflows - Go SDK

This page shows how to do the following:

- [Start a Child Workflow Execution](#child-workflows)
- [Set a Parent Close Policy](#parent-close-policy)

## Start a Child Workflow Execution {/* #child-workflows */}

A [Child Workflow Execution](/child-workflows) is a Workflow Execution that is scheduled from within another Workflow using a Child Workflow API.

When using a Child Workflow API, Child Workflow related Events ([StartChildWorkflowExecutionInitiated](/references/events#startchildworkflowexecutioninitiated), [ChildWorkflowExecutionStarted](/references/events#childworkflowexecutionstarted), [ChildWorkflowExecutionCompleted](/references/events#childworkflowexecutioncompleted), etc...) are logged in the Workflow Execution Event History.

The [ChildWorkflowExecutionStarted](/references/events#childworkflowexecutionstarted) Event must be logged to the Event History before the Parent Workflow completes to ensure the Child Workflow has started.
In Go, you must explicitly call `GetChildWorkflowExecution()` on the `ChildWorkflowFuture` and then call `Get()` on the returned Future to wait for this Event.
See the [Async Child Workflows](#async-child-workflows) section below for a complete example.

To spawn a [Child Workflow Execution](/child-workflows) in Go, use the [`ExecuteChildWorkflow`](https://pkg.go.dev/go.temporal.io/sdk/workflow#ExecuteChildWorkflow) API, which is available from the `go.temporal.io/sdk/workflow` package.
