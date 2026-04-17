##  [Provider-specific search](https://vercel.com/docs/ai-gateway/agent-quickstart#provider-specific-search)[](https://vercel.com/docs/ai-gateway/agent-quickstart#provider-specific-search)
Use native web search tools from Anthropic, OpenAI, or Google. These tools are optimized for their respective providers and may offer additional features.
Pricing for provider-specific web search tools depends on the model you use. See the Web Search price column on the [model detail pages](https://vercel.com/ai-gateway/models) for exact pricing.
###  [Anthropic web search](https://vercel.com/docs/ai-gateway/agent-quickstart#anthropic-web-search)[](https://vercel.com/docs/ai-gateway/agent-quickstart#anthropic-web-search)
For Anthropic models, you can use the native `@ai-sdk/anthropic` package. Import `anthropic` from `@ai-sdk/anthropic` and pass `anthropic.tools.webSearch_20250305()` to the `tools` parameter. The tool returns source information including titles and URLs, which you can access through the `source` event type in the stream.
streamTextgenerateText
anthropic-web-search.ts
```
import { streamText } from 'ai';
import { anthropic } from '@ai-sdk/anthropic';

export async function POST(request: Request) {
  const { prompt } = await request.json();

  const result = streamText({
    model: 'anthropic/claude-opus-4.5',
    prompt,
    tools: {
      web_search: anthropic.tools.webSearch_20250305(),
    },
  });

  return result.toDataStreamResponse();
}
```

anthropic-web-search.ts
```
import { generateText } from 'ai';
import { anthropic } from '@ai-sdk/anthropic';

export async function POST(request: Request) {
  const { prompt } = await request.json();

  const { text } = await generateText({
    model: 'anthropic/claude-opus-4.5',
    prompt,
    tools: {
      web_search: anthropic.tools.webSearch_20250305(),
    },
  });

  return Response.json({ text });
}
```

####  [Anthropic parameters](https://vercel.com/docs/ai-gateway/agent-quickstart#anthropic-parameters)[](https://vercel.com/docs/ai-gateway/agent-quickstart#anthropic-parameters)
The following parameters are supported:
  * `maxUses`: Maximum number of web searches Claude can perform during the conversation.
  * `allowedDomains`: Optional list of domains Claude is allowed to search. If provided, searches will be restricted to these domains.
  * `blockedDomains`: Optional list of domains Claude should avoid when searching.
  * `userLocation`: Optional user location information to provide geographically relevant search results.


streamTextgenerateText
anthropic-web-search-params.ts
```
import { streamText } from 'ai';
import { anthropic } from '@ai-sdk/anthropic';

export async function POST(request: Request) {
  const { prompt } = await request.json();

  const result = streamText({
    model: 'anthropic/claude-opus-4.5',
    prompt,
    tools: {
      web_search: anthropic.tools.webSearch_20250305({
        maxUses: 3,
        allowedDomains: ['techcrunch.com', 'wired.com'],
        blockedDomains: ['example-spam-site.com'],
        userLocation: {
          type: 'approximate',
          country: 'US',
          region: 'California',
          city: 'San Francisco',
          timezone: 'America/Los_Angeles',
        },
      }),
    },
  });

  return result.toDataStreamResponse();
}
```

anthropic-web-search-params.ts
```
import { generateText } from 'ai';
import { anthropic } from '@ai-sdk/anthropic';

export async function POST(request: Request) {
  const { prompt } = await request.json();

  const { text } = await generateText({
    model: 'anthropic/claude-opus-4.5',
    prompt,
    tools: {
      web_search: anthropic.tools.webSearch_20250305({
        maxUses: 3,
        allowedDomains: ['techcrunch.com', 'wired.com'],
        blockedDomains: ['example-spam-site.com'],
        userLocation: {
          type: 'approximate',
          country: 'US',
          region: 'California',
          city: 'San Francisco',
          timezone: 'America/Los_Angeles',
        },
      }),
    },
  });

  return Response.json({ text });
}
```

For more details on using the Anthropic Messages API directly, see the [Anthropic advanced features](https://vercel.com/docs/ai-gateway/sdks-and-apis/anthropic-messages-api/advanced#web-search) documentation.
###  [OpenAI web search](https://vercel.com/docs/ai-gateway/agent-quickstart#openai-web-search)[](https://vercel.com/docs/ai-gateway/agent-quickstart#openai-web-search)
For OpenAI models, you can use the native `@ai-sdk/openai` package. Import `openai` from `@ai-sdk/openai` and pass `openai.tools.webSearch({})` to the `tools` parameter.
streamTextgenerateText
openai-web-search.ts
```
import { streamText } from 'ai';
import { openai } from '@ai-sdk/openai';

export async function POST(request: Request) {
  const { prompt } = await request.json();

  const result = streamText({
    model: 'openai/gpt-5.4',
    prompt,
    tools: {
      web_search: openai.tools.webSearch({}),
    },
  });

  return result.toDataStreamResponse();
}
```

openai-web-search.ts
```
import { generateText } from 'ai';
import { openai } from '@ai-sdk/openai';

export async function POST(request: Request) {
  const { prompt } = await request.json();

  const { text } = await generateText({
    model: 'openai/gpt-5.4',
    prompt,
    tools: {
      web_search: openai.tools.webSearch({}),
    },
  });

  return Response.json({ text });
}
```

###  [Google web search](https://vercel.com/docs/ai-gateway/agent-quickstart#google-web-search)[](https://vercel.com/docs/ai-gateway/agent-quickstart#google-web-search)
For Google Gemini models, you can use `source` event type in the stream.
####  [Google Vertex](https://vercel.com/docs/ai-gateway/agent-quickstart#google-vertex)[](https://vercel.com/docs/ai-gateway/agent-quickstart#google-vertex)
Import `vertex` from `@ai-sdk/google-vertex` and pass `vertex.tools.googleSearch({})` to the `tools` parameter. For users who need zero data retention, see [Enterprise web search](https://vercel.com/docs/ai-gateway/agent-quickstart#enterprise-web-search) below.
streamTextgenerateText
google-vertex-web-search.ts
```
import { streamText } from 'ai';
import { vertex } from '@ai-sdk/google-vertex';

export async function POST(request: Request) {
  const { prompt } = await request.json();

  const result = streamText({
    model: 'google/gemini-3-flash',
    prompt,
    tools: {
      google_search: vertex.tools.googleSearch({}),
    },
  });

  return result.toDataStreamResponse();
}
```

google-vertex-web-search.ts
```
import { generateText } from 'ai';
import { vertex } from '@ai-sdk/google-vertex';

export async function POST(request: Request) {
  const { prompt } = await request.json();

  const { text } = await generateText({
    model: 'google/gemini-3-flash',
    prompt,
    tools: {
      google_search: vertex.tools.googleSearch({}),
    },
  });

  return Response.json({ text });
}
```

####  [Enterprise web search](https://vercel.com/docs/ai-gateway/agent-quickstart#enterprise-web-search)[](https://vercel.com/docs/ai-gateway/agent-quickstart#enterprise-web-search)
For users who need zero data retention, you can use `vertex.tools.enterpriseWebSearch({})` to the `tools` parameter.
Enterprise web search uses indexed content that is a subset of the full web. Use Google search for more up-to-date and comprehensive results.
streamTextgenerateText
enterprise-web-grounding.ts
```
import { streamText } from 'ai';
import { vertex } from '@ai-sdk/google-vertex';

export async function POST(request: Request) {
  const { prompt } = await request.json();

  const result = streamText({
    model: 'google/gemini-3-flash',
    prompt,
    tools: {
      enterprise_web_search: vertex.tools.enterpriseWebSearch({}),
    },
  });

  return result.toDataStreamResponse();
}
```

enterprise-web-grounding.ts
```
import { generateText } from 'ai';
import { vertex } from '@ai-sdk/google-vertex';

export async function POST(request: Request) {
  const { prompt } = await request.json();

  const { text } = await generateText({
    model: 'google/gemini-3-flash',
    prompt,
    tools: {
      enterprise_web_search: vertex.tools.enterpriseWebSearch({}),
    },
  });

  return Response.json({ text });
}
```

####  [Google AI Studio](https://vercel.com/docs/ai-gateway/agent-quickstart#google-ai-studio)[](https://vercel.com/docs/ai-gateway/agent-quickstart#google-ai-studio)
Import `google` from `@ai-sdk/google` and pass `google.tools.googleSearch({})` to the `tools` parameter.
streamTextgenerateText
google-ai-studio-web-search.ts
```
import { streamText } from 'ai';
import { google } from '@ai-sdk/google';

export async function POST(request: Request) {
  const { prompt } = await request.json();

  const result = streamText({
    model: 'google/gemini-3-flash',
    prompt,
    tools: {
      google_search: google.tools.googleSearch({}),
    },
  });

  return result.toDataStreamResponse();
}
```

google-ai-studio-web-search.ts
```
import { generateText } from 'ai';
import { google } from '@ai-sdk/google';

export async function POST(request: Request) {
  const { prompt } = await request.json();

  const { text } = await generateText({
    model: 'google/gemini-3-flash',
    prompt,
    tools: {
      google_search: google.tools.googleSearch({}),
    },
  });

  return Response.json({ text });
}
```

* * *
[ Previous Getting Started ](https://vercel.com/docs/ai-gateway/getting-started)[ Next Models & Providers ](https://vercel.com/docs/ai-gateway/models-and-providers)
Was this helpful?
Send
On this page
  * [Using Perplexity Search](https://vercel.com/docs/ai-gateway/agent-quickstart#using-perplexity-search)
  * [Perplexity parameters](https://vercel.com/docs/ai-gateway/agent-quickstart#perplexity-parameters)
  * [Using Parallel Search](https://vercel.com/docs/ai-gateway/agent-quickstart#using-parallel-search)
  * [Parallel parameters](https://vercel.com/docs/ai-gateway/agent-quickstart#parallel-parameters)
  * [Provider-specific search](https://vercel.com/docs/ai-gateway/agent-quickstart#provider-specific-search)
  * [Anthropic web search](https://vercel.com/docs/ai-gateway/agent-quickstart#anthropic-web-search)
  * [Anthropic parameters](https://vercel.com/docs/ai-gateway/agent-quickstart#anthropic-parameters)
  * [OpenAI web search](https://vercel.com/docs/ai-gateway/agent-quickstart#openai-web-search)
  * [Google web search](https://vercel.com/docs/ai-gateway/agent-quickstart#google-web-search)
  * [Google Vertex](https://vercel.com/docs/ai-gateway/agent-quickstart#google-vertex)
  * [Enterprise web search](https://vercel.com/docs/ai-gateway/agent-quickstart#enterprise-web-search)
  * [Google AI Studio](https://vercel.com/docs/ai-gateway/agent-quickstart#google-ai-studio)


Copy as MarkdownGive feedbackAsk AI about this page
