## Configuration[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/adapterPath#configuration)
To use an adapter, specify the path to your adapter module in `experimental.adapterPath`:
next.config.js
```
/** @type {import('next').NextConfig} */
const nextConfig = {
  experimental: {
    adapterPath: require.resolve('./my-adapter.js'),
  },
}

module.exports = nextConfig
```
