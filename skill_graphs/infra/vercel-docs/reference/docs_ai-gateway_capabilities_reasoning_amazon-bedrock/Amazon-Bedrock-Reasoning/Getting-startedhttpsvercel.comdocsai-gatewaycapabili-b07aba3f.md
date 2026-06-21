##  [Getting started](https://vercel.com/docs/ai-gateway/capabilities/image-generation#getting-started)[](https://vercel.com/docs/ai-gateway/capabilities/image-generation#getting-started)
###  [Adaptive reasoning (Claude 4.6)](https://vercel.com/docs/ai-gateway/capabilities/image-generation#adaptive-reasoning-claude-4.6)[](https://vercel.com/docs/ai-gateway/capabilities/image-generation#adaptive-reasoning-claude-4.6)
For Claude 4.6 models on Bedrock, use `type: 'adaptive'` with a `maxReasoningEffort` level:
bedrock-adaptive.ts
```
import { generateText } from 'ai';

const result = await generateText({
  model: 'anthropic/claude-opus-4.6',
  prompt: 'How many "r"s are in the word "strawberry"?',
  providerOptions: {
    bedrock: {
      reasoningConfig: { type: 'adaptive', maxReasoningEffort: 'max' },
    },
  },
});

console.log(result.reasoning);
console.log(result.text);
```

###  [Manual reasoning (older models)](https://vercel.com/docs/ai-gateway/capabilities/image-generation#manual-reasoning-older-models)[](https://vercel.com/docs/ai-gateway/capabilities/image-generation#manual-reasoning-older-models)
For older Anthropic models on Bedrock, use `type: 'enabled'` with a `budgetTokens` value:
bedrock-manual.ts
```
import { generateText } from 'ai';

const result = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  prompt: 'How many people will live in the world in 2040?',
  providerOptions: {
    bedrock: {
      reasoningConfig: { type: 'enabled', budgetTokens: 2048 },
    },
  },
});

console.log(result.reasoning);
console.log(result.text);
```
