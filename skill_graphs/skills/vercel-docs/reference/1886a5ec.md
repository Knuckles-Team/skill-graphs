##  [Supported agents](https://vercel.com/docs/agent-resources/coding-agents#supported-agents)[](https://vercel.com/docs/agent-resources/coding-agents#supported-agents)
###  [Claude Code](https://vercel.com/docs/agent-resources/coding-agents#claude-code)[](https://vercel.com/docs/agent-resources/coding-agents#claude-code)
```
export ANTHROPIC_BASE_URL="https://ai-gateway.vercel.sh"
export ANTHROPIC_API_KEY="your-ai-gateway-api-key"
```

Once configured, Claude Code works exactly as before, but requests route through the gateway.
See the [Claude Code documentation](https://vercel.com/docs/agent-resources/coding-agents/claude-code) for advanced configuration.
###  [OpenCode](https://vercel.com/docs/agent-resources/coding-agents#opencode)[](https://vercel.com/docs/agent-resources/coding-agents#opencode)
```
opencode
> /connect
# Select "Vercel AI Gateway" and enter your API key
```

OpenCode automatically discovers available models and lets you switch between them on the fly.
See the [OpenCode documentation](https://vercel.com/docs/agent-resources/coding-agents/opencode) for more features.
###  [Blackbox AI](https://vercel.com/docs/agent-resources/coding-agents#blackbox-ai)[](https://vercel.com/docs/agent-resources/coding-agents#blackbox-ai)
```
blackbox configure
# Select "Configure Providers", choose "Vercel AI Gateway", and enter your API key
```

See the [Blackbox AI documentation](https://vercel.com/docs/agent-resources/coding-agents/blackbox) for installation and setup.
###  [Cline](https://vercel.com/docs/agent-resources/coding-agents#cline)[](https://vercel.com/docs/agent-resources/coding-agents#cline)
  1. Open the Cline settings panel
  2. Select Vercel AI Gateway as your API Provider
  3. Paste your API key
  4. Choose a model from the auto-populated catalog


Cline tracks detailed metrics including reasoning tokens, cache performance, and latency.
See the [Cline documentation](https://vercel.com/docs/agent-resources/coding-agents/cline) for troubleshooting tips.
###  [Roo Code](https://vercel.com/docs/agent-resources/coding-agents#roo-code)[](https://vercel.com/docs/agent-resources/coding-agents#roo-code)
  1. Click the gear icon in the Roo Code panel
  2. Select Vercel AI Gateway as your provider
  3. Enter your API key
  4. Choose from hundreds of available models


Roo Code includes prompt caching support for Claude and GPT models to reduce costs.
See the [Roo Code documentation](https://vercel.com/docs/agent-resources/coding-agents/roo-code) for setup details.
###  [Conductor](https://vercel.com/docs/agent-resources/coding-agents#conductor)[](https://vercel.com/docs/agent-resources/coding-agents#conductor)
  1. Go to Settings -> Env
  2. Add the environment variables under Claude Code
  3. Set `ANTHROPIC_BASE_URL` to `https://ai-gateway.vercel.sh`


Conductor lets you review and merge changes from multiple agents in one place.
See the [Conductor documentation](https://vercel.com/docs/agent-resources/coding-agents/conductor) for setup details.
###  [Crush](https://vercel.com/docs/agent-resources/coding-agents#crush)[](https://vercel.com/docs/agent-resources/coding-agents#crush)
```
crush
# Select "Vercel AI Gateway", choose a model, and enter your API Key
```

See the [Crush documentation](https://vercel.com/docs/agent-resources/coding-agents/crush) for installation options.
###  [Superset](https://vercel.com/docs/agent-resources/coding-agents#superset)[](https://vercel.com/docs/agent-resources/coding-agents#superset)
```
export ANTHROPIC_BASE_URL="https://ai-gateway.vercel.sh"
export ANTHROPIC_AUTH_TOKEN="your-ai-gateway-api-key"
export ANTHROPIC_API_KEY=""
```

Superset also includes a Chat UI with built-in provider configuration.
See the [Superset documentation](https://vercel.com/docs/agent-resources/coding-agents/superset) for Chat UI setup.
