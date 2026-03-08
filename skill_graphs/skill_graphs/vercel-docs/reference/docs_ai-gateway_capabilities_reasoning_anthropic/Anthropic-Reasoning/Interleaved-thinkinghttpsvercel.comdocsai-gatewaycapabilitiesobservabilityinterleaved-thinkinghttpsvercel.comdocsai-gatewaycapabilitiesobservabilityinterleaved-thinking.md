##  [Interleaved thinking](https://vercel.com/docs/ai-gateway/capabilities/observability#interleaved-thinking)[](https://vercel.com/docs/ai-gateway/capabilities/observability#interleaved-thinking)
Interleaved thinking lets Claude think between tool calls, producing better reasoning in multi-step workflows.
  * Claude Opus 4.6: Automatically enabled with adaptive thinking
  * Claude Sonnet 4.6, Opus 4.5, 4.1, 4, Sonnet 4.5, 4: Pass the `interleaved-thinking-2025-05-14` beta header when extended thinking is enabled


interleaved-thinking.ts
```
import { generateText } from 'ai';

const result = await generateText({
  model: 'anthropic/claude-sonnet-4.6',
  prompt: 'Search for the weather and summarize it.',
  providerOptions: {
    anthropic: {
      thinking: { type: 'enabled', budgetTokens: 5000 },
      headers: {
        'anthropic-beta': 'interleaved-thinking-2025-05-14',
      },
    },
  },
  tools: {
    // your tools here
  },
});
```

With interleaved thinking, `budgetTokens` can exceed the model's max output tokens since it represents the total budget across all thinking blocks in a single turn.
For more details, see the
