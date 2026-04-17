##  [Scaffold a new project](https://vercel.com/docs/ai-gateway/agent-quickstart#scaffold-a-new-project)[](https://vercel.com/docs/ai-gateway/agent-quickstart#scaffold-a-new-project)
To create a full project that uses AI Gateway with the AI SDK, prompt your agent:
Prompt
```
Create a TypeScript project that uses the AI SDK to stream a response
from Vercel AI Gateway.

- Initialize with pnpm and install the `ai` package, dotenv,
  @types/node, tsx, and typescript
- Store the API key in .env.local as AI_GATEWAY_API_KEY
- Use streamText with the model "openai/gpt-5.4"
- Stream the output to stdout, then log token usage and finish reason
- Run it with tsx to verify it works
```

Your agent will create the project, install dependencies, write the code, and run it.
