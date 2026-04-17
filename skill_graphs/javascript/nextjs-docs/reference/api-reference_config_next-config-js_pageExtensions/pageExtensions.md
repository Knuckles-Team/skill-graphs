# pageExtensions
Last updated February 27, 2026
By default, Next.js accepts files with the following extensions: `.tsx`, `.ts`, `.jsx`, `.js`. This can be modified to allow other extensions like markdown (`.md`, `.mdx`).
next.config.js
```
const withMDX = require('@next/mdx')()

/** @type {import('next').NextConfig} */
const nextConfig = {
  pageExtensions: ['js', 'jsx', 'ts', 'tsx', 'md', 'mdx'],
}

module.exports = withMDX(nextConfig)
```

[Previousoutput](https://nextjs.org/docs/app/api-reference/config/next-config-js/output)[NextpoweredByHeader](https://nextjs.org/docs/app/api-reference/config/next-config-js/poweredByHeader)
Was this helpful?
Send
