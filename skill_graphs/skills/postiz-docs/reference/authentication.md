# Authentication
Source: https://docs.postiz.com/cli/authentication

Set up OAuth2 or API key authentication for the Postiz CLI

## OAuth2 (Recommended)

Authenticate using the device flow — no client ID or secret needed:

```bash theme={null}
postiz auth:login
```

This will:

1. Display a one-time code in your terminal
2. Open your browser to authorize
3. Automatically save credentials to `~/.postiz/credentials.json`

### Auth Commands

```bash theme={null}
