##  [Quick start](https://vercel.com/docs/ai-gateway/sdks-and-apis/ai-sdk#quick-start)[](https://vercel.com/docs/ai-gateway/sdks-and-apis/ai-sdk#quick-start)
Generate text by passing a plain string model ID. AI Gateway resolves the provider and routes the request automatically.
index.ts
```
import { generateText } from 'ai';

const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.6',
  prompt: 'Explain quantum computing in one paragraph.',
});

console.log(text);
```
