##  `middleware` to `proxy`[](https://nextjs.org/docs/app/guides/upgrading/version-16#middleware-to-proxy)
The `middleware` filename is deprecated, and has been renamed to `proxy` to clarify network boundary and routing focus.
The `edge` runtime is **NOT** supported in `proxy`. The `proxy` runtime is `nodejs`, and it cannot be configured. If you want to continue using the `edge` runtime, keep using `middleware`. We will follow up on a minor release with further `edge` runtime instructions.
Terminal
```
# Rename your middleware file
mv middleware.ts proxy.ts
# or
mv middleware.js proxy.js
```

The named export `middleware` is also deprecated. Rename your function to `proxy`.
proxy.ts
TypeScript
JavaScript TypeScript
```
export function proxy(request: Request) {}
```

We recommend changing the function name to `proxy`, even if you are using a default export.
Configuration flags that contained the `middleware` name are also renamed. For example, `skipMiddlewareUrlNormalize` is now `skipProxyUrlNormalize`
next.config.ts
TypeScript
JavaScript TypeScript
```
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  skipProxyUrlNormalize: true,
}

export default nextConfig
```

The version 16 [codemod](https://nextjs.org/docs/app/guides/upgrading/codemods#160) is able to update these flags too.
