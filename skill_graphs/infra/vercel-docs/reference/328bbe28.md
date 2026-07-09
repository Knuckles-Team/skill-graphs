##  [Getting Your OpenAI API Key](https://vercel.com/docs/agent-resources/integrations-for-models/adding-a-model#getting-your-openai-api-key)[](https://vercel.com/docs/agent-resources/integrations-for-models/adding-a-model#getting-your-openai-api-key)
Before you begin, ensure you have an
  1. ###  [Navigate to API Keys](https://vercel.com/docs/agent-resources/integrations-for-models/adding-a-model#navigate-to-api-keys)[](https://vercel.com/docs/agent-resources/integrations-for-models/adding-a-model#navigate-to-api-keys)
Log into your
  2. ###  [Generate API Key](https://vercel.com/docs/agent-resources/integrations-for-models/adding-a-model#generate-api-key)[](https://vercel.com/docs/agent-resources/integrations-for-models/adding-a-model#generate-api-key)
Click on Create new secret key. Copy the generated API key securely.
![](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fopenai%2Fenv-vars.png&w=3840&q=75)
Always keep your API keys confidential. Do not expose them in client-side code. Use [Vercel Environment Variables](https://vercel.com/docs/environment-variables) for safe storage and do not commit these values to git.
  3. ###  [Set Environment Variable](https://vercel.com/docs/agent-resources/integrations-for-models/adding-a-model#set-environment-variable)[](https://vercel.com/docs/agent-resources/integrations-for-models/adding-a-model#set-environment-variable)
Finally, add the `OPENAI_API_KEY` environment variable in your project:
.env.local
```
OPENAI_API_KEY='sk-...3Yu5'
```
