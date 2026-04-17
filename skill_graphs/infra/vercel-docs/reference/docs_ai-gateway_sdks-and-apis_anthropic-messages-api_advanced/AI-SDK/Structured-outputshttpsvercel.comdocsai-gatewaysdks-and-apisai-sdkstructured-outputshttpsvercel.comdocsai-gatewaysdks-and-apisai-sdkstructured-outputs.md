##  [Structured outputs](https://vercel.com/docs/ai-gateway/sdks-and-apis/ai-sdk#structured-outputs)[](https://vercel.com/docs/ai-gateway/sdks-and-apis/ai-sdk#structured-outputs)
Generate type-safe structured data with `generateObject` and a
structured.ts
```
import { generateObject } from 'ai';
import { z } from 'zod';

const { object } = await generateObject({
  model: 'anthropic/claude-sonnet-4.6',
  schema: z.object({
    name: z.string(),
    age: z.number(),
    city: z.string(),
  }),
  prompt: 'Extract: John is 30 years old and lives in NYC.',
});

console.log(object); // { name: 'John', age: 30, city: 'NYC' }
```
