##  [Provider filtering](https://vercel.com/docs/ai-gateway/getting-started#provider-filtering)[](https://vercel.com/docs/ai-gateway/getting-started#provider-filtering)
###  [Restrict providers with the `only` filter](https://vercel.com/docs/ai-gateway/getting-started#restrict-providers-with-the-only-filter)[](https://vercel.com/docs/ai-gateway/getting-started#restrict-providers-with-the-only-filter)
Use the `only` array to restrict routing to a specific subset of providers. Providers are specified by their slug and are matched against the model's available providers.
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
        only: ['bedrock', 'anthropic'], // Only consider these providers.
        // This model is also available via 'vertex', but it won't be considered.
      },
    },
  });

  return result.toUIMessageStreamResponse();
}
```

In this example:
  * Restriction: Only `bedrock` and `anthropic` will be considered for routing and fallbacks.
  * Error on mismatch: If none of the specified providers are available for the model, the request fails with an error indicating the allowed providers.


###  [Using `only` together with `order`](https://vercel.com/docs/ai-gateway/getting-started#using-only-together-with-order)[](https://vercel.com/docs/ai-gateway/getting-started#using-only-together-with-order)
When both `only` and `order` are provided, the `only` filter is applied first to define the allowed set, and then `order` defines the priority within that filtered set. Practically, the end result is the same as taking your `order` list and intersecting it with the `only` list.
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
        only: ['anthropic', 'vertex'],
        order: ['vertex', 'bedrock', 'anthropic'],
      },
    },
  });

  return result.toUIMessageStreamResponse();
}
```

The final order will be `vertex → anthropic` (providers listed in `order` but not in `only` are ignored).
