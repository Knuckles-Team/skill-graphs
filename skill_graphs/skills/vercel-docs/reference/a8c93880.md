##  [Authentication methods](https://vercel.com/docs/ai-gateway/authentication-and-byok#authentication-methods)[](https://vercel.com/docs/ai-gateway/authentication-and-byok#authentication-methods)
###  [API keys](https://vercel.com/docs/ai-gateway/authentication-and-byok#api-keys)[](https://vercel.com/docs/ai-gateway/authentication-and-byok#api-keys)
API keys work anywhere, whether it's local development, external servers, or CI pipelines. Create them in the [AI Gateway page](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fai-gateway&title=AI+Gateway) and they never expire unless you revoke them.
###  [OIDC tokens](https://vercel.com/docs/ai-gateway/authentication-and-byok#oidc-tokens)[](https://vercel.com/docs/ai-gateway/authentication-and-byok#oidc-tokens)
For applications deployed on Vercel, OIDC tokens are automatically available as `VERCEL_OIDC_TOKEN`. No secrets to manage, no keys to rotate. It just works.
```
// Automatically uses OIDC on Vercel, falls back to API key locally
const apiKey = process.env.AI_GATEWAY_API_KEY || process.env.VERCEL_OIDC_TOKEN;
```
