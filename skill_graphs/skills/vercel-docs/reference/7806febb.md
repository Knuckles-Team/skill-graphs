##  [Configuring Crush](https://vercel.com/docs/agent-resources/vercel-mcp#configuring-crush)[](https://vercel.com/docs/agent-resources/vercel-mcp#configuring-crush)
  1. ###  [Create an API Key](https://vercel.com/docs/agent-resources/vercel-mcp#create-an-api-key)[](https://vercel.com/docs/agent-resources/vercel-mcp#create-an-api-key)
Go to the [AI Gateway](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fai-gateway&title=Go+to+AI+Gateway) section in the Vercel dashboard sidebar and click API Keys to create a new API Key.
  2. ###  [Install Crush](https://vercel.com/docs/agent-resources/vercel-mcp#install-crush)[](https://vercel.com/docs/agent-resources/vercel-mcp#install-crush)
Choose your preferred installation method:
HomebrewnpmGo
Terminal
```
brew install charmbracelet/tap/crush
```

Terminal
```
npm install -g @charmland/crush
```

Terminal
```
go install github.com/charmbracelet/crush@latest
```

See the
  3. ###  [Configure AI Gateway](https://vercel.com/docs/agent-resources/vercel-mcp#configure-ai-gateway)[](https://vercel.com/docs/agent-resources/vercel-mcp#configure-ai-gateway)
Start Crush:
Terminal
```
crush
```

When prompted:
    1. Select Provider: Choose Vercel AI Gateway
    2. Select Model: Pick from AI Gateway's model library
    3. Enter API Key: Paste your AI Gateway API Key when prompted
Crush saves your API Key to `~/.local/share/crush/crush.json`, so you only need to enter it once.
Your requests will now be routed through AI Gateway. You can verify this by checking your [AI Gateway Overview](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fai-gateway&title=Go+to+AI+Gateway) in the Vercel dashboard.
  4. ###  [(Optional) Monitor usage and spend](https://vercel.com/docs/agent-resources/vercel-mcp#optional-monitor-usage-and-spend)[](https://vercel.com/docs/agent-resources/vercel-mcp#optional-monitor-usage-and-spend)
View your usage, spend, and request activity in the [AI Gateway](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fai-gateway&title=Go+to+AI+Gateway) section in the Vercel dashboard sidebar. See the [observability documentation](https://vercel.com/docs/ai-gateway/capabilities/observability) for more details.


* * *
[ Previous Markdown Access ](https://vercel.com/docs/agent-resources/markdown-access)[ Next Tools ](https://vercel.com/docs/agent-resources/vercel-mcp/tools)
Was this helpful?
Send
On this page
  * [Configuring Crush](https://vercel.com/docs/agent-resources/vercel-mcp#configuring-crush)
  * [Create an API Key](https://vercel.com/docs/agent-resources/vercel-mcp#create-an-api-key)
  * [Install Crush](https://vercel.com/docs/agent-resources/vercel-mcp#install-crush)
  * [Configure AI Gateway](https://vercel.com/docs/agent-resources/vercel-mcp#configure-ai-gateway)
  * [(Optional) Monitor usage and spend](https://vercel.com/docs/agent-resources/vercel-mcp#optional-monitor-usage-and-spend)


Copy as MarkdownGive feedbackAsk AI about this page
