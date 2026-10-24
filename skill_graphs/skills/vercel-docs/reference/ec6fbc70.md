##  [Authentication](https://vercel.com/docs/vercel-sandbox/sdk-reference#authentication)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#authentication)
Vercel Sandbox supports two authentication methods:
  * [Vercel OIDC tokens](https://vercel.com/docs/vercel-sandbox/concepts/authentication#vercel-oidc-token-recommended) (recommended): Vercel generates the OIDC token that it associates with your Vercel project. For local development, run `vercel link` and `vercel env pull` to get a development token. In production on Vercel, authentication is automatic.
  * [Access tokens](https://vercel.com/docs/vercel-sandbox/concepts/authentication#access-tokens): Use access tokens when `VERCEL_OIDC_TOKEN` is unavailable, such as in external CI/CD systems or non-Vercel environments.


To learn more on each method, see [Authentication](https://vercel.com/docs/vercel-sandbox/concepts/authentication) for complete setup instructions.
