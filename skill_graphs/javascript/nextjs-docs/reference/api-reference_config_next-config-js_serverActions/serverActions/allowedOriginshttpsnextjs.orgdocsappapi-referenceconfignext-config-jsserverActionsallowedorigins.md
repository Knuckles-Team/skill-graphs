##  `allowedOrigins`[](https://nextjs.org/docs/app/api-reference/config/next-config-js/serverActions#allowedorigins)
A list of extra safe origin domains from which Server Actions can be invoked. Next.js compares the origin of a Server Action request with the host domain, ensuring they match to prevent CSRF attacks. If not provided, only the same origin is allowed.
next.config.js
```
/** @type {import('next').NextConfig} */

module.exports = {
  experimental: {
    serverActions: {
      allowedOrigins: ['my-proxy.com', '*.my-proxy.com'],
    },
  },
}
```
