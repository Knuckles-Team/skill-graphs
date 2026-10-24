## Development vs Production Considerations[](https://nextjs.org/docs/pages/guides/content-security-policy#development-vs-production-considerations)
CSP implementation differs between development and production environments:
### Development Environment[](https://nextjs.org/docs/pages/guides/content-security-policy#development-environment)
In development, you will need to enable `'unsafe-eval'` because React uses `eval` to provide enhanced debugging information, such as reconstructing server-side error stacks in the browser to show you where errors originated on the server:
proxy.ts
TypeScript
JavaScript TypeScript
```
export function proxy(request: NextRequest) {
  const nonce = Buffer.from(crypto.randomUUID()).toString('base64')
  const isDev = process.env.NODE_ENV === 'development'

  const cspHeader = `
    default-src 'self';
    script-src 'self' 'nonce-${nonce}' 'strict-dynamic' ${isDev ? "'unsafe-eval'" : ''};
    style-src 'self' ${isDev ? "'unsafe-inline'" : `'nonce-${nonce}'`};
    img-src 'self' blob: data:;
    font-src 'self';
    object-src 'none';
    base-uri 'self';
    form-action 'self';
    frame-ancestors 'none';
    upgrade-insecure-requests;
`

  // Rest of proxy implementation
}
```

### Production Deployment[](https://nextjs.org/docs/pages/guides/content-security-policy#production-deployment)
Common issues in production:
  * **Nonce not applied** : Ensure your proxy runs on all necessary routes
  * **Static assets blocked** : Verify your CSP allows Next.js static assets
  * **Third-party scripts** : Add necessary domains to your CSP policy
