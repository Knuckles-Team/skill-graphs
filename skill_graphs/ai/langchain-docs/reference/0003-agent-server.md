# Agent Server
Source: https://docs.langchain.com/langsmith/agent-server

LangSmith Deployment's **Agent Server** offers an API for creating and managing agent-based applications. It is built on the concept of [assistants](/langsmith/assistants), which are agents configured for specific tasks, and includes built-in [persistence](/oss/python/langgraph/stores) and a [**task queue**](#task-queue). This versatile API supports a wide range of agentic application use cases, from background processing to real-time interactions.

Use Agent Server to create and manage:

<CardGroup>
  <Card title="Assistants" icon="robot" href="/langsmith/assistants" />

  <Card title="Threads" icon="messages" href="/langsmith/use-threads" />

  <Card title="Runs" icon="player-play" href="/langsmith/runs" />

  <Card title="Cron jobs" icon="clock" href="/langsmith/cron-jobs" />
</CardGroup>

<Tip>
  **API reference**<br />
  For detailed information on the API endpoints and data models, refer to the [Agent Server API reference](/langsmith/server-api-ref).
</Tip>

## Application structure

To deploy an Agent Server application, you need to specify the graph(s) you want to deploy, as well as any relevant configuration settings, such as dependencies and environment variables.

Read the [application structure](/langsmith/application-structure) guide to learn how to structure your LangGraph application for deployment.

<Note>
  [LangSmith cloud](/langsmith/cloud) manages the database for you. If you're deploying on your [own infrastructure](/langsmith/self-hosted), you'll need to set it up yourself.
</Note>

## Parts of a deployment

When you deploy Agent Server, you are deploying one or more [graphs](#graphs), a database for [persistence](/oss/python/langgraph/persistence), and a [task queue](#task-queue).

### Graphs

When you deploy a graph with Agent Server, you are deploying a "blueprint" for an [Assistant](/langsmith/assistants).

A graph most commonly implements an [agent](/oss/python/langgraph/workflows-agents), but it does not have to. For example, a graph could implement a simple chatbot that only supports back-and-forth conversation, without the ability to influence any application control flow. In reality, as applications get more complex, a graph will often implement a more complex flow that may use [multiple agents](/oss/python/langchain/multi-agent) working in tandem.

Graphs don't have to be written with LangGraph. You can also deploy agents built with other frameworks—such as Strands or Google ADK—using the LangGraph Functional API. For details, refer to [Deploy other frameworks](/langsmith/deploy-other-frameworks).

#### Graph loading and compilation

How and when your graph is compiled depends on how you register it in your [application structure](/langsmith/application-structure):

1. **Compiled graph** (recommended): Export an already-compiled `CompiledGraph` instance. The server loads it once at container startup and reuses it for every run—no compilation overhead per request.
2. **Factory function**: Export an agent factory function that the server invokes each time it needs the graph. Use this only when you need per-run graph customization (for example, choosing different models or tools based on the assistant config). Keep factory functions lightweight, since they run on every invocation.

<Tip>
  Use a compiled graph unless you specifically need per-run customization. Factory functions add overhead on every invocation; compiled graphs do not.
</Tip>

In both cases, the server automatically injects the checkpointer and memory store configured for that deployment at runtime. **Do not configure these in your graph code** because the server needs to manage them for other operations.

### Persistence

Agent Server persists three types of data, all backed by [PostgreSQL](https://www.postgresql.org/) by default:

* **Core resource data**: assistants, threads, runs, and cron jobs. Always stored in PostgreSQL.
* **Checkpoints (short-term memory)**: snapshots of graph execution state written at each step. They make runs durable: if a worker is interrupted, the run can resume from the last checkpoint rather than from the beginning. Durability mode controls checkpoint frequency—`async` (default) writes after each step; `exit` stores only the final state. LangSmith stores this in PostgreSQL by default; but you can switch to [MongoDB](https://www.mongodb.com/) or a custom implementation. For details, refer to [Configure checkpointer backend](/langsmith/configure-checkpointer).
* **Store (long-term memory)**: memory that persists across threads, enabling agents to retain information between separate conversations. Stored in PostgreSQL by default but can be replaced with a custom implementation. For details, refer to [Add custom store](/langsmith/custom-store).

### Task queue

When a client creates a run, the API server enqueues it and a queue worker picks it up for execution. Workers can also be signaled to cancel a run in progress, and publish output events that open `/stream` connections forward to the client in real time.

[Redis](https://redis.io/) handles the signaling, cancellation, and streaming pub/sub between API servers and queue workers. It stores only ephemeral data—no user or run data persists in Redis. Run data itself is always read from and written to PostgreSQL.

For more information on how to set up and manage these components, review the [hosting options](/langsmith/platform-setup) guide.

## Runtime architecture

### Deployment modes

Agent Server supports three runtime configurations:

* **Single host**: The API server manages the task queue directly with no separate queue workers. This is the default for self-hosted deployments and is suitable for development and low-traffic use cases.
* **Split API and queue**: Dedicated queue workers handle run execution on separate hosts from the API server. For self-hosted deployments, enable this by setting `queue.enabled: true` in your configuration. Each tier scales independently—API servers scale on request volume, queue workers scale on pending run count.
* **Distributed runtime**: The API and queue processes are again run separately, but instead of a single queue process handling both the orchestration and execution of your graph, the distributed runtime uses one process for orchestration and one process for execution. Use this for large-scale deployments with high concurrency requirements.

The container architecture and run lifecycle described below apply to single host and split API and queue configurations.

### Container architecture

A typical deployment consists of two kinds of long-running containers, both built from the same Docker image (a base image with your project code installed on top):

* **API servers** handle client requests (creating runs, reading thread state, streaming results) but do not execute agent code themselves.
* **Queue workers** are the execution engine. They listen to the durable task queue, execute your graph code, and write checkpoints.

Containers are **stateless** but persistent. At least 1 queue worker must listen to the task queue at any time to ensure no runs are orphaned. The containers can serve many runs over their lifetime.

API servers and queue workers are separate container pools and [scale independently](/langsmith/data-plane#autoscaling).

```mermaid theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
flowchart TB
    User["User"]

    API["API Servers"]

    subgraph WorkerContainer["Worker Containers"]
        QueueLoop["Queue Loop"]
        W1["Worker"]
        W2["Worker"]
        Wn["..."]
        QueueLoop -->|dispatch| W1
        QueueLoop -->|dispatch| W2
    end

    DB[(Postgres)]
    Redis[(Redis)]

    User -->|request| API
    API -->|create run| DB
    API -->|notify| Redis

    Redis -->|wake| QueueLoop
    QueueLoop -->|claim next run| DB

    WorkerContainer -->|save checkpoints / update status| DB
    WorkerContainer -->|publish events| Redis

    Redis -->|stream events| API
    API -->|SSE response| User

    style User fill:#F2FAFF,stroke:#40668D,stroke-width:2px,color:#2F4B68
    style API fill:#EBD0F0,stroke:#885270,stroke-width:2px,color:#441E33
    style DB fill:#E5F4FF,stroke:#006DDD,stroke-width:2px,color:#030710
    style Redis fill:#F8E8E6,stroke:#B27D75,stroke-width:2px,color:#634643
    style WorkerContainer fill:#F6FFDB,stroke:#6E8900,stroke-width:2px,color:#2E3900
    style QueueLoop fill:#FDF3FF,stroke:#7E65AE,stroke-width:2px,color:#504B5F
    style W1 fill:#F2FAFF,stroke:#40668D,stroke-width:2px,color:#2F4B68
    style W2 fill:#F2FAFF,stroke:#40668D,stroke-width:2px,color:#2F4B68
    style Wn fill:#F2FAFF,stroke:#40668D,stroke-width:2px,color:#2F4B68
```

### Run execution lifecycle

When you invoke a run, the request flows through several components:

1. A client sends a request to an API server, which creates a pending run in the durable task queue.
2. A queue worker picks up the run, acquires a lease on it, loads the appropriate graph, and begins execution. The queue enforces that at most 1 run can be executed for a given thread at one time.
3. As the graph executes, the worker writes checkpoints to the persistence layer (the frequency depends on the [durability mode](/oss/python/langgraph/checkpointers#durability-modes)) and broadcasts streaming events over the configured pubsub provider.
4. If the client opened a `/stream` connection, the API server subscribes to the pubsub channel and forwards events to the client via server-sent events in real time.
5. When execution completes, the worker updates the run status and releases its slot for the next run.

Each worker handles up to [`N_JOBS_PER_WORKER`](/langsmith/env-var#n_jobs_per_worker) runs concurrently (default: 10), so a single worker container serves many runs in parallel. See [Configure Agent Server for scale](/langsmith/agent-server-scale) for tuning guidance.

## Learn more

* [Application Structure](/langsmith/application-structure) guide explains how to structure your application for deployment.
* The [API Reference](https://docs.langchain.com/langsmith/server-api-ref) provides detailed information on the API endpoints and data models.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/agent-server.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# A2A JSON-RPC
Source: https://docs.langchain.com/langsmith/agent-server-api/a2a/a2a-json-rpc

/langsmith/agent-server-openapi.json post /a2a/{assistant_id}
Communicate with an assistant using the Agent-to-Agent (A2A) Protocol over JSON-RPC 2.0.
This endpoint accepts a JSON-RPC envelope and dispatches based on `method`.

**Supported Methods:**
- `message/send`: Send a message and wait for the final Task result.
- `message/stream`: Send a message and receive Server-Sent Events (SSE) JSON-RPC responses.
- `tasks/get`: Fetch the current state of a Task by ID.
- `tasks/cancel`: Request cancellation (currently not supported; returns an error).

**LangGraph Mapping:**
- `message.contextId` maps to LangGraph `thread_id`.

**Notes:**
- Only `text` and `data` parts are supported; `file` parts are not.
- If `message.contextId` is omitted, a new context is created.
- Text parts require the assistant input schema to include a `messages` field.

# Count Assistants
Source: https://docs.langchain.com/langsmith/agent-server-api/assistants/count-assistants

/langsmith/agent-server-openapi.json post /assistants/count
Get the count of assistants matching the specified criteria.

# Create Assistant
Source: https://docs.langchain.com/langsmith/agent-server-api/assistants/create-assistant

/langsmith/agent-server-openapi.json post /assistants
Create an assistant.

An initial version of the assistant will be created and the assistant is set to that version. To change versions, use the `POST /assistants/{assistant_id}/latest` endpoint.

# Delete Assistant
Source: https://docs.langchain.com/langsmith/agent-server-api/assistants/delete-assistant

/langsmith/agent-server-openapi.json delete /assistants/{assistant_id}
Delete an assistant by ID.

All versions of the assistant will be deleted as well.

# Get Assistant
Source: https://docs.langchain.com/langsmith/agent-server-api/assistants/get-assistant

/langsmith/agent-server-openapi.json get /assistants/{assistant_id}
Get an assistant by ID.

# Get Assistant Graph
Source: https://docs.langchain.com/langsmith/agent-server-api/assistants/get-assistant-graph

/langsmith/agent-server-openapi.json get /assistants/{assistant_id}/graph
Get an assistant by ID.

# Get Assistant Schemas
Source: https://docs.langchain.com/langsmith/agent-server-api/assistants/get-assistant-schemas

/langsmith/agent-server-openapi.json get /assistants/{assistant_id}/schemas
Get an assistant by ID.

# Get Assistant Subgraphs
Source: https://docs.langchain.com/langsmith/agent-server-api/assistants/get-assistant-subgraphs

/langsmith/agent-server-openapi.json get /assistants/{assistant_id}/subgraphs
Get an assistant's subgraphs.

# Get Assistant Subgraphs by Namespace
Source: https://docs.langchain.com/langsmith/agent-server-api/assistants/get-assistant-subgraphs-by-namespace

/langsmith/agent-server-openapi.json get /assistants/{assistant_id}/subgraphs/{namespace}
Get an assistant's subgraphs filtered by namespace.

# Get Assistant Versions
Source: https://docs.langchain.com/langsmith/agent-server-api/assistants/get-assistant-versions

/langsmith/agent-server-openapi.json post /assistants/{assistant_id}/versions
Get all versions of an assistant.

# Patch Assistant
Source: https://docs.langchain.com/langsmith/agent-server-api/assistants/patch-assistant

/langsmith/agent-server-openapi.json patch /assistants/{assistant_id}
Update an assistant.

# Search Assistants
Source: https://docs.langchain.com/langsmith/agent-server-api/assistants/search-assistants

/langsmith/agent-server-openapi.json post /assistants/search
Search for assistants.

This endpoint also functions as the endpoint to list all assistants.

# Set Latest Assistant Version
Source: https://docs.langchain.com/langsmith/agent-server-api/assistants/set-latest-assistant-version

/langsmith/agent-server-openapi.json post /assistants/{assistant_id}/latest
Set the latest version for an assistant.

# Count Crons
Source: https://docs.langchain.com/langsmith/agent-server-api/crons/count-crons

/langsmith/agent-server-openapi.json post /runs/crons/count
Get the count of crons matching the specified criteria.

# Create Cron
Source: https://docs.langchain.com/langsmith/agent-server-api/crons/create-cron

/langsmith/agent-server-openapi.json post /runs/crons
Create a cron to schedule runs on new threads.

# Create Thread Cron
Source: https://docs.langchain.com/langsmith/agent-server-api/crons/create-thread-cron

/langsmith/agent-server-openapi.json post /threads/{thread_id}/runs/crons
Create a cron to schedule runs on a thread.

# Delete Cron
Source: https://docs.langchain.com/langsmith/agent-server-api/crons/delete-cron

/langsmith/agent-server-openapi.json delete /runs/crons/{cron_id}
Delete a cron by ID.

# Get Cron
Source: https://docs.langchain.com/langsmith/agent-server-api/crons/get-cron

/langsmith/agent-server-openapi.json get /runs/crons/{cron_id}
Get a cron by ID.

# Search Crons
Source: https://docs.langchain.com/langsmith/agent-server-api/crons/search-crons

/langsmith/agent-server-openapi.json post /runs/crons/search
Search all active crons

# Update Cron
Source: https://docs.langchain.com/langsmith/agent-server-api/crons/update-cron

/langsmith/agent-server-openapi.json patch /runs/crons/{cron_id}
Update a cron job by ID.

# MCP Get
Source: https://docs.langchain.com/langsmith/agent-server-api/mcp/mcp-get

/langsmith/agent-server-openapi.json get /mcp/
Implemented according to the Streamable HTTP Transport specification.

# MCP Post
Source: https://docs.langchain.com/langsmith/agent-server-api/mcp/mcp-post

/langsmith/agent-server-openapi.json post /mcp/
Implemented according to the Streamable HTTP Transport specification.
Sends a JSON-RPC 2.0 message to the server.

- **Request**: Provide an object with `jsonrpc`, `id`, `method`, and optional `params`.
- **Response**: Returns a JSON-RPC response or acknowledgment.

**Notes:**
- Stateless: Sessions are not persisted across requests.

# Terminate Session
Source: https://docs.langchain.com/langsmith/agent-server-api/mcp/terminate-session

/langsmith/agent-server-openapi.json delete /mcp/
Implemented according to the Streamable HTTP Transport specification.
Terminate an MCP session. The server implementation is stateless, so this is a no-op.

# Create Background Run
Source: https://docs.langchain.com/langsmith/agent-server-api/stateless-runs/create-background-run

/langsmith/agent-server-openapi.json post /runs
Create a run and return the run ID immediately. Don't wait for the final run output.

# Create Run Batch
Source: https://docs.langchain.com/langsmith/agent-server-api/stateless-runs/create-run-batch

/langsmith/agent-server-openapi.json post /runs/batch
Create a batch of runs and return immediately.

# Create Run, Stream Output
Source: https://docs.langchain.com/langsmith/agent-server-api/stateless-runs/create-run-stream-output

/langsmith/agent-server-openapi.json post /runs/stream
Create a run and stream the output.

# Create Run, Wait for Output
Source: https://docs.langchain.com/langsmith/agent-server-api/stateless-runs/create-run-wait-for-output

/langsmith/agent-server-openapi.json post /runs/wait
Create a run, wait for the final output and then return it.

# Delete an item.
Source: https://docs.langchain.com/langsmith/agent-server-api/store/delete-an-item

/langsmith/agent-server-openapi.json delete /store/items

# List namespaces with optional match conditions.
Source: https://docs.langchain.com/langsmith/agent-server-api/store/list-namespaces-with-optional-match-conditions

/langsmith/agent-server-openapi.json post /store/namespaces

# Retrieve a single item.
Source: https://docs.langchain.com/langsmith/agent-server-api/store/retrieve-a-single-item

/langsmith/agent-server-openapi.json get /store/items

# Search or list items within a namespace prefix.
Source: https://docs.langchain.com/langsmith/agent-server-api/store/search-or-list-items-within-a-namespace-prefix

/langsmith/agent-server-openapi.json post /store/items/search
Lists items ordered by last updated time. If a `query` is provided, performs a natural language search instead. Supports pagination via `limit` and `offset`, and filtering via `filter`.

# Store or update an item.
Source: https://docs.langchain.com/langsmith/agent-server-api/store/store-or-update-an-item

/langsmith/agent-server-openapi.json put /store/items

# Protocol v2 Command
Source: https://docs.langchain.com/langsmith/agent-server-api/streaming/protocol-v2-command

/langsmith/agent-server-openapi.json post /threads/{thread_id}/commands
Send a single protocol command scoped to a thread. The request body is a `ProtocolCommand` envelope with a `method` (e.g. `run.start`, `input.respond`, `agent.getTree`) and method-specific `params`. The response is either a `ProtocolSuccess` (with method-specific `result`) or a `ProtocolError`.

Commands that create runs (`run.start`, `input.respond`) leave the run executing in the background on the worker queue. Event streaming for that run is observed via a concurrent `POST /threads/{thread_id}/stream/events` connection.

WebSocket clients use the same command envelope in-band on `/threads/{thread_id}/stream/events` and additionally have access to `subscription.subscribe` / `subscription.unsubscribe` over the same connection.

# Protocol v2 Event Stream (SSE)
Source: https://docs.langchain.com/langsmith/agent-server-api/streaming/protocol-v2-event-stream-sse

/langsmith/agent-server-openapi.json post /threads/{thread_id}/stream/events
Open a connection-scoped SSE event stream for a thread. The request body is a `ProtocolEventStreamRequest` carrying channel and namespace filters; the server replies with `Content-Type: text/event-stream` and pushes matching `ProtocolEvent` frames for the lifetime of the connection. Closing the connection unsubscribes — no state is persisted server-side.

Reconnect: clients pass the last `seq` they received as `since` in the body. Buffered events with `seq > since` are replayed before the stream goes live. The endpoint is POST-only, so browser-native `EventSource` auto-resume (`Last-Event-ID`) does not apply — clients drive resume explicitly via the body.

# API Documentation
Source: https://docs.langchain.com/langsmith/agent-server-api/system/api-documentation

/langsmith/agent-server-openapi.json get /docs
A local reference to the Agent Server API documentation.

# Health Check
Source: https://docs.langchain.com/langsmith/agent-server-api/system/health-check

/langsmith/agent-server-openapi.json get /ok
Check the health status of the server. Optionally check database connectivity.

# Server Information
Source: https://docs.langchain.com/langsmith/agent-server-api/system/server-information

/langsmith/agent-server-openapi.json get /info
Get server version information, feature flags, and metadata.

# System Metrics
Source: https://docs.langchain.com/langsmith/agent-server-api/system/system-metrics

/langsmith/agent-server-openapi.json get /metrics
Get system metrics in Prometheus or JSON format for monitoring and observability.

# Cancel Run
Source: https://docs.langchain.com/langsmith/agent-server-api/thread-runs/cancel-run

/langsmith/agent-server-openapi.json post /threads/{thread_id}/runs/{run_id}/cancel

# Cancel Runs
Source: https://docs.langchain.com/langsmith/agent-server-api/thread-runs/cancel-runs

/langsmith/agent-server-openapi.json post /runs/cancel
Cancel one or more runs. Can cancel runs by thread ID and run IDs, or by status filter.

# Create Background Run
Source: https://docs.langchain.com/langsmith/agent-server-api/thread-runs/create-background-run

/langsmith/agent-server-openapi.json post /threads/{thread_id}/runs
Create a run in existing thread, return the run ID immediately. Don't wait for the final run output.

# Create Run, Stream Output
Source: https://docs.langchain.com/langsmith/agent-server-api/thread-runs/create-run-stream-output

/langsmith/agent-server-openapi.json post /threads/{thread_id}/runs/stream
Create a run in existing thread. Stream the output.

# Create Run, Wait for Output
Source: https://docs.langchain.com/langsmith/agent-server-api/thread-runs/create-run-wait-for-output

/langsmith/agent-server-openapi.json post /threads/{thread_id}/runs/wait
Create a run in existing thread. Wait for the final output and then return it.

# Delete Run
Source: https://docs.langchain.com/langsmith/agent-server-api/thread-runs/delete-run

/langsmith/agent-server-openapi.json delete /threads/{thread_id}/runs/{run_id}
Delete a run by ID.

# Get Run
Source: https://docs.langchain.com/langsmith/agent-server-api/thread-runs/get-run

/langsmith/agent-server-openapi.json get /threads/{thread_id}/runs/{run_id}
Get a run by ID.

# Join Run
Source: https://docs.langchain.com/langsmith/agent-server-api/thread-runs/join-run

/langsmith/agent-server-openapi.json get /threads/{thread_id}/runs/{run_id}/join
Wait for a run to finish.

# Join Run Stream
Source: https://docs.langchain.com/langsmith/agent-server-api/thread-runs/join-run-stream

/langsmith/agent-server-openapi.json get /threads/{thread_id}/runs/{run_id}/stream
Join a run stream. This endpoint streams output in real-time from a run similar to the /threads/__THREAD_ID__/runs/stream endpoint. If the run has been created with `stream_resumable=true`, the stream can be resumed from the last seen event ID.

# List Runs
Source: https://docs.langchain.com/langsmith/agent-server-api/thread-runs/list-runs

/langsmith/agent-server-openapi.json get /threads/{thread_id}/runs
List runs for a thread.

# Copy Thread
Source: https://docs.langchain.com/langsmith/agent-server-api/threads/copy-thread

/langsmith/agent-server-openapi.json post /threads/{thread_id}/copy
Create a new thread with a copy of the state and checkpoints from an existing thread.

# Count Threads
Source: https://docs.langchain.com/langsmith/agent-server-api/threads/count-threads

/langsmith/agent-server-openapi.json post /threads/count
Get the count of threads matching the specified criteria.

# Create Thread
Source: https://docs.langchain.com/langsmith/agent-server-api/threads/create-thread

/langsmith/agent-server-openapi.json post /threads
Create a thread.

# Delete Thread
Source: https://docs.langchain.com/langsmith/agent-server-api/threads/delete-thread

/langsmith/agent-server-openapi.json delete /threads/{thread_id}
Delete a thread by ID.

# Get Thread
Source: https://docs.langchain.com/langsmith/agent-server-api/threads/get-thread

/langsmith/agent-server-openapi.json get /threads/{thread_id}
Get a thread by ID.

# Get Thread History
Source: https://docs.langchain.com/langsmith/agent-server-api/threads/get-thread-history

/langsmith/agent-server-openapi.json get /threads/{thread_id}/history
Get all past states for a thread.

# Get Thread History Post
Source: https://docs.langchain.com/langsmith/agent-server-api/threads/get-thread-history-post

/langsmith/agent-server-openapi.json post /threads/{thread_id}/history
Get all past states for a thread.

# Get Thread State
Source: https://docs.langchain.com/langsmith/agent-server-api/threads/get-thread-state

/langsmith/agent-server-openapi.json get /threads/{thread_id}/state
Get state for a thread.

The latest state of the thread (i.e. latest checkpoint) is returned.

# Get Thread State At Checkpoint
Source: https://docs.langchain.com/langsmith/agent-server-api/threads/get-thread-state-at-checkpoint

/langsmith/agent-server-openapi.json get /threads/{thread_id}/state/{checkpoint_id}
Get state for a thread at a specific checkpoint.

# Get Thread State At Checkpoint
Source: https://docs.langchain.com/langsmith/agent-server-api/threads/get-thread-state-at-checkpoint-1

/langsmith/agent-server-openapi.json post /threads/{thread_id}/state/checkpoint
Get state for a thread at a specific checkpoint.

# Join Thread Stream
Source: https://docs.langchain.com/langsmith/agent-server-api/threads/join-thread-stream

/langsmith/agent-server-openapi.json get /threads/{thread_id}/stream
This endpoint streams output in real-time from a thread. The stream will include the output of each run executed sequentially on the thread and will remain open indefinitely. It is the responsibility of the calling client to close the connection.

# Patch Thread
Source: https://docs.langchain.com/langsmith/agent-server-api/threads/patch-thread

/langsmith/agent-server-openapi.json patch /threads/{thread_id}
Update a thread.

# Prune Threads
Source: https://docs.langchain.com/langsmith/agent-server-api/threads/prune-threads

/langsmith/agent-server-openapi.json post /threads/prune
Prune threads by ID. The 'delete' strategy removes threads entirely. The 'keep_latest' strategy prunes old checkpoints but keeps threads and their latest state.

# Search Threads
Source: https://docs.langchain.com/langsmith/agent-server-api/threads/search-threads

/langsmith/agent-server-openapi.json post /threads/search
Search for threads.

This endpoint also functions as the endpoint to list all threads.

# Update Thread State
Source: https://docs.langchain.com/langsmith/agent-server-api/threads/update-thread-state

/langsmith/agent-server-openapi.json post /threads/{thread_id}/state
Add state to a thread.
