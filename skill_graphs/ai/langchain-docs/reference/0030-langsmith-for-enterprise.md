# LangSmith for Enterprise
Source: https://docs.langchain.com/langsmith/enterprise

Deployment options, access control, data privacy, cost controls, and security compliance for Enterprise users.

This page is a reference hub for enterprise teams and includes information on features that are important for your organization, like [deployment options](#deployment-options), [access control](#access-control), [data privacy](#data-privacy-and-pii), and [cost controls](#cost-controls-and-usage).

<Callout>
  For questions about enterprise [pricing](/langsmith/pricing-plans) or to get started, [contact our sales team](https://www.langchain.com/contact-sales).
</Callout>

## Deployment options

Choose how to host LangSmith to match your infrastructure and data residency requirements.

<CardGroup>
  <Card title="Cloud" icon="cloud" href="/langsmith/cloud">
    Host LangSmith in LangSmith's managed cloud with US or EU data residency.
  </Card>

  <Card title="Hybrid" icon="topology-complex" href="/langsmith/hybrid">
    Run the control plane in LangSmith's cloud and your data plane in your own VPC for full data isolation.
  </Card>

  <Card title="Self-hosted" icon="server-2" href="/langsmith/self-hosted">
    Deploy LangSmith entirely within your own infrastructure using Docker Compose or Kubernetes.
  </Card>
</CardGroup>

## User management

Manage users and automate provisioning across your organization.

<CardGroup>
  <Card title="User management" icon="users" href="/langsmith/user-management">
    Invite users, assign roles, and configure SCIM for automated provisioning and deprovisioning.
  </Card>

  <Card title="SSO & JIT provisioning" icon="login" href="/langsmith/authentication-methods">
    Configure SAML or OIDC single sign-on and just-in-time user provisioning for your identity provider.
  </Card>

  <Card title="Organization setup" icon="building" href="/langsmith/set-up-hierarchy">
    Create and configure organizations, workspaces, and the user hierarchy within your enterprise.
  </Card>

  <Card title="Manage by API" icon="terminal-2" href="/langsmith/manage-organization-by-api">
    Programmatically manage users, configure security settings, and administer your organization via API.
  </Card>
</CardGroup>

## Access control

Control who can access what within your organization.

<CardGroup>
  <Card title="Role-based access control (RBAC)" icon="shield-lock" href="/langsmith/rbac">
    Define permissions per workspace using built-in or custom roles. Available exclusively on Enterprise plans.
  </Card>

  <Card title="Attribute-based access control (ABAC)" icon="tag" href="/langsmith/abac">
    Apply fine-grained, tag-based access policies to restrict resource access—including blocking PII data from specific users.
  </Card>

  <Card title="Workload isolation" icon="layout-sidebar" href="/langsmith/workload-isolation">
    Use multi-workspace models to isolate teams, establish trust boundaries, and separate environments.
  </Card>

  <Card title="Resource tags" icon="tag" href="/langsmith/set-up-resource-tags">
    Tag resources for use with ABAC policies and to organize environments like dev, staging, and prod.
  </Card>
</CardGroup>

## Data privacy and PII

Control how sensitive data is stored and accessed.

<CardGroup>
  <Card title="Data storage & privacy" icon="database" href="/langsmith/data-storage-and-privacy">
    Understand what LangSmith stores, how encryption works, and how to opt out of telemetry and tracing.
  </Card>

  <Card title="PII controls with ABAC" icon="eye-off" href="/langsmith/abac">
    Use ABAC deny policies to restrict access to traces and datasets that contain personally identifiable information.
  </Card>
</CardGroup>

## Data retention & cleanup

Configure how long data is retained and how to delete it.

<CardGroup>
  <Card title="Data purging for compliance" icon="trash" href="/langsmith/data-purging-compliance">
    Set custom retention periods, delete traces by metadata, and meet deletion requirements.
  </Card>

  <Card title="Data retention settings" icon="clock" href="/langsmith/usage-and-billing#data-retention">
    Understand base vs. extended retention tiers, auto-upgrades, and how retention affects billing.
  </Card>
</CardGroup>

## Cost controls and usage

Track and limit spending across your organization.

<CardGroup>
  <Card title="Billing & spend limits" icon="credit-card" href="/langsmith/billing">
    Set monthly usage limits, track prepaid commitment burndown, and optimize tracing spend.
  </Card>

  <Card title="Granular usage reporting" icon="chart-bar" href="/langsmith/granular-usage">
    Break down trace usage by workspace, project, user, or API key to attribute costs across teams.
  </Card>
</CardGroup>

## Security & compliance

Review LangSmith's security posture and compliance certifications.

<CardGroup>
  <Card title="Shared responsibility model" icon="shield-check" href="/langsmith/shared-responsibility-model">
    Review the security responsibilities shared between LangChain and your organization. LangSmith holds SOC 2 Type II, HIPAA, and GDPR certifications.
  </Card>

  <Card title="Scalability & resilience" icon="chart-arrows-vertical" href="/langsmith/scalability-and-resilience">
    Review SLA guarantees, disaster recovery strategies, and high availability configurations.
  </Card>
</CardGroup>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/enterprise.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Environment variables
Source: https://docs.langchain.com/langsmith/env-var

The Agent Server supports specific environment variables for configuring a deployment.

## `BG_JOB_ISOLATED_LOOPS`

Set `BG_JOB_ISOLATED_LOOPS` to `True` to execute background runs in an isolated event loop separate from the serving API event loop.

<Warning>
  Enabling this flag does not remove the underlying problem. It moves synchronous blocking work off the serving API's event loop so health checks stop failing, but the blocking code continues to run on the background loop and **will** continue to cause issues in production, like degraded throughput, tail-latency spikes, starved workers, or connection pool exhaustion (see the pool-size caveat below), and poor scaling under load.

  To properly resolve those issues, use native async drivers and async code throughout your agent. That means async HTTP clients like `httpx` or `aiohttp` (though we recommend caching the clients to avoid CPU overhead loading the SSL context), async database drivers like `asyncpg` or `psycopg[async]`, and async model SDK's. For unavoidable synchronous libraries, wrap the specific call in `asyncio.to_thread(...)` or `loop.run_in_executor(...)` instead of enabling this flag for the whole deployment.
</Warning>

This environment variable should be set to `True` if the implementation of a graph/node contains synchronous code. In this situation, the synchronous code will block the serving API event loop, which may cause the API to be unavailable. A symptom of an unavailable API is continuous application restarts due to failing health checks.

<Warning>
  When `BG_JOB_ISOLATED_LOOPS` is enabled, each background worker runs in its own thread with a **separate Postgres connection pool**. The per-worker pool size is `LANGGRAPH_POSTGRES_POOL_MAX_SIZE // N_JOBS_PER_WORKER`. For example, with `LANGGRAPH_POSTGRES_POOL_MAX_SIZE=20` and `N_JOBS_PER_WORKER=15`, each worker gets a pool of only 1 connection. Small per-worker pools are more susceptible to connection failures because a single stale connection represents a large fraction of the pool. If you enable isolated loops, ensure `LANGGRAPH_POSTGRES_POOL_MAX_SIZE` is large enough to provide at least a few connections per worker.
</Warning>

Defaults to `False`.

## `BG_JOB_MAX_RETRIES`

Maximum number of times a background run will be retried after a retriable failure (e.g. transient database errors, server shutdown cancellations). When a run fails with a retriable error, it is placed back in the queue and resumed from the last checkpointed step. If the run exceeds the maximum number of retries, it is marked as failed.

Defaults to `3`.

## `BG_JOB_SHUTDOWN_GRACE_PERIOD_SECS`

Specifies, in seconds, how long the server will wait for background jobs to finish after the queue receives a shutdown signal. After this period, the server will force termination. Defaults to `180` seconds. The maximum value is `3600` seconds. Set this to ensure jobs have enough time to complete cleanly during shutdown. Added in `langgraph-api==0.2.16`.

## `BG_JOB_TIMEOUT_SECS`

The timeout of a background run can be increased. However, the infrastructure for a Cloud deployment enforces a 1 hour timeout limit for API requests. This means the connection between client and server will timeout after 1 hour. This is not configurable.

A background run can execute for longer than 1 hour, but a client must reconnect to the server (e.g. join stream via `POST /threads/{thread_id}/runs/{run_id}/stream`) to retrieve output from the run if the run is taking longer than 1 hour.

Defaults to `86400`.

## `CORS_ALLOW_ORIGINS`

Set `CORS_ALLOW_ORIGINS` to specify allowed origins.

* Example for allowing a single origin: `CORS_ALLOW_ORIGINS=https://example.com`
* Example for allowing multiple origins: `CORS_ALLOW_ORIGINS=https://example.com,https://app.example.com`

For advanced CORS configuration, see [how to add custom CORS configuration](/langsmith/cli#customizing-http-middleware-and-headers).

Defaults to `*` (all origins).

## `DD_API_KEY`

Specify `DD_API_KEY` (your [Datadog API Key](https://docs.datadoghq.com/account_management/api-app-keys/)) to automatically enable Datadog tracing for the deployment. Specify other [`DD_*` environment variables](https://ddtrace.readthedocs.io/en/stable/configuration.html) to configure the tracing instrumentation.

If `DD_API_KEY` is specified, the application process is wrapped in the [`ddtrace-run` command](https://ddtrace.readthedocs.io/en/stable/installation_quickstart.html). Other `DD_*` environment variables (e.g. `DD_SITE`, `DD_ENV`, `DD_SERVICE`, `DD_TRACE_ENABLED`) are typically needed to properly configure the tracing instrumentation. See [`DD_*` environment variables](https://ddtrace.readthedocs.io/en/stable/configuration.html) for more details. You can enable `DD_TRACE_DEBUG=true` and set `DD_LOG_LEVEL=debug` to troubleshoot.

<Note>
  Enabling `DD_API_KEY` (and thus `ddtrace-run`) can override or interfere with other auto-instrumentation solutions (such as OpenTelemetry) that you may have instrumented into your application code.
</Note>

## `LANGGRAPH_POSTGRES_POOL_MAX_SIZE`

Beginning with langgraph-api version `0.2.12`, the maximum size of the Postgres connection pool (per replica) can be controlled using the `LANGGRAPH_POSTGRES_POOL_MAX_SIZE` environment variable. By setting this variable, you can determine the upper bound on the number of simultaneous connections the server will establish with the Postgres database.

For example, if a deployment is scaled up to 10 replicas and `LANGGRAPH_POSTGRES_POOL_MAX_SIZE` is configured to `150`, then up to `1500` connections to Postgres can be established. This is particularly useful for deployments where database resources are limited (or more available) or where you need to tune connection behavior for performance or scaling reasons.

When [`BG_JOB_ISOLATED_LOOPS`](#bg_job_isolated_loops) is enabled, the pool is not shared. Instead, each background worker thread creates its own pool with a maximum size of `LANGGRAPH_POSTGRES_POOL_MAX_SIZE / N_JOBS_PER_WORKER`. Keep this in mind when lowering the pool size. A value that works well for a shared pool may result in very small per-worker pools under isolated loops.

Defaults to `150` connections.

## `LS_CHECKPOINT_DELETE`

JSON-valued configuration for deferred checkpoint deletion. When enabled, thread delete and prune operations enqueue checkpoints for background deletion instead of deleting synchronously, moving the I/O off the request hot path. Available in `langgraph-api>=0.8.1`.

<Note>
  Only supported with the default PostgreSQL checkpointer backend. Deferred deletes will become the default in a future release.
</Note>

Accepted fields:

* `enabled` (boolean, default `false`): When `true`, thread delete and prune operations enqueue checkpoints into `checkpoint_delete_queue` and return immediately, and the background worker drains the queue.
* `enabledWorkerOnly` (boolean, default `false`): Runs only the background drain worker without enqueuing new entries. Use this to finish draining the queue after rolling `enabled` back to `false`.
* `pollIntervalMs` (integer, default `5000`): How often the worker polls the queue, in milliseconds.
* `batchSize` (integer, default `25`): Number of checkpoint entries the worker dequeues per transaction. Smaller values spread I/O over more time at the cost of longer drain latency.
* `batchSleepMs` (integer, default `500`): How long the worker sleeps between batches when the queue is non-empty, in milliseconds.

Example: `LS_CHECKPOINT_DELETE='{"enabled":true,"batchSize":10,"pollIntervalMs":1000}'`.

Defaults to disabled (synchronous checkpoint deletion).

## `LS_DEFAULT_CHECKPOINTER_BACKEND`

Sets the default [checkpointer backend](/langsmith/configure-checkpointer) for agent servers that don't specify one in `langgraph.json`. Accepted values: `"default"` (PostgreSQL), `"mongo"`, `"custom"`.

If the application's `langgraph.json` includes a `checkpointer.backend` value, it takes precedence over this variable.

When set to `"mongo"`, you must also provide the MongoDB connection URI via [`LS_MONGODB_URI`](#ls_mongodb_uri).

## `LANGSMITH_API_KEY`

For deployments with [self-hosted LangSmith](/langsmith/self-hosted) only.

To send traces to a self-hosted LangSmith instance, set `LANGSMITH_API_KEY` to an API key created from the self-hosted instance.

## `LANGSMITH_ENDPOINT`

For deployments with [self-hosted LangSmith](/langsmith/self-hosted) only.

To send traces to a self-hosted LangSmith instance, set `LANGSMITH_ENDPOINT` to the hostname of the self-hosted instance.

## `LANGSMITH_TRACING`

Set `LANGSMITH_TRACING` to `false` to disable tracing to LangSmith.

<Note>
  For selective tracing control based on runtime conditions (such as per-client requirements or data sensitivity), see [Conditional tracing](/langsmith/conditional-tracing).
</Note>

Defaults to `true`.

## `LOG_COLOR`

This is mainly relevant in the context of using the dev server via the `langgraph dev` command. Set `LOG_COLOR` to `true` to enable ANSI-colored console output when using the default console renderer. Disabling color output by setting this variable to `false` produces monochrome logs. Defaults to `true`.

## `LOG_LEVEL`

Configure [log level](https://docs.python.org/3/library/logging.html#logging-levels). Defaults to `INFO`.

## `LOG_JSON`

Set `LOG_JSON` to `true` to render all log messages as JSON objects using the configured `JSONRenderer`. This produces structured logs that can be easily parsed or ingested by log management systems. Defaults to `false`.

## `MOUNT_PREFIX`

<Info>
  **Only Allowed in Self-Hosted Deployments**
  The `MOUNT_PREFIX` environment variable is only allowed in Self-Hosted Deployment models, LangSmith SaaS will not allow this environment variable.
</Info>

Set `MOUNT_PREFIX` to serve the Agent Server under a specific path prefix. This is useful for deployments where the server is behind a reverse proxy or load balancer that requires a specific path prefix.

For example, if the server is to be served under `https://example.com/langgraph`, set `MOUNT_PREFIX` to `/langgraph`.

## `N_JOBS_PER_WORKER`

Number of jobs per worker for the Agent Server task queue. Defaults to `10`.

## `LS_APM_OTEL_ENABLED`

To configure OpenTelemetry APM tracing for your deployment, set `LS_APM_OTEL_ENABLED` to `true` and `OTEL_EXPORTER_OTLP_TRACES_ENDPOINT` or `OTEL_EXPORTER_OTLP_ENDPOINT` to the target trace ingestion endpoint. Note that both `LS_APM_OTEL_ENABLED` and one of the other two export endpoints are required to activate OpenTelemetry APM tracing in server versions later than `0.7.17`.

Specify other [`OTEL_*` environment variables](https://opentelemetry.io/docs/collector/configuration/) to configure tracing, logging, and other instrumentation.

```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# If you set LS_APM_OTEL_ENABLED AND (OTEL_EXPORTER_OTLP_TRACES_ENDPOINT or OTEL_EXPORTER_OTLP_ENDPOINT),

# the server starts with OpenTelemetry instrumentation enabled.
LS_APM_OTEL_ENABLED=true
OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=<target trace ingestion endpoint>
OTEL_EXPORTER_OTLP_ENDPOINT=https://otlp.nr-data.net
OTEL_SERVICE_NAME=MY_LANGSMITH_DEPLOYMENT
OTEL_EXPORTER_OTLP_HEADERS=api-key=<YOUR_INGEST_LICENSE_KEY>
LANGSMITH_OTEL_ENABLED=true

# Common OTEL settings
OTEL_ATTRIBUTE_VALUE_LENGTH_LIMIT=4095
OTEL_EXPORTER_OTLP_COMPRESSION=gzip
OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf
OTEL_EXPORTER_OTLP_METRICS_TEMPORALITY_PREFERENCE=delta
OTEL_PYTHON_EXCLUDED_URLS=/metrics,/ok,/info

# Optional: OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true
```

For example, to submit OpenTelemetry traces to [New Relic's US region](https://docs.newrelic.com/docs/opentelemetry/best-practices/opentelemetry-otlp/), set the following:

```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
LS_APM_OTEL_ENABLED=true
OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=https://otlp.nr-data.net/v1/traces
OTEL_EXPORTER_OTLP_ENDPOINT=https://otlp.nr-data.net
OTEL_EXPORTER_OTLP_HEADERS=api-key=<YOUR_INGEST_LICENSE_KEY>
```

<Note>
  OTel APM tracing was added in Agent Server version `0.5.32` and is currently in Alpha.
</Note>

## `LS_MONGODB_URI`

MongoDB connection URI for the MongoDB checkpointer backend.

The URI must point to a replica set member or `mongos` router and must include the database name in the path.

See [Configure checkpointer backend](/langsmith/configure-checkpointer) for details.

See [Configure checkpointer backend](/langsmith/configure-checkpointer) for details.

## `POSTGRES_URI_CUSTOM`

<Info>
  **Only for Self-Hosted**
  Custom Postgres instances are only available for [Self-Hosted](/langsmith/self-hosted) deployments.
</Info>

Specify `POSTGRES_URI_CUSTOM` to use a custom Postgres instance. The value of `POSTGRES_URI_CUSTOM` must be a valid [Postgres connection URI](https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING-URIS).

Postgres:

* Version 15.8 or higher.
* An initial database must be present and the connection URI must reference the database.

Control Plane Functionality:

* If `POSTGRES_URI_CUSTOM` is specified, the control plane will not provision a database for the server.
* If `POSTGRES_URI_CUSTOM` is removed, the control plane will not provision a database for the server and will not delete the externally managed Postgres instance.
* If `POSTGRES_URI_CUSTOM` is removed, deployment of the revision will not succeed. Once `POSTGRES_URI_CUSTOM` is specified, it must always be set for the lifecycle of the deployment.
* If the deployment is deleted, the control plane will not delete the externally managed Postgres instance.
* The value of `POSTGRES_URI_CUSTOM` can be updated. For example, a password in the URI can be updated.

Database Connectivity:

* The custom Postgres instance must be accessible by the Agent Server. The user is responsible for ensuring connectivity.

## `REDIS_CLUSTER`

<Warning>
  This feature is in Alpha.
</Warning>

<Info>
  **Only Allowed in Self-Hosted Deployments**
  Redis Cluster mode is only available in Self-Hosted Deployment models, LangSmith SaaS will provision a redis instance for you by default.
</Info>

Set `REDIS_CLUSTER` to `True` to enable Redis Cluster mode. When enabled, the system will connect to Redis using cluster mode. This is useful when connecting to a Redis Cluster deployment.

Defaults to `False`.

## `REDIS_KEY_PREFIX`

<Info>
  **Available in API Server version 0.1.9+**
  This environment variable is supported in API Server version 0.1.9 and above.
</Info>

Specify a prefix for Redis keys. This allows multiple Agent Server instances to share the same Redis instance by using different key prefixes.

Defaults to `''`.

## `REDIS_URI_CUSTOM`

<Info>
  **Only for Self-Hosted**
  Custom Redis instances are only available for [Self-Hosted](/langsmith/self-hosted) deployments.
</Info>

Specify `REDIS_URI_CUSTOM` to use a custom Redis instance. The value of `REDIS_URI_CUSTOM` must be a valid [Redis connection URI](https://redis-py.readthedocs.io/en/stable/connections.html#redis.Redis.from_url).

## `REDIS_MAX_CONNECTIONS`

The maximum size of the Redis connection pool (per replica) can be controlled using the `REDIS_MAX_CONNECTIONS` environment variable. By setting this variable, you can determine the upper bound on the number of simultaneous connections the server will establish with the Redis instance.

For example, if a deployment is scaled up to 10 replicas and `REDIS_MAX_CONNECTIONS` is configured to `150`, then up to `1500` connections to Redis can be established.

Defaults to `2000`.

## `RESUMABLE_STREAM_TTL_SECONDS`

Time-to-live in seconds for resumable stream data in Redis.

When a run is created and the output is streamed, the stream can be configured to be resumable (e.g. `stream_resumable=True`). If a stream is resumable, output from the stream is temporarily stored in Redis. The TTL for this data can be configured by setting `RESUMABLE_STREAM_TTL_SECONDS`.

See the [Python](https://reference.langchain.com/python/langsmith/deployment/sdk/#langgraph_sdk.client.RunsClient.stream) and [JS/TS](https://langchain-ai.github.io/langgraphjs/reference/classes/sdk_client.RunsClient.html#stream) SDKs for more details on how to implement resumable streams.

Defaults to `120` seconds.

<Note>
  Setting a very high value for `RESUMABLE_STREAM_TTL_SECONDS` can result in substantial Redis memory usage when there are many concurrent runs with large or frequent streaming output. Set this value to the minimum value to enable recovery during network interruptions and prefer checkpointing for long term durability and execution snapshotting.
</Note>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/env-var.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Evaluate a chatbot
Source: https://docs.langchain.com/langsmith/evaluate-chatbot-tutorial

In this guide we will set up evaluations for a chatbot. These allow you to measure how well your application is performing over a set of data. Being able to get this insight quickly and reliably will allow you to iterate with confidence.

At a high level, in this tutorial we will:

* *Create an initial golden dataset to measure performance*
* *Define metrics to use to measure performance*
* *Run evaluations on a few different prompts or models*
* *Compare results manually*
* *Track results over time*
* *Set up automated testing to run in CI/CD*

For more information on the evaluation workflows LangSmith supports, check out the [how-to guides](/langsmith/evaluation), or see the reference docs for [evaluate](https://reference.langchain.com/python/langsmith/client/Client/evaluate) and its asynchronous [aevaluate](https://reference.langchain.com/python/langsmith/client/Client/aevaluate) counterpart.

Lots to cover, let's dive in!

## Setup

First install the required dependencies for this tutorial. We happen to use OpenAI, but LangSmith can be used with any model:

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install -U langsmith openai
  ```

  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv add langsmith openai
  ```
</CodeGroup>

And set environment variables to enable LangSmith tracing:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
export LANGSMITH_TRACING="true"
export LANGSMITH_API_KEY="<Your LangSmith API key>"
export OPENAI_API_KEY="<Your OpenAI API key>"
```

## Create a dataset

The first step when getting ready to test and evaluate your application is to define the datapoints you want to evaluate. There are a few aspects to consider here:

* What should the schema of each datapoint be?
* How many datapoints should I gather?
* How should I gather those datapoints?

**Schema:** Each datapoint should consist of, at the very least, the inputs to the application. If you are able, it is also very helpful to define the expected outputs - these represent what you would expect a properly functioning application to output. Often times you cannot define the perfect output - that's okay! Evaluation is an iterative process. Sometimes you may also want to define more information for each example - like the expected documents to fetch in RAG, or the expected steps to take as an agent. LangSmith datasets are very flexible and allow you to define arbitrary schemas.

**How many:** There's no hard and fast rule for how many you should gather. The main thing is to make sure you have proper coverage of edge cases you may want to guard against. Even 10-50 examples can provide a lot of value! Don't worry about getting a large number to start - you can (and should) always add over time!

**How to get:** This is maybe the trickiest part. Once you know you want to gather a dataset... how do you actually go about it? For most teams that are starting a new project, we generally see them start by collecting the first 10-20 datapoints by hand. After starting with these datapoints, these datasets are generally *living* constructs and grow over time. They generally grow after seeing how real users will use your application, seeing the pain points that exist, and then moving a few of those datapoints into this set. There are also methods like synthetically generating data that can be used to augment your dataset. To start, we recommend not worrying about those and just hand labeling \~10-20 examples.

Once you've got your dataset, there are a few different ways to upload them to LangSmith. For this tutorial, we will use the client, but you can also upload via the UI (or even create them in the UI).

For this tutorial, we will create 5 datapoints to evaluate on. We will be evaluating a question-answering application. The input will be a question, and the output will be an answer. Since this is a question-answering application, we can define the expected answer. Let's show how to create and upload this dataset to LangSmith!

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langsmith import Client

client = Client()

# Define dataset: these are your test cases
dataset_name = "QA Example Dataset"
dataset = client.create_dataset(dataset_name)

client.create_examples(
    dataset_id=dataset.id,
    examples=[
        {
            "inputs": {"question": "What is LangChain?"},
            "outputs": {"answer": "A framework for building LLM applications"},
        },
        {
            "inputs": {"question": "What is LangSmith?"},
            "outputs": {"answer": "A platform for observing and evaluating LLM applications"},
        },
        {
            "inputs": {"question": "What is OpenAI?"},
            "outputs": {"answer": "A company that creates Large Language Models"},
        },
        {
            "inputs": {"question": "What is Google?"},
            "outputs": {"answer": "A technology company known for search"},
        },
        {
            "inputs": {"question": "What is Mistral?"},
            "outputs": {"answer": "A company that creates Large Language Models"},
        }
    ]
)
```

Now, if we go the LangSmith UI and look for `QA Example Dataset` in the `Datasets & Testing` page, when we click into it we should see that we have five new examples.

<img alt="Testing tutorial dataset" />

## Define metrics

After creating our dataset, we can now define some metrics to evaluate our responses on. Since we have an expected answer, we can compare to that as part of our evaluation. However, we do not expect our application to output those **exact** answers, but rather something that is similar. This makes our evaluation a little trickier.

In addition to evaluating correctness, let's also make sure our answers are short and concise. This will be a little easier - we can define a simple Python function to measure the length of the response.

Let's go ahead and define these two metrics.

For the first, we will use an LLM to **judge** whether the output is correct (with respect to the expected output). This **LLM-as-a-judge** is relatively common for cases that are too complex to measure with a simple function. We can define our own prompt and LLM to use for evaluation here:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import openai
from langsmith import wrappers

openai_client = wrappers.wrap_openai(openai.OpenAI())

eval_instructions = "You are an expert professor specialized in grading students' answers to questions."

def correctness(inputs: dict, outputs: dict, reference_outputs: dict) -> bool:
    user_content = f"""You are grading the following question:
{inputs['question']}
Here is the real answer:
{reference_outputs['answer']}
You are grading the following predicted answer:
{outputs['response']}
Respond with CORRECT or INCORRECT:
Grade:"""
    response = openai_client.chat.completions.create(
        model="gpt-5.4-mini",
        temperature=0,
        messages=[
            {"role": "system", "content": eval_instructions},
            {"role": "user", "content": user_content},
        ],
    ).choices[0].message.content
    return response == "CORRECT"
```

For evaluating the length of the response, this is a lot easier! We can just define a simple function that checks whether the actual output is less than 2x the length of the expected result.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
def concision(outputs: dict, reference_outputs: dict) -> bool:
    return int(len(outputs["response"]) < 2 * len(reference_outputs["answer"]))
```

## Run evaluations

Great! Now how do we run evaluations? Now that we have a dataset and evaluators, all that we need is our application! We will build a simple application that just has a system message with instructions on how to respond and then passes it to the LLM. We will build this using the OpenAI SDK directly:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
default_instructions = "Respond to the users question in a short, concise manner (one short sentence)."

def my_app(question: str, model: str = "gpt-5.4-mini", instructions: str = default_instructions) -> str:
    return openai_client.chat.completions.create(
        model=model,
        temperature=0,
        messages=[
            {"role": "system", "content": instructions},
            {"role": "user", "content": question},
        ],
    ).choices[0].message.content
```

Before running this through LangSmith evaluations, we need to define a simple wrapper that maps the input keys from our dataset to the function we want to call, and then also maps the output of the function to the output key we expect.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
def ls_target(inputs: str) -> dict:
    return {"response": my_app(inputs["question"])}
```

Great! Now we're ready to run an evaluation. Let's do it!

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
experiment_results = client.evaluate(
    ls_target, # Your AI system
    data=dataset_name, # The data to predict and grade over
    evaluators=[concision, correctness], # The evaluators to score the results
    experiment_prefix="openai-4o-mini", # A prefix for your experiment names to easily identify them
)
```

This will output a URL. If we click on it, we should see results of our evaluation!

<img alt="Testing tutorial run" />

If we go back to the dataset page and select the `Experiments` tab, we can now see a summary of our one run!

<img alt="Testing tutorial one run" />

Let's now try it out with a different model! Let's try `gpt-4-turbo`

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
def ls_target_v2(inputs: str) -> dict:
    return {"response": my_app(inputs["question"], model="gpt-4-turbo")}

experiment_results = client.evaluate(
    ls_target_v2,
    data=dataset_name,
    evaluators=[concision, correctness],
    experiment_prefix="openai-4-turbo",
)
```

And now let's use GPT-4 but also update the prompt to be a bit more strict in requiring the answer to be short.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
instructions_v3 = "Respond to the users question in a short, concise manner (one short sentence). Do NOT use more than ten words."

def ls_target_v3(inputs: str) -> dict:
    response = my_app(
        inputs["question"],
        model="gpt-4-turbo",
        instructions=instructions_v3
    )
    return {"response": response}

experiment_results = client.evaluate(
    ls_target_v3,
    data=dataset_name,
    evaluators=[concision, correctness],
    experiment_prefix="strict-openai-4-turbo",
)
```

If we go back to the `Experiments` tab on the datasets page, we should see that all three runs now show up!

<img alt="Testing tutorial three runs" />

## Comparing results

Awesome, we've evaluated three different runs. But how can we compare results? The first way we can do this is just by looking at the runs in the `Experiments` tab. If we do that, we can see a high level view of the metrics for each run:

<img alt="Testing tutorial compare metrics" />

We can tell that GPT-4 is better than GPT-3.5 at knowing who companies are, and that the strict prompt helped a lot with the length. But what if we want to explore in more detail?

In order to do that, we can select all the runs we want to compare (in this case all three) and open them up in a comparison view. We immediately see all three tests side by side. Some of the cells are color coded - this is showing a regression of *a certain metric* compared to *a certain baseline*. We automatically choose defaults for the baseline and metric, but you can change those yourself. You can also choose which columns and which metrics you see by using the `Display` control. You can also automatically filter to only see the runs that have improvements/regressions by clicking on the icons at the top.

<img alt="Testing tutorial compare runs" />

If we want to see more information, we can also select the `Expand` button that appears when hovering over a row to open up a side panel with more detailed information:

<img alt="Testing tutorial side panel" />

## Set up automated testing to run in CI/CD

Now that we've run this in a one-off manner, we can set it to run in an automated fashion. We can do this pretty easily by just including it as a pytest file that we run in CI/CD. As part of this, we can either just log the results OR set up some criteria to determine if it passes or not. For example, if I wanted to ensure that we always got at least 80% of generated responses passing the `length` check, we could set that up with a test like:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
def test_length_score() -> None:
    """Test that the length score is at least 80%."""
    experiment_results = evaluate(
        ls_target, # Your AI system
        data=dataset_name, # The data to predict and grade over
        evaluators=[concision, correctness], # The evaluators to score the results
    )
    # This will be cleaned up in the next release:
    feedback = client.list_feedback(
        run_ids=[r.id for r in client.list_runs(project_name=experiment_results.experiment_name)],
        feedback_key="concision"
    )
    scores = [f.score for f in feedback]
    assert sum(scores) / len(scores) >= 0.8, "Aggregate score should be at least .8"
```

## Track results over time

Now that we've got these experiments running in an automated fashion, we want to track these results over time. We can do this from the overall `Experiments` tab in the datasets page. By default, we show evaluation metrics over time (highlighted in red). We also automatically track git metrics, to easily associate it with the branch of your code (highlighted in yellow).

<img alt="Testing tutorial over time" />

## Conclusion

That's it for this tutorial!

We've gone over how to create an initial test set, define some evaluation metrics, run experiments, compare them manually, set up CI/CD, and track results over time. This can help you iterate with confidence.

This is just the start. As mentioned earlier, evaluation is an ongoing process. For example - the datapoints you will want to evaluate on will likely continue to change over time. There are many types of evaluators you may wish to explore. For information on this, check out the [how-to guides](/langsmith/evaluation).

Additionally, there are other ways to evaluate data besides in this "offline" manner (e.g. you can evaluate production data). For more information on online evaluation, check out [Set up LLM-as-a-judge online evaluators](/langsmith/online-evaluations-llm-as-judge).

## Reference code

<Accordion title="Click to see a consolidated code snippet">
  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import openai
  from langsmith import Client, wrappers

  # Application code
  openai_client = wrappers.wrap_openai(openai.OpenAI())

  default_instructions = "Respond to the users question in a short, concise manner (one short sentence)."

  def my_app(question: str, model: str = "gpt-5.4-mini", instructions: str = default_instructions) -> str:
      return openai_client.chat.completions.create(
          model=model,
          temperature=0,
          messages=[
              {"role": "system", "content": instructions},
              {"role": "user", "content": question},
          ],
      ).choices[0].message.content

  client = Client()

  # Define dataset: these are your test cases
  dataset_name = "QA Example Dataset"
  dataset = client.create_dataset(dataset_name)

  client.create_examples(
      dataset_id=dataset.id,
      examples=[
          {
              "inputs": {"question": "What is LangChain?"},
              "outputs": {"answer": "A framework for building LLM applications"},
          },
          {
              "inputs": {"question": "What is LangSmith?"},
              "outputs": {"answer": "A platform for observing and evaluating LLM applications"},
          },
          {
              "inputs": {"question": "What is OpenAI?"},
              "outputs": {"answer": "A company that creates Large Language Models"},
          },
          {
              "inputs": {"question": "What is Google?"},
              "outputs": {"answer": "A technology company known for search"},
          },
          {
              "inputs": {"question": "What is Mistral?"},
              "outputs": {"answer": "A company that creates Large Language Models"},
          }
      ]
  )

  # Define evaluators
  eval_instructions = "You are an expert professor specialized in grading students' answers to questions."

  def correctness(inputs: dict, outputs: dict, reference_outputs: dict) -> bool:
      user_content = f"""You are grading the following question:
  {inputs['question']}
  Here is the real answer:
  {reference_outputs['answer']}
  You are grading the following predicted answer:
  {outputs['response']}
  Respond with CORRECT or INCORRECT:
  Grade:"""
      response = openai_client.chat.completions.create(
          model="gpt-5.4-mini",
          temperature=0,
          messages=[
              {"role": "system", "content": eval_instructions},
              {"role": "user", "content": user_content},
          ],
      ).choices[0].message.content
      return response == "CORRECT"

  def concision(outputs: dict, reference_outputs: dict) -> bool:
      return int(len(outputs["response"]) < 2 * len(reference_outputs["answer"]))

  # Run evaluations
  def ls_target(inputs: str) -> dict:
      return {"response": my_app(inputs["question"])}

  experiment_results_v1 = client.evaluate(
      ls_target, # Your AI system
      data=dataset_name, # The data to predict and grade over
      evaluators=[concision, correctness], # The evaluators to score the results
      experiment_prefix="openai-4o-mini", # A prefix for your experiment names to easily identify them
  )

  def ls_target_v2(inputs: str) -> dict:
      return {"response": my_app(inputs["question"], model="gpt-4-turbo")}

  experiment_results_v2 = client.evaluate(
      ls_target_v2,
      data=dataset_name,
      evaluators=[concision, correctness],
      experiment_prefix="openai-4-turbo",
  )

  instructions_v3 = "Respond to the users question in a short, concise manner (one short sentence). Do NOT use more than ten words."

  def ls_target_v3(inputs: str) -> dict:
      response = my_app(
          inputs["question"],
          model="gpt-4-turbo",
          instructions=instructions_v3
      )
      return {"response": response}

  experiment_results_v3 = client.evaluate(
      ls_target_v3,
      data=dataset_name,
      evaluators=[concision, correctness],
      experiment_prefix="strict-openai-4-turbo",
  )
  ```
</Accordion>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/evaluate-chatbot-tutorial.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Evaluate a complex agent
Source: https://docs.langchain.com/langsmith/evaluate-complex-agent

In this tutorial, we'll build a customer support bot that helps users navigate a digital music store. Then, we'll go through the three most effective types of evaluations to run on chat bots:

* **[Final response](#final-response-evaluator)**: Evaluate the agent's final response.
* **[Trajectory](#trajectory-evaluator)**: Evaluate whether the agent took the expected path (e.g., of tool calls) to arrive at the final answer.
* **[Single step](#single-step-evaluators)**: Evaluate any agent step in isolation (e.g., whether it selects the appropriate first tool for a given step).

We'll build our agent using [LangGraph](https://github.com/langchain-ai/langgraph), but the techniques and LangSmith functionality shown here are framework-agnostic.

## Setup

### Configure the environment

Let's install the required dependencies:

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install -U langgraph "langchain[openai]"
  ```

  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv add langgraph "langchain[openai]"
  ```
</CodeGroup>

Let's set up environment variables for OpenAI and [LangSmith](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-evaluate-complex-agent):

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import getpass
import os

def _set_env(var: str) -> None:
    if not os.environ.get(var):
        os.environ[var] = getpass.getpass(f"Set {var}: ")

os.environ["LANGSMITH_TRACING"] = "true"
_set_env("LANGSMITH_API_KEY")
_set_env("OPENAI_API_KEY")
```

### Download the database

We will create a SQLite database for this tutorial. SQLite is a lightweight database that is easy to set up and use. We will load the `chinook` database, which is a sample database that represents a digital media store. For more information, see [Chinook sample database](https://www.sqlitetutorial.net/sqlite-sample-database/).

For convenience, we have hosted the database in a public GCS bucket:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import requests

url = "https://storage.googleapis.com/benchmarks-artifacts/chinook/Chinook.db"
response = requests.get(url)

if response.status_code == 200:
    # Open a local file in binary write mode
    with open("chinook.db", "wb") as file:
        # Write the content of the response (the file) to the local file
        file.write(response.content)
    print("File downloaded and saved as Chinook.db")
else:
    print(f"Failed to download the file. Status code: {response.status_code}")
```

Here's a sample of the data in the db:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import sqlite3
