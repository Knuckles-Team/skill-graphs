# Remove stored credentials
postiz auth:logout
```

### Option 2: API Key

Set your Postiz API key as an environment variable. You can get your API key from the Postiz Settings page.

```bash theme={null}
export POSTIZ_API_KEY=your_api_key_here
```

<Tip>
  Add this to your shell profile (`~/.bashrc`, `~/.zshrc`, etc.) so it persists across sessions.
</Tip>

<Note>
  OAuth2 credentials take priority over the API key when both are present.
</Note>

### Custom API URL (self-hosted)

If you're running a self-hosted Postiz instance, point the CLI to your server:

```bash theme={null}
export POSTIZ_API_URL=https://your-postiz-server.com
```

### Self-Hosting the Auth Server

By default, `postiz auth:login` uses the hosted auth server at `cli-auth.postiz.com`. If you want to self-host the OAuth2 device flow server, see the [Authentication](/cli/authentication) page for the full setup guide.

## Quick Start

```bash theme={null}
