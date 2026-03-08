## Troubleshooting[](https://nextjs.org/docs/app/guides/content-security-policy#troubleshooting)
### Third-party Scripts[](https://nextjs.org/docs/app/guides/content-security-policy#third-party-scripts)
When using third-party scripts with CSP:
app/layout.tsx
TypeScript
JavaScript TypeScript
```
import { GoogleTagManager } from '@next/third-parties/google'
import { headers } from 'next/headers'

export default async function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  const nonce = (await headers()).get('x-nonce')

  return (
    <html lang="en">
      <body>
        {children}
        <GoogleTagManager gtmId="GTM-XYZ" nonce={nonce} />
      </body>
    </html>
  )
}
```

Update your CSP to allow third-party domains:
proxy.ts
TypeScript
JavaScript TypeScript
```
const cspHeader = `
  default-src 'self';
  script-src 'self' 'nonce-${nonce}' 'strict-dynamic' https://www.googletagmanager.com;
  connect-src 'self' https://www.google-analytics.com;
  img-src 'self' data: https://www.google-analytics.com;
`
```

### Common CSP Violations[](https://nextjs.org/docs/app/guides/content-security-policy#common-csp-violations)
  1. **Inline styles** : Use CSS-in-JS libraries that support nonces or move styles to external files
  2. **Dynamic imports** : Ensure dynamic imports are allowed in your script-src policy
  3. **WebAssembly** : Add `'wasm-unsafe-eval'` if using WebAssembly
  4. **Service workers** : Add appropriate policies for service worker scripts
