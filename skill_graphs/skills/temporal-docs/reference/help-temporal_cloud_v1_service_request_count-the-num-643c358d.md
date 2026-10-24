# HELP temporal_cloud_v1_service_request_count The number of RPC requests received by the service..
```

Now you are ready to scrape your metrics\!

### Configuring Grafana \+ Prometheus

#### Update Prometheus Configuration

Add a new scrape job for the OpenMetrics endpoint with your API key.

```yaml
scrape_configs:
  - job_name: temporal-cloud
    static_configs:
      - targets:
          - 'metrics.temporal.io'
    scheme: https
    metrics_path: '/v1/metrics'
    honor_timestamps: true
    scrape_interval: 30s
    scrape_timeout: 30s
    authorization:
      type: Bearer
      credentials: 'API_KEY'
```

:::note

This replaces the direct Grafana datasource configuration you used with the query endpoint.

:::

#### Install New Dashboards

- Download the new Grafana dashboard:
  [temporal_cloud_openmetrics.json](https://github.com/temporalio/dashboards/blob/master/cloud/temporal_cloud_openmetrics.json)
- Import alongside existing dashboards during transition
- Update any custom alerts and queries to use new metrics and remove `rate()` functions

#### Other Observability Providers

Consult the documentation for your observability system for how to configure it to scrape this endpoint and retrieve
your metrics:

- [Datadog](https://docs.datadoghq.com/integrations/temporal-cloud-openmetrics/)
- [NewRelic](https://docs.newrelic.com/docs/infrastructure/prometheus-integrations/install-configure-openmetrics/configure-prometheus-openmetrics-integrations/)
- [OpenTelemetry Collector](https://opentelemetry.io/docs/collector/configuration/#receivers)

Examples for all these integrations live [here](https://github.com/temporal-community/cloud-metrics-scrape-examples).

### Metric Mapping Reference

Below is a template for mapping metrics from the old query endpoint to the new OpenMetrics endpoint. Note that all metrics follow the pattern of `v0` → `v1` version change, and the fundamental difference is the shift from cumulative counters to pre-computed rates for the majority of the metrics. Note that the labels below are only new labels added to the metrics. For the complete list of labels, see the /cloud/metrics/openmetrics/metrics-reference.

#### Frontend Service Metrics

| Old Metric (v0)                                    | New Metric (v1)                                    | New Labels |
| -------------------------------------------------- | -------------------------------------------------- | ---------- |
| `temporal_cloud_v0_frontend_service_error_count`   | `temporal_cloud_v1_service_error_count`            | `region`   |
| `temporal_cloud_v0_frontend_service_request_count` | `temporal_cloud_v1_service_request_count`          | `region`   |
| `temporal_cloud_v0_resource_exhausted_error_count` | `temporal_cloud_v1_resource_exhausted_error_count` | `region`   |
| `temporal_cloud_v0_state_transition_count`         | No direct equivalent                               | -          |
| `temporal_cloud_v0_total_action_count`             | `temporal_cloud_v1_total_action_count`             | `region`   |

:::note State transition count removed

`temporal_cloud_v0_state_transition_count` does not have an equivalent metric in the OpenMetrics endpoint.
To size workloads for Temporal Cloud (for example, when migrating from self-hosted), use action-based metrics (`temporal_cloud_v1_total_action_count`) and request-based metrics (`temporal_cloud_v1_service_request_count`) together instead.

:::

#### Workflow Metrics

| Old Metric (v0)                                     | New Metric (v1)                                     | New Labels                                              |
| --------------------------------------------------- | --------------------------------------------------- | ------------------------------------------------------- |
| `temporal_cloud_v0_workflow_cancel_count`           | `temporal_cloud_v1_workflow_cancel_count`           | `region` `temporal_workflow_type` `temporal_task_queue` |
| `temporal_cloud_v0_workflow_continued_as_new_count` | `temporal_cloud_v1_workflow_continued_as_new_count` | `region` `temporal_workflow_type` `temporal_task_queue` |
| `temporal_cloud_v0_workflow_failed_count`           | `temporal_cloud_v1_workflow_failed_count`           | `region` `temporal_workflow_type` `temporal_task_queue` |
| `temporal_cloud_v0_workflow_success_count`          | `temporal_cloud_v1_workflow_success_count`          | `region` `temporal_workflow_type` `temporal_task_queue` |
| `temporal_cloud_v0_workflow_terminate_count`        | `temporal_cloud_v1_workflow_terminate_count`        | `region` `temporal_workflow_type` `temporal_task_queue` |
| `temporal_cloud_v0_workflow_timeout_count`          | `temporal_cloud_v1_workflow_timeout_count`          | `region` `temporal_workflow_type` `temporal_task_queue` |

#### Poll Metrics

| Old Metric (v0)                             | New Metric (v1)                             | New Labels                     |
| ------------------------------------------- | ------------------------------------------- | ------------------------------ |
| `temporal_cloud_v0_poll_success_count`      | `temporal_cloud_v1_poll_success_count`      | `region` `temporal_task_queue` |
| `temporal_cloud_v0_poll_success_sync_count` | `temporal_cloud_v1_poll_success_sync_count` | `region` `temporal_task_queue` |
| `temporal_cloud_v0_poll_timeout_count`      | `temporal_cloud_v1_poll_timeout_count`      | `region` `temporal_task_queue` |

#### Latency Metrics

| Old Metric (v0)                                                                                                          | New Metric (v1)                                                                                                     | New Labels |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------- | ---------- |
| `temporal_cloud_v0_service_latency_bucket temporal_cloud_v0_service_latency_count temporal_cloud_v0_service_latency_sum` | `temporal_cloud_v1_service_latency_p99 temporal_cloud_v1_service_latency_p95 temporal_cloud_v1_service_latency_p50` | `region`   |
| `temporal_cloud_v0_replication_lag_bucket temporal_cloud_v0_replication_lag_count temporal_cloud_v0_replication_lag_sum` | `temporal_cloud_v1_replication_lag_p99 temporal_cloud_v1_replication_lag_p95 temporal_cloud_v1_replication_lag_p50` | `region`   |

#### Schedule Metrics

| Old Metric (v0)                                          | New Metric (v1)                                          | New Labels |
| -------------------------------------------------------- | -------------------------------------------------------- | ---------- |
| `temporal_cloud_v0_schedule_action_success_count`        | `temporal_cloud_v1_schedule_action_success_count`        | `region`   |
| `temporal_cloud_v0_schedule_buffer_overruns_count`       | `temporal_cloud_v1_schedule_buffer_overruns_count`       | `region`   |
| `temporal_cloud_v0_schedule_missed_catchup_window_count` | `temporal_cloud_v1_schedule_missed_catchup_window_count` | `region`   |
| `temporal_cloud_v0_schedule_rate_limited_count`          | `temporal_cloud_v1_schedule_rate_limited_count`          | `region`   |

In addition to these metrics, there are a number of new metrics provided by our OpenMetrics endpoint.

:::info

See the [metrics reference](/cloud/metrics/openmetrics/metrics-reference) for an up-to-date list of all available metrics and their full descriptions.

:::

### Managing High-Cardinality

The new endpoint provides access to high-cardinality labels that can significantly increase your metric volume:

#### High-Cardinality Labels

- `temporal_task_queue`
- `temporal_workflow_type`

#### Best Practices

##### Namespace/Metric filtering

Namespace filtering can be used to ensure that metrics are scraped for relevant Namespaces, which reduces cardinality.

```
https://metrics.temporal.io/v1/metrics?namespaces=production-*
```

This can be taken further by only scraping relevant metrics for a given namespace which ensures that any new high
cardinality metrics won’t be an issue for your observability system.

```
https://metrics.temporal.io/v1/metrics?metrics=temporal_cloud_v1_workflow_success_count?namespaces=production-*
```

##### Relabeling

If the above doesn’t work, consider dropping problematic labels post-scrape but pre-ingestion into your observability
system.

For example, in Prometheus this can be done via
[relabeling rules](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config).

```yaml
metric_relabel_configs:
- source_labels: [__name__]
  regex: 'temporal_cloud_v1_poll_success_count'
  action: labeldrop
  regex: 'temporal_task_queue'
```

Or you can even relabel certain label values in order to keep significant ones. For example, it’s possible to rename
less important task queues to “unknown” while retaining important ones.

```yaml
metric_relabel_configs:
  - source_labels: [temporal_task_queue]
    regex: '(critical-queue|payment-queue)'
    target_label: __tmp_keep_original
    replacement: 'true'
  # For anything without the keep flag, replace with "unknown"
  - source_labels: [__tmp_keep_original]
    regex: '' # empty/missing value
    target_label: temporal_task_queue
    replacement: 'unknown'
  # Clean up the temporary label
  - regex: '__tmp_keep_original'
    action: labeldrop
```

## Limits

See [API limits](/cloud/metrics/openmetrics/api-reference#api-limits) for details.

## FAQ

### What new metrics are available in OpenMetrics that are not available in PromQL?

OpenMetrics provides visibility into several new areas

- **Activity execution and latency**: completion outcomes (success, fail, timeout, cancel, terminate, plus activity-task-level fail/timeout) and latency percentiles (start-to-close, schedule-to-close), including Standalone Activities.
- **Task queue health**: approximate backlog depth and a rate of tasks added to queues with no active pollers.
- **Namespace utilization and rate limits**: operations counters, throttled-action and throttled-operation rates, a billable-action breakdown, an open-workflow gauge, and configured-limit and on-demand-envelope-limit gauges to chart usage against quotas.
- **Usage against limits**: a request-throttled rate and a pending-requests (active long-pollers) gauge.
- **Higher-dimensional breakdowns**: new labels including region, task queue, workflow type, activity type, worker deployment, and more.

**New metrics:**

- `temporal_cloud_v1_service_request_throttled_count`
- `temporal_cloud_v1_service_pending_requests`
- `temporal_cloud_v1_activity_success_count`
- `temporal_cloud_v1_activity_fail_count`
- `temporal_cloud_v1_activity_timeout_count`
- `temporal_cloud_v1_activity_task_fail_count`
- `temporal_cloud_v1_activity_task_timeout_count`
- `temporal_cloud_v1_activity_cancel_count`
- `temporal_cloud_v1_activity_terminate_count`
- `temporal_cloud_v1_activity_start_to_close_latency_p50` / `_p95` / `_p99`
- `temporal_cloud_v1_activity_schedule_to_close_latency_p50` / `_p95` / `_p99`
- `temporal_cloud_v1_approximate_backlog_count`
- `temporal_cloud_v1_no_poller_tasks_count`
- `temporal_cloud_v1_namespace_open_workflows`
- `temporal_cloud_v1_billable_action_count`
- `temporal_cloud_v1_total_action_throttled_count`
- `temporal_cloud_v1_operations_count`
- `temporal_cloud_v1_operations_throttled_count`
- `temporal_cloud_v1_action_limit`
- `temporal_cloud_v1_operations_limit`
- `temporal_cloud_v1_service_request_limit`
- `temporal_cloud_v1_poller_limit`
- `temporal_cloud_v1_action_on_demand_envelope_limit`
- `temporal_cloud_v1_operations_on_demand_envelope_limit`
- `temporal_cloud_v1_service_request_on_demand_envelope_limit`

**New labels:**

- `region`
- `temporal_task_queue`
- `temporal_workflow_type`
- `task_type`
- `task_priority`
- `is_background`
- `namespace_mode`
- `action_type`
- `timeout_type`
- `temporal_activity_type` (opt-in)
- `temporal_worker_deployment_name` (opt-in)
- `temporal_worker_build_id` (opt-in)
- `worker_version` (opt-in)

For full descriptions, types, and per-metric labels, see the [OpenMetrics metrics reference](/cloud/metrics/openmetrics/metrics-reference).

### Will metrics match between promQL and OpenMetrics endpoints?

No. The metrics will be approximately the same but due to aggregation differences and windowing, values likely won't
match exactly between the two endpoints. Some metrics may be consistently different such as
`temporal_cloud_v1_total_action_count` which includes History Export actions in the OpenMetrics endpoint. In the case of
consistent differences the OpenMetrics endpoint is considered to be more accurate.

### Can I still query metrics directly (e.g. with a Grafana dashboard)?

Currently, the OpenMetrics endpoint requires an observability platform to collect and query metrics. Direct querying via
API to return a time series of data is not supported. Supporting this type of query pattern is a future roadmap item.

### What happens to my existing dashboards and alerts?

During the transition period, both endpoints remain active.

### Will historical data be preserved?

Historical data from the query endpoint will remain in your observability platform. To maintain continuity:

- Combine old (`v0`) and new (`v1`) metrics in your queries during transition
- Consider using the PromQL `or` operator: `metric_v1 or metric_v0`

### Are there limits to how frequently I can scrape or how much data will be returned?

The limits are documented [here](/cloud/metrics/openmetrics/api-reference#api-limits).

### Why are some metrics missing from my scrapes? I don’t see all the metrics documented.

The OpenMetrics endpoint only returns metrics that were generated during the one-minute aggregation window. This is
different from the query endpoint which might return zeros.

**What this means:**

- If no workflows failed in the last minute, `temporal_cloud_v1_workflow_failed_count` won't appear in that scrape.
- If a specific task queue had no activity, its metrics will be absent.
- The set of metrics returned varies between scrapes based on system activity.

**This is normal behavior.** Unlike some metrics systems that populate zeros, the OpenMetrics endpoint follows a sparse
reporting pattern \- metrics only appear when there's actual data to report.

**How to handle this in queries:**

```
(temporal_cloud_v1_workflow_failed_count{namespace="production"} or vector(0))
```

This ensures your dashboards and alerts work correctly even when metrics are temporarily absent due to no activity.

---

## Prometheus Grafana setup

:::danger PromQL endpoint deprecated

The PromQL endpoint and its `temporal_cloud_v0_*` metrics were deprecated on April 2, 2026 and are no longer accepting new users.
The PromQL endpoint will be disabled for all users on **October 5, 2026**.

For Grafana setup with the OpenMetrics endpoint, see the [OpenMetrics integrations page](/cloud/metrics/openmetrics/metrics-integrations).

:::

**How to set up Grafana with Temporal Cloud PromQL endpoint to view Cloud metrics.**

Temporal Cloud emits metrics through a
[Prometheus HTTP API endpoint](https://prometheus.io/docs/prometheus/latest/querying/api/), which can be directly used
as a Prometheus data source in Grafana or to query and export Cloud metrics to any observability platform.

:::note

For setting up SDK metrics (emitted by your Workers and Clients), see
[SDK metrics setup](/cloud/metrics/sdk-metrics-setup).

:::

The process for setting up Temporal Cloud PromQL to work with Grafana includes the following steps:

1. [Generate a Prometheus HTTP API endpoint](/cloud/metrics/general-setup) on Temporal Cloud using valid certificates.
2. Run Grafana and [set up a data source for Temporal Cloud metrics](#grafana-data-source-configuration) in Grafana.
3. [Create dashboards](#grafana-dashboards-setup) in Grafana to view Temporal Cloud metrics. Temporal provides
   [sample community-driven Grafana dashboards](https://github.com/temporalio/dashboards) for Cloud metrics that you can
   use and customize according to your requirements.

If you're following through with the examples provided here, ensure that you have the following:

- Root CA certificates and end-entity certificates. See [Certificate requirements](/cloud/certificates#certificate-requirements) for details.
- Set up your connections to Temporal Cloud using an SDK of your choice and have some Workflows running on Temporal Cloud. See Connect to a Temporal Service for details.

  - [Go](/develop/go/client/temporal-client#connect-to-temporal-cloud)
  - [Java](/develop/java/client/temporal-client#connect-to-temporal-cloud)
  - [PHP](/develop/php/client/temporal-client#connect-to-a-dev-cluster)
  - [Python](/develop/python/client/temporal-client#connect-to-temporal-cloud)
  - [TypeScript](/develop/typescript/client/temporal-client#connect-to-temporal-cloud)
  - [.NET](/develop/dotnet/client/temporal-client#connect-to-temporal-cloud)

- Grafana installed.

## Temporal Cloud metrics setup

Before you set up your Temporal Cloud metrics, ensure that you have the following:

- Account Owner or Global Admin [role privileges](/cloud/manage-access/roles-and-permissions#account-level-roles) for
  the Temporal Cloud account.
- [CA certificate and key](/cloud/certificates) for the Observability integration. You will need the certificate to set
  up the Observability endpoint in Temporal Cloud.

The following steps describe how to set up Observability on Temporal Cloud to generate an endpoint:

1. Log in to Temporal Cloud UI with an Account Owner or Global Admin
   [role](/cloud/manage-access/roles-and-permissions#account-level-roles).
2. Go to **Settings** and select **Integrations**.
3. Select **Configure Observability** (if you're setting it up for the first time) or click **Edit** in the
   Observability section (if it was already configured before).
4. Add your root CA certificate (.pem) and save it. Note that if an observability endpoint is already set up, you can
   append your root CA certificate here to use the generated observability endpoint with your instance of Grafana.
5. To test your endpoint, run the following command on your host:
   ```
   curl -v --cert <path to your client-cert.pem> --key <path to your client-cert.key> "<your generated Temporal Cloud prometheus_endpoint>/api/v1/query?query=temporal_cloud_v0_state_transition_count"
   ```
   If you have Workflows running on a Namespace in your Temporal Cloud instance, you should see some data as a result of
   running this command.
6. Copy the HTTP API endpoint that is generated (it is shown in the UI).

This endpoint should be configured as a data source for Temporal Cloud metrics in Grafana. See
[Grafana data source configuration](#grafana-data-source-configuration) for details.

## SDK metrics setup

SDK metrics are emitted by SDK Clients used to start your Workers and to start, signal, or query your Workflow
Executions. You must configure a Prometheus scrape endpoint for Prometheus to collect and aggregate your SDK metrics.
Each language development guide has details on how to set this up.

- [Go SDK](/develop/go/platform/observability#metrics)
- [Java SDK](/develop/java/platform/observability#metrics)
- [TypeScript SDK](/develop/typescript/platform/observability#metrics)
- [Python](/develop/python/platform/observability#metrics)
- [.NET](/develop/dotnet/platform/observability#metrics)

The following example uses the Java SDK to set the Prometheus registry and Micrometer stats reporter, set the scope, and
expose an endpoint from which Prometheus can scrape the SDK metrics.

```java
//You need the following packages to set up metrics in Java.
//See the Developer's guide for packages required for other SDKs.

//…

//…
   {
     // See the Micrometer documentation for configuration details on other supported monitoring systems.
     // Set up the Prometheus registry.
     PrometheusMeterRegistry yourRegistry = new PrometheusMeterRegistry(PrometheusConfig.DEFAULT);

       public static Scope yourScope(){
     //Set up a scope, report every 10 seconds
       Scope yourScope = new RootScopeBuilder()
               .tags(ImmutableMap.of(
                       "customtag1",
                       "customvalue1",
                       "customtag2",
                       "customvalue2"))
               .reporter(new MicrometerClientStatsReporter(yourRegistry))
               .reportEvery(Duration.ofSeconds(10));

     //Start Prometheus scrape endpoint at port 8077 on your local host
     HttpServer scrapeEndpoint = startPrometheusScrapeEndpoint(yourRegistry, 8077);
     return yourScope;
   }

   /**
    * Starts HttpServer to expose a scrape endpoint. See
    * https://micrometer.io/docs/registry/prometheus for more info.
    */

   public static HttpServer startPrometheusScrapeEndpoint(
           PrometheusMeterRegistry yourRegistry, int port) {
       try {
           HttpServer server = HttpServer.create(new InetSocketAddress(port), 0);
           server.createContext(
                   "/metrics",
                   httpExchange -> {
                       String response = registry.scrape();
                       httpExchange.sendResponseHeaders(200, response.getBytes(UTF_8).length);
                       try (OutputStream os = httpExchange.getResponseBody()) {
                           os.write(response.getBytes(UTF_8));
                       }
                   });
           server.start();
           return server;
       } catch (IOException e) {
           throw new RuntimeException(e);
       }
   }
}

//…

// With your scrape endpoint configured, set the metrics scope in your Workflow service stub and
// use it to create a Client to start your Workers and Workflow Executions.

//…
{
    //Create Workflow service stubs to connect to the Frontend Service.
    WorkflowServiceStubs service = WorkflowServiceStubs.newServiceStubs(
               WorkflowServiceStubsOptions.newBuilder()
                      .setMetricsScope(yourScope()) //set the metrics scope for the WorkflowServiceStubs
                      .build());

   //Create a Workflow service client, which can be used to start, signal, and query Workflow Executions.
   WorkflowClient yourClient = WorkflowClient.newInstance(service,
          WorkflowClientOptions.newBuilder().build());
}

//…
```

To check whether your scrape endpoints are emitting metrics, run your code and go to
[http://localhost:8077/metrics](http://localhost:8077/metrics) to verify that you see the SDK metrics.

You can set up separate scrape endpoints in your Clients that you use to start your Workers and Workflow Executions.

For more examples on setting metrics endpoints in other SDKs, see the metrics samples:

- [Java SDK Samples](https://github.com/temporalio/samples-java/tree/main/core/src/main/java/io/temporal/samples/metrics)
- [Go SDK Samples](https://github.com/temporalio/samples-go/tree/main/metrics)

## Grafana data source configuration {/* #grafana-data-source-configuration */}

**How to configure the Temporal Cloud metrics data source in Grafana.**

Depending on how you use Grafana, you can either install and run it locally, run it as a Docker container, or log in to
Grafana Cloud to set up your data sources.

If you have installed and are running Grafana locally, go to [http://localhost:3000](http://localhost:3000) and sign in.

To add the Temporal Cloud Prometheus HTTP API endpoint that we generated in the
[Temporal Cloud metrics setup](/cloud/metrics/general-setup) section, do the following:

1. Go to **Configuration&nbsp;> Data sources**.
1. Select **Add data source&nbsp;> Prometheus**.
1. Enter a name for your Temporal Cloud metrics data source, such as _Temporal Cloud metrics_.
1. In the **Connection** section, paste the URL that was generated in the Observability section on the Temporal Cloud
   UI.
1. The **Authentication** section may be left as **No Authentication**.
1. In the **TLS Settings** section, select **TLS Client Authentication**:
   - Leave **ServerName** blank. This is not required.
   - Paste in your end-entity certificate and key.
   - Note that the end-entity certificate used here must be part of the certificate chain with the root CA certificates
     used in your [Temporal Cloud observability setup](/cloud/metrics/general-setup).
     <ZoomingImage
       src="/img/cloud/prometheus/add-prometheus-api-endpoint.png"
       alt="Data source configuration in Grafana"
     />
1. Click **Save and test** to verify that the data source is working.

If you see issues in setting this data source, verify your CA certificate chain and ensure that you are setting the
correct certificates in your Temporal Cloud observability setup and in the TLS authentication in Grafana.

### Grafana dashboards setup

To set up dashboards in Grafana, you can use the UI or configure them directly in your Grafana deployment.

:::tip

Temporal provides community-driven
[example dashboards for Temporal Cloud](https://github.com/temporalio/dashboards/tree/master/cloud) that you can
customize to meet your needs.

:::

To import a dashboard in Grafana:

1. In the left-hand navigation bar, select **Dashboards** > **Import dashboard**.
2. You can either copy and paste the JSON from the
   [Temporal Cloud sample dashboards](https://github.com/temporalio/dashboards/tree/master/cloud), or import the JSON
   files into Grafana.
3. Save the dashboard and review the metrics data in the graphs.

To configure dashboards with the UI:

1. Go to **Create > Dashboard** and add an empty panel.
2. On the **Panel configuration** page, in the **Query** tab, select the "Temporal Cloud metrics" data source that you
   configured earlier.
3. Expand the **Metrics browser** and select the metrics you want. You can also select associated labels and values to
   sort the query data. The [PromQL documentation](/cloud/metrics/reference) lists all metrics emitted from PromQL in
   Temporal Cloud.
4. The graph should now display data based on your selected queries.

---

## PromQL Metrics

:::danger PromQL endpoint deprecated

The PromQL endpoint and its `temporal_cloud_v0_*` metrics were deprecated on April 2, 2026 and are no longer accepting new users.
The PromQL endpoint will be disabled for all users on **October 5, 2026**.

Migrate to the [OpenMetrics endpoint](/cloud/metrics/openmetrics).
See the [migration guide](/cloud/metrics/openmetrics/migration-guide) for a complete v0-to-v1 metric mapping.

:::

Metrics for all Namespaces in your account are available from your metrics endpoint. Keep in mind that your Temporal Cloud metrics lag real-time performance by about one minute. Temporal Cloud also only retains raw metrics for seven days.

To ensure security of your metrics, a CA certificate dedicated to observability is required.
Only clients that use certificates signed by that CA, or that chain up to the CA, can query the metrics endpoint.
For more information about CA certificates in Temporal Cloud, see [Certificate requirements](/cloud/certificates#certificate-requirements).

- [General setup](/cloud/metrics/general-setup)
- [Available metrics](/cloud/metrics/reference)
- [Prometheus & Grafana setup](/cloud/metrics/prometheus-grafana)

---

## Temporal Cloud metrics reference

:::danger PromQL endpoint deprecated

The PromQL endpoint and its `temporal_cloud_v0_*` metrics were deprecated on April 2, 2026 and are no longer accepting new users.
The PromQL endpoint will be disabled for all users on **October 5, 2026**.

Migrate to the [OpenMetrics endpoint](/cloud/metrics/openmetrics) which provides `temporal_cloud_v1_*` metrics with higher cardinality, accurate percentiles, and simplified authentication.
See the [migration guide](/cloud/metrics/openmetrics/migration-guide) for a complete v0-to-v1 metric mapping.

:::

A metric is a measurement or data point that provides insights into the performance and health of a system.
This document describes the `temporal_cloud_v0_*` metrics available from the deprecated Temporal Cloud PromQL endpoint.
For the current metrics reference, see the [OpenMetrics metrics reference](/cloud/metrics/openmetrics/metrics-reference).

This document describes:

- **[Available Temporal Cloud metrics](#available-metrics)**:
  The metrics emitted by Temporal Cloud include counts of gRPC errors, requests, successful task matches to a poller, and more.
- **[Metrics labels](#metrics-labels)**:
  Temporal Cloud metrics labels can filter metrics and help categorize and differentiate results.
- **[Operations](#metrics-operations)**:
  An operation is a special type of label that categorizes the type of operation being performed when the metric was collected.

:::info SDK METRICS

This document discusses metrics emitted by [Temporal Cloud](/cloud).
Temporal SDKs also emit metrics, sourced from Temporal Clients and Worker processes.
You can find information about Temporal SDK metrics on its [dedicated page](/references/sdk-metrics).

Please note:

- SDK metrics start with the phrase `temporal_`.
- Temporal Cloud metrics start with `temporal_cloud_`.

:::

## Available Temporal Cloud metrics {/* #available-metrics */}

**What metrics are emitted from Temporal Cloud?**

The following metrics are emitted for your Namespaces:

### Frontend Service metrics {/* #frontend */}

#### temporal_cloud_v0_frontend_service_error_count

This is a count of gRPC errors returned aggregated by operation.
Labels: temporal_account, temporal_namespace, operation, temporal_service_type

#### temporal_cloud_v0_frontend_service_request_count

This is a count of gRPC requests received aggregated by operation.
Labels: temporal_account, temporal_namespace, operation, temporal_service_type

#### temporal_cloud_v0_resource_exhausted_error_count

gRPC requests received that were rate-limited by Temporal Cloud, aggregated by cause.
Labels: temporal_account, temporal_namespace, resource_exhausted_cause

#### temporal_cloud_v0_state_transition_count

Count of state transitions for each Namespace.

#### temporal_cloud_v0_total_action_count

Approximate count of Temporal Cloud Actions.
Labels: temporal_account, temporal_namespace, is_background, namespace_mode

### Poll metrics {/* #poll */}

#### temporal_cloud_v0_poll_success_count

Tasks that are successfully matched to a poller.
Labels: temporal_account, temporal_namespace, operation, task_type, temporal_service_type

#### temporal_cloud_v0_poll_success_sync_count

Tasks that are successfully sync matched to a poller.
Labels: temporal_account, temporal_namespace, operation, task_type, temporal_service_type

#### temporal_cloud_v0_poll_timeout_count

When no tasks are available for a poller before timing out.
Labels: temporal_account, temporal_namespace, operation, task_type, temporal_service_type

### Replication lag metrics {/* #replication-lag */}

#### temporal_cloud_v0_replication_lag_bucket

A histogram of [replication lag](/cloud/metrics/openmetrics/metrics-reference#temporal_cloud_v1_replication_lag_p99) during a specific time interval for a Namespace with high availability.
Labels: temporal_account, temporal_namespace, le

#### temporal_cloud_v0_replication_lag_count

The [replication lag](/cloud/metrics/openmetrics/metrics-reference#temporal_cloud_v1_replication_lag_p99) count during a specific time interval for a Namespace with high availability.
Labels: temporal_account, temporal_namespace

#### temporal_cloud_v0_replication_lag_sum

The sum of [replication lag](/cloud/metrics/openmetrics/metrics-reference#temporal_cloud_v1_replication_lag_p99) during a specific time interval for a Namespace with high availability.
Labels: temporal_account, temporal_namespace

### Schedule metrics {/* #schedule */}

#### temporal_cloud_v0_schedule_action_success_count

Successful execution of a Scheduled Workflow.
Labels: temporal_account, temporal_namespace

#### temporal_cloud_v0_schedule_buffer_overruns_count

When average schedule run length is greater than average schedule interval while a `buffer_all` overlap policy is configured.
Labels: temporal_account, temporal_namespace

#### temporal_cloud_v0_schedule_missed_catchup_window_count

Skipped Scheduled executions when Workflows were delayed longer than the catchup window.
Labels: temporal_account, temporal_namespace

#### temporal_cloud_v0_schedule_rate_limited_count

Workflows that were delayed due to exceeding a rate limit.
Labels: temporal_account, temporal_namespace

### Service latency metrics {/* #service-latency */}

#### temporal_cloud_v0_service_latency_bucket

Latency for `SignalWithStartWorkflowExecution`, `SignalWorkflowExecution`, `StartWorkflowExecution` operations.
Labels: temporal_account, temporal_namespace, le, operation, temporal_service_type

#### temporal_cloud_v0_service_latency_count

Count of latency observations for `SignalWithStartWorkflowExecution`, `SignalWorkflowExecution`, `StartWorkflowExecution` operations.
Labels: temporal_account, temporal_namespace, operation, temporal_service_type

#### temporal_cloud_v0_service_latency_sum

Sum of latency observation time for `SignalWithStartWorkflowExecution`, `SignalWorkflowExecution`, `StartWorkflowExecution` operations.
Labels: temporal_account, temporal_namespace, operation, temporal_service_type

### Workflow metrics {/* #workflow */}

#### temporal_cloud_v0_workflow_cancel_count

Workflows canceled before completing execution.
Labels: temporal_account, temporal_namespace, operation, temporal_service_type

#### temporal_cloud_v0_workflow_continued_as_new_count

Workflow Executions that were Continued-As-New from a past execution.
Labels: temporal_account, temporal_namespace, operation, temporal_service_type

#### temporal_cloud_v0_workflow_failed_count

Workflows that failed before completion.
Labels: temporal_account, temporal_namespace, operation, temporal_service_type

#### temporal_cloud_v0_workflow_success_count

Workflows that successfully completed.
Labels: temporal_account, temporal_namespace, operation, temporal_service_type

#### temporal_cloud_v0_workflow_terminate_count

Workflows terminated before completing execution.
Labels: temporal_account, temporal_namespace, operation, temporal_service_type

#### temporal_cloud_v0_workflow_timeout_count

Workflows that timed out before completing execution.
Labels: temporal_account, temporal_namespace, operation, temporal_service_type

## Metrics labels {/* #metrics-labels */}

**What labels can you use to filter metrics?**

Temporal Cloud metrics include key-value pairs called labels in their associated metadata.
Labels help you categorize and differentiate metrics for precise filtering, querying, and aggregation.
Use labels to filter specific attributes or compare values, such as numeric buckets in histograms.
This added context enhances the monitoring and analysis capabilities, providing deeper insights into your data.

Use the following labels to filter metrics:

| Label                      | Explanation                                                                                                                                                                                                                                                                                |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `le`                       | Less than or equal to (`le`) is used in histograms to categorize observations into buckets based on their value being less than or equal to a predefined upper limit.                                                                                                                      |
| `operation`                | This includes gRPC operations and general Cloud operations such as:SignalWorkflowExecutionStartBatchOperationStartWorkflowExecutionTaskQueueMgrTerminateWorkflowExecutionUpdateNamespaceUpdateSchedule See: [Metric Operations](#metrics-operations) and [Temporal Cloud Operation reference](/references/operation-list)|
| `resource_exhausted_cause` | Cause for resource exhaustion.                                                                                                                                                                                                                                                             |
| `task_type`                | Activity, Workflow, or Nexus.                                                                                                                                                                                                                                                              |
| `temporal_account`         | Temporal Account.                                                                                                                                                                                                                                                                          |
| `temporal_namespace`       | Temporal Namespace.                                                                                                                                                                                                                                                                        |
| `temporal_service_type`    | Frontend or Matching or History or Worker.                                                                                                                                                                                                                                                 |
| `is_background`            | This label on `temporal_cloud_v0_total_action_count` indicates when actions are produced by a Temporal background job, for example: hourly Workflow Export.                                                                                                                                |
| `namespace_mode`           | This label on `temporal_cloud_v0_total_action_count` indicates if actions are produced by an active vs a standby Namespace. For a regular Namespace, `namespace_mode` will always be “active”.                                                                                             |

The following is an example of how you can filter metrics using labels:

```text
temporal_cloud_v0_poll_success_count{__rollup__="true", operation="TaskQueueMgr", task_type="Activity", temporal_account="12345", temporal_namespace="your_namespace.12345", temporal_service_type="matching"}
```

## Operations {/* #metrics-operations */}

**What operation labels are captured by Temporal Cloud?**

Operations are a special class of metrics label.
They describe the context during which a metric was captured.
Temporal Cloud includes the following operations labels:

- AdminDescribeMutableState
- AdminGetWorkflowExecutionRawHistory
- AdminGetWorkflowExecutionRawHistoryV2
- AdminReapplyEvents
- CountWorkflowExecutions
- CreateSchedule
- DeleteSchedule
- DeleteWorkflowExecution
- DescribeBatchOperation
- DescribeNamespace
- DescribeSchedule
- DescribeTaskQueue
- DescribeWorkflowExecution
- GetWorkerBuildIdCompatibility
- GetWorkerTaskReachability
- GetWorkflowExecutionHistory
- GetWorkflowExecutionHistoryReverse
- ListBatchOperations
- ListClosedWorkflowExecutions
- OperatorDeleteNamespace
- PatchSchedule
- PollActivityTaskQueue
- PollNexusTaskQueue
- PollWorkflowExecutionHistory
- PollWorkflowExecutionUpdate
- PollWorkflowTaskQueue
- QueryWorkflow
- RecordActivityTaskHeartbeat
- RecordActivityTaskHeartbeatById
- RegisterNamespace
- RequestCancelWorkflowExecution
- ResetStickyTaskQueue
- ResetWorkflowExecution
- RespondActivityTaskCanceled
- RespondActivityTaskCompleted
- RespondActivityTaskCompletedById
- RespondActivityTaskFailed
- RespondActivityTaskFailedById
- RespondNexusTaskCompleted
- RespondNexusTaskFailed
- RespondQueryTaskCompleted
- RespondWorkflowTaskCompleted
- RespondWorkflowTaskFailed
- SignalWithStartWorkflowExecution
- SignalWorkflowExecution
- StartBatchOperation
- StartWorkflowExecution
- StopBatchOperation
- TerminateWorkflowExecution
- UpdateNamespace
- UpdateSchedule
- UpdateWorkerBuildIdCompatibility
- UpdateWorkflowExecution

As the following table shows, certain [metrics groups](#available-metrics) support [operations](#metrics-operations) for aggregation and filtering:

| Metrics Group / Operations                      | All Operations | SignalWithStartWorkflowExecution / SignalWorkflowExecution / StartWorkflowExecution | TaskQueueMgr | CompletionStats |
| ----------------------------------------------- | -------------- | ----------------------------------------------------------------------------------- | ------------ | --------------- |
| **[Frontend Service Metrics](#frontend)**       | X              |                                                                                     |              |                 |
| **[Service Latency Metrics](#service-latency)** |                | X                                                                                   |              |                 |
| **[Poll Metrics](#poll)**                       |                |                                                                                     | X            |                 |
| **[Workflow Metrics](#workflow)**               |                |                                                                                     |              | X               |

---

## Monitor SDK metrics with Prometheus and Grafana

SDK metrics are emitted by SDK Clients used to start your Workers and to start, signal, or query your Workflow Executions.
Unlike [Temporal Cloud metrics](/cloud/metrics/), which are exposed through a Prometheus HTTP API endpoint, SDK metrics require you to set up a Prometheus scrape endpoint in your application code for Prometheus to collect and aggregate.

For a full list of available SDK metrics and their descriptions, see the [SDK metrics reference](/references/sdk-metrics).

The process for setting up SDK metrics includes the following steps:

1. [Expose a metrics endpoint](#sdk-metrics-setup) in your application code where Prometheus can scrape SDK metrics.
2. [Configure Prometheus](#prometheus-configuration) to scrape your SDK metrics endpoints.
3. [Add an SDK metrics data source](#grafana-data-source-configuration) in Grafana.
4. [Set up dashboards](#grafana-dashboards-setup) to visualize SDK metrics.

Set up your connections to Temporal Cloud using an SDK of your choice and have some Workflows running on Temporal Cloud.
Ensure Prometheus and Grafana are installed.

- [Go](/develop/go/client/temporal-client#connect-to-temporal-cloud)
- [Java](/develop/java/client/temporal-client#connect-to-temporal-cloud)
- [Python](/develop/python/client/temporal-client#connect-to-temporal-cloud)
- [TypeScript](/develop/typescript/client/temporal-client#connect-to-temporal-cloud)
- [.NET](/develop/dotnet/client/temporal-client#connect-to-temporal-cloud)

## Expose a metrics endpoint {/* #sdk-metrics-setup */}

You must configure a Prometheus scrape endpoint for Prometheus to collect and aggregate your SDK metrics.
Each language development guide has details on how to set this up.

- [Go SDK](/develop/go/platform/observability#metrics)
- [Java SDK](/develop/java/platform/observability#metrics)
- [TypeScript SDK](/develop/typescript/platform/observability#metrics)
- [Python](/develop/python/platform/observability#metrics)
- [.NET](/develop/dotnet/platform/observability#metrics)

For working examples of how to configure metrics in each SDK, see the metrics samples:

- [Go SDK Samples](https://github.com/temporalio/samples-go/tree/main/metrics)
- [Java SDK Samples](https://github.com/temporalio/samples-java/tree/main/core/src/main/java/io/temporal/samples/metrics)
- [TypeScript SDK Samples](https://github.com/temporalio/samples-typescript/tree/main/interceptors-opentelemetry)
- [Python SDK Samples](https://github.com/temporalio/samples-python/tree/main/custom_metric)
- [.NET SDK Samples](https://github.com/temporalio/samples-dotnet/tree/main/src/OpenTelemetry/DotNetMetrics)

Some examples use OpenTelemtry to instrument metrics. It is useful to use a
[Prometheus exporter with OpenTelemetry](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/exporter/prometheusexporter) to expose metrics for scraping.

## Configure Prometheus {/* #prometheus-configuration */}

For Temporal SDKs, you must have Prometheus running and configured to listen on the scrape endpoints exposed in your application code.

For this example, you can run Prometheus locally or as a Docker container.
In either case, ensure that you set the listen targets to the ports where you expose your scrape endpoints.
This configuration assumes the scrape endpoint is set to port 8077 as in the [SDK metrics setup](#sdk-metrics-setup) example.

```yaml
global:
  scrape_interval: 30s # Set the scrape interval to every 30 seconds. Default is every 1 minute.
#...
