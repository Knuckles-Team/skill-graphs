##  [Reasoning](https://vercel.com/docs/ai-gateway/capabilities#reasoning)[](https://vercel.com/docs/ai-gateway/capabilities#reasoning)
Reasoning models can think through problems before responding, producing higher-quality answers for complex tasks. AI Gateway supports reasoning across OpenAI, Anthropic, Google, Vertex AI, and Amazon Bedrock, normalizing the different formats so you can switch providers without rewriting your code.
```
import { openai } from '@ai-sdk/openai';
import { generateText } from 'ai';

const { text, reasoning } = await generateText({
  model: openai('openai/gpt-5'),
  prompt: 'Explain the Monty Hall problem step by step.',
  providerOptions: {
    openai: { reasoningSummary: 'detailed' },
  },
});
```

Each provider has its own configuration. See the [Reasoning docs](https://vercel.com/docs/ai-gateway/capabilities/reasoning) for provider-specific setup and examples.
