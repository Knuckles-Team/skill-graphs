## Why This Message Occurred[](https://nextjs.org/docs/messages/webpack5#why-this-message-occurred)
Next.js has adopted webpack 5 as the default for compilation. We've spent a lot of effort into ensuring the transition from webpack 4 to 5 will be as smooth as possible.
Your application currently has webpack 5 disabled using the `webpack5: false` flag which has been removed in Next.js 12:
next.config.js
```
module.exports = {
  // Webpack 5 is enabled by default
  // You can still use webpack 4 while upgrading to the latest version of Next.js by adding the "webpack5: false" flag
  webpack5: false,
}
```

Using webpack 5 in your application has many benefits, notably:
  * Improved Disk Caching: `next build` is significantly faster on subsequent builds
  * Improved Fast Refresh: Fast Refresh work is prioritized
  * Improved Long Term Caching of Assets: Deterministic code output that is less likely to change between builds
  * Improved Tree Shaking
  * Support for assets using `new URL("file.png", import.meta.url)`
  * Support for web workers using `new Worker(new URL("worker.js", import.meta.url))`
  * Support for `exports`/`imports` field in `package.json`


In the past releases we have gradually rolled out webpack 5 to Next.js applications:
  * In Next.js 10.2 we automatically opted-in applications without custom webpack configuration in `next.config.js`
  * In Next.js 10.2 we automatically opted-in applications that do not have a `next.config.js`
  * In Next.js 11 webpack 5 was enabled by default for all applications. You could still opt-out and use webpack 4 to help with backwards compatibility using `webpack5: false` in `next.config.js`
  * In Next.js 12 webpack 4 support was removed.
