##  [Getting started](https://vercel.com/docs/ai-gateway/sdks-and-apis/openresponses#getting-started)[](https://vercel.com/docs/ai-gateway/sdks-and-apis/openresponses#getting-started)
Here's a simple example to generate a text response:
TypeScriptPython
quickstart.ts
```
const apiKey = process.env.AI_GATEWAY_API_KEY;

const response = await fetch('https://ai-gateway.vercel.sh/v1/responses', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    Authorization: `Bearer ${apiKey}`,
  },
  body: JSON.stringify({
    model: 'anthropic/claude-sonnet-4.6',
    input: [
      {
        type: 'message',
        role: 'user',
        content: 'What is the capital of France?',
      },
    ],
  }),
});

const result = await response.json();
console.log(result.output[0].content[0].text);
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
    input=[
        {
            'type': 'message',
            'role': 'user',
            'content': 'What is the capital of France?',
        },
    ],
)

print(response.output[0].content[0].text)
```
