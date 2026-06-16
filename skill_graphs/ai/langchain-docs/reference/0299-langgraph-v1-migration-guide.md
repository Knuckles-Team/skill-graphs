# LangGraph v1 migration guide
Source: https://docs.langchain.com/oss/python/migrate/langgraph-v1

This guide outlines changes in LangGraph v1 and how to migrate from previous versions. For a high-level overview of changes, see the [what's new](/oss/python/releases/langgraph-v1) page.

To upgrade:

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install -U langgraph langchain-core
  ```

  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv add langgraph langchain-core
  ```
</CodeGroup>

## Summary of changes

LangGraph v1 is largely backwards compatible with previous versions. The main change is the deprecation of [`create_react_agent`](https://reference.langchain.com/python/langchain-classic/agents/react/agent/create_react_agent) in favor of LangChain's new [`create_agent`](https://reference.langchain.com/python/langchain/agents/factory/create_agent) function.

## Deprecations

The following table lists all items deprecated in LangGraph v1:

| Deprecated item                            | Alternative                                                                                                                                                                                                                 |
| ------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `create_react_agent`                       | [`langchain.agents.create_agent`](https://reference.langchain.com/python/langchain/agents/factory/create_agent)                                                                                                             |
| `AgentState`                               | [`langchain.agents.AgentState`](https://reference.langchain.com/python/langchain/agents/middleware/types/AgentState)                                                                                                        |
| `AgentStatePydantic`                       | `langchain.agents.AgentState` (no more pydantic state)                                                                                                                                                                      |
| `AgentStateWithStructuredResponse`         | `langchain.agents.AgentState`                                                                                                                                                                                               |
| `AgentStateWithStructuredResponsePydantic` | `langchain.agents.AgentState` (no more pydantic state)                                                                                                                                                                      |
| `HumanInterruptConfig`                     | `langchain.agents.middleware.human_in_the_loop.InterruptOnConfig`                                                                                                                                                           |
| `ActionRequest`                            | `langchain.agents.middleware.human_in_the_loop.InterruptOnConfig`                                                                                                                                                           |
| `HumanInterrupt`                           | `langchain.agents.middleware.human_in_the_loop.HITLRequest`                                                                                                                                                                 |
| `ValidationNode`                           | Tools automatically validate input with [`create_agent`](https://reference.langchain.com/python/langchain/agents/factory/create_agent)                                                                                      |
| `MessageGraph`                             | [`StateGraph`](https://reference.langchain.com/python/langgraph/graph/state/StateGraph) with a `messages` key, like [`create_agent`](https://reference.langchain.com/python/langchain/agents/factory/create_agent) provides |

## `create_react_agent` → `create_agent`

LangGraph v1 deprecates the [`create_react_agent`](https://reference.langchain.com/python/langchain-classic/agents/react/agent/create_react_agent) prebuilt. Use LangChain's [`create_agent`](https://reference.langchain.com/python/langchain/agents/factory/create_agent), which runs on LangGraph and adds a flexible middleware system.

See the LangChain v1 docs for details:

* [Release notes](/oss/python/releases/langchain-v1#create_agent)
* [Migration guide](/oss/python/migrate/langchain-v1#migrate-to-create_agent)

<CodeGroup>
  ```python v1 (new) theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langchain.agents import create_agent

  agent = create_agent(  # [!code highlight]
      model,
      tools,
      system_prompt="You are a helpful assistant.",
  )
  ```

  ```python v0 (old) theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langgraph.prebuilt import create_react_agent

  agent = create_react_agent(  # [!code highlight]
      model,
      tools,
      prompt="You are a helpful assistant.",  # [!code highlight]
  )
  ```
</CodeGroup>

## Breaking changes

### Dropped Python 3.9 support

All LangChain packages now require **Python 3.10 or higher**. Python 3.9 reached [end of life](https://devguide.python.org/versions/) in October 2025.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/migrate/langgraph-v1.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Deep Agents
Source: https://docs.langchain.com/oss/python/reference/deepagents-python

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/reference/deepagents-python.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Integrations
Source: https://docs.langchain.com/oss/python/reference/integrations-python

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/reference/integrations-python.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# LangChain SDK
Source: https://docs.langchain.com/oss/python/reference/langchain-python

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/reference/langchain-python.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# LangGraph SDK
Source: https://docs.langchain.com/oss/python/reference/langgraph-python

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/reference/langgraph-python.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Reference
Source: https://docs.langchain.com/oss/python/reference/overview

Comprehensive API reference documentation for the LangChain and LangGraph Python and TypeScript libraries.

## Reference sites

<CardGroup>
  <Card title="Deep Agents" icon="https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/deep-agents-icon.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=1cc68f66a9e7550331cc0875f1ba53af" href="https://reference.langchain.com/python/deepagents">
    Build agents that can plan, use subagents, and leverage file systems for complex tasks.
  </Card>

  <Card title="LangChain" icon="https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/langchain-icon.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=663b30f85baf99ad708b97e05da2a5a4" href="https://reference.langchain.com/python/langchain">
    Complete API reference for LangChain Python, including chat models, tools, agents, and more.
  </Card>

  <Card title="LangGraph" icon="https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/langgraph-icon.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=b997e1a7487d507a36556eedbfd99f81" href="https://reference.langchain.com/python/langgraph">
    Complete API reference for LangGraph Python, including graph APIs, state management, checkpointing, and more.
  </Card>

  <Card title="LangChain Integrations" icon="plug" href="https://reference.langchain.com/python/integrations/overview">
    LangChain packages to connect with popular LLM providers, vector stores, tools, and other services.
  </Card>

  <Card title="MCP Adapter" icon="plug" href="https://reference.langchain.com/python/langchain_mcp_adapters/">
    Use Model Context Protocol (MCP) tools within LangChain and LangGraph applications.
  </Card>
</CardGroup>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/reference/overview.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Release policy
Source: https://docs.langchain.com/oss/python/release-policy

This page explains the LangChain and LangGraph release policies. Click on the tabs below to view the release policies for each:

<Tabs>
  <Tab title="LangChain">
    The LangChain ecosystem is composed of different component packages (e.g., `langchain-core`, `langchain`, partner packages, etc.)

    ## Release cadence

    With the release of LangChain 1.0, **minor** releases (e.g., from `1.0.x` to `1.1.0`) of `langchain` and `langchain-core` follow semantic versioning and may be released frequently. Minor releases contain new features and improvements but do not include breaking changes.

    Patch versions are released frequently, up to a few times per week, as they contain bug fixes and minor improvements.

    ## API stability

    The development of LLM applications is a rapidly evolving field, and we are constantly learning from our users and the community. As such, we expect that the APIs in `langchain` and `langchain-core` will continue to evolve to better serve the needs of our users.

    With LangChain 1.0's adoption of semantic versioning:

    * Breaking changes to the public API will only occur in major version releases (e.g., `2.0.0`)
    * Minor version bumps (e.g., `1.0.0` to `1.1.0`) add new features without breaking changes
    * Patch version bumps (e.g., `1.0.0` to `1.0.1`) contain bug fixes and minor improvements

    We will generally try to avoid making unnecessary changes, and will provide a deprecation policy for features that are being removed.

    ### Stability of other packages

    The stability of other packages in the LangChain ecosystem may vary:

    * **Partner packages maintained by LangChain** (such as `langchain-openai` and `langchain-anthropic`) follow semantic versioning and are expected to be stable post 1.0. Other partner packages may follow different stability and versioning policies, and users should refer to the documentation of those packages for more information.

    ## Deprecation policy

    We will generally avoid deprecating features until a better alternative is available.

    With LangChain 1.0's semantic versioning approach, deprecated features will continue to work throughout the entire 1.x release series. Breaking changes, including the removal of deprecated features, will only occur in major version releases (e.g., 2.0).

    When a feature is deprecated in `langchain` or `langchain-core`, we will:

    * Clearly mark it as deprecated in the code and documentation
    * Provide migration guidance to the recommended alternative
    * Provide security updates for the deprecated feature through all 1.x minor releases

    In some situations, we may allow deprecated features to remain in the code base even longer if they are not causing maintenance issues, to further reduce the burden on users.

    ## Long-term support (LTS)

    LangChain follows a long-term support (LTS) policy to provide stability for production applications:

    ### Release status definitions

    Packages are marked with one of the following statuses:

    * **ACTIVE**: Current active development, includes bug fixes, security patches, and new features
    * **MAINTENANCE**: Receives all security patches and critical bug fixes, but no new features

    ### Current LTS releases

    **LangChain 1.0** is designated as an LTS release:

    * **Status**: ACTIVE until the release of 2.0
    * **Support period**: After 2.0 is released, 1.0 will enter MAINTENANCE mode for at least 1 year
    * **Semver compliance**: Users can upgrade between minor versions (e.g., 1.0 to 1.1) without breaking changes

    ### Legacy version support

    **LangChain 0.3**:

    * **Status**: MAINTENANCE mode
    * **Support period**: Until December 2026
    * **Support includes**: Security patches and critical bug fixes
  </Tab>

  <Tab title="LangGraph">
    LangGraph follows a structured release policy to ensure stability and predictability for users building production applications.

    ## Release cadence

    We expect to space out **major** releases by at least 6-12 months to provide stability for production applications.

    **Minor** releases are typically released every 1-2 months with new features and improvements.

    **Patch** releases are released as needed, often weekly, to address bugs and security issues.

    ## API stability

    ### Stable APIs

    All APIs without special prefixes are considered stable and ready for production use. We maintain backward compatibility for stable features within a major version.

    ### Beta features

    Features marked as `beta` in the documentation are:

    * Feature-complete and tested
    * Safe for production use with the understanding they may change
    * Subject to minor API adjustments based on user feedback

    ### Experimental features

    Features marked as `experimental` or `alpha`:

    * Are under active development
    * May change significantly or be removed
    * Should be used with caution in production

    ### Internal APIs

    APIs prefixed with underscore (`_`) or explicitly marked as internal:

    * Are not part of the public API
    * May change without notice
    * Should not be used directly

    ## Deprecation policy

    When deprecating features:

    1. **Deprecation Notice**: Features are marked as deprecated with clear migration guidance
    2. **Grace Period**: Deprecated features remain functional for at least one minor version
    3. **Removal**: Features are removed only in major version releases
    4. **Migration Support**: We provide migration guides and, when possible, automated tools

    ## Platform compatibility

    ### Python support

    * We support Python versions that are actively maintained by the Python Software Foundation
    * Python version requirements may change only in major releases
    * Currently requires Python 3.10 or later

    ## Breaking changes

    Breaking changes are only introduced in major versions and include:

    * Removal of deprecated APIs
    * Changes to required parameters
    * Changes to default behavior that affect existing applications
    * Minimum Python/Node.js version updates

    ## Migration support

    For major version upgrades, we provide:

    * Comprehensive migration guides
    * Automated migration scripts when feasible
    * Extended support period for the previous major version
    * Clear documentation of all breaking changes

    ## Long-term support (LTS)

    LangGraph follows a long-term support (LTS) policy to provide stability for production applications:

    ### Release status definitions

    Packages are marked with one of the following statuses:

    * **ACTIVE**: Current active development, includes bug fixes, security patches, and new features
    * **MAINTENANCE**: Receives all security patches and critical bug fixes, but no new features

    ### Current LTS releases

    **LangGraph 1.0** is designated as an LTS release:

    * **Status**: ACTIVE until the release of 2.0
    * **Support period**: After 2.0 is released, 1.0 will enter MAINTENANCE mode for at least 1 year
    * **Semver compliance**: Users can upgrade between minor versions (e.g., 1.0 to 1.1) without breaking changes

    ### Legacy version support

    **LangGraph 0.4**:

    * **Status**: MAINTENANCE mode
    * **Support period**: Until December 2026
    * **Support includes**: All security patches and critical bug fixes

    ## See also

    * [Versioning](/oss/python/versioning) - Version numbering and support details
    * [Releases](/oss/python/releases) - Version-specific release notes and migration guides
  </Tab>

  <Tab title="Deep Agents">
    Deep Agents (`deepagents`) is a rapidly evolving package for building advanced agent architectures.

    ## Pre-1.0 status

    Deep Agents is currently in pre-1.0 development. While we minimize breaking changes when possible, the API may evolve as we incorporate learnings from the community and adapt to the rapidly changing landscape of agentic applications.

    ## Release cadence

    **Minor** releases (e.g., `0.1.0` to `0.2.0`) may contain new features and potentially breaking changes as the package matures.

    **Patch** releases (e.g., `0.1.0` to `0.1.1`) contain bug fixes and minor improvements without breaking changes.

    ## API stability

    As a pre-1.0 package:

    * APIs may change between minor versions
    * We aim to minimize disruption by providing clear migration guidance when changes occur
    * Features marked as `experimental` or `alpha` are subject to more significant changes

    ## Deprecation policy

    When deprecating features in Deep Agents:

    * We provide deprecation warnings in advance when possible
    * Migration guidance is included in release notes
    * Deprecated features are removed in subsequent minor releases

    ## Path to 1.0

    Deep Agents will reach 1.0 when:

    * Core APIs have stabilized based on community feedback
    * The package has been battle-tested in production environments
    * Breaking changes are no longer expected for core functionality

    After 1.0, Deep Agents will follow the same semantic versioning and LTS policies as LangChain and LangGraph.

    ## See also

    * [Versioning](/oss/python/versioning) - Version numbering and support details
  </Tab>
</Tabs>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/release-policy.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Changelog
Source: https://docs.langchain.com/oss/python/releases/changelog

Log of updates and improvements to our Python packages

<Callout icon="rss">
  **Subscribe**: Our changelog includes an [RSS feed](https://docs.langchain.com/oss/python/releases/changelog/rss.xml) that can integrate with [Slack](https://slack.com/help/articles/218688467-Add-RSS-feeds-to-Slack), [email](https://zapier.com/apps/email/integrations/rss/1441/send-new-rss-feed-entries-via-email), Discord bots like [Readybot](https://readybot.io/) or [RSS Feeds to Discord Bot](https://rss.app/en/bots/rssfeeds-discord-bot), and other subscription tools.
</Callout>

<Update label="May 12, 2026">
  ## `deepagents` v0.6.0

  * **[`CodeInterpreterMiddleware`](/oss/python/deepagents/interpreters)**: (experimental) `deepagents` now supports code execution and programmatic tool calling through a scoped QuickJS runtime.
  * Supports `version="v3"` in `stream_events` / `astream_events`. Refer to the [event streaming](/oss/python/deepagents/event-streaming) guide for details.
  * **[`DeltaChannel`](/oss/python/langgraph/pregel#deltachannel) (beta)** ([blog](https://www.langchain.com/blog/delta-channels-evolving-agent-runtime)): Deep Agents now uses `DeltaChannel` for message history and agent files. Rather than re-serializing the full accumulated value into every checkpoint, only the incremental delta written at each step is stored — keeping checkpoint sizes small as threads grow long.
  * **[Harness profiles](/oss/python/deepagents/profiles)**: Register per-provider or per-model configuration bundles (`HarnessProfile`) that `create_deep_agent` applies automatically when a model is selected — system-prompt tweaks, tool overrides, middleware changes, and subagent defaults — without modifying the call site.
  * **[`ContextHubBackend`](/oss/python/deepagents/backends#contexthubbackend)** ([blog](https://www.langchain.com/blog/introducing-context-hub)): A new filesystem backend backed by LangSmith Hub. Agent files — skills, memories, and other persisted context — are stored as Hub commits, giving you version history on every write and LangSmith-native durability without provisioning a separate LangGraph store.
</Update>

<Update label="May 12, 2026">
  ## `langchain` v1.3.0

  This release adds support for `version="v3"` in `stream_events` / `astream_events` for `langchain` agents. Refer to the [event streaming](/oss/python/langchain/event-streaming) guide for details.
</Update>

<Update label="May 12, 2026">
  ## `langgraph` v1.2.0

  This release adds finer-grained control over node execution (timeouts, error recovery, and graceful shutdown), a new channel type that cuts checkpoint overhead for long-running threads, and a new content-block-centric streaming API (v3) with typed, per-channel projections.

  * **[`DeltaChannel`](/oss/python/langgraph/pregel#deltachannel) (beta)**: A new channel type that stores only the incremental delta at each step rather than re-serializing the full accumulated value. Most useful for channels that grow large over time, for example a message list in a long-running thread. Use `snapshot_frequency=K` to write a full snapshot every K steps and bound read latency.

  * **[Per-node timeouts](/oss/python/langgraph/fault-tolerance#timeouts)**: Pass `timeout=` to [`add_node`](https://reference.langchain.com/python/langgraph/graph/state/StateGraph/add_node) to cap how long a single attempt may run. Set a hard wall-clock limit (`run_timeout`), an idle limit that resets on progress (`idle_timeout`), or both via [`TimeoutPolicy`](https://reference.langchain.com/python/langgraph/types/TimeoutPolicy). When the limit fires, LangGraph raises [`NodeTimeoutError`](https://reference.langchain.com/python/langgraph/errors/NodeTimeoutError), clears writes from that attempt, and hands off to the retry policy. Async nodes only.

  * **[Node-level error handlers](/oss/python/langgraph/fault-tolerance#error-handling)**: Pass `error_handler=` to [`add_node`](https://reference.langchain.com/python/langgraph/graph/state/StateGraph/add_node) to run a recovery function after all retries are exhausted. The handler receives a typed [`NodeError`](https://reference.langchain.com/python/langgraph/errors/NodeError) and can return a [`Command`](https://reference.langchain.com/python/langgraph/types/Command) to update state and route to a different node, useful for Saga/compensation patterns.

  * **[Graceful shutdown](/oss/python/langgraph/fault-tolerance#graceful-shutdown)**: Stop an in-flight run cooperatively after the current superstep completes, and save a resumable checkpoint. Create a [`RunControl`](https://reference.langchain.com/python/langgraph/runtime/RunControl) and call `request_drain()` from any thread; the run raises `GraphDrained` and can be resumed later with the same config.

  * **New event streaming API (beta)**: Pass `version="v3"` to `stream_events()` / `astream_events()` for a content-block-centric protocol with typed, per-channel projections (`run.values`, `run.messages`, `run.lifecycle`, `run.subgraphs`) plus opt-in transformers for updates, custom events, checkpoints, tasks, and debug. `run.messages` yields one `ChatModelStream` per LLM call with typed sub-projections for text, reasoning, tool calls, and usage. `version="v1"` and `version="v2"` are unchanged.

  Timeouts and error handlers are Python-only; retry policies continue to work in both Python and TypeScript.
</Update>

<Update label="Apr 7, 2026">
  ## `deepagents` v0.5.0

  * **[Async subagents](/oss/python/deepagents/async-subagents)**: Deep Agents can launch non-blocking background tasks, so users can continue interacting with the agent while subagents work concurrently. Requires [LangSmith Deployment](/langsmith/deployment) for sub-agents.

  * **Multi-modal support**: The `read_file` tool now supports PDFs, audio, and video files in addition to images.

  * **Backend changes**: We've made backward-compatible changes to the Deep Agents [backend protocol](https://github.com/langchain-ai/deepagents/blob/main/libs/deepagents/deepagents/backends/protocol.py):
    * Updated the file format stored in [State and Store backends](/oss/python/deepagents/backends) to support binary files.
    * Improved error propagation from backends to tools.
    * You can now instantiate `StateBackend()` and `StoreBackend()` directly. Specifying with a factory (e.g., `backend=(lambda rt: StateBackend(rt))`) is deprecated.

  * **Anthropic prompt caching improvements**: We've made some improvements to improve prompt caching performance for Anthropic models.
</Update>

<Update label="Mar 10, 2026">
  ## `langgraph` v1.1.0

  * **Type-safe streaming (`version="v2"`)**: Pass `version="v2"` to `stream()` / `astream()` for unified `StreamPart` output with `type`, `ns`, and `data` keys on every chunk. Each mode has its own `TypedDict`, all importable from `langgraph.types`. See [streaming docs](/oss/python/langgraph/streaming#stream-output-format-v2).

  * **Type-safe invoke (`version="v2"`)**: Pass `version="v2"` to `invoke()` / `ainvoke()` to get a `GraphOutput` object with `.value` and `.interrupts` attributes. See [invoke docs](/oss/python/langgraph/streaming#v2-invoke-format).

  * **Pydantic and dataclass coercion**: With `version="v2"`, `invoke()` and `values`-mode stream output are automatically coerced to your declared Pydantic model or dataclass type.

  * **Fixed time travel with interrupts and subgraphs**: Replays no longer reuse stale `RESUME` values, and subgraphs correctly restore the checkpoint for the parent's historical state.

  * **Fully backwards compatible**: `version="v2"` is opt-in. `GraphOutput` supports deprecated dict-style access for gradual migration.
</Update>

<Update label="Feb 10, 2026">
  ## `deepagents` v0.4.0

  * New integration packages for pluggable sandboxes: [`langchain-modal`](https://pypi.org/project/langchain-modal/), [`langchain-daytona`](https://pypi.org/project/langchain-daytona/), and [`langchain-runloop`](https://pypi.org/project/langchain-runloop/). See [sandboxes guide](/oss/python/deepagents/sandboxes) and example [data analysis tutorial](/oss/python/deepagents/data-analysis).
  * Changes to [conversation history summarization](/oss/python/deepagents/context-engineering#summarization):
    * Summarization now happens in the model node via `wrap_model_call` events. Due to this we retain the full message history in the graph state.
    * More accurate token counting.
    * Summarization will now automatically trigger if a chat model raises a [`ContextOverflowError`](https://reference.langchain.com/python/langchain-core/exceptions/ContextOverflowError) (defined in `langchain-core`). Currently `langchain-anthropic` and `langchain-openai` support this.
  * We now default to the Responses API for model strings prefixed with `"openai:"`.
    <Accordion title="Disable data retention with the Responses API">
      ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from langchain.chat_models import init_chat_model

      agent = create_deep_agent(
          model=init_chat_model(
              "openai:...",
              use_responses_api=True,
              store=False,
              include=["reasoning.encrypted_content"],
          )
      )
      ```
    </Accordion>
</Update>

<Update label="Dec 15, 2025">
  ## `langchain` v1.2.0

  * [`create_agent`](/oss/python/langchain/agents): Simplified support for provider-specific tool parameters and definitions via a new [`extras`](https://reference.langchain.com/python/langchain/tools/#langchain.tools.BaseTool.extras) attribute on [tools](/oss/python/langchain/tools). Examples:
    * Provider-specific configuration such as Anthropic's [programmatic tool calling](/oss/python/integrations/chat/anthropic#programmatic-tool-calling) and [tool search](/oss/python/integrations/chat/anthropic#tool-search).
    * Built-in tools that are executed client-side, as supported by [Anthropic](/oss/python/integrations/chat/anthropic#built-in-tools), [OpenAI](/oss/python/integrations/chat/openai#responses-api), and other providers.
  * Support for strict schema-adherence in agent `response_format` (see [`ProviderStrategy`](/oss/python/langchain/structured-output#provider-strategy) docs).
</Update>

<Update label="Dec 8, 2025">
  ## `langchain-google-genai` v4.0.0

  We've re-written the Google GenAI integration to use Google's consolidated Generative AI SDK, which provides access to the Gemini API and Vertex AI Platform under the same interface. This includes minimal breaking changes as well as deprecated packages in `langchain-google-vertexai`.

  See the full [release notes and migration guide](https://github.com/langchain-ai/langchain-google/discussions/1422) for details.
</Update>

<Update label="Nov 25, 2025">
  ## `langchain` v1.1.0

  * [Model profiles](/oss/python/langchain/models#model-profiles): Chat models now expose supported features and capabilities through a `.profile` attribute. These data are derived from [models.dev](https://models.dev), an open source project providing model capability data.
  * [Summarization middleware](/oss/python/langchain/middleware/built-in#summarization): Updated to support flexible trigger points using model profiles for context-aware summarization.
  * [Structured output](/oss/python/langchain/structured-output): `ProviderStrategy` support (native structured output) can now be inferred from model profiles.
  * [`SystemMessage` for `create_agent`](/oss/python/langchain/middleware/custom#dynamic-prompt): Support for passing `SystemMessage` instances directly to `create_agent`'s `system_prompt` parameter, enabling advanced features like cache control and structured content blocks.
  * [Model retry middleware](/oss/python/langchain/middleware/built-in#model-retry): New middleware for automatically retrying failed model calls with configurable exponential backoff.
  * [Content moderation middleware](/oss/python/integrations/middleware/openai#content-moderation): OpenAI content moderation middleware for detecting and handling unsafe content in agent interactions. Supports checking user input, model output, and tool results.
</Update>

<Update label="Oct 20, 2025">
  ## v1.0.0

  ### `langchain`

  * [Release notes](/oss/python/releases/langchain-v1)
  * [Migration guide](/oss/python/migrate/langchain-v1)

  ### `langgraph`

  * [Release notes](/oss/python/releases/langgraph-v1)
  * [Migration guide](/oss/python/migrate/langgraph-v1)

  <Callout icon="speakerphone">
    If you encounter any issues or have feedback, please [open an issue](https://github.com/langchain-ai/docs/issues/new?template=01-langchain.yml) so we can improve. To view v0.x documentation, [go to the archived content](https://github.com/langchain-ai/langchain/tree/v0.3/docs/docs) and [API reference](https://reference.langchain.com/v0.3/python/).
  </Callout>
</Update>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/releases/changelog.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# What's new in LangChain v1
Source: https://docs.langchain.com/oss/python/releases/langchain-v1

**LangChain v1 is a focused, production-ready foundation for building agents.** We've streamlined the framework around three core improvements:

<CardGroup>
  <Card title="create_agent" icon="robot" href="#create_agent">
    The new standard for building agents in LangChain, replacing `langgraph.prebuilt.create_react_agent`.
  </Card>

  <Card title="Standard content blocks" icon="cube" href="#standard-content-blocks">
    A new `content_blocks` property that provides unified access to modern LLM features across providers.
  </Card>

  <Card title="Simplified namespace" icon="sitemap" href="#simplified-package">
    The `langchain` namespace has been streamlined to focus on essential building blocks for agents, with legacy functionality moved to `langchain-classic`.
  </Card>
</CardGroup>

To upgrade,

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install -U langchain
  ```

  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv add langchain
  ```
</CodeGroup>

For a complete list of changes, see the [migration guide](/oss/python/migrate/langchain-v1).

## `create_agent`

[`create_agent`](https://reference.langchain.com/python/langchain/agents/factory/create_agent) is the standard way to build agents in LangChain 1.0. It provides a simpler interface than [`langgraph.prebuilt.create_react_agent`](https://reference.langchain.com/python/langchain-classic/agents/react/agent/create_react_agent) while offering greater customization potential by using [middleware](#middleware).

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain.agents import create_agent

agent = create_agent(
    model="claude-sonnet-4-6",
    tools=[search_web, analyze_data, send_email],
    system_prompt="You are a helpful research assistant."
)

result = agent.invoke({
    "messages": [
        {"role": "user", "content": "Research AI safety trends"}
    ]
})
```

Under the hood, [`create_agent`](https://reference.langchain.com/python/langchain/agents/factory/create_agent) is built on the basic agent loop -- calling a model, letting it choose tools to execute, and then finishing when it calls no more tools:

<div>
  <img alt="Core agent loop diagram" />
</div>

For more information, see [Agents](/oss/python/langchain/agents).

### Middleware

Middleware is the defining feature of [`create_agent`](https://reference.langchain.com/python/langchain/agents/factory/create_agent). It offers a highly customizable entry-point, raising the ceiling for what you can build.

Great agents require [context engineering](/oss/python/langchain/context-engineering): getting the right information to the model at the right time. Middleware helps you control dynamic prompts, conversation summarization, selective tool access, state management, and guardrails through a composable abstraction.

#### Prebuilt middleware

LangChain provides a few [prebuilt middlewares](/oss/python/langchain/middleware#built-in-middleware) for common patterns, including:

* [`PIIMiddleware`](https://reference.langchain.com/python/langchain/agents/middleware/pii/PIIMiddleware): Redact sensitive information before sending to the model
* [`SummarizationMiddleware`](https://reference.langchain.com/python/langchain/agents/middleware/summarization/SummarizationMiddleware): Condense conversation history when it gets too long
* [`HumanInTheLoopMiddleware`](https://reference.langchain.com/python/langchain/agents/middleware/human_in_the_loop/HumanInTheLoopMiddleware): Require approval for sensitive tool calls

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain.agents import create_agent
from langchain.agents.middleware import (
    PIIMiddleware,
    SummarizationMiddleware,
    HumanInTheLoopMiddleware
)

agent = create_agent(
    model="claude-sonnet-4-6",
    tools=[read_email, send_email],
    middleware=[
        PIIMiddleware("email", strategy="redact", apply_to_input=True),
        PIIMiddleware(
            "phone_number",
            detector=(
                r"(?:\+?\d{1,3}[\s.-]?)?"
                r"(?:\(?\d{2,4}\)?[\s.-]?)?"
                r"\d{3,4}[\s.-]?\d{4}"
			),
			strategy="block"
        ),
        SummarizationMiddleware(
            model="claude-sonnet-4-6",
            trigger={"tokens": 500}
        ),
        HumanInTheLoopMiddleware(
            interrupt_on={
                "send_email": {
                    "allowed_decisions": ["approve", "edit", "reject"]
                }
            }
        ),
    ]
)
```

#### Custom middleware

You can also build custom middleware to fit your needs. Middleware exposes hooks at each step in an agent's execution:

<div>
  <img alt="Middleware flow diagram" />
</div>

Build custom middleware by implementing any of these hooks on a subclass of the [`AgentMiddleware`](https://reference.langchain.com/python/langchain/agents/middleware/types/AgentMiddleware) class:

| Hook              | When it runs             | Use cases                               |
| ----------------- | ------------------------ | --------------------------------------- |
| `before_agent`    | Before calling the agent | Load memory, validate input             |
| `before_model`    | Before each LLM call     | Update prompts, trim messages           |
| `wrap_model_call` | Around each LLM call     | Intercept and modify requests/responses |
| `wrap_tool_call`  | Around each tool call    | Intercept and modify tool execution     |
| `after_model`     | After each LLM response  | Validate output, apply guardrails       |
| `after_agent`     | After agent completes    | Save results, cleanup                   |

Example custom middleware:

```python expandable theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from dataclasses import dataclass
from typing import Callable

from langchain_openai import ChatOpenAI

from langchain.agents.middleware import (
    AgentMiddleware,
    ModelRequest
)
from langchain.agents.middleware.types import ModelResponse

@dataclass
class Context:
    user_expertise: str = "beginner"

class ExpertiseBasedToolMiddleware(AgentMiddleware):
    def wrap_model_call(
        self,
        request: ModelRequest,
        handler: Callable[[ModelRequest], ModelResponse]
    ) -> ModelResponse:
        user_level = request.runtime.context.user_expertise

        if user_level == "expert":
            # More powerful model
            model = ChatOpenAI(model="gpt-5.5")
            tools = [advanced_search, data_analysis]
        else:
            # Less powerful model
            model = ChatOpenAI(model="gpt-5-nano")
            tools = [simple_search, basic_calculator]

        return handler(request.override(model=model, tools=tools))

agent = create_agent(
    model="claude-sonnet-4-6",
    tools=[
        simple_search,
        advanced_search,
        basic_calculator,
        data_analysis
    ],
    middleware=[ExpertiseBasedToolMiddleware()],
    context_schema=Context
)
```

For more information, see [the complete middleware guide](/oss/python/langchain/middleware).

### Built on LangGraph

Because [`create_agent`](https://reference.langchain.com/python/langchain/agents/factory/create_agent) is built on [LangGraph](/oss/python/langgraph), you automatically get built in support for long running and reliable agents via:

<CardGroup>
  <Card title="Persistence" icon="database">
    Conversations automatically persist across sessions with built-in checkpointing
  </Card>

  <Card title="Streaming" icon="droplet">
    Stream tokens, tool calls, and reasoning traces in real-time
  </Card>

  <Card title="Human-in-the-loop" icon="hand-stop">
    Pause agent execution for human approval before sensitive actions
  </Card>

  <Card title="Time travel" icon="history">
    Rewind conversations to any point and explore alternate paths and prompts
  </Card>
</CardGroup>

You don't need to learn LangGraph to use these features—they work out of the box.

### Structured output

[`create_agent`](https://reference.langchain.com/python/langchain/agents/factory/create_agent) has improved structured output generation:

* **Main loop integration**: Structured output is now generated in the main loop instead of requiring an additional LLM call
* **Structured output strategy**: Models can choose between calling tools or using provider-side structured output generation
* **Cost reduction**: Eliminates extra expense from additional LLM calls

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy
from pydantic import BaseModel

class Weather(BaseModel):
    temperature: float
    condition: str

def weather_tool(city: str) -> str:
    """Get the weather for a city."""
    return f"it's sunny and 70 degrees in {city}"

agent = create_agent(
    "gpt-5.4-mini",
    tools=[weather_tool],
    response_format=ToolStrategy(Weather)
)

result = agent.invoke({
    "messages": [{"role": "user", "content": "What's the weather in SF?"}]
})

print(repr(result["structured_response"]))

# results in `Weather(temperature=70.0, condition='sunny')`
```

**Error handling**: Control error handling via the `handle_errors` parameter to `ToolStrategy`:

* **Parsing errors**: Model generates data that doesn't match desired structure
* **Multiple tool calls**: Model generates 2+ tool calls for structured output schemas

***

## Standard content blocks

<Note>
  Content block support is currently only available for the following integrations:

  * [`langchain-anthropic`](https://pypi.org/project/langchain-anthropic/)
  * [`langchain-aws`](https://pypi.org/project/langchain-aws/)
  * [`langchain-openai`](https://pypi.org/project/langchain-openai/)
  * [`langchain-google-genai`](https://pypi.org/project/langchain-google-genai/)
  * [`langchain-ollama`](https://pypi.org/project/langchain-ollama/)

  Broader support for content blocks will be rolled out gradually across more providers.
</Note>

The new [`content_blocks`](https://reference.langchain.com/python/langchain-core/messages/base/BaseMessage) property introduces a standard representation for message content that works across providers:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_anthropic import ChatAnthropic

model = ChatAnthropic(model="claude-sonnet-4-6")
response = model.invoke("What's the capital of France?")
