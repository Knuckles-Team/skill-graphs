## Supported features[](https://nextjs.org/docs/pages/api-reference/turbopack#supported-features)
Turbopack in Next.js has **zero-configuration** for the common use cases. Below is a summary of what is supported out of the box, plus some references to how you can configure Turbopack further when needed.
### Language features[](https://nextjs.org/docs/pages/api-reference/turbopack#language-features)
Feature | Status | Notes
---|---|---
**JavaScript & TypeScript** | **Supported** | Uses SWC under the hood. Type-checking is not done by Turbopack (run `tsc --watch` or rely on your IDE for type checks).
**ECMAScript (ESNext)** | **Supported** | Turbopack supports the latest ECMAScript features, matching SWC’s coverage.
**CommonJS** | **Supported** |  `require()` syntax is handled out of the box.
**ESM** | **Supported** | Static and dynamic `import` are fully supported.
**Babel** | **Supported** | Starting in Next.js 16, Turbopack uses Babel automatically if it detects `node_modules` are excluded, unless you [manually configure `babel-loader`](https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopack#configuring-webpack-loaders).
### Framework and React features[](https://nextjs.org/docs/pages/api-reference/turbopack#framework-and-react-features)
Feature | Status | Notes
---|---|---
**JSX / TSX** | **Supported** | SWC handles JSX/TSX compilation.
**Fast Refresh** | **Supported** | No configuration needed.
**React Server Components (RSC)** | **Supported** | For the Next.js App Router. Turbopack ensures correct server/client bundling.
**Root layout creation** | Unsupported | Automatic creation of a root layout in App Router is not supported. Turbopack will instruct you to create it manually.
### CSS and styling[](https://nextjs.org/docs/pages/api-reference/turbopack#css-and-styling)
Feature | Status | Notes
---|---|---
**Global CSS** | **Supported** | Import `.css` files directly in your application.
**CSS Modules** | **Supported** |  `.module.css` files work natively (Lightning CSS).
**CSS Nesting** | **Supported** | Lightning CSS supports
**@import syntax** | **Supported** | Combine multiple CSS files.
**PostCSS** | **Supported** | Automatically processes `postcss.config.js` in a Node.js worker pool. Useful for Tailwind, Autoprefixer, etc.
**Sass / SCSS** |  **Supported** (Next.js) | For Next.js, Sass is supported out of the box. Custom Sass functions (`sassOptions.functions`) are not supported because Turbopack's Rust-based architecture cannot directly execute JavaScript functions, unlike webpack's Node.js environment. Use webpack if you need this feature. In the future, Turbopack standalone usage will likely require a loader config.
**Less** | Planned via plugins | Not yet supported by default. Will likely require a loader config once custom loaders are stable.
**Lightning CSS** | **In Use** | Handles CSS transformations. Some low-usage CSS Modules features (like `:local/:global` as standalone pseudo-classes) are not yet supported. [See below for more details.](https://nextjs.org/docs/pages/api-reference/turbopack#unsupported-and-unplanned-features)
### Assets[](https://nextjs.org/docs/pages/api-reference/turbopack#assets)
Feature | Status | Notes
---|---|---
**Static Assets** (images, fonts) | **Supported** | Importing `import img from './img.png'` works out of the box. In Next.js, returns an object for the `<Image />` component.
**JSON Imports** | **Supported** | Named or default imports from `.json` are supported.
### Module resolution[](https://nextjs.org/docs/pages/api-reference/turbopack#module-resolution)
Feature | Status | Notes
---|---|---
**Path Aliases** | **Supported** | Reads `tsconfig.json`'s `paths` and `baseUrl`, matching Next.js behavior.
**Manual Aliases** | **Supported** |  [Configure `resolveAlias` in `next.config.js`](https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopack#resolving-aliases) (similar to `webpack.resolve.alias`).
**Custom Extensions** | **Supported** |  [Configure `resolveExtensions` in `next.config.js`](https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopack#resolving-custom-extensions).
**AMD** | Partially Supported | Basic transforms work; advanced AMD usage is limited.
### Performance and Fast Refresh[](https://nextjs.org/docs/pages/api-reference/turbopack#performance-and-fast-refresh)
Feature | Status | Notes
---|---|---
**Fast Refresh** | **Supported** | Updates JavaScript, TypeScript, and CSS without a full refresh.
**Incremental Bundling** | **Supported** | Turbopack lazily builds only what’s requested by the dev server, speeding up large apps.
