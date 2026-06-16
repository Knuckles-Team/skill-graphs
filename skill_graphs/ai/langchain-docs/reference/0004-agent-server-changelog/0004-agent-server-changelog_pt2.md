  ## v0.7.36

  * Updated A2A protocol support to v1.0 RC, renamed JSON-RPC methods, added a ListTasks handler, and enhanced role, state, and part formats for improved integration and compliance.
  * Improved authentication filtering for `Crons.search()` and `Crons.count()` to prevent unauthorized thread information access.
  * Fixed gaps in BYOC checkpointer for copy, rollback, and namespace filtering operations, ensuring proper handling across different storage backends.
</Update>

<Update label="2026-02-13">
  ## v0.7.35

  * Added an optional `context` parameter to MCP `tools/call` and A2A `message/send` and `message/stream` endpoints, enabling middleware to inject runtime context from headers.
</Update>

<Update label="2026-02-13">
  ## v0.7.33

  * Enhanced the Redis fixture by removing custom checkpointer test skips, improving typed serialization, and adding missing Redis methods.
  * Resolved a stored XSS vulnerability in the handle\_ui endpoint by sanitizing message names in single-quoted HTML onload attributes.
  * Fixed an authorization bypass issue in `put_item` to ensure correct namespace rewrite by the auth handler.
  * Enforced assistant ownership checks during run creation, preventing execution on unowned assistants while ensuring system assistants remain accessible to all authenticated users.
  * Implemented AES encryption for checkpoint blobs and writes in the Go checkpointer when using LANGGRAPH\_AES\_KEY.
  * Implemented initial checkpointer gRPC servicer with all necessary methods and conversion helpers.
</Update>

<Update label="2026-02-11">
  ## v0.7.32

  * Sanitized error messages in streams and A2A responses to protect sensitive information like database connection strings and internal hostnames.
  * Fixed a bug in `join_run_stream` to correctly handle multiple `stream_mode` parameters, ensuring proper parsing of stringified JSON lists.
  * Added build, test, and publish processes for Node.js 24 images, supporting the latest LTS version.
  * Enhanced custom checkpointer adapter with new capabilities and improved metadata enrichment for consistent API responses.
  * Added stricter version constraints for langgraph libraries in executor Docker images to prevent unintended upgrades.
  * Enhanced security by sanitizing SSE event and id fields to prevent CR/LF injection.
  * Fixed an issue causing cron-created runs to use default encryption contexts instead of properly propagating the specified ones.
</Update>

<Update label="2026-02-11">
  ## v0.7.31

  * Corrected metadata reading functionality to ensure accurate data processing.
</Update>

<Update label="2026-02-10">
  ## v0.7.30

  * Propagated cron metadata for more comprehensive scheduling information.
  * Merges cron metadata on `PATCH` requests to align with other endpoints by preserving existing data.
</Update>

<Update label="2026-02-10">
  ## v0.7.29

  * Refined authentication semantics for cron creation to prevent privilege escalation and ensure independent filtering for crons, threads, and assistants.
  * Validated tar file entries to prevent directory traversal vulnerabilities in the cloudflared download process.
  * Added an IDs filter to the `SearchThreadsRequest` to streamline thread endpoint operations.
  * Updated the fallback mechanism to use a Python Postgres connection for thread state, fixing issues with worker completion checkpoints.
  * Introduced a feature-flagged initial version of the Redis queue implementation with ongoing updates.
</Update>

<Update label="2026-02-07">
  ## v0.7.28

  * Internal maintenance and stability improvements for MCP and gRPC.
</Update>

<Update label="2026-02-07">
  ## v0.7.27

  * Improved MCP tool input schemas by removing common message types for cleaner tool definitions.
  * Added name sanitization for MCP tools to ensure valid tool names.
</Update>

<Update label="2026-02-07">
  ## v0.7.26

  * Added validation for system keys on ingress.
</Update>

<Update label="2026-02-06">
  ## v0.7.25

  * Switched the Python queue worker to use core go `Runs.next()`.
  * Fixed a monitoring issue in the long query monitor
</Update>

<Update label="2026-02-06">
  ## v0.7.24

  * Optimized Postgres connection handling to prevent hitting connection limits under high load and removed unnecessary error logs.
  * Switched to a new backend for runs management and streaming using gRPC.
</Update>

<Update label="2026-02-05">
  ## v0.7.23

  * Corrected the unmarshaling process for the `input` field in `RunCommand` to ensure accurate data mapping and enable a previously gated JS test.
  * Ensured race condition handling for run streaming by fully subscribing before execution starts, with added support for the `FF_LOG_DROPPED_EVENTS` environment variable.
</Update>

<Update label="2026-02-04">
  ## v0.7.22

  * Ensured `get_store()` works in custom routes, enabling Store access from user-defined Starlette endpoints.
</Update>

<Update label="2026-02-05">
  ## v0.7.21

  * Support for PATCH /crons/
</Update>

<Update label="2026-02-04">
  ## v0.7.19

  * Custom encryption improvements for core API.
</Update>

<Update label="2026-02-04">
  ## v0.7.18

  * Update thread streaming for core API usage.
</Update>

<Update label="2026-02-03">
  ## v0.7.17

  * Instrumentation for OTEL now requires explicit opt-in with `LS_APM_OTEL_ENABLED=true` for improved control.
</Update>

<Update label="2026-02-03">
  ## v0.7.16

  * Switched threads streaming to the new gRPC backend for improved performance.
  * Introduced replica tracing in DR for enhanced evaluation capabilities in Studio.
</Update>

<Update label="2026-02-03">
  ## v0.7.15

  * Added support for pausing crons with a new `is_enabled` field, allowing only enabled crons to be executed.
  * Introduced gRPC server support for JSON encryption and decryption operations.
</Update>

<Update label="2026-02-02">
  ## v0.7.14

  * Ensured selected system fields are excluded from custom encryption to prevent unnecessary encryption of non-sensitive data.
  * Introduced a custom checkpointer adapter with unit tests to validate implementation checks.
</Update>

<Update label="2026-01-29">
  ## v0.7.13

  * Fixed a bug where the app state was not properly preserved through requests when a mount prefix was set.
</Update>

<Update label="2026-01-28">
  ## v0.7.11

  * Added configuration to control which payload fields can be exposed to webhooks.
  * Updated all dependencies in the `/api/langgraph_api/js` group, including `@langchain/core`, `hono`, `@types/react`, and `prettier`, to the latest versions for improved performance and security.
  * Upgraded `hono` from version 4.11.4 to 4.11.7 to address multiple security vulnerabilities in the middleware.
</Update>

<Update label="2026-01-27">
  ## v0.7.10

  * Increased the gRPC server startup timeout to 1 minute to prevent occasional connection timeouts with the core server.
  * Updated @langchain/langgraph from version 1.1.0 to 1.1.2, introducing mixed schema support for StateGraph and type bag patterns for GraphNode and ConditionalEdgeRouter utilities.
</Update>

<Update label="2026-01-23">
  ## v0.7.9

  * A2A `messageId` is now mapped to LangChain message IDs for proper message tracking across protocols.
</Update>

<Update label="2026-01-22">
  ## v0.7.7

  * Ensured preservation of custom configurable fields in checkpoint metadata during gRPC serialization.
</Update>

<Update label="2026-01-21">
  ## v0.7.5

  * Enforced custom encryption for values, interrupts, and errors when setting a thread's status, resolving previous inconsistencies.
  * Added A2A validation checks in `message/stream` and `message/send` routes for `parts`, `role`, and `messageId` fields.
  * Added native A2A interrupt support: `input-required` state is now returned when graphs are interrupted. Use the new `command` parameter in `message/stream` and `message/send` requests to resume with a `Command` payload.
  * Mounted `.well-known/agent-card.json` under `/a2a/{assistant_id}/` for A2A agent discovery.
  * Added proper A2A error codes for task existence checks in `tasks/cancel`.
</Update>

<Update label="2026-01-21">
  ## v0.7.4

  * Fixed a bug with Redis URL parsing for `ssl_cert_reqs` field, ensuring compatibility with redis-go.
  * Added a gRPC client for streaming runs, controlled by the `FF_USE_CORE_API` feature flag.
</Update>

<Update label="2026-01-20">
  ## v0.7.2

  * Updated `@langchain/langgraph` to version 1.1.0, introducing type utilities for graph nodes and conditional edges for enhanced TypeScript ergonomics.
</Update>

<Update label="2026-01-17">
  ## v0.7.0

  * Switched to using the Go assistants implementation by default for improved performance.
  * Added `LANGGRAPH_AES_JSON_KEYS` configuration to enable AES encryption for specified JSON fields using a key name allowlist.
</Update>

<Update label="2026-01-16">
  ## v0.6.39

  * Added gRPC client support for `Threads.State()` to the Python `core-api`, improving thread ID and run counting operations.
</Update>

<Update label="2026-01-15">
  ## v0.6.36

  * Validated the length of `$and` and `$or` in auth filters and optimized unnecessary root-level filters.
</Update>

<Update label="2026-01-12">
  ## v0.6.35

  * Unified the error format by removing the `code` field and standardizing all errors to return JSON with a `detail` field.
</Update>

<Update label="2026-01-12">
  ## v0.6.34

  * Small fixes for feature-flagged internal environments (unreleased).
</Update>

<Update label="2026-01-12">
  ## v0.6.33

  * Small fixes for feature-flagged internal environments (unreleased).
</Update>

<Update label="2026-01-11">
  ## v0.6.32

  * Small fixes for feature-flagged internal environments (unreleased).
</Update>

<Update label="2026-01-11">
  ## v0.6.31

  * Properly respected the disable\_a2a setting to ensure accurate configuration handling.
</Update>

<Update label="2026-01-09">
  ## v0.6.29

  * Fix minor bugs.
</Update>

<Update label="2026-01-09">
  ## v0.6.28

  * Added support for `ParentCommand` to correctly propagate control to parent graphs, enhancing command handling and navigation.
  * Added a Python gRPC client for managing run operations, enhancing consistency between Go and Python implementations.
</Update>

<Update label="2026-01-08">
  ## v0.6.27

  * Fixed a regression issue in handling empty thread metadata.
</Update>

<Update label="2026-01-08">
  ## v0.6.26

  * Fixed the port configuration issue for the persistence gRPC server.
</Update>

<Update label="2026-01-08">
  ## v0.6.25

  * Ran the core-api gRPC server in the executor tier to support loopback API calls in graphs and removed unnecessary configuration for disabling the server.
</Update>

<Update label="2026-01-07">
  ## v0.6.24

  * Fixed the behavior of the liveness probe in the executor tier, addressing issues from version 0.6.23.
</Update>

<Update label="2026-01-07">
  ## v0.6.23

  * Integrated gRPC server health check with `/ok` endpoint in liveness probe to ensure proper startup coordination.
  * Reverted the previous change to disable the checkpointer and added a condition to enable RemoteCheckpointer only during testing.
  * Suppressed `langgraph_auth_*` and `langgraph_request_id` fields in checkpoint metadata to prevent inclusion of transient user data.
</Update>

<Update label="2026-01-06">
  ## v0.6.22

  * Resolved an error caused by missing encryption contexts when using blob-only custom encryption, ensuring proper function without errors.
</Update>

<Update label="2026-01-06">
  ## v0.6.21

  * Introduced a Python gRPC client for run operations, including `Search`, `Get`, `Delete`, `Cancel`, `Stats`, and `Sweep`, with updated API implementation and a new unit test suite for enum mappings.
</Update>

<Update label="2026-01-06">
  ## v0.6.19

  * Reproduced OSS implementations of `get_state` and `update_state` in the engine server and re-enabled `test_weather_subgraph`.
</Update>

<Update label="2026-01-05">
  ## v0.6.18

  * Added functionality to enforce specific license claims for self-hosted Enterprise users, enabling remote disabling of the Agent Builder product.
  * Added a new Prune endpoint for better resource management.
  * Merged graph configuration with invoke configuration in Pregel, giving precedence to invoke settings.
  * Introduced the `include=ttl` query parameter to the GET /threads/ endpoint for optional TTL information retrieval without affecting standard read performance.
  * Introduced a `keep_latest` TTL strategy to preserve the latest state while pruning older checkpoints via the core API.
</Update>

<Update label="2025-12-31">
  ## v0.6.17

  * Ensured ongoing runs are stopped when an agent is deleted to prevent lingering processes.
</Update>

<Update label="2025-12-30">
  ## v0.6.16

  * Streamlined and consolidated run operations in the Go persistence layer, improving efficiency and consistency across packages.
</Update>

<Update label="2025-12-26">
  ## v0.6.15

  * Improved the utility converting custom route docstrings to OpenAPI schema content by adding error handling when parsing docstrings, applicable for users with custom Starlette apps.
</Update>

<Update label="2025-12-23">
  ## v0.6.12

  * Improved resolve\_embeddings to be more robust, enabling multiple calls without errors.
  * Updated `@langchain/langgraph` from version 1.0.4 to 1.0.7, adding support for resumableStreams on remote graphs and undeprecating toolsCondition.
  * Implemented `RemoteCheckpointer` to enable subgraph checkpointing, enhancing task execution reliability.
</Update>

<Update label="2025-12-20">
  ## v0.6.11

  * Made the maximum number of retries configurable for enhanced customization.
</Update>

<Update label="2025-12-20">
  ## v0.6.10

  * Ensured run cancellation only processes 'message' type Redis events, improving pubsub client reliability.
  * Added custom encryption for the Store API `value` field, allowing users to choose which keys to encrypt for enhanced security.
  * Enabled streaming for subgraph custom events by updating TeeStream to handle event types separately.
</Update>

<Update label="2025-12-18">
  ## v0.6.9

  * Enforced stable JSON keys for custom encryption, removed model-type-specific custom JSON functions, and improved error handling for double-encryption scenarios.
</Update>

<Update label="2025-12-18">
  ## v0.6.8

  * Added profiling feature to enhance performance analysis and monitoring.
</Update>

<Update label="2025-12-18">
  ## v0.6.7

  * Logged server startup time for improved monitoring and diagnostics.
</Update>

<Update label="2025-12-17">
  ## v0.6.5

  * Added a warning log that triggers during import time for improved visibility.
</Update>

<Update label="2025-12-16">
  ## v0.6.4

  * Enhanced custom encryption by parallelizing metadata and config processes, added encryption for thread.config and some checkpoints, improved tests and schema consistency.
  * Ensured the Go server starts as `core-api` in the queue entrypoint for consistent runtime behavior.
</Update>

<Update label="2025-12-15">
  ## v0.6.2

  * Resolved an issue that caused duplicate calls to middleware when `mount_prefix` was specified.
</Update>

<Update label="2025-12-15">
  ## v0.6.0

  This minor version updates the streaming APIs `/join-stream` and `/stream` behavior with respect to the `last-event-id` parameter to align with the SSE spec. Previously, passing a last-event-id would return that message in addition to any following messages. Going forward, these APIs will only return new messages following the provided last-event-id. For example, with the following stream, previously passing a last-event-id of `2` would return the messages with ids `2` and `3`, but will now only return the message with id `3`:

  ```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  {
      "id": 1,
      "event": "message",
      "data": {
          "content": "Excluded"
      }
  },
  {
      "id": 2,
      "event": "message",
      "data": {
          "content": "Passed last-event-id"
      }
  },
  {
      "id": 3,
      "event": "message",
      "data": {
          "content": "Included"
      }
  }
  ```

  This bump also includes some fixes, including a bug exposing unintended internal events in run streams.
</Update>

<Update label="2025-12-12">
  ## v0.5.42

  * Modified the Go server to rely solely on the CLI `-service` flag for determining service mode, ignoring the globally set `FF_USE_CORE_API` for better deployment specificity.
</Update>

<Update label="2025-12-11">
  ## v0.5.41

  Fixed an issue with cron jobs in hybrid mode by ensuring proper initialization of the ENTERPRISE\_SAAS global flag.
</Update>

<Update label="2025-12-10">
  ## v0.5.39

  * Completed the implementation of custom encryptions for runs and crons, along with simplifying encryption processes.
  * Introduced support for streaming subgraph events in both `values` and `updates` stream modes.
</Update>

<Update label="2025-12-10">
  ## v0.5.38

  * Implemented complete custom encryption for threads, ensuring all thread data is properly secured and encrypted.
  * Ensured Redis attempt flags are consistently expired to prevent stale data.
  * Added core authentication and support for OR/AND filters, enhancing security and flexibility.
</Update>

<Update label="2025-12-09">
  ## v0.5.37

  Added a `name` parameter to the assistants count API for improved search flexibility.
</Update>

<Update label="2025-12-09">
  ## v0.5.36

  * Introduced configurable webhook support, allowing users to customize submitted webhooks and headers.
  * Added an `/ok` endpoint at the root for easier health checks and simplified configuration.
</Update>

<Update label="2025-12-08">
  ## v0.5.34

  Introduced custom encryption middleware, allowing users to define their own encryption methods for enhanced data protection.
</Update>

<Update label="2025-12-08">
  ## v0.5.33

  Set Uvicorn's keep-alive timeout to 75 seconds to prevent occasional 502 errors and improve connection handling.
</Update>

<Update label="2025-12-06">
  ## v0.5.32

  Introduced OpenTelemetry telemetry agent with support for New Relic integration.
</Update>

<Update label="2025-12-05">
  ## v0.5.31

  Added Py-Spy profiling for improved analysis of deployment performance, with some limitations on coverage.
</Update>

<Update label="2025-12-05">
  ## v0.5.30

  * Always configure loopback transport clients to enhance reliability.
  * Ensured authentication headers are passed for remote non-stream methods in JS.
</Update>

<Update label="2025-12-04">
  ## v0.5.28

  * Introduced a faster, Rust-based implementation of uuid7 to improve performance, now used in langsmith and langchain-core.
  * Added support for `$or` and `$and` in PostgreSQL auth filters to enable complex logic in authentication checks.
  * Capped psycopg and psycopg-pool versions to prevent infinite waiting on startup.
</Update>

<Update label="2025-11-26">
  ## v0.5.27

  * Ensured `runs.list` with filters returns only run fields, preventing incorrect status data from being included.
  * (JS) Updated `uuid` from version 10.0.0 to 13.0.0. and `exit-hook` from version 4.0.0 to 5.0.1.
</Update>

<Update label="2025-11-24">
  ## v0.5.26

  Resolved issues with `store.put` when used without AsyncBatchedStore in the JavaScript environment.
</Update>

<Update label="2025-11-22">
  ## v0.5.25

  * Introduced the ability to search assistants by their `name` using a new endpoint.
  * Casted store\_get return types to tuple in JavaScript to ensure type consistency.
</Update>

<Update label="2025-11-21">
  ## v0.5.24

  * Added executor metrics for Datadog and enhanced core stream API metrics for better performance tracking.
  * Disabled Redis Go maintenance notifications to prevent startup errors with unsupported commands in Redis versions below 8.
</Update>

<Update label="2025-11-20">
  ## v0.5.20

  Resolved an error in the executor service that occurred when handling large messages.
</Update>

<Update label="2025-11-19">
  ## v0.5.19

  Upgraded built-in langchain-core to version 1.0.7 to address a prompt formatting vulnerability.
</Update>

<Update label="2025-11-19">
  ## v0.5.18

  Introduced persistent cron threads with `on_run_completed: {keep,delete}` for enhanced cron management and retrieval options.
</Update>

<Update label="2025-11-19">
  ## v0.5.17

  Enhanced task handling to support multiple interrupts, aligning with open-source functionality.
</Update>

<Update label="2025-11-18">
  ## v0.5.15

  Added custom JSON unmarshalling for `Resume` and `Goto` commands to fix map-style null resume interpretation issues.
</Update>

<Update label="2025-11-14">
  ## v0.5.14

  Ensured `pg make start` command functions correctly with core-api enabled.
</Update>

<Update label="2025-11-13">
  ## v0.5.13

  Support `include` and `exclude` (plural form key for `includes` and `excludes`) since a doc incorrectly claimed support for that. Now the server accepts either.
</Update>

<Update label="2025-11-10">
  ## v0.5.11

  * Ensured auth handlers are applied consistently when streaming threads, aligning with recent security practices.
  * Bumped `undici` dependency from version 6.21.3 to 7.16.0, introducing various performance improvements and bug fixes.
  * Updated `p-queue` from version 8.0.1 to 9.0.0, introducing new features and breaking changes, including the removal of the `throwOnTimeout` option.
</Update>

<Update label="2025-11-10">
  ## v0.5.10

  Implemented healthcheck calls in the queue /ok handler to improve Kubernetes liveness and readiness probe compatibility.
</Update>

<Update label="2025-11-09">
  ## v0.5.9

  * Resolved an issue causing an "unbound local error" for the `elapsed` variable during a SIGINT interruption.
  * Mapped the "interrupted" status to A2A's "input-required" status for better task status alignment.
</Update>

<Update label="2025-11-07">
  ## v0.5.8

  * Ensured environment variables are passed as a dictionary when starting langgraph-ui for compatibility with `uvloop`.
  * Implemented CRUD operations for runs in Go, simplifying JSON merges and improving transaction readability, with PostgreSQL as a reference.
</Update>

<Update label="2025-11-07">
  ## v0.5.7

  Replaced no-retry Redis client with a retry client to handle connection errors more effectively and reduced corresponding logging severity.
</Update>

<Update label="2025-11-06">
  ## v0.5.6

  * Added pending time metrics to provide better insights into task waiting times.
  * Replaced `pb.Value` with `ChannelValue` to streamline code structure.
</Update>

<Update label="2025-11-05">
  ## v0.5.5

  Made the Redis `health_check_interval` more frequent and configurable for better handling of idle connections.
</Update>

<Update label="2025-11-05">
  ## v0.5.4

  Implemented `ormsgpack` with `OPT_REPLACE_SURROGATES` and updated for compatibility with the latest FastAPI release affecting custom authentication dependencies.
</Update>

<Update label="2025-11-03">
  ## v0.5.2

  Added retry logic for PostgreSQL connections during startup to enhance deployment reliability and improved error logging for easier debugging.
</Update>

<Update label="2025-11-03">
  ## v0.5.1

  * Resolved an issue where persistence was not functioning correctly with LangChain.js's createAgent feature.
  * Optimized assistants CRUD performance by improving database connection pooling and gRPC client reuse, reducing latency for large payloads.
</Update>

<Update label="2025-10-31">
  ## v0.5.0

  This minor version now requires langgraph-checkpoint versions later than 3.0 to prevent a deserialization vulnerability in earlier versions of the langgraph-checkpoint library.
  The `langgraph-checkpoint` library is compatible with `langgraph` minor versions 0.4, 0.5, 0.6, and 1.0.

  This version removes default support for deserialization of payloads saved using the "json" type, which has never been the default.
  By default, objects are serialized using msgpack. Under certain uncommon situations, payloads were serialized using an older "json" mode. If those payloads contained custom python objects, those will no longer be deserializable unless you provide a `serde` config:

  ```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  {
      "checkpointer": {
          "serde": {
              "allowed_json_modules": [
                  ["my_agent", "my_file", "SomeType"],
              ]
          }
      }
  }
  ```
</Update>

<Update label="2025-10-29">
  ## v0.4.47

  * Validated and auto-corrected environment configuration types using TypeAdapter.
  * Added support for LangChain.js and LangGraph.js version 1.x, ensuring compatibility.
  * Updated hono library from version 4.9.7 to 4.10.3, addressing a CORS middleware security issue and enhancing JWT audience validation.
  * Introduced a modular benchmark framework, adding support for assistants and streams, with improvements to the existing ramp benchmark methodology.
  * Introduced a gRPC API for core threads CRUD operations, with updated Python and TypeScript clients.
  * Updated `hono` package from version 4.9.7 to 4.10.2, including security improvements for JWT audience validation.
  * Updated `hono` dependency from version 4.9.7 to 4.10.3 to fix a security issue and improve CORS middleware handling.
  * Introduced basic CRUD operations for threads, including create, get, patch, delete, search, count, and copy, with support for Go, gRPC server, and Python and TypeScript clients.
</Update>

<Update label="2025-10-21">
  ## v0.4.46
