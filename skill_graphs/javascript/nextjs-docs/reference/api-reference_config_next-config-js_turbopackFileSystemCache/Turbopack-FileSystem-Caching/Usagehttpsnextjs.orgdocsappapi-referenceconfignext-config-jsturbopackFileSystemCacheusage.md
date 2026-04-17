## Usage[](https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopackFileSystemCache#usage)
Turbopack FileSystem Cache enables Turbopack to reduce work across `next dev` or `next build` commands. When enabled, Turbopack will save and restore data to the `.next` folder between builds, which can greatly speed up subsequent builds and dev sessions.
> **Good to know:** The FileSystem Cache feature is considered stable for development and experimental for production builds
next.config.ts
TypeScript
JavaScript TypeScript
```
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  experimental: {
    // Enable filesystem caching for `next dev`
    turbopackFileSystemCacheForDev: true,
    // Enable filesystem caching for `next build`
    turbopackFileSystemCacheForBuild: true,
  },
}

export default nextConfig
```
