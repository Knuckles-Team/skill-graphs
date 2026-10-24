# Agents
## Introduction
Agents are Pydantic AI's primary interface for interacting with LLMs.
In some use cases a single Agent will control an entire application or component, but multiple agents can also interact to embody more complex workflows.
The [`Agent`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent "Agent



      dataclass
  ") class has full API documentation, but conceptually you can think of an agent as a container for:
**Component** | **Description**
---|---
[Instructions](https://ai.pydantic.dev/agent/#instructions) | A set of instructions for the LLM written by the developer.
[Function tool(s)](https://ai.pydantic.dev/tools/) and [toolsets](https://ai.pydantic.dev/toolsets/) | Functions that the LLM may call to get information while generating a response.
[Structured output type](https://ai.pydantic.dev/output/) | The structured datatype the LLM must return at the end of a run, if specified.
[Dependency type constraint](https://ai.pydantic.dev/dependencies/) | Dynamic instructions functions, tools, and output functions may all use dependencies when they're run.
[LLM model](https://ai.pydantic.dev/api/models/base/) | Optional default LLM model associated with the agent. Can also be specified when running the agent.
[Model Settings](https://ai.pydantic.dev/agent/#additional-configuration) | Optional default model settings to help fine tune requests. Can also be specified when running the agent.
In typing terms, agents are generic in their dependency and output types, e.g., an agent which required dependencies of type `Foobar` and produced outputs of type `list[str]` would have type `Agent[Foobar, list[str]]`. In practice, you shouldn't need to care about this, it should just mean your IDE can tell you when you have the right type, and if you choose to use [static type checking](https://ai.pydantic.dev/agent/#static-type-checking) it should work well with Pydantic AI.
Here's a toy example of an agent that simulates a roulette wheel:
[With Pydantic AI Gateway](https://ai.pydantic.dev/agent/#__tabbed_1_1)[Directly to Provider API](https://ai.pydantic.dev/agent/#__tabbed_1_2)
[Learn about Gateway](https://ai.pydantic.dev/gateway) roulette_wheel.py```
from pydantic_ai import Agent, RunContext

roulette_agent = Agent(  [](https://ai.pydantic.dev/agent/#__code_0_annotation_1)
    'gateway/openai:gpt-5.2',
    deps_type=int,
    output_type=bool,
    system_prompt=(
        'Use the `roulette_wheel` function to see if the '
        'customer has won based on the number they provide.'
    ),
)


@roulette_agent.tool
async def roulette_wheel(ctx: RunContext[int], square: int) -> str:  [](https://ai.pydantic.dev/agent/#__code_0_annotation_2)
    """check if the square is a winner"""
    return 'winner' if square == ctx.deps else 'loser'
