  * Docs: add an example of using RunContext to pass data among tools by


#### New Contributors
### v0.4.10 (2025-07-30)
#### What's Changed
  * Fix parallel tool calling with tools returning ToolReturn with content by
  * Always enter Toolset context when running agent by
  * Add `priority` `service_tier` to `OpenAIModelSettings` and respect it in `OpenAIResponsesModel` by
  * Add HTTP Referer request header to Vercel AI Gateway provider by


#### New Contributors
### v0.4.9 (2025-07-28)
#### What's Changed
  * Ensure AG-UI state is isolated between requests by
  * Refine retry logic for parallel tool calling by
  * Fix AgentStream.stream_output and StreamedRunResult.stream_structured with output tools by
  * Allow `default` in tool schema with Gemini by


### v0.4.8 (2025-07-28)
#### What's Changed
  * Add tenacity utilities/integration for improved retry handling by
  * fix: close initialized MCP server if any MCP server fails to initialize by
  * Adding thinkingpart to otel_events in ModelResponse by
  * Fix: TypeError in MCPServerSSE due to improper initialization by
  * Fix: AG-UI assistant text and tool call order by


#### New Contributors
### v0.4.7 (2025-07-24)
#### What's Changed
  * Add MoonshotAI provider with Kimi-K2 model support by
  * Add Vercel AI Gateway provider by
  * Support passing files uploaded to Gemini Files API and setting custom media type by
  * Parse '' tags in streamed text as thinking parts by
  * Rename `MCPServer` `sse_read_timeout` to `read_timeout` and pass to `ClientSession` by
  * Update cohere and MCP, add support for MCP ResourceLink returned from tools by
  * Ignore empty text alongside tool calls when streaming from Ollama by
  * Ignore leading whitespace when streaming text, fixing run_stream + Ollama + Qwen3 by
  * Fix AG-UI parallel tool calls by
  * Fix initial tool call args not being streamed with AG-UI by
  * Handle `None` `created` timestamp coming from OpenRouter API by
  * Update MCP docs to show you can pass ssl options via the http_client arg by
  * Include ThinkingPart in messages.md API documentation graph by


#### New Contributors
### v0.4.6 (2025-07-23)
#### What's Changed
  * Enable URL and binary PDF for Mistral by
  * Fix pydantic-evals panel rendering with evaluators by
  * Fix mp3 handling by
  * Handle built-in tool errors better in tool registration by
  * fix: use `FileUrl.format` to find the extension by
  * Correct code snippet for native output by
  * chore: simplify output function call with model retry by
  * Reduce duplication between StreamedRunResult and AgentStream by
  * chore: add `CLAUDE.md` by
  * Speed up function `_estimate_string_tokens` by


#### New Contributors
### v0.4.5 (2025-07-22)
#### What's Changed
  * Add `async with self` in `agent_to_a2a` by
  * Fix include_content not working as expected by
  * Support streamable HTTP in mcp-run-python by
  * change `format_as_xml` defaults by
  * Fix LLMJudge input handling to preserve BinaryContent as separate message part instead of stringifying by
  * validate OpenAI responses by
  * Remove duplicate field on GeminiModelSettings by
  * Fix AG-UI shared state example by


#### New Contributors
### v0.4.4 (2025-07-18)
#### What's Changed
  * Add Toolsets and Deferred Tools by
  * Support AG-UI protocol for frontend-agent communication by
  * Add identifier field to BinaryContent class by
  * Add OpenAI models o1-pro, o3-pro, o3-deep-research, computer-use by
  * Add grok-4 and groq kimi-k2 models by
  * Remove old Google models by
  * Change clai default model to gpt-4.1 by
  * Fix VertexAI Empty Model Parts Error by
  * Remove incorrect tool call id from OpenAI tool call delta by
  * Speed up method `AgentRunResult._set_output_tool_return` by 18798% by
  * Speed up method `Usage.opentelemetry_attributes` by 85% by
  * Nicer errors under the capture_run_messages context by


#### New Contributors
### v0.4.3 (2025-07-16)
#### What's Changed
  * Include content.1571 by
  * `duckduckgo-search` is renamed to `ddgs` by
  * Add base64 encoding to `tool_return_ta` by
  * Bugfix: avoid race condition when refreshing google token by
  * feat: Add output function tracing by
  * Add Hugging Face as a provider by


#### New Contributors
### v0.4.2 (2025-07-10)
#### What's Changed
  * Let model `settings` be passed to model classes by
  * Add `StructuredDict` for structured outputs with custom JSON schema by
  * Handle DeepSeek reasoning_content in streamed responses by
  * Drop FastA2A from PydanticAI repository by
  * Fix type annotations for `Agent.iter()` by
  * Fix chat-app example doc - python code appear twice by
  * Speed up function `_ensure_decodeable` by 634% by


#### New Contributors
### v0.4.1 (2025-07-08)
#### What's Changed
  * Support evaluating sync tasks by
  * Upgrade a2a to spec v0.2.5 by
  * Drop FastA2A as PydanticAI dependency by


#### New Contributors
### v0.4.0 (2025-07-08)
#### What's Changed
  * BREAKING CHANGE: Make `EvaluationReport` and `ReportCase` into generic dataclasses by
  * Make `ToolDefinition.description` optional and fix Bedrock description handling by
  * Add all audio types supported by Gemini to AudioUrl by
  * Improve number_to_datetime performance by building TypeAdapter only once by
  * Retain defaults in non-strict openai schemas by


### v0.3.7 (2025-07-07)
#### What's Changed
  * Make `AgentStream.stream_output` (available inside `agent.iter`) stream validated output data instead of raising validation errors by
  * Add `model_request_stream_sync` to direct API by
  * Add GitHub Models provider by
  * Added support for google specific arguments for video analysis by
  * Implemented a convenient way to use ACPI.dev Tools in PydanticAI by
  * Fix list rendering in documentation by
  * Raise consistent deprecation warnings by
  * Move docstring warning of model settings as a comment by


#### New Contributors
### v0.3.6 (2025-07-04)
#### What's Changed
  * Deprecate `{FunctionToolCallEvent,FunctionToolResultEvent}.call_id` in favor of `tool_call_id` by
  * Indicate to the model that a `RetryPromptPart` not tied to a tool call contains validation feedback rather than a user message by
  * Update starlette subdomain in docs by
  * Update client.md - Typo by
  * Add support for predicted outputs in OpenAIModelSettings by
  * Record tool response in tool run span by
  * Use contextvars for agent overriding, rather than a local attribute by
  * Fix model parameters not being customized in fallback model request stream by
  * simplify weather example by


#### New Contributors
### v0.3.5 (2025-06-30)
#### What's Changed
  * Add progress bar on evaluate by
  * Fix deprecation warning under Pydantic 2.11 by
  * fix: async fixtures in conftest.py by
  * fix: docs examples python version in tests by
  * Set 'us-central1' by default on `GoogleProvider` by
  * Move `ThinkingPart` to preceed `TextPart` in `OpenAIResponsesModel` by
  * Fix deprecated kwargs validation to prevent silent failures by
  * Support strict mode in NativeOutput by
  * Let tools return ToolReturn to pass additional content to model, or attach metadata that's not passed to the model by
  * Add ability to include snippets in docs with inline-named sections for fragments and highlighting by
  * Add Slack Lead Qualifier example by


#### New Contributors
### v0.3.4 (2025-06-26)
#### What's Changed
  * Scrubbing sensitive content by
  * fix(anthropic): send `ThinkingPart` back when using tool calls by


#### New Contributors
### v0.3.3 (2025-06-24)
#### What's Changed
  * Support `NativeOutput` and `PromptedOutput` modes in addition to `ToolOutput` by
  * Improve Dynamic Instructions Documentation by
  * docs: add API reference to `UserPromptNode` by
  * Include additional usage fields from OpenAI-compatible APIs in usage details by
  * Fix: Handled and pretty-printed exceptions without exiting the CLI. by
  * document alternative otel backends by
  * note on self-hosting logfire by
  * Make Edge hashable by


#### New Contributors
### v0.3.2 (2025-06-21)
#### What's Changed
  * Support MCP sampling by


### v0.3.1 (2025-06-18)
#### What's Changed
  * Update Google models by
  * fix: update `ThinkingPart` when delta contains `signature` by


#### New Contributors
### v0.3.0 (2025-06-18)
#### Breaking Changes
See [###1142](https://ai.pydantic.dev/changelog/%5B#1142%5D\(https://github.com/pydantic/pydantic-ai/pull/1142\)) — Adds support for thinking parts.
We now convert the thinking blocks (`"<think>..."</think>"`) in provider specific text parts to PydanticAI `ThinkingPart`s. Also, as part of this release, we made the choice to not send back the `ThinkingPart`s to the provider - the idea is to save costs on behalf of the user. In the future, we intend to add a setting to customize this behavior.
* * *
#### What's Changed
  * Support Thinking part by


### v0.2.20 (2025-06-18)
#### What's Changed
  * Handle `McpError` from MCP tool calls by
  * Add `process_tool_call` hook to MCP servers to modify tool args, metadata, and return value by
  * Respect `ModelSettings.timeout` in `GoogleModel` by
  * feat: add `RunContext` support to history processors by


#### New Contributors
### v0.2.19 (2025-06-16)
#### What's Changed
  * Proper check if callable is async by
  * More flexible method infer_provider by
  * Ignore dynamic instructions returning an empty string by
  * uprev Pyodide to 0.27.6 by
  * refactor: updated tools doc with function naming: roll_die → roll_dice by
  * Set Anthropic `max_tokens` to 4096 by default by
  * feat: add `history_processors` parameter to `Agent` for message processing by
  * Yield events for unknown tool calls by
  * Always set a parameters schema on a Gemini function declaration, even when it's an empty object by


#### New Contributors
### v0.2.18 (2025-06-13)
#### What's Changed
  * Reuse last request from message history if no user prompt was provided by
  * Prevent Anthropic API errors from empty message content by
  * Add MCP Streamable HTTP implementation by
  * feat(openai): expose Responses API id as vendor_id by
  * Use `GoogleModel` instead of `GeminiModel` on inference by


#### New Contributors
### v0.2.17 (2025-06-12)
#### What's Changed
  * Add token usage metrics to `InstrumentedModel` by
  * Add `service_tier` to `OpenAIModelSettings` by
  * Allow users to supply `httpx.AsyncClient` in `MCPServerHTTP` by
  * Don't send sampling settings like `temperature` and `top_p` to OpenAI reasoning models by
  * Support field `fileData` (direct file URL) for `GeminiModel` and `GoogleModel` by


#### New Contributors
### v0.2.16 (2025-06-08)
#### What's Changed
  * Stop sharing tool retry count across all runs of the same agent by
  * Add support for `HerokuProvider` by
  * Add `stop_sequences` to Google models by
  * Handle model response timestamps in milliseconds rather than seconds by
  * Add convenience method to use LangChain community tools by
  * Infer the right type on output when callables are provided by
  * Revert pyodide to a version that doesn't print to stdout when installing packages by


#### New Contributors
### v0.2.15 (2025-06-05)
#### What's Changed
  * Allow empty messages when using `GoogleModel` by


### v0.2.14 (2025-06-03)
#### What's Changed
  * Temporarily revert "Add support for MCP's Streamable HTTP transport (###1716)" by


### v0.2.13 (2025-06-03)
#### What's Changed
  * Make parallel_evaluation_example more robust by
  * Ensure tool call parts with custom argument model validation errors are serializable by
  * Add option to pass expected output to LLMJudge by
  * Fix unexpected part error when Google model returns empty text delta by
  * Generate ToolCallPart.tool_call_id when OpenAI-compatible API returned an empty string by
  * docs: Fix import for BaseModel in graph example code by
  * Add new _GeminiThoughtPart to adhere to Gemini response by


#### New Contributors
### v0.2.12 (2025-05-29)
#### What's Changed
  * Add `vendor_id` and `vendor_details.finish_reason` to Gemini/Google model responses by
  * Fix units of `sse_read_timeout` `timedelta` by
  * Support functions as `output_type`, as well as lists of functions and other types by
  * Enhance Gemini usage tracking to collect comprehensive token data by
  * docs: add scope when loading credentials from file in google by
  * Add support for Claude 4 Sonnet and Opus models in Bedrock by
  * Add `ModelProfile` to let model-specific behaviors be configured independent of the model class by
  * Add new provider classes for Together AI, Fireworks AI, and Grok with automatic model profile selection by
  * Fix weather agent example with UI by


#### New Contributors
### v0.2.11 (2025-05-27)
#### What's Changed
  * Require `mcp>=1.9.0` on the `pydantic-ai-slim[mcp]` extra by
  * Don't send empty messages to Anthropic by


#### New Contributors
### v0.2.10 (2025-05-27)
#### What's Changed
  * Update Google models by
  * Support Claude Sonnet 4 by
  * Add support for MCP's Streamable HTTP transport by
  * Timeout for initializing MCP client by


#### New Contributors
### v0.2.9 (2025-05-26)
#### What's Changed
  * Cast non-textual responses in `Agent.to_cli` to `str` by
  * Support field `labels` for `GeminiModel` and `GoogleModel` on Vertex AI by


#### New Contributors
### v0.2.8 (2025-05-25)
#### What's Changed
  * Improve assertion on Anthropic by


### v0.2.7 (2025-05-24)
#### What's Changed
  * Support streaming tool calls from models that pass args as None when there are no function parameters by
  * Stream tool calls and structured output from Anthropic as it's received instead of in one go by
  * Remove hardcoded `n` parameter from OpenAIModel requests by
  * Add `tool_prefix` option to MCP servers and error on conflicting tool names by
  * Allow `RunContext` to not be documented when `require_parameter_descriptions=True` as it's not passed to the model anyway by
  * Clean up dataclasses reprs by
  * Addition: Make `prog_name` customizable by
  * Use `AsyncBeta` instead of `AsyncAnthropic` by


#### New Contributors
### v0.2.6 (2025-05-20)
#### What's Changed
  * Add `prepare_tools` param to Agent class by
  * fix: remove forgotten print on `GoogleModel` by
  * fasta2a: be more strict on agent card by
  * fix: rename `prepare_tools` to `_prepare_tools` by
  * fix: create prompt history file when using `Agent.to_cli()` by
  * fix: add `'openrouter'` string to `OpenAIModel` provider param by


#### New Contributors
### v0.2.5 (2025-05-20)
#### What's Changed
  * fasta2a: make `capabilities` required on `AgentCard` by
  * Fix formatting of ints in eval reports by
  * Bugfix: record instructions properly on agent run span when using structured output by
  * Add ability to specify the evaluation name for all provided Evaluators by
  * Add `include_binary_content` flag to `InstrumentationSettings`, rename OTel attribute key from `content` to `binary_content` for `BinaryPart`s by
  * Add logprobs to OpenAI model settings and response by
  * Added `vendor_id` to the model response. by
  * Fix ImportError when opentelemetry is not installed by
  * Add licenses to all packages. by
  * Add OpenRouter provider by
  * Add Google GenAI provider by


#### New Contributors
### v0.2.4 (2025-05-14)
#### What's Changed
  * `clai` should not require `OPENAI_API_KEY` by


#### New Contributors
### v0.2.3 (2025-05-13)
#### What's Changed
  * cli: add current path to `sys.path` by
  * evals: use the correct render object on `include_metadata` and `include_expected_output` by
  * Add A2A server by
  * Allow definition of Model Settings for LLMJudge by
  * improve messages coverage by
  * Add `direct` public API by
  * Ensure CLI prompt history directory and file exist before usage by


#### New Contributors
### v0.2.2 (2025-05-13)
#### What's Changed
  * Add `to_cli()` method to `Agent` by


#### New Contributors
### v0.2.1 (2025-05-13)
#### What's Changed
  * Add AWS Profile Feature by
  * Change Agent.is_?_node() to use TypeIs instead by
  * Add newline separation between Anthropic system prompts by
  * cli: store prompt and config under `~/.pydantic-ai` by
  * otel: send `BinaryContent` information by


#### New Contributors
### v0.2.0 (2025-05-12)
#### Breaking Changes
See [###1647](https://ai.pydantic.dev/changelog/%5B#1647%5D\(https://github.com/pydantic/pydantic-ai/pull/1647\)) — usage makes sense as part of `ModelResponse`, and could be really useful in "messages" (really a sequence of requests and response). In this PR:
  * Adds `usage` to `ModelResponse` (field has a default factory of `Usage()` so it'll work to load data that doesn't have usage)
  * changes the return type of `Model.request` to just `ModelResponse` instead of `tuple[ModelResponse, Usage]`


#### Other Changes
  * Add support for non-string enums in Gemini by
  * Fix parallel tool calls on Bedrock with Nova and Claude models by
  * Fix Anthropic streaming by
  * Fix serializability of ModelRequestParameters by
  * Stop incorrectly treating side-by-side JSON schema $refs as recursion by
  * Set `ToolCallPartDelta.tool_call_id` when known from previous delta by


#### New Contributors
### v0.1.11 (2025-05-10)
#### What's Changed
  * Switch CLI to `clai` by


### v0.1.10 (2025-05-06)
#### What's Changed
  * Allow setting `temperature` to 0 on `BedrockConverseModel` by
  * Add `extra_headers` to `ModelSettings` by
  * Add `thinking_config` to `GeminiModel` by


#### New Contributors
### v0.1.9 (2025-05-02)
#### What's Changed
  * Use the correct discriminator string in `HandleResponseEvent` by
  * Handle multi-modal and error responses from MCP tool calls by
  * Store additional usage details from Anthropic by
  * Add `base_url` to Mistral Provider by


#### New Contributors
### v0.1.8 (2025-04-28)
#### What's Changed
  * Support returning multi-modal content from tools by


### v0.1.7 (2025-04-28)
#### What's Changed
  * Allow multiple instructions and fix instruction concatenation in Agent by
  * Fix OpenAI AudioUrl by
  * Gemini Video Support by
  * Set `use_attribute_docstrings=True` by default on tools by
  * Copy context to new thread for sync tool calls by
  * Record agent run attributes in case of streaming and exception by


#### New Contributors
### v0.1.6 (2025-04-25)
#### What's Changed
  * otel: send `AudioUrl`, `VideoUrl`, `DocumentUrl` and `ImageUrl` information by


### v0.1.5 (2025-04-25)
#### What's Changed
  * Drop `requests` minimum version to 2.32.2 by


### v0.1.4 (2025-04-24)
#### What's Changed
  * Use `report_case_name` in span by
  * Make agent and graph runs serializable again by
  * support MCP logging, increase minimum mcp version to 1.6.0 by
  * Add support for o3 and o4-mini by
  * OpenAI: Enable DocumentUrl and BinaryContent documents by
  * gemini: move `list` type inside the `Annotated` on `function_declarations` field by
  * Replaced incorrect all_message() with new_messages() by


#### New Contributors
### v0.1.3 (2025-04-18)
#### What's Changed
  * Return last text parts on empty message by
  * move `prepare_env.py` to Python file in `mcp-run-python` by
  * Don't set non-recording span as current by
  * opentelemetry: add span event for `instructions` by
  * Add `extra_body` to `ModelSettings` by
  * Do not raise an error when no results are found by
  * Add support for gemini-2.5-flash-preview-04-17 by
  * fix: allow multiple `BinaryContent` in `message_history` by
  * fix: handle empty args for ToolCallPart by


#### New Contributors
### v0.1.2 (2025-04-17)
#### What's Changed
  * Fix max length handling by
  * Do a better job of inferring openai strict mode by
  * Properly validate serialized messages with `BinaryContent` by decoding `base64` by
  * Expose the `StdioServerParameters.cwd` param by


#### New Contributors
### v0.1.1 (2025-04-16)
#### What's Changed
  * fix: Allow empty tool call args by
  * fix: add instructions on further requests besides `UserPromptNode` by
  * Fix handling of `additionalProperties` by gemini by


### v0.1.0 (2025-04-15)
#### What's Changed
  * feat(bedrock): add VideoUrl input for `BedrockConverseModel` by
  * Add spans as an attribute on agent/graph runs/runresults by
  * BREAKING CHANGE: rename `result` -> `output` by
  * Bugfix: ensure parameters are customized when making streaming requests by
  * Customize the parameters as appropriate for the model when using fallback model by
  * Update min openai version by
  * feat(`BedrockConverseModel`): add additional configuration fields to Bedrock Runtime API by
  * Add support for `gemini-2.5-pro-preview-03-25` model (paid version of gemini 2.5 pro) by
  * BREAKING CHANGE (minor) move `format_as_xml` by
  * Add Changelog by
  * Add `instructions` parameter by
  * Generalize the JSON schema transformations by
  * Switch gemini request to camelCase as required by API by


#### New Contributors
### v0.0.55 2025-04-09
#### What's Changed
  * Allow empty user_prompt in run_stream by
  * fix: infer azure provider and environment for key by
  * Fix bug with JSON schema generation when using InstrumentedModel by
  * Add PydanticAI User-Agent header by


#### New Contributors
### v0.0.54 2025-04-09
#### What's Changed
  * evals: error when opentelemetry-sdk is not installed by
  * bedrock: allow empty system prompt by
  * fix import for the bedrock model by
  * Yield initial node during Graph (and therefore Agent) iteration by
  * Make `user_prompt` optional by
  * Add `stop_sequences` to `ModelSettings` by


#### New Contributors
### v0.0.53 2025-04-07
#### What's Changed
  * Improve some error messages by
  * Improve serialization of LLMJudge and custom evaluators by
  * Use `handle_stream.stream_output()` in the CLI by
  * Feature/add openai strict mode by


#### New Contributors
### v0.0.52 2025-04-03
#### What's Changed
  * Add dependencies to evals by


### v0.0.51 2025-04-03
#### What's Changed
  * Match OpenAI models in strictness by
  * Switch `mcp-run-python` server to use deno by


### v0.0.50 2025-04-03
#### What's Changed
  * Fix some issues with non-serializable inputs in evals by
  * Add expected output to logfire attributes for the evals task span by
  * Drop `exclusiveMaximum`/`exclusiveMinimum` from Gemini by
  * Drop JSON schema url from schema on Gemini by
  * Add py.typed marker to pydantic_evals package by


#### New Contributors
### v0.0.49 2025-04-01
#### What's Changed
  * Add Gemini 2.5 pro and improve CLI by
  * Add OpenAI built-in tools by
  * Add `generate_summary` and `truncation` to `OpenAIResponsesModelSettings` by
  * Move imports to try-except block by
  * Don't download content on `ImageUrl` and `DocumentUrl` for Anthropic Models by


#### New Contributors
### v0.0.48 2025-03-31
#### What's Changed
  * Add OpenAI Responses API by
  * Add dynamic version on evals extras by


### v0.0.47 2025-03-31
#### What's Changed
  * Ensure model settings' prefixes are enforced by
  * Bump logfire by
  * improvements while playing with the CLI by
  * add span around tool calls by
  * Add `pydantic-evals` package by
  * remove "preparing model request params" span by
  * Clean up SpanQuery and related APIs by
  * Fix the default types of generic params to EvaluatorContext by
  * More otel cleanup for evals by
  * Clean up public evals API by
  * [Bugfix] Unknown tool called by agent will cause response 400 by
  * feat: Add read timeout and connect timeout for bedrock provider by
  * allow str as model, fix Groq models by
  * CLI fixes and improvements by
  * Allow use of `PYTHONOPTIMIZE=1` by
  * disable cohere with emscripten by


#### New Contributors
### v0.0.46
#### What's Changed
  * Use different HTTP clients based on providers by
  * Add `headers`, `timeout`, and `sse_read_timeout` to `MCPServerHTTP` by
  * Revert "Use `get_running_loop` instead of `get_event_loop`" by


#### New Contributors
### v0.0.45
#### What's Changed
  * Generate tool call id if not present by
  * add `user` mapping in openai chat completion by
  * Remove non-provider parameters from models by


#### New Contributors
### v0.0.44
#### What's Changed
  * Migrate OpenAI models away from `max_tokens` to `max_completion_tokens` by
  * Add return docstring to the function description by
  * Add `model_request_parameters` attribute (containing tool definitions) to chat spans by
  * Use `get_running_loop` instead of `get_event_loop` by
  * Bump openai to 1.66.0 by
  * Use `pydantic-ai-slim` version on CLI instead of `pydantic-ai` by
  * Drop `system` parameter from `OpenAIModel` by
  * Use provider on models inference by
  * Add cohere provider class by


#### New Contributors
### v0.0.43 2025-03-21
#### What's Changed
  * Add timestamp to `SystemPromptPart` by
  * Recreate access token on 401 for Google Vertex provider by


#### New Contributors
### v0.0.42 2025-03-19
#### What's Changed
  * Add support for MCP servers by
  * Make it possible to override JSON schema generation for tools by
  * MCP server to run Python code in a sandbox by
  * change api_key check flow by
  * require 3.12 for development by
  * improved MCP documentation by
  * rename `MCPServerSSE` to `MCPServerHTTP` and more docs by
  * uprev to 0.0.42 by


#### New Contributors
### v0.0.41 2025-03-17
#### What's Changed
  * Improve generic typehints in graph.py by
  * Fix span attributes when instrumenting FallbackModel streaming by
