##  [Streaming](https://vercel.com/docs/ai-gateway/sdks-and-apis/python#streaming)[](https://vercel.com/docs/ai-gateway/sdks-and-apis/python#streaming)
Stream responses for real-time output in chat applications or long-running generations.
Chat CompletionsOpenAI ResponsesAnthropic Messages
streaming.py
```
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv('AI_GATEWAY_API_KEY'),
    base_url='https://ai-gateway.vercel.sh/v1'
)

stream = client.chat.completions.create(
    model='anthropic/claude-sonnet-4.6',
    messages=[
        {'role': 'user', 'content': 'Write a short story about a robot.'}
    ],
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end='', flush=True)
```

streaming.py
```
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv('AI_GATEWAY_API_KEY'),
    base_url='https://ai-gateway.vercel.sh/v1',
)

stream = client.responses.create(
    model='anthropic/claude-sonnet-4.6',
    input='Write a short story about a robot.',
    stream=True,
)

for event in stream:
    if event.type == 'response.output_text.delta':
        print(event.delta, end='', flush=True)
```

streaming.py
```
import os
import anthropic

client = anthropic.Anthropic(
    api_key=os.getenv('AI_GATEWAY_API_KEY'),
    base_url='https://ai-gateway.vercel.sh'
)

with client.messages.stream(
    model='anthropic/claude-sonnet-4.6',
    max_tokens=1024,
    messages=[
        {'role': 'user', 'content': 'Write a short story about a robot.'}
    ]
) as stream:
    for text in stream.text_stream:
        print(text, end='', flush=True)
```
