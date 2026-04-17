##  [Retrieve model](https://vercel.com/docs/ai-gateway/agent-quickstart#retrieve-model)[](https://vercel.com/docs/ai-gateway/agent-quickstart#retrieve-model)
Retrieve details about a specific model.
Endpoint
`GET /models/{model} `
Parameters
  * `model` (required): The model ID to retrieve (e.g., `anthropic/claude-sonnet-4`)


Example request
TypeScriptPython
retrieve-model.ts
```
import OpenAI from 'openai';

const openai = new OpenAI({
  apiKey: process.env.AI_GATEWAY_API_KEY,
  baseURL: 'https://ai-gateway.vercel.sh/v1',
});

const model = await openai.models.retrieve('anthropic/claude-sonnet-4.6');
console.log(model);
```

retrieve-model.py
```
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv('AI_GATEWAY_API_KEY'),
    base_url='https://ai-gateway.vercel.sh/v1'
)

model = client.models.retrieve('anthropic/claude-sonnet-4.6')
print(model)
```

Response format
```
{
  "id": "anthropic/claude-sonnet-4.6",
  "object": "model",
  "created": 1677610602,
  "owned_by": "anthropic"
}
```
