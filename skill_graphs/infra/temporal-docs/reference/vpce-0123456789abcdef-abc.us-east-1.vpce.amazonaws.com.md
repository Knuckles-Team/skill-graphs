# vpce-0123456789abcdef-abc.us-east-1.vpce.amazonaws.com
```

Save the **`vpce-*.amazonaws.com`** value — you will target it in the CNAME record.

#### 2. Create a Route 53 Private Hosted Zone (do not yet attach Worker VPCs)

a. Open _Route 53 → Hosted zones → Create hosted zone_.
b. Enter the domain chosen from the table above, e.g., `payments.abcde.tmprl.cloud`.
c. Type: _Private hosted zone for Temporal Cloud_.
d. Leave VPC associations empty for now (you'll add them in step 4).
e. Create the hosted zone.

#### 3. Add a CNAME record

Inside the new PHZ:

| Field           | Value                                                                                 |
| --------------- | ------------------------------------------------------------------------------------- |
| **Record name** | the Namespace Endpoint (e.g., `payments.abcde.tmprl.cloud`).                          |
| **Record type** | `CNAME`                                                                               |
| **Value**       | Your VPC Endpoint DNS name (`vpce-0123456789abcdef-abc.us-east-1.vpce.amazonaws.com`) |
| **TTL**         | 60s is typical; 15s for Namespaces with High Availability (to minimize recovery time after failover). |

#### 4. Associate the PHZ with your Worker VPCs and verify

Now that the record exists, associate the PHZ with every VPC that contains Temporal Workers or SDK clients (Route 53 → your zone → _Edit settings_ → _Add VPC_).

:::tip Test with a non-production VPC first

We strongly recommend that you test with a non-production VPC first. Attach the PHZ to a non-production VPC, validate end-to-end resolution and connectivity from a host in that VPC, and only then attach production Worker VPCs. This catches misconfigured records before they affect production traffic.

:::

Verify DNS resolution from inside one of the associated VPCs:

```bash
dig payments.abcde.tmprl.cloud
```

If the record resolves to the VPC Endpoint, you are ready to use Temporal Cloud without SNI overrides.

### Updating your workers/clients

With private DNS in place, configure your SDKs exactly as the public-internet examples show (filling in your own namespace):

```go
clientOptions := client.Options{
    HostPort: "payments.abcde.tmprl.cloud:7233",
    Namespace: "payments",
    // No TLS SNI override needed
}
```

The DNS resolver inside your VPC returns the private endpoint, while TLS still validates the original hostname—simplifying both code and certificate management.

## Configure private DNS for Namespaces with High Availability

For Namespaces with [High Availability features](/cloud/high-availability), you need to override DNS for `region.tmprl.cloud` so each region resolves to the local VPC Endpoint, and you need to ensure Workers can reach whichever region is active. Failover is transparent to clients only when this is set up correctly.

The complete guidance — including single-cloud (AWS-only) HA, multi-cloud HA (AWS PrivateLink + GCP Private Service Connect), and a recommended failover-testing plan — lives on a single page: [Connectivity for High Availability](/cloud/high-availability/ha-connectivity).

## Direct VPCE targeting without per-Namespace DNS {/* #direct-vpce */}

For single-region Namespaces, you can avoid creating DNS records for each Namespace by pointing Workers directly at the VPC Endpoint and overriding the TLS Server Name Indicator (SNI):

1. Create the PrivateLink VPC Endpoint (one per region — all Namespaces in that region share it).
2. Configure each Worker with:
   - **Endpoint**: the VPC Endpoint DNS name (e.g., `vpce-0123456789abcdef-abc.us-east-1.vpce.amazonaws.com:7233`)
   - **Server name** (SNI override): the Namespace Endpoint value (e.g., `my-namespace.my-account.tmprl.cloud`)

With this approach, new Namespaces do not require new DNS records.

:::warning Not compatible with High Availability Namespaces

This approach does not work for Namespaces with High Availability features.
HA Namespaces rely on Temporal's public DNS CNAME records to route traffic to the active region during failover.
If you bypass DNS, your Workers cannot follow the CNAME to the new region.
For HA Namespaces, use [private DNS](#configuring-private-dns-for-aws-privatelink) instead.

:::

## Adding PrivateLink from additional AWS accounts

A common pattern is to have separate AWS accounts for different lines of business, environments (staging, production), or compliance scopes (PCI vs non-PCI), each with its own VPC and Workers connecting to the same Temporal Cloud account.

You can create as many AWS PrivateLink VPC endpoints as you need to the same Temporal Cloud regional service — there is nothing to register, approve, or open a ticket for on the Temporal side.

For each additional AWS account or VPC:

1. In that account, create the AWS PrivateLink VPC endpoint targeting the regional service name from the [regions table](#available-aws-regions-privatelink-endpoints-and-dns-record-overrides) — same as in the [creation steps](#creating-an-aws-privatelink-connection) above.
2. Configure DNS in that VPC. You have two options:
   - Create a Route 53 Private Hosted Zone in that account scoped to the appropriate VPC(s), following the [private DNS steps](#configuring-private-dns-for-aws-privatelink) above. Each VPC's PHZ should point at the VPC Endpoint local to that VPC.
   - Or, use [direct VPCE targeting](#direct-vpce) (single-region Namespaces only).
3. **Optional:** if you want to enforce private-only access for a Namespace, add a Connectivity Rule for each VPC endpoint and attach all of them (plus a public rule, if needed) to the Namespace. See [Connectivity Rules](/cloud/connectivity#connectivity-rules).

There is no upper limit on the number of VPC endpoints you can connect from your side to a regional PrivateLink service. The default per-account limit on private Connectivity Rules is 50 — [contact support](/cloud/support#support-ticket) if you need to raise it.

## Available AWS regions, PrivateLink endpoints, and DNS record overrides

The following table lists the available Temporal regions, PrivateLink endpoints, and regional endpoints used for DNS record overrides:

<AWSRegions />

---

## Google Private Service Connect connectivity

[Google Cloud Private Service Connect](https://cloud.google.com/vpc/docs/private-service-connect) allows you to open a path to Temporal without opening a public egress.
It establishes a private connection between your Google Virtual Private Cloud (VPC) and Temporal Cloud.
This one-way connection means Temporal cannot establish a connection back to your service.
This is useful if normally you block traffic egress as part of your security protocols.
If you use a private environment that does not allow external connectivity, you will remain isolated.

:::warning Namespaces with High Availability features and GCP Private Service Connect

Automatic failover via Temporal Cloud DNS is not currently supported with GCP Private Service Connect.
If you use GCP Private Service Connect, you must manually update your workers to point to the active region's Private Service Connect endpoint when a failover occurs.

:::

## Requirements

Your GCP Private Service Connect connection must be in the same region as your Temporal Cloud namespace. If using [replication for High Availability](/cloud/high-availability), the PSC connection must be in the same region as one of the replicas.

## Creating a Private Service Connect connection

Set up Private Service Connect with Temporal Cloud with these steps:

1. Open the Google Cloud console
2. Navigate to **Network Services**, then **Private Service Connect**. If you haven't used **Network Services** recently, you might have to find it by clicking on **View All Products** at the bottom of the left sidebar.

   ![GCP console showing Network Services, and the View All Products button](/img/cloud/gcp/gcp-console.png)

3. Go to the **Endpoints** section. Click on **Connect endpoint**.

   ![GCP console showing the endpoints, and the Connect endpoint button](/img/cloud/gcp/connect-endpoint-button.png)

4. Under **Target**, select **Published service**, this will change the contents of the form to allow you to fill the rest as described below

   ![GCP console showing the endpoints, and the Connect endpoint button](/img/cloud/gcp/connect-endpoint.png)

- For **Target service**, fill in the **Service name** with the Private Service Connect Service Name for the region you’re trying to connect to:

:::tip

GCP Private Service Connect services are regional.
Individual Namespaces do not use separate services.

:::

<JsonTable filename="/json/privatelink_gcp.json" />

- For **Endpoint name**, enter a unique identifier to use for this endpoint. It could be for instance `temporal-api` or `temporal-api-<namespace>` if you want a different endpoint per namespace.
- For **Network** and **Subnetwork**, choose the network and subnetwork where you want to publish your endpoint.
- For **IP address**, click the dropdown and select **Create IP address** to create an internal IP from your subnet dedicated to the endpoint. Select this IP.
- Check **Enable global access** if you intend to connect the endpoint to virtual machines outside of the selected region. We recommend regional connectivity instead of global access, as it can be better in terms of latency for your workers. _**Note:** this requires the network routing mode to be set to **GLOBAL**._

5. Click the **Add endpoint** button at the bottom of the screen. The endpoint will appear with status **Pending**. This is expected — the next step is what flips it to **Accepted**.

6. [Create a Temporal Cloud Connectivity Rule](/cloud/connectivity#creating-a-connectivity-rule) using the Connection ID of the newly created endpoint and the corresponding GCP project. Use the **Connection ID** from the endpoint's detail page in the Google Cloud console (a numeric string such as `1234567890123456789`).

7. Once the status changes from "Pending" to "Accepted", the GCP Private Service Connect endpoint is ready for use.

:::warning PSC stays "Pending" until you create a Connectivity Rule

For GCP Private Service Connect, the Connectivity Rule is what tells Temporal Cloud to accept your PSC connection. Until you [create a Connectivity Rule](/cloud/connectivity#creating-a-connectivity-rule) for the connection, the endpoint will remain in **Pending**. There is no separate producer-side approval step — creating the Connectivity Rule is the approval.

If your endpoint is stuck Pending, the most common causes are:

- No Connectivity Rule exists for the connection ID. (Most common.)
- The Connectivity Rule was created with the wrong `connection-id`, `region`, or `gcp-project-id`.
- The endpoint is in a region that is not a [supported Temporal Cloud region](/cloud/regions).

:::

- Take note of the **IP address** assigned to your endpoint — you will use it to connect to Temporal Cloud.

:::caution
You still need to set up private DNS or override client configuration for your clients to actually use the new Private Service Connect connection to connect to Temporal Cloud.

See [configuring private DNS for GCP Private Service Connect](#configuring-private-dns-for-gcp-private-service-connect)
:::

## Configuring Private DNS for GCP Private Service Connect

### Why configure private DNS?

When you connect to Temporal Cloud through GCP Private Service Connect you normally must:

1. **Point your SDKs/Workers at the Private Service Connect endpoint IP address** _and_
2. **Override the Server Name Indicator (SNI)** so that the TLS handshake still presents the public Temporal Cloud hostname (e.g., `my-namespace.my-account.tmprl.cloud`).

By creating a **private Cloud DNS zone (PZ)** that maps the public Temporal Cloud hostname (or the region hostname) directly to the PSC endpoint IP address, you can:

- Keep using the standard Temporal Cloud hostnames in code and configuration.
- Eliminate the need to set a custom SNI override.
- Make future endpoint rotations transparent—only the DNS record changes.

This approach is **optional**; Temporal Cloud works without it. It simply streamlines configuration and operations. If you cannot use private DNS, refer to [our guide for updating the server and TLS settings on your clients](/cloud/connectivity#update-dns-or-clients-to-use-private-connectivity).

### Prerequisites

| Requirement                                           | Notes                                                                             |
| ----------------------------------------------------- | --------------------------------------------------------------------------------- |
| Google Cloud VPC Network with DNS enabled             | PSC endpoints and the DNS zone must live in (or be attached to) the same network. |
| Private Service Connect endpoint for Temporal Cloud   | Create an endpoint and reserve an internal IP in the namespace region             |
| Cloud DNS API enabled and roles/dns.admin permissions | Needed to create private zones and records.                                       |
| Namespace details                                     | Determines which hostname pattern you override (table below).                     |

### Choose the override domain and endpoint

| Temporal Cloud setup                       | Use this PHZ domain                | Example                                        |
| ------------------------------------------ | ---------------------------------- | ---------------------------------------------- |
| Single-region namespace with mTLS auth     | `<account>.tmprl.cloud`            | `payments.abcde.tmprl.cloud` ↔ `X.X.X.X`       |
| Single-region namespace with API-key auth  | `<cloud_provider>.api.temporal.io` | `us-central1.gcp.api.temporal.io` ↔ `X.X.X.X`  |
| Multi-region namespace | `region.tmprl.cloud`               | `gcp-us-central1.region.tmprl.cloud` ↔ `X.X.X.X` |

### Step-by-step instructions

#### 1. Collect your PSC endpoint IP address

```shell
