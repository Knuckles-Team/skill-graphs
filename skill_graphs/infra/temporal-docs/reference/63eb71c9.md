[ctxpropagation/starter/main.go](https://github.com/temporalio/samples-go/blob/main/ctxpropagation/starter/main.go)
```go
// The client is a heavyweight object that should be created once per process.
c, err := client.Dial(client.Options{
	HostPort:           client.DefaultHostPort,
	Interceptors:       []interceptor.ClientInterceptor{tracingInterceptor},
	ContextPropagators: []workflow.ContextPropagator{ctxpropagation.NewContextPropagator()},
})
if err != nil {
	log.Fatalln("Unable to create client", err)
}
defer c.Close()

workflowID := "ctx-propagation_" + uuid.New()
workflowOptions := client.StartWorkflowOptions{
	ID:        workflowID,
	TaskQueue: "ctx-propagation",
}

ctx := context.Background()
ctx = context.WithValue(ctx, ctxpropagation.PropagateKey, &ctxpropagation.Values{Key: "test", Value: "tested"})

we, err := c.ExecuteWorkflow(ctx, workflowOptions, ctxpropagation.CtxPropWorkflow)
```
<!--SNIPEND-->

You can also register context propagators through a [Plugin](/develop/plugins-guide) if you are building a reusable library.

## Access propagated values

In your Workflow, the propagated values are available on the `workflow.Context`. When the Workflow starts an Activity, the SDK automatically propagates the same values:

<!--SNIPSTART samples-go-ctx-propagation-workflow-->
[ctxpropagation/workflow.go](https://github.com/temporalio/samples-go/blob/main/ctxpropagation/workflow.go)
```go
// CtxPropWorkflow workflow definition
func CtxPropWorkflow(ctx workflow.Context) (err error) {
	ao := workflow.ActivityOptions{
		StartToCloseTimeout: 2 * time.Second, // such a short timeout to make sample fail over very fast
	}
	ctx = workflow.WithActivityOptions(ctx, ao)

	if val := ctx.Value(PropagateKey); val != nil {
		vals := val.(Values)
		workflow.GetLogger(ctx).Info("custom context propagated to workflow", vals.Key, vals.Value)
	}

	var values Values
	if err = workflow.ExecuteActivity(ctx, SampleActivity).Get(ctx, &values); err != nil {
		workflow.GetLogger(ctx).Error("Workflow failed.", "Error", err)
		return err
	}
	workflow.GetLogger(ctx).Info("context propagated to activity", values.Key, values.Value)
	workflow.GetLogger(ctx).Info("Workflow completed.")
	return nil
}
```
<!--SNIPEND-->

<!--SNIPSTART samples-go-ctx-propagation-activity-->
[ctxpropagation/activities.go](https://github.com/temporalio/samples-go/blob/main/ctxpropagation/activities.go)
```go
func SampleActivity(ctx context.Context) (*Values, error) {
	if val := ctx.Value(PropagateKey); val != nil {
		vals := val.(Values)
		return &vals, nil
	}
	return nil, nil
}
```
<!--SNIPEND-->

You can configure multiple context propagators on a single Client, each responsible for its own set of keys.

## Context propagation over Nexus

Nexus does not use the `ContextPropagator` interface. It relies on a Temporal-agnostic protocol with its own header format (`nexus.Header`, a wrapper around `map[string]string`).

To propagate context over Nexus Operation calls, use interceptors to explicitly serialize and deserialize context into the Nexus header. See the [Nexus Context Propagation sample](https://github.com/temporalio/samples-go/tree/main/nexus-context-propagation).

## Further reading

- [Passing Context with Temporal](https://spiralscout.com/blog/passing-context-with-temporal) - A conceptual guide to middleware and walkthrough of building a context propagator in Go

---

## Payload conversion - Go SDK

Temporal SDKs provide a default [Payload Converter](/payload-converter) that can be customized to convert a custom data type to [Payload](/dataconversion#payload) and back.

The order in which your encoding Payload Converters are applied depend on the order given to the Data Converter.
You can set multiple encoding Payload Converters to run your conversions.
When the Data Converter receives a value for conversion, it passes through each Payload Converter in sequence until the converter that handles the data type does the conversion.

Payload Converters can be customized independently of a Payload Codec.
Temporal's Converter architecture looks like this:

<CaptionedImage
    src="/img/info/converter-architecture.png"
    title="Temporal converter architecture"
/>

## Use a custom Payload Converter {/* #custom-payload-converter */}

Use a [Composite Data Converter](https://pkg.go.dev/go.temporal.io/sdk/converter#CompositeDataConverter) to apply custom, type-specific Payload Converters in a specified order.
Defining a new Composite Data Converter is not always necessary to implement custom data handling.
You can override the default Converter with a custom Codec, but a Composite Data Converter may be necessary for complex Workflow logic.

`NewCompositeDataConverter` creates a new instance of `CompositeDataConverter` from an ordered list of type-specific Payload Converters.
The following type-specific Payload Converters are available in the Go SDK, listed in the order that they are applied by the default Data Converter:

- [NewNilPayloadConverter()](https://pkg.go.dev/go.temporal.io/sdk/converter#NilPayloadConverter.ToString)
- [NewByteSlicePayloadConverter()](https://pkg.go.dev/go.temporal.io/sdk/converter#ByteSlicePayloadConverter)
- [NewProtoJSONPayloadConverter()](https://pkg.go.dev/go.temporal.io/sdk/converter#ProtoJSONPayloadConverter)
- [NewProtoPayloadConverter()](https://pkg.go.dev/go.temporal.io/sdk/converter#ProtoPayloadConverter)
- [NewJSONPayloadConverter()](https://pkg.go.dev/go.temporal.io/sdk/converter#JSONPayloadConverter)

The order in which the Payload Converters are applied is important because during serialization the Data Converter tries the Payload Converters in that specific order until a Payload Converter returns a non-nil Payload.

To set your custom Payload Converter, use [`NewCompositeDataConverter`](https://pkg.go.dev/go.temporal.io/sdk/converter#NewCompositeDataConverter) and set it as the Data Converter in the Client options.

- To replace the default Data Converter with a custom `NewCompositeDataConverter`, use the following.

  ```go
  dataConverter := converter.NewCompositeDataConverter(YourCustomPayloadConverter())
  ```

- To add your custom type conversion to the default Data Converter, use the following to keep the defaults but set yours just before the default JSON fall through.

  ```go
  dataConverter := converter.NewCompositeDataConverter(
    converter.NewNilPayloadConverter(),
    converter.NewByteSlicePayloadConverter(),
    converter.NewProtoJSONPayloadConverter(),
    converter.NewProtoPayloadConverter(),
    YourCustomPayloadConverter(),
    converter.NewJSONPayloadConverter(),
  )
  ```

---

## Payload encryption - Go SDK

Temporal's security model is designed around client-side encryption of Payloads.
A client may encrypt Payloads before sending them to the server, and decrypt them after receiving them from the server.
This provides a high degree of confidentiality because the Temporal Server itself has absolutely no knowledge of the actual data.
It also gives implementers more power and more freedom regarding which client is able to read which data. Implementers can control access with keys, algorithms, or other security measures.

A Temporal developer adds client-side encryption of Payloads by providing a Custom Payload Codec to its Client.
Depending on business needs, a complete implementation of Payload Encryption may involve selecting appropriate encryption algorithms, managing encryption keys, restricting a subset of their users from viewing payload output, or a combination of these.

The server itself never adds encryption over Payloads.
Therefore, unless client-side encryption is implemented, Payload data will be persisted in non-encrypted form to the data store, and any Client that can make requests to a Temporal namespace (including the Temporal UI and CLI) will be able to read Payloads contained in Workflows.
When working with sensitive data, you should always implement Payload encryption.

## Use a custom Payload Codec {/* #custom-payload-codec */}

**Step 1: Create a custom Payload Codec**

Create a custom [PayloadCodec](https://pkg.go.dev/go.temporal.io/sdk/converter#PayloadCodec) implementation and define your encryption/compression and decryption/decompression logic in the `Encode` and `Decode` functions.

The Payload Codec converts bytes to bytes.
It must be used in an instance of [CodecDataConverter](https://pkg.go.dev/go.temporal.io/sdk/converter#CodecDataConverter) that wraps a Data Converter to do the [Payload](/dataconversion#payload) conversions, and applies the custom encoding and decoding in `PayloadCodec` to the converted Payloads.

The following example from the [Data Converter sample](https://github.com/temporalio/samples-go/blob/main/codec-server/data_converter.go) shows how to create a custom `NewCodecDataConverter` that wraps an instance of a Data Converter with a custom `PayloadCodec`.

```go
// Create an instance of Data Converter with your codec.
var DataConverter = converter.NewCodecDataConverter(
	converter.GetDefaultDataConverter(),
	NewPayloadCodec(),
)
//...
// Create an instance of PayloadCodec.
func NewPayloadCodec() converter.PayloadCodec {
	return &Codec{}
}
```

Implement your encryption/compression logic in the `Encode` function and the decryption/decompression logic in the `Decode` function in your custom `PayloadCodec`, as shown in the following example.

```go
// Codec implements converter.PayloadEncoder for snappy compression.
type Codec struct{}

// Encode implements converter.PayloadCodec.Encode.
func (Codec) Encode(payloads []*commonpb.Payload) ([]*commonpb.Payload, error) {
	result := make([]*commonpb.Payload, len(payloads))
	for i, p := range payloads {
		// Marshal proto
		origBytes, err := p.Marshal()
		if err != nil {
			return payloads, err
		}
		// Compress
		b := snappy.Encode(nil, origBytes)
		result[i] = &commonpb.Payload{
			Metadata: map[string][]byte{converter.MetadataEncoding: []byte("binary/snappy")},
			Data:     b,
		}
	}

	return result, nil
}

// Decode implements converter.PayloadCodec.Decode.
func (Codec) Decode(payloads []*commonpb.Payload) ([]*commonpb.Payload, error) {
	result := make([]*commonpb.Payload, len(payloads))
	for i, p := range payloads {
		// Decode only if it's our encoding
		if string(p.Metadata[converter.MetadataEncoding]) != "binary/snappy" {
			result[i] = p
			continue
		}
		// Uncompress
		b, err := snappy.Decode(nil, p.Data)
		if err != nil {
			return payloads, err
		}
		// Unmarshal proto
		result[i] = &commonpb.Payload{}
		err = result[i].Unmarshal(b)
		if err != nil {
			return payloads, err
		}
	}

	return result, nil
}
```

**Step 2: Set Data Converter to use custom Payload Codec.**

Set your custom `PayloadCodec` with an instance of `DataConverter` in your `Dial` client options that you use to create the client.

The following example shows how to set your custom Data Converter from a package called `mycodecpackage`.

```go
//...
c, err := client.Dial(client.Options{
		// Set DataConverter here to ensure that Workflow inputs and results are
		// encoded as required.
		DataConverter: mycodecpackage.DataConverter,
	})
//...
```

- Data **encoding** is performed by the client using the converters and codecs provided by Temporal or your custom implementation when passing input to the Temporal Cluster. For example, plain text input is usually serialized into a JSON object, and can then be compressed or encrypted.
- Data **decoding** may be performed by your application logic during your Workflows or Activities as necessary, but decoded Workflow results are never persisted back to the Temporal Cluster. Instead, they are stored encoded on the Cluster, and you need to provide an additional parameter when using the [temporal workflow show](/cli/command-reference/workflow#show) command or when browsing the Web UI to view output.

For reference, see the [Encryption](https://github.com/temporalio/samples-go/tree/main/encryption) sample.

### Using a Codec Server

A Codec Server is an HTTP server that uses your custom Codec logic to decode your data remotely.
The Codec Server is independent of the Temporal Cluster and decodes your encrypted payloads through predefined endpoints.
You create, operate, and manage access to your Codec Server in your own environment.
The Temporal CLI and the Web UI in turn provide built-in hooks to call the Codec Server to decode encrypted payloads on demand.
Refer to the [Codec Server](/production-deployment/data-encryption) documentation for information on how to design and deploy a Codec Server.

For reference, see the [Codec server](https://github.com/temporalio/samples-go/tree/main/codec-server) sample.

---

## External Storage - Go SDK

:::info Release, stability, and dependency info

External Storage is in [Public Preview](/evaluate/development-production-features/release-stages#public-preview). APIs and
configuration may change before General Availability. Join the
[#large-payloads Slack channel](https://temporalio.slack.com/archives/C09VA2DE15Y) to provide feedback or ask for help.

:::

The Temporal Service enforces a 2 MB per-payload limit by default. This limit is configurable on self-hosted
deployments. When your Workflows or Activities handle data larger than the limit, you can offload payloads to external
storage, such as Amazon S3, and pass a small reference token through the Event History instead. This page shows you how
to set up External Storage with Amazon S3 and how to implement a custom storage driver.

For a conceptual overview of External Storage and its use cases, see [External Storage](/external-storage).

## Store and retrieve large payloads with Amazon S3

The Go SDK includes an S3 storage driver. Follow these steps to set it up:

### Prerequisites

- An Amazon S3 bucket that you have read and write access to. Refer to [lifecycle management](/external-storage#lifecycle)
  to ensure that your payloads remain available for the entire lifetime of the Workflow. For multi-region durability, see
  [Durable External Storage](/external-storage#durable-external-storage).
- Install the S3 driver module and its dependencies: `go get go.temporal.io/sdk/contrib/aws/s3driver go.temporal.io/sdk/contrib/aws/s3driver/awssdkv2 github.com/aws/aws-sdk-go-v2/config github.com/aws/aws-sdk-go-v2/service/s3`

### Procedure

1. Load your AWS configuration and create the S3 storage driver. The driver uses your standard [AWS credentials](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/configure-gosdk.html) from the environment (environment variables, IAM role, or AWS config file):

   <!--SNIPSTART go-s3-driver-create-->
[features/snippets/external_storage/s3_setup/s3_driver_create.go](https://github.com/temporalio/features/blob/main/features/snippets/external_storage/s3_setup/s3_driver_create.go)
```go
cfg, err := config.LoadDefaultConfig(context.Background(),
	config.WithRegion("us-east-2"),
)
if err != nil {
	log.Fatalf("load AWS config: %v", err)
}

driver, err := s3driver.NewDriver(s3driver.Options{
	Client: awssdkv2.NewClient(s3.NewFromConfig(cfg)),
	Bucket: s3driver.StaticBucket("my-temporal-payloads"),
})
if err != nil {
	log.Fatalf("create S3 driver: %v", err)
}
```
   <!--SNIPEND-->

2. Configure the driver on `ExternalStorage` and pass it in your Client options:

   <!--SNIPSTART go-s3-external-storage-setup-->
[features/snippets/external_storage/s3_setup/s3_external_storage_setup.go](https://github.com/temporalio/features/blob/main/features/snippets/external_storage/s3_setup/s3_external_storage_setup.go)
```go
c, err := client.Dial(client.Options{
	HostPort: "localhost:7233",
	ExternalStorage: converter.ExternalStorage{
		Drivers: []converter.StorageDriver{driver},
	},
})
if err != nil {
	log.Fatalf("connect to Temporal: %v", err)
}
defer c.Close()

w := worker.New(c, "my-task-queue", worker.Options{})
```
   <!--SNIPEND-->

   By default, payloads larger than 256 KiB are offloaded to external storage. You can adjust this with the
   `PayloadSizeThreshold` option, even setting it to 1 to externalize all payloads regardless of size. Refer to
   [Configure payload size threshold](#configure-payload-size-threshold) for more information.

   All Workflows and Activities running on the Worker use the storage driver automatically without changes to your
   business logic. The driver uploads and downloads payloads concurrently and validates payload integrity on retrieve.

   The S3 driver includes diagnostic metadata, such as the AWS region, in error messages to help troubleshoot storage failures.

## Implement a custom storage driver

If you need a storage backend other than what the built-in drivers allow, you can implement your own storage driver.
Refer to [Choose a storage system](/external-storage#choose-storage) for guidance on selecting a backing store and [Lifecycle management](/external-storage#lifecycle) for retention requirements.

The following example shows a custom driver that uses local disk as the backing store. This example is for local
development and testing only. In production, use a durable storage system that is accessible to all Workers:

<!--SNIPSTART go-custom-storage-driver-->
[features/snippets/external_storage/custom_driver/custom_storage_driver.go](https://github.com/temporalio/features/blob/main/features/snippets/external_storage/custom_driver/custom_storage_driver.go)
```go
type LocalDiskStorageDriver struct {
	storeDir string
}

func NewLocalDiskStorageDriver(storeDir string) converter.StorageDriver {
	return &LocalDiskStorageDriver{storeDir: storeDir}
}

func (d *LocalDiskStorageDriver) Name() string {
	return "my-local-disk"
}

func (d *LocalDiskStorageDriver) Type() string {
	return "local-disk"
}

func (d *LocalDiskStorageDriver) Store(
	ctx converter.StorageDriverStoreContext,
	payloads []*commonpb.Payload,
) ([]converter.StorageDriverClaim, error) {
	dir := d.storeDir
	switch info := ctx.Target.(type) {
	case converter.StorageDriverWorkflowInfo:
		if info.WorkflowID != "" {
			dir = filepath.Join(d.storeDir, info.Namespace, info.WorkflowID)
		}
	case converter.StorageDriverActivityInfo:
		// StorageDriverActivityInfo is only used for standalone (non-workflow-bound)
		// activities. Activities started by a workflow use StorageDriverWorkflowInfo.
		if info.ActivityID != "" {
			dir = filepath.Join(d.storeDir, info.Namespace, info.ActivityID)
		}
	}
	if err := os.MkdirAll(dir, 0o755); err != nil {
		return nil, fmt.Errorf("create store directory: %w", err)
	}

	claims := make([]converter.StorageDriverClaim, len(payloads))
	for i, payload := range payloads {
		key := uuid.NewString() + ".bin"
		filePath := filepath.Join(dir, key)

		data, err := proto.Marshal(payload)
		if err != nil {
			return nil, fmt.Errorf("marshal payload: %w", err)
		}
		if err := os.WriteFile(filePath, data, 0o644); err != nil {
			return nil, fmt.Errorf("write payload: %w", err)
		}

		claims[i] = converter.StorageDriverClaim{
			ClaimData: map[string]string{"path": filePath},
		}
	}
	return claims, nil
}

func (d *LocalDiskStorageDriver) Retrieve(
	ctx converter.StorageDriverRetrieveContext,
	claims []converter.StorageDriverClaim,
) ([]*commonpb.Payload, error) {
	payloads := make([]*commonpb.Payload, len(claims))
	for i, claim := range claims {
		filePath := claim.ClaimData["path"]
		data, err := os.ReadFile(filePath)
		if err != nil {
			return nil, fmt.Errorf("read payload: %w", err)
		}
		payload := &commonpb.Payload{}
		if err := proto.Unmarshal(data, payload); err != nil {
			return nil, fmt.Errorf("unmarshal payload: %w", err)
		}
		payloads[i] = payload
	}
	return payloads, nil
}
```
<!--SNIPEND-->

The following sections walk through the key parts of the driver implementation.

### 1. Implement the StorageDriver interface

A custom driver implements the `converter.StorageDriver` interface with four methods:

- `Name()` returns a unique string that identifies the driver instance. The SDK stores this name in the claim check
  reference so it can route retrieval requests to the correct driver. Changing the name after payloads have been stored
  breaks retrieval. For example, two S3 drivers could be named `"s3-primary"` and `"s3-archive"`.
- `Type()` returns a string that identifies the driver implementation. Unlike `Name()`, this must be the same across all
  instances of the same driver type regardless of configuration. Two S3 drivers named `"s3-primary"` and `"s3-archive"` would both return
  `"aws.s3driver"` as their type, while the local disk driver in the custom driver code sample returns `"local-disk"`.
- `Store()` receives a slice of payloads and returns one `StorageDriverClaim` per payload. A claim is a set of string
  key-value pairs that the driver uses to locate the payload later.
- `Retrieve()` receives the claims that `Store()` produced and returns the original payloads.

### 2. Store payloads

In `Store()`, marshal each Payload protobuf message to bytes with `proto.Marshal(payload)` and write the bytes to
your storage system. The application data has already been serialized by the [Payload Converter](/develop/go/data-handling/data-conversion)
and [Payload Codec](/develop/go/data-handling/data-encryption) before it reaches the driver.
See the [data conversion pipeline](/external-storage#data-pipeline) for more details.

Return a `StorageDriverClaim` for each payload with enough information to retrieve it later. The `ctx.Target`
provides identity information (namespace, Workflow ID) depending on the operation. Use a type switch on
`StorageDriverWorkflowInfo` and `StorageDriverActivityInfo` to access the concrete values. Consider structuring
your storage keys to include this information so that you can identify which Workflow owns each payload.

### 3. Retrieve payloads

In `Retrieve()`, download the bytes using the claim data, then reconstruct the Payload protobuf message with
`proto.Unmarshal(data, payload)`. The Payload Converter handles deserializing the application data after the driver
returns the payload.

### 4. Configure the Client

Pass an `ExternalStorage` struct with your driver in the Client options:

```go
c, err := client.Dial(client.Options{
    ExternalStorage: converter.ExternalStorage{
        Drivers: []converter.StorageDriver{NewLocalDiskStorageDriver("/tmp/temporal-payload-store")},
    },
})
```

You can also package your driver as a [plugin](/develop/plugins-guide) for easier reuse across services.

## Configure payload size threshold

You can configure the payload size threshold that triggers external storage. By default, payloads larger than 256 KiB
are offloaded to external storage. You can adjust this with the `PayloadSizeThreshold` option, or set it to 1 to
externalize all payloads regardless of size. A value of 0 is interpreted as the default (256 KiB).

<!--SNIPSTART go-external-storage-threshold-->
[features/snippets/external_storage/threshold/threshold_config.go](https://github.com/temporalio/features/blob/main/features/snippets/external_storage/threshold/threshold_config.go)
```go
c, err := client.Dial(client.Options{
	ExternalStorage: converter.ExternalStorage{
		Drivers:              []converter.StorageDriver{driver},
		PayloadSizeThreshold: 1,
	},
})
```
<!--SNIPEND-->

## Use multiple storage drivers

When you register multiple drivers, you must provide a `DriverSelector` that implements the `StorageDriverSelector`
interface. The selector chooses which driver stores each payload. Any driver in the list that is not selected for storing is still
available for retrieval, which is useful when migrating between storage backends. Return `nil` from the selector to
keep a specific payload inline in Event History.

Multiple drivers are useful in scenarios such as:

- Driver migration. Your Worker needs to retrieve payloads created by clients that use a different driver than the
  one you prefer. Register both drivers and use the selector to always pick your preferred driver for new payloads.
  The old driver remains available for retrieving existing claims.
- Multi-cloud storage. Route payloads to different storage backends based on your cloud environment. For
  example, use S3 for Workers running on AWS and GCS for Workers running on Google Cloud. The selector chooses the
  appropriate driver based on the runtime environment.

The following example registers two drivers but always selects `preferredDriver` for new payloads. The `legacyDriver`
is only registered so the Worker can retrieve payloads that were previously stored with it:

<!--SNIPSTART go-external-storage-multiple-drivers-->
[features/snippets/external_storage/multiple_drivers/multiple_drivers.go](https://github.com/temporalio/features/blob/main/features/snippets/external_storage/multiple_drivers/multiple_drivers.go)
```go
type PreferredSelector struct {
	preferred converter.StorageDriver
}

func (s *PreferredSelector) SelectDriver(
	ctx converter.StorageDriverStoreContext,
	payload *commonpb.Payload,
) (converter.StorageDriver, error) {
	return s.preferred, nil
}

func MultipleDriversSetup(preferredDriver, legacyDriver converter.StorageDriver) converter.ExternalStorage {
	return converter.ExternalStorage{
		Drivers:        []converter.StorageDriver{preferredDriver, legacyDriver},
		DriverSelector: &PreferredSelector{preferred: preferredDriver},
	}
}
```
<!--SNIPEND-->

## Multi-region durability

To make your S3-backed External Storage tolerant of regional failures, configure the AWS side with
[Cross-Region Replication (CRR)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html) and an
[S3 Multi-Region Access Point (MRAP)](https://aws.amazon.com/s3/features/multi-region-access-points/), then point the
