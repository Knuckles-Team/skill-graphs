# Contributing to code
Source: https://docs.langchain.com/oss/javascript/contributing/code

Code contributions are welcome! Whether you're fixing bugs, adding features, or improving performance, your contributions help deliver a better developer experience for thousands of developers.

## Getting started

If you are looking for something to work on, check out the issue labeled "help wanted" in our repos:

<Columns>
  <Card title="LangChain" icon="link" href="https://github.com/langchain-ai/deepagents/labels?q=help+wanted">Labels</Card>
  <Card title="LangGraph" icon="topology-ring" href="https://github.com/langchain-ai/langgraphjs/labels?q=help+wanted">Labels</Card>
  <Card title="Deep Agents" icon="robot" href="https://github.com/langchain-ai/deepagentsjs/labels?q=help+wanted">Labels</Card>
</Columns>

<Note>
  Before submitting large **new features or refactors**, please first open an issue or post to [the forum](https://forum.langchain.com/) for discussion. This ensures alignment with project goals and prevents duplicate work.
</Note>

### Quick fix: submit a bugfix

For simple bugfixes, you can get started immediately:

<Steps>
  <Step title="Reproduce the issue">
    Before even cloning the repository, ensure you can reliably reproduce the bug. This helps confirm the issue and provides a starting point for your fix. Maintainers and other contributors should be able to reproduce the issue based on your description without additional setup or modifications.
  </Step>

  <Step title="Fork the repository">
    Fork either the [LangChain](https://github.com/langchain-ai/langchainjs), [LangGraph](https://github.com/langchain-ai/langgraphjs), or [Deep Agents](https://github.com/langchain-ai/deepagentsjs) repo to your <Tooltip>personal GitHub account</Tooltip>
  </Step>

  <Step title="Clone and setup">
    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    git clone https://github.com/your-username/name-of-forked-repo.git

    # For instance, for LangChain:
    git clone https://github.com/parrot123/langchainjs.git

    # For LangGraph:
    git clone https://github.com/parrot123/langgraphjs.git
    ```

    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    # Inside your repo, install dependencies
    pnpm install
    # Create a build for all packages to resolve workspace dependencies
    pnpm build
    ```
  </Step>

  <Step title="Create a branch">
    Create a new branch for your fix. This helps keep your changes organized and makes it easier to submit a pull request later.

    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    git checkout -b your-username/short-bugfix-name
    ```
  </Step>

  <Step title="Write failing tests">
    Add [unit tests](#test-writing-guidelines) that will fail without your fix. This allows us to verify the bug is resolved and prevents regressions
  </Step>

  <Step title="Make your changes">
    Fix the bug while following our [code quality standards](#code-quality-standards). Make the **minimal change necessary** to resolve the issue. We strongly encourage contributors to comment on the issue before they start coding. For example:

    > *"I'd like to work on this. My intended approach would be to \[...brief description...]. Does this align with maintainer expectations?"*

    A 30-second comment often prevents wasted effort if your initial approach is wrong.
  </Step>

  <Step title="Run build">
    Run the build command to ensure the package still builds properly

    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    pnpm build
    # or build a specific workspace package
    pnpm --filter @langchain/core build
    ```
  </Step>

  <Step title="Verify the fix">
    Ensure that tests pass and no regressions are introduced. Ensure all tests pass locally before submitting your PR

    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    pnpm lint
    pnpm test

    # For bugfixes involving integrations, also run:
    pnpm test:int

    # Or run tests in a specific workspace package
    cd libs/langchain-core
    pnpm test
    pnpm lint

    # Or run tests for a specific package from the root of the repo
    pnpm --filter @langchain/core test
    pnpm --filter @langchain/core lint
    ```
  </Step>

  <Step title="Document the change">
    Update docstrings and/or inline comments if behavior changes
  </Step>

  <Step title="Submit a pull request">
    Follow the PR template provided. If applicable, reference the issue you're fixing using a [closing keyword](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue#linking-a-pull-request-to-an-issue-using-a-keyword) (e.g. `Fixes #ISSUE_NUMBER`) so that the issue is automatically closed when your PR is merged.
  </Step>
</Steps>

### Full development setup

For ongoing development or larger contributions:

1. Review our [contribution guidelines](#contribution-guidelines) for features, bugfixes, and integrations
2. Set up your environment following our [setup guide](#development-environment) below
3. Understand the [repository structure](#repository-structure) and package organization
4. Learn our [development workflow](#development-workflow) including testing and linting

***

## Contribution guidelines

Before you start contributing to LangChain projects, take a moment to think about why you want to. If your only goal is to add a "first contribution" to your resume (or if you're just looking for a quick win) you might be better off doing a boot-camp or an online tutorial.

Contributing to open source projects takes time and effort, but it can also help you become a better developer and learn new skills. However, it's important to know that it might be harder and slower than following a training course. That said, contributing to open source is worth it if you're willing to take the time to do things well!

### Backwards compatibility

<Warning>
  Breaking changes to public APIs are not allowed except for critical security fixes.

  See our [versioning policy](/oss/javascript/versioning) for details on major version releases.
</Warning>

Maintain compatibility via:

<AccordionGroup>
  <Accordion title="Stable interfaces">
    **Always preserve**:

    * Function signatures and parameter names
    * Class interfaces and method names
    * Return value structure and types
    * Import paths for public APIs
  </Accordion>

  <Accordion title="Safe changes">
    **Acceptable modifications**:

    * Adding new optional parameters/type parameters

    * Adding new methods to classes

    * Improving performance without changing behavior

    * Adding new modules or functions
  </Accordion>

  <Accordion title="Before making changes">
    * **Would this break existing user code?**

    * Check if your target is public

    * Are there existing usage patterns in tests?
  </Accordion>
</AccordionGroup>

### New features

We aim to keep the bar high for new features. We generally don't accept new core abstractions from outside contributors without an existing issue that demonstrates an acute need for them. This also applies to changes to infrastructure and dependencies.

In general, feature contribution requirements include:

<Steps>
  <Step title="Design discussion">
    Open an issue describing:

    * The problem you're solving
    * Proposed API design
    * Expected usage patterns
  </Step>

  <Step title="Implementation">
    * Follow existing code patterns
    * Include comprehensive tests and documentation
    * Consider security implications
  </Step>

  <Step title="Integration considerations">
    * How does this interact with existing features?
    * Are there performance implications?
    * Does this introduce new dependencies?

    We will reject features that are likely to lead to security vulnerabilities or reports.
  </Step>
</Steps>

### Security guidelines

<Warning>
  Security is paramount. Never introduce vulnerabilities or unsafe patterns.
</Warning>

Security checklist:

<AccordionGroup>
  <Accordion title="Input validation">
    * Validate and sanitize all user inputs

    * Properly escape data in templates and queries

    * Never use `eval()`, as this can lead to arbitrary code execution vulnerabilities
  </Accordion>

  <Accordion title="Error handling">
    * Use specific exception types
    * Don't expose sensitive information in error messages
    * Implement proper resource cleanup
  </Accordion>

  <Accordion title="Dependencies">
    * Avoid adding hard dependencies
    * Keep optional dependencies minimal
    * Review third-party packages for security issues
  </Accordion>
</AccordionGroup>

***

## Development environment

<Tip>
  **Using an AI coding agent?** Install [LangChain Skills](https://github.com/langchain-ai/langchain-skills) to improve your agent's performance on LangChain ecosystem tasks, then click the "Copy page" button on the top right of this page and paste the raw content into your agent to have it set up your environment automatically.
</Tip>

<Warning>
  Our JS/TS projects uses [`pnpm`](https://pnpm.io/) for dependency management. Make sure you have the latest version installed, or run `corepack enable` (on Node 24+) to setup the required pnpm version.
</Warning>

<Info>
  We strive to keep setup consistent across all JS/TS packages. From the repo root, run:

  ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pnpm install
  pnpm --filter {package-name} test  # Verify tests pass before starting development
  ```
</Info>

Once you've reviewed the [contribution guidelines](#contribution-guidelines), find the package directory for the component you're working on in the [repository structure](#repository-structure) section below.

***

## Repository structure

<Tabs>
  <Tab title="LangChain" icon="link">
    LangChain is organized as a monorepo with multiple packages:

    <AccordionGroup>
      <Accordion title="Core packages">
        * **[`langchain`](https://github.com/langchain-ai/langchainjs/tree/main/langchain#readme)** (located in `libs/langchain/`): Main package with chains, agents, and retrieval logic
        * **[`@langchain/core`](https://github.com/langchain-ai/langchainjs/tree/main/langchain-core#readme)** (located in `libs/langchain-core/`): Base interfaces and core abstractions
      </Accordion>

      <Accordion title="Partner packages">
        Located in `libs/providers/`, these are independently versioned packages for specific integrations. For example:

        * **[`@langchain/openai`](https://github.com/langchain-ai/langchainjs/tree/main/libs/langchain-openai#readme)**: [OpenAI](/oss/javascript/integrations/providers/openai) integrations
        * **[`@langchain/anthropic`](https://github.com/langchain-ai/langchainjs/tree/main/libs/langchain-anthropic#readme)**: [Anthropic](/oss/javascript/integrations/providers/anthropic) integrations
        * **[`@langchain/google`](https://github.com/langchain-ai/langchainjs/tree/main/libs/providers/langchain-google#readme)**: [Google](/oss/javascript/integrations/providers/google) integrations
      </Accordion>

      <Accordion title="Supporting packages">
        * **[`@langchain/textsplitters`](https://github.com/langchain-ai/langchainjs/tree/main/libs/langchain-textsplitters#readme)**: Text splitting utilities
        * **[`@langchain/standard-tests`](https://github.com/langchain-ai/langchainjs/tree/main/libs/langchain-standard-tests#readme)**: Standard test suites for integrations
      </Accordion>
    </AccordionGroup>
  </Tab>

  <Tab title="LangGraph" icon="topology-ring">
    LangGraph is organized as a monorepo with multiple Python packages:

    <AccordionGroup>
      <Accordion title="Core packages">
        * **[`langgraph`](https://github.com/langchain-ai/langgraph/tree/main/libs/langgraph#readme)** (located in `libs/langgraph/`): Core framework for building stateful, multi-actor agents
        * **[`langgraph-prebuilt`](https://github.com/langchain-ai/langgraph/tree/main/libs/prebuilt#readme)** (located in `libs/prebuilt/`): High-level APIs for creating and running agents and tools
      </Accordion>

      <Accordion title="Checkpoint packages">
        * **[`langgraph-checkpoint`](https://github.com/langchain-ai/langgraph/tree/main/libs/checkpoint#readme)** (located in `libs/checkpoint/`): Base interfaces for checkpoint savers
        * **[`langgraph-checkpoint-postgres`](https://github.com/langchain-ai/langgraph/tree/main/libs/checkpoint-postgres#readme)** (located in `libs/checkpoint-postgres/`): Postgres implementation
        * **[`langgraph-checkpoint-sqlite`](https://github.com/langchain-ai/langgraph/tree/main/libs/checkpoint-sqlite#readme)** (located in `libs/checkpoint-sqlite/`): SQLite implementation
      </Accordion>

      <Accordion title="SDK and CLI">
        * **[`langgraph-sdk`](https://github.com/langchain-ai/langgraph/tree/main/libs/sdk-py#readme)** (located in `libs/sdk-py/`): Python SDK for the Agent Server API
        * **[`langgraph-cli`](https://github.com/langchain-ai/langgraph/tree/main/libs/cli#readme)** (located in `libs/cli/`): Official command-line interface
      </Accordion>
    </AccordionGroup>
  </Tab>

  <Tab title="Deep Agents" icon="robot">
    Deep Agents is organized as a monorepo with multiple Python packages:

    <AccordionGroup>
      <Accordion title="Core packages">
        * **[`deepagents`](https://github.com/langchain-ai/deepagents/tree/main/libs/deepagents#readme)** (located in `libs/deepagents/`): Core framework for building deep agents with planning, filesystem, and subagent capabilities
        * **[`deepagents-code`](https://github.com/langchain-ai/deepagents/tree/main/libs/code#readme)** (located in `libs/code/`): Deep Agents Code — interactive terminal interface with conversation resume, web search, and sandboxes
        * **[`deepagents-cli`](https://github.com/langchain-ai/deepagents/tree/main/libs/cli#readme)** (located in `libs/cli/`): Deploy tooling (`deepagents deploy`, `deepagents init`, `deepagents dev`) for shipping agents to LangSmith Deployments
      </Accordion>

      <Accordion title="Integration packages">
        * **[`deepagents-harbor`](https://github.com/langchain-ai/deepagents/tree/main/libs/harbor#readme)** (located in `libs/harbor/`): Harbor integration with LangSmith tracing
        * **[`deepagents-acp`](https://github.com/langchain-ai/deepagents/tree/main/libs/acp#readme)** (located in `libs/acp/`): Agent Client Protocol integration
      </Accordion>
    </AccordionGroup>
  </Tab>
</Tabs>

***

## Development workflow

### Pre-commit hooks

### Running tests

<Info>
  Directories are relative to the package you're working in.
</Info>

We favor unit tests over integration tests when possible. Unit tests run on every pull request, so they should be fast and reliable. Integration tests run on a schedule and require more setup, so they should be reserved for confirming interface points with external services.

#### Unit tests

**Location**: `src/tests/FILENAME_BEING_TESTED.test.ts`

Unit tests cover modular logic that does not require calls to outside APIs. If you add new logic, you should add a unit test. In unit tests, check pre/post processing and mock external dependencies.

**Requirements**:

* No network calls allowed
* Test all code paths including edge cases
* Use mocks for external dependencies

To run unit tests:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# Run the entire test suite
pnpm test

# Or run a specific test file
pnpm test src/tests/FILENAME_BEING_TESTED.test.ts

# Or run a specific test function
pnpm test -t "the test that should be run"
```

#### Integration tests

**Location**: `src/tests/FILENAME_BEING_TESTED.int.test.ts`

Integration tests cover logic that requires making calls to outside APIs (often integration with other services).

Integration tests require access to external services/provider APIs (which can cost money) and therefore are not run by default.

Not every code change will require an integration test, but keep in mind that we'll require/run integration tests separately as part of our review process.

**Requirements**:

* Test real integrations with external services
* Use environment variables for API keys
* Skip gracefully if credentials unavailable

To run integration tests:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
pnpm test:int
```

### Code quality standards

Contributions must adhere to the following quality requirements:

<Tabs>
  <Tab title="Type hints">
    **Required**: Complete types for all functions

    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    function processDocuments(
        docs: Document[],
        processor: DocumentProcessor,
        batchSize: number = 100
    ): ProcessingResult {
        // ...
    }
    ```
  </Tab>

  <Tab title="Documentation">
    **Required**: [JSDocs](https://jsdoc.app/about-getting-started) for all exported functions and interfaces

    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    /**
     * Document processing instance.
     */
    interface FooDocumentProcessor {
        /**
         * Process documents in batches.
         *
         * @param docs - List of documents to process.
         * @returns Processing results with success/failure counts.
         */
        process(docs: Document[]): ProcessingResult;
    }

    /**
     * Process documents in batches.
     *
     * @param docs - List of documents to process.
     * @param processor - Document processing instance.
     * @param batchSize - Number of documents per batch.
     * @returns Processing results with success/failure counts.
     */
    export function processDocuments(
        docs: Document[],
        processor: DocumentProcessor,
        batchSize: number = 100
    ): ProcessingResult {
        // ...
    }
    ```
  </Tab>

  <Tab title="Code style">
    **Automated**: Formatting and linting:

    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    pnpm lint    # Check style and types
    pnpm format  # Apply formatting
    ```

    **Standards**:

    * Descriptive variable names
    * Break up complex functions (aim for fewer than 20 lines)
    * Follow existing patterns in the codebase
  </Tab>
</Tabs>

***

### Test writing guidelines

In order to write effective tests, there's a few good practices to follow:

* Encapsulate the test in a `describe` block that describes the component being tested
* Use natural language to describe the test name
* Be exhaustive with assertions
* Only use snapshots for reasonably sized data objects

<Tabs>
  <Tab title="Unit tests">
    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    describe("DocumentProcessor", () => {
        it("Should handle empty document list", () => {
            const processor = new DocumentProcessor();
            const result = processor.process([]);

            expect(result.success).toBe(true);
            expect(result.processedCount).toBe(0);
            expect(result.errors).toHaveLength(0);
        });
    });
    ```
  </Tab>

  <Tab title="Integration tests">
    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    describe("ChatOpenAI", () => {
        it("Should test with real API", () => {
            const chat = new ChatOpenAI();
            const response = chat.invoke("Hello");
        });
    });
    ```
  </Tab>

  <Tab title="Mock usage">
    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    describe("APIService", () => {
        it("Should call with retry", () => {
            const mockClient = new MockClient();
            const service = new APIService(client: mockClient);
            const result = service.callWithRetry();
        });
    });
    ```
  </Tab>
</Tabs>

### Submitting your PR

Once your tests pass and code meets quality standards:

1. Push your branch and open a pull request
2. Follow the provided PR template
3. Reference related issues using a [closing keyword](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue#linking-a-pull-request-to-an-issue-using-a-keyword) (e.g., `Fixes #123`)
4. Wait for CI checks to complete

<Note>
  If your PR includes AI-generated content, you must follow our [acceptable uses of LLMs](/oss/javascript/contributing/overview#acceptable-uses-of-llms) policy. PRs that appear to be low-effort, AI-generated spam will be closed without comment.
</Note>

<Warning>
  Address CI failures promptly. Maintainers may close PRs that do not pass CI within a reasonable timeframe.
</Warning>

## Getting help

Our goal is to have the most accessible developer setup possible. Should you experience any difficulty getting setup, please ask in the [community slack](https://www.langchain.com/join-community) or open a [forum post](https://forum.langchain.com/).

<Check>
  You're now ready to contribute high-quality code to LangChain!
</Check>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/contributing/code.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Co-marketing
Source: https://docs.langchain.com/oss/javascript/contributing/comarketing

With over 60 million monthly downloads, LangChain has a large audience of developers building LLM applications. Beyond just listing integrations, we aim to highlight high-quality, educational examples that inspire developers and advance the ecosystem.

<Note>
  While we occasionally share integrations, we prioritize content that provides
  meaningful insights and best practices. Our main social channels are [Twitter](https://x.com/LangChain) and
  [LinkedIn](https://www.linkedin.com/company/langchain/), where we highlight the best examples.
</Note>

### Content we're excited to promote

<AccordionGroup>
  <Accordion title="Educational content" icon="school">
    Blogs, YouTube videos and other media showcasing educational content. Note that we prefer content that is NOT framed as "here's how to use integration XYZ", but rather "here's how to do ABC", as we find that is more educational and helpful for developers.
  </Accordion>

  <Accordion title="End-to-end applications" icon="cube">
    End-to-end applications are great resources for developers looking to build. We prefer to highlight applications that are more complex/agentic in nature, and that use [LangGraph](https://github.com/langchain-ai/langgraphjs) as the orchestration framework. We get particularly excited about anything involving:

    * Long-term memory systems
    * Human-in-the-loop interaction patterns
    * Multi-agent architectures
  </Accordion>

  <Accordion title="Research" icon="flask">
    We love highlighting novel research! Whether it is research built on top of LangChain or that integrates with it.
  </Accordion>
</AccordionGroup>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/contributing/comarketing.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Contributing to documentation
Source: https://docs.langchain.com/oss/javascript/contributing/documentation

We welcome contributions to LangChain documentation, including new features, [integrations](/oss/javascript/contributing/publish-langchain), and improvements to existing docs.

## Quick start - local development

To run a local preview of the documentation:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
git clone https://github.com/langchain-ai/docs.git
```

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
cd docs
```

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
make install
```

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
make dev
```

This starts a development server with hot reload at `http://localhost:3000`. Edit files in `src/` and see changes immediately.

<Tip>
  **Using an AI coding agent?** Install [LangChain Skills](https://github.com/langchain-ai/langchain-skills) to improve your agent's performance on LangChain ecosystem tasks, then click the "Copy page" button on the top right of this page and paste the raw content into your agent to have it set up your environment automatically.
</Tip>

<Tip>
  If you are having issues with you local preview, try running `mint update` to ensure you're using the latest Mintlify version.
</Tip>

<Accordion title="Prerequisites">
  **Required:**

  * Python 3.13+
  * [uv](https://docs.astral.sh/uv/) - Python package manager
  * [Node.js](https://nodejs.org/en) and npm
  * [Make](https://www.gnu.org/software/make/)
  * [Git](https://git-scm.com/)

  **Optional:**

  * [markdownlint-cli](https://github.com/igorshubovych/markdownlint-cli) - `npm install -g markdownlint-cli`
  * [Mintlify MDX VSCode extension](https://www.mintlify.com/blog/mdx-vscode-extension)
</Accordion>

## Edit documentation

<Accordion title="Quick edits on GitHub">
  For typos or small changes, edit directly on GitHub without local setup:

  1. Click **Edit this page on GitHub** at the bottom of any page.
  2. Fork to your personal account.
  3. Make changes in GitHub's web editor.
  4. Create a pull request.
</Accordion>

<Note>
  **Only edit files in `src/`**-- The `build/` directory is automatically generated.
</Note>

1. Edit files in `src/` following our [writing standards](#writing-standards).
2. Run [quality checks](#run-quality-checks) before submitting.
3. Create a pull request for review.

<Note>
  All pull requests must link to an issue or discussion where a solution has been approved by a maintainer. See our [pull request requirements](/oss/javascript/contributing/overview#pull-request-requirements).
</Note>

<Accordion title="Create a sharable preview build (LangChain team only)">
  When you create or update a PR, a [preview branch/ID](https://github.com/langchain-ai/docs/actions/workflows/create-preview-branch.yml) is automatically generated. A comment will be left on the PR with the ID.

  1. Copy the preview branch's ID from the comment
  2. In the [Mintlify dashboard](https://dashboard.mintlify.com/langchain-5e9cc07a/langchain-5e9cc07a?section=previews), click **Create preview deployment**
  3. Enter the preview branch's ID and click **Create deployment**
  4. Select the preview and click **Visit** to view

  To redeploy with latest changes, click **Redeploy** on the dashboard.
</Accordion>

### Run quality checks

Before submitting changes, ensure your code passes formatting and linting checks:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# Check broken links
make broken-links

# Format code automatically
make format

# Check for linting issues
make lint

# Fix markdown issues
make lint_md_fix

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

How-to guides are task-oriented instructions for users who know what they want to accomplish. Examples of how-to guides are on the [LangChain](/oss/javascript/langchain/overview) and [LangGraph](/oss/javascript/langgraph/overview) tabs.

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
    * [Messages](/oss/javascript/langchain/messages)
    * [Tools](/oss/javascript/langchain/tools)
    * [Streaming](/oss/javascript/langgraph/streaming)
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
    * [Memory](/oss/javascript/concepts/memory)
    * [Context](/oss/javascript/concepts/context)
    * [Graph API](/oss/javascript/langgraph/graph-api)
    * [Functional API](/oss/javascript/langgraph/functional-api)
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

Tutorials are longer form step-by-step guides that builds upon itself and takes users through a specific practical activity to build understanding. Tutorials are typically found on the [Learn](/oss/javascript/learn) tab.

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
    * [Semantic search](/oss/javascript/langchain/knowledge-base)
    * [RAG agent](/oss/javascript/langchain/rag)
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
Source: https://docs.langchain.com/oss/javascript/contributing/implement-langchain

Integration packages are Python packages that users can install for use in their projects. They implement one or more components that adhere to the LangChain interface standards.

LangChain components are subclasses of base classes in [`langchain-core`](https://github.com/langchain-ai/langchain/tree/master/libs/core). Examples include [chat models](/oss/javascript/integrations/chat), [tools](/oss/javascript/integrations/tools), [retrievers](/oss/javascript/integrations/retrievers), and more.

Your integration package will typically implement a subclass of at least one of these components. Expand the tabs below to see details on each.

<Tabs>
  <Tab title="Chat Models">
    Chat models are subclasses of the [`BaseChatModel`](https://reference.langchain.com/javascript/langchain-core/language_models/chat_models/BaseChatModel) class. They implement methods for generating chat completions, handling message formatting, and managing model parameters.

    <Warning>
      The chat model integration guide is currently WIP. In the meantime, read the [chat model conceptual guide](/oss/javascript/langchain/models) for details on how LangChain chat models function. You may also refer to existing integrations in the [LangChain repo](https://github.com/langchain-ai/langchainjs/tree/main/libs/providers)
    </Warning>
  </Tab>

  <Tab title="Embeddings">
    Embedding models are subclasses of the [`Embeddings`](https://reference.langchain.com/javascript/langchain-core/embeddings/Embeddings) class.

    <Warning>
      The embedding model integration guide is currently WIP. In the meantime, read the [embedding model conceptual guide](/oss/javascript/integrations/embeddings) for details on how LangChain embedding models function.
    </Warning>
  </Tab>

  <Tab title="Tools">
    Tools are used in 2 main ways:

    1. To define an "input schema" or "args schema" to pass to a chat model's tool calling feature along with a text request, such that the chat model can generate a "tool call", or parameters to call the tool with.
    2. To take a "tool call" as generated above, and take some action and return a response that can be passed back to the chat model as a ToolMessage.

    The Tools class must inherit from the [`BaseTool`](https://reference.langchain.com/javascript/classes/_langchain_core.tools.StructuredTool.html) base class. This interface has 3 properties and 2 methods that should be implemented in a subclass.

    <Warning>
      The tools integration guide is currently WIP. In the meantime, read the [tools conceptual guide](/oss/javascript/langchain/tools) for details on how LangChain tools function.
    </Warning>
  </Tab>

  <Tab title="Middleware">
    [Middleware](/oss/javascript/langchain/middleware/overview) lets you customize agent behavior by hooking into model calls, tool calls, and agent lifecycle events. Middleware classes subclass the [`AgentMiddleware`](https://reference.langchain.com/javascript/langchain/index/AgentMiddleware) base class.

    Read the [custom middleware guide](/oss/javascript/langchain/middleware/custom) to understand hooks, state updates, and middleware patterns before building an integration.

    Middleware integrations typically fall into two categories:

    | Type                  | Description                                | Examples                                                  |
    | --------------------- | ------------------------------------------ | --------------------------------------------------------- |
    | **Provider-specific** | Leverages a provider's unique capabilities | Prompt caching, native tool execution, content moderation |
    | **Cross-provider**    | Works with any model or tool               | Rate limiting, PII detection, logging, guardrails         |

    Provider-specific middleware lives in the provider's integration package (for example `langchain-anthropic`). Cross-provider middleware can be published as a standalone package.

    You can also use these existing middleware integrations as reference:

    <CardGroup>
      <Card title="Anthropic middleware" icon="robot" href="/oss/javascript/integrations/middleware/anthropic">
        Multiple middleware classes for prompt caching, tools, memory, and file search.
      </Card>

      <Card title="Custom middleware guide" icon="code" href="/oss/javascript/langchain/middleware/custom">
        Full reference for hooks, state updates, and patterns.
      </Card>
    </CardGroup>
  </Tab>

  <Tab title="Checkpointers">
    Checkpointers enable [persistence](/oss/javascript/langgraph/persistence) in LangGraph, allowing agents to save and resume state across interactions.

    See existing checkpointer integrations in the [LangGraph repo](https://github.com/langchain-ai/langgraph/tree/main/libs) for implementation examples.
  </Tab>

  <Tab title="Sandboxes">
    Sandbox integrations enable [Deep Agents](/oss/javascript/deepagents/overview) to run code in isolated environments.
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
