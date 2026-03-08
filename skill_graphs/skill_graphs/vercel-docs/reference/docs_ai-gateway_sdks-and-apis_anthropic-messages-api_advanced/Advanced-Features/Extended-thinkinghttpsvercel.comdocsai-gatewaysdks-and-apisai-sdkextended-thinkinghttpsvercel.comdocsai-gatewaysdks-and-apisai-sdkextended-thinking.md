##  [Extended thinking](https://vercel.com/docs/ai-gateway/sdks-and-apis/ai-sdk#extended-thinking)[](https://vercel.com/docs/ai-gateway/sdks-and-apis/ai-sdk#extended-thinking)
Configure extended thinking for models that support chain-of-thought reasoning. The `thinking` parameter allows you to control how reasoning tokens are generated and returned.
Example request
TypeScriptPython
thinking.ts
```
import Anthropic from '@anthropic-ai/sdk';

const apiKey = process.env.AI_GATEWAY_API_KEY || process.env.VERCEL_OIDC_TOKEN;

const anthropic = new Anthropic({
  apiKey,
  baseURL: 'https://ai-gateway.vercel.sh',
});

const message = await anthropic.messages.create({
  model: 'anthropic/claude-sonnet-4.6',
  max_tokens: 2048,
  thinking: {
    type: 'enabled',
    budget_tokens: 5000,
  },
  messages: [
    {
      role: 'user',
      content: 'Explain quantum entanglement in simple terms.',
    },
  ],
});

for (const block of message.content) {
  if (block.type === 'thinking') {
    console.log('🧠 Thinking:', block.thinking);
  } else if (block.type === 'text') {
    console.log('💬 Response:', block.text);
  }
}
```

thinking.py
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
    max_tokens=2048,
    thinking={
        'type': 'enabled',
        'budget_tokens': 5000,
    },
    messages=[
        {
            'role': 'user',
            'content': 'Explain quantum entanglement in simple terms.'
        }
    ],
)

for block in message.content:
    if block.type == 'thinking':
        print('🧠 Thinking:', block.thinking)
    elif block.type == 'text':
        print('💬 Response:', block.text)
```

###  [Thinking parameters](https://vercel.com/docs/ai-gateway/sdks-and-apis/ai-sdk#thinking-parameters)[](https://vercel.com/docs/ai-gateway/sdks-and-apis/ai-sdk#thinking-parameters)
  * `type`: Set to `'enabled'` to enable extended thinking
  * `budget_tokens`: Maximum number of tokens to allocate for thinking


###  [Response with thinking](https://vercel.com/docs/ai-gateway/sdks-and-apis/ai-sdk#response-with-thinking)[](https://vercel.com/docs/ai-gateway/sdks-and-apis/ai-sdk#response-with-thinking)
When thinking is enabled, the response includes thinking blocks:
```
{
  "id": "msg_123",
  "type": "message",
  "role": "assistant",
  "content": [
    {
      "type": "thinking",
      "thinking": "Let me think about how to explain quantum entanglement...",
      "signature": "anthropic-signature-xyz"
    },
    {
      "type": "text",
      "text": "Quantum entanglement is like having two magic coins..."
    }
  ],
  "model": "anthropic/claude-sonnet-4.6",
  "stop_reason": "end_turn",
  "usage": {
    "input_tokens": 15,
    "output_tokens": 150
  }
}
```
