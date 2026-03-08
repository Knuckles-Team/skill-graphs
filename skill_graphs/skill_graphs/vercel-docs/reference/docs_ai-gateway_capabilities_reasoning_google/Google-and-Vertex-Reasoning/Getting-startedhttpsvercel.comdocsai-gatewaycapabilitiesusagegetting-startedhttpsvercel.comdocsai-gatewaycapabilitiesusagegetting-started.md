##  [Getting started](https://vercel.com/docs/ai-gateway/capabilities/usage#getting-started)[](https://vercel.com/docs/ai-gateway/capabilities/usage#getting-started)
###  [Gemini 3 and 3.1 models](https://vercel.com/docs/ai-gateway/capabilities/usage#gemini-3-and-3.1-models)[](https://vercel.com/docs/ai-gateway/capabilities/usage#gemini-3-and-3.1-models)
Use the `thinkingLevel` parameter to control the depth of reasoning:
gemini-3-thinking.ts
```
import { generateText } from 'ai';

const result = await generateText({
  model: 'google/gemini-3.1-pro-preview',
  prompt: 'What is the sum of the first 10 prime numbers?',
  providerOptions: {
    vertex: { // use vertex or google
      thinkingConfig: {
        thinkingLevel: 'high',
        includeThoughts: true,
      },
    },
  },
});

console.log(result.text);
console.log(result.reasoningText);
```

###  [Gemini 2.5 models](https://vercel.com/docs/ai-gateway/capabilities/usage#gemini-2.5-models)[](https://vercel.com/docs/ai-gateway/capabilities/usage#gemini-2.5-models)
Use the `thinkingBudget` parameter to control the number of thinking tokens:
gemini-25-thinking.ts
```
import { generateText } from 'ai';

const result = await generateText({
  model: 'google/gemini-2.5-flash',
  prompt: 'What is the sum of the first 10 prime numbers?',
  providerOptions: {
    vertex: { // use vertex or google
      thinkingConfig: {
        thinkingBudget: 8192,
        includeThoughts: true,
      },
    },
  },
});

console.log(result.text);
console.log(result.reasoningText);
```

###  [Streaming](https://vercel.com/docs/ai-gateway/capabilities/usage#streaming)[](https://vercel.com/docs/ai-gateway/capabilities/usage#streaming)
When streaming, thinking tokens are emitted as `reasoning-delta` stream parts:
gemini-stream-thinking.ts
```
import { streamText } from 'ai';

const result = streamText({
  model: 'google/gemini-2.5-flash',
  prompt: 'Explain quantum computing in simple terms.',
  providerOptions: {
    vertex: { // use vertex or google
      thinkingConfig: {
        thinkingBudget: 2048,
        includeThoughts: true,
      },
    },
  },
});

for await (const part of result.fullStream) {
  if (part.type === 'reasoning-delta') {
    process.stdout.write(part.text);
  } else if (part.type === 'text-delta') {
    process.stdout.write(part.text);
  }
}
```
