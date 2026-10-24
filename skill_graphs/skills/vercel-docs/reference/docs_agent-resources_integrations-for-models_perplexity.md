[Agent Resources](https://vercel.com/docs/agent-resources)
[Integrations for Models](https://vercel.com/docs/agent-resources/integrations-for-models)
Perplexity
[Agent Resources](https://vercel.com/docs/agent-resources)
[Integrations for Models](https://vercel.com/docs/agent-resources/integrations-for-models)
Perplexity
#  Vercel Perplexity Integration
Connectable Account
Last updated June 26, 2025
specializes in providing accurate, real-time answers to user questions by combining AI-powered search with large language models, delivering concise, well-sourced, and conversational responses. Integrating Perplexity via its
##  [Use cases](https://vercel.com/docs/agent-resources/integrations-for-models/perplexity#use-cases)[](https://vercel.com/docs/agent-resources/integrations-for-models/perplexity#use-cases)
You can use the Vercel and Perplexity integration to power a variety of AI applications, including:
  * Real-time, citation-backed answers: Integrate Perplexity to provide users with up-to-date information grounded in live web data, complete with detailed source citations for transparency and trust.
  * Customizable search and data sourcing: Tailor your application's responses by specifying which sources Perplexity should use, ensuring compliance and relevance for your domain or industry.
  * Complex, multi-step query handling: Leverage advanced models like Sonar Pro to process nuanced, multi-part questions, deliver in-depth research, and support longer conversational context windows.
  * Optimized speed and efficiency: Benefit from Perplexity's lightweight, fast models that deliver nearly instant answers at scale, making them ideal for high-traffic or cost-sensitive applications.
  * Fine-grained output control: Adjust model parameters (e.g., creativity, repetition) and manage output quality to align with your application's unique requirements and user expectations.


###  [Available models](https://vercel.com/docs/agent-resources/integrations-for-models/perplexity#available-models)[](https://vercel.com/docs/agent-resources/integrations-for-models/perplexity#available-models)
The Sonar models are each optimized for tasks such as real-time search, advanced reasoning, and in-depth research. Please refer to Perplexity's list of available models
### Some available models on Perplexity API
Sonar Pro
**Type:** Chat
Perplexity's premier offering with search grounding, supporting advanced queries and follow-ups.
Sonar
**Type:** Chat
Perplexity's lightweight offering with search grounding, quicker and cheaper than Sonar Pro.
##  [Getting started](https://vercel.com/docs/agent-resources/integrations-for-models/perplexity#getting-started)[](https://vercel.com/docs/agent-resources/integrations-for-models/perplexity#getting-started)
The Vercel Perplexity API integration can be accessed through the AI tab on your [Vercel dashboard](https://vercel.com/dashboard).
###  [Prerequisites](https://vercel.com/docs/agent-resources/integrations-for-models/perplexity#prerequisites)[](https://vercel.com/docs/agent-resources/integrations-for-models/perplexity#prerequisites)
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



###  [Add the provider to your project](https://vercel.com/docs/agent-resources/integrations-for-models/perplexity#add-the-provider-to-your-project)[](https://vercel.com/docs/agent-resources/integrations-for-models/perplexity#add-the-provider-to-your-project)
####  [Using the dashboard](https://vercel.com/docs/agent-resources/integrations-for-models/perplexity#using-the-dashboard)[](https://vercel.com/docs/agent-resources/integrations-for-models/perplexity#using-the-dashboard)
  1. Navigate to the AI tab in your [Vercel dashboard](https://vercel.com/dashboard)
  2. Select Perplexity API from the list of providers, and press Add
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
pnpm i @ai-sdk/perplexity ai
```

```
yarn add @ai-sdk/perplexity ai
```

```
npm i @ai-sdk/perplexity ai
```

```
bun add @ai-sdk/perplexity ai
```

  10. Connect your project using the code below:
app/api/chat/route.ts
Next.js (/app) Next.js (/pages) SvelteKit Other frameworks
```
import { perplexity } from '@ai-sdk/perplexity';import { streamText } from 'ai';
// Allow streaming responses up to 30 secondsexport const maxDuration = 30;
export async function POST(req: Request) {  // Extract the `messages` from the body of the request  const { messages } = await req.json();
  // Call the language model  const result = streamText({    model: perplexity('sonar-pro'),    messages,  });
  // Respond with the stream  return result.toDataStreamResponse();}

```

```
import { perplexity } from '@ai-sdk/perplexity';import { streamText } from 'ai';import { NextApiRequest, NextApiResponse } from 'next';
// Allow streaming responses up to 30 secondsexport const maxDuration = 30;
export default async function handler(  request: NextApiRequest,  response: NextApiResponse,) {  // Extract the `messages` from the body of the request  const { messages } = await request.body;
  const result = streamText({    model: perplexity('sonar-pro'),    messages,  });
  // Write the data stream to the response  // Note: this is sent as a single response, not a stream  result.pipeDataStreamToResponse(response);}

```

```
import { perplexity } from '@ai-sdk/perplexity';import { streamText } from 'ai';import type { RequestHandler } from './$types';
export const POST = (async ({ request }) => {  const { messages } = await request.json();
  // Call the language model  const result = streamText({    model: perplexity('sonar-pro'),    messages,  });
  // Respond with the stream  return result.toDataStreamResponse();}) satisfies RequestHandler;

```

```
import { perplexity } from '@ai-sdk/perplexity';import { generateText } from 'ai';
const { text } = await generateText({  model: perplexity('sonar-pro'),  prompt: 'Write a vegetarian lasagna recipe for 4 people.',});

```



##  [More resources](https://vercel.com/docs/agent-resources/integrations-for-models/perplexity#more-resources)[](https://vercel.com/docs/agent-resources/integrations-for-models/perplexity#more-resources)
* * *
[ Previous OpenAI ](https://vercel.com/docs/agent-resources/integrations-for-models/openai)[ Next Pinecone ](https://vercel.com/docs/agent-resources/integrations-for-models/pinecone)
Was this helpful?
Send
