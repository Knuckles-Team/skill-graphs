# Embeddings
Last updated January 21, 2026
Generate vector embeddings from input text for semantic search, similarity matching, and retrieval-augmented generation (RAG).
Endpoint
`POST /embeddings `
Example request
TypeScriptPython
embeddings.ts
```
import OpenAI from 'openai';

const apiKey = process.env.AI_GATEWAY_API_KEY || process.env.VERCEL_OIDC_TOKEN;

const openai = new OpenAI({
  apiKey,
  baseURL: 'https://ai-gateway.vercel.sh/v1',
});

const response = await openai.embeddings.create({
  model: 'openai/text-embedding-3-small',
  input: 'Sunny day at the beach',
});

console.log(response.data[0].embedding);
```

embeddings.py
```
import os
from openai import OpenAI

api_key = os.getenv("AI_GATEWAY_API_KEY") or os.getenv("VERCEL_OIDC_TOKEN")

client = OpenAI(
    api_key=api_key,
    base_url="https://ai-gateway.vercel.sh/v1",
)

response = client.embeddings.create(
    model="openai/text-embedding-3-small",
    input="Sunny day at the beach",
)

print(response.data[0].embedding)
```

Response format
```
{
  "object": "list",
  "data": [
    {
      "object": "embedding",
      "index": 0,
      "embedding": [-0.0038, 0.021, ...]
    },
  ],
  "model": "openai/text-embedding-3-small",
  "usage": {
    "prompt_tokens": 6,
    "total_tokens": 6
  },
  "providerMetadata": {
    "gateway": {
      "routing": { ... }, // Detailed routing info
      "cost": "0.00000012"
    }
  }
}
```

Dimensions parameter
You can set the root-level `dimensions` field (from the `providerOptions.[provider]` still passes through as-is and isn't required for `dimensions` to work.
TypeScriptPython
embeddings-dimensions.ts
```
const response = await openai.embeddings.create({
  model: 'openai/text-embedding-3-small',
  input: 'Sunny day at the beach',
  dimensions: 768,
});
```

embeddings-dimensions.py
```
response = client.embeddings.create(
    model='openai/text-embedding-3-small',
    input='Sunny day at the beach',
    dimensions=768,
)
```

* * *
[ Previous Advanced ](https://vercel.com/docs/ai-gateway/sdks-and-apis/openai-chat-completions/advanced)[ Next Image Generation ](https://vercel.com/docs/ai-gateway/sdks-and-apis/openai-chat-completions/image-generation)
Was this helpful?
Send
Copy as MarkdownGive feedbackAsk AI about this page
