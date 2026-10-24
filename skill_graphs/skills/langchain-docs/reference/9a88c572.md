# Agent Server changelog
Source: https://docs.langchain.com/langsmith/agent-server-changelog

<Callout icon="rss">
  **Subscribe**: Our changelog includes an [RSS feed](https://docs.langchain.com/langsmith/agent-server-changelog/rss.xml) that can integrate with [Slack](https://slack.com/help/articles/218688467-Add-RSS-feeds-to-Slack), [email](https://zapier.com/apps/email/integrations/rss/1441/send-new-rss-feed-entries-via-email), Discord bots like [Readybot](https://readybot.io/) or [RSS Feeds to Discord Bot](https://rss.app/en/bots/rssfeeds-discord-bot), and other subscription tools.
</Callout>

[Agent Server](/langsmith/agent-server) is an API platform for creating and managing agent-based applications. It provides built-in persistence, a task queue, and supports deploying, configuring, and running assistants (agentic workflows) at scale. This changelog documents all notable updates, features, and fixes to Agent Server releases.

<Update label="2026-06-10">
  ## v0.10.0

  ### General Notes

  * v0.10.0 is the stable promotion of the v0.10.0rc line. Note in particular the potentially breaking security changes in 0.10.0rc1.
  * Includes dependency and security maintenance updates.

  ### New Features

  * Added DeltaChannel-aware pruning that preserves only the minimum ancestor checkpoints needed for state reconstruction, replacing the previous behavior that refused to prune threads with active delta channels. Supported across the Postgres, SQLite, DeferredDelete, and in-memory runtimes.
</Update>

<Update label="2026-06-05">
  ## v0.10.0rc3

  ### Fixes

  * Fixed protocol v2 event streaming against JS sidecar (remote) graphs, which were incorrectly served through the legacy reconstruction path. Remote graphs now use LangGraphJS's native v3 stream for v2 event-streaming runs, resolving tool calls not rendering, headless interrupts never executing or resuming, and `400: tool_use ids must be unique` errors on the final message after a resume.
</Update>

<Update label="2026-06-02">
  ## v0.10.0rc2

  ### Fixes

  * Fixed protocol v2 runs on JS graphs failing silently. The sidecar rejected `streamEvents` with a 400 due to strict stream-mode validation, the error was swallowed, and runs falsely reported success with 0 nodes executed. Relaxed stream-mode validation at the HTTP boundary and now raise a clear error on non-2xx sidecar responses instead of masking the failure.
</Update>

<Update label="2026-06-01">
  ## v0.10.0rc1

  ### General Notes

  * v0.10.0rc1 includes breaking changes for security and correctness. Refer to the [Security section](#security) for more details.
  * Includes dependency and security maintenance updates.

  ### New Features

  * Added cron retrieval by ID endpoint (`GET /runs/crons/{cron_id}`).

  ### Fixes

  * Fixed Event Streaming v2 run start handling so checkpoint replay targets supplied via `config.configurable.checkpoint_id` are honored.
  * Fixed Event Streaming v2 `input.respond` returning `no_such_interrupt` for legitimate interrupts on the postgres backend over HTTP `POST /commands`.
  * Fixed a bug where a thread's `checkpoint_map` from a prior time-travel run would persist and contaminate a subsequent `Command(resume=...)`, causing nested subgraphs to incorrectly replay from the start.

  ### Security

  * **Potentially breaking** Loopback webhook targets are now denied by default to fix an authentication-bypass primitive ([GHSA-2c9q-c2q9-qgqv](https://github.com/langchain-ai/helm/security/advisories/GHSA-2c9q-c2q9-qgqv)). The `webhooks.url.disable_loopback` policy now defaults to `true`, blocking relative-URL webhooks (which dispatch through the in-process ASGI transport and bypass auth), as well as localhost / 127.x / ::1 / host.docker.internal absolute URLs and any hostname that DNS-resolves into the loopback range (mitigating DNS rebinding). Deployments that legitimately need loopback webhooks (e.g. `langgraph dev` with a localhost webhook receiver, or production setups that dispatch to a custom FastAPI route mounted on the same server) can opt back in by setting `webhooks.url.disable_loopback: false` in `langgraph.json` (or the equivalent `LANGGRAPH_WEBHOOKS` JSON env var). Only do this when you control the routes that loopback webhooks reach, as those routes are dispatched without authentication.
  * **Potentially breaking** `POST /runs` and `POST /threads/{thread_id}/runs` now authorize the attached assistant via the`assistants.read` auth event (matching cron creation and direct GET) instead of the previously-used `assistants.search` event with an incomplete payload ([GHSA-jfj5-wrj9-63x4](https://github.com/langchain-ai/helm/security/advisories/GHSA-jfj5-wrj9-63x4)). Deployments that registered only `@auth.on.assistants.read` (and no `.search` handler) were vulnerable to a cross-user authorization bypass; their existing read handler will now be invoked on the run-creation path. As a defense-in-depth follow-up, client-supplied run/cron metadata is no longer forwarded into the `assistants.read` auth event payload from `Runs.put` or `Crons.put`, and inmem/postgres runtimes now agree on the value shape. Breaking change for deployments with custom auth handlers: (1) any `@auth.on.assistants.search` handler that was previously invoked during run creation is no longer called there — ensure you have an equivalent`@auth.on.assistants.read` handler returning the same owner-style filter; (2) `value["metadata"]` on the `assistants.read` event invoked from run/cron creation is no longer populated, so handlers that inspected or mutated it must move that logic into `@auth.on.runs.create_run` / `@auth.on.crons.create` and rely on returning a filter for ownership enforcement.
  * Deployments now see a structured warning at server start listing every uncovered dispatch path along with a default-deny snippet to copy. The warning is silent for deployments that register a global `@auth.on` handler or that only use `@auth.authenticate` without any resource-level handlers.
</Update>

<Update label="2026-05-27">
  ## v0.9.0

  ### General Notes

  * v0.9.0 is the stable promotion of the v0.9.0rc line.
  * Includes dependency and security maintenance updates.
</Update>

<Update label="2026-05-11">
  ## v0.9.0rc1

  ### General Notes

  * Added cron metadata filtering in /runs/crons/search and /runs/crons/count, matching metadata filter behavior already available for assistants/threads.
  * Added Postgres checkpointer pool tuning knobs for cases when loading lots of large checkpoints at once. LANGGRAPH\_CHECKPOINTER\_POSTGRES\_POOL\_MIN\_SIZE and LANGGRAPH\_CHECKPOINTER\_POSTGRES\_POOL\_TIMEOUT\_SECONDS can now be set.
  * Fixed a crash in update\_state in the mongo checkpointer when a thread has no prior checkpoint.
  * Includes dependency updates for security vulnerabilities.

  ### New Features

  #### Delta channel support

  Delta channels are now supported so checkpoints can store incremental state updates instead of repeatedly storing full channel payloads, which helps with large, append-heavy state like message histories.

  To use, define state channels with LangGraph's DeltaChannel reducer pattern in your graph state.
  This behavior is enabled when the installed langgraph is >= 1.2.
  Docs: [DeltaChannel reference](/oss/python/langgraph/pregel#deltachannel)

  #### Event streaming APIs

  Event streaming APIs are being introduced, with a unified event-streaming surface intended for richer real-time run events and command/event workflows.

  The feature flag `FF_V2_EVENT_STREAMING` can be set to true to enable the new event streaming APIs.

  The new endpoints include:

  * `POST /threads/{thread_id}/stream/events`
  * `POST /threads/{thread_id}/commands`
  * `WS /threads/{thread_id}/stream/events`

  Docs:

  * [Agent Server API reference](/langsmith/server-api-ref)
  * [LangGraph event streaming reference](/oss/python/langgraph/event-streaming)
</Update>

<Update label="2026-05-05">
  ## v0.8.7

  * Reverted changes from #3296 temporarily to address issues with the upcoming 0.8.6 release.
</Update>

<Update label="2026-05-04">
  ## v0.8.6

  * Integrated DeltaChannel into the Postgres checkpointer for efficient snapshot and delta processing.
  * Introduced new v2 streaming primitives to the API for enhanced data handling.
  * Enabled dynamic port discovery for in-memory operations.
  * Linked A2A tool result messages with `toolCallId` correlation metadata to maintain alignment with initiating tool calls.
  * Fixed an issue where JS studio experiments didn't update the experiment screen, ensuring correct run routing to the experiment's tracing project with `reference_example_id` set.
</Update>

<Update label="2026-04-30">
  ## v0.8.5

  * Addressed security vulnerabilities in langgraph JavaScript dependencies reported by Datadog and npm.
</Update>

<Update label="2026-04-29">
  ## v0.8.4

  * Included trace/span IDs in access logs to improve trace correlation in Datadog and OTel.
</Update>

<Update label="2026-04-28">
  ## v0.8.3

  * Added support for IAM-based authentication with Google Cloud Memorystore in cluster mode for secure access.
</Update>

<Update label="2026-04-27">
  ## v0.8.2

  * Fixed the `langgraph-api` queue entrypoint to start correctly on IPv6-only clusters by ensuring the health/metrics server appropriately binds with an IPv6 literal.
</Update>

<Update label="2026-04-23">
  ## v0.8.1

  * Improved performance by skipping the large `values` column in thread state and run endpoints when the full thread body isn't required.
  * Capped checkpoint ingestion batch size and delay window to minimize long-running transactions and row lock contention, with new configuration flags for batch size and delay control.
</Update>

<Update label="2026-04-16">
  ## v0.8.0

  This minor version moves run queue polling from Postgres to Redis, saving database load and improving performance.

  Under the hood, Agent Server uses a durable run queue to manage run execution. Workers poll the queue for new runs and execute them. Previously, the queue polling logic went through Postgres. This could result in long running queries especially under high load. With this update, the queue polling logic now goes through Redis and then fetches run details from Postgres. This makes the hot path for queue polling substantially faster and reduces the load on the database.

  This is not a breaking change and does not require code changes to upgrade, but there are a couple of things to be aware of:

  * In the deployment immediately after upgrading, the queue will shift over. There may be a brief window where threads are scheduled non-chronologically. Run execution order is still guaranteed within each thread.
  * **Self-hosted only:** Redis traffic may increase slightly. In internal testing, the increase was modest.
</Update>

<Update label="2026-04-15">
  ## v0.7.103

  * Resolved migration version conflict for checkpoint\_delete\_queue, ensuring proper execution and added duplicate version detection for future migrations.
</Update>

<Update label="2026-04-14">
  ## v0.7.102

  * Improved handling of parallel interrupts by merging multiple interrupt chunks and ensuring consistent interrupt return behavior.
  * Updated Vite dependency to patch security vulnerabilities CVE-2026-39363 and CVE-2026-39364.
  * Pinned the Datadog image version to `1.9.9` due to missing `arm64` support in `1.9.10` manifest.
</Update>

<Update label="2026-04-14">
  ## v0.7.101

  * Bumped Go stdlib to 1.25.9 to address high severity vulnerabilities CVE-2026-32280 and CVE-2026-32282.
  * Improved error propagation in DD and OTEL tracers to handle UserInterrupt exceptions without causing generator errors.
</Update>

<Update label="2026-04-10">
  ## v0.7.100

  * Implemented background deletion of checkpoints to improve thread deletion and pruning performance, reducing I/O pressure and enhancing efficiency.
  * Bumped `@hono/node-server` from 1.19.12 to 1.19.13 to fix a security issue with the Serve Static Middleware.
  * Updated hono from version 4.12.9 to 4.12.12, including critical security patches for middleware and utilities.
  * Upgraded the hono library to version 4.12.12, addressing several security vulnerabilities.
  * Implemented strict version locking for build dependencies to ensure consistency across builds.
</Update>

<Update label="2026-04-09">
  ## v0.7.99

  * Updated OpenAPI configuration to prevent 405 errors in `/docs` "try it" requests when using Istio with a path prefix.
  * Replaced `signal.raise_signal(SIGINT)` with `sys.exit` in `queue_with_signal` to improve shutdown reliability and handle stuck threads.
  * Added opt-in TLS configuration for executor clients, preserving backward-compatible cleartext behavior for existing non-loopback deployments.
  * Adjusted the precedence order for Datadog API key configuration to ensure proper key usage.
</Update>

<Update label="2026-04-06">
  ## v0.7.98

  * Fixed an import issue in `langgraph dev` to ensure the dev server works without environment variables and added a regression test.
</Update>

<Update label="2026-04-06">
  ## v0.7.97

  * Improved error propagation for JS graphs, ensuring clearer error messages from the `/assistants/<ID>/schemas` endpoint.
  * Ensured stable startup when environment variables like `LANGGRAPH_SERVER_HOST` are set to an IPv6 address.
  * Enhanced query performance by using `->>` for string value filters in `EqAuthFilter`, enabling the use of B-tree indexes.
</Update>

<Update label="2026-04-03">
  ## v0.7.96

  * Enhanced database performance by disabling nested loops and respecting lower `statement_timeout` settings when specified.
</Update>

<Update label="2026-04-03">
  ## v0.7.95

  * Resolved a `BlockingError` by ensuring `ddtrace` is imported at module load time, preventing async context conflicts during initialization.
  * Propagated `ddtrace` context to worker ensuring `langgraph.graph_load` has a parent span instead of emitting as a root.
  * Added support for `Prefer: return=minimal` on `PATCH /threads/{id}` to improve efficiency by returning a 204 status with no body.
  * Enhanced `run_server` with dynamic port discovery to automatically select an available port when the default port (`2024`) is in use.
</Update>

<Update label="2026-03-31">
  ## v0.7.94

  * Resolved an issue where JavaScript installs would incorrectly succeed after retry timeouts, ensuring proper failure handling.
  * Added a `langgraph.graph_load` ddtrace span around the graph factory load to improve APM visibility.
</Update>

<Update label="2026-03-31">
  ## v0.7.93

  * Enabled `FF_OPTIMIZED_STREAMING` flag support from environment variables in `core-api` mode.
</Update>

<Update label="2026-03-31">
  ## v0.7.92

  * Fixed an issue where `keep_latest` threads could accumulate checkpoints indefinitely by recreating the `thread_ttl` entry upon run completion.
  * Improved import performance by caching `importlib.metadata.packages_distributions()`, significantly reducing startup time when using `ddtrace` with Google API packages.
</Update>

<Update label="2026-03-29">
  ## v0.7.91

  * Upgraded cryptography dependency from 46.0.5 to 46.0.6 to address a security issue related to name constraints in peer name verification.
  * Introduced an optimized streaming implementation using Redis Streams with a new protocol version (v2) for better performance and resumability, featuring payload compression and support for Redis Cluster read replicas.
</Update>

<Update label="2026-03-27">
  ## v0.7.90

  * Improved error handling in the DR flow and set a 30-second default timeout for tests to ensure timely CI failure tracking.
  * Upgraded picomatch from 4.0.3 to 4.0.4 to address critical security vulnerabilities.
</Update>

<Update label="2026-03-25">
  ## v0.7.89

  * Enhanced queue server metrics and established a requirement for the OpenTelemetry SDK.
  * Added a missing tag for the `COUNTER_RUN_FAILED_AFTER_RETRY` metric to improve monitoring accuracy.
</Update>

<Update label="2026-03-24">
  ## v0.7.87

  * Implemented retries for run failures due to Redis-related streaming errors, with warning logs for visibility.
</Update>

<Update label="2026-03-23">
  ## v0.7.86

  * Set default `DD_TRACE_ENABLED=false` in all images to reduce Orchestrion log noise for non-Datadog deployments.
</Update>

<Update label="2026-03-23">
  ## v0.7.84

  * Downgraded noisy warning-level logs to info level to reduce log clutter, focusing on informational status messages like license lite mode and tracing disabled.
  * Enhanced Go `core-api-grpc` with Orchestrion DD APM tracing for automatic instrumentation and improved trace context propagation.
</Update>

<Update label="2026-03-19">
  ## v0.7.82

  * Ensured A2A protocol compliance by preserving `kind` discriminators and using lowercase states/roles in responses for all client method name formats.
</Update>

<Update label="2026-03-18">
  ## v0.7.79

  * Introduced beta release of the `swr` function for improved data fetching capabilities.
  * Upgraded the Go runtime to version 1.25.8 across all Dockerfiles and `go.mod` to address multiple CVEs.
</Update>

<Update label="2026-03-17">
  ## v0.7.77

  * Introduced `HTTP_MAX_REQUEST_BODY_BYTES` config to limit HTTP request body size to 300MB, returning a 413 error for oversized requests to prevent memory exhaustion.
  * Added support for accessing store and checkpointer via config in JS graph factories to facilitate deep agent initialization.
  * Updated `pyasn1` dependency from version 0.6.2 to 0.6.3 to enhance security and fix parsing issues.
  * Added instrumentation to log time to first byte (TTFB) and response size for streaming endpoints, improving access log details.
</Update>

<Update label="2026-03-17">
  ## v0.7.76

  * Relaxed `starlette-sse` version bounds to improve dependency compatibility.
</Update>

<Update label="2026-03-17">
  ## v0.7.75

  * Correctly closed streams in `Runs.Enter` to prevent buffer issues and added a configurable environment variable for window size.
</Update>

<Update label="2026-03-16">
  ## v0.7.74

  * Cleaned up some false error logs during queue shutdown operations.
</Update>

<Update label="2026-03-16">
  ## v0.7.73

  * Improved thread search performance with `extract` by avoiding unnecessary detoasting of large JSONB values.
</Update>

<Update label="2026-03-13">
  ## v0.7.72

  * Updated undici package from version 7.22.0 to 7.24.0 to address multiple security vulnerabilities.
</Update>

<Update label="2026-03-13">
  ## v0.7.71

  * Cleaned up the API by removing unused parameters from Threads State Checkpoint and Runs create methods.
  * Fixed the `POST /threads/prune` with `strategy=delete` to ensure thread records are fully removed, not just checkpoint data.
  * Added A2A 1.0 `kind` discriminators to response objects, removed `{"task": ...}` wrapper, and fixed Anthropic streaming metadata issues.
  * Added support for custom encryption in the Redis queue to enhance data security.
</Update>

<Update label="2026-03-11">
  ## v0.7.69

  * Added optional `timezone` field to crons, allowing `next_run_date` computation in user's specified timezone, defaulting to UTC.
  * Corrected the handling of 401 status codes in authentication exceptions to prevent incorrect defaulting to 403.
</Update>

<Update label="2026-03-10">
  ## v0.7.68

  * Fixed issues with non-DR checkpoint AES JSON to improve functionality and extend test coverage.
  * Fixed A2A streaming to correctly emit interrupt artifacts as separate `artifact-update` events according to the specification.
  * Ensured secure tarfile extraction by only extracting validated and safe members to prevent arbitrary file write vulnerabilities.
  * Enhanced security by requiring an exact match for the `noauth` path in authentication middleware.
  * Fixed stale checkpoint values being written to thread state during rollback in multitasking strategy.
</Update>

<Update label="2026-03-06">
  ## v0.7.66

  * Added a fallback to `LS_CHECKPOINTER_BACKEND` for default checkpointer configuration when `LANGGRAPH_CHECKPOINTER` is unset.
</Update>

<Update label="2026-03-05">
  ## v0.7.65

  * Fixed a bug in `messages-tuple` streaming mode where `tool_call_chunks` contained `args_json` instead of `args`, preventing message reconstruction and causing errors.
</Update>

<Update label="2026-03-05">
  ## v0.7.64

  * Enabled the MongoDB checkpointer URI to be set via `LS_MONGODB_URI` or `MONGODB_URI` environment variables, with precedence rules.
</Update>

<Update label="2026-03-04">
  ## v0.7.63

  * Fixed a bug that could potentially deadlock queue instances by exhausting workers with invalid runs.
</Update>

<Update label="2026-03-02">
  ## v0.7.61

  * Fixed a race condition to ensure graceful shutdown of the health and metric server.
</Update>

<Update label="2026-02-27">
  ## v0.7.59

  * Updated the Redis queue to use zset with threads, reducing CPU usage by 25% and improving performance by eliminating unnecessary locking and optimizing indexes.
</Update>

<Update label="2026-02-26">
  ## v0.7.58

  * Upgraded `langgraph-checkpoint` to 4.0.0 in `storage_postgres/uv.lock` to address CVE-2026-27794, with adjustments for dependency pinning issues.
</Update>

<Update label="2026-02-26">
  ## v0.7.57

  * Fixed a regression preventing all users from creating crons associated with system graphs.
</Update>

<Update label="2026-02-25">
  ## v0.7.56

  * Added support for `ttl`, `index`, and `refresh_ttl` parameters in store HTTP API endpoints to align with the SDK and in-process store interface.
  * Added support for the `?include=ttl` query parameter in the `GET /threads/{thread_id}` endpoint to return TTL information.
  * Updated metrics reporting to accurately account for PostgreSQL and Redis connections, ensuring consistent statistics between GRPC and Python metrics.
</Update>

<Update label="2026-02-25">
  ## v0.7.55

  * Fixed a bug that caused duplicate run scheduling in the new cron scheduler backend.
  * Refactored the `GET /docs` endpoint to read from a static OpenAPI spec for improved compatibility with custom ingress configurations.
</Update>

<Update label="2026-02-24">
  ## v0.7.54

  * Resolved an issue where the custom encryption context for gRPC services was not loading correctly due to hardcoded values.
</Update>

<Update label="2026-02-24">
  ## v0.7.52

  * Added feedback URLs to the `/wait` and `/join` endpoint responses under a `__feedback__` key when `feedback_keys` are supplied.
  * Added feedback\_keys support to the distributed runtime, including presigned feedback token generation using langsmith-go SDK.
  * Upgraded Werkzeug from version 3.1.5 to 3.1.6 to address a Windows security issue with special device names in multi-segment paths.
  * Upgraded Go runtime to 1.25.7 to address critical and high severity CVEs identified in vulnerability scans.
</Update>

<Update label="2026-02-22">
  ## v0.7.51

  * Improved license check resilience during upstream outages, including a cached fallback, a 24-hour grace period, and automatic cleanup of Redis entries.
  * Ensured assistant descriptions and names are synced on startup when `LANGSERVE_GRAPHS` config changes.
  * Enhanced the Checkpointer API by introducing a two-level protocol hierarchy and fixing capability detection to support extended methods directly.
</Update>

<Update label="2026-02-20">
  ## v0.7.49

  * Reserved metadata keys in request payloads are now silently stripped rather than causing a 422 error, enhancing user experience.
  * Fixed an issue where store default TTL was not applied to items written without an explicit TTL parameter.
</Update>

<Update label="2026-02-19">
  ## v0.7.46

  * Structured error payloads in webhooks now include `error` and `message` fields, replacing the previous flat string format, which may affect systems parsing the `error` field.
  * Expanded store auth tests with namespace-rewriting to enhance namespace handling and cross-user isolation.
</Update>

<Update label="2026-02-19">
  ## v0.7.45

  * Replaced null bytes with U+FFFD in all handling paths to prevent key collisions.
</Update>

<Update label="2026-02-19">
  ## v0.7.44

  * Increase flexibility of database URI parser
  * Add additional validation on some payloads
</Update>

<Update label="2026-02-18">
  ## v0.7.40

  * Fixed a regression in assistant creation by ensuring `metadata` and `config` are populated as empty objects `{}` instead of `null` when not provided.
</Update>

<Update label="2026-02-17">
  ## v0.7.39

  * Ensured auth configuration is passed correctly in distributed runtime operations to improve executor functionality.
  * Added support for Red Hat UBI-9 based Docker images for enterprise customers using RHEL-based containers.
  * Added graceful shutdown handoff for distributed runtime, allowing in-flight runs to transfer to the next pod without using a retry attempt.
</Update>

<Update label="2026-02-17">
  ## v0.7.38

  * Added `state_updated_at` field to threads for tracking meaningful state changes, allowing filtering and sorting based on these changes.
  * Added support for scheduling crons within the core system.
  * Ensured accurate display of the `https` protocol in agent cards using the x-forwarded-proto header for proper A2A client functionality.
</Update>

<Update label="2026-02-15">
  ## v0.7.37

  * Added generic fallbacks for `acopy_thread`, `aprune`, and `adelete_for_runs` in the BYOC checkpointer adapter, simplifying implementation for custom checkpointers.
</Update>

<Update label="2026-02-13">
