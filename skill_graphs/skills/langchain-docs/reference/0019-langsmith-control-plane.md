# LangSmith control plane
Source: https://docs.langchain.com/langsmith/control-plane

The *control plane* is the part of LangSmith that manages deployments. It includes the control plane UI, where users create and update [Agent Servers](/langsmith/agent-server), and the control plane APIs, which support the UI and provide programmatic access.

When you make an update through the control plane, the update is stored in the control plane state. The [data plane](/langsmith/data-plane) “listener” polls for these updates by calling the control plane APIs. The control plane never connects to the data plane directly.

## Control plane UI

From the control plane UI, you can:

* View a list of outstanding deployments.
* View details of an individual deployment.
* Create a new deployment.
* Update a deployment.
* Update environment variables for a deployment.
* View build and server logs of a deployment.
* View deployment metrics such as CPU and memory usage.
* Delete a deployment.

The Control plane UI is embedded in [LangSmith](https://docs.smith.langchain.com).

## Control plane API

This section describes the data model of the control plane API. The API is used to create, update, and delete deployments. See the [control plane API reference](/langsmith/api-ref-control-plane) for more details.

### Integrations

An integration is an abstraction for a `git` repository provider (e.g. GitHub). It contains all of the required metadata needed to connect with and deploy from a `git` repository.

### Deployments

A deployment is an instance of an Agent Server. A single deployment can have many revisions.

### Revisions

A revision is an iteration of a deployment. When a new deployment is created, an initial revision is automatically created. To deploy code changes or update secrets for a deployment, a new revision must be created.

### Listeners

A listener is an instance of a ["listener" application](/langsmith/data-plane#listener-application). A listener contains metadata about the application (e.g. version) and metadata about the compute infrastructure where it can deploy to (e.g. Kubernetes namespaces).

The listener data model only applies for [Self-Hosted](/langsmith/self-hosted) deployments.

## Control plane features

This section describes various features of the control plane.

### Deployment types

For simplicity, the control plane offers two deployment types with different resource allocations: `Development` and `Production`.

| **Deployment Type** | **CPU/Memory**  | **Scaling**       | **Database**                                                                     |
| ------------------- | --------------- | ----------------- | -------------------------------------------------------------------------------- |
| Development         | 1 CPU, 1 GB RAM | Up to 1 replica   | 10 GB disk, no backups                                                           |
| Production          | 2 CPU, 2 GB RAM | Up to 10 replicas | Autoscaling disk, automatic backups, highly available (multi-zone configuration) |

CPU and memory resources are per replica.

<Warning>
  **Immutable Deployment Type**
  Once a deployment is created, the deployment type cannot be changed.
</Warning>

<Info>
  **Self-Hosted Deployment**
  Resources for [Self-Hosted](/langsmith/self-hosted) deployments can be fully customized. Deployment types are only applicable for [Cloud](/langsmith/cloud) deployments.
</Info>

#### Production

`Production` type deployments are suitable for "production" workloads. For example, select `Production` for customer-facing applications in the critical path.

Resources for `Production` type deployments can be manually increased on a case-by-case basis depending on use case and capacity constraints. Contact support via [support.langchain.com](https://support.langchain.com) to request an increase in resources.

#### Development

`Development` type deployments are suitable development and testing. For example, select `Development` for internal testing environments. `Development` type deployments are not suitable for "production" workloads.

<Danger>
  **Preemptible Compute Infrastructure**
  `Development` type deployments (API server, queue server, and database) are provisioned on preemptible compute infrastructure. This means the compute infrastructure **may be terminated at any time without notice**. This may result in intermittent...

  * Redis connection timeouts/errors
  * Postgres connection timeouts/errors
  * Failed or retrying background runs

  This behavior is expected. Preemptible compute infrastructure **significantly reduces the cost to provision a `Development` type deployment**. By design, Agent Server is fault-tolerant. The implementation will automatically attempt to recover from Redis/Postgres connection errors and retry failed background runs.

  `Production` type deployments are provisioned on durable compute infrastructure, not preemptible compute infrastructure.
</Danger>

Database disk size for `Development` type deployments can be manually increased on a case-by-case basis depending on use case and capacity constraints. For most use cases, [TTLs](/langsmith/configure-ttl) should be configured to manage disk usage. Contact support via [support.langchain.com](https://support.langchain.com) to request an increase in resources.

### Database provisioning

The control plane and [data plane](/langsmith/data-plane) "listener" application coordinate to automatically create a Postgres database for each deployment. The database serves as the [persistence layer](/oss/python/langgraph/stores) for the deployment.

When implementing a LangGraph application, a [checkpointer](/oss/python/langgraph/checkpointers#checkpointer-libraries) does not need to be configured by the developer. Instead, a checkpointer is automatically configured for the graph. Any checkpointer configured for a graph will be replaced by the one that is automatically configured.

There is no direct access to the database. All access to the database occurs through the [Agent Server](/langsmith/agent-server).

The database is never deleted until the deployment itself is deleted.

<Info>
  A custom Postgres instance can be configured for [Self-Hosted](/langsmith/self-hosted) deployments.
</Info>

### Asynchronous deployment

Infrastructure for deployments and revisions are provisioned and deployed asynchronously. They are not deployed immediately after submission. Currently, deployment can take up to several minutes.

* When a new deployment is created, a new database is created for the deployment. Database creation is a one-time step. This step contributes to a longer deployment time for the initial revision of the deployment.
* When a subsequent revision is created for a deployment, there is no database creation step. The deployment time for a subsequent revision is significantly faster compared to the deployment time of the initial revision.
* The deployment process for each revision contains a build step, which can take up to a few minutes.

The control plane and [data plane](/langsmith/data-plane) "listener" application coordinate to achieve asynchronous deployments.

### Monitoring

After a deployment is ready, the control plane monitors the deployment and records various metrics, such as:

* CPU and memory usage of the deployment.
* Number of container restarts.
* Number of replicas (this will increase with [autoscaling](/langsmith/data-plane#autoscaling)).
* [PostgreSQL](/langsmith/data-plane#postgresql) CPU, memory usage, and disk usage.
* [Agent Server queue](/langsmith/agent-server#task-queue) pending/active run count.
* [Agent Server API](/langsmith/agent-server) success response count, error response count, and latency.

These metrics are displayed as charts in the Control Plane UI.

### LangSmith integration

A [LangSmith](/langsmith/observability) tracing project is automatically created for each deployment. The tracing project has the same name as the deployment. When creating a deployment, the `LANGCHAIN_TRACING` and `LANGSMITH_API_KEY`/`LANGCHAIN_API_KEY` environment variables do not need to be specified; they are set automatically by the control plane.

When a deployment is deleted, the traces and the tracing project are not deleted.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/control-plane.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Core capabilities overview
Source: https://docs.langchain.com/langsmith/core-capabilities

Overview of Agent Server core capabilities including streaming, human-in-the-loop, MCP, A2A, distributed tracing, webhooks, and double-texting.

Agent Server provides a set of capabilities for building and operating production agents. This section covers:

<CardGroup>
  <Card title="Event streaming API" icon="bolt" href="/langsmith/event-streaming">
    Stream messages, state, tool calls, and subgraphs from a deployed agent through typed projections. Requires `langgraph-api>=0.10.0`.
  </Card>

  <Card title="Streaming API" icon="player-play" href="/langsmith/streaming">
    The `stream_mode`-based API for streaming run outputs. Supported alongside event streaming.
  </Card>

  <Card title="Human-in-the-loop" icon="user-check" href="/langsmith/add-human-in-the-loop">
    Pause agent execution to review, edit, or approve tool calls before continuing.
  </Card>

  <Card title="Time travel" icon="clock" href="/langsmith/human-in-the-loop-time-travel">
    Replay agent runs from any prior state to debug or explore alternative paths.
  </Card>

  <Card title="MCP endpoint" icon="plug" href="/langsmith/server-mcp">
    Expose your agents as MCP tools, accessible to any MCP-compliant client.
  </Card>

  <Card title="A2A endpoint" icon="arrows-exchange" href="/langsmith/server-a2a">
    Enable agent-to-agent communication using the A2A protocol.
  </Card>

  <Card title="Distributed tracing" icon="git-merge" href="/langsmith/agent-server-distributed-tracing">
    Unify traces across services when calling Agent Server from external applications.
  </Card>

  <Card title="Webhooks" icon="webhook" href="/langsmith/use-webhooks">
    Trigger external systems in response to run events from your deployed agent.
  </Card>

  <Card title="Double-texting" icon="messages" href="/langsmith/double-texting">
    Control how Agent Server handles a new message while a run is already in progress.
  </Card>
</CardGroup>

### Durable execution

At its core, LangSmith Deployment is a durable execution engine. Your agents run on a managed task queue with automatic checkpointing, so any run can be retried, replayed, or resumed from the exact point of interruption, not from scratch.

Because execution is durable, agents can do things that would be fragile or impossible in a stateless runtime:

* **Wait for external input.** An agent calls [`interrupt()`](/langsmith/add-human-in-the-loop) and the runtime checkpoints its state, frees resources, and waits for a human to approve a transaction, a reviewer to edit a draft, or another system to return results. When [`Command(resume=...)`](/langsmith/add-human-in-the-loop) arrives hours or days later, execution picks up exactly where it stopped. This is the primitive underneath [human-in-the-loop](/langsmith/add-human-in-the-loop) workflows and [time-travel debugging](/langsmith/human-in-the-loop-time-travel).
* **Run in the background.** [Background runs](/langsmith/background-run) execute without blocking the caller. The runtime manages the full lifecycle (queuing, execution, checkpointing, completion) while the client moves on.
* **Run on a schedule.** [Cron jobs](/langsmith/cron-jobs) trigger agent execution on a recurring cadence. A daily summary agent, a weekly report, a periodic data sync. The runtime starts a new execution on schedule with the same durability guarantees.
* **Handle concurrent input.** When a user sends new input while an agent is mid-run ([double-texting](/langsmith/double-texting)), the runtime can queue it, cancel the in-progress run, or process both in parallel without data races or corrupted state.
* **Retry on failure.** Configurable [retry policies](/oss/python/langgraph/use-graph-api#add-retry-policies) control backoff, max attempts, and which exceptions trigger retries on a per-node basis. Runs survive process restarts, infrastructure failures, and code revisions mid-execution.

For details on how containers, processes, and the task queue work together, see [Agent Server: Runtime architecture](/langsmith/agent-server#runtime-architecture). For scaling and throughput tuning, see [Configure Agent Server for scale](/langsmith/agent-server-scale).

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/core-capabilities.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
