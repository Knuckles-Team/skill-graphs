# Run tests to ensure your changes don't break existing functionality
make test
```

For more details, see the [available commands](https://github.com/langchain-ai/docs?tab=readme-ov-file#available-commands) section in the `README`.

<Important>
  All pull requests are automatically checked by CI/CD. The same linting and formatting standards will be enforced, and PRs cannot be merged if these checks fail.
</Important>

## Documentation types

All documentation falls under one of four categories:

<CardGroup>
  <Card title="How-to guides" icon="tool" href="#how-to-guides">
    Task-oriented instructions for users who know what they want to accomplish.
  </Card>

  <Card title="Conceptual guides" icon="bulb" href="#conceptual-guides">
    Explanations that provide deeper understanding and insights.
  </Card>

  <Card title="Reference" icon="book" href="#reference">
    Technical descriptions of APIs and implementation details.
  </Card>

  <Card title="Tutorials" icon="school" href="#tutorials">
    Lessons that guide users through practical activities to build understanding.
  </Card>
</CardGroup>

<Note>
  Where applicable, all documentation must have both Python and JavaScript/TypeScript content. For more details, see the [co-locate Python and JavaScript/TypeScript content](#co-locate-python-and-javascript%2Ftypescript-content) section.
</Note>

### How-to guides

How-to guides are task-oriented instructions for users who know what they want to accomplish. Examples of how-to guides are on the [LangChain](/oss/python/langchain/overview) and [LangGraph](/oss/python/langgraph/overview) tabs.

<AccordionGroup>
  <Accordion title="Characteristics">
    * **Task-focused**: Focus on a specific task or problem
    * **Step-by-step**: Break down the task into smaller steps
    * **Hands-on**: Provide concrete examples and code snippets
  </Accordion>

  <Accordion title="Tips">
    * Focus on the **how** rather than the **why**
    * Use concrete examples and code snippets
    * Break down the task into smaller steps
    * Link to related conceptual guides and references
  </Accordion>

  <Accordion title="Examples">
    * [Messages](/oss/python/langchain/messages)
    * [Tools](/oss/python/langchain/tools)
    * [Streaming](/oss/python/langgraph/streaming)
  </Accordion>
</AccordionGroup>

### Conceptual guides

Conceptual guide cover core concepts abstractly, providing deep understanding.

<AccordionGroup>
  <Accordion title="Characteristics">
    * **Understanding-focused**: Explain why things work as they do
    * **Broad perspective**: Higher and wider view than other types
    * **Design-oriented**: Explain decisions and trade-offs
    * **Context-rich**: Use analogies and comparisons
  </Accordion>

  <Accordion title="Tips">
    * Focus on the **"why"** rather than the "how"
    * Provides supplementary information not necessarily required for feature usage
    * Can use analogies and reference alternatives
    * Avoid blending in too much reference content
    * Link to related tutorials and how-to guides
  </Accordion>

  <Accordion title="Examples">
    * [Memory](/oss/python/concepts/memory)
    * [Context](/oss/python/concepts/context)
    * [Graph API](/oss/python/langgraph/graph-api)
    * [Functional API](/oss/python/langgraph/functional-api)
  </Accordion>
</AccordionGroup>

### Reference

Reference documentation contains detailed, low-level information describing exactly what functionality exists and how to use it.

<CardGroup>
  <Card title="Python reference" href="https://reference.langchain.com/python/" icon="brand-python" />

  <Card title="JavaScript/TypeScript reference" href="https://reference.langchain.com/javascript/" icon="brand-javascript" />
</CardGroup>

A good reference should:

* Describe what exists (all parameters, options, return values)
* Be comprehensive and structured for easy lookup
* Serve as the authoritative source for technical details

<AccordionGroup>
  <Accordion title="Contributing to references">
    The generated API reference at [reference.langchain.com](https://reference.langchain.com/python/) is built and deployed outside this repository. To report bugs, missing packages, or broken pages there, [open a reference documentation issue](https://github.com/langchain-ai/docs/issues/new?template=04-reference-docs.yml).
  </Accordion>

  <Accordion title="LangChain reference best practices">
    * **Be consistent**; follow existing patterns for provider-specific documentation
    * Include both basic usage (code snippets) and common edge cases/failure modes
    * Note when features require specific versions
  </Accordion>

  <Accordion title="When to create new reference documentation">
    * New integrations or providers need dedicated reference pages
    * Complex configuration options require detailed explanation
    * API changes introduce new parameters or behavior
    * Community frequently asks questions about specific functionality
  </Accordion>
</AccordionGroup>

### Tutorials

Tutorials are longer form step-by-step guides that builds upon itself and takes users through a specific practical activity to build understanding. Tutorials are typically found on the [Learn](/oss/python/learn) tab.

<Note>
  We generally do not merge new tutorials from outside contributors without an acute need. If you feel that a certain topic is missing from docs or is not sufficiently covered, please [open a new issue](https://github.com/langchain-ai/docs/issues).
</Note>

<AccordionGroup>
  <Accordion title="Characteristics">
    * **Practical**: Focus on practical activities to build understanding.
    * **Step-by-step**: Break down the activity into smaller steps.
    * **Hands-on**: Provide sequential, working code snippets.
    * **Supplementary**: Provide additional context and information not necessarily required for feature usage.
  </Accordion>

  <Accordion title="Tips">
    * Code snippets should be sequential and working if the user follows the steps in order.
    * Provide some context for the activity, but link to related conceptual guides and references for more detailed information.
  </Accordion>

  <Accordion title="Examples">
    * [Semantic search](/oss/python/langchain/knowledge-base)
    * [RAG agent](/oss/python/langchain/rag)
  </Accordion>
</AccordionGroup>

## Writing standards

<Note>
  Standards for pages on [reference.langchain.com](https://reference.langchain.com/python/) live with that site’s build pipeline, not in this repo. Use the [reference documentation issue template](https://github.com/langchain-ai/docs/issues/new?template=04-reference-docs.yml) for questions or fixes about generated API reference content.
</Note>

### Mintlify components

Use [Mintlify components](https://mintlify.com/docs/text) to enhance readability:

<Tabs>
  <Tab title="Callouts">
    * `<Note>` for helpful supplementary information
    * `<Warning>` for important cautions and breaking changes
    * `<Tip>` for best practices and advice
    * `<Info>` for neutral contextual information
    * `<Check>` for success confirmations
  </Tab>

  <Tab title="Structure">
    * `<Steps>` for an overview of sequential procedures. **Not** for long lists of steps or tutorials.
    * `<Tabs>` for platform-specific content.
    * `<AccordionGroup>` and `<Accordion>` for nice-to-have information that can be collapsed by default (e.g., full code examples).
    * `<CardGroup>` and `<Card>` for highlighting content.
  </Tab>

  <Tab title="Code">
    * `<CodeGroup>` for multiple language examples.
    * Always specify language tags on code blocks (e.g., ` ```python`, ` ```javascript`).
    * Titles for code blocks (e.g. `Success`, `Error Response`)
  </Tab>
</Tabs>

### Mermaid diagrams

When adding mermaid diagrams, use the LangChain brand color palette for node styling. Copy `classDef` lines from any existing diagram, or use the reference table in [`CLAUDE.md`](https://github.com/langchain-ai/docs/blob/main/CLAUDE.md#mermaid-diagram-styling).

| Role     | Fill      | Stroke    | Text      |
| -------- | --------- | --------- | --------- |
| process  | `#E5F4FF` | `#006DDD` | `#030710` |
| trigger  | `#F6FFDB` | `#6E8900` | `#2E3900` |
| decision | `#FDF3FF` | `#7E65AE` | `#504B5F` |
| output   | `#EBD0F0` | `#885270` | `#441E33` |
| alert    | `#F8E8E6` | `#B27D75` | `#634643` |
| neutral  | `#F2FAFF` | `#40668D` | `#2F4B68` |

Do not use Tailwind defaults, Material Design colors, or other off-brand palettes.

### Page structure

Every documentation page must begin with YAML frontmatter:

```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
---
title: "Clear, specific title"
sidebarTitle: "Short title for the sidebar (optional)"
---
```

### Co-locate Python and JavaScript/TypeScript content

All documentation must be written in both Python and JavaScript/TypeScript when possible. To do so, we use a custom in-line syntax to differentiate between sections that should appear in one or both languages:

```mdx theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
:::python
Python-specific content. In real docs, the preceding backslash (before `python`) is omitted.
:::

:::js
JavaScript/TypeScript-specific content. In real docs, the preceding backslash (before `js`) is omitted.
:::

Content for both languages (not wrapped)
```

This will generate two outputs (one for each language) at `/oss/python/concepts/foo.mdx` and `/oss/javascript/concepts/foo.mdx`. Each outputted page will need to be added to the `/src/docs.json` file to be included in the navigation.

<Note>
  We don't want a lack of parity to block contributions. If a feature is only available in one language, it's okay to have documentation only in that language until the other language catches up. In such cases, please include a note indicating that the feature is not yet available in the other language.

  If you need help translating content between Python and JavaScript/TypeScript, please ask in the [community slack](https://www.langchain.com/join-community) or tag a maintainer in your PR.
</Note>

## Quality standards

### General guidelines

<AccordionGroup>
  <Accordion title="Avoid duplication">
    Multiple pages covering the same material are difficult to maintain and cause confusion. There should be only one canonical page for each concept or feature. Link to other guides instead of re-explaining.
  </Accordion>

  <Accordion title="Link frequently">
    Documentation sections don't exist in a vacuum. Link to other sections frequently to allow users to learn about unfamiliar topics. This includes linking to API references and conceptual sections.
  </Accordion>

  <Accordion title="Be concise">
    Take a less-is-more approach. If another section with a good explanation exists, link to it rather than re-explain, unless your content presents a new angle.
  </Accordion>
</AccordionGroup>

### Accessibility requirements

Ensure documentation is accessible to all users:

* Structure content for easy scanning with headers and lists
* Use specific, actionable link text instead of "click here"
* Include descriptive alt text for all images and diagrams

### Cross-referencing

Use consistent cross-references to connect docs with API reference documentation.

**From docs to API reference:**

Use the `@[]` syntax to link to API reference pages:

```mdx theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
See @[`ChatAnthropic`] for all configuration options.

The @[`bind_tools`][ChatAnthropic.bind_tools] method accepts...
```

The build pipeline transforms these into proper markdown links based on the current language scope (Python or JavaScript). For example, `@[ChatAnthropic]` becomes a link to the Python or JS API reference page depending on which version of the docs is being built, **but only if an entry exists in the `link_map.py` file!** See below for details.

<Accordion title="How autolinks work">
  The `@[]` syntax is processed by [`handle_auto_links.py`](https://github.com/langchain-ai/docs/blob/main/pipeline/preprocessors/handle_auto_links.py). It looks up link keys in [`link_map.py`](https://github.com/langchain-ai/docs/blob/main/pipeline/preprocessors/link_map.py), which contains dictionary mappings for both Python and JavaScript scopes.

  **Supported formats:**

  | Syntax                   | Result                                                                                     |
  | ------------------------ | ------------------------------------------------------------------------------------------ |
  | `@[ChatAnthropic]`       | Link with "ChatAnthropic" as the displayed text                                            |
  | ``@[`ChatAnthropic`]``   | Link with `` `ChatAnthropic` `` (code formatted) as text                                   |
  | `@[text][ChatAnthropic]` | Link with "text" as text and `ChatAnthropic` as the key in the link map                    |
  | `\@[ChatAnthropic]`      | Escaped: renders as literal `@[ChatAnthropic]` (no link – what's being used on this page!) |

  **Adding new links:**

  If a link isn't found in the map, it will be left unchanged in the output. To add a new autolink:

  1. Open `pipeline/preprocessors/link_map.py`
  2. Add an entry to the appropriate scope (`python` or `js`) in `LINK_MAPS`
  3. The key is the link name used in `@[key]` or `@[text][key]`, the value is the path relative to the reference host
</Accordion>

**From API reference stubs to OSS docs:**

Cross-links and deep anchors in the published Python API reference are generated outside this repository. If a link from reference.langchain.com to docs.langchain.com is wrong or outdated, [open an issue](https://github.com/langchain-ai/docs/issues/new?template=04-reference-docs.yml) with the source and destination URLs.

### Localization

Where a feature exists in both SDKs, document it for [Python and JavaScript/TypeScript together](#co-locate-python-and-javascript%2Ftypescript-content). If only one language is supported yet, ensure the feature and references to it are only visible for that language.

### In-code documentation

Examples must be correct, copy-pasteable where possible, and **tested** before you open a pull request. Mark non-runnable snippets clearly (for example, pseudocode or illustrative fragments).

## Get help

Our goal is to have the simplest developer setup possible. Should you experience any difficulty getting setup, please ask in the [community slack](https://www.langchain.com/join-community) or open a [forum post](https://forum.langchain.com/). Internal team members can reach out in the [#documentation](https://langchain.slack.com/archives/C04GWPE38LV) Slack channel.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/contributing/documentation.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Implement a LangChain integration
Source: https://docs.langchain.com/oss/python/contributing/implement-langchain

Integration packages are Python packages that users can install for use in their projects. They implement one or more components that adhere to the LangChain interface standards.

LangChain components are subclasses of base classes in [`langchain-core`](https://github.com/langchain-ai/langchain/tree/master/libs/core). Examples include [chat models](/oss/python/integrations/chat), [tools](/oss/python/integrations/tools), [retrievers](/oss/python/integrations/retrievers), and more.

Your integration package will typically implement a subclass of at least one of these components. Expand the tabs below to see details on each.

<Tabs>
  <Tab title="Chat Models">
    Chat models are subclasses of the [`BaseChatModel`](https://reference.langchain.com/python/langchain-core/language_models/chat_models/BaseChatModel) class. They implement methods for generating chat completions, handling message formatting, and managing model parameters.

    <Warning>
      The chat model integration guide is currently WIP. In the meantime, read the [chat model conceptual guide](/oss/python/langchain/models) for details on how LangChain chat models function. You may also refer to existing integrations in the [LangChain repo](https://github.com/langchain-ai/langchain/tree/master/libs/partners)
    </Warning>
  </Tab>

  <Tab title="Embeddings">
    Embedding models are subclasses of the [`Embeddings`](https://reference.langchain.com/python/langchain-core/embeddings/embeddings/Embeddings) class.

    <Warning>
      The embedding model integration guide is currently WIP. In the meantime, read the [embedding model conceptual guide](/oss/python/integrations/embeddings) for details on how LangChain embedding models function.
    </Warning>
  </Tab>

  <Tab title="Tools">
    Tools are used in 2 main ways:

    1. To define an "input schema" or "args schema" to pass to a chat model's tool calling feature along with a text request, such that the chat model can generate a "tool call", or parameters to call the tool with.
    2. To take a "tool call" as generated above, and take some action and return a response that can be passed back to the chat model as a ToolMessage.

    The Tools class must inherit from the [`BaseTool`](https://reference.langchain.com/python/langchain-core/tools/base/BaseTool) base class. This interface has 3 properties and 2 methods that should be implemented in a subclass.

    <Warning>
      The tools integration guide is currently WIP. In the meantime, read the [tools conceptual guide](/oss/python/langchain/tools) for details on how LangChain tools function.
    </Warning>
  </Tab>

  <Tab title="Middleware">
    [Middleware](/oss/python/langchain/middleware/overview) lets you customize agent behavior by hooking into model calls, tool calls, and agent lifecycle events. Middleware classes subclass the [`AgentMiddleware`](https://reference.langchain.com/python/langchain/agents/middleware/types/AgentMiddleware) base class.

    Read the [custom middleware guide](/oss/python/langchain/middleware/custom) to understand hooks, state updates, and middleware patterns before building an integration.

    Middleware integrations typically fall into two categories:

    | Type                  | Description                                | Examples                                                  |
    | --------------------- | ------------------------------------------ | --------------------------------------------------------- |
    | **Provider-specific** | Leverages a provider's unique capabilities | Prompt caching, native tool execution, content moderation |
    | **Cross-provider**    | Works with any model or tool               | Rate limiting, PII detection, logging, guardrails         |

    Provider-specific middleware lives in the provider's integration package (for example `langchain-anthropic`). Cross-provider middleware can be published as a standalone package.

    You can also use these existing middleware integrations as reference:

    <CardGroup>
      <Card title="OpenAI content moderation" icon="shield" href="/oss/python/integrations/middleware/openai">
        Single middleware with configuration options and exit behaviors.
      </Card>

      <Card title="Anthropic middleware" icon="robot" href="/oss/python/integrations/middleware/anthropic">
        Multiple middleware classes for prompt caching, tools, memory, and file search.
      </Card>

      <Card title="AWS prompt caching" icon="cloud" href="/oss/python/integrations/middleware/aws">
        Provider-specific prompt caching with model behavior tables.
      </Card>

      <Card title="Custom middleware guide" icon="code" href="/oss/python/langchain/middleware/custom">
        Full reference for hooks, state updates, and patterns.
      </Card>
    </CardGroup>
  </Tab>

  <Tab title="Checkpointers">
    Checkpointers enable [persistence](/oss/python/langgraph/persistence) in LangGraph, allowing agents to save and resume state across interactions.

    See existing checkpointer integrations in the [LangGraph repo](https://github.com/langchain-ai/langgraph/tree/main/libs) for implementation examples.
  </Tab>

  <Tab title="Sandboxes">
    Sandbox integrations enable [Deep Agents](/oss/python/deepagents/overview) to run code in isolated environments.

    Implement the [`SandboxBackendProtocol`](https://reference.langchain.com/python/deepagents/backends/protocol/SandboxBackendProtocol) from Deep Agents. This protocol includes `execute()`, async variants, and the filesystem tool methods such as `ls`, `read`, `write`, `edit`, `glob`, and `grep`.

    In practice, if your sandbox environment can run shell commands and has `python3` available, you should usually subclass [`BaseSandbox`](https://reference.langchain.com/python/deepagents/backends/sandbox/BaseSandbox). `BaseSandbox` provides the filesystem operations through `python3`, so you mainly need to implement `execute()`, `upload_files()`, `download_files()`, and `id`.

    ```python Example BaseSandbox scaffold expandable theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from __future__ import annotations

    from deepagents.backends.protocol import (
        ExecuteResponse,
        FileDownloadResponse,
        FileUploadResponse,
    )
    from deepagents.backends.sandbox import BaseSandbox  # [!code highlight]

    class MySandbox(BaseSandbox):
        def __init__(self, client: MySandboxSdkClient) -> None:
            self._client = client

        @property
        def id(self) -> str:
            return self._client.sandbox_id

        def execute(
            self,
            command: str,
            *,
            timeout: int | None = None,
        ) -> ExecuteResponse:
            # Execute `command` in your sandbox and map the provider response
            # into ExecuteResponse.
            result = self._client.run(command=command, timeout=timeout)
            output = result.stdout or ""
            if result.stderr:
                output += f"\n<stderr>{result.stderr}</stderr>"
            return ExecuteResponse(
                output=output,
                exit_code=result.exit_code,
                truncated=False,
            )

        def upload_files(
            self,
            files: list[tuple[str, bytes]],
        ) -> list[FileUploadResponse]:
            # Validate paths, batch requests where possible, and map provider
            # results back into FileUploadResponse objects in input order.
            # Only catch and normalize errors that an LLM can plausibly retry
            # or fix, such as invalid_path or file_not_found.
            return self._client.upload_files(files)

        def download_files(self, paths: list[str]) -> list[FileDownloadResponse]:
            # Validate paths, batch requests where possible, and map provider
            # results back into FileDownloadResponse objects in input order.
            # Only catch and normalize errors that an LLM can plausibly retry
            # or fix, such as invalid_path or file_not_found.
            return self._client.download_files(paths)

        async def aexecute(
            self,
            command: str,
            *,
            timeout: int | None = None,
        ) -> ExecuteResponse:
            ...

        async def aupload_files(
            self,
            files: list[tuple[str, bytes]],
        ) -> list[FileUploadResponse]:
            ...

        async def adownload_files(
            self,
            paths: list[str],
        ) -> list[FileDownloadResponse]:
            ...
    ```

    ## Test your integration

    Validate your integration with the [sandbox standard test suite](/oss/python/contributing/standard-tests-langchain#sandbox-integrations). The Python suite uses `SandboxIntegrationTests` from `langchain_tests.integration_tests`; subclass it and provide a `sandbox` fixture that yields a clean `SandboxBackendProtocol` instance.

    ```python Example sandbox standard test setup expandable theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from __future__ import annotations

    from collections.abc import Iterator

    import pytest
    from deepagents.backends.protocol import SandboxBackendProtocol
    from langchain_tests.integration_tests import SandboxIntegrationTests

    from langchain_myprovider import MySandbox
    from myprovider_sdk import MySandboxSdkClient

    class TestMySandboxStandard(SandboxIntegrationTests):
        @pytest.fixture(scope="class")
        def sandbox(self) -> Iterator[SandboxBackendProtocol]:
            client = MySandboxSdkClient()
            backend = MySandbox(client=client)
            try:
                yield backend
            finally:
                # Replace this with your provider's cleanup logic.
                client.delete_sandbox(backend.id)
    ```

    Put this in a file such as `tests/integration_tests/test_sandbox.py`. The standard suite will handle the actual filesystem and command-execution assertions for you.

    **Reference implementation:** See the [Daytona partner integration](https://github.com/langchain-ai/deepagents/tree/main/libs/partners/daytona), which subclasses `BaseSandbox` and implements `execute()`, `upload_files()`, `download_files()`, and `id`.
  </Tab>
</Tabs>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/contributing/implement-langchain.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Contributing integrations
Source: https://docs.langchain.com/oss/python/contributing/integrations-langchain

**Integrations are a core component of LangChain.**

LangChain provides standard interfaces for several different components (language models, vector stores, etc) that are crucial when building LLM applications. Implementing a new integration helps expand LangChain's ecosystem and makes your service discoverable to millions of developers.

<Warning>
  New integrations are **not accepted as PRs** to any `langchain-ai` repository. All new integrations must be published as independent packages to PyPI (e.g., `langchain-yourprovider`). The only PR you should open to a `langchain-ai` repo is to add documentation for your published package.
</Warning>

## Why implement a LangChain integration?

<Card title="Discoverability" icon="search">
  LangChain is the most used framework for building LLM applications, with over 200 million monthly downloads.
</Card>

<Card title="Interoperability" icon="refresh">
  LangChain components expose a standard interface, allowing developers to easily swap them for each other. If you implement a LangChain integration, any developer using a different component will easily be able to swap yours in.
</Card>

<Card title="Best Practices" icon="star">
  Through their standard interface, LangChain components encourage and facilitate best practices (streaming, async, etc.) that improve developer experience and application performance.
</Card>

## Components to integrate

While any component can be integrated into LangChain, there are specific types of integrations we encourage more:

**Integrate these ✅**:

* [**Chat Models**](/oss/python/integrations/chat): Most actively used component type
* [**Tools/Toolkits**](/oss/python/integrations/tools): Enable agent capabilities
* [**Retrievers**](/oss/python/integrations/retrievers): Core to RAG applications
* [**Embedding Models**](/oss/python/integrations/embeddings): Foundation for vector operations
* [**Vector Stores**](/oss/python/integrations/vectorstores): Essential for semantic search
* [**Middleware**](/oss/python/integrations/middleware): Extend agent behavior with hooks
* [**Sandboxes**](/oss/python/deepagents/sandboxes): Run code safely with Deep Agents

<Accordion title="Additional third-party sandbox integration criteria">
  Be aware that we feature third-party sandbox integrations only when:

  * The integration is authored and maintained by the company that provides the sandbox.
  * **Or** the integration is widely used, meaning the integration must have a minimum of 10,000 daily downloads on PyPI or npm to be considered for featuring.
</Accordion>

**Not these ❌**:

* **LLMs (Text-Completion Models)**: Deprecated in favor of [Chat Models](/oss/python/integrations/chat)
* [**Document Loaders**](/oss/python/integrations/document_loaders): High maintenance burden
* [**Key-Value Stores**](/oss/python/integrations/stores): Limited usage
* **Document Transformers**: Niche use cases
* **Model Caches**: Infrastructure concerns
* **Graphs**: Complex abstractions
* **Message Histories**: Storage abstractions
* **Callbacks**: System-level components
* **Chat Loaders**: Limited demand
* **Adapters**: Edge case utilities

## How to contribute an integration

<Steps>
  <Step title="Implement your package">
    <Card title="How to implement a LangChain integration" icon="link" href="/oss/python/contributing/implement-langchain" />
  </Step>

  <Step title="Pass standard tests">
    If applicable, implement support for LangChain's [standard test](/oss/python/contributing/standard-tests-langchain) suite for your integration and successfully run them.
  </Step>

  <Step title="Publish integration">
    <Card title="How to publish an integration" icon="upload" href="/oss/python/contributing/publish-langchain" />
  </Step>

  <Step title="Add documentation">
    Open a PR to add documentation for your integration to the official LangChain docs.

    <Accordion title="Integration documentation guide" icon="book">
      An integration is only as useful as its documentation. To ensure a consistent experience for users, docs are required for all new integrations. We have a standard starting-point template for each type of integration for you to copy and modify.

      In a new PR to the LangChain [docs repo](https://github.com/langchain-ai/docs), create a new file in the relevant directory under `src/oss/python/integrations/<component_type>/integration_name.mdx` using the appropriate template file:

      * [Chat models](https://github.com/langchain-ai/docs/blob/main/src/oss/python/integrations/chat/TEMPLATE.mdx)
      * [Tools and toolkits](https://github.com/langchain-ai/docs/blob/main/src/oss/python/integrations/tools/TEMPLATE.mdx)
      * [Middleware](https://github.com/langchain-ai/docs/blob/main/src/oss/python/integrations/middleware/TEMPLATE.mdx)
      * Retrievers - Coming soon
      * Text splitters - Coming soon
      * Embedding models - Coming soon
      * [Vector stores](https://github.com/langchain-ai/docs/blob/main/src/oss/python/integrations/vectorstores/TEMPLATE.mdx)
      * Document loaders - Coming soon
      * Key-value stores - Coming soon
    </Accordion>
  </Step>

  <Step title="Co-marketing" icon="speakerphone">
    (Optional) Engage with the LangChain team for joint [co-marketing](/oss/python/contributing/comarketing).
  </Step>
</Steps>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/contributing/integrations-langchain.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Contributing
Source: https://docs.langchain.com/oss/python/contributing/overview

**Welcome! Thank you for your interest in contributing.**

LangChain has helped form the largest developer community in generative AI, and we're always open to new contributors. Whether you're fixing bugs, adding features, improving documentation, or sharing feedback, your involvement helps make LangChain and LangGraph better for everyone 🦜❤️

## Ways to contribute

<AccordionGroup>
  <Accordion title="Report bugs" icon="bug">
    Found a bug? Please help us fix it by following these steps:

    <Steps>
      <Step title="Search">
        Check if the issue already exists in our GitHub Issues for the respective repo:

        <Columns>
          <Card title="LangChain" icon="link" href="https://github.com/langchain-ai/langchain/issues">Issues</Card>
          <Card title="LangGraph" icon="topology-ring" href="https://github.com/langchain-ai/langgraph/issues">Issues</Card>
          <Card title="Deep Agents" icon="robot" href="https://github.com/langchain-ai/deepagents/issues">Issues</Card>
        </Columns>
      </Step>

      <Step title="Create issue">
        If no issue exists, create a new one. When writing, be sure to follow the template provided and to include a [minimal, reproducible, example](https://stackoverflow.com/help/minimal-reproducible-example). Attach any relevant labels to the final issue once created. If a project maintainer is unable to reproduce the issue, it is unlikely to be addressed in a timely manner.
      </Step>

      <Step title="Wait">
        A project maintainer will triage the issue and may ask for additional information. Please be patient as we manage a high volume of issues. Do not bump the issue unless you have new information to provide.
      </Step>
    </Steps>

    If you are adding an issue, please try to keep it focused on a single topic. If two issues are related, or blocking, please [link them](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue#linking-a-pull-request-to-an-issue-using-a-keyword) rather than combining them. For example:

    ```text theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    This issue is blocked by #123 and related to #456.
    ```
  </Accordion>

  <Accordion title="Suggest features" icon="wand">
    Have an idea for a new feature or enhancement?

    <Steps>
      <Step title="Search">
        Search the issues for the respective repository for existing feature requests:

        <Columns>
          <Card title="LangChain" icon="link" href="https://github.com/langchain-ai/langchain/issues?q=state%3Aopen%20label%3A%22feature%20request%22">Issues</Card>
          <Card title="LangGraph" icon="topology-ring" href="https://github.com/langchain-ai/langgraph/issues?q=state%3Aopen%20label%3Aenhancement">Issues</Card>
          <Card title="Deep Agents" icon="robot" href="https://github.com/langchain-ai/deepagents/issues?q=is%3Aissue%20state%3Aopen%20label%3Afeature">Issues</Card>
        </Columns>
      </Step>

      <Step title="Discuss">
        If no requests exist, start a new discussion under the [relevant category](https://forum.langchain.com/c/oss-product-help-lc-and-lg/16) so that project maintainers and the community can provide feedback.
      </Step>

      <Step title="Describe">
        Be sure to describe the use case and why it would be valuable to others. If possible, provide examples or mockups where applicable. Outline test cases that should pass.
      </Step>
    </Steps>
  </Accordion>

  <Accordion title="Improve documentation" icon="book">
    Documentation improvements are welcome! We strive to keep our docs clear and comprehensive, and your perspective can make a big difference.

    <Card title="How to propose changes to the documentation" href="/oss/python/contributing/documentation">Guide</Card>
  </Accordion>

  <Accordion title="Contribute code" icon="code">
    With a large userbase, it can be hard for our small team to keep up with all the feature requests and bug fixes. If you have the skills and time, we would love your help!

    <Card title="How to make your first Pull Request" href="/oss/python/contributing/code">Guide</Card>

    If you start working on an issue, please assign it to yourself or ask a maintainer to do so. This helps avoid duplicate work.

    If you are looking for something to work on, check out the issue labeled "help wanted" in our repos:

    <Columns>
      <Card title="LangChain" icon="link" href="https://github.com/langchain-ai/langchain/labels?q=help+wanted">Labels</Card>
      <Card title="LangGraph" icon="topology-ring" href="https://github.com/langchain-ai/langgraph/labels?q=help+wanted">Labels</Card>
      <Card title="Deep Agents" icon="robot" href="https://github.com/langchain-ai/deepagents/labels?q=help+wanted">Labels</Card>
    </Columns>
  </Accordion>

  <Accordion title="Build a new integration" icon="plug-connected">
    Anyone can build and publish their own LangChain integration package. New integrations are not accepted as PRs to `langchain-ai` repos — they must be published independently to PyPI or npm.

    <Card title="LangChain" icon="link" href="/oss/python/contributing/integrations-langchain">Guide to building a LangChain integration</Card>
    <Card title="Deep Agents sandboxes" icon="cube" href="/oss/python/contributing/integrations-langchain">Guide to building a sandbox integration</Card>
  </Accordion>
</AccordionGroup>

## Pull request requirements

<Warning>
  **All pull requests must link to an issue or discussion where a solution has been approved by a maintainer.** Do not open a pull request before a maintainer has approved your approach and assigned the linked issue to you. Early PRs may be closed automatically and are not reviewed until assignment.
</Warning>

All pull requests should demonstrate meaningful effort and contextual understanding. **If the effort required to create a pull request is less than the effort required for maintainers to review it, that contribution should not be submitted.** Low-effort drive-by contributions—regardless of how they are produced—often miss the mark in terms of contextual relevance, accuracy, and quality. Mass automated contributions represent a denial-of-service attack on our human effort.

The following requirements must be met for all external pull requests:

* The pull request must link to an issue or discussion where a solution has been approved by a maintainer, and the contributor must be assigned to that issue before opening the PR.
* The pull request must fill in the repository's pull request template.

Maintainers reserve the right to close PRs without comment if these requirements are not met. **We will close pull requests and issues that appear to be low-effort spam.**

## Language policy

All contributions—issues, pull requests, code reviews, and discussions—must be in English. This keeps communications accessible and searchable across our global contributor base.

If English isn't your first language, don't worry. We value clear communication over perfect grammar, and translation tools are welcome.

## Acceptable uses of LLMs

You may use AI assistants to help draft or revise contributions when you **verify every change**: run and test code, check facts against the codebase and official provider docs, and ensure the result matches repository style. Do not submit bulk, unreviewed generated content. We close pull requests that read as low-effort or spam regardless of how they were produced.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/contributing/overview.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Publish an integration
Source: https://docs.langchain.com/oss/python/contributing/publish-langchain

**Make your integration available to the community.**

<Warning>
  **Do not submit integration PRs to the LangChain or Deep Agents repositories.**

  New integrations should be published as **standalone PyPI packages** under your own GitHub organization or account (e.g., `langchain-yourservice`), not as PRs to the [`langchain-ai/langchain`](https://github.com/langchain-ai/langchain) repository.

  The main repository only contains a small subset of first-party integrations (like OpenAI, Anthropic, and Ollama) maintained by the LangChain team.
</Warning>

Now that your package is implemented and tested, you can publish it and add documentation to make it discoverable by the community.

## Publishing your package

<Info>
  This guide assumes you have already implemented your package and written tests for it. If you haven't, please refer to the [implementation guide](/oss/python/contributing/implement-langchain) and [testing guide](/oss/python/contributing/standard-tests-langchain).
</Info>

For the purposes of this guide, we'll be using PyPI as the package registry. You may choose to publish to other registries if you prefer; instructions will vary.

### Setup credentials

First, make sure you have a PyPI account:

<AccordionGroup>
  <Accordion title="How to create a PyPI Token" icon="key">
    <Steps>
      <Step title="Create account">
        Go to the [PyPI website](https://pypi.org/) and create an account
      </Step>

      <Step title="Verify email">
        Verify your email address by clicking the link that PyPI emails to you
      </Step>

      <Step title="Enable 2FA">
        Go to your account settings and click "Generate Recovery Codes" to enable 2FA. To generate an API token, you **must** have 2FA enabled
      </Step>

      <Step title="Generate token">
        Go to your account settings and [generate a new API token](https://pypi.org/manage/account/token/)
      </Step>
    </Steps>
  </Accordion>
</AccordionGroup>

### Build and publish

<Card title="How to publish a package" icon="upload" href="https://docs.astral.sh/uv/guides/package/">
  Helpful guide from `uv` on how to build and publish a package to PyPI.
</Card>

## Adding documentation

To add documentation for your package to this site under the [integrations tab](/oss/python/integrations/providers/overview), you will need to create the relevant documentation pages and open a PR in the [LangChain docs repository](https://github.com/langchain-ai/docs).

### Writing docs

Depending on the type of integration you have built, you will need to create different types of documentation pages. LangChain provides templates for different types of integrations to help you get started.

<CardGroup>
  <Card title="Chat models" icon="message" href="https://github.com/langchain-ai/docs/blob/main/src/oss/python/integrations/chat/TEMPLATE.mdx" />

  <Card title="Tools/toolkits" icon="tool" href="https://github.com/langchain-ai/docs/blob/main/src/oss/python/integrations/tools/TEMPLATE.mdx" />

  <Card title="Middleware" icon="plug" href="https://github.com/langchain-ai/docs/blob/main/src/oss/python/integrations/middleware/TEMPLATE.mdx" />

  <Card title="Vector stores" icon="database" href="https://github.com/langchain-ai/docs/blob/main/src/oss/python/integrations/vectorstores/TEMPLATE.mdx" />
</CardGroup>

<Tip>
  To reference existing documentation, you can look at the [list of integrations](/oss/python/integrations/providers/overview) and find similar ones to yours.

  To view a given documentation page in raw markdown, use the dropdown button next to "Copy page" on the top right of the page and select "View as Markdown".
</Tip>

### Submit a PR to the docs repo

Make a fork of the [LangChain docs repository](https://github.com/langchain-ai/docs) (not the main `langchain` repo) under a personal GitHub account, and clone it locally. Create a new branch for your integration. Copy the template and modify it using your favorite markdown text editor. Make sure to refer to and follow the [documentation guide](/oss/python/contributing/documentation) when writing your documentation.

<Info>
  This PR is for **documentation only**. Your integration package itself should live in its own repository under your GitHub organization or account, published to PyPI as a standalone package.
</Info>

<Warning>
  We may reject PRs or ask for modification if:

  * CI checks fail
  * Severe grammatical errors or typos are present
  * [Mintlify components](/oss/python/contributing/documentation#mintlify-components) are used incorrectly
  * Pages are missing a [frontmatter](/oss/python/contributing/documentation#page-structure)
  * [Localization](/oss/python/contributing/documentation#localization) is missing (where applicable)
  * [Code examples](/oss/python/contributing/documentation#in-code-documentation) do not run or have errors
  * [Quality standards](/oss/python/contributing/documentation#quality-standards) are not met
</Warning>

Please be patient as we handle a large volume of PRs. We will review your PR as soon as possible and provide feedback or merge it. **Do not repeatedly tag maintainers about your PR.**

<Note>
  If your PR includes AI-generated content, you must follow our [acceptable uses of LLMs](/oss/python/contributing/overview#acceptable-uses-of-llms) policy.
</Note>

***

## Next steps

**Congratulations!** Your integration is now published and documented, making it available to the entire LangChain community.

<Card title="Co-marketing" icon="speakerphone" href="/oss/python/contributing/comarketing">
  Get in touch with the LangChain marketing team to explore co-marketing opportunities.
</Card>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/contributing/publish-langchain.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
