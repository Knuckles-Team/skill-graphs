##  [Authentication](https://vercel.com/docs/ai-gateway/sdks-and-apis/python#authentication)[](https://vercel.com/docs/ai-gateway/sdks-and-apis/python#authentication)
All SDKs support the same authentication methods. Use an [API key](https://vercel.com/docs/ai-gateway/authentication-and-byok/authentication#api-key) for local development or [OIDC tokens](https://vercel.com/docs/ai-gateway/authentication-and-byok/authentication#oidc-token) for Vercel deployments.
auth.py
```
import os

# Option 1: API key (recommended for local development)
api_key = os.getenv('AI_GATEWAY_API_KEY')

# Option 2: OIDC token (automatic on Vercel deployments)
api_key = os.getenv('VERCEL_OIDC_TOKEN')

# Fallback pattern for code that runs both locally and on Vercel
api_key = os.getenv('AI_GATEWAY_API_KEY') or os.getenv('VERCEL_OIDC_TOKEN')
```
