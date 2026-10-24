# Assistants
Source: https://docs.langchain.com/langsmith/assistants

*Assistants* are an [Agent Server](/langsmith/agent-server) concept that allow you to manage configurations (e.g., prompts, LLM selection, tools) separately from your graph's core logic. This enables you to create multiple, specialized versions of the same graph architecture with different behavior at runtime. Through configuration variations (rather than structural graph changes), each assistant is optimized for a different [use case](#use-cases).

For example, imagine a general-purpose writing agent built on a common graph architecture. While the structure remains the same, different writing styles—such as blog posts and tweets—require tailored configurations to optimize performance. To support these variations, you can create multiple assistants (e.g., one for blogs and another for tweets) that share the underlying graph but differ in model selection and system prompt.

<img alt="assistant versions" />

The Agent Server API provides several endpoints for creating and managing assistants and their versions. See the [API reference](/langsmith/server-api-ref) for more details.

<Info>
  Assistants are a [LangSmith Deployment](/langsmith/deployment) concept. They are not available in the open source LangGraph library.
</Info>

## Default assistants

When you deploy a graph with LangSmith Deployment, [Agent Server](/langsmith/agent-server) automatically creates a **default assistant** tied to that graph's default configuration. You can then create additional assistants for the same graph, each with its own configuration.

If your deployment defines multiple graphs in [`langgraph.json`](/langsmith/application-structure#configuration-file), each graph gets its own default assistant:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
    "graphs": {
        "graph_id_1": "path_to_graph_id_1",  // default assistant created for graph_id_1
        "graph_id_2": "path_to_graph_id_2"   // default assistant created for graph_id_2
    }
}
```

Assistants have several key features:

* **[Managed via API and UI](/langsmith/configuration-cloud)**: Create, list, update, version, and get assistants using the Agent Server/LangGraph SDKs or the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-assistants).
* **One graph, multiple assistants**: A single deployed graph can support multiple assistants, each with different configurations (e.g., prompts, models, tools).
* **[Versioned](#versioning) configurations**: Each assistant maintains its own configuration history through versioning. Editing an assistant creates a new version, and you can promote or roll back to any version.
* **[Configuration](#configuration) updates without graph changes**: Update prompts, model selection, and other settings through assistant configurations, enabling rapid iteration without modifying or redeploying your graph code.

<Note>
  When invoking an assistant, you can specify either in [`langgraph.json`](/langsmith/application-structure#configuration-file):

  * A **graph ID** (the key in `langgraph.json`, e.g., `"agent"`): Uses the default assistant for that graph.
  * An **assistant ID** (UUID): Uses a specific assistant configuration.

  This flexibility allows you to quickly test with default settings or precisely control which configuration is used.
</Note>

## Configuration

Assistants build on the LangGraph open source concept of [configuration](/oss/python/langgraph/graph-api#runtime-context).

While configuration is available in the open source LangGraph library, assistants are only present in [LangSmith Deployment](/langsmith/deployment) because they are tightly coupled to your deployed graph. Upon deployment, [Agent Server](/langsmith/agent-server) will automatically create a default assistant for each graph using the graph's default configuration settings.

In practice, an assistant is just an *instance* of a graph with a specific configuration. Therefore, multiple assistants can reference the same graph but can contain different configurations (e.g. prompts, models, tools). The LangSmith Deployment API provides several endpoints for creating and managing assistants. See the [API reference](/langsmith/server-api-ref) and [this how-to](/langsmith/configuration-cloud) for more details on how to create assistants.

### Use cases

Assistants are ideal when you need to deploy the same graph architecture with different configurations. Common use cases include:

* **User-level personalization**
  * Customize model selection, system prompts, or tool availability per user.
  * Store user preferences and apply them automatically to each interaction.
  * Enable users to choose between different AI personalities or expertise levels.

* **Customer or organization-specific configurations**
  * Maintain separate configurations for different customers or organizations.
  * Customize behavior for each client without deploying separate infrastructure.
  * Isolate configuration changes to specific customers.

```mermaid actions={false} theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
graph TD
    A["Graph: agent<br/>(deployed)"]
    A --> B["Customer A Assistant<br/>━━━━━━━━━━━━━<br/>Model: GPT-4<br/>Tone: Legal<br/>Tools: Custom"]
    A --> C["Customer B Assistant<br/>━━━━━━━━━━━━━<br/>Model: Claude<br/>Tone: Casual<br/>Tools: Standard"]
    A --> D["Customer C Assistant<br/>━━━━━━━━━━━━━<br/>Model: GPT-3.5<br/>Tone: Formal<br/>Tools: Limited"]

    style A fill:#E5F4FF,stroke:#006DDD,stroke-width:3px,color:#030710
    style B fill:#B3E0F2,stroke:#4A90E2,stroke-width:2px,color:#1E3A5F
    style C fill:#B3E0F2,stroke:#4A90E2,stroke-width:2px,color:#1E3A5F
    style D fill:#B3E0F2,stroke:#4A90E2,stroke-width:2px,color:#1E3A5F
```

* **Environment-specific configurations**
  * Use different models or settings for development, staging, and production.
  * Test configuration changes in staging before promoting to production.
  * Reduce costs in non-production environments with smaller models.

* **A/B testing and experimentation**
  * Compare different prompts, models, or parameter settings.
  * Roll out configuration changes gradually to a subset of users.
  * Measure performance differences between configuration variants.

* **Specialized task variants**
  * Create domain-specific versions of a general-purpose agent.
  * Optimize configurations for different languages, regions, or industries.
  * Maintain consistent graph logic while varying the execution details.

```mermaid actions={false} theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
graph TD
    A["Graph: writing-agent<br/>(deployed)"]
    A --> B["Blog Assistant<br/>━━━━━━━━━━━━━<br/>Model: GPT-4<br/>Tone: Formal<br/>Style: Long-form<br/>Tools: SEO optimization"]
    A --> C["Tweet Assistant<br/>━━━━━━━━━━━━━<br/>Model: GPT-4-mini<br/>Tone: Casual<br/>Style: 280-char limit<br/>Tools: Hashtag suggestions"]
    A --> D["Email Assistant<br/>━━━━━━━━━━━━━<br/>Model: GPT-4<br/>Tone: Professional<br/>Style: Medium length<br/>Tools: Templates"]

    style A fill:#E5F4FF,stroke:#006DDD,stroke-width:3px,color:#030710
    style B fill:#B3E0F2,stroke:#4A90E2,stroke-width:2px,color:#1E3A5F
    style C fill:#B3E0F2,stroke:#4A90E2,stroke-width:2px,color:#1E3A5F
    style D fill:#B3E0F2,stroke:#4A90E2,stroke-width:2px,color:#1E3A5F
```

## How assistants work with deployments

When you deploy a graph with LangSmith Deployment, [Agent Server](/langsmith/agent-server) automatically creates a **default assistant** tied to that graph's default configuration. You can then create additional assistants for the same graph, each with its own configuration.

If your deployment defines multiple graphs in [`langgraph.json`](/langsmith/application-structure#configuration-file), each graph gets its own default assistant:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
    "graphs": {
        "graph_id_1": "path_to_graph_id_1",  // default assistant created for graph_id_1
        "graph_id_2": "path_to_graph_id_2"   // default assistant created for graph_id_2
    }
}
```

That is, there can be multiple default assistants—one for each graph defined in your deployment.

Assistants have several key features:

* **[Managed via API and UI](/langsmith/configuration-cloud)**: Create, list, update, version, and get assistants using the Agent Server/LangGraph SDKs or the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-assistants).
* **One graph, multiple assistants**: A single deployed graph can support multiple assistants, each with different configurations (e.g., prompts, models, tools).
* **[Versioned](#versioning) configurations**: Each assistant maintains its own configuration history through versioning. Editing an assistant creates a new version, and you can promote or roll back to any version.
* **[Configuration](#configuration) updates without graph changes**: Update prompts, model selection, and other settings through assistant configurations, enabling rapid iteration without modifying or redeploying your graph code.

<Note>
  When invoking an assistant, you can specify either in [`langgraph.json`](/langsmith/application-structure#configuration-file):

  * A **graph ID** (e.g., `"agent"`): Uses the default assistant for that graph
  * An **assistant ID** (UUID): Uses a specific assistant configuration

  This flexibility allows you to quickly test with default settings or precisely control which configuration is used.
</Note>

### Configuration

Assistants build on the LangGraph open source concept of [configuration](/oss/python/langgraph/graph-api#runtime-context).

While configuration is available in the open source LangGraph library, assistants are only present in [LangSmith Deployment](/langsmith/deployment) because they are tightly coupled to your deployed graph. Upon deployment, [Agent Server](/langsmith/agent-server) will automatically create a default assistant for each graph using the graph's default configuration settings.

In practice, an assistant is just an *instance* of a graph with a specific configuration. Therefore, multiple assistants can reference the same graph but can contain different configurations (e.g. prompts, models, tools). The LangSmith Deployment API provides several endpoints for creating and managing assistants. See the [API reference](/langsmith/server-api-ref) and [this how-to](/langsmith/configuration-cloud) for more details on how to create assistants.

### Versioning

Assistants support versioning to track changes over time. Once you've created an assistant, subsequent edits will automatically create new versions.

* Each update creates a new version of the assistant.
* You can promote any version to be the active version.
* Rolling back to a previous version is as simple as setting it as active.
* All versions remain available for reference and rollback.

<Warning>
  When updating an assistant, you must provide the entire configuration payload. The update endpoint creates new versions from scratch and does not merge with previous versions. Make sure to include all configuration fields you want to retain.
</Warning>

For more details on how to manage assistant versions, refer to the [Manage assistants guide](/langsmith/configuration-cloud#create-a-new-version-for-your-assistant).

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/assistants.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Log user feedback using the SDK
Source: https://docs.langchain.com/langsmith/attach-user-feedback

LangSmith makes it easy to attach [feedback](/langsmith/observability-concepts#feedback) to [traces](/langsmith/observability-concepts#traces). This feedback can come from users, annotators, automated evaluators, and so on, which is crucial for monitoring and evaluating applications.

This page details how to log feedback using the [SDK](/langsmith/reference). For the structure of feedback objects, refer to [Feedback data format](/langsmith/feedback-data-format).

## Use `create_feedback()` / `createFeedback`

<Info>
  **Child runs**
  You can attach user feedback to **any** child run of a trace, not just the trace (root run) itself.
  This is useful for critiquing specific steps of the LLM application, such as the retrieval step or generation step of a RAG pipeline.
</Info>

<Tip>
  **Non-blocking creation (Python only)**
  The Python client will automatically background feedback creation if you pass `trace_id=` to [`create_feedback()`](https://reference.langchain.com/python/langsmith/client/Client/create_feedback).
  This is essential for low-latency environments, where you want to make sure your application isn't blocked on feedback creation.
</Tip>

The following example creates a trace with two child runs, then logs feedback against the root run and against one of the child runs. The TypeScript snippet shows the equivalent `createFeedback` call shape, assuming a `runId` is already available from your application.

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langsmith import Client, trace, traceable

  @traceable
  def foo(x):
      return {"y": x * 2}

  @traceable
  def bar(y):
      return {"z": y - 1}

  client = Client()

  inputs = {"x": 1}
  with trace(name="foobar", inputs=inputs) as root_run:
      result = foo(**inputs)
      result = bar(**result)
      root_run.outputs = result
      trace_id = root_run.id
      child_runs = root_run.child_runs

  # Provide feedback for a trace (a.k.a. a root run)
  client.create_feedback(
      key="user_feedback",
      score=1,
      trace_id=trace_id,
      comment="the user said that ..."
  )

  # Provide feedback for a child run
  foo_run_id = [run for run in child_runs if run.name == "foo"][0].id
  client.create_feedback(
      key="correctness",
      score=0,
      run_id=foo_run_id,
      # trace_id= is optional but recommended to enable batched and backgrounded
      # feedback ingestion.
      trace_id=trace_id,
  )
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { Client } from "langsmith";
  const client = new Client();

      // ... Run your application and get the run_id...
      // This information can be the result of a user-facing feedback form

  await client.createFeedback(
      runId,
      "feedback-key",
      {
          score: 1.0,
          comment: "comment",
      }
  );
  ```
</CodeGroup>

You can even log feedback for in-progress runs using [`create_feedback()`](https://reference.langchain.com/python/langsmith/client/Client/create_feedback) / [`createFeedback`](https://reference.langchain.com/javascript/classes/langsmith.client.Client.html#createfeedback). See [Access the current run (span) within a traced function](/langsmith/access-current-span) for how to get the run ID of an in-progress run.

## Collect feedback from client-side applications

If you need to collect feedback from a browser or other client-side environment without exposing your API key, use **presigned feedback tokens**. These generate a URL scoped to a specific run and feedback key that clients can call directly.

See [Collect feedback with presigned URLs](/langsmith/presigned-feedback-tokens) for the full guide.

To learn more about how to filter traces based on various attributes, including user feedback, see [Filter traces](/langsmith/filter-traces-in-application).

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/attach-user-feedback.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# How to audit evaluator scores
Source: https://docs.langchain.com/langsmith/audit-evaluator-scores

LLM-as-a-judge evaluators don't always get it right. Because of this, it is often useful for a human to manually audit the scores left by an evaluator and correct them where necessary. LangSmith allows you to make corrections on evaluator scores in the UI or SDK.

## In the comparison view

In the comparison view, you may click on any feedback tag to bring up the feedback details. From there, click the "edit" icon on the right to bring up the corrections view. You may then type in your desired score in the text box under "Make correction". If you would like, you may also attach an explanation to your correction. This is useful if you are using a [few-shot evaluator](/langsmith/create-few-shot-evaluators) and will be automatically inserted into your few-shot examples in place of the `few_shot_explanation` prompt variable.

<img alt="Audit Evaluator Comparison View" />

## In the runs table

In the runs table, find the "Feedback" column and click on the feedback tag to bring up the feedback details. Again, click the "edit" icon on the right to bring up the corrections view.

<img alt="Audit Evaluator Runs Table" />

## In the SDK

Corrections can be made via the SDK's `update_feedback` function, with the `correction` dict. You must specify a `score` key which corresponds to a number for it to be rendered in the UI.

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import langsmith

  client = langsmith.Client()

  client.update_feedback(
      my_feedback_id,
      correction={
          "score": 1,
      },
  )
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { Client } from 'langsmith';

  const client = new Client();

  await client.updateFeedback(
      myFeedbackId,
      {
          correction: {
              score: 1,
          }
      }
  )
  ```
</CodeGroup>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/audit-evaluator-scores.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
