##  [How Vercel handles certificates](https://vercel.com/docs/cdn-security/encryption#how-vercel-handles-certificates)[](https://vercel.com/docs/cdn-security/encryption#how-vercel-handles-certificates)
Vercel uses a wildcard certificate issued for `.vercel.app` to handle all deployment URLs. Vercel generates these certificates through
When you generate custom certificates with `vercel certs issue`, Vercel stores the keys in the database and
When a hostname is requested, the CDN reads the certificate and key from the database to establish the secure connection. Both are cached in memory for optimal SSL termination performance.
