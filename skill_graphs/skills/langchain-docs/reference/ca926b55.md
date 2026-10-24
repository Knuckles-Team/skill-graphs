# Streaming
Source: https://docs.langchain.com/oss/python/langchain/streaming

Stream real-time updates from agent runs

<Tip>
  For new applications, we recommend [event streaming](/oss/python/langchain/event-streaming)—the typed-projection API introduced in LangChain v1.3. Event streaming gives you separate iterators per projection (messages, values, tool calls, subgraphs) so you can consume them independently instead of branching on `stream_mode` chunks.
</Tip>

LangChain implements a streaming system to surface real-time updates.

Streaming is crucial for enhancing the responsiveness of applications built on LLMs. By displaying output progressively, even before a complete response is ready, streaming significantly improves user experience (UX), particularly when dealing with the latency of LLMs.

## Overview

LangChain's streaming system lets you surface live feedback from agent runs to your application.

What's possible with LangChain streaming:

* <Icon icon="brain" /> [**Stream agent progress**](#agent-progress)—get state updates after each agent step.
* <Icon icon="binary" /> [**Stream LLM tokens**](#llm-tokens)—stream language model tokens as they're generated.
* <Icon icon="bulb" /> [**Stream thinking / reasoning tokens**](#streaming-thinking-/-reasoning-tokens)—surface model reasoning as it's generated.
* <Icon icon="table" /> [**Stream custom updates**](#custom-updates)—emit user-defined signals (e.g., `"Fetched 10/100 records"`).
* <Icon icon="stack-push" /> [**Stream multiple modes**](#stream-multiple-modes)—choose from `updates` (agent progress), `messages` (LLM tokens + metadata), or `custom` (arbitrary user data).

See the [common patterns](#common-patterns) section below for additional end-to-end examples.

## Supported stream modes

Pass one or more of the following stream modes as a list to the [`stream`](https://reference.langchain.com/python/langgraph/graphs/#langgraph.graph.state.CompiledStateGraph.stream) or [`astream`](https://reference.langchain.com/python/langgraph/graphs/#langgraph.graph.state.CompiledStateGraph.astream) methods:

| Mode       | Description                                                                                                                                                       |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `updates`  | Streams state updates after each agent step. If multiple updates are made in the same step (e.g., multiple nodes are run), those updates are streamed separately. |
| `messages` | Streams tuples of `(token, metadata)` from any graph nodes where an LLM is invoked.                                                                               |
| `custom`   | Streams custom data from inside your graph nodes using the stream writer.                                                                                         |

## Agent progress

To stream agent progress, use the [`stream`](https://reference.langchain.com/python/langgraph/graphs/#langgraph.graph.state.CompiledStateGraph.stream) or [`astream`](https://reference.langchain.com/python/langgraph/graphs/#langgraph.graph.state.CompiledStateGraph.astream) methods with `stream_mode="updates"`. This emits an event after every agent step.

For example, if you have an agent that calls a tool once, you should see the following updates:

* **LLM node**: [`AIMessage`](https://reference.langchain.com/python/langchain-core/messages/ai/AIMessage) with tool call requests
* **Tool node**: [`ToolMessage`](https://reference.langchain.com/python/langchain-core/messages/tool/ToolMessage) with execution result
* **LLM node**: Final AI response

Pass a `thread_id` via `config` so the conversation is checkpointed and follow-up turns can resume the same history. `thread_id` is independent of `stream_mode`; you can also pass `context` alongside it for per-run data your tools read from `runtime.context`.

<CodeGroup>
  ```python Google theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langchain.agents import create_agent
  from langchain_core.utils.uuid import uuid7
  from langgraph.checkpoint.memory import InMemorySaver

  def get_weather(city: str) -> str:
      """Get weather for a given city."""
      return f"It's always sunny in {city}!"

  agent = create_agent(
      model="google_genai:gemini-3.5-flash",
      tools=[get_weather],
      checkpointer=InMemorySaver()
  )
  config = {"configurable": {"thread_id": str(uuid7())}}
  for chunk in agent.stream(  # [!code highlight]
      {"messages": [{"role": "user", "content": "What is the weather in SF?"}]},
      config=config,
      stream_mode="updates",
      version="v2",  # [!code highlight]
  ):
      if chunk["type"] == "updates":  # [!code highlight]
          for step, data in chunk["data"].items():  # [!code highlight]
              print(f"step: {step}")
              print(f"content: {data['messages'][-1].content_blocks}")
  ```

  ```python OpenAI theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langchain.agents import create_agent
  from langchain_core.utils.uuid import uuid7
  from langgraph.checkpoint.memory import InMemorySaver

  def get_weather(city: str) -> str:
      """Get weather for a given city."""
      return f"It's always sunny in {city}!"

  agent = create_agent(
      model="openai:gpt-5.5",
      tools=[get_weather],
      checkpointer=InMemorySaver()
  )
  config = {"configurable": {"thread_id": str(uuid7())}}
  for chunk in agent.stream(  # [!code highlight]
      {"messages": [{"role": "user", "content": "What is the weather in SF?"}]},
      config=config,
      stream_mode="updates",
      version="v2",  # [!code highlight]
  ):
      if chunk["type"] == "updates":  # [!code highlight]
          for step, data in chunk["data"].items():  # [!code highlight]
              print(f"step: {step}")
              print(f"content: {data['messages'][-1].content_blocks}")
  ```

  ```python Anthropic theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langchain.agents import create_agent
  from langchain_core.utils.uuid import uuid7
  from langgraph.checkpoint.memory import InMemorySaver

  def get_weather(city: str) -> str:
      """Get weather for a given city."""
      return f"It's always sunny in {city}!"

  agent = create_agent(
      model="anthropic:claude-sonnet-4-6",
      tools=[get_weather],
      checkpointer=InMemorySaver()
  )
  config = {"configurable": {"thread_id": str(uuid7())}}
  for chunk in agent.stream(  # [!code highlight]
      {"messages": [{"role": "user", "content": "What is the weather in SF?"}]},
      config=config,
      stream_mode="updates",
      version="v2",  # [!code highlight]
  ):
      if chunk["type"] == "updates":  # [!code highlight]
          for step, data in chunk["data"].items():  # [!code highlight]
              print(f"step: {step}")
              print(f"content: {data['messages'][-1].content_blocks}")
  ```

  ```python OpenRouter theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langchain.agents import create_agent
  from langchain_core.utils.uuid import uuid7
  from langgraph.checkpoint.memory import InMemorySaver

  def get_weather(city: str) -> str:
      """Get weather for a given city."""
      return f"It's always sunny in {city}!"

  agent = create_agent(
      model="openrouter:anthropic/claude-sonnet-4-6",
      tools=[get_weather],
      checkpointer=InMemorySaver()
  )
  config = {"configurable": {"thread_id": str(uuid7())}}
  for chunk in agent.stream(  # [!code highlight]
      {"messages": [{"role": "user", "content": "What is the weather in SF?"}]},
      config=config,
      stream_mode="updates",
      version="v2",  # [!code highlight]
  ):
      if chunk["type"] == "updates":  # [!code highlight]
          for step, data in chunk["data"].items():  # [!code highlight]
              print(f"step: {step}")
              print(f"content: {data['messages'][-1].content_blocks}")
  ```

  ```python Fireworks theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langchain.agents import create_agent
  from langchain_core.utils.uuid import uuid7
  from langgraph.checkpoint.memory import InMemorySaver

  def get_weather(city: str) -> str:
      """Get weather for a given city."""
      return f"It's always sunny in {city}!"

  agent = create_agent(
      model="fireworks:accounts/fireworks/models/qwen3p5-397b-a17b",
      tools=[get_weather],
      checkpointer=InMemorySaver()
  )
  config = {"configurable": {"thread_id": str(uuid7())}}
  for chunk in agent.stream(  # [!code highlight]
      {"messages": [{"role": "user", "content": "What is the weather in SF?"}]},
      config=config,
      stream_mode="updates",
      version="v2",  # [!code highlight]
  ):
      if chunk["type"] == "updates":  # [!code highlight]
          for step, data in chunk["data"].items():  # [!code highlight]
              print(f"step: {step}")
              print(f"content: {data['messages'][-1].content_blocks}")
  ```

  ```python Baseten theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langchain.agents import create_agent
  from langchain_core.utils.uuid import uuid7
  from langgraph.checkpoint.memory import InMemorySaver

  def get_weather(city: str) -> str:
      """Get weather for a given city."""
      return f"It's always sunny in {city}!"

  agent = create_agent(
      model="baseten:zai-org/GLM-5",
      tools=[get_weather],
      checkpointer=InMemorySaver()
  )
  config = {"configurable": {"thread_id": str(uuid7())}}
  for chunk in agent.stream(  # [!code highlight]
      {"messages": [{"role": "user", "content": "What is the weather in SF?"}]},
      config=config,
      stream_mode="updates",
      version="v2",  # [!code highlight]
  ):
      if chunk["type"] == "updates":  # [!code highlight]
          for step, data in chunk["data"].items():  # [!code highlight]
              print(f"step: {step}")
              print(f"content: {data['messages'][-1].content_blocks}")
  ```

  ```python Ollama theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langchain.agents import create_agent
  from langchain_core.utils.uuid import uuid7
  from langgraph.checkpoint.memory import InMemorySaver

  def get_weather(city: str) -> str:
      """Get weather for a given city."""
      return f"It's always sunny in {city}!"

  agent = create_agent(
      model="ollama:devstral-2",
      tools=[get_weather],
      checkpointer=InMemorySaver()
  )
  config = {"configurable": {"thread_id": str(uuid7())}}
  for chunk in agent.stream(  # [!code highlight]
      {"messages": [{"role": "user", "content": "What is the weather in SF?"}]},
      config=config,
      stream_mode="updates",
      version="v2",  # [!code highlight]
  ):
      if chunk["type"] == "updates":  # [!code highlight]
          for step, data in chunk["data"].items():  # [!code highlight]
              print(f"step: {step}")
              print(f"content: {data['messages'][-1].content_blocks}")
  ```
</CodeGroup>

```shell title="Output" theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
step: model
content: [{'type': 'tool_call', 'name': 'get_weather', 'args': {'city': 'San Francisco'}, 'id': 'call_9lBtsDbmmobzyA8xc4I4Ctne'}]
step: tools
content: [{'type': 'text', 'text': "It's always sunny in San Francisco!"}]
step: model
content: [{'type': 'text', 'text': "San Francisco weather: It's always sunny in San Francisco!\n\nIf you’d like the exact current conditions (temperature, humidity, wind) and a short forecast, I can fetch that next. Would you like me to pull live details for San Francisco?"}]
```

<Note>
  Persisting conversation history with `thread_id` requires the agent to be configured with a [checkpointer](/oss/python/langchain/long-term-memory). On [LangSmith deployments](/langsmith/deployment) a checkpointer is provisioned automatically. Locally, pass one explicitly, for example `create_agent(..., checkpointer=InMemorySaver())`. The remaining snippets on this page omit `thread_id` for brevity, but you should pass it in production.
</Note>

## LLM tokens

To stream tokens as they are produced by the LLM, use `stream_mode="messages"`. Below you can see the output of the agent streaming tool calls and the final response.

```python title="Streaming LLM tokens" theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain.agents import create_agent

def get_weather(city: str) -> str:
    """Get weather for a given city."""

    return f"It's always sunny in {city}!"

agent = create_agent(
    model="gpt-5-nano",
    tools=[get_weather],
)
for chunk in agent.stream(  # [!code highlight]
    {"messages": [{"role": "user", "content": "What is the weather in SF?"}]},
    stream_mode="messages",
    version="v2",  # [!code highlight]
):
    if chunk["type"] == "messages":  # [!code highlight]
        token, metadata = chunk["data"]  # [!code highlight]
        print(f"node: {metadata['langgraph_node']}")
        print(f"content: {token.content_blocks}")
        print("\n")
```

```shell title="Output" expandable theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
node: model
content: [{'type': 'tool_call_chunk', 'id': 'call_vbCyBcP8VuneUzyYlSBZZsVa', 'name': 'get_weather', 'args': '', 'index': 0}]

node: model
content: [{'type': 'tool_call_chunk', 'id': None, 'name': None, 'args': '{"', 'index': 0}]

node: model
content: [{'type': 'tool_call_chunk', 'id': None, 'name': None, 'args': 'city', 'index': 0}]

node: model
content: [{'type': 'tool_call_chunk', 'id': None, 'name': None, 'args': '":"', 'index': 0}]

node: model
content: [{'type': 'tool_call_chunk', 'id': None, 'name': None, 'args': 'San', 'index': 0}]

node: model
content: [{'type': 'tool_call_chunk', 'id': None, 'name': None, 'args': ' Francisco', 'index': 0}]

node: model
content: [{'type': 'tool_call_chunk', 'id': None, 'name': None, 'args': '"}', 'index': 0}]

node: model
content: []

node: tools
content: [{'type': 'text', 'text': "It's always sunny in San Francisco!"}]

node: model
content: []

node: model
content: [{'type': 'text', 'text': 'Here'}]

node: model
content: [{'type': 'text', 'text': ''s'}]

node: model
content: [{'type': 'text', 'text': ' what'}]

node: model
content: [{'type': 'text', 'text': ' I'}]

node: model
content: [{'type': 'text', 'text': ' got'}]

node: model
content: [{'type': 'text', 'text': ':'}]

node: model
content: [{'type': 'text', 'text': ' "'}]

node: model
content: [{'type': 'text', 'text': "It's"}]

node: model
content: [{'type': 'text', 'text': ' always'}]

node: model
content: [{'type': 'text', 'text': ' sunny'}]

node: model
content: [{'type': 'text', 'text': ' in'}]

node: model
content: [{'type': 'text', 'text': ' San'}]

node: model
content: [{'type': 'text', 'text': ' Francisco'}]

node: model
content: [{'type': 'text', 'text': '!"\n\n'}]
```

## Custom updates

To stream updates from tools as they are executed, you can use [`get_stream_writer`](https://reference.langchain.com/python/langgraph/config/get_stream_writer).

```python title="Streaming custom updates" theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain.agents import create_agent
from langgraph.config import get_stream_writer  # [!code highlight]

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    writer = get_stream_writer()  # [!code highlight]
    # stream any arbitrary data
    writer(f"Looking up data for city: {city}")
    writer(f"Acquired data for city: {city}")
    return f"It's always sunny in {city}!"

agent = create_agent(
    model="claude-sonnet-4-6",
    tools=[get_weather],
)

for chunk in agent.stream(
    {"messages": [{"role": "user", "content": "What is the weather in SF?"}]},
    stream_mode="custom",  # [!code highlight]
    version="v2",  # [!code highlight]
):
    if chunk["type"] == "custom":  # [!code highlight]
        print(chunk["data"])  # [!code highlight]
```

```shell title="Output" theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
Looking up data for city: San Francisco
Acquired data for city: San Francisco
```

<Note>
  If you add [`get_stream_writer`](https://reference.langchain.com/python/langgraph/config/get_stream_writer) inside your tool, you won't be able to invoke the tool outside of a LangGraph execution context.
</Note>

## Stream multiple modes

You can specify multiple streaming modes by passing stream mode as a list: `stream_mode=["updates", "custom"]`.

Each streamed chunk is a `StreamPart` dict with `type`, `ns`, and `data` keys. Use `chunk["type"]` to determine the stream mode and `chunk["data"]` to access the payload.

```python title="Streaming multiple modes" theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain.agents import create_agent
from langgraph.config import get_stream_writer

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    writer = get_stream_writer()
    writer(f"Looking up data for city: {city}")
    writer(f"Acquired data for city: {city}")
    return f"It's always sunny in {city}!"

agent = create_agent(
    model="gpt-5-nano",
    tools=[get_weather],
)

for chunk in agent.stream(  # [!code highlight]
    {"messages": [{"role": "user", "content": "What is the weather in SF?"}]},
    stream_mode=["updates", "custom"],
    version="v2",  # [!code highlight]
):
    print(f"stream_mode: {chunk['type']}")  # [!code highlight]
    print(f"content: {chunk['data']}")  # [!code highlight]
    print("\n")
```

```shell title="Output" theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
stream_mode: updates
content: {'model': {'messages': [AIMessage(content='', response_metadata={'token_usage': {'completion_tokens': 280, 'prompt_tokens': 132, 'total_tokens': 412, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 256, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_provider': 'openai', 'model_name': 'gpt-5-nano-2025-08-07', 'system_fingerprint': None, 'id': 'chatcmpl-C9tlgBzGEbedGYxZ0rTCz5F7OXpL7', 'service_tier': 'default', 'finish_reason': 'tool_calls', 'logprobs': None}, id='lc_run--480c07cb-e405-4411-aa7f-0520fddeed66-0', tool_calls=[{'name': 'get_weather', 'args': {'city': 'San Francisco'}, 'id': 'call_KTNQIftMrl9vgNwEfAJMVu7r', 'type': 'tool_call'}], usage_metadata={'input_tokens': 132, 'output_tokens': 280, 'total_tokens': 412, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 256}})]}}

stream_mode: custom
content: Looking up data for city: San Francisco

stream_mode: custom
content: Acquired data for city: San Francisco

stream_mode: updates
content: {'tools': {'messages': [ToolMessage(content="It's always sunny in San Francisco!", name='get_weather', tool_call_id='call_KTNQIftMrl9vgNwEfAJMVu7r')]}}

stream_mode: updates
content: {'model': {'messages': [AIMessage(content='San Francisco weather: It's always sunny in San Francisco!\n\n', response_metadata={'token_usage': {'completion_tokens': 764, 'prompt_tokens': 168, 'total_tokens': 932, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 704, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_provider': 'openai', 'model_name': 'gpt-5-nano-2025-08-07', 'system_fingerprint': None, 'id': 'chatcmpl-C9tljDFVki1e1haCyikBptAuXuHYG', 'service_tier': 'default', 'finish_reason': 'stop', 'logprobs': None}, id='lc_run--acbc740a-18fe-4a14-8619-da92a0d0ee90-0', usage_metadata={'input_tokens': 168, 'output_tokens': 764, 'total_tokens': 932, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 704}})]}}
```

## Common patterns

Below are examples showing common use cases for streaming.

### Streaming thinking / reasoning tokens

Some models perform internal reasoning before producing a final answer. You can stream these thinking / reasoning tokens as they're generated by filtering [standard content blocks](/oss/python/langchain/messages#standard-content-blocks) for the `type` `"reasoning"`.

<Note>
  Reasoning output must be enabled on the model.

  See the [reasoning section](/oss/python/langchain/models#reasoning) and your [provider's integration page](/oss/python/integrations/providers/overview) for configuration details.

  To quickly check a model's reasoning support, see [models.dev](https://models.dev).
</Note>

To stream thinking tokens from an agent, use `stream_mode="messages"` and filter for reasoning content blocks:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain.agents import create_agent
from langchain.messages import AIMessageChunk
from langchain_anthropic import ChatAnthropic
from langchain_core.runnables import Runnable

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

model = ChatAnthropic(
    model_name="claude-sonnet-4-6",
    timeout=None,
    stop=None,
    thinking={"type": "enabled", "budget_tokens": 5000},
)
agent: Runnable = create_agent(
    model=model,
    tools=[get_weather],
)

for token, metadata in agent.stream(
    {"messages": [{"role": "user", "content": "What is the weather in SF?"}]},
    stream_mode="messages",  # [!code highlight]
):
    if not isinstance(token, AIMessageChunk):
        continue
    reasoning = [b for b in token.content_blocks if b["type"] == "reasoning"]
    text = [b for b in token.content_blocks if b["type"] == "text"]
    if reasoning:
        print(f"[thinking] {reasoning[0]['reasoning']}", end="")
    if text:
        print(text[0]["text"], end="")
```

```shell title="Output" theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
[thinking] The user is asking about the weather in San Francisco. I have a tool
[thinking]  available to get this information. Let me call the get_weather tool
[thinking]  with "San Francisco" as the city parameter.
The weather in San Francisco is: It's always sunny in San Francisco!
```

This works the same way regardless of the model provider—LangChain normalizes provider-specific formats (Anthropic `thinking` blocks, OpenAI `reasoning` summaries, etc.) into a standard `"reasoning"` content block type via the [`content_blocks`](/oss/python/langchain/messages#standard-content-blocks) property.

To stream reasoning tokens directly from a chat model (without an agent), see [streaming with chat models](/oss/python/langchain/models#reasoning).

### Streaming tool calls

You may want to stream both:

1. Partial JSON as [tool calls](/oss/python/langchain/models#tool-calling) are generated
2. The completed, parsed tool calls that are executed

Specifying [`stream_mode="messages"`](#llm-tokens) will stream incremental [message chunks](/oss/python/langchain/messages#streaming-and-chunks) generated by all LLM calls in the agent. To access the completed messages with parsed tool calls:

1. If those messages are tracked in the [state](/oss/python/langchain/short-term-memory) (as in the model node of [`create_agent`](/oss/python/langchain/agents)), use `stream_mode=["messages", "updates"]` to access completed messages through [state updates](#agent-progress) (demonstrated below).
2. If those messages are not tracked in the state, use [custom updates](#custom-updates) or aggregate the chunks during the streaming loop ([next section](#accessing-completed-messages)).

<Note>
  Refer to the section below on [streaming from sub-agents](#streaming-from-sub-agents) if your agent includes multiple LLMs.
</Note>

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from typing import Any

from langchain.agents import create_agent
from langchain.messages import AIMessage, AIMessageChunk, AnyMessage, ToolMessage

def get_weather(city: str) -> str:
    """Get weather for a given city."""

    return f"It's always sunny in {city}!"

agent = create_agent("openai:gpt-5.5", tools=[get_weather])

def _render_message_chunk(token: AIMessageChunk) -> None:
    if token.text:
        print(token.text, end="|")
    if token.tool_call_chunks:
        print(token.tool_call_chunks)
    # N.B. all content is available through token.content_blocks

def _render_completed_message(message: AnyMessage) -> None:
    if isinstance(message, AIMessage) and message.tool_calls:
        print(f"Tool calls: {message.tool_calls}")
    if isinstance(message, ToolMessage):
        print(f"Tool response: {message.content_blocks}")

input_message = {"role": "user", "content": "What is the weather in Boston?"}
for chunk in agent.stream(
    {"messages": [input_message]},
    stream_mode=["messages", "updates"],  # [!code highlight]
    version="v2",  # [!code highlight]
):
    if chunk["type"] == "messages":  # [!code highlight]
        token, metadata = chunk["data"]  # [!code highlight]
        if isinstance(token, AIMessageChunk):
            _render_message_chunk(token)  # [!code highlight]
    elif chunk["type"] == "updates":  # [!code highlight]
        for source, update in chunk["data"].items():  # [!code highlight]
            if source in ("model", "tools"):  # `source` captures node name
