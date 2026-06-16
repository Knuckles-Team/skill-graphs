You can set multiple encoding Payload Converters to run your conversions.
When the Data Converter receives a value for conversion, it passes through each Payload Converter in sequence until the converter that handles the data type does the conversion.

Payload Converters can be customized independently of a Payload Codec.
Temporal's Converter architecture looks like this:

<CaptionedImage
    src="/img/info/converter-architecture.png"
    title="Temporal converter architecture"
/>

Create a custom implementation of a [PayloadConverter](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/common/converter/PayloadConverter.html) interface and use the `withPayloadConverterOverrides` method to implement the custom object conversion with `DefaultDataConverter`.

`PayloadConverter` serializes and deserializes method parameters that need to be sent over the wire.
You can create a custom implementation of `PayloadConverter` for custom formats, as shown in the following example:

```java
/** Payload Converter specific to your custom object */
public class YourCustomPayloadConverter implements PayloadConverter {
 //...
  @Override
  public String getEncodingType() {
    return "json/plain"; // The encoding type determines which default conversion behavior to override.
  }

  @Override
  public Optional<Payload> toData(Object value) throws DataConverterException {
      // Add your convert-to logic here.
  }

  @Override
  public <T> T fromData(Payload content, Class<T> valueClass, Type valueType)
      throws DataConverterException {
    // Add your convert-from logic here.
  }
//...
}
```

You can also use [specific implementation classes](https://www.javadoc.io/static/io.temporal/temporal-sdk/1.18.1/io/temporal/common/converter/package-summary.html) provided in the Java SDK.

For example, to create a custom `JacksonJsonPayloadConverter`, use the following:

```java
//...
private static JacksonJsonPayloadConverter yourCustomJacksonJsonPayloadConverter() {
  ObjectMapper objectMapper = new ObjectMapper();
  // Add your custom logic here.
  return new JacksonJsonPayloadConverter(objectMapper);
}
//...
```

To set your custom Payload Converter, use it with [withPayloadConverterOverrides](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/common/converter/DefaultDataConverter.html#withPayloadConverterOverrides(io.temporal.common.converter.PayloadConverter...)) with a new instance of `DefaultDataConverter` in your `WorkflowClient` options that you use in your Worker process and to start your Workflow Executions.

The following example shows how to set a custom `YourCustomPayloadConverter` Payload Converter.

```java
//...
DefaultDataConverter ddc =
        DefaultDataConverter.newDefaultInstance()
            .withPayloadConverterOverrides(new YourCustomPayloadConverter());

    WorkflowClientOptions workflowClientOptions =
        WorkflowClientOptions.newBuilder().setDataConverter(ddc).build();
//...
```

---

## Debugging - Java SDK

In addition to writing unit and integration tests, debugging your Workflows is also a very valuable testing tool.
You can debug your Workflow code using a debugger provided by your favorite Java IDE.

Note that when debugging your Workflow code, the Temporal Java SDK includes deadlock detection which fails a Workflow Task in case the code blocks over a second without relinquishing execution control.
Because of this you can often encounter the `PotentialDeadlockException` Exception while stepping through Workflow code during debugging.

To alleviate this issue, you can set the `TEMPORAL_DEBUG` environment variable to true before debugging your Workflow code. Make sure to set `TEMPORAL_DEBUG` to true only during debugging.

## How to debug in a development environment {/* #debug-in-a-development-environment */}

In addition to the normal development tools of logging and a debugger, you can also see what's happening in your Workflow by using the [Web UI](/web-ui) or [Temporal CLI](/cli).

## How to debug in a production environment {/* #debug-in-a-production-environment */}

You can debug production Workflows using:

- [Web UI](/web-ui)
- [Temporal CLI](/cli)
- [Replay](/develop/java/best-practices/testing-suite#replay)
- [Tracing](/develop/java/platform/observability#tracing)
- [Logging](/develop/java/platform/observability#logging)

You can debug and tune Worker performance with metrics and the [Worker performance guide](/develop/worker-performance).
For more information, see [Observability ▶️ Metrics](/develop/java/platform/observability#metrics) for setting up SDK metrics.

Debug Server performance with [Cloud metrics](/cloud/metrics/) or [self-hosted Server metrics](/self-hosted-guide/production-checklist#scaling-and-metrics).

---

## Best practices - Java SDK

![Java SDK Banner](/img/assets/banner-java-temporal.png)

## Best practices

- [Testing](/develop/java/best-practices/testing-suite)
- [Debugging](/develop/java/best-practices/debugging)
- [Converters and encryption](/develop/java/best-practices/converters-and-encryption)

---

## Testing - Java SDK

The Testing section of the Temporal Application development guide describes the frameworks that facilitate Workflow and integration testing.

In the context of Temporal, you can create these types of automated tests:

- **End-to-end:** Running a Temporal Server and Worker with all its Workflows, Activities, and Nexus Operations; starting and interacting with Workflows from a Client.
- **Integration:** Anything between end-to-end and unit testing.
  - Running Activities with mocked Context and other SDK imports (and usually network requests).
  - Running Workers with mock Activities and Nexus Operations, and using a Client to start Workflows.
  - Running Workflows with mocked SDK imports.
- **Unit:** Running a piece of Workflow, Activity, or Nexus Operation code (a function or method) and mocking any code it calls.

We generally recommend writing the majority of your tests as integration tests.

Because the test server supports skipping time, use the test server for both end-to-end and integration tests with Workers.

## Test frameworks {/* #test-frameworks */}

The Temporal Java SDK provides a test framework to facilitate Workflow unit and integration testing.
The test framework provides a `TestWorkflowEnvironment` class which includes an in-memory implementation
of the Temporal service that supports automatic time skipping. This allows you to
easily test long-running Workflows in seconds, without having to change your Workflow code.

You can use the provided `TestWorkflowEnvironment` with a Java unit testing framework of your choice,
such as JUnit.

### Setup testing dependency

To start using the Java SDK test framework, you need to add [`io.temporal:temporal-testing`](https://search.maven.org/artifact/io.temporal/temporal-testing)
as a dependency to your project:

**[Apache Maven](https://maven.apache.org/):**

```maven
<dependency>
    <groupId>io.temporal</groupId>
    <artifactId>temporal-testing</artifactId>
    <version>1.17.0</version>
    <scope>test</scope>
</dependency>
```

**[Gradle Groovy DSL](https://gradle.org/):**

```groovy
testImplementation ("io.temporal:temporal-testing:1.17.0")
```

Make sure to set the version that matches your dependency version of the [Temporal Java SDK](https://github.com/temporalio/sdk-java).

### Sample unit tests

The following code implements unit tests for the `HelloActivity` sample:

```java
public class HelloActivityTest {

    private TestWorkflowEnvironment testEnv;
    private Worker worker;
    private WorkflowClient client;

    // Set up the test workflow environment
    @Before
    public void setUp() {
        testEnv = TestWorkflowEnvironment.newInstance();
        worker = testEnv.newWorker(TASK_QUEUE);
        // Register your workflow implementations
        worker.registerWorkflowImplementationTypes(GreetingWorkflowImpl.class);

        client = testEnv.getWorkflowClient();
    }

    // Clean up test environment after tests are completed
    @After
    public void tearDown() {
        testEnv.close();
    }

    @Test
    public void testActivityImpl() {
        // This uses the actual activity impl
        worker.registerActivitiesImplementations(new GreetingActivitiesImpl());

        // Start test environment
        testEnv.start();

        // Create the workflow stub
        GreetingWorkflow workflow =
                client.newWorkflowStub(
                        GreetingWorkflow.class, WorkflowOptions.newBuilder().setTaskQueue(TASK_QUEUE).build());

        // Execute our workflow waiting for it to complete
        String greeting = workflow.getGreeting("World");
        assertEquals("Hello World!", greeting);
    }
}
```

In cases where you do not wish to execute your actual Activity or Nexus Operation implementations during
unit testing, you can use a framework such as Mockito to mock them.

The following code implements a unit test for the `HelloActivity` sample which shows
how activities can be mocked:

```java
public class HelloActivityTest {

    private TestWorkflowEnvironment testEnv;
    private Worker worker;
    private WorkflowClient client;

    // Set up the test workflow environment
    @Before
    public void setUp() {
        testEnv = TestWorkflowEnvironment.newInstance();
        worker = testEnv.newWorker(TASK_QUEUE);
        // Register your workflow implementations
        worker.registerWorkflowImplementationTypes(GreetingWorkflowImpl.class);

        client = testEnv.getWorkflowClient();
    }

    // Clean up test environment after tests are completed
    @After
    public void tearDown() {
        testEnv.close();
    }

    @Test
    public void testMockedActivity() {
        // Mock our workflow activity
        GreetingActivities activities = mock(GreetingActivities.class);
        when(activities.composeGreeting("Hello", "World")).thenReturn("Hello Mocked World!");
        worker.registerActivitiesImplementations(activities);

        // Start test environment
        testEnv.start();

        // Create the workflow stub
        GreetingWorkflow workflow =
                client.newWorkflowStub(
                        GreetingWorkflow.class, WorkflowOptions.newBuilder().setTaskQueue(TASK_QUEUE).build());

        // Execute our workflow waiting for it to complete
        String greeting = workflow.getGreeting("World");
        assertEquals("Hello Mocked World!", greeting);
    }
}
```

### Testing with JUnit4

For Junit4 tests, Temporal provides the TestWorkflowRule class which simplifies the Temporal test environment setup, as well as the
creation and shutdown of Workflow Workers in your tests.

Make sure to set the version that matches your dependency version of the [Temporal Java SDK](https://github.com/temporalio/sdk-java).

We can now rewrite our above mentioned "HelloActivityTest" test class as follows:

```java
public class HelloActivityJUnit4Test {
    @Rule
    public TestWorkflowRule testWorkflowRule =
            TestWorkflowRule.newBuilder()
                    .setWorkflowTypes(GreetingWorkflowImpl.class)
                    .setActivityImplementations(new GreetingActivitiesImpl())
                    .build();

    @Test
    public void testActivityImpl() {
        // Get a workflow stub using the same task queue the worker uses.
        GreetingWorkflow workflow =
                testWorkflowRule
                        .getWorkflowClient()
                        .newWorkflowStub(
                                GreetingWorkflow.class,
                                WorkflowOptions.newBuilder().setTaskQueue(testWorkflowRule.getTaskQueue()).build());
        // Execute a workflow waiting for it to complete.
        String greeting = workflow.getGreeting("World");
        assertEquals("Hello World!", greeting);

        testWorkflowRule.getTestEnvironment().shutdown();
    }
}
```

### Testing with JUnit5

For Junit5 tests, Temporal also provides the TestWorkflowExtension helper class.
This class can be used to simplify the Temporal test environment setup as well as Workflow Worker startup and shutdowns.

To start using JUnit5 TestWorkflowExtension in your tests with [Gradle](https://gradle.org/), you need to enable capability [`io.temporal:temporal-testing-junit5`]:

Make sure to set the version that matches your dependency version of the [Temporal Java SDK](https://github.com/temporalio/sdk-java).

We can now use JUnit5 and rewrite our above mentioned "HelloActivityTest" test class as follows:

```java
public class HelloActivityJUnit5Test {
    @RegisterExtension
    public static final TestWorkflowExtension testWorkflowExtension =
            TestWorkflowExtension.newBuilder()
                    .setWorkflowTypes(GreetingWorkflowImpl.class)
                    .setActivityImplementations(new GreetingActivitiesImpl())
                    .build();

    @Test
    public void testActivityImpl(
            TestWorkflowEnvironment testEnv, Worker worker, GreetingWorkflow workflow) {
        // Execute a workflow waiting for it to complete.
        String greeting = workflow.getGreeting("World");
        assertEquals("Hello World!", greeting);
    }
}
```

You can find all unit tests for the [Temporal Java samples](https://github.com/temporalio/samples-java) repository in [its test package](https://github.com/temporalio/samples-java/tree/main/core/src/test/java/io/temporal/samples).

## Test Activities {/* #test-activities */}

Mocking isolates code undergoing testing so the focus remains on the code, and not on external dependencies or other state. You can test Activities using a mocked Activity environment.

This approach offers a way to mock the Activity context, listen to Heartbeats, and cancel the Activity. You test the Activity in isolation, calling it directly without needing to create a Worker to run it.

Temporal provides the `TestActivityEnvironment` and `TestActivityExtension` classes for testing Activities outside the scope of a Workflow. Testing
Activities are similar to testing non-Temporal Java code.

For example, you can test an Activity for:

- Exceptions thrown when invoking the Activity Execution.
- Exceptions thrown when checking for the result of the Activity Execution.
- Activity's return values. Check that the return value matches the expected value.

### Run an Activity {/* #run-an-activity */}

During isolation testing, if an Activity references its context, you'll need to mock that context.
Mocked information stands in for the context, allowing you to focus your testing on the Activity's code.

### Listen to Heartbeats {/* #listen-to-heartbeats */}

Activities usually issue periodic Heartbeats, a feature that broadcasts recurring proof-of-life updates.
Each ping shows that an Activity is making progress and the Worker hasn't crashed.
Heartbeats may include details that report task progress in the event an Activity Worker crashes.

When testing Activities that support Heartbeats, make sure you can see those Heartbeats in your test code.
Provide appropriate test coverage.
This enables you to verify both the Heartbeat's content and behavior.

### Cancel an Activity {/* #cancel-an-activity */}

Activity cancellation lets Activities know they don't need to continue work and gives time for the Activity to clean up any resources it's created. You can cancel Java-based activities if they emit Heartbeats. To test an Activity that reacts to Cancellations, make sure that the Activity reacts correctly and cancels.

## Testing Workflows {/* #test-workflows */}

### How to mock Activities {/* #mock-activities */}

Mock the Activity invocation when unit testing your Workflows.

When integration testing Workflows with a Worker, you can mock Activities by providing mock Activity implementations to the Worker.
For more details on mocking activities, see [sample unit tests](#sample-unit-tests).

### How to mock Nexus Operations {/* #mock-nexus-operations */}

When integration testing Workflows with a Worker, you can mock Nexus operations by providing mock Nexus Service handlers to the Worker.
Alternatively, you could just mock the Nexus service itself.

You can find example unit tests for Nexus in the [Temporal Java samples](https://github.com/temporalio/samples-java) repository in [this test package](https://github.com/temporalio/samples-java/tree/main/core/src/test/java/io/temporal/samples/nexus/caller).
These samples show how to call Nexus services in tests using the Temporal testing package and also how to mock them, for both JUnit 4 and 5.
Detailed explanatory comments are included in the code in the repository.

To mock Nexus handlers, create a Rule (for JUnit4) or Extension (for JUnit5) from the Temporal testing package, just as in the [sample unit tests](#sample-unit-tests) and add a call to `setNexusServiceImplementation` to the builder.
That sets up the Nexus endpoints needed for testing as well as the Nexus handler workflows defined by the Nexus Service implementation.
Everything is created and set up by the Temporal Testing package, so no more work is needed than that!

You will need to create workers for each handler just as normal, using either `setWorkflowTypes` (for JUnit4) or `registerWorkflowImplementationTypes` (for JUnit5).
With that in place, you can then mock a Nexus endpoint exactly like any other workflow - again, just as in [the sample unit tests](#sample-unit-tests) above.

The following are samples derived from [the test package](https://github.com/temporalio/samples-java/tree/main/core/src/test/java/io/temporal/samples/nexus/caller) to demonstrate this.

#### Mocking Nexus handlers with JUnit4
{/* SNIPSTART java-nexus-sample-junit4-mock */}
[core/src/test/java/io/temporal/samples/nexus/caller/CallerWorkflowMockTest.java](https://github.com/temporalio/samples-java/blob/main/core/src/test/java/io/temporal/samples/nexus/caller/CallerWorkflowMockTest.java)
```java
public class CallerWorkflowMockTest {
  @Rule
  public TestWorkflowRule testWorkflowRule =
      TestWorkflowRule.newBuilder()
          .setNexusServiceImplementation(new SampleNexusServiceImpl())
          .setWorkflowTypes(HelloCallerWorkflowImpl.class)
          .build();

  @Test
  public void testHelloWorkflow() {
    testWorkflowRule
        .getWorker()
        // Workflows started by a Nexus service can be mocked just like any other workflow
        .registerWorkflowImplementationFactory(
            HelloHandlerWorkflow.class,
            () -> {
              HelloHandlerWorkflow wf = mock(HelloHandlerWorkflow.class);
              when(wf.hello(any())).thenReturn(new SampleNexusService.HelloOutput("Hello Mock World"));
              return wf;
            });

    // Now create the caller workflow
    HelloCallerWorkflow workflow =
        testWorkflowRule
            .getWorkflowClient()
            .newWorkflowStub(
                HelloCallerWorkflow.class,
                WorkflowOptions.newBuilder().setTaskQueue(testWorkflowRule.getTaskQueue()).build());
    String greeting = workflow.hello("World", SampleNexusService.Language.EN);
    assertEquals("Hello Mock World", greeting);

  }
}
```
<!--SNIPEND-->

#### Mocking Nexus handlers with JUnit5
{/* SNIPSTART java-nexus-sample-junit5-mock */}
[core/src/test/java/io/temporal/samples/nexus/caller/CallerWorkflowJunit5MockTest.java](https://github.com/temporalio/samples-java/blob/main/core/src/test/java/io/temporal/samples/nexus/caller/CallerWorkflowJunit5MockTest.java)
```java
public class CallerWorkflowJunit5MockTest {

  @RegisterExtension
  public static final TestWorkflowExtension testWorkflowExtension =
      TestWorkflowExtension.newBuilder()
          // Register the Nexus service as usual and mock things in the unit tests as needed
          .setNexusServiceImplementation(new SampleNexusServiceImpl())
          .registerWorkflowImplementationTypes(HelloCallerWorkflowImpl.class)
          .build();

  @Test
  public void testHelloWorkflow(
          TestWorkflowEnvironment testEnv, Worker worker, HelloCallerWorkflow workflow) {
    // Workflows started by a Nexus service can be mocked just like any other workflow
    worker.registerWorkflowImplementationFactory(
        HelloHandlerWorkflow.class,
        () -> {
          HelloHandlerWorkflow mockHandler = mock(HelloHandlerWorkflow.class);
          when(mockHandler.hello(any()))
              .thenReturn(new SampleNexusService.HelloOutput("Hello Mock World"));
          return mockHandler;
        });

    // Execute a workflow waiting for it to complete.
    String greeting = workflow.hello("World", SampleNexusService.Language.EN);
    assertEquals("Hello Mock World", greeting);
  }
}
```
<!--SNIPEND-->

An alternative approach is to simply mock the Nexus service itself, instead of mocking the handlers.
This is useful if you just want to test the calling logic but can't easily mock the Nexus handlers.

The code will just mock the implementation of the SampleNexusService class with the handler methods, but will need those methods stubbed in for the testing framework.
Those methods can be directly mocked with static return values, or else they can return an instance variable which each unit test can modify to return a desired value.

#### Mocking the Nexus Service with JUnit4
{/* SNIPSTART java-nexus-service-sample-junit4-mock */}
[core/src/test/java/io/temporal/samples/nexus/caller/NexusServiceMockTest.java](https://github.com/temporalio/samples-java/blob/main/core/src/test/java/io/temporal/samples/nexus/caller/NexusServiceMockTest.java)
```java
public class NexusServiceMockTest {

  private final SampleNexusService mockNexusService = mock(SampleNexusService.class);

  /**
   * A test-only Nexus service implementation that delegates to the Mockito mock defined above. The
   * operation is implemented as a synchronous handler that forward calls to the mock, allowing
   * full control over return values and verification of inputs.
   */
  @ServiceImpl(service = SampleNexusService.class)
  public class TestNexusServiceImpl {

    @OperationImpl
    @SuppressWarnings("DirectInvocationOnMock")
    public OperationHandler<SampleNexusService.HelloInput, SampleNexusService.HelloOutput> hello() {
      return OperationHandler.sync((ctx, details, input) -> mockNexusService.hello(input));
    }
  }

  // Using OperationHandler.sync for the operation bypasses the need for a backing workflow,
  // returning results inline just like a synchronous call.

  @Rule
  public TestWorkflowRule testWorkflowRule =
      TestWorkflowRule.newBuilder()
          .setNexusServiceImplementation(new TestNexusServiceImpl())
          .setWorkflowTypes(HelloCallerWorkflowImpl.class)
          .build();

  @Test
  public void testHelloCallerWithMockedService() {
    when(mockNexusService.hello(any()))
        .thenReturn(new SampleNexusService.HelloOutput("Bonjour World"));

    HelloCallerWorkflow workflow =
        testWorkflowRule
            .getWorkflowClient()
            .newWorkflowStub(
                HelloCallerWorkflow.class,
                WorkflowOptions.newBuilder().setTaskQueue(testWorkflowRule.getTaskQueue()).build());

    String result = workflow.hello("World", SampleNexusService.Language.FR);
    assertEquals("Bonjour World", result);

    // Verify the Nexus service was called with the correct name and language
    verify(mockNexusService)
        .hello(
            argThat(
                input ->
                    "World".equals(input.getName())
                        && SampleNexusService.Language.FR == input.getLanguage()));

    // Verify the operation was called exactly once and no other operations were invoked
    verify(mockNexusService, times(1)).hello(any());
  }
}
```
<!--SNIPEND-->

#### Mocking the Nexus Service with JUnit5
{/* SNIPSTART java-nexus-service-sample-junit5-mock */}
[core/src/test/java/io/temporal/samples/nexus/caller/NexusServiceJunit5Test.java](https://github.com/temporalio/samples-java/blob/main/core/src/test/java/io/temporal/samples/nexus/caller/NexusServiceJunit5Test.java)
```java
public class NexusServiceJunit5Test {

  private final SampleNexusService mockNexusService = mock(SampleNexusService.class);

  /**
   * A test-only Nexus service implementation that delegates to the Mockito mock defined above. The
   * operation is implemented as a synchronous handler that forward calls to the mock, allowing
   * full control over return values and verification of inputs.
   */
  @ServiceImpl(service = SampleNexusService.class)
  public class TestNexusServiceImpl {

    @OperationImpl
    @SuppressWarnings("DirectInvocationOnMock")
    public OperationHandler<SampleNexusService.HelloInput, SampleNexusService.HelloOutput> hello() {
      return OperationHandler.sync((ctx, details, input) -> mockNexusService.hello(input));
    }
  }

  // Using OperationHandler.sync for both operations bypasses the need for a backing workflow,
  // returning results inline just like a synchronous call.

  @RegisterExtension
  public final TestWorkflowExtension testWorkflowExtension =
      TestWorkflowExtension.newBuilder()
          // If a Nexus service is registered as part of the test as in the following line of code,
          // the TestWorkflowExtension will, by default, automatically create a Nexus service
          // endpoint and workflows registered as part of the TestWorkflowExtension will
          // automatically inherit the endpoint if none is set.
          .setNexusServiceImplementation(new TestNexusServiceImpl())
          // registerWorkflowImplementationTypes will take the classes given and create workers for
