# With backpressure: limit concurrent runs and queue depth
agent_with_backpressure = Agent(
    'gateway/openai:gpt-5',
    max_concurrency=ConcurrencyLimit(max_running=10, max_queued=100),
)


async def main():
    # These will be rate-limited to 10 concurrent runs
    results = await asyncio.gather(
        *[agent.run(f'Question {i}') for i in range(20)]
    )
    print(len(results))
    #> 20

```

agent_concurrency.py```
import asyncio

from pydantic_ai import Agent, ConcurrencyLimit

# Simple limit: allow up to 10 concurrent runs
agent = Agent('openai:gpt-5', max_concurrency=10)


# With backpressure: limit concurrent runs and queue depth
agent_with_backpressure = Agent(
    'openai:gpt-5',
    max_concurrency=ConcurrencyLimit(max_running=10, max_queued=100),
)


async def main():
    # These will be rate-limited to 10 concurrent runs
    results = await asyncio.gather(
        *[agent.run(f'Question {i}') for i in range(20)]
    )
    print(len(results))
    #> 20

```

When the concurrency limit is reached, additional calls to [`agent.run()`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AbstractAgent.run "run



      async
  ") or [`agent.iter()`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.iter "iter



      async
  ") will wait until a slot becomes available. If you configure `max_queued` and the queue fills up, a [`ConcurrencyLimitExceeded`](https://ai.pydantic.dev/api/exceptions/#pydantic_ai.exceptions.ConcurrencyLimitExceeded "ConcurrencyLimitExceeded") exception is raised.
When instrumentation is enabled, waiting operations appear as "waiting for concurrency" spans with attributes showing queue depth and limits.
### Model specific settings
If you wish to further customize model behavior, you can use a subclass of [`ModelSettings`](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "ModelSettings"), like [`GoogleModelSettings`](https://ai.pydantic.dev/api/models/google/#pydantic_ai.models.google.GoogleModelSettings "GoogleModelSettings"), associated with your model of choice.
For example:
[With Pydantic AI Gateway](https://ai.pydantic.dev/agent/#__tabbed_10_1)[Directly to Provider API](https://ai.pydantic.dev/agent/#__tabbed_10_2)
[Learn about Gateway](https://ai.pydantic.dev/gateway)```
from pydantic_ai import Agent, UnexpectedModelBehavior
from pydantic_ai.models.google import GoogleModelSettings

agent = Agent('gateway/gemini:gemini-3-flash-preview')

try:
    result = agent.run_sync(
        'Write a list of 5 very rude things that I might say to the universe after stubbing my toe in the dark:',
        model_settings=GoogleModelSettings(
            temperature=0.0,  # general model settings can also be specified
            gemini_safety_settings=[
                {
                    'category': 'HARM_CATEGORY_HARASSMENT',
                    'threshold': 'BLOCK_LOW_AND_ABOVE',
                },
                {
                    'category': 'HARM_CATEGORY_HATE_SPEECH',
                    'threshold': 'BLOCK_LOW_AND_ABOVE',
                },
            ],
        ),
    )
except UnexpectedModelBehavior as e:
    print(e)  [](https://ai.pydantic.dev/agent/#__code_22_annotation_1)
    """
    Content filter 'SAFETY' triggered, body:
    <safety settings details>
    """

```

```
from pydantic_ai import Agent, UnexpectedModelBehavior
from pydantic_ai.models.google import GoogleModelSettings

agent = Agent('google-gla:gemini-3-flash-preview')

try:
    result = agent.run_sync(
        'Write a list of 5 very rude things that I might say to the universe after stubbing my toe in the dark:',
        model_settings=GoogleModelSettings(
            temperature=0.0,  # general model settings can also be specified
            gemini_safety_settings=[
                {
                    'category': 'HARM_CATEGORY_HARASSMENT',
                    'threshold': 'BLOCK_LOW_AND_ABOVE',
                },
                {
                    'category': 'HARM_CATEGORY_HATE_SPEECH',
                    'threshold': 'BLOCK_LOW_AND_ABOVE',
                },
            ],
        ),
    )
except UnexpectedModelBehavior as e:
    print(e)

[](https://ai.pydantic.dev/agent/#__code_23_annotation_1)
    """
    Content filter 'SAFETY' triggered, body:
    <safety settings details>
    """

```

  1. This error is raised because the safety thresholds were exceeded.


## Runs vs. Conversations
An agent **run** might represent an entire conversation — there's no limit to how many messages can be exchanged in a single run. However, a **conversation** might also be composed of multiple runs, especially if you need to maintain state between separate interactions or API calls.
Here's an example of a conversation comprised of multiple runs:
[With Pydantic AI Gateway](https://ai.pydantic.dev/agent/#__tabbed_11_1)[Directly to Provider API](https://ai.pydantic.dev/agent/#__tabbed_11_2)
[Learn about Gateway](https://ai.pydantic.dev/gateway) conversation_example.py```
from pydantic_ai import Agent

agent = Agent('gateway/openai:gpt-5.2')

# First run
result1 = agent.run_sync('Who was Albert Einstein?')
print(result1.output)
#> Albert Einstein was a German-born theoretical physicist.

# Second run, passing previous messages
result2 = agent.run_sync(
    'What was his most famous equation?',
    message_history=result1.new_messages(),  [](https://ai.pydantic.dev/agent/#__code_24_annotation_1)
)
print(result2.output)
#> Albert Einstein's most famous equation is (E = mc^2).

```

conversation_example.py```
from pydantic_ai import Agent

agent = Agent('openai:gpt-5.2')
