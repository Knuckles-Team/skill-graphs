
### Workflow execution latency

To monitor end-to-end Workflow execution time (not just the service API latency above), use the workflow schedule-to-close latency metrics:

- [temporal\_cloud\_v1\_workflow\_schedule\_to\_close\_latency\_p50](/cloud/metrics/openmetrics/metrics-reference#temporal_cloud_v1_workflow_schedule_to_close_latency_p50)
- [temporal\_cloud\_v1\_workflow\_schedule\_to\_close\_latency\_p95](/cloud/metrics/openmetrics/metrics-reference#temporal_cloud_v1_workflow_schedule_to_close_latency_p95)
- [temporal\_cloud\_v1\_workflow\_schedule\_to\_close\_latency\_p99](/cloud/metrics/openmetrics/metrics-reference#temporal_cloud_v1_workflow_schedule_to_close_latency_p99)

These measure the time from when a Workflow is scheduled until it closes, including all Activity execution time. A sudden increase may indicate Worker capacity issues, downstream service degradation, or retry storms.

## Monitor Temporal Service errors

Check for Temporal Service gRPC API errors.
Note that Service API errors are not equivalent to guarantees mentioned in the [Temporal Cloud SLA](/cloud/sla).

### Reference Metrics

- [temporal\_cloud\_v1\_service\_error\_count](/cloud/metrics/openmetrics/metrics-reference#temporal_cloud_v1_service_error_count)
- [temporal\_cloud\_v1\_service\_request\_count](/cloud/metrics/openmetrics/metrics-reference#temporal_cloud_v1_service_request_count)

### Prometheus Query for this Metric

Measure your daily average success rate over 10-minute windows.

OpenMetrics v1 metrics are pre-computed rates. Use `sum()` to aggregate across dimensions rather than `increase()` or `rate()`.

```
avg_over_time((
    (
        (
            sum(temporal_cloud_v1_service_request_count{temporal_namespace=~"$namespace", operation=~"StartWorkflowExecution|SignalWorkflowExecution|SignalWithStartWorkflowExecution|RequestCancelWorkflowExecution|TerminateWorkflowExecution"})
            -
            sum(temporal_cloud_v1_service_error_count{temporal_namespace=~"$namespace", operation=~"StartWorkflowExecution|SignalWorkflowExecution|SignalWithStartWorkflowExecution|RequestCancelWorkflowExecution|TerminateWorkflowExecution"})
        )
        /
        sum(temporal_cloud_v1_service_request_count{temporal_namespace=~"$namespace", operation=~"StartWorkflowExecution|SignalWorkflowExecution|SignalWithStartWorkflowExecution|RequestCancelWorkflowExecution|TerminateWorkflowExecution"})
    )

    or vector(1)

    )[1d:1m])
```

## Detecting Activity and Workflow Failures

The metrics `temporal_cloud_v1_activity_fail_count` and `temporal_cloud_v1_workflow_failed_count` together provide failure detection for Temporal applications. These metrics work in tandem to give you both granular component-level visibility and high-level workflow health insights.

### Activity failure cascade

If not using infinite retry policies, Activity failures can lead to Workflow failures:

```
Activity Failure --> Retry Logic --> More Activity Failures --> Workflow Decision --> Potential Workflow Failure
```

Activity failures are often recoverable and expected. Workflow failures represent terminal states requiring immediate attention.
A spike in activity failures may precede workflow failures.
Generally Temporal recommends that Workflows should be designed to always succeed. If an Activity fails more than its retry policy allows, we suggest having the Workflow handle Activity failure and take action to notify a human to take corrective action or be aware of the error.

### Ratio-based monitoring

#### Failure conversion rate

Monitor the ratio of workflow failures to activity failures:

```
workflow_failure_rate = temporal_cloud_v1_workflow_failed_count / temporal_cloud_v1_activity_fail_count
```

What to watch for:
- High ratio (greater than 0.1): Poor error handling - activities failing are causing workflow failures
- Low ratio (less than 0.01): Good resilience - activities fail but workflows recover
- Sudden spikes: May indicate systematic issues

#### Activity success rate

```
activity_success_rate = temporal_cloud_v1_activity_success_count / (temporal_cloud_v1_activity_success_count + temporal_cloud_v1_activity_fail_count)
```

Target: >95% for most applications. Lower success rate can be a sign of system troubles.
See also:
- [Crafting an Error Handling Strategy](https://learn.temporal.io/courses/errstrat/)
- [Temporal Failures reference](/references/failures)
- [Detecting Workflow failures](/encyclopedia/detecting-workflow-failures)

## Monitor replication lag for Namespaces with High Availability features

Replication lag refers to the transmission delay of Workflow updates and history events from the primary Namespace to the replica.
Always check the [metric replication lag](/cloud/metrics/openmetrics/metrics-reference#temporal_cloud_v1_replication_lag_p99) before initiating a failover.
A forced failover when there is a large replication lag has a higher likelihood of rolling back Workflow progress.

**Who owns the replication lag?**
Temporal owns replication lag.

**What guarantees are available?**
There is no SLA for replication lag.
Temporal recommends that customers do not trigger failovers except for testing or emergency situations.
High Availability feature's four-9 guarantee SLA means Temporal will handle failovers and ensure high availability.
Temporal also monitors replication lag.
Customers who decide to trigger failovers should look at this metric before moving forward.

**If the lag is high, what should you do?**
We don't expect users to failover.
Please contact Temporal support if you feel you have a pressing need.

**Where can you read more?**
See [operations and metrics](/cloud/high-availability) for Namespaces with High Availability features.

### Reference Metrics

- [temporal\_cloud\_v1\_replication\_lag\_p99](/cloud/metrics/openmetrics/metrics-reference#temporal_cloud_v1_replication_lag_p99)
- [temporal\_cloud\_v1\_replication\_lag\_p95](/cloud/metrics/openmetrics/metrics-reference#temporal_cloud_v1_replication_lag_p95)
- [temporal\_cloud\_v1\_replication\_lag\_p50](/cloud/metrics/openmetrics/metrics-reference#temporal_cloud_v1_replication_lag_p50)

## Monitoring Trends Against Limits {/* #rps-aps-rate-limits */}

Tracking trends against your account limits is the most important throttling signal to monitor. Unlike [Resource Exhaustion](#detecting-resource-exhaustion), which usually self-heals through retries, hitting a limit slows or stalls progress until the workload backs off or your capacity is increased.

The set of [limit metrics](/cloud/metrics/openmetrics/metrics-reference#limit-metrics) provide a time series of values for limits. Use these
metrics with their corresponding count metrics to monitor general trends against limits and set alerts when limits are exceeded. Use the corresponding throttle metrics
to determine the severity of any active rate limiting.
| Limit Metric | Count Metric | Throttle Metric |
| ------------ | ------------ | --------------- |
| `temporal_cloud_v1_action_limit` | `temporal_cloud_v1_total_action_count` | `temporal_cloud_v1_total_action_throttled_count` |
| `temporal_cloud_v1_service_request_limit` | `temporal_cloud_v1_service_request_count` | `temporal_cloud_v1_service_request_throttled_count` |
| `temporal_cloud_v1_operations_limit` | `temporal_cloud_v1_operations_count` | `temporal_cloud_v1_operations_throttled_count` |

### On-demand envelope limits

For Namespaces using provisioned capacity, the following metrics show what your limits would be under on-demand mode.
Compare these against your current provisioned limits to evaluate capacity mode choices:

| On-Demand Envelope Metric | Equivalent Limit Metric |
| ------------------------- | ----------------------- |
| `temporal_cloud_v1_action_on_demand_envelope_limit` | `temporal_cloud_v1_action_limit` |
| `temporal_cloud_v1_operations_on_demand_envelope_limit` | `temporal_cloud_v1_operations_limit` |
| `temporal_cloud_v1_service_request_on_demand_envelope_limit` | `temporal_cloud_v1_service_request_limit` |

For Namespaces already in on-demand mode, these metrics track the same values as their equivalent limit metrics.

The [Grafana dashboard example](https://github.com/grafana/jsonnet-libs/blob/master/temporal-mixin/dashboards/temporal-overview.json) includes a Usage & Quotas section
that creates demo charts for these limits and count metrics respectively.

The limit metrics, throttle metrics, and count metrics are already directly comparable as per second rates. Keep in mind that each `count` metric is represented as a per second rate averaged
over each minute. For example, to get the total count of Actions, you must multiply this metric by 60.
When setting alerts against limits, consider if your workload is spiky or sensitive to throttling (e.g. does latency matter?). If your workload is sensitive, consider alerting
for `temporal_cloud_v1_total_action_count` at a 50% threshold of the `temporal_cloud_v1_action_limit`. If your workload is not sensitive, consider an alert at 90% of this threshold
or directly when throttling is detected as a value greater than zero for `temporal_cloud_v1_total_action_throttled_count`. This logic can also be used to automatically scale [Temporal
Resource Units](/cloud/capacity-modes#provisioned-capacity) up or down as needed. Some workloads choose to exceed limits and accept throttling because they are not latency sensitive.

### Why does throttling occur when count metrics stay below the limit?

For spiky workloads, the throttle metric can be non-zero even though the count metric never rises above the limit. This looks contradictory, but both values are correct. They describe the workload at different time resolutions.

Count and limit metrics are per-second rates **averaged over a 1-minute window** (see [Metric conventions](/cloud/metrics/openmetrics/metrics-reference#metric-types)). A short burst is smoothed across all 60 seconds, so the count metric can sit well below the limit even though the instantaneous request rate exceeded it and triggered throttling. The throttle metric, not the count-versus-limit comparison, is the definitive signal that a limit was hit.

#### Example: a spiky Actions workload

Assume an Actions per second (APS) limit of 2,000 (`temporal_cloud_v1_action_limit` = 2000).

A workload submits 60,000 Actions in a single second, then stays idle for the rest of the minute:

- The rate limiter admits about 2,000 Actions in that second and throttles the remaining ~58,000. Throttled Actions are retried by the SDK and drain through at the 2,000 APS limit over the next ~30 seconds, so all 60,000 still complete within the minute.
- `temporal_cloud_v1_total_action_throttled_count` reflects the throttling: ~58,000 Actions throttled over the minute, or ~967 per second.
- `temporal_cloud_v1_total_action_count` reports 60,000 Actions / 60 seconds = **1,000 APS** — half the 2,000 limit.

Read in isolation, the count metric (1,000) against the limit (2,000) suggests plenty of headroom and no throttling. The throttle metric tells the true story: the burst exceeded the limit and ~58,000 Actions were delayed.

#### Monitor count, limit, and throttle together

To understand a spiky workload, always read all three metrics in the row as a set:

| Metric | What it tells you |
| ------ | ----------------- |
| Count (e.g. `temporal_cloud_v1_total_action_count`) | Average demand over the minute |
| Limit (e.g. `temporal_cloud_v1_action_limit`) | Your provisioned ceiling |
| Throttle (e.g. `temporal_cloud_v1_total_action_throttled_count`) | Whether the limit was actually hit |

A non-zero throttle value means the limit was hit during that window, even when the count sits comfortably below the limit. For spiky or latency-sensitive workloads, alert on the throttle metric directly (any value greater than zero) rather than relying only on a count-versus-limit threshold, which can hide sub-minute bursts. The same logic applies to all three limit types — Actions (APS), service requests (RPS), and operations — using each row of the [limit / count / throttle table](#rps-aps-rate-limits) above.

## Detecting Resource Exhaustion

Resource exhaustion happens when a single resource (a Namespace, Task Queue, or Workflow ID) receives a burst of operations larger than that resource can absorb in the moment. The Cloud metric `temporal_cloud_v1_resource_exhausted_error_count` increments and `ResourceExhausted` gRPC errors are returned to the client. SDKs retry these errors gracefully, so workflow progress is rarely impacted.

Persistent non-zero values are unexpected and indicate a hot resource. Use the `operation` label to identify which RPC is hitting the burst limit. For example, `StartWorkflowExecution` increments here when the same Workflow ID is started more than once per second.

Resource exhaustion is distinct from rate limiting against your account limits. For workloads that are throttled because they exceed their provisioned capacity, see [Monitoring Trends Against Limits](#rps-aps-rate-limits). Limits-driven throttling slows or stalls a workload, so it is generally the more important signal to monitor.

### Workflow lock contention (BusyWorkflow)

The most common cause of resource exhaustion is Workflow lock contention. Every operation that mutates a single Workflow Execution (starting it, sending a Signal, etc.) is serialized under a per-Workflow lock. When operations reach one Execution faster than that lock can be acquired, the Service rejects the excess with a `ResourceExhausted` error. In Service logs this appears as `Workflow is busy.`

This is contention on a single Execution, not an account limit. Increasing your Actions, Requests, or Operations per second limits does not resolve it.

To confirm lock contention:

1. Rule out account-limit throttling first. If the throttle metrics described in [Monitoring Trends Against Limits](#rps-aps-rate-limits) are elevated, address that throttling first.
2. If you are within your limits but `temporal_cloud_v1_resource_exhausted_error_count` is still non-zero, break it down by the `operation` label. Lock contention concentrates on operations that target individual executions.
3. Match the operation to the guidance below.

| `operation` | What it indicates | What to do |
| ----------- | ----------------- | ---------- |
| `StartWorkflowExecution`, `SignalWithStartWorkflowExecution` | The same Workflow ID was started again within a short de-duplication window (about one second). The first start succeeded; the duplicate was rejected. | Usually safe to ignore. Do not aggressively retry. There may be a client path firing the duplicate start. |
| `SignalWorkflowExecution` | Too high of a rate of Signals to one execution. | Batch or coalesce Signals (for example, one Signal per N events), shard work across more executions, or buffer Signals and drain them in the main Workflow loop. |
| `UpdateWorkflowExecution` | More than the per-execution in-flight Update limit (10) are outstanding. | Cap concurrent in-flight Updates on the client, then back off and retry. |
| `RecordActivityTaskHeartbeat` | Too many Activities are heartbeating to the same execution. | Increase the heartbeat timeout and interval, and reduce the number of Activities heartbeating into one execution concurrently. |
| `RespondWorkflowTaskCompleted` | A single Workflow schedules a large batch of Activities or Child Workflows in parallel, each taking the lock. | Limit concurrent operations to 500 or fewer per execution. Process the batch in smaller groups using a sliding-window or plain batching pattern instead of scheduling everything at once. |
| `QueryWorkflow` | Too many concurrent Queries against one execution, or a side effect of repeated Workflow Task retries. | Reduce concurrent Queries to that execution. If it correlates with Workflow Task failures or timeouts, resolve those first. |

At low, brief rates this error is benign because clients retry it and no progress is lost. Investigate when the rate is sustained or correlates with rising latency on the affected operations. For the per-execution limits referenced above, see [Per Workflow Execution concurrency limits](/cloud/limits#per-workflow-execution-concurrency-limits).

---

## tcld account command reference

The `tcld account` commands manage accounts in Temporal Cloud.

Alias: `a`

- [tcld account audit-log](#audit-log)
- [tcld account get](#get)
- [tcld account list-regions](#list-regions)
- [tcld account metrics](#metrics)

## audit-log

The `tcld account audit-log` command manage Audit Logs in Temporal Cloud.

Alias: `al`

- [tcld account audit-log kinesis](#kinesis)
- [tcld account audit-log pubsub](#pubsub)

### kinesis

The `tcld account audit-log kinesis` command manages Kinesis audit log sinks.

Alias: `k`

- [tcld account audit-log kinesis create](#create)
- [tcld account audit-log kinesis delete](#delete)
- [tcld account audit-log kinesis get](#account-audit-log-kinesis-get)
- [tcld account audit-log kinesis list](#list)
- [tcld account audit-log kinesis update](#update)
- [tcld account audit-log kinesis validate](#validate)

#### create

The `tcld account audit-log kinesis` command creates a Kinesis audit log sink.

Alias: `c`

##### --destination-uri

The destination URI of the audit log sink.

Alias: `du`

##### --region

The region to use for the request.

Alias: `re`

##### --role-name

The role name to use to write to the sink.

Alias: `rn`

##### --sink-name

Provide a name for the sink.

#### delete

The `tcld account audit-log kinesis delete` command deletes an audit log sink.

Alias: `d`

##### --resource-version

The resource-version (etag) to update from, if not set the cli will use the latest (optional).

Alias: `v`

##### --sink-name

Provide a name for the sink.

#### get {/* #account-audit-log-kinesis-get */}

The `tcld account audit-log kinesis get` command gets an audit log sink.

Alias: `g`

##### --sink-name

Provide a name for the sink.

#### list

The `tcld account audit-log kinesis list` command lists audit log sinks on the account.

Alias: `l`

##### --page-size

The page size for list operations.

##### --page-token

The page token for list operations.

#### update

The `tcld account audit-log kinesis update` command updates an audit log sink.

Alias: `u`

##### --destination-uri

The destination URI of the audit log sink.

Alias: `du`

##### --enabled

Whether the sink is enabled.

##### --region

The region to use for the request.

Alias: `re`

##### --resource-version

The resource-version (etag) to update from, if not set the cli will use the latest (optional).

Alias: `v`

##### --role-name

The role name to use to write to the sink.

Alias: `rn`

##### --sink-name

Provide a name for the sink.

#### validate

The `tcld account audit-log kinesis validate` command verifies Temporal Cloud can write to a Kinesis sink.

Alias: `v`

##### --destination-uri

The destination URI of the audit log sink.

Alias: `du`

##### --region

The region to use for the request.

Alias: `re`

##### --role-name

The role name to use to write to the sink.

Alias: `rn`

##### --sink-name

Provide a name for the sink.

### pubsub

The `tcld account audit-log pubsub` command manages Pub/Sub audit log sinks.

Alias: `ps`

- [tcld account audit-log pubsub create](#create)
- [tcld account audit-log pubsub delete](#delete)
- [tcld account audit-log pubsub get](#account-audit-log-pubsub-get)
- [tcld account audit-log pubsub list](#list)
- [tcld account audit-log pubsub update](#update)
- [tcld account audit-log pubsub validate](#validate)

#### create

The `tcld account audit-log pubsub` command creates a Pub/Sub audit log sink.

Alias: `c`

##### --service-account-email

The service account email to impersonate to write to the sink.

Alias: `sae`

##### --sink-name

Provide a name for the sink.

##### --topic-name

The topic name to write to the sink.

Alias: `tn`

#### delete

The `tcld account audit-log pubsub delete` command deletes an audit log sink.

Alias: `d`

##### --resource-version

The resource-version (etag) to update from, if not set the cli will use the latest (optional).

Alias: `v`

##### --sink-name

Provide a name for the sink.

#### get {/* #account-audit-log-pubsub-get */}

The `tcld account audit-log pubsub get` command gets an audit log sink.

Alias: `g`

##### --sink-name

Provide a name for the sink.

#### list

The `tcld account audit-log pubsub list` command lists audit log sinks on the account.

Alias: `l`

##### --page-size

The page size for list operations.

##### --page-token

The page token for list operations.

#### update

The `tcld account audit-log pubsub update` command updates an audit log sink.

Alias: `u`

##### --enabled

Whether the sink is enabled.

##### --resource-version

The resource-version (etag) to update from, if not set the cli will use the latest (optional).

Alias: `v`

##### --service-account-email

The service account email to impersonate to write to the sink.

Alias: `sae`

##### --sink-name

Provide a name for the sink.

##### --topic-name

The topic name to write to the sink.

Alias: `tn`

#### validate

The `tcld account audit-log pubsub validate` command verifies Temporal Cloud can write to a Pub/Sub sink.

Alias: `v`

##### --service-account-email

The service account email to impersonate to write to the sink.

Alias: `sae`

##### --sink-name

Provide a name for the sink.

##### --topic-name

The topic name to write to the sink.

Alias: `tn`

## get

The `tcld account get` command gets information about the Temporal Cloud account you are logged into.

Alias: `g`

`tcld account get`

The command has no modifiers.

## list-regions

The `tcld account list-regions` lists all regions where the account can provision namespaces.

Alias: `l`

## metrics

The `tcld account metrics` commands configure the metrics endpoint for the Temporal Cloud account that is currently logged in.

Alias: `m`

- [tcld account metrics enable](#enable)
- [tcld account metrics disable](#disable)
- [tcld account metrics accepted-client-ca](#accepted-client-ca)

### accepted-client-ca

The `tcld account metrics accepted-client-ca` commands manage the end-entity certificates for the metrics endpoint of the Temporal Cloud account that is currently logged in.

:::info

The end-entity certificates for the metrics endpoint must chain up to the CA certificate used for the account. For more information, see [Certificate requirements](/cloud/certificates#certificate-requirements).

:::

Alias: `ca`

- [tcld account metrics accepted-client-ca add](#add)
- [tcld account metrics accepted-client-ca list](#list)
- [tcld account metrics accepted-client-ca set](#set)
- [tcld account metrics accepted-client-ca remove](#remove)

#### add

The `tcld account metrics accepted-client-ca add` command adds end-entity certificates to the metrics endpoint of a Temporal Cloud account.

:::info

The end-entity certificates for the metrics endpoint must chain up to the CA certificate used for the account. For more information, see [Certificate requirements](/cloud/certificates#certificate-requirements).

:::

`tcld account metrics accepted-client-ca add --ca-certificate <value>`

Alias: `a`

The following modifiers control the behavior of the command.

##### --request-id

Specify a request identifier to use for the asynchronous operation. If not specified, the server assigns a request identifier.

Alias: `-r`

**Example**

```bash
tcld account metrics accepted-client-ca add --request-id <request_id> --ca-certificate <encoded_certificate>
```

##### --resource-version

Specify a resource version (ETag) to update from. If not specified, the latest version is used.

Alias: `-v`

**Example**

```bash
tcld account metrics accepted-client-ca add --resource-version <etag> --ca-certificate <encoded_certificate>
```

##### --ca-certificate

_Required modifier unless `--ca-certificate-file` is specified_

Specify a base64-encoded string of a CA certificate PEM file.

If both `--ca-certificate` and `--ca-certificate-file` are specified, only `--ca-certificate` is used.

Alias: `-c`

**Example**

```bash
tcld account metrics accepted-client-ca add --ca-certificate <encoded_certificate>
```

##### --ca-certificate-file

_Required modifier unless `--ca-certificate` is specified_

Specify a path to a CA certificate PEM file.

If both `--ca-certificate` and `--ca-certificate-file` are specified, only `--ca-certificate` is used.

Alias: `-f`

**Example**

```bash
tcld account metrics accepted-client-ca add --ca-certificate-file <path>
```

#### list

The `tcld account metrics accepted-client-ca list` command lists the end-entity certificates that are currently configured for the metrics endpoint of a Temporal Cloud account.

`tcld account metrics accepted-client-ca list`

Alias: `l`

The command has no modifiers.

#### remove

The `tcld account metrics accepted-client-ca remove` command removes end-entity certificates from the metrics endpoint of a Temporal Cloud account.

`tcld account metrics accepted-client-ca remove --ca-certificate <value>`

Alias: `r`

The following modifiers control the behavior of the command.

##### --request-id

Specify a request identifier to use for the asynchronous operation. If not specified, the server assigns a request identifier.

Alias: `-r`

**Example**

```bash
tcld account metrics accepted-client-ca remove --request-id <request_id> --ca-certificate <encoded_certificate>
```

##### --resource-version

Specify a resource version (ETag) to update from. If not specified, the latest version is used.
