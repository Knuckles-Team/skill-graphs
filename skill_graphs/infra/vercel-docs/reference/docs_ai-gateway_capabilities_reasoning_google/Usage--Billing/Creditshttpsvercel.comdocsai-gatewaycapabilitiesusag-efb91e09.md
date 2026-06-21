##  [Credits](https://vercel.com/docs/ai-gateway/capabilities/usage#credits)[](https://vercel.com/docs/ai-gateway/capabilities/usage#credits)
Check your AI Gateway credit balance and usage information.
Endpoint
`GET /credits `
Example request
TypeScriptPython
credits.ts
```
const apiKey = process.env.AI_GATEWAY_API_KEY || process.env.VERCEL_OIDC_TOKEN;

const response = await fetch('https://ai-gateway.vercel.sh/v1/credits', {
  method: 'GET',
  headers: {
    Authorization: `Bearer ${apiKey}`,
    'Content-Type': 'application/json',
  },
});

const credits = await response.json();
console.log(credits);
```

credits.py
```
import os
import requests

api_key = os.getenv("AI_GATEWAY_API_KEY") or os.getenv("VERCEL_OIDC_TOKEN")

response = requests.get(
    "https://ai-gateway.vercel.sh/v1/credits",
    headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    },
)

credits = response.json()
print(credits)
```

Sample response
```
{
  "balance": "95.50",
  "total_used": "4.50"
}
```

Response fields
  * `balance`: The remaining credit balance
  * `total_used`: The total amount of credits used
