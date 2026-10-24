# authInterrupts
This feature is currently available in the canary channel and subject to change. Try it out by [upgrading Next.js](https://nextjs.org/docs/app/getting-started/upgrading#canary-version), and share your feedback on
Last updated February 27, 2026
The `authInterrupts` configuration option allows you to use [`forbidden`](https://nextjs.org/docs/app/api-reference/functions/forbidden) and [`unauthorized`](https://nextjs.org/docs/app/api-reference/functions/unauthorized) APIs in your application. While these functions are experimental, you must enable the `authInterrupts` option in your `next.config.js` file to use them:
next.config.ts
TypeScript
JavaScript TypeScript
```
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  experimental: {
    authInterrupts: true,
  },
}

export default nextConfig
```

### [forbidden API Reference for the forbidden function.](https://nextjs.org/docs/app/api-reference/functions/forbidden)### [unauthorized API Reference for the unauthorized function.](https://nextjs.org/docs/app/api-reference/functions/unauthorized)### [forbidden.js API reference for the forbidden.js special file.](https://nextjs.org/docs/app/api-reference/file-conventions/forbidden)### [unauthorized.js API reference for the unauthorized.js special file.](https://nextjs.org/docs/app/api-reference/file-conventions/unauthorized)
[PreviousassetPrefix](https://nextjs.org/docs/app/api-reference/config/next-config-js/assetPrefix)[NextbasePath](https://nextjs.org/docs/app/api-reference/config/next-config-js/basePath)
Was this helpful?
Send
