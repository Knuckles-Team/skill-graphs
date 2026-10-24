# File Attachments
Last updated January 21, 2026
Send images and PDF documents as part of your message request.
Example request
TypeScriptPython
file-attachment.ts
```
import Anthropic from '@anthropic-ai/sdk';
import fs from 'node:fs';

const apiKey = process.env.AI_GATEWAY_API_KEY || process.env.VERCEL_OIDC_TOKEN;

const anthropic = new Anthropic({
  apiKey,
  baseURL: 'https://ai-gateway.vercel.sh',
});

// Read files as base64
const pdfData = fs.readFileSync('./document.pdf');
const imageData = fs.readFileSync('./image.png');

const pdfBase64 = pdfData.toString('base64');
const imageBase64 = imageData.toString('base64');

const message = await anthropic.messages.create({
  model: 'anthropic/claude-sonnet-4.6',
  max_tokens: 1024,
  messages: [
    {
      role: 'user',
      content: [
        {
          type: 'document',
          source: {
            type: 'base64',
            media_type: 'application/pdf',
            data: pdfBase64,
          },
        },
        {
          type: 'image',
          source: {
            type: 'base64',
            media_type: 'image/png',
            data: imageBase64,
          },
        },
        {
          type: 'text',
          text: 'Please summarize the PDF and describe the image.',
        },
      ],
    },
  ],
});

console.log('Response:', message.content[0].text);
```

file-attachment.py
```
import os
import base64
import anthropic

api_key = os.getenv('AI_GATEWAY_API_KEY') or os.getenv('VERCEL_OIDC_TOKEN')

client = anthropic.Anthropic(
    api_key=api_key,
    base_url='https://ai-gateway.vercel.sh'
)

# Read files as base64
with open('./document.pdf', 'rb') as f:
    pdf_base64 = base64.b64encode(f.read()).decode('utf-8')

with open('./image.png', 'rb') as f:
    image_base64 = base64.b64encode(f.read()).decode('utf-8')

message = client.messages.create(
    model='anthropic/claude-sonnet-4.6',
    max_tokens=1024,
    messages=[
        {
            'role': 'user',
            'content': [
                {
                    'type': 'document',
                    'source': {
                        'type': 'base64',
                        'media_type': 'application/pdf',
                        'data': pdf_base64,
                    },
                },
                {
                    'type': 'image',
                    'source': {
                        'type': 'base64',
                        'media_type': 'image/png',
                        'data': image_base64,
                    },
                },
                {
                    'type': 'text',
                    'text': 'Please summarize the PDF and describe the image.',
                },
            ],
        }
    ],
)

print('Response:', message.content[0].text)
```

###  [Supported file types](https://vercel.com/docs/ai-gateway/sdks-and-apis/responses#supported-file-types)[](https://vercel.com/docs/ai-gateway/sdks-and-apis/responses#supported-file-types)
  * Images: `image/jpeg`, `image/png`, `image/gif`, `image/webp`
  * Documents: `application/pdf`


* * *
[ Previous AI SDK ](https://vercel.com/docs/ai-gateway/sdks-and-apis/ai-sdk)[ Next OpenAI Chat Completions API ](https://vercel.com/docs/ai-gateway/sdks-and-apis/openai-chat-completions)
Was this helpful?
Send
On this page
  * [Supported file types](https://vercel.com/docs/ai-gateway/sdks-and-apis/responses#supported-file-types)


Copy as MarkdownGive feedbackAsk AI about this page
