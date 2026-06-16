# WebSockets, HMR, and Dev Tunnels
Source: https://docs.postiz.com/reverse-proxies/websockets-and-dev

Running Postiz behind ngrok or a reverse proxy with WebSocket support

## Production reverse proxy

How you reverse-proxy depends on how you're running Postiz:

* **Official Docker image** (`ghcr.io/gitroomhq/postiz-app`): frontend
  and backend are bundled inside one container and exposed on a single
  port (`5000` internally; the official compose maps it to host `4007`).
  Your reverse proxy only needs to forward one upstream. Most users on
  this image don't need anything beyond standard HTTPS termination.
* **Source / multi-container deployments** (`pnpm dev`, `pnpm start`,
  or splitting frontend and backend into separate containers): frontend
  runs on `4200`, backend on `3000`, and you need to route the paths
  below correctly.

For the split setup, forward:

| Path                             | Upstream         | Notes                                                                |
| -------------------------------- | ---------------- | -------------------------------------------------------------------- |
| `/` (everything not below)       | Frontend `:4200` | Pass `Upgrade` and `Connection` headers for Next.js HMR in dev.      |
| `/api/*`                         | Backend `:3000`  | Standard HTTP.                                                       |
| `/public/*`                      | Backend `:3000`  | Public API.                                                          |
| `/auth/*`                        | Backend `:3000`  | Sign-in flow.                                                        |
| `/integrations/*`                | Backend `:3000`  | OAuth callbacks.                                                     |
| `/mcp/*`, `/sse/*`, `/message/*` | Backend `:3000`  | MCP transport — must support streaming HTTP.                         |
| `/webhooks/*`                    | Backend `:3000`  | Inbound webhook callbacks from providers (Stripe, social platforms). |

For configured examples, see [Caddy](/reverse-proxies/caddy),
[Nginx](/reverse-proxies/nginx), and [Traefik](/reverse-proxies/traefik).

## Dev behind ngrok / Cloudflared

Running `next dev` behind an HTTPS tunnel needs three things:

**1. Bind to all interfaces**

```bash theme={null}
pnpm dev # binds 0.0.0.0:4200 by default in this repo
