## API Reference[](https://nextjs.org/docs/app/api-reference/config/next-config-js/adapterPath#api-reference)
###  `modifyConfig(config, context)`[](https://nextjs.org/docs/app/api-reference/config/next-config-js/adapterPath#modifyconfigconfig-context)
Called for any CLI command that loads the next.config to allow modification of the configuration.
**Parameters:**
  * `config`: The complete Next.js configuration object
  * `context.phase`: The current build phase (see [phases](https://nextjs.org/docs/app/api-reference/config/next-config-js#phase))


**Returns:** The modified configuration object (can be async)
###  `onBuildComplete(context)`[](https://nextjs.org/docs/app/api-reference/config/next-config-js/adapterPath#onbuildcompletecontext)
Called after the build process completes with detailed information about routes and outputs.
**Parameters:**
  * `routes`: Object containing route manifests for headers, redirects, rewrites, and dynamic routes
    * `routes.headers`: Array of header route objects with `source`, `sourceRegex`, `headers`, `has`, `missing`, and optional `priority` fields
    * `routes.redirects`: Array of redirect route objects with `source`, `sourceRegex`, `destination`, `statusCode`, `has`, `missing`, and optional `priority` fields
    * `routes.rewrites`: Object with `beforeFiles`, `afterFiles`, and `fallback` arrays, each containing rewrite route objects with `source`, `sourceRegex`, `destination`, `has`, and `missing` fields
    * `routes.dynamicRoutes`: Array of dynamic route objects with `source`, `sourceRegex`, `destination`, `has`, and `missing` fields
  * `outputs`: Detailed information about all build outputs organized by type
  * `projectDir`: Absolute path to the Next.js project directory
  * `repoRoot`: Absolute path to the detected repository root
  * `distDir`: Absolute path to the build output directory
  * `config`: The final Next.js configuration (with `modifyConfig` applied)
  * `nextVersion`: Version of Next.js being used
  * `buildId`: Unique identifier for the current build
