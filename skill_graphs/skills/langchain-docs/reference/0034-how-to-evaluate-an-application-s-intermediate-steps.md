# How to evaluate an application's intermediate steps
Source: https://docs.langchain.com/langsmith/evaluate-on-intermediate-steps

While, in many scenarios, it is sufficient to evaluate the final output of your task, in some cases you might want to evaluate the intermediate steps of your pipeline.

For example, for retrieval-augmented generation (RAG), you might want to

1. Evaluate the retrieval step to ensure that the correct documents are retrieved w\.r.t the input query.
2. Evaluate the generation step to ensure that the correct answer is generated w\.r.t the retrieved documents.

In this guide, we will use a simple, fully-custom evaluator for evaluating criteria 1 and an LLM-based evaluator for evaluating criteria 2 to highlight both scenarios.

In order to evaluate the intermediate steps of your pipeline, your evaluator function should traverse and process the `run`/`rootRun` argument, which is a `Run` object that contains the intermediate steps of your pipeline.

## 1. Define your LLM pipeline

The below RAG pipeline consists of 1) generating a Wikipedia query given the input question, 2) retrieving relevant documents from Wikipedia, and 3) generating an answer given the retrieved documents.

<CodeGroup>
  ```bash Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install -U langsmith langchain[openai] wikipedia
  ```

  ```bash TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  yarn add langsmith langchain @langchain/openai wikipedia
  ```
</CodeGroup>

Requires `langsmith>=0.3.13`

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import wikipedia as wp
  from openai import OpenAI
  from langsmith import traceable, wrappers

  oai_client = wrappers.wrap_openai(OpenAI())

  @traceable
  def generate_wiki_search(question: str) -> str:
      """Generate the query to search in wikipedia."""
      instructions = (
          "Generate a search query to pass into wikipedia to answer the user's question. "
          "Return only the search query and nothing more. "
          "This will passed in directly to the wikipedia search engine."
      )
      messages = [
          {"role": "system", "content": instructions},
          {"role": "user", "content": question}
      ]
      result = oai_client.chat.completions.create(
          messages=messages,
          model="gpt-5.4-mini",
          temperature=0,
      )
      return result.choices[0].message.content

  @traceable(run_type="retriever")
  def retrieve(query: str) -> list:
      """Get up to two search wikipedia results."""
      results = []
      for term in wp.search(query, results = 10):
          try:
              page = wp.page(term, auto_suggest=False)
              results.append({
                  "page_content": page.summary,
                  "type": "Document",
                  "metadata": {"url": page.url}
              })
          except wp.DisambiguationError:
              pass
          if len(results) >= 2:
              return results

  @traceable
  def generate_answer(question: str, context: str) -> str:
      """Answer the question based on the retrieved information."""
      instructions = f"Answer the user's question based ONLY on the content below:\n\n{context}"
      messages = [
          {"role": "system", "content": instructions},
          {"role": "user", "content": question}
      ]
      result = oai_client.chat.completions.create(
          messages=messages,
          model="gpt-5.4-mini",
          temperature=0
      )
      return result.choices[0].message.content

  @traceable
  def qa_pipeline(question: str) -> str:
      """The full pipeline."""
      query = generate_wiki_search(question)
      context = "\n\n".join([doc["page_content"] for doc in retrieve(query)])
      return generate_answer(question, context)
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import OpenAI from "openai";
  import wiki from "wikipedia";
  import { Client } from "langsmith";
  import { traceable } from "langsmith/traceable";
  import { wrapOpenAI } from "langsmith/wrappers";

  const openai = wrapOpenAI(new OpenAI());

  const generateWikiSearch = traceable(
    async (input: { question: string }) => {
      const messages = [
        {
          role: "system" as const,
          content:
            "Generate a search query to pass into Wikipedia to answer the user's question. Return only the search query and nothing more. This will be passed in directly to the Wikipedia search engine.",
        },
        { role: "user" as const, content: input.question },
      ];
      const chatCompletion = await openai.chat.completions.create({
        model: "gpt-5.4-mini",
        messages: messages,
        temperature: 0,
      });
      return chatCompletion.choices[0].message.content ?? "";
    },
    { name: "generateWikiSearch" }
  );

  const retrieve = traceable(
    async (input: { query: string; numDocuments: number }) => {
      const { results } = await wiki.search(input.query, { limit: 10 });
      const finalResults: Array<{
        page_content: string;
        type: "Document";
        metadata: { url: string };
      }> = [];
      for (const result of results) {
        if (finalResults.length >= input.numDocuments) {
          // Just return the top 2 pages for now
          break;
        }
        const page = await wiki.page(result.title, { autoSuggest: false });
        const summary = await page.summary();
        finalResults.push({
          page_content: summary.extract,
          type: "Document",
          metadata: { url: page.fullurl },
        });
      }
      return finalResults;
    },
    { name: "retrieve", run_type: "retriever" }
  );

  const generateAnswer = traceable(
    async (input: { question: string; context: string }) => {
      const messages = [
        {
          role: "system" as const,
          content: `Answer the user's question based only on the content below:\n\n${input.context}`,
        },
        { role: "user" as const, content: input.question },
      ];
      const chatCompletion = await openai.chat.completions.create({
        model: "gpt-5.4-mini",
        messages: messages,
        temperature: 0,
      });
      return chatCompletion.choices[0].message.content ?? "";
    },
    { name: "generateAnswer" }
  );

  const ragPipeline = traceable(
    async ({ question }: { question: string }, numDocuments: number = 2) => {
      const query = await generateWikiSearch({ question });
      const retrieverResults = await retrieve({ query, numDocuments });
      const context = retrieverResults
        .map((result) => result.page_content)
        .join("\n\n");
      const answer = await generateAnswer({ question, context });
      return answer;
    },
    { name: "ragPipeline" }
  );
  ```
</CodeGroup>

This pipeline will produce a trace that looks something like: <img alt="evaluation_intermediate_trace.png" />

## 2. Create a dataset and examples to evaluate the pipeline

We are building a very simple dataset with a couple of examples to evaluate the pipeline.

Requires `langsmith>=0.3.13`

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langsmith import Client

  ls_client = Client()
  dataset_name = "Wikipedia RAG"

  if not ls_client.has_dataset(dataset_name=dataset_name):
      dataset = ls_client.create_dataset(dataset_name=dataset_name)
      examples = [
        {"inputs": {"question": "What is LangChain?"}},
        {"inputs": {"question": "What is LangSmith?"}},
      ]
      ls_client.create_examples(
        dataset_id=dataset.id,
        examples=examples,
      )
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { Client } from "langsmith";

  const client = new Client();
  const examples = [
    [
      "What is LangChain?",
      "LangChain is an open-source framework for building applications using large language models.",
    ],
    [
      "What is LangSmith?",
      "LangSmith is an observability and evaluation tool for LLM products, built by LangChain Inc.",
    ],
  ];
  const datasetName = "Wikipedia RAG";
  const inputs = examples.map(([input, _]) => ({ input }));
  const outputs = examples.map(([_, expected]) => ({ expected }));
  const dataset = await client.createDataset(datasetName);
  await client.createExamples({ datasetId: dataset.id, inputs, outputs });
  ```
</CodeGroup>

## 3. Define your custom evaluators

As mentioned above, we will define two evaluators: one that evaluates the relevance of the retrieved documents w\.r.t the input query and another that evaluates the hallucination of the generated answer w\.r.t the retrieved documents. We will be using LangChain LLM wrappers, along with [`with_structured_output`](https://reference.langchain.com/python/langchain-core/language_models/chat_models/BaseChatModel/with_structured_output) to define the evaluator for hallucination.

The key here is that the evaluator function should traverse the `run` / `rootRun` argument to access the intermediate steps of the pipeline. The evaluator can then process the inputs and outputs of the intermediate steps to evaluate according to the desired criteria.

Example uses `langchain` for convenience, this is not required.

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langchain.chat_models import init_chat_model
  from langsmith.schemas import Run
  from pydantic import BaseModel, Field

  def document_relevance(run: Run) -> bool:
      """Checks if retriever input exists in the retrieved docs."""
      qa_pipeline_run = next(
          r for run in run.child_runs if r.name == "qa_pipeline"
      )
      retrieve_run = next(
          r for run in qa_pipeline_run.child_runs if r.name == "retrieve"
      )
      page_contents = "\n\n".join(
          doc["page_content"] for doc in retrieve_run.outputs["output"]
      )
      return retrieve_run.inputs["query"] in page_contents

  # Data model
  class GradeHallucinations(BaseModel):
      """Binary score for hallucination present in generation answer."""
      is_grounded: bool = Field(..., description="True if the answer is grounded in the facts, False otherwise.")

  # LLM with structured output for grading hallucinations
  # For more see: https://docs.langchain.com/oss/python/langchain/structured-output
  grader_llm= init_chat_model("gpt-5.4-mini", temperature=0).with_structured_output(
      GradeHallucinations,
      method="json_schema",
      strict=True,
  )

  def no_hallucination(run: Run) -> bool:
      """Check if the answer is grounded in the documents.
      Return True if there is no hallucination, False otherwise.
      """
      # Get documents and answer
      qa_pipeline_run = next(
          r for r in run.child_runs if r.name == "qa_pipeline"
      )
      retrieve_run = next(
          r for r in qa_pipeline_run.child_runs if r.name == "retrieve"
      )
      retrieved_content = "\n\n".join(
          doc["page_content"] for doc in retrieve_run.outputs["output"]
      )

      # Construct prompt
      instructions = (
          "You are a grader assessing whether an LLM generation is grounded in / "
          "supported by a set of retrieved facts. Give a binary score 1 or 0, "
          "where 1 means that the answer is grounded in / supported by the set of facts."
      )
      messages = [
          {"role": "system", "content": instructions},
          {"role": "user", "content": f"Set of facts:\n{retrieved_content}\n\nLLM generation: {run.outputs['answer']}"},
      ]
      grade = grader_llm.invoke(messages)
      return grade.is_grounded
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { EvaluationResult } from "langsmith/evaluation";
  import { Run, Example } from "langsmith/schemas";
  import { ChatPromptTemplate } from "@langchain/core/prompts";
  import { ChatOpenAI } from "@langchain/openai";
  import { z } from "zod";

  function findNestedRun(run: Run, search: (run: Run) => boolean): Run | null {
    const queue: Run[] = [run];
    while (queue.length > 0) {
      const currentRun = queue.shift()!;
      if (search(currentRun)) return currentRun;
      queue.push(...currentRun.child_runs);
    }
    return null;
  }

  // A very simple evaluator that checks to see if the input of the retrieval step exists
  // in the retrieved docs.
  function documentRelevance(rootRun: Run, example: Example): EvaluationResult {
    const retrieveRun = findNestedRun(rootRun, (run) => run.name === "retrieve");
    const docs: Array<{ page_content: string }> | undefined =
      retrieveRun.outputs?.outputs;
    const pageContents = docs?.map((doc) => doc.page_content).join("\n\n");
    const score = pageContents.includes(retrieveRun.inputs?.query);
    return { key: "simple_document_relevance", score };
  }

  async function hallucination(
    rootRun: Run,
    example: Example
  ): Promise<EvaluationResult> {
    const rag = findNestedRun(rootRun, (run) => run.name === "ragPipeline");
    const retrieve = findNestedRun(rootRun, (run) => run.name === "retrieve");
    const docs: Array<{ page_content: string }> | undefined =
      retrieve.outputs?.outputs;
    const documents = docs?.map((doc) => doc.page_content).join("\n\n");

    const prompt = ChatPromptTemplate.fromMessages<{
      documents: string;
      generation: string;
    }>([
      [
        "system",
        [
          `You are a grader assessing whether an LLM generation is grounded in / supported by a set of retrieved facts. \n`,
          `Give a binary score 1 or 0, where 1 means that the answer is grounded in / supported by the set of facts.`,
        ].join("\n"),
      ],
      [
        "human",
        "Set of facts: \n\n {documents} \n\n LLM generation: {generation}",
      ],
    ]);

    const llm = new ChatOpenAI({
      model: "gpt-5.4-mini",
      temperature: 0,
    }).withStructuredOutput(
      z
        .object({
          binary_score: z
            .number()
            .describe("Answer is grounded in the facts, 1 or 0"),
        })
        .describe("Binary score for hallucination present in generation answer.")
    );

    const grader = prompt.pipe(llm);
    const score = await grader.invoke({
      documents,
      generation: rag.outputs?.outputs,
    });
    return { key: "answer_hallucination", score: score.binary_score };
  }
  ```
</CodeGroup>

## 4. Evaluate the pipeline

Finally, we'll run `evaluate` with the custom evaluators defined above.

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  def qa_wrapper(inputs: dict) -> dict:
    """Wrap the qa_pipeline so it can accept the Example.inputs dict as input."""
    return {"answer": qa_pipeline(inputs["question"])}

  experiment_results = ls_client.evaluate(
      qa_wrapper,
      data=dataset_name,
      evaluators=[document_relevance, no_hallucination],
      experiment_prefix="rag-wiki-oai"
  )
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { evaluate } from "langsmith/evaluation";

  await evaluate((inputs) => ragPipeline({ question: inputs.input }), {
    data: datasetName,
    evaluators: [hallucination, documentRelevance],
    experimentPrefix: "rag-wiki-oai",
  });
  ```
</CodeGroup>

The experiment will contain the results of the evaluation, including the scores and comments from the evaluators: <img alt="evaluation_intermediate_experiment.png" />

## Related

* [Evaluate a `langgraph` graph](/langsmith/evaluate-on-intermediate-steps)

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/evaluate-on-intermediate-steps.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# How to run a pairwise evaluation
Source: https://docs.langchain.com/langsmith/evaluate-pairwise

<Info>
  Concept: [Pairwise evaluations](/langsmith/evaluation-concepts#pairwise)
</Info>

LangSmith supports evaluating **existing** experiments in a comparative manner. Instead of evaluating one output at a time, you can score the output from multiple experiments against each other. In this guide, you'll use [`evaluate()`](https://docs.smith.langchain.com/reference/python/evaluation/langsmith.evaluation._runner.evaluate) with two existing experiments to [define an evaluator](#define-a-pairwise-evaluator) and [run a pairwise evaluation](#run-a-pairwise-evaluation). Finally, you'll use the LangSmith UI to [view the pairwise experiments](#view-pairwise-experiments).

## Prerequisites

* If you haven't already created experiments to compare, check out the [quick start](/langsmith/evaluation-quickstart) or the [how-to guide](/langsmith/evaluate-llm-application) to get started with evaluations.
* This guide requires `langsmith` Python version `>=0.2.0` or JS version `>=0.2.9`.

<Info>
  You can also use [`evaluate_comparative()`](https://docs.smith.langchain.com/reference/python/evaluation/langsmith.evaluation._runner.evaluate_comparative) with more than two existing experiments.
</Info>

## `evaluate()` comparative args

At its simplest, `evaluate` / `aevaluate` function takes the following arguments:

| Argument     | Description                                                                                                                        |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------- |
| `target`     | A list of the two **existing experiments** you would like to evaluate against each other. These can be uuids or experiment names.  |
| `evaluators` | A list of the pairwise evaluators that you would like to attach to this evaluation. See the section below for how to define these. |

Along with these, you can also pass in the following optional args:

| Argument                                 | Description                                                                                                                                                                                                                                                                                                                                                                    |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `randomize_order` / `randomizeOrder`     | An optional boolean indicating whether the order of the outputs should be randomized for each evaluation. This is a strategy for minimizing positional bias in your prompt: often, the LLM will be biased towards one of the responses based on the order. This should mainly be addressed via prompt engineering, but this is another optional mitigation. Defaults to False. |
| `experiment_prefix` / `experimentPrefix` | A prefix to be attached to the beginning of the pairwise experiment name. Defaults to None.                                                                                                                                                                                                                                                                                    |
| `description`                            | A description of the pairwise experiment. Defaults to None.                                                                                                                                                                                                                                                                                                                    |
| `max_concurrency` / `maxConcurrency`     | The maximum number of concurrent evaluations to run. Defaults to 5.                                                                                                                                                                                                                                                                                                            |
| `client`                                 | The LangSmith client to use. Defaults to None.                                                                                                                                                                                                                                                                                                                                 |
| `metadata`                               | Metadata to attach to your pairwise experiment. Defaults to None.                                                                                                                                                                                                                                                                                                              |
| `load_nested` / `loadNested`             | Whether to load all child runs for the experiment. When False, only the root trace will be passed to your evaluator. Defaults to False.                                                                                                                                                                                                                                        |

## Define a pairwise evaluator

Pairwise evaluators are just functions with an expected signature.

### Evaluator args

Custom evaluator functions must have specific argument names. They can take any subset of the following arguments:

* `inputs: dict`: A dictionary of the inputs corresponding to a single example in a dataset.
* `outputs: list[dict]`: A two-item list of the dict outputs produced by each experiment on the given inputs.
* `reference_outputs` / `referenceOutputs: dict`: A dictionary of the reference outputs associated with the example, if available.
* `runs: list[Run]`: A two-item list of the full [Run](/langsmith/run-data-format) objects generated by the two experiments on the given example. Use this if you need access to intermediate steps or metadata about each run.
* `example: Example`: The full dataset [Example](/langsmith/example-data-format), including the example inputs, outputs (if available), and metadata (if available).

For most use cases you'll only need `inputs`, `outputs`, and `reference_outputs` / `referenceOutputs`. `runs` and `example` are useful only if you need some extra trace or example metadata outside of the actual inputs and outputs of the application.

### Evaluator output

Custom evaluators are expected to return one of the following types:

Python and JS/TS

* `dict`: dictionary with keys:

  * `key`, which represents the feedback key that will be logged
  * `scores`, which is a mapping from run ID to score for that run.
  * `comment`, which is a string. Most commonly used for model reasoning.

Currently Python only

* `list[int | float | bool]`: a two-item list of scores. The list is assumed to have the same order as the `runs` / `outputs` evaluator args. The evaluator function name is used for the feedback key.

Note that you should choose a feedback key that is distinct from standard feedbacks on your run. We recommend prefixing pairwise feedback keys with `pairwise_` or `ranked_`.

## Run a pairwise evaluation

The following example uses [a prompt](https://smith.langchain.com/hub/langchain-ai/pairwise-evaluation-2) which asks the LLM to decide which is better between two AI assistant responses. It uses structured output to parse the AI's response: 0, 1, or 2.

<Info>
  In the Python example below, we are pulling [this structured prompt](https://smith.langchain.com/hub/langchain-ai/pairwise-evaluation-2) from the [LangChain Hub](/langsmith/manage-prompts#public-prompt-hub) and using it with a LangChain chat model wrapper.

  **Usage of LangChain is totally optional.** To illustrate this point, the TypeScript example uses the OpenAI SDK directly.
</Info>

* Python: Requires `langsmith>=0.2.0`
* TypeScript: Requires `langsmith>=0.2.9`

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langchain_classic import hub
  from langchain.chat_models import init_chat_model
  from langsmith import evaluate

  # See the prompt: https://smith.langchain.com/hub/langchain-ai/pairwise-evaluation-2
  prompt = hub.pull("langchain-ai/pairwise-evaluation-2")
  model = init_chat_model("gpt-5.5")
  chain = prompt | model

  def ranked_preference(inputs: dict, outputs: list[dict]) -> list:
      # Assumes example inputs have a 'question' key and experiment
      # outputs have an 'answer' key.
      response = chain.invoke({
          "question": inputs["question"],
          "answer_a": outputs[0].get("answer", "N/A"),
          "answer_b": outputs[1].get("answer", "N/A"),
      })
      if response["Preference"] == 1:
          scores = [1, 0]
      elif response["Preference"] == 2:
          scores = [0, 1]
      else:
          scores = [0, 0]
      return scores

  evaluate(
      ("experiment-1", "experiment-2"),  # Replace with the names/IDs of your experiments
      evaluators=[ranked_preference],
      randomize_order=True,
      max_concurrency=4,
  )
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { evaluate} from "langsmith/evaluation";
  import { Run } from "langsmith/schemas";
  import { wrapOpenAI } from "langsmith/wrappers";
  import OpenAI from "openai";
  import { z } from "zod";

  const openai = wrapOpenAI(new OpenAI());

  async function rankedPreference({
    inputs,
    runs,
  }: {
    inputs: Record<string, any>;
    runs: Run[];
  }) {
    const scores: Record<string, number> = {};
    const [runA, runB] = runs;
    if (!runA || !runB) throw new Error("Expected at least two runs");

    const payload = {
      question: inputs.question,
      answer_a: runA?.outputs?.output ?? "N/A",
      answer_b: runB?.outputs?.output ?? "N/A",
    };

    const output = await openai.chat.completions.create({
      model: "gpt-4-turbo",
      messages: [
        {
          role: "system",
          content: [
            "Please act as an impartial judge and evaluate the quality of the responses provided by two AI assistants to the user question displayed below.",
            "You should choose the assistant that follows the user's instructions and answers the user's question better.",
            "Your evaluation should consider factors such as the helpfulness, relevance, accuracy, depth, creativity, and level of detail of their responses.",
            "Begin your evaluation by comparing the two responses and provide a short explanation.",
            "Avoid any position biases and ensure that the order in which the responses were presented does not influence your decision.",
            "Do not allow the length of the responses to influence your evaluation. Do not favor certain names of the assistants. Be as objective as possible.",
          ].join(" "),
        },
        {
          role: "user",
          content: [
            `[User Question] ${payload.question}`,
            `[The Start of Assistant A's Answer] ${payload.answer_a} [The End of Assistant A's Answer]`,
            `The Start of Assistant B's Answer] ${payload.answer_b} [The End of Assistant B's Answer]`,
          ].join("\n\n"),
        },
      ],
      tool_choice: {
        type: "function",
        function: { name: "Score" },
      },
      tools: [
        {
          type: "function",
          function: {
            name: "Score",
            description: [
              `After providing your explanation, output your final verdict by strictly following this format:`,
              `Output "1" if Assistant A answer is better based upon the factors above.`,
              `Output "2" if Assistant B answer is better based upon the factors above.`,
              `Output "0" if it is a tie.`,
            ].join(" "),
            parameters: {
              type: "object",
              properties: {
                Preference: {
                  type: "integer",
                  description: "Which assistant answer is preferred?",
                },
              },
            },
          },
        },
      ],
    });

    const { Preference } = z
      .object({ Preference: z.number() })
      .parse(
        JSON.parse(output.choices[0].message.tool_calls[0].function.arguments)
      );

    if (Preference === 1) {
      scores[runA.id] = 1;
      scores[runB.id] = 0;
    } else if (Preference === 2) {
      scores[runA.id] = 0;
      scores[runB.id] = 1;
    } else {
      scores[runA.id] = 0;
      scores[runB.id] = 0;
    }

    return { key: "ranked_preference", scores };
  }

  await evaluate(["earnest-name-40", "reflecting-pump-91"], {
    evaluators: [rankedPreference],
  });
  ```
</CodeGroup>

## View pairwise experiments

Navigate to the "Pairwise Experiments" tab from the dataset page:

<img alt="Pairwise Experiments Tab" />

Click on a pairwise experiment that you would like to inspect, and you will be brought to the Comparison View:

<img alt="Pairwise Comparison View" />

You may filter to runs where the first experiment was better or vice versa by clicking the thumbs up/thumbs down buttons in the table header:

<img alt="Pairwise Filtering" />

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/evaluate-pairwise.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
