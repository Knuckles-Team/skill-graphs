# Approximate 99th percentile latency broken down by operation
histogram_quantile(0.99, sum(rate(temporal_cloud_v0_service_latency_bucket[$__rate_interval])) by (le, operation))
```

Metrics are scraped every 30 seconds and exposed to the metrics endpoint with a 1-minute lag.\
The endpoint returns data with a 15-second resolution, which results in displaying the same value twice.

Set up Grafana with Temporal Cloud observability to view metrics by creating or getting your Prometheus endpoint for Temporal Cloud metrics and enabling SDK metrics.

<RelatedReadContainer>
  <RelatedReadItem path="/cloud/metrics/prometheus-grafana" text="How to set up Grafana with Temporal Cloud observability" archetype="feature-guide" />
  <RelatedReadItem path="/cloud/worker-health" text="How to monitor Worker Health with Temporal Cloud Metrics" archetype="feature-guide" />
  <RelatedReadItem path="/cloud/service-health" text="How to monitor Service Health with Temporal Cloud Metrics" archetype="feature-guide" />
</RelatedReadContainer>

---

## Temporal Cloud Metrics

Temporal offers two distinct sources of metrics: [Cloud Metrics](/cloud/metrics/openmetrics/metrics-reference) and [SDK Metrics](/references/sdk-metrics).
Each source provides different levels of granularity, filtering options, monitoring-tool integrations, and configuration.

- **SDK metrics** monitor individual Workers and your code's behavior from the perspective of your application.
- **Cloud metrics** monitor Temporal Cloud's behavior from the perspective of the Temporal Service.

When used together, Cloud and SDK metrics measure the health and performance of your full Temporal infrastructure, including the Temporal Cloud Service and user-supplied Temporal Workers.

:::tip New to Cloud metrics?

Start with the [OpenMetrics Quickstart](/cloud/metrics/openmetrics#quickstart) to create a Service Account, generate an API key, and stream metrics into Datadog, Grafana Cloud, New Relic, ClickStack, or self-hosted Prometheus in about 5 minutes.

:::

## Cloud Metrics

Cloud metrics for all Namespaces in your account are available from the [OpenMetrics endpoint](/cloud/metrics/openmetrics), a Prometheus-compatible scrapable endpoint at `metrics.temporal.io`.

Use the following rule of thumb when deciding which signal to rely on:

| Question | Primary signal |
|---|---|
| Is Temporal Cloud accepting and serving work normally? | Cloud metrics |
| Are Tasks backing up in a Task Queue? | Cloud metrics plus SDK Schedule-To-Start metrics |
| Are my Workers saturated, under-provisioned, or misconfigured? | SDK metrics |
| Is my application logic, downstream dependency, or Activity behavior unhealthy? | SDK metrics and traces |

For a Worker-focused view of how to combine these signals, see [Monitor worker health](/cloud/worker-health).

- [OpenMetrics overview](/cloud/metrics/openmetrics) - Getting started and key concepts
- [Metrics integrations](/cloud/metrics/openmetrics/metrics-integrations) - Datadog, Grafana Cloud, New Relic, ClickStack, and more
- [API reference](/cloud/metrics/openmetrics/api-reference) - Endpoint specification and advanced configuration
- [Metrics reference](/cloud/metrics/openmetrics/metrics-reference) - Complete catalog of all `temporal_cloud_v1_*` metrics

## SDK Metrics

SDK metrics are emitted by your Workers and Clients.
For setup instructions, see [SDK metrics setup](/cloud/metrics/sdk-metrics-setup).

## PromQL Endpoint (Deprecated) {/* #promql-deprecated */}

:::danger PromQL endpoint deprecated

The PromQL endpoint and its `temporal_cloud_v0_*` metrics were deprecated on April 2, 2026 and are no longer accepting new users.
The PromQL endpoint will be disabled for all users on **October 5, 2026**.

Migrate to the [OpenMetrics endpoint](/cloud/metrics/openmetrics).
See the [migration guide](/cloud/metrics/openmetrics/migration-guide) for a complete v0-to-v1 metric mapping.

:::

The legacy PromQL endpoint uses mTLS certificate authentication and exposes `temporal_cloud_v0_*` metrics via a Prometheus query API.

- [PromQL endpoint](/cloud/metrics/promql)
- [PromQL metrics reference](/cloud/metrics/reference)
- [PromQL setup with Grafana](/cloud/metrics/prometheus-grafana)

---

## OpenMetrics API reference

The Temporal Cloud OpenMetrics API provides actionable operational metrics about your Temporal Cloud deployment. This is a scrapable HTTP API that returns metrics in OpenMetrics format, suitable for ingestion by Prometheus-compatible monitoring systems.

## Available Metrics Reference

Metrics descriptions are also available programmatically via the `/v1/descriptors` endpoint. You can see the Metrics Reference for a list of available metrics.

## Authentication

Temporal uses API keys for integrating with the OpenMetrics endpoint. Applications must be authorized and authenticated before they can access metrics from Temporal Cloud.

An API key is owned by a Service Account and inherits the permissions granted to the owner.

### Creating API Keys

API keys can be created using the [Temporal Cloud UI](https://cloud.temporal.io):

1. Navigate to Settings → Service Accounts
2. Create a service account with **"Metrics Read-Only"** Account Level Role
3. Generate an API key within the service account

:::info

See the [docs](https://docs.temporal.io/cloud/api-keys#serviceaccount-api-keys) for more details on generating API keys.

:::

### Using API Keys

All API requests must be made over HTTPS. Calls made over plain HTTP will fail. API requests without authentication will also fail.

```shell
curl -H "Authorization: Bearer <API_KEY>" https://metrics.temporal.io/v1/metrics
```

## Object Model

The object model for the Metrics API follows the [OpenMetrics](https://openmetrics.io/) standard.

### Metrics

A metric is a numeric attribute measured at a specific point in time, labeled with contextual metadata gathered at the point of instrumentation.

### Metric Types

All Temporal Cloud metrics are exposed as *gauges* in OpenMetrics format, but represent different measurement types:

* **Rate metrics**: Pre-computed per-second rates with delta temporality (e.g., `temporal_cloud_v1_workflow_success_count` \- workflows completed per second)
* **Value metrics**: Current or instantaneous values (e.g., `temporal_cloud_v1_approximate_backlog_count` \- current number of tasks in queue)

The list of metrics and their labels are available via the [List Descriptors](/cloud/metrics/openmetrics/api-reference#list-metric-descriptors) endpoint or in the [Metrics Reference](/cloud/metrics/openmetrics/metrics-reference).

### Labels

A label is a key-value attribute associated with a metric data point. Labels can be used to filter or aggregate metrics.

Common labels include:

* `temporal_namespace`: The Temporal namespace
* `temporal_account`: The Temporal account
* `region`: The cloud region where the metric originated
* `temporal_workflow_type`: The workflow type (where applicable)
* `temporal_task_queue`: The task queue name (where applicable)

Each metric has its own set of applicable labels. See the Metrics Reference for complete details.

### Metric Family

A [Metric Family](https://github.com/prometheus/OpenMetrics/blob/main/specification/OpenMetrics.md#metricfamily) may have zero or more metrics.  The set of metrics returned will vary based on actual system activity.  Metrics only appear in a Metric Family if they were reported during the aggregation window.

## Client Considerations

### Rate Limiting

To protect the stability of the API and keep it available to all users, Temporal employs multiple safeguards.

When a rate limit is breached, an HTTP `429 Too Many Requests` error is returned with the following headers:

| Header | Description |
| ----- | ----- |
| `Retry-After` | The time in seconds until the rate limit window resets |

#### Rate Limit Scopes
:::note
Rate limit scopes are subject to change.

:::

| Scope | Limit |
| ----- | ----- |
| Account | 180 requests per hour |

### Response Completeness

The `X-Completeness` header indicates whether the response contains all available data:

* `complete`: The response contains all metrics requested
* `limited`: Response truncated due to size limits (30k metric data points max). Use namespace or metric filtering to reduce the response size.
* `unknown`: Completeness cannot be determined (possibly due to regional issues or timeouts). Clients are encouraged to retry.

### Retry Logic

Implement retry logic in your client to gracefully handle transient API failures. Use exponential backoff with jitter to avoid retry storms with reasonable retry intervals to avoid reaching rate limits.

### Data Latency

Metric data points are available for query within 3 minutes of their origination. This is in line with the freshest metrics [available from any major service provider](https://docs.datadoghq.com/integrations/guide/cloud-metric-delay/). This latency should be accounted for when setting up monitoring alerts.

### Scrape window

The endpoint exposes only the most recently completed one-minute aggregation window. Each scrape returns a snapshot of that window—there is no query interface for historical data. To retain historical metrics, configure your monitoring system to store what it scrapes.

## Endpoints

:::info

All endpoints are served from: `metrics.temporal.io`

:::

### Get Metrics

`GET /v1/metrics`

Returns metrics in OpenMetrics format suitable for scraping by Prometheus-compatible systems.

#### Timestamp Offset

To account for metric data latency, this endpoint returns metrics from the current timestamp minus a fixed offset.  The current offset is 3 minutes rounded down to the start of the minute. To accommodate this offset, the timestamps in the response should be honored when importing the metrics. For example, in Prometheus this can be controlled using the `honor\_timestamps` flag.

#### Query Parameters

| Parameter | Type | Description |
| ----- | ----- | ----- |
| `namespaces` | string array | Filter to specific Namespaces. Supports wildcards (e.g., `production-*`) |
| `metrics` | string array | Filter to specific metrics |

Array parameters use repeated keys. To pass multiple values, repeat the parameter name once per value:

```shell
/v1/metrics?namespaces=prod-payments&namespaces=prod-orders
```

The `namespaces` and `metrics` parameters can be combined, and each may be repeated independently:

```shell
/v1/metrics?namespaces=prod-payments&namespaces=prod-orders&metrics=temporal_cloud_v1_workflow_success_count&metrics=temporal_cloud_v1_approximate_backlog_count
```

#### Response Headers

| Header | Description |
| ----- | ----- |
| `X-Completeness` | Indicates the response status: `complete`, `limited`, or `unknown` |
| `Content-Type` | `application/openmetrics-text` |

:::info Example

Request:

```shell
curl -H "Authorization: Bearer <API_KEY>" \
  "https://metrics.temporal.io/v1/metrics?namespaces=production-*"
```

Response:
```
