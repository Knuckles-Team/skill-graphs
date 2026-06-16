This allows us to provide an alternate implementation for the Activity `SimpleActivity`.
The framework will execute this function whenever the Activity is invoked and pass on the return value from the function as the result of the Activity invocation.

Additionally, the framework will validate that the signature of the "mock" function matches the signature of the original Activity function.

Since this can be an entire function, there is no limitation as to what we can do here. In this example, we assert that the `value` param has the same content as the value param we passed to the Workflow.

### Run an Activity {/* #run-an-activity */}

If an Activity references its context, you need to mock that context when testing in isolation.

### Listen to Heartbeats {/* #listen-to-heartbeats */}

When an Activity sends a Heartbeat, be sure that you can see the Heartbeats in your test code so that you can verify them.

### Cancel an Activity {/* #cancel-an-activity */}

If an Activity is supposed to react to a Cancellation, you can test whether it reacts correctly by canceling it.

## Mock and override Nexus operations

Mocking Nexus operations lets you test a Workflow that executes Nexus operations without needing a
Nexus handler to run the actual Nexus operation. You can mock the Nexus operation or override its
implementation with the test Workflow environment.

Consider a test that simulates a Nexus operation call. In this example, the Nexus operation is
called `sample-operation`, the input type is `SampleInput`, the output type is `SampleOutput`, and
it belongs to the Nexus service `sample-service`.

The example below mocks a call to a Nexus synchronous operation, indicated by the returned value
type `*nexus.HandlerStartOperationResultSync[T]`. Since `OnNexusOperation` needs to know the
operation's name, input type and output type, and you might not have access to the Nexus operation
on the handler side, you can use `nexus.NewOperationReference` to create a Nexus operation reference
that represents the operation without its implementation (basically, it represents the signature of
the Nexus operation). You may also use the operation itself instead of creating the operation
reference if you have it available.

```go
func (s *UnitTestSuite) Test_SimpleWorkflow_NexusSyncOperation() {
        s.env.OnNexusOperation(
                "sample-service",
                nexus.NewOperationReference[SampleInput, SampleOutput]("sample-operation"),
                SampleInput{},
                workflow.NexusOperationOptions{},
        ).Return(
                &nexus.HandlerStartOperationResultSync[SampleOutput]{
                        Value: SampleOutput{},
                },
                nil, // error if you want to simulate an error in the ExecuteOperation call
        )
        // You can also add a delay to return the mock values by calling After().
        // Eg: s.env.OnNexusOperation(...).Return(...).After(1*time.Second)

        s.env.ExecuteWorkflow(SimpleWorkflow, "test_nexus_operation")

        s.True(s.env.IsWorkflowCompleted())
        s.NoError(s.env.GetWorkflowError())
}
```

Besides the synchronous operations, you can also mock asynchronous operations. The following example
demonstrates how to test a Workflow executing a Nexus asynchronous operation. The returned value
type in this case must be `*nexus.HandlerStartOperationResultAsync` with an `OperationToken`, which can
be any string of your choice. Furthermore, you must call `RegisterNexusAsyncOperationCompletion` to
register the result of the asynchronous operation identified by the tuple service name, operation
name, and operation token.

```go
func (s *UnitTestSuite) Test_SimpleWorkflow_NexusAsyncOperation() {
        s.env.OnNexusOperation(
                "sample-service",
                nexus.NewOperationReference[SampleInput, SampleOutput]("sample-operation"),
                SampleInput{},
                workflow.NexusOperationOptions{},
        ).Return(
                &nexus.HandlerStartOperationResultAsync{
                        OperationToken: "sample-operation-token",
                },
                nil, // error if you want to simulate an error in the ExecuteOperation call
        )
        err := env.RegisterNexusAsyncOperationCompletion(
                "sample-service",
                "sample-operation",
                "sample-operation-token", // must match the OperationToken above
                SampleOutput{},
                nil,            // error if you want to simulate an error in the operation
                2*time.Second,  // delay to simulate how long the operation takes after it starts
        )
        s.NoError(err)
        s.env.ExecuteWorkflow(SimpleWorkflow, "test_nexus_operation")

        s.True(s.env.IsWorkflowCompleted())
        s.NoError(s.env.GetWorkflowError())
}
```

If your Workflow executes multiple Nexus asynchronous operations, you can mock each of them with
different operation tokens, and register the completion results using the corresponding operation token.

If mocking Nexus operations is not enough, and you need to run some custom logic when the Nexus
operation is executed, you can override it as follows.

```go
func (s *UnitTestSuite) Test_SimpleWorkflow_NexusSyncOperation() {
        var SampleOperation = nexus.NewSyncOperation(
                "sample-operation",
                func(ctx context.Context, input SampleInput, options nexus.StartOperationOptions) (SampleOutput, error) {
                        // Custom logic here.
                        return SampleOutput{}, nil
                },
        )

        service := nexus.NewService("sample-service")
        s.NoError(service.Register(SampleOperation))
        env.RegisterNexusService(service)
        s.env.ExecuteWorkflow(SimpleWorkflow, "test_nexus_operation")

        s.True(s.env.IsWorkflowCompleted())
        s.NoError(s.env.GetWorkflowError())
}
```

The following example shows how to override a Nexus asynchronous operation.

```go
func (s *UnitTestSuite) Test_SimpleWorkflow_NexusSyncOperation() {
        SampleHandlerWorkflow := func(_ workflow.Context, input SampleInput) (SampleOutput, error) {
                // Custom logic here.
                return SampleOutput{}, nil
        }
        SampleOperation := nexus.NewWorkflowRunOperation(
                "sample-operation",
                SampleHandlerWorkflow,
                func(ctx context.Context, input SampleInput, options nexus.StartOperationOptions) (client.StartWorkflowOptions, error) {
                        // Custom logic to build client.StartWorkflowOptions.
                        return client.StartWorkflowOptions{}, nil
                },
        )

        service := nexus.NewService("sample-service")
        s.NoError(service.Register(SampleOperation))
        env.RegisterNexusService(service)
        s.env.ExecuteWorkflow(SimpleWorkflow, "test_nexus_operation")

        s.True(s.env.IsWorkflowCompleted())
        s.NoError(s.env.GetWorkflowError())
}
```

## Testing Workflows {/* #test-workflows */}

When running unit tests on Workflows, we want to test the Workflow logic in isolation.
The simplest test case we can write is to have the test environment execute the Workflow and then evaluate the results.

```go
func (s *UnitTestSuite) Test_SimpleWorkflow_Success() {
        s.env.ExecuteWorkflow(SimpleWorkflow, "test_success")

        s.True(s.env.IsWorkflowCompleted())
        s.NoError(s.env.GetWorkflowError())
}
```

Calling `s.env.ExecuteWorkflow(...)` executes the Workflow logic and any invoked Activities inside the test process. The first parameter of `s.env.ExecuteWorkflow(...)` contains the Workflow functions, and any subsequent parameters contain values for custom input parameters declared by the Workflow.

> Note that unless the Activity invocations are mocked or Activity implementation replaced (see [Activity mocking and overriding](#mock-and-override-activities)), the test environment will execute the actual Activity code including any calls to outside services.

After executing the Workflow in the above example, we assert that the Workflow ran through completion via the call to `s.env.IsWorkflowCompleted()`. We also assert that no errors were returned by asserting on the return value of `s.env.GetWorkflowError()`.
If our Workflow returned a value, we could have retrieved that value via a call to `s.env.GetWorkflowResult(&value)` and had additional asserts on that value.

### Query tests

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

### How to mock Activities {/* #mock-activities */}

Mock the Activity invocation when unit testing your Workflows.

When integration testing Workflows with a Worker, you can mock Activities by providing mock Activity implementations to the Worker.

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

Set up the time-skipping test framework in the SDK of your choice.

{/* #### Skip time automatically {/* #automatic-method */} */}

You can skip time automatically in the SDK of your choice.
Start a test server process that skips time as needed.
For example, in the time-skipping mode, Timers, which include sleeps and conditional timeouts, are fast-forwarded except when Activities are running.

{/* #### Skip time manually {/* #manual-method */} */}

Skip time manually in the SDK of your choice.

#### Skip time in Activities {/* #skip-time-in-activities */}

Skip time in Activities in the SDK of your choice.

## How to Replay a Workflow Execution {/* #replay */}

Replay recreates the exact state of a Workflow Execution.
You can replay a Workflow from the beginning of its Event History.

Replay succeeds only if the [Workflow Definition](/workflow-definition) is compatible with the provided history from a deterministic point of view.

When you test changes to your Workflow Definitions, we recommend doing the following as part of your CI checks:

1. Determine which Workflow Types or Task Queues (or both) will be targeted by the Worker code under test.
2. Download the Event Histories of a representative set of recent open and closed Workflows from each Task Queue, either programmatically using the SDK client or via the Temporal CLI.
3. Run the Event Histories through replay.
4. Fail CI if any error is encountered during replay.

The following are examples of fetching and replaying Event Histories:

Use the [worker.WorkflowReplayer](https://pkg.go.dev/go.temporal.io/sdk/worker#WorkflowReplayer) to replay an existing Workflow Execution from its Event History to replicate errors.

For example, the following code retrieves the Event History of a Workflow:

```go

	"context"

	"go.temporal.io/api/enums/v1"
	"go.temporal.io/api/history/v1"
	"go.temporal.io/sdk/client"
)

func GetWorkflowHistory(ctx context.Context, client client.Client, id, runID string) (*history.History, error) {
	var hist history.History
	iter := client.GetWorkflowHistory(ctx, id, runID, false, enums.HISTORY_EVENT_FILTER_TYPE_ALL_EVENT)
	for iter.HasNext() {
		event, err := iter.Next()
		if err != nil {
			return nil, err
		}
		hist.Events = append(hist.Events, event)
	}
	return &hist, nil
}
```

This history can then be used to _replay_.
For example, the following code creates a `WorkflowReplayer` and register the `YourWorkflow` Workflow function.
Then it calls the `ReplayWorkflowHistory` to _replay_ the Event History and return an error code.

```go

	"context"

	"go.temporal.io/sdk/client"
	"go.temporal.io/sdk/worker"
)

func ReplayWorkflow(ctx context.Context, client client.Client, id, runID string) error {
	hist, err := GetWorkflowHistory(ctx, client, id, runID)
	if err != nil {
		return err
	}
	replayer := worker.NewWorkflowReplayer()
	replayer.RegisterWorkflow(YourWorkflow)
	return replayer.ReplayWorkflowHistory(nil, hist)
}
```

The code above will cause the Worker to re-execute the Workflow's Workflow Function using the original Event History.
If a noticeably different code path was followed or some code caused a deadlock, it will be returned in the error code.
Replaying a Workflow Execution locally is a good way to see exactly what code path was taken for given input and events.

You can replay many Event Histories by registering all the needed Workflow implementation and then calling `ReplayWorkflowHistory` repeatedly.

---

## Client - Go SDK

![Go SDK Banner](/img/assets/banner-go-temporal.png)

## Temporal Client

- [Temporal Client](/develop/go/client/temporal-client)
- [Namespaces](/develop/go/client/namespaces)

---

## Namespaces - Go SDK

This page shows how to do the following:

- [Register Namespaces](#register-namespace)
- [Manage Namespaces](#manage-namespaces)

You can create, update, deprecate, or delete your [Namespaces](/namespaces) using either the Temporal CLI or SDK APIs.

Use Namespaces to isolate your Workflow Executions according to your needs.
For example, you can use Namespaces to match the development lifecycle by having separate `dev` and `prod` Namespaces.
You could also use them to ensure Workflow Executions between different teams never communicate - such as ensuring that the `teamA` Namespace never impacts the `teamB` Namespace.

On Temporal Cloud, use the [Temporal Cloud UI](/cloud/namespaces#create-a-namespace) to create and manage a Namespace from the UI, or [tcld commands](https://docs.temporal.io/cloud/tcld/namespace/) to manage Namespaces from the command-line interface.

On self-hosted Temporal Service, you can register and manage your Namespaces using the Temporal CLI (recommended) or programmatically using APIs.
Note that these APIs and Temporal CLI commands will not work with Temporal Cloud.

Use a custom [Authorizer](/self-hosted-guide/security#authorizer-plugin) on your Frontend Service in the Temporal Service to set restrictions on who can create, update, or deprecate Namespaces.

You must register a Namespace with the Temporal Service before setting it in the Temporal Client.

### How to register Namespaces {/* #register-namespace */}

Registering a Namespace creates a Namespace on the Temporal Service or Temporal Cloud.

On Temporal Cloud, use the [Temporal Cloud UI](/cloud/namespaces#create-a-namespace) or [tcld commands](https://docs.temporal.io/cloud/tcld/namespace/) to create Namespaces.

On self-hosted Temporal Service, you can register your Namespaces using the Temporal CLI (recommended) or programmatically using APIs.
Note that these APIs and Temporal CLI commands will not work with Temporal Cloud.

Use a custom [Authorizer](/self-hosted-guide/security#authorizer-plugin) on your Frontend Service in the Temporal Service to set restrictions on who can create, update, or deprecate Namespaces.

Use [`Register` API](https://pkg.go.dev/go.temporal.io/sdk/client#NamespaceClient) with the `NamespaceClient` interface to register a [Namespace](/namespaces) and set the [Retention Period](/temporal-service/temporal-server#retention-period) for the Workflow Execution Event History for the Namespace.

You can also [register Namespaces using the Temporal CLI command-line tool](/cli/command-reference/operator#create).

```go
client, err := client.NewNamespaceClient(client.Options{HostPort: ts.config.ServiceAddr})
        //...
    err = client.Register(ctx, &workflowservice.RegisterNamespaceRequest{
        Namespace: your-namespace-name,
        WorkflowExecutionRetentionPeriod: &retention,
    })
```

The Retention Period setting using `WorkflowExecutionRetentionPeriod` is mandatory.
The minimum value you can set for this period is 1 day.

Once registered, set Namespace using `Dial` in a Workflow Client to run your Workflow Executions within that Namespace.
See [how to set Namespace in a Client in Go](/develop/go/client/temporal-client#connect-to-temporal-cloud) for details.

Note that Namespace registration using this API takes up to 10 seconds to complete.
Ensure that you wait for this registration to complete before starting the Workflow Execution against the Namespace.

To update your Namespace, use the [`Update` API](https://pkg.go.dev/go.temporal.io/sdk/client#NamespaceClient) with the `NamespaceClient`.

To update your Namespace using the Temporal CLI, use the [temporal operator namespace update](/cli/command-reference/operator#update) command.

### How to manage Namespaces {/* #manage-namespaces */}

You can get details for your Namespaces, update Namespace configuration, and deprecate or delete your Namespaces.

On Temporal Cloud, use the [Temporal Cloud UI](/cloud/namespaces#create-a-namespace) or [tcld commands](https://docs.temporal.io/cloud/tcld/namespace/) to manage Namespaces.

On self-hosted Temporal Service, you can manage your registered Namespaces using the Temporal CLI (recommended) or programmatically using APIs.
Note that these APIs and Temporal CLI commands will not work with Temporal Cloud.

Use a custom [Authorizer](/self-hosted-guide/security#authorizer-plugin) on your Frontend Service in the Temporal Service to set restrictions on who can create, update, or deprecate Namespaces.

You must register a Namespace with the Temporal Service before setting it in the Temporal Client.

On Temporal Cloud, use the [Temporal Cloud UI](/cloud/namespaces) or [tcld commands](/cloud/tcld/namespace/) to manage Namespaces.

On self-hosted Temporal Service, you can manage your registered Namespaces using the Temporal CLI (recommended) or programmatically using APIs.
Note that these APIs and Temporal CLI commands will not work with Temporal Cloud.

- Update information and configuration for a registered Namespace on your Temporal Service:

  - With the Temporal CLI: [`temporal operator namespace update`](/cli/command-reference/operator#update)
    Example
  - Use the [`UpdateNamespace` API](https://pkg.go.dev/go.temporal.io/sdk/client#NamespaceClient) to update configuration on a Namespace.
    Example

    ```go
    //...
      err = client.Update(context.Background(), &workflowservice.UpdateNamespaceRequest{
      Namespace:         "your-namespace-name",
      UpdateInfo:        &namespace.UpdateNamespaceInfo{ //updates info for the namespace "your-namespace-name"
          Description:   "updated namespace description",
          OwnerEmail:    "newowner@mail.com",
          //Data:        nil,
          //State:       0,
      },
      /*other details that you can update:
      Config:            &namespace.NamespaceConfig{ //updates the configuration of the namespace with the following options
          //WorkflowExecutionRetentionTtl: nil,
          //BadBinaries:                   nil,
          //HistoryArchivalState:          0,
          //HistoryArchivalUri:            "",
          //VisibilityArchivalState:       0,
          //VisibilityArchivalUri:         "",
      },
      ReplicationConfig: &replication.NamespaceReplicationConfig{ //updates the replication configuration for the namespace
          //ActiveClusterName: "",
          //Clusters:          nil,
          //State:             0,
      },
      SecurityToken:     "",
      DeleteBadBinary:   "",
      PromoteNamespace:  false,
      })*/
    //...
    ```

- Get details for a registered Namespace on your Temporal Service:

  - With the Temporal CLI: [`temporal operator namespace describe`](/cli/command-reference/operator#describe)
  - Use the [`DescribeNamespace` API](https://pkg.go.dev/go.temporal.io/sdk/client#NamespaceClient) to return information and configuration details for a registered Namespace.
    Example

    ```go
    //...
      client, err := client.NewNamespaceClient(client.Options{})
      //...
      client.Describe(context.Background(), "default")
    //...
    ```

- Get details for all registered Namespaces on your Temporal Service:

  - With the Temporal CLI: [`temporal operator namespace list`](/cli/command-reference/operator#list)
  - Use the [`ListNamespace` API](https://github.com/temporalio/api/blob/f0350f8032ad2f0c60c539b3b61ea37f412f1cf7/temporal/api/operatorservice/v1/service.proto) to return information and configuration details for all registered Namespaces on your Temporal Service.
    Example

  ```go
  //...
      namespace.Handler.ListNamespaces(context.Context(), &workflowservice.ListNamespacesRequest{ //lists 1 page (1-100) of namespaces on the active Temporal Service. You can set a large PageSize or loop until NextPageToken is nil
          //PageSize:        0,
          //NextPageToken:   nil,
          //NamespaceFilter: nil,
          })
  //...
  ```

- Delete a Namespace: The [`DeleteNamespace` API](https://github.com/temporalio/api/blob/f0350f8032ad2f0c60c539b3b61ea37f412f1cf7/temporal/api/operatorservice/v1/service.proto) deletes a Namespace. Deleting a Namespace deletes all running and completed Workflow Executions on the Namespace, and removes them from the persistence store and the visibility store.
  Example:

  ```go
  //...
  client.OperatorService().DeleteNamespace(ctx, &operatorservice.DeleteNamespaceRequest{...
  //...
  ```

---

## Temporal Client - Go SDK

A [Temporal Client](/encyclopedia/temporal-sdks#temporal-client) enables you to communicate with the
[Temporal Service](/temporal-service). Communication with a Temporal Service lets you perform actions such as starting
Workflow Executions, sending Signals to Workflow Executions, sending Queries to Workflow Executions, getting the results
of a Workflow Execution, and providing Activity Task Tokens.

This page shows you how to do the following using the Go SDK with the Temporal Client:

- [Connect to a local development Temporal Service](#connect-to-development-service)
- [Connect to Temporal Cloud](#connect-to-temporal-cloud)
- [Start a Workflow Execution](#start-workflow-execution)
- [Get Workflow results](#get-workflow-results)

:::caution

A Temporal Client cannot be initialized and used inside a Workflow. However, it is acceptable and common to use a
Temporal Client inside an Activity to communicate with a Temporal Service.

:::

## Connect to development Temporal Service {/* #connect-to-development-service */}

Use the [`Dial()`](https://pkg.go.dev/go.temporal.io/sdk/client#Dial) API available in the
[`go.temporal.io/sdk/client`](https://pkg.go.dev/go.temporal.io/sdk/client) package to create a
