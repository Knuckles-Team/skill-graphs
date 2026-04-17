##  [List models](https://vercel.com/docs/ai-gateway/agent-quickstart#list-models)[](https://vercel.com/docs/ai-gateway/agent-quickstart#list-models)
Retrieve a list of all available models that can be used with the AI Gateway.
Endpoint
`GET /models `
Example request
TypeScriptPython
list-models.ts
```
import OpenAI from 'openai';

const openai = new OpenAI({
  apiKey: process.env.AI_GATEWAY_API_KEY,
  baseURL: 'https://ai-gateway.vercel.sh/v1',
});

const models = await openai.models.list();
console.log(models);
```

list-models.py
```
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv('AI_GATEWAY_API_KEY'),
    base_url='https://ai-gateway.vercel.sh/v1'
)

models = client.models.list()
print(models)
```

Response format
The response follows the OpenAI API format:
```
{
  "object": "list",
  "data": [
    {
      "id": "anthropic/claude-sonnet-4.6",
      "object": "model",
      "created": 1677610602,
      "owned_by": "anthropic"
    },
    {
      "id": "openai/gpt-5.4",
      "object": "model",
      "created": 1677610602,
      "owned_by": "openai"
    }
  ]
}
```
