# Contributing integrations
Source: https://docs.langchain.com/oss/javascript/contributing/integrations-langchain

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

* [**Chat Models**](/oss/javascript/integrations/chat): Most actively used component type
* [**Tools/Toolkits**](/oss/javascript/integrations/tools): Enable agent capabilities
* [**Retrievers**](/oss/javascript/integrations/retrievers): Core to RAG applications
* [**Embedding Models**](/oss/javascript/integrations/embeddings): Foundation for vector operations
* [**Vector Stores**](/oss/javascript/integrations/vectorstores): Essential for semantic search
* [**Middleware**](/oss/javascript/integrations/middleware): Extend agent behavior with hooks
* [**Sandboxes**](/oss/javascript/deepagents/sandboxes): Run code safely with Deep Agents

<Accordion title="Additional third-party sandbox integration criteria">
  Be aware that we feature third-party sandbox integrations only when:

  * The integration is authored and maintained by the company that provides the sandbox.
  * **Or** the integration is widely used, meaning the integration must have a minimum of 10,000 daily downloads on PyPI or npm to be considered for featuring.
</Accordion>

**Not these ❌**:

* **LLMs (Text-Completion Models)**: Deprecated in favor of [Chat Models](/oss/javascript/integrations/chat)
* [**Document Loaders**](/oss/javascript/integrations/document_loaders): High maintenance burden
* [**Key-Value Stores**](/oss/javascript/integrations/stores): Limited usage
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
    <Card title="How to implement a LangChain integration" icon="link" href="/oss/javascript/contributing/implement-langchain" />
  </Step>

  <Step title="Pass standard tests">
    If applicable, implement support for LangChain's [standard test](/oss/javascript/contributing/standard-tests-langchain) suite for your integration and successfully run them.
  </Step>

  <Step title="Publish integration">
    <Card title="How to publish an integration" icon="upload" href="/oss/javascript/contributing/publish-langchain" />
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
    (Optional) Engage with the LangChain team for joint [co-marketing](/oss/javascript/contributing/comarketing).
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
Source: https://docs.langchain.com/oss/javascript/contributing/overview

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
          <Card title="LangChain" icon="link" href="https://github.com/langchain-ai/langchainjs/issues">Issues</Card>
          <Card title="LangGraph" icon="topology-ring" href="https://github.com/langchain-ai/langgraphjs/issues">Issues</Card>
          <Card title="Deep Agents" icon="robot" href="https://github.com/langchain-ai/deepagentsjs/issues">Issues</Card>
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
          <Card title="LangChain" icon="link" href="https://github.com/langchain-ai/langchainjs">Issues</Card>
          <Card title="LangGraph" icon="topology-ring" href="https://github.com/langchain-ai/langgraphjs/labels?q=feature">Issues</Card>
          <Card title="Deep Agents" icon="robot" href="https://github.com/langchain-ai/deepagentsjs/issues?q=is%3Aissue%20state%3Aopen%20label%3Aenhancement">Issues</Card>
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

    <Card title="How to propose changes to the documentation" href="/oss/javascript/contributing/documentation">Guide</Card>
  </Accordion>

  <Accordion title="Contribute code" icon="code">
    With a large userbase, it can be hard for our small team to keep up with all the feature requests and bug fixes. If you have the skills and time, we would love your help!

    <Card title="How to make your first Pull Request" href="/oss/javascript/contributing/code">Guide</Card>

    If you start working on an issue, please assign it to yourself or ask a maintainer to do so. This helps avoid duplicate work.

    If you are looking for something to work on, check out the issue labeled "help wanted" in our repos:

    <Columns>
      <Card title="LangChain" icon="link" href="https://github.com/langchain-ai/deepagents/labels?q=help+wanted">Labels</Card>
      <Card title="LangGraph" icon="topology-ring" href="https://github.com/langchain-ai/langgraphjs/labels?q=help+wanted">Labels</Card>
      <Card title="Deep Agents" icon="robot" href="https://github.com/langchain-ai/deepagentsjs/labels?q=help+wanted">Labels</Card>
    </Columns>
  </Accordion>

  <Accordion title="Build a new integration" icon="plug-connected">
    Anyone can build and publish their own LangChain integration package. New integrations are not accepted as PRs to `langchain-ai` repos — they must be published independently to PyPI or npm.

    <Card title="LangChain" icon="link" href="/oss/javascript/contributing/integrations-langchain">Guide to building a LangChain integration</Card>
    <Card title="Deep Agents sandboxes" icon="cube" href="/oss/javascript/contributing/integrations-langchain">Guide to building a sandbox integration</Card>
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
Source: https://docs.langchain.com/oss/javascript/contributing/publish-langchain

**Make your integration available to the community.**

TODO

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/contributing/publish-langchain.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Using standard tests
Source: https://docs.langchain.com/oss/javascript/contributing/standard-tests-langchain

**Standard tests ensure your integration works as expected.**

When creating either a custom class for yourself or to publish in a LangChain integration, it is necessary to add tests to ensure it works as expected. LangChain provides a comprehensive [set of tests](https://pypi.org/project/langchain-tests/) for each integration type for you. This guide will show you how to add LangChain's standard test suite to each integration type.

## Setup

First, install the required dependencies:

<CardGroup>
  <Card title="langchain-core" icon="cube" href="https://github.com/langchain-ai/langchainjs/tree/main/langchain-core#readme">
    Defines the interfaces we want to import to define our custom components
  </Card>

  <Card title="langchain-tests" icon="flask" href="https://github.com/langchain-ai/langchainjs/tree/main/libs/langchain-standard-tests#readme">
    Provides the standard tests and plugins necessary to run them
  </Card>
</CardGroup>

<CodeGroup>
  ```bash npm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  npm install @langchain/core
  npm install @langchain/standard-tests
  ```

  ```bash pnpm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pnpm add @langchain/core
  pnpm add @langchain/standard-tests
  ```

  ```bash yarn theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  yarn add @langchain/core
  yarn add @langchain/standard-tests
  ```

  ```bash bun theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  bun add @langchain/core
  bun add @langchain/standard-tests
  ```
</CodeGroup>

There are 2 namespaces in the `langchain-tests` package:

<AccordionGroup>
  <Accordion title="Unit tests" icon="settings">
    **Location**: `src.unit_tests`

    Designed to test the component in isolation and without access to external services

    [View API reference](https://reference.langchain.com/python/langchain_tests/unit_tests)
  </Accordion>

  <Accordion title="Integration tests" icon="network">
    **Location**: `src.integration_tests`

    Designed to test the component with access to external services (in particular, the external service that the component is designed to interact with)

    [View API reference](https://reference.langchain.com/python/langchain_tests/integration_tests)
  </Accordion>
</AccordionGroup>

## Implementing standard tests

Depending on your integration type, you will need to implement either or both unit and integration tests.

By subclassing the standard test suite for your integration type, you get the full collection of standard tests for that type. For a test run to be successful, the a given test should pass only if the model supports the capability being tested. Otherwise, the test should be skipped.

Because different integrations offer unique sets of features, most standard tests provided by LangChain are **opt-in by default** to prevent false positives. Consequently, you will need to override properties to indicate which features your integration supports - see the below example for an illustration.

```javascript tests/chat_models.standard.int.test.ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
// Indicate that a chat model supports parallel tool calls

class ChatParrotLinkStandardIntegrationTests extends ChatModelIntegrationTests<
    ChatParrotLinkCallOptions,
    AIMessageChunk
> {
    constructor() {
        // ... other required properties

        super({
            // ... other required properties
            supportsParallelToolCalls: true,  // (The default is False)
            // ...
        });
    }
```

<Note>
  You should organize tests in these subdirectories relative to the root of your package:

  * `tests/unit_tests` for unit tests
  * `tests/integration_tests` for integration tests
</Note>

To see the complete list of configurable capabilities and their defaults, see [Implementing standard tests](/oss/javascript/contributing/standard-tests-langchain#implementing-standard-tests).

## Sandbox integrations

Deep Agents sandbox integrations use `sandboxStandardTests` from `@langchain/sandbox-standard-tests`.
Call it with a config object that includes `createSandbox`, `resolvePath`, and `closeSandbox`.
Use the [Daytona integration tests](https://github.com/langchain-ai/deepagentsjs/blob/main/libs/providers/daytona/src/sandbox.int.test.ts) as a reference implementation.
See [Contributing a sandbox integration](/oss/javascript/contributing/integrations-langchain) for publishing guidelines.

***

## Troubleshooting

For a full list of the standard test suites that are available, as well as information on which tests are included and how to troubleshoot common issues, see the [contributing README](https://github.com/langchain-ai/langchainjs/blob/main/CONTRIBUTING.md).

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/contributing/standard-tests-langchain.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# A2A server
Source: https://docs.langchain.com/oss/javascript/deepagents/a2a

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/deepagents/a2a.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Agent Client Protocol (ACP)
Source: https://docs.langchain.com/oss/javascript/deepagents/acp

Expose Deep Agents over the Agent Client Protocol (ACP) to integrate with code editors and IDEs.

[Agent Client Protocol (ACP)](https://agentclientprotocol.com/get-started/introduction) standardizes communication between coding agents and code editors or IDEs.
With the ACP protocol, you can make use of your custom deep agents with any ACP-compatible client, allowing your code editor to provide project context and receive rich updates.

<Note>
  ACP is designed for agent-editor integrations. If you want your agent to call tools hosted by external servers, see [Model Context Protocol (MCP)](/oss/javascript/langchain/mcp/).
</Note>

## Quickstart

Install the ACP integration package:

<CodeGroup>
  ```bash npm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  npm install deepagents-acp
  ```

  ```bash yarn theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  yarn add deepagents-acp
  ```

  ```bash pnpm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pnpm add deepagents-acp
  ```
</CodeGroup>

Then expose a deep agent over ACP.

This starts an ACP server in stdio mode (it reads requests from stdin and writes responses to stdout). In practice, you usually run this as a command launched by an ACP client (for example, your editor), which then communicates with the server over stdio.

```typescript icon="server" theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { startServer } from "deepagents-acp";

await startServer({
  agents: {
    name: "coding-assistant",
    description: "AI coding assistant with filesystem access",
  },
  workspaceRoot: process.cwd(),
});
```

You can also use the CLI without writing any code:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
npx deepagents-acp
```

<Card title="Deep Agents ACP on npm" icon="brand-npm" href="https://www.npmjs.com/package/deepagents-acp">
  The `deepagents-acp` package provides both a CLI and a programmatic API for exposing deep agents over ACP.
</Card>

## Clients

Deep agents work anywhere you can run an ACP agent server. Some notable ACP clients include:

* [Zed](https://zed.dev/docs/ai/external-agents)
* [JetBrains IDEs](https://www.jetbrains.com/help/ai-assistant/acp.html)
* Visual Studio Code (via [vscode-acp](https://github.com/formulahendry/vscode-acp))
* Neovim (via ACP-compatible plugins)

### Zed

Register your deep agent with [Zed](https://zed.dev/docs/ai/external-agents) by adding it to your Zed settings (`~/.config/zed/settings.json` on Linux, `~/Library/Application Support/Zed/settings.json` on macOS):

**Simple setup (no code required):**

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "agent": {
    "profiles": {
      "deepagents": {
        "name": "DeepAgents",
        "command": "npx",
        "args": ["deepagents-acp"],
        "env": {
          "ANTHROPIC_API_KEY": "sk-ant-..."
        }
      }
    }
  }
}
```

**With CLI options:**

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "agent": {
    "profiles": {
      "deepagents": {
        "name": "DeepAgents",
        "command": "npx",
        "args": [
          "deepagents-acp",
          "--name", "my-assistant",
          "--skills", "./skills",
          "--debug"
        ],
        "env": {
          "ANTHROPIC_API_KEY": "sk-ant-..."
        }
      }
    }
  }
}
```

**Custom server script:**

For more control, create a TypeScript server script:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
// server.ts
import { startServer } from "deepagents-acp";

await startServer({
  agents: {
    name: "my-agent",
    description: "My custom coding agent",
    skills: ["./skills/"],
  },
});
```

Then point Zed at it:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "agent": {
    "profiles": {
      "my-agent": {
        "name": "My Agent",
        "command": "npx",
        "args": ["tsx", "./server.ts"]
      }
    }
  }
}
```

Open Zed's Agents panel and start a Deep Agents thread.

### ACP Registry

Deep Agents is available in the [ACP Agent Registry](https://agentclientprotocol.com/registry/index) for one-click installation in Zed and JetBrains IDEs. When an ACP client supports the registry, users can discover and install Deep Agents without any manual configuration.

## CLI reference

The CLI is the fastest way to start an ACP server. It requires no code — just run `npx deepagents-acp` and connect your editor.

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
npx deepagents-acp [options]
```

| Option                 | Short | Description                                         |
| ---------------------- | ----- | --------------------------------------------------- |
| `--name <name>`        | `-n`  | Agent name (default: `"deepagents"`)                |
| `--description <desc>` | `-d`  | Agent description                                   |
| `--model <model>`      | `-m`  | LLM model (default: `"claude-sonnet-4-5-20250929"`) |
| `--workspace <path>`   | `-w`  | Workspace root directory (default: cwd)             |
| `--skills <paths>`     | `-s`  | Comma-separated skill paths                         |
| `--memory <paths>`     |       | Comma-separated AGENTS.md paths                     |
| `--debug`              |       | Enable debug logging to stderr                      |
| `--help`               | `-h`  | Show help message                                   |
| `--version`            | `-v`  | Show version                                        |

### Environment variables

| Variable            | Description                                    |
| ------------------- | ---------------------------------------------- |
| `ANTHROPIC_API_KEY` | API key for Anthropic/Claude models (required) |
| `OPENAI_API_KEY`    | API key for OpenAI models                      |
| `DEBUG`             | Set to `"true"` to enable debug logging        |
| `WORKSPACE_ROOT`    | Alternative to `--workspace` flag              |

## Programmatic API

### `startServer`

Convenience function to create and start a server in one call:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { startServer } from "deepagents-acp";

const server = await startServer({
  agents: {
    name: "coding-assistant",
    description: "AI coding assistant with filesystem access",
  },
  workspaceRoot: process.cwd(),
});
```

### `DeepAgentsServer`

For full control, use the `DeepAgentsServer` class directly:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { DeepAgentsServer } from "deepagents-acp";

const server = new DeepAgentsServer({
  agents: [
    {
      name: "code-agent",
      description: "Full-featured coding assistant",
      model: "claude-sonnet-4-5-20250929",
      skills: ["./skills/"],
      memory: ["./.deepagents/AGENTS.md"],
    },
    {
      name: "reviewer",
      description: "Code review specialist",
      systemPrompt: "You are a code review expert...",
    },
  ],
  serverName: "my-deepagents-acp",
  serverVersion: "1.0.0",
  workspaceRoot: process.cwd(),
  debug: true,
});

await server.start();
```

#### Server options

| Option          | Type                                   | Default            | Description              |
| --------------- | -------------------------------------- | ------------------ | ------------------------ |
| `agents`        | `DeepAgentConfig \| DeepAgentConfig[]` | required           | Agent configuration(s)   |
| `serverName`    | `string`                               | `"deepagents-acp"` | Server name for ACP      |
| `serverVersion` | `string`                               | `"0.0.1"`          | Server version           |
| `workspaceRoot` | `string`                               | `process.cwd()`    | Workspace root directory |
| `debug`         | `boolean`                              | `false`            | Enable debug logging     |

#### Agent configuration

| Option         | Type                                           | Description                                                                                                          |
| -------------- | ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `name`         | `string`                                       | Unique agent name (required)                                                                                         |
| `description`  | `string`                                       | Agent description                                                                                                    |
| `model`        | `string`                                       | LLM model (default: `"claude-sonnet-4-5-20250929"`)                                                                  |
| `tools`        | `StructuredTool[]`                             | Custom LangChain tools                                                                                               |
| `systemPrompt` | `string`                                       | Custom system prompt                                                                                                 |
| `middleware`   | `AgentMiddleware[]`                            | Custom middleware appended to the [default stack](/oss/javascript/deepagents/customization#default-stack-main-agent) |
| `backend`      | `AnyBackendProtocol`                           | Filesystem backend                                                                                                   |
| `skills`       | `string[]`                                     | Skill source paths                                                                                                   |
| `memory`       | `string[]`                                     | Memory source paths (AGENTS.md)                                                                                      |
| `interruptOn`  | `Record<string, boolean \| InterruptOnConfig>` | Tools requiring user approval (HITL)                                                                                 |
| `commands`     | `Array<{ name, description, input? }>`         | Custom slash commands                                                                                                |

## Customization

### Multiple agents

You can expose multiple agents from a single server. The ACP client selects which agent to use when creating a session:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const server = new DeepAgentsServer({
  agents: [
    { name: "code-agent", description: "General coding" },
    { name: "reviewer", description: "Code reviews" },
  ],
});
```

<Note>
  Some ACP clients (like Zed) don't currently expose a UI for selecting between agents. In that case, consider running separate server instances with a single agent each.
</Note>

### Slash commands

The server registers built-in slash commands with the IDE: `/plan`, `/agent`, `/ask`, `/clear`, and `/status`. You can also define custom commands per agent:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const server = new DeepAgentsServer({
  agents: {
    name: "my-agent",
    commands: [
      { name: "test", description: "Run the project's test suite" },
      { name: "lint", description: "Run linter and fix issues" },
      {
        name: "deploy",
        description: "Deploy to staging",
        input: { hint: "environment (staging or production)" },
      },
    ],
  },
});
```

### Human-in-the-loop

Use `interruptOn` to require user approval in the IDE before the agent runs sensitive tools:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const server = new DeepAgentsServer({
  agents: {
    name: "careful-agent",
    interruptOn: {
      execute: { allowedDecisions: ["approve", "edit", "reject"] },
      write_file: true,
    },
  },
});
```

When the agent calls a protected tool, the IDE prompts the user to allow or reject the operation, with options to remember the decision for the session.

### Custom tools

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { DeepAgentsServer } from "deepagents-acp";
import { tool } from "@langchain/core/tools";
import { z } from "zod";

const searchTool = tool(
  async ({ query }) => {
    return `Results for: ${query}`;
  },
  {
    name: "search",
    description: "Search the codebase",
    schema: z.object({ query: z.string() }),
  },
);

const server = new DeepAgentsServer({
  agents: {
    name: "search-agent",
    tools: [searchTool],
  },
});

await server.start();
```

### Custom backend

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { DeepAgentsServer } from "deepagents-acp";
import { CompositeBackend, FilesystemBackend, StateBackend } from "deepagents";

const server = new DeepAgentsServer({
  agents: {
    name: "custom-agent",
    backend: new CompositeBackend({
      routes: [
        {
          prefix: "/workspace",
          backend: new FilesystemBackend({ rootDir: "./workspace" }),
        },
        { prefix: "/", backend: new StateBackend() },
      ],
    }),
  },
});

await server.start();
```

### Skills and memory

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { startServer } from "deepagents-acp";

await startServer({
  agents: {
    name: "project-agent",
    description: "Agent with project-specific knowledge",
    skills: ["./skills/", "~/.deepagents/skills/"],
    memory: ["./.deepagents/AGENTS.md"],
  },
  workspaceRoot: process.cwd(),
});
```

<Info>
  See the upstream ACP docs for protocol details and editor support:

  * Introduction: [https://agentclientprotocol.com/get-started/introduction](https://agentclientprotocol.com/get-started/introduction)
  * Clients/editors: [https://agentclientprotocol.com/get-started/clients](https://agentclientprotocol.com/get-started/clients)
</Info>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/deepagents/acp.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
