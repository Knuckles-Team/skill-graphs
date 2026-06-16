# Unified access to content blocks
for block in response.content_blocks:
    if block["type"] == "reasoning":
        print(f"Model reasoning: {block['reasoning']}")
    elif block["type"] == "text":
        print(f"Response: {block['text']}")
    elif block["type"] == "tool_call":
        print(f"Tool call: {block['name']}({block['args']})")
```

### Benefits

* **Provider agnostic**: Access reasoning traces, citations, built-in tools (web search, code interpreters, etc.), and other features using the same API regardless of provider
* **Type safe**: Full type hints for all content block types
* **Backward compatible**: Standard content can be [loaded lazily](/oss/python/langchain/messages#standard-content-blocks), so there are no associated breaking changes

For more information, see our guide on [content blocks](/oss/python/langchain/messages#standard-content-blocks).

***

## Simplified package

LangChain v1 streamlines the [`langchain`](https://pypi.org/project/langchain/) package namespace to focus on essential building blocks for agents. The refined namespace exposes the most useful and relevant functionality:

### Namespace

| Module                                                                                | What's available                                                                                                                                                                                                            | Notes                                                                                       |
| ------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| [`langchain.agents`](https://reference.langchain.com/python/langchain/agents)         | [`create_agent`](https://reference.langchain.com/python/langchain/agents/factory/create_agent), [`AgentState`](https://reference.langchain.com/python/langchain/agents/middleware/types/AgentState)                         | Core agent creation functionality                                                           |
| [`langchain.messages`](https://reference.langchain.com/python/langchain/messages)     | Message types, [content blocks](https://reference.langchain.com/python/langchain-core/messages/content/ContentBlock), [`trim_messages`](https://reference.langchain.com/python/langchain-core/messages/utils/trim_messages) | Re-exported from [`langchain-core`](https://reference.langchain.com/python/langchain-core/) |
| [`langchain.tools`](https://reference.langchain.com/python/langchain/tools)           | [`@tool`](https://reference.langchain.com/python/langchain-core/tools/convert/tool), [`BaseTool`](https://reference.langchain.com/python/langchain-core/tools/base/BaseTool), injection helpers                             | Re-exported from [`langchain-core`](https://reference.langchain.com/python/langchain-core/) |
| [`langchain.chat_models`](https://reference.langchain.com/python/langchain/models)    | [`init_chat_model`](https://reference.langchain.com/python/langchain/chat_models/base/init_chat_model), [`BaseChatModel`](https://reference.langchain.com/python/langchain-core/language_models/chat_models/BaseChatModel)  | Unified model initialization                                                                |
| [`langchain.embeddings`](https://reference.langchain.com/python/langchain/embeddings) | [`Embeddings`](https://reference.langchain.com/python/langchain-core/embeddings/embeddings/Embeddings), [`init_embeddings`](https://reference.langchain.com/python/langchain/embeddings/base/init_embeddings)               | Embedding models                                                                            |

Most of these are re-exported from `langchain-core` for convenience, which gives you a focused API surface for building agents.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# Agent building
from langchain.agents import create_agent

# Messages and content
from langchain.messages import AIMessage, HumanMessage

# Tools
from langchain.tools import tool

# Model initialization
from langchain.chat_models import init_chat_model
from langchain.embeddings import init_embeddings
```

### `langchain-classic`

Legacy functionality has moved to [`langchain-classic`](https://pypi.org/project/langchain-classic) to keep the core packages lean and focused.

**What's in `langchain-classic`:**

* Legacy chains and chain implementations
* Retrievers (e.g. `MultiQueryRetriever` or anything from the previous `langchain.retrievers` module)
* The indexing API
* The hub module (for managing prompts programmatically)
* [`langchain-community`](https://pypi.org/project/langchain-community) exports
* Other deprecated functionality

If you use any of this functionality, install [`langchain-classic`](https://pypi.org/project/langchain-classic):

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install langchain-classic
  ```

  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv add langchain-classic
  ```
</CodeGroup>

Then update your imports:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain import ...  # [!code --]
from langchain_classic import ...  # [!code ++]

from langchain.chains import ...  # [!code --]
from langchain_classic.chains import ...  # [!code ++]

from langchain.retrievers import ...  # [!code --]
from langchain_classic.retrievers import ...  # [!code ++]

from langchain import hub  # [!code --]
from langchain_classic import hub  # [!code ++]
```

## Migration guide

See our [migration guide](/oss/python/migrate/langchain-v1) for help updating your code to LangChain v1.

## Reporting issues

Please report any issues discovered with 1.0 on [GitHub](https://github.com/langchain-ai/langchain/issues) using the `'v1'` [label](https://github.com/langchain-ai/langchain/issues?q=state%3Aopen%20label%3Av1).

## Additional resources

<CardGroup>
  <Card title="LangChain 1.0" icon="rocket" href="https://blog.langchain.com/langchain-langchain-1-0-alpha-releases/">
    Read the announcement
  </Card>

  <Card title="Middleware guide" icon="puzzle" href="https://blog.langchain.com/agent-middleware/">
    Deep dive into middleware
  </Card>

  <Card title="Agents Documentation" icon="book" href="/oss/python/langchain/agents">
    Full agent documentation
  </Card>

  <Card title="Message Content" icon="message" href="/oss/python/langchain/messages#message-content">
    New content blocks API
  </Card>

  <Card title="Migration guide" icon="arrows-exchange" href="/oss/python/migrate/langchain-v1">
    How to migrate to LangChain v1
  </Card>

  <Card title="GitHub" icon="brand-github" href="https://github.com/langchain-ai/langchain">
    Report issues or contribute
  </Card>
</CardGroup>

## See also

* [Versioning](/oss/python/versioning) – Understanding version numbers
* [Release policy](/oss/python/release-policy) – Detailed release policies

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/releases/langchain-v1.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# What's new in LangGraph v1
Source: https://docs.langchain.com/oss/python/releases/langgraph-v1

**LangGraph v1 is a stability-focused release for the agent runtime.** It keeps the core graph APIs and execution model unchanged, while refining type safety, docs, and developer ergonomics.

It's designed to work hand-in-hand with [LangChain v1](/oss/python/releases/langchain-v1) (whose `create_agent` is built on LangGraph) so you can start high-level and drop down to granular control when needed.

<CardGroup>
  <Card title="Stable core APIs" icon="sitemap">
    Graph primitives (state, nodes, edges) and the execution/runtime model are unchanged, making upgrades straightforward.
  </Card>

  <Card title="Reliability, by default" icon="database">
    Durable execution with checkpointing, persistence, streaming, and human-in-the-loop continues to be first-class.
  </Card>

  <Card title="Seamless with LangChain v1" icon="link">
    LangChain's `create_agent` runs on LangGraph. Use LangChain for a fast start; drop to LangGraph for custom orchestration.
  </Card>
</CardGroup>

To upgrade,

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install -U langgraph
  ```

  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv add langgraph
  ```
</CodeGroup>

## Deprecation of `create_react_agent`

The LangGraph [`create_react_agent`](https://reference.langchain.com/python/langchain-classic/agents/react/agent/create_react_agent) prebuilt has been deprecated in favor of LangChain's [`create_agent`](https://reference.langchain.com/python/langchain/agents/factory/create_agent). It provides a simpler interface, and offers greater customization potential through the introduction of middleware.

* For information on the new [`create_agent`](https://reference.langchain.com/python/langchain/agents/factory/create_agent) API, see the [LangChain v1 release notes](/oss/python/releases/langchain-v1#create_agent).
* For information on migrating from [`create_react_agent`](https://reference.langchain.com/python/langchain-classic/agents/react/agent/create_react_agent) to [`create_agent`](https://reference.langchain.com/python/langchain/agents/factory/create_agent), see the [LangChain v1 migration guide](/oss/python/migrate/langchain-v1#migrate-to-create_agent).

## Reporting issues

Please report any issues discovered with 1.0 on [GitHub](https://github.com/langchain-ai/langgraph/issues) using the [`'v1'` label](https://github.com/langchain-ai/langgraph/issues?q=state%3Aopen%20label%3Av1).

## Additional resources

<CardGroup>
  <Card title="LangGraph 1.0" icon="rocket" href="https://blog.langchain.com/langchain-langchain-1-0-alpha-releases/">
    Read the announcement
  </Card>

  <Card title="Overview" icon="book" href="/oss/python/langgraph/overview">
    What LangGraph is and when to use it
  </Card>

  <Card title="Graph API" icon="sitemap" href="/oss/python/langgraph/graph-api">
    Build graphs with state, nodes, and edges
  </Card>

  <Card title="LangChain Agents" icon="robot" href="/oss/python/langchain/agents">
    High-level agents built on LangGraph
  </Card>

  <Card title="Migration guide" icon="arrows-exchange" href="/oss/python/migrate/langgraph-v1">
    How to migrate to LangGraph v1
  </Card>

  <Card title="GitHub" icon="brand-github" href="https://github.com/langchain-ai/langgraph">
    Report issues or contribute
  </Card>
</CardGroup>

## See also

* [Versioning](/oss/python/versioning) – Understanding version numbers
* [Release policy](/oss/python/release-policy) – Detailed release policies

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/releases/langgraph-v1.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Security policy
Source: https://docs.langchain.com/oss/python/security-policy

LangChain has a large ecosystem of integrations with various external resources like local and remote file systems, APIs and databases. These integrations allow developers to create versatile applications that combine the power of LLMs with the ability to access, interact with and manipulate external resources.

## Best practices

When building such applications developers should remember to follow good security practices:

* [**Limit permissions**](https://en.wikipedia.org/wiki/Principle_of_least_privilege): Scope permissions specifically to the application's need. Granting broad or excessive permissions can introduce significant security vulnerabilities. To avoid such vulnerabilities, consider using read-only credentials, disallowing access to sensitive resources, using sandboxing techniques (such as running inside a container), specifying proxy configurations to control external requests, etc. as appropriate for your application.
* **Anticipate potential misuse**: Just as humans can err, so can Large Language Models (LLMs). Always assume that any system access or credentials may be used in any way allowed by the permissions they are assigned. For example, if a pair of database credentials allows deleting data, it's safest to assume that any LLM able to use those credentials may in fact delete data.
* [**Defense in depth**](https://en.wikipedia.org/wiki/Defense_in_depth_\(computing\)): No security technique is perfect. Fine-tuning and good chain design can reduce, but not eliminate, the odds that a Large Language Model (LLM) may make a mistake. It's best to combine multiple layered security approaches rather than relying on any single layer of defense to ensure security. For example: use both read-only permissions and sandboxing to ensure that LLMs are only able to access data that is explicitly meant for them to use.

Risks of not doing so include, but are not limited to:

* Data corruption or loss.
* Unauthorized access to confidential information.
* Compromised performance or availability of critical resources.

Example scenarios with mitigation strategies:

* A user may ask an agent with access to the file system to delete files that should not be deleted or read the content of files that contain sensitive information. To mitigate, limit the agent to only use a specific directory and only allow it to read or write files that are safe to read or write. Consider further sandboxing the agent by running it in a container.
* A user may ask an agent with write access to an external API to write malicious data to the API, or delete data from that API. To mitigate, give the agent read-only API keys, or limit it to only use endpoints that are already resistant to such misuse.
* A user may ask an agent with access to a database to drop a table or mutate the schema. To mitigate, scope the credentials to only the tables that the agent needs to access and consider issuing READ-ONLY credentials.

If you're building applications that access external resources like file systems, APIs
or databases, consider speaking with your company's security team to determine how to best
design and secure your applications.

## Reporting OSS vulnerabilities

Please report security vulnerabilities associated with the LangChain open source projects using the following process:

1. **Submit a security advisory** on the Security tab in the GitHubrepository where the vulnerability exists.
2. **Send an email** to `security@langchain.dev` notifying us that you've filed a security issue and which repository it was filed in.

Before reporting a vulnerability, please review the [Best Practices](#best-practices) above to understand what we consider to be a security vulnerability vs. developer responsibility.

### Bug bounty eligibility

We welcome security vulnerability reports for all LangChain libraries. However, we may offer ad hoc bug bounties only for vulnerabilities in the following packages:

* Core libraries owned and maintained by the LangChain team: `langchain-core`, `langchain` (v1), `langgraph`, and related checkpointer packages (or their JavaScript equivalents)
* Popular integrations maintained by the LangChain team (e.g., `langchain-openai`, `langchain-anthropic`, etc., or their JavaScript equivalents)

The vulnerability must be in the library code itself, not in example code or example applications.

We welcome reports for all other LangChain packages and will address valid security concerns, but bug bounties will not be awarded for packages outside this scope. This includes the archived `langchain-community`, which due to its community-driven nature is not eligible for bug bounties, though we will accept and address reports.

### Out-of-scope targets

The following are out-of-scope for security vulnerability reports:

* **langchain-experimental**: This archived repository is for experimental code and is not in scope for security reports (see [package warning](https://pypi.org/project/langchain-experimental/)).
* **Examples and example applications**: Example code and demo applications are not in scope for security reports.
* **Code documented with security notices**: This will be decided on a case-by-case basis, but likely will not be in scope as the code is already documented with guidelines for developers that should be followed for making their application secure.
* **LangSmith related repositories or APIs**: See [Reporting LangSmith Vulnerabilities](#reporting-langsmith-vulnerabilities) below.

## Reporting LangSmith vulnerabilities

Please report security vulnerabilities associated with LangSmith by email to `security@langchain.dev`.

* LangSmith site: [https://smith.langchain.com?utm\_source=docs\&utm\_medium=cta\&utm\_campaign=langsmith-signup\&utm\_content=oss-security-policy](https://smith.langchain.com)
* SDK client: [https://github.com/langchain-ai/langsmith-sdk](https://github.com/langchain-ai/langsmith-sdk)

### Other security concerns

For any other security concerns, please contact us at `security@langchain.dev`.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/security-policy.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Studio
Source: https://docs.langchain.com/oss/python/studio

Develop, run, and debug LangGraph agents in an interactive environment with LangSmith Studio.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/studio.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Versioning
Source: https://docs.langchain.com/oss/python/versioning

Our OSS version numbers follow the format: `MAJOR.MINOR.PATCH`, as defined by [Semantic Versioning](https://semver.org/).

* **Major**: Breaking API updates that require code changes.
* **Minor**: New features and improvements that maintain backward compatibility.
* **Patch**: Bug fixes and minor improvements.

For example:

* `1.0.0`: First stable release with production-ready APIs
* `1.1.0`: New features added in a backward-compatible manner
* `1.0.1`: Backward-compatible bug fixes

## API stability

We communicate the stability of our APIs as follows:

### Stable APIs

All APIs without special prefixes are considered stable and ready for production use. We maintain backward compatibility for stable features and only introduce breaking changes in major releases.

### Beta APIs

APIs marked as `beta` are feature-complete but may undergo minor changes based on user feedback. They are safe for production use but may require small adjustments in future releases.

### Alpha APIs

APIs marked as `alpha` are experimental and subject to significant changes. Use these with caution in production environments.

### Deprecated APIs

APIs marked as `deprecated` will be removed in future major releases. When possible, we specify the intended version of removal. To handle deprecations:

1. Switch to the recommended alternative API
2. Follow the migration guide (released alongside major releases)
3. Use automated migration tools when available

### Internal APIs

Certain APIs are explicitly marked as "internal" in a couple of ways:

* Some documentation refers to internals and mentions them as such. If the documentation says that something is internal, it may change.
* Functions, methods, and other objects prefixed by a leading underscore (**`_`**). This is the standard Python convention of indicating that something is private; if any method starts with a single **`_`**, it's an internal API.
  * **Exception:** Certain methods are prefixed with `_` , but do not contain an implementation. These methods are *meant* to be overridden by sub-classes that provide the implementation. Such methods are generally part of the **Public API** of LangChain.

## Release cycles

<AccordionGroup>
  <Accordion title="Major releases">
    Major releases (e.g., `1.0.0` → `2.0.0`) may include:

    * Breaking API changes
    * Removal of deprecated features
    * Significant architectural improvements

    We provide:

    * Detailed migration guides
    * Automated migration tools when possible
    * Extended support period for the previous major version
  </Accordion>

  <Accordion title="Minor releases">
    Minor releases (e.g., `1.0.0` → `1.1.0`) include:

    * New features and capabilities
    * Performance improvements
    * New optional parameters
    * Backward-compatible enhancements
  </Accordion>

  <Accordion title="Patch releases">
    Patch releases (e.g., `1.0.0` → `1.0.1`) include:

    * Bug fixes
    * Security updates
    * Documentation improvements
    * Performance optimizations without API changes
  </Accordion>
</AccordionGroup>

## Version support policy

* **Latest major version**: Full support with active development (ACTIVE status)
* **Previous major version**: Security updates and critical bug fixes for 12 months after the next major release (MAINTENANCE status)
* **Older versions**: Community support only

### Long-term support (LTS) releases

Both LangChain and LangGraph 1.0 are designated as LTS releases:

* Version 1.0 will remain in ACTIVE status until version 2.0 is released
* After version 2.0 is released, version 1.0 will enter MAINTENANCE mode for at least 1 year
* LTS releases follow semantic versioning (semver), allowing safe upgrades between minor versions
* Legacy versions (LangChain 0.3 and LangGraph 0.4) are in MAINTENANCE mode until December 2026

### Pre-1.0 packages

**Deep Agents** (`deepagents`) is a pre-1.0 package under active development. As a rapidly evolving package, the API may change between minor versions, though we minimize breaking changes when possible. Deep Agents will adopt the same LTS policies as LangChain and LangGraph after reaching version 1.0.

For detailed information about release status and support timelines, see the [Release policy](/oss/python/release-policy).

## Check your version

To check your installed version:

<CodeGroup>
  ```python LangChain theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import langchain_core
  print(langchain_core.__version__)
  ```

  ```python LangGraph theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import langgraph
  print(langgraph.__version__)
  ```
</CodeGroup>

## Upgrade

<CodeGroup>
  ```bash LangChain theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  # Upgrade to the latest version
  pip install -U langchain-core langchain

  # Upgrade to a specific version
  pip install langchain-core==1.0.0
  ```

  ```bash LangGraph theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  # Upgrade to the latest version
  pip install -U langgraph

  # Upgrade to a specific version
  pip install langgraph==1.0.0
  ```

  ```bash Deep Agents theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  # Upgrade to the latest version
  pip install -U deepagents

  # Upgrade to a specific version
  pip install deepagents==0.1.0
  ```
</CodeGroup>

## Pre-release versions

We occasionally release alpha and beta versions for early testing:

* **Alpha** (e.g., `1.0.0a1`): Early preview, significant changes expected
* **Beta** (e.g., `1.0.0b1`): Feature-complete, minor changes possible
* **Release Candidate** (e.g., `1.0.0rc1`): Final testing before stable release

## See also

* [Release policy](/oss/python/release-policy) - Detailed release and deprecation policies

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/versioning.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
