  * Add Anthropic provider classes by
  * Add Mistral provider by


### v0.0.40 2025-03-15
#### What's Changed
  * Update `OpenAIProvider` to use environment variable for base URL by
  * Add `AzureProvider` by
  * State persistence by
  * `InstrumentedModel` and `FallbackModel` fixes by
  * Add PDF support to Anthropic by


#### New Contributors
### v0.0.39 2025-03-13
#### What's Changed
  * Add Groq provider classes by
  * fix: ModuleNotFoundError for mypy_boto3_bedrock_runtime by


#### New Contributors
### v0.0.38 2025-03-13
#### What's Changed
  * Fix instrumentation of FallbackModel by
  * Add `DocumentUrl` and support document via `BinaryContent` by


### v0.0.37 2025-03-12
#### What's Changed
  * Add `base_url` to models, populate `server.address` and `server.port` in spans by
  * Add support for pre-loaded VertexAI service account info by
  * Add support for specifying tool name when using decorator. by
  * Serialize bytes as base64 for JSON by


#### New Contributors
### v0.0.36 2025-03-07
#### What's Changed
  * Update regions url and VertexAIRegion Literal by
  * Add support for AWS Bedrock Converse API by


#### New Contributors
### v0.0.35 2025-03-05
This release only makes sure that `pydantic-ai-examples` have the right dependency versions.
### v0.0.34 2025-03-05
#### What's Changed
  * Add `Agent.instrument_all()` method to instrument all agents by default by
  * Add tool name to tool response events by
  * Add `pai` CLI by


### v0.0.33 2025-03-05
#### What's Changed
  * Make use of `typing-inspection` by
  * Add `Provider`s API by


### v0.0.32 2025-03-04
#### What's Changed
  * **Disable instrumentation by default** , add `instrument` param to `Agent`, use plain OpenTelemetry by
  * Add support for claude sonnet 3-7 by
  * Add support for `gemini-2.0-pro-exp-02-05` by
  * Misc instrumentation followups by


#### New Contributors
### v0.0.31 2025-03-03
#### What's Changed
  * Accept recursive objects in `return_type` by
  * Rename HandleResponseNode to CallToolsNode by
  * Make Graph.iter into an _async_ contextmanager by
  * Fix bug related to handling multiple result tools by
  * Replace `model request` span with `InstrumentedModel` by
  * Replace `all_messages` in agent span with `all_messages_events` in same format as `InstrumentedModel` span by


#### New Contributors
### v0.0.30 2025-02-27
#### What's Changed
  * Use `.iter()` API to fully replace existing streaming implementation by
  * Added gpt-4.5-preview support for OpenAIModel by
  * Add attributes mode to InstrumentedModel by
  * Support different content inputs in `TestModel` by


#### New Contributors
### v0.0.29 2025-02-27
#### What's Changed
  * Add `max_results` parameter to DuckDuckGo search tool by
  * Create a new event loop on each thread by


#### New Contributors
### v0.0.28 2025-02-27
#### What's Changed
  * Allow Anthropic Models to use more broad mime types for `ImageUrl` by
  * Add DuckDuckGoSearch tool by
  * Add tool_call_id to RunContext and update context replacement by
  * Add TavilySearch tool by


#### New Contributors
### v0.0.27 2025-02-26
#### What's Changed
  * Add `FallbackModel` support by
  * fix: send the right data format to gemini image input by


### v0.0.26 2025-02-25
#### What's Changed
  * Support multimodal inputs by
  * Fix agent graph types by


### v0.0.25 2025-02-24
#### What's Changed
  * Add `InstrumentedModel` by
  * Fix JSON streaming unicode issues with gemini by
  * Remove stale `name` methods from openai and mistral models by
  * Add placeholder API key for OpenAI compatible models by
  * Add `request_stream` to `InstrumentedModel` by
  * Add GraphRun object to make use of `next` more ergonomic by
  * Use raw OTel and actual event loggers in `InstrumentedModel` by
  * fix: anthropic parallel tool call results. by


#### New Contributors
### v0.0.24 2025-02-12
#### What's Changed
  * Remove now-invalid reference to graph extra from docs by
  * New gemini 2.0 models for production by
  * Remove `async` from` _get_model` by
  * Populate `ModelResponse.model_name` from responses by
  * Fix OpenAI Model for working with local Ollama without passing an API key by
  * Use abstract properties for otel semantic attributes on models and stream responses by


#### New Contributors
### v0.0.23 2025-02-07
#### What's Changed
  * Fix error in evals example by
  * Add `o3` support for `OpenAIModel` by
  * Remove the `AgentModel` class by
  * Support `reasoning_effort` param for `OpenAIModel` by
  * Fix OpenAI env var tests following by
  * Replace search UI with Algolia backed one by
  * Add support for gemini safety settings by
  * Fix: missing graph extra by
  * Remove unnecessary `project_id == creds_id` check for vertexai by
  * Using `model_name` and `system` model properties by


#### New Contributors
### v0.0.22 2025-02-04
#### What's Changed
  * Port `pydantic_ai.Agent` to using `pydantic_graph` by
  * PR previews by
  * Various docs improvements by
  * Adding new gemini experimental models by
  * Various minor fixes by
  * Build docs for python<3.12 by
  * Weather Agent Sample: Only include `tool_call_id` to chatbot.append if it's set by
  * Support locally served models which do not require an api key by


#### New Contributors
### v0.0.21 2025-01-30
#### What's Changed
  * Update index.md by
  * Add codespell support (config, workflow to detect/not fix) and make it fix few typos by
  * Ensure custom args are used when retried by
  * update `AgentDeps` refs to `AgentDepsT` by
  * Adding subclasses of `ModelSettings` to support specialized model requests by
  * Remove `_utils.Either` by
  * Remove ArgsDict and ArgsJson by
  * Fix typo in Google VertexAIModel documentation (mkdocs) by
  * Fix CI by removing references to shutdown groq models by
  * Updated Docs by
  * Clean up known model names by
  * Update Function tools docs with usage of `docstring_format` and `require_parameter_descriptions` by
  * Disable running gemini tests in test_live.py by
  * Update graph.md by
  * Minor clean up in preparation of graph agent by
  * Fix o1 usage with tool calls by
  * added documentation to visualize a graph within a jupyter-notebook by
  * Remove `OllamaModel` in favor of usage with `OpenAIModel` by
  * Docs fix: use model provider prefix in all examples by
  * Add `Cohere` docs and additional (live) tests by
  * uprev to 0.0.21 by


#### New Contributors
### v0.0.20 2025-01-23
#### What's Changed
  * Add missing `allow_model_requests` check by
  * Improve Algolia indexing by
  * Add support for Cohere models by
  * Add `model_name` to `ModelResponse` by
  * Adding `'deepseek-r1'` to the list of Ollama Model Names by
  * Test minimum versions by
  * Fix handling of OpenAI system prompts in order to support `o1` by
  * Removing `from_text` and `from_tool_call` utilities that complicate snapshot testing by
  * Add support for controlling direction of state diagram generated by Mermaid code by
  * Increase default `IsNow()` delta by
  * Auto-use the `set_event_loop` fixture by
  * Make non-required parameters not required by
  * Improve variance of classes by
  * Support `parallel_tool_calls` in `ModelSettings` by
  * Add support for `user` role system prompts `o1-preview-2024-09-12` by
  * Anthropic streaming support by
  * Fix an issue with retry counting by


#### New Contributors
### v0.0.19 2025-01-15
#### What's Changed
  * Docs: add `asyncio` to all examples that need it. by
  * fix: typo by
  * Add Gradio Demo for weather agent example by
  * Docs: fix freeze frame for gradio demo video by
  * Support `docstring_format` and `require_parameter_descriptions` on tools by
  * Generate llms.txt by
  * Refactor streaming by
  * Adds `phi4` to Ollama by
  * Use Algolia for docs search by
  * Fix agent `run`/ `run_sync` docs by
  * docs: fix typos in `testing-evals` and RAG example by
  * Graph Support by
  * Upgrade "inline-snapshot" by
  * uprev to v0.0.19 by


#### New Contributors
### v0.0.18 2025-01-07
#### What's Changed
  * Added docs contribution docs, a troubleshooting item for docs changes by
  * Improve null handling for Gemini by
  * Improve string format handling for gemini by
  * Suppress griffe logging related to return type by
  * readme links by
  * Docs: Add screenshot for chat-app example. by
  * docs: add OpenAI-compatible models section for Grok (xAI) and DeepSeek by
  * add diff coverage check by
  * set `UV_FROZEN` globally in CI by
  * Adds `dynamic` to `system_prompt` decorator, allowing reevaluation by
  * Use `--reinstall` instead of uninstall/install for docs insiders packages by
  * Custom `result_type` on a run by
  * Prefix all models with provider for consistency by
  * prepare for v0.0.18 by


#### New Contributors
### v0.0.17 2025-01-03
#### What's Changed
  * Multi-agent application documentation by
  * Added troubleshooting section to the docs page by
  * GCP VertexAI: pass explicit `scope` to `google.auth.default()` by
  * Docs fix - remove unnecessary line in multi agent docs by
  * Fix parallel Gemini function calls by
  * Add troubleshooting docs by
  * Docs fix - change to pydantic-ai.git on contributing page by
  * `AgentDeps` default to `None`. by
  * added support for formatting examples by
  * fix: update module name and include devtools as dev dependency for example scripts by
  * uprev to 0.0.17 by


#### New Contributors
### v0.0.16 2024-12-30
#### What's Changed
  * multi-agent usage by
  * support `X | None = None` with Gemini by
  * Link to diff in version warning by
  * fix docs icons by
  * Use Griffe's public API by
  * Clean `chat_app` example by
  * Gemini empty text by
  * correct chat app ordering by
  * Add Ollama API Key Configuration Support by
  * extend `RunContext` by
  * Make `capture_run_messages` support nested agent calls by
  * Ensure `TestModel` handles result retries correctly by
  * uprev to v0.0.16 by


#### New Contributors
### v0.0.15 2024-12-23
#### What's Changed
  * docs: fix typo in pydantic link for /api/models/gemini/ by
  * Prioritize tool calls over eager text responses by
  * add a default to `ResultData`, some related cleanup by
  * Fix typo in type checking note by
  * docs: fix typo in `Agents` page by
  * Adding commentary and tests re heterogeneous behavior by
  * fix settings docs formatting by
  * Add warning about being ahead of release by
  * Reorganize examples by
  * tweak warning rendering by
  * Remove `last_run_messages`, add `capture_run_messages` by
  * Mistral optimised by
  * prepare for v0.0.15 by


#### New Contributors
### v0.0.14 2024-12-19
#### What's Changed
  * Fix `ModelMessage` discriminator in chat_app example by
  * Ignore empty text parts by
  * Rename `Cost` to `Usage` by
  * Add support for usage limits by
  * Fix error when getting messages from DB in chat_app example by
  * Docs: add grids, tables to make intro info easier to digest by
  * Add `openai:o1` model support by
  * Use `RunContext` more widely by
  * Make args handling more robust by


#### New Contributors
### v0.0.13 2024-12-16
#### Breaking changes
All releases prior to V1 can contain breaking changes according to
  * The format of [messages](https://ai.pydantic.dev/api/messages/) has changed significantly since the last release, see
  * more messages/parts are added that before as a result of adding [`ToolReturnPart`](https://ai.pydantic.dev/api/messages/###pydantic_ai.messages.ToolReturnPart) for each tool call, see
  * given how much we've changed since the last release, other things have probably changed along the way


#### What's Changed
  * Minor docs updates by
  * use sqlite for chat_app example by
  * Rename tool_id to tool_call_id by
  * update docs to include remote server example by
  * Add new llama-3.3-70b-versatile to GroqModelName by
  * Documentation: minor spelling and phrasing fixes by
  * Adding a minimal contributing guide by
  * Add note about jupyter workaround for conflicting event loops by
  * Standardize "py" -> "python" in code blocks with pre-commit by
  * Add Anthropic (non-streaming) Support by
  * fix double anthropic reference by
  * Add support for new Gemini model 'gemini-2.0-flash-exp' by
  * Move description onto tool when appropriate by
  * fix formatting of `tests/test_tools.py` by
  * Move function tools docs to a new page by
  * added makefile help target by
  * [docs] update contributing guide to indicate minimum `uv` version by
  * Support tool calling when a structured result is provided by
  * Basic `ModelSettings` logic by
  * Unify model responses by
  * Disable pyright reportUnnecessaryIsInstance by
  * pin ollama action by
  * Mistral Support by
  * feat: add optional base_url kwarg to OpenAIModel by
  * Update install.md for Ollama by
  * live tests for mistral by
  * Change: Internal Discriminator Modification by
  * add model documentation by
  * Formatting nitpicks in `messages.py` by
  * Get chat app working with new messages format by
  * Use `defer_build` with type adapters, not custom `_LazyTypeAdapter` by
  * Use `isinstance` checks for message kinds by
  * add `messages` to `RunContext` by
  * Reformat messages so messages become simple `list[ModelRequest | ModelResponse]` by
  * Fix typo in agent documentation example by
  * Enhance Mistral: Improved Test Coverage, Code Optimization, and Bug Fixes by
  * Streamed response messages by
  * Fix doc error in ollama.md by
  * Alternative intro by
  * uprev to v0.0.13 by


#### New Contributors
### v0.0.12 2024-12-09
#### What's Changed
  * docs: update README.md by
  * Dynamic tools by
  * fix validation errors serialization by
  * add note to docs about `.stream_text(delta=True)` by
  * Generate tool results when using structured result by
  * fix `IndexError` when streaming `OpenAI` by
  * Ollama support by
  * add tests for Ollama by
  * uprev to v0.0.12 by


#### New Contributors
### v0.0.11 2024-12-06
#### What's Changed
  * fix agent name by


### v0.0.10 2024-12-06
#### What's Changed
  * Adding `Agent.name` by
  * Update `bank_support.py` -- fix docstring typo by
  * Add help page to docs by
  * uprev to v0.0.10, fix `logfire` optional group by


#### New Contributors
### v0.0.9 2024-12-04
#### What's Changed
  * readme improvements by
  * Fix typo: `nee` -> `need` by
  * Update README.md to make the comment fitted in screen by
  * add `.vscode/` to `.gitignore` by
  * fix formatting of api docs by
  * add missing popovers to evals by
  * Fix run sync by
  * allow adding tools via `Agent(tools_[...])` by
  * allow tools to return any by
  * uprev to 0.0.9 by


#### New Contributors
### v0.0.8 2024-12-02
#### What's Changed
  * stop ignoring some D linting errors by
  * Logfire docs by
  * add readme by


### v0.0.7 2024-11-29
#### What's Changed
  * fix numerous typos by
  * Rename `retriever` to `tool` by
  * fix broken links and add type checking function by
  * Install setup by
  * adding docs for testing and evals by
  * evals docs by
  * rename `CallContext` -> `RunContext` by
  * improvements to docs index by
  * test with `pydantic-ai-slim` only by
  * uprev to v0.0.7 by


### v0.0.6 2024-11-25
#### What's Changed
  * Fix docs CI? by
  * Add vertex AI by
  * add Groq client support by
  * fix `test-live` by
  * Support VertexAI models in `infer_model` by
  * Make openai optional by
  * Uv workspaces and `pydantic-ai-slim` by
  * uprev to v0.0.6 by


#### New Contributors
### v0.0.6a4 2024-11-25
### v0.0.5 2024-11-20
#### What's Changed
  * Change behaviour to behavior by
  * More minor cleanup by
  * adding whale video by
  * support Pydantic v2.10 by


### v0.0.4 2024-11-19
#### What's Changed
  * tweak agent docs by
  * tweaking index and other docs by
  * install improvements by
  * rename `retriever_context` -> `retriever` by
  * Decorator signatures by
  * Index improvements by
  * Replace dice diagram svgs with mermaid by
  * Result docs by
  * coverage badge and uprev by


### v0.0.3 2024-11-19
#### What's Changed
  * uprev uv and distribute examples by
  * chat app example by
  * rename and split `shared.py` by
  * tweak chat app by
  * Streamed responses by
  * Stream improvements by
  * Rename `ToolCall` to `Structured` in most places by
  * Remove agent error by
  * revert to `ResultData`, rename method/attributes appropriately by
  * Documentation by
  * further docs improvements by
  * remove `Either` from `_handle_model_response` and `_handle_streamed_model_response` by
  * Change `Agent` initialization to take deps type, not deps by
  * allow overriding deps, e.g. in testing by
  * Gemini coverage and other tweaks by
  * Docs insiders by
  * Examples in docs by
  * adding logo by
  * add docs stubs by
  * docs social cards and cleanup by
  * add streaming to chat app by
  * test against real models by
  * Better test functionality by
  * Smokeshow coverage by
  * Concepts docs by
  * Pytest examples by
  * Agent docs by
  * fix header images by
  * remove top menu by
  * Try to fix menu by
  * fixing agent docs and refactoring retriever return types by
  * add UA to requests by
  * Add back api docs by
  * New intro by


### v0.0.2 2024-10-30
#### What's Changed
  * Add timezones by
  * support `TypeAliasType` unions by


#### New Contributors
### v0.0.1 2024-10-29
initial release 🎉
© Pydantic Services Inc. 2024 to present
