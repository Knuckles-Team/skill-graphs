## Disable Webpack cache[](https://nextjs.org/docs/app/guides/memory-usage#disable-webpack-cache)
The
You can disable this behavior by adding a [custom Webpack configuration](https://nextjs.org/docs/app/api-reference/config/next-config-js/webpack) to your application:
next.config.mjs
```
/** @type {import('next').NextConfig} */
const nextConfig = {
  webpack: (
    config,
    { buildId, dev, isServer, defaultLoaders, nextRuntime, webpack }
  ) => {
    if (config.cache && !dev) {
      config.cache = Object.freeze({
        type: 'memory',
      })
    }
    // Important: return the modified config
    return config
  },
}

export default nextConfig
```
