# my_agent/agent.py
from typing import Literal
from typing_extensions import TypedDict

from langgraph.graph import StateGraph, END, START
from my_agent.utils.nodes import call_model, should_continue, tool_node # import nodes
from my_agent.utils.state import AgentState # import state

# Define the runtime context
class GraphContext(TypedDict):
    model_name: Literal["anthropic", "openai"]

workflow = StateGraph(AgentState, context_schema=GraphContext)
workflow.add_node("agent", call_model)
workflow.add_node("action", tool_node)
workflow.add_edge(START, "agent")
workflow.add_conditional_edges(
    "agent",
    should_continue,
    {
        "continue": "action",
        "end": END,
    },
)
workflow.add_edge("action", "agent")

graph = workflow.compile()
```

Example file directory:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
my-app/
├── my_agent # all project code lies within here
│   ├── utils # utilities for your graph
│   │   ├── __init__.py
│   │   ├── tools.py # tools for your graph
│   │   ├── nodes.py # node functions for your graph
│   │   └── state.py # state definition of your graph
│   ├── requirements.txt # package dependencies
│   ├── __init__.py
│   └── agent.py # code for constructing your graph
└── .env # environment variables
```

## Create the configuration file

Create a [configuration file](/langsmith/cli#configuration-file) called `langgraph.json`. See the [configuration file reference](/langsmith/cli#configuration-file) for detailed explanations of each key in the JSON object of the configuration file.

Example `langgraph.json` file:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "dependencies": ["./my_agent"],
  "graphs": {
    "agent": "./my_agent/agent.py:graph"
  },
  "env": ".env"
}
```

Note that the variable name of the `CompiledGraph` appears at the end of the value of each subkey in the top-level `graphs` key (i.e. `:<variable_name>`).

<Warning>
  **Configuration file location**
  The configuration file must be placed in a directory that is at the same level or higher than the Python files that contain compiled graphs and associated dependencies.
</Warning>

Example file directory:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
my-app/
├── my_agent # all project code lies within here
│   ├── utils # utilities for your graph
│   │   ├── __init__.py
│   │   ├── tools.py # tools for your graph
│   │   ├── nodes.py # node functions for your graph
│   │   └── state.py # state definition of your graph
│   ├── requirements.txt # package dependencies
│   ├── __init__.py
│   └── agent.py # code for constructing your graph
├── .env # environment variables
└── langgraph.json # configuration file for LangGraph
```

## Next

After you set up your project and place it in a GitHub repository, it's time to [deploy your app](/langsmith/deployment-quickstart).

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/setup-app-requirements-txt.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# How to set up a JavaScript application
Source: https://docs.langchain.com/langsmith/setup-javascript

An application must be configured with a [configuration file](/langsmith/cli#configuration-file) in order to be deployed to LangSmith (or to be self-hosted). This how-to guide discusses the basic steps to set up a JavaScript application for deployment using `package.json` to specify project dependencies.

This walkthrough is based on [this repository](https://github.com/langchain-ai/langgraphjs-studio-starter), which you can play around with to learn more about how to set up your application for deployment.

The final repository structure will look something like this:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
my-app/
├── src # all project code lies within here
│   ├── utils # optional utilities for your graph
│   │   ├── tools.ts # tools for your graph
│   │   ├── nodes.ts # node functions for your graph
│   │   └── state.ts # state definition of your graph
│   └── agent.ts # code for constructing your graph
├── package.json # package dependencies
├── .env # environment variables
└── langgraph.json # configuration file for LangGraph
```

<Tip>
  LangSmith Deployment supports deploying a [LangGraph](/oss/python/langgraph/overview) *graph*. However, the implementation of a *node* of a graph can contain arbitrary code. This means any framework can be implemented within a node and deployed on LangSmith Deployment. This lets you implement your core application logic without using additional LangGraph OSS APIs while still using LangSmith for [deployment](/langsmith/deployment), scaling, and [observability](/langsmith/observability). For more details, refer to [Use any framework with LangSmith Deployment](/langsmith/application-structure#use-any-framework-with-langsmith-deployment).
</Tip>

After each step, an example file directory is provided to demonstrate how code can be organized.

## Specify dependencies

Dependencies can be specified in a `package.json`. If none of these files is created, then dependencies can be specified later in the [configuration file](#create-the-api-config).

Example `package.json` file:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "name": "langgraphjs-studio-starter",
  "packageManager": "yarn@1.22.22",
  "dependencies": {
    "@langchain/core": "^0.2.31",
    "@langchain/langgraph": "^0.2.0",
    "@langchain/openai": "^0.2.8",
    "@langchain/tavily": "^0.1.5"
  }
}
```

When deploying your app, the dependencies will be installed using the package manager of your choice, provided they adhere to the compatible version ranges listed below:

```
"@langchain/core": "^0.3.42",
"@langchain/langgraph": "^0.2.57",
"@langchain/langgraph-checkpoint": "~0.0.16",
```

Example file directory:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
my-app/
└── package.json # package dependencies
```

## Specify environment variables

Environment variables can optionally be specified in a file (e.g. `.env`). See the [Environment Variables reference](/langsmith/env-var) to configure additional variables for a deployment.

Example `.env` file:

```
MY_ENV_VAR_1=foo
MY_ENV_VAR_2=bar
OPENAI_API_KEY=key
TAVILY_API_KEY=key_2
```

Example file directory:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
my-app/
├── package.json
└── .env # environment variables
```

## Define graphs

Implement your graphs. Graphs can be defined in a single file or multiple files. Make note of the variable names of each compiled graph to be included in the application. The variable names will be used later when creating the [configuration file](/langsmith/cli#configuration-file).

Here is an example `agent.ts`:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import type { AIMessage } from "@langchain/core/messages";
import { TavilySearch } from "@langchain/tavily";
import { ChatOpenAI } from "@langchain/openai";

import { MessagesAnnotation, StateGraph } from "@langchain/langgraph";
import { ToolNode } from "@langchain/langgraph/prebuilt";

const tools = [new TavilySearch({ maxResults: 3 })];

// Define the function that calls the model
async function callModel(state: typeof MessagesAnnotation.State) {
  /**
   * Call the LLM powering our agent.
   * Feel free to customize the prompt, model, and other logic!
   */
  const model = new ChatOpenAI({
    model: "gpt-5.5",
  }).bindTools(tools);

  const response = await model.invoke([
    {
      role: "system",
      content: `You are a helpful assistant. The current date is ${new Date().getTime()}.`,
    },
    ...state.messages,
  ]);

  // MessagesAnnotation supports returning a single message or array of messages
  return { messages: response };
}

// Define the function that determines whether to continue or not
function routeModelOutput(state: typeof MessagesAnnotation.State) {
  const messages = state.messages;
  const lastMessage: AIMessage = messages[messages.length - 1];
  // If the LLM is invoking tools, route there.
  if ((lastMessage?.tool_calls?.length ?? 0) > 0) {
    return "tools";
  }
  // Otherwise end the graph.
  return "__end__";
}

// Define a new graph.
// See https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#getting-started for
// more on defining custom graph states.
const workflow = new StateGraph(MessagesAnnotation)
  // Define the two nodes we will cycle between
  .addNode("callModel", callModel)
  .addNode("tools", new ToolNode(tools))
  // Set the entrypoint as `callModel`
  // This means that this node is the first one called
  .addEdge("__start__", "callModel")
  .addConditionalEdges(
    // First, we define the edges' source node. We use `callModel`.
    // This means these are the edges taken after the `callModel` node is called.
    "callModel",
    // Next, we pass in the function that will determine the sink node(s), which
    // will be called after the source node is called.
    routeModelOutput,
    // List of the possible destinations the conditional edge can route to.
    // Required for conditional edges to properly render the graph in Studio
    ["tools", "__end__"]
  )
  // This means that after `tools` is called, `callModel` node is called next.
  .addEdge("tools", "callModel");

// Finally, we compile it!
// This compiles it into a graph you can invoke and deploy.
export const graph = workflow.compile();
```

Example file directory:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
my-app/
├── src # all project code lies within here
│   ├── utils # optional utilities for your graph
│   │   ├── tools.ts # tools for your graph
│   │   ├── nodes.ts # node functions for your graph
│   │   └── state.ts # state definition of your graph
│   └── agent.ts # code for constructing your graph
├── package.json # package dependencies
├── .env # environment variables
└── langgraph.json # configuration file for LangGraph
```

## Create the API config

Create a [configuration file](/langsmith/cli#configuration-file) called `langgraph.json`. See the [configuration file reference](/langsmith/cli#configuration-file) for detailed explanations of each key in the JSON object of the configuration file.

Example `langgraph.json` file:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "node_version": "20",
  "dockerfile_lines": [],
  "dependencies": ["."],
  "graphs": {
    "agent": "./src/agent.ts:graph"
  },
  "env": ".env"
}
```

Note that the variable name of the `CompiledGraph` appears at the end of the value of each subkey in the top-level `graphs` key (i.e. `:<variable_name>`).

<Info>
  **Configuration Location**
  The configuration file must be placed in a directory that is at the same level or higher than the TypeScript files that contain compiled graphs and associated dependencies.
</Info>

## Next

After you setup your project and place it in a GitHub repository, it's time to [deploy your app](/langsmith/deployment-quickstart).

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/setup-javascript.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# How to set up an application with pyproject.toml
Source: https://docs.langchain.com/langsmith/setup-pyproject

An application must be configured with a [configuration file](/langsmith/cli#configuration-file) in order to be deployed to LangSmith (or to be self-hosted). This how-to guide discusses the basic steps to set up an application for deployment using `pyproject.toml` to define your package's dependencies.

This example is based on [this repository](https://github.com/langchain-ai/langgraph-example-pyproject), which uses the LangGraph framework.

The final repository structure will look something like this:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
my-app/
├── my_agent # all project code lies within here
│   ├── utils # utilities for your graph
│   │   ├── __init__.py
│   │   ├── tools.py # tools for your graph
│   │   ├── nodes.py # node functions for your graph
│   │   └── state.py # state definition of your graph
│   ├── __init__.py
│   └── agent.py # code for constructing your graph
├── .env # environment variables
├── langgraph.json  # configuration file for LangGraph
└── pyproject.toml # dependencies for your project
```

<Tip>
  LangSmith Deployment supports deploying a [LangGraph](/oss/python/langgraph/overview) *graph*. However, the implementation of a *node* of a graph can contain arbitrary code. This means any framework can be implemented within a node and deployed on LangSmith Deployment. This lets you implement your core application logic without using additional LangGraph OSS APIs while still using LangSmith for [deployment](/langsmith/deployment), scaling, and [observability](/langsmith/observability). For more details, refer to [Use any framework with LangSmith Deployment](/langsmith/application-structure#use-any-framework-with-langsmith-deployment).
</Tip>

You can also set up with:

* `requirements.txt`: for dependency management, check out [this how-to guide](/langsmith/setup-app-requirements-txt) on using `requirements.txt` for LangSmith.
* a monorepo: To deploy a graph located inside a monorepo, take a look at [this repository](https://github.com/langchain-ai/langgraph-example-monorepo) for an example of how to do so.

After each step, an example file directory is provided to demonstrate how code can be organized.

## Specify dependencies

Dependencies can optionally be specified in one of the following files: `pyproject.toml`, `setup.py`, or `requirements.txt`. If none of these files is created, then dependencies can be specified later in the [configuration file](#create-the-configuration-file).

The dependencies below will be included in the image, you can also use them in your code, as long as with a compatible version range:

```
langgraph>=0.4.10,<2
langgraph-sdk>=0.3.5
langgraph-checkpoint>=3.0.1,<5
langchain-core>=0.3.66
langsmith>=0.7.31
orjson>=3.9.7
httpx>=0.25.0
tenacity>=8.0.0
uvicorn>=0.26.0
sse-starlette>=2.1.3,<3.4.0
uvloop>=0.18.0
httptools>=0.5.0
jsonschema-rs>=0.20.0
structlog>=24.1.0
cloudpickle>=3.0.0
truststore>=0.1
protobuf>=6.32.1,<7.0.0
grpcio>=1.80.0,<1.81.0
grpcio-tools>=1.80.0,<1.81.0
grpcio-health-checking>=1.80.0,<1.81.0
opentelemetry-api>=0.0.1
opentelemetry-sdk>=0.0.1
opentelemetry-exporter-otlp-proto-http>=0.0.1
```

Example `pyproject.toml` file:

```toml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "my-agent"
version = "0.0.1"
description = "An excellent agent build for LangSmith."
authors = [
    {name = "Assistant", email = "1223+assistant@users.noreply.github.com"}
]
license = {text = "MIT"}
readme = "README.md"
requires-python = ">=3.9"
dependencies = [
    "langgraph>=0.6.0",
    "langchain-fireworks>=0.1.3"
]

[tool.hatch.build.targets.wheel]
packages = ["my_agent"]
```

Example file directory:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
my-app/
└── pyproject.toml   # Python packages required for your graph
```

## Specify environment variables

Environment variables can optionally be specified in a file (e.g. `.env`). See the [Environment Variables reference](/langsmith/env-var) to configure additional variables for a deployment.

Example `.env` file:

```
MY_ENV_VAR_1=foo
MY_ENV_VAR_2=bar
FIREWORKS_API_KEY=key
```

Example file directory:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
my-app/
├── .env # file with environment variables
└── pyproject.toml
```

<Tip>
  By default, LangSmith follows the `uv`/`pip` behavior of **not** installing prerelease versions unless explicitly allowed. If want to use prereleases, you have the following options:

  * With `pyproject.toml`: add `allow-prereleases = true` to your `[tool.uv]` section.
  * With `requirements.txt` or `setup.py`: you must explicitly specify every prerelease dependency, including transitive ones. For example, if you declare `a==0.0.1a1` and `a` depends on `b==0.0.1a1`, then you must also explicitly include `b==0.0.1a1` in your dependencies.
</Tip>

## Define graphs

Implement your graphs. Graphs can be defined in a single file or multiple files. Make note of the variable names of each [CompiledStateGraph](https://reference.langchain.com/python/langgraph/graph/state/CompiledStateGraph) to be included in the application. The variable names will be used later when creating the [configuration file](/langsmith/cli#configuration-file).

Example `agent.py` file, which shows how to import from other modules you define (code for the modules is not shown here, please see [this repository](https://github.com/langchain-ai/langgraph-example-pyproject) to see their implementation):

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# my_agent/agent.py
from typing import Literal
from typing_extensions import TypedDict

from langgraph.graph import StateGraph, END, START
from my_agent.utils.nodes import call_model, should_continue, tool_node # import nodes
from my_agent.utils.state import AgentState # import state

# Define the runtime context
class GraphContext(TypedDict):
    model_name: Literal["anthropic", "openai"]

workflow = StateGraph(AgentState, context_schema=GraphContext)
workflow.add_node("agent", call_model)
workflow.add_node("action", tool_node)
workflow.add_edge(START, "agent")
workflow.add_conditional_edges(
    "agent",
    should_continue,
    {
        "continue": "action",
        "end": END,
    },
)
workflow.add_edge("action", "agent")

graph = workflow.compile()
```

Example file directory:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
my-app/
├── my_agent # all project code lies within here
│   ├── utils # utilities for your graph
│   │   ├── __init__.py
│   │   ├── tools.py # tools for your graph
│   │   ├── nodes.py # node functions for your graph
│   │   └── state.py # state definition of your graph
│   ├── __init__.py
│   └── agent.py # code for constructing your graph
├── .env
└── pyproject.toml
```

## Create the configuration file

Create a [configuration file](/langsmith/cli#configuration-file) called `langgraph.json`. See the [configuration file reference](/langsmith/cli#configuration-file) for detailed explanations of each key in the JSON object of the configuration file.

Example `langgraph.json` file:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "dependencies": ["."],
  "graphs": {
    "agent": "./my_agent/agent.py:graph"
  },
  "env": ".env"
}
```

Note that the variable name of the `CompiledGraph` appears at the end of the value of each subkey in the top-level `graphs` key (i.e. `:<variable_name>`).

<Warning>
  **Configuration file location**
  The configuration file must be placed in a directory that is at the same level or higher than the Python files that contain compiled graphs and associated dependencies.
</Warning>

Example file directory:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
my-app/
├── my_agent # all project code lies within here
│   ├── utils # utilities for your graph
│   │   ├── __init__.py
│   │   ├── tools.py # tools for your graph
│   │   ├── nodes.py # node functions for your graph
│   │   └── state.py # state definition of your graph
│   ├── __init__.py
│   └── agent.py # code for constructing your graph
├── .env # environment variables
├── langgraph.json  # configuration file for LangGraph
└── pyproject.toml # dependencies for your project
```

## Next

After you setup your project and place it in a GitHub repository, it's time to [deploy your app](/langsmith/deployment-quickstart).

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/setup-pyproject.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# LangSmith shared responsibility model
Source: https://docs.langchain.com/langsmith/shared-responsibility-model

Overview of how LangChain and customers share security responsibilities for the LangSmith platform.

LangSmith operates as a multi-tenant SaaS solution. Our security model is designed to be simple: LangChain secures the platform infrastructure and application, while you secure your specific usage, data inputs, and the AI agents you build.

## Responsibility matrix

| Domain             | LangChain responsibility (provider)                                                                                                                             | Customer responsibility (user)                                                                                   |
| :----------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------- |
| **Infrastructure** | We manage the underlying cloud infrastructure (via GCP), including servers, networking, OS patching, and capacity planning. GCP owns the physical data centers. | N/A. You do not provision or maintain compute resources in the SaaS environment.                                 |
| **Application**    | We secure the LangSmith application code, API endpoints, and database clusters, including code scanning and penetration testing.                                | You are responsible for the security and safety of the AI chains and agents you build using our SDKs.            |
| **Data**           | We enforce tenant isolation and encrypt data at rest using AES-256 and in transit using TLS 1.2 or higher.                                                      | You control what data is sent to us and must filter sensitive PII via the SDK before it leaves your environment. |
| **Identity**       | We provide the guardrails, including SSO/SCIM, MFA enforcement options, and RBAC frameworks.                                                                    | You manage your user roster, assign roles (e.g., Admin vs. Viewer), and revoke access for terminated employees.  |
| **Secrets**        | We securely store the secrets you entrust to the platform.                                                                                                      | You are responsible for rotating your API keys and ensuring they are not hard-coded in your applications.        |

## LangChain responsibilities (the platform)

* We maintain SOC 2 Type II, GDPR, and HIPAA compliance and undergo annual third-party audits and penetration testing.
* We manage all underlying infrastructure on Google Cloud Platform (GCP), including network firewalls, DDoS protection via Cloud Armor, and container security.
* We maintain high availability in accordance with our SLA, maintain daily backups, and handle disaster recovery for the LangSmith service.
* We patch confirmed platform vulnerabilities within strict service level agreements, with critical severity issues remediated in less than 2 weeks and high severity issues within 30 days.
* We encrypt all customer data at rest using AES-256 and in transit using TLS 1.2 or higher.

## Customer responsibilities (the usage)

* You must enforce least privilege access and immediately remove access for employees who leave your organization.
* You must ensure no prohibited data, such as PCI DSS cardholder data, is sent to the platform and use the masking features in the SDK to redact PII at the source.
* You are responsible for the security of the environment where you run the LangChain SDK, including your laptops and servers.
* You must rotate your API keys periodically and ensure they are stored in environment variables rather than hard-coded in your source code.

## Customer security best practices

To align with the security assumptions in our SOC 2 Type II framework, we recommend customers maintain the following internal guidelines:

* Maintain up-to-date technical and security contact details in your tenant settings so our team can reach you during an incident.
* Cycle your keys immediately via the self-serve portal if you suspect a compromise. You can always reach out to the LangChain security team if you have questions or need assistance with a breach.
* Develop a disaster recovery plan for your specific application to handle scenarios where the LangSmith service may be unavailable.
* Ensure that workstations and endpoints used to access the LangSmith UI are regularly patched and secured.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/shared-responsibility-model.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# LangSmith skills
Source: https://docs.langchain.com/langsmith/skills

Use Agent Skills to work with LangSmith traces, datasets, and evaluators from your coding agent.

Agent Skills are reusable, on‑demand capabilities that bundle instructions plus optional helper scripts. This page summarizes the LangSmith‑oriented skills you can add to a compatible coding agent to query traces, generate datasets, and define evaluators. To work with the same LangSmith data directly from the terminal, use the [LangSmith CLI](/langsmith/langsmith-cli).

<Note>
  These skills follow the Agent Skills specification and are maintained in the [`langsmith-skills` GitHub repository](https://github.com/langchain-ai/langsmith-skills). You can copy the `SKILL.md` and any referenced `scripts/` into your agent’s skills directory. The installers below only install the LangSmith skills (trace, dataset, evaluator).
</Note>

## Quick install

Install only the LangSmith skills (trace, dataset, evaluator) using `npx skills`:

<CodeGroup>
  ```bash Local (current project) theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  npx skills add langchain-ai/langsmith-skills --skill '*' --yes
  ```

  ```bash Global (all projects) theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  npx skills add langchain-ai/langsmith-skills --skill '*' --yes --global
  ```

  ```bash Link to a specific agent (e.g., Claude Code) theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  npx skills add langchain-ai/langsmith-skills --agent claude-code --skill '*' --yes --global
  ```
</CodeGroup>

<Tip>
  To update, re‑run the command. If target skill folders already exist, remove them first (e.g., `rm -rf ~/.claude/skills/langsmith-*`).
</Tip>

## Configure environment

After installing the skills, set environment variables used by all LangSmith skills, helper scripts, and the [LangSmith CLI](/langsmith/langsmith-cli):

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
export LANGSMITH_API_KEY=<your-key>

# Optional defaults
export LANGSMITH_PROJECT=<default-project>

# Advanced: multi-workspace or certain self-hosted setups only

# export LANGSMITH_WORKSPACE_ID=<workspace-id>
```

## What these skills cover

* [Traces](/langsmith/observability-concepts#traces): Add tracing to apps; list, filter, inspect, and export traces for debugging and analysis.
* [Datasets](/langsmith/evaluation-concepts#datasets): Turn traces into evaluation datasets (final\_response, single\_step, trajectory, RAG) and optionally upload to LangSmith.
* [Evaluators](/langsmith/evaluation-concepts#evaluators): Define code or LLM‑as‑judge evaluators and attach them to datasets (offline) or projects (online).

Each skill directory ships with a `SKILL.md` plus optional `scripts/` helpers you can run or adapt. These skills are designed to plug into compatible coding agents (such as Claude Code or Deep Agents Code), though you can also reuse the helper scripts directly if you prefer not to wire up a full agent. For heavier querying, exports, or automation, you can pair these skills with the [LangSmith CLI](/langsmith/langsmith-cli) to script against the same projects, datasets, and evaluators from your terminal.

## Manual install

Clone the repo and run the install script for more options:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
git clone https://github.com/langchain-ai/langsmith-skills.git
cd langsmith-skills

# Install for Claude Code in current directory (default)
./install.sh

# Install for Claude Code globally
./install.sh --global

# Install for Deep Agents Code in current directory
./install.sh --deepagents

# Install for Deep Agents Code globally (includes agent persona)
./install.sh --deepagents --global

# Install only LangSmith skills (any target)
./install.sh --langsmith
```

If you prefer to copy only specific skills, copy the desired directory from `config/skills/` into your agent's skills folder.

Included LangSmith skills:

* langsmith-trace — Traces (query/export)
* langsmith-dataset — Datasets (generate/upload)
* langsmith-evaluator — Evaluators (create/attach)

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/skills.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# LangSmith API reference
Source: https://docs.langchain.com/langsmith/smith-api-ref

The LangSmith REST API provides programmatic access to LangSmith platform features including tracing, datasets, experiments, annotations, and more.

Browse the full API reference in the **LangSmith API** section in the sidebar.

## Authentication

Pass the `X-Api-Key` header with each request. The value should be a valid [LangSmith API key](/langsmith/create-account-api-key).

```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
curl --request GET \
  --url https://api.smith.langchain.com/api/v1/workspaces \
  --header 'X-Api-Key: LANGSMITH_API_KEY'
```

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/smith-api-ref.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Attach access policies to a role
Source: https://docs.langchain.com/langsmith/smith-api/access_policies/attach-access-policies-to-a-role

/langsmith/langsmith-platform-openapi.json post /v1/platform/orgs/current/access-policies/roles/{role_id}/access-policies
Attaches one or more access policies to a specific role. The request body must contain an array of access policy IDs.

# Create an access policy
Source: https://docs.langchain.com/langsmith/smith-api/access_policies/create-an-access-policy

/langsmith/langsmith-platform-openapi.json post /v1/platform/orgs/current/access-policies
Creates a new access policy.

# Delete an access policy
Source: https://docs.langchain.com/langsmith/smith-api/access_policies/delete-an-access-policy

/langsmith/langsmith-platform-openapi.json delete /v1/platform/orgs/current/access-policies/{access_policy_id}
Deletes a specific access policy by ID.

# Get an access policy
Source: https://docs.langchain.com/langsmith/smith-api/access_policies/get-an-access-policy

/langsmith/langsmith-platform-openapi.json get /v1/platform/orgs/current/access-policies/{access_policy_id}
Gets a specific access policy by ID.

# List access policies
Source: https://docs.langchain.com/langsmith/smith-api/access_policies/list-access-policies

/langsmith/langsmith-platform-openapi.json get /v1/platform/orgs/current/access-policies
Lists all access policies for the organization.

# Execute
Source: https://docs.langchain.com/langsmith/smith-api/ace/execute

/langsmith/langsmith-platform-openapi.json post /api/v1/ace/execute
Execute some custom code for testing purposes.

# Create an alert rule
Source: https://docs.langchain.com/langsmith/smith-api/alert_rules/create-an-alert-rule

/langsmith/langsmith-platform-openapi.json post /v1/platform/alerts/{session_id}
Creates a new alert rule. The request body must be a JSON-encoded alert rule object that follows the CreateAlertRuleRequest schema.

# Delete an alert rule
Source: https://docs.langchain.com/langsmith/smith-api/alert_rules/delete-an-alert-rule

/langsmith/langsmith-platform-openapi.json delete /v1/platform/alerts/{session_id}/{alert_rule_id}
Deletes an alert rule

# Get an alert rule
Source: https://docs.langchain.com/langsmith/smith-api/alert_rules/get-an-alert-rule

/langsmith/langsmith-platform-openapi.json get /v1/platform/alerts/{session_id}/{alert_rule_id}
Gets an alert rule.

# Test an alert action to determine if configuration is valid
Source: https://docs.langchain.com/langsmith/smith-api/alert_rules/test-an-alert-action-to-determine-if-configuration-is-valid

/langsmith/langsmith-platform-openapi.json post /v1/platform/alerts/{session_id}/test
Tests an alert action which will fire a notification to all configured recipients if the configuration is valid.

# Update an alert rule
Source: https://docs.langchain.com/langsmith/smith-api/alert_rules/update-an-alert-rule

/langsmith/langsmith-platform-openapi.json patch /v1/platform/alerts/{session_id}/{alert_rule_id}
Updates an alert rule.

# Add Runs To Annotation Queue
Source: https://docs.langchain.com/langsmith/smith-api/annotation-queues/add-runs-to-annotation-queue

/langsmith/langsmith-platform-openapi.json post /api/v1/annotation-queues/{queue_id}/runs

# Add Runs To Annotation Queue By Key
Source: https://docs.langchain.com/langsmith/smith-api/annotation-queues/add-runs-to-annotation-queue-by-key

/langsmith/langsmith-platform-openapi.json post /api/v1/annotation-queues/{queue_id}/runs/by-key

# Create Annotation Queue
Source: https://docs.langchain.com/langsmith/smith-api/annotation-queues/create-annotation-queue

/langsmith/langsmith-platform-openapi.json post /api/v1/annotation-queues

# Create Identity Annotation Queue Run Status
Source: https://docs.langchain.com/langsmith/smith-api/annotation-queues/create-identity-annotation-queue-run-status

/langsmith/langsmith-platform-openapi.json post /api/v1/annotation-queues/status/{annotation_queue_run_id}

# Delete Annotation Queue
Source: https://docs.langchain.com/langsmith/smith-api/annotation-queues/delete-annotation-queue

/langsmith/langsmith-platform-openapi.json delete /api/v1/annotation-queues/{queue_id}

# Delete Annotation Queues
Source: https://docs.langchain.com/langsmith/smith-api/annotation-queues/delete-annotation-queues

/langsmith/langsmith-platform-openapi.json delete /api/v1/annotation-queues
Delete multiple annotation queues with partial success support.

Returns:
    - 200: All queues deleted successfully
    - 207: Some queues deleted successfully, some failed

# Delete Run From Annotation Queue
Source: https://docs.langchain.com/langsmith/smith-api/annotation-queues/delete-run-from-annotation-queue

/langsmith/langsmith-platform-openapi.json delete /api/v1/annotation-queues/{queue_id}/runs/{queue_run_id}

# Delete Runs From Annotation Queue
Source: https://docs.langchain.com/langsmith/smith-api/annotation-queues/delete-runs-from-annotation-queue

/langsmith/langsmith-platform-openapi.json post /api/v1/annotation-queues/{queue_id}/runs/delete

# Export Annotation Queue Archived Runs
Source: https://docs.langchain.com/langsmith/smith-api/annotation-queues/export-annotation-queue-archived-runs

/langsmith/langsmith-platform-openapi.json post /api/v1/annotation-queues/{queue_id}/export

# Get Annotation Queue
Source: https://docs.langchain.com/langsmith/smith-api/annotation-queues/get-annotation-queue

/langsmith/langsmith-platform-openapi.json get /api/v1/annotation-queues/{queue_id}

# Get Annotation Queues
Source: https://docs.langchain.com/langsmith/smith-api/annotation-queues/get-annotation-queues

/langsmith/langsmith-platform-openapi.json get /api/v1/annotation-queues

# Get Annotation Queues For Run
Source: https://docs.langchain.com/langsmith/smith-api/annotation-queues/get-annotation-queues-for-run

/langsmith/langsmith-platform-openapi.json get /api/v1/annotation-queues/{run_id}/queues

# Get Run From Annotation Queue
Source: https://docs.langchain.com/langsmith/smith-api/annotation-queues/get-run-from-annotation-queue

/langsmith/langsmith-platform-openapi.json get /api/v1/annotation-queues/{queue_id}/run/{index}
Get a run from an annotation queue

# Get Runs From Annotation Queue
Source: https://docs.langchain.com/langsmith/smith-api/annotation-queues/get-runs-from-annotation-queue

/langsmith/langsmith-platform-openapi.json get /api/v1/annotation-queues/{queue_id}/runs

# Get Size From Annotation Queue
Source: https://docs.langchain.com/langsmith/smith-api/annotation-queues/get-size-from-annotation-queue

/langsmith/langsmith-platform-openapi.json get /api/v1/annotation-queues/{queue_id}/size

# Get Total Archived From Annotation Queue
Source: https://docs.langchain.com/langsmith/smith-api/annotation-queues/get-total-archived-from-annotation-queue

/langsmith/langsmith-platform-openapi.json get /api/v1/annotation-queues/{queue_id}/total_archived

# Get Total Size From Annotation Queue
Source: https://docs.langchain.com/langsmith/smith-api/annotation-queues/get-total-size-from-annotation-queue

/langsmith/langsmith-platform-openapi.json get /api/v1/annotation-queues/{queue_id}/total_size

# Populate Annotation Queue
Source: https://docs.langchain.com/langsmith/smith-api/annotation-queues/populate-annotation-queue

/langsmith/langsmith-platform-openapi.json post /api/v1/annotation-queues/populate
Populate annotation queue with runs from an experiment.

# Resolve Annotation Queue Run
Source: https://docs.langchain.com/langsmith/smith-api/annotation-queues/resolve-annotation-queue-run

/langsmith/langsmith-platform-openapi.json get /api/v1/annotation-queues/{queue_id}/runs/resolve/{queue_run_id}
Resolve a queue run ID to its section and run data for deep linking.

# Update Annotation Queue
Source: https://docs.langchain.com/langsmith/smith-api/annotation-queues/update-annotation-queue

/langsmith/langsmith-platform-openapi.json patch /api/v1/annotation-queues/{queue_id}

# Update Run In Annotation Queue
Source: https://docs.langchain.com/langsmith/smith-api/annotation-queues/update-run-in-annotation-queue

/langsmith/langsmith-platform-openapi.json patch /api/v1/annotation-queues/{queue_id}/runs/{queue_run_id}

# Add a reviewer to an annotation queue
Source: https://docs.langchain.com/langsmith/smith-api/annotation_queues/add-a-reviewer-to-an-annotation-queue

/langsmith/langsmith-platform-openapi.json post /v1/platform/annotation-queues/{queue_id}/reviewers
Assigns a single identity as a reviewer for the queue. Idempotent.

# Remove a reviewer from an annotation queue
Source: https://docs.langchain.com/langsmith/smith-api/annotation_queues/remove-a-reviewer-from-an-annotation-queue

/langsmith/langsmith-platform-openapi.json delete /v1/platform/annotation-queues/{queue_id}/reviewers/{identity_id}
Unassigns an identity as a reviewer for the queue. Idempotent.

# Delete Api Key
Source: https://docs.langchain.com/langsmith/smith-api/api-key/delete-api-key

/langsmith/langsmith-platform-openapi.json delete /api/v1/api-key/{api_key_id}
Delete an api key for the user

# Delete Personal Access Token
Source: https://docs.langchain.com/langsmith/smith-api/api-key/delete-personal-access-token

/langsmith/langsmith-platform-openapi.json delete /api/v1/api-key/current/{pat_id}
DEPRECATED: Use /orgs/current/personal-access-tokens/{pat_id} instead

# Generate Api Key
Source: https://docs.langchain.com/langsmith/smith-api/api-key/generate-api-key

/langsmith/langsmith-platform-openapi.json post /api/v1/api-key
Generate an api key for the user

# Generate Personal Access Token
Source: https://docs.langchain.com/langsmith/smith-api/api-key/generate-personal-access-token

/langsmith/langsmith-platform-openapi.json post /api/v1/api-key/current
DEPRECATED: Use /orgs/current/personal-access-tokens instead

# Get Api Keys
Source: https://docs.langchain.com/langsmith/smith-api/api-key/get-api-keys

/langsmith/langsmith-platform-openapi.json get /api/v1/api-key
Get the current tenant's API keys

# Get Personal Access Tokens
Source: https://docs.langchain.com/langsmith/smith-api/api-key/get-personal-access-tokens

/langsmith/langsmith-platform-openapi.json get /api/v1/api-key/current
DEPRECATED: Use /orgs/current/personal-access-tokens instead

# Get Audit Logs
Source: https://docs.langchain.com/langsmith/smith-api/audit-logs/get-audit-logs

/langsmith/langsmith-platform-openapi.json get /api/v1/audit-logs
Retrieve audit log records for the authenticated user's organization in OCSF format.

Requires both start_time and end_time parameters to filter logs within a date range.
Supports cursor-based pagination.

Returns results in OCSF API Activity (Class UID: 6003) format,
which is compatible with security monitoring and SIEM tools.
Reference: https://schema.ocsf.io/1.7.0/classes/api_activity

# Check Sso Email Verification Status
Source: https://docs.langchain.com/langsmith/smith-api/auth/check-sso-email-verification-status

/langsmith/langsmith-platform-openapi.json post /api/v1/sso/email-verification/status
Retrieve the email verification status of an SSO user.

# Confirm Sso User Email
Source: https://docs.langchain.com/langsmith/smith-api/auth/confirm-sso-user-email

/langsmith/langsmith-platform-openapi.json post /api/v1/sso/email-verification/confirm
Confirm the email of an SSO user.

# Get public auth info
Source: https://docs.langchain.com/langsmith/smith-api/auth/get-public-auth-info

/langsmith/langsmith-platform-openapi.json get /auth/public
Returns public authentication information for the current workspace-level session.

# Get Sso Settings
Source: https://docs.langchain.com/langsmith/smith-api/auth/get-sso-settings

/langsmith/langsmith-platform-openapi.json get /api/v1/sso/settings/{sso_login_slug}
Get SSO provider settings from login slug.

# Login
Source: https://docs.langchain.com/langsmith/smith-api/auth/login

/langsmith/langsmith-platform-openapi.json post /api/v1/login

# Lookup Sso By Email
Source: https://docs.langchain.com/langsmith/smith-api/auth/lookup-sso-by-email

/langsmith/langsmith-platform-openapi.json post /api/v1/sso/email-lookup
Look up SSO providers available for a SCIM-provisioned email address.

# Send Sso Email Confirmation
Source: https://docs.langchain.com/langsmith/smith-api/auth/send-sso-email-confirmation

/langsmith/langsmith-platform-openapi.json post /api/v1/sso/email-verification/send
Send an email to confirm the email address for an SSO user.

# AWS Marketplace fulfillment URL registration
Source: https://docs.langchain.com/langsmith/smith-api/aws_marketplace/aws-marketplace-fulfillment-url-registration

/langsmith/langsmith-platform-openapi.json post /aws-marketplace/register
Receives the x-amzn-marketplace-token posted by AWS Marketplace when a customer clicks "Set Up Account", resolves the customer identity, stores it in the DB, and redirects to the thank-you page.

# Restart a backfill job
Source: https://docs.langchain.com/langsmith/smith-api/backfills/restart-a-backfill-job

/langsmith/langsmith-platform-openapi.json post /v1/platform/ops/backfills/restart
Deletes the backfill job record, causing the backfill to restart from the beginning on the next cron tick. Requires instance admin access.

# Cancel Bulk Export
Source: https://docs.langchain.com/langsmith/smith-api/bulk-exports/cancel-bulk-export

/langsmith/langsmith-platform-openapi.json patch /api/v1/bulk-exports/{bulk_export_id}
Cancel a bulk export by ID

# Create Bulk Export
Source: https://docs.langchain.com/langsmith/smith-api/bulk-exports/create-bulk-export

/langsmith/langsmith-platform-openapi.json post /api/v1/bulk-exports
Create a new bulk export

# Create Bulk Export Destination
Source: https://docs.langchain.com/langsmith/smith-api/bulk-exports/create-bulk-export-destination

/langsmith/langsmith-platform-openapi.json post /api/v1/bulk-exports/destinations
Create a new bulk export destination

# Get Bulk Export
Source: https://docs.langchain.com/langsmith/smith-api/bulk-exports/get-bulk-export

/langsmith/langsmith-platform-openapi.json get /api/v1/bulk-exports/{bulk_export_id}
Get a single bulk export by ID

# Get Bulk Export Destination
Source: https://docs.langchain.com/langsmith/smith-api/bulk-exports/get-bulk-export-destination

/langsmith/langsmith-platform-openapi.json get /api/v1/bulk-exports/destinations/{destination_id}
Get a single bulk export destination by ID

# Get Bulk Export Destinations
Source: https://docs.langchain.com/langsmith/smith-api/bulk-exports/get-bulk-export-destinations

/langsmith/langsmith-platform-openapi.json get /api/v1/bulk-exports/destinations
Get the current workspace's bulk export destinations

# Get Bulk Export Run
Source: https://docs.langchain.com/langsmith/smith-api/bulk-exports/get-bulk-export-run

/langsmith/langsmith-platform-openapi.json get /api/v1/bulk-exports/{bulk_export_id}/runs/{run_id}
Get a single bulk export's run by ID

# Get Bulk Export Runs
Source: https://docs.langchain.com/langsmith/smith-api/bulk-exports/get-bulk-export-runs

/langsmith/langsmith-platform-openapi.json get /api/v1/bulk-exports/{bulk_export_id}/runs
Get a bulk export's runs

# Get Bulk Export Runs Filtered
Source: https://docs.langchain.com/langsmith/smith-api/bulk-exports/get-bulk-export-runs-filtered

/langsmith/langsmith-platform-openapi.json get /api/v1/bulk-exports/runs
Get all bulk export runs for exports that were created from a scheduled bulk export

# Get Bulk Exports
Source: https://docs.langchain.com/langsmith/smith-api/bulk-exports/get-bulk-exports

/langsmith/langsmith-platform-openapi.json get /api/v1/bulk-exports
Get the current workspace's bulk exports

# Update Bulk Export Destination
Source: https://docs.langchain.com/langsmith/smith-api/bulk-exports/update-bulk-export-destination

/langsmith/langsmith-platform-openapi.json patch /api/v1/bulk-exports/destinations/{destination_id}
Update a bulk export destination

# Clone Section
Source: https://docs.langchain.com/langsmith/smith-api/charts/clone-section

/langsmith/langsmith-platform-openapi.json post /api/v1/charts/section/clone
Clone a dashboard.

# Create Chart
Source: https://docs.langchain.com/langsmith/smith-api/charts/create-chart

/langsmith/langsmith-platform-openapi.json post /api/v1/charts/create
Create a new chart.

# Create Section
Source: https://docs.langchain.com/langsmith/smith-api/charts/create-section

/langsmith/langsmith-platform-openapi.json post /api/v1/charts/section
Create a new section.
