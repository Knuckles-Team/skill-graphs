##  [Endpoints and authentication](https://vercel.com/docs/ai-gateway/agent-quickstart#endpoints-and-authentication)[](https://vercel.com/docs/ai-gateway/agent-quickstart#endpoints-and-authentication)
Detail | Value
---|---
[OpenResponses](https://vercel.com/docs/ai-gateway/sdks-and-apis/openresponses) endpoint | `https://ai-gateway.vercel.sh/v1/responses`
[OpenAI Responses](https://vercel.com/docs/ai-gateway/sdks-and-apis/responses) endpoint | `https://ai-gateway.vercel.sh/v1`
[Chat Completions](https://vercel.com/docs/ai-gateway/sdks-and-apis/openai-chat-completions) endpoint | `https://ai-gateway.vercel.sh/v1`
[Anthropic Messages](https://vercel.com/docs/ai-gateway/sdks-and-apis/anthropic-messages-api) endpoint | `https://ai-gateway.vercel.sh`
[Auth](https://vercel.com/docs/ai-gateway/authentication-and-byok/authentication) header | `Authorization: Bearer <AI_GATEWAY_API_KEY>`
[Model format](https://vercel.com/docs/ai-gateway/models-and-providers) |  `provider/model` (e.g., `openai/gpt-5.4`, `anthropic/claude-sonnet-4.6`)
Env variable | `AI_GATEWAY_API_KEY`
AI SDK package |  `ai` (uses AI Gateway automatically with model strings)
