# Production
pnpm build
pnpm start:prod
```

### 6. Point the CLI to Your Server

```bash theme={null}
export POSTIZ_AUTH_SERVER="https://your-server-domain.com"
postiz auth:login
```

### Server Endpoints

| Method | Path               | Description                                                                          |
| ------ | ------------------ | ------------------------------------------------------------------------------------ |
| `POST` | `/device/code`     | Start a new device flow. Returns `device_code`, `user_code`, and `verification_uri`. |
| `GET`  | `/device/verify`   | Browser page where the user enters their code.                                       |
| `POST` | `/device/verify`   | Validates user code and redirects to Postiz OAuth.                                   |
| `GET`  | `/device/callback` | Postiz redirects here after authorization. Exchanges auth code for token.            |
| `POST` | `/device/token`    | CLI polls this with `device_code`. Returns token when auth completes.                |
| `GET`  | `/health`          | Health check.                                                                        |

### Deployment

Any platform that runs Node.js and can connect to Postgres works — Railway, Fly.io, Render, VPS, etc.

The server is stateless beyond Postgres, so it scales horizontally. Run multiple instances behind a load balancer if needed.
