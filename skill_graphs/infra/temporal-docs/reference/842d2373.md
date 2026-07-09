2. Make sure the Worker is running (from the [Run a Worker](#run-worker) step above).
3. Open a new terminal, navigate to the `samples-java` directory, and run:

```bash
./gradlew -q execute -PmainClass=io.temporal.samples.standaloneactivities.ExecuteActivity
```

Or use the Temporal CLI:

```bash
./temporal activity execute \
  --type ComposeGreeting \
  --activity-id standalone-activity-id \
  --task-queue standalone-activity-task-queue \
  --start-to-close-timeout 10s \
  --input '"Hello"' \
  --input '"World"'
```

## Start a Standalone Activity without waiting for the result {/* #start-activity */}

Starting a Standalone Activity means sending a request to the Temporal Server to durably enqueue
your Activity job, without waiting for it to be executed by your Worker.

Use
[`ActivityClient.start()`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/client/ActivityClient.html)
to start a Standalone Activity and get a handle without waiting for the result:

[StartActivity.java](https://github.com/temporalio/samples-java/blob/main/core/src/main/java/io/temporal/samples/standaloneactivities/StartActivity.java)

```java
ActivityHandle<String> handle =
    client.start(
        GreetingActivities.class,
        GreetingActivities::composeGreeting,
        options,
        "Hello",
        "World");
System.out.println("Started activity ID: " + ACTIVITY_ID);

// Wait for the result later
String result = handle.getResult();
System.out.println("Activity result: " + result);
```

With the Temporal Server and Worker running, open a new terminal in the `samples-java` directory and
run:

```bash
./gradlew -q execute -PmainClass=io.temporal.samples.standaloneactivities.StartActivity
```

Or use the Temporal CLI:

```bash
./temporal activity start \
  --type ComposeGreeting \
  --activity-id standalone-activity-id \
  --task-queue standalone-activity-task-queue \
  --start-to-close-timeout 10s \
  --input '"Hello"' \
  --input '"World"'
```

## Get a handle to an existing Standalone Activity {/* #get-activity-handle */}

Use `client.getHandle()` to create a typed handle to a previously started Standalone Activity:

```java
ActivityHandle<String> handle =
    client.getHandle("standalone-activity-id", null, String.class);
```

Pass `null` as the run ID to target the latest run of the given activity ID. You can then use the
handle to wait for the result, describe, cancel, or terminate the Activity.

## Wait for the result of a Standalone Activity {/* #get-activity-result */}

Under the hood, calling `client.execute()` is the same as calling `client.start()` to durably
enqueue the Standalone Activity, and then calling `handle.getResult()` to block until the Activity
completes and return the result:

```java
String result = handle.getResult();
```

To wait asynchronously without blocking the calling thread, use `handle.getResultAsync()`, which
returns a `CompletableFuture<R>`:

```java
CompletableFuture<String> future = handle.getResultAsync();
```

Or use the Temporal CLI to wait for a result by Activity ID:

```bash
./temporal activity result --activity-id standalone-activity-id
```

## List Standalone Activities {/* #list-activities */}

Use
[`client.listExecutions()`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/client/ActivityClient.html)
to list Standalone Activity Executions that match a [List Filter](/list-filter) query. The result is
a `Stream<ActivityExecutionMetadata>` that fetches pages from the server on demand as the stream is
consumed.

These APIs return only Standalone Activity Executions. Activities running inside Workflows are not
included.

[ListActivities.java](https://github.com/temporalio/samples-java/blob/main/core/src/main/java/io/temporal/samples/standaloneactivities/ListActivities.java)

```java
client
    .listExecutions("TaskQueue = '" + TASK_QUEUE + "'")
    .forEach(
        info ->
            System.out.printf(
                "ActivityID: %s, Type: %s, Status: %s%n",
                info.getActivityId(), info.getActivityType(), info.getStatus()));
```

Run it:

```bash
./gradlew -q execute -PmainClass=io.temporal.samples.standaloneactivities.ListActivities
```

Or use the Temporal CLI:

```bash
./temporal activity list
```

The query parameter accepts the same [List Filter](/list-filter) syntax used for [Workflow
Visibility](/visibility). For example, `ActivityType = 'composeGreeting' AND Status = 'Running'`.

## Count Standalone Activities {/* #count-activities */}

Use
[`client.countExecutions()`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/client/ActivityClient.html)
to count Standalone Activity Executions that match a [List Filter](/list-filter) query. This returns
the total count of executions (running, completed, failed, etc.) — not the number of queued tasks.
It works the same way as counting Workflow Executions.

[CountActivities.java](https://github.com/temporalio/samples-java/blob/main/core/src/main/java/io/temporal/samples/standaloneactivities/CountActivities.java)

```java
ActivityExecutionCount resp = client.countExecutions("TaskQueue = '" + TASK_QUEUE + "'");
System.out.println("Total activities: " + resp.getCount());
resp.getGroups()
    .forEach(
        group ->
            System.out.println("Group " + group.getGroupValues() + ": " + group.getCount()));
```

Run it:

```bash
./gradlew -q execute -PmainClass=io.temporal.samples.standaloneactivities.CountActivities
```

Or use the Temporal CLI:

```bash
./temporal activity count
```

## Run Standalone Activities with Temporal Cloud {/* #run-standalone-activities-temporal-cloud */}

The code samples on this page use `ClientConfigProfile.load()`, so the same code works against
Temporal Cloud — just configure the connection via environment variables or a TOML profile. No code
changes are needed.

For a step-by-step guide on connecting to Temporal Cloud, including Namespace creation, certificate
generation, and authentication setup in the Cloud UI, see
[Connect to Temporal Cloud](/develop/java/client/temporal-client#connect-to-temporal-cloud).

### Connect with mTLS

Set these environment variables with values from your Temporal Cloud Namespace settings:

```
export TEMPORAL_ADDRESS=<your-namespace>.<your-account-id>.tmprl.cloud:7233
export TEMPORAL_NAMESPACE=<your-namespace>.<your-account-id>
export TEMPORAL_TLS_CLIENT_CERT_PATH='path/to/your/client.pem'
export TEMPORAL_TLS_CLIENT_KEY_PATH='path/to/your/client.key'
```

### Connect with an API key

Set these environment variables with values from your Temporal Cloud API key settings:

```
export TEMPORAL_ADDRESS=<region>.<cloud_provider>.api.temporal.io:7233
export TEMPORAL_NAMESPACE=<your-namespace>.<your-account-id>
export TEMPORAL_API_KEY=<your-api-key>
```

Then run the Worker and starter code as shown in the earlier sections.

---

## Activity Timeouts - Java SDK

## Activity timeouts

Each Activity timeout controls the maximum duration of a different aspect of an Activity Execution.

The following timeouts are available in the Activity Options.

- **[Schedule-To-Close Timeout](/encyclopedia/detecting-activity-failures#schedule-to-close-timeout):** is the maximum amount of time allowed for the overall [Activity Execution](/activity-execution).
- **[Start-To-Close Timeout](/encyclopedia/detecting-activity-failures#start-to-close-timeout):** is the maximum time allowed for a single [Activity Task Execution](/tasks#activity-task-execution).
- **[Schedule-To-Start Timeout](/encyclopedia/detecting-activity-failures#schedule-to-start-timeout):** is the maximum amount of time that is allowed from when an [Activity Task](/tasks#activity-task) is scheduled to when a [Worker](/workers#worker) starts that Activity Task.

An Activity Execution must have either the Start-To-Close or the Schedule-To-Close Timeout set.

Set your Activity Timeout from the [`ActivityOptions.Builder`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/activity/ActivityOptions.Builder.html) class.

Available timeouts are:

- ScheduleToCloseTimeout()
- ScheduleToStartTimeout()
- StartToCloseTimeout()

You can set Activity Options using an `ActivityStub` within a Workflow implementation, or per-Activity using `WorkflowImplementationOptions` within a Worker.

The following uses `ActivityStub`.

```java
GreetingActivities activities = Workflow.newActivityStub(GreetingActivities.class,
    ActivityOptions.newBuilder()
        .setScheduleToCloseTimeout(Duration.ofSeconds(5))
        // .setStartToCloseTimeout(Duration.ofSeconds(2)
        // .setScheduletoCloseTimeout(Duration.ofSeconds(20))
        .build());
```

The following uses `WorkflowImplementationOptions`.

```java
WorkflowImplementationOptions options =
    WorkflowImplementationOptions.newBuilder()
        .setActivityOptions(
            ImmutableMap.of(
                "GetCustomerGreeting",
                // Set Activity Execution timeout
                ActivityOptions.newBuilder()
                    .setScheduleToCloseTimeout(Duration.ofSeconds(5))
                    // .setStartToCloseTimeout(Duration.ofSeconds(2))
                    // .setScheduleToStartTimeout(Duration.ofSeconds(5))
                    .build()))
        .build();
```

:::note

If you define options per-Activity Type options with `WorkflowImplementationOptions.setActivityOptions()`, setting them again specifically with `ActivityStub` in a Workflow will override this setting.

:::

### Custom Activity Retry Policy {/* #activity-retries */}

A Retry Policy works in cooperation with the timeouts to provide fine controls to optimize the execution experience.

Activity Executions are automatically associated with a default [Retry Policy](/encyclopedia/retry-policies) if a custom one is not provided.

To set a Retry Policy, known as the [Retry Options](/encyclopedia/retry-policies) in Java, use [`ActivityOptions.newBuilder.setRetryOptions()`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/activity/ActivityOptions.Builder.html).

- Type: `RetryOptions`
- Default: Server-defined Activity Retry policy.

- With `ActivityStub`

  ```java
  private final ActivityOptions options =
      ActivityOptions.newBuilder()
          // note that either StartToCloseTimeout or ScheduleToCloseTimeout are
          // required when setting Activity options.
          .setStartToCloseTimeout(Duration.ofSeconds(5))
          .setRetryOptions(
              RetryOptions.newBuilder()
                  .setInitialInterval(Duration.ofSeconds(1))
                  .setMaximumInterval(Duration.ofSeconds(10))
                  .build())
          .build();
  ```

- With `WorkflowImplementationOptions`

  ```java
  WorkflowImplementationOptions options =
        WorkflowImplementationOptions.newBuilder()
            .setActivityOptions(
                ImmutableMap.of(
                    "EmailCustomerGreeting",
                    ActivityOptions.newBuilder()
                        // note that either StartToCloseTimeout or ScheduleToCloseTimeout are
                        // required when setting Activity options.
                        .setStartToCloseTimeout(Duration.ofSeconds(5))
                        .setRetryOptions(
                            RetryOptions.newBuilder()
                                .setDoNotRetry(NullPointerException.class.getName())
                                .build())
                        .build()))
            .build();
  ```

## Activity next retry delay {/* #activity-next-retry-delay */}

You may throw an [`ApplicationFailure`](/references/failures#application-failure) with the `NextRetryDelay` field set. This value will replace and override whatever the retry interval would be on the retry policy.

For example, if in an activity, you want to base the interval on the number of attempts, you might do:

```java
int attempt = Activity.getExecutionContext().getInfo().getAttempt();

throw ApplicationFailure.newFailureWithCauseAndDelay(
    "Something bad happened on attempt " + attempt,
    "my_failure_type",
    null,
    3 * Duration.ofSeconds(attempt));
```

## Heartbeat an Activity {/* #activity-heartbeats */}

An [Activity Heartbeat](/encyclopedia/detecting-activity-failures#activity-heartbeat) is a ping from the [Worker Process](/workers#worker-process) that is executing the Activity to the [Temporal Service](/temporal-service).
Each Heartbeat informs the Temporal Service that the [Activity Execution](/activity-execution) is making progress and the Worker has not crashed.
If the Temporal Service does not receive a Heartbeat within a [Heartbeat Timeout](/encyclopedia/detecting-activity-failures#heartbeat-timeout) time period, the Activity will be considered failed and another [Activity Task Execution](/tasks#activity-task-execution) may be scheduled according to the Retry Policy.

Heartbeats may not always be sent to the Temporal Service—they may be [throttled](/encyclopedia/detecting-activity-failures#throttling) by the Worker.

Activity Cancellations are delivered to Activities from the Temporal Service when they Heartbeat. Activities that don't Heartbeat can't receive a Cancellation.
Heartbeat throttling may lead to Cancellation getting delivered later than expected.

Heartbeats can contain a `details` field describing the Activity's current progress.
If an Activity gets retried, the Activity can access the `details` from the last Heartbeat that was sent to the Temporal Service.

To Heartbeat an Activity Execution in Java, use the `Activity.getExecutionContext().heartbeat()` Class method.

```java
public class YourActivityDefinitionImpl implements YourActivityDefinition {

  @Override
  public String yourActivityMethod(YourActivityMethodParam param) {
    // ...
    Activity.getExecutionContext().heartbeat(details);
    // ...
  }
  // ...
}
```

The method takes an optional argument, the `details` variable above that represents latest progress of the Activity Execution.
This method can take a variety of types such as an exception object, custom object, or string.

If the Activity Execution times out, the last Heartbeat `details` are included in the thrown `ActivityTimeoutException`, which can be caught by the calling Workflow.
The Workflow can then use the `details` information to pass to the next Activity invocation if needed.

In the case of Activity retries, the last Heartbeat's `details` are available and can be extracted from the last failed attempt by using `Activity.getExecutionContext().getHeartbeatDetails(Class<V> detailsClass)`

### Heartbeat Timeout {/* #heartbeat-timeout */}

A [Heartbeat Timeout](/encyclopedia/detecting-activity-failures#heartbeat-timeout) works in conjunction with [Activity Heartbeats](/encyclopedia/detecting-activity-failures#activity-heartbeat).

To set a [Heartbeat Timeout](/encyclopedia/detecting-activity-failures#heartbeat-timeout), use [`ActivityOptions.newBuilder.setHeartbeatTimeout`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/activity/ActivityOptions.Builder.html).

- Type: `Duration`
- Default: None

You can set Activity Options using an `ActivityStub` within a Workflow implementation, or per-Activity using `WorkflowImplementationOptions` within a Worker.
Note that if you define options per-Activity Type options with `WorkflowImplementationOptions.setActivityOptions()`, setting them again specifically with `ActivityStub` in a Workflow will override this setting.

- With `ActivityStub`

  ```java
  private final GreetingActivities activities =
      Workflow.newActivityStub(
          GreetingActivities.class,
          ActivityOptions.newBuilder()
              // note that either StartToCloseTimeout or ScheduleToCloseTimeout are
              // required when setting Activity options.
              .setStartToCloseTimeout(Duration.ofSeconds(5))
              .setHeartbeatTimeout(Duration.ofSeconds(2))
              .build());
  ```

- With `WorkflowImplementationOptions`

  ```java
  WorkflowImplementationOptions options =
        WorkflowImplementationOptions.newBuilder()
            .setActivityOptions(
                ImmutableMap.of(
                "EmailCustomerGreeting",
                    ActivityOptions.newBuilder()
                        // note that either StartToCloseTimeout or ScheduleToCloseTimeout are
                        // required when setting Activity options.
                        .setStartToCloseTimeout(Duration.ofSeconds(5))
                        .setHeartbeatTimeout(Duration.ofSeconds(2))
                        .build()))
            .build();
  ```

---

## Converters and encryption - Java SDK

Temporal's security model is designed around client-side encryption of Payloads.
A client may encrypt Payloads before sending them to the server, and decrypt them after receiving them from the server.
This provides a high degree of confidentiality because the Temporal Server itself has absolutely no knowledge of the actual data.
It also gives implementers more power and more freedom regarding which client is able to read which data -- they can control access with keys, algorithms, or other security measures.

A Temporal developer adds client-side encryption of Payloads by providing a Custom Payload Codec to its Client.
Depending on business needs, a complete implementation of Payload Encryption may involve selecting appropriate encryption algorithms, managing encryption keys, restricting a subset of their users from viewing payload output, or a combination of these.

The server itself never adds encryption over Payloads.
Therefore, unless client-side encryption is implemented, Payload data will be persisted in non-encrypted form to the data store, and any Client that can make requests to a Temporal namespace (including the Temporal UI and CLI) will be able to read Payloads contained in Workflows.
When working with sensitive data, you should always implement Payload encryption.

## Custom Payload Codec in Java {/* #custom-payload-codec */}

Create a custom implementation of [`PayloadCodec`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/payload/codec/PayloadCodec.html) and use it in [`CodecDataConverter`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/common/converter/CodecDataConverter.html) to set a custom Data Converter.

The Payload Codec does byte-to-byte conversion and must be set with a Data Converter.

Define custom encryption/compression logic in your `encode` method and decryption/decompression logic in your `decode` method.

The following example from the [Java encryption sample](https://github.com/temporalio/samples-java/tree/main/core/src/main/java/io/temporal/samples/encryptedpayloads/CryptCodec.java) shows how to implement encryption and decryption logic on your payloads in your `encode` and `decode` methods.

```java
class YourCustomPayloadCodec implements PayloadCodec {

  static final ByteString METADATA_ENCODING =
      ByteString.copyFrom("binary/encrypted", StandardCharsets.UTF_8);

  private static final String CIPHER = "AES/GCM/NoPadding";

  // Define constants that you can add to your encoded Payload to create a new Payload.
  static final String METADATA_ENCRYPTION_CIPHER_KEY = "encryption-cipher";

  static final ByteString METADATA_ENCRYPTION_CIPHER =
      ByteString.copyFrom(CIPHER, StandardCharsets.UTF_8);

  static final String METADATA_ENCRYPTION_KEY_ID_KEY = "encryption-key-id";

  private static final Charset UTF_8 = StandardCharsets.UTF_8;

  // See the linked sample for details on the methods called here.
  @NotNull
  @Override
  public List<Payload> encode(@NotNull List<Payload> payloads) {
    return payloads.stream().map(this::encodePayload).collect(Collectors.toList());
  }

  @NotNull
  @Override
  public List<Payload> decode(@NotNull List<Payload> payloads) {
    return payloads.stream().map(this::decodePayload).collect(Collectors.toList());
  }

  private Payload encodePayload(Payload payload) {
    String keyId = getKeyId();
    SecretKey key = getKey(keyId);

    byte[] encryptedData;
    try {
      encryptedData = encrypt(payload.toByteArray(), key); // The encrypt method contains your custom encryption logic.
    } catch (Throwable e) {
      throw new DataConverterException(e);
    }
    // Apply metadata to the encoded Payload that you can verify in your decode method before decoding.
    // See the sample for details on the metadata values set.
    return Payload.newBuilder()
        .putMetadata(EncodingKeys.METADATA_ENCODING_KEY, METADATA_ENCODING)
        .putMetadata(METADATA_ENCRYPTION_CIPHER_KEY, METADATA_ENCRYPTION_CIPHER)
        .putMetadata(METADATA_ENCRYPTION_KEY_ID_KEY, ByteString.copyFromUtf8(keyId))
        .setData(ByteString.copyFrom(encryptedData))
        .build();
  }

  private Payload decodePayload(Payload payload) {
    // Verify the incoming encoded Payload metadata before applying decryption.
    if (METADATA_ENCODING.equals(
        payload.getMetadataOrDefault(EncodingKeys.METADATA_ENCODING_KEY, null))) {
      String keyId;
      try {
        keyId = payload.getMetadataOrThrow(METADATA_ENCRYPTION_KEY_ID_KEY).toString(UTF_8);
      } catch (Exception e) {
        throw new PayloadCodecException(e);
      }
      SecretKey key = getKey(keyId);
      byte[] plainData;
      Payload decryptedPayload;

      try {
        plainData = decrypt(payload.getData().toByteArray(), key); // The decrypt method contains your custom decryption logic.
        decryptedPayload = Payload.parseFrom(plainData);
        return decryptedPayload;
      } catch (Throwable e) {
        throw new PayloadCodecException(e);
      }
    } else {
      return payload;
    }
  }

  private String getKeyId() {
    // Currently there is no context available to vary which key is used.
    // Use a fixed key for all payloads.
    // This still supports key rotation as the key ID is recorded on payloads allowing
    // decryption to use a previous key.

    return "test-key-test-key-test-key-test!";
  }

  private SecretKey getKey(String keyId) {
    // Key must be fetched from KMS or other secure storage.
    // Hard coded here only for example purposes.
    return new SecretKeySpec(keyId.getBytes(UTF_8), "AES");
  }

  //...
}
```

**Set Data Converter to use custom Payload Codec**

Use `CodecDataConverter` with an instance of a Data Converter and the custom `PayloadCodec` in the `WorkflowClient` options that you use in your Worker process and to start your Workflow Executions.

For example, to set a custom `PayloadCodec` implementation with `DefaultDataConverter`, use the following code:

```java
WorkflowServiceStubs service = WorkflowServiceStubs.newLocalServiceStubs();
  // Client that can be used to start and signal Workflows
  WorkflowClient client =
      WorkflowClient.newInstance(
          service,
          WorkflowClientOptions.newBuilder()
              .setDataConverter(
                  new CodecDataConverter(
                      DefaultDataConverter.newDefaultInstance(),
                      Collections.singletonList(new YourCustomPayloadCodec()))) // Sets the custom Payload Codec created in the previous example with an instance of the default Data Converter.
              .build());
```

- Data **encoding** is performed by the client using the converters and codecs provided by Temporal or your custom implementation when passing input to the Temporal Cluster. For example, plain text input is usually serialized into a JSON object, and can then be compressed or encrypted.
- Data **decoding** may be performed by your application logic during your Workflows or Activities as necessary, but decoded Workflow results are never persisted back to the Temporal Cluster. Instead, they are stored encoded on the Cluster, and you need to provide an additional parameter when using the [temporal workflow show](/cli/command-reference/workflow#show) command or when browsing the Web UI to view output.

For reference, see the [Encryption](https://github.com/temporalio/samples-java/tree/main/core/src/main/java/io/temporal/samples/encryptedpayloads) sample.

### Using a Codec Server

A Codec Server is an HTTP server that uses your custom Codec logic to decode your data remotely.
The Codec Server is independent of the Temporal Cluster and decodes your encrypted payloads through predefined endpoints.
You create, operate, and manage access to your Codec Server in your own environment.
The Temporal CLI and the Web UI in turn provide built-in hooks to call the Codec Server to decode encrypted payloads on demand.
Refer to the [Codec Server](/production-deployment/data-encryption) documentation for information on how to design and deploy a Codec Server.

For reference, see the [Codec server](https://github.com/temporalio/sdk-java/tree/master/temporal-remote-data-encoder) sample.

## Using custom Payload conversion {/* #custom-payload-conversion */}

Temporal SDKs provide a [Payload Converter](/payload-converter) that can be customized to convert a custom data type to [Payload](/dataconversion#payload) and back.

Implementing custom Payload conversion is optional.
It is needed only if the [default Data Converter](/default-custom-data-converters#default-data-converter) does not support your custom values.

To support custom Payload conversion, create a [custom Payload Converter](/payload-converter#composite-data-converters) and configure the Data Converter to use it in your Client options.

The order in which your encoding Payload Converters are applied depend on the order given to the Data Converter.
