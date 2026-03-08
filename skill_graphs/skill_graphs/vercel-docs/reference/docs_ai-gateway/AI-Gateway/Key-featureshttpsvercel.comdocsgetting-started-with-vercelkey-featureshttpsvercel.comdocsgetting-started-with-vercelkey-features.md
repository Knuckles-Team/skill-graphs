##  [Key features](https://vercel.com/docs/getting-started-with-vercel#key-features)[](https://vercel.com/docs/getting-started-with-vercel#key-features)
  * One key, hundreds of models: access models from multiple providers with a single API key
  * Unified API: helps you switch between providers and models with minimal code changes
  * High reliability: automatically retries requests to other providers if one fails
  * Embeddings support: generate vector embeddings for search, retrieval, and other tasks
  * Spend monitoring: monitor your spending across different providers
  * No markup on tokens: tokens cost the same as they would from the provider directly, with zero markup, including with [Bring Your Own Key (BYOK)](https://vercel.com/docs/ai-gateway/authentication-and-byok/byok).


TypeScriptPythoncURL
index.ts
```
import { generateText } from 'ai';

const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.6',
  prompt: 'What is the capital of France?',
});

```

index.py
```
import os
from openai import OpenAI

client = OpenAI(
  api_key=os.getenv('AI_GATEWAY_API_KEY'),
  base_url='https://ai-gateway.vercel.sh/v1'
)

response = client.chat.completions.create(
  model='xai/grok-4.1-fast-reasoning',
  messages=[
    {
      'role': 'user',
      'content': 'Why is the sky blue?'
    }
  ]
)
```

index.sh
```
curl -X POST "https://ai-gateway.vercel.sh/v1/chat/completions" \
-H "Authorization: Bearer $AI_GATEWAY_API_KEY" \
-H "Content-Type: application/json" \
-d '{
  "model": "openai/gpt-5.4",
  "messages": [
    {
      "role": "user",
      "content": "Why is the sky blue?"
    }
  ],
  "stream": false
}'
```
