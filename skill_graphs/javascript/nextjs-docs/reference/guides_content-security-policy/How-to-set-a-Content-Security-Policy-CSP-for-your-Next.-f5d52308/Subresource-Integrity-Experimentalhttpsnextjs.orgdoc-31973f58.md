## Subresource Integrity (Experimental)[](https://nextjs.org/docs/app/guides/content-security-policy#subresource-integrity-experimental)
As an alternative to nonces, Next.js offers experimental support for hash-based CSP using Subresource Integrity (SRI). This approach allows you to maintain static generation while still having a strict CSP.
> **Good to know** : This feature is experimental and only available with webpack bundler in App Router applications.
### How SRI works[](https://nextjs.org/docs/app/guides/content-security-policy#how-sri-works)
Instead of using nonces, SRI generates cryptographic hashes of your JavaScript files at build time. These hashes are added as `integrity` attributes to script tags, allowing browsers to verify that files haven't been modified during transit.
### Enabling SRI[](https://nextjs.org/docs/app/guides/content-security-policy#enabling-sri)
Add the experimental SRI configuration to your `next.config.js`:
next.config.js
```
/** @type {import('next').NextConfig} */
const nextConfig = {
  experimental: {
    sri: {
      algorithm: 'sha256', // or 'sha384' or 'sha512'
    },
  },
}

module.exports = nextConfig
```

### CSP configuration with SRI[](https://nextjs.org/docs/app/guides/content-security-policy#csp-configuration-with-sri)
When SRI is enabled, you can continue using your existing CSP policies. SRI works independently by adding `integrity` attributes to your assets:
> **Good to know** : For dynamic rendering scenarios, you can still generate nonces with proxy if needed, combining both SRI integrity attributes and nonce-based CSP approaches.
next.config.js
```
const isDev = process.env.NODE_ENV === 'development'

const cspHeader = `
    default-src 'self';
    script-src 'self'${isDev ? " 'unsafe-eval'" : ''};
    style-src 'self';
    img-src 'self' blob: data:;
    font-src 'self';
    object-src 'none';
    base-uri 'self';
    form-action 'self';
    frame-ancestors 'none';
    upgrade-insecure-requests;
`

module.exports = {
  experimental: {
    sri: {
      algorithm: 'sha256',
    },
  },
  async headers() {
    return [
      {
        source: '/(.*)',
        headers: [
          {
            key: 'Content-Security-Policy',
            value: cspHeader.replace(/\n/g, ''),
          },
        ],
      },
    ]
  },
}
```

### Benefits of SRI over nonces[](https://nextjs.org/docs/app/guides/content-security-policy#benefits-of-sri-over-nonces)
  * **Static generation** : Pages can be statically generated and cached
  * **CDN compatibility** : Static pages work with CDN caching
  * **Better performance** : No server-side rendering required for each request
  * **Build-time security** : Hashes are generated at build time, ensuring integrity


### Limitations of SRI[](https://nextjs.org/docs/app/guides/content-security-policy#limitations-of-sri)
  * **Experimental** : Feature may change or be removed
  * **Webpack only** : Not available with Turbopack
  * **App Router only** : Not supported in Pages Router
  * **Build-time only** : Cannot handle dynamically generated scripts
