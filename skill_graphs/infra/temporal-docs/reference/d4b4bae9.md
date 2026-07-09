
<!--SNIPSTART samples-java-spring-ai-plain-tool-->
[springai/basic/src/main/java/io/temporal/samples/springai/chat/StringTools.java](https://github.com/temporalio/samples-java/blob/main/springai/basic/src/main/java/io/temporal/samples/springai/chat/StringTools.java)
```java
public class StringTools {

  @Tool(description = "Reverse a string, returning the characters in opposite order")
  public String reverse(@ToolParam(description = "The string to reverse") String input) {
    if (input == null) {
      return null;
    }
    return new StringBuilder(input).reverse().toString();
  }

  @Tool(description = "Count the number of words in a text")
  public int countWords(@ToolParam(description = "The text to count words in") String text) {
    if (text == null || text.isBlank()) {
      return 0;
    }
    return text.trim().split("\\s+").length;
  }

  @Tool(description = "Convert text to all uppercase letters")
  public String toUpperCase(@ToolParam(description = "The text to convert") String text) {
    if (text == null) {
      return null;
    }
    return text.toUpperCase(java.util.Locale.ROOT);
  }

  @Tool(description = "Convert text to all lowercase letters")
  public String toLowerCase(@ToolParam(description = "The text to convert") String text) {
    if (text == null) {
      return null;
    }
    return text.toLowerCase(java.util.Locale.ROOT);
  }

  @Tool(description = "Check if a string is a palindrome (reads the same forwards and backwards)")
  public boolean isPalindrome(@ToolParam(description = "The text to check") String text) {
    if (text == null) {
      return false;
    }
    String normalized = text.toLowerCase(java.util.Locale.ROOT).replaceAll("\\s+", "");
    String reversed = new StringBuilder(normalized).reverse().toString();
    return normalized.equals(reversed);
  }
}
```
<!--SNIPEND-->

## Activity options and retry behavior

`ActivityChatModel.forDefault()` and `forModel(name)` build the chat Activity stub with sensible defaults: a 2-minute start-to-close timeout, 3 attempts, and `org.springframework.ai.retry.NonTransientAiException` and `java.lang.IllegalArgumentException` classified as non-retryable so a bad API key or invalid prompt fails fast.

Pass an `ActivityOptions` directly when you need finer control — a specific Task Queue, [heartbeats](/develop/java/activities/execution#heartbeattimeout), [priority](/develop/task-queue-priority-fairness), or a custom `RetryOptions`:

```java
ActivityChatModel chatModel = ActivityChatModel.forDefault(
        ActivityOptions.newBuilder(ActivityChatModel.defaultActivityOptions())
                .setTaskQueue("chat-heavy")
                .build());
```

For configuration-driven per-model overrides, declare a `ChatModelActivityOptions` bean. The plugin consults it whenever `forDefault()` or `forModel(name)` runs in a Workflow. Use the special key `ChatModelTypes.DEFAULT_MODEL_NAME` (the literal `"default"`) as a global catch-all that applies to any model not explicitly listed — including models contributed by third-party starters:

<!--SNIPSTART samples-java-spring-ai-per-model-options-->
[springai/multimodel/src/main/java/io/temporal/samples/springai/multimodel/ChatModelConfig.java](https://github.com/temporalio/samples-java/blob/main/springai/multimodel/src/main/java/io/temporal/samples/springai/multimodel/ChatModelConfig.java)
```java
@Bean
public ChatModelActivityOptions chatModelActivityOptions() {
  return new ChatModelActivityOptions(
      Map.of(
          "anthropicChatModel",
          ActivityOptions.newBuilder(ActivityChatModel.defaultActivityOptions())
              .setStartToCloseTimeout(Duration.ofMinutes(5))
              .setScheduleToCloseTimeout(Duration.ofMinutes(15))
              .build()));
}
```
<!--SNIPEND-->

Keys that neither match a registered `ChatModel` bean nor equal `"default"` cause plugin construction to fail, so a typo surfaces at startup rather than at first call.

`ActivityMcpClient.create()` and `create(ActivityOptions)` work the same way for MCP tool calls, with a 30-second default timeout.

## Provider-specific chat options

Provider-specific `ChatOptions` subclasses — for example, `AnthropicChatOptions` to enable extended thinking, or `OpenAiChatOptions` to set `reasoning_effort` — pass through the Activity boundary unchanged. Attach them via `ChatClient.defaultOptions(...)` and the plugin re-applies them on the Activity side before calling the underlying model:

<!--SNIPSTART samples-java-spring-ai-provider-options-->
[springai/multimodel/src/main/java/io/temporal/samples/springai/multimodel/MultiModelWorkflowImpl.java](https://github.com/temporalio/samples-java/blob/main/springai/multimodel/src/main/java/io/temporal/samples/springai/multimodel/MultiModelWorkflowImpl.java)
```java
AnthropicChatOptions thinkingOptions =
    AnthropicChatOptions.builder()
        .thinking(AnthropicApi.ThinkingType.ENABLED, 1024)
        .temperature(1.0)
        .maxTokens(4096)
        .build();
chatClients.put(
    "think",
    TemporalChatClient.builder(anthropicModel)
        .defaultSystem(
            "You are a helpful assistant powered by Anthropic with extended thinking. "
                + "Use the thinking budget to reason carefully, then give a crisp answer "
                + "that reflects the reasoning you did.")
        .defaultOptions(thinkingOptions)
        .build());
```
<!--SNIPEND-->

The pass-through relies on the `ChatOptions` subclass overriding `copy()` to return its own type — every provider class shipped with Spring AI does.

## Media in messages

Prefer URI-based media when attaching images, audio, or other binary content to chat messages. Raw `byte[]` media gets serialized into every chat Activity's input and result payload, which end up inside Temporal Event history events. Server-side history events have a fixed 2 MiB size limit; to leave headroom for messages, tool definitions, and options, the plugin enforces a **1 MiB default cap** on inline bytes and fails fast with a non-retryable `ApplicationFailure` pointing at the URI alternative.

```java
// Preferred — only the URL crosses the Activity boundary.
Media image = new Media(MimeTypeUtils.IMAGE_PNG, URI.create("https://cdn.example.com/pic.png"));
```

Override the cap by setting the system property `io.temporal.springai.maxMediaBytes` before your worker starts (positive integer; `0` disables the check). For anything larger than a small thumbnail, route the bytes to a binary store from an Activity and pass only the URL across the conversation.

## Use vector stores, embeddings, and MCP

When the corresponding Spring AI modules are on the classpath, the integration registers Activities for vector stores, embeddings, and MCP tool calls. Inject the matching Spring AI types into your Activities or Workflows and use them as you would in any Spring AI application — each operation is executed through a Temporal Activity.

You can also register these plugins explicitly, without relying on auto-configuration:

```java
new VectorStorePlugin(vectorStore);
new EmbeddingModelPlugin(embeddingModel);
new McpPlugin();
```

`ActivityMcpClient` wraps a Spring AI MCP client so that remote MCP tool calls become durable Activity executions.

## Resources

- [`temporal-spring-ai` README](https://github.com/temporalio/sdk-java/blob/master/temporal-spring-ai/README.md) — full reference for the module
- [Spring Boot integration](/develop/java/integrations/spring-boot-integration) — required companion module
- [Plugin system](/develop/plugins-guide) — how integrations are registered with Workers and Clients

---

## Spring Boot integration - Java SDK

This guide introduces the [Temporal Spring Boot](https://central.sonatype.com/artifact/io.temporal/temporal-spring-boot-starter?smo=true) integration. The Temporal Spring Boot integration is the easiest way to get started using the Temporal Java SDK if you are a current [Spring](https://spring.io/) user.

This section includes the following topics:

- [Setup Dependency](#setup-dependency)
- [Connect to your Temporal Service](#connect)
- [Configure Workers](#configure-workers)
- [Customize Options](#customize-options)
- [Interceptors](#interceptors)
- [Integrations](#integrations)
- [Testing](#testing)

## Setup Dependency {/* #setup-dependency */}

To start using the Temporal Spring Boot integration, you need to add [`io.temporal:temporal-spring-boot-starter`](https://search.maven.org/artifact/io.temporal/temporal-spring-boot-starter)
as a dependency to your Spring project:

:::note
Temporal's Spring Boot integration currently supports Spring Boot 2.x, 3.x, and 4.x
:::

**[Apache Maven](https://maven.apache.org/):**

```maven
<dependency>
    <groupId>io.temporal</groupId>
    <artifactId>temporal-spring-boot-starter</artifactId>
    <version>1.31.0</version>
</dependency>
```

**[Gradle Groovy DSL](https://gradle.org/):**

```groovy
implementation ("io.temporal:temporal-spring-boot-starter:1.31.0")
```

## Connect {/* #connect */}

See the [Temporal Client documentation](/develop/java/client/temporal-client) for more information about connecting to a Temporal Service.

To create an autoconfigured `WorkflowClient`, you need to specify some connection details in your `application.yml` file, as described in the next section.

### Connect to your local Temporal Service

```yaml
spring.temporal:
  connection:
    target: local # you can specify a host:port here for a remote connection
```

This is enough to autowire a `WorkflowClient` in your Spring Boot application:

```java
@SpringBootApplication
class App {
  @Autowire
  private WorkflowClient workflowClient;
}
```

### Connect to a custom Namespace

You can also connect to a custom Namespace by specifying the `spring.temporal.namespace` property.

```yaml
spring.temporal:
  connection:
    target: local # you can specify a host:port here for a remote connection
  namespace: <custom namespace> # you can specify a custom namespace that you are using
```

## Connect to Temporal Cloud {/* #connect */}

You can also connect to Temporal Cloud, using either an API key or mTLS for authentication.

See the [Connect to Temporal Cloud](/develop/java/client/temporal-client#connect-to-temporal-cloud) section for more information about connecting to Temporal Cloud.

### Using an API key

```yaml
spring.temporal:
  connection:
    target: <target>
    apiKey: <API key>
  namespace: <namespace>
```

### Using mTLS

```
spring.temporal:
  connection:
    mtls:
      target: <target>
      key-file: /path/to/key.key
      cert-chain-file: /path/to/cert.pem # If you use PKCS12 (.pkcs12, .pfx or .p12), you don't need to set it because the certificates chain is bundled into the key file
  namespace: <namespace>
```

## Configure Workers {/* #configure-workers */}

Temporal's Spring Boot integration supports two configuration methods for Workers: explicit configuration and auto-discovery.

### Explicit configuration

```yaml
spring.temporal:
  workers:
    - task-queue: your-task-queue-name
      name: your-worker-name # unique name of the Worker. If not specified, Task Queue is used as the Worker name.
      workflow-classes:
        - your.package.YourWorkflowImpl
      activity-beans:
        - activity-bean-name1
```

### Auto Discovery

Auto Discovery allows you to skip specifying Workflow classes, Activity beans, and Nexus Service beans explicitly in the config by referencing Worker Task Queue names or Worker Names on Workflow, Activity implementations, and Nexus Service implementations. Auto-discovery is applied after and on top of an explicit configuration.

```
spring.temporal:
  workers-auto-discovery:
    packages:
      - your.package # enumerate all the packages that contain your workflow implementations.
```

#### What is auto-discovered:

- Workflow implementation classes annotated with `io.temporal.spring.boot.WorkflowImpl`
- Activity beans present Spring context whose implementations are annotated with `io.temporal.spring.boot.ActivityImpl`
- Nexus Service beans present in Spring context whose implementations are annotated with `io.temporal.spring.boot.NexusServiceImpl`
- Workers if a Task Queue is referenced by the annotations but not explicitly configured. Default configuration will be used.

:::note
`io.temporal.spring.boot.ActivityImpl` and `io.temporal.spring.boot.NexusServiceImpl` should be applied to beans, one way to do this is to annotate your Activity implementation class with `@Component`
:::

```
@Component
@ActivityImpl(workers = "myWorker")
public class MyActivityImpl implements MyActivity {
  @Override
  public String execute(String input) {
    return input;
  }
}
```

:::note
Auto-discovered Workflow implementation classes, Activity beans, and Nexus Service beans will be registered with the configured Workers if not already registered.
:::

## Interceptors {/* #interceptors */}

To enable Interceptors, you can create beans by implementing the `io.temporal.common.interceptors.WorkflowClientInterceptor`, `io.temporal.common.interceptors.ScheduleClientInterceptor`, or `io.temporal.common.interceptors.WorkerInterceptor` interface. Interceptors will be registered in the order specified by the `@Order` annotation.

## Integrations {/* #integrations */}

The Temporal Spring Boot integration also has built in support for various tools in the Spring ecosystem, such as metrics and tracing.

### Metrics

You can set up built-in Spring Boot metrics using [Spring Boot Actuator](https://docs.spring.io/spring-boot/reference/actuator/metrics.html). The Temporal Spring Boot integration will pick up the `MeterRegistry` bean and use it to report Temporal metrics.

Alternatively, you can define a custom `io.micrometer.core.instrument.MeterRegistry` bean in the application context.

### Tracing

You can set up [Spring Cloud Sleuth](https://spring.io/projects/spring-cloud-sleuth) with an OpenTelemetry export. The Temporal Spring Boot integration will pick up the OpenTelemetry bean configured by `spring-cloud-sleuth-otel-autoconfigure` and use it for Temporal traces.

Alternatively, you can define a custom `io.opentelemetry.api.OpenTelemetry` for OpenTelemetry or `io.opentracing.Tracer` for an OpenTracing bean in the application context.

## Customization of Options {/* #customize-options */}

To programmatically customize the various options that are created by the Spring Boot integration, you can create beans that implement the `io.temporal.spring.boot.TemporalOptionsCustomizer<OptionsBuilderType>` interface. This will be called after the options in your properties files are applied.

Where `OptionsType` may be one of:

    * `WorkflowServiceStubsOptions.Builder`
    * `WorkflowClientOptions.Builder`
    * `WorkerFactoryOptions.Builder`
    * `WorkerOptions.Builder`
    * `WorkflowImplementationOptions.Builder`
    * `TestEnvironmentOptions.Builder`

`io.temporal.spring.boot.WorkerOptionsCustomizer` may be used instead of `TemporalOptionsCustomizer<WorkerOptions.Builder>` if `WorkerOptions` needs to be customized on the Task Queue or Worker name.

`io.temporal.spring.boot.WorkflowImplementationOptionsCustomizer` may be used instead of `TemporalOptionsCustomizer<WorkflowImplementationOptions.Builder>` if `WorkflowImplementationOptions` needs to be customized on Workflow Type.

## Testing {/* #testing */}

The Temporal Spring Boot integration also has easy support for testing your Temporal code. Add the following to your `application.yml` to reconfigure the client to work through `io.temporal.testing.TestWorkflowEnvironment` that uses in-memory Java Test Server:

```
spring.temporal:
  test-server:
    enabled: true
```

When `spring.temporal.test-server.enabled:true` is added, the `spring.temporal.connection` section is ignored. This allows wiring the `TestWorkflowEnvironment` bean in your unit tests:

```
@SpringBootTest(classes = Test.Configuration.class)
@TestInstance(TestInstance.Lifecycle.PER_CLASS)
public class Test {
  @Autowired ConfigurableApplicationContext applicationContext;
  @Autowired TestWorkflowEnvironment testWorkflowEnvironment;
  @Autowired WorkflowClient workflowClient;

  @BeforeEach
  void setUp() {
    applicationContext.start();
  }

  @Test
  @Timeout(value = 10)
  public void test() {
    # ...
  }

  @ComponentScan # to discover Activity beans annotated with @Component
  public static class Configuration {}
}
```

See the [Java SDK test frameworks documentation](/develop/java/best-practices/testing-suite#test-frameworks) for more information about testing.

---

## Temporal Nexus - Java SDK feature guide

Use [Temporal Nexus](/evaluate/nexus) to connect Temporal Applications within and across Namespaces using a Nexus
Endpoint, a Nexus Service contract, and Nexus Operations.

This page shows how to do the following:

- [Run a development Temporal Service with Nexus enabled](#run-the-temporal-nexus-development-server)
- [Create caller and handler Namespaces](#create-caller-handler-namespaces)
- [Create a Nexus Endpoint to route requests from caller to handler](#create-nexus-endpoint)
- [Define the Nexus Service contract](#define-nexus-service-contract)
- [Develop a Nexus Service and Operation handlers](#develop-nexus-service-operation-handlers)
- [Develop a caller Workflow that uses a Nexus Service](#develop-caller-workflow-nexus-service)
- [Make Nexus calls across Namespaces with a development Server](#nexus-calls-across-namespaces-dev-server)
- [Make Nexus calls across Namespaces in Temporal Cloud](#nexus-calls-across-namespaces-temporal-cloud)

:::note

This documentation uses source code derived from the
[Java Nexus sample](https://github.com/temporalio/samples-java/tree/main/core/src/main/java/io/temporal/samples/nexus).

:::

## Run the Temporal Development Server with Nexus enabled {/* #run-the-temporal-nexus-development-server */}

Prerequisites:

- [Install the latest Temporal CLI](https://learn.temporal.io/getting_started/java/dev_environment/#set-up-a-local-temporal-service-for-development-with-temporal-cli)
  (v1.3.0 or higher recommended)
- [Install the latest Temporal Java SDK](https://learn.temporal.io/getting_started/java/dev_environment/#add-temporal-java-sdk-dependencies)
  (v1.28.0 or higher recommended)

The first step in working with Temporal Nexus involves starting a Temporal server with Nexus enabled.

```
temporal server start-dev
```

This command automatically starts the Temporal development server with the Web UI, and creates the `default` Namespace.
It uses an in-memory database, so do not use it for real use cases.

The Temporal Web UI should now be accessible at [http://localhost:8233](http://localhost:8233), and the Temporal Server
should now be available for client connections on `localhost:7233`.

## Create caller and handler Namespaces {/* #create-caller-handler-namespaces */}

Before setting up Nexus endpoints, create separate Namespaces for the caller and handler.

```
temporal operator namespace create --namespace my-target-namespace
temporal operator namespace create --namespace my-caller-namespace
```

`my-target-namespace` will contain the Nexus Operation handler, and we will use a Workflow in `my-caller-namespace` to
call that Operation handler. We use different namespaces to demonstrate cross-Namespace Nexus calls.

## Create a Nexus Endpoint to route requests from caller to handler {/* #create-nexus-endpoint */}

After establishing caller and handler Namespaces, the next step is to create a Nexus Endpoint to route requests.

```
temporal operator nexus endpoint create \
  --name my-nexus-endpoint-name \
  --target-namespace my-target-namespace \
  --target-task-queue my-handler-task-queue
```

You can also use the Web UI to create the Namespaces and Nexus endpoint.

## Define the Nexus Service contract {/* #define-nexus-service-contract */}

Defining a clear contract for the Nexus Service is crucial for smooth communication.

In this example, there is a service package that describes the Service and Operation names along with input/output types
for caller Workflows to use the Nexus Endpoint.

Each [Temporal SDK includes and uses a default Data Converter](https://docs.temporal.io/dataconversion). The default
data converter encodes payloads in the following order: Null, Byte array, Protobuf JSON, and JSON. In a polyglot
environment, that is where more than one language and SDK is being used to develop a Temporal solution, Protobuf and
JSON are common choices. This example uses Java classes serialized into JSON.

<!--SNIPSTART samples-java-nexus-service-->

[core/src/main/java/io/temporal/samples/nexus/service/NexusService.java](https://github.com/temporalio/samples-java/blob/nexus-snip-sync/core/src/main/java/io/temporal/samples/nexus/service/NexusService.java)

```java
@Service
public interface SampleNexusService {
  enum Language {
    EN,
    FR,
    DE,
    ES,
    TR
  }

  class HelloInput {
    private final String name;
    private final Language language;

    @JsonCreator(mode = JsonCreator.Mode.PROPERTIES)
    public HelloInput(
        @JsonProperty("name") String name, @JsonProperty("language") Language language) {
      this.name = name;
      this.language = language;
    }

    @JsonProperty("name")
    public String getName() {
      return name;
    }

    @JsonProperty("language")
    public Language getLanguage() {
      return language;
    }
  }

  class HelloOutput {
    private final String message;

    @JsonCreator(mode = JsonCreator.Mode.PROPERTIES)
    public HelloOutput(@JsonProperty("message") String message) {
      this.message = message;
    }

    @JsonProperty("message")
    public String getMessage() {
      return message;
    }
  }

  class EchoInput {
    private final String message;

    @JsonCreator(mode = JsonCreator.Mode.PROPERTIES)
    public EchoInput(@JsonProperty("message") String message) {
      this.message = message;
    }

    @JsonProperty("message")
    public String getMessage() {
      return message;
    }
  }

  class EchoOutput {
    private final String message;

    @JsonCreator(mode = JsonCreator.Mode.PROPERTIES)
    public EchoOutput(@JsonProperty("message") String message) {
      this.message = message;
    }

    @JsonProperty("message")
    public String getMessage() {
      return message;
    }
  }

  @Operation
  HelloOutput hello(HelloInput input);

  @Operation
  EchoOutput echo(EchoInput input);
}
```

<!--SNIPEND-->

## Develop a Nexus Service and Operation handlers {/* #develop-nexus-service-operation-handlers */}

Nexus Operation handlers are typically defined in the same Worker as the underlying Temporal primitives they abstract.
Operation handlers can decide if a given Nexus Operation will be synchronous or asynchronous. They can invoke underlying
Temporal primitives such as a Query, Signal, or Update using the Temporal SDK Client, or run other reliable code.
Handlers should be reliable since the [circuit breaker](/nexus/operations#circuit-breaking) trips after 5 consecutive
retryable errors, blocking all Operations from the caller to that Endpoint.

The `io.temporal.nexus.*` packages have utilities to help create Nexus Operations:

- `Nexus.getOperationContext().getWorkflowClient()` \- Get the Temporal Client that the Worker was initialized with for
  synchronous handlers backed by Temporal primitives such as Signals and Queries
- `WorkflowRunOperation.fromWorkflowMethod` \- Run a Workflow as an asynchronous Nexus Operation

This example starts with a sync Operation handler example using the `OperationHandler.sync` method, and then shows how
to create an async Operation handler that uses `WorkflowRunOperation.fromWorkflowMethod` to start a handler Workflow
from a Nexus Operation.

### Develop a Synchronous Nexus Operation handler

The `OperationHandler.sync` method is for exposing simple RPC handlers. Use
`Nexus.getOperationContext().getWorkflowClient(ctx)` to get the Temporal Client for signaling, querying, and listing
Workflows. Implementations can also make other calls, but handlers should be reliable to avoid tripping the
[circuit breaker](/nexus/operations#circuit-breaking).

{/* SNIPSTART samples-java-nexus-handler {"selectedLines": ["1-16", "43"]} */}
[core/src/main/java/io/temporal/samples/nexus/handler/NexusServiceImpl.java](https://github.com/temporalio/samples-java/blob/nexus-snip-sync/core/src/main/java/io/temporal/samples/nexus/handler/NexusServiceImpl.java)

```java
// To create a service implementation, annotate the class with @ServiceImpl and provide the
// interface that the service implements. The service implementation class should have methods that
// return OperationHandler that correspond to the operations defined in the service interface.
@ServiceImpl(service = SampleNexusService.class)
public class SampleNexusServiceImpl {
  @OperationImpl
  public OperationHandler<SampleNexusService.EchoInput, SampleNexusService.EchoOutput> echo() {
    // OperationHandler.sync is a meant for exposing simple RPC handlers.
    return OperationHandler.sync(
        // The method is for making arbitrary short calls to other services or databases, or
        // perform simple computations such as this one. Users can also access a workflow client by
        // calling
        // Nexus.getOperationContext().getWorkflowClient(ctx) to make arbitrary calls such as
        // signaling, querying, or listing workflows.
        (ctx, details, input) -> new SampleNexusService.EchoOutput(input.getMessage()));
  }
// ...
}
```

{/* SNIPEND */}

### Use the Temporal Client for Signals, Queries, and Updates
