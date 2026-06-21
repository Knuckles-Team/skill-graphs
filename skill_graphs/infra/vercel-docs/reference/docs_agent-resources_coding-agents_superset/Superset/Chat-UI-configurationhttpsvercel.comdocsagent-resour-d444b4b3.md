##  [Chat UI configuration](https://vercel.com/docs/agent-resources/coding-agents/claude-code#chat-ui-configuration)[](https://vercel.com/docs/agent-resources/coding-agents/claude-code#chat-ui-configuration)
For the Superset Chat UI, configure AI Gateway through the settings panel:
  1. ###  [Download Superset](https://vercel.com/docs/agent-resources/coding-agents/claude-code#download-superset)[](https://vercel.com/docs/agent-resources/coding-agents/claude-code#download-superset)
Download and install Superset by following the
  2. ###  [Open Superset](https://vercel.com/docs/agent-resources/coding-agents/claude-code#open-superset)[](https://vercel.com/docs/agent-resources/coding-agents/claude-code#open-superset)
Open the Superset app.
  3. ###  [Open the model picker](https://vercel.com/docs/agent-resources/coding-agents/claude-code#open-the-model-picker)[](https://vercel.com/docs/agent-resources/coding-agents/claude-code#open-the-model-picker)
Open the model picker at the bottom of the chat interface.
  4. ###  [Open provider settings](https://vercel.com/docs/agent-resources/coding-agents/claude-code#open-provider-settings)[](https://vercel.com/docs/agent-resources/coding-agents/claude-code#open-provider-settings)
Click the key icon next to Anthropic, then select Use API key.
  5. ###  [Create an API key](https://vercel.com/docs/agent-resources/coding-agents/claude-code#create-an-api-key)[](https://vercel.com/docs/agent-resources/coding-agents/claude-code#create-an-api-key)
Go to the [AI Gateway](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fai-gateway&title=Go+to+AI+Gateway) section in the Vercel dashboard sidebar and click API keys to create a new API key.
  6. ###  [Add environment variables](https://vercel.com/docs/agent-resources/coding-agents/claude-code#add-environment-variables)[](https://vercel.com/docs/agent-resources/coding-agents/claude-code#add-environment-variables)
Enter the following environment variables (one per line, `VAR_NAME=value` format):
```
ANTHROPIC_BASE_URL=https://ai-gateway.vercel.sh
ANTHROPIC_AUTH_TOKEN=your-ai-gateway-api-key
ANTHROPIC_API_KEY=
```

  7. ###  [Save settings](https://vercel.com/docs/agent-resources/coding-agents/claude-code#save-settings)[](https://vercel.com/docs/agent-resources/coding-agents/claude-code#save-settings)
Click Save settings to apply your configuration.
Your Superset requests now route through Vercel AI Gateway.
