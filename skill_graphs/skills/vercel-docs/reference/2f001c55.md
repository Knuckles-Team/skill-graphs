## Community
  * [Open source program](https://vercel.com/open-source-program)
  * [Events](https://vercel.com/events)
  * [Shipped on Vercel](https://vercel.com/shipped)


[](https://vercel.com/home)

Select a display theme: systemlightdark
Terminal
![](https://7nyt0uhk7sse4zvn.public.blob.vercel-storage.com/docs-assets/static/topics/icons/pnpm.svg)pnpm bun yarn npm
```
pnpm i @ai-sdk/deepinfra ai
```

```
yarn add @ai-sdk/deepinfra ai
```

```
npm i @ai-sdk/deepinfra ai
```

```
bun add @ai-sdk/deepinfra ai
```

app/api/chat/route.ts
Next.js (/app) Next.js (/pages) SvelteKit Other frameworks
```
import { deepinfra } from '@ai-sdk/deepinfra';import { streamText } from 'ai';
// Allow streaming responses up to 30 secondsexport const maxDuration = 30;
export async function POST(req: Request) {  // Extract the `messages` from the body of the request  const { messages } = await req.json();
  // Call the language model  const result = streamText({    model: deepinfra('deepseek-ai/DeepSeek-R1-Distill-Llama-70B'),    messages,  });
  // Respond with the stream  return result.toDataStreamResponse();}

```

```
import { deepinfra } from '@ai-sdk/deepinfra';import { streamText } from 'ai';import { NextApiRequest, NextApiResponse } from 'next';
// Allow streaming responses up to 30 secondsexport const maxDuration = 30;
export default async function handler(  request: NextApiRequest,  response: NextApiResponse,) {  // Extract the `messages` from the body of the request  const { messages } = await request.body;
  const result = streamText({    model: deepinfra('deepseek-ai/DeepSeek-R1-Distill-Llama-70B'),    messages,  });
  // Write the data stream to the response  // Note: this is sent as a single response, not a stream  result.pipeDataStreamToResponse(response);}

```

```
import { deepinfra } from '@ai-sdk/deepinfra';import { streamText } from 'ai';import type { RequestHandler } from './$types';
export const POST = (async ({ request }) => {  // Extract `messages` from the body of the request  const { messages } = await request.json();
  // Call the language model  const result = streamText({    model: deepinfra('deepseek-ai/DeepSeek-R1-Distill-Llama-70B'),    messages,  });
  // Respond with the stream  return result.toDataStreamResponse();}) satisfies RequestHandler;

```

```
import { deepinfra } from '@ai-sdk/deepinfra';import { generateText } from 'ai';
const { text } = await generateText({  model: deepinfra('deepseek-ai/DeepSeek-R1-Distill-Llama-70B'),  prompt: 'Write a vegetarian lasagna recipe for 4 people.',});

```

Terminal
![](https://7nyt0uhk7sse4zvn.public.blob.vercel-storage.com/docs-assets/static/topics/icons/pnpm.svg)pnpm bun yarn npm
```
pnpm i @ai-sdk/deepinfra ai
```

```
yarn add @ai-sdk/deepinfra ai
```

```
npm i @ai-sdk/deepinfra ai
```

```
bun add @ai-sdk/deepinfra ai
```

```
pnpm i @ai-sdk/deepinfra ai
```

app/api/chat/route.ts
Next.js (/app) Next.js (/pages) SvelteKit Other frameworks
```
import { deepinfra } from '@ai-sdk/deepinfra';import { streamText } from 'ai';
// Allow streaming responses up to 30 secondsexport const maxDuration = 30;
export async function POST(req: Request) {  // Extract the `messages` from the body of the request  const { messages } = await req.json();
  // Call the language model  const result = streamText({    model: deepinfra('deepseek-ai/DeepSeek-R1-Distill-Llama-70B'),    messages,  });
  // Respond with the stream  return result.toDataStreamResponse();}

```

```
import { deepinfra } from '@ai-sdk/deepinfra';import { streamText } from 'ai';import { NextApiRequest, NextApiResponse } from 'next';
// Allow streaming responses up to 30 secondsexport const maxDuration = 30;
export default async function handler(  request: NextApiRequest,  response: NextApiResponse,) {  // Extract the `messages` from the body of the request  const { messages } = await request.body;
  const result = streamText({    model: deepinfra('deepseek-ai/DeepSeek-R1-Distill-Llama-70B'),    messages,  });
  // Write the data stream to the response  // Note: this is sent as a single response, not a stream  result.pipeDataStreamToResponse(response);}

```

```
import { deepinfra } from '@ai-sdk/deepinfra';import { streamText } from 'ai';import type { RequestHandler } from './$types';
export const POST = (async ({ request }) => {  // Extract `messages` from the body of the request  const { messages } = await request.json();
  // Call the language model  const result = streamText({    model: deepinfra('deepseek-ai/DeepSeek-R1-Distill-Llama-70B'),    messages,  });
  // Respond with the stream  return result.toDataStreamResponse();}) satisfies RequestHandler;

```

```
import { deepinfra } from '@ai-sdk/deepinfra';import { generateText } from 'ai';
const { text } = await generateText({  model: deepinfra('deepseek-ai/DeepSeek-R1-Distill-Llama-70B'),  prompt: 'Write a vegetarian lasagna recipe for 4 people.',});

```
