## bundlePagesRouterDependencies[](https://nextjs.org/docs/app/guides/upgrading/version-15#bundlepagesrouterdependencies)
`experimental.bundlePagesExternals` is now stable and renamed to `bundlePagesRouterDependencies`.
next.config.js
```
/** @type {import('next').NextConfig} */
const nextConfig = {
  // Before
  experimental: {
    bundlePagesExternals: true,
  },

  // After
  bundlePagesRouterDependencies: true,
}

module.exports = nextConfig
```
