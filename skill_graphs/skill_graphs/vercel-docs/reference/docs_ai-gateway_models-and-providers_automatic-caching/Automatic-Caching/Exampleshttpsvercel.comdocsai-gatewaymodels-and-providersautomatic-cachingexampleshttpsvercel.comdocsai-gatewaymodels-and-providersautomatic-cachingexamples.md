##  [Examples](https://vercel.com/docs/ai-gateway/models-and-providers/automatic-caching#examples)[](https://vercel.com/docs/ai-gateway/models-and-providers/automatic-caching#examples)
AI SDKChat CompletionsOpenAI ResponsesAnthropic Messages
app/api/chat/route.ts
```
import { streamText } from 'ai';

export async function POST(request: Request) {
  const { prompt } = await request.json();

  const result = streamText({
    model: 'anthropic/claude-sonnet-4.6',
    system: 'You are a helpful assistant with access to a large knowledge base...',
    prompt,
    providerOptions: {
      gateway: {
        caching: 'auto',
      },
    },
  });

  return result.toUIMessageStreamResponse();
}
```

TypeScriptPython
auto-caching.ts
```
import OpenAI from 'openai';

const apiKey = process.env.AI_GATEWAY_API_KEY || process.env.VERCEL_OIDC_TOKEN;

const openai = new OpenAI({
  apiKey,
  baseURL: 'https://ai-gateway.vercel.sh/v1',
});

// @ts-expect-error - providerOptions is a gateway extension
const response = await openai.chat.completions.create({
  model: 'anthropic/claude-sonnet-4.6',
  messages: [
    {
      role: 'system',
      content: 'You are a helpful assistant with access to a large knowledge base...',
    },
    {
      role: 'user',
      content: 'What is the capital of France?',
    },
  ],
  providerOptions: {
    gateway: {
      caching: 'auto',
    },
  },
});

console.log(response.choices[0].message.content);
```

auto-caching.py
```
import os
from openai import OpenAI

api_key = os.getenv('AI_GATEWAY_API_KEY') or os.getenv('VERCEL_OIDC_TOKEN')

client = OpenAI(
    api_key=api_key,
    base_url='https://ai-gateway.vercel.sh/v1'
)

response = client.chat.completions.create(
    model='anthropic/claude-sonnet-4.6',
    messages=[
        {
            'role': 'system',
            'content': 'You are a helpful assistant with access to a large knowledge base...'
        },
        {
            'role': 'user',
            'content': 'What is the capital of France?'
        }
    ],
    extra_body={
        'providerOptions': {
            'gateway': {
                'caching': 'auto'
            }
        }
    }
)

print(response.choices[0].message.content)
```

auto-caching.ts
```
const response = await fetch('https://ai-gateway.vercel.sh/v1/responses', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    Authorization: `Bearer ${apiKey}`,
  },
  body: JSON.stringify({
    model: 'anthropic/claude-sonnet-4.6',
    caching: 'auto',
    instructions: 'You are a helpful assistant with access to a large knowledge base...',
    input: [{ type: 'message', role: 'user', content: 'What is the capital of France?' }],
  }),
});
```

TypeScriptPython
auto-caching.ts
```
import Anthropic from '@anthropic-ai/sdk';

const apiKey = process.env.AI_GATEWAY_API_KEY || process.env.VERCEL_OIDC_TOKEN;

const anthropic = new Anthropic({
  apiKey,
  baseURL: 'https://ai-gateway.vercel.sh',
});

const message = await anthropic.messages.create({
  model: 'anthropic/claude-sonnet-4.6',
  max_tokens: 2048,
  system: 'You are a helpful assistant with access to a large knowledge base...',
  messages: [
    {
      role: 'user',
      content: 'What is the capital of France?',
    },
  ],
  // @ts-expect-error - providerOptions is a gateway extension
  providerOptions: {
    gateway: {
      caching: 'auto',
    },
  },
});

console.log(message.content[0].type === 'text' ? message.content[0].text : '');
```

auto-caching.py
```
import os
import anthropic

api_key = os.getenv('AI_GATEWAY_API_KEY') or os.getenv('VERCEL_OIDC_TOKEN')

client = anthropic.Anthropic(
    api_key=api_key,
    base_url='https://ai-gateway.vercel.sh'
)

message = client.messages.create(
    model='anthropic/claude-sonnet-4.6',
    max_tokens=2048,
    system='You are a helpful assistant with access to a large knowledge base...',
    messages=[
        {
            'role': 'user',
            'content': 'What is the capital of France?'
        }
    ],
    extra_body={
        'providerOptions': {
            'gateway': {
                'caching': 'auto'
            }
        }
    }
)

print(message.content[0].text)
```
