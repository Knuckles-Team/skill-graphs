- [Count Standalone Activities](#count-activities)
- [Run Standalone Activities with Temporal Cloud](#run-standalone-activities-temporal-cloud)

:::note

This documentation uses source code from the
[standalone-activity/helloworld](https://github.com/temporalio/samples-go/tree/main/standalone-activity/helloworld).

:::

## Get Started with Standalone Activities {/* #get-started */}

Prerequisites:

- **[Go](https://go.dev/dl/)** 1.22+

- **[Temporal Go SDK](https://docs.temporal.io/develop/go/core-application#install-a-temporal-sdk)** (v1.41.0 or higher)

- **Temporal CLI** v1.7.0 or higher

  Install with Homebrew:

  ```bash
  brew install temporal
  ```

  Or see the [Temporal CLI install guide](/cli/setup-cli) for other platforms.

  Verify the installation:

  ```bash
  temporal --version
  ```

Start the Temporal development server:

```
temporal server start-dev
```

This command automatically starts the Temporal development server with the Web UI, and creates the `default` Namespace.
It uses an in-memory database, so do not use it for real use cases.

:::info Temporal Cloud

All code samples on this page use
[`envconfig.MustLoadDefaultClientOptions()`](https://pkg.go.dev/go.temporal.io/sdk/contrib/envconfig)
to configure the Temporal Client connection. It responds to [environment
variables](/references/client-environment-configuration) and [TOML configuration
files](/references/client-environment-configuration), so the same code works against a local dev
server and Temporal Cloud without changes. See [Run Standalone Activities with Temporal
Cloud](#run-standalone-activities-temporal-cloud) below.

:::

The Temporal Server should now be available for client connections on `localhost:7233`, and the
Temporal Web UI should now be accessible at [http://localhost:8233](http://localhost:8233). Standalone
Activities are available from the nav bar item located towards the top left of the page:

Clone the [samples-go](https://github.com/temporalio/samples-go) repository to follow along:

```
git clone https://github.com/temporalio/samples-go.git
cd samples-go
```

The sample project is structured as follows:

```
standalone-activity/helloworld/
├── activity.go
├── worker/
│   └── main.go
└── starter/
    └── main.go
```

## Define your Activity {/* #define-activity */}

Define your Activity in a shared file so that both the Worker and starter can reference it.

[standalone-activity/helloworld/activity.go](https://github.com/temporalio/samples-go/blob/main/standalone-activity/helloworld/activity.go)

```go
package helloworld

	"context"
	"go.temporal.io/sdk/activity"
)

func Activity(ctx context.Context, name string) (string, error) {
	logger := activity.GetLogger(ctx)
	logger.Info("Activity", "name", name)
	return "Hello " + name + "!", nil
}
```

## Run a Worker with the Activity registered {/* #run-worker */}

Running a Worker for Standalone Activities is the same as running a Worker for Workflow-driven Activities — you create a
Worker, register the Activity, and call `Run()`. The Worker doesn't need to know whether the Activity will be invoked
from a Workflow or as a Standalone Activity.

See [How to develop a Worker in Go](/develop/go/workers/run-worker-process#develop-worker) for more details on Worker setup and
configuration options.

[standalone-activity/helloworld/worker/main.go](https://github.com/temporalio/samples-go/blob/main/standalone-activity/helloworld/worker/main.go)

```go
package main

	"github.com/temporalio/samples-go/standalone-activity/helloworld"
	"go.temporal.io/sdk/client"
	"go.temporal.io/sdk/contrib/envconfig"
	"go.temporal.io/sdk/worker"
	"log"
)

func main() {
	c, err := client.Dial(envconfig.MustLoadDefaultClientOptions())
	if err != nil {
		log.Fatalln("Unable to create client", err)
	}
	defer c.Close()

	w := worker.New(c, "standalone-activity-helloworld", worker.Options{})

	w.RegisterActivity(helloworld.Activity)

	err = w.Run(worker.InterruptCh())
	if err != nil {
		log.Fatalln("Unable to start worker", err)
	}
}
```

Open a new terminal, navigate to the `samples-go` directory, and run the Worker:

```
go run standalone-activity/helloworld/worker/main.go
```

Leave this terminal running - the Worker needs to stay up to process activities.

## Execute a Standalone Activity {/* #execute-activity */}

Use [`client.ExecuteActivity()`](https://pkg.go.dev/go.temporal.io/sdk/client#Client) to start a Standalone Activity
Execution. This is called from application code (for example, a starter program), not from inside a Workflow Definition.

`ExecuteActivity` returns an [`ActivityHandle`](https://pkg.go.dev/go.temporal.io/sdk/client#ActivityHandle) that you
can use to get the result, describe, cancel, or terminate the Activity.

The following starter program demonstrates how to execute a Standalone Activity, get its result, list activities, and
count activities:

[standalone-activity/helloworld/starter/main.go](https://github.com/temporalio/samples-go/blob/main/standalone-activity/helloworld/starter/main.go)

```go
package main

	"context"
	"github.com/temporalio/samples-go/standalone-activity/helloworld"
	"go.temporal.io/sdk/client"
	"go.temporal.io/sdk/contrib/envconfig"
	"log"
	"time"
)

func main() {
	c, err := client.Dial(envconfig.MustLoadDefaultClientOptions())
	if err != nil {
		log.Fatalln("Unable to create client", err)
	}
	defer c.Close()

	activityOptions := client.StartActivityOptions{
		ID:        "standalone_activity_helloworld_ActivityID",
		TaskQueue: "standalone-activity-helloworld",
		ScheduleToCloseTimeout: 10 * time.Second,
	}

	handle, err := c.ExecuteActivity(context.Background(), activityOptions, helloworld.Activity, "Temporal")
	if err != nil {
		log.Fatalln("Unable to execute activity", err)
	}

	log.Println("Started standalone activity", "ActivityID", handle.GetID(), "RunID", handle.GetRunID())

	var result string
	err = handle.Get(context.Background(), &result)
	if err != nil {
		log.Fatalln("Unable get standalone activity result", err)
	}
	log.Println("Activity result:", result)

	resp, err := c.ListActivities(context.Background(), client.ListActivitiesOptions{
		Query: "TaskQueue = 'standalone-activity-helloworld'",
	})
	if err != nil {
		log.Fatalln("Unable to list activities", err)
	}

	log.Println("ListActivity results")
	for info, err := range resp.Results {
		if err != nil {
			log.Fatalln("Error iterating activities", err)
		}
		log.Printf("\tActivityID: %s, Type: %s, Status: %v\n",
			info.ActivityID, info.ActivityType, info.Status)
	}

	resp1, err := c.CountActivities(context.Background(), client.CountActivitiesOptions{
		Query: "TaskQueue = 'standalone-activity-helloworld'",
	})
	if err != nil {
		log.Fatalln("Unable to count activities", err)
	}

	log.Println("Total activities:", resp1.Count)
}
```

You can pass the Activity as either a function reference or a string Activity type name:

```go
handle, err := c.ExecuteActivity(ctx, options, helloworld.Activity, "arg1")

// Using a string type name
handle, err := c.ExecuteActivity(ctx, options, "Activity", "arg1")
```

`client.StartActivityOptions` requires `ID`, `TaskQueue`, and at least one of `ScheduleToCloseTimeout` or
`StartToCloseTimeout`. See [`StartActivityOptions`](https://pkg.go.dev/go.temporal.io/sdk/client#StartActivityOptions)
in the API reference for the full set of options.

To run the starter:

1. Make sure the Temporal Server is running (from the [Get Started](#get-started) step above).
2. Make sure the Worker is running (from the [Run a Worker](#run-worker) step above).
3. Open a new terminal, navigate to the `samples-go` directory, and run:

```
go run standalone-activity/helloworld/starter/main.go
```

Or use the Temporal CLI to execute a Standalone Activity:

```bash
temporal activity execute \
  --type Activity \
  --activity-id standalone_activity_helloworld_ActivityID \
  --task-queue standalone-activity-helloworld \
  --schedule-to-close-timeout 10s \
  --input '"Temporal"'
```

## Get the result of a Standalone Activity {/* #get-activity-result */}

Use `ActivityHandle.Get()` to block until the Activity completes and retrieve its result. This is analogous to calling
`Get()` on a `WorkflowRun`.

```go
var result string
err = handle.Get(context.Background(), &result)
if err != nil {
	log.Fatalln("Activity failed", err)
}
log.Println("Activity result:", result)
```

If the Activity completed successfully, the result is deserialized into the provided pointer. If the Activity failed,
the failure is returned as an error.

Or use the Temporal CLI to wait for a result by Activity ID:

```bash
temporal activity result --activity-id standalone_activity_helloworld_ActivityID
```

## Get a handle to an existing Standalone Activity {/* #get-activity-handle */}

Use `client.GetActivityHandle()` to create a handle to a previously started Standalone Activity. This is analogous to
`client.GetWorkflow()` for Workflow Executions.

Both `ActivityID` and `RunID` are required.

```go
handle := c.GetActivityHandle(client.GetActivityHandleOptions{
	ActivityID: "standalone_activity_helloworld_ActivityID",
	RunID:      "the-run-id",
})

// Use the handle to get the result, describe, cancel, or terminate
var result string
err := handle.Get(context.Background(), &result)
if err != nil {
	log.Fatalln("Unable to get activity result", err)
}
```

## List Standalone Activities {/* #list-activities */}

Use [`client.ListActivities()`](https://pkg.go.dev/go.temporal.io/sdk/client#Client) to list Standalone Activity
Executions that match a [List Filter](/list-filter) query. The result contains an iterator that yields
[`ActivityExecutionInfo`](https://pkg.go.dev/go.temporal.io/sdk/client#ActivityExecutionInfo) entries.

These APIs return only Standalone Activity Executions. Activities running inside Workflows are not included.

```go
resp, err := c.ListActivities(context.Background(), client.ListActivitiesOptions{
	Query: "TaskQueue = 'standalone-activity-helloworld'",
})
if err != nil {
	log.Fatalln("Unable to list activities", err)
}

for info, err := range resp.Results {
	if err != nil {
		log.Fatalln("Error iterating activities", err)
	}
	log.Printf("ActivityID: %s, Type: %s, Status: %v\n",
		info.ActivityID, info.ActivityType, info.Status)
}
```

Or use the Temporal CLI:

```bash
temporal activity list
```

The `Query` field accepts the same [List Filter](/list-filter) syntax used for Workflow Visibility. For example,
`"ActivityType = 'Activity' AND Status = 'Running'"`.

## Count Standalone Activities {/* #count-activities */}

Use [`client.CountActivities()`](https://pkg.go.dev/go.temporal.io/sdk/client#Client) to count Standalone Activity
Executions that match a [List Filter](/list-filter) query. This returns the total count of executions (running,
completed, failed, etc.) - not the number of queued tasks. It works the same way as counting Workflow Executions.

```go
resp, err := c.CountActivities(context.Background(), client.CountActivitiesOptions{
	Query: "TaskQueue = 'standalone-activity-helloworld'",
})
if err != nil {
	log.Fatalln("Unable to count activities", err)
}

log.Println("Total activities:", resp.Count)
```

Or use the Temporal CLI:

```bash
temporal activity count
```

## Run Standalone Activities with Temporal Cloud {/* #run-standalone-activities-temporal-cloud */}

The code samples on this page use `envconfig.MustLoadDefaultClientOptions()`, so the same code
works against Temporal Cloud - just configure the connection via environment variables or a TOML
profile. No code changes are needed.

For a step-by-step guide on connecting to Temporal Cloud, including Namespace creation, certificate
generation, and authentication setup in the Cloud UI, see
[Connect to Temporal Cloud](/develop/go/client/temporal-client#connect-to-temporal-cloud).

### Connect with mTLS

Set these environment variables with values from your Temporal Cloud Namespace settings:

```
export TEMPORAL_ADDRESS=<your-namespace>.<your-account-id>.tmprl.cloud:7233
export TEMPORAL_NAMESPACE=<your-namespace>.<your-account-id>
export TEMPORAL_TLS_CLIENT_CERT_PATH='path/to/your/client.pem'
export TEMPORAL_TLS_CLIENT_KEY_PATH='path/to/your/client.key'
```

### Connect with an API key

Set these environment variables with values from your Temporal Cloud API key settings:

```
export TEMPORAL_ADDRESS=<region>.<cloud_provider>.api.temporal.io:7233
export TEMPORAL_NAMESPACE=<your-namespace>.<your-account-id>
export TEMPORAL_API_KEY=<your-api-key>
```

Then run the Worker and starter code as shown in the earlier sections.

---

## Activity Timeouts - Go SDK

## How to set Activity timeouts {/* #activity-timeouts */}

Each Activity timeout controls the maximum duration of a different aspect of an Activity Execution.

The following timeouts are available in the Activity Options.

- **[Schedule-To-Close Timeout](/encyclopedia/detecting-activity-failures#schedule-to-close-timeout):** is the maximum amount of time allowed for the overall [Activity Execution](/activity-execution).
- **[Start-To-Close Timeout](/encyclopedia/detecting-activity-failures#start-to-close-timeout):** is the maximum time allowed for a single [Activity Task Execution](/tasks#activity-task-execution).
- **[Schedule-To-Start Timeout](/encyclopedia/detecting-activity-failures#schedule-to-start-timeout):** is the maximum amount of time that is allowed from when an [Activity Task](/tasks#activity-task) is scheduled to when a [Worker](/workers#worker) starts that Activity Task.

An Activity Execution must have either the Start-To-Close or the Schedule-To-Close Timeout set.

To set an Activity Timeout in Go, create an instance of `ActivityOptions` from the `go.temporal.io/sdk/workflow` package, set the Activity Timeout field, and then use the `WithActivityOptions()` API to apply the options to the instance of `workflow.Context`.

Available timeouts are:

- `StartToCloseTimeout`
- `ScheduleToClose`
- `ScheduleToStartTimeout`

```go
activityoptions := workflow.ActivityOptions{
  // Set Activity Timeout duration
  ScheduleToCloseTimeout: 10 * time.Second,
  // StartToCloseTimeout: 10 * time.Second,
  // ScheduleToStartTimeout: 10 * time.Second,
}
ctx = workflow.WithActivityOptions(ctx, activityoptions)
var yourActivityResult YourActivityResult
err = workflow.ExecuteActivity(ctx, YourActivityDefinition, yourActivityParam).Get(ctx, &yourActivityResult)
if err != nil {
  // ...
}
```

### Set a custom Activity Retry Policy {/* #activity-retries */}

A Retry Policy works in cooperation with the timeouts to provide fine controls to optimize the execution experience.

Activity Executions are automatically associated with a default [Retry Policy](/encyclopedia/retry-policies) if a custom one is not provided.

To set a [RetryPolicy](/encyclopedia/retry-policies), create an instance of `ActivityOptions` from the `go.temporal.io/sdk/workflow` package, set the `RetryPolicy` field, and then use the `WithActivityOptions()` API to apply the options to the instance of `workflow.Context`.

- Type: [`RetryPolicy`](https://pkg.go.dev/go.temporal.io/sdk/temporal#RetryPolicy)
- Default:

```go
retrypolicy := &temporal.RetryPolicy{
  InitialInterval:    time.Second,
  BackoffCoefficient: 2.0,
  MaximumInterval:    time.Second * 100, // 100 * InitialInterval
  MaximumAttempts: 0, // Unlimited
  NonRetryableErrorTypes: []string, // empty
}
```

Providing a Retry Policy here is a customization, and overwrites individual Field defaults.

```go
retrypolicy := &temporal.RetryPolicy{
  InitialInterval:    time.Second,
  BackoffCoefficient: 2.0,
  MaximumInterval:    time.Second * 100,
}

activityoptions := workflow.ActivityOptions{
  RetryPolicy: retrypolicy,
}
ctx = workflow.WithActivityOptions(ctx, activityoptions)
var yourActivityResult YourActivityResult
err = workflow.ExecuteActivity(ctx, YourActivityDefinition, yourActivityParam).Get(ctx, &yourActivityResult)
if err != nil {
  // ...
}
```

### Overriding the retry interval with Next Retry Delay {/* #next-retry-delay */}

You may return an [Application Failure](/references/failures#application-failure) with the `NextRetryDelay` field set.
This value will replace and override whatever the Retry interval would be on the Retry Policy.

For example, if in an Activity, you want to base the interval on the number of attempts:

```go
attempt := activity.GetInfo(ctx).Attempt;

return temporal.NewApplicationErrorWithOptions(fmt.Sprintf("Something bad happened on attempt %d", attempt), "NextDelay", temporal.ApplicationErrorOptions{
  NextRetryDelay: 3 * time.Second * delay,
})
```

## Activity Heartbeats {/* #activity-heartbeats */}

An [Activity Heartbeat](/encyclopedia/detecting-activity-failures#activity-heartbeat) is a ping from the [Worker Process](/workers#worker-process) that is executing the Activity to the [Temporal Service](/temporal-service).
Each Heartbeat informs the Temporal Service that the [Activity Execution](/activity-execution) is making progress and the Worker has not crashed.
If the Temporal Service does not receive a Heartbeat within a [Heartbeat Timeout](/encyclopedia/detecting-activity-failures#heartbeat-timeout) time period, the Activity will be considered failed and another [Activity Task Execution](/tasks#activity-task-execution) may be scheduled according to the Retry Policy.

Heartbeats may not always be sent to the Temporal Service—they may be [throttled](/encyclopedia/detecting-activity-failures#throttling) by the Worker.

Activity Cancellations are delivered to Activities from the Temporal Service when they Heartbeat. Activities that don't Heartbeat can't receive a Cancellation.
Heartbeat throttling may lead to Cancellation getting delivered later than expected.

Heartbeats can contain a `details` field describing the Activity's current progress.
If an Activity gets retried, the Activity can access the `details` from the last Heartbeat that was sent to the Temporal Service.

To [Heartbeat](/encyclopedia/detecting-activity-failures#activity-heartbeat) in an Activity in Go, use the `RecordHeartbeat` API.

```go

    // ...
    "go.temporal.io/sdk/workflow"
    // ...
)

func YourActivityDefinition(ctx, YourActivityDefinitionParam) (YourActivityDefinitionResult, error) {
    // ...
    activity.RecordHeartbeat(ctx, details)
    // ...
}
```

When an Activity Task Execution times out due to a missed Heartbeat, the last value of the `details` variable above is returned to the calling Workflow in the `details` field of `TimeoutError` with `TimeoutType` set to `Heartbeat`.

You can also Heartbeat an Activity from an external source:

```go
// The client is a heavyweight object that should be created once per process.
temporalClient, err := client.Dial(client.Options{})
// Record heartbeat.
err := temporalClient.RecordActivityHeartbeat(ctx, taskToken, details)
```

The parameters of the `RecordActivityHeartbeat` function are:

- `taskToken`: The value of the binary `TaskToken` field of the `ActivityInfo` struct retrieved inside
  the Activity.
- `details`: The serializable payload containing progress information.

If an Activity Execution Heartbeats its progress before it failed, the retry attempt will have access to the progress information, so that the Activity Execution can resume from the failed state.
Here's an example of how this can be implemented:

```go
func SampleActivity(ctx context.Context, inputArg InputParams) error {
    startIdx := inputArg.StartIndex
    if activity.HasHeartbeatDetails(ctx) {
        // Recover from finished progress.
        var finishedIndex int
        if err := activity.GetHeartbeatDetails(ctx, &finishedIndex); err == nil {
            startIdx = finishedIndex + 1 // Start from next one.
        }
    }

    // Normal Activity logic...
    for i:=startIdx; i<inputArg.EndIdx; i++ {
        // Code for processing item i goes here...
        activity.RecordHeartbeat(ctx, i) // Report progress.
    }
}
```

### Set a Heartbeat Timeout {/* #heartbeat-timeout */}

A [Heartbeat Timeout](/encyclopedia/detecting-activity-failures#heartbeat-timeout) works in conjunction with [Activity Heartbeats](/encyclopedia/detecting-activity-failures#activity-heartbeat).

To set a [Heartbeat Timeout](/encyclopedia/detecting-activity-failures#heartbeat-timeout), Create an instance of `ActivityOptions` from the `go.temporal.io/sdk/workflow` package, set the `HeartbeatTimeout` field, and then use the `WithActivityOptions()` API to apply the options to the instance of `workflow.Context`.

```go
activityoptions := workflow.ActivityOptions{
  HeartbeatTimeout: 10 * time.Second,
}
ctx = workflow.WithActivityOptions(ctx, activityoptions)
var yourActivityResult YourActivityResult
err = workflow.ExecuteActivity(ctx, YourActivityDefinition, yourActivityParam).Get(ctx, &yourActivityResult)
if err != nil {
  // ...
}
```

---

## Context Propagation - Go SDK

Context propagation lets you pass custom key-value data from a Client to Workflows, and from Workflows to Activities and Child Workflows, without threading it through every function signature. Common use cases include propagating tracing IDs, tenant IDs, auth tokens, or other request-scoped metadata.

{/* TODO: Link to /encyclopedia/context-propagation once that page lands */}

:::tip

If you want to propagate tracing context, check if there is a [built-in tracing interceptor](/develop/go/platform/observability#tracing) for your library before building a custom context propagator.

:::

## How it works

1. **Register** a context propagator on the Client via `ContextPropagators` in [ClientOptions](https://pkg.go.dev/go.temporal.io/sdk/internal#ClientOptions)
2. **Inject** - On outbound calls, the SDK calls `Inject` (from `context.Context`) or `InjectFromWorkflow` (from `workflow.Context`) to serialize values into Temporal headers
3. **Extract** - On inbound calls, the SDK calls `Extract` (into `context.Context`) or `ExtractToWorkflow` (into `workflow.Context`) to deserialize headers back into the context
4. **Access** - Your Workflow and Activity code reads values from the context as usual

## Implement a context propagator

A context propagator implements the [`ContextPropagator`](https://pkg.go.dev/go.temporal.io/sdk/workflow#ContextPropagator) interface:

```go
type ContextPropagator interface {
    // Inject writes values from a Go context.Context into headers (Client/Activity side)
    Inject(context.Context, HeaderWriter) error
    // Extract reads headers into a Go context.Context (Client/Activity side)
    Extract(context.Context, HeaderReader) (context.Context, error)
    // InjectFromWorkflow writes values from a workflow.Context into headers
    InjectFromWorkflow(Context, HeaderWriter) error
    // ExtractToWorkflow reads headers into a workflow.Context
    ExtractToWorkflow(Context, HeaderReader) (Context, error)
}
```

There are two pairs of methods because Go uses `context.Context` in non-Workflow code (Client, Activities) and `workflow.Context` inside Workflows. You must implement all four methods for values to propagate across every boundary (Client → Workflow → Activity/Child Workflow).

Here is a propagator that carries a custom key-value pair from the Client to Workflows and Activities (from the [context propagation sample](https://github.com/temporalio/samples-go/tree/main/ctxpropagation)):

<!--SNIPSTART samples-go-ctx-propagation-propagator-->
[ctxpropagation/propagator.go](https://github.com/temporalio/samples-go/blob/main/ctxpropagation/propagator.go)
```go
type (
	// contextKey is an unexported type used as key for items stored in the
	// Context object
	contextKey struct{}

	// propagator implements the custom context propagator
	propagator struct{}

	// Values is a struct holding values
	Values struct {
		Key   string `json:"key"`
		Value string `json:"value"`
	}
)

// PropagateKey is the key used to store the value in the Context object
var PropagateKey = contextKey{}

// HeaderKey is the key used by the propagator to pass values through the
// Temporal server headers
const HeaderKey = "custom-header"

// NewContextPropagator returns a context propagator that propagates a set of
// string key-value pairs across a workflow
func NewContextPropagator() workflow.ContextPropagator {
	return &propagator{}
}

// Inject injects values from context into headers for propagation
func (s *propagator) Inject(ctx context.Context, writer workflow.HeaderWriter) error {
	value := ctx.Value(PropagateKey)
	payload, err := converter.GetDefaultDataConverter().ToPayload(value)
	if err != nil {
		return err
	}
	writer.Set(HeaderKey, payload)
	return nil
}

// InjectFromWorkflow injects values from context into headers for propagation
func (s *propagator) InjectFromWorkflow(ctx workflow.Context, writer workflow.HeaderWriter) error {
	value := ctx.Value(PropagateKey)
	payload, err := converter.GetDefaultDataConverter().ToPayload(value)
	if err != nil {
		return err
	}
	writer.Set(HeaderKey, payload)
	return nil
}

// Extract extracts values from headers and puts them into context
func (s *propagator) Extract(ctx context.Context, reader workflow.HeaderReader) (context.Context, error) {
	if value, ok := reader.Get(HeaderKey); ok {
		var values Values
		if err := converter.GetDefaultDataConverter().FromPayload(value, &values); err != nil {
			return ctx, nil
		}
		ctx = context.WithValue(ctx, PropagateKey, values)
	}

	return ctx, nil
}
```
<!--SNIPEND-->

## Register the propagator and set context values

Register the propagator on the Client. Then set context values before starting a Workflow:

<!--SNIPSTART samples-go-ctx-propagation-starter-->
