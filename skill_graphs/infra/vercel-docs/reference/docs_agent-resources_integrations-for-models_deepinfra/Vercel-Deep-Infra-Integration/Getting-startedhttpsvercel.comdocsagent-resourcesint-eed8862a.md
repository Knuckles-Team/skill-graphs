##  [Getting started](https://vercel.com/docs/agent-resources/integrations-for-agents#getting-started)[](https://vercel.com/docs/agent-resources/integrations-for-agents#getting-started)
The Vercel Deep Infra integration can be accessed through the AI tab on your [Vercel dashboard](https://vercel.com/dashboard).
###  [Prerequisites](https://vercel.com/docs/agent-resources/integrations-for-agents#prerequisites)[](https://vercel.com/docs/agent-resources/integrations-for-agents#prerequisites)
To follow this guide, you'll need the following:
  * An existing [Vercel project](https://vercel.com/docs/projects/overview#creating-a-project)
  * The latest version of [Vercel CLI](https://vercel.com/docs/cli#installing-vercel-cli)
Terminal
![](https://7nyt0uhk7sse4zvn.public.blob.vercel-storage.com/docs-assets/static/topics/icons/pnpm.svg)pnpm bun yarn npm
```
pnpm i -g vercel@latest
```

```
yarn global add vercel@latest
```

```
npm i -g vercel@latest
```

```
bun add -g vercel@latest
```



###  [Add the provider to your project](https://vercel.com/docs/agent-resources/integrations-for-agents#add-the-provider-to-your-project)[](https://vercel.com/docs/agent-resources/integrations-for-agents#add-the-provider-to-your-project)
####  [Using the dashboard](https://vercel.com/docs/agent-resources/integrations-for-agents#using-the-dashboard)[](https://vercel.com/docs/agent-resources/integrations-for-agents#using-the-dashboard)
  1. Navigate to the AI tab in your [Vercel dashboard](https://vercel.com/dashboard)
  2. Select Deep Infra from the list of providers, and press Add
  3. Review the provider information, and press Add Provider
  4. You can now select which projects the provider will have access to. You can choose from All Projects or Specific Projects
     * If you select Specific Projects, you'll be prompted to select the projects you want to connect to the provider. The list will display projects associated with your scoped team
     * Multiple projects can be selected during this step
  5. Select the Connect to Project button
  6. You'll be redirected to the provider's website to complete the connection process
  7. Once the connection is complete, you'll be redirected back to the Vercel dashboard, and the provider integration dashboard page. From here you can manage your provider settings, view usage, and more
  8. Pull the environment variables into your project using [Vercel CLI](https://vercel.com/docs/cli/env)
terminal
```
vercel env pull
```

  9. Install the providers package
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

  10. Connect your project using the code below:
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



####  [Using the CLI](https://vercel.com/docs/agent-resources/integrations-for-agents#using-the-cli)[](https://vercel.com/docs/agent-resources/integrations-for-agents#using-the-cli)
  1. Add the provider to your project using the [Vercel CLI `install`](https://vercel.com/docs/cli/install) command
terminal
```


vercel install deepinfra


```

During this process, you will be asked to open the dashboard to accept the marketplace terms if you have not installed this integration before. You can also choose which project(s) the provider will have access to.
  2. Install the providers package
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

  3. Connect your project using the code below:
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
