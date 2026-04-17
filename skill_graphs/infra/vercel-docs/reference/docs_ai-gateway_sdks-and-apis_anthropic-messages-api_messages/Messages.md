# Messages
Last updated January 21, 2026
Create messages using the Anthropic Messages API format.
Endpoint
`POST /v1/messages `
###  [Basic message](https://vercel.com/docs/ai-gateway/capabilities#basic-message)[](https://vercel.com/docs/ai-gateway/capabilities#basic-message)
Create a non-streaming message.
Example request
TypeScriptPython
generate.ts
```
import Anthropic from '@anthropic-ai/sdk';

const apiKey = process.env.AI_GATEWAY_API_KEY || process.env.VERCEL_OIDC_TOKEN;

const anthropic = new Anthropic({
  apiKey,
  baseURL: 'https://ai-gateway.vercel.sh',
});

const message = await anthropic.messages.create({
  model: 'anthropic/claude-sonnet-4.6',
  max_tokens: 150,
  messages: [
    {
      role: 'user',
      content: 'Write a one-sentence bedtime story about a unicorn.',
    },
  ],
  temperature: 0.7,
});

console.log('Response:', message.content[0].text);
console.log('Usage:', message.usage);
```

generate.py
```
import os
import anthropic

api_key = os.getenv('AI_GATEWAY_API_KEY') or os.getenv('VERCEL_OIDC_TOKEN')

client = anthropic.Anthropic(
    api_key=api_key,
    base_url='https://ai-gateway.vercel.sh'
)

message = client.messages.create(
    model='anthropic/claude-sonnet-4.6',
    max_tokens=150,
    messages=[
        {
            'role': 'user',
            'content': 'Write a one-sentence bedtime story about a unicorn.'
        }
    ],
    temperature=0.7,
)

print('Response:', message.content[0].text)
print('Usage:', message.usage)
```

Response format
```
{
  "id": "msg_123",
  "type": "message",
  "role": "assistant",
  "content": [
    {
      "type": "text",
      "text": "Once upon a time, a gentle unicorn with a shimmering silver mane danced through moonlit clouds, sprinkling stardust dreams upon sleeping children below."
    }
  ],
  "model": "anthropic/claude-sonnet-4.6",
  "stop_reason": "end_turn",
  "usage": {
    "input_tokens": 15,
    "output_tokens": 28
  }
}
```

###  [Streaming messages](https://vercel.com/docs/ai-gateway/capabilities#streaming-messages)[](https://vercel.com/docs/ai-gateway/capabilities#streaming-messages)
Create a streaming message that delivers tokens as they are generated.
Example request
TypeScriptPython
stream.ts
```
import Anthropic from '@anthropic-ai/sdk';

const apiKey = process.env.AI_GATEWAY_API_KEY || process.env.VERCEL_OIDC_TOKEN;

const anthropic = new Anthropic({
  apiKey,
  baseURL: 'https://ai-gateway.vercel.sh',
});

const stream = await anthropic.messages.create({
  model: 'anthropic/claude-sonnet-4.6',
  max_tokens: 150,
  messages: [
    {
      role: 'user',
      content: 'Write a one-sentence bedtime story about a unicorn.',
    },
  ],
  temperature: 0.7,
  stream: true,
});

for await (const event of stream) {
  if (event.type === 'content_block_delta') {
    if (event.delta.type === 'text_delta') {
      process.stdout.write(event.delta.text);
    }
  }
}
```

stream.py
```
import os
import anthropic

api_key = os.getenv('AI_GATEWAY_API_KEY') or os.getenv('VERCEL_OIDC_TOKEN')

client = anthropic.Anthropic(
    api_key=api_key,
    base_url='https://ai-gateway.vercel.sh'
)

with client.messages.stream(
    model='anthropic/claude-sonnet-4.6',
    max_tokens=150,
    messages=[
        {
            'role': 'user',
            'content': 'Write a one-sentence bedtime story about a unicorn.'
        }
    ],
    temperature=0.7,
) as stream:
    for text in stream.text_stream:
        print(text, end='', flush=True)
```

####  [Streaming event types](https://vercel.com/docs/ai-gateway/capabilities#streaming-event-types)[](https://vercel.com/docs/ai-gateway/capabilities#streaming-event-types)
Streaming responses use
  * `message_start` - Initial message metadata
  * `content_block_start` - Start of a content block (text, tool use, etc.)
  * `content_block_delta` - Incremental content updates
  * `content_block_stop` - End of a content block
  * `message_delta` - Final message metadata (stop reason, usage)
  * `message_stop` - End of the message


* * *
[ Previous Models & Providers ](https://vercel.com/docs/ai-gateway/models-and-providers)[ Next Observability ](https://vercel.com/docs/ai-gateway/capabilities/observability)
Was this helpful?
Send
On this page
  * [Basic message](https://vercel.com/docs/ai-gateway/capabilities#basic-message)
  * [Streaming messages](https://vercel.com/docs/ai-gateway/capabilities#streaming-messages)
  * [Streaming event types](https://vercel.com/docs/ai-gateway/capabilities#streaming-event-types)


Copy as MarkdownGive feedbackAsk AI about this page
