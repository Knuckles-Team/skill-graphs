
The `ExecuteChildWorkflow` call requires an instance of [`workflow.Context`](https://pkg.go.dev/go.temporal.io/sdk/workflow#Context), with an instance of [`workflow.ChildWorkflowOptions`](https://pkg.go.dev/go.temporal.io/sdk/workflow#ChildWorkflowOptions) applied to it, the Workflow Type, and any parameters that should be passed to the Child Workflow Execution.

`workflow.ChildWorkflowOptions` contain the same fields as `client.StartWorkflowOptions`.
Workflow Option fields automatically inherit their values from the Parent Workflow Options if they are not explicitly set.
If a custom `WorkflowID` is not set, one is generated when the Child Workflow Execution is spawned.
Use the [`WithChildOptions`](https://pkg.go.dev/go.temporal.io/sdk/workflow#WithChildOptions) API to apply Child Workflow Options to the instance of `workflow.Context`.

The `ExecuteChildWorkflow` call returns an instance of a [`ChildWorkflowFuture`](https://pkg.go.dev/go.temporal.io/sdk/workflow#ChildWorkflowFuture).

Call the `.Get()` method on the instance of `ChildWorkflowFuture` to wait for the result.

```go
func YourWorkflowDefinition(ctx workflow.Context, params ParentParams) (ParentResp, error) {

  childWorkflowOptions := workflow.ChildWorkflowOptions{}
  ctx = workflow.WithChildOptions(ctx, childWorkflowOptions)

  var result ChildResp
  err := workflow.ExecuteChildWorkflow(ctx, YourOtherWorkflowDefinition, ChildParams{}).Get(ctx, &result)
  if err != nil {
    // ...
  }
  // ...
  return resp, nil
}

func YourOtherWorkflowDefinition(ctx workflow.Context, params ChildParams) (ChildResp, error) {
  // ...
  return resp, nil
}
```

### Async Child Workflows

To asynchronously spawn a Child Workflow Execution, the Child Workflow must have an "Abandon" Parent Close Policy set in the Child Workflow Options.
Additionally, the Parent Workflow Execution must wait for the `ChildWorkflowExecutionStarted` Event to appear in its Event History before it completes.

If the Parent makes the `ExecuteChildWorkflow` call and then immediately completes, the Child Workflow Execution does not spawn.

To be sure that the Child Workflow Execution has started, first call the `GetChildWorkflowExecution` method on the instance of the `ChildWorkflowFuture`, which will return a different Future.
Then call the `Get()` method on that Future, which is what will wait until the Child Workflow Execution has spawned.

```go

  // ...
  "go.temporal.io/api/enums/v1"
)

func YourWorkflowDefinition(ctx workflow.Context, params ParentParams) (ParentResp, error) {

  childWorkflowOptions := workflow.ChildWorkflowOptions{
    ParentClosePolicy: enums.PARENT_CLOSE_POLICY_ABANDON,
  }
  ctx = workflow.WithChildOptions(ctx, childWorkflowOptions)

  childWorkflowFuture := workflow.ExecuteChildWorkflow(ctx, YourOtherWorkflowDefinition, ChildParams{})
  // Wait for the Child Workflow Execution to spawn
  var childWE workflow.Execution
  if err := childWorkflowFuture.GetChildWorkflowExecution().Get(ctx, &childWE); err != nil {
     return err
  }
  // ...
  return resp, nil
}

func YourOtherWorkflowDefinition(ctx workflow.Context, params ChildParams) (ChildResp, error) {
  // ...
  return resp, nil
}
```

#### Set a Parent Close Policy {/* #parent-close-policy */}

A [Parent Close Policy](/parent-close-policy) determines what happens to a Child Workflow Execution if its Parent changes to a Closed status (Completed, Failed, or Timed Out).

The default Parent Close Policy option is set to terminate the Child Workflow Execution.

In Go, a Parent Close Policy is set on the `ParentClosePolicy` field of an instance of [`workflow.ChildWorkflowOptions`](https://pkg.go.dev/go.temporal.io/sdk/workflow#ChildWorkflowOptions).
The possible values can be obtained from the [`go.temporal.io/api/enums/v1`](https://pkg.go.dev/go.temporal.io/api/enums/v1#ParentClosePolicy) package.

- `PARENT_CLOSE_POLICY_ABANDON`
- `PARENT_CLOSE_POLICY_TERMINATE`
- `PARENT_CLOSE_POLICY_REQUEST_CANCEL`

The Child Workflow Options are then applied to the instance of `workflow.Context` by using the `WithChildOptions` API, which is then passed to the `ExecuteChildWorkflow()` call.

- Type: [`ParentClosePolicy`](https://pkg.go.dev/go.temporal.io/api/enums/v1#ParentClosePolicy)
- Default: `PARENT_CLOSE_POLICY_TERMINATE`

```go

  // ...
  "go.temporal.io/api/enums/v1"
)

func YourWorkflowDefinition(ctx workflow.Context, params ParentParams) (ParentResp, error) {
  // ...
  childWorkflowOptions := workflow.ChildWorkflowOptions{
    // ...
    ParentClosePolicy: enums.PARENT_CLOSE_POLICY_ABANDON,
  }
  ctx = workflow.WithChildOptions(ctx, childWorkflowOptions)
  childWorkflowFuture := workflow.ExecuteChildWorkflow(ctx, YourOtherWorkflowDefinition, ChildParams{})
  // ...
}

func YourOtherWorkflowDefinition(ctx workflow.Context, params ChildParams) (ChildResp, error) {
  // ...
  return resp, nil
}
```

---

## Continue-As-New - Go SDK

This page answers the following questions for Go developers:

- [What is Continue-As-New?](#what)
- [How to Continue-As-New?](#how)
- [When is it right to Continue-as-New?](#when)
- [How to test Continue-as-New?](#how-to-test)

## What is Continue-As-New? {/* #what */}

[Continue-As-New](/workflow-execution/continue-as-new) lets a Workflow Execution close successfully and creates a new Workflow Execution.
You can think of it as a checkpoint when your Workflow gets too long or approaches certain scaling limits.

The new Workflow Execution is in the same [chain](/workflow-execution#workflow-execution-chain); it keeps the same Workflow Id but gets a new Run Id and a fresh Event History.
It also receives your Workflow's usual parameters.

## How to Continue-As-New using the Go SDK {/* #how */}

First, design your Workflow parameters so that you can pass in the "current state" when you Continue-As-New into the next Workflow run.
This state is typically set to `None` for the original caller of the Workflow.

    View the source code
  {' '}
  in the context of the rest of the application code.

```go
ClusterManagerInput struct {
    State             *ClusterManagerState
    TestContinueAsNew bool
}

func newClusterManager(ctx workflow.Context, wfInput ClusterManagerInput) (*ClusterManager, error) {

````
The test hook in the above snippet is covered [below](#how-to-test).

Inside your Workflow, return the [`NewContinueAsNewError`](https://pkg.go.dev/go.temporal.io/sdk/workflow#NewContinueAsNewError) error.
This stops the Workflow right away and starts a new one.

    View the source code
  {' '}
  in the context of the rest of the application code.

```go
return ClusterManagerResult{}, workflow.NewContinueAsNewError(
    ctx,
    ClusterManagerWorkflow,
    ClusterManagerInput{
        State:             &cm.state,
        TestContinueAsNew: cm.testContinueAsNew,
    },
)
````

### Considerations for Workflows with Message Handlers {/* #with-message-handlers */}

If you use Updates or Signals, don't call Continue-as-New from the handlers.
Instead, wait for your handlers to finish in your main Workflow before you return `NewContinueAsNewError`.
See the [`AllHandlersFinished`](message-passing#wait-for-message-handlers) example for guidance.

## When is it right to Continue-as-New using the Go SDK? {/* #when */}

Use Continue-as-New when your Workflow might hit [Event History Limits](/workflow-execution/event#event-history).

Temporal tracks your Workflow's progress against these limits to let you know when you should Continue-as-New.
Call `GetInfo(ctx).GetContinueAsNewSuggested()` to check if it's time.

## How to test Continue-as-New using the Go SDK {/* #how-to-test */}

Testing Workflows that naturally Continue-as-New may be time-consuming and resource-intensive.
Instead, add a test hook to check your Workflow's Continue-as-New behavior faster in automated tests.

For example, when `TestContinueAsNew == True`, this sample creates a test-only variable called `maxHistoryLength` and sets it to a small value.
A helper method in the Workflow checks it each time it considers using Continue-as-New:

    View the source code
  {' '}
  in the context of the rest of the application code.

```go
func (cm *ClusterManager) shouldContinueAsNew(ctx workflow.Context) bool {
	if workflow.GetInfo(ctx).GetContinueAsNewSuggested() {
		return true
	}
	if cm.maxHistoryLength > 0 && workflow.GetInfo(ctx).GetCurrentHistoryLength() > cm.maxHistoryLength {
		return true
	}
	return false
}
```

---

## Dynamic Workflow - Go SDK

## Set a Dynamic Workflow {/* #set-a-dynamic-workflow */}

A Dynamic Workflow in Temporal is a Workflow that is invoked dynamically at runtime if no other Workflow with the same name is registered.
A Workflow can be registered as dynamic by using `worker.RegisterDynamicWorkflow()`.
You must register the Workflow with the Worker before it can be invoked.
Only one Dynamic Workflow can be present on a Worker.

The Workflow Definition must then accept a single argument of type `converter.EncodedValues`.
This code snippet is taken from the [Dynamic Workflow example from samples-go](https://github.com/temporalio/samples-go/tree/main/dynamic-workflows).

```go
func DynamicWorkflow(ctx workflow.Context, args converter.EncodedValues) (string, error) {
	var result string
	info := workflow.GetInfo(ctx)

	var arg1, arg2 string
	err := args.Get(&arg1, &arg2)
	if err != nil {
		return "", fmt.Errorf("failed to decode arguments: %w", err)
	}

	if info.WorkflowType.Name == "dynamic-activity" {
		ctx = workflow.WithActivityOptions(ctx, workflow.ActivityOptions{StartToCloseTimeout: 10 * time.Second})
		err := workflow.ExecuteActivity(ctx, "random-activity-name", arg1, arg2).Get(ctx, &result)
		if err != nil {
			return "", err
		}
	} else {
		result = fmt.Sprintf("%s - %s - %s", info.WorkflowType.Name, arg1, arg2)
	}

	return result, nil
}
```

---

## Workflows - Go SDK

![Go SDK Banner](/img/assets/banner-go-temporal.png)

## Workflows

- [Workflow basics](/develop/go/workflows/basics)
- [Child Workflows](/develop/go/workflows/child-workflows)
- [Continue-As-New](/develop/go/workflows/continue-as-new)
- [Cancellation](/develop/go/workflows/cancellation)
- [Timeouts](/develop/go/workflows/timeouts)
- [Message passing](/develop/go/workflows/message-passing)
- [Selectors](/develop/go/workflows/selectors)
- [Side effects](/develop/go/workflows/side-effects)
- [Schedules](/develop/go/workflows/schedules)
- [Timers](/develop/go/workflows/timers)
- [Dynamic Workflow](/develop/go/workflows/dynamic-workflow)
- [Versioning](/develop/go/workflows/versioning)

---

## Workflow message passing - Go SDK

A Workflow can act like a stateful web service that receives messages: Queries, Signals, and Updates.
The Workflow implementation defines these endpoints via handler methods that can react to incoming Queries and Updates, and via Signal channels.
Temporal Clients use messages to read Workflow state and control its execution.
See [Workflow message passing](/encyclopedia/workflow-message-passing) for a general overview of this topic.
This page introduces these features for the Temporal Go SDK.

## Handle messages {/* #handling-messages */}

:::info
The code that follows is part of a working message passing [sample](https://github.com/temporalio/samples-go/tree/message-passing/message-passing-intro).
:::

Follow these guidelines when writing message handlers:

- Values sent in messages, and the return values of message handlers and the main Workflow function, must be [serializable](/dataconversion).
- Prefer using a single struct over multiple input parameters.
  This allows you to add fields without changing the calling signature.

### Query handlers {/* #queries */}

A [Query](/sending-messages#sending-queries) is a synchronous operation that retrieves state from a Workflow Execution:

```go
type Language string

const Chinese Language = "chinese"
const English Language = "english"
const French Language = "french"
const Spanish Language = "spanish"
const Portuguese Language = "portuguese"

const GetLanguagesQuery = "GetLanguages"

type GetLanguagesInput struct {
	IncludeUnsupported bool
}

func GreetingWorkflow(ctx workflow.Context) (string, error) {
    ...
    greeting := map[Language]string{English: "Hello", Chinese: "你好，世界"}
    err := workflow.SetQueryHandler(ctx, GetLanguagesQuery, func(input GetLanguagesInput) ([]Language, error) {
        // 👉 A Query handler returns a value: it can inspect but must not mutate the Workflow state.
        if input.IncludeUnsupported {
            return []Language{Chinese, English, French, Spanish, Portuguese}, nil
        } else {
            // Range over map is a nondeterministic operation.
            // It is OK to have a non-deterministic operation in a query function.
            //workflowcheck:ignore
            return maps.Keys(greeting), nil
        }
    })
    ...
}
```

- Use [`SetQueryHandler`](https://pkg.go.dev/go.temporal.io/sdk/workflow#SetQueryHandler) to set a Query Handler that listens for a Query by name.
- The handler must be a function that returns two values, a serializable result and an error.
- You can't perform async operations such as executing an Activity in a Query handler.

### Signal Channels {/* #signals */}

A [Signal](/sending-messages#sending-signals) is an asynchronous message sent to a running Workflow Execution to change its state and control its flow.
Handle Signal messages by receiving them from their channel:

```go
const ApproveSignal = "approve"

type ApproveInput struct {
	Name string
}

func GreetingWorkflow(ctx workflow.Context) error {
    logger := workflow.GetLogger(ctx)
	approverName := ""
	...
	// Block until the language is approved
	var approveInput ApproveInput
	workflow.GetSignalChannel(ctx, ApproveSignal).Receive(ctx, &approveInput)
	approverName = approveInput.Name
	logger.Info("Received approval", "Approver", approverName)
	...
}
```

- Pass the Signal's name to [`GetSignalChannel`](https://pkg.go.dev/go.temporal.io/sdk/workflow#GetSignalChannel) to get the Signal Channel that listens for Signals of that type.

Alternatively, you might want the Workflow to proceed and still be capable of handling external Signals.

```go
func YourWorkflowDefinition(ctx workflow.Context, param YourWorkflowParam) error {
   var signal MySignal
   signalChan := workflow.GetSignalChannel(ctx, "your-signal-name")
 	workflow.Go(ctx, func(ctx workflow.Context) {
 		for {
 			selector := workflow.NewSelector(ctx)
 			selector.AddReceive(signalChan, func(c workflow.ReceiveChannel, more bool) {
 				c.Receive(ctx, &signal)
 			})
 			selector.Select(ctx)
 		}
 	})
   // You could now submit an activity; any signals will still be received while the activity is pending.
 }
```

In the example above, the Workflow code uses `workflow.GetSignalChannel` to open a `workflow.Channel` for the Signal type (identified by the Signal name).

- Before completing the Workflow or using [Continue-As-New](/develop/go/workflows/continue-as-new), make sure to do an asynchronous drain on the Signal channel.
  Otherwise, the Signals will be lost.
  The [batch sliding window](https://github.com/temporalio/samples-go/tree/main/batch-sliding-window) sample contains an example:
- Delay calling `workflow.GetSignalChannel` until the Workflow initialization needed to process the Signal channel has finished.
  This is safe because the SDK buffers signals when there are no channels created for them.

```go
reportCompletionChannel := workflow.GetSignalChannel(ctx, "ReportCompletion")
// Drain signals async
for {
	var recordId int
	ok := reportCompletionChannel.ReceiveAsync(&recordId)
	if !ok {
		break
	}
	s.recordCompletion(ctx, recordId)
}
```

### Update handlers and validators {/* #updates */}

An [Update](/sending-messages#sending-updates) is a trackable synchronous request sent to a running Workflow Execution.
It can change the Workflow state, control its flow, and return a result.
The sender must wait until the Worker accepts or rejects the Update.
The sender may wait further to receive a returned value or an exception if something goes wrong:

```go
type Language string

const SetLanguageUpdate = "set-language"

func GreetingWorkflow(ctx workflow.Context) error {
	language := English

	err = workflow.SetUpdateHandlerWithOptions(ctx, SetLanguageUpdate, func(ctx workflow.Context, newLanguage Language) (Language, error) {
		// 👉 An Update handler can mutate the Workflow state and return a value.
		var previousLanguage Language
		previousLanguage, language = language, newLanguage
		return previousLanguage, nil
	}, workflow.UpdateHandlerOptions{
		Validator: func(ctx workflow.Context, newLanguage Language) error {
			if _, ok := greeting[newLanguage]; !ok {
				// 👉 In an Update validator you return any error to reject the Update.
				return fmt.Errorf("%s unsupported language", newLanguage)
			}
			return nil
		},
	})
  ...
}
```

- Register an Update handler for a given name using either [workflow.SetUpdateHandler](https://pkg.go.dev/go.temporal.io/sdk/workflow#SetUpdateHandler) or [workflow.SetUpdateHandlerWithOptions](https://pkg.go.dev/go.temporal.io/sdk/workflow#SetUpdateHandlerWithOptions).
- The handler must be a function that accepts a `workflow.Context` as its first parameter.
- The function can return either a serializable value with an error or just an error.

- About validators:
  - Use validators to reject an Update before it is written to History.
    Validators are always optional.
    If you don't need to reject Updates, you don't need a validator.
  - To set a validator, pass the validator function in the [workflow.UpdateHandlerOptions](https://pkg.go.dev/go.temporal.io/sdk@v1.29.1/internal#UpdateHandlerOptions) when calling [workflow.SetUpdateHandlerWithOptions](https://pkg.go.dev/go.temporal.io/sdk/workflow#SetUpdateHandlerWithOptions).
    The validator must be a function that accepts the same argument types as the handler and returns a single value of type error.

- Accepting and rejecting Updates with validators:
  - To reject an Update you must return an error or panic in the validator.
    The Workflow's `WorkflowPanicPolicy` determines how panics are handled inside the Handler function.
  - Without a validator, Updates are always accepted.
- Validators and Event History:
  - The `WorkflowExecutionUpdateAccepted` event is written into History whether the acceptance was automatic or due to a validator function not throwing an error or panicking.
  - When a validator throws an error, the Update is rejected and `WorkflowExecutionUpdateAccepted` _won't_ be added to the Event History.
    The caller receives an "Update failed" error.

- Use [`workflow.GetCurrentUpdateInfo`](https://pkg.go.dev/go.temporal.io/sdk/workflow#GetCurrentUpdateInfo) to obtain information about the current Update.
  This includes the Update ID, which can be useful for deduplication when using Continue-As-New: see [Ensuring your messages are processed exactly once](/handling-messages#exactly-once-message-processing).
- Update handlers can use Activities, Child Workflows, durable [workflow.Sleep](https://pkg.go.dev/go.temporal.io/sdk/workflow#Sleep) Timers, [`workflow.Await`](https://pkg.go.dev/go.temporal.io/sdk/workflow#Await) conditions, and more.
  See [Blocking handlers](#blocking-handlers) and [Workflow message passing](/encyclopedia/workflow-message-passing) for safe usage guidelines.
- Delay calling [`workflow.SetUpdateHandler`](https://pkg.go.dev/go.temporal.io/sdk/workflow#SetUpdateHandler) until the Workflow initialization needed by Update handlers is finished.
  This is safe because the SDK buffers messages when there are no registered handlers for them.
  Note that [`workflow.SetUpdateHandler`](https://pkg.go.dev/go.temporal.io/sdk/workflow#SetUpdateHandler) will immediately invoke the handler of buffered Updates with matching types.
  This could lead to out-of-order processing of messages with different types.

## Send messages {/* #send-messages */}

To send Queries, Signals, or Updates, you call methods on a Temporal [Client](https://pkg.go.dev/go.temporal.io/sdk/client#Client).
To check the argument types required when sending messages -- and the return type for Queries and Updates -- refer to the corresponding handler method in the Workflow Definition.

:::warning Using Continue-as-New and Updates

- Temporal _does not_ support Continue-as-New functionality within Update handlers.
- Complete all handlers _before_ using Continue-as-New.
- Use Continue-as-New from your main Workflow function, just as you would complete or fail a Workflow Execution.

:::

### Send a Query {/* #send-query */}

Queries are sent from a Temporal Client.

Use [`Client.QueryWorkflow`](https://pkg.go.dev/go.temporal.io/sdk/client#Client.QueryWorkflow) or [`Client.QueryWorkflowWithOptions`](https://pkg.go.dev/go.temporal.io/sdk/client#Client.QueryWorkflowWithOptions).

```go
// ...
supportedLangResult, err := temporalClient.QueryWorkflow(context.Background(), we.GetID(), we.GetRunID(), message.GetLanguagesQuery, message.GetLanguagesInput{IncludeUnsupported: false})
if err != nil {
    log.Fatalf("Unable to query workflow: %v", err)
}
var supportedLang []message.Language
err = supportedLangResult.Get(&supportedLang)
if err != nil {
    log.Fatalf("Unable to get query result: %v", err)
}
log.Println("Supported languages:", supportedLang)
// ...
```

- Sending a Query doesn’t add events to a Workflow's Event History.

- You can send Queries to closed Workflow Executions within a Namespace's Workflow retention period.
  This includes Workflows that have completed, failed, or timed out.
  Querying terminated Workflows is not supported.

- A Worker must be online and polling the Task Queue to process a Query.

### Send a Signal {/* #send-signal */}

You can send a Signal to a Workflow Execution from a Temporal Client or from another Workflow Execution.
However, you can only send Signals to Workflow Executions that haven’t closed.

#### Send a Signal from a Client {/* #send-signal-from-client */}

Use [`Client.SignalWorkflow`](https://pkg.go.dev/go.temporal.io/sdk/client#Client.SignalWorkflow).

Pass in both the [Workflow Id](/workflow-execution/workflowid-runid#workflow-id) and [Run Id](/workflow-execution/workflowid-runid#run-id) to uniquely identify the Workflow Execution.
If only the Workflow Id is supplied (provide an empty string as the Run Id param), the Workflow Execution that is running receives the Signal.

```go
// ...
err = temporalClient.SignalWorkflow(context.Background(), we.GetID(), we.GetRunID(), message.ApproveSignal, message.ApproveInput{Name: ""})
if err != nil {
    log.Fatalf("Unable to signal workflow: %v", err)
}
// ...
```

- The call returns when the server accepts the Signal; it does _not_ wait for the Signal to be delivered to the Workflow Execution.

- The [WorkflowExecutionSignaled](/references/events#workflowexecutionsignaled) Event appears in the Workflow's Event History.

#### Sending a Signal from a Workflow {/* #send-signal-from-workflow */}

A Workflow can send a Signal to another Workflow, in which case it's called an External Signal.

```go
// ...
func YourWorkflowDefinition(ctx workflow.Context, param YourWorkflowParam) error {
  ...
  signal := MySignal {
    Message: "Some important data",
  }
  err :=  workflow.SignalExternalWorkflow(ctx, "some-workflow-id", "", "your-signal-name", signal).Get(ctx, nil)
  if err != nil {
    // ...
  }
// ...
}
```

When an External Signal is sent:

- A [SignalExternalWorkflowExecutionInitiated](/references/events#signalexternalworkflowexecutioninitiated) Event appears in the sender's Event History.
- A [WorkflowExecutionSignaled](/references/events#workflowexecutionsignaled) Event appears in the recipient's Event History.

#### Signal-With-Start {/* #signal-with-start */}

Signal-With-Start is used from the Client.
It takes a Workflow Id, Workflow arguments, a Signal name, and Signal arguments.

If there's a Workflow running with the given Workflow Id, it will be signaled. If there isn't, a new Workflow will be started and immediately signaled.

Use the [`Client.SignalWithStartWorkflow`](https://pkg.go.dev/go.temporal.io/sdk/client#Client.SignalWithStartWorkflow) API to start a Workflow Execution (if not already running) and pass it the Signal at the same time.

Because the Workflow Execution might not exist, this API does not take a Run Id as a parameter

```go
// ...
signal := MySignal {
  Message: "Some important data",
}
err = temporalClient.SignalWithStartWorkflow(context.Background(), "your-workflow-id", "your-signal-name", signal)
if err != nil {
	log.Fatalln("Error sending the Signal", err)
	return
}
```

### Send an Update {/* #send-update-from-client */}

An Update is a synchronous, blocking call that can change Workflow state, control its flow, and return a result.

A Client sending an Update must wait until the Server delivers the Update to a Worker.
Workers must be available and responsive.
Setting a timeout with a context provides a hard limit on how long a client will wait for a response.
If you need a response as soon as the Server receives the request, use a Signal instead.

- `WorkflowExecutionUpdateAccepted` is added to the Event History when the Worker confirms that the Update passed validation.
- `WorkflowExecutionUpdateCompleted` is added to the Event History when the Worker confirms that the Update has finished.

Use the [`Client.UpdateWorkflow`](https://pkg.go.dev/go.temporal.io/sdk/client#Client.UpdateWorkflow) API to send an Update to a Workflow Execution.

You must provide the Workflow Id, but specifying a Run Id is optional.
