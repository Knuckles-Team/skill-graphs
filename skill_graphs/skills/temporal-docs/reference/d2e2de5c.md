   [the additional configuration options](https://github.com/temporalio/samples-server/tree/main/compose#other-configuration-files)
   available in the samples-server repository and use `docker compose up` with the corresponding configuration file to
   try them out. The configurations include different databases, visibility stores, and TLS settings.

## Use Temporal Server binaries

You can run a complete Temporal Server by deploying two Go binaries -- the
[core Temporal Server](https://github.com/temporalio/temporal/releases/), and the
[Temporal UI Server](https://github.com/temporalio/ui-server/releases).

Each service can be deployed separately. Refer to
[How to Configure a Temporal Service without a Proxy](https://learn.temporal.io/tutorials/infrastructure/configuring-sqlite-binary/)
to deploy each service using `systemd`. If you need to run the Temporal Server behind a reverse proxy, refer to our
tutorials to deploy the Temporal Service behind an
[Nginx reverse proxy](https://learn.temporal.io/tutorials/infrastructure/nginx-sqlite-binary/) or an
[Envoy edge proxy](https://learn.temporal.io/tutorials/infrastructure/envoy-sqlite-binary/).

### Configuration templating

Configuration templating is how the Temporal Server turns a template config file into the final `config.yaml` it runs
with. It lets you reuse one template across environments by filling in values from environment variables. For example,
database endpoints, TLS paths, or feature flags.

If you are **not** using a custom config template, you can skip this section. The default configuration is rendered
automatically by the server and embedded in the binary.

#### Template compatibility

If you use a custom configuration template, be aware of the following:

- The server renders templates with embedded `sprig`, so any `dockerize`-specific syntax or helpers will fail
- Some template syntax differs, particularly `.Env` and `default` function usage.
- Refer to the [sprig documentation](http://masterminds.github.io/sprig/) for supported template functions
- Use `temporal-server render-config` to verify your templates render correctly

#### Helm Chart configuration

When deploying with Helm charts versions 0.73.1 or later, you may need to adjust the following configuration options
depending on the images you are using.

| Configuration Option         | Description                                                               | Default       |
| ---------------------------- | ------------------------------------------------------------------------- | ------------- |
| `server.useEntrypointScript` | Whether to use entrypoint script that autodetects `dockerize` vs `sprig`. | `false`       |
| `server.configMapsToMount`   | Which config template to mount: `"dockerize"`, `"sprig"`, or `"both"`.    | `"dockerize"` |
| `server.setConfigFilePath`   | Set `TEMPORAL_SERVER_CONFIG_FILE_PATH` environment variable.              | `false`       |

Refer to the following guidelines to determine if you need to adjust the configuration options:

- The default settings work if you are only using pre-1.30 images with 0.73.1 or later Helm chart.
- If you are using 1.30+ images with 0.73.1 or later Helm chart, you need to set `server.configMapsToMount` to `"sprig"`
  and `server.setConfigFilePath` to `true`. Keep the `server.useEntrypointScript` as `false`.
- If you need use the Helm chart with both pre-1.30 and 1.30+ images, you need to set `server.configMapsToMount` to
  `"both"` and `server.useEntrypointScript` to `true`. Keep the `server.setConfigFilePath` as `false`.

## Import the Server package

The Temporal Server is a standalone Go application that can be [imported](/references/server-options) into another
project.

You might want to do this to pass custom plugins or any other customizations through the
[Server Options](/references/server-options). Then you can build and run a binary that contains your customizations.

This requires Go v1.19 or later, as specified in the Temporal Server
[Build prerequisites](https://github.com/temporalio/temporal/blob/main/CONTRIBUTING.md#build-prerequisites).

## Use Helm charts

[Temporal Helm charts](https://github.com/temporalio/helm-charts) enable you to get a Temporal Service running on
[Kubernetes](https://kubernetes.io/) by deploying the Temporal Server services to individual pods and connecting them to
your existing database and Elasticsearch instances.

The Temporal Helm charts repo contains
[extensive documentation](https://github.com/temporalio/helm-charts/blob/main/README.md) about Kubernetes deployments.

:::caution Helm Chart version compatibility

If you are using Temporal Server images 1.30+, you must upgrade to Helm chart version 0.73.1 or later.

Helm chart versions below 0.73.1 are **not compatible** with `server` and `admin-tools` images **version 1.30 and
later**. You **cannot** override old chart versions with newer images.

:::

---

## Embedding Temporal server as a Go library

You can run Temporal server as an embedded Go library instead of deploying it as a separate service.
This approach is useful for testing and development scenarios where you want to run Temporal in-process without managing external infrastructure.

:::caution Not for production use

Embedded deployments with SQLite are suitable for **testing and development only**.
For production workloads, deploy Temporal as a service using [MySQL, PostgreSQL, or Cassandra](/temporal-service/persistence) as the persistence layer.

:::

## Reference implementation

The recommended way to run an embedded Temporal server is to use the Temporal CLI's dev server implementation as a reference.
The CLI's [devserver package](https://github.com/temporalio/cli/tree/main/internal/devserver) provides a complete implementation that handles:

- SQLite configuration and schema setup
- Namespace creation
- Service configuration
- Port allocation

You can study and adapt this implementation for your own embedded use case.

## Basic server API

The core API for embedding Temporal is `temporal.NewServer()`:

```go

    "go.temporal.io/server/temporal"
    "go.temporal.io/server/common/config"
)

server, err := temporal.NewServer(
    temporal.ForServices(temporal.DefaultServices),
    temporal.WithConfig(cfg),
    temporal.InterruptOn(temporal.InterruptCh()),
)
if err != nil {
    log.Fatal(err)
}

if err := server.Start(); err != nil {
    log.Fatal(err)
}
```

The challenge is building the `config.Config` struct correctly, especially for SQLite which requires:

1. **Schema setup** - SQLite databases need schema initialization via `sqliteschema.SetupSchema()`
2. **Namespace creation** - Namespaces can be pre-created via `sqliteschema.CreateNamespaces()`
3. **Service configuration** - All four services (frontend, history, matching, worker) need proper port configuration

## Configuration from file

For non-SQLite databases, you can load configuration from a YAML file:

```go
cfg, err := config.Load(
    config.WithConfigFile("/path/to/config.yaml"),
)
if err != nil {
    log.Fatal(err)
}

server, err := temporal.NewServer(
    temporal.ForServices(temporal.DefaultServices),
    temporal.WithConfig(cfg),
)
```

Or load from a directory with environment-specific files:

```go
cfg, err := config.Load(
    config.WithConfigDir("./config"),
    config.WithEnv("development"),
)
```

## Server options reference

The `temporal.NewServer()` function accepts options to customize the server.
See [Server Options Reference](/references/server-options) for the complete list.

Key options include:

| Option | Description |
|--------|-------------|
| `ForServices([]string)` | Services to run (default: frontend, history, matching, worker) |
| `WithConfig(*config.Config)` | Server configuration |
| `WithLogger(log.Logger)` | Custom logger |
| `WithAuthorizer(authorization.Authorizer)` | Custom authorization |
| `WithClaimMapper(func)` | Role/claim mapping for auth |
| `WithCustomMetricsHandler(metrics.Handler)` | Custom metrics handler |
| `WithDynamicConfigClient(dynamicconfig.Client)` | Runtime configuration |
| `InterruptOn(chan)` | Channel for graceful shutdown |

## SQLite limitations

SQLite is intended for testing and development only:

- **Single writer**: SQLite supports only one writer at a time, limiting write throughput
- **No durability in memory mode**: In-memory mode loses data on restart
- **Not scalable**: Cannot handle production workloads
- **Single shard**: Use `NumHistoryShards: 1` for SQLite

For production, use MySQL, PostgreSQL, or Cassandra with a properly scaled multi-node deployment.

## Examples

For complete working examples, see:

- [Temporal CLI dev server](https://github.com/temporalio/cli/tree/main/internal/devserver) - Reference implementation for SQLite embedding
- [samples-server repository](https://github.com/temporalio/samples-server) - Server extensibility examples:
  - [Authorizer](https://github.com/temporalio/samples-server/tree/main/extensibility/authorizer) - Custom authorization and claim mapping
  - [Metrics handler](https://github.com/temporalio/samples-server/tree/main/extensibility/metrics-handler) - Custom metrics handling
  - [TLS](https://github.com/temporalio/samples-server/tree/main/tls) - TLS configuration for secure communication
  - [Docker Compose](https://github.com/temporalio/samples-server/tree/main/compose) - Database configurations (PostgreSQL, MySQL, Cassandra)

## Related

- [Server Options Reference](/references/server-options)
- [Deployment](/self-hosted-guide/deployment)
- [Visibility Storage](/self-hosted-guide/visibility)

---

## Self-hosted Temporal Service guide

Welcome to the self-hosted Temporal Service guide. This guide shows you how to self-host open source infrastructure
software that orchestrates your durable applications.

:::tip Do you need a production Temporal Service?

If you're still developing and testing your application locally, you may not need a production Temporal Service. Use the
[Temporal CLI development server](/cli/command-reference/server#start-dev) — a single binary with no external dependencies:

`temporal server start-dev`

This starts a complete Temporal Service with Web UI on your local machine. We recommend this for local development
regardless of whether you plan to use Temporal Cloud or self-host in production. See the
[Temporal CLI server](/cli/command-reference/server) page for configuration options.

:::

## Plan and deploy your service

- [Deployment](/self-hosted-guide/deployment): Choose a deployment approach (Docker, Kubernetes, or manual) and set up a
  production-ready Temporal Service.
- [Embedded server](/self-hosted-guide/embedded-server): Run Temporal in-process as a Go library for local development
  and testing scenarios.
- [Defaults](/self-hosted-guide/defaults): Review platform limits and default settings that can affect Workflow and
  Activity behavior.
- [Production checklist](/self-hosted-guide/production-checklist): Validate readiness for scale, reliability,
  operations, and long-term maintainability.

## Operate your self-hosted service

- [Namespaces](/self-hosted-guide/namespaces): Create and manage Namespace isolation, retention, and related
  configuration.
- [Security](/self-hosted-guide/security): Configure TLS/mTLS, authentication, authorization, and related hardening
  controls.
- [Monitoring](/self-hosted-guide/monitoring): Collect and visualize service and SDK metrics to troubleshoot and track
  health.
- [Visibility](/self-hosted-guide/visibility): Configure Visibility storage so you can list, filter, and search Workflow
  Executions.
- [Upgrading server](/self-hosted-guide/upgrade-server#upgrade-server): Perform safe, sequential server and schema
  upgrades.

## Protect data and enable advanced features

- [Data encryption](/production-deployment/data-encryption): Use Payload Codecs and Codec Server patterns to protect
  sensitive Workflow data.
- [Archival](/self-hosted-guide/archival): Move closed Workflow Histories and Visibility records to blob storage for longer
  retention.
- [Multi-Cluster Replication](/self-hosted-guide/multi-cluster-replication): Replicate Workflow state across clusters
  for failover and disaster recovery.
- [Temporal Nexus](/production-deployment/self-hosted-guide/nexus): Enable Nexus in self-hosted environments to connect
  Temporal Applications across boundaries.

---

## Monitor Temporal Platform metrics

The Temporal Service and SDKs emit metrics that can be used to monitor performance and troubleshoot issues.
You can relay these metrics to any monitoring and observability platform.

This guide will provide an example of configuring [Prometheus](https://prometheus.io/) and [Grafana](https://grafana.com/) to work with the observability metrics emitted from Temporal.
This solution can work on its own, or serve as a baseline for you to further customize and integrate with other observability tooling.
For example, it is also possible to use the [OpenTelemetry Collector](https://temporal.io/code-exchange/temporal-opentelemetry) in your stack instead of scraping metrics directly with Prometheus, or [Datadog](#datadog) as a frontend instead of Grafana.

This configuration assumes that you have [Docker](https://www.docker.com/) installed and are running a [Temporal dev server](https://temporal.io/setup/start-development-server) via the CLI.

## Prometheus

This section discusses exporting metrics from Temporal SDKs, and setting up Prometheus to collect metrics on Temporal Service, Temporal Client, and Temporal Worker performance.

The Temporal Service and SDKs emit all metrics by default.
However, you must enable Prometheus in your application code (using the Temporal SDKs) and your Temporal Service configuration to collect the metrics emitted from your SDK and Temporal Service.

First, you'll need to create a `prometheus.yml` configuration file with some target ports to collect metrics from.
Here is a sample with one Temporal Service metrics target and two Temporal Worker (SDK) metrics targets:

```
global:
 scrape_interval: 10s
scrape_configs:
 - job_name: 'temporalmetrics'
   metrics_path: /metrics
   scheme: http
   static_configs:
     # Temporal Service metrics target
     - targets:
         - 'host.docker.internal:8000'
       labels:
         group: 'server-metrics'

     # Local app targets (set in SDK code)
     - targets:
         - 'host.docker.internal:8077'
         - 'host.docker.internal:8078'
       labels:
         group: 'sdk-metrics'
```

In this example, Prometheus is configured to scrape at 10-second intervals and to listen for Temporal Service metrics on `host.docker.internal:8000` and SDK metrics on two targets, `host.docker.internal:8077` and `host.docker.internal:8078`.
The `8077` and `8078` ports must be set on `WorkflowServiceStubs` in your application code with your preferred SDK -- there is an example of this in the next section.
You can set up as many targets as required.

:::info

For further Prometheus configuration options, refer to the [Prometheus documentation](https://prometheus.io/docs/prometheus/latest/configuration/configuration/).

:::

You can use Docker to run the official Prometheus image with this configuration:

```bash
docker run -p 9090:9090 -v /path/to/prometheus.yml /etc/prometheus/prometheus.yml prom/prometheus
```

Next, launch your Temporal dev server from the CLI with an additional `--metrics-port 8000` parameter:

```bash
temporal server start-dev --metrics-port 8000
```

:::info

Refer to the [Temporal Cluster configuration reference](/references/configuration#global) to expose metrics from a production service.

:::

You should now have both Prometheus and a Temporal Service running locally, with Temporal providing Service metrics to Prometheus.
Next, you'll want to configure SDK metrics as well.

### SDK metrics setup

SDK metrics are emitted by Temporal Workers and other Clients, and must be configured in your application code.
The Metrics section in the Observability guide details how to create hooks for all supported SDKs:

- [Go](/develop/go/platform/observability#metrics)
- [Java](/develop/java/platform/observability#metrics)
- [PHP](/develop/php/platform/observability)
- [Python](/develop/python/platform/observability#metrics)
- [TypeScript](/develop/typescript/platform/observability#metrics)
- [.NET](/develop/dotnet/platform/observability#metrics)
- [Ruby](/develop/ruby/platform/observability#metrics)

For end-to-end examples of how to expose metrics from each SDK, see the metrics samples:

- [Go SDK Sample](https://github.com/temporalio/samples-go/tree/main/metrics)
- [Java SDK Sample](https://github.com/temporalio/samples-java/tree/main/core/src/main/java/io/temporal/samples/metrics)
- [Python SDK Sample](https://github.com/temporalio/samples-python/tree/main/prometheus)
- [TypeScript SDK Sample](https://github.com/temporalio/samples-typescript/tree/main/interceptors-opentelemetry)
- [.NET SDK Sample](https://github.com/temporalio/samples-dotnet/tree/main/src/OpenTelemetry)

Some of these may require you to set different metrics port numbers based on the Prometheus example here, which is configured to scrape port `8077` and `8078` by default.
Follow the instructions from each of the samples to run Workflows and begin emitting metrics.
This will allow you to populate a dashboard in the next section and understand how to further customize Temporal observability for your needs.

### Verifying Prometheus configuration

Once your Workflows are running and emitting metrics, you can visit [http://localhost:9090/targets](http://localhost:9090/targets) on your local Prometheus instance to verify that it is able to scrape the provided endpoints.

![Prometheus scrape targets](/img/observability/prometheus-targets.png)

This example shows a response from the server metrics endpoint, provided by the Temporal dev server, and two SDK metrics endpoints, as defined in the Prometheus configuration.
To create this example, we used the Go and Python metrics samples, running on port 8077 and 8088 respectively.
If you are not pushing data to exactly 3 metrics endpoints, your environment may be different.

Next, you can visit the [local Prometheus query endpoint](http://localhost:9090/query) to manually run [PromQL](https://prometheus.io/docs/prometheus/latest/querying/basics/) queries on your exported metrics, or proceed to the next section to configure Grafana to generate dashboards from those metrics.

## Grafana

With [Prometheus](#prometheus) configured, deploy Grafana as a metrics frontend, and configure it to use Prometheus as a data source.

As before, you can use Docker to run the official Grafana image:

```bash
docker run -d -p 3000:3000 grafana/grafana-enterprise
```

This will deploy a Grafana instance with a default username and password of `admin`/`admin`.
In production, you would want to [configure authentication](https://grafana.com/docs/grafana/latest/setup-grafana/configure-security/configure-authentication/generic-oauth/) and control port access to Grafana.

:::info

For more information on how to customize your Grafana setup, see the [Grafana documentation](https://grafana.com/docs/grafana/latest/setup-grafana/).

:::

Next, configure Grafana to use Prometheus as the data source.
To do this, click on "Add new data source" from the "Connections" menu in the Grafana sidebar, and add Prometheus from the list.

You will be prompted to add additional configuration parameters.
If you are following this guide using Docker, use `http://host.docker.internal:9090` as the Prometheus address.
This is a [DNS name provided by Docker Desktop](https://docs.docker.com/desktop/features/networking/#use-cases-and-workarounds) which resolves to the internal IP address used by the host machine, and allows you to connect applications across Docker containers without additional configuration rules.
This is the only parameter you will need to set for your Prometheus configuration.
After providing it, scroll down to the "Save and Test" button, and you can validate Prometheus as a data source for this Grafana instance.

![Grafana data sources](/img/observability/grafana-data-sources.png)

In this example, Grafana is set to pull metrics from Prometheus at the port 9090, as defined in the Prometheus configuration.

Now, you'll just need to add some of our provided dashboards for visualizing Temporal metrics.

### Dashboard setup

We provide community-driven Grafana dashboards that can be used for monitoring Temporal Server and SDK metrics in a [dashboards](https://github.com/temporalio/dashboards/) repo.
Follow the instructions in that repo's README to import the dashboards to Grafana.

This way, you can create at least one dashboard for monitoring server metrics:

![Grafana server metrics](/img/observability/grafana-server-metrics.png)

And at least one other dashboard for monitoring SDK metrics:

![Grafana SDK metrics](/img/observability/grafana-sdk-metrics.png)

:::info

You can provide additional queries in your dashboard to report other data as needed.
For more details on configuring Grafana dashboards, see the [Grafana Dashboards documentation](https://grafana.com/docs/grafana/latest/dashboards/).

:::

From here, you can configure Grafana [Alerts](https://grafana.com/docs/grafana/latest/alerting/) for any monitored parameters, add custom metrics to your Temporal SDK code, and use these observability features to help scale your Temporal deployment.
Refer to the [Cluster metrics](/references/cluster-metrics) and [SDK metrics](/references/sdk-metrics) reference for more.

## Configuring Temporal Service health checks {/* #health-checks */}

The [Frontend Service](/temporal-service/temporal-server#frontend-service) supports TCP or [gRPC](https://github.com/grpc/grpc/blob/875066b61e3b57af4bb1d6e36aabe95a4f6ba4f7/src/proto/grpc/health/v1/health.proto#L45) health checks on port 7233.

If you use [Nomad](https://www.nomadproject.io/) to manage your containers, the [check stanza](https://developer.hashicorp.com/nomad/docs/job-specification/check) would look like this for TCP:

```
service {
  check {
    type     = "tcp"
    port     = 7233
    interval = "10s"
    timeout  = "2s"
  }
```

or like this for gRPC (requires Consul ≥ `1.0.5`):

```
service {
  check {
    type         = "grpc"
    port         = 7233
    interval     = "10s"
    timeout      = "2s"
  }
```

## Installing via Helm Chart

If you are installing and running Temporal via [Helm chart](https://github.com/temporalio/helm-charts), you can also [provide additional parameters](https://github.com/temporalio/helm-charts?tab=readme-ov-file#exploring-metrics-via-grafana) to populate and explore a Grafana dashboard out of the box.

## Datadog {/* #datadog */}

Datadog has a Temporal integration for collecting Temporal Service metrics.
Once you've [configured Prometheus](#prometheus), you can configure the [Datadog Agent](https://docs.datadoghq.com/integrations/temporal/).

If you are using [Temporal Cloud](/cloud/overview), you can also [integrate Datadog directly](https://docs.datadoghq.com/integrations/temporal-cloud/), without needing to use Prometheus.

---

## Self-hosted Multi-Cluster Replication

Multi-Cluster Replication is a feature which asynchronously replicates Workflow Executions from active Clusters to other passive Clusters, for backup and state reconstruction.
When necessary, for higher availability, Cluster operators can failover to any of the backup Clusters.

Temporal's Multi-Cluster Replication feature is considered **experimental** and not subject to normal [versioning and support policy](/temporal-service/temporal-server#versions-and-support).

Temporal automatically forwards Start, Signal, and Query requests to the active Cluster.
This feature must be enabled through a Dynamic Config flag per [Global Namespace](/global-namespace).

When the feature is enabled, Tasks are sent to the Parent Task Queue partition that matches that Namespace, if it exists.

All Visibility APIs can be used against active and standby Clusters.
This enables [Temporal UI](https://docs.temporal.io/web-ui) to work seamlessly for Global Namespaces.
Applications making API calls directly to the Temporal Visibility API continue to work even if a Global Namespace is in standby mode.
However, they might see a lag due to replication delay when querying the Workflow Execution state from a standby Cluster.

#### Namespace Versions

A _version_ is a concept in Multi-Cluster Replication that describes the chronological order of events per Namespace.

With Multi-Cluster Replication, all Namespace change events and Workflow Execution History events are replicated asynchronously for high throughput.
This means that data across clusters is **not** strongly consistent.
To guarantee that Namespace data and Workflow Execution data will achieve eventual consistency (especially when there is a data conflict during a failover), a **version** is introduced and attached to Namespaces.
All Workflow Execution History entries generated in a Namespace will also come with the version attached to that Namespace.

All participating Clusters are pre-configured with a unique initial version and a shared version increment:

- `initial version < shared version increment`

When performing failover for a Namespace from one Cluster to another Cluster, the version attached to the Namespace will be changed by the following rule:

- for all versions which follow `version % (shared version increment) == (active cluster's initial version)`, find the smallest version which has `version >= old version in namespace`
