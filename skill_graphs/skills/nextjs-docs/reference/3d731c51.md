## Configuration[](https://nextjs.org/docs/app/api-reference/turbopack#configuration)
Turbopack can be configured via `next.config.js` (or `next.config.ts`) under the `turbopack` key. Configuration options include:
  * **`rules`**Define additional[webpack loaders](https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopack#configuring-webpack-loaders) for file transformations.
  * **`resolveAlias`**Create manual aliases (like`resolve.alias` in webpack).
  * **`resolveExtensions`**Change or extend file extensions for module resolution.


next.config.js
```
module.exports = {
  turbopack: {
    // Example: adding an alias and custom file extension
    resolveAlias: {
      underscore: 'lodash',
    },
    resolveExtensions: ['.mdx', '.tsx', '.ts', '.jsx', '.js', '.json'],
  },
}
```

For more in-depth configuration examples, see the [Turbopack config documentation](https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopack).
