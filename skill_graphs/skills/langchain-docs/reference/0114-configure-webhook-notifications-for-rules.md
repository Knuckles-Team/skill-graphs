# Configure webhook notifications for rules
Source: https://docs.langchain.com/langsmith/webhooks

Configure webhook notifications to receive POST requests when automation rules match new runs in LangSmith.

When you add a webhook URL on an automation action, LangSmith makes a POST request to your webhook endpoint any time the rules you defined match any new runs.

<img alt="Webhook" />

## Webhook payload

The payload LangSmith sends to your webhook endpoint contains:

* `"rule_id"`: this is the ID of the automation that sent this payload.
* `"start_time"` and `"end_time"`: these are the time boundaries where LangSmith found matching runs.
* `"runs"`: this is an array of runs, where each run is a dictionary. If you need more information about each run, use the SDK in your endpoint to fetch it from the API.
* `"feedback_stats"`: this is a dictionary with the feedback statistics for the runs. An example payload for this field is shown in the following code block.

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
"feedback_stats": {
    "about_langchain": {
        "n": 1,
        "avg": 0.0,
        "show_feedback_arrow": true,
        "values": {}
    },
    "category": {
        "n": 0,
        "avg": null,
        "show_feedback_arrow": true,
        "values": {
            "CONCEPTUAL": 1
        }
    },
    "user_score": {
        "n": 2,
        "avg": 0.0,
        "show_feedback_arrow": false,
        "values": {}
    },
    "vagueness": {
        "n": 1,
        "avg": 0.0,
        "show_feedback_arrow": true,
        "values": {}
    }
}
```

<Note>
  **fetching from S3 URLs**

  Depending on how recent your runs are, the `inputs_s3_urls` and `outputs_s3_urls` fields may contain S3 URLs to the actual data instead of the data itself.

  The `inputs` and `outputs` can be fetched by the `ROOT.presigned_url` provided in `inputs_s3_urls` and `outputs_s3_urls` respectively.
</Note>

This is an example of the entire payload LangSmith sends to your webhook endpoint:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "rule_id": "d75d7417-0c57-4655-88fe-1db3cda3a47a",
  "start_time": "2024-04-05T01:28:54.734491+00:00",
  "end_time": "2024-04-05T01:28:56.492563+00:00",
  "runs": [
    {
      "status": "success",
      "is_root": true,
      "trace_id": "6ab80f10-d79c-4fa2-b441-922ed6feb630",
      "dotted_order": "20230505T051324571809Z6ab80f10-d79c-4fa2-b441-922ed6feb630",
      "run_type": "tool",
      "modified_at": "2024-04-05T01:28:54.145062",
      "tenant_id": "2ebda79f-2946-4491-a9ad-d642f49e0815",
      "end_time": "2024-04-05T01:28:54.085649",
      "name": "Search",
      "start_time": "2024-04-05T01:28:54.085646",
      "id": "6ab80f10-d79c-4fa2-b441-922ed6feb630",
      "session_id": "6a3be6a2-9a8c-4fc8-b4c6-a8983b286cc5",
      "parent_run_ids": [],
      "child_run_ids": null,
      "direct_child_run_ids": null,
      "total_tokens": 0,
      "completion_tokens": 0,
      "prompt_tokens": 0,
      "total_cost": null,
      "completion_cost": null,
      "prompt_cost": null,
      "first_token_time": null,
      "app_path": "/o/2ebda79f-2946-4491-a9ad-d642f49e0815/projects/p/6a3be6a2-9a8c-4fc8-b4c6-a8983b286cc5/r/6ab80f10-d79c-4fa2-b441-922ed6feb630?trace_id=6ab80f10-d79c-4fa2-b441-922ed6feb630&start_time=2023-05-05T05:13:24.571809",
      "in_dataset": false,
      "last_queued_at": null,
      "inputs": null,
      "inputs_s3_urls": null,
      "outputs": null,
      "outputs_s3_urls": null,
      "extra": null,
      "events": null,
      "feedback_stats": null,
      "serialized": null,
      "share_token": null
    }
  ]
}
```

## Security

Add a secret query string parameter to the webhook URL and verify it on every incoming request. This ensures that if someone discovers your webhook URL, you can distinguish those calls from authentic webhook notifications.

An example would be

```
https://api.example.com/langsmith_webhook?secret=38ee77617c3a489ab6e871fbeb2ec87d
```

### Webhook custom HTTP headers

If you'd like to send any specific headers with your webhook, this can be configured per URL. To set this up, click on the `Headers` option next to the URL field and add your headers.

<Note>
  Headers are stored in encrypted format.
</Note>

<img alt="Webhook headers" />

### Webhook delivery

When delivering events to your webhook endpoint, LangSmith follows these guidelines:

* If LangSmith fails to connect to your endpoint, LangSmith retries the transport connection up to 2 times before declaring the delivery failed.
* If your endpoint takes longer than 5 seconds to reply, LangSmith declares the delivery failed and does not retry.
* If your endpoint returns a 5xx status code in less than 5 seconds, LangSmith retries up to 2 times with exponential backoff.
* If your endpoint returns a 4xx status code, LangSmith declares the delivery failed and does not retry.
* Anything your endpoint returns in the body will be ignored.

## Ensuring evaluations complete before the webhook fires

By default, automation rules run on independent schedules. A webhook rule and an online evaluator rule scanning the same project can pick up the same run at different times, so the webhook may fire before the evaluator has had a chance to score the run.

The recommended solution is to add a *feedback filter* to your webhook rule. This tells LangSmith to send a run to your webhook only once it already carries the expected score, regardless of when it was evaluated.

For example, you have an online evaluator that produces an `answer_usefulness` score, and a webhook rule that should only fire after that score is present.

1. Open the webhook automation rule in the **Automations** tab of your tracing project.

2. Edit the rule's filter to require the feedback key. In the filter builder, add a condition:

   ```
   has(feedback_key, "answer_usefulness")
   ```

3. Save the rule.

Now the webhook rule will skip any run that does not yet have an `answer_usefulness` score. When the evaluator rule runs and attaches the score, the webhook rule's next polling cycle will pick up those runs and send them to your endpoint.

<Tip>
  You can also filter on the score value itself, not just its presence. For example, to only send runs with a low usefulness score to your endpoint:

  ```
  has(feedback_key, "answer_usefulness") and feedback_score < 0.5
  ```

  For the full filter syntax, refer to [Filter traces](/langsmith/filter-traces-in-application).
</Tip>

<Note>
  Within a single automation rule, actions execute in a fixed order: annotation queue → dataset → webhook → evaluation. This means that if your webhook and evaluator are configured on the **same** rule, the webhook will always fire before the evaluation completes on that rule's run. To ensure the webhook receives evaluation scores, keep the webhook and evaluator as **separate rules** and use a feedback filter on the webhook rule as described in the example.
</Note>

## Example with Modal

### Setup

For an example of how to set this up, this guide uses [Modal](https://modal.com/). Modal provides autoscaling GPUs for inference and fine-tuning, secure containerization for code agents, and serverless Python web endpoints. This guide focuses on the web endpoints.

First, create a Modal account. Then, locally install the Modal SDK:

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install modal
  ```

  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv add modal
  ```
</CodeGroup>

To finish setting up your account, run the command:

```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
modal setup
```

Follow the instructions to finish setting up your account.

### Secrets

Next, you will need to set up some secrets in Modal.

First, LangSmith will need to authenticate to Modal by passing in a secret.
The easiest way to do this is to pass in a secret in the query parameters.
To validate this secret, add a secret in *Modal* to validate it.
Do this by [creating a Modal secret](https://modal.com/docs/guide/secrets).
Name the secret `ls-webhook` and set an environment variable with the name `LS_WEBHOOK`.

You can also set up a LangSmith secret—luckily there is already an integration template for this!

<img alt="LangSmith Modal Template" />

### Service

After that, you can create a Python file that will serve as your endpoint.
An example is shown in the following code block, with comments explaining what is going on:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from fastapi import HTTPException, status, Request, Query
from modal import Secret, Stub, web_endpoint, Image

stub = Stub("auth-example", image=Image.debian_slim().pip_install("langsmith"))

@stub.function(
    secrets=[Secret.from_name("ls-webhook"), Secret.from_name("my-langsmith-secret")]
)

# We want this to be a `POST` endpoint since we will post data here
@web_endpoint(method="POST")

# We set up a `secret` query parameter
def f(data: dict, secret: str = Query(...)):
    # You can import dependencies you don't have locally inside Modal functions
    from langsmith import Client

    # First, we validate the secret key we pass
    import os

    if secret != os.environ["LS_WEBHOOK"]:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect bearer token",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # This is where we put the logic for what should happen inside this webhook
    ls_client = Client()
    runs = data["runs"]
    ids = [r["id"] for r in runs]
    feedback = list(ls_client.list_feedback(run_ids=ids))
    for r, f in zip(runs, feedback):
        try:
            ls_client.create_example(
                inputs=r["inputs"],
                outputs={"output": f.correction},
                dataset_name="classifier-github-issues",
            )
        except Exception:
            raise ValueError(f"{r} and {f}")
    # Function body
    return "success!"
```

Deploy this with `modal deploy ...` (see [managing Modal deployments](https://modal.com/docs/guide/managing-deployments)).

You should now get something like:

```
✓ Created objects.
├── 🔨 Created mount /Users/harrisonchase/workplace/langsmith-docs/example-webhook.py
├── 🔨 Created mount PythonPackage:langsmith
└── 🔨 Created f => https://hwchase17--auth-example-f.modal.run
✓ App deployed! 🎉

View Deployment: https://modal.com/apps/hwchase17/auth-example
```

Note the function URL: `https://hwchase17--auth-example-f.modal.run`.
NOTE: this is NOT the final deployment URL, make sure not to accidentally use that.

### Hooking it up

Take the function URL you created previously and add it as a webhook.
Remember to also pass in the secret key as a query parameter.
Putting it all together, it should look something like:

```
https://hwchase17--auth-example-f-dev.modal.run?secret={SECRET}
```

Replace `{SECRET}` with the secret key you created to access the Modal service.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/webhooks.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Workload isolation
Source: https://docs.langchain.com/langsmith/workload-isolation

LangSmith uses a hierarchical structure to organize your work: [*organizations*](/langsmith/administration-overview#organizations), [*workspaces*](/langsmith/administration-overview#workspaces), [*applications*](/langsmith/administration-overview#applications), and [*resources*](/langsmith/administration-overview#resources). This structure lets you balance collaboration with access control, allowing you to choose the right level of isolation for your team's needs.

The LangSmith permission system builds on this hierarchy. With [role-based access control (RBAC)](/langsmith/rbac), user [permissions](/langsmith/organization-workspace-operations) are scoped to one or more workspaces, enforcing isolation between workspaces. With more fine-grained [attribute-based access control](/langsmith/organization-workspace-operations#access-policies) (ABAC), access can be further restricted or granted based on attributes such as tags or applications within a workspace (for example, allowing users to access only development resources or only resources associated with a specific application).

This page explains three common approaches to organizing workspaces based on your team's isolation requirements:

* [Team-centric workspaces](#team-centric-workspaces): Single workspace per team (recommended for most customers)
* [Collaborative workspaces](#collaborative-workspaces): Multiple teams per workspace
* [Project-isolated workspaces](#project-isolated-workspaces): Multiple workspaces per team (for strict isolation requirements)

<Tip>
  For details on setting up organizations and workspaces, refer to [Set up hierarchy](/langsmith/set-up-hierarchy).
</Tip>

## Team-centric workspaces

<Warning>
  This is the default model and recommended choice for most customers.
</Warning>

This model (single workspace per team) uses a single organization as the top-level boundary. Within the organization, multiple workspaces are used to isolate different teams or business units. Each workspace represents a logical boundary for a specific team and governs which data and resources that team can access. Within a workspace, teams use multiple applications to group together resources that support the same agent. An application may also contain distinct resources, such as separate tracing projects, for development and production environments.

```mermaid actions={false} theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
graph LR
    Org[Organization]

    WS1[Workspace: Team A]
    WS2[Workspace: Team B]

    App1A[Application]
    App1B[Application]

    DevA[Dev Tracing Project]
    ProdA[Prod Tracing Project]
    DatasetA[Dataset]

    DevB[Dev Tracing Project]
    ProdB[Prod Tracing Project]
    DatasetB[Dataset]

    Org --> WS1
    Org --> WS2

    WS1 --> App1A
    WS2 --> App1B

    App1A --> DevA
    App1A --> ProdA
    App1A --> DatasetA

    App1B --> DevB
    App1B --> ProdB
    App1B --> DatasetB

    classDef orgStyle fill:#B2DEFF,stroke:#006DDD,stroke-width:2px,color:#030710
    classDef wsStyle fill:#E5F4FF,stroke:#006DDD,stroke-width:2px,color:#030710
    classDef appStyle fill:#F6FFDB,stroke:#6E8900,stroke-width:2px,color:#2E3900
    classDef resourceStyle fill:#F2FAFF,stroke:#40668D,stroke-width:1px,color:#2F4B68

    class Org orgStyle
    class WS1,WS2 wsStyle
    class App1A,App1B appStyle
    class DevA,ProdA,DatasetA,DevB,ProdB,DatasetB resourceStyle
```

* **Pros:** A single workspace allows all team resources to be shared, making collaboration and iteration within a team straightforward. It also simplifies promotion from development to production. For example, the same [prompt](/langsmith/prompt-engineering) can be versioned and promoted to production using tags, without copying or duplication.
* **Cons:** The primary trade-off is limited isolation between environments of the same team. Development, test, and production resources coexist within the same application, so teams must rely on tagging and conventions to avoid accidental impact on production. [RBAC](/langsmith/rbac) is scoped at the workspace level. [ABAC](/langsmith/organization-workspace-operations#access-policies) provides more granular permissions within a workspace by restricting access based on resource attributes, such as allowing a user to access only development resources.

## Collaborative workspaces

In this model (multiple teams per workspace), multiple teams share a single workspace within an organization and use applications and [ABAC](/langsmith/organization-workspace-operations#access-policies) to separate resources and govern access. As a result, shared resources such as [prompts](/langsmith/prompt-engineering) and [deployments](/langsmith/deployment) can be reused across teams, while access to sensitive resources like [traces](/langsmith/observability-concepts#traces) and [datasets](/langsmith/evaluation-concepts#datasets) is limited to the owning team.

```mermaid actions={false} theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
graph LR
    Org[Organization]

    WS[Shared Workspace]

    AppA[Application: Team A]
    AppB[Application: Team B]

    TracesA[Traces: Team A]
    DatasetA[Dataset: Team A]
    PromptA[Prompt: Shared]

    TracesB[Traces: Team B]
    DatasetB[Dataset: Team B]
    PromptB[Prompt: Shared]

    Org --> WS

    WS --> AppA
    WS --> AppB

    AppA --> TracesA
    AppA --> DatasetA
    AppA --> PromptA

    AppB --> TracesB
    AppB --> DatasetB
    AppB --> PromptB

    classDef orgStyle fill:#B2DEFF,stroke:#006DDD,stroke-width:2px,color:#030710
    classDef wsStyle fill:#E5F4FF,stroke:#006DDD,stroke-width:2px,color:#030710
    classDef appStyle fill:#F6FFDB,stroke:#6E8900,stroke-width:2px,color:#2E3900
    classDef restrictedStyle fill:#F8E8E6,stroke:#B27D75,stroke-width:1px,color:#634643
    classDef sharedStyle fill:#FDF3FF,stroke:#7E65AE,stroke-width:1px,color:#504B5F

    class Org orgStyle
    class WS wsStyle
    class AppA,AppB appStyle
    class TracesA,DatasetA,TracesB,DatasetB restrictedStyle
    class PromptA,PromptB sharedStyle
```

* **Pros:** Common resources such as prompts and deployments can be shared and reused across teams, increasing collaboration and reducing duplicated work. Unlike the team-centric workspace model, collaboration is not limited to a single team and can span all teams within the workspace.
* **Cons:** Isolation between teams and environments is weaker than in multi-workspace models and depends on correct use of ABAC. Misconfigured tags or policies can expose sensitive [traces](/langsmith/observability-concepts#traces) or [datasets](/langsmith/evaluation-concepts#datasets) across teams, and managing permissions across multiple teams adds operational complexity.

## Project-isolated workspaces

<Callout icon="check">
  This approach should be used only when strict isolation is required.
</Callout>

In this model (multiple workspaces per team), isolation is increased by creating multiple workspaces for a single team. Workspaces may be organized by project or by environment, such as separate development and production workspaces. Each workspace is fully isolated, with its own users, data, and resources, and access is strictly scoped to that workspace.

```mermaid actions={false} theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
graph LR
    Org[Organization]

    WSDev[Workspace: Dev]
    WSProd[Workspace: Prod]

    AppDev[Application]
    AppProd[Application]

    TracesDev[Traces]
    DatasetDev[Dataset]
    DeploymentDev[Deployment]

    TracesProd[Traces]
    DatasetProd[Dataset]
    DeploymentProd[Deployment]

    Org --> WSDev
    Org --> WSProd

    WSDev --> AppDev
    WSProd --> AppProd

    AppDev --> TracesDev
    AppDev --> DatasetDev
    AppDev --> DeploymentDev

    AppProd --> TracesProd
    AppProd --> DatasetProd
    AppProd --> DeploymentProd

    classDef orgStyle fill:#B2DEFF,stroke:#006DDD,stroke-width:2px,color:#030710
    classDef wsStyle fill:#E5F4FF,stroke:#006DDD,stroke-width:2px,color:#030710
    classDef appStyle fill:#F6FFDB,stroke:#6E8900,stroke-width:2px,color:#2E3900
    classDef resourceStyle fill:#F2FAFF,stroke:#40668D,stroke-width:1px,color:#2F4B68

    class Org orgStyle
    class WSDev,WSProd wsStyle
    class AppDev,AppProd appStyle
    class TracesDev,DatasetDev,DeploymentDev,TracesProd,DatasetProd,DeploymentProd resourceStyle
```

* **Pros:** Strong isolation between teams, projects, and environments. Users with only access to the development workspace cannot view or access production data or any production resources, reducing the risk of accidental changes or cross-environment misuse.
* **Cons:** Resources cannot be shared across workspaces. Reusing [prompts](/langsmith/prompt-engineering), [datasets](/langsmith/evaluation-concepts#datasets), or [experiments](/langsmith/evaluation-concepts#experiment), even when promoting an agent from development to production, requires manual copying between workspaces, which introduces friction and duplication.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/workload-isolation.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Write your prompt with AI
Source: https://docs.langchain.com/langsmith/write-prompt-with-ai

The prompt canvas makes it easy to edit a prompt with the help of an LLM. This allows you to iterate faster on long prompts and also makes it easier to make overarching stylisting or tonal changes to your prompt. You can enter the promp canvas by clicking the glowing wand over any message in your prompt:

<img alt="Prompt canvas open" />

## Chat sidebar

You can use the chat sidebar to ask questions about your prompt, or to give instructions in natural language to the LLM for how to rewrite your prompt.

<img alt="Prompt canvas rewrite" />

<Note>
  You can also edit the prompt directly - you don't **need** to use the LLM. This is useful if you know what edits you want to make and just want to make them directly
</Note>

## Quick actions

There are quick actions to change the reading level or length of the prompt with a single mouse click:

<img alt="Prompt canvas quick actions" />

## Custom quick actions

You can also save your own custom quick actions, for ease of use across all the prompts you are working on in LangSmith:

<img alt="Prompt canvas custom quick action" />

## Diffing

You can also see the specific differences between each version of your prompt by selecting the diff slider in the top right of the canvas:

<img alt="Prompt canvas diff" />

## Saving and using prompts

Lastly, you can save the prompt you have created in the canvas by clicking the "Use this Version" button in the bottom right:

<img alt="Prompt canvas save" />

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/write-prompt-with-ai.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Build
Source: https://docs.langchain.com/oss/javascript/build-overview

Build agents with LangChain, LangGraph, and Deep Agents using TypeScript.

<div>
  <div>
    <h1>Build</h1>

    The LangChain open source stack provides the building blocks you need to design, test, and ship agents in TypeScript.

    <h2>Choose your starting point</h2>

    Deep Agents, LangChain, and LangGraph share the same stack, so choose based on how much control you need:

    <CardGroup>
      <Card title="Deep Agents" href="/oss/javascript/deepagents/overview" icon="https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/deep-agents-icon.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=1cc68f66a9e7550331cc0875f1ba53af">
        Build agents for complex, long-running tasks. A complete agent harness with planning, subagents, a virtual filesystem, and long-term memory built in. The fastest way to start.
      </Card>

      <Card title="LangChain" href="/oss/javascript/langchain/overview" icon="https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/langchain-icon.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=663b30f85baf99ad708b97e05da2a5a4">
        A minimal, configurable agent framework. Compose exactly what you need from models, tools, prompts, and middleware.
      </Card>

      <Card title="LangGraph" href="/oss/javascript/langgraph/overview" icon="https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/langgraph-icon.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=b997e1a7487d507a36556eedbfd99f81">
        Low-level orchestration for stateful, long-running agents: durable execution, streaming, memory, and human-in-the-loop.
      </Card>
    </CardGroup>

    <h2>Explore</h2>

    <CardGroup>
      <Card title="Integrations" href="/oss/javascript/integrations/providers/overview" icon="plug">
        Connect to model providers, vector stores, retrievers, and other components.
      </Card>

      <Card title="Learn" href="/oss/javascript/learn" icon="book">
        Follow tutorials and conceptual guides for common agent patterns and use cases.
      </Card>

      <Card title="Reference" href="/oss/javascript/reference/overview" icon="code">
        API references, error codes, release notes, and migration guides.
      </Card>

      <Card title="Contribute" href="/oss/javascript/contributing/overview" icon="heart-plus">
        Contribute documentation, code, and integrations to the LangChain ecosystem.
      </Card>
    </CardGroup>
  </div>
</div>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/javascript/build-overview.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Errors
Source: https://docs.langchain.com/oss/javascript/common-errors

This page contains guides around resolving common errors you may find while building with LangChain and LangGraph.

Errors referenced below will have an `lc_error_code` property corresponding to one of the below codes when they are thrown in code.

| Error code                                                                                              |
| ------------------------------------------------------------------------------------------------------- |
| [GRAPH\_RECURSION\_LIMIT](/oss/javascript/langgraph/errors/GRAPH_RECURSION_LIMIT)                       |
| [INVALID\_CHAT\_HISTORY](/oss/javascript/langgraph/errors/INVALID_CHAT_HISTORY)                         |
| [INVALID\_CONCURRENT\_GRAPH\_UPDATE](/oss/javascript/langgraph/errors/INVALID_CONCURRENT_GRAPH_UPDATE)  |
| [INVALID\_GRAPH\_NODE\_RETURN\_VALUE](/oss/javascript/langgraph/errors/INVALID_GRAPH_NODE_RETURN_VALUE) |
| [INVALID\_PROMPT\_INPUT](/oss/javascript/langchain/errors/INVALID_PROMPT_INPUT)                         |
| [INVALID\_TOOL\_RESULTS](/oss/javascript/langchain/errors/INVALID_TOOL_RESULTS)                         |
| [MESSAGE\_COERCION\_FAILURE](/oss/javascript/langchain/errors/MESSAGE_COERCION_FAILURE)                 |
| [MISSING\_CHECKPOINTER](/oss/javascript/langgraph/errors/MISSING_CHECKPOINTER)                          |
| [MODEL\_AUTHENTICATION](/oss/javascript/langchain/errors/MODEL_AUTHENTICATION)                          |
| [MODEL\_NOT\_FOUND](/oss/javascript/langchain/errors/MODEL_NOT_FOUND)                                   |
| [MODEL\_RATE\_LIMIT](/oss/javascript/langchain/errors/MODEL_RATE_LIMIT)                                 |
| [MULTIPLE\_SUBGRAPHS](/oss/javascript/langgraph/errors/MULTIPLE_SUBGRAPHS)                              |
| [OUTPUT\_PARSING\_FAILURE](/oss/javascript/langchain/errors/OUTPUT_PARSING_FAILURE)                     |

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/common-errors.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Context overview
Source: https://docs.langchain.com/oss/javascript/concepts/context

**Context engineering** is the practice of building dynamic systems that provide the right information and tools, in the right format, so that an AI application can accomplish a task. Context can be characterized along two key dimensions:

1. By **mutability**:
   * **Static context**: Immutable data that doesn't change during execution (e.g., user metadata, database connections, tools)
   * **Dynamic context**: Mutable data that evolves as the application runs (e.g., conversation history, intermediate results, tool call observations)
2. By **lifetime**:
   * **Runtime context**: Data scoped to a single run or invocation
   * **Cross-conversation context**: Data that persists across multiple conversations or sessions

<Tip>
  Runtime context refers to local context: data and dependencies your code needs to run. It does **not** refer to:

  * The LLM context, which is the data passed into the LLM's prompt.
  * The "context window", which is the maximum number of tokens that can be passed to the LLM.

  The runtime context is how you thread data through your agent. Rather than storing things in global state, you can attach values — like a database connection, user session, or configuration — to the context and access them inside tools and middleware. This keeps things stateless, testable, and reusable. For example, you can use user metadata in the runtime context to fetch user preferences and feed them into the context window.
</Tip>

LangGraph provides three ways to manage context, which combines the mutability and lifetime dimensions:

| Context type                                                                          | Description                                   | Mutability | Lifetime           |
| ------------------------------------------------------------------------------------- | --------------------------------------------- | ---------- | ------------------ |
| [**Config**](#config)                                                                 | data passed at the start of a run             | Static     | Single run         |
| [**Dynamic runtime context (state)**](#dynamic-runtime-context)                       | Mutable data that evolves during a single run | Dynamic    | Single run         |
| [**Dynamic cross-conversation context (store)**](#dynamic-cross-conversation-context) | Persistent data shared across conversations   | Dynamic    | Cross-conversation |

## Config

Config is for immutable data like user metadata or API keys. Use this when you have values that don't change mid-run.

Specify configuration using a key called **"configurable"** which is reserved for this purpose.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
await graph.invoke(
  { messages: [{ role: "user", content: "hi!" }] },
  { configurable: { user_id: "user_123" } } // [!code highlight]
);
```

## Dynamic runtime context

**Dynamic runtime context** represents mutable data that can evolve during a single run and is managed through the LangGraph state object. This includes conversation history, intermediate results, and values derived from tools or LLM outputs. In LangGraph, the state object acts as [short-term memory](/oss/javascript/concepts/memory) during a run.

<Tabs>
  <Tab title="In an agent">
    Example shows how to incorporate state into an agent **prompt**.

    State can also be accessed by the agent's **tools**, which can read or update the state as needed. See [tool calling guide](/oss/javascript/langchain/tools#access-context) for details.

    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { createAgent, createMiddleware } from "langchain";
    import type { AgentState } from "langchain";
    import * as z from "zod";

    const CustomState = z.object({ // [!code highlight]
      userName: z.string(),
    });

    const personalizedPrompt = createMiddleware({ // [!code highlight]
      name: "PersonalizedPrompt",
      stateSchema: CustomState,
      wrapModelCall: (request, handler) => {
        const userName = request.state.userName || "User";
        const systemPrompt = `You are a helpful assistant. User's name is ${userName}`;
        return handler({ ...request, systemPrompt });
      },
    });

    const agent = createAgent({  // [!code highlight]
      model: "claude-sonnet-4-6",
      tools: [/* your tools here */],
      middleware: [personalizedPrompt] as const, // [!code highlight]
    });

    await agent.invoke({
      messages: [{ role: "user", content: "hi!" }],
      userName: "John Smith",
    });
    ```
  </Tab>

  <Tab title="In a workflow">
    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { z } from "zod/v4";
    import { StateGraph, StateSchema, MessagesValue, START } from "@langchain/langgraph";

    const CustomState = new StateSchema({  // [!code highlight]
      messages: MessagesValue,
      extraField: z.number(),
    });

    const builder = new StateGraph(CustomState)
      .addNode("node", async (state) => {  // [!code highlight]
        const messages = state.messages;
        // ...
        return {  // [!code highlight]
          extraField: state.extraField + 1,
        };
      })
      .addEdge(START, "node");

    const graph = builder.compile();
    ```
  </Tab>
</Tabs>

<Tip>
  **Turning on memory**
  Please see the [memory guide](/oss/javascript/langgraph/add-memory) for more details on how to enable memory. This is a powerful feature that allows you to persist the agent's state across multiple invocations. Otherwise, the state is scoped only to a single run.
</Tip>

## Dynamic cross-conversation context

**Dynamic cross-conversation context** represents persistent, mutable data that spans across multiple conversations or sessions and is managed through the LangGraph store. This includes user profiles, preferences, and historical interactions. The LangGraph store acts as [long-term memory](/oss/javascript/concepts/memory#long-term-memory) across multiple runs. This can be used to read or update persistent facts (e.g., user profiles, preferences, prior interactions).

## Learn more

* [Memory conceptual overview](/oss/javascript/concepts/memory)
* [Short-term memory in LangChain](/oss/javascript/langchain/short-term-memory)
* [Memory in LangGraph](/oss/javascript/langgraph/add-memory)

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/concepts/context.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
