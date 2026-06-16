
With Provisioned Capacity, you can set your rate limits by selecting the number of Temporal Resource Units (TRUs) on your Namespace.
Each TRU supports up to 500 APS and can be provisioned in groups of 2, 3, 4, 6, 8, 10, or 12 TRUs if there is capacity available in a region.
When TRUs are requested we aim to provision the additional capacity within two minutes.

:::tip Large TRU requests

For Requests in excess of 4 TRUs in regions outside of the US, we recommend submitting a support ticket to ensure capacity availability.

:::

### Provisioned Capacity Availability
The amount of capacity available within a region may vary.
Temporal will check available capacity at the time of your request and aims to provision requested capacity within two minutes.
If you need capacity beyond what is self-serviceable or available in a region, please [file a support ticket](https://docs.temporal.io/cloud/support#ticketing) indicating the limit, region, and timeframe that the capacity is needed.

### When should I use Provisioned Capacity?

Provisioned Capacity works well when you’re aware of specific increases in load on your Namespace. For example:

* Planned events
* Unplanned events/usage spikes
* Known but sudden system spikes
* Load testing
* Migrating workloads

Depending on your usage patterns and your system monitoring, you can use Provisioned Capacity to quickly remedy rate limiting without contacting support.
You can also automate changes in capacity if you have a known event or a recurring usage pattern that produces predictable usage spikes.

## Setting Capacity Modes
Capacity Modes and TRUs can be set via the Temporal Cloud UI, CLI, or API.
Capacity modes can be set and adjusted by Global Admin and Namespace Admin.

### Setting Capacity Modes from the UI

You can set Capacity Modes for an individual Namespace by navigating to the Namespace page in the Temporal Cloud UI (`https://cloud.temporal.io/namespaces/<Namespace ID>`).
To view your current capacity configuration and change your capacity mode, navigate to the capacity tile and click *Manage Capacity*.

![Manage Capacity button in the Temporal UI](/img/cloud/provisioned-capacity/manage_capacity_button.png)

Under *Manage Capacity* you will be able to select between *On-Demand* and *Provisioned Capacity* modes.
The *On-Demand* section will display your available On-Demand capacity.
The *Provisioned* section will display the limit available with selected TRUs and the Included Actions required per hour. [See details on Provisioned Capacity Pricing](/cloud/pricing#capacity-modes-pricing).

To switch to Provisioned capacity:

1. Select the *Provisioned* radio button.
1. Specify the requested number of TRUs using the slider.
1. Check the dialog acknowledging potential pricing implications.
1. Click *Confirm*.

In addition to the Capacity Mode selections, a summary of APS usage over the last seven days is included to help you estimate your current usage.
For more detailed information, we recommend setting up metrics that track your APS and Limits.
See [Monitoring Trends Against Limits](/cloud/service-health#rps-aps-rate-limits) to track usage trends.

![Manage Capacity panel in the Temporal UI](/img/cloud/provisioned-capacity/manage_capacity_panel.png)

### Setting Capacity Modes from the CLI

```command
tcld namespace capacity update --namespace <namespace_name> --capacity-mode <on_demand|provisioned> --capacity-value <tru value> [--request–id <request_id> --resource-version <resource-version>]
```

Use this command to specify the Namespace name and configure the capacity settings:

* `--capacity-mode` sets the billing mode for the Namespace. Use `on_demand` for automatic scaling or `provisioned` for a fixed capacity allocation.
* `--capacity-value` sets the throughput value in TRUs (Temporal Resource Units).

Optional flags:

* `--request-id` specifies a request identifier for the asynchronous operation. If not specified, the server assigns one automatically.
* `--resource-version` specifies the resource version (etag) to update from. If not set, the CLI uses the latest version.

If using API key authentication with the `--api-key` flag, you must add it directly after the tcld command and before capacity update.

### Setting Capacity Modes from the API

Call the `UpdateNamespace` API after Namespace creation and define the desired capacity state as part of the capacity spec.

---

## AWS PrivateLink connectivity

[AWS PrivateLink](https://aws.amazon.com/privatelink/) allows you to open a path to Temporal without opening a public egress.
It establishes a private connection between your Amazon Virtual Private Cloud (VPC) and Temporal Cloud.
This one-way connection means Temporal cannot establish a connection back to your service.
This is useful if normally you block traffic egress as part of your security protocols.
If you use a private environment that does not allow external connectivity, you will remain isolated.

After creating the PrivateLink endpoint, configure your clients to use it through either [private DNS](#configuring-private-dns-for-aws-privatelink) or [direct VPCE targeting](#direct-vpce) (single-region Namespaces only).

## Requirements

Your AWS PrivateLink endpoint must be in the same region as your Temporal Cloud namespace. If using [replication for High Availability](/cloud/high-availability), the PL connection must be in the same region as one of the replicas.

AWS Cross Region endpoints are not supported.

## Creating an AWS PrivateLink connection

Set up PrivateLink connectivity with Temporal Cloud with these steps:

1. Open the AWS console with the region you want to use to establish the PrivateLink.
2. Search for "VPC" in _Services_ and select the option.

   ![AWS console showing services, features, resources](/img/cloud/privatelink/aws-console.png)
3. Select _Virtual private cloud_ > _Endpoints_ from the left menu bar.
4. Click the _Create endpoint_ button to the right of the _Actions_ pulldown menu.
5. Under _Type_ category, select _Endpoint services that use NLBs and GWLBs_.
   This option lets you find services shared with you by service name.
6. Under _Service settings_, fill in the _Service name_ with the PrivateLink Service Name for the region you’re trying to connect from:

:::tip

PrivateLink endpoint services are regional.
Individual Namespaces do not use separate services.

:::

<JsonTable filename="/json/privatelink_aws.json" />

7. Confirm your service by clicking on the _Verify service_ button. AWS should respond "Service name verified."

   ![The service name field is filled out and the Verify service button is shown](/img/cloud/privatelink/service-settings.png)
8. Select the VPC and subnets to peer with the Temporal Cloud service endpoint.
9. Select the security group that will control traffic sources for this VPC endpoint.
   The security group must accept TCP ingress traffic to port 7233 for gRPC communication with Temporal Cloud.
10. Click the _Create endpoint_ button at the bottom of the screen.
    If successful, AWS reports "Successfully created VPC endpoint." and lists the new endpoint.
    The new endpoint appears in the Endpoints list, along with its ID.

    ![The created endpoint appears in the Endpoints list](/img/cloud/privatelink/endpoint-created.png)
11. Click on the VPC endpoint ID in the Endpoints list to check its status.
    Wait for the status to be “Available”.
    This can take up to 10 minutes.
12. Once the status is "Available", the AWS PrivateLink is ready for use.

    ![Highlighted DNS names section shows your hostname](/img/cloud/privatelink/details.png)

The next step is to [configure private DNS](#configuring-private-dns-for-aws-privatelink) so your clients can use the PrivateLink connection. For single-region Namespaces that don't need per-Namespace DNS records, you can use [direct VPCE targeting](#direct-vpce) instead.

## Configuring Private DNS for AWS PrivateLink

### Why configure private DNS?

When you connect to Temporal Cloud through AWS PrivateLink you normally must:

1. **Point your SDKs/Workers at the PrivateLink DNS name** for the VPC Endpoint (e.g., `vpce-0123456789abcdef-abc.us-east-1.vpce.amazonaws.com`), **and**
2. **Override the Server Name Indicator (SNI)** so that the TLS handshake still presents the public Temporal Cloud hostname (e.g., `my-namespace.my-account.tmprl.cloud`).

By creating a Route 53 **private hosted zone (PHZ)** that maps the public Temporal Cloud hostname (or region hostname) to your VPC Endpoint, you can:

- Keep using the standard Temporal Cloud hostnames in code and configuration.
- Eliminate the need to set a custom SNI override.
- Make future Endpoint rotations transparent—only the PHZ record changes.

This approach is **optional**; Temporal Cloud works without it. It simply streamlines configuration and operations. If you cannot use private DNS, refer to [our guide for updating the server and TLS settings on your clients](/cloud/connectivity#update-dns-or-clients-to-use-private-connectivity).

### Prerequisites

| Requirement                                           | Notes                                                                                                                              |
| ----------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| AWS VPC with DNS resolution and DNS hostnames enabled | _VPC console → Edit DNS settings → enable both checkboxes._                                                                        |
| Interface VPC Endpoint for Temporal Cloud             | Subnets must be associated with the VPC and Security Group must allow TCP ingress traffic to port 7233 from the appropriate hosts. |
| Route 53 available in your AWS account                | You need permission to create Private Hosted Zones and records.                                                                    |
| Namespace details                                     | Needed to choose the correct override domain pattern below.                                                                        |

### Choose the override domain and endpoint

| Endpoint type      | PHZ domain format                     | Example                                 | Use when |
| ------------------ | ------------------------------------- | --------------------------------------- | -------- |
| Namespace endpoint | `<namespace-id>.tmprl.cloud`          | `payments.abcde.tmprl.cloud`            | **Single-region Namespaces only.** Simplest pattern — one record per Namespace. Do not use this for [High Availability](/cloud/high-availability/ha-connectivity) Namespaces: the override short-circuits Temporal's regional CNAME chain and failover stops working. |
| Regional endpoint  | `<cloud>-<region>.region.tmprl.cloud` | `aws-ap-northeast-2.region.tmprl.cloud` | **Single-region or HA Namespaces.** One record per Temporal Cloud region, reused by every Namespace active or replicated in that region. **Required for HA Namespaces** — see [Connectivity for High Availability](/cloud/high-availability/ha-connectivity). |

:::warning HA Namespaces require the regional override

For Namespaces with [High Availability](/cloud/high-availability/ha-connectivity), use the regional-endpoint PHZ pattern only. The Namespace-endpoint override is read out of the PHZ before public DNS, so the regional CNAME that Temporal Cloud rewrites on failover is never followed and Workers stay pinned to the old region. If you're switching an existing single-region private Namespace to HA, see [How to enable HA on a Namespace using Private Connectivity](/cloud/high-availability/ha-connectivity#how-to-enable-ha-on-a-namespace-using-private-connectivity) for the PHZ migration steps.

:::

The step-by-step below walks through the **Namespace endpoint** pattern, which is the simpler single-region case. For HA, follow the [HA Connectivity guide](/cloud/high-availability/ha-connectivity) instead, which uses the same Route 53 mechanics but on the regional records.

### Step-by-step instructions

:::warning Order matters

A Route 53 private hosted zone with no records causes DNS resolution to fail (NXDOMAIN) inside any associated VPC. If you create an empty PHZ for `<account>.tmprl.cloud` and associate it with a VPC where Workers are running, **all Worker traffic to Temporal Cloud in that VPC stops** until you add the CNAME record. Follow the steps below in order to avoid this.

:::

#### 1. Collect your PrivateLink endpoint DNS name

```bash
aws ec2 describe-vpc-endpoints \
  --vpc-endpoint-ids $VPC_ENDPOINT_ID \
  --query "VpcEndpoints[0].DnsEntries[0].DnsName" \
  --output text
