##  [Provider ordering](https://vercel.com/docs/ai-gateway/getting-started#provider-ordering)[](https://vercel.com/docs/ai-gateway/getting-started#provider-ordering)
Use the `order` array to specify the sequence in which providers should be attempted. Providers are specified using their `slug` string. You can find the slugs in the [table of available providers](https://vercel.com/docs/ai-gateway/models-and-providers/provider-options#available-providers).
You can also copy the provider slug using the copy button next to a provider's name on a model's detail page:
Through the Vercel Dashboard:
  1. Click the [AI Gateway](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fai-gateway&title=Go+to+AI+Gateway) tab
  2. Click [Model List](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fai-gateway%2Fmodels&title=Go+to+Model+List) on the left
  3. Click a model entry in the list


Through the AI Gateway site:
Visit a model's page on the [AI Gateway models page](https://vercel.com/ai-gateway/models) (e.g., [Claude Sonnet 4.5](https://vercel.com/ai-gateway/models/anthropic-claude-sonnet-4-5)).
The bottom section of the page lists the available providers for that model. The copy button next to a provider's name will copy their slug for pasting.
###  [Getting started](https://vercel.com/docs/ai-gateway/getting-started#getting-started)[](https://vercel.com/docs/ai-gateway/getting-started#getting-started)
  1. ###  [Install the AI SDK package](https://vercel.com/docs/ai-gateway/getting-started#install-the-ai-sdk-package)[](https://vercel.com/docs/ai-gateway/getting-started#install-the-ai-sdk-package)
First, ensure you have the necessary package installed:
Terminal
```
pnpm install ai
```

  2. ###  [Configure the provider order in your request](https://vercel.com/docs/ai-gateway/getting-started#configure-the-provider-order-in-your-request)[](https://vercel.com/docs/ai-gateway/getting-started#configure-the-provider-order-in-your-request)
Use the `providerOptions.gateway.order` configuration:
app/api/chat/route.ts
```
import { streamText } from 'ai';

export async function POST(request: Request) {
  const { prompt } = await request.json();

  const result = streamText({
    model: 'anthropic/claude-sonnet-4.6',
    prompt,
    providerOptions: {
      gateway: {
        order: ['bedrock', 'anthropic'], // Try Amazon Bedrock first, then Anthropic
      },
    },
  });

  return result.toUIMessageStreamResponse();
}
```

In this example:
     * The gateway will first attempt to use Amazon Bedrock to serve the Claude 4 Sonnet model
     * If Amazon Bedrock is unavailable or fails, it will fall back to Anthropic
     * Other providers (like Vertex AI) are still available but will only be used after the specified providers
  3. ###  [Test the routing behavior](https://vercel.com/docs/ai-gateway/getting-started#test-the-routing-behavior)[](https://vercel.com/docs/ai-gateway/getting-started#test-the-routing-behavior)
You can monitor which provider you used by checking the provider metadata in the response.
app/api/chat/route.ts
```
import { streamText } from 'ai';

export async function POST(request: Request) {
  const { prompt } = await request.json();

  const result = streamText({
    model: 'anthropic/claude-sonnet-4.6',
    prompt,
    providerOptions: {
      gateway: {
        order: ['bedrock', 'anthropic'],
      },
    },
  });

  // Log which provider was actually used
  console.log(JSON.stringify(await result.providerMetadata, null, 2));

  return result.toUIMessageStreamResponse();
}
```



###  [Provider metadata output](https://vercel.com/docs/ai-gateway/getting-started#provider-metadata-output)[](https://vercel.com/docs/ai-gateway/getting-started#provider-metadata-output)
```
{
  "anthropic": {},
  "gateway": {
    "routing": {
      "originalModelId": "anthropic/claude-sonnet-4.6",
      "resolvedProvider": "anthropic",
      "resolvedProviderApiModelId": "claude-sonnet-4.6",
      "internalResolvedModelId": "anthropic:claude-sonnet-4.6",
      "fallbacksAvailable": ["bedrock", "vertex"],
      "internalReasoning": "Selected anthropic as preferred provider for claude-sonnet-4.6. 2 fallback(s) available: bedrock, vertex",
      "planningReasoning": "System credentials planned for: anthropic. Total execution order: anthropic(system)",
      "canonicalSlug": "anthropic/claude-sonnet-4.6",
      "finalProvider": "anthropic",
      "attempts": [
        {
          "provider": "anthropic",
          "internalModelId": "anthropic:claude-sonnet-4.6",
          "providerApiModelId": "claude-sonnet-4.6",
          "credentialType": "system",
          "success": true,
          "startTime": 458753.407267,
          "endTime": 459891.705775
        }
      ],
      "modelAttemptCount": 1,
      "modelAttempts": [
        {
          "modelId": "anthropic/claude-sonnet-4.6",
          "canonicalSlug": "anthropic/claude-sonnet-4.6",
          "success": true,
          "providerAttemptCount": 1,
          "providerAttempts": [
            {
              "provider": "anthropic",
              "internalModelId": "anthropic:claude-sonnet-4.6",
              "providerApiModelId": "claude-sonnet-4.6",
              "credentialType": "system",
              "success": true,
              "startTime": 458753.407267,
              "endTime": 459891.705775
            }
          ]
        }
      ],
      "totalProviderAttemptCount": 1
    },
    "cost": "0.0045405",
    "marketCost": "0.0045405",
    "generationId": "gen_01K8KPJ0FZA7172X6CSGNZGDWY"
  }
}
```

The `gateway.cost` value is the amount debited from your AI Gateway Credits balance for this request. It is returned as a decimal string. The `gateway.marketCost` represents the market rate cost for the request. The `gateway.generationId` is a unique identifier for this generation that can be used with the [Generation Lookup API](https://vercel.com/docs/ai-gateway/capabilities/usage#generation-lookup). For more on pricing see [Pricing](https://vercel.com/docs/ai-gateway/pricing).
In cases where your request encounters issues with one or more providers or if your BYOK credentials fail, you'll find error detail in the `attempts` field of the provider metadata:
```
"attempts": [
  {
    "provider": "novita",
    "internalModelId": "novita:zai-org/glm-4.5",
    "providerApiModelId": "zai-org/glm-4.5",
    "credentialType": "byok",
    "success": false,
    "error": "Unauthorized",
    "startTime": 1754639042520,
    "endTime": 1754639042710
  },
  {
    "provider": "novita",
    "internalModelId": "novita:zai-org/glm-4.5",
    "providerApiModelId": "zai-org/glm-4.5",
    "credentialType": "system",
    "success": true,
    "startTime": 1754639042710,
    "endTime": 1754639043353
  }
]
```
