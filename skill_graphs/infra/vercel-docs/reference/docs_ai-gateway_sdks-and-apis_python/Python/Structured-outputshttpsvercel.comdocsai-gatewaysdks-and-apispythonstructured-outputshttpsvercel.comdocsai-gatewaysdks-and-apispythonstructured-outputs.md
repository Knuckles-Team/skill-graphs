##  [Structured outputs](https://vercel.com/docs/ai-gateway/sdks-and-apis/python#structured-outputs)[](https://vercel.com/docs/ai-gateway/sdks-and-apis/python#structured-outputs)
Generate responses that conform to a JSON schema for reliable parsing.
structured.py
```
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv('AI_GATEWAY_API_KEY'),
    base_url='https://ai-gateway.vercel.sh/v1'
)

response = client.chat.completions.create(
    model='anthropic/claude-sonnet-4.6',
    messages=[
        {'role': 'user', 'content': 'Extract: John is 30 years old and lives in NYC'}
    ],
    response_format={
        'type': 'json_schema',
        'json_schema': {
            'name': 'person',
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string'},
                    'age': {'type': 'integer'},
                    'city': {'type': 'string'}
                },
                'required': ['name', 'age', 'city']
            }
        }
    }
)

import json
data = json.loads(response.choices[0].message.content)
print(data)  # {'name': 'John', 'age': 30, 'city': 'NYC'}
```

See [structured outputs](https://vercel.com/docs/ai-gateway/sdks-and-apis/openai-chat-completions/structured-outputs) for more details.
