
#### Using the Go SDK

If you're developing in Go, we recommend using the [Go SDK](https://github.com/temporalio/cloud-sdk-go) which provides pre-compiled Go bindings and a more idiomatic interface. The Go SDK handles all the protobuf compilation and provides ready-to-use Go types and client interfaces. You can also use the [Go samples](https://github.com/temporalio/cloud-samples-go) to help you get started with the Cloud Ops API using the Go SDK.

To start using the Go SDK with the Cloud Ops API, follow these steps:

1. Install the Go SDK:
   ```go
   go get github.com/temporalio/cloud-sdk-go
   ```

2. Import and use the SDK:
   ```go

       "github.com/temporalio/cloud-sdk-go/client"
   )
   ```

3. The Go SDK provides pre-built client interfaces that handle authentication and connection setup. Refer to the [Go samples](https://github.com/temporalio/cloud-samples-go) for detailed usage examples.

The Go SDK eliminates the need to work directly with generated protobuf files and provides a more idiomatic Go experience.

#### Compile the API and use the generated code (For other languages)

For programming languages other than Go, download the gRPC protobufs from the [Cloud Ops API repository](https://github.com/temporalio/cloud-api/tree/main/temporal/api/cloud) and compile them manually.

Use [gRPC](https://grpc.io/docs/) to compile and generate code in your preferred [programming language](https://grpc.io/docs/#official-support). The steps below use Python as an example and require [Python's gRPC tools](https://grpc.io/docs/languages/python/quickstart/#grpc-tools) to be installed, but the approach can be adapted for other supported programming languages.

1. Clone the Temporal Cloud API repository:

   ```command
   git clone https://github.com/temporalio/cloud-api.git
   cd cloud-api
   ```

2. Copy Protobuf files:

   - Navigate to the `temporal` directory.
   - Copy the protobuf files to your project directory.

3. Compile the Protobuf files:

   ```python
   python -m grpc_tools.protoc -I./ --python_out=./ --grpc_python_out=./ *.proto
   ```
   - `-I` specifies the directory of the `.proto` files.
   - `--python_out=` sets the output directory for generated Python classes.
   - `--grpc_python_out=` sets the output directory for generated gRPC service classes.
   - `*.proto` processes all `.proto` files.

   After compiling the Protobuf files, you will have generated code files in your project directory.
   These files enable interaction with the Temporal Cloud API in your chosen programming language.

4. Import the Generated Files:

   - Locate the Python files (.py) generated in your project directory.
   - Import these files into your Python application where you intend to interact with the Temporal Cloud API.

2. Use the API:
   - Use the classes and methods defined in the imported files to communicate with the Temporal Cloud services.
   - Ensure to handle any required authentication or configuration as needed for Temporal Cloud.

This approach can be adapted for other programming languages by following their respective import and usage conventions for the generated code files.

## Usage guidelines

When interacting with the Temporal Cloud Ops API, follow these guidelines:

- API version header:
   - Always include the `temporal-cloud-api-version` header in your requests, specifying the API version identifier.
   - The current API version can be found [here](https://github.com/temporalio/cloud-api/blob/main/VERSION#L1C1-L1C14).
- Connection URL:
   - Connect to the Temporal Cloud using the gRPC URL: `saas-api.tmprl.cloud:443`.
- Engagement steps:
   - Generate API key:
     - Obtain an [API Key for authentication](/cloud/api-keys#manage-api-keys). Note that many operations may require Admin privileges.
   - Set up client:
     - Establish a secure connection to the Temporal Cloud. Refer to the example [Client setup in Go](https://github.com/temporalio/cloud-samples-go/blob/main/client/temporal/client.go) for guidance.
   - Execute operations:
     - For operation specifics, refer to the `cloudservice/v1/request_response.proto` for gRPC messages and `cloudservice/v1/service.proto` for gRPC services.

These steps provide a structured approach to using the Temporal Cloud Ops API effectively, ensuring proper authentication and connection setup.

## Rate limits

The Temporal Cloud Operations API implements rate limiting to ensure system stability and fair usage across all users. Rate limits are applied based on identity type, with different limits for users and service accounts.

### Account-level rate limit

**Total rate limit: 160 requests per second (RPS)**

This limit applies to all requests made to the Temporal Cloud Control Plane by any client (tcld, UI, Cloud Ops API) or identity type (user, service account) within your account. The total account throughput cannot exceed the limit regardless of the number of users or service accounts making requests.

### Per-identity rate limits

**User rate limit: 40 RPS per user**

This limit applies to all requests made by each user through any client (tcld, UI, Cloud Ops API), regardless of the authentication method used (SSO or API keys).

**Service account rate limit: 80 RPS per service account**

This limit applies to all requests made by each service account through any client (tcld, Cloud Ops API).

**Asynchronous Operations: 10 concurrent operations at a time**

This limits the number of concurrent asynchronous operations that can be in-flight at any given time.

### Important considerations

- Rate limits are enforced across all Temporal Cloud Control Plane operations
- Multiple clients used by the same identity (user or service account) share the same rate limit
- Authentication method (SSO, API keys) does not affect rate limiting
- These limits help ensure system stability and prevent any single account or identity from overwhelming the service

### Request limit increases

If your use case requires higher rate limits, you can request an increase by [submitting a support ticket](/cloud/support#support-ticket). When requesting a limit increase, please provide:

- Your current usage patterns and requirements
- The specific limits you need increased
- A description of your use case and why higher limits are necessary

### Provide feedback

Your input is valuable!

You can provide feedback through the following channels:

- Submit request or feedback through a [support ticket](/cloud/support#support-ticket)
- Open an issue in the [GitHub Repo](https://github.com/temporalio/cloud-api)

---

## Awsregions

### Asia Pacific - Tokyo (`ap-northeast-1`)

- **Cloud API Code**: `aws-ap-northeast-1`
- **Regional Endpoint**: `aws-ap-northeast-1.region.tmprl.cloud`
- **PrivateLink Endpoint Service**: `com.amazonaws.vpce.ap-northeast-1.vpce-svc-08f34c33f9fb8a48a`
- **Same Region Replication**:  Not Available
- **Multi-Region Replication**:
  - `aws-ap-northeast-2`
  - `aws-ap-south-1`
  - `aws-ap-south-2`
  - `aws-ap-southeast-1`
  - `aws-ap-southeast-2`
- **Multi-Cloud Replication**:
  - `gcp-asia-south1`

### Asia Pacific - Seoul (`ap-northeast-2`)

- **Cloud API Code**: `aws-ap-northeast-2`
- **Regional Endpoint**: `aws-ap-northeast-2.region.tmprl.cloud`
- **PrivateLink Endpoint Service**: `com.amazonaws.vpce.ap-northeast-2.vpce-svc-08c4d5445a5aad308`
- **Same Region Replication**:  Not Available
- **Multi-Region Replication**:
  - `aws-ap-northeast-1`
  - `aws-ap-south-1`
  - `aws-ap-south-2`
  - `aws-ap-southeast-1`
  - `aws-ap-southeast-2`
- **Multi-Cloud Replication**:
  - `gcp-asia-south1`

### Asia Pacific - Mumbai (`ap-south-1`)

- **Cloud API Code**: `aws-ap-south-1`
- **Regional Endpoint**: `aws-ap-south-1.region.tmprl.cloud`
- **PrivateLink Endpoint Service**: `com.amazonaws.vpce.ap-south-1.vpce-svc-0ad4f8ed56db15662`
- **Same Region Replication**:  Not Available
- **Multi-Region Replication**:
  - `aws-ap-northeast-1`
  - `aws-ap-northeast-2`
  - `aws-ap-south-2`
  - `aws-ap-southeast-1`
  - `aws-ap-southeast-2`
- **Multi-Cloud Replication**:
  - `gcp-asia-south1`

### Asia Pacific - Hyderabad (`ap-south-2`)

- **Cloud API Code**: `aws-ap-south-2`
- **Regional Endpoint**: `aws-ap-south-2.region.tmprl.cloud`
- **PrivateLink Endpoint Service**: `com.amazonaws.vpce.ap-south-2.vpce-svc-08bcf602b646c69c1`
- **Same Region Replication**:  Not Available
- **Multi-Region Replication**:
  - `aws-ap-northeast-1`
  - `aws-ap-northeast-2`
  - `aws-ap-south-1`
  - `aws-ap-southeast-1`
  - `aws-ap-southeast-2`
- **Multi-Cloud Replication**:
  - `gcp-asia-south1`

### Asia Pacific - Singapore (`ap-southeast-1`)

- **Cloud API Code**: `aws-ap-southeast-1`
- **Regional Endpoint**: `aws-ap-southeast-1.region.tmprl.cloud`
- **PrivateLink Endpoint Service**: `com.amazonaws.vpce.ap-southeast-1.vpce-svc-05c24096fa89b0ccd`
- **Same Region Replication**:  Not Available
- **Multi-Region Replication**:
  - `aws-ap-northeast-1`
  - `aws-ap-northeast-2`
  - `aws-ap-south-1`
  - `aws-ap-south-2`
  - `aws-ap-southeast-2`
- **Multi-Cloud Replication**:
  - `gcp-asia-south1`

### Asia Pacific - Sydney (`ap-southeast-2`)

- **Cloud API Code**: `aws-ap-southeast-2`
- **Regional Endpoint**: `aws-ap-southeast-2.region.tmprl.cloud`
- **PrivateLink Endpoint Service**: `com.amazonaws.vpce.ap-southeast-2.vpce-svc-0634f9628e3c15b08`
- **Same Region Replication**: Available
- **Multi-Region Replication**:
  - `aws-ap-northeast-1`
  - `aws-ap-northeast-2`
  - `aws-ap-south-1`
  - `aws-ap-south-2`
  - `aws-ap-southeast-1`
- **Multi-Cloud Replication**:
  - `gcp-asia-south1`

### Europe - Frankfurt (`eu-central-1`)

- **Cloud API Code**: `aws-eu-central-1`
- **Regional Endpoint**: `aws-eu-central-1.region.tmprl.cloud`
- **PrivateLink Endpoint Service**: `com.amazonaws.vpce.eu-central-1.vpce-svc-073a419b36663a0f3`
- **Same Region Replication**:  Not Available
- **Multi-Region Replication**:
  - `aws-eu-west-1`
  - `aws-eu-west-2`
- **Multi-Cloud Replication**:
  - `gcp-europe-west3`

### Europe - Ireland (`eu-west-1`)

- **Cloud API Code**: `aws-eu-west-1`
- **Regional Endpoint**: `aws-eu-west-1.region.tmprl.cloud`
- **PrivateLink Endpoint Service**: `com.amazonaws.vpce.eu-west-1.vpce-svc-04388e89f3479b739`
- **Same Region Replication**:  Not Available
- **Multi-Region Replication**:
  - `aws-eu-central-1`
  - `aws-eu-west-2`
- **Multi-Cloud Replication**:
  - `gcp-europe-west3`

### Europe - London (`eu-west-2`)

- **Cloud API Code**: `aws-eu-west-2`
- **Regional Endpoint**: `aws-eu-west-2.region.tmprl.cloud`
- **PrivateLink Endpoint Service**: `com.amazonaws.vpce.eu-west-2.vpce-svc-0ac7f9f07e7fb5695`
- **Same Region Replication**:  Not Available
- **Multi-Region Replication**:
  - `aws-eu-central-1`
  - `aws-eu-west-1`
- **Multi-Cloud Replication**:
  - `gcp-europe-west3`

### North America - Central Canada (`ca-central-1`)

- **Cloud API Code**: `aws-ca-central-1`
- **PrivateLink Endpoint Service**: `com.amazonaws.vpce.ca-central-1.vpce-svc-080a781925d0b1d9d`
- **Regional Endpoint**: `aws-ca-central-1.region.tmprl.cloud`
- **Same Region Replication**:  Not Available
- **Multi-Region Replication**:
  - `aws-us-east-1`
  - `aws-us-east-2`
  - `aws-us-west-2`
- **Multi-Cloud Replication**:
  - `gcp-us-central1`
  - `gcp-us-west1`
  - `gcp-us-east4`

### North America - Northern Virginia (`us-east-1`)

- **Cloud API Code**: `aws-us-east-1`
- **Regional Endpoint**: `aws-us-east-1.region.tmprl.cloud`
- **PrivateLink Endpoint Service**: `com.amazonaws.vpce.us-east-1.vpce-svc-0822256b6575ea37f`
- **Same Region Replication**:  Available
- **Multi-Region Replication**:
  - `aws-ca-central-1`
  - `aws-us-east-2`
  - `aws-us-west-2`
- **Multi-Cloud Replication**:
  - `gcp-us-central1`
  - `gcp-us-west1`
  - `gcp-us-east4`

### North America - Ohio (`us-east-2`)

- **Cloud API Code**: `aws-us-east-2`
- **Regional Endpoint**: `aws-us-east-2.region.tmprl.cloud`
- **PrivateLink Endpoint Service**: `com.amazonaws.vpce.us-east-2.vpce-svc-01b8dccfc6660d9d4`
- **Same Region Replication**:  Not Available
- **Multi-Region Replication**:
  - `aws-ca-central-1`
  - `aws-us-east-1`
  - `aws-us-west-2`
- **Multi-Cloud Replication**:
  - `gcp-us-central1`
  - `gcp-us-west1`
  - `gcp-us-east4`

### North America - Oregon (`us-west-2`)

- **Cloud API Code**: `aws-us-west-2`
- **Regional Endpoint**: `aws-us-west-2.region.tmprl.cloud`
- **PrivateLink Endpoint Service**: `com.amazonaws.vpce.us-west-2.vpce-svc-0f44b3d7302816b94`
- **Same Region Replication**:  Available
- **Multi-Region Replication**:
  - `aws-ca-central-1`
  - `aws-us-east-1`
  - `aws-us-east-2`
- **Multi-Cloud Replication**:
  - `gcp-us-central1`
  - `gcp-us-west1`
  - `gcp-us-east4`

### South America - São Paulo (`sa-east-1`)

- **Cloud API Code**: `aws-sa-east-1`
- **Regional Endpoint**: `aws-sa-east-1.region.tmprl.cloud`
- **PrivateLink Endpoint Service**: `com.amazonaws.vpce.sa-east-1.vpce-svc-0ca67a102f3ce525a`
- **Same Region Replication**:  Not Available
- **Multi-Region Replication**:
  - None
- **Multi-Cloud Replication**:
  - None

---

## Outages and Recovery Objectives (RTO / RPO)

When a cloud outage disrupts a Namespace, Temporal Cloud takes measures to maintain the Namespace's availability and
data durability. The time it takes to recover from the outage is called the _recovery time_. The _recovery point_ is how
far back in time data must be recovered from after an outage. A durable system should have a low recovery time and a
near recovery point.

Temporal Cloud publishes goals for the recovery time and recovery point for each kind of outage. These goals are called
the Recovery Time Objective (RTO) and Recovery Point Objective (RPO). For details on how each is measured, see
[How RTO and RPO are measured](#how-rto-and-rpo-are-measured). These objectives are complementary to Temporal Cloud's
[Service Level Agreement (SLA)](/cloud/sla).

The RTO and RPO for a Namespace depend on the type of outage and which [High Availability](/cloud/high-availability)
features the Namespace has enabled.

## RTO and RPO summary

The following table summarizes the RTO and RPO targets for each type of outage. These targets apply to Namespaces that
have automatic failovers enabled, which is the default. Automatic failovers are triggered by
Temporal's tooling and on-call engineers without user action. Users can always initiate a failover independently. In an
outage, a user-initiated failover will not cancel out or reverse an automatic failover.

These targets are for unplanned cloud outages and do not apply to user-initiated failovers during healthy periods, such
as DR drills. Read about [triggering a failover](/cloud/high-availability/failovers/manage#trigger-failover) to see how a Namespace failover
performs during healthy periods.

| Outage type                                           | Applicable Namespaces                                                 | RPO            | RTO              |
| ----------------------------------------------------- | --------------------------------------------------------------------- | -------------- | ---------------- |
| [Availability Zone outage](#availability-zone-outage) | All Namespaces                                                        | Zero           | Near-zero        |
| [Cell outage](#cell-outage)                           | Namespaces with Same-region, Multi-region, or Multi-cloud Replication | Under 1 minute | Under 20 minutes |
| [Cloud Region outage](#cloud-region-outage)           | Namespaces with Multi-region or Multi-cloud Replication               | Under 1 minute | Under 20 minutes |
| [Cloud-wide outage](#cloud-wide-outage)               | Namespaces with Multi-cloud Replication                               | Under 1 minute | Under 20 minutes |

:::tip

Temporal highly recommends keeping automatic failovers enabled. When automatic failovers are
_disabled,_ Temporal Cloud cannot set an RPO and RTO for that Namespace, because it cannot control when or if the user
will trigger a failover.

:::

As soon as a cloud outage resolves, Temporal's on-call engineers work to restore service to Namespaces that were not
protected by High Availability. A cloud outage can leave lingering effects in Temporal's systems and applications, even
after the cloud provider restores the underlying service. An affected Namespace's outage may last longer than the cloud
provider's outage.

All Namespaces are backed up every 4 hours. If an outage causes data loss on a Namespace that was not protected by High
Availability, Temporal uses the backup to restore as much data as feasible.

## Outage types and their RTO/RPO

The following sections explain each type of outage in more detail, including the blast radius, Temporal Cloud features
that mitigate the outage, and whether the outage is included in the SLA calculation.

### Availability Zone outage {/* #availability-zone-outage */}

An
[Availability Zone](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-availability-zones)
(AZ) is akin to an isolated datacenter managed by a cloud hyperscaler, with independent power, networking, and cooling
infrastructure. Each cloud region contains multiple AZs, and an individual AZ can fail due to events such as hardware
failure, power loss, or a localized network partition.

AZ outages are the most common type of outage, and Temporal Cloud has weathered many of them transparently.

**Blast Radius:** A single Availability Zone within a single cloud region. Because every Namespace's components are
spread across at least three AZs, the blast radius to Temporal Cloud users is typically zero — Namespaces stay
operational with little to no downtime.

:::caution

While Temporal Cloud can withstand single AZ outages without disruption, if you have Workers that are deployed in the
impacted AZ, those Workers may be disrupted. To mitigate this risk, Temporal recommends deploying your Workers across
multiple AZs.

:::

**Mitigation:** Every Namespace is automatically spread across at least three Availability Zones, and any Namespace can
handle a single AZ failure without disruption to end-user Temporal operations.
[High Availability](/cloud/high-availability) features are _not_ required to keep Temporal Cloud operations running
through an AZ outage.

**SLA inclusion:** Included in the [SLA](/cloud/sla) calculation. Any errors during an AZ outage count toward SLA
credits, since AZ resilience is within Temporal's responsibility.

If two AZs fail simultaneously, Temporal Cloud treats the event as a [Cloud Region outage](#cloud-region-outage). In
that case, Namespaces in the region may be impacted, including those using
[Same-region Replication](/cloud/high-availability#same-region-replication).

:::info

When an AZ fails, Temporal may also trigger a failover on Namespaces that have High Availability enabled, as a
precaution in case the outage scope expands. For Multi-region and Multi-cloud Replication, you can opt out of this
behavior by [disabling automatic failovers](/cloud/high-availability/enable#automatic-failovers) on the Namespace.
Same-region Replication Namespaces always fail over automatically and cannot opt out.

:::

#### RTO and RPO

When using Temporal Cloud (no additional features required):

- **Near-zero RTO.** When a single AZ fails, the remaining two AZs continue serving requests without a failover, so end
  users see little to no disruption.
- **Zero RPO.** Writes to Workflow state are synchronously replicated across all three AZs before being acknowledged
  back to the Client, so an AZ failure cannot cause data loss.

### Cell outage {/* #cell-outage */}

Temporal Cloud runs on a
[cell architecture](https://docs.aws.amazon.com/wellarchitected/latest/reducing-scope-of-impact-with-cell-based-architecture/what-is-a-cell-based-architecture.html).
Each cell contains the software and services necessary to host a Namespace, and components within a cell are distributed
across at least three Availability Zones. Cells provide a strong unit of isolation: a problem inside one cell does not
propagate to other cells. A cell outage occurs when a cell becomes degraded or unavailable, disrupting the Namespaces
hosted within it.

**Blast Radius:** One cell, and the Namespaces within that cell, within a single region. Even though your Workers will
remain healthy, they will not be able to process Workflows because the Namespace is down.

**Mitigation:** [Multi-region Replication](/cloud/high-availability) and
[Multi-cloud Replication](/cloud/high-availability) replicate a Namespace into another cell in a different region or
different cloud provider. [Same-region Replication](/cloud/high-availability) replicates a Namespace into another cell
within the same region. When any of these features are enabled for a Namespace, an outage that disrupts a single cell
can be mitigated by failing the Namespace over to its replica.

**SLA inclusion:** Included in the [SLA](/cloud/sla) calculation. Any errors during a cell outage count toward SLA
credits, since mitigating cell outages is within Temporal's responsibility.

Cell-level disruptions occur from time to time, and Temporal's replication and failover tooling has restored affected
Namespaces in real-world incidents.

#### RTO and RPO

When using Same-region Replication, Multi-region Replication, or Multi-cloud Replication for automatic failover:

- **RTO under 20 minutes.** Temporal detects the disruption and fails the Namespace over to its replica cell.
- **RPO under 1 minute.** Asynchronous replication keeps the replica close to the active cell.

Even though the RPO target is under 1 minute, data is virtually never "lost" thanks to Temporal's built-in Recovery and
Conflict Resolution process, which reconciles state between the active and replica when the outage is over.

### Cloud Region outage {/* #cloud-region-outage */}

A cloud region as a whole can become degraded, with effects that span beyond any single cell or Availability Zone.

**Blast Radius:** All Namespaces and Workers within a single cloud region are potentially affected.

**Mitigation:** [Multi-region Replication](/cloud/high-availability) and
[Multi-cloud Replication](/cloud/high-availability) place the replica outside the affected region, so a Namespace can
fail over and continue serving Workflows. Same-region Replication does not protect against a Cloud Region outage, since
the replica resides in the same region.

**SLA inclusion:** Included in the [SLA](/cloud/sla) calculation only for Namespaces that have Multi-region Replication
or Multi-cloud Replication enabled with automatic failovers — in those cases, Temporal can mitigate the outage.
For Namespaces without these features, a Cloud Region outage is excluded from the SLA calculation, as it is beyond
Temporal's control to mitigate.

If two or more regions in the same cloud provider experience an outage simultaneously, Temporal Cloud treats the event
as a [Cloud-wide outage](#cloud-wide-outage).

Regional outages are less common than cell or AZ outages, but they do happen. During the
[AWS us-east-1 incident on October 20, 2025](https://temporal.io/blog/how-devs-kept-running-during-the-aws-us-east-1-oct-20-2025),
Temporal Cloud's regional failover kept customer Namespaces running.

#### RTO and RPO

When using Multi-region Replication or Multi-cloud Replication for automatic failover:

- **RTO under 20 minutes.** Temporal detects the regional disruption and fails the Namespace over to its replica in
  another region.
- **RPO under 1 minute.** Asynchronous replication keeps the replica close to the active region.

Even though the RPO target is under 1 minute, data is virtually never "lost" thanks to Temporal's built-in Recovery and
Conflict Resolution process, which reconciles state between the active and replica when a failover occurs.

### Cloud-wide outage {/* #cloud-wide-outage */}

On rare occasions, an issue affects two or more regions of a single cloud provider at once. Any simultaneous outage of
two or more regions in the same cloud provider is treated as a cloud-wide outage.

**Example causes:** a software bug rolled out to every region of a cloud provider that triggers cascading failures
across the provider's infrastructure, or two or more regions in the same cloud experiencing independent regional outages
at the same time.

**Blast Radius:** Most or all regions of a single cloud provider. Every Namespace and every Worker hosted in that cloud
is potentially affected.

**Mitigation:** [Multi-cloud Replication](/cloud/high-availability) places the replica in a different cloud provider
entirely, so the Namespace can fail over even when an entire cloud provider goes down.

**SLA inclusion:** Included in the [SLA](/cloud/sla) calculation only for Namespaces that have Multi-cloud Replication
enabled with automatic failovers — in those cases, Temporal can mitigate the outage. For Namespaces without this
feature, a cloud-wide outage is excluded from the SLA calculation, as it is beyond Temporal's control to mitigate.

Cloud-wide outages are the rarest category, but they
[have occurred](https://status.cloud.google.com/incidents/ow5i3PPK96RduMcb1SsW). Multi-cloud Replication is designed to
keep Namespaces running through such events.

#### RTO and RPO

When using Multi-cloud Replication for automatic failover:

- **RTO under 20 minutes.** Temporal detects the cloud-wide disruption and fails the Namespace over to its replica in a
  different cloud provider.
- **RPO under 1 minute.** Asynchronous replication keeps the replica close to the active region, even across cloud
