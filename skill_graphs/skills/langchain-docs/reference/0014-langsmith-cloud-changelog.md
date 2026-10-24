# LangSmith Cloud changelog
Source: https://docs.langchain.com/langsmith/changelog

Weekly updates to LangSmith Cloud

Weekly updates to [LangSmith Cloud](/langsmith/observability) and [LangSmith Fleet](/langsmith/fleet).

<Callout icon="rss">
  **Subscribe**: This changelog includes an [RSS feed](https://docs.langchain.com/langsmith/product-changelog/rss.xml) that can integrate with [Slack](https://slack.com/help/articles/218688467-Add-RSS-feeds-to-Slack), [email](https://zapier.com/apps/email/integrations/rss/1441/send-new-rss-feed-entries-via-email), Discord bots like [Readybot](https://readybot.io/) or [RSS Feeds to Discord Bot](https://rss.app/en/bots/rssfeeds-discord-bot), and other subscription tools.
</Callout>

<Info>
  If you use self-hosted LangSmith, see the [self-hosted changelog](/langsmith/self-hosted-changelog) for updates.
</Info>

<Tabs>
  <Tab title="LangSmith Cloud">
    <Update label="June 1-5, 2026">
      ## Observability and evaluations

      ### Automations

      * [Run rule](/langsmith/rules) webhook payloads now include a trace deep link for each run, so downstream systems can jump straight back to the trace.

      ### Engine

      * Per-workspace [Engine](/langsmith/engine) spend is now generally available: you can view LCU and USD spend directly on the Engine settings page, including session-level spend.
      * The Engine settings page now surfaces additional Engine details in one place.
      * You can rotate [Engine issue-board webhook](/langsmith/engine-webhooks) signing secrets from both the API and the webhook settings UI.
      * The Engine issues list adds a sort option by trace count.

      ### Datasets and experiments

      * A new out-of-the-box [Assertions evaluator](/langsmith/assertions) scores outputs against an explicit list of criteria specified in the reference output, and an Assertions rule is auto-attached when you add assertion-style examples to a dataset.
      * Evaluator metrics are improved in the experiment detail, [comparison](/langsmith/compare-experiment-results), and global experiments tables.

      ### Prompts and playground

      * The [Playground](/langsmith/playground-model-providers) supports Amazon Bedrock API key authentication, letting you authenticate with a bearer token instead of AWS credentials.

      ### Tracing

      * The [trace view](/langsmith/view-traces) now shows an unread indicator on a run's actions menu when the run has reviewer notes you have not seen yet.
      * The waterfall view is now full-height with sticky turn headers, so you keep your place while scrolling through long traces.
      * Global search now includes context and sandboxes

      ## Deployment

      * You can now trigger a LangSmith Deployment from the [Studio](/langsmith/studio) page.
      * LangSmith Deployment now supports [deploying Google Agent Development Kit (ADK) agents](/langsmith/deploy-google-adk).

      ## Sandboxes

      * [Sandbox proxy rules](/langsmith/sandbox-auth-proxy) now support configuring AWS authentication, so sandboxes can reach AWS services through the proxy with signed requests.
      * Sandboxes can create [snapshots](/langsmith/sandbox-snapshots) from a Dockerfile build source.

      ## Admin and billing

      ### Administration

      * Organization admins can now disable personal access token creation from the [organization settings](/langsmith/administration-overview) page.

      ### Usage and billing

      * [Granular billable usage](/langsmith/granular-usage) now supports filtering and grouping by retention tier, separating long-lived from short-lived traces.
      * The Granular Billable Usage page now surfaces LangSmith Deployment usage, including nodes executed, agent runs, and agent uptime, alongside trace usage.

      ## Fixes

      * Performance improvements for the loading of large traces.
      * Filter values for metadata are now preserved when you reopen a filter dropdown to edit it.
      * Dataset creation now uses a multi-select dropdown for choosing CSV fields.
    </Update>
  </Tab>

  <Tab title="LangSmith Fleet">
    <Update label="June 1-5, 2026">
      ## New features

      * [Skills](/langsmith/fleet/skills) load faster: the skills list fetches lightweight metadata first and loads file contents only when you open a skill.
      * The agent creation menu adds a [Templates](/langsmith/fleet/templates) entry.
      * The [remote MCP](/langsmith/fleet/remote-mcp-servers) authorization screen now shows the connecting application's name, logo, and homepage, terms, and privacy links instead of its raw client ID.
      * [Slack integration](/langsmith/fleet/slack-app) available in AWS and APAC regions.

      ## Fixes

      * [Scheduled (cron) execution](/langsmith/fleet/schedules) is restored for enterprise Fleet agents.
      * Long-running agent runs and agent-builder generations are no longer cut off after 60 seconds.
      * The Gmail read-emails [tool](/langsmith/fleet/tools) now returns results when you search sent mail with an `in:sent` query.
      * Scrolling is improved for long toolbox, skill, and sub-agent lists in the agent editor, and webhook dialogs now scroll within the viewport.
    </Update>
  </Tab>
</Tabs>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/changelog.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# LangSmith Chat
Source: https://docs.langchain.com/langsmith/chat

Use Chat in LangSmith to analyze traces, threads, prompts, and evaluations.

**LangSmith Chat** (formerly Polly) is built directly into your LangSmith [workspace](/langsmith/administration-overview#workspaces) to help you analyze and understand your application data.

Chat helps you gain insight from your traces, conversation threads, and prompts without having to dig through data manually. By asking natural language questions, you can quickly understand agent performance, debug issues, and analyze user sentiment.

<img alt="LangSmith Chat icon" /> Chat appears in the right-hand bottom corner of the following locations within [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-chat):

<br /><br />**Observability & Debugging:**

* [Projects](#projects): Browse and filter runs across a project.
* [Trace pages](#trace-pages): Analyze individual runs and execution traces.
* [Thread views](#thread-views): Understand conversation threads and user interactions.

**Prompt Engineering:**

* [Playground](#playground): Edit and optimize prompts.
* [Prompt Hub pages](#prompt-hub-pages): Explore and understand shared prompts.

**Evaluation & Testing:**

* [Dataset Experiments](#dataset-experiments): Analyze experiment results and compare runs.
* [Dataset Examples](#dataset-examples): Browse and understand dataset structure.
* [Annotation Queues](#annotation-queues): Review runs and make informed annotation decisions.
* [Evaluators](#evaluators): Build and refine evaluators with AI assistance.

<img alt="Chat in the sidebar on a dataset view." />

<img alt="Chat in the sidebar on a dataset view." />

## Get started

Before you start using Chat, you need to add an API key for the model you're using:

In the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=snippets-langsmith-set-workspace-secrets), ensure that your API key is set as a [workspace secret](/langsmith/set-up-hierarchy#configure-workspace-settings).

1. Navigate to <Icon icon="settings" /> **Settings** and then move to the **Secrets** tab.
2. Select **Add secret** and enter the key environment variable (e.g.,`OPENAI_API_KEY` or `ANTHROPIC_API_KEY`) and your API key as the **Value**.
3. Select **Save secret**.

<Note> When adding workspace secrets in the LangSmith UI, make sure the secret keys match the environment variable names expected by your model provider.</Note>

<Note>
  Chat calls model providers from LangSmith's egress IP addresses. If your model provider (or a proxy in front of it) restricts traffic by IP, allowlist the LangSmith egress IPs listed in [Allowlist IP addresses](/langsmith/deploy-to-cloud#allowlist-ip-addresses).
</Note>

### Supported models

Chat supports the following model providers out of the box:

* Anthropic (Claude)
* OpenAI
* Google Gemini
* AWS Bedrock
* Groq
* Mistral
* xAI
* DeepSeek
* Fireworks AI

You can also use any custom model you've configured in [Playground Settings](/langsmith/prompt-engineering-concepts#playground) by enabling the **Available in Chat** toggle on that configuration. Workspace admins manage which custom models are available.

### Keyboard shortcuts

| Action                  | Mac           | Windows/Linux  |
| ----------------------- | ------------- | -------------- |
| Toggle Chat open/closed | `Cmd+I`       | `Ctrl+I`       |
| Clear current thread    | `Cmd+Shift+O` | `Ctrl+Shift+O` |

## Observability

### Projects

On a project's run list, Chat can browse and filter runs across the entire project, create datasets, and add examples. Use Chat to quickly explore what's happening across your traces without manually paging through results.

**Example questions:**

* "Show me all the failed runs from the last 24 hours"
* "Which runs took the longest?"
* "Add the failing runs to my test dataset"
* "How many runs errored this week?"

### Trace pages

On an individual [trace](/langsmith/observability-concepts#traces), Chat analyzes the [run](/langsmith/observability-concepts#runs) data and execution trajectory. Chat examines the full trace context, including [run metadata](/langsmith/observability-concepts#metadata), inputs, outputs, intermediate steps, and configuration to help you understand what happened and identify areas for improvement.

**Example questions:**

* "Is there anything that the agent could have done better here?"
* "Why did this run fail?"
* "What took the most time in this trace?"
* "Summarize what happened in this trace"

### Thread views

Under the **Threads** tab, Chat analyzes conversation [threads](/langsmith/observability-concepts#threads) to help you understand user sentiment, conversation outcomes, and interaction patterns. Use Chat to identify user pain points and understand whether issues were resolved.

**Example questions:**

* "Did the user seem frustrated?"
* "What issues is the user experiencing?"
* "Was the user's problem solved?"
* "What was the main topic of this thread?"

## Prompt engineering

### Playground

In the [Playground](/langsmith/prompt-engineering-concepts#playground), Chat helps you edit and optimize your [prompts](/langsmith/prompt-engineering-concepts#prompts-in-langsmith). Use automated options like **Optimize prompt**, **Generate a tool**, or **Generate an output schema**, or give Chat custom instructions for editing your prompt. Chat can directly modify the playground state—updating messages, tools, output schemas, and examples—so you can iterate on prompts conversationally.

**Example questions:**

* "Make it respond in Italian"
* "Add more context about the user's role"
* "Make the tone more professional"
* "Simplify the instructions"

### Prompt Hub pages

When viewing a prompt in the [LangSmith Hub](/langsmith/prompt-engineering-concepts#prompts-in-langsmith), Chat helps you understand the prompt's structure, messages, tools, and configuration. This is useful for exploring and learning from shared prompts.

**Example questions:**

* "What does this prompt do?"
* "What tools does this prompt use?"
* "Explain the structure of this prompt"
* "What are the key instructions in this prompt?"

## Evaluation

### Dataset Experiments

On the **Datasets** page under the **Experiments** tab, Chat analyzes experiment results and helps you compare runs across different experiments. Chat can identify patterns, summarize performance, and help you understand which approaches work best.

**Example questions:**

* "Which experiment performed best?"
* "What are the main differences between these runs?"
* "Summarize the results of this experiment"
* "What patterns do you see in the failures?"

### Dataset Examples

On the **Datasets** page under the **Examples** tab, Chat helps you understand your dataset structure, browse examples, and identify data patterns. This is useful for understanding what data you're working with and preparing datasets for experiments.

**Example questions:**

* "What type of data is in this dataset?"
* "Show me examples with errors"
* "What patterns do you see in the inputs?"
* "How many examples are in this dataset?"

### Annotation Queues

In **Annotation Queues**, Chat helps you analyze runs before making annotation decisions. Whether you're reviewing runs individually or comparing them pairwise, Chat provides insights into run behavior, errors, and execution patterns to inform your scoring.

**Example questions:**

* "What went wrong in this run?"
* "Summarize what happened in this run"
* "Compare these two runs"
* "What should I consider when scoring this?"

### Evaluators

In the **Evaluators** builder, Chat helps you write and refine evaluator logic. Chat can generate evaluator code, suggest improvements, and help you test your evaluator against examples.

**Example questions:**

* "Write an evaluator that checks for hallucinations"
* "Improve the accuracy of this evaluator"
* "What does this evaluator check for?"
* "Add handling for edge cases"

## What's next

Learn more about the features that Chat helps you explore:

<CardGroup>
  <Card title="Observability" icon="search" href="/langsmith/observability">
    Learn more about tracing and monitoring your LLM applications
  </Card>

  <Card title="Threads" icon="messages" href="/langsmith/threads">
    Understand how threads work in LangSmith
  </Card>

  <Card title="Prompt Engineering" icon="wand" href="/langsmith/prompt-engineering">
    Create and iterate on prompts in the Playground
  </Card>

  <Card title="Evaluation" icon="clipboard-check" href="/langsmith/evaluation">
    Evaluate and test your applications systematically
  </Card>
</CardGroup>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/chat.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# LangSmith Chat
Source: https://docs.langchain.com/langsmith/chat-evaluation

Use Chat to analyze evaluations and experiments.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/chat-evaluation.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# LangSmith Chat
Source: https://docs.langchain.com/langsmith/chat-observability

Use Chat to analyze traces and runs.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/chat-observability.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# LangSmith Chat
Source: https://docs.langchain.com/langsmith/chat-prompt-engineering

Use Chat to optimize prompts in the Playground.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/chat-prompt-engineering.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Implement a CI/CD pipeline using LangSmith Deployment and Evaluation
Source: https://docs.langchain.com/langsmith/cicd-pipeline-example

This guide demonstrates how to implement a comprehensive CI/CD pipeline for AI agent applications deployed in LangSmith Deployment. In this example, you'll use the [LangGraph](/oss/python/langgraph/overview) open source framework for orchestrating and building the agent, [LangSmith](/langsmith/observability) for observability and evaluations. This pipeline is based on the [cicd-pipeline-example repository](https://github.com/langchain-ai/cicd-pipeline-example).

## Overview

The CI/CD pipeline provides:

* <Icon icon="circle-check" /> **Automated testing**: Unit, integration, and end-to-end tests.
* <Icon icon="chart-line" /> **Offline evaluations**: Performance assessment using [AgentEvals](/oss/python/langchain/test/evals), [OpenEvals](/langsmith/openevals#setup) and [LangSmith](/langsmith/observability).
* <Icon icon="rocket" /> **Preview and production deployments**: Automated staging and quality-gated production releases using the Control Plane API.
* <Icon icon="eye" /> **Monitoring**: Continuous evaluation and alerting.

## Pipeline architecture

The CI/CD pipeline consists of several key components that work together to ensure code quality and reliable deployments:

```mermaid theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
graph TD
    A1[Code or Graph Change] --> B1[Trigger CI Pipeline]
    A2[Prompt Commit in PromptHub] --> B1
    A3[Online Evaluation Alert] --> B1
    A4[PR Opened] --> B1

    subgraph "Testing"
        B1 --> C1[Run Unit Tests]
        B1 --> C2[Run Integration Tests]
        B1 --> C3[Run End to End Tests]
        B1 --> C4[Run Offline Evaluations]

        C4 --> D1[Evaluate with OpenEvals or AgentEvals]
        C4 --> D2[Assertions: Hard and Soft]

        C1 --> E1[Run LangGraph Dev Server Test]
        C2 --> E1
        C3 --> E1
        D1 --> E1
        D2 --> E1
    end

    E1 --> F1[Push to Staging Deployment - Deploy to LangSmith as Development Type]

    F1 --> G1[Run Online Evaluations on Live Data]
    G1 --> H1[Attach Scores to Traces]

    H1 --> I1[If Quality Below Threshold]
    I1 --> J1[Send to Annotation Queue]
    I1 --> J2[Trigger Alert via Webhook]
    I1 --> J3[Push Trace to Golden Dataset]

    F1 --> K1[Promote to Production if All Pass - Deploy to LangSmith Production]

    J2 --> L1[Slack or PagerDuty Notification]

    subgraph Manual Review
        J1 --> M1[Human Labeling]
        M1 --> J3
    end

    classDef trigger fill:#F6FFDB,stroke:#6E8900,stroke-width:2px,color:#2E3900
    classDef process fill:#E5F4FF,stroke:#006DDD,stroke-width:2px,color:#030710
    classDef decision fill:#FDF3FF,stroke:#7E65AE,stroke-width:2px,color:#504B5F
    classDef output fill:#EBD0F0,stroke:#885270,stroke-width:2px,color:#441E33
    classDef alert fill:#F8E8E6,stroke:#B27D75,stroke-width:2px,color:#634643
    classDef neutral fill:#F2FAFF,stroke:#40668D,stroke-width:2px,color:#2F4B68

    class A1,A2,A3,A4 trigger
    class B1,C1,C2,C3,C4,D1,D2,E1 process
    class H1,I1 decision
    class F1,G1,K1 output
    class J2,L1 alert
    class J1,J3,M1 neutral
```

### Trigger sources

There are multiple ways you can trigger this pipeline, either during development or if your application is already live. The pipeline can be triggered by:

* <Icon icon="git-branch" /> **Code changes**: Pushes to main/development branches where you can modify the LangGraph architecture, try different models, update agent logic, or make any code improvements.
* <Icon icon="edit" /> **PromptHub updates**: Changes to prompt templates stored in LangSmith PromptHub—whenever there's a new prompt commit, the system triggers a webhook to run the pipeline.
* <Icon icon="alert-triangle" /> **Online evaluation alerts**: Performance degradation notifications from live deployments
* <Icon icon="webhook" /> **LangSmith traces webhooks**: Automated triggers based on trace analysis and performance metrics.
* <Icon icon="player-play" /> **Manual trigger**: Manual initiation of the pipeline for testing or emergency deployments.

### Testing layers

Compared to traditional software, testing AI agent applications also requires assessing response quality, so it is important to test each part of the workflow. The pipeline implements multiple testing layers:

1. <Icon icon="puzzle" /> **Unit tests**: Individual node and utility function testing.
2. <Icon icon="link" /> **Integration tests**: Component interaction testing.
3. <Icon icon="route" /> **End-to-end tests**: Full graph execution testing.
4. <Icon icon="brain" /> **Offline evaluations**: Performance assessment with real-world scenarios including end-to-end evaluations, single-step evaluations, agent trajectory analysis, and multi-turn simulations.
5. <Icon icon="server" /> **LangGraph dev server tests**: Use the [langgraph-cli](/langsmith/cli) tool for spinning up (inside the GitHub Action) a local server to run the LangGraph agent. This polls the `/ok` server API endpoint until it is available and for 30 seconds, after that it throws an error.

## GitHub actions workflow

The CI/CD pipeline uses GitHub Actions with the [Control Plane API](/langsmith/api-ref-control-plane) and [LangSmith API](/langsmith/smith-api-ref) to automate deployment. A helper script manages API interactions and deployments: [https://github.com/langchain-ai/cicd-pipeline-example/blob/main/.github/scripts/langgraph\_api.py](https://github.com/langchain-ai/cicd-pipeline-example/blob/main/.github/scripts/langgraph_api.py).

The workflow includes:

* **New agent deployment**: When a new PR is opened and tests pass, a new preview deployment is created in LangSmith Deployment using the [Control Plane API](/langsmith/api-ref-control-plane). This allows you to test the agent in a staging environment before promoting to production.

* **Agent deployment revision**: A revision happens when an existing deployment with the same ID is found, or when the PR is merged into main. In the case of merging to main, the preview deployment is deleted and a production deployment is created. This ensures that any updates to the agent are properly deployed and integrated into the production infrastructure.

  <img alt="Agent Deployment Revision Workflow" />

* **Testing and evaluation workflow**: In addition to the more traditional testing phases (unit tests, integration tests, end-to-end tests, etc.), the pipeline includes [offline evaluations](/langsmith/evaluation-concepts#offline-evaluations) and [Agent dev server testing](/langsmith/local-dev-testing) because you want to test the quality of your agent. These evaluations provide comprehensive assessment of the agent's performance using real-world scenarios and data.

  <img alt="Test with Results Workflow" />

  <AccordionGroup>
    <Accordion title="Final Response Evaluation" icon="circle-check">
      Evaluates the final output of your agent against expected results. This is the most common type of evaluation that checks if the agent's final response meets quality standards and answers the user's question correctly.
    </Accordion>

    <Accordion title="Single Step Evaluation" icon="player-skip-forward">
      Tests individual steps or nodes within your LangGraph workflow. This allows you to validate specific components of your agent's logic in isolation, ensuring each step functions correctly before testing the full pipeline.
    </Accordion>

    <Accordion title="Agent Trajectory Evaluation" icon="route">
      Analyzes the complete path your agent takes through the graph, including all intermediate steps and decision points. This helps identify bottlenecks, unnecessary steps, or suboptimal routing in your agent's workflow. It also evaluates whether your agent invoked the right tools in the right order or at the right time.
    </Accordion>

    <Accordion title="Multi-Turn Evaluation" icon="messages">
      Tests conversational flows where the agent maintains context across multiple interactions. This is crucial for agents that handle follow-up questions, clarifications, or extended dialogues with users.
    </Accordion>
  </AccordionGroup>

  See the [LangGraph testing documentation](/oss/python/langgraph/test) for specific testing approaches and the [evaluation approaches guide](/langsmith/evaluation-approaches) for a comprehensive overview of offline evaluations.

### Prerequisites

Before setting up the CI/CD pipeline, ensure you have:

* <Icon icon="robot" /> An AI agent application (in this case built using [LangGraph](/oss/python/langgraph/overview))
* <Icon icon="user" /> A [LangSmith account](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-cicd-pipeline-example)
* <Icon icon="key" /> A [LangSmith API key](/langsmith/create-account-api-key) needed to deploy agents and retrieve experiment results
* <Icon icon="settings" /> Project-specific environment variables configured in your repository secrets (e.g., LLM model API keys, vector store credentials, database connections)

<Note>
  While this example uses GitHub, the CI/CD pipeline works with other Git hosting platforms including GitLab, Bitbucket, and others.
</Note>

## Deployment options

LangSmith supports multiple deployment methods, depending on how your [LangSmith instance is hosted](/langsmith/platform-setup):

* <Icon icon="cloud" /> **Cloud LangSmith**: Direct GitHub integration.
* <Icon icon="server" /> **Self-Hosted/Hybrid**: Container registry-based deployments.

The deployment flow starts by modifying your agent implementation. At minimum, you must have a [`langgraph.json`](/langsmith/application-structure) and dependency file in your project (`requirements.txt` or `pyproject.toml`). Use the `langgraph dev` CLI tool to check for errors—fix any errors; otherwise, the deployment will succeed when deployed to LangSmith Deployment.

```mermaid actions={false} theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
graph TD
    A[Agent Implementation] --> B[langgraph.json + dependencies]
    B --> C[Test Locally with langgraph dev]
    C --> D{Errors?}
    D -->|Yes| E[Fix Issues]
    E --> C
    D -->|No| F[Choose LangSmith Instance]

    F --> G[Cloud LangSmith]
    F --> H[Self-Hosted/Hybrid LangSmith]

    subgraph "Cloud LangSmith"
        G --> I[Method 1: Connect GitHub Repo in UI]
        G --> J[Method 2: Control Plane API with GitHub Repo]
        I --> K[Deploy via LangSmith UI]
        J --> L[Deploy via Control Plane API]
    end

    subgraph "Self-Hosted/Hybrid LangSmith"
        H --> S[Build Docker Image langgraph build]
        S --> T[Push to Container Registry]
        T --> U{Deploy via?}
        U -->|UI| V[Specify Image URI in UI]
        U -->|API| W[Use Control Plane API]
        V --> X[Deploy via LangSmith UI]
        W --> Y[Deploy via Control Plane API]
    end

    K --> AA[Agent Ready for Use]
    L --> AA
    X --> AA
    Y --> AA

    AA --> BB{Connect via?}
    BB -->|LangGraph SDK| CC[Use LangGraph SDK]
    BB -->|RemoteGraph| DD[Use RemoteGraph]
    BB -->|REST API| EE[Use REST API]
    BB -->|LangGraph Studio UI| FF[Use LangGraph Studio UI]

    classDef trigger fill:#F6FFDB,stroke:#6E8900,stroke-width:2px,color:#2E3900
    classDef process fill:#E5F4FF,stroke:#006DDD,stroke-width:2px,color:#030710
    classDef decision fill:#FDF3FF,stroke:#7E65AE,stroke-width:2px,color:#504B5F
    classDef output fill:#EBD0F0,stroke:#885270,stroke-width:2px,color:#441E33

    class A trigger
    class B,C process
    class D,U,BB decision
    class E process
    class F decision
    class G,H process
    class I,J,S,T process
    class K,L,V,W process
    class X,Y,AA output
    class CC,DD,EE,FF output
```

### Prerequisites for manual deployment

Before deploying your agent, ensure you have:

1. <Icon icon="sitemap" /> **LangGraph graph**: Your agent implementation (e.g., `./agents/simple_text2sql.py:agent`).
2. <Icon icon="box" /> **Dependencies**: Either `requirements.txt` or `pyproject.toml` with all required packages.
3. <Icon icon="settings" /> **Configuration**: `langgraph.json` file specifying:
   * Path to your agent graph
   * Dependencies location
   * Environment variables
   * Python version

Example `langgraph.json`:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
    "graphs": {
        "simple_text2sql": "./agents/simple_text2sql.py:agent"
    },
    "env": ".env",
    "python_version": "3.11",
    "dependencies": ["."],
    "image_distro": "wolfi"
}
```

### Local development and testing

<img alt="Studio CLI Interface" />

First, test your agent locally using [Studio](/langsmith/studio):

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# Start local development server with Studio
langgraph dev
```

This will:

* Spin up a local server with Studio.
* Allow you to visualize and interact with your graph.
* Validate that your agent works correctly before deployment.

<Note>
  If your agent runs locally without any errors, it means that deployment to LangSmith will likely succeed. This local testing helps catch configuration issues, dependency problems, and agent logic errors before attempting deployment.
</Note>

See the [LangGraph CLI documentation](/langsmith/cli#dev) for more details.

### Method 1: LangSmith Deployment UI

Deploy your agent using the LangSmith deployment interface:

1. Go to your [LangSmith dashboard](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-cicd-pipeline-example).
2. Navigate to the **Deployments** section.
3. Click the **+ New Deployment** button in the top right.
4. Select your GitHub repository containing your LangGraph agent from the dropdown menu.

**Supported deployments:**

* <Icon icon="cloud" /> **Cloud LangSmith**: Direct GitHub integration with dropdown menu
* <Icon icon="server" /> **Self-Hosted/Hybrid LangSmith**: Specify your image URI in the Image Path field (e.g., `docker.io/username/my-agent:latest`)

<Info>
  **Benefits:**

  * Simple UI-based deployment
  * Direct integration with your GitHub repository (cloud)
  * No manual Docker image management required (cloud)
</Info>

### Method 2: Control plane API

Deploy using the Control Plane API with different approaches for each deployment type:

**For Cloud LangSmith:**

* Use the Control Plane API to create deployments by pointing to your GitHub repository
* No Docker image building required for cloud deployments

**For Self-Hosted/Hybrid LangSmith:**

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# Build Docker image
langgraph build -t my-agent:latest

# Push to your container registry
docker push my-agent:latest
```

You can push to any container registry (Docker Hub, AWS ECR, Azure ACR, Google GCR, etc.) that your deployment environment has access to.

**Supported deployments:**

* <Icon icon="cloud" /> **Cloud LangSmith**: Use the Control Plane API to create deployments from your GitHub repository
* <Icon icon="server" /> **Self-Hosted/Hybrid LangSmith**: Use the Control Plane API to create deployments from your container registry

See the [LangGraph CLI build documentation](/langsmith/cli#build) for more details.

### Connect to your deployed Agent

* <Icon icon="code" /> **[LangGraph SDK](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/#langgraph-sdk-python)**: Use the LangGraph SDK for programmatic integration.
* <Icon icon="sitemap" /> **[RemoteGraph](/langsmith/use-remote-graph)**: Connect using RemoteGraph for remote graph connections (to use your graph in other graphs).
* <Icon icon="globe" /> **[REST API](/langsmith/server-api-ref)**: Use HTTP-based interactions with your deployed agent.
* <Icon icon="device-desktop" /> **[Studio](/langsmith/studio)**: Access the visual interface for testing and debugging.

### Environment configuration

#### Database & cache configuration

By default, LangSmith Deployment create PostgreSQL and Redis instances for you. To use external services, set the following environment variables in your new deployment or revision:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# Set environment variables for external services
export POSTGRES_URI_CUSTOM="postgresql://user:pass@host:5432/db"
export REDIS_URI_CUSTOM="redis://host:6379/0"
```

See the [environment variables documentation](/langsmith/env-var#postgres_uri_custom) for more details.

## Troubleshooting

### Wrong API endpoints

If you're experiencing connection issues, verify you're using the correct endpoint format for your LangSmith instance. There are two different APIs with different endpoints:

#### LangSmith API (Traces, ingestion, etc.)

For LangSmith API operations (traces, evaluations, datasets):

<table>
  <thead>
    <tr>
      <th>Region</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>GCP US</td>
    </tr>

    <tr>
      <td>GCP EU</td>
    </tr>

    <tr>
      <td>GCP APAC</td>
    </tr>

    <tr>
      <td>AWS US</td>
    </tr>
  </tbody>
</table>

For self-hosted LangSmith instances, use `http(s)://<langsmith-url>/api` where `<langsmith-url>` is your self-hosted instance URL.

<Note>
  If you're setting the endpoint in the `LANGSMITH_ENDPOINT` environment variable, you need to add `/v1` at the end (e.g., `https://api.smith.langchain.com/v1` or `http(s)://<langsmith-url>/api/v1` if self-hosted).
</Note>

#### LangSmith Deployment API (Deployments)

For LangSmith Deployment operations (deployments, revisions):

<table>
  <thead>
    <tr>
      <th>Region</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>GCP US</td>
    </tr>

    <tr>
      <td>GCP EU</td>
    </tr>

    <tr>
      <td>GCP APAC</td>
    </tr>

    <tr>
      <td>AWS US</td>
    </tr>
  </tbody>
</table>

For self-hosted LangSmith instances, use `http(s)://<langsmith-url>/api-host` where `<langsmith-url>` is your self-hosted instance URL.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/cicd-pipeline-example.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
