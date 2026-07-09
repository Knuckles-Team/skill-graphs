## Unsupported and unplanned features[](https://nextjs.org/docs/app/api-reference/turbopack#unsupported-and-unplanned-features)
Some features are not yet implemented or not planned:
  * **Legacy CSS Modules features**
    * Standalone `:local` and `:global` pseudo-classes (only the function variant `:global(...)` is supported).
    * The `@value` rule (superseded by CSS variables).
    * `:import` and `:export` ICSS rules.
    * `composes` in `.module.css` composing a `.css` file. In webpack this would treat the `.css` file as a CSS Module, with Turbopack the `.css` file will always be global. This means that if you want to use `composes` in a CSS Module, you need to change the `.css` file to a `.module.css` file.
    * `@import` in CSS Modules importing `.css` as a CSS Module. In webpack this would treat the `.css` file as a CSS Module, with Turbopack the `.css` file will always be global. This means that if you want to use `@import` in a CSS Module, you need to change the `.css` file to a `.module.css` file.
  * **`sassOptions.functions`**Custom Sass functions defined in`sassOptions.functions` are not supported. This feature allows defining JavaScript functions that can be called from Sass code during compilation. Turbopack's Rust-based architecture cannot directly execute JavaScript functions passed through `sassOptions.functions`, unlike webpack's Node.js-based sass-loader which runs entirely in JavaScript. If you're using custom Sass functions, you'll need to use webpack instead of Turbopack.
  * **`webpack()`configuration** in `next.config.js` Turbopack replaces webpack, so `webpack()` configs are not recognized. Use the [`turbopack` config](https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopack) instead.
  * **Yarn PnP** Not planned for Turbopack support in Next.js.
  * **`experimental.urlImports`**Not planned for Turbopack.
  * **`experimental.esmExternals`**Not planned. Turbopack does not support the legacy`esmExternals` configuration in Next.js.
  * **Some Next.js Experimental Flags**
    * `experimental.nextScriptWorkers`
    * `experimental.sri.algorithm`
    * `experimental.fallbackNodePolyfills` We plan to implement these in the future.


For a full, detailed breakdown of each feature flag and its status, see the [Turbopack API Reference](https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopack).
