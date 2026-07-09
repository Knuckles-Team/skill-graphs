# Self-hosted LangSmith changelog
Source: https://docs.langchain.com/langsmith/self-hosted-changelog

<Callout icon="rss">
  **Subscribe**: Our changelog includes an [RSS feed](https://docs.langchain.com/langsmith/self-hosted-changelog/rss.xml) that can integrate with [Slack](https://slack.com/help/articles/218688467-Add-RSS-feeds-to-Slack), [email](https://zapier.com/apps/email/integrations/rss/1441/send-new-rss-feed-entries-via-email), Discord bots like [Readybot](https://readybot.io/) or [RSS Feeds to Discord Bot](https://rss.app/en/bots/rssfeeds-discord-bot), and other subscription tools.
</Callout>

[Self-hosted LangSmith](/langsmith/self-hosted) is an add-on to the Enterprise plan designed for our largest, most security-conscious customers. For more details, refer to [Pricing](https://www.langchain.com/pricing). [Contact our sales team](https://www.langchain.com/contact-sales) if you want to get a license key to trial LangSmith in your environment.

<Update label="2026-06-11">
  ## langsmith-0.16.0-rc.2

  * For the full list of changes in the 0.16.0 release candidate, refer to the [langsmith-0.16.0-rc.1](#langsmith-0-16-0-rc-1) release notes below.

  **Download the Helm chart:** [`langsmith-0.16.0-rc.2.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.16.0-rc.2/langsmith-0.16.0-rc.2.tgz)
</Update>

<Update label="2026-06-11">
  ## langsmith-0.15.10

  * Patched dependencies.

  * Fixed security vulnerabilities. See CVE-2026-25087, CVE-2026-45134, CVE-2026-9256 for details.

  **Download the Helm chart:** [`langsmith-0.15.10.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.15.10/langsmith-0.15.10.tgz)
</Update>

<Update label="2026-06-09">
  ## langsmith-0.16.0-rc.1

  * Evaluator detach confirmation dialog showed a "Detach" button instead of "Delete."

  * Included extended stats became available to all organizations for code evaluators.

  * Added two dedicated permissions `bulk-exports:read` and `bulk-exports:manage` for fetching and creating/updating bulk exports.

  * Fixed the Engine "Connect GitHub" flow when the GitHub app was already installed via another workspace in the same organization.

  * Bumped `@langchain/langgraph-sdk` to 1.9.4 in `smith-frontend`.

  * Added an opt-in Smith-ACE v2 sandbox implementation behind `SMITH_ACE_SANDBOX_IMPLEMENTATION=v2`.

  * Threads table now showed the actual last output in the *Last Output* column and surfaced thread-level errors in a new *Last Error* column.

  * Hid the \$0.00 cost badge for tool calls in the trace tree view.

  * Similar cron schedules on the same agent could now be created multiple times with the same expression.

  * Agent Builder "View agent traces" and "View trace" links always opened in the fleet tracing project.

  * Added LangSmith model pricing entry for `gemini-3.1-flash-lite`.

  * LLM-as-judge evaluators could now opt into include extended stats and map prompt variables from `run.*` fields.

  * Default sandbox rootfs images now included Docker Compose and started the Docker daemon automatically.

  * Added cost tracking for `gemini-3.5-flash`.

  * Gateway spend cap policies could now be configured with a weekly period.

  * Added Centralize as an MCP marketplace integration.

  * Sandbox-enabled agents now saw configured proxy profiles (hosts, injected header keys, network rule, OAuth providers) in their system prompt, replacing the older hosts-only auth-proxy section.

  * Hid the Sandboxes nav entry and `/sandboxes` page in regions where `SANDBOX_FEATURE_ENABLED` was off.

  * Self-hosted DockerHub images now included Cosign signatures and signed SPDX SBOM attestations.

  * Fixed a bug where special characters in thread IDs were not encoded, causing the UI to not be able to query these threads.

  * Fixed "Query timeout exceeded" errors when opening large traces.

  * Self-hosted OIDC: fixed SSO groups sync silently no-op'ing during login.

  * Managed Deep Agents private preview now supported MCP server registration with header-based auth.

  * Emitted Prometheus metrics from `queue` workers.

  * Clarified the "Stats unavailable" message when text filters were applied.

  * Context repos now supported metadata updates and deletion from the Hub overflow menu.

  * Typed responses and standard error envelope for Fleet `/v1/fleet/agents/{agent_id}/connections` (List / Create / Delete).

  * Sandbox snapshots could now export a Docker image built inside a sandbox.

  * Fixed ACE subprocess handling so early child-process exits returned request failures instead of crashing the service.

  * Fixed large integer preservation in native run ingest payloads.

  * Waterfall turn view now took full height if available.

  * Added `is one of` operator for metadata value filters when SmithDB was enabled.

  * Organization admins could now disable Engine even when their plan auto-enabled it; their explicit choice persisted across the UI and the backend gates.

  * Workspace admins could now override the workspace-default weekly spend cap on a per-evaluator-rule basis from the evaluator side panel; non-admins saw the resolved cap as read-only text.

  * Fixed incorrect metadata facet suggestions and improved group stats latency for projects with rich run metadata.

  * SmithDB experiments-endpoint reads (`ExecuteQuery`, `QueryRuns`, `QueryRunStats`) now transparently retried up to 3 times on `UNAVAILABLE` with exponential backoff.

  * Alert rules for Run Count, Errors, Latency, and Cost now supported `<`, `<=`, `>`, and `>=` comparison operators (previously the UI only allowed `>=`).

  * Fleet `/v1/fleet/auth-agents/{agent_id}/connections` endpoints moved to `/v1/fleet/agents/{agent_id}/connections` with typed responses, request validation, and the standard Fleet error envelope. The old URL returned 404.

  * Fixed Fleet redirect after deleting the active agent.

  * Removed the Type column from the LangSmith datasets table.

  * Encrypted/redacted "reasoning" content blocks no longer appeared as empty or garbled cards in the trace messages view. Meaningful extended-thinking content continued to render normally.

  * Fleet agent APIs now required `thread_scoped_sandbox` or `agent_scoped_sandbox` for sandbox-backed agents.

  * Allowed exporting all experiments in a workspace via the new `all_experiments` parameter for bulk exports. Limited to 250 experiments per export, could be increased at request.

  * Fleet uses langchain-fireworks 1.4.2 for Fireworks model calls.

  * This enabled a redesign of the run details panel with improved readability and more robust message parsing.

  * Fleet/Agent Builder now included Gemini 3.5 Flash as a selectable built-in model.

  * Computer use now had an in-chat callout for eligible general chat users.

  * Fixed a bug where the blob storage banner incorrectly flashed on page load.

  * This enabled a new way to leave feedback on a run, directly within the run details panel.

  * Added token pricing support for Claude Opus 4.8.

  * Agent Builder now offered Claude Opus 4.8 as a built-in Anthropic model.

  * Org admins could now update an existing API key's role via the service-keys API without rotating the key.

  * Managed Deep Agents MCP server setup now supported OAuth under the `/v1/deepagents` API namespace.

  * Extra Parameters entered for Bedrock Nova 2 (and any other provider requiring camelCase API fields) now preserved their original key casing when the model configuration was saved and reloaded in the Playground.

  * Self-hosted OIDC users now got a display name resolved from the `name` / `given_name`+`family_name` id\_token claims.

  * Fixed SSRF policy for `playground` service such that it respected `SSRF_ALLOW_K8S_INTERNAL`.

  * Fixed an LLM gateway data-protection bug that could corrupt Anthropic images or documents when PII redaction was enabled.

  * Hid sandbox file explorer controls while allowing explicit sandbox summary downloads.

  * Engine now supported an optional monthly LCU spend limit (set by finance, plan, or org admins) that paused new Engine runs once reached.

  * Chat-input file uploads in agent builder/fleet now reached the sandbox filesystem at `/tmp/uploads/` when sandboxes were enabled.

  * Fleet Default now appeared first in the model picker for eligible plans.

  * Fixes the project stats sidebar trace count label and header layout.

  * Run rules webhook payloads now included a `trace_url` deep link for each run.

  * Experiment loading progress bars displayed the number of runs completed and evaluated within the experiments table.

  * Sandboxes now allowed password-based SSH for non-root users while keeping root SSH login key-only.

  * Workspace switcher on the data-plane no-access screen only listed current organization workspaces.

  * Restored cron execution for enterprise Fleet agents that had been silently failing to fire since early March 2026.

  * Fixed security vulnerabilities. See CVE-2026-45736, CVE-2026-44664, CVE-2025-71176 for details.

  **Download the Helm chart:** [`langsmith-0.16.0-rc.1.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.16.0-rc.1/langsmith-0.16.0-rc.1.tgz)
</Update>

<Update label="2026-06-09">
  ## langsmith-0.15.9

  * This release packages the same LangSmith application version as langsmith-0.15.7. Refer to the [langsmith-0.15.7](#langsmith-0-15-7) release notes below.

  **Download the Helm chart:** [`langsmith-0.15.9.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.15.9/langsmith-0.15.9.tgz)
</Update>

<Update label="2026-06-08">
  ## langsmith-0.15.8

  * This release packages the same LangSmith application version as langsmith-0.15.7. Refer to the [langsmith-0.15.7](#langsmith-0-15-7) release notes below.

  **Download the Helm chart:** [`langsmith-0.15.8.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.15.8/langsmith-0.15.8.tgz)
</Update>

<Update label="2026-06-06">
  ## langsmith-0.15.7

  * Added support for API key authentication with Amazon Bedrock in the Playground. Bedrock API keys let you authenticate requests with a bearer token instead of AWS credentials.
  * Fixed the LLM auth proxy for two cases: evaluator batch requests and Bedrock model configurations.

  **Download the Helm chart:** [`langsmith-0.15.7.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.15.7/langsmith-0.15.7.tgz)
</Update>

<Update label="2026-06-03">
  ## langsmith-0.15.6

  * Fixed a bug in SSO Groups Sync where the group-name separator was ignored and did not behave like SCIM sync.
  * Added structured server logs identifying which workspace group claims resolved and which did not, simplifying SSO Groups Sync diagnosis.
  * Patched dependencies.

  **Download the Helm chart:** [`langsmith-0.15.6.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.15.6/langsmith-0.15.6.tgz)
</Update>

<Update label="2026-06-02">
  ## langsmith-0.15.5

  * Fixed the SSRF policy for the `playground` service so that it respected `SSRF_ALLOW_K8S_INTERNAL`.
  * Patched dependencies.
  * Fixed security vulnerabilities. See CVE-2026-45736, CVE-2026-44664 for details.

  **Download the Helm chart:** [`langsmith-0.15.5.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.15.5/langsmith-0.15.5.tgz)
</Update>

<Update label="2026-06-01">
  ## langsmith-0.15.4

  * This release packages the same LangSmith application version as langsmith-0.15.2. Refer to the [langsmith-0.15.2](#langsmith-0-15-2) release notes below.

  **Download the Helm chart:** [`langsmith-0.15.4.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.15.4/langsmith-0.15.4.tgz)
</Update>

<Update label="2026-05-29">
  ## langsmith-0.15.3

  * This release packages the same LangSmith application version as langsmith-0.15.2. Refer to the [langsmith-0.15.2](#langsmith-0-15-2) release notes below.

  **Download the Helm chart:** [`langsmith-0.15.3.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.15.3/langsmith-0.15.3.tgz)
</Update>

<Update label="2026-05-29">
  ## langsmith-0.15.2

  * Fixed an OIDC login redirect loop (`ERR_TOO_MANY_REDIRECTS`) for identity providers that use the hybrid flow with a `form_post` callback.

  **Download the Helm chart:** [`langsmith-0.15.2.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.15.2/langsmith-0.15.2.tgz)
</Update>

<Update label="2026-05-29">
  ## langsmith-0.15.1

  * Fixed a bug where the blob storage banner incorrectly flashed on page load.
  * Fixed an issue in self-hosted OIDC (v15) where the SSO Groups Sync silently no-op'ed during login.

  **Download the Helm chart:** [`langsmith-0.15.1.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.15.1/langsmith-0.15.1.tgz)
</Update>

<Update label="2026-05-26">
  ## langsmith-0.15.0

  LangSmith Self-Hosted v0.15 brings **reusable evaluators and a library of 30+ evaluator templates** that centralize evaluation across your workspace, ships **per-example assertions** alongside reference outputs in annotation queues, lets you download **Insights reports** as PDFs for offline analysis, and introduces the **Context Hub** for version-controlled, environment-aware management of agent instructions and tools. Several breaking changes are worth reviewing before upgrade: the `agent-bootstrap` script is deprecated, the Agent Builder rename to [Fleet](/langsmith/fleet) may require workload-identity service-account updates, and the `projects:update-retention` permission splits into `projects:increase-trace-tier` and `projects:decrease-trace-tier`.

  Follow the [upgrade instructions](/langsmith/self-host-upgrades) to get access to everything. To book time with LangChain support for your upgrade, contact the team via the [Support Portal](https://support.langchain.com).

  ### Breaking changes

  * Deprecated the `agent-bootstrap` script. LangSmith agents are now standalone services that deploy with the Helm chart instead of through the LangSmith Deployment control plane. If you were using [Fleet](/langsmith/fleet) through this script previously, this may require a migration. Contact support to walk through migration.
  * Renamed Agent Builder to [Fleet](/langsmith/fleet). If you use workload identity, you may need to update any service accounts.
  * `POST /workspaces/current/members` now requires `role_id` for [RBAC](/langsmith/rbac)-enabled organizations. Requests without it return `400` instead of defaulting to `WORKSPACE_ADMIN`.
  * Deprecated the `USAGE_EXPORT_ADMIN_EMAILS` environment variable. Use `INSTANCE_ADMIN_EMAILS` instead.
  * Replaced the `projects:update-retention` permission with `projects:increase-trace-tier` and `projects:decrease-trace-tier` for separate control over raising and lowering trace retention. Permissions were backfilled to existing roles, so no changes are needed for existing roles. New roles should use the new permissions. See [RBAC permissions](/langsmith/rbac).
  * Added a `fleet-admin:read` permission that gates the new Fleet Admin section. Admins of existing tenants need to grant it. Permissions were backfilled to existing roles, so no changes are needed for existing roles. New roles should use the new permissions. See [RBAC permissions](/langsmith/rbac).

  ### Infrastructure changes

  * **Section renames from the Fleet rename** — several sections were renamed as part of the Agent Builder to [Fleet](/langsmith/fleet) rename (see [Breaking changes](#breaking-changes)). You may need to update service accounts or shift values in your configuration.

  ### New features

  * **Context Hub** — version-controlled, environment-aware management of agent instructions and tools. Create and manage versioned [skill and agent repos](/langsmith/context-engineering-concepts), promote commits to `staging` or `production` environments, and resolve context by environment tag at runtime. See [Use the Context Hub](/langsmith/use-the-context-hub) and [Manage contexts with the SDK](/langsmith/manage-contexts-sdk) to get started.
  * **Reusable evaluators and evaluator templates** — a new [Evaluators](/langsmith/evaluators) tab centralizes every evaluator in your workspace, with 30+ templates covering safety, response quality, trajectory, user behavior, and multimodal evaluation. Attach an existing evaluator to a new tracing project in seconds without maintaining duplicate copies.
  * **Per-example assertions** — write [assertions](/langsmith/assertions) instead of or alongside reference outputs when editing examples in an [annotation queue](/langsmith/annotation-queues).
  * **Downloadable Insights reports** — download an [Insights](/langsmith/insights) report as a PDF from the report details page for offline analysis.

  ### Admin changes

  * **Expanded ABAC coverage** — [ABAC](/langsmith/abac) now applies to `runs:create` on `POST /runs` and `POST /runs/batch`, plus the remaining `/sessions/{session_id}/` endpoints.
  * **SCIM email-case-mismatch fix** — identity providers that send a different email casing are no longer rejected as email-change attempts.

  **Download the Helm chart:** [`langsmith-0.15.0.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.15.0/langsmith-0.15.0.tgz)
</Update>

<Update label="2026-05-21">
  ## langsmith-0.15.0-rc.16

  * This release packages the same LangSmith application version as langsmith-0.15.0-rc.14. Refer to the [langsmith-0.15.0-rc.14](#langsmith-0-15-0-rc-14) release notes below.

  **Download the Helm chart:** [`langsmith-0.15.0-rc.16.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.15.0-rc.16/langsmith-0.15.0-rc.16.tgz)
</Update>

<Update label="2026-05-20">
  ## langsmith-0.15.0-rc.15

  * This release packages the same LangSmith application version as langsmith-0.15.0-rc.14. Refer to the [langsmith-0.15.0-rc.14](#langsmith-0-15-0-rc-14) release notes below.

  **Download the Helm chart:** [`langsmith-0.15.0-rc.15.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.15.0-rc.15/langsmith-0.15.0-rc.15.tgz)
</Update>

<Update label="2026-05-20">
  ## langsmith-0.8.31

  * This release packages the same LangSmith application version as langsmith-0.8.30. Refer to the [langsmith-0.8.30](#langsmith-0-8-30) release notes below.

  **Download the Helm chart:** [`langsmith-0.8.31.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.8.31/langsmith-0.8.31.tgz)
</Update>

<Update label="2026-05-18">
  ## langsmith-0.15.0-rc.14

  * Fixed the truncation issue of the 'Enabled' column in the automations table.
  * Improved handling of click events in the UI with the polly button icon fix.
  * Implemented multiple UI enhancements such as the addition of solid icons, icon xs variants, and updated details view headers.
  * Improved performance by removing unused join operations from session stats and optimizing query handling.
  * Added new event hooks for model invocation and updated the fleet-admin permissions to include read access.
  * Expanded model support with new tools for GLM5 and Minimax 2.5.
  * Added new features to the evaluator UI, including filters by created\_by, feedback key, and resource.
  * Recognized external type definitions in evaluators, enabling more sophisticated feedback and sorting options.
  * Introduced loading improvements for better data handling in various Fleet UI components.
  * Enhanced fleet management with tool usage breakdowns, spend limit enforcement, and improved usage dashboards.
  * Added support for auditing logs across Go write endpoints and audit logging for sensitive data access.
  * Implemented new security features such as SSRF protection, transparent HTTP/HTTPS proxying, and enhanced authorization for self-hosted environments.
  * Supported service identification with GitHub OAuth installation synchronization and CRUD operations.
  * Introduced mobile-friendly login and a Progressive Web App (PWA) capability.
  * Added the capability to invite users to organizations via a new endpoint.
  * Enhanced message processing with SubAgentDetails, facilitating better context capture and management.

  **Download the Helm chart:** [`langsmith-0.15.0-rc.14.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.15.0-rc.14/langsmith-0.15.0-rc.14.tgz)
</Update>

<Update label="2026-05-14">
  ## langsmith-0.15.0-rc.13

  * This release packages the same LangSmith application version as langsmith-0.15.0-rc.12. Refer to the [langsmith-0.15.0-rc.12](#langsmith-0-15-0-rc-12) release notes below.

  **Download the Helm chart:** [`langsmith-0.15.0-rc.13.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.15.0-rc.13/langsmith-0.15.0-rc.13.tgz)
</Update>

<Update label="2026-05-14">
  ## langsmith-0.14.6

  * Fixed storage issue by backporting S3 CopyObject KMS headers to v14, improving data transfer security for S3 integrations.
  * Fixed security vulnerabilities: CVE-2026-40192, CVE-2026-40347, CVE-2026-41205, CVE-2026-42561

  **Download the Helm chart:** [`langsmith-0.14.6.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.14.6/langsmith-0.14.6.tgz)
</Update>

<Update label="2026-05-13">
  ## langsmith-0.15.0-rc.12

  * Fixed the truncation issue in the 'Enabled' column of the automations table to improve UI usability.
  * Improved the evaluator details page and added sorting capabilities for created and updated timestamps.
  * Enhanced evaluator tables by adding a type filter and click-to-filter functionality for type, feedback key, and resource cells.
  * Added a new evaluator reuse feature to streamline the use of existing evaluators.
  * Improved frontend evaluators to include feedback key and resource filters, enhancing usability.
  * Added support for tracing tool usage and displaying agent names in the usage dashboard, enhancing performance insights.
  * Expanded session management features with Redis tracking for SmithDB run rules.
  * Enhanced mobile friendliness and PWA support for login interfaces.
  * Improved performance by optimizing session synchronization and indexing strategies.
  * Added mTLS support for ClickHouse migrations.
  * Added parallel tool calls rendering in the messages view for better visual representation of concurrent processes.
  * Introduced a new endpoint to update licenses for self-hosted instances via JWT.
  * Added a new UI section for displaying evaluator actions required when creating an issue board.
  * Implemented mobile-friendly login and an installable PWA to enhance accessibility for mobile users.
  * Streamlined session and dataset tracking by integrating Redis for run rules in SmithDB.
  * Enhanced DataGrid components for better UI performance in tracing views.

  These updates focus on improving user experience, performance, security, and feature set for self-hosted deployments.

  **Download the Helm chart:** [`langsmith-0.15.0-rc.12.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.15.0-rc.12/langsmith-0.15.0-rc.12.tgz)
</Update>

<Update label="2026-05-11">
  ## langsmith-0.15.0-rc.10

  * This release packages the same LangSmith application version as langsmith-0.15.0-rc.4. Refer to the [langsmith-0.15.0-rc.4](#langsmith-0-15-0-rc-4) release notes below.

  **Download the Helm chart:** [`langsmith-0.15.0-rc.10.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.15.0-rc.10/langsmith-0.15.0-rc.10.tgz)
</Update>

<Update label="2026-05-09">
  ## langsmith-0.15.0-rc.9

  * This release packages the same LangSmith application version as langsmith-0.15.0-rc.4. Refer to the [langsmith-0.15.0-rc.4](#langsmith-0-15-0-rc-4) release notes below.

  **Download the Helm chart:** [`langsmith-0.15.0-rc.9.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.15.0-rc.9/langsmith-0.15.0-rc.9.tgz)
</Update>

<Update label="2026-05-08">
  ## langsmith-0.15.0-rc.8

  * This release packages the same LangSmith application version as langsmith-0.15.0-rc.4. Refer to the [langsmith-0.15.0-rc.4](#langsmith-0-15-0-rc-4) release notes below.

  **Download the Helm chart:** [`langsmith-0.15.0-rc.8.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.15.0-rc.8/langsmith-0.15.0-rc.8.tgz)
</Update>

<Update label="2026-05-08">
  ## langsmith-0.15.0-rc.7

  * This release packages the same LangSmith application version as langsmith-0.15.0-rc.4. Refer to the [langsmith-0.15.0-rc.4](#langsmith-0-15-0-rc-4) release notes below.

  **Download the Helm chart:** [`langsmith-0.15.0-rc.7.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.15.0-rc.7/langsmith-0.15.0-rc.7.tgz)
</Update>

<Update label="2026-05-06">
  ## langsmith-0.15.0-rc.6

  * This release packages the same LangSmith application version as langsmith-0.15.0-rc.4. Refer to the [langsmith-0.15.0-rc.4](#langsmith-0-15-0-rc-4) release notes below.

  **Download the Helm chart:** [`langsmith-0.15.0-rc.6.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.15.0-rc.6/langsmith-0.15.0-rc.6.tgz)
</Update>

<Update label="2026-05-05">
  ## langsmith-0.15.0-rc.5

  * This release packages the same LangSmith application version as langsmith-0.15.0-rc.4. Refer to the [langsmith-0.15.0-rc.4](#langsmith-0-15-0-rc-4) release notes below.

  **Download the Helm chart:** [`langsmith-0.15.0-rc.5.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.15.0-rc.5/langsmith-0.15.0-rc.5.tgz)
</Update>

<Update label="2026-05-04">
