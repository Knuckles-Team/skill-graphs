}
```

- `region` (required): The [region code](/cloud/regions) of the region to failover to. Must be a region where the
  Namespace has a replica in `Activated` replica state, indicating the replica is ready to be failed over to. Example:
  `aws-us-east-1`
- `asyncOperationId` (optional): A user-defined ID for tracking the async operation. If not set, the server will assign
  one.

**Using gRPC**

Use the
[`FailoverNamespaceRegion`](https://buf.build/temporalio/cloud-api/docs/main:temporal.api.cloud.cloudservice.v1#temporal.api.cloud.cloudservice.v1.CloudService.FailoverNamespaceRegion)
RPC with a
[`FailoverNamespaceRegionRequest`](https://buf.build/temporalio/cloud-api/docs/main:temporal.api.cloud.cloudservice.v1#temporal.api.cloud.cloudservice.v1.FailoverNamespaceRegionRequest):

```protobuf
message FailoverNamespaceRegionRequest {
    // The namespace to failover.
    string namespace = 1;
    // The id of the region to failover to.
    // Must be a region that the namespace is currently available in.
    string region = 2;
    // The id to use for this async operation - optional.
    string async_operation_id = 3;
}
```

Both methods return a
[`FailoverNamespaceRegionResponse`](https://buf.build/temporalio/cloud-api/docs/main:temporal.api.cloud.cloudservice.v1#temporal.api.cloud.cloudservice.v1.FailoverNamespaceRegionResponse)
containing an async operation that you can use to track the failover status.

</TabItem>

</Tabs>

:::info Terraform not supported

The [Temporal Cloud Terraform provider](https://registry.terraform.io/providers/temporalio/temporalcloud/latest) does
not support triggering failovers. You must use the Web UI, tcld CLI, or Cloud Ops API.

:::

Once the failover async operation returns successfully, the Namespace will be failed over. Temporal manages retries for
the failover Workflow. In the rare event that an internal error prevents the failover from completing, the Temporal
on-call team is automatically paged to intervene and force the failover to completion.

## Return to the primary with failbacks {/* #failbacks */}

Failback behavior depends on whether the failover was automatic or manually triggered.

### After an automatic failover {/* #after-an-automatic-failover */}

After an automatic failover, Temporal Cloud automatically fails back to the original region once the region is
healthy. No action is required from you. Follow [Temporal's status page](https://status.temporal.io) for updates on the
original region's health.

If you prefer to manage failback yourself, you have two options:

- **Opt out of automatic failback (manage failback manually):** After the automatic failover has completed,
  [disable automatic failovers](/cloud/high-availability/enable#automatic-failovers) on the Namespace to prevent
  Temporal from automatically failing back. When you're ready to return to the original region,
  [trigger a failover](#trigger-failover) to that region and then re-enable automatic failovers.

- **Stay on the new region permanently ("fail forward"):** After the automatic failover has completed,
  [trigger a failover](#trigger-failover) to the region that is already active. This tells Temporal that you want to
  treat the new region as your primary for as long as it's healthy. Automatic failovers remain enabled,
  so Temporal will still protect you if the new region has an outage.

### After a user-triggered failover

If you triggered a failover yourself during an outage (instead of relying on an automatic failover), Temporal will
_not_ automatically fail back for you. You must [trigger a failover](#trigger-failover) back to the original region when
it is healthy. Monitor [Temporal's status page](https://status.temporal.io) for updates on region health.

Automatic failback is only available when the most recent failover was automatic.

### How to check whether your Namespace will be automatically failed back

If you are not sure whether your Namespace will be automatically failed back, check the list of failovers in the
Temporal Cloud Web UI on your Namespace's detail page:

- If the most recent failover was **automatic**, then Temporal will fail the Namespace back when
  the original region is healthy.
- If the most recent failover was **user-triggered**, then the Namespace will _not_ be automatically failed back. You
  must trigger the failback yourself.

## Workers and failovers {/* #worker */}

Enabling High Availability for Namespaces does not require specific Worker configuration. When a Namespace fails over to
the replica, the DNS redirection orchestrated by Temporal ensures that your existing Workers continue to poll the
Namespace without interruption. Temporal Cloud forwards their requests from the passive replica to the active region and
the responses back, so Workers keep running through a failover.

To route Workers to the passive region's replica, see [How requests reach the replica](/cloud/high-availability/ha-connectivity#how-requests-reach-the-replica).

To stop forwarding Worker polls to the active region, see [Change the forwarding behavior](/cloud/high-availability/enable#change-forwarding-behavior).

To disable automatic failovers, see [Enable or disable automatic failovers](/cloud/high-availability/enable#automatic-failovers).

When a Namespace fails over to a replica in a different region, Workers will be communicating cross-region.

- If your application cannot tolerate this latency, deploy a second set of Workers in the replica's region or opt for a
  replica in the same region.
- In the case of a complete regional outage, Workers in the original region may fail alongside the original Namespace.
  To keep Workflows moving during this level of outage, deploy a second set of Workers to the secondary region.

Temporal Cloud enforces a maximum connection lifetime of 5 minutes, which gives your Workers an opportunity to
re-resolve the DNS.

## Test failovers {/* #testing */}

Temporal recommends regular failover testing for mission-critical applications in production. By testing in
non-emergency conditions, you verify that your application continues to function even when parts of the infrastructure
fail.

Because failover testing relies on manually triggering a failover, it applies to Multi-region and Multi-cloud
Replication. A [Same-region Replication](/cloud/high-availability#same-region-replication) Namespace fails over
automatically between cells and cannot be failed over manually for testing.

:::tip

If this is your first time performing a failover test, run it with a test-specific Namespace and application. Practice
runs help ensure the process runs smoothly during real incidents in production.

:::

<DiscoverableDisclosure label="Why test?">

Failover testing (also known as "<ToolTipTerm term="trigger testing" />") can:

- **Validate replicated deployments:** In multi-region setups, failover testing ensures your application can run from
  another region when the primary region experiences outages.

- **Assess replication lag:** In multi-region deployments, monitoring
  [replication lag](/cloud/metrics/openmetrics/metrics-reference#temporal_cloud_v1_replication_lag_p99) between regions
  is important. Check the lag before initiating a failover to avoid rolling back Workflow progress.

- **Assess recovery time:** Manual testing helps you measure actual recovery time and check if it meets your expected
  [Recovery Time Objective (RTO)](/cloud/rpo-rto).

- **Identify potential issues:** Failover testing uncovers problems not visible during normal operation, including
  issues like
  [backlogs and capacity planning](https://temporal.io/blog/workers-in-production#testing-failure-paths-2438) and how
  external dependencies behave during a failover event.

- **Operational readiness:** Regular testing familiarizes your team with the failover process, improving their ability
  to handle real incidents.

</DiscoverableDisclosure>

---

## Connectivity for High Availability

A Namespace with High Availability features spans two regions, and the endpoint your Workers and Clients connect through determines how they behave before, during, and after a failover.
This page covers:

- How to choose between the Namespace Endpoint and a Regional Endpoint for a Namespace with High Availability features.
- How to configure PrivateLink so that failover remains transparent to Workers on private networks.

## How to choose an endpoint for a Namespace with High Availability features

Temporal Cloud exposes two kinds of gRPC endpoints for a Namespace.
See [How to access a Namespace](/cloud/namespaces#access-namespaces) for the general definitions; this section focuses on how each behaves with replication and failover.

### Namespace Endpoint (recommended)

Format: `<namespace>.<account>.tmprl.cloud:7233`

The Namespace Endpoint always connects to whichever region is currently active.
Under the hood, it is a CNAME that points at the active region's Regional Endpoint.
When Temporal Cloud fails the Namespace over, it updates the CNAME to point at the new active region.
The DNS TTL is 15 seconds, so Clients converge within about 30 seconds with no configuration change on your side.

Use the Namespace Endpoint unless you have a specific reason to pin traffic to a region.

### Regional Endpoint

Format: `<cloud>-<region>.region.tmprl.cloud:7233` (for example, `aws-us-west-2.region.tmprl.cloud` or `gcp-us-central1.region.tmprl.cloud`).
See [regions](/cloud/regions) for the full list.

A Regional Endpoint is shared across every Namespace that is active or replicated in that region.
Unlike the Namespace Endpoint, a Regional Endpoint stays pinned to the region in its name — if that region holds the passive replica of your Namespace, the Regional Endpoint connects to the passive replica.

Use a Regional Endpoint only when you need explicit control over which replica a Client or Worker reaches.

Trade-offs to consider:

- **Faster recovery.** A Worker connecting through a Regional Endpoint skips the DNS step that Clients on the Namespace Endpoint wait for during a failover. This removes the ~30-second DNS convergence window from the recovery path, which is useful for Workloads that must minimize [Recovery Time](/cloud/rpo-rto) at all costs.
- **You are responsible for regional coverage.** A Worker using the Regional Endpoint of a region cannot reach the Namespace if that region is in an outage. To stay available through a failover, you must run Workers that use the **replica** region's Regional Endpoint — Workers pointed only at the outage region's Regional Endpoint will not reconnect automatically.

When authenticating with mTLS, set the Client's `server_name` / `serverNameOverride` config equal to the Namespace Endpoint.
This overrides the SNI that the Client will expect during the TLS Handshake with Temporal Cloud.
The Regional Endpoint forwards the request to your Namespace, so the Client must expect the Namespace's certificate during the TLS handshake.

For example, in Typescript, the Client's config would be set like this:

```typescript
await Connection.connect({
  address: 'aws-us-east-1.region.tmprl.cloud:7233',
  tls: {
    serverNameOverride: 'my-namespace.my-account.tmprl.cloud',
    clientCertPair: { crt: clientCert, key: clientKey },
  },
  ...
});
```

### How endpoints route on failover

Consider a Namespace replicated across `us-east-1` (initially active) and `us-west-2` (initially the replica), with a failover that swaps the two.

| Client connects via                         | Before failover | After failover          |
| ------------------------------------------- | --------------- | ----------------------- |
| Namespace Endpoint                          | `us-east-1`     | `us-west-2` (automatic) |
| Regional Endpoint `aws-us-east-1.region...` | `us-east-1`     | `us-east-1`             |
| Regional Endpoint `aws-us-west-2.region...` | `us-west-2`     | `us-west-2`             |

The Namespace Endpoint moves with the active region via an updated CNAME — no Client changes required.
The Regional Endpoints do not change their targets on failover: each continues to route to the replica that lives in its region.

## How requests reach the replica {/* #how-requests-reach-the-replica */}

A request can reach the passive replica in three ways:

- **Through the passive region's Regional Endpoint.** A [Regional Endpoint](#regional-endpoint) is pinned to its region, so the Regional Endpoint of the region that currently holds the passive replica connects to the passive replica.
- **Through a PrivateLink or Private Service Connect endpoint in the passive region.** A VPC Endpoint or PSC endpoint in the passive region routes to the passive replica.
- **Through the Namespace Endpoint during a failover.** When a Namespace fails over, two things happen in parallel:
  1. The replica becomes active, and the former active becomes a replica.
  2. The Namespace Endpoint changes to point at the replica's region, and the Worker re-resolves the Namespace Endpoint to connect to the new active region via DNS.

  If #1 completes before #2, a Worker that was connected to the former active before the failover will stay connected to it even after it becomes the replica. The Worker will change to point at the new active when the DNS changes propagate and the Client re-resolves DNS (typically 30 seconds, though up to 5 minutes, bounded by Temporal Cloud's maximum connection lifetime).

By default, Temporal Cloud transparently forwards any request that reaches the passive replica to the active region, and the response back.

To learn what forwarding does, see [Request forwarding](/cloud/high-availability/#request-forwarding).

To stop forwarding Worker polls on a Namespace, see [Change the forwarding behavior](/cloud/high-availability/enable#change-forwarding-behavior).

## How to use PrivateLink with High Availability features

:::tip

Proper networking configuration is required for failover to be transparent to Clients and Workers when using PrivateLink.
This section describes how to configure routing for Namespaces with High Availability features on AWS PrivateLink.

:::

These instructions assume you already have the private connections in place. If not, follow the [AWS PrivateLink](/cloud/connectivity/aws-connectivity) or [GCP Private Service Connect](/cloud/connectivity/gcp-connectivity) creation guides first.

## How HA + private connectivity works

A Namespace with High Availability features has two replicas — a primary and a secondary, in different regions or different cloud providers. At any moment, one is **active** and one is **passive**. On failover, Temporal Cloud changes the active replica.

Temporal Cloud expresses the active replica through DNS:

- The Namespace DNS record (`<ns>.<account>.tmprl.cloud`) is a CNAME.
- It points to the active region's regional record (`<provider>-<region>.region.tmprl.cloud`).
- On failover, Temporal Cloud rewrites the CNAME target.

Namespace DNS records have a 15-second TTL. Clients should converge to the new region within roughly 30 seconds (about twice the TTL) once their resolver cache expires.

For private connectivity, your job is to make sure that:

- Override the Regional Endpoint's DNS zone to resolve to a VPC Endpoint.
- Ensure network connectivity between the two regions.

:::warning Do not override the Namespace Endpoint in your private hosted zone

For HA Namespaces, the PHZ must override only the regional records (`<provider>-<region>.region.tmprl.cloud`) — never the Namespace Endpoint itself (`<ns>.<account>.tmprl.cloud`).

If the PHZ holds a record for the Namespace Endpoint, the resolver answers from the PHZ before consulting public DNS, so Temporal Cloud's active-region CNAME is never followed. On failover, Workers keep resolving to the old (now passive) region's VPC Endpoint and never reach the new active region.

This matters most when **enabling HA on a Namespace that previously used the [single-region PHZ pattern](/cloud/connectivity/aws-connectivity#configuring-private-dns-for-aws-privatelink)**, where the Namespace Endpoint itself was the overridden name. See [How to enable HA on a Namespace using Private Connectivity](#how-to-enable-ha-on-a-namespace-using-private-connectivity) below for the migration steps.

:::

:::warning Do not attach a Stable IPs public Connectivity Rule

If you attach a public [Connectivity Rule with Stable IPs](/cloud/connectivity/ip-addresses#stable-ip-addresses) to a Namespace, the Namespace Endpoint resolves to a public Stable IP instead of to `<provider>-<region>.region.tmprl.cloud`. Stable IPs DNS behavior supersedes the regional DNS behavior described here, so the Namespace Endpoint's DNS resolution will not work in the way the Private Hosted Zone needs. To keep HA + Private Connectivity working, do not attach a Stable IPs public Connectivity Rule to that Namespace.

:::

## How to enable HA on a Namespace using Private Connectivity: changing private DNS overrides from single-region to multi-region {/* #how-to-enable-ha-on-a-namespace-using-private-connectivity */}

If you are turning on [High Availability features](/cloud/high-availability/enable) on a Namespace that already uses AWS PrivateLink or GCP Private Service Connect, the existing private DNS setup almost certainly needs to change before failover will work.

The common single-region private DNS pattern (described in the [AWS PrivateLink guide](/cloud/connectivity/aws-connectivity#configuring-private-dns-for-aws-privatelink) and the [GCP PSC guide](/cloud/connectivity/gcp-connectivity)) overrides the **Namespace Endpoint** directly. That pattern short-circuits Temporal Cloud's regional CNAME and prevents failover from working — see the warning above.

Follow these steps in order to update your private DNS overrides without interrupting traffic:

1. **Inventory the existing PHZ records.** List the records in your private hosted zone for `tmprl.cloud`. Note any CNAME (or A record) for `<ns>.<account>.tmprl.cloud` — that is the single-region override you'll be removing.

2. **Add regional records for both the source and target HA regions.** Before removing anything, create:
   - `aws-<source-region>.region.tmprl.cloud` → source-region VPC Endpoint
   - `aws-<target-region>.region.tmprl.cloud` → target-region VPC Endpoint

   (Or the GCP Cloud DNS equivalents — see [GCP PSC](#single-cloud-ha-on-gcp-private-service-connect) below.) These records are additive and do not yet affect resolution of `<ns>.<account>.tmprl.cloud`, because the Namespace-endpoint override still short-circuits the chain.

3. **Confirm both VPC Endpoints are reachable from your Worker VPCs.** From a Worker host, `dig` the new regional names and confirm they resolve to the right VPC Endpoint. Also verify the network path actually works in both regions (security groups, route tables, cross-region connectivity).

4. **Enable HA on the Namespace.** Follow [Enable High Availability features](/cloud/high-availability/enable). Temporal Cloud creates the replica and starts replicating.

5. **Remove the Namespace-endpoint PHZ record.** Delete the `<ns>.<account>.tmprl.cloud` record from the PHZ. With it gone, Workers resolve the name through public DNS → regional CNAME → PHZ regional override → VPC Endpoint, which is the correct HA chain. **Do not skip this step.** If the Namespace-endpoint override remains, failover does not work.

6. **Test failover end-to-end.** Use [forced failover](/cloud/high-availability/failovers) in a staging environment to confirm Workers converge to the new active region within the expected window (about 30 seconds after the public CNAME update, given the 15-second TTL).

:::caution Order matters

Adding the regional records first (step 2) and removing the Namespace-endpoint record last (step 5) means Workers always have a working DNS resolution. Reversing the order leaves a window where Workers cannot resolve the Namespace Endpoint at all.

:::

## How to migrate to another Temporal Cloud Region when using Private Connectivity {/* #how-to-migrate-regions-with-private-connectivity */}

To move a Namespace to a new Temporal Cloud Region while keeping Private Connectivity in place, the recommended pattern is to use a **separate private hosted zone in each region**, each overriding the Namespace Endpoint to point at that region's own VPC Endpoint. Because a PHZ is scoped only to the VPCs it is associated with, Workers in each region resolve the Namespace Endpoint to their local VPC Endpoint and traffic stays in-region throughout the move.

This is not the only way to handle a region change with Private Connectivity, but it is the most commonly used.

Steps:

1. **Keep the existing Namespace Endpoint PHZ override in the original region.** Do not change anything in the original region's private DNS setup yet.

2. **Create a new VPC Endpoint in the new region.** Follow the [AWS PrivateLink](/cloud/connectivity/aws-connectivity) (or [GCP PSC](/cloud/connectivity/gcp-connectivity)) creation steps in the new region's VPC.

3. **In the new region, create a PHZ that overrides the Namespace Endpoint to point at the new VPC Endpoint.** Use the [single-region PHZ pattern](/cloud/connectivity/aws-connectivity#configuring-private-dns-for-aws-privatelink), scoped only to the new region's Worker VPCs. With one PHZ per region, traffic in each region routes through that region's own VPC Endpoint.

4. **Add a replica in the new region.** Follow [Enable High Availability features](/cloud/high-availability/enable). The new region comes up as a passive replica.

5. **Start Workers in the new region.** They begin processing tasks immediately, even though they are connecting to the passive replica, because Temporal Cloud forwards Workflow and Activity tasks across regions transparently. This is what keeps the region change zero-downtime.

6. **Failover to the new region.** Trigger a [forced failover](/cloud/high-availability/failovers) to make the new region active. Workers in the old region keep running and keep using the old VPC Endpoint — they now connect to the passive replica that lives in the old region, and Temporal Cloud forwards their tasks to the new active region.

7. **Drain and remove Workers and the VPC Endpoint in the old region.** Once you are confident the new region is handling all new work and you no longer need old-region Workers, stop them and tear down the old region's VPC Endpoint and PHZ.

8. **Remove the replica in the old region.** See [Migrate between regions](/cloud/migrate/migrate-within-cloud) for the replica-removal step. The Namespace is now single-region in the new location, and the HA pricing surcharge no longer applies.

:::note Per-region PHZ vs. shared regional-record PHZ

This pattern is **different** from the long-term HA setup described in [Single-cloud HA on AWS PrivateLink](#single-cloud-ha-on-aws-privatelink), which uses one shared PHZ holding regional records (`aws-<region>.region.tmprl.cloud`) and relies on DNS-based failover to switch Workers between regions. The region-change pattern instead uses one PHZ per region, each overriding the Namespace Endpoint itself, and relies on Temporal Cloud's cross-region task forwarding rather than DNS to keep Workers productive across the cutover.

:::

## Single-cloud HA on AWS PrivateLink

### How Namespace DNS records work with PrivateLink

When using PrivateLink, you connect to Temporal Cloud through a VPC Endpoint, which uses addresses local to your network.
Temporal treats each `region.<tmprl_domain>` as a separate zone.
This setup allows you to override the default zone, ensuring that traffic is routed internally for the regions you're using.

A Namespace's active region is reflected in the target of the Namespace Endpoint's CNAME record.
For example, if the active region of a Namespace is AWS us-east-1, the DNS configuration would look like this:

| ha-namespace.account-id.tmprl.cloud | CNAME | aws-us-east-1.region.tmprl.cloud |
| ----------------------------------- | ----- | -------------------------------- |

After a failover, the CNAME record is updated to point to the failover region, for example:

| ha-namespace.account-id.tmprl.cloud | CNAME | aws-us-west-2.region.tmprl.cloud |
| ----------------------------------- | ----- | -------------------------------- |

The Temporal domain did not change, but the CNAME updated from us-east-1 to us-west-2.

<CaptionedImage
    src="/img/cloud/high-availability/private-link.png"
    title="Customer side solution example"
    zoom="true"
/>

### How to set up the DNS override

In AWS, use a Route 53 private hosted zone for `region.tmprl.cloud` to override resolution per region:

| Record name                          | Record type | Value (your VPC Endpoint DNS)                                |
| ------------------------------------ | ----------- | ------------------------------------------------------------ |
| `aws-us-west-2.region.tmprl.cloud`   | CNAME       | `vpce-...-us-west-2.vpce.amazonaws.com`                      |
| `aws-us-east-1.region.tmprl.cloud`   | CNAME       | `vpce-...-us-east-1.vpce.amazonaws.com`                      |

Link the private zone to every VPC where Workers run.

When your Workers connect to the Namespace, they first resolve `<ns>.<account>.tmprl.cloud`, which CNAMEs to `<aws-active-region>.region.tmprl.cloud`, which then resolves to your local VPC Endpoint.

You also need to decide how Workers reach whichever region becomes active. Either:

- Run Workers in **both** regions continuously (recommended), or
