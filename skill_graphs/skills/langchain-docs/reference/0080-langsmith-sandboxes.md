# LangSmith Sandboxes
Source: https://docs.langchain.com/langsmith/sandboxes

Use LangSmith managed sandboxes to safely execute code and interact with the filesystem in isolated environments.

Sandboxes are isolated environments that allow agents to safely execute potentially risky operations, like running arbitrary code or interacting with the filesystem, without affecting your main infrastructure.

From the [LangSmith homepage](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-sandboxes), select **Sandboxes** to manage all your sandbox resources.

<img alt="Sandboxes overview page" />

## Environment availability

| Environment                           | Status              |
| ------------------------------------- | ------------------- |
| GCP US (`smith.langchain.com`)        | Generally available |
| GCP EU (`eu.smith.langchain.com`)     | Generally available |
| GCP APAC (`apac.smith.langchain.com`) | Generally available |
| AWS US (`aws.smith.langchain.com`)    | In development      |

## Get started

### 1. Install the SDK

<CodeGroup>
  ```bash Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  # uv
  uv add "langsmith[sandbox]"

  # pip
  pip install "langsmith[sandbox]"
  ```

  ```bash TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  npm install langsmith
  ```
</CodeGroup>

### 2. Set your API key

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
export LANGSMITH_API_KEY="<your-api-key>"
```

### 3. Create and run a sandbox

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langsmith.sandbox import SandboxClient

  client = SandboxClient()

  with client.sandbox() as sb:
      result = sb.run("python -c 'print(2 + 2)'")
      print(result.stdout)  # "4\n"
  ```

  ```ts TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { SandboxClient } from "langsmith/sandbox";

  const client = new SandboxClient();
  const sandbox = await client.createSandbox();
  const result = await sandbox.run("node -e 'console.log(2 + 2)'");
  console.log(result.stdout); // "4\n"
  await sandbox.delete();
  ```
</CodeGroup>

<Tip>
  Prefer the command line? The [Sandbox CLI](/langsmith/sandbox-cli) lets you create sandboxes, run commands, and open interactive shells without writing any code.
</Tip>

### 4. Use sandboxes with your agents

To wire sandboxes into agent code, see the Open Source docs:

* **Deep Agents**: [Use `LangSmithSandbox` as a backend](/oss/python/integrations/sandboxes/langsmith), covering installation, backend creation, and cleanup.
* **Sandboxes as agent backends**: [Configure any sandbox as the execution backend](/oss/python/deepagents/sandboxes) to give your agent `execute` and filesystem tools automatically.
* **LangChain / LangGraph integrations**: [Connect third-party providers](/oss/python/integrations/sandboxes) such as Daytona and Modal, or use LangSmith sandboxes as a first-party option.

## Resources

<CardGroup>
  <Card title="Snapshots" icon="camera" href="/langsmith/sandbox-snapshots">
    Build filesystem images from Docker images or capture a running sandbox, then boot sandboxes from them.
  </Card>

  <Card title="Service URLs" icon="globe" href="/langsmith/sandbox-service-urls">
    Access HTTP services running inside sandboxes via authenticated URLs.
  </Card>

  <Card title="Auth proxy" icon="shield-lock" href="/langsmith/sandbox-auth-proxy">
    Inject credentials into outbound API requests without hardcoding secrets.
  </Card>

  <Card title="Permissions" icon="user-lock" href="/langsmith/sandbox-permissions">
    Control which workspace members can interact with a sandbox after it is created.
  </Card>

  <Card title="CLI" icon="terminal-2" href="/langsmith/sandbox-cli">
    Build snapshots, manage sandboxes, open consoles, and tunnel TCP ports from the command line.
  </Card>

  <Card title="SDK usage" icon="code" href="/langsmith/sandbox-sdk">
    Create and manage sandboxes programmatically with the Python or TypeScript SDK.
  </Card>

  <Card title="Harbor" icon="flask" href="/langsmith/sandbox-harbor">
    Run Harbor evaluations and rollouts on LangSmith sandboxes.
  </Card>
</CardGroup>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/sandboxes.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Scalability & resilience
Source: https://docs.langchain.com/langsmith/scalability-and-resilience

LangSmith is designed to scale horizontally with your workload. Each instance of the service is stateless, and keeps no resources in memory. The service is designed to gracefully handle new instances being added or removed, including hard shutdown cases.

## Server scalability

As you add more instances to a service, they will share the HTTP load as long as an appropriate load balancer mechanism is placed in front of them. In most deployment modalities we configure a load balancer for the service automatically. In the “self-hosted without control plane” modality it’s your responsibility to add a load balancer. Since the instances are stateless any load balancing strategy will work, no session stickiness is needed, or recommended. Any instance of the server can communicate with any queue instance (through Redis PubSub), meaning that requests to cancel or stream an in-progress run can be handled by any arbitrary instance.

## Queue scalability

As you add more instances to a service, they will increase run throughput linearly, as each instance is configured to handle a set number of concurrent runs (by default 10). Each attempt for each run will be handled by a single instance, with exactly-once semantics enforced through Postgres’s MVCC model (refer to section below for crash resilience details). Attempts that fail due to transient database errors are retried up to 3 times. We do not make use of long-lived transactions or locks, this enables us to make more efficient use of Postgres resources.

## Resilience

While a run is being handled by a queue instance, a periodic heartbeat timestamp will be recorded in Redis by that queue worker.

When a graceful shutdown request is received (SIGINT) an instance enters shutdown mode, which

* stops accepting new HTTP requests
* gives any in-progress runs a limited number of seconds to finish (if not finished it will be put back in the queue)
* stops the instance from picking up more runs from the queue

If a hard shutdown occurs due to a server crash or an infrastructure failure, any runs that were in progress will be picked up by an internal sweeper task that looks for in-progress runs that have breached their heartbeat window. The sweeper runs every 2 minutes and will put the runs back in the queue for another instance to pick them up.

## Postgres resilience

For deployment modalities where we manage the Postgres database, we have periodic backups and continuously replicated standby replicas for automatic failover. This Postgres configuration is available in the [Cloud deployment option](/langsmith/cloud) for [`Production` deployment types](/langsmith/control-plane#deployment-types) only.

All communication with Postgres implements retries for retry-able errors. If Postgres is momentarily unavailable, such as during a database restart, most/all traffic should continue to succeed. Prolonged failure of Postgres will render the Agent Server unavailable.

## Redis resilience

All data that requires durable storage is stored in Postgres, not Redis. Redis is used only for ephemeral metadata, and communication between instances. Therefore we place no durability requirements on Redis.

All communication with Redis implements retries for retry-able errors. If Redis is momentarily unavailable, such as during a database restart, most/all traffic should continue to succeed. Prolonged failure of Redis will render the Agent Server unavailable.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/scalability-and-resilience.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Delete workspaces
Source: https://docs.langchain.com/langsmith/script-delete-a-workspace

<Note>
  Deleting a workspace is supported **nativley in LangSmith Self-Hosted v0.10**. View [instructions for deleting a workspace](/langsmith/set-up-hierarchy#delete-a-workspace).

  Follow the guide below for Self-Hosted versions before v0.10.
</Note>

The LangSmith UI does not currently support the deletion of an individual workspace from an organization. This, however, can be accomplished by directly removing all traces from all materialized views in ClickHouse (except the runs\_history views) and the runs and feedbacks tables and then removing the Workspace from the Postgres tenants table.

This command using the Workspace ID as an argument.

### Prerequisites

Ensure you have the following tools/items ready.

1. kubectl

   * [https://kubernetes.io/docs/tasks/tools/](https://kubernetes.io/docs/tasks/tools/)

2. PostgreSQL client

   * [https://www.postgresql.org/download/](https://www.postgresql.org/download/)

3. PostgreSQL database connection:

   * Host
   * Port
   * Username
     * If using the bundled version, this is `postgres`
   * Password
     * If using the bundled version, this is `postgres`
   * Database name
     * If using the bundled version, this is `postgres`

4. Clickhouse database credentials

   * Host
   * Port
   * Username
     * If using the bundled version, this is `default`
   * Password
     * If using the bundled version, this is `password`
   * Database name
     * If using the bundled version, this is `default`

5. Connectivity to the PostgreSQL database from the machine you will be running the migration script on.

   * If you are using the bundled version, you may need to port forward the postgresql service to your local machine.
   * Run `kubectl port-forward svc/langsmith-postgres 5432:5432` to port forward the postgresql service to your local machine.

6. Connectivity to the Clickhouse database from the machine you will be running the migration script on.

   * If you are using the bundled version, you may need to port forward the clickhouse service to your local machine.
     * Run `kubectl port-forward svc/langsmith-clickhouse 8123:8123` to port forward the clickhouse service to your local machine.
   * If you are using Clickhouse Cloud you will want to specify the --ssl flag and use port `8443`

7. The script to delete a workspace

   * Download the [workspace script](https://github.com/langchain-ai/helm/blob/main/charts/langsmith/scripts/delete_workspace.sh)

### Running the deletion script for a single workspace

Run the following command to run the workspace removal script:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
sh delete_workspace.sh <postgres_url> <clickhouse_url> --workspace_id <workspace_id>
```

For example, if you are using the bundled version with port-forwarding, the command would look like:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
sh delete_workspace.sh "postgres://postgres:postgres@localhost:5432/postgres" "clickhouse://default:password@localhost:8123/default" --workspace_id 4ec70ec7-0808-416a-b836-7100aeec934b
```

If you visit the LangSmith UI, you should now see workspace is deleted.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/script-delete-a-workspace.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Delete organizations
Source: https://docs.langchain.com/langsmith/script-delete-an-organization

The LangSmith UI does not currently support the deletion of an individual organization from a self-hosted instance of LangSmith. This, however, can be accomplished by directly removing all traces from all materialized views in ClickHouse (except the runs\_history views) and the runs and feedbacks tables and then removing the Organization from the Postgres tenants table.

This command using the Organization ID as an argument.

### Prerequisites

Ensure you have the following tools/items ready.

1. kubectl

   * [https://kubernetes.io/docs/tasks/tools/](https://kubernetes.io/docs/tasks/tools/)

2. PostgreSQL client

   * [https://www.postgresql.org/download/](https://www.postgresql.org/download/)

3. PostgreSQL database connection:

   * Host
   * Port
   * Username
     * If using the bundled version, this is `postgres`
   * Password
     * If using the bundled version, this is `postgres`
   * Database name
     * If using the bundled version, this is `postgres`

4. Clickhouse database credentials

   * Host
   * Port
   * Username
     * If using the bundled version, this is `default`
   * Password
     * If using the bundled version, this is `password`
   * Database name
     * If using the bundled version, this is `default`

5. Connectivity to the PostgreSQL database from the machine you will be running the migration script on.

   * If you are using the bundled version, you may need to port forward the postgresql service to your local machine.
   * Run `kubectl port-forward svc/langsmith-postgres 5432:5432` to port forward the postgresql service to your local machine.

6. Connectivity to the Clickhouse database from the machine you will be running the migration script on.

   * If you are using the bundled version, you may need to port forward the clickhouse service to your local machine.
     * Run `kubectl port-forward svc/langsmith-clickhouse 8123:8123` to port forward the clickhouse service to your local machine.
   * If you are using Clickhouse Cloud you will want to specify the --ssl flag and use port `8443`

7. The script to delete an organization

   * Download the [delete organization script](https://github.com/langchain-ai/helm/blob/main/charts/langsmith/scripts/delete_organization_sh)

### Running the deletion script for a single organization

Run the following command to run the organization removal script:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
sh delete_organization.sh <postgres_url> <clickhouse_url> --organization_id <organization_id>
```

For example, if you are using the bundled version with port-forwarding, the command would look like:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
sh delete_organization.sh "postgres://postgres:postgres@localhost:5432/postgres" "clickhouse://default:password@localhost:8123/default" --organization_id 4ec70ec7-0808-416a-b836-7100aeec934b
```

If you visit the LangSmith UI, you should now see organization is no longer present.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/script-delete-an-organization.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Delete traces
Source: https://docs.langchain.com/langsmith/script-delete-traces

The LangSmith UI does not currently support the deletion of an individual trace. This, however, can be accomplished by directly removing the trace from all materialized views in ClickHouse (except the runs\_history views) and the runs and feedback table themselves.

This command can either be run using a trace ID as an argument or using a file that is a list of trace IDs.

### Prerequisites

Ensure you have the following tools/items ready.

1. kubectl

   * [https://kubernetes.io/docs/tasks/tools/](https://kubernetes.io/docs/tasks/tools/)

2. Clickhouse database credentials

   * Host
   * Port
   * Username
     * If using the bundled version, this is `default`
   * Password
     * If using the bundled version, this is `password`
   * Database name
     * If using the bundled version, this is `default`

3. Connectivity to the Clickhouse database from the machine you will be running the `delete_trace_by_id` script on.

   * If you are using the bundled version, you may need to port forward the clickhouse service to your local machine.
   * Run `kubectl port-forward svc/langsmith-clickhouse 8123:8123` to port forward the clickhouse service to your local machine.

4. The script to delete a trace

   * Download the [trace script](https://github.com/langchain-ai/helm/blob/main/charts/langsmith/scripts/delete_trace_by_id.sh)

<Warning>
  **Batch size limits**

  This script issues `DELETE` mutations against multiple ClickHouse tables per batch. Large deletions can cause service disruption.

  * **Maximum 10,000 traces per run**: split larger files and process sequentially.
  * **Wait between batches**: allow time for deletions to complete before starting the next batch.
  * Use the `--sync` flag for sequential (slower but safer) deletion.
</Warning>

### Running the deletion script for a single trace

Run the following command to run the trace deletion script using a single trace ID:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
sh delete_trace_by_id.sh <clickhouse_url> --trace_id <trace_id>
```

For example, if you are using the bundled version with port-forwarding, the command would look like:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
sh delete_trace_by_id.sh "clickhouse://default:password@localhost:8123/default" --trace_id 4ec70ec7-0808-416a-b836-7100aeec934b
```

If you visit the LangSmith UI, you should now see specified trace ID is no longer present nor reflected in stats.

### Running the deletion script for a multiple traces from a file with one trace ID per line

Run the following command to run the trace deletion script using a list of trace IDs:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
sh delete_trace_by_id.sh <clickhouse_url> --file <path/to/foo.txt>
```

For example, if you are using the bundled version with port-forwarding, the command would look like:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
sh delete_trace_by_id.sh "clickhouse://default:password@localhost:8123/default" --file path/to/traces.txt
```

If you visit the LangSmith UI, you should now see all the specified traces have been removed.

## Troubleshooting

### "Could not find trace IDs" error

If you receive an error message stating that trace IDs could not be found, add the `--ssl` flag to your command. Without this flag, the script may not be able to properly connect to ClickHouse, resulting in false "trace ID not found" errors.

Example with SSL flag:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
sh delete_trace_by_id.sh "clickhouse://default:password@localhost:8123/default" --file path/to/traces.txt --ssl
```

You can also verify that traces exist by connecting to ClickHouse directly using `clickhouse-cli` and querying for the trace IDs before running the deletion script.

### Service disruption after large deletion

If the service becomes unresponsive after deleting many traces, the deletion queue is likely overwhelmed.

**Prevention:** Limit deletions to 10,000 traces per run and wait several minutes between batches for deletions to process.

If you experience issues after a large deletion, contact [support](https://support.langchain.com/).

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/script-delete-traces.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Generate ClickHouse stats
Source: https://docs.langchain.com/langsmith/script-generate-clickhouse-stats

As part of troubleshooting your self-hosted instance of LangSmith, the LangChain team may ask you to generate Clickhouse statistics that will help us understand memory and CPU consumption and connection concurrency.

This command will generate a CSV that can be shared with the LangChain team.

### Prerequisites

Ensure you have the following tools/items ready.

1. kubectl

   * [https://kubernetes.io/docs/tasks/tools/](https://kubernetes.io/docs/tasks/tools/)

2. Clickhouse database credentials

   * Host
   * Port
   * Username
     * If using the bundled version, this is `default`
   * Password
     * If using the bundled version, this is `password`
   * Database name
     * If using the bundled version, this is `default`

3. Connectivity to the Clickhouse database from the machine you will be running the `get_clickhouse_stats` script on.

   * If you are using the bundled version, you may need to port forward the clickhouse service to your local machine.
   * Run `kubectl port-forward svc/langsmith-clickhouse 8123:8123` to port forward the clickhouse service to your local machine.

4. The script to generate ClickHouse stats

   * Download the [ClickHouse stats script](https://github.com/langchain-ai/helm/blob/main/charts/langsmith/scripts/get_clickhouse_stats.sh)

### Running the clickhouse stats generation script

Run the following command to run the stats generation script:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
sh get_clickhouse_stats.sh <clickhouse_url> --output path/to/file.csv
```

For example, if you are using the bundled version with port-forwarding, the command would look like:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
sh get_clickhouse_stats.sh "clickhouse://default:password@localhost:8123/default" --output clickhouse_stats.csv
```

and after running this command you should see a file, clickhouse\_stats.csv, has been created with Clickhouse statistics.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/script-generate-clickhouse-stats.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Generate query stats
Source: https://docs.langchain.com/langsmith/script-generate-query-stats

As part of troubleshooting your self-hosted instance of LangSmith, the LangChain team may ask you to generate LangSmith query statistics that will help us understand the performance of various queries that drive the LangSmith product experience.

This command will generate a CSV that can be shared with the LangChain team.

### Prerequisites

Ensure you have the following tools/items ready.

1. kubectl

   * [https://kubernetes.io/docs/tasks/tools/](https://kubernetes.io/docs/tasks/tools/)

2. Clickhouse database credentials

   * Host
   * Port
   * Username
     * If using the bundled version, this is `default`
   * Password
     * If using the bundled version, this is `password`
   * Database name
     * If using the bundled version, this is `default`

3. Connectivity to the Clickhouse database from the machine you will be running the `get_query_stats` script on.

   * If you are using the bundled version, you may need to port forward the clickhouse service to your local machine.
   * Run `kubectl port-forward svc/langsmith-clickhouse 8123:8123` to port forward the clickhouse service to your local machine.

4. The script to generate query stats

   * Download the [query stats script](https://github.com/langchain-ai/helm/blob/main/charts/langsmith/scripts/get_query_stats.sh)

### Running the query stats generation script

Run the following command to run the stats generation script:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
sh get_query_stats.sh <clickhouse_url> --output path/to/file.csv
```

For example, if you are using the bundled version with port-forwarding, the command would look like:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
sh get_query_stats.sh "clickhouse://default:password@localhost:8123/default" --output query_stats.csv
```

and after running this command you should see a file, query\_stats.csv, has been created with LangSmith query statistics.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/script-generate-query-stats.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Run support queries against ClickHouse
Source: https://docs.langchain.com/langsmith/script-running-ch-support-queries

This Helm repository contains queries to produce output that the LangSmith UI does not currently support directly (e.g. obtaining query exception logs from Clickhouse).

This command takes a clickhouse connection string that contains an embedded name and password (which can be passed in from a call to a secrets manager) and executes a query from an input file. In the example below, we are using the `ch_get_query_exceptions.sql` input file in the `support_queries/clickhouse` directory.

### Prerequisites

Ensure you have the following tools/items ready.

1. kubectl

   * [https://kubernetes.io/docs/tasks/tools/](https://kubernetes.io/docs/tasks/tools/)

2. Clickhouse database credentials

   * Host
   * Port
   * Username
     * If using the bundled version, this is `default`
   * Password
     * If using the bundled version, this is `password`
   * Database name
     * If using the bundled version, this is `default`

3. Connectivity to the Clickhouse database from the machine you will be running the migration script on.

   * If you are using the bundled version, you may need to port forward the clickhouse service to your local machine.
   * Run `kubectl port-forward svc/langsmith-clickhouse 8123:8123` to port forward the clickhouse service to your local machine.

4. The script to run a support query

   * Download the [ClickHouse support query script](https://github.com/langchain-ai/helm/blob/main/charts/langsmith/scripts/run_support_query_ch.sh)

### Running the query script

Run the following command to run the desired query:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
sh run_support_query_ch.sh <clickhouse_url> --input path/to/query.sql
```

For example, if you are using the bundled version with port-forwarding, the command might look like:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
sh run_support_query_ch.sh "clickhouse://default:password@localhost:8123/default" --input support_queries/clickhouse/ch_get_query_exceptions.sql
```

which will output query logs for all queries that have thrown exceptions in Clickhouse in the last 7 days. To extract this to a file add the flag `--output path/to/file.csv`

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/script-running-ch-support-queries.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Run support queries against PostgreSQL
Source: https://docs.langchain.com/langsmith/script-running-pg-support-queries

This Helm repository contains queries to produce output that the LangSmith UI does not currently support directly (e.g. obtaining trace counts for multiple organizations in a single query).

This command takes a postgres connection string that contains an embedded name and password (which can be passed in from a call to a secrets manager) and executes a query from an input file. In the example below, we are using the `pg_get_trace_counts_daily.sql` input file in the `support_queries/postgres` directory.

## Prerequisites

Ensure you have the following tools/items ready.

1. kubectl

   * [https://kubernetes.io/docs/tasks/tools/](https://kubernetes.io/docs/tasks/tools/)

2. PostgreSQL client

   * [https://www.postgresql.org/download/](https://www.postgresql.org/download/)

3. PostgreSQL database connection:

   * Host
   * Port
   * Username
     * If using the bundled version, this is `postgres`
   * Password
     * If using the bundled version, this is `postgres`
   * Database name
     * If using the bundled version, this is `postgres`

4. Connectivity to the PostgreSQL database from the machine you will be running the migration script on.

   * If you are using the bundled version, you may need to port forward the postgresql service to your local machine.
   * Run `kubectl port-forward svc/langsmith-postgres 5432:5432` to port forward the postgresql service to your local machine.

5. The script to run a support query

   * Download the [PostgreSQL support query script](https://github.com/langchain-ai/helm/blob/main/charts/langsmith/scripts/run_support_query_pg.sh)

## Running the query script

Run the following command to run the desired query:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
sh run_support_query_pg.sh <postgres_url> --input path/to/query.sql
```

For example, if you are using the bundled version with port-forwarding, the command might look like:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
sh run_support_query_pg.sh "postgres://postgres:postgres@localhost:5432/postgres" --input support_queries/pg_get_trace_counts_daily.sql
```

which will output the count of daily traces by workspace ID and organization ID. To extract this to a file add the flag `--output path/to/file.csv`

## Export usage data

All export methods produce the same data: LangSmith trace counts, LangSmith Deployments node usage, and Fleet run counts across all workspaces and organizations.

<Note>
  The UI and API exports require both of the following:

  * The `organization:manage` permission.
  * The caller's email must be listed in `USAGE_EXPORT_ADMIN_EMAILS`, or `ORG_ADMINS_INSTALLATION_USAGE_EXPORT_ENABLED` must be set to `true`.

  ```env theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  USAGE_EXPORT_ADMIN_EMAILS='["admin@example.com", "admin2@example.com"]'
  ORG_ADMINS_INSTALLATION_USAGE_EXPORT_ENABLED=true
  ```
</Note>

### Export from the UI (recommended)

1. Navigate to **Settings** > **Usage and billing** > **Usage export**.
2. Click **Export usage data**.
3. A ZIP file containing all usage data will download.

### Export via API

If you prefer to export usage data programmatically, you can call the export API endpoint directly.

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
curl -OJ \
  -H "X-API-Key: <your_api_key>" \
  https://<langsmith_url>/api/v1/orgs/current/usage/backfill-export
```

### Export via SQL scripts

You can also run SQL scripts directly against your PostgreSQL database to export usage data. This requires database access credentials — no application-level permissions apply.

To export trace usage (requires Helm chart version 0.11.4 or later):

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
sh run_support_query_pg.sh <postgres_url> \
  --input support_queries/postgres/pg_usage_traces_full_export.sql \
  --output ls_export.csv
```

To export node usage (requires Helm chart version 0.11.4 or later):

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
sh run_support_query_pg.sh <postgres_url> \
  --input support_queries/postgres/pg_usage_nodes_full_export.sql \
  --output lgp_export.csv
```

To export Fleet run counts (requires Helm chart version 0.13.25 or later):

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
sh run_support_query_pg.sh <postgres_url> \
  --input support_queries/postgres/pg_usage_agent_builder_full_export.sql \
  --output ab_export.csv
```

To export usage snapshots (daily entity counts such as workspaces, projects, datasets, prompts, and active users):

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
sh run_support_query_pg.sh <postgres_url> \
  --input support_queries/postgres/pg_usage_snapshots_full_export.sql \
  --output usage_snapshots_export.csv
```

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/script-running-pg-support-queries.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Basic authentication with email and password
Source: https://docs.langchain.com/langsmith/self-host-basic-auth

LangSmith supports login via username/password with a few limitations:

* You cannot change an existing installation from basic auth mode to OAuth with PKCE (deprecated) or vice versa - installations must be either one or the other. **A basic auth installation requires a completely fresh installation including a separate PostgreSQL database/schema, unless migrating from an existing `None` type installation (see below).**
* Users must be given their initial auto-generated password once they are invited. This password may be changed later by any Organization Admin.
* You cannot use both basic auth and OAuth with client secret at the same time.

## Requirements and features

* There is a single `Default` organization that is provisioned during initial installation, and creating additional organizations is not supported
* Your initial password (configured below) must be least 12 characters long and have at least one lowercase, uppercase, and symbol
* There are no strict requirements for the secret used for signing JWTs, but we recommend securely generating a string of at least 32 characters. For example: `openssl rand -base64 32`

### Migrating from none auth

**Only supported in versions 0.7 and above.**

Migrating an installation from [None](/langsmith/authentication-methods#none) auth mode replaces the single "default" user with a user with the configured credentials and keeps all existing resources. The single pre-existing workspace ID post-migration remains `00000000-0000-0000-0000-000000000000`, but everything else about the migrated installation is standard for a basic auth installation.

To migrate, simply update your configuration as shown below and run `helm upgrade` (or `docker-compose up`) as usual.

### Configuration

<Note>
  Changing the JWT secret will log out your users
</Note>

<CodeGroup>
  ```yaml Helm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  config:
    authType: mixed
    basicAuth:
      enabled: true
      initialOrgAdminEmail: <YOUR EMAIL ADDRESS>
      initialOrgAdminPassword: <PASSWORD> # Must be at least 12 characters long and have at least one lowercase, uppercase, and symbol
      jwtSecret: <SECRET>
  ```

  ```bash Docker theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  # In your .env file
  AUTH_TYPE=mixed
  BASIC_AUTH_ENABLED=true
  INITIAL_ORG_ADMIN_EMAIL=<YOUR EMAIL ADDRESS>
  INITIAL_ORG_ADMIN_PASSWORD=<PASSWORD> # Must be at least 12 characters long and have at least one lowercase, uppercase, and symbol
  BASIC_AUTH_JWT_SECRET=<SECRET>
  ```
</CodeGroup>

Additionally, in docker-compose you will need to run the bootstrap command to create the initial organization and user:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
docker-compose exec langchain-backend python hooks/auth_bootstrap.pyc
```

Once configured, you will see a login screen like the one below. You should be able to login with the `initialOrgAdminEmail` and `initialOrgAdminPassword` values, and your user will be auto-provisioned with role `Organization Admin`. See the [admin guide](/langsmith/administration-overview#organization-roles) for more details on organization roles.

<img alt="LangSmith UI with basic auth" />

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/self-host-basic-auth.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
