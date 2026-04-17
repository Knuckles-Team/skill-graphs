##  [Terminal configuration](https://vercel.com/docs/agent-resources/coding-agents/claude-code#terminal-configuration)[](https://vercel.com/docs/agent-resources/coding-agents/claude-code#terminal-configuration)
  1. ###  [Download Superset](https://vercel.com/docs/agent-resources/coding-agents/claude-code#download-superset)[](https://vercel.com/docs/agent-resources/coding-agents/claude-code#download-superset)
Download and install Superset by following the
  2. ###  [Create an API key](https://vercel.com/docs/agent-resources/coding-agents/claude-code#create-an-api-key)[](https://vercel.com/docs/agent-resources/coding-agents/claude-code#create-an-api-key)
Go to the [AI Gateway](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fai-gateway&title=Go+to+AI+Gateway) section in the Vercel dashboard sidebar and click API keys to create a new API key.
  3. ###  [Configure environment variables](https://vercel.com/docs/agent-resources/coding-agents/claude-code#configure-environment-variables)[](https://vercel.com/docs/agent-resources/coding-agents/claude-code#configure-environment-variables)
Terminal-based agents in Superset work automatically when you configure your environment. Add the following to your shell configuration file, for example in `~/.zshrc` or `~/.bashrc`:
```
export ANTHROPIC_BASE_URL="https://ai-gateway.vercel.sh"
export ANTHROPIC_AUTH_TOKEN="your-ai-gateway-api-key"
export ANTHROPIC_API_KEY=""
```

Setting `ANTHROPIC_API_KEY` to an empty string is important. This prevents direct Anthropic authentication and ensures requests route through AI Gateway.
  4. ###  [Restart your terminal session](https://vercel.com/docs/agent-resources/coding-agents/claude-code#restart-your-terminal-session)[](https://vercel.com/docs/agent-resources/coding-agents/claude-code#restart-your-terminal-session)
Open a new terminal window or run `source ~/.zshrc` or `source ~/.bashrc` to apply the changes.
Your terminal-based Superset agents now route requests through Vercel AI Gateway.
