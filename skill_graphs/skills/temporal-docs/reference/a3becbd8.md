
In Workflow Update methods, all Workflow features are available, such as executing Activities and child Workflows, and waiting on timers/conditions.
In cases where it's known that the update will take a long time to execute, or you are not interested in the outcome of its execution, you can use the stub method [`startUpdate`](https://php.temporal.io/classes/Temporal-Client-WorkflowStubInterface.html#method_startUpdate) and move on immediately after receiving the validation result.
Note that the processing Workflow Worker must be available.
Otherwise, the request may block indefinitely or fail due to a timeout.

```php
use Ramsey\Uuid\UuidInterface;
use Temporal\Client\Update\UpdateOptions;
use Temporal\Client\Update\WaitPolicy;
use Temporal\Client\Update\LifecycleStage;

// Create an untyped Workflow stub for GreetingsWorkflow
$stub = $client->newUntypedWorkflowStub('GreetingWorkflow', $workflowOptions);

// Start the Workflow
$run = $client->start($stub);

// Send an Update to the Workflow. UpdateHandle returns
$handle = $stub->startUpdate('addGreeting', 'World');

// Use the UpdateHandle to get the Update result with timeout 2.5 seconds
$result = $handle->getResult(timeout: 2.5);

// You can get more control using UpdateOptions
$resultUuid = $stub->startUpdate(
    UpdateOptions::new('storeGreetings', LifecycleStage::StageCompleted)
        ->withResultType(UuidInterface::class)
 )->getResult();
```

#### Update-With-Start {/* #update-with-start */}

[Update-with-Start](/sending-messages#update-with-start) lets you [send an Update](#send-update-from-client) that checks whether an already-running Workflow with that ID exists:

- If the Workflow exists, the Update is processed.
- If the Workflow does not exist, a new Workflow Execution is started with the given ID, and the Update is processed before the main Workflow method starts to execute.

You can:

- Use the [`updateWithStart`](https://php.temporal.io/classes/Temporal-Client-WorkflowClientInterface.html#method_updateWithStart) WorkflowClient API.
  It returns once the requested Update wait stage has been reached; or when the request times out.
- Use the [`UpdateHandle`](https://php.temporal.io/classes/Temporal-Client-Update-UpdateHandle.html) to retrieve a result from the Update.

You provide:

- A WorkflowStub created from [`WorkflowOptions`](https://php.temporal.io/classes/Temporal-Client-WorkflowOptions.html).
  - The `WorkflowOptions` require a [Workflow Id Conflict Policy](/workflow-execution/workflowid-runid#workflow-id-conflict-policy) to be specified.
  - Choose ["Use Existing"](https://php.temporal.io/classes/Temporal-Common-WorkflowIdConflictPolicy.html#enumcase_UseExisting) and use an idempotent Update handler to ensure your code can be executed again in case of a Client failure.
    Not all `WorkflowOptions` are allowed.
    For example, specifying a Cron Schedule will result in an error.

- Update name or [`UpdateOptions`](https://php.temporal.io/classes/Temporal-Client-Update-UpdateOptions.html).
  This mirrors the approach used for [Update Workflow](#send-update-from-client).
  - For Update-with-Start, the Workflow Id is optional.
  - When specified, the Id must match the one used in `WorkflowOptions`.
  - Since a running Workflow Execution may not already exist, you can't set a Run Id.

For example:

```php
$stub = $workflowClient->newUntypedWorkflowStub(
    ShoppingCartWorkflow::class,
    WorkflowOptions::new()
        ->withTaskQueue('service-queue')
        ->withWorkflowId($cartId)
        ->withWorkflowIdConflictPolicy(WorkflowIdConflictPolicy::UseExisting),
);
$handle = $workflowClient->updateWithStart(
    workflow: $stub,
    update: 'addItem',
    updateArgs: [$itemId, $quantity],
);

$price = $handle->getResult();
```

To wait on the Update result, run the Update with the wait stage set to [`LifecycleStage::StageCompleted`](https://php.temporal.io/classes/Temporal-Client-Update-LifecycleStage.html#enumcase_StageCompleted).
This returns once the update result is available; or when the API call times out.

For example:

```php
$handle = $workflowClient->updateWithStart(
    workflow: $stub,
    update: UpdateOptions::new('addItem', LifecycleStage::StageCompleted),
    updateArgs: [$itemId, $quantity],
);

assert($handle->hasResult() === true);
$price = $handle->getResult();
```

## Message handler patterns {/* #message-handler-patterns */}

This section covers common write operations, such as Signal and Update handlers.
It doesn't apply to pure read operations, like Queries or Update Validators.

:::tip

For additional information, see [Inject work into the main Workflow](/handling-messages#injecting-work-into-main-workflow), [Ensuring your messages are processed exactly once](/handling-messages#exactly-once-message-processing), and [this sample](https://github.com/temporalio/samples-php/tree/master/app/src/SafeMessageHandlers) demonstrating safe `async` message handling.
:::

### Add wait conditions to block

Sometimes, async Signal or Update handlers need to meet certain conditions before they should continue.
You can use a wait condition ([`Workflow::await()`](https://php.temporal.io/classes/Temporal-Workflow.html#method_await)) to set a function that prevents the code from proceeding until the condition returns `true`.
This is an important feature that helps you control your handler logic.

Here are two important use cases for `Workflow::await()`:

- Waiting in a handler until it is appropriate to continue.
- Waiting in the main Workflow until all active handlers have finished.

The condition state you're waiting for can be updated by and reflect any part of the Workflow code.
This includes the main Workflow method, other handlers, or child coroutines spawned by the main Workflow method (see [`Workflow::async()`](https://php.temporal.io/classes/Temporal-Workflow.html#method_async).

### Use wait conditions in handlers

It's common to use a Workflow wait condition to wait until a handler should start.
You can also use wait conditions anywhere else in the handler to wait for a specific condition to become `true`.
This allows you to write handlers that pause at multiple points, each time waiting for a required condition to become `true`.

Consider a `readyForUpdateToExecute` method that runs before your Update handler executes.
The `Workflow::await` method waits until your condition is met:

```php
    #[UpdateMethod]
    public function myUpdate(UpdateInput $input)
    {
        yield Workflow::await(
            fn() => $this->readyForUpdateToExecute($input),
        );

        // ...
    }
```

Remember: Handlers can execute before the main Workflow method starts.

### Ensure your handlers finish before the Workflow completes {/* #wait-for-message-handlers */}

Workflow wait conditions can ensure your handler completes before a Workflow finishes.
When your Workflow uses async Signal or Update handlers, your main Workflow method can return or continue-as-new while a handler is still waiting on an async task, such as an Activity result.
The Workflow completing may interrupt the handler before it finishes crucial work and cause client errors when trying retrieve Update results.
Use [`Workflow::await()`](https://php.temporal.io/classes/Temporal-Workflow.html#method_await) and [`Workflow::allHandlersFinished()`](https://php.temporal.io/classes/Temporal-Workflow.html#method_allHandlersFinished) to address this problem and allow your Workflow to end smoothly:

```php
#[WorkflowInterface]
class MyWorkflow
{
    #[WorkflowMethod]
    public function run()
    {
        // ...
        yield Workflow::await(fn() => Workflow::allHandlersFinished());
        return "workflow-result";
    }
}
```

By default, your Worker will log a warning when you allow a Workflow Execution to finish with unfinished handler executions.
You can silence these warnings on a per-handler basis by passing the `unfinishedPolicy` argument to the [`UpdateMethod`](https://php.temporal.io/classes/Temporal-Workflow-UpdateMethod.html) / [`SignalMethod`](https://php.temporal.io/classes/Temporal-Workflow-SignalMethod.html) attribute:

```php
#[UpdateMethod(unfinishedPolicy: HandlerUnfinishedPolicy::Abandon)]
public function myUpdate()
{
    // ...
}
```

See [Finishing handlers before the Workflow completes](/handling-messages#finishing-message-handlers) for more information.

### Use `#[WorkflowInit]` to operate on Workflow input before any handler executes

Normally, your Workflows constructor won't have any parameters.
However, if you use the `#[WorkflowInit]` attribute on your constructor, you can give it the same [Workflow parameters](/develop/php/workflows/basics#workflow-parameters) as your `#[WorkflowMethod]`.
The SDK will then ensure that your constructor receives the Workflow input arguments that the [Client sent](/develop/php/client/temporal-client#start-workflow-execution).
The Workflow input arguments are also passed to your `#[WorkflowMethod]` method -- that always happens, whether or not you use the `#[WorkflowInit]` attribute.
This is useful if you have message handlers that need access to Workflow input: see [Initializing the Workflow first](/sending-messages).

Here's an example.
Notice that the constructor and `getGreeting` must have the same parameters:

```php
use Temporal\Workflow;

#[Workflow\WorkflowInterface]
class GreetingExample
{
    private readonly string $nameWithTitle;
    private bool $titleHasBeenChecked;

    // Note the attribute is on a public constructor
    #[Workflow\WorkflowInit]
    public function __construct(string $input)
    {
        $this->nameWithTitle = 'Sir ' . $input;
        $this->titleHasBeenChecked = false;
    }

    #[Workflow\WorkflowMethod]
    public function getGreeting(string $input)
    {
        yield Workflow::await(fn() => $this->titleHasBeenChecked);
        return "Hello " . $this->nameWithTitle;
    }

    #[Workflow\UpdateMethod]
    public function checkTitleValidity()
    {
        // 👉 The handler is now guaranteed to see the workflow input
        // after it has been processed by the constructor.
        $isValid = yield Workflow::executeActivity('activity.checkTitleValidity', [$this->nameWithTitle]);
        $this->titleHasBeenChecked = true;
        return $isValid;
    }
}
```

:::note

By default, the Workflow Handler runs before Signals and Updates in PHP SDK v2. This behavior is incorrect.
To avoid breaking already written Workflows, since PHP SDK v2.11.0, a [feature flag](https://php.temporal.io/classes/Temporal-Worker-FeatureFlags.html#property_workflowDeferredHandlerStart) was added to enhance the behavior of the Workflow Handler.
Make sure to set this flag to `true` to enable the correct behavior.

:::

### Use `Mutex` to prevent concurrent handler execution {/* #control-handler-concurrency */}

Concurrent processes can interact in unpredictable ways.
Incorrectly written [concurrent message-passing](/handling-messages#message-handler-concurrency) code may not work correctly when multiple handler instances run simultaneously.
Here's an example of a pathological case:

```php
use Temporal\Workflow;

#[Workflow\WorkflowInterface]
class MyWorkflow
{
    // ...

    #[Workflow\SignalMethod]
    public function badAsyncHandler()
    {
        $data = yield Workflow::executeActivity(
            type: 'fetch_data',
            args: ['url' => 'http://example.com'],
            options: ActivityOptions::new()->withStartToCloseTimeout('10 seconds'),
        );
        $this->x = $data->x;
        # 🐛🐛 Bug!! If multiple instances of this handler are executing concurrently, then
        # there may be times when the Workflow has $this->x from one Activity execution and $this->y from another.
        yield Workflow::timer(1);  # or await anything else
        $this->y = $data->y;
    }
}
```

Coordinating access using `Mutex` corrects this code.
Locking makes sure that only one handler instance can execute a specific section of code at any given time:

```php
use Temporal\Workflow;

#[Workflow\WorkflowInterface]
class MyWorkflow
{
    // ...

    private Workflow\Mutex $mutex;

    public function __construct()
    {
        $this->mutex = new Workflow\Mutex();
    }

    #[Workflow\SignalMethod]
    public function safeAsyncHandler()
    {
        $data = yield Workflow::executeActivity(
            type: 'fetch_data',
            args: ['url' => 'http://example.com'],
            options: ActivityOptions::new()->withStartToCloseTimeout('10 seconds'),
        );
        yield Workflow::runLocked($this->mutex, function () use ($data) {
            $this->x = $data->x;
            # ✅ OK: the scheduler may switch now to a different handler execution, or to the main workflow
            # method, but no other execution of this handler can run until this execution finishes.
            yield Workflow::timer(1);  # or await anything else
            $this->y = $data->y;
        });
    }
```

## Message handler troubleshooting {/* #message-handler-troubleshooting */}

When sending a Signal, Update, or Query to a Workflow, your Client might encounter the following errors:

- **The client can't contact the server**:
  You'll receive a [`ServiceClientException`](https://php.temporal.io/classes/Temporal-Exception-Client-ServiceClientException.html) in case of a server connection error.
  [How to configure RPC Retry Policy](/develop/php/client/temporal-client#configure-rpc-retry-policy)

- **RPC timeout**:
  You'll receive a [`TimeoutException`](https://php.temporal.io/classes/Temporal-Exception-Client-TimeoutException.html) in case of an RPC timeout.
  [How to configure RPC timeout](/develop/php/client/temporal-client#configure-rpc-timeout)

- **The workflow does not exist**:
  You'll receive a [`WorkflowNotFoundException`](https://php.temporal.io/classes/Temporal-Exception-Client-WorkflowNotFoundException.html) exception.

See [Exceptions in message handlers](/handling-messages#exceptions) for a non–PHP-specific discussion of this topic.

### Problems when sending a Signal {/* #signal-problems */}

When using Signal, the only exception that will result from your requests during its execution is `ServiceClientException`.
All handlers may experience additional exceptions during the initial (pre-Worker) part of a handler request lifecycle.

For Queries and Updates, the client waits for a response from the Worker.
If an issue occurs during the handler Execution by the Worker, the client may receive an exception.

### Problems when sending an Update {/* #update-problems */}

When working with Updates, you may encounter these errors:

- **No Workflow Workers are polling the Task Queue**:
  Your request will be retried by the SDK Client indefinitely.
  You can [configure RPC timeout](/develop/php/client/temporal-client#configure-rpc-timeout) to impose a timeout.
  This raises a [`WorkflowUpdateRPCTimeoutOrCanceledException`](https://php.temporal.io/classes/Temporal-Exception-Client-WorkflowUpdateRPCTimeoutOrCanceledException.html).

- **Update failed**: You'll receive a [`WorkflowUpdateException`](https://php.temporal.io/classes/Temporal-Exception-Client-WorkflowUpdateException.html) exception.
  There are two ways this can happen:

  - The Update was rejected by an Update validator defined in the Workflow alongside the Update handler.

  - The Update failed after having been accepted.

Update failures are like [Workflow failures](/references/failures#errors-in-workflows).
Issues that cause a Workflow failure in the main method also cause Update failures in the Update handler.
These might include:

    - A failed Child Workflow
    - A failed Activity (if the Activity retries have been set to a finite number)
    - The Workflow author raising `ApplicationFailure`

- **The handler caused the Workflow Task to fail**:
  A [Workflow Task Failure](/references/failures#errors-in-workflows) causes the server to retry Workflow Tasks indefinitely. What happens to your Update request depends on its stage:
  - If the request hasn't been accepted by the server, you receive a [`WorkflowUpdateException`](https://php.temporal.io/classes/Temporal-Exception-Client-WorkflowUpdateException.html).
  - If the request has been accepted, it is durable.
    Once the Workflow is healthy again after a code deploy, use an [`UpdateHandle`](https://php.temporal.io/classes/Temporal-Client-Update-UpdateHandle.html) to fetch the Update result.

- **The Workflow finished while the Update handler execution was in progress**:
  You'll receive a [`WorkflowUpdateException`](https://php.temporal.io/classes/Temporal-Exception-Client-WorkflowUpdateException.html).
  This happens if the Workflow finished while the Update handler execution was in progress, for example because

  - The Workflow was canceled or failed.

  - The Workflow completed normally or continued-as-new and the Workflow author did not [wait for handlers to be finished](/handling-messages#finishing-message-handlers).

### Problems when sending a Query {/* #query-problems */}

When working with Queries, you may encounter these errors:

- **There is no Workflow Worker polling the Task Queue**:
  You'll receive a [`WorkflowNotFoundException`](https://php.temporal.io/classes/Temporal-Exception-Client-WorkflowNotFoundException.html).

- **Query failed**:
  You'll receive a [`WorkflowQueryException`](https://php.temporal.io/classes/Temporal-Exception-Client-WorkflowQueryException.html) if something goes wrong during a Query.
  Any exception in a Query handler will trigger this error.
  This differs from Signal and Update requests, where exceptions can lead to Workflow Task Failure instead.

- **The handler caused the Workflow Task to fail.**
  This would happen, for example, if the Query handler blocks the thread for too long without yielding.

## Dynamic components {/* #dynamic-handler */}

Temporal supports Dynamic Queries, Signals, and Updates.
These are unnamed handlers that are invoked if no other statically defined handler with the given name exists.

Dynamic Handlers provide flexibility to handle cases where the names of Queries, Signals, or Updates aren't known at run time.

:::caution

Dynamic Handlers should be used judiciously as a fallback mechanism rather than the primary approach.
Overusing them can lead to maintainability and debugging issues down the line.

Instead, Signals, or Queries should be defined statically whenever possible, with clear names that indicate their purpose.
Use static definitions as the primary way of structuring your Workflows.

Reserve Dynamic Handlers for cases where the handler names are not known at development time and need to be looked up dynamically at runtime.
They are meant to handle edge cases and act as a catch-all, not as the main way of invoking logic.

:::

### How to set a Dynamic Query {/* #set-a-dynamic-query */}

A Dynamic Query in Temporal is a Query method that is invoked dynamically at runtime if no other Query with the same name is registered.
Use [`Workflow::registerDynamicQuery()`](https://php.temporal.io/classes/Temporal-Workflow.html#method_registerDynamicQuery) to set a dynamic Query handler.

The Query Handler parameters must accept a `string` name and [`ValuesInterface`](https://php.temporal.io/classes/Temporal-DataConverter-ValuesInterface.html) for the arguments.

```php
Workflow::registerDynamicQuery(function (string $name, ValuesInterface $arguments): string {
    return \sprintf(
        'Got query `%s` with %d arguments',
        $name,
        $arguments->count(),
    );
});
```

### How to set a Dynamic Signal {/* #set-a-dynamic-signal */}

A Dynamic Signal in Temporal is a Signal that is invoked dynamically at runtime if no other Signal with the same input is registered.
Use [`Workflow::registerDynamicSignal()`](https://php.temporal.io/classes/Temporal-Workflow.html#method_registerDynamicSignal) to set a dynamic Signal handler.

The Signal Handler parameters must accept a `string` name and [`ValuesInterface`](https://php.temporal.io/classes/Temporal-DataConverter-ValuesInterface.html) for the arguments.

```php
Workflow::registerDynamicSignal(function (string $name, ValuesInterface $arguments): void {
     Workflow::getLogger()->info(\sprintf(
         'Executed signal `%s` with %d arguments',
         $name,
         $arguments->count(),
     ));
 });
```

### How to set a Dynamic Update {/* #set-a-dynamic-update */}

A Dynamic Update in Temporal is an Update that is invoked dynamically at runtime if no other Update with the same input is registered.
Use [`Workflow::registerDynamicUpdate()`](https://php.temporal.io/classes/Temporal-Workflow.html#method_registerDynamicUpdate) to set a dynamic Update handler.

The method accepts two arguments:

- Update Handler
- Update Validator (optional) that should throw an exception if the validation fails

Both the Handler and the Validator must accept a `string` name and [`ValuesInterface`](https://php.temporal.io/classes/Temporal-DataConverter-ValuesInterface.html) for the arguments.

```php
Workflow::registerDynamicUpdate(
    static fn(string $name, ValuesInterface $arguments): string => \sprintf(
        'Got update `%s` with %d arguments',
        $name,
        $arguments->count(),
    ),
    static fn(string $name, ValuesInterface $arguments) => \str_starts_with(
        $name,
        'update_',
    ) or throw new \InvalidArgumentException('Invalid update name'),
);
```

---

## Schedules - PHP SDK

This page shows how to do the following:

- [How to use Start Delay](#start-delay)
- [How to use Temporal Cron Jobs](#temporal-cron-jobs)

## How to use Start Delay {/* #start-delay */}

Use the Workflow [Start Delay](/workflow-execution/timers-delays) functionality if you need to delay the execution of the Workflow without the need for regular launches.
Here you simply specify the time to wait before dispatching the first Workflow task.

```php
$workflow = $workflowClient->newWorkflowStub(
    GreeterWorkflowInterface::class,
    WorkflowOptions::new()
        ->withWorkflowStartDelay(CarbonInterval::minutes(10)),
);
$workflowClient->start($workflow, 'Hello world!');
```

## How to use Temporal Cron Jobs {/* #temporal-cron-jobs */}

:::caution Cron support is not recommended

We recommend using [Schedules](https://docs.temporal.io/schedule) instead of Cron Jobs.
Schedules were built to provide a better developer experience, including more configuration options and the ability to update or pause running Schedules.

:::

A [Temporal Cron Job](/cron-job) is the series of Workflow Executions that occur when a Cron Schedule is provided in the call to spawn a Workflow Execution.

A Cron Schedule is provided as an option when the call to spawn a Workflow Execution is made.

Set your Cron Schedule with `CronSchedule('* * * * *')`.
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

The following example sets a Cron Schedule in PHP:

```php
  $workflow = $this->workflowClient->newWorkflowStub(
      CronWorkflowInterface::class,
      WorkflowOptions::new()
          ->withWorkflowId(CronWorkflowInterface::WORKFLOW_ID)
          ->withCronSchedule('* * * * *')
          // Execution timeout limits total time. Cron will stop executing after this timeout.
          ->withWorkflowExecutionTimeout(CarbonInterval::minutes(10))
          // Run timeout limits duration of a single workflow invocation.
          ->withWorkflowRunTimeout(CarbonInterval::minute(1))
  );

  $output->writeln("Starting <comment>CronWorkflow</comment>... ");

  try {
      $run = $this->workflowClient->start($workflow, 'Antony');
      // ...
  }
```

Setting `withCronSchedule` turns the Workflow Execution into a Temporal Cron Job.
For more information, see the [PHP samples](https://github.com/temporalio/samples-php/tree/master/app/src/Cron) for example code or the PHP SDK `WorkflowOptions` [source code](https://github.com/temporalio/sdk-php/blob/master/src/Client/WorkflowOptions.php).

:::tip Schedule Auto-Deletion

Once a Schedule has completed creating all its Workflow Executions, the Temporal Service deletes it since it won’t fire again.
The Temporal Service doesn't guarantee when this removal will happen.

:::

---

## Side Effects - PHP SDK

## How to use Side Effects in PHP {/* #side-effects */}

Side Effects are used to execute non-deterministic code, such as generating a UUID or a random number, without compromising determinism in the Workflow. This is done by storing the results of the Side Effect into the Workflow [Event History](/workflow-execution/event#event-history).

A Side Effect doesn't re-execute during a Replay. Instead, it returns the recorded result from the Workflow Execution Event History.

Side Effects shouldn't fail. An exception that is thrown from the Side Effect causes failure and retry of the current Workflow Task.

An Activity or a Local Activity can also be used instead of a Side Effect, as its results are also persisted in Workflow Execution History.

:::note

You shouldn't modify the Workflow state inside a Side Effect, because they're not re-executed during Replay. Side Effect functions should only return a value, and that value can be used in Workflow code to alter state.
