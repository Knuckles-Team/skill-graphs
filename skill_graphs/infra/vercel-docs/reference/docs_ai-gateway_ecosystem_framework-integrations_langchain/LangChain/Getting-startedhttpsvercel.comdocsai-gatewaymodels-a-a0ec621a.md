##  [Getting started](https://vercel.com/docs/ai-gateway/models-and-providers#getting-started)[](https://vercel.com/docs/ai-gateway/models-and-providers#getting-started)
  1. ###  [Create a new project](https://vercel.com/docs/ai-gateway/models-and-providers#create-a-new-project)[](https://vercel.com/docs/ai-gateway/models-and-providers#create-a-new-project)
First, create a new directory for your project and initialize it:
terminal
```
mkdir langchain-ai-gateway
cd langchain-ai-gateway
pnpm dlx init -y
```

  2. ###  [Install dependencies](https://vercel.com/docs/ai-gateway/models-and-providers#install-dependencies)[](https://vercel.com/docs/ai-gateway/models-and-providers#install-dependencies)
Install the required LangChain packages along with the `dotenv` and `@types/node` packages:
Terminal
![](https://7nyt0uhk7sse4zvn.public.blob.vercel-storage.com/docs-assets/static/topics/icons/pnpm.svg)pnpm bun yarn npm
```
pnpm i langchain @langchain/core @langchain/openai dotenv @types/node
```

```
yarn add langchain @langchain/core @langchain/openai dotenv @types/node
```

```
npm i langchain @langchain/core @langchain/openai dotenv @types/node
```

```
bun add langchain @langchain/core @langchain/openai dotenv @types/node
```

  3. ###  [Configure environment variables](https://vercel.com/docs/ai-gateway/models-and-providers#configure-environment-variables)[](https://vercel.com/docs/ai-gateway/models-and-providers#configure-environment-variables)
Create a `.env` file with your [Vercel AI Gateway API key](https://vercel.com/docs/ai-gateway#using-the-ai-gateway-with-an-api-key):
.env
```
AI_GATEWAY_API_KEY=your-api-key-here
```

If you're using the [AI Gateway from within a Vercel deployment](https://vercel.com/docs/ai-gateway#using-the-ai-gateway-with-a-vercel-oidc-token), you can also use the `VERCEL_OIDC_TOKEN` environment variable which will be automatically provided.
  4. ###  [Create your LangChain application](https://vercel.com/docs/ai-gateway/models-and-providers#create-your-langchain-application)[](https://vercel.com/docs/ai-gateway/models-and-providers#create-your-langchain-application)
Create a new file called `index.ts` with the following code:
index.ts
```
import 'dotenv/config';
import { ChatOpenAI } from '@langchain/openai';
import { HumanMessage } from '@langchain/core/messages';

async function main() {
  console.log('=== LangChain Chat Completion with AI Gateway ===');

  const apiKey =
    process.env.AI_GATEWAY_API_KEY || process.env.VERCEL_OIDC_TOKEN;

  const chat = new ChatOpenAI({
    apiKey: apiKey,
    modelName: 'openai/gpt-5.4',
    temperature: 0.7,
    configuration: {
      baseURL: 'https://ai-gateway.vercel.sh/v1',
    },
  });

  try {
    const response = await chat.invoke([
      new HumanMessage('Write a one-sentence bedtime story about a unicorn.'),
    ]);

    console.log('Response:', response.content);
  } catch (error) {
    console.error('Error:', error);
  }
}

main().catch(console.error);
```

The following code:
     * Initializes a `ChatOpenAI` instance configured to use the AI Gateway
     * Sets the model `temperature` to `0.7`
     * Makes a chat completion request
     * Handles any potential errors
  5. ###  [Running the application](https://vercel.com/docs/ai-gateway/models-and-providers#running-the-application)[](https://vercel.com/docs/ai-gateway/models-and-providers#running-the-application)
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
[ Previous Agent Quickstart ](https://vercel.com/docs/ai-gateway/agent-quickstart)[ Next Provider Options ](https://vercel.com/docs/ai-gateway/models-and-providers/provider-options)
Was this helpful?
Send
On this page
  * [Getting started](https://vercel.com/docs/ai-gateway/models-and-providers#getting-started)
  * [Create a new project](https://vercel.com/docs/ai-gateway/models-and-providers#create-a-new-project)
  * [Install dependencies](https://vercel.com/docs/ai-gateway/models-and-providers#install-dependencies)
  * [Configure environment variables](https://vercel.com/docs/ai-gateway/models-and-providers#configure-environment-variables)
  * [Create your LangChain application](https://vercel.com/docs/ai-gateway/models-and-providers#create-your-langchain-application)
  * [Running the application](https://vercel.com/docs/ai-gateway/models-and-providers#running-the-application)


Copy as MarkdownGive feedbackAsk AI about this page
