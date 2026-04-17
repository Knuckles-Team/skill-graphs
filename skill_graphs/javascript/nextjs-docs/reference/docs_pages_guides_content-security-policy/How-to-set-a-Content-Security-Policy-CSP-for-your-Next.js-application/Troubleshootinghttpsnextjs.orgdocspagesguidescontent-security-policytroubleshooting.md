## Troubleshooting[](https://nextjs.org/docs/pages/guides/content-security-policy#troubleshooting)
### Third-party Scripts[](https://nextjs.org/docs/pages/guides/content-security-policy#third-party-scripts)
When using third-party scripts with CSP, ensure you add the necessary domains and pass the nonce:
pages/_app.tsx
TypeScript
JavaScript TypeScript
```
import type { AppProps } from 'next/app'
import Script from 'next/script'

export default function App({ Component, pageProps }: AppProps) {
  const nonce = pageProps.nonce

  return (
    <>
      <Component {...pageProps} />
      <Script
        src="https://www.googletagmanager.com/gtag/js"
        strategy="afterInteractive"
        nonce={nonce}
      />
    </>
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

### Common CSP Violations[](https://nextjs.org/docs/pages/guides/content-security-policy#common-csp-violations)
  1. **Inline styles** : Use CSS-in-JS libraries that support nonces or move styles to external files
  2. **Dynamic imports** : Ensure dynamic imports are allowed in your script-src policy
  3. **WebAssembly** : Add `'wasm-unsafe-eval'` if using WebAssembly
  4. **Service workers** : Add appropriate policies for service worker scripts
