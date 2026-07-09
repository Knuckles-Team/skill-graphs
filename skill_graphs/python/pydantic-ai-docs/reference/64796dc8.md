## Streamed Results
There two main challenges with streamed results:
  1. Validating structured responses before they're complete, this is achieved by "partial validation" which was recently added to Pydantic in
  2. When receiving a response, we don't know if it's the final response without starting to stream it and peeking at the content. Pydantic AI streams just enough of the response to sniff out if it's a tool call or an output, then streams the whole thing and calls tools, or returns the stream as a [`StreamedRunResult`](https://ai.pydantic.dev/api/result/#pydantic_ai.result.StreamedRunResult "StreamedRunResult



      dataclass
  ").


Note
As the `run_stream()` method will consider the first output matching the `output_type` to be the final output, it will stop running the agent graph and will not execute any tool calls made by the model after this "final" output.
If you want to always run the agent graph to completion and stream all events from the model's streaming response and the agent's execution of tools, use [`agent.run_stream_events()`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AbstractAgent.run_stream_events "run_stream_events") ([docs](https://ai.pydantic.dev/agent/#streaming-all-events)) or [`agent.iter()`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AbstractAgent.iter "iter



      abstractmethod
      async
  ") ([docs](https://ai.pydantic.dev/agent/#streaming-all-events-and-output)) instead.
### Streaming Text
Example of streamed text output:
[With Pydantic AI Gateway](https://ai.pydantic.dev/output/#__tabbed_13_1)[Directly to Provider API](https://ai.pydantic.dev/output/#__tabbed_13_2)
[Learn about Gateway](https://ai.pydantic.dev/gateway) streamed_hello_world.py```
from pydantic_ai import Agent

agent = Agent('gateway/gemini:gemini-3-flash-preview')  [](https://ai.pydantic.dev/output/#__code_27_annotation_1)


async def main():
    async with agent.run_stream('Where does "hello world" come from?') as result:  [](https://ai.pydantic.dev/output/#__code_27_annotation_2)
        async for message in result.stream_text():  [](https://ai.pydantic.dev/output/#__code_27_annotation_3)
            print(message)
            #> The first known
            #> The first known use of "hello,
            #> The first known use of "hello, world" was in
            #> The first known use of "hello, world" was in a 1974 textbook
            #> The first known use of "hello, world" was in a 1974 textbook about the C
            #> The first known use of "hello, world" was in a 1974 textbook about the C programming language.

```

streamed_hello_world.py```
from pydantic_ai import Agent

agent = Agent('google-gla:gemini-3-flash-preview')

[](https://ai.pydantic.dev/output/#__code_28_annotation_1)


async def main():
    async with agent.run_stream('Where does "hello world" come from?') as result:

[](https://ai.pydantic.dev/output/#__code_28_annotation_2)
        async for message in result.stream_text():

[](https://ai.pydantic.dev/output/#__code_28_annotation_3)
            print(message)
            #> The first known
            #> The first known use of "hello,
            #> The first known use of "hello, world" was in
            #> The first known use of "hello, world" was in a 1974 textbook
            #> The first known use of "hello, world" was in a 1974 textbook about the C
            #> The first known use of "hello, world" was in a 1974 textbook about the C programming language.

```

  1. Streaming works with the standard [`Agent`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent "Agent



      dataclass
  ") class, and doesn't require any special setup, just a model that supports streaming (currently all models support streaming).
  2. The [`Agent.run_stream()`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AbstractAgent.run_stream "run_stream



      async
  ") method is used to start a streamed run, this method returns a context manager so the connection can be closed when the stream completes.
  3. Each item yield by [`StreamedRunResult.stream_text()`](https://ai.pydantic.dev/api/result/#pydantic_ai.result.StreamedRunResult.stream_text "stream_text



      async
  ") is the complete text response, extended as new data is received.


_(This example is complete, it can be run "as is" — you'll need to add`asyncio.run(main())` to run `main`)_
We can also stream text as deltas rather than the entire text in each item:
[With Pydantic AI Gateway](https://ai.pydantic.dev/output/#__tabbed_14_1)[Directly to Provider API](https://ai.pydantic.dev/output/#__tabbed_14_2)
[Learn about Gateway](https://ai.pydantic.dev/gateway) streamed_delta_hello_world.py```
from pydantic_ai import Agent

agent = Agent('gateway/gemini:gemini-3-flash-preview')


async def main():
    async with agent.run_stream('Where does "hello world" come from?') as result:
        async for message in result.stream_text(delta=True):  [](https://ai.pydantic.dev/output/#__code_29_annotation_1)
            print(message)
            #> The first known
            #> use of "hello,
            #> world" was in
            #> a 1974 textbook
            #> about the C
            #> programming language.

```

streamed_delta_hello_world.py```
from pydantic_ai import Agent

agent = Agent('google-gla:gemini-3-flash-preview')


async def main():
    async with agent.run_stream('Where does "hello world" come from?') as result:
        async for message in result.stream_text(delta=True):

[](https://ai.pydantic.dev/output/#__code_30_annotation_1)
            print(message)
            #> The first known
            #> use of "hello,
            #> world" was in
            #> a 1974 textbook
            #> about the C
            #> programming language.

```

  1. [`stream_text`](https://ai.pydantic.dev/api/result/#pydantic_ai.result.StreamedRunResult.stream_text "stream_text



      async
  ") will error if the response is not text.


_(This example is complete, it can be run "as is" — you'll need to add`asyncio.run(main())` to run `main`)_
Output message not included in `messages`
The final output message will **NOT** be added to result messages if you use `.stream_text(delta=True)`, see [Messages and chat history](https://ai.pydantic.dev/message-history/) for more information.
### Streaming Structured Output
Here's an example of streaming a user profile as it's built:
[With Pydantic AI Gateway](https://ai.pydantic.dev/output/#__tabbed_15_1)[Directly to Provider API](https://ai.pydantic.dev/output/#__tabbed_15_2)
[Learn about Gateway](https://ai.pydantic.dev/gateway) streamed_user_profile.py```
from datetime import date

from typing_extensions import NotRequired, TypedDict

from pydantic_ai import Agent


class UserProfile(TypedDict):
    name: str
    dob: NotRequired[date]
    bio: NotRequired[str]


agent = Agent(
    'gateway/openai:gpt-5.2',
    output_type=UserProfile,
    instructions='Extract a user profile from the input',
)


async def main():
    user_input = 'My name is Ben, I was born on January 28th 1990, I like the chain the dog and the pyramid.'
    async with agent.run_stream(user_input) as result:
        async for profile in result.stream_output():
            print(profile)
            #> {'name': 'Ben'}
            #> {'name': 'Ben'}
            #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes'}
            #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes the chain the '}
            #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes the chain the dog and the pyr'}
            #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes the chain the dog and the pyramid'}
            #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes the chain the dog and the pyramid'}

```

streamed_user_profile.py```
from datetime import date

from typing_extensions import NotRequired, TypedDict

from pydantic_ai import Agent


class UserProfile(TypedDict):
    name: str
    dob: NotRequired[date]
    bio: NotRequired[str]


agent = Agent(
    'openai:gpt-5.2',
    output_type=UserProfile,
    instructions='Extract a user profile from the input',
)


async def main():
    user_input = 'My name is Ben, I was born on January 28th 1990, I like the chain the dog and the pyramid.'
    async with agent.run_stream(user_input) as result:
        async for profile in result.stream_output():
            print(profile)
            #> {'name': 'Ben'}
            #> {'name': 'Ben'}
            #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes'}
            #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes the chain the '}
            #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes the chain the dog and the pyr'}
            #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes the chain the dog and the pyramid'}
            #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes the chain the dog and the pyramid'}

```

_(This example is complete, it can be run "as is" — you'll need to add`asyncio.run(main())` to run `main`)_
As setting an `output_type` uses the [Tool Output](https://ai.pydantic.dev/output/#tool-output) mode by default, this will only work if the model supports streaming tool arguments. For models that don't, like Gemini, try [Native Output](https://ai.pydantic.dev/output/#native-output) or [Prompted Output](https://ai.pydantic.dev/output/#prompted-output) instead.
### Streaming Model Responses
If you want fine-grained control of validation, you can use the following pattern to get the entire partial [`ModelResponse`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse "ModelResponse



      dataclass
  "):
[With Pydantic AI Gateway](https://ai.pydantic.dev/output/#__tabbed_16_1)[Directly to Provider API](https://ai.pydantic.dev/output/#__tabbed_16_2)
[Learn about Gateway](https://ai.pydantic.dev/gateway) streamed_user_profile.py```
from datetime import date

from pydantic import ValidationError
from typing_extensions import TypedDict

from pydantic_ai import Agent


class UserProfile(TypedDict, total=False):
    name: str
    dob: date
    bio: str


agent = Agent('gateway/openai:gpt-5.2', output_type=UserProfile)


async def main():
    user_input = 'My name is Ben, I was born on January 28th 1990, I like the chain the dog and the pyramid.'
    async with agent.run_stream(user_input) as result:
        async for message, last in result.stream_responses(debounce_by=0.01):  [](https://ai.pydantic.dev/output/#__code_33_annotation_1)
            try:
                profile = await result.validate_response_output(  [](https://ai.pydantic.dev/output/#__code_33_annotation_2)
                    message,
                    allow_partial=not last,
                )
            except ValidationError:
                continue
            print(profile)
            #> {'name': 'Ben'}
            #> {'name': 'Ben'}
            #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes'}
            #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes the chain the '}
            #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes the chain the dog and the pyr'}
            #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes the chain the dog and the pyramid'}
            #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes the chain the dog and the pyramid'}
            #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes the chain the dog and the pyramid'}

```

streamed_user_profile.py```
from datetime import date

from pydantic import ValidationError
from typing_extensions import TypedDict

from pydantic_ai import Agent


class UserProfile(TypedDict, total=False):
    name: str
    dob: date
    bio: str


agent = Agent('openai:gpt-5.2', output_type=UserProfile)


async def main():
    user_input = 'My name is Ben, I was born on January 28th 1990, I like the chain the dog and the pyramid.'
    async with agent.run_stream(user_input) as result:
        async for message, last in result.stream_responses(debounce_by=0.01):

[](https://ai.pydantic.dev/output/#__code_34_annotation_1)
            try:
                profile = await result.validate_response_output(

[](https://ai.pydantic.dev/output/#__code_34_annotation_2)
                    message,
                    allow_partial=not last,
                )
            except ValidationError:
                continue
            print(profile)
            #> {'name': 'Ben'}
            #> {'name': 'Ben'}
            #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes'}
            #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes the chain the '}
            #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes the chain the dog and the pyr'}
            #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes the chain the dog and the pyramid'}
            #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes the chain the dog and the pyramid'}
            #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes the chain the dog and the pyramid'}

```

  1. [`stream_responses`](https://ai.pydantic.dev/api/result/#pydantic_ai.result.StreamedRunResult.stream_responses "stream_responses



      async
  ") streams the data as [`ModelResponse`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse "ModelResponse



      dataclass
  ") objects, thus iteration can't fail with a `ValidationError`.
  2. [`validate_response_output`](https://ai.pydantic.dev/api/result/#pydantic_ai.result.StreamedRunResult.validate_response_output "validate_response_output



      async
  ") validates the data, `allow_partial=True` enables pydantic's [`experimental_allow_partial` flag on `TypeAdapter`](https://docs.pydantic.dev/latest/api/type_adapter/#pydantic.type_adapter.TypeAdapter.validate_json).


_(This example is complete, it can be run "as is" — you'll need to add`asyncio.run(main())` to run `main`)_
