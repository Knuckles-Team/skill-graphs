# Remove stored credentials
postiz auth:logout
```

## API Key

Alternatively, set your Postiz API key as an environment variable:

```bash theme={null}
export POSTIZ_API_KEY=your_api_key_here
```

You can get your API key from the Postiz Settings page.

<Note>
  OAuth2 credentials take priority over the API key when both are present.
</Note>

## Environment Variables

| Variable             | Required | Default                       | Description                                          |
| -------------------- | -------- | ----------------------------- | ---------------------------------------------------- |
| `POSTIZ_API_KEY`     | No\*     | -                             | Your Postiz API key                                  |
| `POSTIZ_API_URL`     | No       | `https://api.postiz.com`      | Custom API endpoint (for self-hosted Postiz)         |
| `POSTIZ_AUTH_SERVER` | No       | `https://cli-auth.postiz.com` | Custom auth server URL (for self-hosted auth server) |

\*Either OAuth2 (via `postiz auth:login`) or `POSTIZ_API_KEY` is required.

## Self-Hosting the Auth Server

By default, `postiz auth:login` uses the hosted auth server at `cli-auth.postiz.com`. If you want to self-host the OAuth2 device flow server, you can run your own instance.

The auth server mediates the OAuth2 device flow so CLI users can authenticate without needing client credentials.

### Prerequisites

* Node.js >= 18
* PostgreSQL

### How It Works

```
CLI                        Auth Server                    Postiz
 |                              |                           |
 |-- POST /device/code ------->|                           |
 |<-- device_code + user_code --|                           |
 |                              |                           |
 |  User opens browser ------->|                           |
 |  Enters code                |                           |
 |                              |-- redirect to OAuth ----->|
 |                              |<-- callback with code ----|
 |                              |-- exchange for token ---->|
 |                              |<-- access_token ----------|
 |                              |  (stored in Postgres)     |
 |                              |                           |
 |  POST /device/token (poll) >|                           |
 |<-- access_token ------------|                           |
```

### 1. Clone the Repository

The auth server lives in the [postiz-agent](https://github.com/gitroomhq/postiz-agent) repository:

```bash theme={null}
git clone https://github.com/gitroomhq/postiz-agent.git
cd postiz-agent/server
```

### 2. Create an OAuth App in Postiz

Go to **Postiz Settings > Developer > OAuth Apps** and create a new app. Set the callback URL to:

```
https://your-server-domain.com/device/callback
```

### 3. Set Up Postgres

Create a database. The server auto-creates the `device_requests` table on startup.

### 4. Configure Environment

```bash theme={null}
export DATABASE_URL="postgresql://user:password@localhost:5432/postiz_auth"
export POSTIZ_OAUTH_CLIENT_ID="pca_xxx"
export POSTIZ_OAUTH_CLIENT_SECRET="pcs_xxx"
export SERVER_URL="https://your-server-domain.com"
```

| Variable                     | Required | Default                       | Description                             |
| ---------------------------- | -------- | ----------------------------- | --------------------------------------- |
| `DATABASE_URL`               | Yes      | -                             | Postgres connection string              |
| `POSTIZ_OAUTH_CLIENT_ID`     | Yes      | -                             | OAuth app client ID from Postiz         |
| `POSTIZ_OAUTH_CLIENT_SECRET` | Yes      | -                             | OAuth app client secret from Postiz     |
| `PORT`                       | No       | `3111`                        | Server port                             |
| `SERVER_URL`                 | No       | `http://localhost:{PORT}`     | Public URL of this server               |
| `POSTIZ_FRONTEND_URL`        | No       | `https://platform.postiz.com` | Postiz frontend URL for OAuth redirects |
| `POSTIZ_API_URL`             | No       | `https://api.postiz.com`      | Postiz API URL for token exchange       |

### 5. Run the Server

```bash theme={null}
pnpm install
