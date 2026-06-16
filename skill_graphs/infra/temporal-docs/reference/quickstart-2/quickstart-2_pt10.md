          // them, enabling workflows to run.
          // Since both operations are mocked with OperationHandler.sync, no backing workflow is
          // needed for hello — only the caller workflow types need to be registered.
          .registerWorkflowImplementationTypes(HelloCallerWorkflowImpl.class)
          // The workflow will start before each test, and will shut down after each test.
          // See CallerWorkflowTest for an example of how to control this differently if needed.
          .build();

  // The TestWorkflowExtension extension in the Temporal testing library creates the
  // arguments to the test cases and initializes them from the extension setup call above.
  @Test
  public void testHelloWorkflow(
      TestWorkflowEnvironment testEnv, Worker worker, HelloCallerWorkflow workflow) {

    // Set the mock value to return
    when(mockNexusService.hello(any()))
        .thenReturn(new SampleNexusService.HelloOutput("Hello Mock World"));

    // Execute a workflow waiting for it to complete.
    String greeting = workflow.hello("World", SampleNexusService.Language.EN);
    assertEquals("Hello Mock World", greeting);

    // Verify the operation was called exactly once and no other operations were invoked
    verify(mockNexusService, times(1)).hello(any());
    // Verify the Nexus service was called with the correct input
    verify(mockNexusService).hello(argThat(input -> "World".equals(input.getName())));

    verifyNoMoreInteractions(mockNexusService);
  }
}
```
<!--SNIPEND-->

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
For example, in the time-skipping mode, Timers, which include sleeps and conditional timeouts, are fast-forwarded except when Activities or Nexus Operation handlers are running. Nexus Operation handlers timeout after 10 seconds and time skipping is allowed while waiting for retries.

{/* #### Skip time manually {/* #manual-method */} */}

Skip time manually in the SDK of your choice.

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

To replay Workflow Executions, use the [WorkflowReplayer](https://www.javadoc.io/doc/io.temporal/temporal-testing/latest/io/temporal/testing/WorkflowReplayer.html) class in the `temporal-testing` package.

In the following example, Event Histories are downloaded from the server, and then replayed.
Note that this requires Advanced Visibility to be enabled.

```java
// Note we assume you already have a WorkflowServiceStubs (`service`) and WorkflowClient (`client`)
// in scope.
ListWorkflowExecutionsRequest listWorkflowExecutionRequest =
    ListWorkflowExecutionsRequest.newBuilder()
        .setNamespace(client.getOptions().getNamespace())
        .setQuery("TaskQueue = 'mytaskqueue'")
        .build();
ListWorkflowExecutionsResponse listWorkflowExecutionsResponse =
    service.blockingStub().listWorkflowExecutions(listWorkflowExecutionRequest);
List<WorkflowExecutionHistory> histories =
    listWorkflowExecutionsResponse.getExecutionsList().stream()
        .map(
            (info) -> {
              GetWorkflowExecutionHistoryResponse weh =
                  service.blockingStub().getWorkflowExecutionHistory(
                      GetWorkflowExecutionHistoryRequest.newBuilder()
                          .setNamespace(testEnvironment.getNamespace())
                          .setExecution(info.getExecution())
                          .build());
              return new WorkflowExecutionHistory(
                  weh.getHistory(), info.getExecution().getWorkflowId());
            })
        .collect(Collectors.toList());

WorkflowReplayer.replayWorkflowExecutions(
    histories, true, WorkflowA.class, WorkflowB.class, WorkflowC.class);
```

In the next example, a single history is loaded from a JSON file on disk:

```java
File file = new File("my_history.json");
WorkflowReplayer.replayWorkflowExecution(file, MyWorkflow.class);
```

In both examples, if Event History is non-deterministic, an error is thrown.
You can choose to wait until all histories have been replayed with `replayWorkflowExecutions` by setting the `failFast` argument to `false`.

---

## Client - Java SDK

![Java SDK Banner](/img/assets/banner-java-temporal.png)

## Temporal Client

- [Temporal Client](/develop/java/client/temporal-client)
- [Namespaces](/develop/java/client/namespaces)

---

## Namespaces - Java SDK

This page shows how to do the following:

- [Register a Namespace](#register-namespace)
- [Manage Namespaces](#manage-namespaces)

You can create, update, deprecate or delete your [Namespaces](/namespaces) using either the Temporal CLI or SDK APIs.

Use Namespaces to isolate your Workflow Executions according to your needs.
For example, you can use Namespaces to match the development lifecycle by having separate `dev` and `prod` Namespaces.
You could also use them to ensure Workflow Executions between different teams never communicate - such as ensuring that the `teamA` Namespace never impacts the `teamB` Namespace.

On Temporal Cloud, use the [Temporal Cloud UI](/cloud/namespaces#create-a-namespace) to create and manage a Namespace from the UI, or [tcld commands](https://docs.temporal.io/cloud/tcld/namespace/) to manage Namespaces from the command-line interface.

On self-hosted Temporal Service, you can register and manage your Namespaces using the Temporal CLI (recommended) or programmatically using APIs.
Note that these APIs and Temporal CLI commands will not work with Temporal Cloud.

Use a custom [Authorizer](/self-hosted-guide/security#authorizer-plugin) on your Frontend Service in the Temporal Service to set restrictions on who can create, update, or deprecate Namespaces.

You must register a Namespace with the Temporal Service before setting it in the Temporal Client.

## Register a Namespace {/* #register-namespace */}

Registering a Namespace creates a Namespace on the Temporal Service or Temporal Cloud.

On Temporal Cloud, use the [Temporal Cloud UI](/cloud/namespaces#create-a-namespace) or [tcld commands](https://docs.temporal.io/cloud/tcld/namespace/) to create Namespaces.

On self-hosted Temporal Service, you can register your Namespaces using the Temporal CLI (recommended) or programmatically using APIs.
Note that these APIs and Temporal CLI commands will not work with Temporal Cloud.

Use a custom [Authorizer](/self-hosted-guide/security#authorizer-plugin) on your Frontend Service in the Temporal Service to set restrictions on who can create, update, or deprecate Namespaces.

Use the [`RegisterNamespace` API](https://github.com/temporalio/api/blob/f0350f8032ad2f0c60c539b3b61ea37f412f1cf7/temporal/api/workflowservice/v1/service.proto) to register a [Namespace](/namespaces) and set the [Retention Period](/temporal-service/temporal-server#retention-period) for the Workflow Execution Event History for the Namespace.

```java
//...

//...
public static void createNamespace(String name) {
    RegisterNamespaceRequest req = RegisterNamespaceRequest.newBuilder()
            .setNamespace("your-custom-namespace")
            .setWorkflowExecutionRetentionPeriod(Durations.fromDays(3)) // keeps the Workflow Execution
            //Event History for up to 3 days in the Persistence store. Not setting this value will throw an error.
            .build();
    service.blockingStub().registerNamespace(req);
}
//...
```

The Retention Period setting using `WorkflowExecutionRetentionPeriod` is mandatory.
The minimum value you can set for this period is 1 day.

Once registered, set Namespace using `WorkflowClientOptions` within a Workflow Client to run your Workflow Executions within that Namespace.
See [Connect to a Development Temporal Service](/develop/java/client/temporal-client#connect-to-development-service) for details.

Note that Namespace registration using this API takes up to 10 seconds to complete.
Ensure that you wait for this registration to complete before starting the Workflow Execution against the Namespace.

To update your Namespace use the [UpdateNamespace API](#manage-namespaces) with the NamespaceClient.

## Manage Namespaces {/* #manage-namespaces */}

You can get details for your Namespaces, update Namespace configuration, and deprecate or delete your Namespaces.

On Temporal Cloud, use the [Temporal Cloud UI](/cloud/namespaces#create-a-namespace) or [tcld commands](https://docs.temporal.io/cloud/tcld/namespace/) to manage Namespaces.

On self-hosted Temporal Service, you can manage your registered Namespaces using the Temporal CLI (recommended) or programmatically using APIs.
Note that these APIs and Temporal CLI commands will not work with Temporal Cloud.

Use a custom [Authorizer](/self-hosted-guide/security#authorizer-plugin) on your Frontend Service in the Temporal Service to set restrictions on who can create, update, or deprecate Namespaces.

You must register a Namespace with the Temporal Service before setting it in the Temporal Client.

On Temporal Cloud, use the [Temporal Cloud UI](/cloud/namespaces) or [tcld commands](https://docs.temporal.io/cloud/tcld/namespace/) to manage Namespaces.

On self-hosted Temporal Service, you can manage your registered Namespaces using the Temporal CLI (recommended) or programmatically using APIs.
Note that these APIs and Temporal CLI commands will not work with Temporal Cloud.

- Update information and configuration for a registered Namespace on your Temporal Service:

  - With the Temporal CLI: [`temporal operator namespace update`](/cli/command-reference/operator#update)
    Example
  - Use the [`UpdateNamespace` API](https://github.com/temporalio/api/blob/e5cf521c6fdc71c69353f3d2ac5506dd6e827af8/temporal/api/workflowservice/v1/service.proto) to update configuration on a Namespace.
    Example

  ```java

  //...
  UpdateNamespaceRequest updateNamespaceRequest = UpdateNamespaceRequest.newBuilder()
              .setNamespace("your-namespace-name") //the namespace that you want to update
              .setUpdateInfo(UpdateNamespaceInfo.newBuilder() //has options to update namespace info
                      .setDescription("your updated namespace description") //updates description in the namespace info.
                      .build())
              .setConfig(NamespaceConfig.newBuilder() //has options to update namespace configuration
                      .setWorkflowExecutionRetentionTtl(Durations.fromHours(30)) //updates the retention period for the namespace "your-namespace--name" to 30 hrs.
                      .build())
              .build();
      UpdateNamespaceResponse updateNamespaceResponse = namespaceservice.blockingStub().updateNamespace(updateNamespaceRequest);
  //...
  ```

- Get details for a registered Namespace on your Temporal Service:

  - With the Temporal CLI: [`temporal operator namespace describe`](/cli/command-reference/operator#describe)
  - Use the [`DescribeNamespace` API](https://github.com/temporalio/api/blob/e5cf521c6fdc71c69353f3d2ac5506dd6e827af8/temporal/api/workflowservice/v1/service.proto) to return information and configuration details for a registered Namespace.
    Example

  ```java

  //...
  DescribeNamespaceRequest descNamespace = DescribeNamespaceRequest.newBuilder()
              .setNamespace("your-namespace-name") //specify the namespace you want details for
              .build();
      DescribeNamespaceResponse describeNamespaceResponse = namespaceservice.blockingStub().describeNamespace(descNamespace);
      System.out.println("Namespace Description: " + describeNamespaceResponse);
  //...
  ```

- Get details for all registered Namespaces on your Temporal Service:

  - With the Temporal CLI: [`temporal operator namespace list`](/cli/command-reference/operator#list)
  - Use the [`ListNamespace` API](https://github.com/temporalio/api/blob/e5cf521c6fdc71c69353f3d2ac5506dd6e827af8/temporal/api/workflowservice/v1/service.proto) to return information and configuration details for all registered Namespaces on your Temporal Service.
    Example

  ```java

  //...
  ListNamespacesRequest listNamespaces = ListNamespacesRequest.newBuilder().build();
      ListNamespacesResponse listNamespacesResponse = namespaceservice.blockingStub().listNamespaces(listNamespaces); //lists 1-100 namespaces (1 page) in the active Temporal Service. To list all, set the page size or loop until NextPageToken is nil.
  //...
  ```

- Deprecate a Namespace: The [`DeprecateNamespace` API](https://github.com/temporalio/api/blob/e5cf521c6fdc71c69353f3d2ac5506dd6e827af8/temporal/api/workflowservice/v1/service.proto) updates the state of a registered Namespace to "DEPRECATED". Once a Namespace is deprecated, you cannot start new Workflow Executions on it. All existing and running Workflow Executions on a deprecated Namespace will continue to run.
  Example:

  ```java

  //...
  DeprecateNamespaceRequest deprecateNamespace = DeprecateNamespaceRequest.newBuilder()
              .setNamespace("your-namespace-name") //specify the namespace that you want to deprecate
              .build();
      DeprecateNamespaceResponse response = namespaceservice.blockingStub().deprecateNamespace(deprecateNamespace);
  //...
  ```

- Delete a Namespace: The [`DeleteNamespace` API](https://github.com/temporalio/api/blob/e5cf521c6fdc71c69353f3d2ac5506dd6e827af8/temporal/api/workflowservice/v1/service.proto) deletes a Namespace. Deleting a Namespace deletes all running and completed Workflow Executions on the Namespace, and removes them from the persistence store and the visibility store.

  Example:

  ```java
  //...
  DeleteNamespaceResponse res =
  OperatorServiceStubs.newServiceStubs(OperatorServiceStubsOptions.newBuilder()
          .setChannel(service.getRawChannel())
          .validateAndBuildWithDefaults())
      .blockingStub()
      .deleteNamespace(DeleteNamespaceRequest.newBuilder().setNamespace("your-namespace-name").build());
  //...
  ```

---

## Temporal Client - Java SDK

A [Temporal Client](/encyclopedia/temporal-sdks#temporal-client) enables you to communicate with the
[Temporal Service](/temporal-service). Communication with a Temporal Service lets you perform actions such as starting
Workflow Executions, sending Signals to Workflow Executions, sending Queries to Workflow Executions, getting the results
of a Workflow Execution, and providing Activity Task Tokens.

This page shows you how to do the following using the Java SDK with the Temporal Client:

- [Connect to a local development Temporal Service](#connect-to-development-service)
- [Connect to Temporal Cloud](#connect-to-temporal-cloud)
- [Start a Workflow Execution](#start-workflow-execution)
- [Get Workflow results](#get-workflow-results)

:::caution

A Temporal Client cannot be initialized and used inside a Workflow. However, it is acceptable and common to use a
Temporal Client inside an Activity to communicate with a Temporal Service.

:::

## Connect to a development Temporal Service {/* #connect-to-development-service */}

Use the `newLocalServiceStubs` method to create a stub that points to the Temporal development service, and then use the
[`WorkflowClient.newInstance` method](https://javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/client/WorkflowClient.html#newInstance(io.temporal.serviceclient.WorkflowServiceStubs))
to create a Temporal Client.

<!--SNIPSTART javasdk-build-caller-app-using-local-client {"selectedLines": ["11-17"], "highlightedLines": ["3","7"]}-->
[sample-apps/java/client/devserver-client-sample/src/main/java/clientsample/YourCallerApp.java](https://github.com/temporalio/documentation/blob/main/sample-apps/java/client/devserver-client-sample/src/main/java/clientsample/YourCallerApp.java)
```java {3,7}
// ...
        // Create an instance that connects to a Temporal Service running on the local
        // machine, using the default port (7233)
        WorkflowServiceStubs serviceStub = WorkflowServiceStubs.newLocalServiceStubs();

        // Initialize the Temporal Client
        // This application uses the Client to communicate with the local Temporal Service
        WorkflowClient client = WorkflowClient.newInstance(serviceStub);
```
<!--SNIPEND-->

When you create a new Client with an instance of `newLocalServiceStubs`, the Client connects to the default local port
at port 7233. When you don't specify a custom Namespace, the Client connects to the `default` Namespace.

To connect to a custom Namespace, use the `WorkflowClientOptions.Builder.setNamespace` method to set the Namespace. Then
pass the `clientOptions` to the `WorkflowClient.newInstance` method.

<Tabs groupId="connect-options" defaultValue="config-file" >

<TabItem value="config-file" label="Configuration File">

You can use a TOML configuration file to set connection options for the Temporal Client. The configuration file lets you
configure multiple profiles, each with its own set of connection options. You can then specify which profile to use when
creating the Temporal Client. You can use the environment variable `TEMPORAL_CONFIG_FILE` to specify the location of the
TOML file or provide the path to the file directly in code. If you don't provide the configuration file path, the SDK
looks for it at the path `~/.config/temporalio/temporal.toml`. For a list of all available configuration options, refer
to [Environment Configuration](/references/client-environment-configuration)

:::info

The connection options set in configuration files have lower precedence than environment variables. This means that if
you set the same option in both the configuration file and as an environment variable, the environment variable value
overrides the option set in the configuration file.

:::

For example, the following TOML configuration file defines two profiles: `default` and `prod`. Each profile has its own
set of connection options.

```toml
