##  [Streaming](https://vercel.com/docs/ai-gateway/sdks-and-apis/ai-sdk#streaming)[](https://vercel.com/docs/ai-gateway/sdks-and-apis/ai-sdk#streaming)
Stream responses token-by-token for real-time output:
stream.ts
```
import { streamText } from 'ai';

const result = streamText({
  model: 'openai/gpt-5.4',
  prompt: 'Write a short story about a robot discovering music.',
});

for await (const textPart of result.textStream) {
  process.stdout.write(textPart);
}
```
