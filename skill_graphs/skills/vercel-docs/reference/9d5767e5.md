##  [Generation lookup](https://vercel.com/docs/ai-gateway/capabilities/usage#generation-lookup)[](https://vercel.com/docs/ai-gateway/capabilities/usage#generation-lookup)
Retrieve detailed information about a specific generation by its ID. This endpoint allows you to look up usage data, costs, and metadata for any generation created through AI Gateway. Generation information is available shortly after the generation completes. Note that much of this data is also included in the `providerMetadata` field of the chat completion responses.
Endpoint
`GET /generation?id={generation_id} `
Parameters
  * `id` (required): The generation ID to look up (format: `gen_<ulid>`)


Example request
TypeScriptPython
generation-lookup.ts
```
const generationId = 'gen_01ARZ3NDEKTSV4RRFFQ69G5FAV';

const response = await fetch(
  `https://ai-gateway.vercel.sh/v1/generation?id=${generationId}`,
  {
    method: 'GET',
    headers: {
      Authorization: `Bearer ${process.env.AI_GATEWAY_API_KEY}`,
      'Content-Type': 'application/json',
    },
  },
);

const generation = await response.json();
console.log(generation);
```

generation-lookup.py
```
import os
import requests

generation_id = 'gen_01ARZ3NDEKTSV4RRFFQ69G5FAV'

response = requests.get(
    f"https://ai-gateway.vercel.sh/v1/generation?id={generation_id}",
    headers={
        "Authorization": f"Bearer {os.getenv('AI_GATEWAY_API_KEY')}",
        "Content-Type": "application/json",
    },
)

generation = response.json()
print(generation)
```

Sample response
```
{
  "data": {
    "id": "gen_01ARZ3NDEKTSV4RRFFQ69G5FAV",
    "total_cost": 0.00123,
    "usage": 0.00123,
    "created_at": "2024-01-01T00:00:00.000Z",
    "model": "gpt-4",
    "is_byok": false,
    "provider_name": "openai",
    "streamed": true,
    "latency": 200,
    "generation_time": 1500,
    "tokens_prompt": 100,
    "tokens_completion": 50,
    "native_tokens_prompt": 100,
    "native_tokens_completion": 50,
    "native_tokens_reasoning": 0,
    "native_tokens_cached": 0
  }
}
```

Response fields
  * `id`: The generation ID
  * `total_cost`: Total cost in USD for this generation
  * `usage`: Usage cost (same as total_cost)
  * `created_at`: ISO 8601 timestamp when the generation was created
  * `model`: Model identifier used for this generation
  * `is_byok`: Whether this generation used Bring Your Own Key credentials
  * `provider_name`: The provider that served this generation
  * `streamed`: Whether this generation used streaming (`true` for streamed responses, `false` otherwise)
  * `latency`: Time to first token in milliseconds
  * `generation_time`: Total generation time in milliseconds
  * `tokens_prompt`: Number of prompt tokens
  * `tokens_completion`: Number of completion tokens
  * `native_tokens_prompt`: Native prompt tokens (provider-specific)
  * `native_tokens_completion`: Native completion tokens (provider-specific)
  * `native_tokens_reasoning`: Reasoning tokens used (if applicable)
  * `native_tokens_cached`: Cached tokens used (if applicable)


Generation IDs: Generation IDs are included in chat completion responses as the
* * *
[ Previous Observability ](https://vercel.com/docs/ai-gateway/capabilities/observability)[ Next Image Generation ](https://vercel.com/docs/ai-gateway/capabilities/image-generation)
Was this helpful?
Send
On this page
  * [Base URL](https://vercel.com/docs/ai-gateway/capabilities/usage#base-url)
  * [Supported endpoints](https://vercel.com/docs/ai-gateway/capabilities/usage#supported-endpoints)
  * [Credits](https://vercel.com/docs/ai-gateway/capabilities/usage#credits)
  * [Generation lookup](https://vercel.com/docs/ai-gateway/capabilities/usage#generation-lookup)


Copy as MarkdownGive feedbackAsk AI about this page
[AI Gateway](https://vercel.com/docs/ai-gateway)
[Capabilities](https://vercel.com/docs/ai-gateway/capabilities)
Usage & Billing
