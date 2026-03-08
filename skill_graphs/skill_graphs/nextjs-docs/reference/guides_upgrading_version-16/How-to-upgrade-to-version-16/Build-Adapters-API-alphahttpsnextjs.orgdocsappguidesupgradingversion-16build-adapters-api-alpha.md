## Build Adapters API (alpha)[](https://nextjs.org/docs/app/guides/upgrading/version-16#build-adapters-api-alpha)
Following the
Build Adapters allow you to create custom adapters that hook into the build process, enabling deployment platforms and custom build integrations to modify Next.js configuration or process build output.
next.config.js
```
const nextConfig = {
  experimental: {
    adapterPath: require.resolve('./my-adapter.js'),
  },
}

module.exports = nextConfig
```

Share your feedback in the
