##  [Using Perplexity Search](https://vercel.com/docs/ai-gateway/agent-quickstart#using-perplexity-search)[](https://vercel.com/docs/ai-gateway/agent-quickstart#using-perplexity-search)
The `perplexitySearch` tool can be used with any model regardless of the model provider or creator. This makes it a flexible option when you want consistent web search behavior across different models, or when you want to use web search with a model whose provider doesn't offer native web search capabilities.
To use Perplexity Search, import `gateway` from `ai` and pass `gateway.tools.perplexitySearch()` to the `tools` parameter. When the model needs current information, it calls the tool and AI Gateway routes the request to
Perplexity web search requests are charged at $5 per 1,000 requests. See
streamTextgenerateText
perplexity-web-search.ts
```
import { gateway, streamText } from 'ai';

export async function POST(request: Request) {
  const { prompt } = await request.json();

  const result = streamText({
    model: 'openai/gpt-5.4', // Works with any model, not just Perplexity
    prompt,
    tools: {
      perplexity_search: gateway.tools.perplexitySearch(),
    },
  });

  for await (const part of result.fullStream) {
    if (part.type === 'text-delta') {
      process.stdout.write(part.text);
    } else if (part.type === 'tool-call') {
      console.log('Tool call:', part.toolName);
    } else if (part.type === 'tool-result') {
      console.log('Search results received');
    }
  }

  return result.toDataStreamResponse();
}
```

perplexity-web-search.ts
```
import { gateway, generateText } from 'ai';

export async function POST(request: Request) {
  const { prompt } = await request.json();

  const { text } = await generateText({
    model: 'openai/gpt-5.4', // Works with any model, not just Perplexity
    prompt,
    tools: {
      perplexity_search: gateway.tools.perplexitySearch(),
    },
  });

  return Response.json({ text });
}
```

###  [Perplexity parameters](https://vercel.com/docs/ai-gateway/agent-quickstart#perplexity-parameters)[](https://vercel.com/docs/ai-gateway/agent-quickstart#perplexity-parameters)
You can configure the `perplexitySearch` tool with these parameters:
  * `maxResults`: Number of results to return (1-20). Defaults to 10.
  * `maxTokens`: Total token budget across all results. Defaults to 25,000, max 1,000,000.
  * `maxTokensPerPage`: Tokens extracted per webpage. Defaults to 2,048.
  * `country`: ISO 3166-1 alpha-2 country code (e.g., `'US'`, `'GB'`) for regional results.
  * `searchLanguageFilter`: ISO 639-1 language codes (e.g., `['en', 'fr']`). Max 10 codes.
  * `searchDomainFilter`: Domains to include (e.g., `['reuters.com']`) or exclude with `-` prefix (e.g., `['-reddit.com']`). Max 20 domains. Cannot mix allowlist and denylist.
  * `searchRecencyFilter`: Filter by content recency. Values: `'day'`, `'week'`, `'month'`, or `'year'`.


streamTextgenerateText
perplexity-web-search-params.ts
```
import { gateway, streamText } from 'ai';

export async function POST(request: Request) {
  const { prompt } = await request.json();

  const result = streamText({
    model: 'openai/gpt-5.4',
    prompt,
    tools: {
      perplexity_search: gateway.tools.perplexitySearch({
        maxResults: 5,
        maxTokens: 50000,
        maxTokensPerPage: 2048,
        country: 'US',
        searchLanguageFilter: ['en'],
        searchDomainFilter: ['reuters.com', 'bbc.com', 'nytimes.com'],
        searchRecencyFilter: 'week',
      }),
    },
  });

  return result.toDataStreamResponse();
}
```

perplexity-web-search-params.ts
```
import { gateway, generateText } from 'ai';

export async function POST(request: Request) {
  const { prompt } = await request.json();

  const { text } = await generateText({
    model: 'openai/gpt-5.4',
    prompt,
    tools: {
      perplexity_search: gateway.tools.perplexitySearch({
        maxResults: 5,
        maxTokens: 50000,
        maxTokensPerPage: 2048,
        country: 'US',
        searchLanguageFilter: ['en'],
        searchDomainFilter: ['reuters.com', 'bbc.com', 'nytimes.com'],
        searchRecencyFilter: 'week',
      }),
    },
  });

  return Response.json({ text });
}
```
