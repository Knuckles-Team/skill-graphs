## Custom webpack configuration[](https://nextjs.org/docs/messages/webpack5#custom-webpack-configuration)
In case you do have custom webpack configuration, either through custom plugins or your own modifications you'll have to take a few steps to ensure your applications works with webpack 5.
  * When using `next-transpile-modules` make sure you use the latest version which includes
  * When using `@zeit/next-css` / `@zeit/next-sass` make sure you use the [built-in CSS/Sass support](https://nextjs.org/docs/app/getting-started/css) instead
  * When using `@zeit/next-preact` use
  * When using `@zeit/next-source-maps` use the [built-in production Source Map support](https://nextjs.org/docs/pages/api-reference/config/next-config-js/productionBrowserSourceMaps)
  * When using webpack plugins make sure they're upgraded to the latest version, in most cases the latest version will include webpack 5 support. In some cases these upgraded webpack plugins will only support webpack 5.
