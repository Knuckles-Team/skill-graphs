# LangSmith CLI
Source: https://docs.langchain.com/langsmith/langsmith-cli

Query and manage LangSmith projects, traces, runs, datasets, evaluators, experiments, and threads from the terminal

The LangSmith CLI is a command-line tool for querying and managing your LangSmith data. It's designed for both developers and AI coding agents and outputs JSON by default for scripting, with a `--format pretty` option for human-readable tables. Use it when you need scriptable access to your LangSmith data, such as bulk exports, automation, or giving a coding agent direct access to your [traces, runs, and datasets](/langsmith/observability-concepts).

<Warning>
  The LangSmith CLI is in **alpha**. Commands, flags, and output schemas may change between releases. Report issues on [GitHub](https://github.com/langchain-ai/langsmith-cli/issues).
</Warning>

## Install

<CodeGroup>
  ```bash macOS / Linux (recommended) theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  curl -fsSL https://cli.langsmith.com/install.sh | sh
  ```

  ```powershell Windows theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  irm https://cli.langsmith.com/install.ps1 | iex
  ```

  ```bash GitHub Releases theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  # Download the latest binary for your platform:
  # https://github.com/langchain-ai/langsmith-cli/releases
  ```

  ```bash Go install theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  go install github.com/langchain-ai/langsmith-cli/cmd/langsmith@latest
  ```
</CodeGroup>

To upgrade at any time:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
langsmith self-update
```

Use the `--dry-run` flag to preview the update without installing.

## Authenticate

`langsmith auth login` requires LangSmith CLI `v0.2.30` or later. `langsmith profile` commands require LangSmith CLI `v0.2.26` or later.

The recommended local setup is to authenticate with OAuth:

<Note>
  `langsmith auth login` currently supports LangSmith Cloud (SaaS) only. For self-hosted or other non-SaaS LangSmith endpoints, authenticate with an API key or create an API-key profile.
</Note>

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
langsmith auth login
```

This opens a browser-based authorization flow and stores OAuth tokens in `~/.langsmith/config.json` under the selected [profile](/langsmith/profile-configuration). Select a profile with `--profile` or `LANGSMITH_PROFILE`:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
langsmith auth login --profile dev
langsmith --profile dev project list
```

In headless environments, pass `--no-browser` and open the printed URL manually:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
langsmith auth login --no-browser --workspace-id <workspace-id>
```

To manage saved profiles:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
langsmith profile list
langsmith profile create dev --workspace-id <workspace-id> --set-current
langsmith profile use dev
langsmith profile set-workspace <workspace-id>
```

For the full profile configuration reference, see [Profile configuration](/langsmith/profile-configuration).

You can also authenticate with an API key directly.

Set your [API key](/langsmith/create-account-api-key) as an environment variable:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
export LANGSMITH_API_KEY="lsv2_..."
```

Optionally, set a default project for queries:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
export LANGSMITH_PROJECT="my-default-project"
```

If you're using LangSmith [self-hosted](/langsmith/self-hosted), also set the endpoint:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
export LANGSMITH_ENDPOINT="https://your-langsmith-instance.com"
```

Or, pass them as flags per command:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
langsmith --api-key lsv2_... trace list --project my-app
```

## Quickstart

The following commands cover the core resource types:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# List tracing projects
langsmith project list

# List recent traces in a project
langsmith trace list --project my-app --limit 5

# Get a specific trace with full detail
langsmith trace get <trace-id> --project my-app --full

# List LLM runs with token counts
langsmith run list --project my-app --run-type llm --include-metadata

# Datasets and experiments
langsmith dataset list
langsmith experiment list --dataset my-eval-set

# Conversation threads
langsmith thread list --project my-chatbot

# Sandboxes
langsmith sandbox list
langsmith sandbox tunnel my-vm --remote-port 5432
```

## Output formats

**Default**

JSON to stdout — easy to pipe, script, or feed to an agent:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
langsmith trace list --project my-app
```

**Pretty tables**

`--format pretty` for human-readable output:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
langsmith --format pretty trace list --project my-app
```

**Write to file**

`-o <path>`:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
langsmith trace list --project my-app -o traces.json
```

## Commands

Each command group targets a specific LangSmith resource. Most commands support `--limit`, `--offset`, and a shared set of [filter flags](#filter-flags).

### List projects

Returns up to 20 projects by default, sorted by most recent activity. Lists tracing projects only. (Use [`experiment list`](#view-experiments) to list evaluation experiments.)

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
langsmith project list
langsmith project list --limit 50 --name-contains chatbot
langsmith --format pretty project list
```

### Query traces

Defaults to the last 7 days, newest first. Use `--since` or `--last-n-minutes` to change the time window.

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
langsmith trace list --project my-app --limit 50 --last-n-minutes 60
langsmith trace list --project my-app --error                     # errors only
langsmith trace list --project my-app --min-latency 5             # slow traces (>5s)
langsmith trace list --project my-app --tags production           # filter by tag
langsmith trace list --project my-app --full                      # all fields
langsmith trace list --project my-app --show-hierarchy --limit 3  # include full run tree
langsmith trace get <trace-id> --project my-app --full
langsmith trace export ./traces --project my-app --limit 20 --full
```

### Query runs

Defaults to 50 results (most other commands default to 20). The same 7-day time window applies. Use `--since` or `--last-n-minutes` to override.

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
langsmith run list --project my-app --run-type llm
langsmith run list --project my-app --run-type tool --name search
langsmith run list --project my-app --min-tokens 1000 --include-metadata
langsmith run get <run-id> --full
langsmith run export llm_calls.jsonl --project my-app --run-type llm --full
```

### Query threads

`--project` is required for all thread commands.

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
langsmith thread list --project my-chatbot --last-n-minutes 120
langsmith thread get <thread-id> --project my-chatbot --full
```

### Manage datasets

`dataset export` exports the examples (rows) within a dataset, not the dataset metadata itself.

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
langsmith dataset list
langsmith dataset list --name-contains eval
langsmith dataset get my-dataset
langsmith dataset create --name my-eval-set --description "QA pairs for v2"
langsmith dataset delete my-old-dataset --yes
langsmith dataset export my-dataset ./data.json --limit 500
langsmith dataset upload data.json --name new-dataset
```

### Manage examples

Use `--split` to assign examples to named splits (such as `test` or `train`) when creating or listing.

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
langsmith example list --dataset my-dataset --limit 50
langsmith example list --dataset my-dataset --split test
langsmith example create --dataset my-dataset \
  --inputs '{"question": "What is LangSmith?"}' \
  --outputs '{"answer": "A platform for LLM observability"}' \
  --split test
langsmith example delete <example-id> --yes
```

### Manage evaluators

Evaluators can be offline (run against a dataset during experiments) or online (run against a live project). Use `--sampling-rate` to evaluate only a fraction of production runs, and `--replace` to overwrite an existing evaluator by name.

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
langsmith evaluator list
langsmith evaluator upload evals.py --name accuracy \
  --function check_accuracy --dataset my-eval-set
langsmith evaluator upload evals.py --name latency-check \
  --function check_latency --project my-app --sampling-rate 0.5
langsmith evaluator upload evals.py --name accuracy \
  --function check_accuracy_v2 --dataset my-eval-set --replace --yes
langsmith evaluator delete accuracy --yes
```

### View experiments

`experiment list` shows evaluation experiments, not tracing projects. (Use [`project list`](#list-projects) to list tracing projects.)

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
langsmith experiment list
langsmith experiment list --dataset my-eval-set
langsmith experiment get my-experiment-2024-01-15
```

### Manage sandboxes

Sandbox commands let you build snapshots, create sandboxes, execute commands, open interactive consoles, and tunnel TCP ports to services running inside sandboxes.

See [Sandbox CLI](/langsmith/sandbox-cli) for the full sandbox command reference.

### Call the LangSmith API directly

The `api` command is an authenticated, scriptable wrapper around the raw LangSmith REST API — useful for endpoints the typed commands above don't cover, or for piping JSON into and out of shell scripts. It's modeled after `gh api` and `curl`: pass the path as the only positional argument, and use `-X` to set the HTTP method (defaults to `GET`). Auth headers (`x-api-key`, `x-tenant-id`) are injected automatically.

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# GET (default method) — query string supported in the path
langsmith api sessions?limit=5

# Discover endpoints from the OpenAPI spec
langsmith api ls --tag datasets
langsmith api info GET sessions

# Typed JSON fields with -F (numbers, booleans, null, objects, arrays parsed as JSON)

# Method auto-promotes to POST when -F/-f/--input/--body is supplied
langsmith api runs/query -F session_id=abc -F limit=10

# String-typed fields with -f (always sent as a JSON string, even if numeric)
langsmith api datasets -f name=my-dataset -f description="QA pairs"

# Other HTTP methods via -X
langsmith api sessions/abc-123 -X DELETE

# Send a request body from a file or stdin
langsmith api datasets --input create-dataset.json
echo '{"name":"test"}' | langsmith api sessions --input -

# Force GET with fields — fields go to the query string instead of a body
langsmith api runs -X GET -F limit=5 -F session=abc

# Inspect response status + headers
langsmith api sessions --include

# Add custom headers
langsmith api sessions -H "Accept: text/csv"
```

Key flags:

| Flag          | Short | Default | Description                                                                               |
| ------------- | ----- | ------- | ----------------------------------------------------------------------------------------- |
| `--method`    | `-X`  | `GET`   | HTTP method                                                                               |
| `--field`     | `-F`  | —       | Typed JSON field as `key=value`. Repeatable. Use `@<path>` or `@-` for file/stdin values. |
| `--raw-field` | `-f`  | —       | String JSON field as `key=value`. Repeatable.                                             |
| `--input`     | —     | —       | File to use as the request body (`-` for stdin)                                           |
| `--body`      | —     | —       | Raw request body (JSON string, `@file`, or `@-` for stdin)                                |
| `--header`    | `-H`  | —       | Additional headers as `Key:Value`. Repeatable.                                            |
| `--include`   | `-i`  | `false` | Print response status line and headers before body                                        |

`--input` and `--body` are mutually exclusive. Subcommands `langsmith api ls` and `langsmith api info` browse and describe endpoints from the cached OpenAPI spec — pass `--refresh` to re-fetch.

## Filter flags

Most `trace` and `run` commands share these filters:

| Flag                              | Description                      | Example                          |
| --------------------------------- | -------------------------------- | -------------------------------- |
| `--project`                       | Project name                     | `--project my-app`               |
| `--limit, -n`                     | Max results                      | `-n 10`                          |
| `--offset`                        | Pagination offset                | `--offset 20`                    |
| `--last-n-minutes`                | Override the 7-day default       | `--last-n-minutes 60`            |
| `--since`                         | After ISO timestamp              | `--since 2024-01-15T00:00:00Z`   |
| `--error` / `--no-error`          | Filter by error status           | `--error`                        |
| `--name`                          | Name search (case-insensitive)   | `--name ChatOpenAI`              |
| `--run-type`                      | Run type (`llm` or `tool`)       | `--run-type llm`                 |
| `--min-latency` / `--max-latency` | Latency range in seconds         | `--min-latency 2.5`              |
| `--min-tokens`                    | Minimum total tokens             | `--min-tokens 1000`              |
| `--tags`                          | Tags, comma-separated (OR logic) | `--tags prod,v2`                 |
| `--filter`                        | Raw LangSmith filter DSL         | `--filter 'eq(status, "error")'` |
| `--trace-ids`                     | Specific trace IDs               | `--trace-ids abc123,def456`      |

**Detail flags** — control which fields are included in the response:

| Flag                 | Adds                            |
| -------------------- | ------------------------------- |
| `--include-metadata` | Status, duration, tokens, costs |
| `--include-io`       | Inputs, outputs, error          |
| `--include-feedback` | Feedback stats                  |
| `--full`             | All of the above                |
| `--show-hierarchy`   | Full run tree (traces only)     |

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/langsmith-cli.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Configure your collector for LangSmith telemetry
Source: https://docs.langchain.com/langsmith/langsmith-collector

The various services in a LangSmith deployment emit telemetry data in the form of logs, metrics, and traces. You may already have telemetry collectors set up in your Kubernetes cluster, or would like to deploy one to monitor your application.

This page describes how to configure an [OTel Collector](https://opentelemetry.io/docs/collector/configuration/) to gather telemetry data from LangSmith. Note that all of the concepts discussed below can be translated to other collectors such as [Fluentd](https://www.fluentd.org/) or [FluentBit](https://fluentbit.io/).

<Warning>
  **This section is only applicable for Kubernetes deployments.**
</Warning>

# Receivers

## Logs

This is an example for a ***Sidecar*** collector to read logs from its own pod, excluding logs from non domain-specific containers. A Sidecar configuration is useful here because we require access to every container's filesystem. A DaemonSet can also be used.

```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
filelog:
  exclude:
    - "**/otc-container/*.log"
  include:
    - /var/log/pods/${POD_NAMESPACE}_${POD_NAME}_${POD_UID}/*/*.log
  include_file_name: false
  include_file_path: true
  operators:
    - id: container-parser
      type: container
  retry_on_failure:
    enabled: true
  start_at: end
env:
  - name: POD_NAME
    valueFrom:
      fieldRef:
        fieldPath: metadata.name
  - name: POD_NAMESPACE
    valueFrom:
      fieldRef:
        fieldPath: metadata.namespace
  - name: POD_UID
    valueFrom:
      fieldRef:
        fieldPath: metadata.uid
volumes:
  - name: varlogpods
    hostPath:
      path: /var/log/pods
volumeMounts:
  - name: varlogpods
    mountPath: /var/log/pods
    readOnly: true
```

<Info>
  **This configuration requires 'get', 'list', and 'watch' permissions on pods in the given namespace.**
</Info>

## Metrics

Metrics can be scraped using the Prometheus endpoints. A single instance ***Gateway*** collector can be used to avoid duplication of queries when fetching metrics. The following config scrapes all of the default named LangSmith services:

```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
prometheus:
  config:
    scrape_configs:
      - job_name: langsmith-services
        metrics_path: /metrics
        scrape_interval: 15s
        # Only scrape endpoints in the LangSmith namespace
        kubernetes_sd_configs:
          - role: endpoints
            namespaces:
              names: [<langsmith-namespace>]
        relabel_configs:
          # Only scrape services with the name langsmith-.*
          - source_labels: [__meta_kubernetes_service_name]
            regex: "langsmith-.*"
            action: keep
          # Only scrape ports with the following names
          - source_labels: [__meta_kubernetes_endpoint_port_name]
            regex: "(backend|platform|playground|redis-metrics|postgres-metrics|metrics)"
            action: keep
          # Promote useful metadata into regular labels
          - source_labels: [__meta_kubernetes_service_name]
            target_label: k8s_service
          - source_labels: [__meta_kubernetes_pod_name]
            target_label: k8s_pod
          # Replace the default "host:port" as Prom's instance label
          - source_labels: [__address__]
            target_label: instance
```

<Info>
  **This configuration requires 'get', 'list', and 'watch' permissions on pods, services and endpoints in the given namespace.**
</Info>

### Traces

For traces, you need to enable the OTLP receiver. The following configuration can be used to listen to HTTP traces on port 4318, and GRPC on port 4317:

```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
otlp:
  protocols:
    grpc:
      endpoint: 0.0.0.0:4317
    http:
      endpoint: 0.0.0.0:4318
```

## Processors

### Recommended OTEL processors

The following processors are recommended when using the OTel collector:

* [Batch Processor](https://github.com/open-telemetry/opentelemetry-collector/blob/main/processor/batchprocessor/README.md): Groups the data into batches before sending to exporters.
* [Memory Limiter](https://github.com/open-telemetry/opentelemetry-collector/blob/main/processor/memorylimiterprocessor/README.md): Prevents the collector from using too much memory and crashing. When the soft limit is crossed, the collector stops accepting new data.
* [Kubernetes Attributes Processor](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/processor/k8sattributesprocessor): Adds Kubernetes metadata such as pod name into the telemetry data.

## Exporters

Exporters just need to point to an external endpoint of your liking. The following configuration allows you to configure a separate endpoint for logs, metrics and traces:

```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
otlphttp/logs:
  endpoint: <your_logs_endpoint>
otlphttp/metrics:
  endpoint: <your_metrics_endpoint>
otlphttp/traces:
  endpoint: <your_traces_endpoint>
```

<Note>
  **The OTel Collector also supports exporting directly to a [Datadog](https://docs.datadoghq.com/opentelemetry/setup/collector_exporter) endpoint.**
</Note>

# Example collector configuration: Logs sidecar

```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
mode: sidecar
image: otel/opentelemetry-collector-contrib
config:
  receivers:
    filelog:
      exclude:
        - "**/otc-container/*.log"
      include:
        - /var/log/pods/${POD_NAMESPACE}_${POD_NAME}_${POD_UID}/*/*.log
      include_file_name: false
      include_file_path: true
      operators:
        - id: container-parser
          type: container
      retry_on_failure:
        enabled: true
      start_at: end
  processors:
    batch:
      send_batch_size: 8192
      timeout: 10s
    memory_limiter:
      check_interval: 1m
      limit_percentage: 90
      spike_limit_percentage: 80
  exporters:
    otlphttp/logs:
      endpoint: <your-endpoint>
  service:
    pipelines:
      logs/langsmith:
        receivers: [filelog]
        processors: [batch, memory_limiter]
        exporters: [otlphttp/logs]
env:
  - name: POD_NAME
    valueFrom:
      fieldRef:
        fieldPath: metadata.name
  - name: POD_NAMESPACE
    valueFrom:
      fieldRef:
        fieldPath: metadata.namespace
  - name: POD_UID
    valueFrom:
      fieldRef:
        fieldPath: metadata.uid
volumes:
  - name: varlogpods
    hostPath:
      path: /var/log/pods
volumeMounts:
  - name: varlogpods
    mountPath: /var/log/pods
    readOnly: true
```

# Example collector configuration: Metrics and traces Gateway

```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
mode: deployment
image: otel/opentelemetry-collector-contrib
config:
  receivers:
    prometheus:
      config:
        scrape_configs:
          - job_name: langsmith-services
            metrics_path: /metrics
            scrape_interval: 15s
            # Only scrape endpoints in the LangSmith namespace
            kubernetes_sd_configs:
              - role: endpoints
                namespaces:
                  names: [<langsmith-namespace>]
            relabel_configs:
              # Only scrape services with the name langsmith-.*
              - source_labels: [__meta_kubernetes_service_name]
                regex: "langsmith-.*"
                action: keep
              # Only scrape ports with the following names
              - source_labels: [__meta_kubernetes_endpoint_port_name]
                regex: "(backend|platform|playground|redis-metrics|postgres-metrics|metrics)"
                action: keep
              # Promote useful metadata into regular labels
              - source_labels: [__meta_kubernetes_service_name]
                target_label: k8s_service
              - source_labels: [__meta_kubernetes_pod_name]
                target_label: k8s_pod
              # Replace the default "host:port" as Prom's instance label
              - source_labels: [__address__]
                target_label: instance
    otlp:
      protocols:
        grpc:
          endpoint: 0.0.0.0:4317
        http:
          endpoint: 0.0.0.0:4318
  processors:
    batch:
      send_batch_size: 8192
      timeout: 10s
    memory_limiter:
      check_interval: 1m
      limit_percentage: 90
      spike_limit_percentage: 80
  exporters:
    otlphttp/metrics:
      endpoint: <metrics_endpoint>
    otlphttp/traces:
      endpoint: <traces_endpoint>
  service:
    pipelines:
      metrics/langsmith:
        receivers: [prometheus]
        processors: [batch, memory_limiter]
        exporters: [otlphttp/metrics]
      traces/langsmith:
        receivers: [otlp]
        processors: [batch, memory_limiter]
        exporters: [otlphttp/traces]
```

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/langsmith-collector.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# LangSmith-managed ClickHouse
Source: https://docs.langchain.com/langsmith/langsmith-managed-clickhouse

<Check>
  Please read the [LangSmith architectural overview](/langsmith/self-hosted) and [guide on connecting to external ClickHouse](/langsmith/self-host-external-clickhouse) before proceeding with this guide.
</Check>

LangSmith uses ClickHouse as the primary storage engine for **traces** and **feedback**. For easier management and scaling, it is recommended to connect a self-hosted LangSmith instance to an external ClickHouse instance. LangSmith-managed ClickHouse is an option that allows you to use a fully managed ClickHouse instance that is monitored and maintained by the LangSmith team.

## Architecture overview

The architecture of using LangSmith-managed ClickHouse with your self-hosted LangSmith instance is similar to using a fully self-hosted ClickHouse instance, with a few key differences:

* You will need to set up a private network connection between your LangSmith instance and the LangSmith-managed ClickHouse instance. This is to ensure that your data is secure and that you can connect to the ClickHouse instance from your self-hosted LangSmith instance.
* With this option, sensitive information (inputs and outputs) of your traces will be stored in cloud object storage (S3 or GCS) within your cloud instead of ClickHouse to ensure that sensitive information doesn't leave your VPC. For more details on where particular data fields are stored, refer to [Data storage](#data-storage).
* The LangSmith team will monitor your ClickHouse instance and ensure that it is running smoothly. This allows us to track metrics like run-ingestion delay and query performance.

The overall architecture looks like this:

<img alt="LangSmith managed ClickHouse architecture." />

<img alt="LangSmith managed ClickHouse architecture." />

## Requirements

* **You must use a supported blob storage option.** Read the [blob storage guide](/langsmith/self-host-blob-storage) for more information.
* To use private endpoints, ensure that your VPC is in a ClickHouse Cloud supported [region](https://clickhouse.com/docs/en/cloud/reference/supported-regions). Otherwise, you will need to use a public endpoint we will secure with firewall rules. Your VPC will need to have a NAT gateway to allow us to allowlist your traffic.
* You must have a VPC that can connect to the LangSmith-managed ClickHouse service. You will need to work with our team to set up the necessary networking.
* You must have a LangSmith self-hosted instance running. You can use our managed ClickHouse service with [Kubernetes](/langsmith/kubernetes) installations.

## Data storage

ClickHouse stores **runs** and **feedback** data, specifically:

* All feedback data fields.
* Some run data fields.

For a list of fields, refer to [Stored run data fields](#stored-run-data-fields) and [Stored feedback data fields](#stored-feedback-data-fields).

LangChain defines sensitive application data as `inputs`, `outputs`, `errors`, `manifests`, `extras`, and `events` of a run, since these fields may contain LLM prompts and completions. With LangSmith-managed ClickHouse, these sensitive fields are stored in cloud object storage (S3 or GCS) within your cloud, while the rest of the run data is stored in ClickHouse, ensuring sensitive information never leaves your VPC.

### Stored feedback data fields

<Note>
  Because all feedback data is stored in ClickHouse, do not send sensitive information in feedback (scores and annotations/comments) or in any other run fields that are mentioned in [Stored run data fields](#stored-run-data-fields).
</Note>

Using a LangSmith-managed ClickHouse setup, **all feedback data fields are stored in ClickHouse**:

| Field Name                 | Type     | Description                                                                                            |
| -------------------------- | -------- | ------------------------------------------------------------------------------------------------------ |
| `id`                       | UUID     | Unique identifier for the record itself                                                                |
| `created_at`               | datetime | Timestamp when the record was created                                                                  |
| `modified_at`              | datetime | Timestamp when the record was last modified                                                            |
| `session_id`               | UUID     | Unique identifier for the experiment or tracing project the run was a part of                          |
| `run_id`                   | UUID     | Unique identifier for a specific run within a session                                                  |
| `key`                      | string   | A key describing the criteria of the feedback, e.g. `'correctness'`                                    |
| `score`                    | number   | Numerical score associated with the feedback key                                                       |
| `value`                    | string   | Reserved for storing a value associated with the score. Useful for categorical feedback.               |
| `comment`                  | string   | Any comment or annotation associated with the record. This can be a justification for the score given. |
| `correction`               | object   | Reserved for storing correction details, if any                                                        |
| `feedback_source`          | object   | Object containing information about the feedback source                                                |
| `feedback_source.type`     | string   | The type of source where the feedback originated, e.g. `'api'`, `'app'`, `'evaluator'`                 |
| `feedback_source.metadata` | object   | Reserved for additional metadata, currently                                                            |
| `feedback_source.user_id`  | UUID     | Unique identifier for the user providing feedback                                                      |

This [reference doc](/langsmith/feedback-data-format) explains the stored feedback format, which is the LangSmith's way of representing evaluation scores and annotations on runs.

### Stored run data fields

Run data fields are split between the managed ClickHouse database and your cloud object storage (e.g., S3 or GCS).

<Note>
  For run fields stored in object storage, only a reference or pointer is kept in ClickHouse. For example, `inputs` and `outputs` content are offloaded to S3/GCS, with the ClickHouse record storing corresponding S3 URLs in the `inputs_s3_urls` and `outputs_s3_urls` fields.
</Note>

The table details each run field and where it is stored:

| Field                          | Storage Location   |
| ------------------------------ | ------------------ |
| `id`                           | ClickHouse         |
| `name`                         | ClickHouse         |
| `inputs`                       | **Object Storage** |
| `run_type`                     | ClickHouse         |
| `start_time`                   | ClickHouse         |
| `end_time`                     | ClickHouse         |
| `extra`                        | **Object Storage** |
| `error`                        | **Object Storage** |
| `outputs`                      | **Object Storage** |
| `events`                       | **Object Storage** |
| `tags`                         | ClickHouse         |
| `trace_id`                     | ClickHouse         |
| `dotted_order`                 | ClickHouse         |
| `status`                       | ClickHouse         |
| `child_run_ids`                | ClickHouse         |
| `direct_child_run_ids`         | ClickHouse         |
| `parent_run_ids`               | ClickHouse         |
| `feedback_stats`               | ClickHouse         |
| `reference_example_id`         | ClickHouse         |
| `total_tokens`                 | ClickHouse         |
| `prompt_tokens`                | ClickHouse         |
| `completion_tokens`            | ClickHouse         |
| `total_cost`                   | ClickHouse         |
| `prompt_cost`                  | ClickHouse         |
| `completion_cost`              | ClickHouse         |
| `first_token_time`             | ClickHouse         |
| `session_id`                   | ClickHouse         |
| `in_dataset`                   | ClickHouse         |
| `parent_run_id`                | ClickHouse         |
| `execution_order` (deprecated) | ClickHouse         |
| `serialized`                   | ClickHouse         |
| `manifest_id` (deprecated)     | ClickHouse         |
| `manifest_s3_id`               | ClickHouse         |
| `inputs_s3_urls`               | ClickHouse         |
| `outputs_s3_urls`              | ClickHouse         |
| `price_model_id`               | ClickHouse         |
| `app_path`                     | ClickHouse         |
| `last_queued_at`               | ClickHouse         |
| `share_token`                  | ClickHouse         |

This [reference doc](/langsmith/run-data-format) explains the format of stored runs (spans), which are the building blocks of traces.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/langsmith-managed-clickhouse.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
