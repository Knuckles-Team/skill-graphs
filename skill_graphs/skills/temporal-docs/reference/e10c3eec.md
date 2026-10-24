
Each piece of data (like a single argument or return value) is encoded as a [Payload](/dataconversion#payload), which consists of binary data and key-value metadata.

For details, see the API references:

- [Go](https://pkg.go.dev/go.temporal.io/sdk/converter#DataConverter)
- [Java](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/common/converter/DataConverter.html)
- [Python](https://python.temporal.io/temporalio.converter.DataConverter.html)
- [TypeScript](https://typescript.temporal.io/api/interfaces/common.DataConverter)

### What is a Payload? {/* #payload */}

A [Payload](https://api-docs.temporal.io/#temporal.api.common.v1.Payload) represents binary data such as input and output from Activities and Workflows.
Payloads also contain metadata that describe their data type or other parameters for use by custom encoders/converters.

When processed through the SDK, the [default Data Converter](/default-custom-data-converters#default-data-converter) serializes your data/value to a Payload before sending it to the Temporal Server.
The default Data Converter processes supported type values to Payloads. You can create a custom [Payload Converter](/payload-converter) to apply different conversion steps.

You can additionally apply [custom codecs](/payload-codec), such as for encryption or compression, on your Payloads.

---

## Default and Custom Data Converters

This page discusses the following:

- [Default Data Converter](#default-data-converter)
- [Custom Data Converter](#custom-data-converter)

## What is a default Data Converter? {/* #default-data-converter */}

Each Temporal SDK includes and uses a default Data Converter.
The default Data Converter converts objects to bytes using a series of Payload Converters and supports binary, Protobufs, and JSON formats.
It encodes values in the following order:

- Null
- Byte array
- Protobuf JSON
- JSON

In SDKs that cannot determine parameter types at runtime (for example, TypeScript), Protobufs aren't included in the default converter.

For example:

- If a value is an instance of a Protobuf message, it is encoded with [proto3 JSON](https://developers.google.com/protocol-buffers/docs/proto3#json).
- If a value isn't null, binary, or a Protobuf, it is encoded as JSON. Most common input types — including strings, integers, floating point numbers, and booleans — are serializable as JSON. If any part of it is not serializable as JSON, {/* (for example, a Date—see JSON data types) */} an error is thrown.

The default Data Converter serializes objects based on their root type, rather than nested types.
The JSON serializers of some SDKs cannot process lists with Protobuf children objects without implementing a [custom Data Converter](#custom-data-converter).

## What is a custom Data Converter? {/* #custom-data-converter */}

A custom Data Converter extends the default Data Converter with custom logic for [Payload](/dataconversion#payload) conversion or encoding.

You can create a custom Data Converter to alter formats (for example, using [MessagePack](https://msgpack.org/) instead of JSON) or add compression and encryption.

A Payload Codec encodes and decodes [Payloads](/dataconversion#payload), with bytes-to-bytes conversion.
To use custom encryption or compression logic, create a custom Payload Codec with your encryption/compression logic in the `encode` function and your decryption/decompression logic in the `decode` function.
To implement a custom Payload Codec, you can override the default Data Converter, or create a customized Data Converter that defines its own Payload Converter.

Custom Data Converters are not applied to all data; for example, [Search Attributes](/search-attribute) are persisted unencoded so they can be indexed for searching.

A customized Data Converter can have the following three components:

- [Payload Converter](/payload-converter)
- [Payload Codec](/payload-codec)
- [Failure Converter](/failure-converter)

For details on how to implement custom encryption and compression in your SDK, see [Data Encryption](/production-deployment/data-encryption).

---

## External Storage

:::info Release, stability, and dependency info

External Storage is in [Public Preview](/evaluate/development-production-features/release-stages#public-preview). APIs
and configuration may change before General Availability. Join the
[#large-payloads Slack channel](https://temporalio.slack.com/archives/C09VA2DE15Y) to provide feedback or ask for help.

:::

External Storage offloads payloads to an external store (such as Amazon S3) and passes a small reference token through
the Event History instead. This is called the
[claim check pattern](https://dataengineering.wiki/Concepts/Software+Engineering/Claim+Check+Pattern).

For SDK-specific usage guides, see:

- [Go SDK: Large payload storage](/develop/go/data-handling/external-storage)
- [Python SDK: Large payload storage](/develop/python/data-handling/external-storage)

## Why use External Storage

The Temporal Service enforces a maximum per-payload size. The default and recommended limit is 2 MB. Self-hosted users
can [configure this limit](/self-hosted-guide/defaults), but it is fixed at 2 MB on Temporal Cloud. Payloads that exceed
this limit fail the operation. Without External Storage, you must restructure your code to work around the limit, for
example by splitting data across multiple Workflows.

Even when individual payloads stay under the hard limit, payload data accumulates in Event History. Every Activity input
and output is persisted, so Workflows that pass data through many Activities can see history size grow quickly. Large
histories degrade Workflow Task latency. You may use [Continue-as-New](/workflow-execution/continue-as-new) to work
around this problem, but that comes with other tradeoffs.

External Storage addresses several common scenarios:

- **Data processing pipelines.** Workflows that process documents, images, or other large blobs can exceed the
  per-payload limit.
- **AI agent conversations.** Long conversation histories grow with each turn, and the cumulative size can degrade
  Workflow performance.
- **Spiky data sizes.** Some Workflows handle data that is usually small but occasionally large. The Claim check pattern
  handles these spikes transparently, offloading only the payloads that exceed the size threshold.
- **Migration to Temporal Cloud.** Self-hosted deployments may have higher configured payload limits. External Storage
  lets you migrate to Cloud without restructuring Workflows that exceed the 2 MB limit.
- **Data governance.** While Temporal supports end-to-end client-side encryption, some organizations prefer to store
  payload data in infrastructure they control. Set the offload size threshold to zero to externalize all payloads
  regardless of size.

For SDK-specific usage guides, see:

- [Go SDK: Large payload storage](/develop/go/data-handling/external-storage)
- [Python SDK: Large payload storage](/develop/python/data-handling/external-storage)

## How External Storage fits in the data conversion pipeline {/* #data-pipeline */}

During [Data Conversion](/dataconversion), External Storage sits at the end of the pipeline, after both the
[Payload Converter](/payload-converter) and the [Payload Codec](/payload-codec):

<CaptionedImage
  src="/diagrams/data-converter-flow-with-external-storage.svg"
  srcDark="/diagrams/data-converter-flow-dark.svg"
  title="The Flow of Data through a Data Converter"
  alt="The Flow of Data through a Data Converter"
/>

When a Temporal Client sends a payload that exceeds the configured size threshold, the storage driver uploads the
payload to your external store and replaces it with a lightweight reference. Payloads below the threshold stay inline in
the Event History.

When the Temporal Service dispatches Tasks to the Worker, the process reverses. The Worker downloads the referenced
payloads from external storage in parallel, then passes them back through the Payload Codec and Payload Converter to
reconstruct the original data.

The SDK parallelizes uploads and downloads to minimize latency. When a single Workflow Task involves multiple payloads
that exceed the threshold, the SDK uploads or downloads all of them concurrently rather than one at a time. This allows
external storage operations to scale well even when a Task carries many large payloads.

When a payload is offloaded to external storage, the Temporal UI displays a reference token instead of the actual data.
This is expected. Your application code receives the fully decoded result because the SDK transparently retrieves the
payload from external storage before returning it to your Workflow or Client.

Because External Storage runs after the Payload Codec, if you use an encryption codec, payloads are already encrypted
before upload to your store.

## Choose a storage system {/* #choose-storage */}

A production storage system should meet the following requirements:

- Store payload data durably and retain it for the full Workflow lifetime plus the Namespace retention period. See
  [Lifecycle management](#lifecycle) for details.
- Be reachable from every Client, Worker, and Codec Server that encodes or decodes payloads.
- Support your expected payload sizes.
- Return consistent data immediately after a write completes.
- Meet your latency and throughput requirements under realistic load.
- Provide appropriate controls for authentication, encryption, monitoring, and backup.

Start with an object store such as Amazon S3, Google Cloud Storage, or Azure Blob Storage unless you have a specific
reason to use a different system, such as lower latency or existing infrastructure constraints.

- **Amazon S3, Google Cloud Storage, Azure Blob Storage:** Default choice for durable payload storage. We provide a
  first-party S3 storage driver for the [Go](/develop/go/data-handling/external-storage#store-and-retrieve-large-payloads-with-amazon-s3) and [Python](/develop/python/data-handling/external-storage#store-and-retrieve-large-payloads-with-amazon-s3) SDKs.
- **Google Cloud Bigtable:** Low-latency reads on Google Cloud, but payloads must fit within Bigtable's cell and row size limits.
- **Redis:** Suitable when configured for durability (such as with AOF persistence), not as an evicting cache. Refer to the [Python Redis storage driver sample](https://github.com/temporalio/samples-python/tree/main/external_storage_redis) for an example implementation.

## Storage drivers

A storage driver connects External Storage to a backing store. Each driver provides two operations:

- **Store**. Upload payloads and return a claim, which is a set of key-value pairs the driver uses to locate the payload
  later.
- **Retrieve**. Download payloads using the claims that `store` produced.

The S3 driver also includes diagnostic metadata in error messages, such as the AWS region, to help with troubleshooting
storage failures.

Temporal SDKs include built-in drivers for common storage systems like Amazon S3. You can configure multiple storage
drivers and use a selector function to route payloads to different drivers based on size, type, or other criteria such
as hot and cold storage tiers.

### Custom storage drivers

If the built-in drivers don't support your storage backend, you can implement a custom driver. For SDK-specific
examples, see:

- [Go SDK: Implement a custom storage driver](/develop/go/data-handling/external-storage#implement-a-custom-storage-driver)
- [Python SDK: Implement a custom storage driver](/develop/python/data-handling/external-storage#implement-a-custom-storage-driver)

For example, see the
[Redis storage driver sample](https://github.com/temporalio/samples-python/tree/main/external_storage_redis).

## Key configuration settings

Configure External Storage on the Data Converter. The key settings are:

- **Size threshold**. The driver offloads payloads larger than this value, which defaults to 256 KiB.
- **Drivers**. One or more storage driver implementations.
- **Driver selector**. When using multiple drivers, you must provide a function that chooses which driver handles each
  payload.

## Lifecycle management for external storage {/* #lifecycle */}

Temporal does not automatically delete payloads from your external store. Payloads can also be orphaned if a request
fails after the upload completes. We recommend you configure a lifecycle policy that both ensures these payloads are
eventually cleaned up and provides a grace period for debugging and recovery.

Your TTL must be long enough that payloads remain available for the entire lifetime of the Workflow plus its retention
window:

```
TTL > Maximum Workflow Run Timeout + Namespace Retention Period
```

For example, if your longest-running Workflow has a Run Timeout of 14 days and your Namespace retention period is 30
days, configure your lifecycle rule to expire objects after at least 44 days.

If your Workflows run indefinitely (no Run Timeout), there is no finite TTL that guarantees safety. Set a generous TTL
based on your operational needs. Use [Continue-as-New](/workflow-execution/continue-as-new) for Workflows that need to
run longer. The new run uploads fresh payloads, and the old run's payloads only need to survive through its retention
period.

## Durable External Storage {/* #durable-external-storage */}

External Storage stores payloads in a single storage backend. If that backend becomes unavailable, Workers can't
retrieve payloads. To protect against regional or provider failures, implement your drivers in a way that takes
advantage of your storage provider's redundancy features, such as cross-region replication and multi-region routing.

### S3 Multi-Region Access Points

The built-in S3 storage driver supports
[S3 Multi-Region Access Points (MRAP)](https://aws.amazon.com/s3/features/multi-region-access-points/) as the bucket
endpoint. Combined with
[Cross-Region Replication (CRR)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html), this gives you
automatic failover across regions: if a bucket or region becomes unavailable, requests route to the closest healthy
bucket.

For setup instructions, see
[Configuring S3 Multi-Region Access Points with replication](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiRegionAccessPointBucketReplication.html)
in the AWS documentation. After creating the MRAP, configure the External Storage S3 driver to use the MRAP ARN in place
of the bucket name.

### Replication tradeoffs

Cross-region replication introduces eventual consistency. After a write, a read in another region may temporarily miss
the object. To mitigate:

- Ensure Activities that read from External Storage have appropriate retry policies, so they recover from transient
  unavailability caused by replication lag.
- If an Activity needs to read a payload immediately after it is written, prefer scheduling it on the same Worker or in
  the same region to avoid the lag window.

By default, S3 CRR has no SLA on replication time. If you need stronger guarantees, enable
[Replication Time Control](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication-time-control.html).

Replication and versioning can also significantly increase storage costs. Check your provider's pricing before enabling.

---

## Failure Converter

This page discusses [Failure Converter](#failure-converter).

## What is a Failure Converter? {/* #failure-converter */}

As with input and output, Temporal also uses its own default converter logic for errors that are generated by Workflows.
The default Failure Converter copies error messages and call stacks as plain text, and this text output is then directly accessible in the `Message` field of these Workflow Executions.

This may be undesirable for your application. In some cases, errors could contain privileged or sensitive information that you would need to prevent from leaking or being available via a side channel.
Failure messages and call stacks are not encoded as codec-capable Payloads by default; you must explicitly enable encoding these common attributes on failures.

If your errors might contain sensitive information, you can encrypt the message and call stack by configuring the default Failure Converter to use your encoding.
This moves your `message` and `stack_trace` fields to a Payload that's run through your codec.

For example, with the Temporal Go SDK, you can do this by adding a `FailureConverter` parameter to your `client.Options{}` array when calling `client.Dial()`.
The `FailureConverter` should override the `DefaultFailureConverterOptions{}` by setting `EncodeCommonAttributes: true` like so:

```go
c, err := client.Dial(client.Options{
	// Set DataConverter here to ensure that workflow inputs and results are
	// encoded as required.
	DataConverter: mycustom.DataConverter,
	FailureConverter: temporal.NewDefaultFailureConverter(temporal.DefaultFailureConverterOptions{
		EncodeCommonAttributes: true,
	}),
})
```

If for some reason you need to specify a different set of Converter logic for your Failures, you can replace the `NewDefaultFailureConverter` with a custom method.
For example, if you are both working with highly sensitive data and using a sophisticated logging/observability implementation, you may need to implement different encryption methods for each of them.

---

## Key management

This page discusses [Key Management](#key-management).

## What is Key Management? {/* #key-management */}

Key Management is a fundamental part of working with encryption keys.

There are many computational and logistical aspects to generating and rotating keys, and this usually calls for a dedicated application in your stack. Here are some general recommendations for working with encryption keys for Temporal applications:

- [Symmetric Encryption](https://en.wikipedia.org/wiki/Symmetric-key_algorithm) is generally faster and will produce smaller payloads than asymmetric. Normally, an advantage of _asymmetric_ encryption is that it allows you to distribute your encryption and decryption keys separately, but depending on your infrastructure, this might not offer any security benefits with Temporal.

- AES-based algorithms are [hardware accelerated in Go](https://pkg.go.dev/crypto/aes) and other languages. AES algorithms are widely vetted and trusted, and there are many different variants that may suit your requirements. Load tests using `ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY` have performed well.

- Store your encryption keys in the same manner as you store passwords, config details, and other sensitive data. When possible, load the key into your application, so you don't need to make a network call to retrieve it. Separate keys for each environment or namespace as much as possible.

- Make sure you have a key rotation strategy in place in the event that your keys are compromised or need to be replaced for another reason. Consider using a dedicated secrets engine or a key management system (KMS). Note that when you rotate keys, you may also need to retain old keys to query old Workflows.

### Key Rotation

National Institute of Standards and Technology (NIST) guidance recommends periodic rotation of encryption keys. For AES-GCM keys, rotation should occur before approximately 2^32 encryptions have been performed by a key version, following the guidelines of NIST publication 800-38D.

It is recommended that operators estimate the encryption rate of a key and use that to determine a frequency of rotation that prevents the guidance limits from being reached. For example, if one determines that the estimated rate is 40 million operations per day, then rotating a key every three months is sufficient.

Key rotation should generally be transparent to the Temporal Data Converter implementation. Temporal's `Encode()` and `Decode()` steps only need to trigger as expected, and Temporal has no knowledge of how or when you are generating your encryption keys.

You should design your Encode and Decode steps to accept all the necessary parameters for your key management, such as the key version, alongside your payloads. Like the Data Converters, keys should be mapped to a Namespace in Temporal.

---

## Payload Codec

This page discusses [Payload Codec](#payload-codec).

## What is a Payload Codec? {/* #payload-codec */}

A Payload Codec transforms an array of [Payloads](/dataconversion#payload) (for example, a list of Workflow arguments) into another array of Payloads.

When serializing to Payloads, the Payload Converter is applied first to convert your objects to bytes, followed by codecs that convert bytes to bytes.
When deserializing from Payloads, codecs are applied first to last to reverse the effect, followed by the Payload Converter.

Use a custom Payload Codec to transform your Payloads; for example, implementing compression and/or encryption on your Workflow Execution data.

### Encryption {/* #encryption */}

Using end-to-end encryption in your custom Data Converter ensures that sensitive application data is secure when handled by the Temporal Server.

Apply your encryption logic in a custom Payload Codec and use it locally to encrypt data.
You maintain all the encryption keys, and the Temporal Server sees only encrypted data. Refer to [What is Key Management?](/key-management) for more guidance.

Your data exists unencrypted only on the Client and the Worker process that is executing the Workflows and Activities, on hosts that you control. For details, see [Securing your data](/production-deployment/data-encryption).

The following samples use encryption (AES GCM with 256-bit key) in a custom Data Converter:

- [Go sample](https://github.com/temporalio/samples-go/tree/main/encryption)
- [Java sample](https://github.com/temporalio/samples-java/tree/main/core/src/main/java/io/temporal/samples/encryptedpayloads)
- [Python sample](https://github.com/temporalio/samples-python/tree/main/encryption)
- [TypeScript sample](https://github.com/temporalio/samples-typescript/tree/main/encryption)

---

## Payload Converter

This page discusses [Payload Converter](#payload-converter).

## What is a Payload Converter? {/* #payload-converter */}

A Payload Converter serializes data, converting values to bytes and back.

When you initiate a Workflow Execution through a Client and pass data as input, the input is serialized using a Data Converter that runs it through a set of Payload Converters.
When your Workflow Execution starts, this data input is deserialized and passed as input to your Workflow.

### Composite Data Converters {/* #composite-data-converters */}

A Composite Data Converter is used to apply custom, type-specific Payload Converters in a specified order.
A Composite Data Converter can be comprised of custom rules that you created, and it can also leverage the default Data Converters built into Temporal.
In fact, the default Data Converter logic is implemented internally in the Temporal source as a Composite Data Converter. It defines these rules in this order:

```go
defaultDataConverter = NewCompositeDataConverter(
    NewNilPayloadConverter(),
    NewByteSlicePayloadConverter(),
    NewProtoJSONPayloadConverter(),
    NewProtoPayloadConverter(),
    NewJSONPayloadConverter(),
)
```

The order in which the Payload Converters are applied is important.
During serialization, the Data Converter tries the Payload Converters in that specific order until a Payload Converter returns a non-nil Payload.
A custom PayloadConverter must implement the functions:

- `FromPayload` (for a single value) or
- `FromPayloads` (for a list of values) to convert to values from a Payload, and
- `ToPayload` (for a single value) or
- `ToPayloads` (for a list of values) to convert values to a Payload.

Defining a new Composite Data Converter is not always necessary to implement custom data handling.
Each SDK allows you to override or configure the default Converter with a custom Payload Codec.

---

## Remote data encoding

This page discusses [Remote Data Encoding](#remote-data-encoding).

## What is remote data encoding? {/* #remote-data-encoding */}

Remote data encoding is exposing your Payload Codec via HTTP endpoints to support remote encoding and decoding.

Running your encoding remotely allows you to use it with the [Temporal CLI](/cli) to encode/decode data for several commands including `temporal workflow show` and with Temporal Web UI to decode data in your Workflow Execution details view.

To run data encoding/decoding remotely, use a [Codec Server](/codec-server). A Codec Server is an HTTP server that uses your custom Codec logic to decode your data remotely.
The Codec Server is independent of the Temporal Service and decodes your encrypted payloads through predefined endpoints.
You create, operate, and manage access to your Codec Server in your own environment.
The Temporal CLI and the Web UI in turn provide built-in hooks to call the Codec Server to decode encrypted payloads on demand.

### Encoding data on the Web UI and CLI

You can perform some operations on your Workflow Execution using the Temporal CLI and the Web UI.
For example, you can start or signal an active Workflow Execution from the Temporal CLI or cancel a Workflow Execution from the Web UI, which might require inputs that contain sensitive data.

To encode this data, specify your [Codec Server endpoints](/codec-server) with the `codec-endpoint` parameter in [the Temporal CLI](/cli) and configure your Web UI to use the Codec Server endpoints.

### Decoding data on the Web UI and CLI

If you use custom encoding, Payload data handled by the Temporal Service is stored encoded. Since the Web UI uses the [Visibility](/temporal-service/visibility) database to show events and data stored on the Temporal Server, all data in the Workflow Execution History in your Web UI is displayed in the encoded format.
