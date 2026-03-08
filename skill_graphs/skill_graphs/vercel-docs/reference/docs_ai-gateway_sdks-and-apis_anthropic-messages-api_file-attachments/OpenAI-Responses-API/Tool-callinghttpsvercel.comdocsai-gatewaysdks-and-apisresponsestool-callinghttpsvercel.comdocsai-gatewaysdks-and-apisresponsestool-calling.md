##  [Tool calling](https://vercel.com/docs/ai-gateway/sdks-and-apis/responses#tool-calling)[](https://vercel.com/docs/ai-gateway/sdks-and-apis/responses#tool-calling)
Define tools with JSON Schema parameters. The model can call them, and you can feed the results back in a follow-up request:
TypeScriptPython
tools.ts
```
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env.AI_GATEWAY_API_KEY,
  baseURL: 'https://ai-gateway.vercel.sh/v1',
});

const response = await client.responses.create({
  model: 'openai/gpt-5.4',
  input: 'What is the weather in San Francisco?',
  tools: [
    {
      type: 'function',
      name: 'get_weather',
      description: 'Get the current weather for a location',
      strict: true,
      parameters: {
        type: 'object',
        properties: {
          location: { type: 'string' },
        },
        required: ['location'],
        additionalProperties: false,
      },
    },
  ],
});

// The model returns function_call items in the output
for (const item of response.output) {
  if (item.type === 'function_call') {
    console.log(`Call: ${item.name}(${item.arguments})`);
  }
}
```

tools.py
```
import os
import json
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv('AI_GATEWAY_API_KEY'),
    base_url='https://ai-gateway.vercel.sh/v1',
)

response = client.responses.create(
    model='openai/gpt-5.4',
    input='What is the weather in San Francisco?',
    tools=[
        {
            'type': 'function',
            'name': 'get_weather',
            'description': 'Get the current weather for a location',
            'strict': True,
            'parameters': {
                'type': 'object',
                'properties': {
                    'location': {'type': 'string'},
                },
                'required': ['location'],
                'additionalProperties': False,
            },
        },
    ],
)

for item in response.output:
    if item.type == 'function_call':
        print(f'Call: {item.name}({item.arguments})')
```

To continue the conversation with tool results, include the function call and its output in the next request's `input` array:
TypeScriptPython
tool-followup.ts
```
const functionCall = response.output.find(
  (item) => item.type === 'function_call',
);

const followup = await client.responses.create({
  model: 'openai/gpt-5.4',
  input: [
    { role: 'user', content: 'What is the weather in San Francisco?' },
    {
      type: 'function_call',
      id: functionCall.id,
      call_id: functionCall.call_id,
      name: functionCall.name,
      arguments: functionCall.arguments,
    },
    {
      type: 'function_call_output',
      call_id: functionCall.call_id,
      output: JSON.stringify({ temperature: 68, condition: 'Sunny' }),
    },
  ],
  tools: [
    /* same tools as above */
  ],
});

console.log(followup.output_text);
```

tool-followup.py
```
import json

function_call = next(
    item for item in response.output if item.type == 'function_call'
)

followup = client.responses.create(
    model='openai/gpt-5.4',
    input=[
        {'role': 'user', 'content': 'What is the weather in San Francisco?'},
        {
            'type': 'function_call',
            'id': function_call.id,
            'call_id': function_call.call_id,
            'name': function_call.name,
            'arguments': function_call.arguments,
        },
        {
            'type': 'function_call_output',
            'call_id': function_call.call_id,
            'output': json.dumps({'temperature': 68, 'condition': 'Sunny'}),
        },
    ],
    tools=[
        # same tools as above
    ],
)

print(followup.output_text)
```
