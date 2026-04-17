## Partial Pre-Rendering (PPR)[](https://nextjs.org/docs/app/guides/upgrading/version-16#partial-pre-rendering-ppr)
**Next.js 16** removes the experimental **Partial Pre-Rendering (PPR)** flag and configuration options, including the route level segment `experimental_ppr`.
Starting with **Next.js 16** , you can opt into PPR using the [`cacheComponents`](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheComponents) configuration.
next.config.js
```
/** @type {import('next').NextConfig} */
const nextConfig = {
  cacheComponents: true,
}

module.exports = nextConfig
```

PPR in **Next.js 16** works differently than in **Next.js 15** canaries. If you are using PPR today, stay in the current Next.js 15 canary you are using. We will follow up with a guide to migrate to Cache Components.
next.config.js
```
/** @type {import('next').NextConfig} */
const nextConfig = {
  // If you are using PPR today
  // stay in the current Next.js 15 canary
  experimental: {
    ppr: true,
  },
}

module.exports = nextConfig
```
