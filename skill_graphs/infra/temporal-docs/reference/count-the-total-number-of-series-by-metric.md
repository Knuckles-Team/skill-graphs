# Count the total number of series by metric
count({__name__=~"temporal_cloud_v1_.*"}) by (__name__)
```

## API Limits

| Limit | Impact | Mitigation |
| ----- | ----- | ----- |
| 30k total datapoints per scrape | Response may be truncated | Use namespace/metric filtering |
| 180 requests per account per hour (~3 requests per minute) | HTTP 429 returned | Set scrape interval to 30s |

---

## Temporal Cloud OpenMetrics

:::tip PRICING

Future pricing may apply to high-volume usage that exceeds standard [limits](/cloud/metrics/openmetrics/api-reference#api-limits).

:::

Temporal Cloud's [OpenMetrics](https://openmetrics.io/) endpoint provides operational metrics for your Temporal Cloud workloads in industry-standard Prometheus format, enabling comprehensive monitoring across Namespaces, Workflows, and Task Queues with your existing observability stack.

## Quickstart

Stream metrics from Temporal Cloud into your observability tool in about 5 minutes.

**Prerequisites**

- An **Account Owner** or **Global Admin** role on the Temporal Cloud account. The Metrics Read-Only role is an account-level role and can only be granted by these roles. A Namespace Admin cannot complete these steps.
- An account in the observability tool you want to use (Datadog, Grafana Cloud, New Relic, ClickStack, self-hosted Prometheus, etc.).

**Steps**

1. **Create a Service Account with the Metrics Read-Only role.**

   In the Temporal Cloud UI, go to **Settings → Service Accounts → Create Service Account** and assign the **Metrics Read-Only** account-level role.

2. **Generate an API key for the Service Account.**

   Open the Service Account and create an API key. Copy the key and store it somewhere secure. It is shown only once.

3. **Verify the endpoint is reachable.**

   ```shell
   curl -H "Authorization: Bearer <API_KEY>" https://metrics.temporal.io/v1/metrics
   ```

   You should see OpenMetrics-formatted output beginning with `# TYPE temporal_cloud_v1_...`.

   :::note `metrics.temporal.io` is for scrapers, not browsers

   The endpoint requires an `Authorization: Bearer <API key>` header on every request. There is no browser UI. Opening `https://metrics.temporal.io` or `https://metrics.temporal.io/v1/metrics` directly in a browser returns `Jwt is missing`. Configure the endpoint inside your observability tool instead.

   :::

4. **Configure your observability tool.**

   Paste the API key into the integration for your tool of choice. See [Metrics integrations](/cloud/metrics/openmetrics/metrics-integrations) for tool-specific setup:

   - [Datadog](/cloud/metrics/openmetrics/metrics-integrations#datadog)
   - [Grafana Cloud](/cloud/metrics/openmetrics/metrics-integrations#grafana-cloud)
   - [New Relic](/cloud/metrics/openmetrics/metrics-integrations#new-relic)
   - [ClickStack](/cloud/metrics/openmetrics/metrics-integrations#clickstack)
   - [Self-hosted Prometheus or OpenTelemetry Collector](/cloud/metrics/openmetrics/metrics-integrations#prometheus-grafana)

Metrics begin populating in your tool within a few minutes.

## Quick Links
* [Integrations](/cloud/metrics/openmetrics/metrics-integrations) - Get started exporting metrics with common integrations
* [API Documentation](/cloud/metrics/openmetrics/api-reference) - Endpoint specification and advanced configuration
* [Metrics Reference](/cloud/metrics/openmetrics/metrics-reference) - Complete catalog of all metrics with descriptions and labels
* [Migration Guide](/cloud/metrics/openmetrics/migration-guide) - Transition from the deprecated Prometheus query endpoint to OpenMetrics

## Overview
Temporal Cloud OpenMetrics exposes 50+ metrics covering workflow lifecycles, task queue operations, service performance, and system limits. All metrics are aggregated over one-minute windows and available for scraping within three minutes. Each scrape returns only the most recently completed one-minute window—configure your monitoring system to retain what it scrapes.

* [Set up authentication and scraping](/cloud/metrics/openmetrics/api-reference#authentication) with the API documentation.
* Browse the [complete metrics catalog](/cloud/metrics/openmetrics/metrics-reference) for descriptions and labels.
* Teams using the query endpoint should review the [migration guide](/cloud/metrics/openmetrics/migration-guide).

## API key authentication
Create a Service Account with the "Metrics Read-Only" role and generate an API key. See the [Quickstart](#quickstart) above for step-by-step instructions. API keys work with standard HTTPS, with no certificate rotation or distribution required.

## Global endpoint
This is a single endpoint at `metrics.temporal.io` which serves all metrics across your entire account with API key authentication and standard HTTPS.

## Namespace and metric filtering
You can use query parameters to enable selective scraping to manage data volume and costs, which support wildcards for flexible namespace selection and specific metric filtering.

## Dashboard templates
Production-ready [Grafana dashboards](https://github.com/grafana/jsonnet-libs/blob/master/temporal-mixin/dashboards/temporal-overview.json) provide immediate visibility with pre-built queries and visualizations.

---

## Metrics integrations

Metrics can be exported from Temporal Cloud using the OpenMetrics endpoint. This document describes configuring integrations that have third party support or are based on open standards.
This document is for basic configuration only. For advanced concepts such as label management and high cardinality scenarios see the
[general API reference](/cloud/metrics/openmetrics/api-reference).

## Integrations

Before configuring any integration, complete the [Quickstart](/cloud/metrics/openmetrics#quickstart) to create a Service Account with the **Metrics Read-Only** role and generate an API key. This requires the **Account Owner** or **Global Admin** role - a Namespace Admin cannot grant the Metrics Read-Only role.

### Datadog

Datadog provides a serverless integration with the OpenMetrics endpoint. It scrapes metrics, stores them in Datadog, and ships a default dashboard with built-in monitors.

1. In Datadog, open the [Integrations catalog](https://app.datadoghq.com/integrations) and search for **Temporal Cloud OpenMetrics**. Install the integration.
2. Click **Add Account** in the integration tile and paste your Temporal Cloud API key into the **API Key** field.
3. Save the configuration. The default Temporal Cloud dashboard appears in **Dashboards → Dashboards List** once data starts flowing (typically within a few minutes).

For Datadog-side details, see the [Datadog integration page](https://docs.datadoghq.com/integrations/temporal-cloud-openmetrics/).

For Datadog users, treat this integration as the Cloud-side half of your observability setup:

- Use OpenMetrics in Datadog to monitor Temporal Cloud behavior such as Task Queue backlog, poll success, and rate limiting.
- Collect [SDK metrics](/cloud/metrics/sdk-metrics-setup) from your Workers separately to monitor saturation, Schedule-To-Start latency, slot availability, and sticky cache behavior.

If you only ingest Cloud metrics, you will miss many worker-side bottlenecks. For recommended Worker monitors, see
[Monitor worker health](/cloud/worker-health).

### Grafana Cloud

Grafana Cloud provides a serverless integration with the OpenMetrics endpoint. It scrapes metrics, stores them in Grafana Cloud, and ships a default dashboard for visualizing them.

1. In Grafana Cloud, go to **Connections → Add new connection** and search for **Temporal Cloud**.
2. On the integration page, paste your Temporal Cloud API key into the **API Key** field.
3. Add `metrics.temporal.io` to **Allowed hosts** so Grafana Cloud can reach the endpoint.
4. Click **Install** to enable the integration and import the pre-built dashboard.

If the dashboard shows no data after a few minutes, confirm the API key's Service Account has the **Metrics Read-Only** role and that the endpoint is reachable using the `curl` check from the [Quickstart](/cloud/metrics/openmetrics#quickstart).

For Grafana-side details, see the [Grafana Cloud integration page](https://grafana.com/docs/grafana-cloud/monitor-infrastructure/integrations/integration-reference/integration-temporal/).

### ClickStack

ClickHouse provides an integration with the OpenMetrics endpoint for ClickStack. This integration uses an OpenTelemetry collector to read from the OpenMetrics endpoint, ingest data into ClickHouse, and
includes a default dashboard to visualize the data with HyperDX. See the [integration page](https://clickhouse.com/docs/use-cases/observability/clickstack/integrations/temporal-metrics) for more details.

1. Save your Temporal Cloud API key to a local file named `temporal.key` (no trailing newline or spaces).
2. Create an OpenTelemetry collector config named `temporal-metrics.yaml` that uses a Prometheus receiver against `metrics.temporal.io` with Bearer token auth, a 60-second scrape interval, the `service.name: "temporal"` resource attribute, and the ClickHouse exporter. Copy the full template from the [ClickStack integration page](https://clickhouse.com/docs/use-cases/observability/clickstack/integrations/temporal-metrics).
3. Mount both files into your ClickStack collector and set the custom config env var. With Docker Compose:

   ```yaml
   volumes:
     - ./temporal-metrics.yaml:/etc/otelcol-contrib/custom.config.yaml
     - ./temporal.key:/etc/otelcol-contrib/temporal.key
   environment:
     CUSTOM_OTELCOL_CONFIG_FILE: /etc/otelcol-contrib/custom.config.yaml
   ```

4. In HyperDX, open the **Metrics explorer** and confirm metrics with the `temporal` prefix are arriving.
5. Import the pre-built dashboard: in HyperDX click **Import Dashboard**, upload `temporal-metrics-dashboard.json` from the ClickStack integration page, then click **Finish Import**.

### New Relic

The New Relic integration pulls metrics from the OpenMetrics endpoint via the `nri-flex` integration that runs alongside the New Relic infrastructure agent.

:::note Requires a host

The integration runs on a host (Linux, Windows, or Kubernetes) with the New Relic infrastructure agent installed. The agent scrapes the endpoint and forwards metrics to New Relic.

:::

1. Install the **New Relic infrastructure agent** on a host. See the [agent install docs](https://docs.newrelic.com/docs/infrastructure/install-infrastructure-agent/get-started/install-infrastructure-agent/) for platform-specific instructions.
2. Create `/etc/newrelic-infra/integrations.d/nri-flex-temporal-cloud-config.yml` using the template from the [New Relic integration page](https://docs.newrelic.com/docs/infrastructure/host-integrations/host-integrations-list/temporal-cloud-integration/), and replace the `${TEMPORAL_API_KEY}` placeholder with your Temporal Cloud API key.
3. Restart the agent so the new config is picked up:

   ```shell
   sudo systemctl restart newrelic-infra.service
   ```

4. In **one.newrelic.com**, go to **Integrations & Agents → Dashboards**, search for **Temporal Cloud**, and install the pre-built dashboard. Data appears within a few minutes.

For New Relic-side details, see the [New Relic integration page](https://docs.newrelic.com/docs/infrastructure/host-integrations/host-integrations-list/temporal-cloud-integration/).

### Prometheus \+ Grafana {/* #prometheus-grafana */}

Self hosted Prometheus can be used to scrape the OpenMetrics endpoint.

1. Add a new scrape job for the OpenMetrics endpoint with your [API key](/cloud/metrics/openmetrics/api-reference#creating-api-keys).

```yaml
scrape_configs:
  - job_name: 'temporal-cloud'
    scrape_interval: 30s
    scrape_timeout: 30s
    honor_timestamps: true
    scheme: https
    authorization:
      type: Bearer
      credentials: '<API_KEY>'
    static_configs:
      - targets: ['metrics.temporal.io']
    metrics_path: '/v1/metrics'
```

2. Import the [Grafana dashboard](https://github.com/grafana/jsonnet-libs/blob/master/temporal-mixin/dashboards/temporal-overview.json) and configure your Prometheus datasource.

### OpenTelemetry Collector Configuration

Collect metrics with a self-hosted OpenTelemetry Collector to ingest into the system of your choosing.

1. Add a new prometheus receiver for the OpenMetrics endpoint with your [API key](/cloud/metrics/openmetrics/api-reference#creating-api-keys).

```yaml
receivers:
  prometheus:
    config:
      scrape_configs:
      - job_name: 'temporal-cloud'
        scrape_interval: 30s
        scrape_timeout: 30s
        honor_timestamps: true
        scheme: https
        authorization:
          type: Bearer
          credentials_file: <API_KEY_FILE>
        static_configs:
          - targets: ['metrics.temporal.io']
        metrics_path: '/v1/metrics'

processors:
  batch:

exporters:
  otlphttp:
    endpoint: <ENDPOINT>

service:
  pipelines:
    metrics:
      receivers: [prometheus]
      processors: [batch]
      exporters: [otlphttp]
```

:::info

Examples for these integrations and more are [here](https://github.com/temporal-community/cloud-metrics-scrape-examples).

:::

---

## OpenMetrics metrics reference

This document describes all metrics available from the Temporal Cloud OpenMetrics endpoint.

## Metric Conventions

### Metric Types

All metrics are exposed as OpenMetrics gauges, but represent different measurement types:

* *Rate Metrics*: per-second rate of the aggregated values
* *Value Metrics*: The most recent aggregate value within a look-back window (e.g. backlogs, limits)
* *Percentile Metrics*: Pre-calculated aggregated latency percentiles in seconds

:::note

All metrics are stored as 1 minute aggregates. Rate metrics are therefore per-second rates averaged over each minute, which smooths sub-minute bursts. A short spike can read below your limit even when it triggered throttling. See [Why does throttling occur when count metrics stay below the limit?](/cloud/service-health#why-does-throttling-occur-when-count-metrics-stay-below-the-limit) for a worked example.

:::

### Common Labels

All metrics include these base labels:

| Label | Description |
| ----- | ----- |
| `temporal_namespace` | The Temporal namespace |
| `temporal_account` | The Temporal account identifier |
| `region` | Cloud region where the metric originated |

### Opt-in Labels

Some labels are **opt-in** due to their high cardinality.
These labels are not included by default when you scrape the OpenMetrics endpoint.
To enable an opt-in label, add it to the `labels` query parameter on your scrape URL.
When an opt-in label is enabled, it is populated on **all metrics** that support it.

| Label | Available on | Description |
| ----- | ----- | ----- |
| `temporal_activity_type` | Activity metrics | The activity type name |
| `temporal_worker_deployment_name` | `temporal_cloud_v1_approximate_backlog_count` | The Worker Deployment name |
| `temporal_worker_build_id` | `temporal_cloud_v1_approximate_backlog_count` | The Worker Deployment Version Build ID |

For example, to include `temporal_activity_type` in your scrape results:

```
/v1/metrics?labels=temporal_activity_type
```

Enable multiple labels at the same time by concatenating multiple `labels` query parameters:

```
/v1/metrics?labels=temporal_worker_build_id&labels=temporal_worker_deployment_name
```

## Metrics Catalog

### Frontend Service Metrics

#### temporal\_cloud\_v1\_service\_request\_count

gRPC requests received per second.

| Label | Description |
| ----- | ----- |
| `operation` | The name of the RPC operation |

**Type**: Rate

#### temporal\_cloud\_v1\_service\_request\_throttled\_count

gRPC requests throttled per second. See [Monitoring Trends Against Limits](/cloud/service-health#rps-aps-rate-limits) for guidance on setting alert thresholds against the corresponding limit metric.

| Label | Description |
| ----- | ----- |
| `operation` | The name of the RPC operation |

**Type**: Rate

#### temporal\_cloud\_v1\_service\_error\_count

gRPC errors per second.

| Label | Description |
| ----- | ----- |
| `operation` | The name of the RPC operation |

**Type**: Rate

#### temporal\_cloud\_v1\_service\_pending\_requests

The number of pollers that are actively long polling for a task. Use this to track against ``temporal_cloud_v1_poller_limit``

| Label | Description |
| ----- | ----- |
| `operation` | The name of the operation |

**Type**: Value

#### temporal\_cloud\_v1\_resource\_exhausted\_error\_count

Resource exhaustion errors per second, incremented when a single resource receives a burst larger than it can absorb. SDKs retry these errors gracefully. This metric does not include throttling due to Namespace limits - see [`temporal_cloud_v1_total_action_throttled_count`](#temporal_cloud_v1_total_action_throttled_count) and related throttle metrics for rate limiting against account limits.

See [Detecting Resource Exhaustion](/cloud/service-health#detecting-resource-exhaustion) for guidance on investigating non-zero values.

| Label | Description |
| ----- | ----- |
| `operation` | The name of the operation |

**Type**: Rate

#### temporal\_cloud\_v1\_service\_latency\_p50

:::caution

Avoid aggregating this metric across dimensions because the percentile won't be accurate.

:::

The 50th percentile latency of service requests in seconds

| Label | Description |
| ----- | ----- |
| `operation` | The name of the operation |

**Type**: Latency

#### temporal\_cloud\_v1\_service\_latency\_p95

:::caution

Avoid aggregating this metric across dimensions because the percentile won't be accurate.

:::

The 95th percentile latency of service requests in seconds

| Label | Description |
| ----- | ----- |
| `operation` | The name of the operation |

**Type**: Latency

#### temporal\_cloud\_v1\_service\_latency\_p99

:::caution

Avoid aggregating this metric across dimensions as the percentile won't be accurate.

:::

The 99th percentile latency of service requests in seconds

| Label | Description |
| ----- | ----- |
| `operation` | The name of the operation |

**Type**: Latency

### Workflow Completion Metrics

:::caution High Cardinality

These metrics could have high cardinality depending on number of workflow types and task queues.

:::

#### temporal\_cloud\_v1\_workflow\_success\_count

Successful workflow completions per second.

| Label | Description |
| ----- | ----- |
| `temporal_task_queue` | The task queue name |
| `temporal_workflow_type` | The workflow type |

**Type**: Rate

#### temporal\_cloud\_v1\_workflow\_failed\_count

Workflow failures per second.

| Label | Description |
| ----- | ----- |
| `temporal_task_queue` | The task queue name |
| `temporal_workflow_type` | The workflow type |

**Type**: Rate

#### temporal\_cloud\_v1\_workflow\_timeout\_count

Workflow timeouts per second.

| Label | Description |
| ----- | ----- |
| `temporal_task_queue` | The task queue name |
| `temporal_workflow_type` | The workflow type |

**Type**: Rate

#### temporal\_cloud\_v1\_workflow\_cancel\_count

Workflow cancellations per second.

| Label | Description |
| ----- | ----- |
| `temporal_task_queue` | The task queue name |
| `temporal_workflow_type` | The workflow type |

**Type**: Rate

#### temporal\_cloud\_v1\_workflow\_terminate\_count

Workflow terminations per second.

| Label | Description |
| ----- | ----- |
| `temporal_task_queue` | The task queue name |
| `temporal_workflow_type` | The workflow type |

**Type**: Rate

#### temporal\_cloud\_v1\_workflow\_continued\_as\_new\_count

Workflows continued as new per second.

| Label | Description |
| ----- | ----- |
| `temporal_task_queue` | The task queue name |
| `temporal_workflow_type` | The workflow type |

**Type**: Rate

#### temporal\_cloud\_v1\_workflow\_schedule\_to\_close\_latency\_p50

:::caution

Avoid aggregating this metric across dimensions because the percentile won't be accurate.

:::

The 50th percentile workflow schedule-to-close latency in seconds.

| Label | Description |
| ----- | ----- |
| `temporal_workflow_type` | The workflow type |

**Type**: Latency

#### temporal\_cloud\_v1\_workflow\_schedule\_to\_close\_latency\_p95

:::caution

Avoid aggregating this metric across dimensions because the percentile won't be accurate.

:::

The 95th percentile workflow schedule-to-close latency in seconds.

| Label | Description |
| ----- | ----- |
| `temporal_workflow_type` | The workflow type |

**Type**: Latency

#### temporal\_cloud\_v1\_workflow\_schedule\_to\_close\_latency\_p99

:::caution

Avoid aggregating this metric across dimensions because the percentile won't be accurate.

:::

The 99th percentile workflow schedule-to-close latency in seconds.

| Label | Description |
| ----- | ----- |
| `temporal_workflow_type` | The workflow type |

**Type**: Latency

### Activity Metrics

:::caution High Cardinality

These metrics could have high cardinality depending on number of activity types, workflow types, and task queues. The `temporal_activity_type` label is [opt-in](#opt-in-labels) to help manage cardinality.

:::

:::note Standalone Activities

Standalone Activities are Activity Executions that are started independently, without an associated Workflow. For Activity metrics that include the `temporal_workflow_type` label, Standalone Activities use the placeholder value `"__standalone_activity"`.

:::

#### temporal\_cloud\_v1\_activity\_success\_count

Successful activity completions per second.

| Label | Description |
| ----- | ----- |
| `temporal_task_queue` | The task queue name |
| `temporal_workflow_type` | The workflow type |
| `temporal_activity_type` | The activity type (opt-in) |

**Type**: Rate

#### temporal\_cloud\_v1\_activity\_fail\_count

Activity failures per second.

| Label | Description |
| ----- | ----- |
| `temporal_task_queue` | The task queue name |
| `temporal_workflow_type` | The workflow type |
| `temporal_activity_type` | The activity type (opt-in) |

**Type**: Rate

#### temporal\_cloud\_v1\_activity\_timeout\_count

Activity timeouts per second.

| Label | Description |
| ----- | ----- |
| `temporal_task_queue` | The task queue name |
| `temporal_workflow_type` | The workflow type |
| `temporal_activity_type` | The activity type (opt-in) |
| `timeout_type` | The timeout type |

**Type**: Rate

#### temporal\_cloud\_v1\_activity\_task\_fail\_count

Activity task failures per second.

| Label | Description |
| ----- | ----- |
| `temporal_task_queue` | The task queue name |
| `temporal_workflow_type` | The workflow type |
| `temporal_activity_type` | The activity type (opt-in) |

**Type**: Rate

#### temporal\_cloud\_v1\_activity\_task\_timeout\_count

Activity task timeouts per second.

| Label | Description |
| ----- | ----- |
| `temporal_task_queue` | The task queue name |
| `temporal_workflow_type` | The workflow type |
| `temporal_activity_type` | The activity type (opt-in) |
| `timeout_type` | The timeout type |

**Type**: Rate

#### temporal\_cloud\_v1\_activity\_cancel\_count

Activity cancellations per second.

| Label | Description |
| ----- | ----- |
| `temporal_task_queue` | The task queue name |
| `temporal_workflow_type` | The workflow type |
| `temporal_activity_type` | The activity type (opt-in) |

**Type**: Rate

#### temporal\_cloud\_v1\_activity\_terminate\_count

Activity terminations per second.  This metric only applies to Standalone Activities. Regular Activities that run within a Workflow cannot be terminated independently.

| Label | Description |
| ----- | ----- |
| `temporal_task_queue` | The task queue name |
| `temporal_workflow_type` | The workflow type |
| `temporal_activity_type` | The activity type (opt-in) |

**Type**: Rate

:::info Activity latency labels

Activity latency metrics include only the `temporal_activity_type` label.
Labels such as `temporal_task_queue` and `temporal_workflow_type` are intentionally excluded because pre-calculated percentile values cannot be accurately aggregated across additional dimensions.

:::

#### temporal\_cloud\_v1\_activity\_start\_to\_close\_latency\_p50

:::caution

Avoid aggregating this metric across dimensions because the percentile won't be accurate.

:::

The 50th percentile activity start-to-close latency in seconds.

| Label | Description |
| ----- | ----- |
| `temporal_activity_type` | The activity type (opt-in) |

**Type**: Latency

#### temporal\_cloud\_v1\_activity\_start\_to\_close\_latency\_p95

:::caution

Avoid aggregating this metric across dimensions because the percentile won't be accurate.

:::

The 95th percentile activity start-to-close latency in seconds.

| Label | Description |
| ----- | ----- |
| `temporal_activity_type` | The activity type (opt-in) |

**Type**: Latency

#### temporal\_cloud\_v1\_activity\_start\_to\_close\_latency\_p99

:::caution

Avoid aggregating this metric across dimensions because the percentile won't be accurate.

:::

The 99th percentile activity start-to-close latency in seconds.

| Label | Description |
| ----- | ----- |
| `temporal_activity_type` | The activity type (opt-in) |

**Type**: Latency

#### temporal\_cloud\_v1\_activity\_schedule\_to\_close\_latency\_p50

:::caution

Avoid aggregating this metric across dimensions because the percentile won't be accurate.

:::

The 50th percentile activity schedule-to-close latency in seconds.

| Label | Description |
| ----- | ----- |
| `temporal_activity_type` | The activity type (opt-in) |

**Type**: Latency

#### temporal\_cloud\_v1\_activity\_schedule\_to\_close\_latency\_p95

:::caution

Avoid aggregating this metric across dimensions because the percentile won't be accurate.

:::

The 95th percentile activity schedule-to-close latency in seconds.

| Label | Description |
| ----- | ----- |
| `temporal_activity_type` | The activity type (opt-in) |

**Type**: Latency

#### temporal\_cloud\_v1\_activity\_schedule\_to\_close\_latency\_p99

:::caution

Avoid aggregating this metric across dimensions because the percentile won't be accurate.

:::

The 99th percentile activity schedule-to-close latency in seconds.

| Label | Description |
| ----- | ----- |
| `temporal_activity_type` | The activity type (opt-in) |

**Type**: Latency

### Task Queue Metrics

:::caution High Cardinality

These metrics could have high cardinality depending on number of task queues present.

:::

#### temporal\_cloud\_v1\_approximate\_backlog\_count

The approximate number of tasks pending in a task queue. Started Activities are not included in the count as they have been dequeued from the task queue.

:::note Known accuracy limitations
This metric is approximate.
It can overcount because invalid or expired Tasks, like from cancelled, terminated, completed, or timed out Workflows, remain in the count until they reach the head of the queue and are processed and discarded.

It can also reset to zero on an idle Task Queue. If no Worker polls, no new Tasks are added, and no other Task Queue calls occur (such as `DescribeTaskQueue` or `UpdateTaskQueueConfig`) for approximately 5 minutes. The Task Queue is unloaded from memory.
Infrequent metadata updates and database time-to-live settings can also cause this metric to drift at a smaller magnitude.
See [backlog accuracy limitations](/develop/worker-performance#backlog-accuracy-limitations) for details.
:::

| Label | Description |
| ----- | ----- |
| `temporal_task_queue` | The task queue name |
| `task_type` | Type of task: `workflow` or `activity` |
| `task_priority` | The task priority |
| `temporal_worker_deployment_name` | The Worker Deployment name (opt-in) |
| `temporal_worker_build_id` | The Worker Deployment Version Build ID (opt-in) |

**Type**: Value

#### temporal\_cloud\_v1\_poll\_success\_count

Successfully matched tasks per second.

| Label | Description |
| ----- | ----- |
| `operation` | The poll operation name |
| `task_type` | Type of task: `workflow` or `activity` |
| `temporal_task_queue` | The task queue name |

**Type**: Rate

#### temporal\_cloud\_v1\_poll\_success\_sync\_count

Tasks matched synchronously per second (no polling wait).

| Label | Description |
| ----- | ----- |
| `operation` | The poll operation name |
| `task_type` | Type of task: `workflow` or `activity` |
| `temporal_task_queue` | The task queue name |

**Type**: Rate

#### temporal\_cloud\_v1\_poll\_timeout\_count

The rate of poll requests that timed out without receiving a task.

| Label | Description |
| ----- | ----- |
| `operation` | The poll operation name |
| `task_type` | Type of task: `workflow` or `activity` |
| `temporal_task_queue` | The task queue name |

**Type**: Rate

#### temporal\_cloud\_v1\_no\_poller\_tasks\_count

The rate of tasks added to queues with no active pollers.

| Label | Description |
| ----- | ----- |
| `temporal_task_queue` | The task queue name |
| `task_type` | Type of task: `workflow` or `activity` |

**Type**: Rate

### Namespace Metrics

#### temporal\_cloud\_v1\_namespace\_open\_workflows

The current number of open workflows in a namespace.

**Type**: Value

#### temporal\_cloud\_v1\_total\_action\_count

The total number of actions performed per second. Actions with `is_background=false` are counted toward the ``temporal_cloud_v1_action_limit``.

| Label | Description |
| ----- | ----- |
| `is_background` | Whether the action was background: `true` or `false`. Background actions (e.g. History export) do not count toward the action rate limit |
| `namespace_mode` | Indicates if actions are produced by an `active` or a `standby` Namespace |

:::note

Does not include the `region` label. Actions are scoped to the Namespace level.

:::

#### temporal\_cloud\_v1\_billable\_action\_count

The number of billable actions per second, broken down by action type and Workflow Type. Not all billable actions are included in this metric; see [Actions](/cloud/actions) for details on exceptions.

| Label | Description |
| ----- | ----- |
| `action_type` | The [action](/cloud/actions) type |
| `temporal_workflow_type` | The workflow type |

:::note Public Preview

This metric is currently in [Public Preview](/evaluate/development-production-features/release-stages#public-preview).

:::

:::caution High Cardinality

This metric could have high cardinality depending on number of action types and workflow types.

:::

**Type**: Rate

#### temporal\_cloud\_v1\_total\_action\_throttled\_count

The total number of actions throttled per second. See [Monitoring Trends Against Limits](/cloud/service-health#rps-aps-rate-limits) for guidance on setting alert thresholds against the corresponding limit metric.

**Type**: Rate

#### temporal\_cloud\_v1\_operations\_count

Operations performed per second.

| Label | Description |
| ----- | ----- |
| `operation` | The name of the operation |
| `is_background` | Whether the operation was background: `true` or `false`. Background operations do not count toward the operation rate limit |
| `namespace_mode` | Indicates if operations are produced by an `active` or a `standby` Namespace |

**Type**: Rate

#### temporal\_cloud\_v1\_operations\_throttled\_count

Operations throttled due to rate limits per second. See [Monitoring Trends Against Limits](/cloud/service-health#rps-aps-rate-limits) for guidance on setting alert thresholds against the corresponding limit metric.

| Label | Description |
| ----- | ----- |
| `operation` | The name of the operation |
| `is_background` | Whether the operation was background: `true` or `false`. Background operations do not count toward the operation rate limit |
| `namespace_mode` | Indicates if actions are throttled in an `active` or a `standby` Namespace |

**Type**: Rate

### Schedule Metrics

#### temporal\_cloud\_v1\_schedule\_action\_success\_count

Successfully executed scheduled workflows per second.

**Type**: Rate

#### temporal\_cloud\_v1\_schedule\_buffer\_overruns\_count

The rate of schedule buffer overruns when using `BUFFER_ALL` overlap policy.

**Type**: Rate

#### temporal\_cloud\_v1\_schedule\_missed\_catchup\_window\_count

The rate of missed schedule executions outside the catchup window.

**Type**: Rate

#### temporal\_cloud\_v1\_schedule\_rate\_limited\_count

The rate of scheduled workflows delayed due to rate limiting.

**Type**: Rate

### Replication Metrics

#### temporal\_cloud\_v1\_replication\_lag\_p50

The 50th percentile cross-region replication lag in seconds.

**Type**: Latency

#### temporal\_cloud\_v1\_replication\_lag\_p95

The 95th percentile cross-region replication lag in seconds.

**Type**: Latency

#### temporal\_cloud\_v1\_replication\_lag\_p99

The 99th percentile cross-region replication lag in seconds.

**Type**: Latency

### Limit Metrics

#### temporal\_cloud\_v1\_operations\_limit

The current configured operations per second limit for a namespace.

**Type**: Value

#### temporal\_cloud\_v1\_action\_limit

The current configured actions per second limit for a namespace. Track utilization against this limit with ``temporal_cloud_v1_total_action_count`` and `is_background=false`.

**Type**: Value

#### temporal\_cloud\_v1\_service\_request\_limit

The current configured frontend service RPS limit for a namespace. Track utilization against this limit with ``temporal_cloud_v1_service_request_count``

**Type**: Value

#### temporal\_cloud\_v1\_poller\_limit

The current configured poller limit for a namespace. Track utilization against this limit with ``temporal_cloud_v1_service_pending_requests``.

**Type**: Value

#### temporal\_cloud\_v1\_action\_on\_demand\_envelope\_limit

The on-demand envelope limit for actions per second. For Namespaces in provisioned capacity mode, this shows what the action limit would be if operating in on-demand mode. For Namespaces already in on-demand mode, this tracks the same value as `temporal_cloud_v1_action_limit`.

:::note

Does not include the `region` label. Limits are scoped to the Namespace level.

:::

**Type**: Value

#### temporal\_cloud\_v1\_operations\_on\_demand\_envelope\_limit

The on-demand envelope limit for operations per second. For Namespaces in provisioned capacity mode, this shows what the operations limit would be if operating in on-demand mode. For Namespaces already in on-demand mode, this tracks the same value as `temporal_cloud_v1_operations_limit`.

:::note

Does not include the `region` label. Limits are scoped to the Namespace level.

:::

**Type**: Value

#### temporal\_cloud\_v1\_service\_request\_on\_demand\_envelope\_limit

The on-demand envelope limit for service requests per second. For Namespaces in provisioned capacity mode, this shows what the service request limit would be if operating in on-demand mode. For Namespaces already in on-demand mode, this tracks the same value as `temporal_cloud_v1_service_request_limit`.

:::note

Does not include the `region` label. Limits are scoped to the Namespace level.

:::

**Type**: Value

---

## OpenMetrics migration guide

Temporal Cloud is transitioning from our Prometheus query endpoint to an industry-standard OpenMetrics
(Prometheus-compatible) endpoint for metrics collection. This migration represents a significant improvement in how you
can monitor your Temporal Cloud workloads, bringing enhanced capabilities, better integration with observability tools,
and access to high-cardinality metrics that were previously unavailable.

:::danger PromQL endpoint deprecated

The PromQL endpoint was deprecated on April 2, 2026 and is no longer accepting new users.
The PromQL endpoint will be disabled for all users on **October 5, 2026**.
Complete your migration to the OpenMetrics endpoint before this date.

:::

## Why We're Making This Change

1. **Industry-Standard Format**: Native compatibility with Prometheus and OpenTelemetry and all major observability
   platforms (Datadog, New Relic etc.) without custom integrations.

2. **High-Cardinality Metrics**: Access to previously unavailable dimensions including:
   - `temporal_task_queue` labels on multiple metrics
   - `temporal_workflow_type` labels for workflow-specific monitoring
   - New task queue backlog metrics for better operational visibility
3. **Accurate Percentiles**: Our new system provides accurate percentile calculations for latency metrics, even in the
   presence of substantial outliers, unlike Prometheus-style histograms.

4. **Simplified Integration**: Direct scraping from your observability tools without intermediate translation layers.

5. **Enhanced Performance**: Optimized for high-cardinality data with built-in safeguards for system stability. Data is
   available to scrape three minutes from the time it was emitted, in line with the freshest metrics
   [available from any major service provider](https://docs.datadoghq.com/integrations/guide/cloud-metric-delay/).

## What's Changing

| Aspect                 | Current Query Endpoint                             | New OpenMetrics Endpoint                    |
| ---------------------- | -------------------------------------------------- | ------------------------------------------- |
| **Protocol**           | Prometheus Query API (`/api/v1/query`)             | OpenMetrics scrape endpoint (`/v1/metrics`) |
| **Authentication**     | mTLS certificates with customer-specific endpoints | API keys with global endpoint               |
| **Metric Temporality** | Cumulative counters                                | Delta temporality (pre-computed rates)      |
| **Query Requirement**  | Direct queries supported                           | Requires observability platform             |
| **Cardinality**        | Limited labels                                     | High-cardinality labels available           |
| **Metric Naming**      | `*_v0_*` metrics                                   | `*_v1_*` metrics                            |

## Migration Timeline

**April 2, 2026 - PromQL endpoint deprecated**

- The PromQL endpoint is no longer accepting new users.
- Existing users should begin migrating to the OpenMetrics endpoint.

**October 5, 2026 - PromQL endpoint disabled**

- The PromQL endpoint will be disabled for all users.
- All metrics consumption must use the OpenMetrics endpoint by this date.

:::important Action Required

Complete migration before October 5, 2026.

:::

## Notable Differences

### 1\. No longer use `rate()` in Prometheus queries

Metrics are now pre-computed as per-second rates with delta temporality.

**Before (Prometheus query endpoint)**:

```
rate(temporal_cloud_v0_frontend_service_request_count[1m])
```

**After (OpenMetrics endpoint)**:

```
temporal_cloud_v1_service_request_count
```

### 2\. Functions that no longer apply

Metrics from OpenMetrics are already rates, therefore certain Prometheus functions no longer make sense. Below is a
non-exhaustive list of some of the functions:

- ❌ `rate()` \- Already computed
- ❌ `increase()` \- Increase of a rate is meaningless
- ❌ `irate()` \- Instant rate not applicable
- ❌ `histogram_quantile()` \- Not applicable (explicit percentiles provided instead)
- ✅ `sum()`, `avg()`, `max()`, `min()` \- Still work normally

### 3\. Percentile metrics

The new endpoint provides explicit percentile metrics (p50, p95, p99) rather than histogram buckets:

**Before (Prometheus query endpoint)**: Calculate percentiles using `histogram_quantile()`

```shell
histogram_quantile(0.95, rate(temporal_cloud_v0_service_latency_bucket[5m]))
```

**After (OpenMetrics endpoint)**: Use pre-calculated percentiles directly

```
temporal_cloud_v1_service_latency_p95
```

**Important Tradeoff**: While pre-calculated percentiles are more accurate for individual time series, they _cannot be
accurately aggregated_. For example:

- ❌ Cannot sum or average p95 values across Namespaces to get a global p95
- ❌ Cannot aggregate p95 values across regions or Task Queues
- ✅ Can still view individual namespace/task queue percentiles accurately
- ✅ More accurate percentile calculations for individual series, especially with outliers

### 4\. Authentication Setup

**Before**: mTLS certificates with customer-specific endpoint

```shell
curl --cert /path/to/client.pem \
     --key /path/to/client.key \
     --cacert /path/to/ca.pem \

"https://<customer-specific>.tmprl.cloud/api/v1/query?query=rate(temporal_cloud_v0_frontend_service_request_count[5m])&time=2025-01-15T10:00:00Z"
```

**After**: API key with global endpoint

```shell
curl -H "Authorization: Bearer <API_KEY>" https://metrics.temporal.io/v1/metrics
```

## Migration Steps

### Create an API Key

Create a service account within the Temporal Cloud UI settings with the “Metrics Read-Only” Account Level Role.

:::note

As this is an account-level role, scoping it to specific namespaces has no effect as it will have access to the full
account’s metrics.

:::

<CaptionedImage
  src="/img/cloud/metrics/service-account-with-metrics-role.png"
  title="Create Service Account with Metrics Read-Only Role"
/>

Once this is created, you can create an API key within this service account which will inherit the role. Save this API
key in a secure location and use it to access the metrics APIs.

To test that this works, curl the endpoint with your API Key.

The output should resemble the following example:

```shell
$ curl -H "Authorization: Bearer <API_KEY>" https://metrics.temporal.io/v1/metrics
