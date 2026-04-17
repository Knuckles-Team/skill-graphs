# Second run, passing previous messages
result2 = agent.run_sync(
    'What was his most famous equation?',
    message_history=result1.new_messages(),

[](https://ai.pydantic.dev/agent/#__code_25_annotation_1)
)
print(result2.output)
#> Albert Einstein's most famous equation is (E = mc^2).

```

  1. Continue the conversation; without `message_history` the model would not know who "his" was referring to.


_(This example is complete, it can be run "as is")_
## Type safe by design
Pydantic AI is designed to work well with static type checkers, like mypy and pyright.
Typing is (somewhat) optional
Pydantic AI is designed to make type checking as useful as possible for you if you choose to use it, but you don't have to use types everywhere all the time.
That said, because Pydantic AI uses Pydantic, and Pydantic uses type hints as the definition for schema and validation, some types (specifically type hints on parameters to tools, and the `output_type` arguments to [`Agent`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent "Agent



      dataclass
  ")) are used at runtime.
We (the library developers) have messed up if type hints are confusing you more than helping you, if you find this, please create an
In particular, agents are generic in both the type of their dependencies and the type of the outputs they return, so you can use the type hints to ensure you're using the right types.
Consider the following script with type mistakes:
type_mistakes.py```
from dataclasses import dataclass

from pydantic_ai import Agent, RunContext


@dataclass
class User:
    name: str


agent = Agent(
    'test',
    deps_type=User,  [](https://ai.pydantic.dev/agent/#__code_26_annotation_1)
    output_type=bool,
)


@agent.system_prompt
def add_user_name(ctx: RunContext[str]) -> str:  [](https://ai.pydantic.dev/agent/#__code_26_annotation_2)
    return f"The user's name is {ctx.deps}."


def foobar(x: bytes) -> None:
    pass


result = agent.run_sync('Does their name start with "A"?', deps=User('Anne'))
foobar(result.output)  [](https://ai.pydantic.dev/agent/#__code_26_annotation_3)

```

Running `mypy` on this will give the following output:
```
➤ uv run mypy type_mistakes.py
type_mistakes.py:18: error: Argument 1 to "system_prompt" of "Agent" has incompatible type "Callable[[RunContext[str]], str]"; expected "Callable[[RunContext[User]], str]"  [arg-type]
type_mistakes.py:28: error: Argument 1 to "foobar" has incompatible type "bool"; expected "bytes"  [arg-type]
Found 2 errors in 1 file (checked 1 source file)

```

Running `pyright` would identify the same issues.
## System Prompts
System prompts might seem simple at first glance since they're just strings (or sequences of strings that are concatenated), but crafting the right system prompt is key to getting the model to behave as you want.
Tip
For most use cases, you should use `instructions` instead of "system prompts".
If you know what you are doing though and want to preserve system prompt messages in the message history sent to the LLM in subsequent completions requests, you can achieve this using the `system_prompt` argument/decorator.
See the section below on [Instructions](https://ai.pydantic.dev/agent/#instructions) for more information.
Generally, system prompts fall into two categories:
  1. **Static system prompts** : These are known when writing the code and can be defined via the `system_prompt` parameter of the [`Agent` constructor](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.__init__ "__init__").
  2. **Dynamic system prompts** : These depend in some way on context that isn't known until runtime, and should be defined via functions decorated with [`@agent.system_prompt`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.system_prompt "system_prompt").


You can add both to a single agent; they're appended in the order they're defined at runtime.
Here's an example using both types of system prompts:
[With Pydantic AI Gateway](https://ai.pydantic.dev/agent/#__tabbed_12_1)[Directly to Provider API](https://ai.pydantic.dev/agent/#__tabbed_12_2)
[Learn about Gateway](https://ai.pydantic.dev/gateway) system_prompts.py```
from datetime import date

from pydantic_ai import Agent, RunContext

agent = Agent(
    'gateway/openai:gpt-5.2',
    deps_type=str,  [](https://ai.pydantic.dev/agent/#__code_28_annotation_1)
    system_prompt="Use the customer's name while replying to them.",  [](https://ai.pydantic.dev/agent/#__code_28_annotation_2)
)


@agent.system_prompt  [](https://ai.pydantic.dev/agent/#__code_28_annotation_3)
def add_the_users_name(ctx: RunContext[str]) -> str:
    return f"The user's name is {ctx.deps}."


@agent.system_prompt
def add_the_date() -> str:  [](https://ai.pydantic.dev/agent/#__code_28_annotation_4)
    return f'The date is {date.today()}.'


result = agent.run_sync('What is the date?', deps='Frank')
print(result.output)
#> Hello Frank, the date today is 2032-01-02.

```

system_prompts.py```
from datetime import date

from pydantic_ai import Agent, RunContext

agent = Agent(
    'openai:gpt-5.2',
    deps_type=str,

[](https://ai.pydantic.dev/agent/#__code_29_annotation_1)
    system_prompt="Use the customer's name while replying to them.",

[](https://ai.pydantic.dev/agent/#__code_29_annotation_2)
)


@agent.system_prompt

[](https://ai.pydantic.dev/agent/#__code_29_annotation_3)
def add_the_users_name(ctx: RunContext[str]) -> str:
    return f"The user's name is {ctx.deps}."


@agent.system_prompt
def add_the_date() -> str:

[](https://ai.pydantic.dev/agent/#__code_29_annotation_4)
    return f'The date is {date.today()}.'


result = agent.run_sync('What is the date?', deps='Frank')
print(result.output)
#> Hello Frank, the date today is 2032-01-02.

```

  1. The agent expects a string dependency.
  2. Static system prompt defined at agent creation time.
  3. Dynamic system prompt defined via a decorator with [`RunContext`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext



      dataclass
  "), this is called just after `run_sync`, not when the agent is created, so can benefit from runtime information like the dependencies used on that run.
  4. Another dynamic system prompt, system prompts don't have to have the `RunContext` parameter.


_(This example is complete, it can be run "as is")_
## Instructions
Instructions are similar to system prompts. The main difference is that when an explicit `message_history` is provided in a call to `Agent.run` and similar methods, _instructions_ from any existing messages in the history are not included in the request to the model — only the instructions of the _current_ agent are included.
You should use:
  * `instructions` when you want your request to the model to only include system prompts for the _current_ agent
  * `system_prompt` when you want your request to the model to _retain_ the system prompts used in previous requests (possibly made using other agents)


In general, we recommend using `instructions` instead of `system_prompt` unless you have a specific reason to use `system_prompt`.
Instructions, like system prompts, can be specified at different times:
  1. **Static instructions** : These are known when writing the code and can be defined via the `instructions` parameter of the [`Agent` constructor](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.__init__ "__init__").
  2. **Dynamic instructions** : These rely on context that is only available at runtime and should be defined using functions decorated with [`@agent.instructions`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.instructions "instructions"). Unlike dynamic system prompts, which may be reused when `message_history` is present, dynamic instructions are always reevaluated.
  3. **Runtime instructions** : These are additional instructions for a specific run that can be passed to one of the [run methods](https://ai.pydantic.dev/agent/#running-agents) using the `instructions` argument.


All three types of instructions can be added to a single agent, and they are appended in the order they are defined at runtime.
Here's an example using a static instruction as well as dynamic instructions:
[With Pydantic AI Gateway](https://ai.pydantic.dev/agent/#__tabbed_13_1)[Directly to Provider API](https://ai.pydantic.dev/agent/#__tabbed_13_2)
[Learn about Gateway](https://ai.pydantic.dev/gateway) instructions.py```
from datetime import date

from pydantic_ai import Agent, RunContext

agent = Agent(
    'gateway/openai:gpt-5.2',
    deps_type=str,  [](https://ai.pydantic.dev/agent/#__code_30_annotation_1)
    instructions="Use the customer's name while replying to them.",  [](https://ai.pydantic.dev/agent/#__code_30_annotation_2)
)


@agent.instructions  [](https://ai.pydantic.dev/agent/#__code_30_annotation_3)
def add_the_users_name(ctx: RunContext[str]) -> str:
    return f"The user's name is {ctx.deps}."


@agent.instructions
def add_the_date() -> str:  [](https://ai.pydantic.dev/agent/#__code_30_annotation_4)
    return f'The date is {date.today()}.'


result = agent.run_sync('What is the date?', deps='Frank')
print(result.output)
#> Hello Frank, the date today is 2032-01-02.

```

instructions.py```
from datetime import date

from pydantic_ai import Agent, RunContext

agent = Agent(
    'openai:gpt-5.2',
    deps_type=str,

[](https://ai.pydantic.dev/agent/#__code_31_annotation_1)
    instructions="Use the customer's name while replying to them.",

[](https://ai.pydantic.dev/agent/#__code_31_annotation_2)
)


@agent.instructions

[](https://ai.pydantic.dev/agent/#__code_31_annotation_3)
def add_the_users_name(ctx: RunContext[str]) -> str:
    return f"The user's name is {ctx.deps}."


@agent.instructions
def add_the_date() -> str:

[](https://ai.pydantic.dev/agent/#__code_31_annotation_4)
    return f'The date is {date.today()}.'


result = agent.run_sync('What is the date?', deps='Frank')
print(result.output)
#> Hello Frank, the date today is 2032-01-02.

```

  1. The agent expects a string dependency.
  2. Static instructions defined at agent creation time.
  3. Dynamic instructions defined via a decorator with [`RunContext`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext



      dataclass
  "), this is called just after `run_sync`, not when the agent is created, so can benefit from runtime information like the dependencies used on that run.
  4. Another dynamic instruction, instructions don't have to have the `RunContext` parameter.


_(This example is complete, it can be run "as is")_
Note that returning an empty string will result in no instruction message added.
## Reflection and self-correction
Validation errors from both function tool parameter validation and [structured output validation](https://ai.pydantic.dev/output/#structured-output) can be passed back to the model with a request to retry.
You can also raise [`ModelRetry`](https://ai.pydantic.dev/api/exceptions/#pydantic_ai.exceptions.ModelRetry "ModelRetry") from within a [tool](https://ai.pydantic.dev/tools/) or [output function](https://ai.pydantic.dev/output/#output-functions) to tell the model it should retry generating a response.
  * The default retry count is **1** but can be altered for the [entire agent](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.__init__ "__init__"), a [specific tool](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.tool "tool"), or [outputs](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.__init__ "__init__").
  * You can access the current retry count from within a tool, output validator, or output function via [`ctx.retry`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext.retry "retry



      class-attribute
      instance-attribute
  ").


Here's an example:
[With Pydantic AI Gateway](https://ai.pydantic.dev/agent/#__tabbed_14_1)[Directly to Provider API](https://ai.pydantic.dev/agent/#__tabbed_14_2)
[Learn about Gateway](https://ai.pydantic.dev/gateway) tool_retry.py```
from pydantic import BaseModel

from pydantic_ai import Agent, RunContext, ModelRetry

from fake_database import DatabaseConn


class ChatResult(BaseModel):
    user_id: int
    message: str


agent = Agent(
    'gateway/openai:gpt-5.2',
    deps_type=DatabaseConn,
    output_type=ChatResult,
)


@agent.tool(retries=2)
def get_user_by_name(ctx: RunContext[DatabaseConn], name: str) -> int:
    """Get a user's ID from their full name."""
    print(name)
    #> John
    #> John Doe
    user_id = ctx.deps.users.get(name=name)
    if user_id is None:
        raise ModelRetry(
            f'No user found with name {name!r}, remember to provide their full name'
        )
    return user_id


result = agent.run_sync(
    'Send a message to John Doe asking for coffee next week', deps=DatabaseConn()
)
print(result.output)
"""
user_id=123 message='Hello John, would you be free for coffee sometime next week? Let me know what works for you!'
"""

```

tool_retry.py```
from pydantic import BaseModel

from pydantic_ai import Agent, RunContext, ModelRetry

from fake_database import DatabaseConn


class ChatResult(BaseModel):
    user_id: int
    message: str


agent = Agent(
    'openai:gpt-5.2',
    deps_type=DatabaseConn,
    output_type=ChatResult,
)


@agent.tool(retries=2)
def get_user_by_name(ctx: RunContext[DatabaseConn], name: str) -> int:
    """Get a user's ID from their full name."""
    print(name)
    #> John
    #> John Doe
    user_id = ctx.deps.users.get(name=name)
    if user_id is None:
        raise ModelRetry(
            f'No user found with name {name!r}, remember to provide their full name'
        )
    return user_id


result = agent.run_sync(
    'Send a message to John Doe asking for coffee next week', deps=DatabaseConn()
)
print(result.output)
"""
user_id=123 message='Hello John, would you be free for coffee sometime next week? Let me know what works for you!'
"""

```

## Debugging and Monitoring
Agents require a different approach to observability than traditional software. With traditional web endpoints or data pipelines, you can largely predict behavior by reading the code. With agents, this is much harder. The model's decisions are stochastic, and that stochasticity compounds through the agentic loop as the agent reasons, calls tools, observes results, and reasons again. You need to actually see what happened.
This means setting up your application to record what's happening in a way you can review afterward, both during development (to understand and iterate) and in production (to debug issues and monitor behavior). The ergonomics matter too: a plaintext dump of everything that happened isn't a practical way to review agent behavior, even during development. You want tooling that lets you step through each decision and tool call interactively.
We recommend [Pydantic Logfire](https://logfire.pydantic.dev/docs/), which has been designed with Pydantic AI workflows in mind.
### Tracing with Logfire
```
import logfire

logfire.configure()
logfire.instrument_pydantic_ai()

```

With Logfire instrumentation enabled, every agent run creates a detailed trace showing:
  * **Messages exchanged** with the model (system, user, assistant)
  * **Tool calls** including arguments and return values
  * **Token usage** per request and cumulative
  * **Latency** for each operation
  * **Errors** with full context


This visibility is invaluable for:
  * Understanding why an agent made a specific decision
  * Debugging unexpected behavior
  * Optimizing performance and costs
  * Monitoring production deployments


### Systematic Testing with Evals
For systematic evaluation of agent behavior beyond runtime debugging, [Pydantic Evals](https://ai.pydantic.dev/evals/) provides a code-first framework for testing AI systems:
```
from pydantic_evals import Case, Dataset

dataset = Dataset(
    cases=[
        Case(name='capital_question', inputs='What is the capital of France?', expected_output='Paris'),
    ]
)
report = dataset.evaluate_sync(my_agent_function)

```

Evals let you define test cases, run them against your agent, and score the results. When combined with Logfire, evaluation results appear in the web UI for visualization and comparison across runs. See the [Logfire integration guide](https://ai.pydantic.dev/evals/how-to/logfire-integration/) for setup.
### Using Other Backends
Pydantic AI's instrumentation is built on [alternative backends](https://ai.pydantic.dev/logfire/#using-opentelemetry) for setup instructions.
[Full Logfire integration guide →](https://ai.pydantic.dev/logfire/)
## Model errors
If models behave unexpectedly (e.g., the retry limit is exceeded, or their API returns `503`), agent runs will raise [`UnexpectedModelBehavior`](https://ai.pydantic.dev/api/exceptions/#pydantic_ai.exceptions.UnexpectedModelBehavior "UnexpectedModelBehavior").
In these cases, [`capture_run_messages`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.capture_run_messages "capture_run_messages") can be used to access the messages exchanged during the run to help diagnose the issue.
[With Pydantic AI Gateway](https://ai.pydantic.dev/agent/#__tabbed_15_1)[Directly to Provider API](https://ai.pydantic.dev/agent/#__tabbed_15_2)
[Learn about Gateway](https://ai.pydantic.dev/gateway) agent_model_errors.py```
from pydantic_ai import Agent, ModelRetry, UnexpectedModelBehavior, capture_run_messages

agent = Agent('gateway/openai:gpt-5.2')


@agent.tool_plain
def calc_volume(size: int) -> int:  [](https://ai.pydantic.dev/agent/#__code_36_annotation_1)
    if size == 42:
        return size**3
    else:
        raise ModelRetry('Please try again.')


with capture_run_messages() as messages:  [](https://ai.pydantic.dev/agent/#__code_36_annotation_2)
    try:
        result = agent.run_sync('Please get me the volume of a box with size 6.')
    except UnexpectedModelBehavior as e:
        print('An error occurred:', e)
        #> An error occurred: Tool 'calc_volume' exceeded max retries count of 1
        print('cause:', repr(e.__cause__))
        #> cause: ModelRetry('Please try again.')
        print('messages:', messages)
        """
        messages:
        [
            ModelRequest(
                parts=[
                    UserPromptPart(
                        content='Please get me the volume of a box with size 6.',
                        timestamp=datetime.datetime(...),
                    )
                ],
                timestamp=datetime.datetime(...),
                run_id='...',
            ),
            ModelResponse(
                parts=[
                    ToolCallPart(
                        tool_name='calc_volume',
                        args={'size': 6},
                        tool_call_id='pyd_ai_tool_call_id',
                    )
                ],
                usage=RequestUsage(input_tokens=62, output_tokens=4),
                model_name='gpt-5.2',
                timestamp=datetime.datetime(...),
                run_id='...',
            ),
            ModelRequest(
                parts=[
                    RetryPromptPart(
                        content='Please try again.',
                        tool_name='calc_volume',
                        tool_call_id='pyd_ai_tool_call_id',
                        timestamp=datetime.datetime(...),
                    )
                ],
                timestamp=datetime.datetime(...),
                run_id='...',
            ),
            ModelResponse(
                parts=[
                    ToolCallPart(
                        tool_name='calc_volume',
                        args={'size': 6},
                        tool_call_id='pyd_ai_tool_call_id',
                    )
                ],
                usage=RequestUsage(input_tokens=72, output_tokens=8),
                model_name='gpt-5.2',
                timestamp=datetime.datetime(...),
                run_id='...',
            ),
        ]
        """
    else:
        print(result.output)

```

agent_model_errors.py```
from pydantic_ai import Agent, ModelRetry, UnexpectedModelBehavior, capture_run_messages

agent = Agent('openai:gpt-5.2')


@agent.tool_plain
def calc_volume(size: int) -> int:

[](https://ai.pydantic.dev/agent/#__code_37_annotation_1)
    if size == 42:
        return size**3
    else:
        raise ModelRetry('Please try again.')


with capture_run_messages() as messages:

[](https://ai.pydantic.dev/agent/#__code_37_annotation_2)
    try:
        result = agent.run_sync('Please get me the volume of a box with size 6.')
    except UnexpectedModelBehavior as e:
        print('An error occurred:', e)
        #> An error occurred: Tool 'calc_volume' exceeded max retries count of 1
        print('cause:', repr(e.__cause__))
        #> cause: ModelRetry('Please try again.')
        print('messages:', messages)
        """
        messages:
        [
            ModelRequest(
                parts=[
                    UserPromptPart(
                        content='Please get me the volume of a box with size 6.',
                        timestamp=datetime.datetime(...),
                    )
                ],
                timestamp=datetime.datetime(...),
                run_id='...',
            ),
            ModelResponse(
                parts=[
                    ToolCallPart(
                        tool_name='calc_volume',
                        args={'size': 6},
                        tool_call_id='pyd_ai_tool_call_id',
                    )
                ],
                usage=RequestUsage(input_tokens=62, output_tokens=4),
                model_name='gpt-5.2',
                timestamp=datetime.datetime(...),
                run_id='...',
            ),
            ModelRequest(
                parts=[
                    RetryPromptPart(
                        content='Please try again.',
                        tool_name='calc_volume',
                        tool_call_id='pyd_ai_tool_call_id',
                        timestamp=datetime.datetime(...),
                    )
                ],
                timestamp=datetime.datetime(...),
                run_id='...',
            ),
            ModelResponse(
                parts=[
                    ToolCallPart(
                        tool_name='calc_volume',
                        args={'size': 6},
                        tool_call_id='pyd_ai_tool_call_id',
                    )
                ],
                usage=RequestUsage(input_tokens=72, output_tokens=8),
                model_name='gpt-5.2',
                timestamp=datetime.datetime(...),
                run_id='...',
            ),
        ]
        """
    else:
        print(result.output)

```

  1. Define a tool that will raise `ModelRetry` repeatedly in this case.
  2. [`capture_run_messages`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.capture_run_messages "capture_run_messages") is used to capture the messages exchanged during the run.


_(This example is complete, it can be run "as is")_
Note
If you call [`run`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AbstractAgent.run "run



      async
  "), [`run_sync`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AbstractAgent.run_sync "run_sync"), or [`run_stream`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AbstractAgent.run_stream "run_stream



      async
  ") more than once within a single `capture_run_messages` context, `messages` will represent the messages exchanged during the first call only.
© Pydantic Services Inc. 2024 to present
