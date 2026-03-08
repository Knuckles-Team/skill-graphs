##  [Integrate into an existing app](https://vercel.com/docs/ai-gateway/agent-quickstart#integrate-into-an-existing-app)[](https://vercel.com/docs/ai-gateway/agent-quickstart#integrate-into-an-existing-app)
If you already have a project, prompt your agent to add AI Gateway:
Prompt
```
Add AI Gateway to this project using the AI SDK.

- Install the `ai` package if not already installed
- Use my AI_GATEWAY_API_KEY from .env.local
- Models use the format "provider/model", for example "openai/gpt-5.4"
```

Your agent will determine where and how to integrate based on your project's structure and framework.
See [available models](https://vercel.com/docs/ai-gateway/models-and-providers) for the full list of supported model strings.
