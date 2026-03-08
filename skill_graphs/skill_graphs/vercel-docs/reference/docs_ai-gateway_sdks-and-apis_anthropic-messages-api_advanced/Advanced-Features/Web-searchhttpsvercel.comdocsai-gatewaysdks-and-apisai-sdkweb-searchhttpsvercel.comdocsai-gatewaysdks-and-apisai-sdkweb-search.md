##  [Web search](https://vercel.com/docs/ai-gateway/sdks-and-apis/ai-sdk#web-search)[](https://vercel.com/docs/ai-gateway/sdks-and-apis/ai-sdk#web-search)
Use the built-in web search tool to give the model access to current information from the web.
Example request
TypeScriptPython
web-search.ts
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
  tools: [
    {
      type: 'web_search_20250305',
      name: 'web_search',
    },
  ],
  messages: [
    {
      role: 'user',
      content: 'What are the latest developments in quantum computing?',
    },
  ],
});

for (const block of message.content) {
  if (block.type === 'text') {
    console.log(block.text);
  } else if (block.type === 'web_search_tool_result') {
    console.log('Search results received');
  }
}
```

web-search.py
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
    tools=[
        {
            'type': 'web_search_20250305',
            'name': 'web_search',
        }
    ],
    messages=[
        {
            'role': 'user',
            'content': 'What are the latest developments in quantum computing?'
        }
    ],
)

for block in message.content:
    if block.type == 'text':
        print(block.text)
    elif block.type == 'web_search_tool_result':
        print('Search results received')
```
