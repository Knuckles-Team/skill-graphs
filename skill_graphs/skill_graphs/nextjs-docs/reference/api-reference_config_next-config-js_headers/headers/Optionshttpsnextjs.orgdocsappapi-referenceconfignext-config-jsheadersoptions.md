## Options[](https://nextjs.org/docs/app/api-reference/config/next-config-js/headers#options)
### CORS[](https://nextjs.org/docs/app/api-reference/config/next-config-js/headers#cors)
`Access-Control-Allow-Origin` header to allow a specific origin to access your Route Handlers.
```
async headers() {
    return [
      {
        source: "/api/:path*",
        headers: [
          {
            key: "Access-Control-Allow-Origin",
            value: "*", // Set your origin
          },
          {
            key: "Access-Control-Allow-Methods",
            value: "GET, POST, PUT, DELETE, OPTIONS",
          },
          {
            key: "Access-Control-Allow-Headers",
            value: "Content-Type, Authorization",
          },
        ],
      },
    ];
  },
```

### X-DNS-Prefetch-Control[](https://nextjs.org/docs/app/api-reference/config/next-config-js/headers#x-dns-prefetch-control)
```
{
  key: 'X-DNS-Prefetch-Control',
  value: 'on'
}
```

### Strict-Transport-Security[](https://nextjs.org/docs/app/api-reference/config/next-config-js/headers#strict-transport-security)
`max-age` of 2 years. This blocks access to pages or subdomains that can only be served over HTTP.
```
{
  key: 'Strict-Transport-Security',
  value: 'max-age=63072000; includeSubDomains; preload'
}
```

### X-Frame-Options[](https://nextjs.org/docs/app/api-reference/config/next-config-js/headers#x-frame-options)
`iframe`. This can prevent against clickjacking attacks.
**This header has been superseded by CSP's`frame-ancestors` option**, which has better support in modern browsers (see [Content Security Policy](https://nextjs.org/docs/app/guides/content-security-policy) for configuration details).
```
{
  key: 'X-Frame-Options',
  value: 'SAMEORIGIN'
}
```

### Permissions-Policy[](https://nextjs.org/docs/app/api-reference/config/next-config-js/headers#permissions-policy)
`Feature-Policy`.
```
{
  key: 'Permissions-Policy',
  value: 'camera=(), microphone=(), geolocation=(), browsing-topics=()'
}
```

### X-Content-Type-Options[](https://nextjs.org/docs/app/api-reference/config/next-config-js/headers#x-content-type-options)
`Content-Type` header is not explicitly set. This can prevent XSS exploits for websites that allow users to upload and share files.
For example, a user trying to download an image, but having it treated as a different `Content-Type` like an executable, which could be malicious. This header also applies to downloading browser extensions. The only valid value for this header is `nosniff`.
```
{
  key: 'X-Content-Type-Options',
  value: 'nosniff'
}
```

### Referrer-Policy[](https://nextjs.org/docs/app/api-reference/config/next-config-js/headers#referrer-policy)
```
{
  key: 'Referrer-Policy',
  value: 'origin-when-cross-origin'
}
```

### Content-Security-Policy[](https://nextjs.org/docs/app/api-reference/config/next-config-js/headers#content-security-policy)
Learn more about adding a [Content Security Policy](https://nextjs.org/docs/app/guides/content-security-policy) to your application.
