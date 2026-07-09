##  [With Claude Code Max](https://vercel.com/docs/agent-resources/coding-agents/claude-code#with-claude-code-max)[](https://vercel.com/docs/agent-resources/coding-agents/claude-code#with-claude-code-max)
If you have a
  1. ###  [Set up environment variables](https://vercel.com/docs/agent-resources/coding-agents/claude-code#set-up-environment-variables)[](https://vercel.com/docs/agent-resources/coding-agents/claude-code#set-up-environment-variables)
Add the following to your shell configuration file (e.g., `~/.zshrc` or `~/.bashrc`):
```
export ANTHROPIC_BASE_URL="https://ai-gateway.vercel.sh"
export ANTHROPIC_CUSTOM_HEADERS="x-ai-gateway-api-key: Bearer your-ai-gateway-api-key"
```

Replace `your-ai-gateway-api-key` with your actual AI Gateway API key.
  2. ###  [Start Claude Code](https://vercel.com/docs/agent-resources/coding-agents/claude-code#start-claude-code)[](https://vercel.com/docs/agent-resources/coding-agents/claude-code#start-claude-code)
Start Claude Code:
```
claude
```

  3. ###  [Log in with your Claude subscription](https://vercel.com/docs/agent-resources/coding-agents/claude-code#log-in-with-your-claude-subscription)[](https://vercel.com/docs/agent-resources/coding-agents/claude-code#log-in-with-your-claude-subscription)
If you're not already logged in, Claude Code will prompt you to authenticate. Choose Option 1 - Claude account with subscription and log in as normal with your Anthropic account.
If you encounter issues, try logging out with `claude /logout` and logging in again.


Your requests will now be routed through Vercel AI Gateway using your Claude Code Max subscription. You'll be able to monitor usage and view traces in your Vercel dashboard while using your Anthropic subscription for model access.
* * *
[ Previous Coding Agents ](https://vercel.com/docs/agent-resources/coding-agents)[ Next Conductor ](https://vercel.com/docs/agent-resources/coding-agents/conductor)
Was this helpful?
Send
On this page
  * [Configuring Claude Code](https://vercel.com/docs/agent-resources/coding-agents/claude-code#configuring-claude-code)
  * [Configure environment variables](https://vercel.com/docs/agent-resources/coding-agents/claude-code#configure-environment-variables)
  * [Run Claude Code](https://vercel.com/docs/agent-resources/coding-agents/claude-code#run-claude-code)
  * [(Optional) macOS: Secure token storage with Keychain](https://vercel.com/docs/agent-resources/coding-agents/claude-code#optional-macos:-secure-token-storage-with-keychain)
  * [With Claude Code Max](https://vercel.com/docs/agent-resources/coding-agents/claude-code#with-claude-code-max)
  * [Set up environment variables](https://vercel.com/docs/agent-resources/coding-agents/claude-code#set-up-environment-variables)
  * [Start Claude Code](https://vercel.com/docs/agent-resources/coding-agents/claude-code#start-claude-code)
  * [Log in with your Claude subscription](https://vercel.com/docs/agent-resources/coding-agents/claude-code#log-in-with-your-claude-subscription)


Copy as MarkdownGive feedbackAsk AI about this page
[Agent Resources](https://vercel.com/docs/agent-resources)
[Coding Agents](https://vercel.com/docs/agent-resources/coding-agents)
Claude Code
