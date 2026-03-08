##  [Verify AI Gateway works](https://vercel.com/docs/ai-gateway/agent-quickstart#verify-ai-gateway-works)[](https://vercel.com/docs/ai-gateway/agent-quickstart#verify-ai-gateway-works)
The fastest way to confirm your API key is working is to have your agent make a single request. Copy this prompt into your agent:
Prompt
```
Make a request to the Vercel AI Gateway to verify my API key works.

- Use cURL to POST to https://ai-gateway.vercel.sh/v1/responses
- Authenticate with a Bearer token using my AI_GATEWAY_API_KEY env var
- Use the model "anthropic/claude-sonnet-4.6"
- Send the prompt: "Invent a new holiday and describe its traditions."
- Run it and show me the response.
```

Your agent will run something like:
Terminal
```
curl -X POST "https://ai-gateway.vercel.sh/v1/responses" \
  -H "Authorization: Bearer $AI_GATEWAY_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "anthropic/claude-sonnet-4.6",
    "input": [
      {
        "type": "message",
        "role": "user",
        "content": "Invent a new holiday and describe its traditions."
      }
    ]
  }'
```

If you see a model response, your API key and AI Gateway are working.
