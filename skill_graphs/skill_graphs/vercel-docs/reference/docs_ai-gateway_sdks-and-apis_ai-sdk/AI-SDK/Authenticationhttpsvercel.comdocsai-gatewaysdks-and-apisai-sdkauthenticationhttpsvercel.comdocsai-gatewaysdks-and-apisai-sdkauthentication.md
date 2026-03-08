##  [Authentication](https://vercel.com/docs/ai-gateway/sdks-and-apis/ai-sdk#authentication)[](https://vercel.com/docs/ai-gateway/sdks-and-apis/ai-sdk#authentication)
The AI SDK uses the `AI_GATEWAY_API_KEY` environment variable by default. Set it in your `.env.local` file:
.env.local
```
AI_GATEWAY_API_KEY=your_ai_gateway_api_key
```

On Vercel deployments, you can also authenticate with [OIDC tokens](https://vercel.com/docs/ai-gateway/authentication-and-byok/authentication#oidc-token) for keyless authentication.
See [Authentication](https://vercel.com/docs/ai-gateway/authentication-and-byok/authentication) for more details.
