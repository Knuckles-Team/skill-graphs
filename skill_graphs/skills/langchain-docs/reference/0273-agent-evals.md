# Agent Evals
Source: https://docs.langchain.com/oss/python/langchain/test/evals

Evaluate agent trajectories using deterministic matching or LLM-as-judge evaluators with AgentEvals and LangSmith.

Evaluations ("evals") measure how well your agent performs by assessing its execution trajectory, the sequence of messages and tool calls it produces. Unlike [integration tests](/oss/python/langchain/test/integration-testing) that verify basic correctness, evals score agent behavior against a reference or rubric, making them useful for catching regressions when you change prompts, tools, or models.

An evaluator is a function that takes agent outputs (and optionally reference outputs) and returns a score:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
def evaluator(*, outputs: dict, reference_outputs: dict):
    output_messages = outputs["messages"]
    reference_messages = reference_outputs["messages"]
    score = compare_messages(output_messages, reference_messages)
    return {"key": "evaluator_score", "score": score}
```

The [`agentevals`](https://github.com/langchain-ai/agentevals) package provides prebuilt evaluators for agent trajectories. You can evaluate by performing a **trajectory match** (deterministic comparison) or by using an **LLM judge** (qualitative assessment):

| Approach                                        | When to use                                                                     |
| ----------------------------------------------- | ------------------------------------------------------------------------------- |
| [Trajectory match](#trajectory-match-evaluator) | You know the expected tool calls and want fast, deterministic, cost-free checks |
| [LLM-as-judge](#llm-as-judge-evaluator)         | You want to assess overall quality and reasoning without strict expectations    |

## Install AgentEvals

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
pip install agentevals
```

Or, clone the [AgentEvals repository](https://github.com/langchain-ai/agentevals) directly.

## Trajectory match evaluator

AgentEvals offers the `create_trajectory_match_evaluator` function to match your agent's trajectory against a reference. There are four modes:

| Mode        | Description                                                                                    | Use case                                                              |
| ----------- | ---------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `strict`    | Exact match of message structure and tool calls in the same order (message content can differ) | Testing specific sequences (e.g., policy lookup before authorization) |
| `unordered` | Same message structure and tool calls as reference, but tool calls can happen in any order     | Verifying information retrieval when order doesn't matter             |
| `subset`    | Agent calls only tools from reference (no extras)                                              | Ensuring agent doesn't exceed expected scope                          |
| `superset`  | Agent calls at least the reference tools (extras allowed)                                      | Verifying minimum required actions are taken                          |

The examples below share a common setup, an agent with a `get_weather` tool:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain.agents import create_agent
from langchain.tools import tool
from langchain.messages import HumanMessage, AIMessage, ToolMessage
from agentevals.trajectory.match import create_trajectory_match_evaluator

@tool
def get_weather(city: str):
    """Get weather information for a city."""
    return f"It's 75 degrees and sunny in {city}."

agent = create_agent("claude-sonnet-4-6", tools=[get_weather])
```

<Accordion title="Strict match">
  The `strict` mode ensures trajectories contain identical messages in the same order with the same tool calls, though it allows for differences in message content. This is useful when you need to enforce a specific sequence of operations, such as requiring a policy lookup before authorizing an action.

  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  evaluator = create_trajectory_match_evaluator(  # [!code highlight]
      trajectory_match_mode="strict",  # [!code highlight]
  )  # [!code highlight]

  def test_weather_tool_called_strict():
      result = agent.invoke({
          "messages": [HumanMessage(content="What's the weather in San Francisco?")]
      })

      reference_trajectory = [
          HumanMessage(content="What's the weather in San Francisco?"),
          AIMessage(content="", tool_calls=[
              {"id": "call_1", "name": "get_weather", "args": {"city": "San Francisco"}}
          ]),
          ToolMessage(content="It's 75 degrees and sunny in San Francisco.", tool_call_id="call_1"),
          AIMessage(content="The weather in San Francisco is 75 degrees and sunny."),
      ]

      evaluation = evaluator(
          outputs=result["messages"],
          reference_outputs=reference_trajectory
      )
      # {
      #     'key': 'trajectory_strict_match',
      #     'score': True,
      #     'comment': None,
      # }
      assert evaluation["score"] is True
  ```
</Accordion>

<Accordion title="Unordered match">
  The `unordered` mode allows the same tool calls in any order. This is helpful when you want to verify that specific information was retrieved but don't care about the sequence. For example, an agent that checks both weather and events for a city with different tool calls.

  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  @tool
  def get_events(city: str):
      """Get events happening in a city."""
      return f"Concert at the park in {city} tonight."

  agent = create_agent("claude-sonnet-4-6", tools=[get_weather, get_events])

  evaluator = create_trajectory_match_evaluator(  # [!code highlight]
      trajectory_match_mode="unordered",  # [!code highlight]
  )  # [!code highlight]

  def test_multiple_tools_any_order():
      result = agent.invoke({
          "messages": [HumanMessage(content="What's happening in SF today?")]
      })

      reference_trajectory = [
          HumanMessage(content="What's happening in SF today?"),
          AIMessage(content="", tool_calls=[
              {"id": "call_1", "name": "get_events", "args": {"city": "SF"}},
              {"id": "call_2", "name": "get_weather", "args": {"city": "SF"}},
          ]),
          ToolMessage(content="Concert at the park in SF tonight.", tool_call_id="call_1"),
          ToolMessage(content="It's 75 degrees and sunny in SF.", tool_call_id="call_2"),
          AIMessage(content="Today in SF: 75 degrees and sunny with a concert at the park tonight."),
      ]

      evaluation = evaluator(
          outputs=result["messages"],
          reference_outputs=reference_trajectory,
      )
      assert evaluation["score"] is True
  ```
</Accordion>

<Accordion title="Subset and superset match">
  The `superset` and `subset` modes match partial trajectories. The `superset` mode verifies that the agent called at least the tools in the reference trajectory, allowing additional tool calls. The `subset` mode ensures the agent did not call any tools beyond those in the reference.

  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  @tool
  def get_detailed_forecast(city: str):
      """Get detailed weather forecast for a city."""
      return f"Detailed forecast for {city}: sunny all week."

  agent = create_agent("claude-sonnet-4-6", tools=[get_weather, get_detailed_forecast])

  evaluator = create_trajectory_match_evaluator(  # [!code highlight]
      trajectory_match_mode="superset",  # [!code highlight]
  )  # [!code highlight]

  def test_agent_calls_required_tools_plus_extra():
      result = agent.invoke({
          "messages": [HumanMessage(content="What's the weather in Boston?")]
      })

      # Reference only requires get_weather, but agent may call additional tools
      reference_trajectory = [
          HumanMessage(content="What's the weather in Boston?"),
          AIMessage(content="", tool_calls=[
              {"id": "call_1", "name": "get_weather", "args": {"city": "Boston"}},
          ]),
          ToolMessage(content="It's 75 degrees and sunny in Boston.", tool_call_id="call_1"),
          AIMessage(content="The weather in Boston is 75 degrees and sunny."),
      ]

      evaluation = evaluator(
          outputs=result["messages"],
          reference_outputs=reference_trajectory,
      )
      assert evaluation["score"] is True
  ```
</Accordion>

<Info>
  You can also set the `tool_args_match_mode` property and/or `tool_args_match_overrides` to customize how the evaluator considers equality between tool calls in the actual trajectory vs. the reference. By default, only tool calls with the same arguments to the same tool are considered equal. Visit the [repository](https://github.com/langchain-ai/agentevals?tab=readme-ov-file#tool-args-match-modes) for more details.
</Info>

## LLM-as-judge evaluator

You can use an LLM to evaluate the agent's execution path with the `create_trajectory_llm_as_judge` function. Unlike trajectory match evaluators, it doesn't require a reference trajectory, but one can be provided if available.

<Accordion title="Without reference trajectory">
  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from agentevals.trajectory.llm import create_trajectory_llm_as_judge, TRAJECTORY_ACCURACY_PROMPT

  evaluator = create_trajectory_llm_as_judge(  # [!code highlight]
      model="openai:o3-mini",  # [!code highlight]
      prompt=TRAJECTORY_ACCURACY_PROMPT,  # [!code highlight]
  )  # [!code highlight]

  def test_trajectory_quality():
      result = agent.invoke({
          "messages": [HumanMessage(content="What's the weather in Seattle?")]
      })

      evaluation = evaluator(
          outputs=result["messages"],
      )
      assert evaluation["score"] is True
  ```
</Accordion>

<Accordion title="With reference trajectory">
  If you have a reference trajectory, use the prebuilt `TRAJECTORY_ACCURACY_PROMPT_WITH_REFERENCE` prompt:

  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from agentevals.trajectory.llm import create_trajectory_llm_as_judge, TRAJECTORY_ACCURACY_PROMPT_WITH_REFERENCE

  evaluator = create_trajectory_llm_as_judge(
      model="openai:o3-mini",
      prompt=TRAJECTORY_ACCURACY_PROMPT_WITH_REFERENCE,
  )
  evaluation = evaluator(
      outputs=result["messages"],
      reference_outputs=reference_trajectory,
  )
  ```
</Accordion>

<Info>
  For more configurability over how the LLM evaluates the trajectory, visit the [repository](https://github.com/langchain-ai/agentevals?tab=readme-ov-file#trajectory-llm-as-judge).
</Info>

### Async support

All `agentevals` evaluators support Python asyncio. Async versions are available by adding `async` after `create_` in the function name.

<Accordion title="Async judge and evaluator example">
  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from agentevals.trajectory.llm import create_async_trajectory_llm_as_judge, TRAJECTORY_ACCURACY_PROMPT
  from agentevals.trajectory.match import create_async_trajectory_match_evaluator

  async_judge = create_async_trajectory_llm_as_judge(
      model="openai:o3-mini",
      prompt=TRAJECTORY_ACCURACY_PROMPT,
  )

  async_evaluator = create_async_trajectory_match_evaluator(
      trajectory_match_mode="strict",
  )

  async def test_async_evaluation():
      result = await agent.ainvoke({
          "messages": [HumanMessage(content="What's the weather?")]
      })

      evaluation = await async_judge(outputs=result["messages"])
      assert evaluation["score"] is True
  ```
</Accordion>

## Run evals in LangSmith

For tracking experiments over time, log evaluator results to [LangSmith](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=oss-langchain-test-evals). First, set the required environment variables:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
export LANGSMITH_API_KEY="your_langsmith_api_key"
export LANGSMITH_TRACING="true"
```

LangSmith offers two main approaches for running evaluations: [pytest](/langsmith/pytest) integration and the `evaluate` function.

<Accordion title="Use pytest integration">
  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import pytest
  from langsmith import testing as t
  from agentevals.trajectory.llm import create_trajectory_llm_as_judge, TRAJECTORY_ACCURACY_PROMPT

  trajectory_evaluator = create_trajectory_llm_as_judge(
      model="openai:o3-mini",
      prompt=TRAJECTORY_ACCURACY_PROMPT,
  )

  @pytest.mark.langsmith
  def test_trajectory_accuracy():
      result = agent.invoke({
          "messages": [HumanMessage(content="What's the weather in SF?")]
      })

      reference_trajectory = [
          HumanMessage(content="What's the weather in SF?"),
          AIMessage(content="", tool_calls=[
              {"id": "call_1", "name": "get_weather", "args": {"city": "SF"}},
          ]),
          ToolMessage(content="It's 75 degrees and sunny in SF.", tool_call_id="call_1"),
          AIMessage(content="The weather in SF is 75 degrees and sunny."),
      ]

      t.log_inputs({})
      t.log_outputs({"messages": result["messages"]})
      t.log_reference_outputs({"messages": reference_trajectory})

      trajectory_evaluator(
          outputs=result["messages"],
          reference_outputs=reference_trajectory
      )
  ```

  Run the evaluation with pytest:

  ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pytest test_trajectory.py --langsmith-output
  ```
</Accordion>

<Accordion title="Use the evaluate function">
  Create a [LangSmith dataset](/langsmith/manage-datasets) and use the `evaluate` function. The dataset must have the following schema:

  * **input**: `{"messages": [...]}` input messages to call the agent with.
  * **output**: `{"messages": [...]}` expected message history in the agent output. For trajectory evaluation, you can choose to keep only assistant messages.

  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langsmith import Client
  from agentevals.trajectory.llm import create_trajectory_llm_as_judge, TRAJECTORY_ACCURACY_PROMPT

  client = Client()

  trajectory_evaluator = create_trajectory_llm_as_judge(
      model="openai:o3-mini",
      prompt=TRAJECTORY_ACCURACY_PROMPT,
  )

  def run_agent(inputs):
      return agent.invoke(inputs)["messages"]

  experiment_results = client.evaluate(
      run_agent,
      data="your_dataset_name",
      evaluators=[trajectory_evaluator]
  )
  ```
</Accordion>

<Tip>
  To learn more about evaluating your agent, see the [LangSmith docs](/langsmith/pytest).
</Tip>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/test/evals.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Test
Source: https://docs.langchain.com/oss/python/langchain/test/index

Strategies for testing LangChain agents, including unit tests, integration tests, and trajectory evaluations.

Agentic applications let an LLM decide its own next steps to solve a problem. That flexibility is powerful, but the model's black-box nature makes it hard to predict how a tweak in one part of your agent will affect the whole. To build production-ready agents, thorough testing is essential.

There are a few approaches to testing your agents:

* **Unit tests** exercise small, deterministic pieces of your agent in isolation using in-memory fakes so you can assert exact behavior quickly and deterministically.
* **Integration tests** test the agent using real network calls to confirm that components work together, credentials and schemas line up, and latency is acceptable.
* **Evals** use evaluators to assess your agent's execution trajectory, either via deterministic matching or an LLM judge.

Agentic applications tend to lean more on integration because they chain multiple components together and must deal with flakiness due to the nondeterministic nature of LLMs.

<Tip>
  Run evaluations at scale, track results over time, and compare experiments with [LangSmith](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=oss-langchain-test-index). See [Evaluate an LLM application](/langsmith/evaluate-llm-application) to get started.
</Tip>

<CardGroup>
  <Card title="Unit testing" icon="flask" href="/oss/python/langchain/test/unit-testing">
    Mock chat models and use in-memory persistence to test agent logic without API calls.
  </Card>

  <Card title="Integration testing" icon="plug" href="/oss/python/langchain/test/integration-testing">
    Test your agent with real LLM APIs. Organize tests, manage keys, handle flakiness, and control costs.
  </Card>

  <Card title="Evals" icon="scale" href="/oss/python/langchain/test/evals">
    Evaluate agent trajectories with deterministic matching or LLM-as-judge evaluators.
  </Card>
</CardGroup>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/test/index.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Integration testing
Source: https://docs.langchain.com/oss/python/langchain/test/integration-testing

Test agents with real LLM APIs by organizing tests, managing keys, handling flakiness, and controlling costs.

Integration tests verify that your agent works correctly with model APIs and external services. Unlike [unit tests](/oss/python/langchain/test/unit-testing) that use fakes and mocks, integration tests make actual network calls to confirm that components work together, credentials are valid, and latency is acceptable.

Because LLM responses are nondeterministic, integration tests require different strategies than traditional software tests. This guide covers how to organize, write, and run integration tests for your agents. For general test infrastructure when contributing to LangChain itself, see [Contributing to code](/oss/python/contributing/code#running-tests).

## Separate unit and integration tests

Integration tests are slower and require API credentials, so keep them separate from unit tests. This lets you run fast unit tests on every change and reserve integration tests for CI or pre-deploy checks.

Use pytest markers to tag integration tests:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import pytest

@pytest.mark.integration
def test_agent_with_real_model():
    agent = create_agent("claude-sonnet-4-6", tools=[get_weather])
    result = agent.invoke({
        "messages": [HumanMessage(content="What's the weather in SF?")]
    })
    assert len(result["messages"]) > 1
```

Configure pytest to recognize the marker and exclude integration tests from default runs:

<CodeGroup>
  ```ini pytest.ini theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  [pytest]
  markers =
      integration: tests that call real LLM APIs
  addopts = -m "not integration"
  ```

  ```toml pyproject.toml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  [tool.pytest.ini_options]
  markers = [
    "integration: tests that call real LLM APIs"
  ]
  addopts = "-m 'not integration'"
  ```
</CodeGroup>

Run integration tests explicitly:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
pytest -m integration
```

## Manage API keys

Integration tests require real API credentials. Load them from environment variables so keys stay out of source control.

Use a `conftest.py` fixture to validate that required keys are available:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import os
import pytest

@pytest.fixture(autouse=True)
def check_api_keys():
    if not os.environ.get("OPENAI_API_KEY"):
        pytest.skip("OPENAI_API_KEY not set")
```

For local development, store keys in a `.env` file and load them with [`python-dotenv`](https://pypi.org/project/python-dotenv/):

```bash .env theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
OPENAI_API_KEY=sk-...
```

```python conftest.py theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from dotenv import load_dotenv

load_dotenv()
```

<Warning>
  Add `.env` to your `.gitignore` to avoid committing credentials. In CI, inject secrets through your provider's secrets management (e.g., GitHub Actions secrets).
</Warning>

## Assert on structure, not content

LLM responses vary between runs. Instead of asserting on exact output strings, verify the structural properties of the response: message types, tool call names, argument shapes, and message count.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
def test_agent_calls_weather_tool():
    agent = create_agent("claude-sonnet-4-6", tools=[get_weather])
    result = agent.invoke({
        "messages": [HumanMessage(content="What's the weather in SF?")]
    })

    messages = result["messages"]
    tool_calls = [
        tc
        for msg in messages
        if hasattr(msg, "tool_calls")
        for tc in (msg.tool_calls or [])
    ]

    assert any(tc["name"] == "get_weather" for tc in tool_calls)
    assert isinstance(messages[-1], AIMessage)
    assert len(messages[-1].content) > 0
```

<Tip>
  For more rigorous trajectory assertions, use the [AgentEvals](/oss/python/langchain/test/evals) evaluators which support fuzzy matching modes like `unordered` and `superset`.
</Tip>

## Reduce cost and latency

Integration tests that call LLM APIs incur real costs. A few practices help keep test suites fast and affordable:

* **Use smaller models**: `gemini-3.1-flash-lite` or equivalent for tests that only need to verify tool calling and response structure.
* **Set `maxTokens`**: Cap response length to avoid long, expensive completions.
* **Limit test scope**: Test one behavior per test. Avoid end-to-end scenarios that chain many LLM calls when a single-turn test suffices.
* **Run selectively**: Use the test separation from [above](#separate-unit-and-integration-tests) to run integration tests only in CI or before deploy, not on every file save.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
agent = create_agent(
    "gemini-3.1-flash-lite",
    tools=[get_weather],
    model_kwargs={"max_tokens": 256},
)
```

## Record and replay HTTP calls

For tests that run frequently in CI, you can record HTTP interactions on the first run and replay them on subsequent runs without making real API calls. This eliminates cost and latency after the initial recording.

[`vcrpy`](https://pypi.org/project/vcrpy/1.5.2/) records HTTP request/response pairs into YAML "cassette" files. The [`pytest-recording`](https://pypi.org/project/pytest-recording/) plugin integrates this with pytest.

Set up your `conftest.py` to filter sensitive information from cassettes:

```py conftest.py theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import pytest

@pytest.fixture(scope="session")
def vcr_config():
    return {
        "filter_headers": [
            ("authorization", "XXXX"),
            ("x-api-key", "XXXX"),
        ],
        "filter_query_parameters": [
            ("api_key", "XXXX"),
            ("key", "XXXX"),
        ],
    }
```

Configure your project to recognize the `vcr` marker:

<CodeGroup>
  ```ini pytest.ini theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  [pytest]
  markers =
      vcr: record/replay HTTP via VCR
  addopts = --record-mode=once
  ```

  ```toml pyproject.toml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  [tool.pytest.ini_options]
  markers = [
    "vcr: record/replay HTTP via VCR"
  ]
  addopts = "--record-mode=once"
  ```
</CodeGroup>

<Info>
  The `--record-mode=once` option records HTTP interactions on the first run and replays them on subsequent runs.
</Info>

Decorate your tests with the `vcr` marker:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
@pytest.mark.vcr()
def test_agent_trajectory():
    agent = create_agent("claude-sonnet-4-6", tools=[get_weather])
    result = agent.invoke({
        "messages": [HumanMessage(content="What's the weather in SF?")]
    })
    assert any(
        tc["name"] == "get_weather"
        for msg in result["messages"]
        if hasattr(msg, "tool_calls")
        for tc in (msg.tool_calls or [])
    )
```

The first run makes real network calls and generates a cassette file in `tests/cassettes/`. Subsequent runs replay the recorded responses.

<Warning>
  When you modify prompts, add new tools, or change expected trajectories, your saved cassettes will become outdated and your existing tests **will fail**. Delete the corresponding cassette files and rerun the tests to record fresh interactions.
</Warning>

## Next steps

Learn how to evaluate agent trajectories with deterministic matching or LLM-as-judge evaluators in [Evals](/oss/python/langchain/test/evals).

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/test/integration-testing.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Unit testing
Source: https://docs.langchain.com/oss/python/langchain/test/unit-testing

Test agent logic without API calls using fake chat models and in-memory persistence.

Unit tests exercise small, deterministic pieces of your agent in isolation. By replacing the real LLM with an in-memory fake (AKA fixture), you can script exact responses (text, tool calls, and errors) so tests are fast, free, and repeatable without API keys.

## Mock chat model

LangChain provides [`GenericFakeChatModel`](https://reference.langchain.com/python/langchain-core/language_models/fake_chat_models/GenericFakeChatModel) for mocking text responses. It accepts an iterator of responses ([`AIMessage`](https://reference.langchain.com/python/langchain-core/messages/ai/AIMessage) objects or strings) and returns one per invocation. It supports both regular and streaming usage.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_core.language_models.fake_chat_models import GenericFakeChatModel

model = GenericFakeChatModel(messages=iter([
    AIMessage(content="", tool_calls=[ToolCall(name="foo", args={"bar": "baz"}, id="call_1")]),
    "bar"
]))

model.invoke("hello")

# AIMessage(content='', ..., tool_calls=[{'name': 'foo', 'args': {'bar': 'baz'}, 'id': 'call_1', 'type': 'tool_call'}])
```

If we invoke the model again, it will return the next item in the iterator:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
model.invoke("hello, again!")

# AIMessage(content='bar', ...)
```

## InMemorySaver checkpointer

To enable persistence during testing, you can use the [`InMemorySaver`](https://reference.langchain.com/python/langgraph/checkpoints/#langgraph.checkpoint.memory.InMemorySaver) checkpointer. This allows you to simulate multiple turns to test state-dependent behavior:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langgraph.checkpoint.memory import InMemorySaver

agent = create_agent(
    model,
    tools=[],
    checkpointer=InMemorySaver()
)

# First invocation
agent.invoke(
    {"messages": [HumanMessage(content="I live in Sydney, Australia")]},
    config={"configurable": {"thread_id": "session-1"}}
)

# Second invocation: the first message is persisted (Sydney location), so the model returns GMT+10 time
agent.invoke(
    {"messages": [HumanMessage(content="What's my local time?")]},
    config={"configurable": {"thread_id": "session-1"}}
)
```

## Next steps

Learn how to test your agent with real model provider APIs in [Integration testing](/oss/python/langchain/test/integration-testing).

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/test/unit-testing.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Tools
Source: https://docs.langchain.com/oss/python/langchain/tools

Tools extend what [agents](/oss/python/langchain/agents) can do—letting them fetch real-time data, execute code, query external databases, and take actions in the world.

Under the hood, tools are callable functions with well-defined inputs and outputs that get passed to a [chat model](/oss/python/langchain/models). The model decides when to invoke a tool based on the conversation context, and what input arguments to provide.

<Tip>
  For details on how models handle tool calls, see [Tool calling](/oss/python/langchain/models#tool-calling). Trace tool calls and debug errors with [LangSmith](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=oss-langchain-tools). Follow the [tracing quickstart](/langsmith/trace-with-langchain) to get set up.

  We recommend you also set up [LangSmith Engine](/langsmith/engine) which monitors your traces, detects issues, and proposes fixes.
</Tip>

## Create tools

### Basic tool definition

The simplest way to create a tool is with the [`@tool`](https://reference.langchain.com/python/langchain-core/tools/convert/tool) decorator. By default, the function's docstring becomes the tool's description that helps the model understand when to use it:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain.tools import tool

@tool
def search_database(query: str, limit: int = 10) -> str:
    """Search the customer database for records matching the query.

    Args:
        query: Search terms to look for
        limit: Maximum number of results to return
    """
    return f"Found {limit} results for '{query}'"
```

Type hints are **required** as they define the tool's input schema. The docstring should be informative and concise to help the model understand the tool's purpose.

<Note>
  **Server-side tool use:** Some chat models feature built-in tools (web search, code interpreters) that are executed server-side. See [Server-side tool use](#server-side-tool-use) for details.
</Note>

<Warning>
  Prefer `snake_case` for tool names (e.g., `web_search` instead of `Web Search`). Some model providers have issues with or reject names containing spaces or special characters with errors. Sticking to alphanumeric characters, underscores, and hyphens helps to improve compatibility across providers.
</Warning>

### Customize tool properties

#### Custom tool name

By default, the tool name comes from the function name. Override it when you need something more descriptive:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
@tool("web_search")  # Custom name
def search(query: str) -> str:
    """Search the web for information."""
    return f"Results for: {query}"

print(search.name)  # web_search
```

#### Custom tool description

Override the auto-generated tool description for clearer model guidance:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
@tool("calculator", description="Performs arithmetic calculations. Use this for any math problems.")
def calc(expression: str) -> str:
    """Evaluate mathematical expressions."""
    return str(eval(expression))
```

### Advanced schema definition

Define complex inputs with Pydantic models or JSON schemas:

<CodeGroup>
  ```python Pydantic model theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from pydantic import BaseModel, Field
  from typing import Literal

  class WeatherInput(BaseModel):
      """Input for weather queries."""
      location: str = Field(description="City name or coordinates")
      units: Literal["celsius", "fahrenheit"] = Field(
          default="celsius",
          description="Temperature unit preference"
      )
      include_forecast: bool = Field(
          default=False,
          description="Include 5-day forecast"
      )

  @tool(args_schema=WeatherInput)
  def get_weather(location: str, units: str = "celsius", include_forecast: bool = False) -> str:
      """Get current weather and optional forecast."""
      temp = 22 if units == "celsius" else 72
      result = f"Current weather in {location}: {temp} degrees {units[0].upper()}"
      if include_forecast:
          result += "\nNext 5 days: Sunny"
      return result
  ```

  ```python JSON Schema theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  weather_schema = {
      "type": "object",
      "properties": {
          "location": {"type": "string"},
          "units": {"type": "string"},
          "include_forecast": {"type": "boolean"}
      },
      "required": ["location", "units", "include_forecast"]
  }

  @tool(args_schema=weather_schema)
  def get_weather(location: str, units: str = "celsius", include_forecast: bool = False) -> str:
      """Get current weather and optional forecast."""
      temp = 22 if units == "celsius" else 72
      result = f"Current weather in {location}: {temp} degrees {units[0].upper()}"
      if include_forecast:
          result += "\nNext 5 days: Sunny"
      return result
  ```
</CodeGroup>

### Reserved argument names

The following parameter names are reserved and cannot be used as tool arguments. Using these names will cause runtime errors.

| Parameter name | Purpose                                                                |
| -------------- | ---------------------------------------------------------------------- |
| `config`       | Reserved for passing `RunnableConfig` to tools internally              |
| `runtime`      | Reserved for `ToolRuntime` parameter (accessing state, context, store) |

To access runtime information, use the [`ToolRuntime`](https://reference.langchain.com/python/langchain/tools/#langchain.tools.ToolRuntime) parameter instead of naming your own arguments `config` or `runtime`.

If you use `InjectedState`, `InjectedStore`, `get_runtime()`, or `InjectedToolCallId`, see [Migrate from older injection patterns](#migrate-from-older-injection-patterns).

## Access context

Tools are most powerful when they can access runtime information like conversation history, user data, and persistent memory. This section covers how to access and update this information from within your tools.

Tools can access runtime information through the [`ToolRuntime`](https://reference.langchain.com/python/langchain/tools/#langchain.tools.ToolRuntime) parameter, which provides:

| Component          | Description                                                                                                                 | Use case                                                    |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| **State**          | Short-term memory - mutable data that exists for the current conversation (messages, counters, custom fields)               | Access conversation history, track tool call counts         |
| **Context**        | Immutable configuration passed at invocation time (user IDs, session info)                                                  | Personalize responses based on user identity                |
| **Store**          | Long-term memory - persistent data that survives across conversations                                                       | Save user preferences, maintain knowledge base              |
| **Stream Writer**  | Emit real-time updates during tool execution                                                                                | Show progress for long-running operations                   |
| **Execution Info** | Identity and retry information for the current execution (thread ID, run ID, attempt number)                                | Access thread/run IDs, adjust behavior based on retry state |
| **Server Info**    | Server-specific metadata when running on LangGraph Server (assistant ID, graph ID, authenticated user)                      | Access assistant ID, graph ID, or authenticated user info   |
| **Config**         | [`RunnableConfig`](https://reference.langchain.com/python/langchain-core/runnables/config/RunnableConfig) for the execution | Access callbacks, tags, and metadata                        |
| **Tool Call ID**   | Unique identifier for the current tool invocation                                                                           | Correlate tool calls for logs and model invocations         |

```mermaid theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
graph LR
    %% Runtime Context
    subgraph "🔧 Tool Runtime Context"
        A[Tool Call] --> B[ToolRuntime]
        B --> C[State Access]
        B --> D[Context Access]
        B --> E[Store Access]
        B --> F[Stream Writer]
    end

    %% Available Resources
    subgraph "📊 Available Resources"
        C --> G[Messages]
        C --> H[Custom State]
        D --> I[User ID]
        D --> J[Session Info]
        E --> K[Long-term Memory]
        E --> L[User Preferences]
    end

    %% Tool Capabilities
    subgraph "⚡ Enhanced Tool Capabilities"
        M[Context-Aware Tools]
        N[Stateful Tools]
        O[Memory-Enabled Tools]
        P[Streaming Tools]
    end

    %% Connections
    G --> M
    H --> N
    I --> M
    J --> M
    K --> O
    L --> O
    F --> P

    classDef trigger fill:#F6FFDB,stroke:#6E8900,stroke-width:2px,color:#2E3900
    classDef process fill:#E5F4FF,stroke:#006DDD,stroke-width:2px,color:#030710
    classDef output fill:#EBD0F0,stroke:#885270,stroke-width:2px,color:#441E33
    classDef neutral fill:#F2FAFF,stroke:#40668D,stroke-width:2px,color:#2F4B68

    class A trigger
    class B,C,D,E,F process
    class G,H,I,J,K,L neutral
    class M,N,O,P output
```

### Short-term memory (State)

State represents short-term memory that exists for the duration of a conversation. It includes the message history and any custom fields you define in your [graph state](/oss/python/langgraph/graph-api#state).

<Info>
  Add `runtime: ToolRuntime` to your tool signature to access state. This parameter is automatically injected and hidden from the LLM - it won't appear in the tool's schema.
</Info>

#### Access state

Tools can access the current conversation state using `runtime.state`:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain.tools import tool, ToolRuntime
from langchain.messages import HumanMessage

@tool
def get_last_user_message(runtime: ToolRuntime) -> str:
    """Get the most recent message from the user."""
    messages = runtime.state["messages"]

    # Find the last human message
    for message in reversed(messages):
        if isinstance(message, HumanMessage):
            return message.content

    return "No user messages found"
