##  [Configuring Claude Code](https://vercel.com/docs/agent-resources/coding-agents/claude-code#configuring-claude-code)[](https://vercel.com/docs/agent-resources/coding-agents/claude-code#configuring-claude-code)
  * Monitor traffic and token usage in your AI Gateway Overview
  * View detailed traces in Vercel Observability under AI


  1. ###  [Configure environment variables](https://vercel.com/docs/agent-resources/coding-agents/claude-code#configure-environment-variables)[](https://vercel.com/docs/agent-resources/coding-agents/claude-code#configure-environment-variables)
First, log out if you're already logged in:
```
claude /logout
```

Next, ensure you have your AI Gateway API key handy, and configure Claude Code to use the AI Gateway by adding this to your shell configuration file, for example in `~/.zshrc` or `~/.bashrc`:
```
export ANTHROPIC_BASE_URL="https://ai-gateway.vercel.sh"
export ANTHROPIC_AUTH_TOKEN="your-ai-gateway-api-key"
export ANTHROPIC_API_KEY=""
```

Setting `ANTHROPIC_API_KEY` to an empty string is important. Claude Code checks this variable first, and if it's set to a non-empty value, it will use that instead of `ANTHROPIC_AUTH_TOKEN`.
  2. ###  [Run Claude Code](https://vercel.com/docs/agent-resources/coding-agents/claude-code#run-claude-code)[](https://vercel.com/docs/agent-resources/coding-agents/claude-code#run-claude-code)
Run `claude` to start Claude Code with AI Gateway:
```
claude
```

Your requests will now be routed through Vercel AI Gateway.
  3. ###  [(Optional) macOS: Secure token storage with Keychain](https://vercel.com/docs/agent-resources/coding-agents/claude-code#optional-macos:-secure-token-storage-with-keychain)[](https://vercel.com/docs/agent-resources/coding-agents/claude-code#optional-macos:-secure-token-storage-with-keychain)
If you're on a Mac and would like to manage your API key through a keychain for improved security, set your API key in the keystore with:
```
security add-generic-password -a "$USER" -s "ANTHROPIC_AUTH_TOKEN" \
  -w "your-ai-gateway-api-key"
```

and edit the `ANTHROPIC_AUTH_TOKEN` line above to:
```
export ANTHROPIC_AUTH_TOKEN=$(
  security find-generic-password -a "$USER" -s "ANTHROPIC_AUTH_TOKEN" -w
)
```

If you need to update the API key value later, you can do it with:
```
security add-generic-password -U -a "$USER" -s "ANTHROPIC_AUTH_TOKEN" \
  -w "new-ai-gateway-api-key"
```
