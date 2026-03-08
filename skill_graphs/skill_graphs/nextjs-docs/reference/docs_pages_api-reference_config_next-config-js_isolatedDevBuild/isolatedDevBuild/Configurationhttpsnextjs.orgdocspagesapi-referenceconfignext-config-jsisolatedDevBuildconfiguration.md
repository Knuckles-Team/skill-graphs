## Configuration[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/isolatedDevBuild#configuration)
To opt out of this feature, set `isolatedDevBuild` to `false` in your configuration:
next.config.ts
TypeScript
JavaScript TypeScript
```
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  experimental: {
    isolatedDevBuild: false, // defaults to true
  },
}

export default nextConfig
```
