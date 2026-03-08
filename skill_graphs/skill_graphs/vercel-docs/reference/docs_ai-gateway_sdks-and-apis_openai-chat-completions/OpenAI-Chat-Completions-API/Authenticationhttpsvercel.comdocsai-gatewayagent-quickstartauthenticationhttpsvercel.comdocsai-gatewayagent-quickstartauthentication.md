##  [Authentication](https://vercel.com/docs/ai-gateway/agent-quickstart#authentication)[](https://vercel.com/docs/ai-gateway/agent-quickstart#authentication)
The Chat Completions API supports the same authentication methods as the main AI Gateway:
  * API key: Use your AI Gateway API key with the `Authorization: Bearer <token>` header
  * OIDC token: Use your Vercel OIDC token with the `Authorization: Bearer <token>` header


You only need to use one of these forms of authentication. If an API key is specified it will take precedence over any OIDC token, even if the API key is invalid.
