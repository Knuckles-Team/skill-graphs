## Reference[](https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopack#reference)
### Options[](https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopack#options)
The following options are available for the `turbopack` configuration:
Option | Description
---|---
`root` | Sets the application root directory. Should be an absolute path.
`rules` | List of supported webpack loaders to apply when running with Turbopack.
`resolveAlias` | Map aliased imports to modules to load in their place.
`resolveExtensions` | List of extensions to resolve when importing files.
`debugIds` | Enable generation of
### Supported loaders[](https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopack#supported-loaders)
The following loaders have been tested to work with Turbopack's webpack loader implementation, but many other webpack loaders should work as well even if not listed here:
  * [_(Configured automatically if a Babel configuration file is found)_](https://nextjs.org/docs/app/api-reference/turbopack#language-features)
  * [_(Configured automatically)_](https://nextjs.org/docs/app/api-reference/turbopack#css-and-styling)


#### Missing Webpack loader features[](https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopack#missing-webpack-loader-features)
Turbopack uses the
**Module loading:**
**File system and output:**
  * `fs.readFile` is currently implemented.


**Context properties:**
**Utilities:**
If you have a loader that is critically dependent upon one of these features please file an issue.
