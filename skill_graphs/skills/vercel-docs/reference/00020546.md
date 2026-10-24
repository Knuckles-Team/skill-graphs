##  [Getting started](https://vercel.com/docs/ai-gateway/capabilities#getting-started)[](https://vercel.com/docs/ai-gateway/capabilities#getting-started)
  1. ###  [Create a new project](https://vercel.com/docs/ai-gateway/capabilities#create-a-new-project)[](https://vercel.com/docs/ai-gateway/capabilities#create-a-new-project)
First, create a new directory for your project and initialize it:
terminal
```
mkdir langfuse-ai-gateway
cd langfuse-ai-gateway
pnpm dlx init -y
```

  2. ###  [Install dependencies](https://vercel.com/docs/ai-gateway/capabilities#install-dependencies)[](https://vercel.com/docs/ai-gateway/capabilities#install-dependencies)
Install the required LangFuse packages along with the `dotenv` and `@types/node` packages:
Terminal
![](https://7nyt0uhk7sse4zvn.public.blob.vercel-storage.com/docs-assets/static/topics/icons/pnpm.svg)pnpm bun yarn npm
```
pnpm i langfuse openai dotenv @types/node
```

```
yarn add langfuse openai dotenv @types/node
```

```
npm i langfuse openai dotenv @types/node
```

```
bun add langfuse openai dotenv @types/node
```

  3. ###  [Configure environment variables](https://vercel.com/docs/ai-gateway/capabilities#configure-environment-variables)[](https://vercel.com/docs/ai-gateway/capabilities#configure-environment-variables)
Create a `.env` file with your [Vercel AI Gateway API key](https://vercel.com/docs/ai-gateway#using-the-ai-gateway-with-an-api-key) and LangFuse API keys:
.env
```
AI_GATEWAY_API_KEY=your-api-key-here

LANGFUSE_PUBLIC_KEY=your_langfuse_public_key
LANGFUSE_SECRET_KEY=your_langfuse_secret_key
LANGFUSE_HOST=https://cloud.langfuse.com
```

If you're using the [AI Gateway from within a Vercel deployment](https://vercel.com/docs/ai-gateway#using-the-ai-gateway-with-a-vercel-oidc-token), you can also use the `VERCEL_OIDC_TOKEN` environment variable which will be automatically provided.
  4. ###  [Create your LangFuse application](https://vercel.com/docs/ai-gateway/capabilities#create-your-langfuse-application)[](https://vercel.com/docs/ai-gateway/capabilities#create-your-langfuse-application)
Create a new file called `index.ts` with the following code:
index.ts
```
import { observeOpenAI } from 'langfuse';
import OpenAI from 'openai';

const openaiClient = new OpenAI({
  apiKey: process.env.AI_GATEWAY_API_KEY,
  baseURL: 'https://ai-gateway.vercel.sh/v1',
});

const client = observeOpenAI(openaiClient, {
  generationName: 'fun-fact-request', // Optional: Name of the generation in Langfuse
});

const response = await client.chat.completions.create({
  model: 'moonshotai/kimi-k2',
  messages: [
    { role: 'system', content: 'You are a helpful assistant.' },
    { role: 'user', content: 'Tell me about the food scene in San Francisco.' },
  ],
});

console.log(response.choices[0].message.content);
```

The following code:
     * Creates an OpenAI client configured to use the Vercel AI Gateway
     * Uses `observeOpenAI` to wrap the client for automatic tracing and logging
     * Makes a chat completion request through the AI Gateway
     * Automatically captures request/response data, token usage, and metrics
  5. ###  [Running the application](https://vercel.com/docs/ai-gateway/capabilities#running-the-application)[](https://vercel.com/docs/ai-gateway/capabilities#running-the-application)
Run your application using Node.js:
Terminal
![](https://7nyt0uhk7sse4zvn.public.blob.vercel-storage.com/docs-assets/static/topics/icons/pnpm.svg)pnpm bun yarn npm
```
pnpm dlx tsx index.ts
```

```
yarn dlx tsx index.ts
```

```
npx tsx index.ts
```

```
bunx tsx index.ts
```

You should see a response from the AI model in your console.


* * *
[ Previous Models & Providers ](https://vercel.com/docs/ai-gateway/models-and-providers)[ Next Observability ](https://vercel.com/docs/ai-gateway/capabilities/observability)
Was this helpful?
Send
On this page
  * [Getting started](https://vercel.com/docs/ai-gateway/capabilities#getting-started)
  * [Create a new project](https://vercel.com/docs/ai-gateway/capabilities#create-a-new-project)
  * [Install dependencies](https://vercel.com/docs/ai-gateway/capabilities#install-dependencies)
  * [Configure environment variables](https://vercel.com/docs/ai-gateway/capabilities#configure-environment-variables)
  * [Create your LangFuse application](https://vercel.com/docs/ai-gateway/capabilities#create-your-langfuse-application)
  * [Running the application](https://vercel.com/docs/ai-gateway/capabilities#running-the-application)


Copy as MarkdownGive feedbackAsk AI about this page
