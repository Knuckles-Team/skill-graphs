# Application-specific evaluation approaches
Source: https://docs.langchain.com/langsmith/evaluation-approaches

Below, we will discuss evaluation of a few popular types of LLM applications.

## Agents

[LLM-powered autonomous agents](https://lilianweng.github.io/posts/2023-06-23-agent/) combine three components (1) Tool calling, (2) Memory, and (3) Planning. Agents [use tool calling](https://docs.langchain.com/oss/python/langchain/tools) with planning (e.g., often via prompting) and memory (e.g., often short-term message history) to generate responses. [Tool calling](https://docs.langchain.com/oss/python/langchain/tools) allows a model to respond to a given prompt by generating two things: (1) a tool to invoke and (2) the input arguments required.

<img alt="Tool use" />

Below is a tool-calling agent in [LangGraph](https://langchain-ai.github.io/langgraph/tutorials/introduction/). The `assistant node` is an LLM that determines whether to invoke a tool based upon the input. The `tool condition` sees if a tool was selected by the `assistant node` and, if so, routes to the `tool node`. The `tool node` executes the tool and returns the output as a tool message to the `assistant node`. This loop continues until as long as the `assistant node` selects a tool. If no tool is selected, then the agent directly returns the LLM response.

<img alt="Agent" />

This sets up three general types of agent evaluations that users are often interested in:

* `Final Response`: Evaluate the agent's final response.
* `Single step`: Evaluate any agent step in isolation (e.g., whether it selects the appropriate tool).
* `Trajectory`: Evaluate whether the agent took the expected path (e.g., of tool calls) to arrive at the final answer.

<img alt="Agent-eval" />

Below we will cover what these are, the components (inputs, outputs, evaluators) needed for each one, and when you should consider this. Note that you likely will want to do multiple (if not all!) of these types of evaluations - they are not mutually exclusive!

### Evaluating an agent's final response

One way to evaluate an agent is to assess its overall performance on a task. This basically involves treating the agent as a black box and simply evaluating whether or not it gets the job done.

The inputs should be the user input and (optionally) a list of tools. In some cases, tool are hardcoded as part of the agent and they don't need to be passed in. In other cases, the agent is more generic, meaning it does not have a fixed set of tools and tools need to be passed in at run time.

The output should be the agent's final response.

The evaluator varies depending on the task you are asking the agent to do. Many agents perform a relatively complex set of steps and the output a final text response. Similar to RAG, LLM-as-judge evaluators are often effective for evaluation in these cases because they can assess whether the agent got a job done directly from the text response.

However, there are several downsides to this type of evaluation. First, it usually takes a while to run. Second, you are not evaluating anything that happens inside the agent, so it can be hard to debug when failures occur. Third, it can sometimes be hard to define appropriate evaluation metrics.

### Evaluating a single step of an agent

Agents generally perform multiple actions. While it is useful to evaluate them end-to-end, it can also be useful to evaluate these individual actions. This generally involves evaluating a single step of the agent - the LLM call where it decides what to do.

The inputs should be the input to a single step. Depending on what you are testing, this could just be the raw user input (e.g., a prompt and / or a set of tools) or it can also include previously completed steps.

The outputs are just the output of that step, which is usually the LLM response. The LLM response often contains tool calls, indicating what action the agent should take next.

The evaluator for this is usually some binary score for whether the correct tool call was selected, as well as some heuristic for whether the input to the tool was correct. The reference tool can be simply specified as a string.

There are several benefits to this type of evaluation. It allows you to evaluate individual actions, which lets you hone in where your application may be failing. They are also relatively fast to run (because they only involve a single LLM call) and evaluation often uses simple heuristic evaluation of the selected tool relative to the reference tool. One downside is that they don't capture the full agent - only one particular step. Another downside is that dataset creation can be challenging, particular if you want to include past history in the agent input. It is pretty easy to generate a dataset for steps early on in an agent's trajectory (e.g., this may only include the input prompt), but it can be difficult to generate a dataset for steps later on in the trajectory (e.g., including numerous prior agent actions and responses).

### Evaluating an agent's trajectory

Evaluating an agent's trajectory involves evaluating all the steps an agent took.

The inputs are again the inputs to the overall agent (the user input, and optionally a list of tools).

The outputs are a list of tool calls, which can be formulated as an "exact" trajectory (e.g., an expected sequence of tool calls) or simply a set of tool calls that are expected (in any order).

The evaluator here is some function over the steps taken. Assessing the "exact" trajectory can use a single binary score that confirms an exact match for each tool name in the sequence. This is simple, but has some flaws. Sometimes there can be multiple correct paths. This evaluation also does not capture the difference between a trajectory being off by a single step versus being completely wrong.

To address these flaws, evaluation metrics can focused on the number of "incorrect" steps taken, which better accounts for trajectories that are close versus ones that deviate significantly. Evaluation metrics can also focus on whether all of the expected tools are called in any order.

However, none of these approaches evaluate the input to the tools; they only focus on the tools selected. In order to account for this, another evaluation technique is to pass the full agent's trajectory (along with a reference trajectory) as a set of messages (e.g., all LLM responses and tool calls) an LLM-as-judge. This can evaluate the complete behavior of the agent, but it is the most challenging reference to compile (luckily, using a framework like LangGraph can help with this!). Another downside is that evaluation metrics can be somewhat tricky to come up with.

## Retrieval augmented generation (RAG)

Retrieval Augmented Generation (RAG) is a powerful technique that involves retrieving relevant documents based on a user's input and passing them to a language model for processing. RAG enables AI applications to generate more informed and context-aware responses by leveraging external knowledge.

<Info>
  For a comprehensive review of RAG concepts, see our [`RAG From Scratch` series](https://github.com/langchain-ai/rag-from-scratch).
</Info>

### Dataset

When evaluating RAG applications, a key consideration is whether you have (or can easily obtain) reference answers for each input question. Reference answers serve as ground truth for assessing the correctness of the generated responses. However, even in the absence of reference answers, various evaluations can still be performed using reference-free RAG evaluation prompts (examples provided below).

### Evaluator

`LLM-as-judge` is a commonly used evaluator for RAG because it's an effective way to evaluate factual accuracy or consistency between texts.

<img alt="rag-types.png" />

When evaluating RAG applications, you can have evaluators that require reference outputs and those that don't:

1. **Require reference output**: Compare the RAG chain's generated answer or retrievals against a reference answer (or retrievals) to assess its correctness.
2. **Don't require reference output**: Perform self-consistency checks using prompts that don't require a reference answer (represented by orange, green, and red in the above figure).

### Applying RAG evaluation

When applying RAG evaluation, consider the following approaches:

1. `Offline evaluation`: Use offline evaluation for any prompts that rely on a reference answer. This is most commonly used for RAG answer correctness evaluation, where the reference is a ground truth (correct) answer.

2. `Online evaluation`: Employ online evaluation for any reference-free prompts. This allows you to assess the RAG application's performance in real-time scenarios.

3. `Pairwise evaluation`: Utilize pairwise evaluation to compare answers produced by different RAG chains. This evaluation focuses on user-specified criteria (e.g., answer format or style) rather than correctness, which can be evaluated using self-consistency or a ground truth reference.

### RAG evaluation summary

| Evaluator           | Detail                                            | Needs reference output | LLM-as-judge?                                                                         | Pairwise relevant |
| ------------------- | ------------------------------------------------- | ---------------------- | ------------------------------------------------------------------------------------- | ----------------- |
| Document relevance  | Are documents relevant to the question?           | No                     | Yes - [prompt](https://smith.langchain.com/hub/langchain-ai/rag-document-relevance)   | No                |
| Answer faithfulness | Is the answer grounded in the documents?          | No                     | Yes - [prompt](https://smith.langchain.com/hub/langchain-ai/rag-answer-hallucination) | No                |
| Answer helpfulness  | Does the answer help address the question?        | No                     | Yes - [prompt](https://smith.langchain.com/hub/langchain-ai/rag-answer-helpfulness)   | No                |
| Answer correctness  | Is the answer consistent with a reference answer? | Yes                    | Yes - [prompt](https://smith.langchain.com/hub/langchain-ai/rag-answer-vs-reference)  | No                |
| Pairwise comparison | How do multiple answer versions compare?          | No                     | Yes - [prompt](https://smith.langchain.com/hub/langchain-ai/pairwise-evaluation-rag)  | Yes               |

## Summarization

Summarization is one specific type of free-form writing. The evaluation aim is typically to examine the writing (summary) relative to a set of criteria.

`Developer curated examples` of texts to summarize are commonly used for evaluation (see a [summarization dataset example](https://smith.langchain.com/public/659b07af-1cab-4e18-b21a-91a69a4c3990/d)). However, `user logs` from a production (summarization) app can be used for online evaluation with any of the `Reference-free` evaluation prompts below.

`LLM-as-judge` is typically used for evaluation of summarization (as well as other types of writing) using `Reference-free` prompts that follow provided criteria to grade a summary. It is less common to provide a particular `Reference` summary, because summarization is a creative task and there are many possible correct answers.

`Online` or `Offline` evaluation are feasible because of the `Reference-free` prompt used. `Pairwise` evaluation is also a powerful way to perform comparisons between different summarization chains (e.g., different summarization prompts or LLMs):

| Use Case         | Detail                                                                     | Needs reference output | LLM-as-judge?                                                                                | Pairwise relevant |
| ---------------- | -------------------------------------------------------------------------- | ---------------------- | -------------------------------------------------------------------------------------------- | ----------------- |
| Factual accuracy | Is the summary accurate relative to the source documents?                  | No                     | Yes - [prompt](https://smith.langchain.com/hub/langchain-ai/summary-accurancy-evaluator)     | Yes               |
| Faithfulness     | Is the summary grounded in the source documents (e.g., no hallucinations)? | No                     | Yes - [prompt](https://smith.langchain.com/hub/langchain-ai/summary-hallucination-evaluator) | Yes               |
| Helpfulness      | Is summary helpful relative to user need?                                  | No                     | Yes - [prompt](https://smith.langchain.com/hub/langchain-ai/summary-helpfulness-evaluator)   | Yes               |

## Classification and tagging

Classification and tagging apply a label to a given input (e.g., for toxicity detection, sentiment analysis, etc). Classification/tagging evaluation typically employs the following components, which we will review in detail below:

A central consideration for classification/tagging evaluation is whether you have a dataset with `reference` labels or not. If not, users frequently want to define an evaluator that uses criteria to apply label (e.g., toxicity, etc) to an input (e.g., text, user-question, etc). However, if ground truth class labels are provided, then the evaluation objective is focused on scoring a classification/tagging chain relative to the ground truth class label (e.g., using metrics such as precision, recall, etc).

If ground truth reference labels are provided, then it's common to simply define a [custom heuristic evaluator](/langsmith/code-evaluator-ui) to compare ground truth labels to the chain output. However, it is increasingly common given the emergence of LLMs simply use `LLM-as-judge` to perform the classification/tagging of an input based upon specified criteria (without a ground truth reference).

`Online` or `Offline` evaluation is feasible when using `LLM-as-judge` with the `Reference-free` prompt used. In particular, this is well suited to `Online` evaluation when a user wants to tag / classify application input (e.g., for toxicity, etc).

| Use Case  | Detail              | Needs reference output | LLM-as-judge? | Pairwise relevant |
| --------- | ------------------- | ---------------------- | ------------- | ----------------- |
| Accuracy  | Standard definition | Yes                    | No            | No                |
| Precision | Standard definition | Yes                    | No            | No                |
| Recall    | Standard definition | Yes                    | No            | No                |

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/evaluation-approaches.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# How to run an evaluation asynchronously
Source: https://docs.langchain.com/langsmith/evaluation-async

<Info>
  [Evaluations](/langsmith/evaluation-concepts#evaluation-lifecycle) | [Evaluators](/langsmith/evaluation-concepts#evaluators) | [Datasets](/langsmith/evaluation-concepts#datasets) | [Experiments](/langsmith/evaluation-concepts#experiment)
</Info>

We can run evaluations asynchronously via the SDK using [aevaluate()](https://docs.smith.langchain.com/reference/python/evaluation/langsmith.evaluation._arunner.aevaluate), which accepts all of the same arguments as [evaluate()](https://docs.smith.langchain.com/reference/python/evaluation/langsmith.evaluation._runner.evaluate) but expects the application function to be asynchronous. To learn more, see [how to use the `evaluate()` function](/langsmith/evaluate-llm-application).

<Info>
  This guide is only relevant when using the Python SDK. In JS/TS the `evaluate()` function is already async. For more information, see [Evaluate LLM applications](/langsmith/evaluate-llm-application).
</Info>

## Use `aevaluate()`

* Python

Requires `langsmith>=0.3.13`

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langsmith import wrappers, Client
from openai import AsyncOpenAI

# Optionally wrap the OpenAI client to trace all model calls.
oai_client = wrappers.wrap_openai(AsyncOpenAI())

# Optionally add the 'traceable' decorator to trace the inputs/outputs of this function.
@traceable
async def researcher_app(inputs: dict) -> str:
    instructions = """You are an excellent researcher. Given a high-level research idea, \
list 5 concrete questions that should be investigated to determine if the idea is worth pursuing."""

    response = await oai_client.chat.completions.create(
        model="gpt-5.4-mini",
        messages=[
            {"role": "system", "content": instructions},
            {"role": "user", "content": inputs["idea"]},
        ],
    )
    return response.choices[0].message.content

# Evaluator functions can be sync or async
def concise(inputs: dict, outputs: dict) -> bool:
    return len(outputs["output"]) < 3 * len(inputs["idea"])

ls_client = Client()
ideas = [
    "universal basic income",
    "nuclear fusion",
    "hyperloop",
    "nuclear powered rockets",
]
dataset = ls_client.create_dataset("research ideas")
ls_client.create_examples(
    dataset_name=dataset.name,
    examples=[{"inputs": {"idea": i}} for i in ideas],
)

# Can equivalently use the 'aevaluate' function directly:

# from langsmith import aevaluate

# await aevaluate(...)
results = await ls_client.aevaluate(
    researcher_app,
    data=dataset,
    evaluators=[concise],
    # Optional, add concurrency.
    max_concurrency=2,  # Optional, add concurrency.
    experiment_prefix="gpt-5.4-mini-baseline"  # Optional, random by default.
)
```

## Related

* [Run an evaluation (synchronously)](/langsmith/evaluate-llm-application)
* [Handle model rate limits](/langsmith/rate-limiting)

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/evaluation-async.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Evaluation concepts
Source: https://docs.langchain.com/langsmith/evaluation-concepts

LLM outputs are non-deterministic, which makes response quality hard to assess. Evaluations (evals) are a way to breakdown what "good" looks like and measure it. LangSmith Evaluation provides a framework for measuring quality throughout the application lifecycle, from pre-deployment testing to production monitoring.

## What to evaluate

Before building evaluations, identify what matters for your application. Break down your system into its critical components—LLM calls, retrieval steps, tool invocations, output formatting—and determine quality criteria for each.

**Start with manually curated examples.** Create 5-10 examples of what "good" looks like for each critical component. These examples serve as your ground truth and inform which evaluation approaches to use. For instance:

* **RAG system**: Examples of good retrievals (relevant documents) and good answers (accurate, complete).
* **Agent**: Examples of correct tool selection and proper argument formatting or trajectory that the agent took.
* **Chatbot**: Examples of helpful, on-brand responses that address user intent.

Once you've defined "good" through examples, you can measure how often your system produces similar quality outputs.

## Offline and online evaluations

LangSmith supports two types of evaluations that serve different purposes in your development workflow:

### Offline evaluations

<Icon icon="flask" /> Use offline evaluations for **pre-deployment testing**:

* **Benchmarking**: Compare multiple versions to find the best performer.
* **Regression testing**: Ensure new versions don't degrade quality.
* **Unit testing**: Verify correctness of individual components.
* **Backtesting**: Test new versions against historical data.

Offline evaluations target [*examples*](#examples) from [*datasets*](#datasets): curated test cases with reference outputs that define what "good" looks like.

### Online evaluations

<Icon icon="radar" /> Use online evaluations for **production monitoring**:

* **Real-time monitoring**: Track quality continuously on live traffic.
* **Anomaly detection**: Flag unusual patterns or edge cases.
* **Production feedback**: Identify issues to add to offline datasets.

Online evaluations target [*runs*](#runs) and [*threads*](#threads) from [tracing](/langsmith/observability-quickstart): real production traces without reference outputs.

This difference in targets determines what you can evaluate: offline evaluations can check correctness against expected answers, while online evaluations focus on quality patterns, safety, and real-world behavior.

## Evaluation lifecycle

As you develop and [deploy your application](/langsmith/deployment), your evaluation strategy evolves from pre-deployment testing to production monitoring. During development and testing, offline evaluations validate functionality against curated datasets. After deployment, online evaluations monitor production behavior on live traffic. As applications mature, both evaluation types work together in an iterative feedback loop to improve quality continuously.

```mermaid theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
graph LR
    A[Development] --> B[Testing]
    B --> C[Deployment]
    C --> D[Monitoring]
    D --> E[Iteration]

    A -.-> F[Offline]
    B -.-> F
    C -.-> G[Online]
    D -.-> G
    E -.-> H[Both]

    classDef process fill:#E5F4FF,stroke:#006DDD,stroke-width:2px,color:#030710

    class A,B,C,D,E process

    style F fill:#EBD0F0,stroke:#885270,color:#441E33
    style G fill:#EBD0F0,stroke:#885270,color:#441E33
    style H fill:#EBD0F0,stroke:#885270,color:#441E33
```

### 1. Development with offline evaluation

Before production deployment, use offline evaluations to validate functionality, benchmark different approaches, and build confidence.

Follow the [quickstart](/langsmith/evaluation-quickstart) to run your first offline evaluation.

### 2. Initial deployment with online evaluation

After deployment, use online evaluations to monitor production quality, detect unexpected issues, and collect real-world data.

Learn how to [configure online evaluations](/langsmith/online-evaluations-llm-as-judge) for production monitoring.

### 3. Continuous improvement

Use both evaluation types together in an iterative feedback loop. Online evaluations surface issues that become offline test cases, offline evaluations validate fixes, and online evaluations confirm production improvements.

## Core evaluation targets

Evaluations run on different targets depending on whether they are offline or online.

### Targets for offline evaluation

Offline evaluations run on datasets and examples. The presence of reference outputs enables comparison between expected and actual results.

#### Datasets

A dataset is a *collection of examples* used for evaluating an application. An example is a test input, reference output pair.

<img alt="List of datasets on the Examples tab in the LangSmith UI." />

<img alt="List of datasets on the Examples tab in the LangSmith UI." />

#### Examples

Each example consists of:

* **Inputs**: a dictionary of input variables to pass to your application.
* **Reference outputs** (optional): a dictionary of reference outputs. These do not get passed to your application, they are only used in evaluators.
* **Metadata** (optional): a dictionary of additional information that can be used to create filtered views of a dataset.

<img alt="Example in the LangSmith UI." />

<img alt="Example in the LangSmith UI." />

Learn more about [managing datasets](/langsmith/manage-datasets).

#### Experiment

An *experiment* represents the results of evaluating a specific application version on a dataset. Each experiment captures outputs, evaluator scores, and execution traces for every example in the dataset.

<img alt="Experiment view" />

Multiple experiments typically run on a given dataset to test different application configurations (e.g., different prompts or LLMs). LangSmith displays all experiments associated with a dataset and supports [comparing multiple experiments](/langsmith/compare-experiment-results) side-by-side.

Learn [how to analyze experiment results](/langsmith/analyze-an-experiment).

### Targets for online evaluation

Online evaluations run on runs and threads from production traffic. Without reference outputs, evaluators focus on detecting issues, anomalies, and quality degradation in real-time.

#### Runs

A *run* is a single execution trace from your [deployed application](/langsmith/deployment). Each run contains:

* **Inputs**: The actual user inputs your application received.
* **Outputs**: What your application actually returned.
* **Intermediate steps**: All the child runs (tool calls, LLM calls, and so on).
* **Metadata**: Tags, user feedback, latency metrics, etc.

Unlike examples in datasets, runs do not include reference outputs. Online evaluators must assess quality without knowing what the "correct" answer should be, relying instead on quality heuristics, safety checks, and reference-free evaluation techniques.

Learn more about [runs and traces in the Observability concepts](/langsmith/observability-concepts#runs).

#### Threads

*Threads* are collections of related runs representing multi-turn conversations. Online evaluators can run at the thread level to evaluate entire conversations rather than individual turns. This enables assessment of conversation-level properties like coherence across turns, topic maintenance, and user satisfaction throughout an interaction.

## Evaluators

*Evaluators* are workspace-level resources that score application performance. They provide the measurement layer for both offline and online evaluation, adapting their inputs based on what data is available. Because evaluators are scoped to the workspace, you can attach a single evaluator to multiple tracing projects and datasets without recreating it each time.

Run evaluators using any of the following:

* The [Evaluators](/langsmith/evaluators) page, to attach them to tracing projects or datasets
* The [Playground](/langsmith/prompt-engineering-concepts#playground)
* The LangSmith SDK ([Python](https://docs.smith.langchain.com/reference/python/reference) and [TypeScript](https://docs.smith.langchain.com/reference/js))
* [Rules](/langsmith/rules), to run them automatically on tracing projects or datasets

### Evaluator inputs

Evaluator inputs differ based on evaluation type:

**Offline evaluators** receive:

* [Example](#examples): The example from your [dataset](#datasets), containing inputs, reference outputs, and metadata.
* [Run](/langsmith/observability-concepts#runs): The actual outputs and intermediate steps from running the application on the example inputs.

**Online evaluators** receive:

* [Run](/langsmith/observability-concepts#runs): The production trace containing inputs, outputs, and intermediate steps (no reference outputs available).

### Evaluator outputs

Evaluators return **feedback**, which is the scores from evaluation. Feedback is a dictionary or list of dictionaries. Each dictionary contains:

* `key`: The metric name.
* `score` | `value`: The metric value (`score` for numerical metrics, `value` for categorical metrics).
* `comment` (optional): Additional reasoning or explanation for the score.

### Evaluation techniques

LangSmith supports several evaluation approaches:

* [Human](#human)
* [Code](#code)
* [LLM-as-judge](#llm-as-judge)
* [Pairwise](#pairwise)

#### Human

*Human evaluation* involves manual review of application outputs and execution traces. This approach is [often an effective starting point for evaluation](https://hamel.dev/blog/posts/evals/#looking-at-your-traces). LangSmith provides tools to review application outputs and traces (all intermediate steps).

**Annotation queues**

[Annotation queues](/langsmith/annotation-queues) streamline structured collection of human feedback on runs. They complement [inline annotation](/langsmith/annotate-traces-inline) by providing organized workflows with prescribed rubrics, team collaboration features, and progress tracking.

LangSmith supports two queue types:

* **Single-run queues**: Review one run at a time against custom rubric items. Useful for triaging issues or building datasets from production traces. Single-run queues also support [assertions](/langsmith/assertions), free-form acceptance criteria that an offline evaluator can grade future runs against.
* **Pairwise queues**: Compare two runs side-by-side to judge which is better. Designed for fast A/B comparisons between experiments.

Key features include configuring multiple reviewers per run, enabling reservations to prevent conflicts, and exporting annotated runs directly to datasets for future evaluations.

#### Code

*Code evaluators* are deterministic, rule-based functions. They work well for checks such as verifying the structure of a chatbot's response is not empty, that generated code compiles, or that a classification matches exactly.

#### LLM-as-judge

*LLM-as-judge evaluators* use LLMs to score application outputs. The grading rules and criteria are typically encoded in the LLM prompt. These evaluators can be:

* **Reference-free**: Check if output contains offensive content or adheres to specific criteria.
* **Reference-based**: Compare output to a reference (e.g., check factual accuracy relative to the reference).

LLM-as-judge evaluators require careful review of scores and prompt tuning. Few-shot evaluators, which include examples of inputs, outputs, and expected grades in the grader prompt, often improve performance.

Learn about [how to define an LLM-as-a-judge evaluator](/langsmith/llm-as-judge).

#### Pairwise

*Pairwise evaluators* compare outputs from two application versions using heuristics (e.g., which response is longer), LLMs (with pairwise prompts), or human reviewers.

Pairwise evaluation works well when directly scoring an output is difficult but comparing two outputs is straightforward. For example, in summarization tasks, choosing the more informative of two summaries is often easier than assigning an absolute score to a single summary.

Learn [how run pairwise evaluations](/langsmith/evaluate-pairwise).

### Reference-free vs reference-based evaluators

Understanding whether an evaluator requires reference outputs is essential for determining when it can be used.

**Reference-free evaluators** assess quality without comparing to expected outputs. These work for both offline and online evaluation:

* **Safety checks**: Toxicity detection, PII detection, content policy violations
* **Format validation**: JSON structure, required fields, schema compliance
* **Quality heuristics**: Response length, latency, specific keywords
* **Reference-free LLM-as-judge**: Clarity, coherence, helpfulness, tone

**Reference-based evaluators** require reference outputs and only work for offline evaluation:

* **Correctness**: Semantic similarity to reference answer
* **Factual accuracy**: Fact-checking against ground truth
* **Exact match**: Classification tasks with known labels
* **Reference-based LLM-as-judge**: Comparing output quality to a reference

When designing an evaluation strategy, reference-free evaluators provide consistency across both offline testing and online monitoring, while reference-based evaluators enable more precise correctness checks during development.

## Evaluation types

LangSmith supports various evaluation approaches for different stages of development and deployment. Understanding when to use each type helps build a comprehensive evaluation strategy.

Offline and online evaluations serve different purposes:

* **Offline evaluation types** test pre-deployment on curated datasets with reference outputs
* **Online evaluation types** monitor production behavior on live traffic without reference outputs

Learn more about [evaluation types and when to use each](/langsmith/evaluation-types).

## Best practices

### Building datasets

There are various strategies for building datasets:

**Manually curated examples**

This is the recommended starting point. Create 10–20 high-quality examples covering common scenarios and edge cases. These examples define what "good" looks like for your application.

**Historical traces**

Once in production, convert real traces into examples. For high-traffic applications:

* **User feedback**: Add runs that received negative feedback to test against.
* **Heuristics**: Identify interesting runs (e.g., long latency, errors).
* **LLM feedback**: Use LLMs to detect noteworthy conversations.

**Synthetic data**

Generate additional examples from existing ones. Works best when starting with several high-quality, hand-crafted examples as templates.

### Dataset organization

**Splits**

Splits are named subsets of a dataset used to segment examples into separate groups. Common patterns include:

* **ML-style splits**: divide examples into training, validation, and test sets to avoid overfitting, where a model performs well on training data but poorly on unseen data.
* **Category-based splits**: evaluate different input types separately when a dataset spans multiple task categories.
* **Staged rollout**: keep exploratory examples isolated until you're ready to include them in the main evaluation set.

Splits differ from metadata: use splits for high-level organizational grouping for evaluation, and metadata for per-example information such as tags and provenance.

In machine learning, best practice is for each example to belong to exactly one split. LangSmith allows examples to belong to multiple splits, which is useful when an example fits several evaluation categories.

Learn how to [create and manage dataset splits](/langsmith/manage-datasets-in-application#create-and-manage-dataset-splits).

**Versions**

LangSmith automatically creates dataset [versions](/langsmith/manage-datasets#version-a-dataset) when examples change. [Tag versions](/langsmith/manage-datasets#tag-a-version) to mark important milestones. Target specific versions in CI pipelines to ensure dataset updates don't break workflows.

### Human feedback collection

Human feedback often provides the most valuable assessment, particularly for subjective quality dimensions.

**Annotation queues**

[Annotation queues](/langsmith/annotation-queues) enable structured collection of human feedback. Flag specific runs for review, collect annotations in a streamlined interface, and transfer annotated runs to datasets for future evaluations.

Annotation queues complement [inline annotation](/langsmith/annotate-traces-inline) by offering additional capabilities: grouping runs, specifying criteria, and configuring reviewer permissions.

### Evaluations vs testing

Testing and evaluation are similar but distinct concepts.

**Evaluation measures performance according to metrics.** Metrics can be fuzzy or subjective, and prove more useful in relative terms. They typically compare systems against each other.

**Testing asserts correctness.** A system can only be deployed if it passes all tests.

Evaluation metrics can be converted into tests. For example, regression tests can assert that new versions must outperform baseline versions on relevant metrics. Run tests and evaluations together for efficiency when systems are expensive to run.

Evaluations can be written using standard testing tools like [pytest](/langsmith/pytest) or [Vitest/Jest](/langsmith/vitest-jest).

## Quick reference: Offline vs online evaluation

The following table summarizes the key differences between offline and online evaluations:

|                       | **Offline Evaluation**                                      | **Online Evaluation**                                                             |
| --------------------- | ----------------------------------------------------------- | --------------------------------------------------------------------------------- |
| **Runs on**           | Dataset (Examples)                                          | Tracing Project (Runs/Threads)                                                    |
| **Data access**       | Inputs, Outputs, Reference Outputs                          | Inputs, Outputs only                                                              |
| **When to use**       | Pre-deployment, during development                          | Production, post-deployment                                                       |
| **Primary use cases** | Benchmarking, unit testing, regression testing, backtesting | Real-time monitoring, production feedback, anomaly detection                      |
| **Evaluation timing** | Batch processing on curated test sets                       | Real-time or near real-time on live traffic                                       |
| **Setup location**    | Evaluation tab (SDK, UI, Playground)                        | [Observability tab](/langsmith/online-evaluations-llm-as-judge) (automated rules) |
| **Data requirements** | Requires dataset curation                                   | No dataset needed, evaluates live traces                                          |

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/evaluation-concepts.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
