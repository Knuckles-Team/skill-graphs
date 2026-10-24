## serverExternalPackages[](https://nextjs.org/docs/app/guides/upgrading/version-15#serverexternalpackages)
`experimental.serverComponentsExternalPackages` is now stable and renamed to `serverExternalPackages`.
next.config.js
```
/** @type {import('next').NextConfig} */
const nextConfig = {
  // Before
  experimental: {
    serverComponentsExternalPackages: ['package-name'],
  },

  // After
  serverExternalPackages: ['package-name'],
}

module.exports = nextConfig
```
