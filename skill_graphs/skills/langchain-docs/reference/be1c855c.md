
  **Download the Helm chart:** [`langsmith-0.13.29.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.13.29/langsmith-0.13.29.tgz)
</Update>

<Update label="2026-03-21">
  ## langsmith-0.13.28

  * Fixed ABAC permission checks to improve self-hosted instance functionality.
  * Enhanced agent builder by handling DotDict in decrypting passthrough headers.
  * Improved fleet logo for better dark mode support.
  * Updated Slack reauthorization required message with link to integrations page in Agent Builder.
  * Added network allow-deny list feature.
  * Introduced new access control UI for the sandbox proxy.
  * Fixed GCS workload identity in storage and added copy health check.
  * Reduced concurrency and added timeout for scheduled insights jobs.
  * Enhanced frontend performance by reducing the number of preload chunks during initial load.
  * Added caching for `/info` and `/auth/v1/user` responses in localStorage to improve frontend performance.
  * Enabled JWT generation for auth-proxy in playground service for enhanced security.
  * Recreated feedbacks index in the backend for storage optimization.
  * Implemented gating for workspace skill editing by repo ownership in the Agent Builder.
  * Added static TTL expiry for sandbox claims for improved management.
  * Enabled Slack channels for personal agents in Agent Builder.
  * Adjusted frontend contrast for run status icons in light mode for better visibility.
  * Implemented JWT generation for LLM-as-judge evals to enhance evaluation security.
  * Always display creator name on agent workspace cards for better transparency.
  * Reordered inbox tabs to improve navigation.
  * Supported Google IAP session refresh in self-hosted environments.
  * Replaced MUI checkboxes in various sections to improve UI consistency.
  * Improved experimental evaluator SAQ timeouts matching online eval paths for better performance.
  * Supported RDS DB instance on k8s platform for enhanced infrastructure flexibility.
  * Loaded LLM auth proxy JWT signing key from `LANGSMITH_SIGNING_JWKS` to align with security standards.
  * Improved run detail dropdown design for a better user experience.
  * Added service key authentication to runs, sessions, and sandbox endpoints for enhanced security.
  * Added LangChain vendor extractor to enhance message processing capabilities.
  * Fixed parsing errors related to cache reads impacting costs for better performance metrics.
  * Introduced support for specifying environment variables from secret references for improved configuration management.

  **Download the Helm chart:** [`langsmith-0.13.28.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.13.28/langsmith-0.13.28.tgz)
</Update>

<Update label="2026-03-18">
  ## langsmith-0.13.27

  * Organization admins can now edit member display names inline from the members table in Settings.
  * Multipart ingestion requests no longer accept Inputs, Outputs, or Events as inline fields. These must be sent as dedicated out-of-band parts.
  * Tracing support email on the Home page error banner is now a clickable mailto link.
  * Improved run details tab highlighting so selected sections stay correctly highlighted near scroll boundaries.
  * Improved keyboard shortcut rendering in the chat assistant tooltip.
  * Fixed connect/disconnect button on Slack integrations.
  * Added prompt environments support.

  **Download the Helm chart:** [`langsmith-0.13.27.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.13.27/langsmith-0.13.27.tgz)
</Update>

<Update label="2026-03-13">
  ## langsmith-0.13.26

  * Sub-agents spawned during Fleet conversations now display real-time status cards inline in the chat, with a detail sidebar showing the sub-agent's live timeline, tool calls, and results.
  * Prebuilt LLM evaluators now use strict structured output mode by default. Strict mode automatically toggles when switching between OpenAI and non-OpenAI model providers.
  * Fixed a bug where online evaluator scores were lost when the evaluation succeeded on a retry but the total job time exceeded the queue timeout.
  * Deleting a run from an annotation queue now fully removes it instead of incorrectly marking it as completed.
  * Included per-annotator feedback in experiments CSV export.
  * Uploading dataset examples with invalid UTF-8 in inputs or outputs now returns a 422 error instead of a 500.
  * Reduced CPU and memory requirements for dev and dev\_free self-hosted deployments.
  * Reject insecure default JWT secret at startup for improved security.
  * Updated brand colors for neutral backgrounds and surfaces.
  * Renamed prompt usage example label from "Use object in LangChain" to "Use Programmatically".
  * Fixed agent zip upload to correctly place cron schedules in the Schedule section.
  * Inbox now sorts the All tab by recency and properly wraps long messages in preview.
  * Fixed chat assistant tooltips rendering behind the chatbox.
  * Added ABAC authorization middleware.

  **Download the Helm chart:** [`langsmith-0.13.26.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.13.26/langsmith-0.13.26.tgz)
</Update>

<Update label="2026-03-12">
  ## langsmith-0.13.25

  * This release packages the same LangSmith application version as langsmith-0.13.24. Refer to the [langsmith-0.13.24](#langsmith-0-13-24) release notes below.

  **Download the Helm chart:** [`langsmith-0.13.25.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.13.25/langsmith-0.13.25.tgz)
</Update>

<Update label="2026-03-10">
  ## langsmith-0.13.24

  * Added rich markdown editor with toolbar and slash commands in Fleet.
  * Added skill creation flow with page entry and navigation in Fleet.
  * Annotation queue CSV exports now include per-annotator feedback scores and a reviewer notes column.
  * Fixed dataset metadata filters not matching number fields across pages.
  * Fixed datasets table only showing first page of results on tall screens.
  * Alert like/notlike filters on error, inputs, and outputs now correctly match individual tokens instead of the full phrase.
  * Fixed `list_runs` tool crashing when the LangSmith API returns an error.
  * Fixed stray artifact in system prompt for Gemini models.
  * Accepting an organization invite now navigates to the newly joined organization.
  * Improved Playground auto-scroll during streaming output.
  * Added workspace scope display for personal API keys.
  * Bumped Python to 3.13 and pinned OpenSSL to resolve security vulnerabilities.
  * Blocked shell injection characters in build/install commands.
  * Improved Polly assistant understanding of traces and runs.
  * Fixed baseline experiment stats not showing on initial page load.
  * Fixed duplicated x-axis date labels on the insights time series chart.
  * Re-enabled ABAC for listing datasets.
  * Added ABAC runs delete endpoint.

  **Download the Helm chart:** [`langsmith-0.13.24.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.13.24/langsmith-0.13.24.tgz)
</Update>

<Update label="2026-03-07">
  ## langsmith-0.13.23

  * Patched security vulnerabilities in smith-frontend.
  * Patched security vulnerabilities in smith-polly.
  * Fixed a code injection vulnerability.
  * Restricted `--allow-run` to only the deno binary in smith-ace.
  * Fixed XSS vulnerability by escaping URLs in the RichTextEditor.
  * Fixed Playground functionality in self-hosted environments.

  **Download the Helm chart:** [`langsmith-0.13.23.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.13.23/langsmith-0.13.23.tgz)
</Update>

<Update label="2026-03-06">
  ## langsmith-0.13.21

  * This release packages the same LangSmith application version as langsmith-0.13.20. Refer to the [langsmith-0.13.20](#langsmith-0-13-20) release notes below.

  **Download the Helm chart:** [`langsmith-0.13.21.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.13.21/langsmith-0.13.21.tgz)
</Update>

<Update label="2026-03-06">
  ## langsmith-0.13.20

  * Added JSON/YAML syntax highlighting to experiment comparison for better readability.
  * Improved thread trace opening behavior in the frontend, removing the need for an expand button.
  * Eliminated n+1 query issue in the backend for listing personal access tokens, improving performance.
  * Fixed support for OpenAI compatible endpoints with smith-polly integration.
  * Timed out bulk exports stuck in `CREATED` status to avoid indefinite processing.
  * Addressed issue where service identity access was blocked from creating repository endpoints.
  * Recorded hub prompt commit in experiment session metadata for better session tracking.
  * Improved authentication for /sessions shadow queries.
  * Updated backend deployments with ABAC (Attribute-Based Access Control).
  * Enhanced UI with projects and runs write permissions support.
  * Added support for new models: GPT-5.4 and GPT-5.4 pro.
  * Fixed large attachment image preview issue for better UI experience.
  * Made GPT-5.4 the default OpenAI playground model, simplifying model selection.
  * Increased maximum tags displayed in `RunTags` component for better visibility.
  * Added models and prompts columns to experiments table, enhancing data insights.
  * Resolved agent builder runs rejection issue when limit settings were changed.
  * Fixed float errors in /sessions go endpoint for improved data handling.
  * Returned fetched value when Redis cache `SET` fails, improving reliability.
  * Enabled AWS IAM role support for agent builder, Polly, and Insights features.
  * Redesigned custom chart CRUD in the frontend, enhancing user satisfaction.
  * Introduced prompt filtering in the experiments table for targeted data analysis.
  * Updated inbox counts and thread fetching logic in Agent Builder for real-time information.
  * Added a feature to group experiments by prompt for streamlined data management.

  **Download the Helm chart:** [`langsmith-0.13.20.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.13.20/langsmith-0.13.20.tgz)
</Update>

<Update label="2026-03-06">
  ## langsmith-0.13.19

  * This release packages the same LangSmith application version as langsmith-0.13.18. Refer to the [langsmith-0.13.18](#langsmith-0-13-18) release notes below.

  **Download the Helm chart:** [`langsmith-0.13.19.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.13.19/langsmith-0.13.19.tgz)
</Update>

<Update label="2026-03-05">
  ## langsmith-0.13.18

  * Introduced a redesigned run details view in threads for improved user experience.
  * Fixed an issue where popovers were covering other content in the UI.
  * Added Microsoft Outlook Calendar Tools to the Agent Builder for integration.
  * Addressed bugs related to agent chat popups and placeholders in the Agent Builder.
  * Improved support for disabling feedback comment filtering in self-hosted instances.
  * Enhanced performance with improved code splitting in the frontend.
  * Added model support for GPT 5.3 instant and GPT-5.3-chat-latest.
  * Introduced a new single\_run filter type for more refined querying.
  * Added ability to read insights reports and show insights categories over time.
  * Added drag-to-resize functionality with persistence in custom iframe output renderer.
  * Enhanced security with more robust user migration processes.
  * Enabled tagging support for evaluators and enhanced their reuse functionality.
  * Fixed issues with session expired warnings after logout.
  * Enhanced UI components for better user interaction in the playground and feedback tagging.
  * Improved metadata handling in datasets and fixed overflow issues.
  * Introduced support for Microsoft Teams Tools in the Agent Builder.
  * Implemented better handling for OAuth provider updates.
  * Added new /orgs/current/info endpoint to the platform-backend for more robust organizational information retrieval.
  * Introduced compatibility testing for session API with added safety checks for PostgreSQL and Redis connections.
  * Added functionality to bind Slack agents dynamically, enhancing the integration experience.

  **Download the Helm chart:** [`langsmith-0.13.18.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.13.18/langsmith-0.13.18.tgz)
</Update>

<Update label="2026-03-03">
  ## langsmith-0.13.17

  * Fixed a bug in the executor deployment handling for new operator versions.
  * Added a setting to filter out internal helper threads from the inbox.
  * Improved the evaluator's page by providing context to Polly's feedback.
  * Forced trace filtering for dataset code evaluators to enhance stability.
  * Updated OAuth mode management, restricting changes during updates.
  * Fixed an issue with experiment cell colors to enhance user clarity.
  * Improved the usage configuration modal to utilize a new TTL endpoint for trace retention.
  * Addressed a bug where workspace invites were not displaying correctly in the UI.
  * Applied brand color adjustments in dark mode and various UI elements.
  * Enhanced OAuth callback security by preventing potential reflected XSS vulnerabilities.
  * Added a dynamic OAuth feature for user management.
  * Fixed a bug preventing filter updates when certain conditions were met.
  * Implemented rebranding updates for the auth screen.
  * Added a feature to collapse sidebar automatically on small viewports.
  * Fixed issues with variable handling in playground evaluate mode.
  * Enhanced the Agent Builder with infinite scroll and improved inbox fetching.
  * Added a new Outlook Trigger feature in the Agent Builder.
  * Upgraded agent-builder to use websockets and new OpenAI model API (gpt-5.3-codex).
  * Fixed auto-save on API key during onboarding process.
  * Resolved issues causing errors in the playground due to empty placeholders.
  * Updated frontend with a new logo for favicon.
  * Fixed authorization bugs in cron deployment for Gmail/Outlook.
  * Updated styling in various UI components, including studio button and index column behavior.
  * Enhanced onboarding snippets for better integration with Langchain Python.
  * Added support for [custom separators in SCIM group names](/langsmith/user-management#configure-custom-separator).

  **Download the Helm chart:** [`langsmith-0.13.17.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.13.17/langsmith-0.13.17.tgz)
</Update>

<Update label="2026-02-26">
  ## langsmith-0.13.16

  * This release packages the same LangSmith application version as langsmith-0.13.15. Refer to the [langsmith-0.13.15](#langsmith-0-13-15) release notes below.

  **Download the Helm chart:** [`langsmith-0.13.16.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.13.16/langsmith-0.13.16.tgz)
</Update>

<Update label="2026-02-26">
  ## langsmith-0.13.15

  * Added rebranded primary colors to button under feature flag in the frontend UI.
  * Replaced dataset autocomplete with tag input to improve user experience.
  * Auto-hide and position Models column in the frontend based on data.
  * Fixed revalidation conflict in the Smith frontend.
  * Improved workspace model configurations to prevent text overflow with tooltips.
  * Surfaced Models option in Group By popover under a feature flag.
  * Supported loading ChatAnthropicVertex model configs in Smith-Polly.
  * Added "No matching filters" message for empty search results in Filter Component Select V2.
  * Enabled navigating automatically to insights with global scroll support.
  * Resolved issues with playground and evaluators provider selector not filtering out disabled providers.
  * Improved messaging mode user experience and styling.
  * Implemented Raw Query Mode for Inline Filters.
  * Allow `secret_key_ref` to be `None` in `K8sEnvVarSource` for backend improvements.
  * Fixed agent builder UI to wrap question text on narrow viewports and dismiss "Add API Key to Get Started" dialog.
  * Updated UX to match evaluator button height with tool button pattern.
  * Persisted selected model in local storage for a consistent UI experience.
  * Auto-generated thread titles for improved thread management.
  * Enhanced backend by gating secrets access with granular RBAC permissions.
  * Implemented Outlook Email Tools in the Agent Builder.
  * Improved keyboard shortcuts in the inbox feature of the Agent Builder UI.

  **Download the Helm chart:** [`langsmith-0.13.15.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.13.15/langsmith-0.13.15.tgz)
</Update>

<Update label="2026-02-24">
  ## langsmith-0.13.14

  * Fixed agent generation interruptions and handling, improving stability in the user experience.
  * Fixed long feedback header text overflow when dragged to the last column.
  * Added OAuth connections for built-in tools and providers on the tool page.
  * Fixed crashes occurring on the run details page.
  * Fixed onboarding dialog not fetching tools unnecessarily.
  * Updated agent builder frontend to show real-time run count.
  * Added private registry UI to the frontend.
  * Enhanced support for SerializedConstructor model configs in playground and insights.
  * Added Gemini 3.1 Pro model to playground and backend model lists.
  * Fixed tool registry crash in the playground.
  * Added support for Gmail authentication improvements, including refresh token capability.
  * Added new API endpoints for running playground experiments using a new service.
  * Improved UI for trace filters with version 2 UX using Filterbar.
  * Enhanced syntax highlighting to match Figma design for standardization.
  * Supported Gmail OAuth v2 with cron logic for higher reliability.
  * Added new models column in the experiment view with updated filtering options.
  * Supported multiple paths for query shadowing log improvements.
  * Added UIs for managing and editing model API key names in the playground.

  **Download the Helm chart:** [`langsmith-0.13.14.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.13.14/langsmith-0.13.14.tgz)
</Update>

<Update label="2026-02-14">
  ## langsmith-0.13.13

  * Reverted the PostgreSQL version to v14.7 and the Redis version to v7. This fixes breaking changes introduced in langsmith-0.13.10.
  * Fixed internal error details being leaked in 5xx responses to enhance security.
  * Improved View UI by moving SaveViewButton from ViewDropdown and changing SaveForm to a modal for better usability.
  * Added model select dropdown to the template creation flow for enhanced user experience.
  * Added warning for duplicate URLs when creating MCP server to prevent configuration errors.
  * Added user context to agents and sub-agents for better feature functionality.
  * Added support for SerializedConstructor model configs in the playground for improved flexibility.
  * Enhanced UI by showing categorical feedback in experiment view config and hiding the sort icon.
  * Improved playground and experiment views by fixing cell alignment.
  * Added image upload support to facilitate better asset management.
  * Added onboarding dialog to general-purpose agent for improved user guidance.
  * Added spinner to loading triggers skeleton for better loading indication.

  **Download the Helm chart:** [`langsmith-0.13.13.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.13.13/langsmith-0.13.13.tgz)
</Update>

<Update label="2026-02-12">
  ## langsmith-0.13.12

  * Improved button sizes and filter chip alignment in the InlineFilters UX.
  * Added commit tags search and display to the Prompt Hub.
  * Fixed issue with viewing experiments having objects for feedback scores.
  * Enhanced tracing for the deploy\_image task.
  * Added a search bar for the new consolidated filter dropdown.
  * Added environment variable for globally disabling personal access token creation.
  * Added cost charts feature.
  * Improved homepage styling and fixed related design issues.
  * Fixed issues with rerendering in General Purpose API (GPA).
  * Improved system to count PENDING, RETRY, and FAILED transactions in self-hosted offline usage reporting.
  * Enhanced the agent builder to localize the current date to the user's timezone.
  * Added Bedrock inference profile dropdown to the playground.
  * Improved error detection and messaging for server issues in agent-chat.
  * Fixed styling issues including email count in invite modal and load state display in the agent editor.
  * Implemented initial design for a tools page with feature flags.
  * Added icon-only filter popover mode to the frontend filter UI.
  * Added beacon endpoint for Self Hosted Agent Builder Runs Limiting.
  * Enable new Granular Usage tab for reporting billable usage by workspace, project, user, and API key (enable with `DEFAULT_ORG_FEATURE_ENABLE_GRANULAR_USAGE_REPORTING=true` and `GRANULAR_USAGE_TABLE_ENABLED=true` environment variables in `commonEnv`)

  **Download the Helm chart:** [`langsmith-0.13.12.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.13.12/langsmith-0.13.12.tgz)
</Update>

<Update label="2026-02-12">
  ## langsmith-0.13.11

  * Improved Agent Builder by using persisted simple model config.
  * Fixed UI for Playground with better message block and tool button consistency.
  * Added a search bar for the new consolidated filter dropdown.
  * Fixed agent builder model selector for users without 'workspaces:manage' permission.
  * Added file upload feature for General Purpose Agent.
  * Added button to create General Purpose Agent.
  * Enhanced the Playground by preserving baseline setting in URL on page reload.
  * Improved Playground experiment table UI and alignment.
  * Fixed bulk deletion of datasets to update the table correctly.
  * Added new API: workspace-scoped tool registry API.
  * Improved support for multifield runFields.
  * Enhanced insights scheduler with backend changes.
  * Added ability to navigate pages in Polly and an initial set of base evaluations.
  * Added tracing enhancements to Agent Builder, including tool call tracing.
  * Integrated changes to support custom model configs temporarily.

  **Download the Helm chart:** [`langsmith-0.13.11.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.13.11/langsmith-0.13.11.tgz)
</Update>

<Update label="2026-02-10">
  ## langsmith-0.13.10

  * This release packages the same LangSmith application version as langsmith-0.13.9. Refer to the [langsmith-0.13.9](#langsmith-0-13-9) release notes below.

  **Download the Helm chart:** [`langsmith-0.13.10.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.13.10/langsmith-0.13.10.tgz)
</Update>

<Update label="2026-02-09">
  ## langsmith-0.13.9

  * Fixed sorting of workspaces alphabetically in the new switcher to improve user experience.
  * Improved playground with new tool modal design and model config popup windows for enhanced usability.
  * Fixed issue with creating tags being idempotent.
  * Modified Agent Builder to cache MCP tools list, session ID, and OAuth tokens for better performance.
  * Fixed updated error message for exhausted agent builder runs.
  * Fixed routing configuration for the agent builder /allow-run API endpoint.
  * Fixed spacing of home page tables for improved UI.
  * Fixed issue with datasets repeatedly fetching if empty.
  * Fixed edit access for API keys for non-admin users.
  * Added cost and token columns in the experiment view for better data insights.
  * Fixed an issue where the Slack trigger was dropping messages due to authentication errors.
  * Fixed boolean feedback values handling in comparison table cells.
  * Updated service key subject for API calls to /allow-run for accurate authentication.
  * Improved agent builder to use persisted simple model config.
  * Fixed error state handling for OAuth login failures.
  * Enhanced agent builder by ensuring threads display errors on reconnect in agent chat.
  * Fixed UI to ensure the footer menu closes on organization switch.
  * Improved tagging authentication by using specific resource auth.
  * Enhanced UI to prevent closing the pane from within the app selector dropdown.
  * Fixed potential SQL injection risks in feedback and annotation queue listing.
  * Added a 15-second timeout to the OAuth HTTP client for improved connection reliability.

  **Download the Helm chart:** [`langsmith-0.13.9.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.13.9/langsmith-0.13.9.tgz)
</Update>

<Update label="2026-02-06">
  ## langsmith-0.13.7

  * This release packages the same LangSmith application version as langsmith-0.13.6. Refer to the [langsmith-0.13.6](#langsmith-0-13-6) release notes below.

  **Download the Helm chart:** [`langsmith-0.13.7.tgz`](https://github.com/langchain-ai/helm/releases/download/langsmith-0.13.7/langsmith-0.13.7.tgz)
</Update>

<Update label="2026-02-05">
  ## langsmith-0.13.6

  * Fixed an issue with truncated large numbers affecting the user interface.
  * Improved error string conversion from S3 to enhance error handling.
  * Updated Filters UX to save DateTimeRange, improving user experience.
  * Fixed UUID conversion to ensure consistent general agent identification.
  * Fixed agent ID conversion to always use a string instead of UUID for stability.
  * Enhanced the experiment comparison view by showing custom computed columns.
  * Fixed chat preview for langchain-shaped output for better user experience.
  * Improved caching mechanisms and authentication control planes' RetryableHTTP.
