1. Select **Save**.

**Update permissions for multiple users within a single Namespace:**

1. In Temporal Web UI, select **Settings** in the left portion of the window.
1. On the **Settings** page in the **Users** tab, select the user.
1. On the user profile page, select **Edit User**.
1. On the **Edit User** page in **Namespace permissions**, change the permissions for one or more Namespaces.
1. Select **Save**.

</TabItem>

<TabItem value="update-perms-tcld" label="tcld">

Use the [`tcld user set-namespace-permissions`](/cloud/tcld/user/#set-namespace-permissions) command. Specify the user
by email or ID and one or more Namespace permissions.

Each permission value must be in the format `namespace=permission-type`.

Available Namespace permissions: `Admin` | `Write` | `Read`.

```command
tcld user set-namespace-permissions --user-email <user@example.com> --namespace-permission <namespace>=<permission>
```

You can set multiple Namespace permissions in a single request:

```command
tcld user set-namespace-permissions --user-email <user@example.com> \
  --namespace-permission ns1=Admin \
  --namespace-permission ns2=Write
```

</TabItem>

<TabItem value="update-perms-api" label="Cloud Ops API">

Use the [SetUserNamespaceAccess](https://saas-api.tmprl.cloud/docs/httpapi.html#tag/users) endpoint to set a user's
permission for a specific Namespace.

```
POST /cloud/namespaces/{namespace}/users/{userId}/access
```

Set the `access.permission` field to the desired permission.

Available permissions: `PERMISSION_ADMIN` | `PERMISSION_WRITE` | `PERMISSION_READ`.

</TabItem>

</Tabs>

## Delete a user from your Temporal Cloud account {/* #delete-users */}

With Account Owner or Global Admin privileges, you can delete a user from your Temporal Cloud account.

<Tabs>

<TabItem value="delete-user-webui" label="Web UI">

1. In Temporal Web UI, select **Settings** in the left portion of the window.
1. On the **Settings** page, find the user and, on the right end of the row, select **Delete**.
1. In the **Delete User** dialog, select **Delete**.

You can also delete a user in two other ways in Web UI:

- User profile page: Select the down arrow next to **Edit User** and then select **Delete**.
- **Edit User** page: Select **Delete User**.

</TabItem>

<TabItem value="delete-user-tcld" label="tcld">

Use the [`tcld user delete`](/cloud/tcld/user/#delete) command. Specify the user by email or ID.

```command
tcld user delete --user-email <user@example.com>
```

You can also identify the user by ID:

```command
tcld user delete --user-id <user-id>
```

</TabItem>

<TabItem value="delete-user-api" label="Cloud Ops API">

Use the [DeleteUser](https://saas-api.tmprl.cloud/docs/httpapi.html#tag/users) endpoint to remove a user from your
account.

```
DELETE /cloud/users/{userId}
```

</TabItem>

</Tabs>

---

## Enable and manage High Availability

You can enable [High Availability](/cloud/high-availability) features for a new or existing Namespace by adding a
replica. When you add a replica, Temporal Cloud begins asynchronously replicating ongoing and existing Workflow
Executions.

 The replica region must be on the same continent as the primary region. Because of that, not all replication options are available in all Temporal Cloud regions. See the [Service regions](/cloud/regions) page for the supported replica regions for each active region.

Using private network connectivity with a HA namespace requires extra setup. See
[Connectivity for HA](/cloud/high-availability/ha-connectivity).

There are charges associated with Replication and enabling High Availability features. For pricing details, visit
Temporal Cloud's [Pricing](/cloud/pricing) page.

## Create a Namespace with High Availability features {/* #create */}

To create a new Namespace with High Availability features, you can use the Temporal Cloud UI or the tcld command line
utility.

<Tabs>

<TabItem value="webui" label="Web UI">

    1. Visit Temporal Cloud in your Web browser.
    1. During Namespace creation, specify the primary [region](/cloud/regions) for the Namespace.
    1. Select "Add a replica".
    1. Choose the [region](/cloud/regions) for the replica.

    The web interface will present an estimated time for replication to complete.
    This time is based on your selection and the size and scale of the Workflows in your Namespace.

</TabItem>

<TabItem value="tcldcli" label="tcld">

At the command line, enter:

```
tcld namespace create \
   --namespace <namespace_id>.<account_id> \
   --region <primary_region> \
   --region <replica_region>
```

Specify the [region codes](/cloud/regions) as arguments to the two `--region` flags.

If using API key authentication with the `--api-key` flag, you must add it directly after the tcld command and before
`namespace create`.

</TabItem>

</Tabs>

Temporal Cloud sends an email alert to all Namespace Admins once your Namespace replica is ready for use.

## Add High Availability to an existing Namespace {/* #upgrade */}

A replica can be added after a namespace has already been created.

<Tabs>

<TabItem value="webui" label="Web UI">

1. Visit Temporal Cloud Namespaces in your Web browser.
1. Navigate to the Namespace details page.
1. Select the “Add a replica” button.
1. Choose the [region](/cloud/regions) for the replica.

The web interface will present an estimated time for replication to complete. This time is based on your selection and
the size and scale of the Workflows in your Namespace.

Temporal Cloud sends an email alert to all Namespace Admins once your Namespace replica is ready for use.

</TabItem>

<TabItem value="tcldcli" label="tcld">

At the command line, enter:

```
tcld namespace add-region \
   --namespace <namespace_id>.<account_id> \
   --region <replica_region>
```

Specify the region name (for example, `us-east-1`) of the region where you want to create the replica as an argument to the
`--region` flag. See [Regions](/cloud/regions) for available region names.

If using API key authentication with the `--api-key` flag, you must add it directly after the tcld command and before
`namespace add-region`.

Temporal Cloud sends an email alert once your Namespace is ready for use.

</TabItem>

</Tabs>

## Change a replica location {/* #changing */}

Temporal Cloud can't change replica locations directly. To change a replica's location, you need to remove the replica
and add a new one.

:::caution

We discourage changing the location of your replica for deployed applications, except under exceptional circumstances.
If you remove your replica, you lose the availability guarantees of the Namespace, and it can take time to add another
replica.

If you remove a replica from a region, you must wait seven days before you can re-enable High Availability (HA) in that
same location. During this period, you may add a replica to a different region, provided you have not had one
there within the last seven days.

:::

Follow these steps to change the replica location:

1. [Remove your replica](#disable). This disables High Availability for your Namespace.
2. [Add a new replica](#upgrade) to your Namespace.

You will receive an email alert once your Namespace is ready for use.

## Change the forwarding behavior {/* #change-forwarding-behavior */}

Requests that reach the passive replica can be [forwarded](/cloud/high-availability/#request-forwarding) to the active region, and responses sent back to the Worker or Client. The `disablePassivePollerForwarding` Namespace setting controls this behavior for Worker poll traffic.

With `disablePassivePollerForwarding` enabled, Worker polls that reach a passive replica are not forwarded, and these Workers do not execute Workflows or Activities. Workers connected to such a passive replica receive a `NamespaceNotActive` error on poll requests. These Workers stay connected and will start executing Workflows and Activities if the replica becomes active.

Client APIs (Start, Signal, Cancel, Terminate, Query, and the equivalent Activity APIs) are forwarded to the active region regardless of this setting, with responses sent back to the Client.

Same-region replicas are not affected by this setting.

:::info

To see which endpoints route to which replica, see [How requests reach the replica](/cloud/high-availability/ha-connectivity#how-requests-reach-the-replica).

:::

`disablePassivePollerForwarding` can be set through the [Cloud Ops API](/ops), the [cloud-api SDK](https://github.com/temporalio/cloud-sdk-go), or the [`temporal cloud` CLI extension](/cli/cloud). Use one of the recipes below.

### Set the forwarding behavior with the `temporal cloud` CLI {/* #set-forwarding-cli */}

Use the [`temporal cloud namespace ha update`](/cli/command-reference/cloud/namespace#ha-update) command:

```bash
temporal cloud namespace ha update \
    --namespace <namespace>.<account> \
    --disable-passive-poller-forwarding true
```

Set the flag to `false` to re-enable forwarding.

### Set the forwarding behavior with the Cloud Ops API {/* #set-forwarding-curl */}

This recipe uses `curl` against the Cloud Ops API. Because `UpdateNamespace` replaces the entire Namespace spec, it fetches the current spec, merges in the new value, and posts it back with the current `resourceVersion`. The `jq` filter preserves any other High Availability fields you have set (such as `disableManagedFailover`).

Set the Cloud Ops API key and Namespace ID. The Namespace ID is in `<namespace>.<account>` format (the full identifier shown in the Cloud Web UI):

```bash
export TEMPORAL_CLOUD_OPS_API_KEY='<your-api-key>'
export NS='<namespace>.<account>'
```

Fetch the current spec:

```bash
curl -sS "https://saas-api.tmprl.cloud/cloud/namespaces/$NS" \
  -H "Authorization: Bearer $TEMPORAL_CLOUD_OPS_API_KEY" > /tmp/ns.json
```

Build the update payload. Set the value to `true` to disable forwarding, or `false` to restore the default:

```bash
jq --arg rv "$(jq -r '.namespace.resourceVersion' /tmp/ns.json)" '{
  spec: (.namespace.spec
    | .highAvailability = ((.highAvailability // {}) + {disablePassivePollerForwarding: true})),
  resourceVersion: $rv
}' /tmp/ns.json > /tmp/ns-update.json
```

Post the update. The response contains an `asyncOperation` ID; the change is complete when `GET /cloud/operations/<id>` reports a terminal state.

```bash
curl -sS -X POST "https://saas-api.tmprl.cloud/cloud/namespaces/$NS" \
  -H "Authorization: Bearer $TEMPORAL_CLOUD_OPS_API_KEY" \
  -H "Content-Type: application/json" \
  -d @/tmp/ns-update.json
```

Verify the current value:

```bash
curl -sS "https://saas-api.tmprl.cloud/cloud/namespaces/$NS" \
  -H "Authorization: Bearer $TEMPORAL_CLOUD_OPS_API_KEY" \
  | jq '.namespace.spec.highAvailability.disablePassivePollerForwarding'
```

A result of `null` means the field has never been set, which is equivalent to `false` — proto3 JSON omits default-`false` values from responses.

## Enable or disable automatic failovers {/* #automatic-failovers */}

When a Temporal Cloud Namespace has a replica in a different region or cloud, Temporal Cloud automatically fails over the Namespace to its replica in the event of an outage. _This is the recommended and default option._

If you prefer to disable automatic failovers and handle your own failovers, follow these instructions:

:::warning Disabling automatic failovers voids Temporal's RTO

With automatic failovers disabled, Temporal Cloud cannot fail your Namespace over to its replica during an outage. You take responsibility for detecting outages and [triggering a failover](/cloud/high-availability/failovers/manage#trigger-failover) yourself. Temporal's [20-minute RTO](/cloud/rpo-rto) does not apply while this setting is disabled.

:::

<Tabs>

<TabItem value="webui" label="Web UI">

1. Navigate to the Namespace detail page in Temporal Cloud.
1. Choose the "Disable Temporal-initiated failovers" option.

</TabItem>

<TabItem value="tcldcli" label="tcld">

To disable automatic failovers, run the following command in your terminal:

```
tcld namespace update-high-availability \
    --namespace <namespace_id>.<account_id> \
    --disable-auto-failover=true
```

If using API key authentication with the `--api-key` flag, you must add it directly after the tcld command and before
`namespace update-high-availability`.

</TabItem>

</Tabs>

To restore the default behavior, unselect the option in the Web UI or change `true` to `false` in the CLI command.

:::note Automatic failovers are always enabled for Same-region Replication

This setting applies only to Multi-region and Multi-cloud Replication. You cannot disable automatic failovers for a [Same-region Replication](/cloud/high-availability#same-region-replication) Namespace, because same-region failovers between cells are always managed by Temporal.

:::

## Disable High Availability (remove a replica) {/* #disable */}

To disable High Availability features on a Namespace, remove the replica from that Namespace. Removing a replica
disables all High Availability features:

- Discontinues replication of the Workflows in the Namespace.
- Disables the Namespace's ability to trigger a failover to a different region or cloud.
- Ends High Availability charges.

:::caution

After removing a Namespace's replica, you cannot add a new replica to that same region for seven days.
During that time, you can still add a replica to any other region.

:::

Follow these steps to remove a replica from a Namespace:

<Tabs>

<TabItem value="webui" label="Web UI">

1. Navigate to the Namespace details page in Temporal Cloud
1. Select the option to "Remove Replica" on the "Region" card.

</TabItem>

<TabItem value="tcldcli" label="tcld">

Run the following command to remove the replica:

```
tcld namespace delete-region \
    --api-key <api_key> \
    --namespace <namespace_id>.<account_id> \
    --region <replica_region_name>
```

See [Regions](/cloud/regions) for available region names.

</TabItem>

</Tabs>

---

## Failovers

When a Namespace with [High Availability](/cloud/high-availability) is disrupted by an outage, Temporal Cloud can fail
over the Namespace from the primary to the replica. This lets in-flight Workflow Executions continue, new Workflow
Executions start, and closed Workflow Executions be inspected, all with minimal interruptions or data loss.

Returning control from the replica to the primary is called a <ToolTipTerm term="failback" />. After an automatic
failover, Temporal automatically fails back to the original region once it is healthy, unless you
[opt out](/cloud/high-availability/failovers/manage#after-an-automatic-failover). See
[Failbacks](/cloud/high-availability/failovers/manage#failbacks) for details.

## Automatic failover

Temporal Cloud offers managed outage detection and failover to all Namespaces that use High Availability.
These automatic failovers keep your Namespace available without manual intervention. Temporal aims to both detect the outage and complete a failover in minutes from when the outage began,
according to the stated [Recovery Time Objective (RTO)](/cloud/rpo-rto).

After an automatic failover, the Namespace will have a replica in its original region. Once the original region is
healthy again, Temporal Cloud automatically performs a [failback](/cloud/high-availability/failovers/manage#failbacks),
moving the Namespace back to its original region.

<CaptionedImage
  src="/img/cloud/high-availability/failover.png"
  title="On failover, the replica becomes active and the Namespace endpoint directs access to it."
/>

To opt out of automatic failovers and their RTO, you can
[disable automatic failovers](/cloud/high-availability/enable#automatic-failovers).

### Conditions that trigger an automatic failover

While the failover operation itself usually completes in seconds, the bulk of the Recovery Time in an outage is spent
detecting the disruption and deciding to trigger a failover. See [The failover process](#failover-process) for a
detailed breakdown.

Temporal Cloud runs automated Workflows that detect outages and trigger failovers. These Workflows continuously monitor
the health of Temporal Cloud in every region and every cell.

If any of the monitored conditions are failing for too long, Temporal Cloud automatically triggers a failover on any
Namespaces with High Availability that have a healthy replica.

Temporal's on-call engineers may also trigger a failover at their discretion, for example, if they see early signs of a
regional outage.

:::info

The following list gives a general idea of the conditions that trigger an automatic failover. This is not an
exhaustive list, and it may change over time.

:::

- Whether Temporal Cloud's services in the cell are reachable from the Control Plane.
- The average latency of inbound RPC calls (excluding long-polling APIs) to Temporal services in the cell.
- The percentage of inbound RPC calls that returned errors related to server health.
- The average latency of calls from Temporal Cloud's services in the cell to its persistence layer.
- The percentage of calls to the persistence layer that returned errors related to persistence health.

## Manual failover

You can also [manually trigger a failover](/cloud/high-availability/failovers/manage#trigger-failover) based on your own
monitoring or for failover testing.

Most Namespaces with High Availability are well-served by automatic failovers. The cases where a manual failover
is warranted are:

- **Testing failover or migrating to a new region.** A manual failover is the standard way to exercise your failover
  process with your Clients and Workers, or to move a Namespace to a different region.
- **An outage that affects only your systems.** If an outage is contained to your application, Workers, or other
  infrastructure, and Temporal Cloud is not affected, Temporal will not initiate a failover on your behalf. Detect the
  outage with your own monitoring and trigger a failover yourself.
- **Failing over more aggressively during a regional outage.** Even with automatic failovers enabled, you can
  trigger a failover yourself if you detect a regional outage before Temporal does. Whichever failover happens first
  takes effect, and the later one is a no-op. A user-triggered failover does not conflict with Temporal's automatic
  failover.

:::note Same-region Replication

Manual failovers apply only to Multi-region and Multi-cloud Replication. A [Same-region Replication](/cloud/high-availability#same-region-replication) Namespace fails over automatically between cells and cannot be failed over manually or have its automatic failovers disabled.

:::

## The failover process {/* #failover-process */}

The failover process is the same whether it is triggered automatically by Temporal or manually by a user.

1. **During normal operation**, the primary asynchronously replicates data to the replica, keeping them in sync.
2. **A failover is triggered.** For automatic failovers, the majority of time is spent on outage detection. Temporal's
   automated health checks must confirm the disruption before initiating a failover. For the overall timing target, see
   the [Recovery Time Objective (RTO)](/cloud/rpo-rto).
3. **The Namespace becomes active in the replica's region.**
   1. Temporal Cloud first attempts a _graceful failover_: it pauses traffic, drains in-flight replication, and switches
      to the replica with no data conflicts.
   2. If the graceful attempt does not complete within 10 seconds, Temporal Cloud falls back to a _forced failover_,
      which immediately activates the replica. In a forced failover, any events not yet replicated undergo
      [conflict resolution](#conflict-resolution) once the original region comes back.
   3. This hybrid strategy balances consistency and availability. During the switch, Workflow operations are briefly
      paused, and Temporal Cloud returns a retryable "Service unavailable" error to SDKs.

4. **The Namespace Endpoint re-routes to the active region.** This DNS change can take a few minutes to fully propagate
   to all Clients and Workers. If your application has an extremely demanding Recovery Time, you can eliminate this
   stage by connecting through a [Regional Endpoint](/cloud/high-availability/ha-connectivity#regional-endpoint) instead
   of the Namespace Endpoint.
5. **Failback.** If the failover was triggered by Temporal, Temporal automatically triggers a failback to the original
   region once the region is healthy. If the failover was triggered by a user, the Namespace continues as-is until a
   user triggers another failover. See [failback options](/cloud/high-availability/failovers/manage#failbacks) for
   details.

## Post-failover events {/* #post-failover-events */}

After any failover, whether triggered by you or by Temporal, an event appears in both the [Temporal Cloud Web UI](https://cloud.temporal.io/namespaces) (on the Namespace detail page) and in your audit logs. The audit log entry uses the `"operation": "FailoverNamespace"` event. Temporal Cloud [notifies you via email](/cloud/notifications#admin-notifications) whenever a failover occurs.

After an automatic failover, Temporal automatically fails back to the original region once the region is healthy, unless you [opt out](/cloud/high-availability/failovers/manage#after-an-automatic-failover). After a user-triggered failover, the Namespace stays in the replica region until a user triggers another failover. See [failback options](/cloud/high-availability/failovers/manage#failbacks) for details.

## Split-brain scenario

At any time, only the primary or the replica should be active. However, if a network partition separates the two
regions, the regions cannot communicate with each other. If you promote the replica to active during a network
partition, both regions will be active simultaneously, accepting writes independently. This is known as a split-brain
scenario.

When the network partition resolves and the regions can communicate again, Temporal's
[conflict resolution](#conflict-resolution) process reconciles the divergent histories and determines which region
remains active.

## Conflict resolution {/* #conflict-resolution */}

Namespaces with replicas rely on asynchronous event replication. Updates made to the primary may not immediately be
reflected in the replica due to <ToolTipTerm term="replication lag" />, particularly during failovers. In the event of a
non-graceful failover, replication lag may cause a temporary setback in Workflow progress.

Namespaces that are not replicated can be configured to provide _at-most-once_ semantics for Activity execution when a
retry policy's [maximum attempts](https://docs.temporal.io/retry-policies#maximum-attempts) is set to 0. High
Availability Namespaces provide _at-least-once_ semantics for execution of Activities. Completed Activities _may_ be
re-dispatched in a newly active Namespace, leading to repeated executions.

When a Workflow Execution is updated in a newly active replica following a failover, events from the previously active
Namespace that arrive after the failover cannot be directly applied. At this point, Temporal Cloud has forked the Event
History.

After failover, Temporal Cloud creates a new branch history for execution and begins its <ToolTipTerm term="conflict resolution" /> process. The Temporal Service ensures that Event Histories remain valid and are replayable by SDKs post-failover or after conflict resolution.

---

## Manage failovers

## Trigger a failover {/* #trigger-failover */}

You can trigger a failover manually using the Temporal Cloud Web UI, the tcld CLI, or the Cloud Ops API.

Manual failovers apply only to Multi-region and Multi-cloud Replication. A
[Same-region Replication](/cloud/high-availability#same-region-replication) Namespace fails over automatically between
cells and cannot be failed over manually.

:::warning Check your replication lag

Always check the <ToolTipTerm term="replication lag" /> before initiating a failover. A forced failover when there is a
significant replication lag has a higher likelihood of rolling back Workflow progress.

:::

<Tabs>

<TabItem value="webui" label="Web UI">

1. Visit the [Namespace page](https://cloud.temporal.io/namespaces) on the Temporal Cloud Web UI.
1. Navigate to your Namespace details page and select the **Trigger a failover** option from the menu.
1. Confirm your action. After confirmation, Temporal initiates the failover.

</TabItem>

<TabItem value="tcldcli" label="tcld">

To manually trigger a failover, run the following command in your terminal:

```
tcld namespace failover \
    --namespace <namespace_id>.<account_id> \
    --region <target_region>
```

The `<target_region>` must be the name of a region (example: `us-east-1`) where the Namespace has a replica that is
ready to be failed over to (replica state is `Activated`).

If using API key authentication with the `--api-key` flag, you must add it directly after the tcld command and before
`namespace failover`.

</TabItem>

<TabItem value="ops-api" label="Cloud Ops API">

You can trigger a failover programmatically using the [Cloud Ops API](/ops). The API is available via both HTTP and
gRPC.

**Using HTTP**

Send a POST request to the
[`FailoverNamespaceRegion`](https://saas-api.tmprl.cloud/docs/httpapi.html#tag/high-availability/POST/cloud/namespaces/{namespace}/failover-region)
endpoint:

```
POST https://saas-api.tmprl.cloud/cloud/namespaces/<namespace>/failover-region
```

Request body:

```json
{
  "region": "<target_region>",
  "asyncOperationId": "<optional_async_operation_id>"
