# Run the agent
success_number = 18  [](https://ai.pydantic.dev/agent/#__code_0_annotation_3)
result = roulette_agent.run_sync('Put my money on square eighteen', deps=success_number)
print(result.output)  [](https://ai.pydantic.dev/agent/#__code_0_annotation_4)
#> True

result = roulette_agent.run_sync('I bet five is the winner', deps=success_number)
print(result.output)
#> False

```

roulette_wheel.py```
from pydantic_ai import Agent, RunContext

roulette_agent = Agent(

[](https://ai.pydantic.dev/agent/#__code_1_annotation_1)
    'openai:gpt-5.2',
    deps_type=int,
    output_type=bool,
    system_prompt=(
        'Use the `roulette_wheel` function to see if the '
        'customer has won based on the number they provide.'
    ),
)


@roulette_agent.tool
async def roulette_wheel(ctx: RunContext[int], square: int) -> str:

[](https://ai.pydantic.dev/agent/#__code_1_annotation_2)
    """check if the square is a winner"""
    return 'winner' if square == ctx.deps else 'loser'


# Run the agent
success_number = 18

[](https://ai.pydantic.dev/agent/#__code_1_annotation_3)
result = roulette_agent.run_sync('Put my money on square eighteen', deps=success_number)
print(result.output)

[](https://ai.pydantic.dev/agent/#__code_1_annotation_4)
#> True

result = roulette_agent.run_sync('I bet five is the winner', deps=success_number)
print(result.output)
#> False

```

  1. Create an agent, which expects an integer dependency and produces a boolean output. This agent will have type `Agent[int, bool]`.
  2. Define a tool that checks if the square is a winner. Here [`RunContext`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext



      dataclass
  ") is parameterized with the dependency type `int`; if you got the dependency type wrong you'd get a typing error.
  3. In reality, you might want to use a random number here e.g. `random.randint(0, 36)`.
  4. `result.output` will be a boolean indicating if the square is a winner. Pydantic performs the output validation, and it'll be typed as a `bool` since its type is derived from the `output_type` generic parameter of the agent.


Agents are designed for reuse, like FastAPI Apps
You can instantiate one agent and use it globally throughout your application, as you would a small
## Running Agents
There are five ways to run an agent:
  1. [`agent.run()`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AbstractAgent.run "run



      async
  ") — an async function which returns a [`RunResult`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AgentRunResult "AgentRunResult



      dataclass
  ") containing a completed response.
  2. [`agent.run_sync()`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AbstractAgent.run_sync "run_sync") — a plain, synchronous function which returns a [`RunResult`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AgentRunResult "AgentRunResult



      dataclass
  ") containing a completed response (internally, this just calls `loop.run_until_complete(self.run())`).
  3. [`agent.run_stream()`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AbstractAgent.run_stream "run_stream



      async
  ") — an async context manager which returns a [`StreamedRunResult`](https://ai.pydantic.dev/api/result/#pydantic_ai.result.StreamedRunResult "StreamedRunResult



      dataclass
  "), which contains methods to stream text and structured output as an async iterable. [`agent.run_stream_sync()`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AbstractAgent.run_stream_sync "run_stream_sync") is a synchronous variation that returns a [`StreamedRunResultSync`](https://ai.pydantic.dev/api/result/#pydantic_ai.result.StreamedRunResultSync "StreamedRunResultSync



      dataclass
  ") with synchronous versions of the same methods.
  4. [`agent.run_stream_events()`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AbstractAgent.run_stream_events "run_stream_events") — a function which returns an async iterable of [`AgentStreamEvent`s](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.AgentStreamEvent "AgentStreamEvent



      module-attribute
  ") and a [`AgentRunResultEvent`](https://ai.pydantic.dev/api/run/#pydantic_ai.run.AgentRunResultEvent "AgentRunResultEvent



      dataclass
  ") containing the final run result.
  5. [`agent.iter()`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.iter "iter



      async
  ") — a context manager which returns an [`AgentRun`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AgentRun "AgentRun



      dataclass
  "), an async iterable over the nodes of the agent's underlying [`Graph`](https://ai.pydantic.dev/api/pydantic_graph/graph/#pydantic_graph.graph.Graph "Graph



      dataclass
  ").


Here's a simple example demonstrating the first four:
[With Pydantic AI Gateway](https://ai.pydantic.dev/agent/#__tabbed_2_1)[Directly to Provider API](https://ai.pydantic.dev/agent/#__tabbed_2_2)
[Learn about Gateway](https://ai.pydantic.dev/gateway) run_agent.py```
from pydantic_ai import Agent, AgentRunResultEvent, AgentStreamEvent

agent = Agent('gateway/openai:gpt-5.2')

result_sync = agent.run_sync('What is the capital of Italy?')
print(result_sync.output)
#> The capital of Italy is Rome.


async def main():
    result = await agent.run('What is the capital of France?')
    print(result.output)
    #> The capital of France is Paris.

    async with agent.run_stream('What is the capital of the UK?') as response:
        async for text in response.stream_text():
            print(text)
            #> The capital of
            #> The capital of the UK is
            #> The capital of the UK is London.

    events: list[AgentStreamEvent | AgentRunResultEvent] = []
    async for event in agent.run_stream_events('What is the capital of Mexico?'):
        events.append(event)
    print(events)
    """
    [
        PartStartEvent(index=0, part=TextPart(content='The capital of ')),
        FinalResultEvent(tool_name=None, tool_call_id=None),
        PartDeltaEvent(index=0, delta=TextPartDelta(content_delta='Mexico is Mexico ')),
        PartDeltaEvent(index=0, delta=TextPartDelta(content_delta='City.')),
        PartEndEvent(
            index=0, part=TextPart(content='The capital of Mexico is Mexico City.')
        ),
        AgentRunResultEvent(
            result=AgentRunResult(output='The capital of Mexico is Mexico City.')
        ),
    ]
    """

```

run_agent.py```
from pydantic_ai import Agent, AgentRunResultEvent, AgentStreamEvent

agent = Agent('openai:gpt-5.2')

result_sync = agent.run_sync('What is the capital of Italy?')
print(result_sync.output)
#> The capital of Italy is Rome.


async def main():
    result = await agent.run('What is the capital of France?')
    print(result.output)
    #> The capital of France is Paris.

    async with agent.run_stream('What is the capital of the UK?') as response:
        async for text in response.stream_text():
            print(text)
            #> The capital of
            #> The capital of the UK is
            #> The capital of the UK is London.

    events: list[AgentStreamEvent | AgentRunResultEvent] = []
    async for event in agent.run_stream_events('What is the capital of Mexico?'):
        events.append(event)
    print(events)
    """
    [
        PartStartEvent(index=0, part=TextPart(content='The capital of ')),
        FinalResultEvent(tool_name=None, tool_call_id=None),
        PartDeltaEvent(index=0, delta=TextPartDelta(content_delta='Mexico is Mexico ')),
        PartDeltaEvent(index=0, delta=TextPartDelta(content_delta='City.')),
        PartEndEvent(
            index=0, part=TextPart(content='The capital of Mexico is Mexico City.')
        ),
        AgentRunResultEvent(
            result=AgentRunResult(output='The capital of Mexico is Mexico City.')
        ),
    ]
    """

```

_(This example is complete, it can be run "as is" — you'll need to add`asyncio.run(main())` to run `main`)_
You can also pass messages from previous runs to continue a conversation or provide context, as described in [Messages and Chat History](https://ai.pydantic.dev/message-history/).
### Streaming Events and Final Output
As shown in the example above, [`run_stream()`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AbstractAgent.run_stream "run_stream



      async
  ") makes it easy to stream the agent's final output as it comes in. It also takes an optional `event_stream_handler` argument that you can use to gain insight into what is happening during the run before the final output is produced.
The example below shows how to stream events and text output. You can also [stream structured output](https://ai.pydantic.dev/output/#streaming-structured-output).
Note
The `run_stream()` and `run_stream_sync()` methods will consider the first output that matches the [output type](https://ai.pydantic.dev/output/#structured-output) (which could be text, an [output tool](https://ai.pydantic.dev/output/#tool-output) call, or a [deferred](https://ai.pydantic.dev/deferred-tools/) tool call) to be the final output of the agent run, even when the model generates (additional) tool calls after this "final" output.
These "dangling" tool calls will not be executed unless the agent's [`end_strategy`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.end_strategy "end_strategy



      instance-attribute
  ") is set to `'exhaustive'`, and even then their results will not be sent back to the model as the agent run will already be considered completed. In short, if the model returns both tool calls and text, and the agent's output type is `str`, **the tool calls will not run** in streaming mode with the default setting.
If you want to always keep running the agent when it performs tool calls, and stream all events from the model's streaming response and the agent's execution of tools, use [`agent.run_stream_events()`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AbstractAgent.run_stream_events "run_stream_events") or [`agent.iter()`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AbstractAgent.iter "iter



      abstractmethod
      async
  ") instead, as described in the following sections.
[With Pydantic AI Gateway](https://ai.pydantic.dev/agent/#__tabbed_3_1)[Directly to Provider API](https://ai.pydantic.dev/agent/#__tabbed_3_2)
[Learn about Gateway](https://ai.pydantic.dev/gateway) run_stream_event_stream_handler.py```
import asyncio
from collections.abc import AsyncIterable
from datetime import date

from pydantic_ai import (
    Agent,
    AgentStreamEvent,
    FinalResultEvent,
    FunctionToolCallEvent,
    FunctionToolResultEvent,
    PartDeltaEvent,
    PartStartEvent,
    RunContext,
    TextPartDelta,
    ThinkingPartDelta,
    ToolCallPartDelta,
)

weather_agent = Agent(
    'gateway/openai:gpt-5.2',
    system_prompt='Providing a weather forecast at the locations the user provides.',
)


@weather_agent.tool
async def weather_forecast(
    ctx: RunContext,
    location: str,
    forecast_date: date,
) -> str:
    return f'The forecast in {location} on {forecast_date} is 24°C and sunny.'


output_messages: list[str] = []

async def handle_event(event: AgentStreamEvent):
    if isinstance(event, PartStartEvent):
        output_messages.append(f'[Request] Starting part {event.index}: {event.part!r}')
    elif isinstance(event, PartDeltaEvent):
        if isinstance(event.delta, TextPartDelta):
            output_messages.append(f'[Request] Part {event.index} text delta: {event.delta.content_delta!r}')
        elif isinstance(event.delta, ThinkingPartDelta):
            output_messages.append(f'[Request] Part {event.index} thinking delta: {event.delta.content_delta!r}')
        elif isinstance(event.delta, ToolCallPartDelta):
            output_messages.append(f'[Request] Part {event.index} args delta: {event.delta.args_delta}')
    elif isinstance(event, FunctionToolCallEvent):
        output_messages.append(
            f'[Tools] The LLM calls tool={event.part.tool_name!r} with args={event.part.args} (tool_call_id={event.part.tool_call_id!r})'
        )
    elif isinstance(event, FunctionToolResultEvent):
        output_messages.append(f'[Tools] Tool call {event.tool_call_id!r} returned => {event.result.content}')
    elif isinstance(event, FinalResultEvent):
        output_messages.append(f'[Result] The model starting producing a final result (tool_name={event.tool_name})')


async def event_stream_handler(
    ctx: RunContext,
    event_stream: AsyncIterable[AgentStreamEvent],
):
    async for event in event_stream:
        await handle_event(event)

async def main():
    user_prompt = 'What will the weather be like in Paris on Tuesday?'

    async with weather_agent.run_stream(user_prompt, event_stream_handler=event_stream_handler) as run:
        async for output in run.stream_text():
            output_messages.append(f'[Output] {output}')


if __name__ == '__main__':
    asyncio.run(main())

    print(output_messages)
    """
    [
        "[Request] Starting part 0: ToolCallPart(tool_name='weather_forecast', tool_call_id='0001')",
        '[Request] Part 0 args delta: {"location":"Pa',
        '[Request] Part 0 args delta: ris","forecast_',
        '[Request] Part 0 args delta: date":"2030-01-',
        '[Request] Part 0 args delta: 01"}',
        '[Tools] The LLM calls tool=\'weather_forecast\' with args={"location":"Paris","forecast_date":"2030-01-01"} (tool_call_id=\'0001\')',
        "[Tools] Tool call '0001' returned => The forecast in Paris on 2030-01-01 is 24°C and sunny.",
        "[Request] Starting part 0: TextPart(content='It will be ')",
        '[Result] The model starting producing a final result (tool_name=None)',
        '[Output] It will be ',
        '[Output] It will be warm and sunny ',
        '[Output] It will be warm and sunny in Paris on ',
        '[Output] It will be warm and sunny in Paris on Tuesday.',
    ]
    """

```

run_stream_event_stream_handler.py```
import asyncio
from collections.abc import AsyncIterable
from datetime import date

from pydantic_ai import (
    Agent,
    AgentStreamEvent,
    FinalResultEvent,
    FunctionToolCallEvent,
    FunctionToolResultEvent,
    PartDeltaEvent,
    PartStartEvent,
    RunContext,
    TextPartDelta,
    ThinkingPartDelta,
    ToolCallPartDelta,
)

weather_agent = Agent(
    'openai:gpt-5.2',
    system_prompt='Providing a weather forecast at the locations the user provides.',
)


@weather_agent.tool
async def weather_forecast(
    ctx: RunContext,
    location: str,
    forecast_date: date,
) -> str:
    return f'The forecast in {location} on {forecast_date} is 24°C and sunny.'


output_messages: list[str] = []

async def handle_event(event: AgentStreamEvent):
    if isinstance(event, PartStartEvent):
        output_messages.append(f'[Request] Starting part {event.index}: {event.part!r}')
    elif isinstance(event, PartDeltaEvent):
        if isinstance(event.delta, TextPartDelta):
            output_messages.append(f'[Request] Part {event.index} text delta: {event.delta.content_delta!r}')
        elif isinstance(event.delta, ThinkingPartDelta):
            output_messages.append(f'[Request] Part {event.index} thinking delta: {event.delta.content_delta!r}')
        elif isinstance(event.delta, ToolCallPartDelta):
            output_messages.append(f'[Request] Part {event.index} args delta: {event.delta.args_delta}')
    elif isinstance(event, FunctionToolCallEvent):
        output_messages.append(
            f'[Tools] The LLM calls tool={event.part.tool_name!r} with args={event.part.args} (tool_call_id={event.part.tool_call_id!r})'
        )
    elif isinstance(event, FunctionToolResultEvent):
        output_messages.append(f'[Tools] Tool call {event.tool_call_id!r} returned => {event.result.content}')
    elif isinstance(event, FinalResultEvent):
        output_messages.append(f'[Result] The model starting producing a final result (tool_name={event.tool_name})')


async def event_stream_handler(
    ctx: RunContext,
    event_stream: AsyncIterable[AgentStreamEvent],
):
    async for event in event_stream:
        await handle_event(event)

async def main():
    user_prompt = 'What will the weather be like in Paris on Tuesday?'

    async with weather_agent.run_stream(user_prompt, event_stream_handler=event_stream_handler) as run:
        async for output in run.stream_text():
            output_messages.append(f'[Output] {output}')


if __name__ == '__main__':
    asyncio.run(main())

    print(output_messages)
    """
    [
        "[Request] Starting part 0: ToolCallPart(tool_name='weather_forecast', tool_call_id='0001')",
        '[Request] Part 0 args delta: {"location":"Pa',
        '[Request] Part 0 args delta: ris","forecast_',
        '[Request] Part 0 args delta: date":"2030-01-',
        '[Request] Part 0 args delta: 01"}',
        '[Tools] The LLM calls tool=\'weather_forecast\' with args={"location":"Paris","forecast_date":"2030-01-01"} (tool_call_id=\'0001\')',
        "[Tools] Tool call '0001' returned => The forecast in Paris on 2030-01-01 is 24°C and sunny.",
        "[Request] Starting part 0: TextPart(content='It will be ')",
        '[Result] The model starting producing a final result (tool_name=None)',
        '[Output] It will be ',
        '[Output] It will be warm and sunny ',
        '[Output] It will be warm and sunny in Paris on ',
        '[Output] It will be warm and sunny in Paris on Tuesday.',
    ]
    """

```

_(This example is complete, it can be run "as is")_
### Streaming All Events
Like `agent.run_stream()`, [`agent.run()`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AbstractAgent.run_stream "run_stream



      async
  ") takes an optional `event_stream_handler` argument that lets you stream all events from the model's streaming response and the agent's execution of tools. Unlike `run_stream()`, it always runs the agent graph to completion even if text was received ahead of tool calls that looked like it could've been the final result.
For convenience, a [`agent.run_stream_events()`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AbstractAgent.run_stream_events "run_stream_events") method is also available as a wrapper around `run(event_stream_handler=...)`, which returns an async iterable of [`AgentStreamEvent`s](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.AgentStreamEvent "AgentStreamEvent



      module-attribute
  ") and a [`AgentRunResultEvent`](https://ai.pydantic.dev/api/run/#pydantic_ai.run.AgentRunResultEvent "AgentRunResultEvent



      dataclass
  ") containing the final run result.
Note
As they return raw events as they come in, the `run_stream_events()` and `run(event_stream_handler=...)` methods require you to piece together the streamed text and structured output yourself from the `PartStartEvent` and subsequent `PartDeltaEvent`s.
To get the best of both worlds, at the expense of some additional complexity, you can use [`agent.iter()`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AbstractAgent.iter "iter



      abstractmethod
      async
  ") as described in the next section, which lets you [iterate over the agent graph](https://ai.pydantic.dev/agent/#iterating-over-an-agents-graph) and [stream both events and output](https://ai.pydantic.dev/agent/#streaming-all-events-and-output) at every step.
run_events.py```
import asyncio

from pydantic_ai import AgentRunResultEvent

from run_stream_event_stream_handler import handle_event, output_messages, weather_agent


async def main():
    user_prompt = 'What will the weather be like in Paris on Tuesday?'

    async for event in weather_agent.run_stream_events(user_prompt):
        if isinstance(event, AgentRunResultEvent):
            output_messages.append(f'[Final Output] {event.result.output}')
        else:
            await handle_event(event)

if __name__ == '__main__':
    asyncio.run(main())

    print(output_messages)
    """
    [
        "[Request] Starting part 0: ToolCallPart(tool_name='weather_forecast', tool_call_id='0001')",
        '[Request] Part 0 args delta: {"location":"Pa',
        '[Request] Part 0 args delta: ris","forecast_',
        '[Request] Part 0 args delta: date":"2030-01-',
        '[Request] Part 0 args delta: 01"}',
        '[Tools] The LLM calls tool=\'weather_forecast\' with args={"location":"Paris","forecast_date":"2030-01-01"} (tool_call_id=\'0001\')',
        "[Tools] Tool call '0001' returned => The forecast in Paris on 2030-01-01 is 24°C and sunny.",
        "[Request] Starting part 0: TextPart(content='It will be ')",
        '[Result] The model starting producing a final result (tool_name=None)',
        "[Request] Part 0 text delta: 'warm and sunny '",
        "[Request] Part 0 text delta: 'in Paris on '",
        "[Request] Part 0 text delta: 'Tuesday.'",
        '[Final Output] It will be warm and sunny in Paris on Tuesday.',
    ]
    """

```

_(This example is complete, it can be run "as is")_
### Iterating Over an Agent's Graph
Under the hood, each `Agent` in Pydantic AI uses **pydantic-graph** to manage its execution flow. **pydantic-graph** is a generic, type-centric library for building and running finite state machines in Python. It doesn't actually depend on Pydantic AI — you can use it standalone for workflows that have nothing to do with GenAI — but Pydantic AI makes use of it to orchestrate the handling of model requests and model responses in an agent's run.
In many scenarios, you don't need to worry about pydantic-graph at all; calling `agent.run(...)` simply traverses the underlying graph from start to finish. However, if you need deeper insight or control — for example to inject your own logic at specific stages — Pydantic AI exposes the lower-level iteration process via [`Agent.iter`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.iter "iter



      async
  "). This method returns an [`AgentRun`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AgentRun "AgentRun



      dataclass
  "), which you can async-iterate over, or manually drive node-by-node via the [`next`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AgentRun.next "next



      async
  ") method. Once the agent's graph returns an [`End`](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.End "End



      dataclass
  "), you have the final result along with a detailed history of all steps.
####  `async for` iteration
Here's an example of using `async for` with `iter` to record each node the agent executes:
[With Pydantic AI Gateway](https://ai.pydantic.dev/agent/#__tabbed_4_1)[Directly to Provider API](https://ai.pydantic.dev/agent/#__tabbed_4_2)
[Learn about Gateway](https://ai.pydantic.dev/gateway) agent_iter_async_for.py```
from pydantic_ai import Agent

agent = Agent('gateway/openai:gpt-5.2')


async def main():
    nodes = []
    # Begin an AgentRun, which is an async-iterable over the nodes of the agent's graph
    async with agent.iter('What is the capital of France?') as agent_run:
        async for node in agent_run:
            # Each node represents a step in the agent's execution
            nodes.append(node)
    print(nodes)
    """
    [
        UserPromptNode(
            user_prompt='What is the capital of France?',
            instructions_functions=[],
            system_prompts=(),
            system_prompt_functions=[],
            system_prompt_dynamic_functions={},
        ),
        ModelRequestNode(
            request=ModelRequest(
                parts=[
                    UserPromptPart(
                        content='What is the capital of France?',
                        timestamp=datetime.datetime(...),
                    )
                ],
                timestamp=datetime.datetime(...),
                run_id='...',
            )
        ),
        CallToolsNode(
            model_response=ModelResponse(
                parts=[TextPart(content='The capital of France is Paris.')],
                usage=RequestUsage(input_tokens=56, output_tokens=7),
                model_name='gpt-5.2',
                timestamp=datetime.datetime(...),
                run_id='...',
            )
        ),
        End(data=FinalResult(output='The capital of France is Paris.')),
    ]
    """
    print(agent_run.result.output)
    #> The capital of France is Paris.

```

agent_iter_async_for.py```
from pydantic_ai import Agent

agent = Agent('openai:gpt-5.2')


async def main():
    nodes = []
    # Begin an AgentRun, which is an async-iterable over the nodes of the agent's graph
    async with agent.iter('What is the capital of France?') as agent_run:
        async for node in agent_run:
            # Each node represents a step in the agent's execution
            nodes.append(node)
    print(nodes)
    """
    [
        UserPromptNode(
            user_prompt='What is the capital of France?',
            instructions_functions=[],
            system_prompts=(),
            system_prompt_functions=[],
            system_prompt_dynamic_functions={},
        ),
        ModelRequestNode(
            request=ModelRequest(
                parts=[
                    UserPromptPart(
                        content='What is the capital of France?',
                        timestamp=datetime.datetime(...),
                    )
                ],
                timestamp=datetime.datetime(...),
                run_id='...',
            )
        ),
        CallToolsNode(
            model_response=ModelResponse(
                parts=[TextPart(content='The capital of France is Paris.')],
                usage=RequestUsage(input_tokens=56, output_tokens=7),
                model_name='gpt-5.2',
                timestamp=datetime.datetime(...),
                run_id='...',
            )
        ),
        End(data=FinalResult(output='The capital of France is Paris.')),
    ]
    """
    print(agent_run.result.output)
    #> The capital of France is Paris.

```

_(This example is complete, it can be run "as is" — you'll need to add`asyncio.run(main())` to run `main`)_
  * The `AgentRun` is an async iterator that yields each node (`BaseNode` or `End`) in the flow.
  * The run ends when an `End` node is returned.


#### Using `.next(...)` manually
You can also drive the iteration manually by passing the node you want to run next to the `AgentRun.next(...)` method. This allows you to inspect or modify the node before it executes or skip nodes based on your own logic, and to catch errors in `next()` more easily:
[With Pydantic AI Gateway](https://ai.pydantic.dev/agent/#__tabbed_5_1)[Directly to Provider API](https://ai.pydantic.dev/agent/#__tabbed_5_2)
[Learn about Gateway](https://ai.pydantic.dev/gateway) agent_iter_next.py```
from pydantic_ai import Agent
from pydantic_graph import End

agent = Agent('gateway/openai:gpt-5.2')


async def main():
    async with agent.iter('What is the capital of France?') as agent_run:
        node = agent_run.next_node  [](https://ai.pydantic.dev/agent/#__code_9_annotation_1)

        all_nodes = [node]

        # Drive the iteration manually:
        while not isinstance(node, End):  [](https://ai.pydantic.dev/agent/#__code_9_annotation_2)
            node = await agent_run.next(node)  [](https://ai.pydantic.dev/agent/#__code_9_annotation_3)
            all_nodes.append(node)  [](https://ai.pydantic.dev/agent/#__code_9_annotation_4)

        print(all_nodes)
        """
        [
            UserPromptNode(
                user_prompt='What is the capital of France?',
                instructions_functions=[],
                system_prompts=(),
                system_prompt_functions=[],
                system_prompt_dynamic_functions={},
            ),
            ModelRequestNode(
                request=ModelRequest(
                    parts=[
                        UserPromptPart(
                            content='What is the capital of France?',
                            timestamp=datetime.datetime(...),
                        )
                    ],
                    timestamp=datetime.datetime(...),
                    run_id='...',
                )
            ),
            CallToolsNode(
                model_response=ModelResponse(
                    parts=[TextPart(content='The capital of France is Paris.')],
                    usage=RequestUsage(input_tokens=56, output_tokens=7),
                    model_name='gpt-5.2',
                    timestamp=datetime.datetime(...),
                    run_id='...',
                )
            ),
            End(data=FinalResult(output='The capital of France is Paris.')),
        ]
        """

```

agent_iter_next.py```
from pydantic_ai import Agent
from pydantic_graph import End

agent = Agent('openai:gpt-5.2')


async def main():
    async with agent.iter('What is the capital of France?') as agent_run:
        node = agent_run.next_node

[](https://ai.pydantic.dev/agent/#__code_10_annotation_1)

        all_nodes = [node]

        # Drive the iteration manually:
        while not isinstance(node, End):

[](https://ai.pydantic.dev/agent/#__code_10_annotation_2)
            node = await agent_run.next(node)

[](https://ai.pydantic.dev/agent/#__code_10_annotation_3)
            all_nodes.append(node)

[](https://ai.pydantic.dev/agent/#__code_10_annotation_4)

        print(all_nodes)
        """
        [
            UserPromptNode(
                user_prompt='What is the capital of France?',
                instructions_functions=[],
                system_prompts=(),
                system_prompt_functions=[],
                system_prompt_dynamic_functions={},
            ),
            ModelRequestNode(
                request=ModelRequest(
                    parts=[
                        UserPromptPart(
                            content='What is the capital of France?',
                            timestamp=datetime.datetime(...),
                        )
                    ],
                    timestamp=datetime.datetime(...),
                    run_id='...',
                )
            ),
            CallToolsNode(
                model_response=ModelResponse(
                    parts=[TextPart(content='The capital of France is Paris.')],
                    usage=RequestUsage(input_tokens=56, output_tokens=7),
                    model_name='gpt-5.2',
                    timestamp=datetime.datetime(...),
                    run_id='...',
                )
            ),
            End(data=FinalResult(output='The capital of France is Paris.')),
        ]
        """

```

  1. We start by grabbing the first node that will be run in the agent's graph.
  2. The agent run is finished once an `End` node has been produced; instances of `End` cannot be passed to `next`.
  3. When you call `await agent_run.next(node)`, it executes that node in the agent's graph, updates the run's history, and returns the _next_ node to run.
  4. You could also inspect or mutate the new `node` here as needed.


_(This example is complete, it can be run "as is" — you'll need to add`asyncio.run(main())` to run `main`)_
#### Accessing usage and final output
You can retrieve usage statistics (tokens, requests, etc.) at any time from the [`AgentRun`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AgentRun "AgentRun



      dataclass
  ") object via `agent_run.usage()`. This method returns a [`RunUsage`](https://ai.pydantic.dev/api/usage/#pydantic_ai.usage.RunUsage "RunUsage



      dataclass
  ") object containing the usage data.
Once the run finishes, `agent_run.result` becomes an [`AgentRunResult`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AgentRunResult "AgentRunResult



      dataclass
  ") object containing the final output (and related metadata).
#### Streaming All Events and Output
Here is an example of streaming an agent run in combination with `async for` iteration:
streaming_iter.py```
import asyncio
from dataclasses import dataclass
from datetime import date

from pydantic_ai import (
    Agent,
    FinalResultEvent,
    FunctionToolCallEvent,
    FunctionToolResultEvent,
    PartDeltaEvent,
    PartStartEvent,
    RunContext,
    TextPartDelta,
    ThinkingPartDelta,
    ToolCallPartDelta,
)


@dataclass
class WeatherService:
    async def get_forecast(self, location: str, forecast_date: date) -> str:
        # In real code: call weather API, DB queries, etc.
        return f'The forecast in {location} on {forecast_date} is 24°C and sunny.'

    async def get_historic_weather(self, location: str, forecast_date: date) -> str:
        # In real code: call a historical weather API or DB
        return f'The weather in {location} on {forecast_date} was 18°C and partly cloudy.'


weather_agent = Agent[WeatherService, str](
    'openai:gpt-5.2',
    deps_type=WeatherService,
    output_type=str,  # We'll produce a final answer as plain text
    system_prompt='Providing a weather forecast at the locations the user provides.',
)


@weather_agent.tool
async def weather_forecast(
    ctx: RunContext[WeatherService],
    location: str,
    forecast_date: date,
) -> str:
    if forecast_date >= date.today():
        return await ctx.deps.get_forecast(location, forecast_date)
    else:
        return await ctx.deps.get_historic_weather(location, forecast_date)


output_messages: list[str] = []


async def main():
    user_prompt = 'What will the weather be like in Paris on Tuesday?'

    # Begin a node-by-node, streaming iteration
    async with weather_agent.iter(user_prompt, deps=WeatherService()) as run:
        async for node in run:
            if Agent.is_user_prompt_node(node):
                # A user prompt node => The user has provided input
                output_messages.append(f'=== UserPromptNode: {node.user_prompt} ===')
            elif Agent.is_model_request_node(node):
                # A model request node => We can stream tokens from the model's request
                output_messages.append('=== ModelRequestNode: streaming partial request tokens ===')
                async with node.stream(run.ctx) as request_stream:
                    final_result_found = False
                    async for event in request_stream:
                        if isinstance(event, PartStartEvent):
                            output_messages.append(f'[Request] Starting part {event.index}: {event.part!r}')
                        elif isinstance(event, PartDeltaEvent):
                            if isinstance(event.delta, TextPartDelta):
                                output_messages.append(
                                    f'[Request] Part {event.index} text delta: {event.delta.content_delta!r}'
                                )
                            elif isinstance(event.delta, ThinkingPartDelta):
                                output_messages.append(
                                    f'[Request] Part {event.index} thinking delta: {event.delta.content_delta!r}'
                                )
                            elif isinstance(event.delta, ToolCallPartDelta):
                                output_messages.append(
                                    f'[Request] Part {event.index} args delta: {event.delta.args_delta}'
                                )
                        elif isinstance(event, FinalResultEvent):
                            output_messages.append(
                                f'[Result] The model started producing a final result (tool_name={event.tool_name})'
                            )
                            final_result_found = True
                            break

                    if final_result_found:
                        # Once the final result is found, we can call `AgentStream.stream_text()` to stream the text.
                        # A similar `AgentStream.stream_output()` method is available to stream structured output.
                        async for output in request_stream.stream_text():
                            output_messages.append(f'[Output] {output}')
            elif Agent.is_call_tools_node(node):
                # A handle-response node => The model returned some data, potentially calls a tool
                output_messages.append('=== CallToolsNode: streaming partial response & tool usage ===')
                async with node.stream(run.ctx) as handle_stream:
                    async for event in handle_stream:
                        if isinstance(event, FunctionToolCallEvent):
                            output_messages.append(
                                f'[Tools] The LLM calls tool={event.part.tool_name!r} with args={event.part.args} (tool_call_id={event.part.tool_call_id!r})'
                            )
                        elif isinstance(event, FunctionToolResultEvent):
                            output_messages.append(
                                f'[Tools] Tool call {event.tool_call_id!r} returned => {event.result.content}'
                            )
            elif Agent.is_end_node(node):
                # Once an End node is reached, the agent run is complete
                assert run.result is not None
                assert run.result.output == node.data.output
                output_messages.append(f'=== Final Agent Output: {run.result.output} ===')


if __name__ == '__main__':
    asyncio.run(main())

    print(output_messages)
    """
    [
        '=== UserPromptNode: What will the weather be like in Paris on Tuesday? ===',
        '=== ModelRequestNode: streaming partial request tokens ===',
        "[Request] Starting part 0: ToolCallPart(tool_name='weather_forecast', tool_call_id='0001')",
        '[Request] Part 0 args delta: {"location":"Pa',
        '[Request] Part 0 args delta: ris","forecast_',
        '[Request] Part 0 args delta: date":"2030-01-',
        '[Request] Part 0 args delta: 01"}',
        '=== CallToolsNode: streaming partial response & tool usage ===',
        '[Tools] The LLM calls tool=\'weather_forecast\' with args={"location":"Paris","forecast_date":"2030-01-01"} (tool_call_id=\'0001\')',
        "[Tools] Tool call '0001' returned => The forecast in Paris on 2030-01-01 is 24°C and sunny.",
        '=== ModelRequestNode: streaming partial request tokens ===',
        "[Request] Starting part 0: TextPart(content='It will be ')",
        '[Result] The model started producing a final result (tool_name=None)',
        '[Output] It will be ',
        '[Output] It will be warm and sunny ',
        '[Output] It will be warm and sunny in Paris on ',
        '[Output] It will be warm and sunny in Paris on Tuesday.',
        '=== CallToolsNode: streaming partial response & tool usage ===',
        '=== Final Agent Output: It will be warm and sunny in Paris on Tuesday. ===',
    ]
    """

```

_(This example is complete, it can be run "as is")_
### Additional Configuration
#### Usage Limits
Pydantic AI offers a [`UsageLimits`](https://ai.pydantic.dev/api/usage/#pydantic_ai.usage.UsageLimits "UsageLimits



      dataclass
  ") structure to help you limit your usage (tokens, requests, and tool calls) on model runs.
You can apply these settings by passing the `usage_limits` argument to the `run{_sync,_stream}` functions.
Consider the following example, where we limit the number of response tokens:
[With Pydantic AI Gateway](https://ai.pydantic.dev/agent/#__tabbed_6_1)[Directly to Provider API](https://ai.pydantic.dev/agent/#__tabbed_6_2)
[Learn about Gateway](https://ai.pydantic.dev/gateway)```
from pydantic_ai import Agent, UsageLimitExceeded, UsageLimits

agent = Agent('gateway/anthropic:claude-sonnet-4-6')

result_sync = agent.run_sync(
    'What is the capital of Italy? Answer with just the city.',
    usage_limits=UsageLimits(response_tokens_limit=10),
)
print(result_sync.output)
#> Rome
print(result_sync.usage())
#> RunUsage(input_tokens=62, output_tokens=1, requests=1)

try:
    result_sync = agent.run_sync(
        'What is the capital of Italy? Answer with a paragraph.',
        usage_limits=UsageLimits(response_tokens_limit=10),
    )
except UsageLimitExceeded as e:
    print(e)
    #> Exceeded the output_tokens_limit of 10 (output_tokens=32)

```

```
from pydantic_ai import Agent, UsageLimitExceeded, UsageLimits

agent = Agent('anthropic:claude-sonnet-4-6')

result_sync = agent.run_sync(
    'What is the capital of Italy? Answer with just the city.',
    usage_limits=UsageLimits(response_tokens_limit=10),
)
print(result_sync.output)
#> Rome
print(result_sync.usage())
#> RunUsage(input_tokens=62, output_tokens=1, requests=1)

try:
    result_sync = agent.run_sync(
        'What is the capital of Italy? Answer with a paragraph.',
        usage_limits=UsageLimits(response_tokens_limit=10),
    )
except UsageLimitExceeded as e:
    print(e)
    #> Exceeded the output_tokens_limit of 10 (output_tokens=32)

```

Restricting the number of requests can be useful in preventing infinite loops or excessive tool calling:
[With Pydantic AI Gateway](https://ai.pydantic.dev/agent/#__tabbed_7_1)[Directly to Provider API](https://ai.pydantic.dev/agent/#__tabbed_7_2)
[Learn about Gateway](https://ai.pydantic.dev/gateway)```
from typing_extensions import TypedDict

from pydantic_ai import Agent, ModelRetry, UsageLimitExceeded, UsageLimits


class NeverOutputType(TypedDict):
    """
    Never ever coerce data to this type.
    """

    never_use_this: str


agent = Agent(
    'gateway/anthropic:claude-sonnet-4-6',
    retries=3,
    output_type=NeverOutputType,
    system_prompt='Any time you get a response, call the `infinite_retry_tool` to produce another response.',
)


@agent.tool_plain(retries=5)  [](https://ai.pydantic.dev/agent/#__code_14_annotation_1)
def infinite_retry_tool() -> int:
    raise ModelRetry('Please try again.')


try:
    result_sync = agent.run_sync(
        'Begin infinite retry loop!', usage_limits=UsageLimits(request_limit=3)  [](https://ai.pydantic.dev/agent/#__code_14_annotation_2)
    )
except UsageLimitExceeded as e:
    print(e)
    #> The next request would exceed the request_limit of 3

```

```
from typing_extensions import TypedDict

from pydantic_ai import Agent, ModelRetry, UsageLimitExceeded, UsageLimits


class NeverOutputType(TypedDict):
    """
    Never ever coerce data to this type.
    """

    never_use_this: str


agent = Agent(
    'anthropic:claude-sonnet-4-6',
    retries=3,
    output_type=NeverOutputType,
    system_prompt='Any time you get a response, call the `infinite_retry_tool` to produce another response.',
)


@agent.tool_plain(retries=5)

[](https://ai.pydantic.dev/agent/#__code_15_annotation_1)
def infinite_retry_tool() -> int:
    raise ModelRetry('Please try again.')


try:
    result_sync = agent.run_sync(
        'Begin infinite retry loop!', usage_limits=UsageLimits(request_limit=3)

[](https://ai.pydantic.dev/agent/#__code_15_annotation_2)
    )
except UsageLimitExceeded as e:
    print(e)
    #> The next request would exceed the request_limit of 3

```

  1. This tool has the ability to retry 5 times before erroring, simulating a tool that might get stuck in a loop.
  2. This run will error after 3 requests, preventing the infinite tool calling.


##### Capping tool calls
If you need a limit on the number of successful tool invocations within a single run, use `tool_calls_limit`:
[With Pydantic AI Gateway](https://ai.pydantic.dev/agent/#__tabbed_8_1)[Directly to Provider API](https://ai.pydantic.dev/agent/#__tabbed_8_2)
[Learn about Gateway](https://ai.pydantic.dev/gateway)```
from pydantic_ai import Agent
from pydantic_ai.exceptions import UsageLimitExceeded
from pydantic_ai.usage import UsageLimits

agent = Agent('gateway/anthropic:claude-sonnet-4-6')

@agent.tool_plain
def do_work() -> str:
    return 'ok'

try:
    # Allow at most one executed tool call in this run
    agent.run_sync('Please call the tool twice', usage_limits=UsageLimits(tool_calls_limit=1))
except UsageLimitExceeded as e:
    print(e)
    #> The next tool call(s) would exceed the tool_calls_limit of 1 (tool_calls=2).

```

```
from pydantic_ai import Agent
from pydantic_ai.exceptions import UsageLimitExceeded
from pydantic_ai.usage import UsageLimits

agent = Agent('anthropic:claude-sonnet-4-6')

@agent.tool_plain
def do_work() -> str:
    return 'ok'

try:
    # Allow at most one executed tool call in this run
    agent.run_sync('Please call the tool twice', usage_limits=UsageLimits(tool_calls_limit=1))
except UsageLimitExceeded as e:
    print(e)
    #> The next tool call(s) would exceed the tool_calls_limit of 1 (tool_calls=2).

```

Note
  * Usage limits are especially relevant if you've registered many tools. Use `request_limit` to bound the number of model turns, and `tool_calls_limit` to cap the number of successful tool executions within a run.
  * The `tool_calls_limit` is checked before executing tool calls. If the model returns parallel tool calls that would exceed the limit, no tools will be executed.


#### Model (Run) Settings
Pydantic AI offers a [`settings.ModelSettings`](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "ModelSettings") structure to help you fine tune your requests. This structure allows you to configure common parameters that influence the model's behavior, such as `temperature`, `max_tokens`, `timeout`, and more.
There are three ways to apply these settings, with a clear precedence order:
  1. **Model-level defaults** - Set when creating a model instance via the `settings` parameter. These serve as the base defaults for that model.
  2. **Agent-level defaults** - Set during [`Agent`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent "Agent



      dataclass
  ") initialization via the `model_settings` argument. These are merged with model defaults, with agent settings taking precedence.
  3. **Run-time overrides** - Passed to `run{_sync,_stream}` functions via the `model_settings` argument. These have the highest priority and are merged with the combined agent and model defaults.


For example, if you'd like to set the `temperature` setting to `0.0` to ensure less random behavior, you can do the following:
```
from pydantic_ai import Agent, ModelSettings
from pydantic_ai.models.openai import OpenAIChatModel
