##  [Quick start](https://vercel.com/docs/ai-gateway/sdks-and-apis#quick-start)[](https://vercel.com/docs/ai-gateway/sdks-and-apis#quick-start)
Point your existing SDK to the gateway:
AI SDKChat CompletionsOpenAI ResponsesAnthropic MessagesOpenResponses
```
npm i ai @ai-sdk/openai
```

```
import { generateText } from 'ai';

const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.6',
  prompt: 'Hello!',
});
```

```
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env.AI_GATEWAY_API_KEY,
  baseURL: 'https://ai-gateway.vercel.sh/v1',
});

const response = await client.chat.completions.create({
  model: 'anthropic/claude-sonnet-4.6',
  messages: [{ role: 'user', content: 'Hello!' }],
});
```

```
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env.AI_GATEWAY_API_KEY,
  baseURL: 'https://ai-gateway.vercel.sh/v1',
});

const response = await client.responses.create({
  model: 'anthropic/claude-sonnet-4.6',
  input: 'Hello!',
});
```

```
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env.AI_GATEWAY_API_KEY,
  baseURL: 'https://ai-gateway.vercel.sh',
});

const message = await client.messages.create({
  model: 'anthropic/claude-sonnet-4.6',
  max_tokens: 1024,
  messages: [{ role: 'user', content: 'Hello!' }],
});
```

```
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env.AI_GATEWAY_API_KEY,
  baseURL: 'https://ai-gateway.vercel.sh/openresponses/v1',
});

const response = await client.responses.create({
  model: 'anthropic/claude-sonnet-4.6',
  input: 'Hello!',
});
```
