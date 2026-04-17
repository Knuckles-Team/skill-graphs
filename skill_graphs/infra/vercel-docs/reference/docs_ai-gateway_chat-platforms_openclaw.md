[AI Gateway](https://vercel.com/docs/ai-gateway)
[Chat Platforms](https://vercel.com/docs/ai-gateway/chat-platforms)
OpenClaw (Clawdbot)
[AI Gateway](https://vercel.com/docs/ai-gateway)
[Chat Platforms](https://vercel.com/docs/ai-gateway/chat-platforms)
OpenClaw (Clawdbot)
# OpenClaw (Clawdbot)
Last updated February 10, 2026
##  [Configuring OpenClaw (Clawdbot)](https://vercel.com/docs/ai-gateway/chat-platforms/openclaw#configuring-openclaw-clawdbot)[](https://vercel.com/docs/ai-gateway/chat-platforms/openclaw#configuring-openclaw-clawdbot)
  1. ###  [Create an API key](https://vercel.com/docs/ai-gateway/chat-platforms/openclaw#create-an-api-key)[](https://vercel.com/docs/ai-gateway/chat-platforms/openclaw#create-an-api-key)
Go to the [AI Gateway](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fai-gateway&title=Go+to+AI+Gateway) section in the Vercel dashboard sidebar and click API keys to create a new API key.
  2. ###  [Install OpenClaw (Clawdbot)](https://vercel.com/docs/ai-gateway/chat-platforms/openclaw#install-openclaw-clawdbot)[](https://vercel.com/docs/ai-gateway/chat-platforms/openclaw#install-openclaw-clawdbot)
Choose your preferred installation method:
Quick Installnpm/pnpm
macOS/Linux:
Terminal
```
curl -fsSL https://clawd.bot/install.sh | bash
```

Windows (PowerShell):
PowerShell
```
iwr -useb https://clawd.bot/install.ps1 | iex
```

Terminal
```
npm install -g clawdbot@latest
```

Or with pnpm:
Terminal
```
pnpm add -g clawdbot@latest
```

Requires Node.js 22 or later.
  3. ###  [Run onboarding wizard](https://vercel.com/docs/ai-gateway/chat-platforms/openclaw#run-onboarding-wizard)[](https://vercel.com/docs/ai-gateway/chat-platforms/openclaw#run-onboarding-wizard)
Start the interactive setup:
Terminal
```
clawdbot onboard --install-daemon
```

  4. ###  [Configure AI Gateway](https://vercel.com/docs/ai-gateway/chat-platforms/openclaw#configure-ai-gateway)[](https://vercel.com/docs/ai-gateway/chat-platforms/openclaw#configure-ai-gateway)
During the onboarding wizard:
    1. Model/Auth Provider: Select Vercel AI Gateway
    2. Authentication Method: Choose Vercel AI Gateway API key
    3. Enter API key: Paste your AI Gateway API key
    4. Select Model: Choose from available models
    5. Additional Configuration: Complete remaining setup options (communication channels, daemon installation, etc.)
Models follow the `creator/model-name` format. Check the [models catalog](https://vercel.com/ai-gateway/models) for available options.
  5. ###  [Verify installation](https://vercel.com/docs/ai-gateway/chat-platforms/openclaw#verify-installation)[](https://vercel.com/docs/ai-gateway/chat-platforms/openclaw#verify-installation)
Check that OpenClaw (Clawdbot) is configured correctly:
Terminal
```
clawdbot health
clawdbot status
```

Your requests will now be routed through AI Gateway. You can verify this by checking your [AI Gateway Overview](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fai-gateway&title=Go+to+AI+Gateway) in the Vercel dashboard.
  6. ###  [(Optional) Monitor usage and spend](https://vercel.com/docs/ai-gateway/chat-platforms/openclaw#optional-monitor-usage-and-spend)[](https://vercel.com/docs/ai-gateway/chat-platforms/openclaw#optional-monitor-usage-and-spend)
View your usage, spend, and request activity in the [AI Gateway](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fai-gateway&title=Go+to+AI+Gateway) section in the Vercel dashboard sidebar. See the [observability documentation](https://vercel.com/docs/ai-gateway/capabilities/observability) for more details.


* * *
[ Previous LibreChat ](https://vercel.com/docs/ai-gateway/chat-platforms/librechat)[ Next Chatbox ](https://vercel.com/docs/ai-gateway/chat-platforms/chatbox)
Was this helpful?
Send
