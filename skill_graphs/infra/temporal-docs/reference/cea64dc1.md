[`WorkflowOptions.Builder.setWorkflowRunTimeout`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/client/WorkflowOptions.Builder.html).

- Type: `Duration`
- Default: Same as [WorkflowExecutionTimeout](#workflowexecutiontimeout).

```java
//create Workflow stub for YourWorkflowInterface
YourWorkflowInterface workflow1 =
    WorkerGreet.greetclient.newWorkflowStub(
        GreetWorkflowInterface.class,
        WorkflowOptions.newBuilder()
                .setWorkflowId("YourWF")
                .setTaskQueue(WorkerGreet.TASK_QUEUE)
                // Set Workflow Run Timeout duration
                .setWorkflowRunTimeout(Duration.ofSeconds(10))
                .build());
```

#### WorkflowTaskTimeout

Set the Workflow Task Timeout with the
[`WorkflowStub`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/client/WorkflowStub.html)
instance in the Client code using
[`WorkflowOptions.Builder.setWorkflowTaskTimeout`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/client/WorkflowOptions.Builder.html).

- Type: `Duration`
- Default: 10 seconds.
- Values: Maximum accepted value is 60 seconds.

```java
//create Workflow stub for YourWorkflowInterface
YourWorkflowInterface workflow1 =
    WorkerGreet.greetclient.newWorkflowStub(
        GreetWorkflowInterface.class,
        WorkflowOptions.newBuilder()
                .setWorkflowId("YourWF")
                .setTaskQueue(WorkerGreet.TASK_QUEUE)
                // Set Workflow Task Timeout duration
                .setWorkflowTaskTimeout(Duration.ofSeconds(10))
                .build());
```

#### WorkflowIDReusePolicy

- Type: `WorkflowIdReusePolicy`
- Default: `AllowDuplicate`
- Values:
  - `enums.AllowDuplicateFailedOnly`: The Workflow can start if the earlier Workflow Execution failed, Canceled, or
    Terminated.
  - `AllowDuplicate`: The Workflow can start regardless of the earlier Execution's closure status.
  - `RejectDuplicate`: The Workflow can not start if there is a earlier Run.

```java
//create Workflow stub for GreetWorkflowInterface
GreetWorkflowInterface workflow1 =
    WorkerGreet.greetclient.newWorkflowStub(
        GreetWorkflowInterface.class,
        WorkflowOptions.newBuilder()
                .setWorkflowId("GreetWF")
                .setTaskQueue(WorkerGreet.TASK_QUEUE)
                // Set Workflow Id Reuse Policy
                .setWorkflowIdReusePolicy(
                        WorkflowIdReusePolicy.WORKFLOW_ID_REUSE_POLICY_REJECT_DUPLICATE)
                .build());
```

#### RetryOptions

To set a Workflow Retry Options in the
[`WorkflowStub`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/client/WorkflowStub.html)
instance use
[`WorkflowOptions.Builder.setWorkflowRetryOptions`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/client/WorkflowOptions.Builder.html).

- Type: `RetryOptions`
- Default: `Null` which means no retries will be attempted.

```java
//create Workflow stub for GreetWorkflowInterface
GreetWorkflowInterface workflow1 =
    WorkerGreet.greetclient.newWorkflowStub(
        GreetWorkflowInterface.class,
        WorkflowOptions.newBuilder()
                .setWorkflowId("GreetWF")
                .setTaskQueue(WorkerGreet.TASK_QUEUE)
                // Set Workflow Retry Options
                .setRetryOptions(RetryOptions.newBuilder()
                .build());
```

#### CronSchedule

A [Temporal Cron Job](/cron-job) is the series of Workflow Executions that occur when a Cron Schedule is provided in the
call to spawn a Workflow Execution.

A Cron Schedule is provided as an option when the call to spawn a Workflow Execution is made.

Set the Cron Schedule with the
[`WorkflowStub`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/client/WorkflowStub.html)
instance in the Client code using
[`WorkflowOptions.Builder.setCronSchedule`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/client/WorkflowOptions.Builder.html).

Setting `setCronSchedule` changes the Workflow Execution into a Temporal Cron Job. The default timezone for a Cron is
UTC.

- Type: `String`
- Default: None

```java
//create Workflow stub for YourWorkflowInterface
YourWorkflowInterface workflow1 =
    YourWorker.yourclient.newWorkflowStub(
        YourWorkflowInterface.class,
        WorkflowOptions.newBuilder()
                .setWorkflowId("YourWF")
                .setTaskQueue(YourWorker.TASK_QUEUE)
                // Set Cron Schedule
                .setCronSchedule("* * * * *")
                .build());
```

For more details, see the
[HelloCron Sample](https://github.com/temporalio/samples-java/blob/main/core/src/main/java/io/temporal/samples/hello/HelloCron.java).

#### Memo

- Type: `String`
- Default: None

```java
//create Workflow stub for GreetWorkflowInterface
GreetWorkflowInterface workflow1 =
    WorkerGreet.greetclient.newWorkflowStub(
        GreetWorkflowInterface.class,
        WorkflowOptions.newBuilder()
                .setWorkflowId("GreetWF")
                .setTaskQueue(WorkerGreet.TASK_QUEUE)
                // Set Memo. You can set additional non-indexed info via Memo
                        .setMemo(ImmutableMap.of(
                                "memoKey", "memoValue"
                        ))
                .build());
```

#### SearchAttributes

Search Attributes are additional indexed information attributed to Workflow and used for search and visibility. These
can be used in a query of List/Scan/Count Workflow APIs. The key and its value type must be registered on Temporal
server side.

- Type: `Map<String, Object>`
- Default: None

```java
private static void parentWorkflow() {
        ChildWorkflowOptions childworkflowOptions =
                ChildWorkflowOptions.newBuilder()
                        // Set Search Attributes
                        .setSearchAttributes(ImmutableMap.of("MySearchAttributeNAme", "value"))
                        .build();
```

The following Java types are supported:

- String
- Long, Integer, Short, Byte
- Boolean
- Double
- OffsetDateTime
- Collection of the types in this list.

### How to get the result of a Workflow Execution in Java {/* #get-workflow-results */}

If the call to start a Workflow Execution is successful, you will gain access to the Workflow Execution's Run Id.

The Workflow Id, Run Id, and Namespace may be used to uniquely identify a Workflow Execution in the system and get its
result.

It's possible to both block progress on the result (synchronous execution) or get the result at some other point in time
(asynchronous execution).

In the Temporal Platform, it's also acceptable to use Queries as the preferred method for accessing the state and
results of Workflow Executions.

A synchronous Workflow Execution blocks your client thread until the Workflow Execution completes (or fails) and get the
results (or error in case of failure).

The following example is a type-safe approach for getting the results of a synchronous Workflow Execution.

```java
 FileProcessingWorkflow workflow = client.newWorkflowStub(
                FileProcessingWorkflow.class,
                WorkflowOptions.newBuilder()
                        .setWorkflowId(workflowId)
                        .setTaskQueue(taskQueue)
                        .build();

// start sync and wait for results (or failure)
String result = workflow.processfile(new Argument());
```

An asynchronous Workflow Execution immediately returns a value to the caller.

The following examples show how to get the results of a Workflow Execution through typed and untyped `WorkflowStub`.

- **Typed WorkflowStub Example**

  ```java
  // create typed Workflow stub
  FileProcessingWorkflow workflow = client.newWorkflowStub(FileProcessingWorkflow.class,
                WorkflowOptions.newBuilder()
                        .setTaskQueue(taskQueue)
                        .setWorkflowId(workflowId)
                        .build());
  // use WorkflowClient.execute (if your Workflow takes in arguments) or WorkflowClient.start (for zero arguments)
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

If you need to wait for a Workflow Execution to complete after an asynchronous start, the most straightforward way is to
call the blocking Workflow instance again.

Note that if `WorkflowOptions.WorkflowIdReusePolicy` is not set to `AllowDuplicate`, then instead of throwing
`DuplicateWorkflowException`, it reconnects to an existing Workflow and waits for its completion.

The following example shows how to do this from a different process than the one that started the Workflow Execution.

```java
YourWorkflow workflow = client.newWorkflowStub(YourWorkflow.class, workflowId);

// Returns the result after waiting for the Workflow to complete.
String result = workflow.yourMethod();
```

Another way to connect to an existing Workflow and wait for its completion from another process, is to use
`UntypedWorkflowStub`. For example:

```java
WorkflowStub workflowStub = client.newUntypedWorkflowStub(workflowType, workflowOptions);

// Returns the result after waiting for the Workflow to complete.
String result = untyped.getResult(String.class);
```

**Get last (successful) completion result**

For a Temporal Cron Job, get the result of previous successful runs using `GetLastCompletionResult()`. The method
returns `null` if there is no previous completion. The following example shows how to implement this in a Workflow.

```java
public String cronWorkflow() {
    String lastProcessedFileName = Workflow.getLastCompletionResult(String.class);

    // Process work starting from the lastProcessedFileName.
    // Business logic implementation goes here.
    // Updates lastProcessedFileName to the new value.

    return lastProcessedFileName;
}
```

Note that this works even if one of the Cron schedule runs failed. The next schedule will still get the last successful
result if it ever successfully completed at least once. For example, for a daily cron Workflow, if the run succeeds on
the first day and fails on the second day, then the third day run will get the result from first day's run using these
APIs.

---

## Java SDK developer guide

![Java SDK Banner](/img/assets/banner-java-temporal.png)

## Install and get started

You can find detailed installation instructions for the Java SDK in the [Quickstart](/develop/java/set-up-your-local-java).

There's also a short walkthrough of how to use the Temporal primitives (Activities, Workflows, and Workers) to build and run a Temporal application to get you up and running.

Once your local Temporal Service is set up, continue building with the following resources:

- [Develop a Workflow](/develop/java/workflows/basics)
- [Develop an Activity](/develop/java/activities/basics)
- [Start an Activity execution](/develop/java/activities/execution)
- [Run Worker processes](/develop/java/workers/run-worker-process)

From there, you can dive deeper into any of the Temporal primitives to start building Workflows that fit your use cases.

## [Workflows](/develop/java/workflows)

- [Workflow basics](/develop/java/workflows/basics)
- [Child Workflows](/develop/java/workflows/child-workflows)
- [Continue-As-New](/develop/java/workflows/continue-as-new)
- [Message passing](/develop/java/workflows/message-passing)
- [Cancellation](/develop/java/workflows/cancellation)
- [Timeouts](/develop/java/workflows/timeouts)
- [Schedules](/develop/java/workflows/schedules)
- [Timers](/develop/java/workflows/timers)
- [Side effects](/develop/java/workflows/side-effects)
- [Versioning](/develop/java/workflows/versioning)

## [Activities](/develop/java/activities)

- [Activity basics](/develop/java/activities/basics)
- [Activity execution](/develop/java/activities/execution)
- [Standalone Activities](/develop/java/activities/standalone-activities)
- [Timeouts](/develop/java/activities/timeouts)
- [Asynchronous Activity Completion](/develop/java/activities/asynchronous-activity)
- [Benign exceptions](/develop/java/activities/benign-exceptions)

## [Workers](/develop/java/workers)

- [Worker processes](/develop/java/workers/run-worker-process)
- [Observability](/develop/java/platform/observability)

## [Temporal Client](/develop/java/client)

- [Temporal Client](/develop/java/client/temporal-client)
- [Namespaces](/develop/java/client/namespaces)

## [Temporal Nexus](/develop/java/nexus)

- [Quickstart](/develop/java/nexus/quickstart)
- [Feature guide](/develop/java/nexus/feature-guide)

## [Platform](/develop/java/platform)

- [Observability](/develop/java/platform/observability)
- [Enriching the UI](/develop/java/platform/enriching-ui)

## [Best practices](/develop/java/best-practices)

- [Testing](/develop/java/best-practices/testing-suite)
- [Debugging](/develop/java/best-practices/debugging)
- [Converters and encryption](/develop/java/best-practices/converters-and-encryption)

## Spring Boot Integration

- [Spring Boot Integration](/develop/java/integrations/spring-boot-integration)

## Temporal Java Technical Resources

- [Java SDK Quickstart - Setup Guide](https://docs.temporal.io/develop/java/set-up-your-local-java)
- [Java API Documentation](https://javadoc.io/doc/io.temporal/temporal-sdk)
- [Java SDK Code Samples](https://github.com/temporalio/samples-java)
- [Java SDK GitHub](https://github.com/temporalio/sdk-java)
- [Temporal 101 in Java Free Course](https://learn.temporal.io/courses/temporal_101/java/)

## Get Connected with the Temporal Java Community

- [Temporal Java Community Slack](https://temporalio.slack.com/archives/CTT84KXK9)
- [Java SDK Forum](https://community.temporal.io/tag/java-sdk)

---

## Integrations - Java SDK

The following integrations are available for the Temporal Java SDK.
These integrations are built on the Temporal Java SDK's [Plugin system](/develop/plugins-guide), which you can also use to build your own integrations.

<IntegrationsGrid defaultSdks={["Java"]} />

---

## Spring AI integration - Java SDK

[Spring AI](https://docs.spring.io/spring-ai/reference/) is an agent framework for Java applications — chat clients, tool calling, vector stores, embeddings, and MCP servers, all wired through Spring Boot.

The [Temporal Spring AI integration](https://central.sonatype.com/artifact/io.temporal/temporal-spring-ai) makes Spring AI agents durable: model calls run through Temporal Activities recorded in Event history, and tools are dispatched per their type so each kind lands in the right place in Workflow execution — Activity stubs and Nexus stubs as durable operations, `@SideEffectTool` classes wrapped in `Workflow.sideEffect`, and plain tools running directly in Workflow code. Agents retry on failure and replay deterministically without changing how you write Spring AI code.

The integration is built on the Temporal Java SDK's [Plugin system](/develop/plugins-guide) and is distributed as the `io.temporal:temporal-spring-ai` module alongside the existing [Spring Boot integration](/develop/java/integrations/spring-boot-integration).

<ReleaseNoteHeader type="publicPreview" />

## Prerequisites

The integration requires all of the following on your application's classpath. The plugin won't auto-configure if any of these are missing or below the listed minimum:

| Dependency        | Minimum version |
| ----------------- | --------------- |
| Java              | 17              |
| Spring Boot       | 3.x             |
| Spring AI         | 1.1.0           |
| Temporal Java SDK | 1.35.0          |

You also need the [`temporal-spring-boot-starter`](/develop/java/integrations/spring-boot-integration) and a Spring AI model starter (for example, `spring-ai-starter-model-openai`) — `temporal-spring-ai` does not pull in a model provider on its own.

## Add the dependency

Add `temporal-spring-ai` alongside `temporal-spring-boot-starter` and a Spring AI model starter (for example, `spring-ai-starter-model-openai`).

**[Apache Maven](https://maven.apache.org/):**

```xml
<dependency>
    <groupId>io.temporal</groupId>
    <artifactId>temporal-spring-ai</artifactId>
    <version>${temporal-sdk.version}</version>
</dependency>
```

**[Gradle Groovy DSL](https://gradle.org/):**

```groovy
implementation "io.temporal:temporal-spring-ai:${temporalSdkVersion}"
```

When `temporal-spring-ai` is on the classpath, the `SpringAiPlugin` auto-registers `ChatModelActivity` with all Temporal Workers created by the Spring Boot integration. Optional Activities are auto-configured when their dependencies are present:

| Feature      | Dependency      | Registered Activity      |
| ------------ | --------------- | ------------------------ |
| Vector store | `spring-ai-rag` | `VectorStoreActivity`    |
| Embeddings   | `spring-ai-rag` | `EmbeddingModelActivity` |
| MCP          | `spring-ai-mcp` | `McpClientActivity`      |

## Call a chat model from a Workflow

Use `ActivityChatModel` as a Spring AI `ChatModel` inside a Workflow. Every call goes through a Temporal Activity, so model responses are durable and retried per your Activity options.

Wrap `ActivityChatModel` in a `TemporalChatClient` to build prompts and register tools:

<!--SNIPSTART samples-java-spring-ai-chat-workflow-init-->
[springai/basic/src/main/java/io/temporal/samples/springai/chat/ChatWorkflowImpl.java](https://github.com/temporalio/samples-java/blob/main/springai/basic/src/main/java/io/temporal/samples/springai/chat/ChatWorkflowImpl.java)
```java
@WorkflowInit
public ChatWorkflowImpl(String systemPrompt) {
  // Build an activity-backed chat model. The factory creates the activity stub
  // internally and registers per-call Summaries on the Temporal UI.
  ActivityChatModel activityChatModel = ActivityChatModel.forDefault();

  // Create an activity stub for weather tools - these execute as durable activities
  WeatherActivity weatherTool =
      Workflow.newActivityStub(
          WeatherActivity.class,
          ActivityOptions.newBuilder()
              .setStartToCloseTimeout(Duration.ofSeconds(30))
              .setRetryOptions(RetryOptions.newBuilder().setMaximumAttempts(3).build())
              .build());

  // Create deterministic tools - these execute directly in the workflow
  StringTools stringTools = new StringTools();

  // Create side-effect tools - these are wrapped in Workflow.sideEffect()
  // The result is recorded in history, making replay deterministic
  TimestampTools timestampTools = new TimestampTools();

  // Create chat memory - uses in-memory storage that gets rebuilt on replay
  ChatMemory chatMemory =
      MessageWindowChatMemory.builder()
          .chatMemoryRepository(new InMemoryChatMemoryRepository())
          .maxMessages(20)
          .build();

  // Build a TemporalChatClient with tools and memory
  // - Activity stubs (weatherTool) become durable AI tools
  // - plain workflow tool classes (stringTools) execute directly in workflow
  // - @SideEffectTool classes (timestampTools) are wrapped in sideEffect()
  // - PromptChatMemoryAdvisor maintains conversation history
  this.chatClient =
      TemporalChatClient.builder(activityChatModel)
          .defaultSystem(systemPrompt)
          .defaultTools(weatherTool, stringTools, timestampTools)
          .defaultAdvisors(PromptChatMemoryAdvisor.builder(chatMemory).build())
          .build();
}

```
<!--SNIPEND-->

`ActivityChatModel.forDefault()` resolves to the default Spring AI `ChatModel` bean. To target a specific model in a multi-model application, pass its bean name to `ActivityChatModel.forModel("openai")`.

:::note

Streaming responses are not currently supported.
:::

## Register tools

In Spring AI, [tools](https://docs.spring.io/spring-ai/reference/api/tools.html) are methods the model can choose to call to fetch data or take action — you make them available to a chat client by registering them, typically through `ChatClient.defaultTools(...)` or per-prompt `tools(...)`. The chat client advertises the methods to the model, the model decides which (if any) to call, and the framework runs the chosen method and feeds the result back into the conversation.

The Temporal integration extends this by inspecting the type of each tool you register and dispatching it to the appropriate Temporal primitive, so you can mix durable and in-Workflow tools in the same chat client. The integration handles Temporal determinism for you when the tool is durable, and gives you control when it isn't.

### Activity stubs

An interface annotated with both `@ActivityInterface` and Spring AI `@Tool` methods is auto-detected and executed as a Temporal Activity. Use this for external calls that need retries and timeouts.

<!--SNIPSTART samples-java-spring-ai-activity-tool-->
[springai/basic/src/main/java/io/temporal/samples/springai/chat/WeatherActivity.java](https://github.com/temporalio/samples-java/blob/main/springai/basic/src/main/java/io/temporal/samples/springai/chat/WeatherActivity.java)
```java
@ActivityInterface
public interface WeatherActivity {

  /**
   * Gets the current weather for a city.
   *
   * The {@code @Tool} annotation makes this method available to the AI model, while the
   * {@code @ActivityInterface} ensures it executes as a Temporal activity.
   *
   * @param city the name of the city
   * @return a description of the current weather
   */
  @Tool(
      description =
          "Get the current weather for a city. Returns temperature, conditions, and humidity.")
  @ActivityMethod
  String getWeather(
      @ToolParam(description = "The name of the city (e.g., 'Seattle', 'New York')") String city);

  /**
   * Gets the weather forecast for a city.
   *
   * @param city the name of the city
   * @param days the number of days to forecast (1-7)
   * @return the weather forecast
   */
  @Tool(description = "Get the weather forecast for a city for the specified number of days.")
  @ActivityMethod
  String getForecast(
      @ToolParam(description = "The name of the city") String city,
      @ToolParam(description = "Number of days to forecast (1-7)") int days);
}
```
<!--SNIPEND-->

### Nexus service stubs

Nexus service stubs with `@Tool` methods are auto-detected and invoked as [Nexus operations](/develop/java/nexus), enabling cross-Namespace tool calls.

### `@SideEffectTool`

Classes annotated with `@SideEffectTool` have each `@Tool` method wrapped in `Workflow.sideEffect()`. The result is recorded in history on first execution and replayed from history afterward. Use this for cheap, non-deterministic operations such as timestamps or UUIDs.

<!--SNIPSTART samples-java-spring-ai-side-effect-tool-->
[springai/basic/src/main/java/io/temporal/samples/springai/chat/TimestampTools.java](https://github.com/temporalio/samples-java/blob/main/springai/basic/src/main/java/io/temporal/samples/springai/chat/TimestampTools.java)
```java
@SideEffectTool
public class TimestampTools {

  private static final DateTimeFormatter FORMATTER =
      DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss z").withZone(ZoneId.systemDefault());

  /**
   * Gets the current date and time.
   *
   * This is non-deterministic (returns different values each time), but wrapped in sideEffect()
   * it becomes safe for workflow replay.
   *
   * @return the current date and time as a formatted string
   */
  @Tool(description = "Get the current date and time")
  public String getCurrentDateTime() {
    return FORMATTER.format(Instant.now());
  }

  /**
   * Gets the current Unix timestamp in milliseconds.
   *
   * @return the current time in milliseconds since epoch
   */
  @Tool(description = "Get the current Unix timestamp in milliseconds")
  public long getCurrentTimestamp() {
    return System.currentTimeMillis();
  }

  /**
   * Generates a random UUID.
   *
   * @return a new random UUID string
   */
  @Tool(description = "Generate a random UUID")
  public String generateUuid() {
    return UUID.randomUUID().toString();
  }

  /**
   * Gets the current date and time in a specific timezone.
   *
   * @param timezone the timezone ID (e.g., "America/New_York", "UTC", "Europe/London")
   * @return the current date and time in the specified timezone
   */
  @Tool(description = "Get the current date and time in a specific timezone")
  public String getDateTimeInTimezone(
      @ToolParam(description = "Timezone ID (e.g., 'America/New_York', 'UTC', 'Europe/London')")
          String timezone) {
    try {
      ZoneId zoneId = ZoneId.of(timezone);
      DateTimeFormatter formatter =
          DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss z").withZone(zoneId);
      return formatter.format(Instant.now());
    } catch (Exception e) {
      return "Invalid timezone: " + timezone + ". Use formats like 'America/New_York' or 'UTC'.";
    }
  }
}
```
<!--SNIPEND-->

### Plain tools

Any class with `@Tool` methods that isn't an Activity stub, Nexus stub, or `@SideEffectTool` runs directly on the Workflow thread. Use this for inherently deterministic tools (such as updating in-memory agent state), or for orchestration of durable primitives as you need, e.g. calling multiple Activities, child Workflows, wait conditions, or other Temporal durable primitives.
