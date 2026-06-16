implement the Activity with a polling mechanism, but a simpler and less resource-intensive implementation is to
asynchronously complete a Temporal Activity.

There are two parts to implementing an asynchronously completed Activity:

1. The Activity provides the information necessary for completion from an external system and notifies the Temporal
   service that it is waiting for that outside callback.
2. The external service calls the Temporal service to complete the Activity.

The following example demonstrates the first part:

<!--SNIPSTART samples-php-async-activity-completion-activity-class-->
[app/src/AsyncActivityCompletion/GreetingActivity.php](https://github.com/temporalio/samples-php/blob/main/app/src/AsyncActivityCompletion/GreetingActivity.php)
```php
class GreetingActivity implements GreetingActivityInterface
{
    private LoggerInterface $logger;

    public function __construct()
    {
        $this->logger = new Logger();
    }
    /**
     * Demonstrates how to implement an Activity asynchronously.
     * When {@link Activity::doNotCompleteOnReturn()} is called,
     * the Activity implementation function that returns doesn't complete the Activity.
     */
    public function composeGreeting(string $greeting, string $name): string
    {
        // In real life this request can be executed anywhere. By a separate service for example.
        $this->logger->info(sprintf('GreetingActivity token: %s', base64_encode(Activity::getInfo()->taskToken)));
        // Send the taskToken to the external service that will complete the Activity.
        // Return from the Activity a function indicating that Temporal should wait
        // for an async completion message.
        Activity::doNotCompleteOnReturn();
        // When doNotCompleteOnReturn() is invoked the return value is ignored.
        return 'ignored';
    }
}
```
<!--SNIPEND-->

The following code demonstrates how to complete the Activity successfully using `WorkflowClient`:

<!--SNIPSTART samples-php-async-activity-completion-completebytoken-->
[app/src/AsyncActivityCompletion/CompleteCommand.php](https://github.com/temporalio/samples-php/blob/main/app/src/AsyncActivityCompletion/CompleteCommand.php)
```php
$client = $this->workflowClient->newActivityCompletionClient();
// Complete the Activity.
$client->completeByToken(
    base64_decode($input->getArgument('token')),
    $input->getArgument('message')
);
```
<!--SNIPEND-->

To fail the Activity, you would do the following:

```php
// Fail the Activity.
$activityClient->completeExceptionallyByToken($taskToken, new \Error("activity failed"));
```

---

## Activity Basics - PHP SDK

## How to develop a basic Activity {/* #develop-activities */}

One of the primary things that Workflows do is orchestrate the execution of Activities.
An Activity is a normal function or method execution that's intended to execute a single, well-defined action (either short or long-running), such as querying a database, calling a third-party API, or transcoding a media file.
An Activity can interact with world outside the Temporal Platform or use a Temporal Client to interact with a Temporal Service.
For the Workflow to be able to execute the Activity, we must define the [Activity Definition](/activity-definition).

Activities are defined as methods of a plain PHP interface annotated with `#[ActivityInterface]`.

Following is an example of an interface that defines four Activities:

```php
#[ActivityInterface]
// Defining an interface for the activities.
interface FileProcessingActivities
{
    public function upload(string $bucketName, string $localName, string $targetName): void;

    #[ActivityMethod("transcode_file")]
    public function download(string $bucketName, string $remoteName): void;

    public function processFile(): string;

    public function deleteLocalFile(string $fileName): void;
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

Each method defines a single Activity type.
A single Workflow can use more than one Activity interface and call more than one Activity method from the same interface.

The only requirement is that Activity method arguments and return values are serializable to a byte array using the provided [DataConverter](https://github.com/temporalio/sdk-php/blob/master/src/DataConverter/DataConverterInterface.php) interface.
The default implementation uses a JSON serializer, but an alternative implementation can be easily configured.

### How to define Activity return values {/* #activity-return-values */}

All data returned from an Activity must be serializable.

Activity return values are subject to payload size limits in Temporal. The default payload size limit is 2MB, and there is a hard limit of 4MB for any gRPC message size in the Event History transaction ([see Cloud limits here](https://docs.temporal.io/cloud/limits#per-message-grpc-limit)). Keep in mind that all return values are recorded in a [Workflow Execution Event History](/workflow-execution/event#event-history).

Return values must be serializable to a byte array using the provided [DataConverter](https://github.com/temporalio/sdk-php/blob/master/src/DataConverter/DataConverterInterface.php) interface.
The default implementation uses a JSON serializer, but an alternative implementation can be easily configured.
Thus, you can return both primitive types:

```php
class GreetingActivity implements GreetingActivityInterface
{
    public function composeGreeting(string $greeting, string $name): string
    {
        return $greeting . ' ' . $name;
    }
}
```

And objects:

```php
class GreetingActivity implements GreetingActivityInterface
{
    public function composeGreeting(string $greeting, string $name): Greeting
    {
        return new Greeting($greeting, $name);
    }
}
```

### How to customize your Activity Type {/* #activity-type */}

Activities have a Type that are referred to as the Activity name.
The following examples demonstrate how to set a custom name for your Activity Type.

An optional `#[ActivityMethod]` attribute can be used to override a default Activity name.

You can define your own prefix for all Activity names by adding the `prefix` option to the `ActivityInterface` attribute.
(The default prefix is empty.)

```php
#[ActivityInterface("file_activities.")]
interface FileProcessingActivities
{
    public function upload(string $bucketName, string $localName, string $targetName);

    #[ActivityMethod("transcode_file")]
    public function download(string $bucketName, string $remoteName);

    public function processFile(): string;

    public function deleteLocalFile(string $fileName);
}
```

The `#[ActivityInterface("file_activities.")]` is an attribute that tells the PHP SDK to generate a class to implement the `FileProcessingActivities` interface. The functions define Activities that are used in the Workflow.

---

## Activity execution - PHP SDK

## How to start an Activity Execution {/* #activity-execution */}

Calls to spawn [Activity Executions](/activity-execution) are written within a [Workflow Definition](/workflow-definition).
The call to spawn an Activity Execution generates the [ScheduleActivityTask](/references/commands#scheduleactivitytask) Command.
This results in the set of three [Activity Task](/tasks#activity-task) related Events ([ActivityTaskScheduled](/references/events#activitytaskscheduled), [ActivityTaskStarted](/references/events#activitytaskstarted), and ActivityTask[Closed]) in your Workflow Execution Event History.

A single instance of the Activities implementation is shared across multiple simultaneous Activity invocations.
Activity implementation code should be _idempotent_.

The values passed to Activities through invocation parameters or returned through a result value are recorded in the Execution history.
The entire Execution history is transferred from the Temporal service to Workflow Workers when a Workflow state needs to recover.
A large Execution history can thus adversely impact the performance of your Workflow.

Therefore, be mindful of the amount of data you transfer through Activity invocation parameters or Return Values.
Otherwise, no additional limitations exist on Activity implementations.

Activity implementation is an implementation of an Activity interface.
The following code example, uses a constructor that takes an Amazon S3 client and a local directory, and uploads a file to the S3 bucket.
Then, the code uses a function to download a file from the S3 bucket passing a bucket name, remote name, and local name as arguments.
Finally, it uses a function that takes a local file name as an argument and returns a string.

```php
// An implementation of an Activity interface.
class FileProcessingActivitiesImpl implements FileProcessingActivities {

    private S3Client $s3Client;

    private string $localDirectory;

    public function __construct(S3Client $s3Client, string $localDirectory) {
        $this->s3Client = $s3Client;
        $this->localDirectory = $localDirectory;
    }

    // Uploading a file to S3.
    public function upload(string $bucketName, string $localName, string $targetName): void
    {
        $this->s3Client->putObject(
            $bucketName,
            $targetName,
            fopen($this->localDirectory . $localName, 'rb+')
        );
    }

// Downloading a file from S3.
    public function download(
        string $bucketName,
        string $remoteName,
        string $localName
    ): void
    {
        $this->s3Client->downloadObject(
            $bucketName,
            $remoteName,
            fopen($this->localDirectory .$localName, 'wb+')
        );
    }

// A function that takes a local file name as an argument and returns a string.
    public function processFile(string $localName): string
    {
        // Implementation omitted for brevity.
        return compressFile($this->localDirectory . $localName);
    }

    public function deleteLocalFile(string $fileName): void
    {
        unlink($this->localDirectory . $fileName);
    }
}
```

### How to set the required Activity Timeouts {/* #required-timeout */}

Activity Execution semantics rely on several parameters.
The only required value that needs to be set is either a [Schedule-To-Close Timeout](/encyclopedia/detecting-activity-failures#schedule-to-close-timeout) or a [Start-To-Close Timeout](/encyclopedia/detecting-activity-failures#start-to-close-timeout).
These values are set in the Activity Options.

### How to get the results of an Activity Execution {/* #get-activity-results */}

The call to spawn an [Activity Execution](/activity-execution) generates the [ScheduleActivityTask](/references/commands#scheduleactivitytask) Command and provides the Workflow with an Awaitable.
Workflow Executions can either block progress until the result is available through the Awaitable or continue progressing, making use of the result when it becomes available.

`Workflow::newActivityStub`returns a client-side stub an implements an Activity interface. The client-side stub can be used within the Workflow code. It takes the Activity's type and`ActivityOptions` as arguments.

Calling (via `yield`) a method on this interface invokes an Activity that implements this method.
An Activity invocation synchronously blocks until the Activity completes, fails, or times out.
Even if Activity Execution takes a few months, the Workflow code still sees it as a single synchronous invocation.
It doesn't matter what happens to the processes that host the Workflow.
The business logic code just sees a single method call.

```php
class GreetingWorkflow implements GreetingWorkflowInterface
{
    private $greetingActivity;

    public function __construct()
    {
        $this->greetingActivity = Workflow::newActivityStub(
            GreetingActivityInterface::class,
            ActivityOptions::new()->withStartToCloseTimeout(\DateInterval::createFromDateString('30 seconds'))
        );
    }

    public function greet(string $name): \Generator
    {
        // This is a blocking call that returns only after the activity has completed.
        return yield $this->greetingActivity->composeGreeting('Hello', $name);
    }
}
```

If different Activities need different options, like timeouts or a task queue, multiple client-side stubs can be created with different options.

```php
$greetingActivity = Workflow::newActivityStub(
    GreetingActivityInterface::class,
    ActivityOptions::new()->withStartToCloseTimeout(\DateInterval::createFromDateString('30 seconds'))
);

$greetingActivity = Workflow::newActivityStub(
    GreetingActivityInterface::class,
    ActivityOptions::new()->withStartToCloseTimeout(\DateInterval::createFromDateString('30 minutes'))
);
```

---

## Activities - PHP SDK

![PHP SDK Banner](/img/assets/banner-php-temporal.png)

## Activities

- [Activity Basics](/develop/php/activities/basics)
- [Activity Execution](/develop/php/activities/execution)
- [Timeouts](/develop/php/activities/timeouts)
- [Asynchronous Activity Completion](/develop/php/activities/asynchronous-activity)

---

## Activity Timeouts - PHP SDK

## How to set Activity timeouts {/* #activity-timeouts */}

Each Activity timeout controls the maximum duration of a different aspect of an Activity Execution.

The following timeouts are available in the Activity Options.

- **[Schedule-To-Close Timeout](/encyclopedia/detecting-activity-failures#schedule-to-close-timeout):** is the maximum amount of time allowed for the overall [Activity Execution](/activity-execution).
- **[Start-To-Close Timeout](/encyclopedia/detecting-activity-failures#start-to-close-timeout):** is the maximum time allowed for a single [Activity Task Execution](/tasks#activity-task-execution).
- **[Schedule-To-Start Timeout](/encyclopedia/detecting-activity-failures#schedule-to-start-timeout):** is the maximum amount of time that is allowed from when an [Activity Task](/tasks#activity-task) is scheduled to when a [Worker](/workers#worker) starts that Activity Task.

An Activity Execution must have either the Start-To-Close or the Schedule-To-Close Timeout set.

Because Activities are reentrant, only a single stub can be used for multiple Activity invocations.

Available timeouts are:

- withScheduleToCloseTimeout()
- withStartToCloseTimeout()
- withScheduleToStartTimeout()

```php
$this->greetingActivity = Workflow::newActivityStub(
    GreetingActivityInterface::class,
    // Set Activity Timeout duration
    ActivityOptions::new()
        ->withScheduleToCloseTimeout(CarbonInterval::seconds(2))
        // ->withStartToCloseTimeout(CarbonInterval::seconds(2))
        // ->withScheduleToStartTimeout(CarbonInterval::seconds(10))
);
```

### How to set an Activity Retry Policy {/* #activity-retries */}

A Retry Policy works in cooperation with the timeouts to provide fine controls to optimize the execution experience.

Activity Executions are automatically associated with a default [Retry Policy](/encyclopedia/retry-policies) if a custom one is not provided.

To set an Activity Retry, set `{@link RetryOptions}` on `{@link ActivityOptions}`.
The follow example creates a new Activity with the given options.

```php
$this->greetingActivity = Workflow::newActivityStub(
    GreetingActivityInterface::class,
    ActivityOptions::new()
        ->withScheduleToCloseTimeout(CarbonInterval::seconds(10))
        ->withRetryOptions(
            RetryOptions::new()
                ->withInitialInterval(CarbonInterval::seconds(1))
                ->withMaximumAttempts(5)
                ->withNonRetryableExceptions([\InvalidArgumentException::class])
        )
);
}
```

For an executable code sample, see [ActivityRetry sample](https://github.com/temporalio/samples-php/tree/master/app/src/ActivityRetry) in the PHP samples repository.

### How to set the required Activity Timeouts {/* #required-timeout */}

Activity Execution semantics rely on several parameters.
The only required value that needs to be set is either a [Schedule-To-Close Timeout](/encyclopedia/detecting-activity-failures#start-to-close-timeout) or a [Start-To-Close Timeout](/encyclopedia/detecting-activity-failures#start-to-close-timeout).
These values are set in the Activity Options.

## Activity next Retry delay {/* #activity-next-retry-delay */}

**How to override the next Retry delay following an Activity failure using the Temporal PHP SDK**

You may throw an [`ApplicationFailure`](/references/failures#application-failure) with the `nextRetryDelay` field set.
This value will replace and override whatever the retry interval would be on the retry policy.

For example, if in an Activity, you want to base the interval on the number of attempts, you might do:

```php
$attempt = \Temporal\Activity::getInfo()->attempt;

throw new \Temporal\Exception\Failure\ApplicationFailure(
    message: "Something bad happened on attempt $attempt",
    type: 'my_failure_type',
    nonRetryable: false,
    nextRetryDelay: \DateInterval::createFromDateString(\sprintf('%d seconds', $attempt * 3)),
);
```

## How to Heartbeat an Activity {/* #activity-heartbeats */}

An [Activity Heartbeat](/encyclopedia/detecting-activity-failures#activity-heartbeat) is a ping from the [Worker Process](/workers#worker-process) that is executing the Activity to the [Temporal Service](/temporal-service).
Each Heartbeat informs the Temporal Service that the [Activity Execution](/activity-execution) is making progress and the Worker has not crashed.
If the Temporal Service does not receive a Heartbeat within a [Heartbeat Timeout](/encyclopedia/detecting-activity-failures#heartbeat-timeout) time period, the Activity will be considered failed and another [Activity Task Execution](/tasks#activity-task-execution) may be scheduled according to the Retry Policy.

Heartbeats may not always be sent to the Temporal Service—they may be [throttled](/encyclopedia/detecting-activity-failures#throttling) by the Worker.

Activity Cancellations are delivered to Activities from the Temporal Service when they Heartbeat. Activities that don't Heartbeat can't receive a Cancellation.
Heartbeat throttling may lead to Cancellation getting delivered later than expected.

Heartbeats can contain a `details` field describing the Activity's current progress.
If an Activity gets retried, the Activity can access the `details` from the last Heartbeat that was sent to the Temporal Service.

Some Activities are long-running.
To react to a crash quickly, use the Heartbeat mechanism, `Activity::heartbeat()`, which lets the Temporal Server know that the Activity is still alive.
This acts as a periodic checkpoint mechanism for the progress of an Activity.

You can piggyback `details` on an Activity Heartbeat.
If an Activity times out, the last value of `details` is included in the `TimeoutFailure` delivered to a Workflow.
Then the Workflow can pass the details to the next Activity invocation.
Additionally, you can access the details from within an Activity via `Activity::getHeartbeatDetails`.
When an Activity is retried after a failure `getHeartbeatDetails` enables you to get the value from the last successful Heartbeat.

```php
use Temporal\Activity;

class FileProcessingActivitiesImpl implements FileProcessingActivities
{
    // ...
    public function download(
        string $bucketName,
        string $remoteName,
        string $localName
    ): void
    {
        $this->dowloader->downloadWithProgress(
            $bucketName,
            $remoteName,
            $localName,
            // on progress
            function ($progress) {
                Activity::heartbeat($progress);
            }
        );

        Activity::heartbeat(100); // download complete

        // ...
    }

    // ...
}
```

#### How to set a Heartbeat Timeout {/* #heartbeat-timeout */}

A [Heartbeat Timeout](/encyclopedia/detecting-activity-failures#heartbeat-timeout) works in conjunction with [Activity Heartbeats](/encyclopedia/detecting-activity-failures#activity-heartbeat).

Some Activities are long-running.
To react to a crash quickly, use the Heartbeat mechanism, `Activity::heartbeat()`, which lets the Temporal Server know that the Activity is still alive.
This acts as a periodic checkpoint mechanism for the progress of an Activity.

You can piggyback `details` on an Activity Heartbeat.
If an Activity times out, the last value of `details` is included in the `TimeoutFailure` delivered to a Workflow.
Then the Workflow can pass the details to the next Activity invocation.
Additionally, you can access the details from within an Activity via `Activity::getHeartbeatDetails`.
When an Activity is retried after a failure `getHeartbeatDetails` enables you to get the value from the last successful Heartbeat.

```php
use Temporal\Activity;

class FileProcessingActivitiesImpl implements FileProcessingActivities
{
    // ...
    public function download(
        string $bucketName,
        string $remoteName,
        string $localName
    ): void
    {
        $this->dowloader->downloadWithProgress(
            $bucketName,
            $remoteName,
            $localName,
            // on progress
            function ($progress) {
                Activity::heartbeat($progress);
            }
        );

        Activity::heartbeat(100); // download complete

        // ...
    }

    // ...
}
```

---

## Debugging - PHP SDK

## Debugging {/* #debug */}

### How to debug in a development environment {/* #debug-in-a-development-environment */}

In addition to the normal development tools of logging and a debugger, you can also see what's happening in your Workflow by using the [Web UI](/web-ui) or [Temporal CLI](/cli).

### How to debug in a production environment {/* #debug-in-a-development-production */}

You can debug production Workflows using:

- [Web UI](/web-ui)
- [Temporal CLI](/cli)

You can debug and tune Worker performance with metrics and the [Worker performance guide](/develop/worker-performance).

Debug Server performance with [Cloud metrics](/cloud/metrics/) or [self-hosted Server metrics](/self-hosted-guide/production-checklist#scaling-and-metrics).

---

## Best Practices - PHP SDK

![PHP SDK Banner](/img/assets/banner-php-temporal.png)

## Best practices

- [Testing](/develop/php/best-practices/testing-suite)
- [Debugging](/develop/php/best-practices/debugging)

---

## Testing - PHP SDK

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

## Testing Activities {/* #test-activities */}

An Activity can be tested with a mock Activity environment, which provides a way to mock the Activity context, listen to Heartbeats, and cancel the Activity.
This behavior allows you to test the Activity in isolation by calling it directly, without needing to create a Worker to run the Activity.

## Testing Workflows {/* #test-workflows */}

### How to mock Activities {/* #mock-activities */}

Mock the Activity invocation when unit testing your Workflows.

When integration testing Workflows with a Worker, you can mock Activities by providing mock Activity implementations to the Worker.

**RoadRunner config**

To mock an Activity in PHP, use [RoadRunner Key-Value storage](https://github.com/spiral/roadrunner-kv) and add the following lines to your `tests/.rr.test.yaml` file.

```yaml
