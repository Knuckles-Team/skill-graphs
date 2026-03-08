##  [Getting started](https://vercel.com/docs/ai-gateway/sdks-and-apis/responses#getting-started)[](https://vercel.com/docs/ai-gateway/sdks-and-apis/responses#getting-started)
Set your SDK's base URL to AI Gateway and use your API key for authentication:
TypeScriptPython
basic.ts
```
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env.AI_GATEWAY_API_KEY,
  baseURL: 'https://ai-gateway.vercel.sh/v1',
});

const response = await client.responses.create({
  model: 'anthropic/claude-sonnet-4.6',
  input: 'What is the capital of France?',
});

console.log(response.output_text);
```

basic.py
```
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv('AI_GATEWAY_API_KEY'),
    base_url='https://ai-gateway.vercel.sh/v1',
)

response = client.responses.create(
    model='anthropic/claude-sonnet-4.6',
    input='What is the capital of France?',
)

print(response.output_text)
```
