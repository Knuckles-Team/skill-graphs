driver at the MRAP ARN instead of a bucket name. See
[Durable External Storage](/external-storage#durable-external-storage) for the full pattern and trade-offs.

In code, the only change is the value you pass to `s3driver.StaticBucket`:

```go
driver, err := s3driver.NewDriver(s3driver.Options{
	Client: awssdkv2.NewClient(s3.NewFromConfig(cfg)),
	Bucket: s3driver.StaticBucket("arn:aws:s3::123456789012:accesspoint/mfzwi23gnjvgw.mrap"),
})
```

The AWS SDK for Go v2 automatically uses [SigV4A](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv-create-signed-request.html)
signing when the bucket value is an MRAP ARN, so no additional client configuration is required.

---

## Data handling - Go SDK

All data sent to and from the Temporal Service passes through the **Data Converter**. The Data Converter has three
layers that handle different concerns:

<CaptionedImage
  src="/diagrams/data-converter-flow-with-external-storage.svg"
  srcDark="/diagrams/data-converter-flow-dark.svg"
  title="The Flow of Data through a Data Converter"
  alt="The Flow of Data through a Data Converter"
/>

Of these three layers, only the PayloadConverter is required. Temporal uses a default PayloadConverter that handles JSON
serialization. The PayloadCodec and ExternalStorage layers are optional. You only need to customize these layers when
your application requires non-JSON types, encryption, or payload offloading.

|                           | [PayloadConverter](/develop/go/data-handling/data-conversion) | [PayloadCodec](/develop/go/data-handling/data-encryption) | [ExternalStorage](/develop/go/data-handling/external-storage) |
| ------------------------- | ------------------------------------------------------------- | --------------------------------------------------------- | ------------------------------------------------------------------ |
| **Purpose**               | Serialize application data to bytes                           | Transform encoded payloads (encrypt, compress)            | Offload large payloads to external store                           |
| **Default**               | JSON serialization                                            | None (passthrough)                                        | None (all payloads are stored in Event History)                  |

For a deeper conceptual explanation, see the [Data Conversion encyclopedia](/dataconversion) and [External Storage](/external-storage).

---

## Debugging - Go SDK

You can use a debugger tool provided by your favorite IDE to debug your Workflow Definitions prior to testing or executing them.

The Temporal Go SDK includes deadlock detection which fails a Workflow Task in case the code blocks over a second without relinquishing execution control.
Because of this you can often encounter a `PanicError: Potential deadlock detected` while stepping through Workflow Definitions during debugging.

To alleviate this issue, you can set the `TEMPORAL_DEBUG` environment variable to `true` before debugging your Workflow Definition.

:::note

Make sure to set `TEMPORAL_DEBUG` to true only during debugging.

:::

## How to debug in a development environment {/* #debug-in-a-development-environment */}

In addition to the normal development tools of logging and a debugger, you can also see what's happening in your Workflow by using the [Web UI](/web-ui) or [Temporal CLI](/cli).

## How to debug in a production environment {/* #debug-in-a-production-environment */}

You can debug production Workflows using:

- [Web UI](/web-ui)
- [Temporal CLI](/cli)
- [Replay](/develop/go/best-practices/testing-suite#replay)
- [Tracing](/develop/go/platform/observability#tracing)
- [Logging](/develop/go/platform/observability#logging)

You can debug and tune Worker performance with metrics and the [Worker performance guide](/develop/worker-performance).
For more information, see [Metrics](/develop/go/platform/observability#metrics) for setting up SDK metrics.

Debug Server performance with [Cloud metrics](/cloud/metrics/) or [self-hosted Server metrics](/self-hosted-guide/production-checklist#scaling-and-metrics).

## How to test Workflow Definitions in Go {/* #testing-and-debugging */}

The Temporal Go SDK provides a test framework to facilitate testing Workflow implementations.

This framework is suited for implementing unit tests as well as functional tests of the Workflow logic.

The following code implements unit tests for the `SimpleWorkflow` sample:

```go
package sample

        "context"
        "errors"
        "testing"

        "github.com/stretchr/testify/mock"
        "github.com/stretchr/testify/suite"

        "go.temporal.io/sdk/activity"
        "go.temporal.io/sdk/testsuite"
)

type UnitTestSuite struct {
        suite.Suite
        testsuite.WorkflowTestSuite

        env *testsuite.TestWorkflowEnvironment
}

func (s *UnitTestSuite) SetupTest() {
        s.env = s.NewTestWorkflowEnvironment()
}

func (s *UnitTestSuite) AfterTest(suiteName, testName string) {
        s.env.AssertExpectations(s.T())
}

func (s *UnitTestSuite) Test_SimpleWorkflow_Success() {
        s.env.ExecuteWorkflow(SimpleWorkflow, "test_success")

        s.True(s.env.IsWorkflowCompleted())
        s.NoError(s.env.GetWorkflowError())
}

func (s *UnitTestSuite) Test_SimpleWorkflow_ActivityParamCorrect() {
        s.env.OnActivity(SimpleActivity, mock.Anything, mock.Anything).Return(
          func(ctx context.Context, value string) (string, error) {
                s.Equal("test_success", value)
                return value, nil
        })
        s.env.ExecuteWorkflow(SimpleWorkflow, "test_success")

        s.True(s.env.IsWorkflowCompleted())
        s.NoError(s.env.GetWorkflowError())
}

func (s *UnitTestSuite) Test_SimpleWorkflow_ActivityFails() {
        s.env.OnActivity(SimpleActivity, mock.Anything, mock.Anything).Return(
          "", errors.New("SimpleActivityFailure"))
        s.env.ExecuteWorkflow(SimpleWorkflow, "test_failure")

        s.True(s.env.IsWorkflowCompleted())

        err := s.env.GetWorkflowError()
        s.Error(err)
        var applicationErr *temporal.ApplicationError
        s.True(errors.As(err, &applicationErr))
        s.Equal("SimpleActivityFailure", applicationErr.Error())
}

func TestUnitTestSuite(t *testing.T) {
        suite.Run(t, new(UnitTestSuite))
}
```

#### Setup

To run unit tests, we first define a test suite struct that absorbs both the
basic suite functionality from [testify](https://pkg.go.dev/github.com/stretchr/testify/suite)
via `suite.Suite` and the suite functionality from the Temporal test framework via
`testsuite.WorkflowTestSuite`. Because every test in this test suite will test our Workflow, we
add a property to our struct to hold an instance of the test environment. This allows us to initialize
the test environment in a setup method. For testing Workflows, we use a `testsuite.TestWorkflowEnvironment`.

Next, we implement a `SetupTest` method to set up a new test environment before each test. Doing so
ensures that each test runs in its own isolated sandbox. We also implement an `AfterTest` function
where we assert that all the mocks we set up were indeed called by invoking `s.env.AssertExpectations(s.T())`.

Timeout for the entire test can be set using `SetTestTimeout` in the Workflow or Activity environment.

Finally, we create a regular test function recognized by the `go test` command, and pass the struct to `suite.Run`.

#### A Simple Test

The simplest test case we can write is to have the test environment execute the Workflow and then
evaluate the results.

```go
func (s *UnitTestSuite) Test_SimpleWorkflow_Success() {
        s.env.ExecuteWorkflow(SimpleWorkflow, "test_success")

        s.True(s.env.IsWorkflowCompleted())
        s.NoError(s.env.GetWorkflowError())
}
```

Calling `s.env.ExecuteWorkflow(...)` executes the Workflow logic and any invoked Activities inside the
test process. The first parameter of `s.env.ExecuteWorkflow(...)` contains the Workflow functions,
and any subsequent parameters contain values for custom input parameters declared by the Workflow
function.

> Note that unless the Activity invocations are mocked or Activity implementation
> replaced (see [Activity mocking and overriding](#activity-mocking-and-overriding)), the test environment
> will execute the actual Activity code including any calls to outside services.

After executing the Workflow in the above example, we assert that the Workflow ran through completion
via the call to `s.env.IsWorkflowComplete()`. We also assert that no errors were returned by asserting
on the return value of `s.env.GetWorkflowError()`. If our Workflow returned a value, we could have
retrieved that value via a call to `s.env.GetWorkflowResult(&value)` and had additional asserts on that
value.

#### Activity mocking and overriding

When running unit tests on Workflows, we want to test the Workflow logic in isolation. Additionally,
we want to inject Activity errors during our test runs. The test framework provides two mechanisms
that support these scenarios: Activity mocking and Activity overriding. Both of these mechanisms allow
you to change the behavior of Activities invoked by your Workflow without the need to modify the actual
Workflow code.

Let's take a look at a test that simulates a test that fails via the "Activity mocking" mechanism.

```go
func (s *UnitTestSuite) Test_SimpleWorkflow_ActivityFails() {
        s.env.OnActivity(SimpleActivity, mock.Anything, mock.Anything).Return(
          "", errors.New("SimpleActivityFailure"))
        s.env.ExecuteWorkflow(SimpleWorkflow, "test_failure")

        s.True(s.env.IsWorkflowCompleted())

        err := s.env.GetWorkflowError()
        s.Error(err)
        var applicationErr *temporal.ApplicationError
        s.True(errors.As(err, &applicationErr))
        s.Equal("SimpleActivityFailure", applicationErr.Error())
}
```

This test simulates the execution of the Activity `SimpleActivity` that is invoked by our Workflow
`SimpleWorkflow` returning an error. We accomplish this by setting up a mock on the test environment
for the `SimpleActivity` that returns an error.

```go
s.env.OnActivity(SimpleActivity, mock.Anything, mock.Anything).Return(
  "", errors.New("SimpleActivityFailure"))
```

With the mock set up we can now execute the Workflow via the `s.env.ExecuteWorkflow(...)` method and
assert that the Workflow completed successfully and returned the expected error.

Simply mocking the execution to return a desired value or error is a pretty powerful mechanism to
isolate Workflow logic. However, sometimes we want to replace the Activity with an alternate implementation
to support a more complex test scenario. Let's assume we want to validate that the Activity gets called
with the correct parameters.

```go
func (s *UnitTestSuite) Test_SimpleWorkflow_ActivityParamCorrect() {
        s.env.OnActivity(SimpleActivity, mock.Anything, mock.Anything).Return(
          func(ctx context.Context, value string) (string, error) {
                s.Equal("test_success", value)
                return value, nil
        })
        s.env.ExecuteWorkflow(SimpleWorkflow, "test_success")

        s.True(s.env.IsWorkflowCompleted())
        s.NoError(s.env.GetWorkflowError())
}
```

In this example, we provide a function implementation as the parameter to `Return`. This allows us to
provide an alternate implementation for the Activity `SimpleActivity`. The framework will execute this
function whenever the Activity is invoked and pass on the return value from the function as the result
of the Activity invocation. Additionally, the framework will validate that the signature of the "mock"
function matches the signature of the original Activity function.

Since this can be an entire function, there is no limitation as to what we can do here. In this
example, we assert that the `value` param has the same content as the value param we passed to the Workflow.

#### Queries

`TestWorkflowEnvironment` instances have a [`QueryWorkflow()` method](https://pkg.go.dev/go.temporal.io/temporal/internal#TestWorkflowEnvironment.QueryWorkflow) that lets you query the state of the currently running Workflow.
For example, suppose you have a Workflow that lets you query the progress of a long running task as shown below.

```go
func ProgressWorkflow(ctx workflow.Context, percent int) error {
	logger := workflow.GetLogger(ctx)

	err := workflow.SetQueryHandler(ctx, "getProgress", func(input []byte) (int, error) {
		return percent, nil
	})
	if err != nil {
		logger.Info("SetQueryHandler failed.", "Error", err)
		return err
	}

	for percent = 0; percent<100; percent++ {
                // Important! Use `workflow.Sleep()`, not `time.Sleep()`, because Temporal's
                // test environment doesn't stub out `time.Sleep()`.
		workflow.Sleep(ctx, time.Second*1)
	}

	return nil
}
```

This Workflow tracks the current progress of a task in percentage terms, and increments the percentage by 1 every second.
Below is how you would write a test case that queries this Workflow.
Note that you should always query the Workflow either after `ExecuteWorkflow()` is done or in a `RegisterDelayedCallback()` callback, otherwise you'll get a `runtime error` panic.

```go
func (s *UnitTestSuite) Test_ProgressWorkflow() {
	value := 0

	// After 10 seconds plus padding, progress should be 10.
	// Note that `RegisterDelayedCallback()` doesn't actually make your test wait for 10 seconds!
	// Temporal's test framework advances time internally, so this test should take < 1 second.
	s.env.RegisterDelayedCallback(func() {
		res, err := s.env.QueryWorkflow("getProgress")
		s.NoError(err)
		err = res.Get(&value)
		s.NoError(err)
		s.Equal(10, value)
	}, time.Second*10+time.Millisecond*1)

	s.env.ExecuteWorkflow(ProgressWorkflow, 0)

	s.True(s.env.IsWorkflowCompleted())

	// Once the workflow is completed, progress should always be 100
	res, err := s.env.QueryWorkflow("getProgress")
	s.NoError(err)
	err = res.Get(&value)
	s.NoError(err)
	s.Equal(value, 100)
}
```

:::note

`RegisterDelayedCallback` can also be used to send [Signals](/sending-messages#sending-signals).
When using "Signal-With-Start", set the delay to `0`.
:::

#### Debugging

You can use a debugger tool provided by your favorite IDE to debug your Workflow Definitions prior to testing or executing them.

The Temporal Go SDK includes deadlock detection which fails a Workflow Task in case the code blocks over a second without relinquishing execution control.
Because of this you can often encounter a `PanicError: Potential deadlock detected` while stepping through Workflow Definitions during debugging.

To alleviate this issue, you can set the `TEMPORAL_DEBUG` environment variable to `true` before debugging your Workflow Definition.

:::note

Make sure to set `TEMPORAL_DEBUG` to true only during debugging.

:::

---

## Error handling - Go SDK

## Error handling {/* #error-handling */}

Within a Workflow, an Activity or Child Workflow execution might fail. You can
handle errors differently based on the error type.

If the Activity returns an error as `errors.New()` or `fmt.Errorf()`, that error is converted into `*temporal.ApplicationError`.

If the Activity returns an error as `temporal.NewNonRetryableApplicationError("error message", details)`, that error is returned as `*temporal.ApplicationError`.

There are other types of errors such as `*temporal.TimeoutError`, `*temporal.CanceledError` and
`*temporal.PanicError`.

Here's an example of handling Activity errors within Workflow code that differentiates between different error types.

```go
err := workflow.ExecuteActivity(ctx, YourActivity, ...).Get(ctx, nil)
if err != nil {
	var applicationErr *ApplicationError
	if errors.As(err, &applicationErr) {
		// retrieve error message
		workflow.GetLogger(ctx).Info("Application error", "error", applicationErr.Error())

		// handle Activity errors (created via NewApplicationError() API)
		var detailMsg string // assuming Activity return error by NewApplicationError("message", true, "string details")
		applicationErr.Details(&detailMsg) // extract strong typed details

		// handle Activity errors (errors created other than using NewApplicationError() API)
		switch applicationErr.Type() {
		case "CustomErrTypeA":
			// handle CustomErrTypeA
		case CustomErrTypeB:
			// handle CustomErrTypeB
		default:
			// newer version of Activity could return new errors that Workflow was not aware of.
		}
	}

	var canceledErr *CanceledError
	if errors.As(err, &canceledErr) {
		// handle cancellation
	}

	var timeoutErr *TimeoutError
	if errors.As(err, &timeoutErr) {
		// handle timeout, could check timeout type by timeoutErr.TimeoutType()
        switch err.TimeoutType() {
        case commonpb.ScheduleToStart:
            // Handle ScheduleToStart timeout.
        case commonpb.StartToClose:
            // Handle StartToClose timeout.
        case commonpb.Heartbeat:
            // Handle heartbeat timeout.
        default:
        }
	}

	var panicErr *PanicError
	if errors.As(err, &panicErr) {
		// handle panic, message and call stack are available by panicErr.Error() and panicErr.StackTrace()
	}
}
```

### Panics and deferred functions

In Go, [`defer` schedules cleanup functions and `recover()` catches panics](https://go.dev/blog/defer-panic-and-recover) to prevent them from crashing the program.
This doesn't work the same way in Temporal Workflow code — you cannot `recover()` from a panic inside a `defer`.
Deferred functions that try to interact with the Temporal SDK during panic unwinding will re-panic immediately.

Use `defer` only for local cleanup.
Handle Temporal API cleanup through explicit error checks instead.

---

## Best Practices - Go SDK

![Go SDK Banner](/img/assets/banner-go-temporal.png)

## Best practices

- [Multithreading](/develop/go/best-practices/multithreading)
- [Error handling](/develop/go/best-practices/error-handling)
- [Debugging](/develop/go/best-practices/debugging)
- [Testing](/develop/go/best-practices/testing-suite)
- [Data handling](/develop/go/data-handling)

---

## Temporal Go SDK multithreading

The Temporal Go SDK allows you to create additional goroutines (threads) in your Workflows by calling `workflow.Go()`.
Native Go threading is never allowed in Workflow code, as it would create determinism errors.

You might sometimes need to execute multiple Activities or Child Workflows in parallel and then await the result of all of them.
Normally, this would require a lock or [mutex](https://en.wikipedia.org/wiki/Lock_(computer_science)) around some shared data structure to avoid race conditions that could occur when multiple asynchronous operations try to modify the data structure.

Although Temporal Workflows run Asynchronously in Go, there is a control in place that ensures only one thread can access at a time.

## How multithreading works

Temporal's Go SDK contains a deterministic runner to control the thread execution.
This deterministic runner will decide which Workflow thread to run in the right order, and one at a time.
Each task will execute in a loop until all threads are blocked.

`workflow.Go()` creates a new thread and adds it to this runner.
This significantly minimizes the likelihood of race conditions, and eliminates the need to use a mutex.

For a complex example, refer to the [Go Particle Swarm Operation Sample](https://github.com/temporalio/samples-go/tree/main/pso).

For an example using Signals, refer to the [Go Await Signal Sample](https://github.com/temporalio/samples-go/tree/main/await-signals)

## Static analysis with the workflowcheck tool

The Temporal Go SDK also provides a command line tool called [`workflowcheck`](https://github.com/temporalio/sdk-go/blob/main/contrib/tools/workflowcheck/README.md) to statically analyze Workflow Definitions. This can help eliminate potential instances of non-determinism.

---

## Testing - Go SDK

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

The Temporal Go SDK provides a test framework to facilitate testing Workflow implementations.

This framework is suited for implementing unit tests as well as functional tests of the Workflow logic.

## Test setup

To run unit tests, we first define a test suite struct that absorbs both the basic suite functionality from [testify](https://pkg.go.dev/github.com/stretchr/testify/suite) via `suite.Suite` and the suite functionality from the Temporal test framework via `testsuite.WorkflowTestSuite`.

Because every test in this test suite will test our Workflow, we
add a property to our struct to hold an instance of the test environment. This allows us to initialize the test environment in a setup method.

For testing Workflows, we use a `testsuite.TestWorkflowEnvironment`.

```go
type UnitTestSuite struct {
        suite.Suite
        testsuite.WorkflowTestSuite

        env *testsuite.TestWorkflowEnvironment
}
```

Next, we implement a `SetupTest` method to set up a new test environment before each test.
Doing so ensures that each test runs in its own isolated sandbox.

```go
func (s *UnitTestSuite) SetupTest() {
        s.env = s.NewTestWorkflowEnvironment()
}
```

We also implement an `AfterTest` function where we assert that all the mocks we set up were indeed called by invoking `s.env.AssertExpectations(s.T())`.
Timeout for the entire test can be set using `SetTestTimeout` in the Workflow or Activity environment.

```go
func (s *UnitTestSuite) AfterTest(suiteName, testName string) {
        s.env.AssertExpectations(s.T())
}
```

Finally, we create a regular test function recognized by the `go test` command, and pass the struct to `suite.Run`.

```go
func TestUnitTestSuite(t *testing.T) {
        suite.Run(t, new(UnitTestSuite))
}
```

## Testing Activities {/* #test-activities */}

An Activity can be tested with a mock Activity environment, which provides a way to mock the Activity context, listen to Heartbeats, and cancel the Activity.
This behavior allows you to test the Activity in isolation by calling it directly, without needing to create a Worker to run the Activity.

## Mock and override Activities

When running unit tests on Workflows, we want to test the Workflow logic in isolation. Additionally, we want to inject Activity errors during our test runs. The test framework provides two mechanisms that support these scenarios: Activity mocking and Activity overriding. Both of these mechanisms allow you to change the behavior of Activities invoked by your Workflow without the need to modify the actual Workflow code.

Let's take a look at a test that simulates a test that fails via the "Activity mocking" mechanism.

```go
func (s *UnitTestSuite) Test_SimpleWorkflow_ActivityFails() {
        s.env.OnActivity(SimpleActivity, mock.Anything, mock.Anything).Return(
          "", errors.New("SimpleActivityFailure"))
        s.env.ExecuteWorkflow(SimpleWorkflow, "test_failure")

        s.True(s.env.IsWorkflowCompleted())

        err := s.env.GetWorkflowError()
        s.Error(err)
        var applicationErr *temporal.ApplicationError
        s.True(errors.As(err, &applicationErr))
        s.Equal("SimpleActivityFailure", applicationErr.Error())
}
```

This test simulates the execution of the Activity `SimpleActivity` that is invoked by our Workflow `SimpleWorkflow` returning an error. We accomplish this by setting up a mock on the test environment for the `SimpleActivity` that returns an error.

```go
s.env.OnActivity(SimpleActivity, mock.Anything, mock.Anything).Return(
  "", errors.New("SimpleActivityFailure"))
```

With the mock set up we can now execute the Workflow via the `s.env.ExecuteWorkflow(...)` method and assert that the Workflow completed successfully and returned the expected error.

Simply mocking the execution to return a desired value or error is a pretty powerful mechanism to isolate Workflow logic.
However, sometimes we want to replace the Activity with an alternate implementation to support a more complex test scenario.
Let's assume we want to validate that the Activity gets called with the correct parameters.

```go
func (s *UnitTestSuite) Test_SimpleWorkflow_ActivityParamCorrect() {
        s.env.OnActivity(SimpleActivity, mock.Anything, mock.Anything).Return(
          func(ctx context.Context, value string) (string, error) {
                s.Equal("test_success", value)
                return value, nil
        })
        s.env.ExecuteWorkflow(SimpleWorkflow, "test_success")

        s.True(s.env.IsWorkflowCompleted())
        s.NoError(s.env.GetWorkflowError())
}
```

In this example, we provide a function implementation as the parameter to `Return`.
