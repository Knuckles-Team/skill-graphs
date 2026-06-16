# Remember that langgraph graphs are also langchain runnables.
target = example_to_state | app

async def main():
    experiment_results = await aevaluate(
        target,
        data="weather agent",
        evaluators=[correct],
        max_concurrency=4,  # optional
        experiment_prefix="claude-sonnet-4-6-baseline",  # optional
        metadata={  # optional, used to populate model/prompt/tool columns in UI
            "models": "google_genai:gemini-3.5-flash",
            "tools": [{"name": "search", "description": "Call to surf the web."}],
        },
    )
    print(experiment_results)

asyncio.run(main())
```

## Evaluating intermediate steps

Often it is valuable to evaluate not only the final output of an agent but also the intermediate steps it has taken. What's nice about `langgraph` is that the output of a graph is a state object that often already carries information about the intermediate steps taken. Usually we can evaluate whatever we're interested in just by looking at the messages in our state. For example, we can look at the messages to assert that the model invoked the 'search' tool upon as a first step.

Requires `langsmith>=0.2.0`

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
def right_tool(outputs: dict) -> bool:
    tool_calls = outputs["messages"][1].tool_calls
    return bool(tool_calls and tool_calls[0]["name"] == "search")

async def main():
    experiment_results = await aevaluate(
        target,
        data="weather agent",
        evaluators=[correct, right_tool],
        max_concurrency=4,  # optional
        experiment_prefix="claude-sonnet-4-6-baseline",  # optional
        metadata={  # optional, used to populate model/prompt/tool columns in UI
            "models": "google_genai:gemini-3.5-flash",
            "tools": [{"name": "search", "description": "Call to surf the web."}],
        },
    )
    print(experiment_results)
```

If we need access to information about intermediate steps that isn't in state, we can look at the Run object. This contains the full traces for all node inputs and outputs:

<Check>
  See more about what arguments you can pass to custom evaluators in this [how-to guide](/langsmith/code-evaluator-ui).
</Check>

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langsmith.schemas import Run, Example

def right_tool_from_run(run: Run, example: Example) -> dict:
    # Get documents and answer
    first_model_run = next(run for run in root_run.child_runs if run.name == "agent")
    tool_calls = first_model_run.outputs["messages"][-1].tool_calls
    right_tool = bool(tool_calls and tool_calls[0]["name"] == "search")
    return {"key": "right_tool", "value": right_tool}

async def main():
    experiment_results = await aevaluate(
        target,
        data="weather agent",
        evaluators=[correct, right_tool_from_run],
        max_concurrency=4,  # optional
        experiment_prefix="claude-sonnet-4-6-baseline",  # optional
        metadata={  # optional, used to populate model/prompt/tool columns in UI
            "models": "google_genai:gemini-3.5-flash",
            "tools": [{"name": "search", "description": "Call to surf the web."}],
        },
    )
    print(experiment_results)
```

## Running and evaluating individual nodes

Sometimes you want to evaluate a single node directly to save time and costs. `langgraph` makes it easy to do this. In this case we can even continue using the evaluators we've been using.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
node_target = example_to_state | app.nodes["agent"]

async def main():
    node_experiment_results = await aevaluate(
        node_target,
        data="weather agent",
        evaluators=[right_tool_from_run],
        max_concurrency=4,  # optional
        experiment_prefix="claude-sonnet-4-6-model-node",  # optional
        metadata={  # optional, used to populate model/prompt/tool columns in UI
            "models": "google_genai:gemini-3.5-flash",
            "tools": [{"name": "search", "description": "Call to surf the web."}],
        },
    )
    print(node_experiment_results)
```

## Related

* [`langgraph` evaluation docs](https://langchain-ai.github.io/langgraph/tutorials/#evaluation)

## Reference code

<Accordion title="Click to see a consolidated code snippet">
  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import asyncio
  from typing import Annotated, Literal, TypedDict
  from langchain.chat_models import init_chat_model
  from langchain.tools import tool
  from langgraph.prebuilt import ToolNode
  from langgraph.graph import END, START, StateGraph
  from langgraph.graph.message import add_messages
  from langsmith import Client, aevaluate

  # Define a graph
  class State(TypedDict):
      # Messages have the type "list". The 'add_messages' function
      # in the annotation defines how this state key should be updated
      # (in this case, it appends messages to the list, rather than overwriting them)
      messages: Annotated[list, add_messages]

  # Define the tools for the agent to use
  @tool
  def search(query: str) -> str:
      """Call to surf the web."""
      # This is a placeholder, but don't tell the LLM that...
      if "sf" in query.lower() or "san francisco" in query.lower():
          return "It's 60 degrees and foggy."
      return "It's 90 degrees and sunny."

  tools = [search]
  tool_node = ToolNode(tools)
  model = init_chat_model("claude-sonnet-4-6").bind_tools(tools)

  # Define the function that determines whether to continue or not
  def should_continue(state: State) -> Literal["tools", END]:
      messages = state['messages']
      last_message = messages[-1]

      # If the LLM makes a tool call, then we route to the "tools" node
      if last_message.tool_calls:
          return "tools"

      # Otherwise, we stop (reply to the user)
      return END

  # Define the function that calls the model
  def call_model(state: State):
      messages = state['messages']
      response = model.invoke(messages)
      # We return a list, because this will get added to the existing list
      return {"messages": [response]}

  # Define a new graph
  workflow = StateGraph(State)

  # Define the two nodes we will cycle between
  workflow.add_node("agent", call_model)
  workflow.add_node("tools", tool_node)

  # Set the entrypoint as 'agent'
  # This means that this node is the first one called
  workflow.add_edge(START, "agent")

  # We now add a conditional edge
  workflow.add_conditional_edges(
      # First, we define the start node. We use 'agent'.
      # This means these are the edges taken after the 'agent' node is called.
      "agent",
      # Next, we pass in the function that will determine which node is called next.
      should_continue,
  )

  # We now add a normal edge from 'tools' to 'agent'.
  # This means that after 'tools' is called, 'agent' node is called next.
  workflow.add_edge("tools", 'agent')

  # Finally, we compile it!
  # This compiles it into a LangChain Runnable,
  # meaning you can use it as you would any other runnable.
  # Note that we're (optionally) passing the memory when compiling the graph
  app = workflow.compile()

  questions = [
      "what's the weather in sf",
      "what's the weather in san fran",
      "what's the weather in tangier"
  ]

  answers = [
      "It's 60 degrees and foggy.",
      "It's 60 degrees and foggy.",
      "It's 90 degrees and sunny.",
  ]

  # Create a dataset
  ls_client = Client()
  dataset = ls_client.create_dataset("weather agent")
  ls_client.create_examples(
      inputs=[{"question": q} for q in questions],
      outputs=[{"answer": a} for a in answers],
      dataset_id=dataset.id,
  )

  # Define evaluators

  judge_llm = init_chat_model("gpt-5.5")

  async def correct(outputs: dict, reference_outputs: dict) -> bool:
      instructions = (
          "Given an actual answer and an expected answer, determine whether"
          " the actual answer contains all of the information in the"
          " expected answer. Respond with 'CORRECT' if the actual answer"
          " does contain all of the expected information and 'INCORRECT'"
          " otherwise. Do not include anything else in your response."
      )
      # Our graph outputs a State dictionary, which in this case means
      # we'll have a 'messages' key and the final message should
      # be our actual answer.
      actual_answer = outputs["messages"][-1].content
      expected_answer = reference_outputs["answer"]
      user_msg = (
          f"ACTUAL ANSWER: {actual_answer}"
          f"\n\nEXPECTED ANSWER: {expected_answer}"
      )
      response = await judge_llm.ainvoke(
          [
              {"role": "system", "content": instructions},
              {"role": "user", "content": user_msg}
          ]
      )
      return response.content.upper() == "CORRECT"

  def right_tool(outputs: dict) -> bool:
      tool_calls = outputs["messages"][1].tool_calls
      return bool(tool_calls and tool_calls[0]["name"] == "search")

  def example_to_state(inputs: dict) -> dict:
    return {"messages": [{"role": "user", "content": inputs['question']}]}

  # We use LCEL declarative syntax here.
  # Remember that langgraph graphs are also langchain runnables.
  target = example_to_state | app

  # Run evaluation
  async def main():
      experiment_results = await aevaluate(
          target,
          data="weather agent",
          evaluators=[correct, right_tool],
          max_concurrency=4,  # optional
          experiment_prefix="claude-sonnet-4-6-baseline",  # optional
          metadata={  # optional, used to populate model/prompt/tool columns in UI
              "models": "google_genai:gemini-3.5-flash",
              "tools": [{"name": "search", "description": "Call to surf the web."}],
          },
      )
      print(experiment_results)

  asyncio.run(main())
  ```
</Accordion>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/evaluate-graph.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# How to evaluate an LLM application
Source: https://docs.langchain.com/langsmith/evaluate-llm-application

This guide shows you how to run an evaluation on an LLM application using the LangSmith SDK.

<Info>
  [Evaluations](/langsmith/evaluation-concepts#evaluation-lifecycle) | [Evaluators](/langsmith/evaluation-concepts#evaluators) | [Datasets](/langsmith/evaluation-concepts#datasets)
</Info>

In this guide we'll go over how to evaluate an application using the [evaluate()](https://docs.smith.langchain.com/reference/python/evaluation/langsmith.evaluation._runner.evaluate) method in the LangSmith SDK.

<Check>
  For larger evaluation jobs in Python we recommend using [aevaluate()](https://docs.smith.langchain.com/reference/python/evaluation/langsmith.evaluation._arunner.aevaluate), the asynchronous version of [evaluate()](https://docs.smith.langchain.com/reference/python/evaluation/langsmith.evaluation._runner.evaluate). It is still worthwhile to read this guide first, as the two have identical interfaces, before reading the how-to guide on [running an evaluation asynchronously](/langsmith/evaluation-async).

  In JS/TS evaluate() is already asynchronous so no separate method is needed.

  It is also important to configure the `max_concurrency`/`maxConcurrency` arg when running large jobs. This parallelizes evaluation by effectively splitting the dataset across threads.
</Check>

## Define an application

First we need an application to evaluate. Let's create a simple toxicity classifier for this example.

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langsmith import traceable, wrappers
  from openai import OpenAI

  # Optionally wrap the OpenAI client to trace all model calls.
  oai_client = wrappers.wrap_openai(OpenAI())

  # Optionally add the 'traceable' decorator to trace the inputs/outputs of this function.
  @traceable
  def toxicity_classifier(inputs: dict) -> dict:
      instructions = (
        "Please review the user query below and determine if it contains any form of toxic behavior, "
        "such as insults, threats, or highly negative comments. Respond with 'Toxic' if it does "
        "and 'Not toxic' if it doesn't."
      )
      messages = [
          {"role": "system", "content": instructions},
          {"role": "user", "content": inputs["text"]},
      ]
      result = oai_client.chat.completions.create(
          messages=messages, model="gpt-5.4-mini", temperature=0
      )
      return {"class": result.choices[0].message.content}
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { OpenAI } from "openai";
  import { wrapOpenAI } from "langsmith/wrappers";
  import { traceable } from "langsmith/traceable";

  // Optionally wrap the OpenAI client to trace all model calls.
  const oaiClient = wrapOpenAI(new OpenAI());

  // Optionally add the 'traceable' wrapper to trace the inputs/outputs of this function.
  const toxicityClassifier = traceable(
    async (text: string) => {
      const result = await oaiClient.chat.completions.create({
        messages: [
          {
             role: "system",
            content: "Please review the user query below and determine if it contains any form of toxic behavior, such as insults, threats, or highly negative comments. Respond with 'Toxic' if it does, and 'Not toxic' if it doesn't.",
          },
          { role: "user", content: text },
        ],
        model: "gpt-5.4-mini",
        temperature: 0,
      });

      return result.choices[0].message.content;
    },
    { name: "toxicityClassifier" }
  );
  ```
</CodeGroup>

We've optionally enabled tracing to capture the inputs and outputs of each step in the pipeline. To understand how to annotate your code for tracing, please refer to [Custom instrumentation](/langsmith/annotate-code).

## Create or select a dataset

We need a [Dataset](/langsmith/evaluation-concepts#datasets) to evaluate our application on. Our dataset will contain labeled [examples](/langsmith/evaluation-concepts#examples) of toxic and non-toxic text.

Requires `langsmith>=0.3.13`

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langsmith import Client
  ls_client = Client()

  examples = [
    {
      "inputs": {"text": "Shut up, idiot"},
      "outputs": {"label": "Toxic"},
    },
    {
      "inputs": {"text": "You're a wonderful person"},
      "outputs": {"label": "Not toxic"},
    },
    {
      "inputs": {"text": "This is the worst thing ever"},
      "outputs": {"label": "Toxic"},
    },
    {
      "inputs": {"text": "I had a great day today"},
      "outputs": {"label": "Not toxic"},
    },
    {
      "inputs": {"text": "Nobody likes you"},
      "outputs": {"label": "Toxic"},
    },
    {
      "inputs": {"text": "This is unacceptable. I want to speak to the manager."},
      "outputs": {"label": "Not toxic"},
    },
  ]

  dataset = ls_client.create_dataset(dataset_name="Toxic Queries")
  ls_client.create_examples(
    dataset_id=dataset.id,
    examples=examples,
  )
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { Client } from "langsmith";

  const langsmith = new Client();

  // create a dataset
  const labeledTexts = [
    ["Shut up, idiot", "Toxic"],
    ["You're a wonderful person", "Not toxic"],
    ["This is the worst thing ever", "Toxic"],
    ["I had a great day today", "Not toxic"],
    ["Nobody likes you", "Toxic"],
    ["This is unacceptable. I want to speak to the manager.", "Not toxic"],
  ];

  const [inputs, outputs] = labeledTexts.reduce<
    [Array<{ input: string }>, Array<{ outputs: string }>]
  >(
    ([inputs, outputs], item) => [
      [...inputs, { input: item[0] }],
      [...outputs, { outputs: item[1] }],
    ],
    [[], []]
  );

  const datasetName = "Toxic Queries";
  const toxicDataset = await langsmith.createDataset(datasetName);
  await langsmith.createExamples({ inputs, outputs, datasetId: toxicDataset.id });
  ```
</CodeGroup>

For more details on datasets, refer to the [Manage datasets](/langsmith/manage-datasets) page.

## Define an evaluator

There are two main ways to define an evaluator.

### Locally in code

<Check>
  You can also check out LangChain's open source evaluation package [openevals](https://github.com/langchain-ai/openevals) for common prebuilt evaluators.
</Check>

[Evaluators](/langsmith/evaluation-concepts#evaluators) are functions for scoring your application's outputs. They take in the example inputs, actual outputs, and, when present, the reference outputs. Since we have labels for this task, our evaluator can directly check if the actual outputs match the reference outputs.

* Python: Requires `langsmith>=0.3.13`
* TypeScript: Requires `langsmith>=0.2.9`

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  def correct(inputs: dict, outputs: dict, reference_outputs: dict) -> bool:
      return outputs["class"] == reference_outputs["label"]
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import type { EvaluationResult } from "langsmith/evaluation";

  function correct({
    outputs,
    referenceOutputs,
  }: {
    outputs: Record<string, any>;
    referenceOutputs?: Record<string, any>;
  }): EvaluationResult {
    const score = outputs.output === referenceOutputs?.outputs;
    return { key: "correct", score };
  }
  ```
</CodeGroup>

### In LangSmith UI

You can also define an evaluator in the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-evaluate-llm-application). You can [create evaluators in the UI](/langsmith/llm-as-judge) under the **Evaluators** tab. These evaluators will be [automatically triggered with every new experiment](/langsmith/bind-evaluator-to-dataset).

## Run the evaluation

We'll use the [evaluate()](https://docs.smith.langchain.com/reference/python/evaluation/langsmith.evaluation._runner.evaluate) / [aevaluate()](https://docs.smith.langchain.com/reference/python/evaluation/langsmith.evaluation._arunner.aevaluate) methods to run the evaluation.

The key arguments are:

* a target function that takes an input dictionary and returns an output dictionary. The `example.inputs` field of each [Example](/langsmith/example-data-format) is what gets passed to the target function. In this case our `toxicity_classifier` is already set up to take in example inputs so we can use it directly.
* `data` - the name OR UUID of the LangSmith dataset to evaluate on, or an iterator of examples.
* `evaluators` - a list of evaluators to score the outputs of the function; dataset evaluators in the [Langsmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-evaluate-llm-application) will also automatically get triggered.
* `metadata` - an optional object to attach to the experiment. Pass `models`, `prompts`, and `tools` keys to populate the corresponding columns in the experiment table view.

Python: Requires `langsmith>=0.3.13`

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  # optional metadata, used to populate model/prompt/tool columns in UI
  EXPERIMENT_METADATA = {
      "models": [
          "openai:gpt-5.4-mini",
          {
              "id": ["langchain", "chat_models", "openai", "ChatOpenAI"],
              "lc": 1,
              "type": "constructor",
              "kwargs": {"model_name": "gpt-5.5", "temperature": 0.2},
          },
      ],
      "prompts": ["my-org/my-eval-prompt:abc12345"],
      "tools": [
          {
              "name": "web_search",
              "description": "Search the web for information",
              "parameters": {
                  "type": "object",
                  "properties": {"query": {"type": "string"}},
                  "required": ["query"],
              },
          },
      ],
  }

  # Can equivalently use the 'evaluate' function directly:
  # from langsmith import evaluate; evaluate(...)
  results = ls_client.evaluate(
      toxicity_classifier,
      data=dataset.name,
      evaluators=[correct],
      experiment_prefix="gpt-5.4-mini, baseline",  # optional, experiment name prefix
      description="Testing the baseline system.",  # optional, experiment description
      max_concurrency=4,  # optional, add concurrency
      metadata=EXPERIMENT_METADATA,  # optional, used to populate model/prompt/tool columns in UI
  )
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { evaluate } from "langsmith/evaluation";

  // optional metadata, used to populate model/prompt/tool columns in UI
  const EXPERIMENT_METADATA = {
    models: [
      "openai:gpt-5.4-mini",
      {
        id: ["langchain", "chat_models", "openai", "ChatOpenAI"],
        lc: 1,
        type: "constructor",
        kwargs: { model_name: "gpt-5.5", temperature: 0.2 },
      },
    ],
    prompts: ["my-org/my-eval-prompt:abc12345"],
    tools: [
      {
        name: "web_search",
        description: "Search the web for information",
        parameters: {
          type: "object",
          properties: { query: { type: "string" } },
          required: ["query"],
        },
      },
    ],
  };

  await evaluate((inputs) => toxicityClassifier(inputs["input"]), {
    data: datasetName,
    evaluators: [correct],
    experimentPrefix: "gpt-5.4-mini, baseline",  // optional, experiment name prefix
    maxConcurrency: 4, // optional, add concurrency
    metadata: EXPERIMENT_METADATA,  // optional, used to populate model/prompt/tool columns in UI
  });
  ```
</CodeGroup>

## Add metadata to an experiment

Metadata is a set of key-value pairs you can attach to an experiment to group and filter experiments in the experiments table. You can pass metadata when running an experiment via the `metadata` argument (see [Run the evaluation](#run-the-evaluation)), or add it afterwards directly in the LangSmith UI.

To open the **Edit Experiment** panel, hover over an experiment row in the experiments table and click the **Edit** pencil icon that appears at the right of the row.

<img alt="Experiments table with the edit pencil icon visible on a hovered row." />

<img alt="Experiments table with the edit pencil icon visible on a hovered row." />

The **Edit Experiment** panel lets you update the experiment name and description, and manage metadata key-value pairs. Click **+ Add Metadata** to add a new key-value pair, then click **Submit** in the top right to save your changes.

<img alt="Edit Experiment panel showing metadata key-value pairs and the Add Metadata button." />

<img alt="Edit Experiment panel showing metadata key-value pairs and the Add Metadata button." />

Once experiments are tagged with metadata, use the **Group by** control at the top of the experiments table to cluster experiments by any metadata field. The summary charts above the table update per group, showing average feedback scores, latency, and token usage for each configuration. This makes it easy to compare how different prompt versions, models, or other changes perform across the same dataset.

The reserved `models`, `prompts`, and `tools` keys automatically populate dedicated columns in the experiments table. Click a value in one of those columns to filter or group by it. For full details, see [Filter and group by models, prompts, and tools](/langsmith/analyze-an-experiment#filter-and-group-by-models-prompts-and-tools-in-the-experiments-tab-view).

## Explore the results

Each invocation of `evaluate()` creates an [experiment](/langsmith/evaluation-concepts#experiment) that you can view in the LangSmith UI or query via the SDK. See [Analyze an experiment](/langsmith/analyze-an-experiment) for more details.

Experiments run against a dataset are listed in the experiments table.

<img alt="Experiments table showing a list of experiments with columns for experiment name, description, dataset, feedback score, and more." />

<img alt="Experiments table showing a list of experiments with columns for experiment name, description, dataset, feedback score, and more." />

Click an experiment row to see scores for each example. Filter and sort by score to identify patterns in where your application performs well or poorly.

<img alt="Experiment view showing a table of examples with columns for input, output, reference output, feedback score, and more." />

<img alt="Experiment view showing a table of examples with columns for input, output, reference output, feedback score, and more." />

Click an example to open its details panel, which includes inputs, outputs, reference outputs, and any associated traces (if you've annotated your code for tracing).

<img alt="Experiment view details panel showing the inputs, outputs, reference outputs, and trace for a single example." />

<img alt="Experiment view details panel showing the inputs, outputs, reference outputs, and trace for a single example." />

## Reference code

<Accordion title="Click to see a consolidated code snippet">
  <CodeGroup>
    ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from langsmith import Client, traceable, wrappers
    from openai import OpenAI

    # Step 1. Define an application
    oai_client = wrappers.wrap_openai(OpenAI())

    @traceable
    def toxicity_classifier(inputs: dict) -> str:
        system = (
          "Please review the user query below and determine if it contains any form of toxic behavior, "
          "such as insults, threats, or highly negative comments. Respond with 'Toxic' if it does "
          "and 'Not toxic' if it doesn't."
        )
        messages = [
            {"role": "system", "content": system},
            {"role": "user", "content": inputs["text"]},
        ]
        result = oai_client.chat.completions.create(
            messages=messages, model="gpt-5.4-mini", temperature=0
        )
        return result.choices[0].message.content

    # Step 2. Create a dataset
    ls_client = Client()
    dataset = ls_client.create_dataset(dataset_name="Toxic Queries")
    examples = [
      {
        "inputs": {"text": "Shut up, idiot"},
        "outputs": {"label": "Toxic"},
      },
      {
        "inputs": {"text": "You're a wonderful person"},
        "outputs": {"label": "Not toxic"},
      },
      {
        "inputs": {"text": "This is the worst thing ever"},
        "outputs": {"label": "Toxic"},
      },
      {
        "inputs": {"text": "I had a great day today"},
        "outputs": {"label": "Not toxic"},
      },
      {
        "inputs": {"text": "Nobody likes you"},
        "outputs": {"label": "Toxic"},
      },
      {
        "inputs": {"text": "This is unacceptable. I want to speak to the manager."},
        "outputs": {"label": "Not toxic"},
      },
    ]
    ls_client.create_examples(
      dataset_id=dataset.id,
      examples=examples,
    )

    # Step 3. Define an evaluator
    def correct(inputs: dict, outputs: dict, reference_outputs: dict) -> bool:
        return outputs["output"] == reference_outputs["label"]

    # Step 4. Run the evaluation

    # optional metadata, used to populate model/prompt/tool columns in UI
    EXPERIMENT_METADATA = {
        "models": [
            "openai:gpt-5.4-mini",
            {
                "id": ["langchain", "chat_models", "openai", "ChatOpenAI"],
                "lc": 1,
                "type": "constructor",
                "kwargs": {"model_name": "gpt-5.5", "temperature": 0.2},
            },
        ],
        "prompts": ["my-org/my-eval-prompt:abc12345"],
        "tools": [
            {
                "name": "web_search",
                "description": "Search the web for information",
                "parameters": {
                    "type": "object",
                    "properties": {"query": {"type": "string"}},
                    "required": ["query"],
                },
            },
        ],
    }

    # Client.evaluate() and evaluate() behave the same.
    results = ls_client.evaluate(
        toxicity_classifier,
        data=dataset.name,
        evaluators=[correct],
        experiment_prefix="gpt-5.4-mini, simple",  # optional, experiment name prefix
        description="Testing the baseline system.",  # optional, experiment description
        max_concurrency=4,  # optional, add concurrency
        metadata=EXPERIMENT_METADATA,  # optional, used to populate model/prompt/tool columns in UI
    )
    ```

    ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { OpenAI } from "openai";
    import { Client } from "langsmith";
    import { evaluate, EvaluationResult } from "langsmith/evaluation";
    import type { Run, Example } from "langsmith/schemas";
    import { traceable } from "langsmith/traceable";
    import { wrapOpenAI } from "langsmith/wrappers";

    const oaiClient = wrapOpenAI(new OpenAI());

    const toxicityClassifier = traceable(
      async (text: string) => {
        const result = await oaiClient.chat.completions.create({
          messages: [
            {
              role: "system",
              content: "Please review the user query below and determine if it contains any form of toxic behavior, such as insults, threats, or highly negative comments. Respond with 'Toxic' if it does, and 'Not toxic' if it doesn't.",
            },
            { role: "user", content: text },
          ],
          model: "gpt-5.4-mini",
          temperature: 0,
        });
        return result.choices[0].message.content;
      },
      { name: "toxicityClassifier" }
    );

    const langsmith = new Client();

    // create a dataset
    const labeledTexts = [
      ["Shut up, idiot", "Toxic"],
      ["You're a wonderful person", "Not toxic"],
      ["This is the worst thing ever", "Toxic"],
      ["I had a great day today", "Not toxic"],
      ["Nobody likes you", "Toxic"],
      ["This is unacceptable. I want to speak to the manager.", "Not toxic"],
    ];

    const [inputs, outputs] = labeledTexts.reduce<
      [Array<{ input: string }>, Array<{ outputs: string }>]
    >(
      ([inputs, outputs], item) => [
        [...inputs, { input: item[0] }],
        [...outputs, { outputs: item[1] }],
      ],
      [[], []]
    );

    const datasetName = "Toxic Queries";
    const toxicDataset = await langsmith.createDataset(datasetName);
    await langsmith.createExamples({ inputs, outputs, datasetId: toxicDataset.id });

    // Row-level evaluator
    function correct({
      outputs,
      referenceOutputs,
    }: {
      outputs: Record<string, any>;
      referenceOutputs?: Record<string, any>;
    }): EvaluationResult {
      const score = outputs.output === referenceOutputs?.outputs;
      return { key: "correct", score };
    }

    // optional metadata, used to populate model/prompt/tool columns in UI
    const EXPERIMENT_METADATA = {
      models: [
        "openai:gpt-5.4-mini",
        {
          id: ["langchain", "chat_models", "openai", "ChatOpenAI"],
          lc: 1,
          type: "constructor",
          kwargs: { model_name: "gpt-5.5", temperature: 0.2 },
        },
      ],
      prompts: ["my-org/my-eval-prompt:abc12345"],
      tools: [
        {
          name: "web_search",
          description: "Search the web for information",
          parameters: {
            type: "object",
            properties: { query: { type: "string" } },
            required: ["query"],
          },
        },
      ],
    };

    await evaluate((inputs) => toxicityClassifier(inputs["input"]), {
      data: datasetName,
      evaluators: [correct],
      experimentPrefix: "gpt-5.4-mini, simple",  // optional, experiment name prefix
      maxConcurrency: 4, // optional, add concurrency
      metadata: EXPERIMENT_METADATA,  // optional, used to populate model/prompt/tool columns in UI
    });
    ```
  </CodeGroup>
</Accordion>

## Related

* [Run an evaluation asynchronously](/langsmith/evaluation-async)
* [Run an evaluation via the REST API](/langsmith/run-evals-api-only)
* [Run an evaluation from the Playground](/langsmith/run-evaluation-from-playground)

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/evaluate-llm-application.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
