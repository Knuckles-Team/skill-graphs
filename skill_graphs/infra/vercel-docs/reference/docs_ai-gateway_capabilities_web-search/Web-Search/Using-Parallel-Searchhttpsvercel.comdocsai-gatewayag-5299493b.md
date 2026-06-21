##  [Using Parallel Search](https://vercel.com/docs/ai-gateway/agent-quickstart#using-parallel-search)[](https://vercel.com/docs/ai-gateway/agent-quickstart#using-parallel-search)
The `parallelSearch` tool can be used with any model regardless of the model provider or creator.
To use Parallel Search, import `gateway` from `ai` and pass `gateway.tools.parallelSearch()` to the `tools` parameter. When the model needs current information, it calls the tool and AI Gateway routes the request to
Parallel web search requests are charged at $5 per 1,000 requests (includes up to 10 results per request). Additional results beyond 10 are charged at $1 per 1,000 additional results.
streamTextgenerateText
parallel-web-search.ts
```
import { gateway, streamText } from 'ai';

export async function POST(request: Request) {
  const { prompt } = await request.json();

  const result = streamText({
    model: 'anthropic/claude-sonnet-4.6', // Works with any model
    prompt,
    tools: {
      parallel_search: gateway.tools.parallelSearch(),
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

parallel-web-search.ts
```
import { gateway, generateText } from 'ai';

export async function POST(request: Request) {
  const { prompt } = await request.json();

  const { text } = await generateText({
    model: 'anthropic/claude-sonnet-4.6', // Works with any model
    prompt,
    tools: {
      parallel_search: gateway.tools.parallelSearch(),
    },
  });

  return Response.json({ text });
}
```

###  [Parallel parameters](https://vercel.com/docs/ai-gateway/agent-quickstart#parallel-parameters)[](https://vercel.com/docs/ai-gateway/agent-quickstart#parallel-parameters)
You can configure the `parallelSearch` tool with these parameters:
  * `mode`: Search mode preset. Values: `'one-shot'` (comprehensive results with longer excerpts, default) or `'agentic'` (concise, token-efficient results for multi-step workflows).
  * `maxResults`: Maximum number of results to return (1-20). Defaults to 10.
  * `searchQueries`: Optional list of keyword search queries to supplement the objective.
  * `sourcePolicy`: Controls which domains and date ranges to include or exclude.
    * `includeDomains`: List of domains to restrict search results to (e.g., `['arxiv.org', 'nature.com']`).
    * `excludeDomains`: List of domains to exclude from search results.
    * `afterDate`: Only return results published after this date (format: `YYYY-MM-DD`).
  * `excerpts`: Controls result excerpt length.
    * `maxCharsPerResult`: Maximum characters per result excerpt.
    * `maxCharsTotal`: Maximum total characters across all result excerpts.
  * `fetchPolicy`: Controls content freshness.
    * `maxAgeSeconds`: Maximum age of cached content in seconds for time-sensitive queries.


streamTextgenerateText
parallel-web-search-params.ts
```
import { gateway, streamText } from 'ai';

export async function POST(request: Request) {
  const { prompt } = await request.json();

  const result = streamText({
    model: 'anthropic/claude-sonnet-4.6',
    prompt,
    tools: {
      parallel_search: gateway.tools.parallelSearch({
        mode: 'one-shot',
        maxResults: 5,
        sourcePolicy: {
          includeDomains: ['arxiv.org', 'nature.com', 'science.org'],
          afterDate: '2025-01-01',
        },
        excerpts: {
          maxCharsPerResult: 5000,
        },
      }),
    },
  });

  return result.toDataStreamResponse();
}
```

parallel-web-search-params.ts
```
import { gateway, generateText } from 'ai';

export async function POST(request: Request) {
  const { prompt } = await request.json();

  const { text } = await generateText({
    model: 'anthropic/claude-sonnet-4.6',
    prompt,
    tools: {
      parallel_search: gateway.tools.parallelSearch({
        mode: 'one-shot',
        maxResults: 15,
        sourcePolicy: {
          includeDomains: ['arxiv.org', 'nature.com', 'science.org'],
          afterDate: '2025-01-01',
        },
        excerpts: {
          maxCharsPerResult: 5000,
        },
      }),
    },
  });

  return Response.json({ text });
}
```

For more details on search parameters and API options, see the
