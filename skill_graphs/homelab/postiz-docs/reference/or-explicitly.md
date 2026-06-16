# or explicitly
pnpm --filter @postiz/frontend exec next dev -p 4200 -H 0.0.0.0
```

**2. Allow the tunnel host in `next.config`**

Add your tunnel hostname to the `allowedDevOrigins` field in
`apps/frontend/next.config.js` (introduced in Next.js 15.x). Without
this, Next.js refuses HMR connections coming through the tunnel.

```js theme={null}
const nextConfig = {
  allowedDevOrigins: ['your-subdomain.ngrok-free.app'],
  // …
};
```

**3. WebSockets must reach the dev server**

Most tunnels support WSS out of the box. If you've put your own
reverse proxy in front of the tunnel, ensure `Upgrade` and `Connection`
headers pass through — without them the HMR client disconnects every
few seconds.

## `redirectmeto` — why OAuth redirects sometimes go through a third party

When `FRONTEND_URL` is plain HTTP, several social providers
(Slack, TikTok, Threads, VK, Instagram standalone) refuse to register
your redirect URI. Postiz works around this by wrapping the redirect
through `https://redirectmeto.com/`:

```
https://redirectmeto.com/http://localhost:4200/integrations/social/slack
```

The browser hits `redirectmeto`, which serves an HTTPS page that
immediately redirects to the HTTP target — satisfying the provider's
HTTPS-only validation without needing your dev environment to have a
TLS cert.

**You only see this in dev.** Once `FRONTEND_URL` is HTTPS, Postiz
skips `redirectmeto` entirely and uses your URL directly.

If you don't want `redirectmeto` in the middle even in dev, terminate
TLS at your tunnel (ngrok and Cloudflared both do this by default) and
set `FRONTEND_URL` to the `https://` tunnel URL.
