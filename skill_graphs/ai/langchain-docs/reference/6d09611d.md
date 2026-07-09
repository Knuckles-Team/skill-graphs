  ## langsmith-0.15.0-rc.4

  * Enhanced the Messages View with auto-scroll navigation, parallel tool calls rendering, and improved styling
  * Improved Messages View performance with better memory utilization and processing times
  * Added thread ID display in run details with copy-to-clipboard functionality
  * Added the ability to open threads in new tabs
  * Fixed dark mode gradient styling
  * Fixed OAuth refresh race condition in Fleet
  * Fixed run rules not marking matched runs as completed in Redis at max attempts
  * Fixed dataset evaluators incorrectly created with group\_by thread\_id
  * Added new run rules logic for workspaces with no existing rules
  * Removed self-hosted gate for Fleet usage page
  * Hidden minimal reasoning effort option for GPT-5.x models in the playground

  **Download the Helm chart:** [`langsmith-0.15.0-rc.4.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.15.0-rc.4/langsmith-0.15.0-rc.4.tgz)
</Update>

<Update label="2026-05-01">
  ## langsmith-0.14.5

  * Fixed the agent-builder failure to start on v14 self-hosted 0.14.6 due to the `langgraph-api 0.8.3` base image bundling `LangSmith 0.7.37`, which removed `SandboxTemplate`, by pinning `LangSmith<0.7.34` to downgrade to a compatible version.

  **Download the Helm chart:** [`langsmith-0.14.5.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.14.5/langsmith-0.14.5.tgz)
</Update>

<Update label="2026-04-30">
  ## langsmith-0.15.0-rc.3

  * This release packages the same LangSmith application version as langsmith-0.15.0-rc.1. Refer to the [langsmith-0.15.0-rc.1](#langsmith-0-15-0-rc-1) release notes below.

  **Download the Helm chart:** [`langsmith-0.15.0-rc.3.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.15.0-rc.3/langsmith-0.15.0-rc.3.tgz)
</Update>

<Update label="2026-04-29">
  ## langsmith-0.14.3

  * Fixed silent corruption of `traceId`, `spanId`, and `parentSpanId` for OTLP/JSON (`Content-Type: application/json`) trace ingestion.
  * Reduced Microsoft Graph permission requirements for Microsoft 365 docs and Teams private-message tools.

  **Download the Helm chart:** [`langsmith-0.14.3.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.14.3/langsmith-0.14.3.tgz)
</Update>

<Update label="2026-04-24">
  ## langsmith-0.15.0-rc.2

  * This release packages the same LangSmith application version as langsmith-0.15.0-rc.1. Refer to the [langsmith-0.15.0-rc.1](#langsmith-0-15-0-rc-1) release notes below.

  **Download the Helm chart:** [`langsmith-0.15.0-rc.2.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.15.0-rc.2/langsmith-0.15.0-rc.2.tgz)
</Update>

<Update label="2026-04-24">
  ## langsmith-0.15.0-rc.1

  * Fixed truncation issue by widening the 'Enabled' column in the automations table for better header visibility.
  * Updated details view header for improved user experience.
  * Improved performance by removing dead run\_stats\_facets join from session stats queries.
  * Fixed MCP server filter dropdown to make it scrollable.
  * Added 'user cost' table and toggle for agent/user view in the fleet.
  * Enhanced security by adding URL allowlist enforcement for JWT injection.
  * Added ability to sort evaluators by creation and update time in the backend.
  * Added 'Feedback Key' filtering in the evaluators table for more precise searches.
  * Showed back button on the full-page trace view to enhance navigation.
  * Fixed audit-logs and various performance improvements for lower latency.
  * Enhanced UI by showing 'Feedback Key' in evaluator column dropdown.
  * Added session insights, views, metadata, and dashboard endpoints to improve data accessibility.
  * Fixed file creation issues to prevent active interrupt state clearance.
  * Provided async support for agents in the fleet to improve reliability.
  * Fixed issues with agent cloning that previously caused flow issues.
  * Added spend limit enforcement and the ability to track usage, enhancing cost management features.
  * Made more efficient use of resources with new skill memory-store mirror updates in fleets.
  * Improved evaluator reuse UX for users with better management of evaluator actions on issue generation.
  * Enhanced security features by preventing sub-agents from triggering unauthorized actions.
  * Optimized memory and resource management in the agent builder chat.
  * Improved evaluator trace detail navigation by preserving search model in URLs.
  * Upgraded per-environment favicon colors for clarity in staging and dev environments.
  * Performance improvements in session sync reducing resource usage.
  * Added default agent name support in usage dashboard for clarity in report generation.
  * Made UI improvements to evaluator details for a smoother experience.
  * Enabled auto-wake and auto-stop for Sandbox environments to save resources.
  * Integrated tracing tool functionality in issue creation for better context and reliability.
  * Added "create agent manually" button to navigation for easier agent management.
  * Enhanced memory management tools UI for better approval process visualization.
  * Fixed tool usage table and improved its performance for a better UX.
  * Enabled auditing for sensitive data access endpoints for enhanced security compliance.
  * Improved tracing project name display in usage dashboard for better project clarity.
  * Introduced keyboard shortcuts in the editor page for rapid interaction.
  * Set default MSP cron schedule as standard to reduce manual setup effort.
  * Added integration user flow with prompt messages for smooth operation and understanding.
  * Fixed default tracing project selection to Fleet to prevent inconsistencies.

  **Download the Helm chart:** [`langsmith-0.15.0-rc.1.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.15.0-rc.1/langsmith-0.15.0-rc.1.tgz)
</Update>

<Update label="2026-04-20">
  ## langsmith-0.14.2

  * This release packages the same LangSmith application version as langsmith-0.14.0. Refer to the [langsmith-0.14.0](#langsmith-0-14-0) release notes below.

  **Download the Helm chart:** [`langsmith-0.14.2.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.14.2/langsmith-0.14.2.tgz)
</Update>

<Update label="2026-04-20">
  ## langsmith-0.14.1

  * This release packages the same LangSmith application version as langsmith-0.14.0. Refer to the [langsmith-0.14.0](#langsmith-0-14-0) release notes below.

  **Download the Helm chart:** [`langsmith-0.14.1.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.14.1/langsmith-0.14.1.tgz)
</Update>

<Update label="2026-04-20">
  ## langsmith-0.14.0

  LangSmith Self-Hosted v0.14 brings **Chat** (our in-product chat for traces and runs) to self-hosted, takes **ABAC and audit logs** GA (on by default), and enables the **LLM Auth Proxy** by default with URL allowlisting and richer JWT claims. Admins get **unified model configurations** shared across Agent Builder, Chat, Insights, Playground, and Evaluators, and fine-grained **Prompt Owners** for locking down who can promote or delete individual prompts. Evaluators gain **multi-modal support** and workspaces can now set **cost alerts** on tracing projects. Playground model support expands (Anthropic via Vertex AI, custom Azure models, Bedrock inference profiles, Gemini 3.1 Pro, GPT-5.3 / 5.4, Baseten + GLM-5), and new agent tools and triggers land for Google Sheets & Docs, Outlook, Teams, and Salesforce SOQL. On the infrastructure side, v0.14 adds **GCS Workload Identity** support for blob storage, **Valkey** as a drop-in Redis replacement, and a pre-upgrade migration hook for safer rollouts.

  Follow the [upgrade instructions](/langsmith/self-host-upgrades) to get access to everything. To book time with LangChain support for your upgrade, contact the team via the [Support Portal](https://support.langchain.com).

  ### Breaking changes

  * Fixed an issue where `host-backend` wasn't picking up `commonEnv`. This may result in duplicate environment variables that need to be removed.

  ### Infrastructure changes

  * Migrations now run as a `Pre-upgrade` hook prior to image versions rolling out. This will prevent issues when migrations fail.
  * **GCS Workload Identity support** — authenticate to GCS blob storage using cloud-native workload identity instead of long-lived credentials.
  * **Valkey support** — Valkey can now be used as a drop-in replacement for Redis.

  ### New features

  * **Chat on self-hosted** — in-product Chat for understanding traces, runs, and evaluator feedback is now available in self-hosted.
  * **ABAC and audit logs GA** — Attribute-Based Access Control and audit logs are enabled by default for self-hosted deployments.
  * **LLM Auth Proxy on by default** — URL allowlist prevents credential forwarding to unintended hosts, and JWTs now carry `organization_name` and `workspace_name` claims.
  * **Unified model configurations** — Agent Builder, Chat, Insights, Playground, and Evaluators now share a single set of model configs, with workspace-admin controls over model access across all AI features.
  * **Prompt Owners** — designate a specific group of users with fine-grained permission to promote or delete individual prompts, without granting broader org access.
  * **Multi-modal evaluators** — pass attachments and base64 content (images, audio, PDFs) directly into evaluators.
  * **Cost alerts on tracing projects** — set alerts on tracing project-level costs alongside existing LangSmith alerts.
  * **Expanded playground model support** — Anthropic via Vertex AI, custom Azure models, Bedrock inference profiles and configurable base URLs, Gemini 3.1 Pro, GPT-5.3 / 5.4 (now default), and Baseten + GLM-5.
  * **New agent tools and triggers** — Google Sheets and Docs, Outlook mail and calendar, Microsoft Teams, Salesforce SOQL, Gmail OAuth v2 with refresh tokens, and an Outlook Trigger.
  * **Insights enhancements** — scheduled Insights reports, categories trending over time, full feedback comments in analysis, and a lower minimum job interval (6h → 1h).
  * **Annotation and review upgrades** — required reviewers per queue, pairwise queues that honor `reviewer_access_mode`, an "Assigned to me" filter, per-annotator CSV export, and bulk table actions.
  * **Prompt Hub and tool registry** — commit tag search, model select in template creation, a workspace-scoped tool registry API, and a private registry UI.
  * **Evaluator workflow improvements** — prebuilt LLM evaluators use strict structured outputs by default, evaluators support tagging and reuse, retries no longer lose scores, and a new API runs playground experiments programmatically.
  * **Custom iframe output renderer** — drag-to-resize HTML chart outputs in experiments and trace views.
  * **Thread and inbox UX** — auto-generated thread titles, redesigned run details in threads, session-level feedback stats, keyboard shortcuts, and filtering out internal helper threads.

  ### Admin changes

  * **Granular usage reporting** — granular billable usage APIs that allow you to retrieve detailed trace usage data broken down by workspace, project, user, or API key.

  **Download the Helm chart:** [`langsmith-0.14.0.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.14.0/langsmith-0.14.0.tgz)
</Update>

<Update label="2026-04-17">
  ## langsmith-0.13.43

  * This release packages the same LangSmith application version as langsmith-0.13.42. Refer to the [langsmith-0.13.42](#langsmith-0-13-42) release notes below.

  **Download the Helm chart:** [`langsmith-0.13.43.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.13.43/langsmith-0.13.43.tgz)
</Update>

<Update label="2026-04-14">
  ## langsmith-0.13.42

  * Fixed issue in metadata filtering to recognize json.Number as a primitive type, improving data ingestion accuracy.

  **Download the Helm chart:** [`langsmith-0.13.42.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.13.42/langsmith-0.13.42.tgz)
</Update>

<Update label="2026-04-14">
  ## langsmith-0.13.41

  * Internal improvements and maintenance updates

  **Download the Helm chart:** [`langsmith-0.13.41.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.13.41/langsmith-0.13.41.tgz)
</Update>

<Update label="2026-04-09">
  ## langsmith-0.13.40

  * Added support for mTLS configuration to enhance self-hosted security.
  * Improved the loading speed of the Fleet interface.
  * Fixed a bug in the tracing UI that caused intermittent display issues.
  * Added support for Redis Cluster, improving scalability for self-hosted deployments.
  * Improved PostgreSQL IAM integration for better database management in self-hosted instances.

  **Download the Helm chart:** [`langsmith-0.13.40.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.13.40/langsmith-0.13.40.tgz)
</Update>

<Update label="2026-04-07">
  ## langsmith-0.13.39

  * Users can now run experiments without `projects:create`, decoupling experiment execution from project governance controls.
  * Added skeleton loading state when switching between agent chat threads instead of a blank chat input.
  * Improved the Fleet Arcade integrations page to display correct actions and clearer backend states.
  * Arcade gateway installs now automatically sanitize invalid MCP server names before adding them to a workspace.
  * Users can now see assigned reviewers as name chips in the annotation queue list and filter to queues they are assigned to via an "Assigned to me" button.
  * Improved run details hover on the trace tree for less flicker when clicking or moving quickly between rows.
  * Fixed a timeout when generating Insights reports with feedback enabled on high-volume workspaces.
  * Arcade integrations now show a permission error instead of a generic upstream failure when a connected user lacks access to the configured Arcade project.
  * Added a clickable ID badge to the experiment detail page header for easy copying of the experiment ID.
  * LLM auth proxy JWTs now include `organization_name` and `workspace_name` claims.
  * Added dataset split selection to the evaluator playground, allowing users to run evaluator experiments on specific dataset splits.
  * Fixed experiment comparison view showing contradictory improvement arrows and regression cell colors for composite scores.
  * Fixed a bug where deleting traces from pre-compression multipart blob storage objects could corrupt byte ranges for other traces in the same object, causing 416 errors when reading their payloads.
  * Fixed crash when viewing a tool run in an in-progress trace.
  * Lowered Insights job schedule minimum interval from 6 hours to 1 hour, configurable via `CLIO_SCHEDULE_MIN_INTERVAL_SECONDS` environment variable.
  * LLM auth proxy now supports Insights (CLIO) service identity for JWT-based LLM authentication.
  * Fixed subagent files not being deleted from hub repo memory when subagents are removed in the agent editor.
  * Simplified Arcade workspace connection status to show "Workspace configured" instead of the confusing "Connected account" label with a redundant badge.
  * Fixed a bug where expanding a tool call in the run detail view and scrolling away caused it to collapse back when scrolled into view again.
  * Agent file reads (clone, inspect, startup) now correctly use the hub as the source of truth when hub memory is enabled.
  * Fixed custom output rendering (HTML charts via iframe) not working in the redesigned experiment detail panes.
  * Allowed usage of LLM Auth Proxy in self-hosted by default.
  * Sessions facets raw path now returns input/output KV facets when `RUNS_LITE_STATS_TENANTS` is enabled, matching the Python backend behavior.
  * Click-to-copy tooltips (e.g. project ID) now respond to clicks on the tooltip content itself, not just the trigger badge.
  * Improved MCP server authorization enforcement in the platform backend.
  * Added Baseten as a model provider with GLM-5 support.
  * Improved LLM inference efficiency by reducing date precision in system prompts from minute-level to date-only.
  * Fixed Polly losing trace context when a trace page is expanded to full page view.
  * Added a unified files sidebar to Fleet chat, accessible via a "Files" button in the header, to browse, search, create, rename, move, and preview all agent-generated files in one panel.
  * Added `SSRF_ALLOW_PRIVATE_IPS_WEBHOOKS`, `SSRF_ALLOW_PRIVATE_IPS_MCP_SERVERS`, and `SSRF_ALLOW_PRIVATE_IPS_TOOLS` environment variables to allow self-hosted deployments to connect to services on private IP ranges.
  * Added `get_current_time` tool to Polly so relative time expressions in filter queries resolve correctly.
  * Reference outputs are now always visible in the experiment trace detail view, fixing an issue where they were hidden for some organizations.
  * Fixed agent OAuth connections failing with "Unknown provider" errors for non-personal agents.
  * Added Base URL configuration support for Bedrock models in the playground and model configurations, enabling custom endpoint URLs for proxy or gateway deployments.
  * Added sign out button back to the settings page sidebar.
  * The run rules list endpoint now returns `backfill_id` when backfill progress is requested.
  * SSO users can no longer see or accept pending invites to organizations other than their own SSO organization.
  * Fleet webhook execution now uses a dedicated endpoint instead of the MCP proxy.
  * Added session-level feedback stats to the sessions API for parity with the Python backend.
  * Improved MCP proxy authorization and URL safety checks for agent runtime requests.

  **Download the Helm chart:** [`langsmith-0.13.39.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.13.39/langsmith-0.13.39.tgz)
</Update>

<Update label="2026-04-03">
  ## langsmith-0.13.38

  * Fixed MCP OAuth tools (e.g., Hex, Notion) failing on self-hosted deployments when `HOST_BACKEND_ENDPOINT_PUBLIC` lacked an `https://` scheme.
  * Insights agent now includes full feedback comments when analyzing traces.
  * Removed the legacy Feed page in Fleet; Inbox is now the default thread view for all tenants.
  * Fixed a permission error that blocked users from creating evaluators when using the evaluator reuse feature.
  * Org admins can now grant Model Configuration management to workspace editors and custom roles via Settings > Roles.
  * Pairwise annotation queues now respect `reviewer_access_mode`: completion/archive logic gates on assigned reviewers only, and GET responses include `assigned_reviewers`.
  * Agent chat messages are no longer grouped into a collapsible "Completed N steps" container. A single copy dropdown on the last AI message of each turn lets you copy just the response or all steps including tool outputs.
  * Fixed pagination in the waterfall view for thread traces, where threads with more than 20 turns now load additional traces when scrolling.
  * Fixed "Empty Message" text appearing in the agent editor chat when AI invokes tools without accompanying text.
  * Added Salesforce SOQL query tool to Fleet, enabling agents to query Salesforce data via OAuth.
  * Annotation queue run list items now show reviewer names and avatars when hovering over the review stats badge.
  * Go session stats now return `feedback_key`, `feedback_key_score`, `feedback_value`, and `feedback_source` facets in `run_facets`, matching the Python backend.
  * Fixed `/info` endpoint returning 401 when `infoEndpointAuthRequired` is enabled with SSO authentication.
  * Added a documentation link button to the "Trigger Webhook" section in the Save prompt dialog for easier access to webhook docs.
  * Fixed layout shift in agent chat caused by the copy button unmounting during streaming.

  **Download the Helm chart:** [`langsmith-0.13.38.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.13.38/langsmith-0.13.38.tgz)
</Update>

<Update label="2026-04-01">
  ## langsmith-0.13.37

  * Added URL allowlist for the LLM Auth Proxy to prevent credential forwarding to unintended hosts.
  * Enabled audit logs by default for self-hosted deployments.
  * MCP servers now respect granular RBAC permissions in the UI; users only see actions their role allows.
  * Enabled ABAC by default for self-hosted deployments.
  * Fixed low-frequency SmithDB ingestion errors ("incomplete chunked payload") during multipart uploads when the HTTP body is truncated.
  * Fixed a bug with OpenAI tools rendering.

  **Download the Helm chart:** [`langsmith-0.13.37.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.13.37/langsmith-0.13.37.tgz)
</Update>

<Update label="2026-03-30">
  ## langsmith-0.13.36

  * This release packages the same LangSmith application version as langsmith-0.13.32. Refer to the [langsmith-0.13.32](#langsmith-0-13-32) release notes below.

  **Download the Helm chart:** [`langsmith-0.13.36.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.13.36/langsmith-0.13.36.tgz)
</Update>

<Update label="2026-03-27">
  ## langsmith-0.13.35

  * This release packages the same LangSmith application version as langsmith-0.13.32. Refer to the [langsmith-0.13.32](#langsmith-0-13-32) release notes below.

  **Download the Helm chart:** [`langsmith-0.13.35.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.13.35/langsmith-0.13.35.tgz)
</Update>

<Update label="2026-03-27">
  ## langsmith-0.13.34

  * This release packages the same LangSmith application version as langsmith-0.13.32. Refer to the [langsmith-0.13.32](#langsmith-0-13-32) release notes below.

  **Download the Helm chart:** [`langsmith-0.13.34.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.13.34/langsmith-0.13.34.tgz)
</Update>

<Update label="2026-03-27">
  ## langsmith-0.13.33

  * This release packages the same LangSmith application version as langsmith-0.13.32. Refer to the [langsmith-0.13.32](#langsmith-0-13-32) release notes below.

  **Download the Helm chart:** [`langsmith-0.13.33.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.13.33/langsmith-0.13.33.tgz)
</Update>

<Update label="2026-03-27">
  ## langsmith-0.13.32

  * Added ability for users to find account labels for first-class providers.
  * Fixed issue where switching alerts did not switch charts accordingly.
  * Fixed key error for experiments with attachments.
  * Added dismiss button functionality to the agentify banner.
  * Improved responsiveness in run details header and compare traces.
  * Added truncate property to feedback chips list to respond to container width.
  * Fixed subpixel bleed on body rows in the repetition summary table.
  * Fixed race condition in AQ run archive check.
  * Patched 9 medium security alerts and 4 high security alerts.
  * Renamed Metadata to Attributes in the comparison detail pane.
  * Enabled toggle panel size button in RepetitionDetailPane.
  * Updated model cards in the frontend.
  * Fixed issue to load prompt picker when opening playground from experiments table.
  * Properly disabled environment promotion buttons for users without tag permissions.
  * Enabled granular usage rollup cron for self-hosted instances.
  * Onboarded more CUD operations for audit logs.
  * Added Ashby integration migration to Agent Builder.
  * Improved performance by parallelizing graph loading and eliminating redundant MCP fetches in Agent Builder.
  * Automatically expanded/collapsed keys for improved UI.
  * Fixed blue hover state for trace comparison divider.
  * Avoided MITM races during sandbox startup with Smithbox proxy.
  * Fixed bar height calculation in the granular usage chart.
  * Added Dynatrace webhook integration for alerts.
  * Displayed toast notification on "run now" button click in Forge.
  * Handled non-string resource fields in MCP OAuth discovery.
  * Added feedback banner for experiment sidebar redesign.
  * Added example attachments to experiment detail panes.
  * Wired Arcade integration to real OAuth flow in Agent Builder.
  * Fixed loading flash in host revisions table during revalidation.
  * Fixed imports in host backend for truststore.
  * Added request context to authentication middleware error log in Agent Builder.
  * Fixed editing prompt feature in evaluator.
  * Fetched full run data in new experiment detail pane.

  **Download the Helm chart:** [`langsmith-0.13.32.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.13.32/langsmith-0.13.32.tgz)
</Update>

<Update label="2026-03-23">
  ## langsmith-0.13.31

  * This release packages the same LangSmith application version as langsmith-0.13.28. Refer to the [langsmith-0.13.28](#langsmith-0-13-28) release notes below.

  **Download the Helm chart:** [`langsmith-0.13.31.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.13.31/langsmith-0.13.31.tgz)
</Update>

<Update label="2026-03-23">
  ## langsmith-0.13.30

  * This release packages the same LangSmith application version as langsmith-0.13.28. Refer to the [langsmith-0.13.28](#langsmith-0-13-28) release notes below.

  **Download the Helm chart:** [`langsmith-0.13.30.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.13.30/langsmith-0.13.30.tgz)
</Update>

<Update label="2026-03-21">
  ## langsmith-0.13.29

  * This release packages the same LangSmith application version as langsmith-0.13.28. Refer to the [langsmith-0.13.28](#langsmith-0-13-28) release notes below.
