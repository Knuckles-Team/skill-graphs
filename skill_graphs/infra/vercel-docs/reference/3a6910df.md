##  [Tool calling](https://vercel.com/docs/ai-gateway/sdks-and-apis/python#tool-calling)[](https://vercel.com/docs/ai-gateway/sdks-and-apis/python#tool-calling)
Enable models to call functions you define. This example shows a weather tool that the model can invoke.
Chat CompletionsOpenAI ResponsesAnthropic Messages
tools.py
```
import os
import json
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv('AI_GATEWAY_API_KEY'),
    base_url='https://ai-gateway.vercel.sh/v1'
)

tools = [{
    'type': 'function',
    'function': {
        'name': 'get_weather',
        'description': 'Get the current weather for a location',
        'parameters': {
            'type': 'object',
            'properties': {
                'location': {
                    'type': 'string',
                    'description': 'City name, e.g. San Francisco'
                }
            },
            'required': ['location']
        }
    }
}]

response = client.chat.completions.create(
    model='anthropic/claude-sonnet-4.6',
    messages=[
        {'role': 'user', 'content': "What's the weather in Tokyo?"}
    ],
    tools=tools
)

# Check if the model wants to call a tool
if response.choices[0].message.tool_calls:
    tool_call = response.choices[0].message.tool_calls[0]
    args = json.loads(tool_call.function.arguments)
    print(f"Model wants to call: {tool_call.function.name}")
    print(f"With arguments: {args}")
```

tools.py
```
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv('AI_GATEWAY_API_KEY'),
    base_url='https://ai-gateway.vercel.sh/v1',
)

response = client.responses.create(
    model='openai/gpt-5.4',
    input='What is the weather in Tokyo?',
    tools=[
        {
            'type': 'function',
            'name': 'get_weather',
            'description': 'Get the current weather for a location',
            'parameters': {
                'type': 'object',
                'properties': {
                    'location': {'type': 'string'},
                },
                'required': ['location'],
            },
        },
    ],
)

for item in response.output:
    if item.type == 'function_call':
        print(f'Call: {item.name}({item.arguments})')
```

tools.py
```
import os
import anthropic

client = anthropic.Anthropic(
    api_key=os.getenv('AI_GATEWAY_API_KEY'),
    base_url='https://ai-gateway.vercel.sh'
)

tools = [{
    'name': 'get_weather',
    'description': 'Get the current weather for a location',
    'input_schema': {
        'type': 'object',
        'properties': {
            'location': {
                'type': 'string',
                'description': 'City name, e.g. San Francisco'
            }
        },
        'required': ['location']
    }
}]

message = client.messages.create(
    model='anthropic/claude-sonnet-4.6',
    max_tokens=1024,
    messages=[
        {'role': 'user', 'content': "What's the weather in Tokyo?"}
    ],
    tools=tools
)

# Check if the model wants to call a tool
for block in message.content:
    if block.type == 'tool_use':
        print(f"Model wants to call: {block.name}")
        print(f"With arguments: {block.input}")
```

See [Chat Completions tool calls](https://vercel.com/docs/ai-gateway/sdks-and-apis/openai-chat-completions/tool-calls), [OpenAI Responses API tool calling](https://vercel.com/docs/ai-gateway/sdks-and-apis/responses#tool-calling), or [Anthropic Messages tool calls](https://vercel.com/docs/ai-gateway/sdks-and-apis/anthropic-messages-api/tool-calls) for more examples.
