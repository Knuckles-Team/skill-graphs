##  [Getting started](https://vercel.com/docs/ai-gateway/capabilities/observability#getting-started)[](https://vercel.com/docs/ai-gateway/capabilities/observability#getting-started)
###  [Adaptive thinking (Claude 4.6)](https://vercel.com/docs/ai-gateway/capabilities/observability#adaptive-thinking-claude-4.6)[](https://vercel.com/docs/ai-gateway/capabilities/observability#adaptive-thinking-claude-4.6)
Configure adaptive thinking through `providerOptions`. Claude dynamically decides when and how much to think:
adaptive-thinking.ts
```
import { generateText } from 'ai';

const result = await generateText({
  model: 'anthropic/claude-sonnet-4.6',
  prompt: 'Explain quantum entanglement in simple terms.',
  providerOptions: {
    anthropic: {
      thinking: { type: 'adaptive' },
    },
  },
});

console.log('Thinking:', result.reasoningText);
console.log('Response:', result.text);
```

###  [Streaming with adaptive thinking](https://vercel.com/docs/ai-gateway/capabilities/observability#streaming-with-adaptive-thinking)[](https://vercel.com/docs/ai-gateway/capabilities/observability#streaming-with-adaptive-thinking)
stream-adaptive.ts
```
import { streamText } from 'ai';

const result = streamText({
  model: 'anthropic/claude-opus-4.6',
  prompt: 'Explain quantum entanglement in simple terms.',
  providerOptions: {
    anthropic: {
      thinking: { type: 'adaptive' },
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

###  [Manual thinking (Claude 4, Opus 4.5)](https://vercel.com/docs/ai-gateway/capabilities/observability#manual-thinking-claude-4-opus-4.5)[](https://vercel.com/docs/ai-gateway/capabilities/observability#manual-thinking-claude-4-opus-4.5)
For older models, use `type: 'enabled'` with a `budgetTokens` value:
manual-thinking.ts
```
import { generateText } from 'ai';

const result = await generateText({
  model: 'anthropic/claude-opus-4',
  prompt: 'Explain quantum entanglement in simple terms.',
  providerOptions: {
    anthropic: {
      thinking: {
        type: 'enabled',
        budgetTokens: 5000,
      },
    },
  },
});

console.log('Thinking:', result.reasoningText);
console.log('Response:', result.text);
```
