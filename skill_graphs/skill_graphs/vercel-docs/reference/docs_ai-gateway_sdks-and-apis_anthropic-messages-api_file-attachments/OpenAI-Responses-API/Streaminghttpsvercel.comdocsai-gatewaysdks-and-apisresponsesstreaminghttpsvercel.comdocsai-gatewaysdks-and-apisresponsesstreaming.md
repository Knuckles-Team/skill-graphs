##  [Streaming](https://vercel.com/docs/ai-gateway/sdks-and-apis/responses#streaming)[](https://vercel.com/docs/ai-gateway/sdks-and-apis/responses#streaming)
Set `stream: true` to receive tokens as they're generated. The SDK returns an async iterator of server-sent events:
TypeScriptPython
stream.ts
```
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env.AI_GATEWAY_API_KEY,
  baseURL: 'https://ai-gateway.vercel.sh/v1',
});

const stream = await client.responses.create({
  model: 'openai/gpt-5.4',
  input: 'Write a haiku about programming.',
  stream: true,
});

for await (const event of stream) {
  if (event.type === 'response.output_text.delta') {
    process.stdout.write(event.delta);
  }
}
```

stream.py
```
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv('AI_GATEWAY_API_KEY'),
    base_url='https://ai-gateway.vercel.sh/v1',
)

stream = client.responses.create(
    model='openai/gpt-5.4',
    input='Write a haiku about programming.',
    stream=True,
)

for event in stream:
    if event.type == 'response.output_text.delta':
        print(event.delta, end='', flush=True)
```
