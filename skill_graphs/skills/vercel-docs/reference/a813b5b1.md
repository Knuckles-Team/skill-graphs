##  [Integration with existing tools](https://vercel.com/docs/ai-gateway/sdks-and-apis/openai-chat-completions#integration-with-existing-tools)[](https://vercel.com/docs/ai-gateway/sdks-and-apis/openai-chat-completions#integration-with-existing-tools)
You can use the AI Gateway's Chat Completions API with existing tools and libraries like the [API key](https://vercel.com/docs/ai-gateway/authentication#api-key) or [OIDC token](https://vercel.com/docs/ai-gateway/authentication#oidc-token) for authentication.
###  [OpenAI client libraries](https://vercel.com/docs/ai-gateway/sdks-and-apis/openai-chat-completions#openai-client-libraries)[](https://vercel.com/docs/ai-gateway/sdks-and-apis/openai-chat-completions#openai-client-libraries)
TypeScriptPython
client.ts
```
import OpenAI from 'openai';

const openai = new OpenAI({
  apiKey: process.env.AI_GATEWAY_API_KEY,
  baseURL: 'https://ai-gateway.vercel.sh/v1',
});

const response = await openai.chat.completions.create({
  model: 'anthropic/claude-sonnet-4.6',
  messages: [{ role: 'user', content: 'Hello, world!' }],
});
```

client.py
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
        {'role': 'user', 'content': 'Hello, world!'}
    ]
)
```

###  [AI SDK](https://vercel.com/docs/ai-gateway/sdks-and-apis/openai-chat-completions#ai-sdk)[](https://vercel.com/docs/ai-gateway/sdks-and-apis/openai-chat-completions#ai-sdk)
For compatibility with
client.ts
```
import { createOpenAICompatible } from '@ai-sdk/openai-compatible';
import { generateText } from 'ai';

const gateway = createOpenAICompatible({
  name: 'openai',
  apiKey: process.env.AI_GATEWAY_API_KEY,
  baseURL: 'https://ai-gateway.vercel.sh/v1',
});

const response = await generateText({
  model: gateway('anthropic/claude-sonnet-4.6'),
  prompt: 'Hello, world!',
});
```
