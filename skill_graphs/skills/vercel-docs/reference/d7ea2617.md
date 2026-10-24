##  [Getting started](https://vercel.com/docs/ai-gateway/capabilities/reasoning/openai#getting-started)[](https://vercel.com/docs/ai-gateway/capabilities/reasoning/openai#getting-started)
###  [Streaming with reasoning summaries](https://vercel.com/docs/ai-gateway/capabilities/reasoning/openai#streaming-with-reasoning-summaries)[](https://vercel.com/docs/ai-gateway/capabilities/reasoning/openai#streaming-with-reasoning-summaries)
Set `reasoningSummary` to receive the model's thought process as it streams. Different models support different summarizers. For example, o4-mini supports detailed summaries.
stream-reasoning.ts
```
import { streamText } from 'ai';

const result = streamText({
  model: 'openai/gpt-5',
  prompt: 'Tell me about the Mission burrito debate in San Francisco.',
  providerOptions: {
    openai: {
      reasoningEffort: 'high',
      reasoningSummary: 'detailed', // 'auto' for condensed or 'detailed' for comprehensive
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

###  [Non-streaming](https://vercel.com/docs/ai-gateway/capabilities/reasoning/openai#non-streaming)[](https://vercel.com/docs/ai-gateway/capabilities/reasoning/openai#non-streaming)
For non-streaming calls, reasoning summaries are available in the `reasoning` field:
generate-reasoning.ts
```
import { generateText } from 'ai';

const result = await generateText({
  model: 'openai/gpt-5',
  prompt: 'Tell me about the Mission burrito debate in San Francisco.',
  providerOptions: {
    openai: {
      reasoningEffort: 'high',
      reasoningSummary: 'auto',
    },
  },
});

console.log('Reasoning:', result.reasoningText);
```
