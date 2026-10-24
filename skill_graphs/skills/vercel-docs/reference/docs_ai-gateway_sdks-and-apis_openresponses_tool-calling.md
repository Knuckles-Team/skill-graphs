[AI Gateway](https://vercel.com/docs/ai-gateway)
[SDKs & APIs](https://vercel.com/docs/ai-gateway/sdks-and-apis)
[OpenResponses API](https://vercel.com/docs/ai-gateway/sdks-and-apis/openresponses)
Tool Calling
[AI Gateway](https://vercel.com/docs/ai-gateway)
[SDKs & APIs](https://vercel.com/docs/ai-gateway/sdks-and-apis)
[OpenResponses API](https://vercel.com/docs/ai-gateway/sdks-and-apis/openresponses)
Tool Calling
# Tool Calling
Last updated January 21, 2026
The [OpenResponses API](https://vercel.com/docs/ai-gateway/sdks-and-apis/openresponses) supports tool calling to give models access to external functions. Define tools in your request with a name, description, and JSON schema for parameters. When the model determines it needs a tool to answer the user's question, it returns a `function_call` output with the tool name and arguments for you to execute.
TypeScriptPython
tool-calls.ts
```
const apiKey = process.env.AI_GATEWAY_API_KEY;

const response = await fetch('https://ai-gateway.vercel.sh/v1/responses', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    Authorization: `Bearer ${apiKey}`,
  },
  body: JSON.stringify({
    model: 'openai/gpt-5.4',
    input: [
      {
        type: 'message',
        role: 'user',
        content: 'What is the weather like in New York?',
      },
    ],
    tools: [
      {
        type: 'function',
        function: {
          name: 'get_weather',
          description: 'Get the current weather in a location',
          parameters: {
            type: 'object',
            properties: {
              location: {
                type: 'string',
                description: 'The city and state, e.g. San Francisco, CA',
              },
            },
            required: ['location'],
          },
        },
      },
    ],
    tool_choice: 'auto',
  }),
});
```

tool-calls.py
```
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv('AI_GATEWAY_API_KEY'),
    base_url='https://ai-gateway.vercel.sh/v1',
)

response = client.responses.create(
    model='openai/gpt-5.4',
    input=[
        {
            'type': 'message',
            'role': 'user',
            'content': 'What is the weather like in New York?',
        },
    ],
    tools=[
        {
            'type': 'function',
            'function': {
                'name': 'get_weather',
                'description': 'Get the current weather in a location',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'location': {
                            'type': 'string',
                            'description': 'The city and state, e.g. San Francisco, CA',
                        },
                    },
                    'required': ['location'],
                },
            },
        },
    ],
    tool_choice='auto',
)
```

##  [Tool call response](https://vercel.com/docs/ai-gateway/sdks-and-apis/openresponses/tool-calling#tool-call-response)[](https://vercel.com/docs/ai-gateway/sdks-and-apis/openresponses/tool-calling#tool-call-response)
When the model decides to call a tool, the response includes a `function_call` output:
```
{
  "output": [
    {
      "type": "function_call",
      "name": "get_weather",
      "arguments": "{\"location\": \"New York, NY\"}",
      "call_id": "call_abc123"
    }
  ]
}
```

##  [Tool choice options](https://vercel.com/docs/ai-gateway/sdks-and-apis/openresponses/tool-calling#tool-choice-options)[](https://vercel.com/docs/ai-gateway/sdks-and-apis/openresponses/tool-calling#tool-choice-options)
  * `auto` - The model decides whether to call a tool
  * `required` - The model must call at least one tool
  * `none` - The model cannot call any tools


* * *
[ Previous Image Input ](https://vercel.com/docs/ai-gateway/sdks-and-apis/openresponses/image-input)[ Next Provider Options ](https://vercel.com/docs/ai-gateway/sdks-and-apis/openresponses/provider-options)
Was this helpful?
Send
