## Examples[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/turbopack#examples)
### Root directory[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/turbopack#root-directory)
Turbopack uses the root directory to resolve modules. Files outside of the project root are not resolved.
The reason files are not resolved outside of the project root is to improve cache validation, reduce filesystem watching overhead, and reduce the number of resolving steps needed.
Next.js automatically detects the root directory of your project. It does so by looking for one of these files:
  * `pnpm-lock.yaml`
  * `package-lock.json`
  * `yarn.lock`
  * `bun.lock`
  * `bun.lockb`


If you have a different project structure, for example if you don't use workspaces, you can manually set the `root` option:
next.config.js
```
const path = require('path')
module.exports = {
  turbopack: {
    root: path.join(__dirname, '..'),
  },
}
```

To resolve files from linked dependencies outside the project root (via `npm link`, `yarn link`, `pnpm link`, etc.), you must configure the `turbopack.root` to the parent directory of both the project and the linked dependencies.
While this expands the scope of filesystem watching, it's typically only necessary during development when actively working on linked packages.
### Configuring webpack loaders[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/turbopack#configuring-webpack-loaders)
If you need loader support beyond what's built in, many webpack loaders already work with Turbopack. There are currently some limitations:
  * Only a core subset of the webpack loader API is implemented. Currently, there is enough coverage for some popular loaders, and we'll expand our API support in the future.
  * Only loaders that return JavaScript code are supported. Loaders that transform files like stylesheets or images are not currently supported.
  * Options passed to webpack loaders must be plain JavaScript primitives, objects, and arrays. For example, it's not possible to pass `require()` plugin modules as option values.


To configure loaders, add the names of the loaders you've installed and any options in `next.config.js`, mapping file extensions to a list of loaders. Rules are evaluated in order.
Here is an example below using the `.svg` files and rendering them as React components.
next.config.js
```
module.exports = {
  turbopack: {
    rules: {
      '*.svg': {
        loaders: ['@svgr/webpack'],
        as: '*.js',
      },
    },
  },
}
```

> **Good to know** : Globs used in the `rules` object match based on file name, unless the glob contains a `/` character, which will cause it to match based on the full project-relative file path. Windows file paths are normalized to use unix-style `/` path separators.
> Turbopack uses a modified version of the
For loaders that require configuration options, you can use an object format instead of a string:
next.config.js
```
module.exports = {
  turbopack: {
    rules: {
      '*.svg': {
        loaders: [
          {
            loader: '@svgr/webpack',
            options: {
              icon: true,
            },
          },
        ],
        as: '*.js',
      },
    },
  },
}
```

> **Good to know** : Prior to Next.js version 13.4.4, `turbopack.rules` was named `turbo.loaders` and only accepted file extensions like `.mdx` instead of `*.mdx`.
### Advanced webpack loader conditions[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/turbopack#advanced-webpack-loader-conditions)
You can further restrict where a loader runs using the advanced `condition` syntax:
next.config.js
```
module.exports = {
  turbopack: {
    rules: {
      // '*' will match all file paths, but we restrict where our
      // rule runs with a condition.
      '*': {
        condition: {
          all: [
            // 'foreign' is a built-in condition.
            { not: 'foreign' },
            // 'path' can be a RegExp or a glob string. A RegExp matches
            // anywhere in the full project-relative file path.
            { path: /^img\/[0-9]{3}\// },
            {
              any: [
                { path: '*.svg' },
                // 'content' is always a RegExp, and can match
                // anywhere in the file.
                { content: /\<svg\W/ },
              ],
            },
          ],
        },
        loaders: ['@svgr/webpack'],
        as: '*.js',
      },
    },
  },
}
```

  * Supported boolean operators are `{all: [...]}`, `{any: [...]}` and `{not: ...}`.
  * Supported customizable operators are `{path: string | RegExp}` and `{content: RegExp}`. If `path` and `content` are specified in the same object, it acts as an implicit `and`.


In addition, a number of built-in conditions are supported:
  * `browser`: Matches code that will execute on the client. Server code can be matched using `{not: 'browser'}`.
  * `foreign`: Matches code in `node_modules`, as well as some Next.js internals. Usually you'll want to restrict loaders to `{not: 'foreign'}`. This can improve performance by reducing the number of files the loader is invoked on.
  * `development`: Matches when using `next dev`.
  * `production`: Matches when using `next build`.
  * `node`: Matches code that will run on the default Node.js runtime.
  * `edge-light`: Matches code that will run on the [Edge runtime](https://nextjs.org/docs/app/api-reference/edge).


Rules can be an object or an array of objects. An array is often useful for modeling disjoint conditions:
next.config.js
```
module.exports = {
  turbopack: {
    rules: {
      '*.svg': [
        {
          condition: 'browser',
          loaders: ['@svgr/webpack'],
          as: '*.js',
        },
        {
          condition: { not: 'browser' },
          loaders: [require.resolve('./custom-svg-loader.js')],
          as: '*.js',
        },
      ],
    },
  },
}
```

> **Good to know** : All matching rules are executed in order.
### Resolving aliases[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/turbopack#resolving-aliases)
Turbopack can be configured to modify module resolution through aliases, similar to webpack's
To configure resolve aliases, map imported patterns to their new destination in `next.config.js`:
next.config.js
```
module.exports = {
  turbopack: {
    resolveAlias: {
      underscore: 'lodash',
      mocha: { browser: 'mocha/browser-entry.js' },
    },
  },
}
```

This aliases imports of the `underscore` package to the `lodash` package. In other words, `import underscore from 'underscore'` will load the `lodash` module instead of `underscore`.
Turbopack also supports conditional aliasing through this field, similar to Node.js' `browser` condition is supported. In the case above, imports of the `mocha` module will be aliased to `mocha/browser-entry.js` when Turbopack targets browser environments.
### Resolving custom extensions[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/turbopack#resolving-custom-extensions)
Turbopack can be configured to resolve modules with custom extensions, similar to webpack's
To configure resolve extensions, use the `resolveExtensions` field in `next.config.js`:
next.config.js
```
module.exports = {
  turbopack: {
    resolveExtensions: ['.mdx', '.tsx', '.ts', '.jsx', '.js', '.mjs', '.json'],
  },
}
```

This overwrites the original resolve extensions with the provided list. Make sure to include the default extensions.
For more information and guidance for how to migrate your app to Turbopack from webpack, see
### Debug IDs[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/turbopack#debug-ids)
Turbopack can be configured to generate
To configure debug IDs, use the `debugIds` field in `next.config.js`:
next.config.js
```
module.exports = {
  turbopack: {
    debugIds: true,
  },
}
```

The option automatically adds a polyfill for debug IDs to the JavaScript bundle to ensure compatibility. The debug IDs are available in the `globalThis._debugIds` global variable.
