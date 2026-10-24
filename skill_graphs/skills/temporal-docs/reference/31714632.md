# Cloud profile for Temporal Cloud
[profile.cloud]
address = "your-namespace.a1b2c.tmprl.cloud:7233"
namespace = "your-namespace"
tls_client_cert_data = "your-tls-client-cert-data"
tls_client_key_path = "your-tls-client-key-path"
```

With the connections options defined in the configuration file, use the `LoadClientOptions` function in the `envconfig`
package to create a Temporal Client using the `cloud` profile as follows. After loading the profile, you can also
programmatically override specific connection options before creating the client.

```java {25-30,33-35,42-44}

public class LoadProfile {

  private static final Logger logger = LoggerFactory.getLogger(LoadProfile.class);

  public static void main(String[] args) {
    String profileName = "cloud";

    try {
      String configFilePath =
          Paths.get(LoadProfile.class.getResource("/config.toml").toURI()).toString();

      logger.info("--- Loading '{}' profile from {} ---", profileName, configFilePath);

      // Load specific profile from file with environment variable overrides
      ClientConfigProfile profile =
          ClientConfigProfile.load(
              LoadClientConfigProfileOptions.newBuilder()
                  .setConfigFilePath(configFilePath)
                  .setConfigFileProfile(profileName)
                  .build());

      // Demonstrate programmatic override - fix the incorrect address from staging profile
      ClientConfigProfile.Builder profileBuilder = profile.toBuilder();
      profileBuilder.setAddress("localhost:7233"); // Override the incorrect address
      profile = profileBuilder.build();

      WorkflowServiceStubsOptions serviceStubsOptions = profile.toWorkflowServiceStubsOptions();
      WorkflowClientOptions clientOptions = profile.toWorkflowClientOptions();

      try {
        // Create the workflow client using the loaded configuration
        WorkflowClient client =
            WorkflowClient.newInstance(
                WorkflowServiceStubs.newServiceStubs(serviceStubsOptions), clientOptions);

        // Test the connection by getting system info
        var systemInfo =
            client
                .getWorkflowServiceStubs()
                .blockingStub()
                .getSystemInfo(
                    io.temporal.api.workflowservice.v1.GetSystemInfoRequest.getDefaultInstance());

        logger.info("✅ Client connected successfully!");
        logger.info("   Server version: {}", systemInfo.getServerVersion());

      } catch (Exception e) {
        logger.error("❌ Failed to connect: {}", e.getMessage());
      }

    } catch (Exception e) {
      logger.error("Failed to load configuration: {}", e.getMessage(), e);
      System.exit(1);
    }
  }
}
```

</TabItem>
<TabItem value="env-vars" label="Environment Variables">

The following environment variables are required to connect to Temporal Cloud:

- `TEMPORAL_NAMESPACE`: Your Namespace and Account ID combination in the format `<namespace_id>.<account_id>`.
- `TEMPORAL_ADDRESS`: The gRPC endpoint for your Temporal Cloud Namespace.
- `TEMPORAL_API_KEY`: Your API key value. Required if you are using API key authentication.
- `TEMPORAL_TLS_CLIENT_CERT_DATA` or `TEMPORAL_TLS_CLIENT_CERT_PATH`: Your mTLS client certificate data or file path.
  Required if you are using mTLS authentication.
- `TEMPORAL_TLS_CLIENT_KEY_DATA` or `TEMPORAL_TLS_CLIENT_KEY_PATH`: Your mTLS client private key data or file path.
  Required if you are using mTLS authentication.

Ensure these environment variables exist in your environment before running your Java application.

Import the `io.temporal.envconfig` package to set connection options for the Temporal Client using environment variables. The `ClientConfigProfile.load` method will automatically load all environment variables. For a list of all available environment variables and their default values, refer to [Environment Configuration](/references/client-environment-configuration).

For example, the following code snippet loads all environment variables and creates a Temporal Client with the options specified in those variables. If you have defined a configuration file at either the default location (`~/.config/temporalio/temporal.toml`) or a custom location specified by the `TEMPORAL_CONFIG_FILE` environment variable, this will also load the default profile in the configuration file. However, any options set via environment variables will take precedence.

```java {17-18,25-27}

public class LoadFromFile {

  private static final Logger logger = LoggerFactory.getLogger(LoadFromFile.class);

  public static void main(String[] args) {
    try {

      ClientConfigProfile profile =
          ClientConfigProfile.load(LoadClientConfigProfileOptions.newBuilder().build());

      WorkflowServiceStubsOptions serviceStubsOptions = profile.toWorkflowServiceStubsOptions();
      WorkflowClientOptions clientOptions = profile.toWorkflowClientOptions();

      try {
        // Create the workflow client using the loaded configuration
        WorkflowClient client =
            WorkflowClient.newInstance(
                WorkflowServiceStubs.newServiceStubs(serviceStubsOptions), clientOptions);

        // Test the connection by getting system info
        var systemInfo =
            client
                .getWorkflowServiceStubs()
                .blockingStub()
                .getSystemInfo(
                    io.temporal.api.workflowservice.v1.GetSystemInfoRequest.getDefaultInstance());

        logger.info("✅ Client connected successfully!");
        logger.info("   Server version: {}", systemInfo.getServerVersion());

      } catch (Exception e) {
        logger.error("❌ Failed to connect: {}", e.getMessage());
      }

    } catch (Exception e) {
      logger.error("Failed to load configuration: {}", e.getMessage(), e);
      System.exit(1);
    }
  }
}
```

</TabItem>
<TabItem value="code" label="Code">

Now, when instantiating a Temporal `client` in your Temporal Java SDK code, provide the API key with
`WorkflowServiceStubsOptions` and the Namespace and Account ID in `WorkflowClient.newInstance`:

```java
    WorkflowServiceStubs service =
        WorkflowServiceStubs.newServiceStubs(
            WorkflowServiceStubsOptions.newBuilder()
                .addApiKey(
                    () ->
                        <API key>)
                .setTarget(<endpoint>)
                .setEnableHttps(true)
                ...
                .build());

    WorkflowClient client =
        WorkflowClient.newInstance(
            service, WorkflowClientOptions.newBuilder().setNamespace(<namespace_id>.<account_id>).build());
```

To update the API key, update the `stubOptions`:

```java
String myKey = <APIKey>;
WorkflowServiceStubsOptions stubOptions =
    WorkflowServiceStubsOptions.newBuilder()
        .addApiKey(() -> myKey)
        .build();
// Update by replacing, this must be done in a thread safe way
myKey = "Bearer " + <new APIKey>;
```

To connect to Temporal Cloud using mTLS, you need to provide the mTLS CA certificate and mTLS private key. You can then
use the `SimpleSslContextBuilder` to build an SSL context. Then use the
`WorkflowServiceStubsOptions.Builder.setSslContext` method to set the SSL context.

When you use a remote service, you don't use the `newLocalServiceStubs` convenience method. Instead, set your
connection details as stub configuration options:

<!--SNIPSTART javasdk-build-caller-app-using-temporal-cloud {"selectedLines": ["46-54"]}-->
[sample-apps/java/client/cloudserver-client-sample/src/main/java/clientsample/YourCallerApp.java](https://github.com/temporalio/documentation/blob/main/sample-apps/java/client/cloudserver-client-sample/src/main/java/clientsample/YourCallerApp.java)
```java
// ...
            // Set the Service Stub options (SSL context and gRPC endpoint)
            WorkflowServiceStubsOptions stubsOptions = WorkflowServiceStubsOptions
                .newBuilder()
                .setSslContext(sslContext)
                .setTarget(gRPCEndpoint)
                .build();

             // Create a stub that accesses a Temporal Service
            WorkflowServiceStubs serviceStub = WorkflowServiceStubs.newServiceStubs(stubsOptions);
```
<!--SNIPEND-->

Each Temporal Cloud service Client has four prerequisites.

- The full Namespace Id from the [Cloud Namespace](https://cloud.temporal.io/namespaces) details page
- The gRPC endpoint from the [Cloud Namespace](https://cloud.temporal.io/namespaces) details page
- Your mTLS private key
- Your mTLS x509 Certificate

Retrieve these values before building your Client.

The following sample generates an SSL context from the mTLS .pem and .key files. Along with the gRPC endpoint, this
information configures a service stub for Temporal Cloud. Add the Namespace to your Client build options and initialize
the new Client:

<!--SNIPSTART javasdk-build-caller-app-using-temporal-cloud {"selectedLines": ["41-64"]}-->
[sample-apps/java/client/cloudserver-client-sample/src/main/java/clientsample/YourCallerApp.java](https://github.com/temporalio/documentation/blob/main/sample-apps/java/client/cloudserver-client-sample/src/main/java/clientsample/YourCallerApp.java)
```java
// ...
            // Generate an SSL context
            InputStream clientCertInputStream = new FileInputStream(clientCertPath);
            InputStream clientKeyInputStream = new FileInputStream(clientKeyPath);
            SslContext sslContext = SimpleSslContextBuilder.forPKCS8(clientCertInputStream, clientKeyInputStream).build();

            // Set the Service Stub options (SSL context and gRPC endpoint)
            WorkflowServiceStubsOptions stubsOptions = WorkflowServiceStubsOptions
                .newBuilder()
                .setSslContext(sslContext)
                .setTarget(gRPCEndpoint)
                .build();

             // Create a stub that accesses a Temporal Service
            WorkflowServiceStubs serviceStub = WorkflowServiceStubs.newServiceStubs(stubsOptions);

            // Set the Client options
            WorkflowClientOptions clientOptions = WorkflowClientOptions
                .newBuilder()
                .setNamespace(namespace)
                .build();

            // Initialize the Temporal Client
            // This application uses the Client to communicate with the Temporal Service
            WorkflowClient client = WorkflowClient.newInstance(serviceStub, clientOptions);
```
<!--SNIPEND-->

</TabItem>
</Tabs>

## Start a Workflow Execution {/* #start-workflow-execution */}

[Workflow Execution](/workflow-execution) semantics rely on several parameters—that is, to start a Workflow Execution
you must supply a Task Queue that will be used for the Tasks (one that a Worker is polling), the Workflow Type,
language-specific contextual data, and Workflow Function parameters.

In the examples below, all Workflow Executions are started using a Temporal Client. To spawn Workflow Executions from
within another Workflow Execution, use either the [Child Workflow](/develop/java/workflows/child-workflows) or External Workflow
APIs.

See the [Customize Workflow Type](/develop/java/workflows/basics#workflow-type) section to see how to customize the name
of the Workflow Type.

A request to spawn a Workflow Execution causes the Temporal Service to create the first Event
([WorkflowExecutionStarted](/references/events#workflowexecutionstarted)) in the Workflow Execution Event History. The
Temporal Service then creates the first Workflow Task, resulting in the first
[WorkflowTaskScheduled](/references/events#workflowtaskscheduled) Event.

Use `WorkflowStub` to start a Workflow Execution from within a Client, and `ExternalWorkflowStub` to start a different
Workflow Execution from within a Workflow.

See [`SignalwithStart`](/develop/java/workflows/message-passing#signal-with-start) to start a Workflow Execution to receive a
Signal from within another Workflow.

**Using `WorkflowStub`**

`WorkflowStub` is a proxy generated by the `WorkflowClient`. Each time a new Workflow Execution is started, an instance
of the Workflow implementation object is created. Then, one of the methods (depending on the Workflow Type of the
instance) annotated with `@WorkflowMethod` can be invoked. As soon as this method returns, the Workflow Execution is
considered to be complete.

You can use a typed or untyped `WorkflowStub` in the client code.

- Typed `WorkflowStub` are useful because they are type safe and allow you to invoke your Workflow methods such as
  `@WorkflowMethod`, `@QueryMethod`, and `@SignalMethod` directly.
- An untyped `WorkflowStub` does not use the Workflow interface, and is not type safe. It is more flexible because it
  has methods from the `WorkflowStub` interface, such as `start`, `signalWithStart`, `getResults` (sync and async),
  `query`, `signal`, `cancel` and `terminate`. Note that the Temporal Java SDK also provides typed `WorkflowStub`
  versions for these methods. When using untyped `WorkflowStub`, we rely on the Workflow Type, Activity Type, Child
  Workflow Type, as well as Query and Signal names. For details, see [Temporal Client](#connect-to-development-service).

A Workflow Execution can be started either synchronously or asynchronously.

- Synchronous invocation starts a Workflow and then waits for its completion. If the process that started the Workflow
  crashes or stops waiting, the Workflow continues executing. Because Workflows are potentially long-running, and Client
  crashes happen, it is not very commonly found in production use. The following example is a type-safe approach for
  starting a Workflow Execution synchronously.

  ```java
    NotifyUserAccounts workflow = client.newWorkflowStub(
          NotifyUserAccounts.class,
          WorkflowOptions.newBuilder()
                  .setWorkflowId("notifyAccounts")
                  .setTaskQueue(taskQueue)
                  .build()
          );

  // start the Workflow and wait for a result.
    workflow.notify(new String[] { "Account1", "Account2", "Account3", "Account4", "Account5",
                  "Account6", "Account7", "Account8", "Account9", "Account10"});
      }
  // notify(String[] accountIds) is a Workflow method defined in the Workflow Definition.
  ```

- Asynchronous start initiates a Workflow Execution and immediately returns to the caller. This is the most common way
  to start Workflows in production code. The
  [`WorkflowClient`](https://github.com/temporalio/sdk-java/blob/master/temporal-sdk/src/main/java/io/temporal/client/WorkflowClient.java)
  provides some static methods, such as `start`, `execute`, `signalWithStart` etc., that help with starting your
  Workflows asynchronously.

  The following examples show how to start Workflow Executions asynchronously, with either typed or untyped
  `WorkflowStub`.
  - **Typed WorkflowStub Example**

    ```java
    // create typed Workflow stub
    FileProcessingWorkflow workflow = client.newWorkflowStub(FileProcessingWorkflow.class,
          WorkflowOptions.newBuilder()
                  .setTaskQueue(taskQueue)
                  .setWorkflowId(workflowId)
                  .build());
    // use WorkflowClient.execute to return future that contains Workflow result or failure, or
    // use WorkflowClient.start to return WorkflowId and RunId of the started Workflow).
    WorkflowClient.start(workflow::greetCustomer);
    ```

  - **Untyped WorkflowStub Example**

    ```java
    WorkflowStub untyped = client.newUntypedWorkflowStub("FileProcessingWorkflow",
          WorkflowOptions.newBuilder()
                  .setWorkflowId(workflowId)
                  .setTaskQueue(taskQueue)
                  .build());

    // blocks until Workflow Execution has been started (not until it completes)
    untyped.start(argument);
    ```

You can call a Dynamic Workflow implementation using an untyped `WorkflowStub`. The following example shows how to call
the Dynamic Workflow implementation in the Client code.

```java
    WorkflowClient client = WorkflowClient.newInstance(service);
    /**
      * Note that for this part of the client code, the dynamic Workflow implementation must
      * be known to the Worker at runtime in order to dispatch Workflow tasks, and may be defined
      * in the Worker definition as:*/
    // worker.registerWorkflowImplementationTypes(DynamicGreetingWorkflowImpl.class);

    /* Create the Workflow stub to call the dynamic Workflow.
    * Note that the Workflow Type is not explicitly registered with the Worker.*/
    WorkflowOptions workflowOptions =
        WorkflowOptions.newBuilder().setTaskQueue(TASK_QUEUE).setWorkflowId(WORKFLOW_ID).build();
    WorkflowStub workflow = client.newUntypedWorkflowStub("DynamicWF", workflowOptions);
```

`DynamicWorkflow` can be used to invoke different Workflow Types. To check what type is running when your Dynamic
Workflow `execute` method runs, use `getWorkflowType()` in the implementation code.

```java
String type = Workflow.getInfo().getWorkflowType();
```

See [Workflow Execution Result](#get-workflow-results) for details on how to get the results of the Workflow Execution.

**Using `ExternalWorkflowStub`**

Use `ExternalWorkflowStub` within a Workflow to invoke, and send Signals to, other Workflows by type.

This helps particularly for executing Workflows written in other language SDKs, as shown in the following example.

```java
@Override
  public String yourWFMethod(String name) {
      ExternalWorkflowStub callOtherWorkflow = Workflow.newUntypedExternalWorkflowStub("OtherWFId");
    }
```

See the [Temporal Polyglot](https://github.com/tsurdilo/temporal-polyglot) code for examples of executing Workflows
written in other language SDKs.

**Recurring start**

You can start a Workflow Execution on a regular schedule by using
[`setCronSchedule`](/develop/java/workflows/schedules#cron-schedule) Workflow option in the Client code.

### How to set a Workflow's Task Queue {/* #set-task-queue */}

In most SDKs, the only Workflow Option that must be set is the name of the [Task Queue](/task-queue).

For your code to execute, a Worker Process must be running. This process needs a Worker Entity that is polling the same
Task Queue name.

Set the Workflow Task Queue with the
[`WorkflowStub`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/client/WorkflowStub.html)
instance in the Client code using
[`WorkflowOptions.Builder.setTaskQueue`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/client/WorkflowOptions.Builder.html).

- Type: `String`
- Default: none

```java
//create Workflow stub for YourWorkflowInterface
YourWorkflowInterface workflow1 =
    WorkerGreet.greetclient.newWorkflowStub(
        GreetWorkflowInterface.class,
        WorkflowOptions.newBuilder()
                .setWorkflowId("YourWF")
                // Set the Task Queue
                .setTaskQueue(WorkerGreet.TASK_QUEUE)
                .build());
```

### How to set a Workflow Id {/* #workflow-id */}

Although it is not required, we recommend providing your own
[Workflow Id](/workflow-execution/workflowid-runid#workflow-id) that maps to a business process or business entity
identifier, such as an order identifier or customer identifier.

Set the Workflow Id with the
[`WorkflowStub`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/client/WorkflowStub.html)
instance in the Client code using
[`WorkflowOptions.Builder.setWorkflowId​`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/client/WorkflowOptions.Builder.html).

- Type: `String`
- Default: none

```java
//create Workflow stub for YourWorkflowInterface
YourWorkflowInterface workflow1 =
    WorkerGreet.greetclient.newWorkflowStub(
        GreetWorkflowInterface.class,
        WorkflowOptions.newBuilder()
                // Set the Workflow Id
                .setWorkflowId("YourWF")
                .setTaskQueue(WorkerGreet.TASK_QUEUE)
                .build());
```

### Java WorkflowOptions reference {/* #workflow-options-reference */}

Create a
[`newWorkflowStub`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/client/WorkflowStub.html) in
the Temporal Client code, call the instance of the Workflow, and set the Workflow options with the
[`WorkflowOptions.Builder`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/client/WorkflowOptions.Builder.html)
class.

The following fields are available:

| Option                                                  | Required             | Type                                                                                                                 |
| ------------------------------------------------------- | -------------------- | -------------------------------------------------------------------------------------------------------------------- |
| [`WorkflowId`](#workflowid)                             | No (but recommended) | String                                                                                                               |
| [`TaskQueue`](#taskqueue)                               | **Yes**              | String                                                                                                               |
| [`WorkflowExecutionTimeout`](#workflowexecutiontimeout) | No                   | `Duration`                                                                                                           |
| [`WorkflowRunTimeout`](#workflowruntimeout)             | No                   | `Duration`                                                                                                           |
| [`WorkflowTaskTimeout`](#workflowtasktimeout)           | No                   | `Duration`                                                                                                           |
| [`WorkflowIdReusePolicy`](#workflowidreusepolicy)       | No                   | `WorkflowIdReusePolicy`                                                                                              |
| [`RetryOptions`](#retryoptions)                         | No                   | [`RetryOptions`](https://www.javadoc.io/static/io.temporal/temporal-sdk/1.17.0/io/temporal/common/RetryOptions.html) |
| [`CronSchedule`](#cronschedule)                         | No                   | String                                                                                                               |
| [`Memo`](#memo)                                         | No                   | string                                                                                                               |
| [`SearchAttributes`](#searchattributes)                 | No                   | `Map<String, Object>`                                                                                                |

#### WorkflowId

Set the Workflow Id with the
[`WorkflowStub`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/client/WorkflowStub.html)
instance in the Client code using
[`WorkflowOptions.Builder.setWorkflowId​`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/client/WorkflowOptions.Builder.html).

- Type: `String`
- Default: none

```java
//create Workflow stub for YourWorkflowInterface
YourWorkflowInterface workflow1 =
    WorkerGreet.greetclient.newWorkflowStub(
        GreetWorkflowInterface.class,
        WorkflowOptions.newBuilder()
                // Set the Workflow Id
                .setWorkflowId("YourWF")
                .setTaskQueue(WorkerGreet.TASK_QUEUE)
                .build());
```

#### TaskQueue

Set the Workflow Task Queue with the
[`WorkflowStub`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/client/WorkflowStub.html)
instance in the Client code using
[`WorkflowOptions.Builder.setTaskQueue`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/client/WorkflowOptions.Builder.html).

- Type: `String`
- Default: none

```java
//create Workflow stub for YourWorkflowInterface
YourWorkflowInterface workflow1 =
    WorkerGreet.greetclient.newWorkflowStub(
        GreetWorkflowInterface.class,
        WorkflowOptions.newBuilder()
                .setWorkflowId("YourWF")
                // Set the Task Queue
                .setTaskQueue(WorkerGreet.TASK_QUEUE)
                .build());
```

#### WorkflowExecutionTimeout

Set the [Workflow Execution Timeout](/encyclopedia/detecting-workflow-failures#workflow-execution-timeout) with the
[`WorkflowStub`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/client/WorkflowStub.html)
instance in the Client code using
[`WorkflowOptions.Builder.setWorkflowExecutionTimeout`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/client/WorkflowOptions.Builder.html).

- Type: `Duration`
- Default: Unlimited

```java
//create Workflow stub for YourWorkflowInterface
YourWorkflowInterface workflow1 =
    WorkerGreet.greetclient.newWorkflowStub(
        GreetWorkflowInterface.class,
        WorkflowOptions.newBuilder()
                .setWorkflowId("YourWF")
                .setTaskQueue(WorkerGreet.TASK_QUEUE)
                // Set Workflow Execution Timeout duration
                .setWorkflowExecutionTimeout(Duration.ofSeconds(10))
                .build());
```

#### WorkflowRunTimeout

Set the Workflow Run Timeout with the
[`WorkflowStub`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/client/WorkflowStub.html)
instance in the Client code using
