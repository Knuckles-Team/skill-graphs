## Full Changelog
### v1.67.0 (2026-03-06)
#### What's Changed
##### 🚀 Features
  * Add GPT-5.4 support by
  * Support `WebSearchTool` for `OpenRouterModel` through OpenRouter plugins by
  * Rehaul Tavily search tool by
  * Enable native structured output support for Ollama provider by


##### 🐛 Bug Fixes
  * Add missing Vercel AI SDK v6 tool approval part types by


#### New Contributors
### v1.66.0 (2026-03-04)
#### What's Changed
##### 🚀 Features
  * Enable native structured output for Qwen 3.5 models by
  * Add Nano Banana 2 (`gemini-3.1-flash-image-preview`) by


##### 🐛 Bug Fixes
  * Fix builtin tool availability checking when using `TemporalAgent` with multiple models by
  * Fix `HasMatchingSpan` YAML export/import round-trip for `SpanQuery` arguments by


#### New Contributors
### v1.65.0 (2026-03-03)
#### What's Changed
##### 🚀 Features
  * Support files uploaded to providers via new `UploadedFile` object by
  * feat: add `gemini-3.1-flash-lite-preview` model by


##### 🐛 Bug Fixes
  * fix: add `__reduce__` to exception classes for pickle support by


#### New Contributors
### v1.64.0 (2026-03-02)
#### What's Changed
##### 🚀 Features
  * feat: support `template=False` on `PromptedOutput` and `NativeOutput` to disable schema prompt by


##### 🐛 Bug Fixes
  * Fix missing `run_id` on `ModelRequest` in UI adapter runs by
  * Wrap Google streaming errors as `ModelHTTPError`/`ModelAPIError` by
  * fix(mcp): move `__aexit__` guard inside lock to prevent TOCTOU race by
  * fix: `BaseToolCallPart.has_content()` incorrectly returns False for falsy arg values by
  * fix(anthropic): auto-fallback to streaming for high `max_tokens` by
  * fix(vercel): Align `dump_messages` output with Vercel spec by
  * fix: cancel sibling tasks on any exception in parallel tool execution by


#### New Contributors
### v1.63.0 (2026-02-23)
#### What's Changed
##### 🚀 Features
  * Add Gemini 3.1 Pro Preview support by
  * feat(gemini): Logprob Support by
  * Add `args_validator` parameter to tools for pre-execution validation by


##### 🐛 Bug Fixes
  * Fix Temporal and DBOS MCP to use cached tools instead of fetching each time by
  * Updated Cohere content item typing to fix the incompatibility by
  * Fix Anthropic model on Bedrock incorrectly being treated as supporting json schema output by
  * fix(pydantic-evals): gracefully handle custom `TracerProviders` without `add_span_processor` by
  * fix: use non-greedy regex in `strip_markdown_fences` to stop at closing fence by
  * fix: add defaults for optional fields in OpenRouter streaming models by
  * Set `BuiltinToolCallPart.id` for OpenAI Responses WebSearch/FileSearch by
  * fix: Identify new messages by `run_id` instead of index by


#### New Contributors
### v1.62.0 (2026-02-18)
#### What's Changed
##### 🚀 Features
  * Add tool approval integration for Vercel AI adapter by
  * Add LinePlot analysis type, ROCAUCEvaluator, and KolmogorovSmirnovEvaluator by


##### 🐛 Bug Fixes
  * Fix missing pages in llms.txt and llms-full.txt by
  * Handle Groq `tool_use_failed` errors without tool name/args by retrying by
  * fix: handle content filter refusals for Google `prompt_feedback` and OpenAI refusals by


##### 📦 Dependencies
  * bump `huggingface` to 1.3.4 by
  * Use `griffelib` instead of `griffe` by


### v1.61.0 (2026-02-17)
#### What's Changed
##### 🚀 Features
  * Support Python 3.14 by


##### 📦 Dependencies
  * Upgrade anthropic to 0.80.0, add Claude Sonnet 4.6 by


### v1.60.0 (2026-02-16)
#### What's Changed
##### 🚀 Features
  * Add ‍`video_url` support to `OpenRouterModel` by
  * Add instrumentation version 4 to match OTel GenAI semantic conventions for multimodal input by


##### 🐛 Bug Fixes
  * Fix AG-UI `parent_message_id` for back-to-back builtin tool calls by
  * Only suggest 'call a tool' in retry when tools are available by
  * Wrap `_stream_text_deltas` with `aclosing` to prevent `StopAsyncIteration` on client disconnect by


#### New Contributors
### v1.59.0 (2026-02-13)
#### What's Changed
##### 🚀 Features
  * Add `Model.model_id` property that returns `provider:model` by
  * Add opt-in flag for aggregated usage attribute names by
  * Enhance `Contains` evaluator to support `pydantic.BaseModel` by
  * Vercel AI adapter: let `BaseChunk`s be injected through `ToolReturnPart.metadata` by


##### 🐛 Bug Fixes
  * XAI: lazily create AsyncClient per event loop to avoid gRPC loop mismatch by


#### New Contributors
### v1.58.0 (2026-02-10)
#### What's Changed
##### 🚀 Features
  * Report-level evaluators & experiment-wide analyses by
  * Add multi-run aggregation support (repeat parameter) to pydantic-evals by
  * Add `extra_headers` support for Google model provider by


#### New Contributors
### v1.57.0 (2026-02-09)
#### What's Changed
##### 🐛 Bug Fixes
  * Fix A2A FilePart base64 decoding for image/file uploads by


#### New Contributors
### v1.56.0 (2026-02-05)
#### What's Changed
##### 🚀 Features
  * Add Claude Opus 4.6, `anthropic_effort` and `anthropic_thinking.type='adaptive'` by
  * Add `anthropic_betas` to `AnthropicModelSettings` by


##### 🐛 Bug Fixes
  * Fix Bedrock `CachePoint` placement with multiple trailing documents by
  * Disallow downloading `FileUrl`s pointing at the local network by default by


### v1.55.0 (2026-02-04)
#### What's Changed
##### 🐛 Bug Fixes
  * Fix error when using `OpenAIResponsesModel` with "compatible" provider that returns `reasoning_tokens` as `None` instead by
  * Fix `MultiModalContent` union missing discriminator causing incorrect deserialization by


### v1.54.0 (2026-02-04)
#### What's Changed
##### 🚀 Features
  * Add concurrency limiting for Agents and Models by


### v1.53.0 (2026-02-04)
#### What's Changed
##### 🚀 Features
  * Infer gateway base URL from token region by


### v1.52.0 (2026-02-02)
#### What's Changed
##### 🚀 Features
  * Add `openai_store` setting to control data retention by
  * Add number of output validation retries to agent's run context by
  * Have `OpenAIChatModel` send back reasoning content via field it's received in by


##### 🐛 Bug Fixes
  * Fix compatibility with Vercel AI SDK v5 by adding SDK version param by
  * Handle non-primitive types in `BaseModel` in `format_as_xml` by


#### New Contributors
### v1.51.0 (2026-01-30)
#### What's Changed
##### 🚀 Features
  * feat(ui): Add `html_source` parameter to customize Chat UI source by


##### 🐛 Bug Fixes
  * Fix error when Gemini calls tools in agent run with instructions but no user prompt by
  * Fix Bedrock caching when user message ended on non-text content by


#### New Contributors
### v1.50.0 (2026-01-29)
#### What's Changed
##### 🚀 Features
  * Expose `usage_limits` and `model_settings` to users running with `to_cli()` by
  * Add setting to include OpenAI raw text annotations in `TextPart.provider_details` by


##### 🐛 Bug Fixes
  * Fix serialization of `BinaryContent` returned by tool in Temporal by
  * Fix serialization of `DocumentUrl` with custom `media_type` in Temporal by
  * Retry instead of raising error when Google returns 0 candidates by
  * Correct OpenAI `prompt_cache_retention` literal from 'in-memory' to 'in_memory' by


#### New Contributors
### v1.49.0 (2026-01-28)
#### What's Changed
##### 🚀 Features
  * Support parallel tool calls in `DBOSAgent` by
  * Add `BedrockEmbeddingModel` for Nova, Cohere and Titan endpoints by
  * Match Vercel AI SDK types with AI SDK v6 by


### v1.48.0 (2026-01-27)
#### What's Changed
##### 🚀 Features
  * Add `allowed_domains` support for `WebSearchTool` with OpenAI by
  * Add `continuous_usage_stats` model setting for OpenAI by
  * Apply `model_settings` to Mistral streaming JSON mode by


##### 🐛 Bug Fixes
  * Allow sampling params for GPT-5.1+ when reasoning is off by
  * Support "OpenAI-compatible" embeddings APIs that omit usage by


#### New Contributors
### v1.47.0 (2026-01-23)
#### What's Changed
##### 🚀 Features
  * Ensure thought signatures and other provider metadata survive a round trip through a Vercel AI frontend by


#### New Contributors
### v1.46.0 (2026-01-22)
#### What's Changed
##### 🚀 Features
  * Add `XaiModel` that uses the xAI SDK and deprecate `GrokProvider` that used the OpenAI-compatible API by
  * Bump `mcp` and other dependencies for Dependabot alerts by


#### New Contributors
### v1.45.0 (2026-01-21)
#### What's Changed
##### 🚀 Features
  * VoyageAI embeddings support by


##### 🐛 Bug Fixes
  * Update the default behavior for `OpenRouter` from downloading `DocumentUrl`s and sending them as bytes, to sending them as URLs by
  * fix(google): Set timeout in `HttpOptions` to prevent requests hanging indefinitely by
  * Fix Gemini ignoring user prompt when continuing conversation that ended on structured output by
  * bug: Fix gateway snippet auto-generation for the `google-gla` shorthand by
  * Use `get_type_hints()` in `function_schema()` by


#### New Contributors
### v1.44.0 (2026-01-16)
#### What's Changed
##### 🚀 Features
  * feat: Add Exa search tools integration by
  * Add support for Bedrock Nova 2.0 built-in `Code Interpreter` tool by


##### 🐛 Bug Fixes
  * Make `count_tokens()` work on `WrapperModel` by


#### New Contributors
### v1.43.0 (2026-01-15)
#### What's Changed
##### 🚀 Features
  * Support Google embedding models by


##### 🐛 Bug Fixes
  * Fix OpenAI never populating `dict[str, ...]` tool args by


### v1.42.0 (2026-01-13)
#### What's Changed
##### 🚀 Features
  * Add SambaNova provider support by
  * Consistently raise `ContentFilterError` when model response is empty because of content filter by
  * Bump google-genai to 1.56.0 by
  * Add OTel GenAI semantic convention attributes by


##### 🐛 Bug Fixes
  * Cancel tool calls when `Agent.run` or `Agent.run_stream_events` coroutine is cancelled by


#### New Contributors
### v1.41.0 (2026-01-09)
#### What's Changed
##### 🚀 Features
  * Add YAML and TOML media type support in `BinaryContent.from_path` by
  * Add `metadata` support for `DeferredToolResults` by


##### 🐛 Bug Fixes
  * Don't raise error when Mistral returns `ReferenceChunk` by


#### New Contributors
### v1.40.0 (2026-01-06)
#### What's Changed
##### 🚀 Features
  * Set human-readable Temporal activity summaries by
  * Let agent call nonexistent tool as often as `Agent` `retries` limit specifies by


##### 🐛 Bug Fixes
  * Ensure `stream_output()` always calls output function/validator with `partial_output=False` at the end of streaming by
  * Fix `PydanticAIPlugin` to preserve custom `payload_codec` and respect `PydanticPayloadConverter` subclasses by


#### New Contributors
### v1.39.1 (2026-01-05)
#### What's Changed
##### 🐛 Bug Fixes
  * Fix `partial_output` flag in `TextOutput` during streaming by
  * Fix duplicated tool calls with `partial_output=False` and cache result by
  * Update `thoughtSignature` for Vertex Gemini 3 compatibility by
  * Fix `input_tokens` calculation for Bedrock model (###3850) by


#### New Contributors
### v1.39.0 (2025-12-23)
#### What's Changed
  * Support embedding models by
  * Add Agent and agent run metadata and expose it on result objects and span attributes by
  * Support system prompts functions returning `None` by
  * Handle ThinkingPart in MCP Sampling by
  * Add `bedrock_service_tier` setting to `BedrockModelSettings` by
  * Add docs and tests for `RunContext.partial_output` in output tools by
  * Update docs about choosing priority of output and deferred tool calls with run_stream by
  * docs: Fix cross references by
  * Add pydantic-deep + toolsets to docs by


#### New Contributors
### v1.38.0 (2025-12-22)
#### What's Changed
  * Add local timestamps to request and response models - include provider timestamp in `provider_details` by
  * Respect `VideoUrl.vendor_metadata` for GCS URIs on google-vertex by
  * Fix media type inference for URLs with query parameters by
  * Allow typed `RunContext[Deps]` in `TextOutput` signature by
  * Silently ignore AG-UI `ActivityMessage` instead of raising error by
  * docs: Add Azure, Bedrock and Vertex examples to use Anthropic models by
  * docs: Add note on persistence to beta graph docs by


#### New Contributors
### v1.37.0 (2025-12-19)
#### What's Changed
  * Allow `TemporalAgent` to switch model at `agent.run`-time by
  * Add `DynamicToolset` support in Temporal by
  * Add support for `ImageGenerationTool` `output_compression` and `output_format` for Vertex AI Gemini image models by
  * Update known Groq model names (add production/preview, remove deprecated) by
  * Add model profile flag for APIs that support native output but still require JSON schema in instructions by
  * Set `ToolRetryError` message by
  * Fix `StreamedRunResult.get_output()` creating duplicate messages if `stream_output()` has already been called by
  * Re-add `clai --help` output to clai README by


#### New Contributors
### v1.36.0 (2025-12-18)
#### What's Changed
  * Add AI SDK data chunk ID and tool approval types by
  * Ensure `type` field when converting `const` to `enum` in `GoogleJsonSchemaTransformer` by
  * Bump `google-genai` to 1.56.0 by


#### New Contributors
### v1.35.0 (2025-12-17)
#### What's Changed
  * Add `FileSearchTool` with support for OpenAI and Google by
  * Add support for `ImageGenerationTool.size` to Gemini image models by
  * Adding Gemini 3 flash by
  * Add Alibaba Cloud `DashScopeProvider` and support audio input for Qwen Omni by
  * Added support for AG-UI Multi-modal Messages by
  * Set timestamps on AG-UI events by
  * Support OpenAI reasoning summary option 'auto' by
  * Operate on a deepcopy of `$defs` in `JsonSchemaTransformer` instead of the original schema by
  * Fix typing issue when using `UIAdapter.dispatch_request` with agent with `output_type` by


#### New Contributors
### v1.34.0 (2025-12-16)
#### What's Changed
  * Add Web Chat UI for any agent that can be launched using `clai web` or `Agent.to_web()` by
  * Support `FileUrl.force_download` in `AnthropicModel` and `OpenAIResponsesModel` by
  * Fix using sync history processors, instructions functions, and output functions with `TemporalAgent` by
  * Make `OpenRouterProvider` and `DeepSeekProvider` `__init__` overloads less restrictive by
  * Bump min version of griffe to `1.14.0` by


### v1.33.0 (2025-12-15)
#### What's Changed
  * Pass `s3://` file URLs directly to API in `BedrockConverseModel` by
  * Insert agent `instructions` after `system_prompt`s for models that don't natively support instructions by
  * Bump google-genai to 1.55 by
  * docs: Update mkdocstrings-python to 2.x and fix cross-reference paths by


#### New Contributors
### v1.32.0 (2025-12-12)
#### What's Changed
  * Add tool timeout support by
  * Let `TemporalAgent`s be registered to a Temporal workflow using `__pydantic_ai_agents__` field by
  * Make `end_strategy` also work for output tools, not just tools by
  * Replace OTel events with logs by
  * Fix `UIAdapter.dispatch_request` typing by


#### New Contributors
### v1.31.0 (2025-12-11)
#### What's Changed
  * Add prompt caching support for AWS Bedrock by
  * Add `Agent.output_json_schema()` method by
  * Allow custom `clientInfo` when connecting to MCP servers by
  * Add `provider_url` to `ModelResponse` and use it in `cost()` by
  * Add GPT-5.2 and bump openai to v2.11.0 by
  * Allow model to be a string in `LLMJudge` by
  * Fix `OpenAIResponsesModel` web search `find_in_page` action handling by


#### New Contributors
### v1.30.1 (2025-12-11)
#### What's Changed
  * Restore compatibility with `openai` v1 by
  * Temporarily revert support for OpenAI prompt caching options (
    * This feature will return in v1.31.0


### v1.30.0 (2025-12-10)
#### What's Changed
  * Add prompt caching options to OpenAIChatModelSettings by
  * Support multi-modal output in `LLMJudge` by
  * Add `CerebrasModel` by
  * Fix `GraphBuildingError` when using `g.stream` multiple times by
  * Fix `BedrockConverseModel` error when `ModelResponse.parts` is empty by
  * Pin deno to v2.5.x by


#### New Contributors
### v1.29.0 (2025-12-09)
#### What's Changed
  * Add support for aspect ratio in Gemini image generation by
  * Pass `container_id` back to Anthropic API by
  * Upgrade temporalio to 1.20.0 by
  * Fix error when OpenRouter response includes file annotations by
  * Suppress broken resource errors if cancelling by
  * Fix GoogleModel thinking signature not stored on tool calls when streaming by
  * Don't require `anthropic` dependency when using Anthropic model with other provider by


#### New Contributors
### v1.28.0 (2025-12-08)
#### What's Changed
  * Adds native structured output support for `claude-haiku-4-5` by
  * Support `us-gov.` and other multi-character Bedrock geo prefixes by
  * Allow missing content in streamed OpenRouter reasoning details by
  * Remove typings stubs by


#### New Contributors
### v1.27.0 (2025-12-04)
#### What's Changed
  * feat: Allow dynamic configuration of built-in tools via RunContext by
  * Support tool and resource caching for MCP servers that support change notifications by
  * Support raw CoT reasoning from LM Studio and other OpenAI Responses-compatible APIs by
  * Fix structured output with nested definitions with Gemini via OpenRouter by
  * fix: Copy `extra_headers` to allow `model_settings` reuse by
  * Add `VercelAIAdapter.dump_messages` to convert Pydantic AI messages to Vercel AI messages by
  * Disable use of `tool_choice=required` for deepseek-reasoner by
  * Use custom reasoning field for OpenRouter by


#### New Contributors
### v1.26.0 (2025-12-02)
#### What's Changed
  * Support JSON object output for Deepseek provider by
  * Clarify `FallbackModel` behavior on `ValidationError`s by
  * Add latest Grok (xAI) models by
  * Automatically omit TTL from `cache_control` when `AnthropicModel` is used with Bedrock client by
  * Add custom reasoning field support to OpenAI model profiles by
  * Add `gateway/...:...` to Known Model Names by


#### New Contributors
### v1.25.1 (2025-11-28)
#### What's Changed
  * Make `FastMCPToolset` work with DBOS by
  * Fix `OpenRouterModel` error when `native_finish_reason` is `None` by
  * Fix error when OpenRouter API returns `None` tool call arguments by


#### New Contributors
### v1.25.0 (2025-11-27)
#### What's Changed
  * Support `gemini-3-pro-image-preview` with Nano Banana Pro by
  * Return tool error to Google in 'error' key by


### v1.24.0 (2025-11-26)
#### What's Changed
  * Support native JSON output and strict tool calls for Anthropic by
  * Support Pydantic validation context by
  * Support logprobs output from Responses API by
  * Support instructions-only agent run with `OpenAIResponsesModel` by
  * Enable `PLW1514` rule (use `utf-8` encoding) by
  * Replace direct `_model_name` access with `model_name` property in OpenAI models and streamed responses by
  * Update docs on multi-modal file URLs being downloaded or sent directly by


#### New Contributors
### v1.23.0 (2025-11-25)
#### What's Changed
  * Add Anthropic built-in `WebFetchTool` support by
  * Allow `user_prompt` in HITL by
  * Add `anthropic_cache_messages` model setting and automatically strip cache points over the limit by
  * Add Gemini 3 Pro support to `OpenRouterModel` by
  * Ensure `openrouter_reasoning` model setting is sent to API by
  * Don't close custom httpx client provided to `MCPServerHTTP` by
  * Fix double counting of request tokens in evals by
  * Fix `pydantic_graph.beta.GraphRun` `GeneratorExit` handling by
  * Add test to ensure we allow message history starting with assistant message (model response) by
  * Remove `README.md` from wheel for `pydantic-ai` by
  * Upgrade `Ruff` to v0.14.6 by
  * Use `model_name` property in `OpenAIChatModel` chat completion create request by
  * Pin `huggingface-hub` to `<1` by
  * Add docs examples to use the Gateway aside from the `gateway/<provider>:<model>` shorthand by


#### New Contributors
### v1.22.0 (2025-11-21)
#### What's Changed
  * Add OpenRouterModel as OpenAIChatModel subclass with additional feature support by
  * Make `FallbackModel` fall back on all model API errors, not just HTTP status 400+ by
  * Don't skip model request when history ends on response but there are new instructions by
  * Revert "feat: enforce message history starts with user message" by
  * Don't send Google messages with 0 parts by
  * Immediately raise error when response is empty because of token limit by
  * Relax UserError into a warning when state deps is not provided with AG-UI by
  * Add type stubs for some third-party libraries by
  * Add document to allowed `cacheable_types` for anthropic by
  * Don't insert empty `ThinkingPart` when `Google` response ends in text with `thought_signature` by
  * Fix deprecated `GeminiModel` structured output and tool call thought signatures by


#### New Contributors
### v1.21.0 (2025-11-20)
#### What's Changed
  * Feature: MCP client Resources support by
  * Expose MCP server instructions in `MCPServer.instructions` property by
  * Add `BinaryContent.from_path` convenience method by
  * Enforce message history starts with user message by
  * Always strip Markdown fences from structured output by
  * Fix Gemini nested tool argument schemas by removing `title` from `$defs` by
  * Fix issue with Gemini and Prefect by removing unused `GoogleModel._url` by


#### New Contributors
### v1.20.0 (2025-11-18)
#### What's Changed
  * Add support for Gemini 3 Pro by
  * Support Gemini enhanced JSON Schema features by
  * Wrap `GoogleModel` `google.genai.errors.APIError` in `ModelHTTPError` so it works with `FallbackModel` by
  * fix: Change handling of empty state objects for AG-UI by
  * Adds `{ModelRequest,ModelResponse}.metadata` fields by
  * Make `RunContext.usage` available with Temporal by
  * Add `ttl` to `CachePoint` and Anthropic caching model settings by
  * Extract google model usage using genai-prices by
  * Update has_content method to check content data by


#### New Contributors
### v1.19.0 (2025-11-17)
#### What's Changed
  * Let `metadata` be passed to `CallDeferred` and `ApprovalRequired` exceptions and end up on `DeferredToolRequests` by
  * Add AnthropicModel `count_tokens` and support `UsageLimits.count_tokens_before_request` by
  * Fix bug with running graphs in temporal workflows by
  * Fix Gateway with Temporal by adding sniffio to sandbox passthrough modules by
  * Fix Gateway links in code blocks by


#### New Contributors
### v1.18.0 (2025-11-14)
#### What's Changed
  * Add Anthropic prompt caching support by
  * Bump `openai` to v2.8.0 (v1 still supported), add GPT-5.1 to known model names by
  * Bump `google-genai` to v1.50.1 and remove patches by
  * Bump `temporalio` to v1.19.0 and use `SimplePlugin` by


#### New Contributors
### v1.17.0 (2025-11-13)
#### What's Changed
  * Add [Pydantic AI Gateway](https://ai.pydantic.dev/gateway) docs by
  * Make `FastMCPToolset` work with `Temporal` by
  * Support `mcp.json` environment variable expansion in `load_mcp_servers()` by


#### New Contributors
### v1.16.0 (2025-11-13)
#### What's Changed
  * refactor(gateway): add `upstream_provider` back by


### v1.15.0 (2025-11-12)
#### What's Changed
  * Wrap `BedrockConverseModel` errors in `ModelHTTPError` to work well with `FallbackModel` by
  * Add unique `run_id` to run, run result, and message (request, response) classes by
  * Add `BedrockConverseModel.count_tokens` so it works with `UsageLimits.count_tokens_before_request` by


### v1.14.1 (2025-11-11)
#### What's Changed
  * Fix Vercel AI tool input/output always showing up as a JSON string rather than object by
  * Make `ModelRetry` hashable by
  * Don't run CI steps that require secrets on PRs from fork branch to fork `main` by


#### New Contributors
### v1.14.0 (2025-11-10)
#### What's Changed
  * Allow custom provider factory to be passed into `infer_model` by
  * Fix error when Google returns only empty text parts by
  * Docs: AWS Bedrock retry behavior by
  * docs: fix link to AG-UI Dojo by


#### New Contributors
### v1.13.0 (2025-11-10)
#### What's Changed
  * Ignore empty text parts in `GoogleModel` by
  * Add `AgentRun.{all,new}_messages{_json}` by
  * Update known models on Cerebras and Heroku by
  * feat(gateway): support `api_type` by
  * feat(gateway): support `profile` and `routing_group` by


#### New Contributors
### v1.12.0 (2025-11-06)
#### What's Changed
  * Fix tool call incorrectly being considered approved when agent run is resumed with history ending in unapproved tool call by
  * Bump `temporalio` to v1.18.2 as v1.18.0 is broken by
  * docs: Add Braintrust to integrations by


#### New Contributors
### v1.11.1 (2025-11-05)
#### What's Changed
  * `FallbackModel` support for Native output mode and `ModelProfile.default_structured_output_mode` by
  * Fix task cancellation bug in graph beta API triggered by using `MCPServerStreamableHTTP` with `agent.run_stream` by
  * Fix type annotation for `DuckDuckGoTool` with latest version of `ddgs` package by
  * Fix typo in docs variable name by


#### New Contributors
### v1.11.0 (2025-11-04)
#### What's Changed
  * Improve validation error retry message by
  * OpenAI gpt-5-chat does not support (encrypted) reasoning by
  * Complete thinking.md documentation with AWS Bedrock examples by
