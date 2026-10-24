##  [Quick start](https://vercel.com/docs/ai-gateway/sdks-and-apis/python#quick-start)[](https://vercel.com/docs/ai-gateway/sdks-and-apis/python#quick-start)
Chat CompletionsOpenAI ResponsesAnthropic Messages
quickstart.py
```
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv('AI_GATEWAY_API_KEY'),
    base_url='https://ai-gateway.vercel.sh/v1'
)

response = client.chat.completions.create(
    model='anthropic/claude-sonnet-4.6',
    messages=[
        {'role': 'user', 'content': 'Explain quantum computing in one paragraph.'}
    ]
)

print(response.choices[0].message.content)
```

quickstart.py
```
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv('AI_GATEWAY_API_KEY'),
    base_url='https://ai-gateway.vercel.sh/v1',
)

response = client.responses.create(
    model='anthropic/claude-sonnet-4.6',
    input='Explain quantum computing in one paragraph.',
)

print(response.output_text)
```

quickstart.py
```
import os
import anthropic

client = anthropic.Anthropic(
    api_key=os.getenv('AI_GATEWAY_API_KEY'),
    base_url='https://ai-gateway.vercel.sh'
)

message = client.messages.create(
    model='anthropic/claude-sonnet-4.6',
    max_tokens=1024,
    messages=[
        {'role': 'user', 'content': 'Explain quantum computing in one paragraph.'}
    ]
)

print(message.content[0].text)
```
