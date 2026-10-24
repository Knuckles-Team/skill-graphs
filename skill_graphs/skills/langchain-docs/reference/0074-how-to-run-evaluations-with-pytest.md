# How to run evaluations with pytest
Source: https://docs.langchain.com/langsmith/pytest

The LangSmith pytest plugin lets Python developers define their datasets and evaluations as pytest test cases.

Compared to the standard evaluation flow, this is useful when:

* **Each example requires different evaluation logic**: Standard evaluation flows assume consistent application and evaluator execution across all dataset examples. For more complex systems or comprehensive evaluations, specific system subsets may require evaluation with particular input types and metrics. These heterogeneous evaluations are simpler to write as distinct test case suites that track together.
* **You want to assert binary expectations**: Track assertions in LangSmith and raise assertion errors locally (e.g. in CI pipelines). Testing tools help when both evaluating system outputs and asserting basic properties about them.
* **You want pytest-like terminal outputs**: Get familiar pytest output formatting
* **You already use pytest to test your app**: Add LangSmith tracking to existing pytest workflows

<Info>
  The JS/TS SDK has an analogous [Vitest/Jest integration](/langsmith/vitest-jest).
</Info>

## Installation

This functionality requires Python SDK version `langsmith>=0.3.4`.

For extra features like [rich terminal outputs](#rich-outputs) and [test caching](#caching) install:

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install -U "langsmith[pytest]"
  ```

  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv add "langsmith[pytest]"
  ```
</CodeGroup>

## Define and run tests

The pytest integration lets you define datasets and evaluators as test cases.

To track a test in LangSmith add the `@pytest.mark.langsmith` decorator. Every decorated test case will be synced to a dataset example. When you run the test suite, the dataset will be updated and a new experiment will be created with one result for each test case.

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  ###################### my_app/main.py ######################
  import openai
  from langsmith import traceable, wrappers

  oai_client = wrappers.wrap_openai(openai.OpenAI())

  @traceable
  def generate_sql(user_query: str) -> str:
      result = oai_client.chat.completions.create(
          model="gpt-5.4-mini",
          messages=[
              {"role": "system", "content": "Convert the user query to a SQL query."},
              {"role": "user", "content": user_query},
          ],
      )
      return result.choices[0].message.content

  ###################### tests/test_my_app.py ######################
  import pytest
  from langsmith import testing as t

  def is_valid_sql(query: str) -> bool:
      """Return True if the query is valid SQL."""
      return True  # Dummy implementation

  @pytest.mark.langsmith  # <-- Mark as a LangSmith test case
  def test_sql_generation_select_all() -> None:
      user_query = "Get all users from the customers table"
      t.log_inputs({"user_query": user_query})  # <-- Log example inputs, optional
      expected = "SELECT * FROM customers;"
      t.log_reference_outputs({"sql": expected})  # <-- Log example reference outputs, optional

      sql = generate_sql(user_query)
      t.log_outputs({"sql": sql})  # <-- Log run outputs, optional

      t.log_feedback(key="valid_sql", score=is_valid_sql(sql))  # <-- Log feedback, optional
      assert sql == expected  # <-- Test pass/fail status automatically logged to LangSmith under 'pass' feedback key
  ```
</CodeGroup>

When you run this test it will have a default `pass` boolean feedback key based on the test case passing / failing. It will also track any inputs, outputs, and reference (expected) outputs that you log.

Use `pytest` as you normally would to run the tests:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
pytest tests/
```

In most cases we recommend setting a test suite name:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
LANGSMITH_TEST_SUITE='SQL app tests' pytest tests/
```

Each time you run this test suite, LangSmith:

* creates a [dataset](/langsmith/evaluation-concepts#datasets) for each test file. If a dataset for this test file already exists it will be updated
* creates an [experiment](/langsmith/evaluation-concepts#experiment) in each created/updated dataset
* creates an experiment row for each test case, with the inputs, outputs, reference outputs and feedback you've logged
* collects the pass/fail rate under the `pass` feedback key for each test case

Here's what a test suite dataset looks like:

<img alt="Dataset" />

And what an experiment against that test suite looks like:

<img alt="Experiment" />

## Log inputs, outputs, and reference outputs

Every time we run a test we're syncing it to a dataset example and tracing it as a run. There's a few different ways that we can trace the example inputs and reference outputs and the run outputs. The simplest is to use the `log_inputs`, `log_outputs`, and `log_reference_outputs` methods. You can run these any time in a test to update the example and run for that test:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import pytest
from langsmith import testing as t

@pytest.mark.langsmith
def test_foo() -> None:
    t.log_inputs({"a": 1, "b": 2})
    t.log_reference_outputs({"foo": "bar"})
    t.log_outputs({"foo": "baz"})
    assert True
```

Running this test will create/update an example with name "test\_foo", inputs `{"a": 1, "b": 2}`, reference outputs `{"foo": "bar"}` and trace a run with outputs `{"foo": "baz"}`.

**NOTE**: If you run `log_inputs`, `log_outputs`, or `log_reference_outputs` twice, the previous values will be overwritten.

Another way to define example inputs and reference outputs is via pytest fixtures/parametrizations. By default any arguments to your test function will be logged as inputs on the corresponding example. If certain arguments are meant to represent reference outputs, you can specify that they should be logged as such using `@pytest.mark.langsmith(output_keys=["name_of_ref_output_arg"])`:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import pytest

@pytest.fixture
def c() -> int:
    return 5

@pytest.fixture
def d() -> int:
    return 6

@pytest.mark.langsmith(output_keys=["d"])
def test_cd(c: int, d: int) -> None:
    result = 2 * c
    t.log_outputs({"d": result})  # Log run outputs
    assert result == d
```

This will create/sync an example with name "test\_cd", inputs `{"c": 5}` and reference outputs `{"d": 6}`, and run output `{"d": 10}`.

## Log feedback

By default LangSmith collects the pass/fail rate under the `pass` feedback key for each test case. You can add additional feedback with `log_feedback`.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import openai
import pytest
from langsmith import wrappers
from langsmith import testing as t

oai_client = wrappers.wrap_openai(openai.OpenAI())

@pytest.mark.langsmith
def test_offtopic_input() -> None:
    user_query = "what's up"
    t.log_inputs({"user_query": user_query})

    sql = generate_sql(user_query)
    t.log_outputs({"sql": sql})

    expected = "Sorry that is not a valid query."
    t.log_reference_outputs({"sql": expected})

    # Use this context manager to trace any steps used for generating evaluation
    # feedback separately from the main application logic
    with t.trace_feedback():
        instructions = (
            "Return 1 if the ACTUAL and EXPECTED answers are semantically equivalent, "
            "otherwise return 0. Return only 0 or 1 and nothing else."
        )

        grade = oai_client.chat.completions.create(
            model="gpt-5.4-mini",
            messages=[
                {"role": "system", "content": instructions},
                {"role": "user", "content": f"ACTUAL: {sql}\nEXPECTED: {expected}"},
            ],
        )
        score = float(grade.choices[0].message.content)
        t.log_feedback(key="correct", score=score)

    assert score
```

Note the use of the `trace_feedback()` context manager. This makes it so that the LLM-as-judge call is traced separately from the rest of the test case. Instead of showing up in the main test case run it will instead show up in the trace for the `correct` feedback key.

**NOTE**: Make sure that the `log_feedback` call associated with the feedback trace occurs inside the `trace_feedback` context. This way we'll be able to associate the feedback with the trace, and when seeing the feedback in the UI you'll be able to click on it to see the trace that generated it.

## Trace intermediate calls

LangSmith will automatically trace any traceable intermediate calls that happen in the course of test case execution.

## Grouping tests into a test suite

By default, all tests within a given file will be grouped as a single "test suite" with a corresponding dataset. You can configure which test suite a test belongs to by passing the `test_suite_name` parameter to `@pytest.mark.langsmith` for case-by-case grouping, or you can set the `LANGSMITH_TEST_SUITE` env var to group all tests from an execution into a single test suite:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
LANGSMITH_TEST_SUITE="SQL app tests" pytest tests/
```

We generally recommend setting `LANGSMITH_TEST_SUITE` to get a consolidated view of all of your results.

## Naming experiments

You can name an experiment using the `LANGSMITH_EXPERIMENT` env var:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
LANGSMITH_TEST_SUITE="SQL app tests" LANGSMITH_EXPERIMENT="baseline" pytest tests/
```

## Experiment metadata

You can attach custom metadata to the experiment (project) created by each test run. This is useful for tracking which model, prompt version, or environment was used for a given experiment.

**Option 1: Fixture (recommended)**

Define a session-scoped fixture in your `conftest.py`:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# conftest.py
import os
import pytest

@pytest.fixture(scope="session")
def langsmith_experiment_metadata():
    return {
        "model": "gpt-4o",
        "prompt_version": "v2.3",
        "environment": os.environ.get("ENV", "local"),
    }
```

The fixture is dynamic (can read env vars, call functions, etc.) and follows pytest's `conftest.py` hierarchy so it can be scoped per directory.

**Option 2: Environment variable**

Set `LANGSMITH_EXPERIMENT_METADATA` to a JSON string. This is useful in CI/CD pipelines where you don't want to modify code:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
LANGSMITH_EXPERIMENT_METADATA='{"model":"gpt-4o","env":"staging"}' pytest tests/
```

If both the fixture and the env var are set, the fixture takes precedence. System-managed metadata keys (like `revision_id` and git info) always take precedence over user-supplied keys.

<Note>
  This feature requires `langsmith>=0.7.13`.
</Note>

## Caching

LLMs on every commit in CI can get expensive. To save time and resources, LangSmith lets you cache HTTP requests to disk. To enable caching, install with `langsmith[pytest]` and set an env var: `LANGSMITH_TEST_CACHE=/my/cache/path`:

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install -U "langsmith[pytest]"
  LANGSMITH_TEST_CACHE=tests/cassettes pytest tests/my_llm_tests
  ```

  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv add "langsmith[pytest]"
  LANGSMITH_TEST_CACHE=tests/cassettes pytest tests/my_llm_tests
  ```
</CodeGroup>

All requests will be cached to `tests/cassettes` and loaded from there on subsequent runs. If you check this in to your repository, your CI will be able to use the cache as well.

In `langsmith>=0.4.10`, you may selectively enable caching for requests to individual URLs or hostnames like this:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
@pytest.mark.langsmith(cached_hosts=["api.openai.com", "https://api.anthropic.com"])
def my_test():
    ...
```

## pytest features

`@pytest.mark.langsmith` is designed to stay out of your way and works well with familiar `pytest` features.

### Parametrize with `pytest.mark.parametrize`

You can use the `parametrize` decorator as before. This will create a new test case for each parametrized instance of the test.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
@pytest.mark.langsmith(output_keys=["expected_sql"])
@pytest.mark.parametrize(
    "user_query, expected_sql",
    [
        ("Get all users from the customers table", "SELECT * FROM customers"),
        ("Get all users from the orders table", "SELECT * FROM orders"),
    ],
)
def test_sql_generation_parametrized(user_query, expected_sql):
    sql = generate_sql(user_query)
    assert sql == expected_sql
```

**Note:** as the parametrized list grows, you may consider using `evaluate()` instead. This parallelizes the evaluation and makes it easier to control individual experiments and the corresponding dataset.

### Parallelize with `pytest-xdist`

You can use [pytest-xdist](https://pytest-xdist.readthedocs.io/en/stable/) as you normally would to parallelize test execution:

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install -U pytest-xdist
  pytest -n auto tests
  ```

  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv add pytest-xdist
  pytest -n auto tests
  ```
</CodeGroup>

### Async tests with `pytest-asyncio`

`@pytest.mark.langsmith` works with sync or async tests, so you can run async tests exactly as before.

### Watch mode with `pytest-watch`

Use watch mode to quickly iterate on your tests. We *highly* recommend only using this with test caching (see below) enabled to avoid unnecessary LLM calls:

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install pytest-watch
  LANGSMITH_TEST_CACHE=tests/cassettes ptw tests/my_llm_tests
  ```

  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv add pytest-watch
  LANGSMITH_TEST_CACHE=tests/cassettes ptw tests/my_llm_tests
  ```
</CodeGroup>

## Rich outputs

If you'd like to see a rich display of the LangSmith results of your test run you can specify `--langsmith-output`:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
pytest --langsmith-output tests
```

**Note:** This flag used to be `--output=langsmith` in `langsmith<=0.3.3` but was updated to avoid collisions with other pytest plugins.

You'll get a nice table per test suite that updates live as the results are uploaded to LangSmith:

<img alt="Rich pytest outputs" />

Some important notes for using this feature:

* Make sure you've installed `pip install -U "langsmith[pytest]"`
* Rich outputs do not currently work with `pytest-xdist`

<Note>
  The custom output removes all the standard pytest outputs. If you're trying to debug some unexpected behavior it's often better to show the regular pytest outputs so to get full error traces.
</Note>

## Dry-run mode

If you want to run the tests without syncing the results to LangSmith, you can set `LANGSMITH_TEST_TRACKING=false` in your environment.

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
LANGSMITH_TEST_TRACKING=false pytest tests/
```

The tests will run as normal, but the experiment logs will not be sent to LangSmith.

## Expectations

LangSmith provides an [expect](https://reference.langchain.com/python/langsmith/observability/sdk/expect/) utility to help define expectations about your LLM output. For example:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langsmith import expect

@pytest.mark.langsmith
def test_sql_generation_select_all():
    user_query = "Get all users from the customers table"
    sql = generate_sql(user_query)
    expect(sql).to_contain("customers")
```

This will log the binary "expectation" score to the experiment results, additionally `assert`ing that the expectation is met possibly triggering a test failure.

`expect` also provides "fuzzy match" methods. For example:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
@pytest.mark.langsmith(output_keys=["expectation"])
@pytest.mark.parametrize(
    "query, expectation",
    [
       ("what's the capital of France?", "Paris"),
    ],
)
def test_embedding_similarity(query, expectation):
    prediction = my_chatbot(query)
    expect.embedding_distance(
        # This step logs the distance as feedback for this run
        prediction=prediction, expectation=expectation
        # Adding a matcher (in this case, 'to_be_*"), logs 'expectation' feedback
    ).to_be_less_than(0.5) # Optional predicate to assert against

    expect.edit_distance(
        # This computes the normalized Damerau-Levenshtein distance between the two strings
        prediction=prediction, expectation=expectation
        # If no predicate is provided below, 'assert' isn't called, but the score is still logged
    )
```

This test case will be assigned 4 scores:

1. The `embedding_distance` between the prediction and the expectation
2. The binary `expectation` score (1 if cosine distance is less than 0.5, 0 if not)
3. The `edit_distance` between the prediction and the expectation
4. The overall test pass/fail score (binary)

The `expect` utility is modeled off of [Jest](https://jestjs.io/docs/expect)'s expect API, with some off-the-shelf functionality to make it easier to grade your LLMs.

## Legacy

#### `@test` / `@unit` decorator

The legacy method for marking test cases is using the `@test` or `@unit` decorators:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langsmith import test

@test
def test_foo() -> None:
    pass
```

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/pytest.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Query threads using the SDK
Source: https://docs.langchain.com/langsmith/query-threads

Programmatically fetch and inspect multi-turn conversation threads from your LangSmith projects.

If you're building a conversational agent or any multi-turn application, LangSmith automatically groups your [runs](/langsmith/run-data-format) into [*threads*](/langsmith/observability-concepts#threads). Querying threads lets you replay full conversations, audit agent behavior across sessions, build analytics on conversation length and latency, and feed downstream workflows like fine-tuning and evaluation.

The SDK exposes two methods for working with threads:

| Method                                                                                                                                                                                          | Use when                                         |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| [`list_threads`](https://reference.langchain.com/python/langsmith/client/Client/list_threads) / [`listThreads`](https://reference.langchain.com/javascript/langsmith/client/Client/listThreads) | You want to browse all threads in a project      |
| [`read_thread`](https://reference.langchain.com/python/langsmith/client/Client/read_thread) / [`readThread`](https://reference.langchain.com/javascript/langsmith/client/Client/readThread)     | You already know the thread ID and need its runs |

## How threads work

Each run you create can carry a `thread_id` in its metadata. LangSmith uses this to group runs into threads. The backend looks for `thread_id` in `metadata` (falling back to `session_id` or `conversation_id`).

<Note>
  We recommend using **UUID v7** thread IDs. UUIDv7 embeds a timestamp, which preserves correct time-ordering of threads. The LangSmith SDK exports a uuid7 helper (Python v0.4.43+, JS v0.3.80+):

  * **Python**: `from langsmith import uuid7`
  * **JS/TS**: `import { uuid7 } from 'langsmith'`
</Note>

If you're using a [tracing integration](/langsmith/integrations), pass `thread_id` in the run metadata:

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langsmith import traceable, uuid7

  THREAD_ID = str(uuid7())

  @traceable(metadata={"thread_id": THREAD_ID})
  def my_agent(user_message: str) -> str:
      ...
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { traceable } from "langsmith/traceable";
  import { uuid7 } from "langsmith";

  const THREAD_ID = uuid7();

  const myAgent = traceable(
    async (userMessage: string) => {
      // ...
    },
    { metadata: { thread_id: THREAD_ID } }
  );
  ```
</CodeGroup>

## List all threads in a project

`list_threads` / `listThreads` fetches all threads in a project and groups their runs together. Results are sorted by most recent activity first.

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langsmith import Client

  client = Client()

  threads = client.list_threads(project_name="my-project")

  for thread in threads:
      print(thread["thread_id"])
      print(f"  {thread['count']} runs")
      print(f"  last active: {thread['max_start_time']}")
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { Client } from "langsmith";

  const client = new Client();

  const threads = await client.listThreads({ projectName: "my-project" });

  for (const thread of threads) {
    console.log(thread.thread_id);
    console.log(`  ${thread.count} runs`);
    console.log(`  last active: ${thread.max_start_time}`);
  }
  ```
</CodeGroup>

Results are sorted by most recent activity:

```text Output theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
conv-abc123
  3 runs
  last active: 2026-02-25T10:05:42+00:00
conv-def456
  1 runs
  last active: 2026-02-25T09:30:00+00:00
```

### Parameters

| Parameter                      | Type                | Default   | Description                                                                                                        |
| ------------------------------ | ------------------- | --------- | ------------------------------------------------------------------------------------------------------------------ |
| `project_name` / `projectName` | `string`            | —         | Project name. Required if `project_id` is not set.                                                                 |
| `project_id` / `projectId`     | `string`            | —         | Project ID. Required if `project_name` is not set.                                                                 |
| `limit`                        | `int`               | all       | Maximum number of threads to return.                                                                               |
| `offset`                       | `int`               | `0`       | Number of threads to skip (for pagination).                                                                        |
| `filter`                       | `string`            | —         | Filter expression applied when fetching runs, using [LangSmith trace query syntax](/langsmith/trace-query-syntax). |
| `start_time` / `startTime`     | `datetime` / `Date` | 1 day ago | Only include runs started after this time. Widen this window to surface older threads.                             |

### Return value

A list of thread objects, each containing:

| Field            | Type                                                                    | Description                                                      |
| ---------------- | ----------------------------------------------------------------------- | ---------------------------------------------------------------- |
| `thread_id`      | `string`                                                                | The thread identifier.                                           |
| `runs`           | `[Run](https://reference.langchain.com/python/langsmith/schemas/Run)[]` | Root runs in this thread, sorted chronologically (oldest first). |
| `count`          | `int`                                                                   | Number of runs in this thread.                                   |
| `min_start_time` | `string \| null`                                                        | ISO timestamp of the earliest run.                               |
| `max_start_time` | `string \| null`                                                        | ISO timestamp of the most recent run.                            |

<Note>
  `list_threads` always returns root runs only. If you need child runs (e.g., tool calls, sub-chains), use `read_thread` instead, which accepts an `is_root` / `isRoot` parameter you can set to `false`.
</Note>

## Read runs for a single thread

When you already know the `thread_id`, use `read_thread` / `readThread`. It returns an iterator over the thread's runs directly, without fetching all threads first.

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langsmith import Client

  client = Client()

  for run in client.read_thread(
      thread_id="conv-abc123",
      project_name="my-project",
  ):
      print(run.id, run.name, run.start_time)
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { Client } from "langsmith";

  const client = new Client();

  for await (const run of client.readThread({
    threadId: "conv-abc123",
    projectName: "my-project",
  })) {
    console.log(run.id, run.name, run.start_time);
  }
  ```
</CodeGroup>

Unlike `list_threads`, each item here is a `Run` object directly — there is no grouping wrapper. Runs are returned in ascending chronological order by default.

```python Output theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
[
    Run(id=UUID("a1b2..."), name="my_agent", run_type="chain", status="success", start_time=datetime(2026, 2, 25, 10, 0, 0, tzinfo=utc), ...),
    Run(id=UUID("c3d4..."), name="my_agent", run_type="chain", status="success", start_time=datetime(2026, 2, 25, 10, 3, 11, tzinfo=utc), ...),
    Run(id=UUID("e5f6..."), name="my_agent", run_type="chain", status="error",   start_time=datetime(2026, 2, 25, 10, 5, 42, tzinfo=utc), ...),
]
```

### Parameters

| Parameter                      | Type                 | Default    | Description                                                       |
| ------------------------------ | -------------------- | ---------- | ----------------------------------------------------------------- |
| `thread_id` / `threadId`       | `string`             | —          | **Required.** The thread to query.                                |
| `project_name` / `projectName` | `string`             | —          | Project name. Required if `project_id` is not set.                |
| `project_id` / `projectId`     | `string \| string[]` | —          | Project ID or list of IDs. Required if `project_name` is not set. |
| `is_root` / `isRoot`           | `bool`               | `true`     | Return only root runs. Set to `false` to include child runs.      |
| `limit`                        | `int`                | all        | Maximum number of runs to return.                                 |
| `filter`                       | `string`             | —          | Additional filter expression (combined with the thread filter).   |
| `order`                        | `"asc" \| "desc"`    | `"asc"`    | Sort order. `"asc"` returns runs oldest-first (chronological).    |
| `select`                       | `string[]`           | all fields | Specific run fields to return, to reduce response size.           |

### Return value

An iterator ([Python](https://reference.langchain.com/python/langsmith)) or async iterator ([TypeScript](https://reference.langchain.com/javascript/langsmith)) of `Run` objects.

## Examples

### Filter threads by run properties

Pass a filter expression to narrow results using [LangSmith trace query syntax](/langsmith/trace-query-syntax). For example, to surface only threads containing at least one failed run:

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  threads = client.list_threads(
      project_name="my-project",
      filter='eq(status, "error")',
  )
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  const threads = await client.listThreads({
    projectName: "my-project",
    filter: 'eq(status, "error")',
  });
  ```
</CodeGroup>

### Look back further than 24 hours

By default, `list_threads` only surfaces threads with runs from the last day. Pass `start_time` to widen the window:

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import datetime

  threads = client.list_threads(
      project_name="my-project",
      start_time=datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=2),
  )
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  const threads = await client.listThreads({
    projectName: "my-project",
    startTime: new Date(Date.now() - 2 * 24 * 60 * 60 * 1000),
  });
  ```
</CodeGroup>

### Reconstruct a conversation

Use `read_thread` with `order="asc"` to replay a conversation turn by turn:

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  runs = list(
      client.read_thread(
          thread_id="conv-abc123",
          project_name="my-project",
          order="asc",
      )
  )

  for run in runs:
      user_msg = run.inputs.get("messages", [{}])[-1].get("content", "")
      assistant_msg = (run.outputs or {}).get("content", "")
      print(f"User:      {user_msg}")
      print(f"Assistant: {assistant_msg}")
      print()
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  const runs: Run[] = [];
  for await (const run of client.readThread({
    threadId: "conv-abc123",
    projectName: "my-project",
    order: "asc",
  })) {
    runs.push(run);
  }

  for (const run of runs) {
    const messages = (run.inputs?.messages ?? []) as Array<Record<string, string>>;
    const userMsg = messages.at(-1)?.content ?? "";
    const assistantMsg = (run.outputs as Record<string, string>)?.content ?? "";
    console.log(`User:      ${userMsg}`);
    console.log(`Assistant: ${assistantMsg}`);
  }
  ```
</CodeGroup>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/query-threads.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Get started with Studio
Source: https://docs.langchain.com/langsmith/quick-start-studio

[Studio](/langsmith/studio) in the [LangSmith Deployment UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-quick-start-studio) supports connecting to two types of graphs:

* Graphs deployed on [cloud or self-hosted](#deployed-graphs).
* Graphs running locally with [Agent Server](#local-development-server).

## Deployed graphs

Studio is accessed in the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-quick-start-studio) from the **Deployments** navigation.

For applications that are [deployed](/langsmith/deployment-quickstart), you can access Studio as part of that deployment. To do so, navigate to the deployment in the UI and select **Studio**.

This will load Studio connected to your live deployment, allowing you to create, read, and update the [threads](/oss/python/langgraph/checkpointers#threads), [assistants](/langsmith/assistants), and [memory](/oss/python/concepts/memory) in that deployment.

## Local development server

### Prerequisites

To test your application locally using Studio:

* Follow the [local application quickstart](/langsmith/local-dev-testing) first.
* If you don't want data [traced](/langsmith/observability-concepts#traces) to LangSmith, set `LANGSMITH_TRACING=false` in your application's `.env` file. With tracing disabled, no data leaves your local server.

### Setup

1. Install the [LangGraph CLI](/langsmith/cli):

   <CodeGroup>
     ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
     pip install -U "langgraph-cli[inmem]"
     langgraph dev
     ```

     ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
     uv add "langgraph-cli[inmem]"
     langgraph dev
     ```

     ```bash npm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
     npx @langchain/langgraph-cli dev
     ```
   </CodeGroup>

   <Warning>
     **Browser Compatibility**
     Safari blocks `localhost` connections to Studio. To work around this, run the command with `--tunnel` to access Studio via a secure tunnel. You'll need to manually add the tunnel URL to allowed origins by clicking **Connect to a local server** in the Studio UI. See the [troubleshooting guide](/langsmith/troubleshooting-studio#safari-connection-issues) for steps.
   </Warning>

   This will start the Agent Server locally, running in-memory. The server will run in watch mode, listening for and automatically restarting on code changes. Read this [reference](/langsmith/cli#dev) to learn about all the options for starting the API server.

   You will see the following logs:

   ```
   > Ready!
   >
   > - API: [http://localhost:2024](http://localhost:2024/)
   >
   > - Docs: http://localhost:2024/docs
   >
   > - LangSmith Studio Web UI: https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024
   ```

   Once running, you will automatically be directed to Studio.

2. For a running server, access the Dbugger with one of the following:

   1. Directly navigate to the following URL: `https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024`.
   2. Navigate to **Deployments** in the UI, click the **Studio** button on a deployment, enter `http://127.0.0.1:2024` and click **Connect**.

   If running your server at a different host or port, update the `baseUrl` to match.

### (Optional) Attach a debugger

For step-by-step debugging with breakpoints and variable inspection, run the following:

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  # Install debugpy package
  pip install debugpy
  # Start server with debugging enabled
  langgraph dev --debug-port 5678
  ```

  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  # Install debugpy package
  uv add debugpy
  # Start server with debugging enabled
  langgraph dev --debug-port 5678
  ```
</CodeGroup>

Then attach your preferred debugger:

<Tabs>
  <Tab title="VS Code">
    Add this configuration to `launch.json`:

    ```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    {
        "name": "Attach to LangGraph",
        "type": "debugpy",
        "request": "attach",
        "connect": {
          "host": "0.0.0.0",
          "port": 5678
        }
    }
    ```
  </Tab>

  <Tab title="PyCharm">
    1. Go to Run → Edit Configurations
    2. Click + and select "Python Debug Server"
    3. Set IDE host name: `localhost`
    4. Set port: `5678` (or the port number you chose in the previous step)
    5. Click "OK" and start debugging
  </Tab>
</Tabs>

<Tip>
  For issues getting started, refer to the [troubleshooting guide](/langsmith/troubleshooting-studio).
</Tip>

## Next steps

For more information on how to run Studio, refer to the following guides:

* [Run application](/langsmith/use-studio#run-application)
* [Manage assistants](/langsmith/use-studio#manage-assistants)
* [Manage threads](/langsmith/use-studio#manage-threads)
* [Iterate on prompts](/langsmith/observability-studio)
* [Debug LangSmith traces](/langsmith/observability-studio#debug-langsmith-traces)
* [Add node to dataset](/langsmith/observability-studio#add-node-to-dataset)

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/quick-start-studio.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# How to handle model rate limits
Source: https://docs.langchain.com/langsmith/rate-limiting

A common issue when running large evaluation jobs is running into third-party API rate limits, usually from model providers. There are a few ways to deal with rate limits.

## Using `langchain` RateLimiters (Python only)

If you're using `langchain` Python chat models in your application or evaluators, you can add rate limiters to your model(s) that will add client-side control of the frequency with which requests are sent to the model provider API to avoid rate limit errors.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain.chat_models import init_chat_model
from langchain_core.rate_limiters import InMemoryRateLimiter

rate_limiter = InMemoryRateLimiter(
    requests_per_second=0.1,  # <-- Super slow! We can only make a request once every 10 seconds!!
    check_every_n_seconds=0.1,  # Wake up every 100 ms to check whether allowed to make a request,
    max_bucket_size=10,  # Controls the maximum burst size.
)

model = init_chat_model("gpt-5.5", rate_limiter=rate_limiter)

def app(inputs: dict) -> dict:
    response = model.invoke(...)
    ...

def evaluator(inputs: dict, outputs: dict, reference_outputs: dict) -> dict:
    response = model.invoke(...)
    ...
```

See the [`langchain`](/oss/python/langchain/models#rate-limiting) documentation for more on how to configure rate limiters.

## Retrying with exponential backoff

A very common way to deal with rate limit errors is retrying with exponential backoff. Retrying with exponential backoff means repeatedly retrying failed requests with an (exponentially) increasing wait time between each retry. This continues until either the request succeeds or a maximum number of requests is made.

#### With `langchain`

If you're using `langchain` components you can add retries to all model calls with the `.with_retry(...)` / `.withRetry()` method:

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langchain import init_chat_model

  model_with_retry = init_chat_model("gpt-5.4-mini").with_retry(stop_after_attempt=6)
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { initChatModel } from "langchain";

  const model = await initChatModel("gpt-5.5", {
      modelProvider: "openai",
  });

  const modelWithRetry = model.withRetry({ stopAfterAttept: 2 });
  ```
</CodeGroup>

See the `langchain` [Python](https://reference.langchain.com/python/langchain_core/language_models/#langchain_core.language_models.BaseChatModel.with_retry) and [JS](https://reference.langchain.com/javascript/langchain-core/language_models/chat_models/BaseChatModel/withRetry) API references for more.

#### Without `langchain`

If you're not using `langchain` you can use other libraries like `tenacity` (Python) or `backoff` (Python) to implement retries with exponential backoff, or you can implement it from scratch. See some examples of how to do this in the [OpenAI docs](https://platform.openai.com/docs/guides/rate-limits#retrying-with-exponential-backoff).

## Limiting `max_concurrency`

Limiting the number of concurrent calls you're making to your application and evaluators is another way to decrease the frequency of model calls you're making, and in that way avoid rate limit errors. `max_concurrency` can be set directly on the [evaluate()](https://docs.smith.langchain.com/reference/python/evaluation/langsmith.evaluation._runner.evaluate) / [aevaluate()](https://docs.smith.langchain.com/reference/python/evaluation/langsmith.evaluation._arunner.aevaluate) functions. This parallelizes evaluation by effectively splitting the dataset across threads.

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langsmith import aevaluate

  results = await aevaluate(
      ...
      max_concurrency=4,
  )
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { evaluate } from "langsmith/evaluation";

  await evaluate(..., {
    ...,
    maxConcurrency: 4,
  });
  ```
</CodeGroup>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/rate-limiting.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
