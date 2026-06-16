# How to compare experiment results
Source: https://docs.langchain.com/langsmith/compare-experiment-results

When you are iterating on your LLM application (such as changing the model or the prompt), you may want to compare the results of different [*experiments*](/langsmith/evaluation-concepts#experiment).

LangSmith supports a comparison view that lets you identify key differences, regressions, and improvements between different experiments.

## Open the comparison view

1. To access the experiment comparison view, navigate to the **Datasets & Experiments** page.
2. Select a dataset, which will open the **Experiments** tab.
3. Select two or more experiments and then click **Compare**.

<div>
  <img alt="The Experiments view in the UI with 3 experiments selected and the Compare button highlighted, in light mode." />

  <img alt="The Experiments view in the UI with 3 experiments selected and the Compare button highlighted, in dark mode." />
</div>

## Adjust the table display

You can toggle between different display options on the top right of the comparison view.

<img alt="Table display options, in light mode." />

<img alt="Table display options, in dark mode." />

### Filters

Click the <Icon icon="filter-2" /> icon to apply filters to the comparison view to narrow down specific examples. Common examples for filters include:

* Examples that contain specific `input` / `output`.
* Runs with status `success` or `error`.
* Runs that take more than x seconds in `latency`.
* Specific `metadata`, `tag`, or `feedback`.

In addition to applying filters on the overall experiment view, you can apply filters on individual columns as well. Select the <Icon icon="dots-vertical" /> icon at the top of any column to view the available filters for that column's data.

### Columns

Click the <Icon icon="columns-3" /> icon to show or hide individual feedback keys or metrics in the comparison view.

### Table views

Select one of three table view icons at the top right of the comparison view:

* **Compact**: Shows a preview of the experiment results for each example.
* **Full**: Shows the full text of the input, output, and reference output for each run. If the output is too long to display in the table, you can click **Expand** to view the full content.
* **Diff**: Shows the text difference between experiment outputs for each run. This is only supported for 2 experiments at a time. See [View side-by-side diffs](#view-side-by-side-diffs) for more details.

### Display types

There are three built-in experiment views that cover several display types: **Default**, **YAML**, **JSON**.

## View regressions and improvements

In the comparison view, red highlights runs that *regressed* on any feedback key against your source experiment, while green highlights runs that *improved*. At the top of each feedback column, you can see how many runs did better or worse than your source experiment.

Click the regression or improvement buttons at the top of each column to show only runs that regressed or improved in that experiment.

<img alt="The comparison view comparing 4 experiments with the regressions and improvements in red and green respectively." />

<img alt="The comparison view comparing 4 experiments with the regressions and improvements in red and green respectively." />

## View side-by-side diffs

When comparing two experiments, for JSON and YAML display styles, you can toggle on the experiment diff mode to compare experiment outputs. The diff mode highlights modifications between outputs, and can be particularly useful for structured output comparisons.

<div>
  <img alt="The comparison diff mode in light." />

  <img alt="The comparison diff mode in dark." />
</div>

## Update source experiment and metric

To track regressions across experiments, you can:

1. At the top of the comparison view, hover over an experiment icon and select **Set as source experiment** from the dropdown. You can also add or remove experiments from this dropdown. By default, the first selected experiment is set as the source.

   <img alt="Setting a source experiment from the experiment icons at the top of the Comparison view." />

   <img alt="Setting a source experiment from the experiment icons at the top of the Comparison view." />

2. Within the **Feedback** columns, you can configure whether a higher score is better for each feedback key. This preference will be stored. By default, a higher score is assumed to be better.

   <img alt="Dropdown for feedback metric column, configuring whether a higher score is better, in light mode." />

   <img alt="Dropdown for feedback metric column, configuring whether a higher score is better, in dark mode." />

## Expand details panel

Click on any row to open a details panel for that example for the compared experiments.

Use the toggle in the top right of the panel to switch between two modes:

* **Details**: Shows feedback keys and scores, along with a metrics summary for the example, as well as the input, output, and reference output, and attributes for each experiment.

  <img alt="An example in the expanded Comparing Experiments view, in light mode." />

  <img alt="An example in the expanded Comparing Experiments view, in dark mode." />

* **Traces**: Shows traces for each experiment side by side.

  <img alt="An example in the expanded Comparing Experiments view, in light mode." />

  <img alt="An example in the expanded Comparing Experiments view, in dark mode." />

When comparing more than two experiments, the panel displays two experiments at a time. Use the header to switch which experiment you are comparing against.

## Use experiment metadata as chart labels

You can configure the x-axis labels for the charts based on [experiment metadata](/langsmith/filter-experiments-ui#background-add-metadata-to-your-experiments).

Select a metadata key from the **Charts** dropdown at the top-right of the comparison view to change the x-axis labels.

<img alt="x-axis dropdown highlighted with a list of the metadata attached to the experiment, in light mode." />

<img alt="x-axis dropdown highlighted with a list of the metadata attached to the experiment, in dark mode." />

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/compare-experiment-results.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# LangSmith Deployment components
Source: https://docs.langchain.com/langsmith/components

Overview of Agent Server, LangGraph CLI, Studio, SDKs, RemoteGraph, control plane, and data plane components.

When running self-hosted [LangSmith Deployment](/langsmith/deploy-self-hosted-full-platform), your installation includes several key components. Together these tools and services provide a complete solution for building, deploying, and managing graphs (including agentic applications) in your own infrastructure:

```mermaid theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
flowchart
    subgraph LangSmith Deployment
        A[LangGraph CLI] -->|creates| B(Agent Server deployment)
        B <--> D[Studio]
        B <--> E[SDKs]
        B <--> F[RemoteGraph]
    end

    classDef process fill:#E5F4FF,stroke:#006DDD,stroke-width:2px,color:#030710

    class A,B,D,E,F process
```

* [Agent Server](/langsmith/agent-server): Defines an opinionated API and runtime for deploying graphs and agents. Handles execution, state management, and persistence so you can focus on building logic rather than server infrastructure.
* [LangGraph CLI](/langsmith/cli): A command-line interface to build, package, and interact with graphs locally and prepare them for deployment.
* [Studio](/langsmith/studio): A specialized IDE for visualization, interaction, and debugging. Connects to a local Agent Server for developing and testing your graph.
* [Python/JS SDK](/langsmith/reference): The Python/JS SDK provides a programmatic way to interact with deployed graphs and agents from your applications.
* [RemoteGraph](/langsmith/use-remote-graph): Allows you to interact with a deployed graph as though it were running locally.
* [Control Plane](/langsmith/control-plane): The UI and APIs for creating, updating, and managing Agent Server deployments.
* [Data plane](/langsmith/data-plane): The runtime layer that executes your graphs, including Agent Servers, their backing services (PostgreSQL, Redis, etc.), and the listener that reconciles state from the control plane.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/components.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# How to create a composite evaluator
Source: https://docs.langchain.com/langsmith/composite-evaluators-sdk

*Composite evaluators* are a way to combine multiple evaluator scores into a single [score](/langsmith/evaluation-concepts#evaluator-outputs). This is useful when you want to evaluate multiple aspects of your application and combine the results into a single result.

This guide describes setting up an evaluation that uses multiple evaluators and combines their scores with a custom aggregation function using the [LangSmith SDK](https://reference.langchain.com/python/langsmith/observability/sdk).

<Note> Requires langsmith>=0.4.29 </Note>

<Tip>
  To create composite evaluators in the LangSmith UI, refer to [How to create a composite evaluator (UI)](/langsmith/composite-evaluators-ui).
</Tip>

## 1. Configure evaluators on a dataset

Start by configuring your evaluators. In this example, the application generates a tweet from a blog introduction and uses three evaluators—summary, tone, and formatting—to assess the output.

If you already have your own dataset with evaluators configured, you can skip this step.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import os
from dotenv import load_dotenv
from openai import OpenAI
from langsmith import Client
from pydantic import BaseModel
import json

# Load environment variables from .env file
load_dotenv()

# Access environment variables
openai_api_key = os.getenv('OPENAI_API_KEY')
langsmith_api_key = os.getenv('LANGSMITH_API_KEY')
langsmith_project = os.getenv('LANGSMITH_PROJECT', 'default')

# Create a dataset. Only need to do this once.
client = Client()
oai_client = OpenAI()

examples = [
  {
    "inputs": {"blog_intro": "Today we're excited to announce the general availability of LangSmith—our purpose-built infrastructure and management layer for deploying and scaling long-running, stateful agents. Since our beta last June, nearly 400 companies have used LangSmith to deploy their agents into production. Agent deployment is the next hard hurdle for shipping reliable agents, and LangSmith dramatically lowers this barrier with: 1-click deployment to go live in minutes, 30 API endpoints for designing custom user experiences that fit any interaction pattern, Horizontal scaling to handle bursty, long-running traffic, A persistence layer to support memory, conversational history, and async collaboration with human-in-the-loop or multi-agent workflows, Native Studio, the agent IDE, for easy debugging, visibility, and iteration "},
  },
  {
    "inputs": {"blog_intro": "Klarna has reshaped global commerce with its consumer-centric, AI-powered payment and shopping solutions. With over 85 million active users and 2.5 million daily transactions on its platform, Klarna is a fintech leader that simplifies shopping while empowering consumers with smarter, more flexible financial solutions. Klarna's flagship AI Assistant is revolutionizing the shopping and payments experience. Built on LangGraph and powered by LangSmith, the AI Assistant handles tasks ranging from customer payments, to refunds, to other payment escalations. With 2.5 million conversations to date, the AI Assistant is more than just a chatbot; it's a transformative agent that performs the work equivalent of 700 full-time staff, delivering results quickly and improving company efficiency."},
  },
]

dataset = client.create_dataset(dataset_name="Blog Intros")

client.create_examples(
  dataset_id=dataset.id,
  examples=examples,
)

# Define a target function. In this case, we're using a simple function that generates a tweet from a blog intro.
def generate_tweet(inputs: dict) -> dict:
    instructions = (
      "Given the blog introduction, please generate a catchy yet professional tweet that can be used to promote the blog post on social media. Summarize the key point of the blog post in the tweet. Use emojis in a tasteful manner."
    )
    messages = [
        {"role": "system", "content": instructions},
        {"role": "user", "content": inputs["blog_intro"]},
    ]
    result = oai_client.responses.create(
        input=messages, model="gpt-5-nano"
    )
    return {"tweet": result.output_text}

# Define evaluators. In this case, we're using three evaluators: summary, formatting, and tone.
def summary(inputs: dict, outputs: dict) -> bool:
    """Judge whether the tweet is a good summary of the blog intro."""
    instructions = "Given the following text and summary, determine if the summary is a good summary of the text."

    class Response(BaseModel):
        summary: bool

    msg = f"Question: {inputs['blog_intro']}\nAnswer: {outputs['tweet']}"
    response = oai_client.responses.parse(
        model="gpt-5-nano",
        input=[{"role": "system", "content": instructions,}, {"role": "user", "content": msg}],
        text_format=Response
    )

    parsed_response = json.loads(response.output_text)
    return parsed_response["summary"]

def formatting(inputs: dict, outputs: dict) -> bool:
    """Judge whether the tweet is formatted for easy human readability."""
    instructions = "Given the following text, determine if it is formatted well so that a human can easily read it. Pay particular attention to spacing and punctuation."

    class Response(BaseModel):
        formatting: bool

    msg = f"{outputs['tweet']}"
    response = oai_client.responses.parse(
        model="gpt-5-nano",
        input=[{"role": "system", "content": instructions,}, {"role": "user", "content": msg}],
        text_format=Response
    )

    parsed_response = json.loads(response.output_text)
    return parsed_response["formatting"]

def tone(inputs: dict, outputs: dict) -> bool:
    """Judge whether the tweet's tone is informative, friendly, and engaging."""
    instructions = "Given the following text, determine if the tweet is informative, yet friendly and engaging."

    class Response(BaseModel):
        tone: bool

    msg = f"{outputs['tweet']}"
    response = oai_client.responses.parse(
        model="gpt-5-nano",
        input=[{"role": "system", "content": instructions,}, {"role": "user", "content": msg}],
        text_format=Response
    )
    parsed_response = json.loads(response.output_text)
    return parsed_response["tone"]

# Calling evaluate() with the dataset, target function, and evaluators.
results = client.evaluate(
    generate_tweet,
    data=dataset.name,
    evaluators=[summary, tone, formatting],
    experiment_prefix="gpt-5-nano",
)

# Get the experiment name to be used in client.get_experiment_results() in the next section
experiment_name = results.experiment_name
```

## 2. Create composite feedback

Create composite feedback that aggregates the individual evaluator scores using your custom function. This example uses a weighted average of the individual evaluator scores.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from typing import Dict
import math
from langsmith import Client
from dotenv import load_dotenv

load_dotenv()

# TODO: Replace with your experiment name. Can be found in UI or from the above client.evaluate() result
YOUR_EXPERIMENT_NAME = "placeholder_experiment_name"

# Set weights for the individual evaluator scores
DEFAULT_WEIGHTS: Dict[str, float] = {
    "summary": 0.7,
    "tone": 0.2,
    "formatting": 0.1,
}
WEIGHTED_FEEDBACK_NAME = "weighted_summary"

# Pull experiment results
client = Client()
results = client.get_experiment_results(
    name=YOUR_EXPERIMENT_NAME,
)

# Calculate weighted score for each run
def calculate_weighted_score(feedback_stats: dict) -> float:
    if not feedback_stats:
        return float("nan")

    # Check if all required metrics are present and have data
    required_metrics = set(DEFAULT_WEIGHTS.keys())
    available_metrics = set(feedback_stats.keys())

    if not required_metrics.issubset(available_metrics):
        return float("nan")

    # Calculate weighted score
    total_score = 0.0
    for metric, weight in DEFAULT_WEIGHTS.items():
        metric_data = feedback_stats[metric]
        if metric_data.get("n", 0) > 0 and "avg" in metric_data:
            total_score += metric_data["avg"] * weight
        else:
            return float("nan")

    return total_score

# Process each run and write feedback

# Note that experiment results need to finish processing before this should be called.
for example_with_runs in results["examples_with_runs"]:
    for run in example_with_runs.runs:
        if run.feedback_stats:
            score = calculate_weighted_score(run.feedback_stats)
            if not math.isnan(score):
                client.create_feedback(
                    run_id=run.id,
                    key=WEIGHTED_FEEDBACK_NAME,
                    score=float(score)
                )
```

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/composite-evaluators-sdk.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# How to create a composite evaluator
Source: https://docs.langchain.com/langsmith/composite-evaluators-ui

*Composite evaluators* are a way to combine multiple evaluator scores into a single [score](/langsmith/evaluation-concepts#evaluator-outputs). This is useful when you want to evaluate multiple aspects of your application and combine the results into a single result.

This guide shows you how to define a [composite evaluator](/langsmith/evaluation-concepts#llm-as-judge) using the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-composite-evaluators-ui).

<Note>
  To create composite evaluators programmatically using the SDK, refer to [How to create a composite evaluator (SDK)](/langsmith/composite-evaluators-sdk).
</Note>

## Create a composite evaluator

You can create composite evaluators on a [tracing project](/langsmith/observability-concepts#projects) (for [online evaluations](/langsmith/evaluation-concepts#online-evaluations)) or a [dataset](/langsmith/evaluation-concepts#datasets) (for [offline evaluations](/langsmith/evaluation-concepts#offline-evaluations)). With composite evaluators in the UI, you can compute a weighted average or weighted sum of multiple evaluator scores, with configurable weights.

<div>
  <img alt="LangSmith UI showing an LLM call trace called ChatOpenAI with a system and human input followed by an AI Output." />

  <img alt="LangSmith UI showing an LLM call trace called ChatOpenAI with a system and human input followed by an AI Output." />
</div>

### 1. Navigate to the tracing project or dataset

To start configuring a composite evaluator, navigate to the **Tracing Projects** or **Dataset & Experiments** tab and select a project or dataset.

* From within a tracing project: **+ New** > **Evaluator** > **Composite score**
* From within a dataset: **+ Evaluator** > **Composite score**

### 2. Configure the composite evaluator

1. Name your evaluator.
2. Select an aggregation method, either **Average** or **Sum**.
   * **Average**: ∑(weight\*score) / ∑(weight).
   * **Sum**: ∑(weight\*score).
3. Add the feedback keys you want to include in the composite score.
4. Add the weights for the feedback keys. By default, the weights are equal for each feedback key. Adjust the weights to increase or decrease the importance of specific feedback keys in the final score.
5. Click **Create** to save the evaluator.

<Tip> If you need to adjust the weights for the composite scores, they can be updated after the evaluator is created. The resulting scores will be updated for all runs that have the evaluator configured. </Tip>

### 3. View composite evaluator results

Composite scores are attached to a run as **feedback**, similarly to feedback from a single evaluator. How you can view them depends on where the evaluation was run:

**On a tracing project**:

* Composite scores appear as feedback on runs.
* [Filter for runs](/langsmith/filter-traces-in-application) with a composite score, or where the composite score meets a certain threshold.
* [Create a chart](/langsmith/dashboards#custom-dashboards) to visualize trends in the composite score over time.

**On a dataset**:

* View the composite scores in the experiments tab. You can also filter and sort experiments based on the average composite score of their runs.
* Click into an experiment to view the composite score for each run.

<Note> If any of the constituent evaluators are not configured on the run, the composite score will not be calculated for that run. </Note>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/composite-evaluators-ui.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Conditional tracing
Source: https://docs.langchain.com/langsmith/conditional-tracing

When you have the environment variable `LANGSMITH_TRACING=true` set globally, traces are automatically sent to LangSmith. This guide shows you how to disable or customize tracing selectively for specific requests.

Use conditional tracing when you need to:

* **Comply with data retention policies**: Some clients may require zero data retention for compliance or privacy reasons.
* **Handle sensitive operations**: Disable tracing for operations involving PII, credentials, or confidential data.
* **Implement per-tenant configurations**: Route traces to different projects or apply different settings based on the customer.
* **Control costs**: Disable tracing for low-value requests while maintaining visibility into critical operations.
* **Support feature flags**: Enable tracing only when specific features or experimental code paths are active.

<Tip>
  To reduce trace volume by logging only a percentage of all runs, refer to [Set a sampling rate for traces](/langsmith/sample-traces).
</Tip>

The [`tracing_context`](https://reference.langchain.com/python/langsmith/run_helpers/tracing_context) context manager (Python) and [`tracingEnabled`](https://reference.langchain.com/javascript/classes/langsmith.run_trees.RunTree.html#tracingenabled) option (TypeScript) allow you to override global tracing settings at runtime, without restructuring your code or changing environment variables.

<Note>
  The following sections provide language-specific examples that you can adapt to your application logic and business requirements.
</Note>

<Tabs>
  <Tab title="Python" icon="brand-python">
    ## How tracing context works

    When you use the [`tracing_context`](https://reference.langchain.com/python/langsmith/run_helpers/tracing_context) context manager, it overrides the global tracing configuration for code executed within its scope. This means you can keep automatic tracing enabled globally while selectively controlling tracing behavior for specific function calls.

    There are three priority levels of control:

    1. **`tracing_context(enabled=...)`**: highest priority (context manager for scoped tracing control).
    2. **`ls.configure(enabled=...)`**: global configuration (sets global tracing behavior).
    3. **Environment variables**: lowest priority (`LANGSMITH_TRACING`).

    ## Disable tracing for specific invocations

    To disable tracing for a specific operation, wrap it in a `tracing_context` with `enabled=False`:

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import langsmith as ls
    from langsmith import traceable

    # LANGSMITH_TRACING=true is set globally

    @traceable
    def my_function(input_text: str):
        return process(input_text)

    # Default invocation - is traced
    result = my_function("regular data")

    # Disable tracing for sensitive data
    with ls.tracing_context(enabled=False):
        result = my_function("sensitive data")  # not traced
    ```

    This pattern is useful for one-off cases where you know specific data should not be logged.

    ## Enable conditional tracing based on business logic

    You can dynamically enable or disable tracing based on runtime conditions, such as client settings or request properties.

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import langsmith as ls
    from langsmith import traceable

    @traceable
    def my_function(input_text: str):
        return process(input_text)

    def client_requires_zero_retention(client_id: str) -> bool:
        """
        Check if a client has a zero-retention policy.

        In production, this would query a database, configuration service,
        or feature flag system. Consider caching results for performance.
        """
        # Example: Query from database or config
        zero_retention_clients = get_zero_retention_clients()  # Your implementation
        return client_id in zero_retention_clients

    def handle_request(client_id: str, user_input: str):
        """
        Process a request with conditional tracing based on client requirements.
        """
        should_disable = client_requires_zero_retention(client_id)

        with ls.tracing_context(enabled=not should_disable):
            return my_function(user_input)

    # Example usage
    handle_request("client-a", "some input")  # Traced or not based on client settings
    ```

    ## Customize tracing configuration per request

    You can also customize tracing settings dynamically, such as routing traces to different projects or adding request-specific metadata.

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import langsmith as ls
    from langsmith import traceable

    @traceable
    def my_function(input_text: str):
        return process(input_text)

    def handle_request(client_id: str, user_input: str, region: str):
        """
        Route traces to client-specific projects with custom metadata.
        """
        client_tier = get_client_tier(client_id)  # e.g., "enterprise", "standard"

        with ls.tracing_context(
            enabled=True,
            project_name=f"client-{client_id}",
            tags=["production", f"tier-{client_tier}", f"region-{region}"],
            metadata={
                "client_id": client_id,
                "region": region,
                "tier": client_tier
            }
        ):
            return my_function(user_input)

    # Traces go to "client-abc" project with custom tags and metadata
    handle_request("abc", "some input", "us-west")
    ```

    This pattern is useful for:

    * **Multi-tenant applications**: Isolate traces by customer in separate projects
    * **Regional deployments**: Track performance and behavior by geographic region
    * **Feature branches**: Route experimental feature traces to dedicated projects
    * **User segmentation**: Analyze behavior by user tier, cohort, or A/B test group

    ## Work with automatic tracing

    The [`tracing_context`](https://reference.langchain.com/python/langsmith/run_helpers/tracing_context) context manager works with automatic tracing. You can keep `LANGSMITH_TRACING=true` set globally and use `tracing_context` to override settings for specific requests:

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import os
    import langsmith as ls

    # Global environment variable set
    os.environ["LANGSMITH_TRACING"] = "true"

    @ls.traceable
    def process_data(data: str):
        return data.upper()

    # Automatically traced (respects LANGSMITH_TRACING)
    process_data("hello")

    # Override global setting - disable for this call
    with ls.tracing_context(enabled=False):
        process_data("sensitive")  # not traced

    # Override global setting - enable with custom config
    with ls.tracing_context(
        enabled=True,
        project_name="special-project"
    ):
        process_data("important")  # Traced to "special-project"
    ```

    ## Nest tracing contexts

    When you nest `tracing_context` blocks, the innermost context takes precedence.

    ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import langsmith as ls

    @ls.traceable
    def inner_function(data: str):
        return data

    @ls.traceable
    def outer_function(data: str):
        # This call respects the inner context
        return inner_function(data)

    # Outer context disables tracing
    with ls.tracing_context(enabled=False):
        # But inner context re-enables it
        with ls.tracing_context(enabled=True):
            outer_function("data")  # is traced
    ```

    This can be useful when you want to temporarily enable tracing for debugging within a normally non-traced section.

    ## Conditionally redact inputs and outputs

    Sometimes you want the trace to be recorded—so you keep run timing, structure, errors, and metadata—but the inputs and outputs should be hidden for specific requests (for example, traces from tenants with strict privacy requirements). This is different from [disabling tracing](#disable-tracing-for-specific-invocations) entirely and from [`Client(hide_inputs=...)`](/langsmith/mask-inputs-outputs#hide-inputs-and-outputs), which applies the same redaction to every trace the client sends.

    To redact per-request, use [`tracing_context`](https://reference.langchain.com/python/langsmith/run_helpers/tracing_context) with the `replicas` parameter and pass an `updates` dict that overrides `inputs` and `outputs` on the recorded run. Because `tracing_context` is scoped to the current execution context, concurrent requests with different redaction policies do not race.

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import langsmith as ls
    from langsmith import traceable

    @traceable
    def my_agent(user_input: str) -> str:
        return process(user_input)

    def should_redact(tenant_id: str) -> bool:
        """Return True if traces for this tenant should have inputs/outputs masked."""
        return tenant_id in get_redacted_tenants()

    def handle_request(tenant_id: str, user_input: str) -> str:
        replica: dict = {"project_name": "my-project"}
        if should_redact(tenant_id):
            # Recorded run will have empty inputs/outputs but full structure,
            # timing, metadata, and any errors.
            replica["updates"] = {"inputs": {}, "outputs": {}}

        with ls.tracing_context(replicas=[replica]):
            return my_agent(user_input)
    ```

    You can use any subset of run fields in `updates` (for example, `{"inputs": {"redacted": True}}` to keep a marker, or `{"outputs": {}}` to redact only outputs). The same pattern works for routing different redaction policies to different destinations—each replica can specify its own `project_name`, `api_key`, and `updates`. See [Write traces to multiple destinations with replicas](/langsmith/log-traces-to-project#write-traces-to-multiple-destinations-with-replicas) for the full replica reference.

    <Note>
      Always set `project_name` on the replica when using `updates` to redact inputs or outputs. If the replica's `project_name` matches the active session's project, the `updates` may be dropped and the unredacted inputs/outputs will be sent.
    </Note>

    ## Customize tracing in deployed agents

    Tracing is enabled by default within LangSmith Deployment's [Agent Server](/langsmith/agent-server). When using a [factory function](/langsmith/graph-rebuild), you can wrap the yielded graph with `tracing_context` to control tracing per-execution. This is useful for adding custom metadata, disabling tracing entirely, or customizing tracing based on the authenticated user.

    ### Disable tracing for a graph

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import contextlib
    import langsmith as ls
    from langgraph_sdk.runtime import ServerRuntime

    @contextlib.asynccontextmanager
    async def make_graph(runtime: ServerRuntime):
        graph = build_my_graph()

        # You can use tracing_context to dynamically enable/disable tracing,
        # set metadata or tags, override the tracing project, etc.
        with ls.tracing_context(enabled=False, metadata={"foo": "bar"}):
            yield graph
    ```

    ### Per-user tracing

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import contextlib
    import langsmith as ls
    from langgraph_sdk.runtime import ServerRuntime

    def get_project_for_user(user_id: str) -> str | None:
        ...
        return "my-project"

    graph = build_my_graph()

    @contextlib.asynccontextmanager
    async def make_graph(runtime: ServerRuntime):
        user = runtime.user
        # Route traces to a different project depending on user or disable tracing entirely
        project_name = get_project_for_user(user.identity)

        if project_name is None:
            with ls.tracing_context(enabled=False):
                yield graph
        else:
            with ls.tracing_context(
                enabled=True,
                project_name=project_name,
                metadata={"user_id": user.identity, "foo": "bar"},
            ):
                yield graph
    ```

    ## Reusable tracing wrapper

    Create a decorator to automatically apply conditional tracing logic.

    ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import functools
    import langsmith as ls
    from langsmith import traceable

    def conditional_trace(check_function):
        """
        Decorator that conditionally traces based on a check function.

        Args:
            check_function: Function that returns True if tracing should be enabled
        """
        def decorator(func):
            traced_func = traceable(func)

            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                should_trace = check_function(*args, **kwargs)
                with ls.tracing_context(enabled=should_trace):
                    return traced_func(*args, **kwargs)
            return wrapper
        return decorator

    # Usage
    def should_trace_client(client_id: str, *args, **kwargs) -> bool:
        return not client_requires_zero_retention(client_id)

    @conditional_trace(should_trace_client)
    def process_request(client_id: str, data: str):
        return data.upper()

    # Automatically applies conditional tracing based on client_id
    process_request("client-a", "some data")
    ```
  </Tab>

  <Tab title="TypeScript" icon="brand-typescript">
    ## How tracing enabled works

    In TypeScript, you control tracing per-function using the [`tracingEnabled`](https://reference.langchain.com/javascript/classes/langsmith.run_trees.RunTree.html#tracingenabled) parameter when calling [`traceable()`](https://reference.langchain.com/python/langsmith/run_helpers/traceable). This allows you to selectively enable or disable tracing at the function level.

    A two-level system where tracing is controlled per-function:

    1. **`tracingEnabled` parameter**: highest priority (pass to [`traceable()`](https://reference.langchain.com/python/langsmith/run_helpers/traceable) config).
    2. **Environment variables**: lowest priority (`LANGSMITH_TRACING`).

    ## Disable tracing for specific invocations

    To disable tracing for a specific operation, create a version of your traceable function with `tracingEnabled: false`:

    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { traceable } from "langsmith/traceable";

    const myFunction = traceable(
        (inputText: string) => {
            return process(inputText);
        },
        { name: "my_function" }
    );

    // Default invocation - is traced
    await myFunction("regular data");

    // Disable tracing for sensitive data
    const myFunctionNoTrace = traceable(
        (inputText: string) => {
            return process(inputText);
        },
        { name: "my_function", tracingEnabled: false }
    );

    await myFunctionNoTrace("sensitive data");  // not traced
    ```

    This pattern is useful for one-off cases where you know specific data should not be logged.

    ## Enable conditional tracing based on business logic

    In many applications, you need to dynamically control tracing based on runtime conditions—such as client privacy requirements, regulatory compliance, or feature flags.

    In TypeScript, the most efficient approach is to create both traced and non-traced variants of your function upfront, then select between them at runtime based on your business logic. This avoids the performance overhead of creating new traced wrappers on every request while still providing fine-grained control over when tracing occurs. For example:

    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { traceable } from "langsmith/traceable";

    // Define the core logic once
    function processText(inputText: string): string {
        // Your actual processing logic
        return inputText.toUpperCase();
    }

    // Create traced and non-traced variants upfront
    const myFunction = traceable(processText, { name: "my_function" });
    const myFunctionNoTrace = traceable(processText, {
        name: "my_function",
        tracingEnabled: false
    });

    function clientRequiresZeroRetention(clientId: string): boolean {
        /**
         * Check if a client has a zero-retention policy.
         *
         * In production, this would query a database, configuration service,
         * or feature flag system. Consider caching results for performance.
         */
        const zeroRetentionClients = getZeroRetentionClients();  // Your implementation
        return zeroRetentionClients.includes(clientId);
    }

    async function handleRequest(clientId: string, userInput: string) {
        /**
         * Process a request with conditional tracing based on client requirements.
         * Efficiently selects pre-created traced or non-traced variant.
         */
        const shouldDisable = clientRequiresZeroRetention(clientId);

        // Select the appropriate pre-created variant
        const fn = shouldDisable ? myFunctionNoTrace : myFunction;
        return await fn(userInput);
    }

    // Example usage
    await handleRequest("client-a", "some input");  // Traced or not based on client settings
    ```

    ## Work with automatic tracing

    The [`tracingEnabled`](https://reference.langchain.com/javascript/classes/langsmith.run_trees.RunTree.html#tracingenabled) option works seamlessly with automatic tracing. You can keep `LANGSMITH_TRACING=true` set globally and use `tracingEnabled` to override settings for specific functions.

    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { traceable } from "langsmith/traceable";

    // Global tracing enabled via environment
    process.env.LANGSMITH_TRACING = "true";

    const processData = traceable(
        (data: string) => {
            return data.toUpperCase();
        },
        { name: "process_data" }
    );

    // Automatically traced (respects LANGSMITH_TRACING)
    await processData("hello");

    // Override global setting - disable for this call
    const processDataNoTrace = traceable(
        (data: string) => {
            return data.toUpperCase();
        },
        { name: "process_data", tracingEnabled: false }
    );

    await processDataNoTrace("sensitive");  // not traced

    // Override global setting - enable with custom config
    const processDataCustom = traceable(
        (data: string) => {
            return data.toUpperCase();
        },
        {
            name: "process_data",
            project_name: "special-project",
            tracingEnabled: true
        }
    );

    await processDataCustom("important");  // Traced to "special-project"
    ```
  </Tab>
</Tabs>

## Comparison with sampling

Conditional tracing and [sampling](/langsmith/sample-traces) serve different purposes:

| Feature            | Conditional tracing                               | Sampling                                     |
| ------------------ | ------------------------------------------------- | -------------------------------------------- |
| **Control**        | Deterministic (explicit enable/disable)           | Probabilistic (random sampling)              |
| **Use case**       | Business logic, compliance, per-request decisions | Cost optimization, high-volume observability |
| **Predictability** | Guaranteed behavior for specific requests         | Statistical representation of traffic        |
| **Configuration**  | Runtime code logic                                | Environment variable or client config        |

You can combine both approaches for fine-grained control.

## Related

* [Trace without environment variables](/langsmith/trace-without-env-vars): Configure tracing programmatically instead of using environment variables.
* [Set a sampling rate for traces](/langsmith/sample-traces): Probabilistically sample traces to reduce volume
* [Mask inputs and outputs](/langsmith/mask-inputs-outputs): Hide sensitive data in traces instead of disabling tracing entirely.
* [Add metadata and tags to traces](/langsmith/add-metadata-tags): Categorize and filter traces with custom attributes.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/conditional-tracing.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Use HTTP headers for runtime configuration
Source: https://docs.langchain.com/langsmith/configurable-headers

LangGraph allows runtime configuration to modify agent behavior and permissions dynamically. When using [LangSmith Deployment](/langsmith/deployment-quickstart), you can pass this configuration in the request body (`config`) or specific request headers. This enables adjustments based on user identity or other requests.

For privacy, control which headers are passed to the runtime configuration via the `http.configurable_headers` section in your [`langgraph.json`](/langsmith/application-structure#configuration-file) file.

Here's how to customize the included and excluded headers:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "http": {
    "configurable_headers": {
      "includes": ["x-user-id", "x-organization-id", "my-prefix-*"],
      "excludes": ["authorization", "x-api-key"]
    }
  }
}
```

The `includes` and `excludes` lists accept exact header names or patterns using `*` to match any number of characters. For your security, no other regex patterns are supported.

## Using within your graph

You can access the included headers in your graph using the `config` argument of any node.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
def my_node(state, config):
  organization_id = config["configurable"].get("x-organization-id")
  ...
```

Or by fetching from context (useful in tools and or within other nested functions).

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langgraph.config import get_config

def search_everything(query: str):
  organization_id = get_config()["configurable"].get("x-organization-id")
  ...
```

You can even use this to dynamically compile the graph.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# my_graph.py.
import contextlib

@contextlib.asynccontextmanager
async def generate_agent(config):
  organization_id = config["configurable"].get("x-organization-id")
  if organization_id == "org1":
    graph = ...
    yield graph
  else:
    graph = ...
    yield graph

```

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "graphs": {"agent": "my_grph.py:generate_agent"}
}
```

### Opt-out of configurable headers

If you'd like to opt-out of configurable headers, you can simply set a wildcard pattern in the `s` list:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "http": {
    "configurable_headers": {
      "excludes": ["*"]
    }
  }
}
```

This will exclude all headers from being added to your run's configuration.

Note that exclusions take precedence over inclusions.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/configurable-headers.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
