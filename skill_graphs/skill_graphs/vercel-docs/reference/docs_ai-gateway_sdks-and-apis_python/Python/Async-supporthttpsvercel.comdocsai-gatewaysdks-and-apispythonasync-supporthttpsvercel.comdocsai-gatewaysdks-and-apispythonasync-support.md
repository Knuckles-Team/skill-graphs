##  [Async support](https://vercel.com/docs/ai-gateway/sdks-and-apis/python#async-support)[](https://vercel.com/docs/ai-gateway/sdks-and-apis/python#async-support)
Both the OpenAI and Anthropic SDKs provide async clients for use with `asyncio`.
Chat CompletionsOpenAI ResponsesAnthropic Messages
async_client.py
```
import os
import asyncio
from openai import AsyncOpenAI

client = AsyncOpenAI(
    api_key=os.getenv('AI_GATEWAY_API_KEY'),
    base_url='https://ai-gateway.vercel.sh/v1'
)

async def main():
    response = await client.chat.completions.create(
        model='anthropic/claude-sonnet-4.6',
        messages=[
            {'role': 'user', 'content': 'Hello!'}
        ]
    )
    print(response.choices[0].message.content)

asyncio.run(main())
```

async_client.py
```
import os
import asyncio
from openai import AsyncOpenAI

client = AsyncOpenAI(
    api_key=os.getenv('AI_GATEWAY_API_KEY'),
    base_url='https://ai-gateway.vercel.sh/v1',
)

async def main():
    response = await client.responses.create(
        model='anthropic/claude-sonnet-4.6',
        input='Hello!',
    )
    print(response.output_text)

asyncio.run(main())
```

async_client.py
```
import os
import asyncio
import anthropic

client = anthropic.AsyncAnthropic(
    api_key=os.getenv('AI_GATEWAY_API_KEY'),
    base_url='https://ai-gateway.vercel.sh'
)

async def main():
    message = await client.messages.create(
        model='anthropic/claude-sonnet-4.6',
        max_tokens=1024,
        messages=[
            {'role': 'user', 'content': 'Hello!'}
        ]
    )
    print(message.content[0].text)

asyncio.run(main())
```
