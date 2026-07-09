
- [`scheduleToCloseTimeout`](https://typescript.temporal.io/api/interfaces/common.ActivityOptions/#scheduletoclosetimeout)
- [`startToCloseTimeout`](https://typescript.temporal.io/api/interfaces/common.ActivityOptions/#starttoclosetimeout)
- [`scheduleToStartTimeout`](https://typescript.temporal.io/api/interfaces/common.ActivityOptions/#scheduletostarttimeout)

```typescript
const { myActivity } = proxyActivities<typeof activities>({
  scheduleToCloseTimeout: '5m',
  // startToCloseTimeout: "30s", // recommended
  // scheduleToStartTimeout: "60s",
});
```

## Activity Retry Policy {/* #activity-retries */}

**How to set an Activity Retry Policy using the Temporal TypeScript SDK**

A Retry Policy works in cooperation with the timeouts to provide fine controls to optimize the execution experience.

Activity Executions are automatically associated with a default [Retry Policy](/encyclopedia/retry-policies) if a custom one is not provided.

To set an Activity's Retry Policy in TypeScript, assign the [`ActivityOptions.retry`](https://typescript.temporal.io/api/interfaces/common.ActivityOptions#retry) property when creating the corresponding Activity proxy function using the [`proxyActivities()`](https://typescript.temporal.io/api/namespaces/workflow#proxyactivities) API.

```typescript
const { myActivity } = proxyActivities<typeof activities>({
  // ...
  retry: {
    initialInterval: '10s',
    maximumAttempts: 5,
  },
});
```

## Activity next Retry delay {/* #activity-next-retry-delay */}

**How to override the next Retry delay following an Activity failure using the Temporal TypeScript SDK**

The time to wait after a retryable Activity failure until the next retry is attempted is normally determined by that Activity's Retry Policy.
However, an Activity may override that duration when explicitly failing with an [`ApplicationFailure`](https://typescript.temporal.io/api/classes/common.ApplicationFailure) by setting a next Retry delay.

To override the next Retry delay for an `ApplicationFailure` thrown by an Activity in TypeScript, provide the [`nextRetryDelay`](https://typescript.temporal.io/api/interfaces/common.ApplicationFailureOptions#nextretrydelay) property on the object argument of the [`ApplicationFailure.create()`](https://typescript.temporal.io/api/classes/common.ApplicationFailure#create) factory method.

```typescript
throw ApplicationFailure.create({
  // ...
  nextRetryDelay: '15s',
});
```

## Heartbeat an Activity {/* #activity-heartbeats */}

**How to Heartbeat an Activity using the Temporal TypeScript SDK**

An [Activity Heartbeat](/encyclopedia/detecting-activity-failures#activity-heartbeat) is a ping from the [Worker Process](/workers#worker-process) that is executing the Activity to the [Temporal Service](/temporal-service).
Each Heartbeat informs the Temporal Service that the [Activity Execution](/activity-execution) is making progress and the Worker has not crashed.
If the Temporal Service does not receive a Heartbeat within a [Heartbeat Timeout](/encyclopedia/detecting-activity-failures#heartbeat-timeout) time period, the Activity will be considered as timed out and another [Activity Task Execution](/tasks#activity-task-execution) may be scheduled according to the Retry Policy.

Activity Cancellations are delivered to Activities from the Temporal Service when they Heartbeat.
Activities that don't Heartbeat can't get notified of Cancellation requests.

:::note Handling Activity Cancellation
In the TypeScript SDK, Activity implementations must opt in to observe cancellation.

Use one of the following in your Activity to be notified of cancellation:
- `await Context.current().cancelled` — rejects with `CancelledFailure`.
- `await Context.current().sleep(ms)` — rejects on cancellation.
- Pass `Context.current().cancellationSignal` (an `AbortSignal`) to libraries that support abort.

> **Important:** Activities receive cancellation notifications when they heartbeat; if an Activity doesn’t heartbeat, delivery of the cancellation notification can be delayed.

See [Activity namespace reference](https://typescript.temporal.io/api/namespaces/activity#cancellation) and [Context API](https://typescript.temporal.io/api/classes/activity.Context) for more information.
:::

Heartbeats may not always be sent to the Temporal Service—they may be [throttled](/encyclopedia/detecting-activity-failures#throttling) by the Worker.
Heartbeat throttling may lead to Cancellation getting delivered later than expected.

To Heartbeat an Activity Execution in TypeScript, call the [`heartbeat()`](https://typescript.temporal.io/api/namespaces/activity#heartbeat) function from the Activity implementation.

```typescript
export async function myActivity(): Promise<void> {
  for (let progress = 1; progress <= 1000; ++progress) {
    // Do something that takes time
    await sleep('1s');

    heartbeat();
  }
}
```

An Activity may optionally checkpoint its progression, by providing a `details` argument to the [`heartbeat()`](https://typescript.temporal.io/api/namespaces/activity#heartbeat) function.
Should the Activity Execution times out and gets retried, then the Temporal Server will provide the `details` from the last Heartbeat it received to the next Activity Execution.
This can be used to allow the Activity to efficiently resume its work.

```typescript
export async function myActivity(): Promise<void> {
  // Resume work from latest heartbeat, if there's one, or start from 1 otherwise
  const startingPoint = activityInfo().heartbeatDetails?.progress ?? 1;

  for (let progress = startingPoint; progress <= 1000; ++progress) {
    // Do something that takes time
    await sleep('1s');

    heartbeat({ progress });
  }
}
```

## Activity Heartbeat Timeout {/* #activity-heartbeat-timeout */}

**How to set a Heartbeat Timeout using the Temporal TypeScript SDK**

A [Heartbeat Timeout](/encyclopedia/detecting-activity-failures#heartbeat-timeout) works in conjunction with [Activity Heartbeats](/encyclopedia/detecting-activity-failures#activity-heartbeat).
If the Temporal Server doesn't receive a Heartbeat before expiration of the Heartbeat Timeout, the Activity is considered as timed out and another [Activity Task Execution](/tasks#activity-task-execution) may be scheduled according to the Retry Policy.

To set an Activity's Heartbeat Timeout in TypeScript, set the [`ActivityOptions.heartbeatTimeout`](https://typescript.temporal.io/api/interfaces/common.ActivityOptions#heartbeattimeout) property when creating the corresponding Activity proxy functions using the [`proxyActivities()`](https://typescript.temporal.io/api/namespaces/workflow#proxyactivities) API.

```typescript
const { myLongRunningActivity } = proxyActivities<typeof activities>({
  // ...
  heartbeatTimeout: '30s',
});
```

---

## Converters and encryption - TypeScript SDK

## Payload Converter and Payload Codec Summary

This section summarizes the difference between a Payload Converter and Payload Codec.

### Payload Converter

Payload Converters are responsible for serializing application objects into a Payload and deserializing them back into application objects. A Payload, in this context, is a binary form suitable for network transmission that may include some metadata. This serialization process transforms an object (like those in JSON or Protobuf formats) into a binary format and vice versa. For example, an object might be serialized to JSON with UTF-8 byte encoding or to a protobuf binary using a specific set of protobuf message definitions.

Due to their operation within the Workflow context, Payload Converters run inside the Workflow sandbox. Consequently, Payload Converters cannot access external services or employ non-deterministic modules, which excludes most types of encryption due to their non-deterministic nature.

### Payload Codec

Payload Codecs transform one Payload into another, converting binary data to a different binary format. Unlike Payload Converters, Payload Codecs do not operate within the Workflow sandbox. This allows them to execute operations that can include calls to remote services and the use of non-deterministic modules, which are critical for tasks such as encrypting Payloads, compressing data, or offloading large payloads to an object store. Payload Codecs can also be implemented as a Codec Server (which will be described later on).

### Operational Chain

In practice, these two components operate in a chain to handle data securely. Incoming data first passes through a Payload Converter through the `toPayload` method, turning application objects into Payloads. These Payloads are then processed by the Payload Codec through the `encode` method, which adjusts the Payload according to the required security or efficiency needs before it is sent to the Temporal Cluster.

The process is symmetric for outgoing data. Payloads retrieved from the Temporal Cluster first pass through the Payload Codec through the `decode` method, which reverses any transformations applied during encoding. Finally, the resulting Payload is converted back into an application object by the Payload Converter through the `fromPayload` method, making it ready for use within the application.

## Payload Codec

> API documentation: [PayloadCodec](https://typescript.temporal.io/api/interfaces/common.PayloadCodec)

The default `PayloadCodec` does nothing. To create a custom one, you can implement the following interface:

```ts
interface PayloadCodec {
  /**
   * Encode an array of {@link Payload}s for sending over the wire.
   * @param payloads May have length 0.
   */
  encode(payloads: Payload[]): Promise<Payload[]>;

  /**
   * Decode an array of {@link Payload}s received from the wire.
   */
  decode(payloads: Payload[]): Promise<Payload[]>;
}
```

## Use custom payload conversion

Temporal SDKs provide a [Payload Converter](/payload-converter) that can be customized to convert a custom data type to a [Payload](/dataconversion#payload) and back.

The order in which your encoding Payload Converters are applied depends on the order given to the Data Converter.
You can set multiple encoding Payload Converters to run your conversions.
When the Data Converter receives a value for conversion, the value gets passed through each Payload Converter in sequence until the converter that handles the data type does the conversion.

## Composite Data Converters

Use a [Composite Data Converter](https://typescript.temporal.io/api/classes/common.CompositePayloadConverter) to apply custom, type-specific Payload Converters in a specified order. Defining a new Composite Data Converter is not always necessary to implement custom data handling. You can override the default Converter with a custom Codec, but a Composite Data Converter may be necessary for complex Workflow logic.

A Composite Data Converter can include custom rules created, and it can also
leverage the default Data Converters built into Temporal. In fact, the default
Data Converter logic is implemented internally in the Temporal source as a
Composite Data Converter. It defines these rules in this order:

```typescript
export class DefaultPayloadConverter extends CompositePayloadConverter {
  constructor() {
    super(
      new UndefinedPayloadConverter(),
      new BinaryPayloadConverter(),
      new JsonPayloadConverter(),
    );
  }
}
```

The order of applying the Payload Converters is important. During
serialization, the Data Converter tries the Payload Converters in that specific
order until a Payload Converter returns a non-null Payload.

To replace the default Data Converter with a custom `CompositeDataConverter`, use the following:

```typescript
export const payloadConverter = new CompositePayloadConverter(
  new UndefinedPayloadConverter(),
  new EjsonPayloadConverter(),
);
```

You can do this in its own `payload-converter.ts` file for example.

In the code snippet above, a converter is created that first attempts to handle `null` and `undefined` values. If the value isn't `null` or `undefined`, the EJSON serialization logic written in the `EjsonPayloadConverter` is then used. The Payload Converter is then provided to the Worker and Client.

Here is the Worker code:

```typescript
const worker = await Worker.create({
  workflowsPath: require.resolve('./workflows'),
  taskQueue: 'ejson',
  dataConverter: {
    payloadConverterPath: require.resolve('./payload-converter'),
  },
});
```

With this code, you now ensure that the Worker serializes and deserializes Workflow and Activity inputs and outputs using your EJSON-based logic, along with handling undefined values appropriately.

Here is the Client:

```typescript
const client = new Client({
  dataConverter: {
    payloadConverterPath: require.resolve('./payload-converter'),
  },
});
```

You can now use a variety of data types in arguments.

## How to use a custom payload converter in TypeScript {/* #custom-payload-conversion */}

To support custom Payload conversion, create a [custom Payload Converter](/payload-converter#composite-data-converters) and configure the Data Converter to use it in your Client options.
You can use Custom Payload Converters to change how application objects get serialized to binary Payload. To handle custom data types that are not natively JSON-serializable (e.g., `BigInt`, `Date`, or binary data), you can create a custom Payload Converter. A Custom Payload Converter is responsible for converting your custom data types to a payload format that Temporal can manage.

To implement a Custom Payload Converter in TypeScript, you need to do the following steps:

1. **Implement `PayloadConverter` Interface**: Start by creating a class that implements Temporal's [`PayloadConverter`](https://typescript.temporal.io/api/interfaces/common.PayloadConverter) interface.

```typescript
interface PayloadConverter {
  /**
   * Converts a value to a {@link Payload}.
   * @param value The value to convert. Example values include the Workflow args sent by the client and the values returned by a Workflow or Activity.
   */
  toPayload<T>(value: T): Payload;

  /**
   * Converts a {@link Payload} back to a value.
   */
  fromPayload<T>(payload: Payload): T;
}
```

This custom converter should include logic for both serialization (`toPayload`) and deserialization (`fromPayload`), handling your specific data types or serialization format. The method `toPayload` returns a Payload object, which is used to manage and transport serialized data. The method `fromPayload` returns the deserialized data. This ensures that the data returned is in the same format as it was before serialization, allowing it to be used directly in the application.

2. Configure the Data Converter. To send values that are not JSON-serializable like a `BigInt` or `Date`, provide the custom Data Converter to the Client and Worker as described in the [Composite Data Converters](#composite-data-converters) section.

#### Custom implementation

Some example implementations are in the SDK itself:

- [common/src/converter/payload-converter.ts](https://github.com/temporalio/sdk-typescript/blob/main/packages/common/src/converter/payload-converter.ts)
- [common/src/converter/protobuf-payload-converters.ts](https://github.com/temporalio/sdk-typescript/blob/main/packages/common/src/converter/protobuf-payload-converters.ts)

The sample project [samples-typescript/ejson](https://github.com/temporalio/samples-typescript/tree/main/ejson) creates an EJSON custom `PayloadConverter`.
It implements `PayloadConverterWithEncoding` instead of `PayloadConverter` so that it could be used with [CompositePayloadConverter](https://typescript.temporal.io/api/classes/common.CompositePayloadConverter/):

<!--SNIPSTART typescript-ejson-converter-impl -->
[ejson/src/ejson-payload-converter.ts](https://github.com/temporalio/samples-typescript/blob/main/ejson/src/ejson-payload-converter.ts)
```ts

  EncodingType,
  METADATA_ENCODING_KEY,
  Payload,
  PayloadConverterWithEncoding,
  PayloadConverterError,
} from '@temporalio/common';

/**
 * Converts between values and [EJSON](https://docs.meteor.com/api/ejson.html) Payloads.
 */
export class EjsonPayloadConverter implements PayloadConverterWithEncoding {
  // Use 'json/plain' so that Payloads are displayed in the UI
  public encodingType = 'json/plain' as EncodingType;

  public toPayload(value: unknown): Payload | undefined {
    if (value === undefined) return undefined;
    let ejson;
    try {
      ejson = EJSON.stringify(value);
    } catch (e) {
      throw new UnsupportedEjsonTypeError(
        `Can't run EJSON.stringify on this value: ${value}. Either convert it (or its properties) to EJSON-serializable values (see https://docs.meteor.com/api/ejson.html ), or create a custom data converter. EJSON.stringify error message: ${errorMessage(
          e,
        )}`,
        e as Error,
      );
    }

    return {
      metadata: {
        [METADATA_ENCODING_KEY]: encode('json/plain'),
        // Include an additional metadata field to indicate that this is an EJSON payload
        format: encode('extended'),
      },
      data: encode(ejson),
    };
  }

  public fromPayload<T>(content: Payload): T {
    return content.data ? EJSON.parse(decode(content.data)) : content.data;
  }
}

export class UnsupportedEjsonTypeError extends PayloadConverterError {
  public readonly name: string = 'UnsupportedJsonTypeError';

  constructor(
    message: string | undefined,
    public readonly cause?: Error,
  ) {
    super(message ?? undefined);
  }
}
```
<!--SNIPEND-->

Then we instantiate one and export it:

<!--SNIPSTART typescript-ejson-converter -->
[ejson/src/payload-converter.ts](https://github.com/temporalio/samples-typescript/blob/main/ejson/src/payload-converter.ts)
```ts

export const payloadConverter = new CompositePayloadConverter(
  new UndefinedPayloadConverter(),
  new EjsonPayloadConverter(),
);
```
<!--SNIPEND-->

We provide it to the Worker and Client:

<!--SNIPSTART typescript-ejson-worker -->
[ejson/src/worker.ts](https://github.com/temporalio/samples-typescript/blob/main/ejson/src/worker.ts)
```ts
const worker = await Worker.create({
  workflowsPath: require.resolve('./workflows'),
  taskQueue: 'ejson',
  dataConverter: { payloadConverterPath: require.resolve('./payload-converter') },
});
```
<!--SNIPEND-->

<!--SNIPSTART typescript-ejson-client-setup -->
[ejson/src/client.ts](https://github.com/temporalio/samples-typescript/blob/main/ejson/src/client.ts)
```ts
const client = new Client({
  connection,
  dataConverter: { payloadConverterPath: require.resolve('./payload-converter') },
});
```
<!--SNIPEND-->

Then we can use supported data types in arguments:

<!--SNIPSTART typescript-ejson-client -->
[ejson/src/client.ts](https://github.com/temporalio/samples-typescript/blob/main/ejson/src/client.ts)
```ts
const user: User = {
  id: uuid(),
  // age: 1000n, BigInt isn't supported
  hp: Infinity,
  matcher: /.*Stormblessed/,
  token: Uint8Array.from([1, 2, 3]),
  createdAt: new Date(),
};

const handle = await client.workflow.start(example, {
  args: [user],
  taskQueue: 'ejson',
  workflowId: `example-user-${user.id}`,
});
```
<!--SNIPEND-->

And they get parsed correctly for the Workflow:

<!--SNIPSTART typescript-ejson-workflow -->
[ejson/src/workflows.ts](https://github.com/temporalio/samples-typescript/blob/main/ejson/src/workflows.ts)
```ts

export async function example(user: User): Promise<Result> {
  const success =
    user.createdAt.getTime() < Date.now() &&
    user.hp > 50 &&
    user.matcher.test('Kaladin Stormblessed') &&
    user.token instanceof Uint8Array;
  return { success, at: new Date() };
}
```
<!--SNIPEND-->

#### Protobufs

To serialize values as [Protocol Buffers](https://protobuf.dev/) (protobufs):

- Use [protobufjs](https://protobufjs.github.io/protobuf.js/).
- Use runtime-loaded messages (not generated classes) and `MessageClass.create` (not `new MessageClass()`).
- Generate `json-module.js` with a command like the following:

  ```sh
  pbjs -t json-module --workflow-id commonjs -o protos/json-module.js protos/*.proto
  ```

- Patch `json-module.js`:

<!--SNIPSTART typescript-protobuf-root -->
[protobufs/protos/root.js](https://github.com/temporalio/samples-typescript/blob/main/protobufs/protos/root.js)
```js
const { patchProtobufRoot } = require('@temporalio/common/lib/protobufs');
const unpatchedRoot = require('./json-module');
module.exports = patchProtobufRoot(unpatchedRoot);
```
<!--SNIPEND-->

- Generate `root.d.ts` with the following command:

  ```sh
  pbjs -t static-module protos/*.proto | pbts -o protos/root.d.ts -
  ```

- Create a [`DefaultPayloadConverterWithProtobufs`](https://typescript.temporal.io/api/classes/protobufs.DefaultPayloadConverterWithProtobufs/):

<!--SNIPSTART typescript-protobuf-converter -->
[protobufs/src/payload-converter.ts](https://github.com/temporalio/samples-typescript/blob/main/protobufs/src/payload-converter.ts)
```ts

export const payloadConverter = new DefaultPayloadConverterWithProtobufs({ protobufRoot: root });
```
<!--SNIPEND-->

Alternatively, we can use Protobuf Payload Converters directly, or with other converters.
If we know that we only use Protobuf objects, and we want them binary encoded (which saves space over proto3 JSON, but can't be viewed in the Web UI), we could do the following:

```ts

export const payloadConverter = new ProtobufBinaryPayloadConverter(root);
```

Similarly, if we wanted binary-encoded Protobufs in addition to the other default types, we could do the following:

```ts

  BinaryPayloadConverter,
  CompositePayloadConverter,
  JsonPayloadConverter,
  UndefinedPayloadConverter,
} from '@temporalio/common';

export const payloadConverter = new CompositePayloadConverter(
  new UndefinedPayloadConverter(),
  new BinaryPayloadConverter(),
  new ProtobufBinaryPayloadConverter(root),
  new JsonPayloadConverter(),
);
```

- Provide it to the Worker:

<!--SNIPSTART typescript-protobuf-worker -->
[protobufs/src/worker.ts](https://github.com/temporalio/samples-typescript/blob/main/protobufs/src/worker.ts)
```ts
const worker = await Worker.create({
  workflowsPath: require.resolve('./workflows'),
  activities,
  taskQueue: 'protobufs',
  dataConverter: { payloadConverterPath: require.resolve('./payload-converter') },
});
```
<!--SNIPEND-->

[WorkerOptions.dataConverter](https://typescript.temporal.io/api/interfaces/worker.WorkerOptions#dataconverter)

- Provide it to the Client:

<!--SNIPSTART typescript-protobuf-client -->
[protobufs/src/client.ts](https://github.com/temporalio/samples-typescript/blob/main/protobufs/src/client.ts)
```ts

async function run() {
  const config = loadClientConnectConfig();
  const connection = await Connection.connect(config.connectionOptions);
  const client = new Client({
    connection,
    dataConverter: { payloadConverterPath: require.resolve('./payload-converter') },
  });

  const handle = await client.workflow.start(example, {
    args: [foo.bar.ProtoInput.create({ name: 'Proto', age: 2 })],
    // can't do:
    // args: [new foo.bar.ProtoInput({ name: 'Proto', age: 2 })],
    taskQueue: 'protobufs',
    workflowId: 'my-business-id-' + uuid(),
  });

  console.log(`Started workflow ${handle.workflowId}`);

  const result: ProtoResult = await handle.result();
  console.log(result.toJSON());
}
```
<!--SNIPEND-->

- Use protobufs in your Workflows and Activities:

<!--SNIPSTART typescript-protobuf-workflow -->
[protobufs/src/workflows.ts](https://github.com/temporalio/samples-typescript/blob/main/protobufs/src/workflows.ts)
```ts

const { protoActivity } = proxyActivities<typeof activities>({
  startToCloseTimeout: '1 minute',
});

export async function example(input: foo.bar.ProtoInput): Promise<ProtoResult> {
  const result = await protoActivity(input);
  return result;
}
```
<!--SNIPEND-->

<!--SNIPSTART typescript-protobuf-activity -->
[protobufs/src/activities.ts](https://github.com/temporalio/samples-typescript/blob/main/protobufs/src/activities.ts)
```ts

export async function protoActivity(input: foo.bar.ProtoInput): Promise<ProtoResult> {
  return ProtoResult.create({ sentence: `${input.name} is ${input.age} years old.` });
}
```
<!--SNIPEND-->

#### Encryption

> Background: [Encryption](/payload-codec#encryption)

The following is an example class that implements the `PayloadCodec` interface:

<!--SNIPSTART typescript-encryption-codec -->
[encryption/src/encryption-codec.ts](https://github.com/temporalio/samples-typescript/blob/main/encryption/src/encryption-codec.ts)
```ts

const ENCODING = 'binary/encrypted';
const METADATA_ENCRYPTION_KEY_ID = 'encryption-key-id';

export class EncryptionCodec implements PayloadCodec {
  constructor(
    protected readonly keys: Map<string, crypto.CryptoKey>,
    protected readonly defaultKeyId: string,
  ) {}

  static async create(keyId: string): Promise<EncryptionCodec> {
    const keys = new Map<string, crypto.CryptoKey>();
    keys.set(keyId, await fetchKey(keyId));
    return new this(keys, keyId);
  }

  async encode(payloads: Payload[]): Promise<Payload[]> {
    return Promise.all(
      payloads.map(async (payload) => ({
        metadata: {
          [METADATA_ENCODING_KEY]: encode(ENCODING),
          [METADATA_ENCRYPTION_KEY_ID]: encode(this.defaultKeyId),
        },
        // Encrypt entire payload, preserving metadata
        data: await encrypt(
          temporal.api.common.v1.Payload.encode(payload).finish(),
          this.keys.get(this.defaultKeyId)!, // eslint-disable-line @typescript-eslint/no-non-null-assertion
        ),
      })),
    );
  }

  async decode(payloads: Payload[]): Promise<Payload[]> {
