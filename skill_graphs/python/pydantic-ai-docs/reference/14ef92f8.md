  * Fix graph execution bug with multiple joins downstream of same fork by
  * Skip installing outlines dependencies mlx, vllm, torch on Intel Macs by
  * Let additional `instructions` be provided at `agent.run` time. by
  * Add `partial_output` to `RunContext` provided to output validators by


#### New Contributors
### v1.10.0 (2025-11-03)
#### What's Changed
  * Fix `MCPServer` error handling with Temporal by
  * Update directory path in ag-ui.md example by
  * Implement `OpenAIResponsesModel.base_url` property by
  * Fix types to let `OpenRouterProvider` be created with only `http_client` by
  * Add `Agent.run_stream_sync` method and sync convenience methods on `StreamedRunResult` by
  * Fix typevar variance for agent deps by
  * Add support for detecting and handling `application/msword` files. by
  * Ensure AG-UI `ToolCallStartEvent` doesn't use a `parent_message_id` from a previous request/response by


#### New Contributors
### v1.9.1 (2025-10-30)
#### What's Changed
  * Support AsyncAnthropicVertex as AnthropicProvider.anthropic_client by
  * Set AG-UI frontend state directly on provided `deps` so it can be read from `on_complete` handler by
  * Retry instead of error when Google response is empty with `MALFORMED_FUNCTION_CALL` or other recoverable finish reason by
  * Add Version Policy to docs by


### v1.9.0 (2025-10-29)
#### What's Changed
  * Support Vercel AI Data Stream Protocol by
  * Fix docs custom retry logic example by


#### New Contributors
### v1.8.0 (2025-10-29)
#### What's Changed
  * Add experiment metadata by
  * Respect `openai_supports_tool_choice_required` model profile setting in `OpenAIResponsesModel` by
  * Use latest OpenAI, Google, Anthropic models in all examples by
  * Fix agent name inference when using `run_stream_events` by


#### New Contributors
### v1.7.0 (2025-10-27)
#### What's Changed
  * Add `OutlinesModel` to run local models using Transformers, Llama.cpp, MLXLM, SGLang and vLLM via Outlines by
  * Fix pydantic-graph importing pydantic-ai by


#### New Contributors
### v1.6.0 (2025-10-24)
#### What's Changed
  * Add `FastMCPToolset` by
  * Add `OpenAIModelProfile.openai_responses_requires_function_call_status_none` flag to satisfy vLLM Responses API by
  * Sanitize auto-generated output tool name to support generic types by
  * Ensure `ToolCallPart.args` resulting from `TestModel(custom_output_args=...)` is always a `dict` by


### v1.5.0 (2025-10-24)
#### What's Changed
  * Introduce new graph API in beta by
  * Preformat run graph/node span names for other OTel backends by
  * Ensure that google-genai doesn't close httpx client provided by Pydantic AI or user by


### v1.4.0 (2025-10-23)
#### What's Changed
  * Support OpenAI and Anthropic native MCP support via `MCPServerTool` builtin tool by
  * Use correct agent's instructions when telling model to retry output by
  * Raise clear error when any Google content filter is hit resulting in empty response by
  * Expand docs for pydantic-evals by


#### New Contributors
### v1.3.0 (2025-10-22)
#### What's Changed
  * Raise `IncompleteToolCall` when token limit is reached during generation of tool call by
  * Include evals report averages in span attributes by
  * Make `AbstractBuiltinTool` serializable and work with durable execution by
  * Ignore empty text deltas when streaming gpt-oss on Bedrock by
  * Ignore empty text deltas when streaming gpt-oss via Ollama by
  * docs: Replace deprecated Cohere model 'command' with 'command-r7b-12-… by
  * Include all usage fields in OTel attributes by
  * Correct Prefect `.serve` example by
  * Ensure toolset spans (e.g. MCP sampling) are nested under agent run span by
  * Update genai-prices, fix default `api_flavor`, fixes anthropic usage extraction by
  * feat(gateway): support AWS Bedrock by
  * Add OVHcloud AI Endpoints provider by
  * Use `gateway/<upstream_provider>:` as provider name prefix for Gateway by
  * Add `http_client` option to `GoogleProvider`, support `api_key` for Vertex AI, and use Pydantic AI's cached httpx client by default by


#### New Contributors
### v1.2.0 (2025-10-20)
#### What's Changed
  * Strip markdown fences when generating evals datasets by
  * Include `final_result` agent span attribute after streaming by
  * Add Claude Haiku 4.5 model by
  * change paig base url by
  * Extract openai usage using genai-prices by


#### New Contributors
### v1.1.0 (2025-10-15)
#### Features in v1.1.0
  * Add support for durable execution with Prefect by


#### Selected Features since v1.0.0
  * Support image generation and output with Google and OpenAI by
  * Add Pydantic AI Gateway provider by
  * Add support for `previous_response_id` from OpenAI Responses API by
  * Add support for durable execution with DBOS by
  * Built-in tool call streaming from OpenAI, Google, Anthropic by
  * Support Anthropic built-in memory tool by
  * Support text, JSON, XML and YAML `DocumentUrl` and `BinaryContent` on OpenAI by
  * Added MCP metadata and annotations to `ToolDefinition.metadata` for use in filtering by
  * Let agent `name` be overridden contextually by
  * Support contextually overriding agent `instructions` by
  * Tools can now return AG-UI events separate from result sent to model by
  * Add `AgentRunResult.response` convenience method to get latest model response by
  * Add `ModelResponse.text`, `thinking`, `files`, `images`, `tool_calls`, and `builtin_tool_calls` convenience methods by
  * Add `Agent.run_stream_events()` convenience method wrapping `run(event_stream_handler=...)` by


#### Other Changes in v1.1.0
  * Record instructions on the agent run span even when they are dynamic by
  * Add `description` arg to tool function decorators by
  * fix(gateway): update base_url by
  * Document OpenAI-compatible provider prefixes by
  * Explicitly request image response modality from Google API when model supports it by


#### New Contributors
### v1.0.18 (2025-10-13)
#### What's Changed
  * Add `render` method to `EvaluationReport` class by
  * Omit `previous_response_id` when unset instead of sending `null` to OpenAI Responses by
  * Include all API docs in llms.txt by
  * Add anyio and httpcore to Temporal passthrough modules by
  * Add Nebius AI Studio provider support by
  * Add new `ToolCallPart.id` field for OpenAI Responses by


#### New Contributors
### v1.0.17 (2025-10-09)
#### What's Changed
  * Let `builtin_tools` be specified at agent run time by
  * Make `BinaryImage` work with inline-snapshot by
  * Document `InstrumentationSettings(version=3)` by


### v1.0.16 (2025-10-08)
#### What's Changed
  * Add support for datetime.time/timedelta to format_as_xml by
  * Ensure graph persistence snapshots are not mutated when run is resumed by
  * Use `Sequence[ModelMessage]` instead of `list` for method arg types by
  * Let agent name be overridden contextually by
  * Respect `FileUrl.force_download` flag in OpenAI Chat and Responses models by
  * Ensure `FileUrl` and `BinaryContent` without `identifier` are valid by
  * Don't include ToolResultPart for external tool call when streaming by
  * Fix token usage for anthropic streaming by
  * plain text docs, fix redirects and add logfire by


#### New Contributors
### v1.0.15 (2025-10-03)
#### What's Changed
  * Support image generation and output with Google and OpenAI by
  * Add `AgentRunResult.response` convenience method to get latest model response by
  * Add `ModelResponse.text`, `thinking`, `files`, `images`, `tool_calls`, and `builtin_tool_calls` convenience methods by
  * Add `Agent.run_stream_events()` convenience method wrapping `run(event_stream_handler=...)` by
  * Add content (e.g. files) returned by tool to `FunctionToolResultEvent` by
  * Set `MCPServer` `id` and `tool_prefix` in `load_mcp_servers` by
  * Add latest gemini 2.5 flash(-lite) model names and aliases by
  * Support enums in `format_as_xml` by
  * Fix dataset serialization when inputs have discriminators with defaults by
  * Fix parallel tool call limit enforcement by


### v1.0.14 (2025-10-02)
#### What's Changed
  * Remove leftover debug `print` statement by
  * Fix duplicate output tool return part when concatenating first run messages with follow-up `new_messages` by


#### New Contributors
### v1.0.13 (2025-10-01)
#### What's Changed
  * feat: Otel instrumentation version 3 by
  * Don't send strict to HuggingFace API as it's not supported by their types and at least some models by
  * Correctly merge `Model.settings` with `model_settings` in direct mode by
  * Expose `server_info` in `MCPServer` by
  * Support contextually overriding agent instructions by
  * Update evals attributes by


#### New Contributors
### v1.0.12 (2025-09-30)
#### What's Changed
  * Support Anthropic built-in memory tool by
  * Support text, JSON, XML and YAML `DocumentUrl` and `BinaryContent` on OpenAI by
  * Prefer `structuredContent` MCP tool result when present by
  * Expose `.messages`, `.toolsets` types in top-level `pydantic_ai` to aid IDE auto-import by
  * Add cost metric to the pydantic-evals output by
  * Add retry args to `pydantic_evals.Dataset.evaluate_sync` by
  * Change type of common_tools to work with agent with any deps type by
  * Don't error when Gemini returns more than one candidate response by
  * Handle Ollama responses without `finish_reason` and document Ollama Cloud by
  * Add custom Vertex AI Model Garden example by
  * Fix StructuredDict with nested JSON schemas using $ref by


#### New Contributors
### v1.0.11 (2025-09-29)
#### What's Changed
  * Support OpenAI image detail on `ImageUrl` and `BinaryContent` via `vendor_metadata` by
  * Support callable classes as history processors by
  * Add `claude-sonnet-4-5` to known model names by
  * Add `operation.cost` metric to instrumented models by
  * Fix streaming gpt-oss using Ollama by
  * Raise error when using Anthropic thinking with output tools by
  * Make `OutputObjectDefinition` public on `pydantic_ai.output` by
  * Update `pyproject.toml` to be PEP639 compliant by
  * Bump temporalio to 1.18.0 by
  * Bump genai-prices to 0.0.28 by
  * Document that Gemini requires native or prompted output mode for structured output streaming by
  * Update Ollama docs instructions by
  * Update docs and tests for DBOS v2.0 by


#### New Contributors
### v1.0.10 (2025-09-19)
#### What's Changed
  * Fix OTel for built-in tools returning a list (e.g. Anthropic web search) by
  * Drop assertion that Google streaming chunk has candidates by
  * Retry model request that produced an empty response by
  * Clarify `Agent(retries=...)` description by
  * Stop redundantly encoding binary data as base64 when sending to Google genai SDK by
  * Use model class names as tags in `format_as_xml` and add option to include field titles and descriptions as attributes by


### v1.0.9 (2025-09-18)
#### What's Changed
  * Stream built-in tool calls from OpenAI, Google, Anthropic and return them on next request (required for OpenAI reasoning) by
  * Include built-in tool calls and results in OTel messages by
  * Add `RunContext.max_retries` and `.last_attempt` by
  * Fix `StreamedResponse.model_name` for Azure OpenAI with content filter by
  * Fix TemporalAgent dropping model-specific `ModelSettings` (e.g. `openai_reasoning_effort`) by
  * Don't send item IDs to Responses API for non-reasoning models by
  * Update DBOS version by


### v1.0.8 (2025-09-16)
#### What's Changed
  * Tools can now return AG-UI events separate from result sent to model by
  * Fix bug causing doubled reasoning tokens usage by deepcopying by
  * Fix auto-detection of HTTP proxy settings by
  * Fix `new_messages()` and `capture_run_messages()` when history processors are used by
  * chore: Remove 'text' from RunUsage docstrings by


#### New Contributors
### v1.0.7 (2025-09-15)
#### What's Changed
  * Added MCP metadata and annotations to `ToolDefinition.metadata` for use in filtering by
  * When starting run with message history ending in `ModelRequest`, make its content available in `RunContext.prompt` by
  * Let `FunctionToolset` take default values for `strict`, `sequential`, `requires_approval`, `metadata` by
  * Don't require `mcp` or `logfire` to use Temporal or DBOS by
  * Combine consecutive AG-UI user and assistant messages into the same model request/response by
  * Fix `new_messages()` when `deferred_tool_results` is used with `message_history` ending in `ToolReturnPart`s by


### v1.0.6 (2025-09-12)
#### What's Changed
  * Add support for `previous_response_id` from Responses API by
  * Let MCP servers be loaded from file by
  * Fix how thinking summaries are sent back to Responses API by
  * Bump Cohere SDK and remove incorrect typing workaround by
  * Update MCP tool call customisation docs by


#### New Contributors
### v1.0.5 (2025-09-11)
#### What's Changed
  * Don't lose Azure OpenAI Responses encrypted_content if no summary was included by
  * Store OpenAI Responses text part ID to prevent error with reasoning by
  * Make OpenAIResponsesModel work with reasoning from other models and modified history by


### v1.0.4 (2025-09-11)
#### What's Changed
  * Add Pydantic AI Gateway provider by
  * Fix OpenAI Responses API tool calls with reasoning by
  * Support OpenAI Responses API returning encrypted reasoning content without summary by
  * Don't ask for OpenAI Responses API to include encrypted reasoning content for models that don't support it by
  * docs: update builtin-tools md by


#### New Contributors
### v1.0.3 (2025-09-10)
#### What's Changed
  * Include thinking parts in subsequent model requests to improve performance and cache hit rates by
  * Add `on_complete` callback to AG-UI functions to get access to `AgentRunResult` by
  * Support `ModelSettings.seed` in `GoogleModel` by
  * Add `with agent.sequential_tool_calls():` contextmanager and use it in `DBOSAgent` by
  * Ensure `ModelResponse` fields are set from actual model response when streaming by
  * Send AG-UI thinking start and end events by
  * Support models that return output tool args as `{"response': "<JSON string>"}` by
  * Support `NativeOutput` with `FunctionModel` by
  * Raise error when `WebSearchTool` is used with `OpenAIChatModel` and unsupported model by


#### New Contributors
### v1.0.2 (2025-09-08)
#### What's Changed
  * Add support for durable execution with DBOS by
  * Support sequential tool calling by
  * Add `GoogleModelSettings.google_cached_content` to pass `cached_content` by
  * Add `ModelResponse.finish_reason` and set `provider_response_id` while streaming by
  * Add support for `gen_ai.response.id` by
  * Only send tool choice to Bedrock Converse API for Anthropic and Nova models by
  * Handle errors in cost calculation in InstrumentedModel by


#### New Contributors
### v1.0.1 (2025-09-05)
#### Breaking Changes
The following breaking change was slated to go into v1.0.0 but accidentally left out. Because it's a security issue, an uncommonly used feature, and few people will have updated to v1 yet within 24 hours, we decided it was justified to make an exception to the no-breaking-changes policy to get it out ASAP.
  * Remove `Python` evaluator from `pydantic_evals` for security reasons by


#### Other Changes
  * Remove `eval-type-backport` dependency by


### v1.0.0 (2025-09-04)
#### What's Changed
  * Drop support for Python 3.9 by
  * Deprecate `OpenAIModelProfile.openai_supports_sampling_settings` by
  * Add support for human-in-the-loop tool call approval by
  * Add `tool_calls_limit` to `UsageLimits` and `tool_calls` to `RunUsage` by
  * Add LiteLLM provider for OpenAI API compatible models by
  * Add `identifier` field to `FileUrl` and subclasses by
  * Support `NativeOutput` with Groq by
  * Add `docstring_format`, `require_parameter_descriptions`, `schema_generator` to `FunctionToolset` by
  * Gracefully handle errors in evals by
  * Include `logfire` with pydantic-ai package by
  * Let almost all types used in docs examples be imported directly from `pydantic_ai` by
  * Bump `temporalio` to 1.17.0 by
  * Default `InstrumentationSettings` `version` to 2 by
  * Remove cases and averages from eval span by
  * Make many more dataclasses kw-only by
  * Don't emit empty AG-UI thinking message events by
  * Update `mcp` package version by
  * Raise error if MCP server `__aexit__` is called when `_running_count` is already `0` by
  * Fix error when streaming from Gemini includes only `executable_code` or `code_execution_result` by
  * Close original response when retrying HTTP request by
  * `Agent.__aenter__` returns `Self`, use default instrumentation for MCP sampling model by
  * Fix Anthropic streaming usage counting by
  * Create separate `ThinkingParts` for separate OpenAI Responses reasoning summary parts by
  * Handle Groq `tool_use_failed` errors by getting model to retry by
  * Raise error when trying to use Google built-in tools with user/output tools by
  * Move `mcp-run-python` to its own repo by
  * Fix Azure OpenAI streaming when async content filter is enabled by
  * Don't emit AG-UI text message content events with empty text part deltas by
  * Handle streaming thinking signature deltas from Bedrock Converse API by
  * Don't require `MCPServerStreamableHTTP` and `MCPServerSSE` `url` to be a keyword argument by
  * Add `operation.cost` span attribute to model request spans, rename `ModelResponse.price()` to `.cost()` by
  * Ensure that old `ModelResponse`s stored in a DB can still be deserialized by
  * Type `ModelRequest.parts` and `ModelResponse.parts` as `Sequence` by
  * Always run `event_stream_handler` inside Temporal activity by
  * Document that various functions need to be async to be used with Temporal by


#### New Contributors
### v1.0.0b1 (2025-08-30)
#### What's Changed
  * Drop support for Python 3.9 by
  * Add support for human-in-the-loop tool call approval by
  * Deprecate `OpenAIModelProfile.openai_supports_sampling_settings` by
  * Gracefully handle errors in evals by
  * Include logfire with pydantic-ai package by
  * Remove errors when passing Retrying instead of RetryConfig to TenacityTransport by
  * Default `InstrumentationSettings` `version` to 2 by
  * Remove cases and averages from eval span by
  * Make many more dataclasses kw-only by


### v0.8.1 (2025-08-29)
#### What's Changed
  * Add `gen_ai.system_instructions` attribute to agent run spans by
  * Bump `temporalio` to 1.16.0 by
  * Rename `StreamedRunResult` methods to be consistent with `AgentStream` by
  * Deprecate specifying a model name without a provider prefix, and the `vertexai` provider name by
  * Rename `ModelResponse.provider_request_id` to `provider_response_id` by
  * docs: Add `message_history` parameter documentation for CLI methods by


### v0.8.0 (2025-08-26)
#### What's Changed
  * Add elicitation callback support to MCP servers by
  * Add `message_history` parameter to `agent.to_cli()` by
  * Properly deserialize complex tool arguments with Temporal by
  * Fix serialization / deserialization of `FileUrl.media_type` by
  * Handle missing token details in vLLM/OpenAI-compatible APIs by
  * Make AgentStreamEvent union of ModelResponseStreamEvent and HandleResponseEvent by


### v0.7.6 (2025-08-26)
#### What's Changed
  * Replace `all_messages_events` with `pydantic_ai.all_messages` for `InstrumentationSettings(version=2)` by
  * Fix inability to call response.raise_for_status in AsyncTenacityTransport by
  * Deprecate `OpenAIModel` in favor of `OpenAIChatModel` by
  * anthropic: drop new lines on empty system prompt by
  * fix(bedrock): skip SystemPromptPart with empty content by
  * BREAKING CHANGE: Fix tenacity implementation for improved retry behavior by
  * Add Cerebras provider by


#### New Contributors
### v0.7.5 (2025-08-25)
#### What's Changed
  * Handle 'STOP' finish_reason in GeminiStreamedResponse by
  * Add `price()` method to `ModelResponse` by
  * Include thoughts tokens in output_tokens for Google models by
  * Add `span_id` and `trace_id` to `EvaluationReport` by
  * Allow proper type on `AnthropicProvider` when using Bedrock by
  * Use new OpenTelemetry GenAI chat span attribute conventions by
  * Ensure `content` is always set for assistant tool call messages for OpenAI. by


#### New Contributors
### v0.7.4 (2025-08-20)
#### What's Changed
  * Fix bug with google model safety handling by
  * Add `takes_ctx` arg to `Tool.from_schema` by
  * feat: support Google's url_context builtin tool by
  * Add missing UrlContextTool into **all** by
  * Drop assertion on Google streaming by


#### New Contributors
### v0.7.3 (2025-08-19)
#### What's Changed
  * Deprecate `Usage` in favour of `RequestUsage` and `RunUsage` by
  * Make `FallbackModel` accept string model names by
  * Move `system_prompt_role` from `OpenAIModel` to `OpenAIModelProfile` by
  * Add `/cp` command to CLI to copy last response to clipboard by
  * Pin temporalio to 1.15.0 as plugins API is still experimental by
  * Use `_provider.name` instead of `_system` by


#### New Contributors
### v0.7.2 (2025-08-14)
#### What's Changed
  * Let message history end on ModelResponse and execute pending tool calls by
  * Ignore leading whitespace when streaming from Qwen or DeepSeek by
  * Stop calling MCP server `get_tools` ahead of `agent run` span by
  * Remove anthropic-beta default header set in `AnthropicModel` by
  * Add `OllamaProvider` by
  * Add `profile` and `settings` to `HuggingfaceModel` by
  * Ask model to try again if it produced a response without text or tool calls, only thinking by
  * Forward max_uses parameter to Anthropic WebSearchTool by


#### New Contributors
### v0.7.1 (2025-08-13)
#### What's Changed
  * Add new OpenAI GPT-5 models by
  * Add support for OpenAI verbosity parameter in Responses API by
  * Add support for `"openai-responses"` model inference string by
  * Add `UsageLimits.count_tokens_before_request` using Gemini `count_tokens` API by
  * Fix `FallbackModel` to respect each model's model settings by


#### New Contributors
### v0.7.0 (2025-08-12)
#### What's Changed
  * Let Agent be run in a Temporal workflow by moving model requests, tool calls, and MCP to Temporal activities by
  * Let toolsets be built dynamically based on run context by
  * Add `event_stream_handler` to agent and run methods by
  * History processor replaces message history by
  * Add `AbstractAgent` and `WrapperAgent` by
  * Add `Agent.override(tools=...)` by
  * Bump mcp-run-python by
  * Fix error when using GPT-5 with a temperature setting by
  * Fix KeyError when parsing video metadata without audio track in Google models by
  * Make OpenAIResponsesModelSettings.openai_builtin_tools work again by


#### New Contributors
### v0.6.2 (2025-08-07)
#### What's Changed
  * Add `builtin_tools` to `Agent` by


#### New Contributors
### v0.6.1 (2025-08-07)
#### What's Changed
  * Automatically use OpenAI strict mode for strict-compatible native output types by
  * Make `InlineDefsJsonSchemaTransformer` public by
  * Send `ThinkingPart`s back to Anthropic used through Bedrock by
  * Support `AWS_BEARER_TOKEN_BEDROCK` API key env var by
  * Add new Heroku models by


### v0.6.0 (2025-08-06)
#### What's Changed
  * Remove older deprecated models and add new model of Anthropic by
  * BREAKING CHANGE: Remove `next()` method from `Graph` by
  * BREAKING CHANGE: Remove `data` from `FinalResult` by
  * BREAKING CHANGE: Remove `get_data` and `validate_structured_result` from `StreamedRunResult` by
  * docs: add `griffe_warnings_deprecated` by
  * BREAKING CHANGE: Remove `format_as_xml` module by
  * BREAKING CHANGE: Remove `result_type` parameter and similar from `Agent` by
  * Deprecate `GoogleGLAProvider` and `GoogleVertexProvider` by
  * BREAKING CHANGE: drop 4 months old deprecation warnings by


### v0.5.1 (2025-08-06)
#### What's Changed
  * google: add more information about schema on union by
  * Deprecate `GeminiModel` in favor of `GoogleModel` by
  * Use `httpx` on `GoogleProvider` by


#### New Contributors
### v0.5.0 (2025-08-04)
#### What's Changed
  * Breaking Change: The `EvaluationReport.print` and `EvaluationReport.console_table` methods now require most arguments be passed by keyword. by
  * Breaking Change: The `source` field of an `EvaluationResult` is now of type `EvaluatorSpec` rather than the actual source `Evaluator` instance, to help with serialization/deserialization by
  * Let more `BaseModel`s use OpenAI strict JSON mode by defaulting to `additionalProperties=False` by
  * Allow string format, pattern and others in OpenAI strict JSON mode by
  * Include default values in tool arguments JSON schema by
  * Fix ImageUrl, VideoUrl, AudioUrl and DocumentUrl not being serializable by
  * Fix `test_download_item_no_content_type` test failing on macOS by
  * Document performance implications of async vs sync tools by
  * Document that tools become toolset internally by
  * docs: add missing optional packages in `install.md` by


#### New Contributors
### v0.4.11 (2025-08-01)
#### What's Changed
  * Add convenience functions to handle AG-UI requests with request-specific deps by
  * Support custom thinking tags specified on the model profile by
  * Rename gemini-2.5-flash-lite-preview-06-17 to gemini-2.5-flash-lite as it's out of preview by
  * Fix toggleable toolset example so toolset state is not shared across agent runs by
