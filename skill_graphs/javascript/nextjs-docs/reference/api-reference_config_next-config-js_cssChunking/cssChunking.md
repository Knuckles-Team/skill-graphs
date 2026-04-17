# cssChunking
This feature is currently experimental and subject to change, it's not recommended for production. Try it out and share your feedback on
Last updated February 27, 2026
CSS Chunking is a strategy used to improve the performance of your web application by splitting and re-ordering CSS files into chunks. This allows you to load only the CSS that is needed for a specific route, instead of loading all the application's CSS at once.
You can control how CSS files are chunked using the `experimental.cssChunking` option in your `next.config.js` file:
next.config.ts
TypeScript
JavaScript TypeScript
```
import type { NextConfig } from 'next'

const nextConfig = {
  experimental: {
    cssChunking: true, // default
  },
} satisfies NextConfig

export default nextConfig
```
