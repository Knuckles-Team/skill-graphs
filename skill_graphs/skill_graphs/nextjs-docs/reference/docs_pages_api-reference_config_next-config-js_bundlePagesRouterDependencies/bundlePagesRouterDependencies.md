# bundlePagesRouterDependencies
Last updated February 27, 2026
Enable automatic server-side dependency bundling for Pages Router applications. Matches the automatic dependency bundling in App Router.
next.config.js
```
/** @type {import('next').NextConfig} */
const nextConfig = {
  bundlePagesRouterDependencies: true,
}

module.exports = nextConfig
```

Explicitly opt-out certain packages from being bundled using the [`serverExternalPackages`](https://nextjs.org/docs/pages/api-reference/config/next-config-js/serverExternalPackages) option.
