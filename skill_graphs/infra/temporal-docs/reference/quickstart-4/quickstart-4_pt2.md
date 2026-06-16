
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

## Child Workflows - PHP SDK

## How to start a Child Workflow Execution {/* #child-workflows */}

A [Child Workflow Execution](/child-workflows) is a Workflow Execution that is scheduled from within another Workflow using a Child Workflow API.

When using a Child Workflow API, Child Workflow related Events ([StartChildWorkflowExecutionInitiated](/references/events#startchildworkflowexecutioninitiated), [ChildWorkflowExecutionStarted](/references/events#childworkflowexecutionstarted), [ChildWorkflowExecutionCompleted](/references/events#childworkflowexecutioncompleted), etc...) are logged in the Workflow Execution Event History.

The [ChildWorkflowExecutionStarted](/references/events#childworkflowexecutionstarted) Event must be logged to the Event History before the Parent Workflow completes to ensure the Child Workflow has started.
In PHP, yielding `$child->start()` or `Workflow::executeChildWorkflow()` internally waits for this Event before returning, so the Child Workflow is guaranteed to have started once the yield resolves.
See the [Parent Close Policy](#parent-close-policy) section below for an example.

Besides Activities, a Workflow can also start other Workflows.

`Workflow::executeChildWorkflow` and `Workflow::newChildWorkflowStub` enables the scheduling of other Workflows from within a Workflow's implementation.
The parent Workflow has the ability to monitor and impact the lifecycle of the Child Workflow, similar to the way it does for an Activity that it invoked.

```php
// Use one stub per child workflow run
$child = Workflow::newChildWorkflowStub(
    ChildWorkflowInterface::class,
    ChildWorkflowOptions::new()
        // Do not specify WorkflowId if you want Temporal to generate a unique Id
        // for the child execution.
        ->withWorkflowId('BID-SIMPLE-CHILD-WORKFLOW')
        ->withExecutionStartToCloseTimeout(DateInterval::createFromDateString('30 minutes'))
);

// This is a non blocking call that returns immediately.
// Use yield $child->workflowMethod(name) to call synchronously.
$promise = $child->workflowMethod('value');

// Do something else here.
try{
    $value = yield $promise;
} catch(TemporalException $e) {
    $logger->error('child workflow failed');
    throw $e;
}
```

Let's take a look at each component of this call.

Before calling `$child->workflowMethod()`, you must configure `ChildWorkflowOptions` for the invocation.
These options customize various execution timeouts, and are passed into the Workflow stub defined by the `Workflow::newChildWorkflowStub`.
Once stub created you can invoke its Workflow method based on attribute `WorkflowMethod`.

The method call returns immediately and returns a `Promise`.
This allows you to execute more code without having to wait for the scheduled Workflow to complete.

When you are ready to process the results of the Workflow, call the `yield $promise` method on the returned promise object.

When a parent Workflow is cancelled by the user, the Child Workflow can be cancelled or abandoned based on a configurable child policy.

You can also skip the stub part of Child Workflow initiation and use `Workflow::executeChildWorkflow` directly:

```php
// Use one stub per child workflow run
$childResult = yield Workflow::executeChildWorkflow(
    'ChildWorkflowName',
    ['args'],
    ChildWorkflowOptions::new()->withWorkflowId('BID-SIMPLE-CHILD-WORKFLOW'),
    Type::TYPE_STRING // optional: defines the return type
);
```

#### How to set a Parent Close Policy {/* #parent-close-policy */}

A [Parent Close Policy](/parent-close-policy) determines what happens to a Child Workflow Execution if its Parent changes to a Closed status (Completed, Failed, or Timed Out).

The default Parent Close Policy option is set to terminate the Child Workflow Execution.

In PHP, a [Parent Close Policy](/parent-close-policy) is set via the `ChildWorkflowOptions` object and `withParentClosePolicy()` method.
The possible values can be obtained from the [`ParentClosePolicy`](https://github.com/temporalio/sdk-php/blob/master/src/Workflow/ParentClosePolicy.php) class.

- `POLICY_TERMINATE`
- `POLICY_ABANDON`
- `POLICY_REQUEST_CANCEL`

Then `ChildWorkflowOptions` object is used to create a new Child Workflow object:

```php
$child = Workflow::newUntypedChildWorkflowStub(
    'child-workflow',
    ChildWorkflowOptions::new()
        ->withParentClosePolicy(ParentClosePolicy::POLICY_ABANDON)
);

yield $child->start();
```

In the snippet above we:

1. Create a new untyped Child Workflow stub with `Workflow::newUntypedChildWorkflowStub`.
2. Provide `ChildWorkflowOptions` object with Parent Close Policy set to `ParentClosePolicy::POLICY_ABANDON`.
3. Start Child Workflow Execution asynchronously using `yield` and method `start()`.

We need `yield` here to ensure that a Child Workflow Execution starts before the parent closes.

---

## Continue-As-New - PHP SDK

This page answers the following questions for PHP developers:

- [What is Continue-As-New?](#what)
- [How to Continue-As-New?](#how)
- [When is it right to Continue-as-New?](#when)
- [How to test Continue-as-New?](#how-to-test)

## What is Continue-As-New? {/* #what */}

[Continue-As-New](/workflow-execution/continue-as-new) lets a Workflow Execution close successfully and creates a new Workflow Execution.
You can think of it as a checkpoint when your Workflow gets too long or approaches certain scaling limits.

The new Workflow Execution is in the same [chain](/workflow-execution#workflow-execution-chain); it keeps the same Workflow Id but gets a new Run Id and a fresh Event History.
It also receives your Workflow's usual parameters.

## How to Continue-As-New using the PHP SDK {/* #how */}

First, design your Workflow parameters so that you can pass in the "current state" when you Continue-As-New into the next Workflow run.
This state is typically set to `None` for the original caller of the Workflow.

    View the source code
  {' '}
  in the context of the rest of the application code.

```php
final class ClusterManagerInput {
    public function __construct(
        public ?ClusterManagerState $state = null,
        public bool $testContinueAsNew = false,
    ) {}
}

#[Workflow\WorkflowInterface]
interface MessageHandlerWorkflowInterface
{
#[Workflow\WorkflowMethod]
public function run(ClusterManagerInput $input);
}

````
The test hook in the above snippet is covered [below](#how-to-test).

Inside your Workflow, call the [`continueAsNew()`](https://php.temporal.io/classes/Temporal-Workflow.html#method_continueAsNew) function with the same type.
This stops the Workflow right away and starts a new one.

    View the source code
  {' '}
  in the context of the rest of the application code.

```php
Workflow::continueAsNew(
    Workflow::getInfo()->type->name,
    [new ClusterManagerInput($this->state, $input->testContinueAsNew)],
);
````

### Considerations for Workflows with Message Handlers {/* #with-message-handlers */}

If you use Updates or Signals, don't call Continue-as-New from the handlers.
Instead, wait for your handlers to finish in your main Workflow before you run `continueAsNew`.
See the [`allHandlersFinished`](message-passing#wait-for-message-handlers) example for guidance.

## When is it right to Continue-as-New using the PHP SDK? {/* #when */}

Use Continue-as-New when your Workflow might hit [Event History Limits](/workflow-execution/event#event-history).

Temporal tracks your Workflow's progress against these limits to let you know when you should Continue-as-New.
Call `Workflow::getInfo()->shouldContinueAsNew` to check if it's time.

## How to test Continue-as-New using the PHP SDK {/* #how-to-test */}

Testing Workflows that naturally Continue-as-New may be time-consuming and resource-intensive.
Instead, add a test hook to check your Workflow's Continue-as-New behavior faster in automated tests.

For example, when `testContinueAsNew == true`, this sample creates a test-only variable called `$this->maxHistoryLength` and sets it to a small value.
A helper method in the Workflow checks it each time it considers using Continue-as-New:

    View the source code
  {' '}
  in the context of the rest of the application code.

```php
private function shouldContinueAsNew(): bool
{
    if (Workflow::getInfo()->shouldContinueAsNew) {
        return true;
    }

    // This is just for ease-of-testing.  In production, we trust temporal to tell us when to continue as new.
    if ($this->maxHistoryLength !== null && Workflow::getInfo()->historyLength > $this->maxHistoryLength) {
        return true;
    }

    return false;
}
```

---

## Workflows - PHP SDK

![PHP SDK Banner](/img/assets/banner-php-temporal.png)

## Workflows

- [Workflow Basics](/develop/php/workflows/basics)
- [Child Workflows](/develop/php/workflows/child-workflows)
- [Continue-As-New](/develop/php/workflows/continue-as-new)
- [Cancellation](/develop/php/workflows/cancellation)
- [Timeouts](/develop/php/workflows/timeouts)
- [Message Passing](/develop/php/workflows/message-passing)
- [Schedules](/develop/php/workflows/schedules)
- [Timers](/develop/php/workflows/timers)
- [Side effects](/develop/php/workflows/side-effects)
- [Versioning](/develop/php/workflows/versioning)

---

## Workflow message passing - PHP SDK

## How to develop with Signals {/* #signals */}

A [Signal](/sending-messages#sending-signals) is a message sent to a running Workflow Execution.

Signals are defined in your code and handled in your Workflow Definition.
Signals can be sent to Workflow Executions from a Temporal Client or from another Workflow Execution.

### How to define a Signal {/* #define-signal */}

A Signal has a name and can have arguments.

- The name, also called a Signal type, is a string.
- The arguments must be [serializable](/dataconversion).

Workflows can answer synchronous [Queries](/sending-messages#sending-queries) and receive [Signals](/sending-messages#sending-signals).

All interface methods must have one of the following attributes:

- **#[WorkflowMethod]** indicates an entry point to a Workflow.
  It contains parameters that specify timeouts and a Task Queue name.
  Required parameters (such as `executionStartToCloseTimeoutSeconds`) that are not specified through the attribute must be provided at runtime.
- **#[SignalMethod]** indicates a method that reacts to external signals. It must have a `void` return type.
- **#[QueryMethod]** indicates a method that reacts to synchronous query requests. It must have a non `void` return type.

> It is possible (though not recommended for usability reasons) to annotate concrete class implementation.

You can have more than one method with the same attribute (except #[WorkflowMethod]).

For example:

```php
use Temporal\Workflow\WorkflowInterface;
use Temporal\Workflow\WorkflowMethod;
use Temporal\Workflow\SignalMethod;
use Temporal\Workflow\QueryMethod;

#[WorkflowInterface]
interface FileProcessingWorkflow
{
    #[WorkflowMethod]
    public function processFile(Argument $args);

    #[QueryMethod("history")]
    public function getHistory(): array;

    #[QueryMethod("status")]
    public function getStatus(): string;

    #[SignalMethod]
    public function retryNow(): void;

    #[SignalMethod]
    public function abandon(): void;
}
```

Note that name parameter of Workflow method attributes can be used to specify name of Workflow, Signal and Query types.
If name is not specified the short name of the Workflow interface is used.

In the preceding code the `#[WorkflowMethod(name)]` is not specified, thus the Workflow Type defaults to `"FileProcessingWorkflow"`.

### How to handle a Signal {/* #handle-signal */}

Workflows listen for Signals by the Signal's name.

Use the `#[SignalMethod]` attribute to handle Signals in the Workflow interface:

```php
use Temporal\Workflow;

#[Workflow\WorkflowInterface]
class YourWorkflow
{
    private bool $value;

    #[Workflow\WorkflowMethod]
    public function run()
    {
        yield Workflow::await(fn()=> $this->value);
        return 'OK';
    }

    #[Workflow\SignalMethod]
    public function setValue(bool $value)
    {
        $this->value = $value;
    }
}
```

In the preceding example, the Workflow updates the protected value.
The main Workflow coroutine waits for the value to change by using the `Workflow::await()` function.

### How to send a Signal from a Temporal Client {/* #send-signal-from-client */}

When a Signal is sent successfully from the Temporal Client, the [WorkflowExecutionSignaled](/references/events#workflowexecutionsignaled) Event appears in the Event History of the Workflow that receives the Signal.

To send a Signal to a Workflow Execution from a Client, call the Signal method, annotated with `#[SignalMethod]` in the Workflow interface, from the Client code.

To send a Signal to a Workflow, use `WorkflowClient->newWorkflowStub` or `WorkflowClient->newUntypedWorkflowStub`:

```php
$workflow = $workflowClient->newWorkflowStub(YourWorkflow::class);

$run = $workflowClient->start($workflow);

// do something

$workflow->setValue(true);

assert($run->getValue() === true);
```

Use `WorkflowClient->newRunningWorkflowStub` or `WorkflowClient->newUntypedRunningWorkflowStub` with Workflow Id to send Signals to already running Workflows.

```php
$workflow = $workflowClient->newRunningWorkflowStub(YourWorkflow::class, 'workflowID');
$workflow->setValue(true);
```

See [Handle Signal](#handle-signal) for details on how to handle Signals in a Workflow.

### How to send a Signal from a Workflow {/* #send-signal-from-workflow */}

A Workflow can send a Signal to another Workflow, in which case it's called an _External Signal_.

When an External Signal is sent:

- A [SignalExternalWorkflowExecutionInitiated](/references/events#signalexternalworkflowexecutioninitiated) Event appears in the sender's Event History.
- A [WorkflowExecutionSignaled](/references/events#workflowexecutionsignaled) Event appears in the recipient's Event History.

To send Signal to a Workflow use `WorkflowClient`->`newWorkflowStub` or `WorkflowClient`->`newUntypedWorkflowStub`:

```php
$workflow = $workflowClient->newWorkflowStub(YourWorkflow::class);

$run = $workflowClient->start($workflow);

// do something

$workflow->setValue(true);

assert($run->getValue() === true);
```

Use `WorkflowClient`->`newRunningWorkflowStub` or `WorkflowClient->newUntypedRunningWorkflowStub` with Workflow Id to send
Signals to a running Workflow.

```php
$workflow = $workflowClient->newRunningWorkflowStub(YourWorkflow::class, 'workflowID');
$workflow->setValue(true);
```

### How to Signal-With-Start {/* #signal-with-start */}

Signal-With-Start is used from the Client.
It takes a Workflow Id, Workflow arguments, a Signal name, and Signal arguments.

If there's a Workflow running with the given Workflow Id, it will be signaled. If there isn't, a new Workflow will be started and immediately signaled.

In cases where you may not know if a Workflow is running, and want to send a Signal to it, use `startwithSignal`.
If a running Workflow exists, the `startwithSignal` API sends the Signal.
If there is no running Workflow, the API starts a new Workflow Run and delivers the Signal to it.

```php
$workflow = $workflowClient->newWorkflowStub(YourWorkflow::class);

$run = $workflowClient->startWithSignal(
    $workflow,
    'setValue',
    [true], // signal arguments
    [] // start arguments
);
```

## How to develop with Queries {/* #queries */}

A [Query](/sending-messages#sending-queries) is a synchronous operation that is used to get the state of a Workflow Execution.

### How to define a Query {/* #define-query */}

A Query has a name and can have arguments.

- The name, also called a Query type, is a string.
- The arguments must be [serializable](/dataconversion).

Workflows can answer synchronous [Queries](/sending-messages#sending-queries) and receive [Signals](/sending-messages#sending-signals).

All interface methods must have one of the following attributes:

- **#[WorkflowMethod]** indicates an entry point to a Workflow.
  It contains parameters that specify timeouts and a Task Queue name.
  Required parameters (such as `executionStartToCloseTimeoutSeconds`) that are not specified through the attribute must be provided at runtime.
- **#[SignalMethod]** indicates a method that reacts to external signals. It must have a `void` return type.
- **#[QueryMethod]** indicates a method that reacts to synchronous query requests. It must have a non `void` return type.

> It is possible (though not recommended for usability reasons) to annotate concrete class implementation.

You can have more than one method with the same attribute (except #[WorkflowMethod]).

For example:

```php
use Temporal\Workflow\WorkflowInterface;
use Temporal\Workflow\WorkflowMethod;
use Temporal\Workflow\SignalMethod;
use Temporal\Workflow\QueryMethod;

#[WorkflowInterface]
interface FileProcessingWorkflow
{
    #[WorkflowMethod]
    public function processFile(Argument $args);

    #[QueryMethod("history")]
    public function getHistory(): array;

    #[QueryMethod("status")]
    public function getStatus(): string;

    #[SignalMethod]
    public function retryNow(): void;

    #[SignalMethod]
    public function abandon(): void;
}
```

Note that name parameter of Workflow method attributes can be used to specify name of Workflow, Signal and Query types.
If name is not specified the short name of the Workflow interface is used.

In the preceding code the `#[WorkflowMethod(name)]` is not specified, thus the Workflow Type defaults to `"FileProcessingWorkflow"`.

### How to handle a Query {/* #handle-query */}

Queries are handled by your Workflow.

Don't include any logic that causes [Command](/workflow-execution#command) generation within a Query handler (such as executing Activities).
Including such logic causes unexpected behavior.

You can add custom Query types to handle Queries such as Querying the current state of a
Workflow, or Querying how many Activities the Workflow has completed. To do this, you need to set
up a Query handler using method attribute `QueryMethod` or `Workflow::registerQuery`.

```php
#[Workflow\WorkflowInterface]
class YourWorkflow
{
    #[Workflow\QueryMethod]
    public function getValue()
    {
        return 42;
    }

    #[Workflow\WorkflowMethod]
    public function run()
    {
        // workflow code
    }
}
```

The handler function can receive any number of input parameters, but all input parameters must be
serializable. The following sample code sets up a Query handler that handles the Query type of
`currentState`:

```php
#[Workflow\WorkflowInterface]
class YourWorkflow
{
    private string $currentState;

    #[Workflow\QueryMethod('current_state')]
    public function getCurrentState(): string
    {
        return $this->currentState;
    }

    #[Workflow\WorkflowMethod]
    public function run()
    {
        // Your normal Workflow code begins here, and you update the currentState
        // as the code makes progress.
        $this->currentState = 'waiting timer';
        try{
            yield Workflow::timer(DateInterval::createFromDateString('1 hour'));
        } catch (\Throwable $e) {
            $this->currentState = 'timer failed';
            throw $e;
        }

        $yourActivity = Workflow::newActivityStub(
            YourActivityInterface::class,
            ActivityOptions::new()->withScheduleToStartTimeout(60)
        );

        $this->currentState = 'waiting activity';
        try{
            yield $yourActivity->doSomething('some input');
        } catch (\Throwable $e) {
            $this->currentState = 'activity failed';
            throw $e;
        }

        $this->currentState = 'done';

        return null;
    }
}
```

You can also issue a Query from code using the `QueryWorkflow()` API on a Temporal Client object.

Use `WorkflowStub` to Query Workflow instances from your Client code (can be applied to both running and closed Workflows):

```php
$workflow = $workflowClient->newWorkflowStub(
    YourWorkflow::class,
    WorkflowOptions::new()
);

$workflowClient->start($workflow);

var_dump($workflow->getCurrentState());
sleep(60);
var_dump($workflow->getCurrentState());
```

### How to send a Query {/* #send-query */}

Queries are sent from a Temporal Client.

## How to develop with Updates {/* #updates */}

An [Update](/sending-messages#sending-updates) is an operation that can mutate the state of a Workflow Execution and return a response.

### Define Update {/* #define-update */}

**How to define an Update using the PHP SDK.**

Workflow Updates handlers are methods in your Workflow Definition designed to handle updates.
These updates can be triggered during the lifecycle of a Workflow Execution.

An Update handler has a name, arguments, response, and an optional validator.

- The name, also called an Update type, is a string.
- The arguments and response must be [serializable](/dataconversion).

The [`#[UpdateMethod]`](https://php.temporal.io/classes/Temporal-Workflow-UpdateMethod.html) attribute indicates that the method is used to handle and respond to update requests.

```php
#[UpdateMethod]
public function myUpdate(string $value);
```

### Handle Update {/* #handle-updates */}

**How to handle Updates in a Workflow using the PHP SDK.**

Workflows listen for Update by the Update's name.

Use the `#[UpdateMethod]` attribute to handle Updates in the Workflow interface.
The handler method can accept multiple serializable input parameters, but it's recommended using only a single parameter.
The function can return a [serializable](/dataconversion) value or `void`.

```php
#[WorkflowInterface]
interface FileProcessingWorkflow {
    #[WorkflowMethod]
    #[ReturnType(ProcessResult::class)]
    public function processFile(File $file);

    #[UpdateMethod]
    public function pauseProcessing(): void;
}
```

Update handlers, unlike Query handlers, can change Workflow state.

The Updates type defaults to the name of the method.
To overwrite this default naming and assign a custom Update type, use the `#[UpdateMethod]` attribute with the `name` parameter.

```php
#[WorkflowInterface]
interface FileProcessingWorkflow {
    #[WorkflowMethod]
    public function processFiles(FileList $files);

    #[UpdateMethod(name: 'pause')]
    public function pauseProcessing(): void;
}
```

**Register Update Handler dynamically**

You can register Update handlers dynamically using the `Workflow::registerUpdate()` method.
The third argument is an optional Update validator. The validator function must have the same parameters as the handler and throw an exception if the validation fails.

```php
Workflow::registerUpdate(
    name: 'pause',
    handler: fn() => $this->paused = true,
    validator: fn() => $this->paused === false or throw new \Exception('Workflow is already paused'),
);
```

### Validate Update {/* #validate-an-update */}

**How to validate Updates in a Workflow using the PHP SDK.**

Validate certain aspects of the data sent to the Workflow using an Update Validator method. For instance, a counter Workflow might never want to accept a non-positive number. Use the [`#[UpdateValidatorMethod]`](https://php.temporal.io/classes/Temporal-Workflow-UpdateValidatorMethod.html) attribute and set the `forUpdate` argument to the name of your Update handler. Your Update Validator should accept the same input parameters as your Update Handler and return `void`.

```php
#[WorkflowInterface]
interface GreetingWorkflow {
    #[WorkflowMethod]
    public function getGreetings(): array;

    #[UpdateMethod]
    public function addGreeting(string $name): int;

    #[UpdateValidatorMethod(forUpdate: 'addGreeting')]
    public function addGreetingValidator(string $name): void;
}
```

### Send Update from a Client {/* #send-update-from-client */}

**How to send an Update to a Workflow Execution from a Temporal Client using the PHP SDK.**

To send an Update to a Workflow Execution from a Client, call the Update method, annotated with `#[UpdateMethod]` in the Workflow interface, from the Client code.

In the following Client code example, start the Workflow `getGreetings` and call the Update method `addGreeting` that is handled in the Workflow.

```php
// Create a typed Workflow stub for GreetingsWorkflow
$workflow = $workflowClient->newWorkflowStub(GreetingWorkflow::class, $workflowOptions);

// Start the Workflow
$run = $workflowClient->start($workflow);

// Send an update to the Workflow. addGreeting returns
// the number of greetings our workflow has received.
$count = $workflow->addGreeting("World");
```

**Async accept**
