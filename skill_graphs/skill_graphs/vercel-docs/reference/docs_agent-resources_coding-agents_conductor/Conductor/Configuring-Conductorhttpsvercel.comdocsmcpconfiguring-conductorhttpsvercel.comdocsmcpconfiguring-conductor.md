##  [Configuring Conductor](https://vercel.com/docs/mcp#configuring-conductor)[](https://vercel.com/docs/mcp#configuring-conductor)
Conductor runs using your local Claude Code login. You can check your auth status by running `claude /login` in your terminal.
Conductor also supports running Claude Code on OpenRouter, AWS Bedrock, Google Vertex AI, Vercel AI Gateway, or any Anthropic API compatible provider. You can configure it to use Vercel AI Gateway, enabling you to:
  * Monitor traffic and token usage in your AI Gateway Overview
  * View detailed traces in Vercel Observability under AI


  1. ###  [Create an API key](https://vercel.com/docs/mcp#create-an-api-key)[](https://vercel.com/docs/mcp#create-an-api-key)
Go to the [AI Gateway](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fai-gateway&title=Go+to+AI+Gateway) section in the Vercel dashboard sidebar and click API keys to create a new API key.
  2. ###  [Configure environment variables](https://vercel.com/docs/mcp#configure-environment-variables)[](https://vercel.com/docs/mcp#configure-environment-variables)
In Conductor, go to Settings -> Env to set environment variables. Add the following under Claude Code:
```
ANTHROPIC_BASE_URL="https://ai-gateway.vercel.sh"
ANTHROPIC_AUTH_TOKEN="your-vercel-ai-gateway-api-key"
ANTHROPIC_API_KEY=""
```

Setting `ANTHROPIC_API_KEY` to an empty string is required. This prevents Claude Code from attempting to authenticate with Anthropic directly.
Check out the
  3. ###  [Start using Conductor](https://vercel.com/docs/mcp#start-using-conductor)[](https://vercel.com/docs/mcp#start-using-conductor)
Your requests will now be routed through Vercel AI Gateway. You can verify this by checking your [AI Gateway Overview](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fai-gateway&title=Go+to+AI+Gateway) in the Vercel dashboard.


* * *
[ Previous AI Gateway ](https://vercel.com/docs/ai-gateway)[ Next Deploy MCP servers ](https://vercel.com/docs/mcp/deploy-mcp-servers-to-vercel)
Was this helpful?
Send
On this page
  * [Configuring Conductor](https://vercel.com/docs/mcp#configuring-conductor)
  * [Create an API key](https://vercel.com/docs/mcp#create-an-api-key)
  * [Configure environment variables](https://vercel.com/docs/mcp#configure-environment-variables)
  * [Start using Conductor](https://vercel.com/docs/mcp#start-using-conductor)


Copy as MarkdownGive feedbackAsk AI about this page
