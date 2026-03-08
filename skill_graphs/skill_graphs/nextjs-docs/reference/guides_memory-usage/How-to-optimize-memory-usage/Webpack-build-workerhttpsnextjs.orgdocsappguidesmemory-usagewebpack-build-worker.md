## Webpack build worker[](https://nextjs.org/docs/app/guides/memory-usage#webpack-build-worker)
The Webpack build worker allows you to run Webpack compilations inside a separate Node.js worker which will decrease memory usage of your application during builds.
This option is enabled by default if your application does not have a custom Webpack configuration starting in `v14.1.0`.
If you are using an older version of Next.js or you have a custom Webpack configuration, you can enable this option by setting `experimental.webpackBuildWorker: true` inside your `next.config.js`.
> **Good to know** : This feature may not be compatible with all custom Webpack plugins.
