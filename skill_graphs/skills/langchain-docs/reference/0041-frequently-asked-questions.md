# Frequently asked questions
Source: https://docs.langchain.com/langsmith/faq

## Observability

### *I can't create API keys or manage users in the UI, what's wrong?*

* You have likely deployed LangSmith without setting up SSO. LangSmith requires SSO to manage users and API keys. You can find more information on setting up SSO in the [configuration section.](/langsmith/self-host-sso)

### *How does load balancing/ingress work*?

* You will need to expose the frontend container/service to your applications/users. This will handle routing to all downstream services.
* You will need to terminate SSL at the ingress level. We recommend using a managed service like AWS ALB, GCP Load Balancer, or Nginx.

### *How can we authenticate to the application?*

* Currently, our self-hosted solution supports SSO with OAuth2.0 and OIDC as an authn solution. Note, we do offer a no-auth solution but highly recommend setting up oauth before moving into production.

You can find more information on setting up SSO in the [configuration section.](/langsmith/self-host-sso)

### *Can I use external storage services?*

* You can configure LangSmith to use external versions of all storage services. In a production setting, we strongly recommend using external storage services. Check out the [configuration section](/langsmith/self-hosted) for more information.

### *Does my application need egress to function properly?*

Our deployment only needs egress for a few things (most of which can reside within your VPC):

* Fetching images (If mirroring your images, this may not be needed)

* Talking to any LLM endpoints

* Talking to any external storage services you may have configured

* Fetching OAuth information

* Subscription Metrics and Operational Metadata (if not running in offline mode)

  * Requires egress to `https://beacon.langchain.com`
  * See [Egress](/langsmith/self-host-egress) for more information

Your VPC can set up rules to limit any other access. Note: We require the `X-Organization-Id` and `X-Tenant-Id` headers to be allowed to be passed through to the backend service. These are used to determine which organization and workspace (previously called "tenant") the request is for.

### *Resource requirements for the application?*

* In kubernetes, we recommend a minimum helm configuration which you can see in the [medium size example](https://github.com/langchain-ai/helm/blob/main/charts/langsmith/examples/medium_size.yaml). For docker, we recommend a minimum of 16GB of RAM and 4 CPUs.
* For Postgres, we recommend a minimum of 8GB of RAM and 2 CPUs.
* For Redis, we recommend 4GB of RAM and 2 CPUs.
* For Clickhouse, we recommend 32GB of RAM and 8 CPUs.

### SAML SSO FAQs

#### *How do I change a SAML SSO user's email address?*

Some identity providers retain the original `User ID` through an email change while others do not, so we recommend that you follow these steps to avoid duplicate users in LangSmith:

1. Remove the user from the organization (see [manage users](/langsmith/set-up-hierarchy#manage-users))
2. Change their email address in the IdP
3. Have them login to LangSmith again via SAML SSO - this will trigger the usual [JIT provisioning](/langsmith/user-management#just-in-time-jit-provisioning) flow with their new email address

Changing email address via SCIM or otherwise is not currently supported for users with multiple linked login methods. This error message is shown: `email update not supported with linked login methods`. For example, if a user previously logged in via email/password or Google social login, and then is added with the same email address via SSO, changing their email address is not supported. This applies to both self-hosted and cloud.

#### *Can I change identity providers?*

Reach out to the LangChain support team through our portal at [https://support.langchain.com](https://support.langchain.com) for support on migration.

#### *How do I fix "405 method not allowed"?*

Ensure you're using the correct ACS URL: [https://auth.langchain.com/auth/v1/sso/saml/acs](https://auth.langchain.com/auth/v1/sso/saml/acs)

### SCIM FAQs

#### *Can I use SCIM without SAML SSO?*

* **Cloud**: No, SAML SSO is required for SCIM in cloud deployments
* **Self-hosted**: Yes, SCIM works with OAuth with Client Secret authentication mode

#### *What happens if I have both JIT provisioning and SCIM enabled?*

JIT provisioning and SCIM can conflict with each other. We recommend disabling JIT provisioning before enabling SCIM to ensure consistent user provisioning behavior.

#### *How do I change a user's role or workspace access?*

Update the user's group membership in your IdP. The changes will be synchronized to LangSmith according to the [role precedence rules](/langsmith/user-management#role-precedence).

#### *What happens when a user is removed from all groups?*

The user will be deprovisioned from your LangSmith organization according to your IdP's deprovisioning settings.

#### *Can I use custom group names?*

Yes. If your identity provider supports syncing alternate fields to the `displayName` group attribute, you may use an alternate attribute (like `description`) as the `displayName` in LangSmith and retain full customizability of the identity provider group name. Otherwise, groups must follow the specific naming convention described in the [Group Naming Convention](/langsmith/user-management#group-naming-convention) section to properly map to LangSmith roles and workspaces.

You can also [configure a custom separator](/langsmith/user-management#configure-custom-separator) (e.g., `-`, `_`, `&`) instead of the default colon (`:`) to accommodate identity providers with restrictions on group name characters.

#### *Why is my Okta integration not working?*

See Okta's troubleshooting guide here: [https://help.okta.com/en-us/content/topics/users-groups-profiles/usgp-group-push-troubleshoot.htm](https://help.okta.com/en-us/content/topics/users-groups-profiles/usgp-group-push-troubleshoot.htm).

### *Are downgrades supported?*

Downgrades are not officially supported. LangSmith upgrades may include database migrations and other changes that are not backward-compatible. If you need to roll back to a previous version, contact technical support via the [Support Portal](https://support.langchain.com) for guidance.

## Deployment

### Do I need to use LangChain to use LangGraph? what's the difference?

No. LangGraph is an orchestration framework for complex agentic systems and is more low-level and controllable than LangChain agents. LangChain provides a standard interface to interact with models and other components, useful for straight-forward chains and retrieval flows.

### How is LangGraph different from other agent frameworks?

Other agentic frameworks can work for simple, generic tasks but fall short for complex tasks bespoke to a company’s needs. LangGraph provides a more expressive framework to handle companies’ unique tasks without restricting users to a single black-box cognitive architecture.

### Does LangGraph impact the performance of my app?

LangGraph will not add any overhead to your code and is specifically designed with streaming workflows in mind.

### Is LangGraph open source? is it free?

Yes. LangGraph is an MIT-licensed open-source library and is free to use.

### How are LangGraph and LangSmith different?

LangGraph is a stateful, orchestration framework that brings added control to agent workflows. LangSmith is a service for deploying and scaling agentic applications, with an opinionated API for building agent UXs, plus an integrated developer UI.

| Features            | LangGraph (open source)                                   | LangSmith                                                                                              |
| ------------------- | --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Description         | Stateful orchestration framework for agentic applications | Scalable infrastructure for deploying LangGraph applications                                           |
| SDKs                | Python and JavaScript                                     | Python and JavaScript                                                                                  |
| HTTP APIs           | None                                                      | Yes - useful for retrieving & updating state or long-term memory, or creating a configurable assistant |
| Streaming           | Basic                                                     | Dedicated mode for token-by-token messages                                                             |
| Checkpointer        | Community contributed                                     | Supported out-of-the-box                                                                               |
| Persistence Layer   | Self-managed                                              | Managed Postgres with efficient storage                                                                |
| Deployment          | Self-managed                                              | • Cloud <br /> • Free self-hosted <br /> • Enterprise (paid self-hosted)                               |
| Scalability         | Self-managed                                              | Auto-scaling of task queues and servers                                                                |
| Fault-tolerance     | Self-managed                                              | Automated retries                                                                                      |
| Concurrency Control | Simple threading                                          | Supports double-texting                                                                                |
| Scheduling          | None                                                      | Cron scheduling                                                                                        |
| Monitoring          | None                                                      | Integrated with LangSmith for observability                                                            |
| IDE integration     | Studio                                                    | Studio                                                                                                 |

### Is LangSmith open source?

No. LangSmith is proprietary software.

There is a free, self-hosted version of LangSmith with access to basic features. The Cloud deployment option and the Self-Hosted deployment options are paid services. [Contact our sales team](https://www.langchain.com/contact-sales) to learn more.

For more information, see our [LangSmith pricing page](https://www.langchain.com/pricing).

### Does LangGraph work with LLMs that don't support tool calling?

Yes! You can use LangGraph with any LLMs. The main reason we use LLMs that support tool calling is that this is often the most convenient way to have the LLM make its decision about what to do. If your LLM does not support tool calling, you can still use it - you just need to write a bit of logic to convert the raw LLM string response to a decision about what to do.

### Does LangGraph work with OSS LLMs?

Yes! LangGraph is totally ambivalent to what LLMs are used under the hood. The main reason we use closed LLMs in most of the tutorials is that they seamlessly support tool calling, while OSS LLMs often don't. But tool calling is not necessary (see [Does LangGraph work with LLMs that don't support tool calling?](#does-langgraph-work-with-llms-that-dont-support-tool-calling)) so you can totally use LangGraph with OSS LLMs.

### Can I use Studio without logging in to LangSmith?

Yes! You can use the [development version of Agent Server](/langsmith/local-dev-testing) to run the backend locally.
This will connect to the Studio frontend hosted as part of LangSmith.
If you set an environment variable of `LANGSMITH_TRACING=false`, then no traces will be sent to LangSmith.

### What is a Deployment Run?

An Deployment Run is one end-to-end invocation of a LangGraph agent deployed via LangSmith Deployment. Nodes and subgraphs are not charged separately. Calls to other LangGraph agents (through RemoteGraph or the LangGraph SDK or the API directly) are charged separately, to the deployment that hosts the agent being called. An interrupt for human-in-the-loop creates a separate Deployment Run when resuming.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/faq.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Feedback data format
Source: https://docs.langchain.com/langsmith/feedback-data-format

<Check>
  Before diving into this content, it might be helpful to read the following:

  * [Conceptual guide on tracing and feedback](/langsmith/observability-concepts)
</Check>

**Feedback** is LangSmith's way of storing the criteria and scores from evaluation on a particular trace or intermediate run (span). Feedback can be produced from a variety of ways, such as:

1. [Sent up along with a trace](/langsmith/attach-user-feedback) from the LLM application
2. Generated by a user in the app [inline](/langsmith/annotate-traces-inline) or in an [annotation queue](/langsmith/annotation-queues)
3. Generated by an automatic evaluator during [offline evaluation](/langsmith/evaluate-llm-application)
4. Generated by an [online evaluator](/langsmith/online-evaluations-llm-as-judge)

Feedback is stored in a simple format with the following fields:

| Field Name                 | Type     | Description                                                                                            |
| -------------------------- | -------- | ------------------------------------------------------------------------------------------------------ |
| `id`                       | UUID     | Unique identifier for the record itself                                                                |
| `created_at`               | datetime | Timestamp when the record was created                                                                  |
| `modified_at`              | datetime | Timestamp when the record was last modified                                                            |
| `session_id`               | UUID     | Unique identifier for the experiment or tracing project the run was a part of                          |
| `run_id`                   | UUID     | Unique identifier for a specific run within a session                                                  |
| `key`                      | string   | A key describing the criteria of the feedback, e.g. `'correctness'`                                    |
| `score`                    | number   | Numerical score associated with the feedback key                                                       |
| `value`                    | string   | Reserved for storing a value associated with the score. Useful for categorical feedback.               |
| `comment`                  | string   | Any comment or annotation associated with the record. This can be a justification for the score given. |
| `correction`               | object   | Reserved for storing correction details, if any                                                        |
| `feedback_source`          | object   | Object containing information about the feedback source                                                |
| `feedback_source.type`     | string   | The type of source where the feedback originated, e.g. `'api'`, `'app'`, `'evaluator'`                 |
| `feedback_source.metadata` | object   | Reserved for additional metadata, currently                                                            |
| `feedback_source.user_id`  | UUID     | Unique identifier for the user providing feedback                                                      |

Here is an example JSON representation of a feedback record in the above format:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "created_at": "2024-05-05T23:23:11.077838",
  "modified_at": "2024-05-05T23:23:11.232962",
  "session_id": "c919298b-0af2-4517-97a2-0f98ed4a48f8",
  "run_id": "e26174e5-2190-4566-b970-7c3d9a621baa",
  "key": "correctness",
  "score": 1.0,
  "value": null,
  "comment": "I gave this score because the answer was correct.",
  "correction": null,
  "id": "62104630-c7f5-41dc-8ee2-0acee5c14224",
  "feedback_source": {
    "type": "app",
    "metadata": null,
    "user_id": "ad52b092-1346-42f4-a934-6e5521562fab"
  }
}
```

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/feedback-data-format.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# How to fetch performance metrics for an experiment
Source: https://docs.langchain.com/langsmith/fetch-perf-metrics-experiment

<Check>
  Tracing projects and experiments use the same underlying data structure in our backend, which is called a "session."

  You might see these terms interchangeably in our documentation, but they all refer to the same underlying data structure.

  We are working on unifying the terminology across our documentation and APIs.
</Check>

When you run an experiment using `evaluate` with the Python or TypeScript SDK, you can fetch the performance metrics for the experiment using the `read_project`/`readProject` methods.

The payload for experiment details includes the following values:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "start_time": "2024-06-06T01:02:51.299960",
  "end_time": "2024-06-06T01:03:04.557530+00:00",
  "extra": {
    "metadata": {
      "git": {
        "tags": null,
        "dirty": true,
        "branch": "ankush/agent-eval",
        "commit": "...",
        "repo_name": "...",
        "remote_url": "...",
        "author_name": "Ankush Gola",
        "commit_time": "...",
        "author_email": "..."
      },
      "revision_id": null,
      "dataset_splits": ["base"],
      "dataset_version": "2024-06-05T04:57:01.535578+00:00",
      "num_repetitions": 3
    }
  },
  "name": "SQL Database Agent-ae9ad229",
  "description": null,
  "default_dataset_id": null,
  "reference_dataset_id": "...",
  "id": "...",
  "run_count": 9,
  "latency_p50": 7.896,
  "latency_p99": 13.09332,
  "first_token_p50": null,
  "first_token_p99": null,
  "total_tokens": 35573,
  "prompt_tokens": 32711,
  "completion_tokens": 2862,
  "total_cost": 0.206485,
  "prompt_cost": 0.163555,
  "completion_cost": 0.04293,
  "tenant_id": "...",
  "last_run_start_time": "2024-06-06T01:02:51.366397",
  "last_run_start_time_live": null,
  "feedback_stats": {
    "cot contextual accuracy": {
      "n": 9,
      "avg": 0.6666666666666666,
      "values": {
        "CORRECT": 6,
        "INCORRECT": 3
      }
    }
  },
  "session_feedback_stats": {},
  "run_facets": [],
  "error_rate": 0,
  "streaming_rate": 0,
  "test_run_number": 11
}
```

From here, you can extract performance metrics such as:

* `latency_p50`: The 50th percentile latency in seconds.
* `latency_p99`: The 99th percentile latency in seconds.
* `total_tokens`: The total number of tokens used.
* `prompt_tokens`: The number of prompt tokens used.
* `completion_tokens`: The number of completion tokens used.
* `total_cost`: The total cost of the experiment.
* `prompt_cost`: The cost of the prompt tokens.
* `completion_cost`: The cost of the completion tokens.
* `feedback_stats`: The feedback statistics for the experiment.
* `error_rate`: The error rate for the experiment.
* `first_token_p50`: The 50th percentile latency for the time to generate the first token (if using streaming).
* `first_token_p99`: The 99th percentile latency for the time to generate the first token (if using streaming).

Here is an example of how you can fetch the performance metrics for an experiment using the Python and TypeScript SDKs.

First, as a prerequisite, we will create a trivial dataset. Here, we only demonstrate this in Python, but you can do the same in TypeScript. Please view the [how-to guide](/langsmith/evaluate-llm-application) on evaluation for more details.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langsmith import Client

client = Client()

# Create a dataset
dataset_name = "HelloDataset"
dataset = client.create_dataset(dataset_name=dataset_name)

examples = [
    {
        "inputs": {"input": "Harrison"},
        "outputs": {"expected": "Hello Harrison"},
    },
    {
        "inputs": {"input": "Ankush"},
        "outputs": {"expected": "Hello Ankush"},
    },
]

client.create_examples(dataset_id=dataset.id, examples=examples)
```

Next, we will create an experiment, retrieve the experiment name from the result of `evaluate`, then fetch the performance metrics for the experiment.

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langsmith.schemas import Example, Run
  dataset_name = "HelloDataset"

  def foo_label(root_run: Run, example: Example) -> dict:
      return {"score": 1, "key": "foo"}

  from langsmith import evaluate

  results = evaluate(
      lambda inputs: "Hello " + inputs["input"],
      data=dataset_name,
      evaluators=[foo_label],
      experiment_prefix="Hello",
  )

  resp = client.read_project(project_name=results.experiment_name, include_stats=True)
  print(resp.model_dump_json(indent=2))
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { Client } from "langsmith";
  import { evaluate } from "langsmith/evaluation";
  import type { EvaluationResult } from "langsmith/evaluation";
  import type { Run, Example } from "langsmith/schemas";

  // Row-level evaluator
  function fooLabel(rootRun: Run, example: Example): EvaluationResult {
      return {score: 1, key: "foo"};
  }

  const client = new Client();

  const results = await evaluate(
      (inputs) => {
          return { output: "Hello " + inputs.input };
      },
      {
          data: "HelloDataset",
          experimentPrefix: "Hello",
          evaluators: [fooLabel],
      }
  );

  const resp = await client.readProject({
      projectName: results.experimentName,
      includeStats: true
  })
  console.log(JSON.stringify(resp, null, 2))
  ```
</CodeGroup>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/fetch-perf-metrics-experiment.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# How to filter experiments in the UI
Source: https://docs.langchain.com/langsmith/filter-experiments-ui

LangSmith lets you filter your previous experiments by feedback scores and metadata to make it easy to find only the experiments you care about.

## Background: add metadata to your experiments

When you run an experiment in the SDK, you can attach metadata to make it easier to filter in UI. This is helpful if you know what axes you want to drill down into when running experiments.

In our example, we are going to attach metadata to our experiment around the model used, the model provider, and a known ID of the prompt:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
models = {
    "openai-gpt-5.5": ChatOpenAI(model="gpt-5.5", temperature=0),
    "openai-gpt-5.4-mini": ChatOpenAI(model="gpt-5.4-mini", temperature=0),
    "anthropic-claude-3-sonnet-20240229": ChatAnthropic(temperature=0, model_name="claude-3-sonnet-20240229")
}

prompts = {
    "singleminded": "always answer questions with the word banana.",
    "fruitminded": "always discuss fruit in your answers.",
    "basic": "you are a chatbot."
}

def answer_evaluator(run, example) -> dict:
    llm = ChatOpenAI(model="gpt-5.5", temperature=0)
    answer_grader = hub.pull("langchain-ai/rag-answer-vs-reference") | llm
    score = answer_grader.invoke(
        {
            "question": example.inputs["question"],
            "correct_answer": example.outputs["answer"],
            "student_answer": run.outputs,
        }
    )
    return {"key": "correctness", "score": score["Score"]}

dataset_name = "Filterable Dataset"

for model_type, model in models.items():
    for prompt_type, prompt in prompts.items():
        def predict(example):
            return model.invoke(
                [("system", prompt), ("user", example["question"])]
            )

        model_provider = model_type.split("-")[0]
        model_name = model_type[len(model_provider) + 1:]

        evaluate(
            predict,
            data=dataset_name,
            evaluators=[answer_evaluator],
            # ADD IN METADATA HERE!!
            metadata={
                "model_provider": model_provider,
                "model_name": model_name,
                "prompt_id": prompt_type
            }
        )
```

## Filter experiments in the UI

In the UI, we see all experiments that have been run by default.

<img alt="Filter all experiments" />

If we, say, have a preference for openai models, we can easily filter down and see scores within just openai models first:

<img alt="Filter openai" />

We can stack filters, allowing us to filter out low scores on correctness to make sure we only compare relevant experiments:

<img alt="Filter feedback" />

Finally, we can clear and reset filters. For example, if we see there is clear there's a winner with the `singleminded` prompt, we can change filtering settings to see if any other model providers' models work as well with it:

<img alt="Filter singleminded" />

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/filter-experiments-ui.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Filter traces
Source: https://docs.langchain.com/langsmith/filter-traces-in-application

Tracing projects can accumulate large amounts of data across [threads](/langsmith/observability-concepts#threads), [traces](/langsmith/observability-concepts#traces), and [runs](/langsmith/observability-concepts#runs). LangSmith's filtering tools let you navigate and analyze that data precisely.

This page covers:

* [Applying filters from the filter bar](#create-and-apply-filters) and **Filter Shortcuts** panel
* [Filtering by attributes, full-text content, and key-value pairs](#specific-filtering-techniques)
* [Saving and copying filter configurations](#save-a-filter)
* [Filtering within the Details view](#filter-runs-in-the-details-view)
* [Advanced filters](#advanced-filters) for filtering on root or child run properties

If you are programmatically exporting data for analysis via the [API](/langsmith/smith-api/run/query-runs) or [SDK](https://docs.smith.langchain.com/reference/python/client/langsmith.client.Client#langsmith.client.Client.list_runs), refer to the [exporting traces guide](/langsmith/export-traces) instead.

## Create and apply filters

### Filter by run attributes

There are two ways to filter data in a tracing project:

1. **Filters**: Located at the top left of the **Tracing** project page. This is where you construct and manage filter criteria.
   * The first dropdown filters for default and [saved views](#save-a-filter).
   * Quick filter by **Threads**, **Traces**, or **Runs**.
   * **Add filter** to [configure a filter based](#specific-filtering-techniques) on an attribute or full-text search.

2. **Filter Shortcuts**: Positioned on the right sidebar of the **Tracing** project page. The filter shortcuts bar provides quick access to filters based on the most frequently occurring attributes in your project's runs.

### Filter operators

The available filter operators depend on the data type of the attribute you are filtering on. Here's an overview of common operators:

* **is**: Exact match on the filter value
* **is not**: Negative match on the filter value
* **contains**: Partial match on the filter value
* **does not contain**: Negative partial match on the filter value
* **is one of**: Match on any of the values in the list
* `>` / `<`: Available for numeric fields

## Specific filtering techniques

### Filter for runs (spans)

To filter for runs (spans), change the default from **Traces** to **Runs**. For example, you would do this if you wanted to filter by **run name** for runs or filter by **run type**.

Run metadata and tags are also useful to filter on. These rely on good tagging across all parts of your pipeline. To learn more, refer to [Add metadata and tags to traces](/langsmith/add-metadata-tags).

As you specify more filters, you can click each filter individually to update the attributes you're searching on.

### Filter based on inputs and outputs

You can filter tracing data based on the content in the inputs and outputs of the thread, trace, or run.

To filter either inputs or outputs, you can use the **<Icon icon="zoom" /> Full-Text Search** filter, which will match keywords in either field. For a more targeted search, you can use the&#x20;**&#x20;Input** or **<Icon icon="arrow-up-left" /> Output** filters, which will only match content based on the respective field.

<Note>
  For performance, LangSmith indexes up to 250 characters of data for full-text search. If your search query exceeds this limit, we recommend using [Input/Output key-value search](/langsmith/filter-traces-in-application#filter-based-on-input-%2F-output-key-value-pairs) instead.
</Note>

You can also specify multiple to match all terms provided, either by:

* Including multiple terms separated by whitespace with the **Full-Text Search**.
* Adding multiple filters with the <Icon icon="plus" /> button after you've added the first filter.

LangSmith splits the text and matches any partial keyword matches in any order. LangSmith excludes common stop words from the search (from the nltk stop word list along with a few other common JSON keywords).

<Note>
  Tokens must be at least 2 characters long to be indexed. Single-character tokens (for example, `a`, `x`) are excluded from search.
</Note>

<img alt="LangSmith filter bar showing full-text search and input/output filters with example search terms for python, tensorflow, embedding, fine, and tune" />

<img alt="LangSmith filter bar showing full-text search and input/output filters with example search terms for python, tensorflow, embedding, fine, and tune" />

Based on the filters in the image, the system will search for `python` and `tensorflow` in either inputs or outputs, and `embedding` in the inputs along with `fine` and `tune` in the outputs.

You can remove filters as needed from the filter path, which will widen the search to the remaining filters.

### Filter based on input / output key-value pairs

In addition to full-text search, you can filter based on specific key-value pairs in the inputs and outputs. This allows for more precise filtering, especially when dealing with structured data.

<Note>
  LangSmith indexes up to 100 unique keys per run to keep your data organized and searchable. Each key also has a character limit of 250 characters per value. If your data exceeds either of these limits, the text won't be indexed. This helps ensure fast, reliable performance.
</Note>

To filter based on key-value pairs, for example, to match the following input:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "input": "What is the capital of France?"
}
```

1. Select **Add filter**.
2. Select **Input** from the first dropdown and leave **Key** as the second dropdown and select **input** as the key.
3. Click **+ Value** and enter the value: `What is the capital of France?` as the value.

You can also match nested keys by using dot notation to select the nested key name. For example, to match nested keys in the output:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "documents": [
    {
      "page_content": "The capital of France is Paris",
      "metadata": {},
      "type": "Document"
    }
  ]
}
```

Select **Output Key**, enter `documents.page_content` as the key and enter `The capital of France is Paris` as the value. This will match the nested key `documents.page_content` with the specified value.

You can add multiple key-value filters to create more complex queries. You can also use the **Filter Shortcuts** on the right side to filter based on common key-value pairs quickly:

<img alt="LangSmith filter shortcuts panel showing quick access to common key-value pair filters" />

<img alt="LangSmith filter shortcuts panel showing quick access to common key-value pair filters" />

### Example: Filtering for tool calls

It's common to want to search for traces that contain specific tool calls. Tool calls are typically indicated in the output of an LLM run. To filter for tool calls, you would use the **Output Key** filter.

While this example will show you how to filter for tool calls, you can apply the same logic to filter for any key-value pair in the output.

In this case, let's assume this is the output you want to filter for:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "generations": [
    [
      {
        "text": "",
        "type": "ChatGeneration",
        "message": {
          "lc": 1,
          "type": "constructor",
          "id": [],
          "kwargs": {
            "type": "ai",
            "id": "run-ca7f7531-f4de-4790-9c3e-960be7f8b109",
            "tool_calls": [
              {
                "name": "Plan",
                "args": {
                  "steps": [
                    "Research LangGraph's node configuration capabilities",
                    "Investigate how to add a Python code execution node",
                    "Find an example or create a sample implementation of a code execution node"
                  ]
                },
                "id": "toolu_01XexPzAVknT3gRmUB5PK5BP",
                "type": "tool_call"
              }
            ]
          }
        }
      }
    ]
  ],
  "llm_output": null,
  "run": null,
  "type": "LLMResult"
}
```

With the example, the KV search will map each nested JSON path as a key-value pair that you can use to search and filter.

LangSmith will break it into the following set of searchable key-value pairs:

| Key                                                | Value                                                                        |
| -------------------------------------------------- | ---------------------------------------------------------------------------- |
| `generations.type`                                 | `ChatGeneration`                                                             |
| `generations.message.type`                         | `constructor`                                                                |
| `generations.message.kwargs.type`                  | `ai`                                                                         |
| `generations.message.kwargs.id`                    | `run-ca7f7531-f4de-4790-9c3e-960be7f8b109`                                   |
| `generations.message.kwargs.tool_calls.name`       | `Plan`                                                                       |
| `generations.message.kwargs.tool_calls.args.steps` | `Research LangGraph's node configuration capabilities`                       |
| `generations.message.kwargs.tool_calls.args.steps` | `Investigate how to add a Python code execution node`                        |
| `generations.message.kwargs.tool_calls.args.steps` | `Find an example or create a sample implementation of a code execution node` |
| `generations.message.kwargs.tool_calls.id`         | `toolu_01XexPzAVknT3gRmUB5PK5BP`                                             |
| `generations.message.kwargs.tool_calls.type`       | `tool_call`                                                                  |
| `type`                                             | `LLMResult`                                                                  |

To search for a specific tool call, you can use the following **Output Key** search while removing the root runs filter:

`generations.message.kwargs.tool_calls.name` = `Plan`

This will match root and non-root runs where the `tool_calls` name is `Plan`.

### Negative filtering on key-value pairs

Different types of negative filtering can be applied to **\{x} Metadata**, **<Icon icon="arrow-down-right" /> Input**, and **<Icon icon="arrow-up-left" /> Output** fields to exclude specific runs from your results.

For example, to find all runs where the metadata key `phone` is not equal to `1234567890`:

1. Set the **Metadata Key** operator to `is` and **Key** field to `phone`.
2. Set the **Value** operator to `is not` and the **Value** field to `1234567890`.

This will match all runs that have a metadata key `phone` with any value except `1234567890`.

To find runs that don't have a specific metadata key: set the **Key** operator to `is not`. For example, setting the `Key` operator to `is not` with `phone` as the key will match all runs that don't have a `phone` field in their metadata.

You can also filter for runs that neither have a specific key nor a specific value. To find runs where the metadata has neither the key `phone` nor any field with the value `1234567890`, set the **Key** operator to `is not` with key `phone`, and the **Value** operator to `is not` with value `1234567890`.

Finally, you can also filter for runs that do not have a specific key but have a specific value. To find runs where there is no `phone` key but there is a value of `1234567890` for some other key, set the **Key** operator to `is not` with key `phone`, and the **Value** operator to `is` with value `1234567890`.

<Tip>
  You can use the `does not contain` operator instead of `is not` to perform a substring match.
</Tip>

## Save a filter

Saving filters allows you to store and reuse frequently used filter configurations. Saved filters are specific to a tracing project.

After you have constructed your filter, click the **Save as** button to save it. This will bring up a dialog to specify the name and a description of the filter.

After saving a filter, it is available in the view dropdown as a quick filter for you to use.

### Update a saved filter

With the filter selected in the dropdown, you can make any changes to filter parameters. Then, click **Save** to update the filter.

### Delete a saved filter

Click the <Icon icon="dots-vertical" /> icon next to the saved filter in the dropdown, and delete the filter using the trash <Icon icon="trash" /> icon.

## Copy a filter

You can copy a constructed filter to share it with colleagues, reuse it later, or query runs programmatically in the [API](/langsmith/smith-api/run/query-runs) or [SDK](https://docs.smith.langchain.com/reference/python/client/langsmith.client.Client#langsmith.client.Client.list_runs).

To copy the filter:

1. Create it in the UI.
2. Click the <Icon icon="copy" /> icon in the filter bar. If you have constructed tree or trace filters, you can also copy those.
3. This will give you a string representing the filter in the LangSmith query language. For example: `and(eq(is_root, true), and(eq(feedback_key, "user_score"), eq(feedback_score, 1)))`.

For more information on the query language syntax, refer to the [Trace query syntax](/langsmith/trace-query-syntax#filter-query-language).

## Filter runs in the Details view

You can also apply filters directly in the [Details view](/langsmith/view-traces#details-view), which is useful for sifting through traces with a large number of runs. The same filters available in the main runs table view can be applied here.

By default, only the runs that match the filters will be shown. To see the matched runs within the broader context of the trace tree, switch the view option from "Filtered Only" to "Show All" or "Most relevant".

<img alt="LangSmith trace view showing filter options with 'Filtered Only', 'Show All', and 'Most relevant' view modes" />

<img alt="LangSmith trace view showing filter options with 'Filtered Only', 'Show All', and 'Most relevant' view modes" />

## Manually specify a raw query in LangSmith query language

If you have [copied a previously constructed filter](#copy-a-filter), you may want to manually apply this raw query in a future session.

In order to do this, you can click on **Switch to raw query** on the bottom of the filters popover in the Details view. From there you can paste a raw query into the text box.

<Note>
  This will add that query to the existing queries, not overwrite it.
</Note>

## Advanced filters

### Filter for runs (spans) on properties of the root

A common concept is to filter for runs which are part of a trace whose root run has some attribute. An example is filtering for runs of a particular type whose root run has positive (or negative) feedback associated with it. To do this:

1. Click **Runs** in the Threads/Traces/Runs toggle.
2. Add another filter rule. You can then click the **Advanced** filters link at the bottom of the filter dropdown.
3. A modal will open where you can add **Trace** filters. These filters will apply to the traces of all the parent runs of the individual runs you've already filtered for.

### Filter for runs (spans) whose child runs have some attribute

You may want to search for runs who have specific types of sub runs. An example of this could be searching for all traces that had a sub run with name `Foo`. This is useful when `Foo` is not always called, but you want to analyze the cases where it is.

1. Click **Runs** in the Threads/Traces/Runs toggle.
2. Add another filter rule. You can then click the **Advanced** filters link at the bottom of the filter dropdown.
3. A modal will open where you can add **Tree** filters. This will make the rule you specify apply to all child runs of the individual runs you've already filtered for.

### Example: Filtering on all runs whose tree contains the tool call filter

Extending the [tool call filtering example](#example-filtering-for-tool-calls), if you would like to filter for all runs *whose tree contains* the tool filter call, you can use the tree filter in the **Advanced** filters setting.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/filter-traces-in-application.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
