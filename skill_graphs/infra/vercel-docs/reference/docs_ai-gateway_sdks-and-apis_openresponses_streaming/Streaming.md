# Streaming
Last updated January 21, 2026
The [OpenResponses API](https://vercel.com/docs/ai-gateway/sdks-and-apis/openresponses) supports streaming to receive tokens as they're generated instead of waiting for the complete response. Set `stream: true` in your request, then read the response body as a stream of server-sent events. Each event contains a response chunk that you can display incrementally.
TypeScriptPython
stream.ts
```
const apiKey = process.env.AI_GATEWAY_API_KEY;

const response = await fetch('https://ai-gateway.vercel.sh/v1/responses', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    Authorization: `Bearer ${apiKey}`,
  },
  body: JSON.stringify({
    model: 'google/gemini-3-flash',
    input: [
      {
        type: 'message',
        role: 'user',
        content: 'Write a haiku about debugging code.',
      },
    ],
    stream: true,
  }),
});

const reader = response.body.getReader();
const decoder = new TextDecoder();

while (true) {
  const { done, value } = await reader.read();
  if (done) break;

  const chunk = decoder.decode(value);
  const lines = chunk.split('\n');

  for (const line of lines) {
    if (line.startsWith('data:')) {
      const data = line.substring(6).trim();
      if (data) {
        const event = JSON.parse(data);
        if (event.type === 'response.output_text.delta') {
          process.stdout.write(event.delta);
        }
      }
    }
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
    model='google/gemini-3-flash',
    input=[
        {
            'type': 'message',
            'role': 'user',
            'content': 'Write a haiku about debugging code.',
        },
    ],
    stream=True,
)

for event in stream:
    if event.type == 'response.output_text.delta':
        print(event.delta, end='', flush=True)
```
