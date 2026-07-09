  - The list is grouped by cloud region. The Namespace endpoint will resolve to an IP from the group for the Namespace's active region.
- Workers and Temporal Clients connecting via the Namespace endpoint will connect to these stable IP addresses.
- Regional endpoints continue to work but resolve to dynamic IP addresses.
- For replicated Namespaces, the Stable IP corresponds to the Namespace's active region. During failover to a different region, DNS updates to point to a Stable IP in the new active region.

:::note

Stable IPs apply only to Namespace traffic, sometimes called the "data plane." The Temporal Cloud management plane, observability endpoints, and Web UI do not have stable public IP addresses.

:::

:::warning Stable IPs supersedes HA + Private Connectivity DNS

If you attach a public Connectivity Rule with Stable IPs to a Namespace that is also configured for [High Availability with Private Connectivity](/cloud/high-availability/ha-connectivity), the Namespace Endpoint resolves to a public Stable IP instead of to `<provider>-<region>.region.tmprl.cloud`. Stable IPs DNS behavior supersedes the regional DNS behavior that HA + Private Connectivity relies on, so the Namespace Endpoint's DNS resolution will not work in the way the Private Hosted Zone needs. Do not attach a Stable IPs public Connectivity Rule to a Namespace where you want HA + Private Connectivity to keep routing traffic over PrivateLink / PSC.

:::

### How to enable Stable IPs

Stable IPs is a setting on a public [Connectivity Rule](/cloud/connectivity#connectivity-rules). You enable it by creating (or updating) a public Connectivity Rule with Stable IPs enabled, then attaching that rule to the Namespaces that should resolve to Stable IPs.

:::note Creating a public Connectivity Rule with Stable IPs requires the Cloud Ops API

`tcld` does not currently support creating a public Connectivity Rule with Stable IPs enabled. Create the rule using either:

- The [Cloud Ops API](/ops) directly (HTTP or gRPC at `saas-api.tmprl.cloud`), or
- The generated client in the [`temporalio/cloud-api`](https://github.com/temporalio/cloud-api) repository.

Once the rule exists, you can attach it to a Namespace using any Connectivity Rule management interface: `tcld`, the Cloud Ops API, the `cloud-api` client, or the [Terraform provider](/cloud/terraform-provider). There is no Temporal Cloud UI option at this time.

:::

To enable Stable IPs:

1. Create a public Connectivity Rule with Stable IPs enabled via the Cloud Ops API or the `cloud-api` client. Only one public Connectivity Rule exists per account, so if you already have one, update or recreate it with Stable IPs enabled. The Cloud Ops API field is `enableStableIps` (boolean) on the `PublicConnectivityRule` message and requires Cloud Ops API `v0.15.0` or later. See [How to enable Stable IPs with curl](#how-to-enable-stable-ips-with-curl) below for a copy-pasteable example.
2. Attach the rule to your Namespace using any Connectivity Rule management interface — for example, `tcld namespace set-connectivity-rules`, the Cloud Ops API, the `cloud-api` client, or Terraform.
3. Retrieve the list of Stable IPs from the [public JSON file](/cloud/connectivity/ip-addresses#how-to-view-stable-ip-ranges).
4. Configure your firewall to allowlist the Stable IP ranges for your Namespace's region.
5. Ensure your Workers and Temporal Clients connect using the Namespace endpoint, not regional endpoints.

You can enable Stable IPs on new Namespaces at creation time or on existing Namespaces.

:::note DNS propagation

When enabling Stable IPs on an existing Namespace, Temporal updates DNS records to point the Namespace endpoint to Stable IPs. DNS propagation typically takes 5 to 15 minutes for AWS, but can take up to 60 minutes or longer if you have custom TTLs configured.

:::

#### How to enable Stable IPs with curl

If you cannot use `tcld` or Terraform, you can access the Cloud Ops API directly. The following procedure creates a public Connectivity Rule with Stable IPs enabled and attaches it to a Namespace.

All requests require two headers:

- `Authorization: Bearer $TEMPORAL_CLOUD_OPS_API_KEY`
- `temporal-cloud-api-version: v0.16.0` (or any version ≥ `v0.15.0`)

Base URL: `https://saas-api.tmprl.cloud`

Set up environment variables:

```bash
export TEMPORAL_CLOUD_OPS_API_KEY='<paste-api-key>'
export NS='<namespace>.<account>'   # The Cloud-side Namespace identifier, e.g. "myns.a1b2c3"
H_AUTH="Authorization: Bearer $TEMPORAL_CLOUD_OPS_API_KEY"
H_VER="temporal-cloud-api-version: v0.16.0"
```

**Step 1. Read the current Namespace spec and resource version.**

`UpdateNamespace` replaces the entire spec and requires the latest `resource_version`. Fetch them first:

```bash
curl -sS "https://saas-api.tmprl.cloud/cloud/namespaces/$NS" \
  -H "$H_AUTH" -H "$H_VER" | tee /tmp/ns.json | \
  jq '{resource_version: .namespace.resourceVersion, connectivity_rule_ids: .namespace.spec.connectivityRuleIds}'

RV=$(jq -r '.namespace.resourceVersion' /tmp/ns.json)
```

**Step 2. Create a public Connectivity Rule with Stable IPs enabled.**

```bash
curl -sS -X POST "https://saas-api.tmprl.cloud/cloud/connectivity-rules" \
  -H "$H_AUTH" -H "$H_VER" -H "Content-Type: application/json" \
  -d '{
        "spec": {
          "publicRule": { "enableStableIps": true }
        }
      }' | tee /tmp/cr.json

CR_ID=$(jq -r '.connectivityRuleId' /tmp/cr.json)
OP_ID=$(jq -r '.asyncOperation.id // .asyncOperation.operationId' /tmp/cr.json)
```

Field names follow proto3 JSON camelCase: `enable_stable_ips` becomes `enableStableIps`.

**Step 3. Wait for the create operation to reach a terminal state.**

```bash
curl -sS "https://saas-api.tmprl.cloud/cloud/operations/$OP_ID" \
  -H "$H_AUTH" -H "$H_VER" | jq '.asyncOperation.state'
```

Re-run until `state` is `FULFILLED` (the rule is now `ACTIVE`). Any `*_FAILED` state means you should stop and inspect the operation.

**Step 4. Attach the rule to the Namespace.**

`UpdateNamespace` posts the whole `NamespaceSpec` back. Update the spec from Step 1 by appending `$CR_ID` to `connectivityRuleIds`:

```bash
jq --arg id "$CR_ID" --arg rv "$RV" --arg ns "$NS" '
  {
    namespace: $ns,
    resourceVersion: $rv,
    spec: (.namespace.spec
           | .connectivityRuleIds = ((.connectivityRuleIds // []) + [$id]))
  }' /tmp/ns.json > /tmp/update.json

curl -sS -X POST "https://saas-api.tmprl.cloud/cloud/namespaces/$NS" \
  -H "$H_AUTH" -H "$H_VER" -H "Content-Type: application/json" \
  -d @/tmp/update.json | tee /tmp/update-resp.json
```

Poll the returned `asyncOperation` the same way as Step 3.

Take note of the following:

- The `namespace` in the URL is the Cloud-side Namespace identifier (for example, `myns.a1b2c3`), not the SDK gRPC hostname (`myns.a1b2c3.tmprl.cloud`). Strip the trailing `.tmprl.cloud`.
- Do not omit fields from `spec` in Step 4. Proto3 update is full-replace — any field left out will be cleared. Building the body from the GET response avoids surprises.
- A Namespace can have at most one public Connectivity Rule attached, and only one public rule exists per account. If `connectivityRuleIds` already references a public rule without Stable IPs, replace that entry instead of appending — you cannot create a second public rule.
- Stable IPs requires `temporal-cloud-api-version` of `v0.15.0` or later.

#### How to enable Stable IPs with gRPC

If you prefer to call the Cloud Ops API directly over gRPC (for example, with `grpcurl` or a generated client), the same flow uses the [CloudService](https://github.com/temporalio/api-cloud) gRPC API. Proto definitions live in [`temporal/api/cloud/cloudservice/v1/service.proto`](https://github.com/temporalio/api-cloud/blob/main/temporal/api/cloud/cloudservice/v1/service.proto) and [`temporal/api/cloud/connectivityrule/v1/message.proto`](https://github.com/temporalio/api-cloud/blob/main/temporal/api/cloud/connectivityrule/v1/message.proto).

- Endpoint: `saas-api.tmprl.cloud:443` (TLS required)
- Fully qualified service: `temporal.api.cloud.cloudservice.v1.CloudService`
- Required metadata on every call:
  - `authorization: Bearer $TEMPORAL_CLOUD_OPS_API_KEY`
  - `temporal-cloud-api-version: v0.16.0` (or any version ≥ `v0.15.0`)

The examples below use `grpcurl`. They assume you have a local checkout of [`temporalio/api-cloud`](https://github.com/temporalio/api-cloud) at `./api-cloud` and a `proto/` directory containing the standard `google/api/annotations.proto` and associated files.

Set up environment variables:

```bash
export TEMPORAL_CLOUD_OPS_API_KEY='<paste-api-key>'
export NS='<namespace>.<account>'   # The Cloud-side Namespace identifier, e.g. "myns.a1b2c3"
GRPC_HEADERS=(-H "authorization: Bearer $TEMPORAL_CLOUD_OPS_API_KEY" -H "temporal-cloud-api-version: v0.16.0")
PROTO_FLAGS=(-import-path ./api-cloud -import-path ./proto -proto temporal/api/cloud/cloudservice/v1/service.proto)
```

**Step 1. Read the current Namespace spec and resource version.**

```bash
grpcurl "${PROTO_FLAGS[@]}" "${GRPC_HEADERS[@]}" \
  -d "{\"namespace\": \"$NS\"}" \
  saas-api.tmprl.cloud:443 \
  temporal.api.cloud.cloudservice.v1.CloudService/GetNamespace | tee /tmp/ns.json

RV=$(jq -r '.namespace.resourceVersion' /tmp/ns.json)
```

**Step 2. Create a public Connectivity Rule with Stable IPs enabled.**

```bash
grpcurl "${PROTO_FLAGS[@]}" "${GRPC_HEADERS[@]}" \
  -d '{
        "spec": {
          "public_rule": { "enable_stable_ips": true }
        }
      }' \
  saas-api.tmprl.cloud:443 \
  temporal.api.cloud.cloudservice.v1.CloudService/CreateConnectivityRule | tee /tmp/cr.json

CR_ID=$(jq -r '.connectivityRuleId' /tmp/cr.json)
OP_ID=$(jq -r '.asyncOperation.id' /tmp/cr.json)
```

Field names in gRPC JSON requests can use either snake_case (proto field names) or camelCase — `grpcurl` accepts both. Responses come back in camelCase.

**Step 3. Wait for the create operation to reach a terminal state.**

```bash
grpcurl "${PROTO_FLAGS[@]}" "${GRPC_HEADERS[@]}" \
  -d "{\"async_operation_id\": \"$OP_ID\"}" \
  saas-api.tmprl.cloud:443 \
  temporal.api.cloud.cloudservice.v1.CloudService/GetAsyncOperation | jq '.asyncOperation.state'
```

Re-run until `state` is `FULFILLED` (the rule is now `ACTIVE`). Any `*_FAILED` state means you should stop and inspect the operation.

**Step 4. Attach the rule to the Namespace.**

`UpdateNamespace` posts the whole `NamespaceSpec` back. Update the spec from Step 1 by appending `$CR_ID` to `connectivity_rule_ids`:

```bash
jq --arg id "$CR_ID" --arg rv "$RV" --arg ns "$NS" '
  {
    namespace: $ns,
    resource_version: $rv,
    spec: (.namespace.spec
           | .connectivity_rule_ids = ((.connectivityRuleIds // []) + [$id]))
  }' /tmp/ns.json > /tmp/update.json

grpcurl "${PROTO_FLAGS[@]}" "${GRPC_HEADERS[@]}" \
  -d @ \
  saas-api.tmprl.cloud:443 \
  temporal.api.cloud.cloudservice.v1.CloudService/UpdateNamespace < /tmp/update.json | tee /tmp/update-resp.json
```

Poll the returned `asyncOperation` the same way as Step 3.

Take note of the following:

- The `namespace` field is the Cloud-side Namespace identifier (for example, `myns.a1b2c3`), not the SDK gRPC hostname (`myns.a1b2c3.tmprl.cloud`). Strip the trailing `.tmprl.cloud`.
- Do not omit fields from `spec` in Step 4. Proto3 update is full-replace — any field left out will be cleared. Building the body from the `GetNamespace` response avoids surprises.
- A Namespace can have at most one public Connectivity Rule attached, and only one public rule exists per account. If `connectivity_rule_ids` already references a public rule without Stable IPs, replace that entry instead of appending — you cannot create a second public rule.
- Stable IPs requires `temporal-cloud-api-version` of `v0.15.0` or later.
- Authentication uses Cloud API keys; mTLS client certificates are not accepted on `saas-api.tmprl.cloud`. The metadata key is `authorization` (lowercase), per the gRPC convention.

### How to view Stable IP ranges

The full list of Stable IP ranges is published as a public JSON file at:

**[https://docs.temporal.io/json/stable-ip-ranges-prod.json](https://docs.temporal.io/json/stable-ip-ranges-prod.json)**

Click the link to inspect the list in your browser, or copy the URL into your firewall tooling, a `curl`/`wget` script, or a Terraform `http` data source:

```
https://docs.temporal.io/json/stable-ip-ranges-prod.json
```

The file is publicly accessible without authentication and returns a JSON response grouped by cloud provider and region:

```json
{
  "all_stable_ip_ranges": [
    "34.195.80.228/32",
    "34.195.80.10/30",
    "44.235.214.171/32"
  ],
  "clouds": {
    "aws": {
      "regions": {
        "us-east-1": {
          "stable_ip_ranges": [
            "34.195.80.228/32",
            "34.195.80.10/30"
          ]
        },
        "us-west-2": {
          "stable_ip_ranges": [
            "44.235.214.171/32"
          ]
        }
      }
    },
    "gcp": {
      "regions": {
        ...
      }
    }
  }
}
```

:::note IP format

IP addresses are provided in IPv4 or IPv6 format with CIDR notation. At launch, Temporal uses predominantly `/32` ranges (single IP addresses). Each region typically contains approximately 6 IP addresses.

:::

### How to connect using Stable IPs

To connect to a Namespace with Stable IPs enabled:

1. **Use the Namespace endpoint**: Configure Workers and Temporal Clients to use the Namespace endpoint format: `<namespace>.<account>.tmprl.cloud:7233`
2. **Do not use Regional endpoints**: Regional endpoints (`<region>.<cloud>.api.temporal.io`) will route to the Namespace but resolve to dynamic IP addresses.
3. **Do not use PrivateLink**: PrivateLink endpoints do not resolve to Stable IPs. To use Stable IPs, connect over public endpoints.

Stable IPs work with both mTLS certificate-based authentication and API key authentication.

If your Workers run on the same cloud provider as your Namespace (for example, both on AWS), traffic stays on the cloud provider's backbone network and does not traverse the public internet, even when using public Stable IPs. AWS, GCP, and Azure all guarantee that traffic between locations on their networks never leaves their backbone.

### How to migrate to Stable IPs

When you enable Stable IPs on an existing Namespace:

**Workers using Namespace endpoints**:
- Existing connections continue uninterrupted
- DNS updates to point the Namespace endpoint to Stable IPs
- Existing connections remain connected to their current dynamic IP
- New connections automatically use Stable IPs after DNS propagates
- No Worker restart required

**Workers using Regional endpoints**:
- Existing connections continue uninterrupted
- To use Stable IPs, update Worker configuration to use the Namespace endpoint and restart Workers

**Workers using PrivateLink**:
- Existing connections continue uninterrupted through PrivateLink
- To use Stable IPs, update Worker configuration to use the Namespace endpoint and restart Workers
- Note: You cannot use both PrivateLink and Stable IPs simultaneously

**Connectivity Rules**: Stable IPs is enabled when the `enableStableIps` config is `true` on a public [Connectivity Rule](/cloud/connectivity#connectivity-rules). Every Namespace that should resolve to Stable IPs must have that public Connectivity Rule attached. Namespaces without the rule attached continue to resolve to dynamic IPs.

#### How to migrate from AWS PrivateLink to Stable IPs

If your Namespace is currently reached over AWS PrivateLink and protected by a private Connectivity Rule, the safe migration path is to add the public path while the private path is still working, verify, and then remove the private path. This applies whether your Namespace is single-region or replicated.

**Prerequisites:**

- Note your existing private (PrivateLink) Connectivity Rule ID — you'll keep it attached during the overlap window.
- Check whether your account already has a public Connectivity Rule. Only one is allowed per account; if one exists without Stable IPs enabled, you'll need to delete and recreate it (see [Permissions and limits](/cloud/connectivity#permissions-and-limits)).
- Confirm that the VPCs and security groups that host your Workers and Temporal Clients allow egress to the Stable IP ranges on port `443`. If your egress is currently locked down to the PrivateLink VPC endpoint, you must expand it first.

**Steps:**

1. **Allowlist Stable IPs in your firewall first.** Fetch the IP ranges for your Namespace's region from [https://docs.temporal.io/json/stable-ip-ranges-prod.json](https://docs.temporal.io/json/stable-ip-ranges-prod.json) and add them to your egress allowlist before changing anything else. If you skip this step, traffic will be lost.

2. **Create (or update) the account's public Connectivity Rule with Stable IPs enabled.** This step requires the [Cloud Ops API](#how-to-enable-stable-ips-with-curl) or the [`cloud-api` client](https://github.com/temporalio/cloud-api) — `tcld` does not currently support creating a public Connectivity Rule with Stable IPs.

   If you already have a public Connectivity Rule without Stable IPs, delete and recreate it — there is no in-place update flag, and creating a second public rule returns an error. Wait for the rule to reach `ACTIVE` before continuing.

3. **Attach both rules to the Namespace simultaneously.** Connectivity Rules attach as a set (full replace), so include the existing private rule ID and the new public rule ID in one call:

   ```bash
   tcld namespace set-connectivity-rules \
     --namespace "<namespace>.<account>" \
     --connectivity-rule-ids "<private-rule-id>" \
     --connectivity-rule-ids "<public-rule-id>"
   ```

   Workers continue to use PrivateLink at this point, because your private DNS still resolves the Namespace endpoint to the VPC endpoint. The public path is now *allowed* on Temporal's side but not yet *used*.

4. **Switch client DNS resolution from PrivateLink to public.** This is the actual cutover. Remove the private DNS override — Route 53 private hosted zone, `/etc/hosts`, or VPC DNS resolver rules — so that `<namespace>.<account>.tmprl.cloud` resolves through public DNS to a Stable IP. Restart Workers to drop existing PrivateLink connections and force re-resolution.

5. **Verify traffic is flowing over Stable IPs.** On a Worker host, run `dig <namespace>.<account>.tmprl.cloud` and confirm the answer is a Stable IP from the [published JSON list](https://docs.temporal.io/json/stable-ip-ranges-prod.json), not your VPC endpoint IP. Confirm Workers are polling and there are no `RESOURCE_EXHAUSTED` or connection errors in their logs.

6. **Detach the private Connectivity Rule.** Once you are confident all traffic is on the public path, remove the private rule by re-attaching only the public rule:

   ```bash
   tcld namespace set-connectivity-rules \
     --namespace "<namespace>.<account>" \
     --connectivity-rule-ids "<public-rule-id>"
   ```

7. **(Optional) Tear down the PrivateLink VPC endpoint** in AWS to stop incurring PrivateLink hourly and data-processing charges. Do not do this until step 6 has been stable for at least a few hours.

Take note of the following:

- Do not remove the private Connectivity Rule before step 4. If you detach the private rule while Workers are still resolving the Namespace endpoint to the PrivateLink VPC endpoint, Temporal Cloud will block those connections at the edge.
- A single connection uses one network path or the other. Workers connect over either PrivateLink or Stable IPs based on DNS resolution at connect time. There is no in-place switch without dropping the connection — that's why step 4 includes a Worker restart.
- Same-region traffic still stays on the AWS backbone over Stable IPs (since both your Worker and the Namespace are in AWS), so you do not lose the "does not traverse the public internet" property by moving off PrivateLink.
- TLS and SNI do not change. You are still hitting the Namespace endpoint (`<namespace>.<account>.tmprl.cloud`); only the IP it resolves to changes. mTLS and API key authentication continue to work unchanged.

### Changes to Stable IP ranges

Temporal does not intend to make changes to published Stable IP ranges. In the rare exception that a Stable IP range needs to be added to or removed from the list, Temporal will communicate via targeted communication to affected Temporal Cloud users and the [Temporal Cloud changelog](https://temporal.io/change-log), and will give ample time for users to update their firewalls with the changed IPs.

Temporal will never route traffic to IP addresses that are not listed in the API response.

### Pricing

Temporal Cloud does not charge additional fees for using Stable IPs.

### How to disable Stable IPs

You can disable Stable IPs on a Namespace by detaching the public Connectivity Rule from that Namespace. Temporal performs a DNS update to point the Namespace endpoint back to dynamic IP addresses.

Existing Worker connections are not interrupted. New Worker connections will no longer resolve to Stable IPs after DNS propagates.

---

## Workflow History Export

Workflow History Export allows users to export closed Workflow Histories from Temporal Cloud to cloud object storage (AWS S3 or GCP GCS), enabling:

- Compliance and audit trails of complete Event History data in [proto format](https://github.com/temporalio/api/blob/main/temporal/api/export/v1/message.proto)
- Analytics on Event History when ingested to the data platform of your choice

Workflow History Export in Temporal Cloud provides similar functionality as [Archival](/self-hosted-guide/archival) in a Self-Hosted Temporal Server.
Archival is not supported in Temporal Cloud.

Exports run hourly, beginning 10 minutes after the hour.
Allow up to 24 hours for a closed Workflow to appear in the exported file.
Delivery is guaranteed at least once.

## What's in the exported data {/* #exported-data */}

Each exported file contains one or more complete Workflow Execution histories serialized as protocol buffers using the [`WorkflowExecutions`](https://github.com/temporalio/api/blob/main/temporal/api/export/v1/message.proto) proto.

Each history is an ordered sequence of events that records everything that happened during a Workflow Execution:

- **Workflow configuration** - Input data, timeouts, Task Queue, retry policies, search attributes, and memo
- **Activity lifecycle** - Each Activity scheduled, started, completed, or failed/timed out, including inputs and results
- **Timers** - Timer starts and fires
- **Signals and Updates** - External Signals received and Update requests handled
- **Child Workflows** - Child Workflow starts and completions
- **Workflow result** - How the Workflow ended (completed, failed, timed out, terminated, canceled, or continued-as-new)

Search attributes in the export use your **user-defined names** (for example, `customerId`), not internal column names.

The export format is **protobuf binary**.
You must deserialize using the [proto schema](https://github.com/temporalio/api/blob/main/temporal/api/export/v1/message.proto) before the data is human-readable.

The following is a simplified JSON representation of what one Workflow Execution looks like after deserialization.
This example shows a Workflow that started, ran one Activity, and completed:

```json
{
  "items": [
    {
      "history": {
        "events": [
          {
            "eventId": "1",
            "eventTime": "2025-02-24T18:00:00Z",
            "eventType": "EVENT_TYPE_WORKFLOW_EXECUTION_STARTED",
            "workflowExecutionStartedEventAttributes": {
              "workflowType": { "name": "OrderWorkflow" },
              "taskQueue": { "name": "order-processing" },
              "input": { "payloads": ["...serialized input..."] },
              "workflowExecutionTimeout": "3600s",
              "searchAttributes": {
                "indexedFields": {
                  "customerId": { "data": "\"customer-42\"" },
                  "orderType": { "data": "\"standard\"" }
                }
              }
            }
          },
          {
            "eventId": "2",
            "eventTime": "2025-02-24T18:00:00Z",
            "eventType": "EVENT_TYPE_WORKFLOW_TASK_SCHEDULED"
          },
          {
            "eventId": "3",
            "eventTime": "2025-02-24T18:00:01Z",
            "eventType": "EVENT_TYPE_ACTIVITY_TASK_SCHEDULED",
            "activityTaskScheduledEventAttributes": {
              "activityType": { "name": "ChargeCustomer" },
              "taskQueue": { "name": "order-processing" },
              "input": { "payloads": ["...serialized input..."] },
              "scheduleToCloseTimeout": "300s",
              "startToCloseTimeout": "60s"
            }
          },
          {
            "eventId": "4",
            "eventTime": "2025-02-24T18:00:02Z",
            "eventType": "EVENT_TYPE_ACTIVITY_TASK_STARTED"
          },
          {
            "eventId": "5",
            "eventTime": "2025-02-24T18:00:03Z",
            "eventType": "EVENT_TYPE_ACTIVITY_TASK_COMPLETED",
            "activityTaskCompletedEventAttributes": {
              "result": { "payloads": ["...serialized result..."] }
            }
          },
          {
            "eventId": "6",
            "eventTime": "2025-02-24T18:00:03Z",
            "eventType": "EVENT_TYPE_WORKFLOW_TASK_COMPLETED"
          },
          {
            "eventId": "7",
            "eventTime": "2025-02-24T18:00:03Z",
            "eventType": "EVENT_TYPE_WORKFLOW_EXECUTION_COMPLETED",
            "workflowExecutionCompletedEventAttributes": {
