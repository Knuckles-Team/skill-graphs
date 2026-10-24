# Output
"Output" refers to the final value returned from [running an agent](https://ai.pydantic.dev/agent/#running-agents). This can be either plain text, [structured data](https://ai.pydantic.dev/output/#structured-output), an [image](https://ai.pydantic.dev/output/#image-output), or the result of a [function](https://ai.pydantic.dev/output/#output-functions) called with arguments provided by the model.
The output is wrapped in [`AgentRunResult`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AgentRunResult "AgentRunResult



      dataclass
  ") or [`StreamedRunResult`](https://ai.pydantic.dev/api/result/#pydantic_ai.result.StreamedRunResult "StreamedRunResult



      dataclass
  ") so that you can access other data, like [usage](https://ai.pydantic.dev/api/usage/#pydantic_ai.usage.RunUsage "RunUsage



      dataclass
  ") of the run and [message history](https://ai.pydantic.dev/message-history/#accessing-messages-from-results).
Both `AgentRunResult` and `StreamedRunResult` are generic in the data they wrap, so typing information about the data returned by the agent is preserved.
A run ends when the model responds with one of the output types, or, if no output type is specified or `str` is one of the allowed options, when a plain text response is received. A run can also be cancelled if usage limits are exceeded, see [Usage Limits](https://ai.pydantic.dev/agent/#usage-limits).
Here's an example using a Pydantic model as the `output_type`, forcing the model to respond with data matching our specification:
[With Pydantic AI Gateway](https://ai.pydantic.dev/output/#__tabbed_1_1)[Directly to Provider API](https://ai.pydantic.dev/output/#__tabbed_1_2)
[Learn about Gateway](https://ai.pydantic.dev/gateway) olympics.py```
from pydantic import BaseModel

from pydantic_ai import Agent


class CityLocation(BaseModel):
    city: str
    country: str


agent = Agent('gateway/gemini:gemini-3-flash-preview', output_type=CityLocation)
result = agent.run_sync('Where were the olympics held in 2012?')
print(result.output)
#> city='London' country='United Kingdom'
print(result.usage())
#> RunUsage(input_tokens=57, output_tokens=8, requests=1)

```

olympics.py```
from pydantic import BaseModel

from pydantic_ai import Agent


class CityLocation(BaseModel):
    city: str
    country: str


agent = Agent('google-gla:gemini-3-flash-preview', output_type=CityLocation)
result = agent.run_sync('Where were the olympics held in 2012?')
print(result.output)
#> city='London' country='United Kingdom'
print(result.usage())
#> RunUsage(input_tokens=57, output_tokens=8, requests=1)

```

_(This example is complete, it can be run "as is")_
