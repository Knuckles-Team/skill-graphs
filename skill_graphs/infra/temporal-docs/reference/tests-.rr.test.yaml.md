# tests/.rr.test.yaml
kv:
  test:
    driver: memory
    config:
      interval: 10
```

If you want to be able to mock Activities, use `WorkerFactory` from the `Temporal\Testing` Namespace
in your PHP Worker:

```php
// worker.test.php
use Temporal\Testing\WorkerFactory;

$factory = WorkerFactory::create();
$worker = $factory->newWorker();

$worker->registerWorkflowTypes(MyWorkflow::class);
$worker->registerActivity(MyActivity::class);
$factory->run();
```

Then, in your tests to mock an Activity, use the`ActivityMocker` class.

Assume we have the following Activity:

```php
#[ActivityInterface(prefix: "SimpleActivity.")]
interface SimpleActivityInterface
{
    #[ActivityMethod('doSomething')]
    public function doSomething(string $input): string;
```

To mock it in the test, you can do this:

```php
final class SimpleWorkflowTestCase extends TestCase
{
    private WorkflowClient $workflowClient;
    private ActivityMocker $activityMocks;

    protected function setUp(): void
    {
        $this->workflowClient = new WorkflowClient(ServiceClient::create('localhost:7233'));
        $this->activityMocks = new ActivityMocker();

        parent::setUp();
    }

    protected function tearDown(): void
    {
        $this->activityMocks->clear();
        parent::tearDown();
    }

    public function testWorkflowReturnsUpperCasedInput(): void
    {
        $this->activityMocks->expectCompletion('SimpleActivity.doSomething', 'world');
        $workflow = $this->workflowClient->newWorkflowStub(SimpleWorkflow::class);
        $run = $this->workflowClient->start($workflow, 'hello');
        $this->assertSame('world', $run->getResult('string'));
    }
}
```

In the preceding test case, we do the following:

1. Instantiate `ActivityMocker` in the `setUp()` method of the test.
2. Clear the cache after each test in `tearDown()`.
3. Mock an Activity call to return a string `world`.

To mock a failure, use the `expectFailure()` method:

```php
$this->activityMocks->expectFailure('SimpleActivity.echo', new \LogicException('something went wrong'));
```

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

1. In the `tests` folder, create `bootstrap.php` with the following contents:

```php
declare(strict_types=1);

require __DIR__ . '/../vendor/autoload.php';

use Temporal\Testing\Environment;

$environment = Environment::create();
$environment->start();
register_shutdown_function(fn () => $environment->stop());
```

If you don't want to run the test server with all of your tests, you can add a condition to start a test only if the `RUN_TEMPORAL_TEST_SERVER` environment variable is present:

```php
if (getenv('RUN_TEMPORAL_TEST_SERVER') !== false) {
    $environment = Environment::create();
    $environment->start('./rr serve -c .rr.silent.yaml --workflow-id tests');
    register_shutdown_function(fn() => $environment->stop());
}
```

2. Add `bootstrap.php` and the `TEMPORAL_ADDRESS` environment variable to `phpunit.xml`:

```xml
<phpunit xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:noNamespaceSchemaLocation="https://schema.phpunit.de/9.3/phpunit.xsd"
         bootstrap="tests/bootstrap.php"
>
    <php>
        <env name="TEMPORAL_ADDRESS" value="127.0.0.1:7233" />
    </php>
</phpunit>
```

3. Add the test server executable to `.gitignore`:

```gitignore
temporal-test-server
```

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

To replay Workflow Executions, use the `\Temporal\Testing\Replay\WorkflowReplayer` class.

In the following example, Event Histories are fetching from the Temporal, and then replayed.
If the Workflow is non-deterministic, a `NonDeterministicWorkflowException` will be thrown.
Note that this requires [Advanced Visibility](/visibility#advanced-visibility) to be enabled.

```php
/**
 * We assume you already have a WorkflowClient and WorkflowReplayer in scope.
 * @var \Temporal\Client\WorkflowClientInterface $workflowClient
 * @var \Temporal\Testing\Replay\WorkflowReplayer $replayer
 */

// Find all workflow executions of type "MyWorkflow" and task queue "MyTaskQueue".
$executions = $workflowClient->listWorkflowExecutions(
    "WorkflowType='MyWorkflow' AND TaskQueue='MyTaskQueue'"
);

// Replay each workflow execution.
foreach ($executions as $executionInfo) {
    try {
        $replayer->replayFromServer(
            workflowType: $executionInfo->type->name,
            execution: $executionInfo->execution,
        );
    } catch (\Temporal\Testing\Replay\Exception\ReplayerException $e) {
        // Handle a replay error.
    }
}
```

In the next example, an Event History is loaded from a JSON file, and the maximum number of replayed Events is limited to 42.

```php
$replayer->replayFromJSON(
    workflowType: 'MyWorkflow',
    path: 'history.json',
    lastEventId: 42,  // optional
);
```

You can download a Event History using PHP, and then replay it from a memorized History object:

```php
$history = $this->workflowClient->getWorkflowHistory(
    execution: $run->getExecution(),
)->getHistory();

(new WorkflowReplayer())->replayHistory($history);
```

---

## Client - PHP SDK

![PHP SDK Banner](/img/assets/banner-php-temporal.png)

## Temporal Client

- [Temporal Client](/develop/php/client/temporal-client)

---

## Temporal Client - PHP SDK

This guide introduces Temporal Clients.
It explains the role and use of Clients and shows you how to configure your PHP Client code to connect to the Temporal Service.

This page shows how to do the following:

- [Connect to a local development Temporal Service](#connect-to-a-dev-cluster)
- [Connect to Temporal Cloud](#connect-to-temporal-cloud)
- [Start a Workflow Execution](#start-workflow-execution)
- [Advanced connection options](#advanced-connection-options)

## How to connect a Temporal Client to a Temporal Service {/* #connect-to-a-dev-cluster */}

A [Temporal Client](/encyclopedia/temporal-sdks#temporal-client) enables you to communicate with the [Temporal Service](/temporal-service).
Communication with a Temporal Service includes, but isn't limited to, the following:

- Scheduling Workflow Executions.
- Starting Workflow Executions.
- Sending Signals to Workflow Executions.
- Sending Queries to Workflow Executions.
- Sending Updates to Workflow Executions.
- Getting the results of a Workflow Execution.
- Providing an Activity Task Token.

:::caution

A Temporal Client cannot be initialized and used inside a Workflow.
However, it is acceptable and common to use a Temporal Client inside an Activity to communicate with a Temporal Service.

:::

When you are running a Temporal Service locally (such as the [Temporal CLI](https://docs.temporal.io/cli/command-reference/server#start-dev)), the number of connection options you must provide is minimal.
Many SDKs default to `127.0.0.1:7233`.

In the PHP SDK, different client classes are responsible for different functional areas.
The [`ServiceClient`](https://php.temporal.io/classes/Temporal-Client-GRPC-ServiceClient.html) is responsible for the low-level API and connection to the Temporal Service.
It is also used in higher-level clients: [`WorkflowClient`](https://php.temporal.io/classes/Temporal-Client-WorkflowClient.html) and [`ScheduleClient`](https://php.temporal.io/classes/Temporal-Client-ScheduleClient.html).

:::note

RoadRunner is not required to work only with the client API; however, the [gRPC extension](https://pecl.php.net/package/grpc) is necessary.

:::

Use `create()` factory methods to create clients.

```php
use Temporal\Client\GRPC\ServiceClient;
use Temporal\Client\WorkflowClient;

$serviceClient = ServiceClient::create('localhost:7233');
$workflowClient = WorkflowClient::create($serviceClient);

// Use $workflowClient to work with Workflows ...
```

See the [Advanced connection options](#advanced-connection-options) section for more information on configuring the connection.

## How to connect a Temporal Client to a Temporal Cloud {/* #connect-to-temporal-cloud */}

When you connect to [Temporal Cloud](/cloud), you need to provide additional connection and client options that include the following:

- The [Temporal Cloud Namespace Id](/cloud/namespaces#temporal-cloud-namespace-id).
- The [Namespace's gRPC endpoint](/cloud/namespaces#temporal-cloud-grpc-endpoint).
  An endpoint listing is available at the [Temporal Cloud Website](https://cloud.temporal.io/namespaces) on each Namespace detail page.
  The endpoint contains the Namespace Id and port.
- mTLS CA certificate.
- mTLS private key.

For more information about managing and generating client certificates for Temporal Cloud, see [How to manage certificates in Temporal Cloud](/cloud/certificates).

For more information about configuring TLS to secure inter- and intra-network communication for a Temporal Service, see [Temporal Customization Samples](https://github.com/temporalio/samples-server).

Use the [`ServiceClient::createSSL()`](https://php.temporal.io/classes/Temporal-Client-GRPC-BaseClient.html#method_createSSL) method to configure a client connection to the Temporal Service.
The `$clientKey` argument must be combined with the `$clientPem` to authenticate the Client.

```php
use Temporal\Client\ClientOptions;
use Temporal\Client\GRPC\ServiceClient;
use Temporal\Client\WorkflowClient;

$serviceClient = \Temporal\Client\GRPC\ServiceClient::createSSL(
    address: '<your-custom-namespace>.tmprl.cloud:7233',
    // crt: 'certs/server-root-ca-cert.pem', # ROOT CA to validate the server cert
    clientKey: 'certs/client-private-key.pem',
    clientPem: 'certs/client-cert.pem',
    // overrideServerName: 'tls-sample',
);

$workflowClient = WorkflowClient::create(
    serviceClient: $serviceClient,
    options: (new ClientOptions())
        ->withNamespace('<your-custom-namespace>.<id>'),
);
```

To [run Worker processes](/develop/php/workers/run-worker-process#run-a-dev-worker) managed by Temporal Cloud, configure RoadRunner in the same way.

```yml
temporal:
  # ...
  tls:
    # root_ca: 'certs/server-root-ca-cert.pem'
    key: 'certs/client-private-key.pem'
    cert: 'certs/client-cert.pem'
    client_auth_type: require_and_verify_client_cert
    # server_name: 'tls-sample'
```

To set up the [API key](/cloud/api-keys) in the Client, use the [`ServiceClient::withAuthKey()`](https://php.temporal.io/classes/Temporal-Client-GRPC-BaseClient.html#method_withAuthKey) method:

```php
$serviceClient = \Temporal\Client\GRPC\ServiceClient::createSSL(/*...*/)
    ->withAuthKey('your-api-key');
```

## How to start a Workflow Execution {/* #start-workflow-execution */}

[Workflow Execution](/workflow-execution) semantics rely on several parameters—that is, to start a Workflow Execution you must supply a Task Queue that will be used for the Tasks (one that a Worker is polling), the Workflow Type, language-specific contextual data, and Workflow Function parameters.

In the examples following all Workflow Executions are started using a Temporal Client.
To spawn Workflow Executions from within another Workflow Execution, use either the [Child Workflow](/develop/php/workflows/child-workflows) or External Workflow APIs.

See the [Customize Workflow Type](/develop/php/workflows/basics#workflow-type) section to see how to customize the name of the Workflow Type.

A request to spawn a Workflow Execution causes the Temporal Service to create the first Event ([WorkflowExecutionStarted](/references/events#workflowexecutionstarted)) in the Workflow Execution Event History.
The Temporal Service then creates the first Workflow Task, resulting in the first [WorkflowTaskScheduled](/references/events#workflowtaskscheduled) Event.

Use Workflow stub to start a Workflow Execution from within a Client.
Workflow stub is a proxy generated by the [`WorkflowClient`](https://php.temporal.io/classes/Temporal-Client-WorkflowClient.html).
You can use a typed or untyped Workflow stub in the client code.

- Typed Workflow stubs are useful because they are type safe and allow you to invoke your Workflow methods such as `#[WorkflowMethod]`, `#[QueryMethod]`, `#[SignalMethod]`, and `#[UpdateMethod]` directly.
- An untyped Workflow stub does not use a Workflow interface. It is more flexible because it has methods from the [`WorkflowStubInterface`](https://php.temporal.io/classes/Temporal-Client-WorkflowStubInterface.html), such as `start`, `signal`, `getResults`, `query`, `signal`, `update`, `cancel`, `terminate`, etc.
  When using untyped Workflow stub, we rely on the Workflow Type, Activity Type, Child Workflow Type, as well as Query and Signal names.

For example, there is a Workflow defined as follows:

```php
#[WorkflowInterface]
interface AccountTransferWorkflowInterface
{
    #[WorkflowMethod(name: "account.transfer")]
    public function begin(UuidInterface $transactionId);

    #[UpdateMethod(name: "pay")]
    public function move(UuidInterface $from, UuidInterface $to, int $amount);

    #[UpdateMethod(name: "finish")]
    public function commit();

    #[UpdateMethod(name: "cancel")]
    public function rollback(string $reason);
}
```

In case of a **typed** Workflow stub, you can use the `AccountTransferWorkflowInterface` to call the Workflow methods directly:

```php
$stub = $workflowClient->newWorkflowStub(AccountTransferWorkflowInterface::class);

$workflowClient->start($stub, $transactionId);
$stub->move($from1, $to1, $amount1);
$stub->move($from2, $to2, $amount2);
$stub->commit();
```

In case of an **untyped** Workflow stub, you need to specify Workflow Type and method names explicitly:

```php
$stub = $workflowClient->newUntypedWorkflowStub('account.transfer');

$workflowClient->start($stub, $transactionId);
$stub->update('pay', $from1, $to1, $amount1);
$stub->update('pay', $from2, $to2, $amount2);
$stub->update('finish');
```

A Workflow Execution can be started either synchronously or asynchronously.

**Synchronous start**

A synchronous start initiates a Workflow and then waits for its completion. The started Workflow will not rely on the
invocation process and will continue executing even if the waiting process crashes or stops.

Be sure to acquire the Workflow interface or class name you want to start.
For example:

```php
#[WorkflowInterface]
interface AccountTransferWorkflowInterface
{
    #[WorkflowMethod(name: "MoneyTransfer")]
    #[ReturnType(UuidInterface::class)]
    public function transfer( string $fromAccountId, string $toAccountId, string $referenceId, int $amountCents);
}
```

To start the Workflow in sync mode:

```php
$accountTransfer = $workflowClient->newWorkflowStub(
    AccountTransferWorkflowInterface::class,
);

$result = $accountTransfer->transfer('fromID', 'toID', 'refID', 1000);
```

**Asynchronous start**

An asynchronous start initiates a Workflow Execution and immediately returns to the caller without waiting for a result.
This is the most common way to start Workflows in a live environment.

To start a Workflow asynchronously, pass the Workflow stub instance and start parameters into the [`WorkflowClient::start()`](https://php.temporal.io/classes/Temporal-Client-WorkflowClientInterface.html#method_start) method.

```php
$accountTransfer = $workflowClient->newWorkflowStub(
    AccountTransferWorkflowInterface::class,
);

$run = $this->workflowClient->start($accountTransfer, 'fromID', 'toID', 'refID', 1000);
```

After the Workflow is started, you can receive details about the Workflow Execution or result via the [`WorkflowRun`](https://php.temporal.io/classes/Temporal-Workflow-WorkflowRunInterface.html) object methods:

```php
$run = $workflowClient->start($accountTransfer, 'fromID', 'toID', 'refID', 1000);

// Get the Workflow ID
var_dump($run->getExecution()->getID());

// Describe the Workflow Execution
var_dump($run->describe());

// Wait for the Workflow to complete and get the result with 10-second timeout
var_dump($run->getResult(timeout: 10));
```

**Recurring start**

You can start a Workflow Execution on a regular schedule with [the CronSchedule option](/develop/php/workflows/schedules#temporal-cron-jobs).

### How to set a Workflow's Task Queue {/* #set-task-queue */}

In most SDKs, the only Workflow Option that must be set is the name of the [Task Queue](/task-queue).
When developing in PHP, the Task Queue name defaults to `"default"`.
While setting a meaningful Task Queue name is recommended for better observability, Workflows can be run without setting this option.

:::note

PHP's default is different from most SDKs, which do require an explicit Task Queue name.

:::

For your code to execute, a Worker Process must be running ([how to run Worker Processes](/develop/php/workers/run-worker-process#run-a-dev-worker)).
This process needs a Worker Entity that is polling the same Task Queue name.

Set the Workflow Task Queue with the Workflow stub in the Client code using [`WorkflowOptions::withTaskQueue()`](https://php.temporal.io/classes/Temporal-Client-WorkflowOptions.html#method_withTaskQueue).

```php
$stub = $workflowClient->newWorkflowStub(
    YourWorkflowInterface::class,
    WorkflowOptions::new()
        ->withTaskQueue("Workflow-Task-Queue-1"),
);
```

### How to set a Workflow Id {/* #workflow-id */}

Although it is not required, we recommend providing your own [Workflow Id](/workflow-execution/workflowid-runid#workflow-id)that maps to a business process or business entity identifier, such as an order identifier or customer identifier.

Set the Workflow Id with the Workflow stub in the Client code using [`WorkflowOptions::withTaskQueue()`](https://php.temporal.io/classes/Temporal-Client-WorkflowOptions.html#method_withWorkflowId).

```php
$stub = $workflowClient->newWorkflowStub(
    YourWorkflowInterface::class,
    WorkflowOptions::new()
        ->withWorkflowId("Workflow-Id"),
);
```

### How to get the results of a Workflow Execution {/* #get-workflow-results */}

If the call to start a Workflow Execution is successful, you will gain access to the Workflow Execution's Run Id.

The Workflow Id, Run Id, and Namespace may be used to uniquely identify a Workflow Execution in the system and get its result.

It's possible to both block progress on the result (synchronous execution) or get the result at some other point in time (asynchronous execution).

In the Temporal Platform, it's also acceptable to use Queries as the preferred method for accessing the state and results of Workflow Executions.

If you need to wait for the completion of a Workflow after an asynchronous start, make a blocking call to
the `WorkflowRun::getResult()` method.

```php
$stub = $workflowClient->newWorkflowStub(YourWorkflowInterface::class);
$run = $workflowClient->start($stub, 'fromID', 'toID', 'refID', 1000);

var_dump($run->getResult());
```

In case of untyped Workflow stub, you can use the [`WorkflowStub::getResult()`](https://php.temporal.io/classes/Temporal-Workflow-WorkflowRunInterface.html#method_getResult) method:

```php
$stub = $workflowClient->newUntypedWorkflowStub('account.transfer');
$workflowClient->start($stub, 'fromID', 'toID', 'refID', 1000);

var_dump($stub->getResult(timeout: 5.5));
```

Note that you can specify a timeout for the `getResult()` method in seconds.
If the Workflow does not complete within the specified time, a `TimeoutException` will be thrown.
See how to limit all RPC calls in the [RPC timeout](#configure-rpc-timeout) section.

## Advanced connection options {/* #advanced-connection-options */}

In PHP, it is common practice to work with resources in blocking mode.
Long blocks can quickly exhaust the pool of available workers and lead to application failure.

This section introduces features and configuration examples of the PHP SDK when working with the Temporal Client API.

### Connection

gRPC connections in the PHP SDK are lazy by default, meaning they are not established until the first call.
To force establishing the connection to the Temporal Service, you can call the [`ConnectionInterface::connect()`](https://php.temporal.io/classes/Temporal-Client-GRPC-Connection-ConnectionInterface.html#method_connect) or [`ServiceClient::getServerCapabilities()`](https://php.temporal.io/classes/Temporal-Client-GRPC-ServiceClientInterface.html#method_getServerCapabilities) method.

```php
// ...
$serviceClient->getConnection()->connect(timeout: 10);

// or
$serviceClient->getServerCapabilities();
```

If, for some reason, the established connection is broken, the SDK will automatically attempt to restore it, taking into account the configured retry policy.

### Retry policy {/* #configure-rpc-retry-policy */}

Whenever the client fails to connect to the server, an error with a status code is generated.
If the status code is `UNKNOWN`, `UNAVAILABLE`, or `RESOURCE_EXHAUSTED`, the client will make another connection attempt.
By default, the number of attempts is unlimited, and the interval between them will range from 0.5 to 100 seconds with a backoff coefficient of 2.
This means that the client will likely be blocked until it establishes a connection to the server through infinite attempts.

If you want to change the default behavior, use the `withRetryPolicy()` method when creating a client service:

```php
use Temporal\Client\Common\RpcRetryOptions;
use Temporal\Client\GRPC\ServiceClient;
use Temporal\Client\WorkflowClient;

$serviceClient = ServiceClient::create('localhost:7233');
$workflowClient = WorkflowClient::create($serviceClient)
    ->withRetryOptions(
        RpcRetryOptions::new()
            ->withMaximumAttempts(10)
            ->withInitialInterval('1 second')   // The first retry will be in 1 second
            ->withBackoffCoefficient(2.5)       // Each next retry time will be multiplied by 2.5
            ->withMaximumInterval('20 seconds') // The maximum interval between attempts
            ->withMaximumJitterCoefficient(0.2) // Actual retry time can be +/- 20% of the calculated time
    );
```

### RPC timeout {/* #configure-rpc-timeout */}

When the client calls the service's RPC, there is no default time limit for waiting for a response. This can result in the code call `$result = $workflowHandle->getResult();` blocking the PHP worker until the Workflow completes. In some cases, this is not the desired behavior, and there may be a need to set a reasonable timeout for waiting for the RPC to complete.

Use the `withTimeout()` method to build a client with a timeout for all RPC calls.

```php
use Temporal\Client\GRPC\ServiceClient;
use Temporal\Client\WorkflowClient;

$serviceClient = ServiceClient::create('localhost:7233');
$workflowClient = WorkflowClient::create($serviceClient)
    ->withTimeout(5.75);

// Create a Workflow stub
$stub = $workflowClient->newWorkflowStub(AccountTransferWorkflowInterface::class);

// If the Workflow does not complete within 5.75 seconds, a TimeoutException will be thrown
$result = $stub->transfer('fromID', 'toID', 'refID', 1000);
```

:::note

The `withTimeout()` method is immutable.
If you need to change the timeout for individual operations, create a new client from the existing one with a specific timeout: `$newClient = $workflowClient->withTimeout(0);` (`0` means no timeout).

:::

---

## PHP SDK developer guide

![PHP SDK Banner](/img/assets/banner-php-temporal.png)

## Install and get started

You can find detailed installation instructions for the PHP SDK in the [Quickstart](/develop/php/set-up-your-local-php).

There's also a short walkthrough of how to use the Temporal primitives (Activities, Workflows, and Workers) to build and run a Temporal application to get you up and running.

Once your local Temporal Service is set up, continue building with the following resources:

- [Activity Basics](/develop/php/activities/basics)
- [Workflow Basics](/develop/php/workflows/basics)
- [Start an Activity Execution](/develop/php/activities/execution)
- [Run Worker Processes](/develop/php/workers/run-worker-process)

From there, you can dive deeper into any of the Temporal primitives to start building Workflows that fit your use cases.

## [Workflows](/develop/php/workflows)

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

## [Activities](/develop/php/activities)

- [Activity Basics](/develop/php/activities/basics)
- [Activity Execution](/develop/php/activities/execution)
- [Timeouts](/develop/php/activities/timeouts)
- [Asynchronous Activity Completion](/develop/php/activities/asynchronous-activity)

## [Workers](/develop/php/workers)

- [Run Worker processes](/develop/php/workers/run-worker-process)

## [Temporal Client](/develop/php/client)

- [Temporal Client](/develop/php/client/temporal-client)

## [Platform](/develop/php/platform)

- [Observability](/develop/php/platform/observability)
- [Enriching the UI](/develop/php/platform/enriching-ui)

## [Best practices](/develop/php/best-practices)

- [Testing](/develop/php/best-practices/testing-suite)
- [Debugging](/develop/php/best-practices/debugging)

## Temporal PHP Technical Resources

- [PHP SDK Quickstart - Setup Guide](/develop/php/set-up-your-local-php)
- [PHP API Documentation](https://php.temporal.io)
- [PHP SDK Code Samples](https://github.com/temporalio/samples-php)
- [PHP SDK GitHub](https://github.com/temporalio/sdk-php)

## Get Connected with the Temporal PHP Community

- [Temporal PHP Community Slack](https://temporalio.slack.com/archives/C01LK9FAMM0)
- [PHP SDK Forum](https://community.temporal.io/tag/php-sdk)

---

## Enriching the user interface - PHP SDK

Temporal supports adding context to Workflows and Events with metadata.
This helps users identify and understand Workflows and their operations.

## Adding Summary and Details to Workflows

### Starting a Workflow

When starting a Workflow, you can provide a static summary and details to help identify the Workflow in the UI:

```php
use Temporal\Client\WorkflowClient;
use Temporal\Client\WorkflowOptions;

// Create workflow client
$workflowClient = WorkflowClient::create($serviceClient);

// Start a workflow with static summary and details
$workflow = $workflowClient->newWorkflowStub(
    YourWorkflow::class,
    WorkflowOptions::new()
        ->withWorkflowId('your-workflow-id')
        ->withTaskQueue('your-task-queue')
        ->withStaticSummary('Order processing for customer #12345')
        ->withStaticDetails('Processing premium order with expedited shipping')
);

$result = $workflow->yourWorkflowMethod('workflow input');
```

`withStaticSummary()` sets a single-line description that appears in the Workflow list view, limited to 200 bytes.
`withStaticDetails()` sets multi-line comprehensive information that appears in the Workflow details view, with a larger limit of 20K bytes.

The input format is standard Markdown excluding images, HTML, and scripts.

You can also start a Workflow asynchronously:

```php
// Start workflow asynchronously
$workflowClient->start($workflow, 'workflow input');
```

### Adding Summary to Activities and Timers

You can attach a `summary` to timers within a workflow:

```php
use Temporal\Workflow;
use Temporal\Workflow\TimerOptions;

#[WorkflowInterface]
interface YourWorkflow
{
    #[WorkflowMethod]
    public function yourWorkflowMethod(string $input): string;
}

class YourWorkflowImpl implements YourWorkflow
{
    public function yourWorkflowMethod(string $input): \Generator
    {
        // Create a timer with a summary
        yield Workflow::timer(
            300, // 5 minutes in seconds
            TimerOptions::new()->withSummary('Waiting for payment confirmation')
        );

        return 'Timer completed';
    }
}
```

For Activities, you can set a summary using Activity options:

```php
use Temporal\Activity\ActivityOptions;
use Temporal\Workflow;

class YourWorkflowImpl implements YourWorkflow
{
    private YourActivitiesInterface $activities;

    public function __construct()
    {
        $this->activities = Workflow::newActivityStub(
            YourActivitiesInterface::class,
            ActivityOptions::new()
                ->withStartToCloseTimeout('10 seconds')
                ->withSummary('Processing user data')
        );
    }

    public function yourWorkflowMethod(string $input): \Generator
    {
        // Execute the activity with the summary
        $result = yield $this->activities->yourActivity($input);

        return $result;
    }
}
```

The input format for `summary` is a string, and limited to 200 bytes.

## Viewing Summary and Details in the UI

Once you've added summaries and details to your Workflows, Activities, and Timers, you can view this enriched information in the Temporal Web UI.
Navigate to your Workflow's details page to see the metadata displayed in two key locations:

### Workflow Overview Section

At the top of the Workflow details page, you'll find the Workflow-level metadata:

- **Summary & Details** - Displays the static summary and static details set when starting the Workflow
- **Current Details** - Displays the dynamic details that can be updated during Workflow Execution

All Workflow details support standard Markdown formatting (excluding images, HTML, and scripts), allowing you to create rich, structured information displays.

### Event History

Individual events in the Workflow's Event History display their associated summaries when available.

Workflow, Activity and Timer summaries appear in purple text next to their corresponding Events, providing immediate context without requiring you to expand the event details.
When you do expand an Event, the summary is also prominently displayed in the detailed view.

---

## Client - PHP SDK(Platform)

![PHP SDK Banner](/img/assets/banner-php-temporal.png)

## Platform

- [Observability](/develop/php/platform/observability)
- [Enriching the UI](/develop/php/platform/enriching-ui)

---

## Observability - PHP SDK

The observability section of the Temporal Developer's guide covers the many ways to view the current state of your [Temporal Application](/temporal#temporal-application)—that is, ways to view which [Workflow Executions](/workflow-execution) are tracked by the [Temporal Platform](/temporal#temporal-platform) and the state of any specified Workflow Execution, either currently or at points of an execution.

This section covers features related to viewing the state of the application, including:

- [Log from a Workflow](#logging)
- [Visibility](#visibility)

## Log from a Workflow {/* #logging */}

Logging enables you to record critical information during code execution.
Loggers create an audit trail and capture information about your Workflow's operation.
An appropriate logging level depends on your specific needs.
During development or troubleshooting, you might use debug or even trace.
In production, you might use info or warn to avoid excessive log volume.

The logger supports the following logging levels:

| Level   | Use                                                                                                       |
| ------- | --------------------------------------------------------------------------------------------------------- |
| `TRACE` | The most detailed level of logging, used for very fine-grained information.                               |
| `DEBUG` | Detailed information, typically useful for debugging purposes.                                            |
| `INFO`  | General information about the application's operation.                                                    |
| `WARN`  | Indicates potentially harmful situations or minor issues that don't prevent the application from working. |
| `ERROR` | Indicates error conditions that might still allow the application to continue running.                    |

The Temporal SDK core normally uses `WARN` as its default logging level.

To get a PSR-3 compatible logger in your Workflow code, use the [`Workflow::getLogger()`](https://php.temporal.io/classes/Temporal-Workflow.html#method_getLogger) method.

```php
use Temporal\Workflow;

#[Workflow\WorkflowInterface]
class MyWorkflow
{
    #[Workflow\WorkflowMethod]
    public function execute(string $param): \Generator
    {
        Workflow::getLogger()->info('Workflow started', ['parameter' => $param]);

        // Your workflow implementation

        Workflow::getLogger()->info('Workflow completed');
        return 'Done';
    }
}
```

The Workflow logger automatically enriches log context with the current Task Queue name.

Logs in replay mode are omitted unless the [`enableLoggingInReplay`](https://php.temporal.io/classes/Temporal-Worker-WorkerOptions.html#method_withEnableLoggingInReplay) Worker option is set to true.

```php
$factory = WorkerFactory::create();
$worker = $factory->newWorker('your-task-queue', WorkerOptions::new()
    ->withEnableLoggingInReplay(true)
);
```

### Default Logger

By default, PHP SDK uses a [`StderrLogger`](https://php.temporal.io/classes/Temporal-Worker-Logger-StderrLogger.html) that outputs log messages to the standard error stream.
These messages are automatically captured by RoadRunner and incorporated into its logging system with the INFO level, ensuring proper log collection in both development and production environments.
For more details on RoadRunner's logging capabilities, see the [RoadRunner Logger documentation](https://docs.roadrunner.dev/docs/logging-and-observability/logger).

### How to provide a custom logger {/* #custom-logger */}

You can set a custom PSR-3 compatible logger when creating a Worker:

```php
$myLogger = new MyLogger();

$workerFactory = WorkerFactory::create(converter: $converter);
$worker = $workerFactory->newWorker(
    taskQueue: 'my-task-queue',
    logger: $myLogger,
);
```

## Visibility APIs {/* #visibility */}

The term Visibility, within the Temporal Platform, refers to the subsystems and APIs that enable an operator to view Workflow Executions that currently exist within a Temporal Service.

### How to use Search Attributes {/* #search-attributes */}

The typical method of retrieving a Workflow Execution is by its Workflow Id.

However, sometimes you'll want to retrieve one or more Workflow Executions based on another property. For example, imagine you want to get all Workflow Executions of a certain type that have failed within a time range, so that you can start new ones with the same arguments.

You can do this with [Search Attributes](/search-attribute).

- [Default Search Attributes](/search-attribute#default-search-attribute) like `WorkflowType`, `StartTime` and `ExecutionStatus` are automatically added to Workflow Executions.
- [Custom Search Attributes](/search-attribute#custom-search-attribute) can contain their own domain-specific data (like `customerId` or `numItems`).

The steps to using custom Search Attributes are:

- Create a new Search Attribute in your Temporal Service using `temporal operator search-attribute create` or the Cloud UI.
- Set the value of the Search Attribute for a Workflow Execution:
  - On the Client by including it as an option when starting the Execution.
  - In the Workflow by calling `UpsertSearchAttributes`.
- Read the value of the Search Attribute:
  - On the Client by calling `DescribeWorkflow`.
  - In the Workflow by looking at `WorkflowInfo`.
- Query Workflow Executions by the Search Attribute using a [List Filter](/list-filter):
  - [In the Temporal CLI](/cli/command-reference/workflow#list).
  - In code by calling `ListWorkflowExecutions`.

Here is how to query Workflow Executions:

Use the [listWorkflowExecutions()](https://php.temporal.io/classes/Temporal-Client-WorkflowClientInterface.html#method_listWorkflowExecutions) method on the Client and pass a [List Filter](/list-filter) as an argument to filter the listed Workflows.
The result is an iterable paginator, so you can use the `foreach` loop to iterate over the results.

```php
$paginator = $workflowClient->listWorkflowExecutions('WorkflowType="GreetingWorkflow"');

foreach ($paginator as $info) {
    echo "Workflow ID: {$info->execution->getID()}\n";
}
```

### How to set custom Search Attributes {/* #custom-search-attributes */}

After you've created custom Search Attributes in your Temporal Service (using `temporal operator search-attribute create` or the Cloud UI), you can set the values of the custom Search Attributes when starting a Workflow.

To set custom Search Attributes, use the `withTypedSearchAttributes` method on `WorkflowOptions` for a Workflow stub.
Typed search attributes are a `TypedSearchAttributes` collection.

```php
$keyDestinationTime = SearchAttributeKey::forDatetime('DestinationTime');
$keyOrderId = SearchAttributeKey::forKeyword('OrderId');

$workflow = $workflowClient->newWorkflowStub(
    OrderWorkflowInterface::class,
    WorkflowOptions::new()
        ->withWorkflowExecutionTimeout('10 minutes')
        ->withTypedSearchAttributes(
            TypedSearchAttributes::empty()
                ->withValue($keyOrderId, $orderid)
                ->withValue($keyDestinationTime, new \DateTimeImmutable('2028-11-05T00:10:07Z'))
        ),
);
```

### How to upsert Search Attributes {/* #upsert-search-attributes */}

Within the Workflow code, you can dynamically add or update Search Attributes using [`upsertTypedSearchAttributes`](https://php.temporal.io/classes/Temporal-Workflow.html#method_upsertTypedSearchAttributes).
This method is particularly useful for Workflows whose attributes need to change based on internal logic or external events.

```php
#[Workflow\UpdateMethod]
public function postponeDestinationTime(\DateInterval $interval)
{
    // Get the key for the DestinationTime attribute
    $keyDestinationTime = SearchAttributeKey::forDatetime('DestinationTime');

    /** @var DateTimeImmutable $destinationTime */
    $destinationTime = Workflow::getInfo()->typedSearchAttributes->get($keyDestinationTime);

    Workflow::upsertTypedSearchAttributes(
        $keyDestinationTime->valueSet($destinationTime->add($interval)),
    );
}
```

### How to remove a Search Attribute from a Workflow {/* #remove-search-attribute */}

To remove a Search Attribute that was previously set, set it to an empty Map.

```php
#[Workflow\UpdateMethod]
public function unsetDestinationTime()
{
    // Get the key for the DestinationTime attribute
    $keyDestinationTime = SearchAttributeKey::forDatetime('DestinationTime');

    Workflow::upsertTypedSearchAttributes(
        $keyDestinationTime->valueUnset(),
    );
}
```

---

## Set up your local development with the PHP SDK
