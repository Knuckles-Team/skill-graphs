##  [Tool calling](https://vercel.com/docs/ai-gateway/sdks-and-apis/ai-sdk#tool-calling)[](https://vercel.com/docs/ai-gateway/sdks-and-apis/ai-sdk#tool-calling)
Define tools that models can invoke to interact with external systems:
tools.ts
```
import { generateText, tool } from 'ai';
import { z } from 'zod';

const { text, toolResults } = await generateText({
  model: 'anthropic/claude-sonnet-4.6',
  tools: {
    getWeather: tool({
      description: 'Get the current weather for a location',
      parameters: z.object({
        location: z.string().describe('City name, e.g. San Francisco'),
      }),
      execute: async ({ location }) => ({
        location,
        temperature: 72,
        condition: 'sunny',
      }),
    }),
  },
  prompt: "What's the weather in Tokyo?",
});

console.log(text);
```
