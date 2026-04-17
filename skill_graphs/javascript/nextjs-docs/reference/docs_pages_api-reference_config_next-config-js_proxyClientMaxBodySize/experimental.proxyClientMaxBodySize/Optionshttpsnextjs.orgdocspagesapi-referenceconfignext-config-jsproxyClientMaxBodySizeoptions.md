## Options[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/proxyClientMaxBodySize#options)
### String format (recommended)[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/proxyClientMaxBodySize#string-format-recommended)
Specify the size using a human-readable string format:
next.config.ts
TypeScript
JavaScript TypeScript
```
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  experimental: {
    proxyClientMaxBodySize: '1mb',
  },
}

export default nextConfig
```

Supported units: `b`, `kb`, `mb`, `gb`
### Number format[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/proxyClientMaxBodySize#number-format)
Alternatively, specify the size in bytes as a number:
next.config.ts
TypeScript
JavaScript TypeScript
```
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  experimental: {
    proxyClientMaxBodySize: 1048576, // 1MB in bytes
  },
}

export default nextConfig
```
