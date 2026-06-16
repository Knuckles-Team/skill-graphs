
You have `SayHelloWorkflow` running in the `default` Namespace.
By the end of this guide:

1. A Nexus Service will expose `SayHelloWorkflow` as an Operation.
2. A second Namespace will contain a Workflow that calls that Operation.
3. The caller Workflow will get back `"Hello Temporal"` — the same result, but across Namespaces.

<SetupSteps>

<SetupStep code={
<>

<CodeSnippet language="java">
{`package helloworkflow;

@Service
public interface SayHelloNexusService {

    @Operation
    String sayHello(String name);

}`}
</CodeSnippet>

</>
}>

## 1. Define the Nexus Service

Create a file called `SayHelloNexusService.java` that defines the Nexus Service contract.

Creating a Nexus Service establishes the contract between your implementation and any callers.
It provides type safety when invoking Nexus Operations and ensures that Operation Handlers fulfill the contract.

The `@Service` annotation declares this as a Nexus Service.
The `@Operation` annotation marks `sayHello` as a callable Nexus Operation.
`SayHelloWorkflow` returns `String`, so the operation output type is also `String`.

</SetupStep>

<SetupStep code={
<>

<CodeSnippet language="java">
{`package helloworkflow;

@ServiceImpl(service = SayHelloNexusService.class)
public class SayHelloNexusServiceImpl {

    @OperationImpl
    public OperationHandler<String, String> sayHello() {
        return WorkflowRunOperation.fromWorkflowMethod(
            (ctx, details, name) ->
                Nexus.getOperationContext()
                    .getWorkflowClient()
                    .newWorkflowStub(
                        SayHelloWorkflow.class,
                        WorkflowOptions.newBuilder()
                            .setWorkflowId("say-hello-nexus-" + details.getRequestId())
                            .build())
                    ::sayHello
        );
    }

}`}
</CodeSnippet>

</>
}>

## 2. Define the Nexus Operation Handlers

Create a file called `SayHelloNexusServiceImpl.java` that implements the Nexus Operation handler.

Operation handlers contain the logic that runs when a caller invokes a Nexus Operation.

The `@OperationImpl` annotation creates an asynchronous Nexus Operation that starts `SayHelloWorkflow`.
The handler bridges the Nexus `String` input to `SayHelloWorkflow`'s `sayHello` method directly.

</SetupStep>

<SetupStep code={
<>

<CodeSnippet language="java">
{`package helloworkflow;

public class SayHelloWorker {

    public static void main(String[] args) {

        WorkflowServiceStubs service = WorkflowServiceStubs.newLocalServiceStubs();
        WorkflowClient client = WorkflowClient.newInstance(service);
        WorkerFactory factory = WorkerFactory.newInstance(client);

        Worker worker = factory.newWorker("my-task-queue");
        worker.registerWorkflowImplementationTypes(SayHelloWorkflowImpl.class);
        worker.registerActivitiesImplementations(new GreetActivitiesImpl());
        worker.registerNexusServiceImplementation(new SayHelloNexusServiceImpl());

        System.out.println("Starting SayHelloWorker for task queue 'my-task-queue'...");

        factory.start();

    }

}`}
</CodeSnippet>

</>
}>

## 3. Register the Nexus Service Handler in a Worker

Update your existing `SayHelloWorker.java` to register the Nexus Service Handler.

A Worker will only poll for and process incoming Nexus requests if the Nexus Service Handlers are registered.
This is the same Worker concept used for Workflows and Activities.

The registerNexusServiceImplementation parameter registers the handler so it can receive Nexus Operation requests.

</SetupStep>

<SetupStep code={
<>

<CodeSnippet language="java">
{`package helloworkflow;

@WorkflowInterface
public interface NexusCallerWorkflow {

    @WorkflowMethod
    String greetThroughNexus(String name);

}`}
</CodeSnippet>

<CodeSnippet language="java">
{`package helloworkflow;

public class NexusCallerWorkflowImpl implements NexusCallerWorkflow {

    private final SayHelloNexusService nexusService = Workflow.newNexusServiceStub(
        SayHelloNexusService.class,
        NexusServiceOptions.newBuilder()
            .setOperationOptions(
                NexusOperationOptions.newBuilder()
                    .setScheduleToCloseTimeout(Duration.ofSeconds(10))
                    .build())
            .build()
    );

    @Override
    public String greetThroughNexus(String name) {
        return nexusService.sayHello(name);
    }

}`}
</CodeSnippet>

</>
}>

## 4. Develop the caller Workflow

Create two files — `NexusCallerWorkflow.java` and `NexusCallerWorkflowImpl.java` — that define a Workflow which invokes the Nexus Operation.

The caller Workflow demonstrates the consumer side of Nexus.
Instead of importing handler code directly, the caller only depends on the Service contract.
This keeps the caller and handler decoupled so they can live in separate Namespaces, repositories, or even teams.

The `Workflow.newNexusServiceStub` method creates a client bound to your Nexus Service and Endpoint.

</SetupStep>

<SetupStep code={
<>

<CodeSnippet language="bash">
temporal operator namespace create --namespace my-caller-namespace
</CodeSnippet>

<CodeSnippet language="bash">
{`temporal operator nexus endpoint create \\
  --name my-nexus-endpoint-name \\
  --target-namespace default \\
  --target-task-queue my-task-queue`}
</CodeSnippet>

</>
}>

## 5. Create the caller Namespace and Nexus Endpoint

Before running the application, create a caller Namespace and a Nexus Endpoint to route requests from the caller to the handler.
The handler uses the `default` Namespace that was created when you started the dev server.

Namespaces provide isolation between the caller and handler sides.
The Nexus Endpoint acts as a routing layer that connects the caller Namespace to the handler's target Namespace and Task Queue.

Make sure your local Temporal dev server is running (`temporal server start-dev`).

</SetupStep>

<SetupStep wide code={
<>

<CodeSnippet language="java">
{`package helloworkflow;

public class NexusCallerStarter {

    public static void main(String[] args) {

        WorkflowServiceStubs service = WorkflowServiceStubs.newLocalServiceStubs();
        WorkflowClient client = WorkflowClient.newInstance(service,
            WorkflowClientOptions.newBuilder()
                .setNamespace("my-caller-namespace")
                .build()
        );
        WorkerFactory factory = WorkerFactory.newInstance(client);

        Worker worker = factory.newWorker("my-caller-task-queue");
        worker.registerWorkflowImplementationTypes(
            WorkflowImplementationOptions.newBuilder()
                .setNexusServiceOptions(
                    Collections.singletonMap(
                        "SayHelloNexusService",
                        NexusServiceOptions.newBuilder()
                            .setEndpoint("my-nexus-endpoint-name")
                            .build()))
                .build(),
            NexusCallerWorkflowImpl.class
        );
        factory.start();

        NexusCallerWorkflow workflow = client.newWorkflowStub(
            NexusCallerWorkflow.class,
            WorkflowOptions.newBuilder()
                .setTaskQueue("my-caller-task-queue")
                .setWorkflowId("nexus-caller-workflow-id")
                .build()
        );

        String result = workflow.greetThroughNexus("Temporal");
        System.out.println("Workflow result: " + result);

        factory.shutdown();
        System.exit(0);

    }

}`}
</CodeSnippet>

</>
}>

## 6. Run and Verify

Create `NexusCallerStarter.java` to start the caller Worker and execute the Workflow.

This brings everything together: the caller Worker hosts `NexusCallerWorkflow`, which uses the Nexus stub to invoke `sayHello` on the handler side.
The full request flows from the caller Workflow, through the Nexus Endpoint, to the handler Worker running `SayHelloWorkflow`, and back to the caller.

**Run the application:**

1. Start the handler Worker in one terminal:

```bash
mvn compile exec:java \
  -Dexec.mainClass="helloworkflow.SayHelloWorker"
```

2. Run the caller in another terminal:

```bash
mvn compile exec:java \
  -Dexec.mainClass="helloworkflow.NexusCallerStarter"
```

You should see:

```
Workflow result: Hello Temporal
```

Open the [Temporal Web UI](http://localhost:8233) and switch between Namespaces to see both Workflow Executions.
In `my-caller-namespace`, find the `NexusCallerWorkflow` execution — you should see `NexusOperationScheduled`, `NexusOperationStarted`, and `NexusOperationCompleted` events in its history.
In `default`, find the `SayHelloWorkflow` execution that was started by the Nexus Operation.

</SetupStep>
</SetupSteps>

## Next Steps

Now that you have a working Nexus Service, here are some resources to deepen your understanding:

- **[Java Nexus Feature Guide](/develop/java/nexus)**: Covers synchronous and asynchronous Operations, error handling, cancellation, and cross-Namespace calls.
- **[Nexus Operations](/nexus/operations)**: The full Operation lifecycle, including retries, timeouts, and execution semantics.
- **[Nexus Services](/nexus/services)**: Designing Service contracts and registering multiple Services per Worker.
- **[Nexus Patterns](/nexus/patterns)**: Comparing the collocated and router-queue deployment patterns.
- **[Error Handling in Nexus](/nexus/error-handling)**: Handling retryable and non-retryable errors across caller and handler boundaries.
- **[Execution Debugging](/nexus/execution-debugging)**: Bi-directional linking and OpenTelemetry tracing for debugging Nexus calls.
- **[Nexus Endpoints](/nexus/endpoints)**: Managing Endpoints and understanding how they route requests.
- **[Temporal Nexus on Temporal Cloud](/cloud/nexus)**: Deploying Nexus in a production Temporal Cloud environment with built-in access controls and multi-region connectivity.

---

## Enriching the user interface - Java SDK

Temporal supports adding context to Workflows and Events with metadata.
This helps users identify and understand Workflows and their operations.

## Adding Summary and Details to Workflows

### Starting a Workflow

When starting a workflow, you can provide a static summary and details to help identify the Workflow in the UI:

```java

public class Main {
    public static void main(String[] args) {
        // Create service stubs and workflow client
        WorkflowServiceStubs service = WorkflowServiceStubs.newLocalServiceStubs();
        WorkflowClient workflowClient = WorkflowClient.newInstance(service);

        // Create workflow options with static summary and details
        WorkflowOptions options = WorkflowOptions.newBuilder()
                .setWorkflowId("your-workflow-id")
                .setTaskQueue("your-task-queue")
                .setStaticSummary("Order processing for customer #12345")
                .setStaticDetails("Processing premium order with expedited shipping")
                .build();

        // Create the workflow stub
        YourWorkflow workflow = workflowClient.newWorkflowStub(YourWorkflow.class, options);

        // Start the workflow
        String result = workflow.yourWorkflowMethod("workflow input");
    }
}
```

`setStaticSummary()` sets a single-line description that appears in the Workflow list view, limited to 200 bytes.
`setStaticDetails()` sets multi-line comprehensive information that appears in the Workflow details view, with a larger limit of 20K bytes.

The input format is standard Markdown excluding images, HTML, and scripts.

You can also use `WorkflowClient.start()` for async execution:

```java
// Start workflow asynchronously
WorkflowExecution execution = WorkflowClient.start(workflow::yourWorkflowMethod, "workflow input");
```

### Inside the Workflow

Within a Workflow, you can get and set the _current workflow details_.
Unlike static summary/details set at Workflow start, this value can be updated throughout the life of the Workflow.
Current Workflow details also takes Markdown format (excluding images, HTML, and scripts) and can span multiple lines.

```java

public class YourWorkflowImpl implements YourWorkflow {
    @Override
    public String yourWorkflowMethod(String input) {
        // Get the current details
        String currentDetails = Workflow.getCurrentDetails();
        Workflow.getLogger(YourWorkflowImpl.class).info("Current details: " + currentDetails);

        // Set/update the current details
        Workflow.setCurrentDetails("Updated workflow details with new status");

        return "Workflow completed";
    }
}
```

### Adding Summary to Activities and Timers

You can attach a `setSummary()` to Activities when starting them from within a Workflow:

```java

public class YourWorkflowImpl implements YourWorkflow {
    private final YourActivities activities =
        Workflow.newActivityStub(YourActivities.class,
            ActivityOptions.newBuilder()
                .setStartToCloseTimeout(Duration.ofSeconds(10))
                .setSummary("Processing user data")
                .build());

    @Override
    public String yourWorkflowMethod(String input) {
        // Execute the activity with the summary
        String result = activities.yourActivity(input);
        return result;
    }
}
```

Similarly, you can attach a `setSummary()` to timers within a Workflow:

```java

public class YourWorkflowImpl implements YourWorkflow {
    @Override
    public String yourWorkflowMethod(String input) {
        // Create a timer with a summary
        Workflow.newTimer(Duration.ofMinutes(5),
            TimerOptions.newBuilder()
                .setSummary("Waiting for payment confirmation")
                .build())
            .get(); // Wait for the timer to fire

        return "Timer completed";
    }
}
```

The input format for `setSummary()` is a string, and limited to 200 bytes.

## Viewing Summary and Details in the UI

Once you've added summaries and details to your Workflows, Activities, and Timers, you can view this enriched information in the Temporal Web UI.
Navigate to your Workflow's details page to see the metadata displayed in two key locations:

### Workflow Overview Section

At the top of the workflow details page, you'll find the workflow-level metadata:

- **Summary & Details** - Displays the static summary and static details set when starting the workflow
- **Current Details** - Displays the dynamic details that can be updated during workflow execution

All Workflow details support standard Markdown formatting (excluding images, HTML, and scripts), allowing you to create rich, structured information displays.

### Event History

Individual events in the Workflow's Event History display their associated summaries when available.

Workflow, Activity and Timer summaries appear in purple text next to their corresponding events, providing immediate context without requiring you to expand the Event details.
When you do expand an Event, the summary is also prominently displayed in the detailed view.

---

## Client - Java SDK(Platform)

![Java SDK Banner](/img/assets/banner-java-temporal.png)

## Platform

- [Observability](/develop/java/platform/observability)
- [Enriching the UI](/develop/java/platform/enriching-ui)

---

## Observability - Java SDK

The observability section of the Temporal Developer's guide covers the many ways to view the current state of your [Temporal Application](/temporal#temporal-application)—that is, ways to view which [Workflow Executions](/workflow-execution) are tracked by the [Temporal Platform](/temporal#temporal-platform) and the state of any specified Workflow Execution, either currently or at points of an execution.

This section covers features related to viewing the state of the application, including:

- [Emit metrics](#metrics)
- [Set up tracing](#tracing)
- [Log from a Workflow](#logging)
- [Visibility APIs](#visibility)

## Emit metrics {/* #metrics */}

Each Temporal SDK is capable of emitting an optional set of metrics from either the Client or the Worker process.
For a complete list of metrics capable of being emitted, see the [SDK metrics reference](/references/sdk-metrics).

- For an overview of Prometheus and Grafana integration, refer to the [Monitoring](/self-hosted-guide/monitoring) guide.
- For a list of metrics, see the [SDK metrics reference](/references/sdk-metrics).
- For an end-to-end example that exposes metrics with the Java SDK, refer to the [samples-java](https://github.com/temporalio/samples-java/tree/main/core/src/main/java/io/temporal/samples/metrics) repo.

To emit metrics with the Java SDK, use the [`MicrometerClientStatsReporter`](https://github.com/temporalio/sdk-java/blob/55ee7894aec427d7e384c3519732bdd61119961a/src/main/java/io/temporal/common/reporter/MicrometerClientStatsReporter.java#L34) class to integrate with Micrometer MeterRegistry configured for your metrics backend.
[Micrometer](https://micrometer.io/docs) is a popular Java framework that provides integration with Prometheus and other backends.

The following example shows how to use `MicrometerClientStatsReporter` to define the metrics scope and set it with the `WorkflowServiceStubsOptions`.

```java
//...
   // see the Micrometer documentation for configuration details on other supported monitoring systems.
   // in this example shows how to set up Prometheus registry and stats reported.
   PrometheusMeterRegistry registry = new PrometheusMeterRegistry(PrometheusConfig.DEFAULT);
   StatsReporter reporter = new MicrometerClientStatsReporter(registry);
    // set up a new scope, report every 10 seconds
     Scope scope = new RootScopeBuilder()
             .reporter(reporter)
             .reportEvery(com.uber.m3.util.Duration.ofSeconds(10));
   // for Prometheus collection, expose a scrape endpoint.
   //...
   // add metrics scope to WorkflowServiceStub options
   WorkflowServiceStubsOptions stubOptions =
       WorkflowServiceStubsOptions.newBuilder().setMetricsScope(scope).build();
//...
```

For more details, see the [Java SDK Samples](https://github.com/temporalio/samples-java/tree/637c2e66fd2dab43d9f3f39e5fd9c55e4f3884f0/core/src/main/java/io/temporal/samples/metrics).
For details on configuring a Prometheus scrape endpoint with Micrometer, see the [Micrometer Prometheus Configuring](https://docs.micrometer.io/micrometer/reference/implementations/prometheus.html#_configuring) documentation.

## Set up tracing {/* #tracing */}

Tracing allows you to view the call graph of a Workflow along with its Activities, Nexus Operations, and any Child Workflows.

Temporal Web's tracing capabilities mainly track Activity Execution within a Temporal context. If you need custom tracing specific for your use case, you should make use of context propagation to add tracing logic accordingly.

To configure tracing in Java, register the `OpenTracingClientInterceptor()` interceptor.
You can register the interceptors on both the Temporal Client side and the Worker side, or through a [Plugin](/develop/plugins-guide#interceptors) if you're building a reusable library.

The following code examples demonstrate the `OpenTracingClientInterceptor()` on the Temporal Client.

```java
WorkflowClientOptions.newBuilder()
   //...
   .setInterceptors(new OpenTracingClientInterceptor())
   .build();
```

```java
WorkflowClientOptions clientOptions =
    WorkflowClientOptions.newBuilder()
        .setInterceptors(new OpenTracingClientInterceptor(JaegerUtils.getJaegerOptions(type)))
        .build();
WorkflowClient client = WorkflowClient.newInstance(service, clientOptions);
```

The following code examples demonstrate the `OpenTracingClientInterceptor()` on the Worker.

```java
WorkerFactoryOptions.newBuilder()
   //...
   .setWorkerInterceptors(new OpenTracingWorkerInterceptor())
   .build();
```

```java
WorkerFactoryOptions factoryOptions =
    WorkerFactoryOptions.newBuilder()
        .setWorkerInterceptors(
            new OpenTracingWorkerInterceptor(JaegerUtils.getJaegerOptions(type)))
        .build();
WorkerFactory factory = WorkerFactory.newInstance(client, factoryOptions);
```

For more information, see the Temporal [OpenTracing module](https://github.com/temporalio/sdk-java/blob/master/temporal-opentracing/README.md).

### Context Propagation Over Nexus Operation Calls

Nexus does not use the standard context propagator header structure.
Instead, it relies on a Temporal-agnostic protocol designed to connect arbitrary systems.
To propagate context over Nexus Operation calls, the context is serialized into a `Map<String, String>`.
This map is special as it will normalize all keys to lowercase.

Because Nexus uses this custom format, and because Nexus calls may involve external systems, the `ContextPropagator` interface doesn’t apply to Nexus headers.
Context must be explicitly propagated through interceptors, as shown in the [Nexus Context Propagation sample](https://github.com/temporalio/samples-java/tree/main/core/src/main/java/io/temporal/samples/nexuscontextpropagation).

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

To get a standard `slf4j` logger in your Workflow code, use the [`Workflow.getLogger`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/workflow/Workflow.html) method.

```java
private static final Logger logger = Workflow.getLogger(DynamicDslWorkflow.class);
```

Logs in replay mode are omitted unless the [`WorkerFactoryOptions.Builder.setEnableLoggingInReplay(boolean)`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/worker/WorkerFactoryOptions.Builder.html#setEnableLoggingInReplay(boolean)) method is set to true.

### How to provide a custom logger {/* #custom-logger */}

Use a custom logger for logging.

To set a custom logger, supply your own logging implementation and configuration details the same way you would in any other Java application.

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
  - In the Workflow by calling `upsertTypedSearchAttributes`.
- Read the value of the Search Attribute:
  - On the Client by calling `DescribeWorkflow`.
  - In the Workflow by looking at `WorkflowInfo`.
- Query Workflow Executions by the Search Attribute using a [List Filter](/list-filter):
  - [In the Temporal CLI](/cli/command-reference/workflow#list).
  - In code by calling `ListWorkflowExecutions`.

### How to set custom Search Attributes {/* #custom-search-attributes */}

After you've created custom Search Attributes in your Temporal Service (using `temporal operator search-attribute create` or the Cloud UI), you can set the values of the custom Search Attributes when starting a Workflow.

When starting a Workflow Execution with your Client, include the Custom Search Attribute in the options using `WorkflowOptions.newBuilder().setTypedSearchAttributes()`:

```java
    // In a shared constants file, so all files have access

    public static final SearchAttributeKey<Boolean> IS_ORDER_FAILED = SearchAttributeKey.forBoolean("isOrderFailed");
