##  [Reasoning](https://vercel.com/docs/ai-gateway/sdks-and-apis/responses#reasoning)[](https://vercel.com/docs/ai-gateway/sdks-and-apis/responses#reasoning)
For models that support reasoning, set the `reasoning` parameter to control how much effort the model spends thinking:
TypeScriptPython
reasoning.ts
```
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env.AI_GATEWAY_API_KEY,
  baseURL: 'https://ai-gateway.vercel.sh/v1',
});

const response = await client.responses.create({
  model: 'anthropic/claude-sonnet-4.6',
  input: 'Explain the Monty Hall problem step by step.',
  reasoning: {
    effort: 'high',
  },
  max_output_tokens: 2048,
});

console.log(response.output_text);
```

reasoning.py
```
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv('AI_GATEWAY_API_KEY'),
    base_url='https://ai-gateway.vercel.sh/v1',
)

response = client.responses.create(
    model='anthropic/claude-sonnet-4.6',
    input='Explain the Monty Hall problem step by step.',
    reasoning={
        'effort': 'high',
    },
    max_output_tokens=2048,
)

print(response.output_text)
```

The `effort` parameter accepts `none`, `minimal`, `low`, `medium`, `high`, or `xhigh`. AI Gateway maps this to provider-specific reasoning settings.
