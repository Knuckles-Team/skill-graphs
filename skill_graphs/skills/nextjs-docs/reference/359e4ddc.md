## Caveats[](https://nextjs.org/docs/app/api-reference/config/next-config-js/output#caveats)
  * While tracing in monorepo setups, the project directory is used for tracing by default. For `next build packages/web-app`, `packages/web-app` would be the tracing root and any files outside of that folder will not be included. To include files outside of this folder you can set `outputFileTracingRoot` in your `next.config.js`.


packages/web-app/next.config.js
```
const path = require('path')

module.exports = {
  // this includes files from the monorepo base two directories up
  outputFileTracingRoot: path.join(__dirname, '../../'),
}
```

  * There are some cases in which Next.js might fail to include required files, or might incorrectly include unused files. In those cases, you can leverage `outputFileTracingExcludes` and `outputFileTracingIncludes` respectively in `next.config.js`. Each option accepts an object whose keys are **route globs** (matched with `/api/hello`) and whose values are **glob patterns resolved from the project root** that specify files to include or exclude in the trace.


> **Good to know** : In a monorepo, `project root` refers to the Next.js project root (the folder containing next.config.js, e.g., packages/web-app), not necessarily the monorepo root.
next.config.js
```
module.exports = {
  outputFileTracingExcludes: {
    '/api/hello': ['./un-necessary-folder/**/*'],
  },
  outputFileTracingIncludes: {
    '/api/another': ['./necessary-folder/**/*'],
    '/api/login/\\[\\[\\.\\.\\.slug\\]\\]': [
      './node_modules/aws-crt/dist/bin/**/*',
    ],
  },
}
```

Using a `src/` directory does not change how you write these options:
  * **Keys** still match the route path (`'/api/hello'`, `'/products/[id]'`, etc.).
  * **Values** can reference paths under `src/` since they are resolved relative to the project root.


next.config.js
```
module.exports = {
  outputFileTracingIncludes: {
    '/products/*': ['src/lib/payments/**/*'],
    '/*': ['src/config/runtime/**/*.json'],
  },
  outputFileTracingExcludes: {
    '/api/*': ['src/temp/**/*', 'public/large-logs/**/*'],
  },
}
```

You can also target all routes using a global key like `'/*'`:
next.config.js
```
module.exports = {
  outputFileTracingIncludes: {
    '/*': ['src/i18n/locales/**/*.json'],
  },
}
```

These options are applied to server traces and do not affect routes that do not produce a server trace file:
  * Edge Runtime routes are not affected.
  * Fully static pages are not affected.


In monorepos or when you need to include files outside the app folder, combine `outputFileTracingRoot` with includes:
next.config.js
```
const path = require('path')

module.exports = {
  // Trace from the monorepo root
  outputFileTracingRoot: path.join(__dirname, '../../'),
  outputFileTracingIncludes: {
    '/route1': ['../shared/assets/**/*'],
  },
}
```

> **Good to know** :
>   * Prefer forward slashes (`/`) in patterns for cross-platform compatibility.
>   * Keep patterns as narrow as possible to avoid oversized traces (avoid `**/*` at the repo root).
>

Common include patterns for native/runtime assets:
next.config.js
```
module.exports = {
  outputFileTracingIncludes: {
    '/*': ['node_modules/sharp/**/*', 'node_modules/aws-crt/dist/bin/**/*'],
  },
}
```

[PreviousoptimizePackageImports](https://nextjs.org/docs/app/api-reference/config/next-config-js/optimizePackageImports)[NextpageExtensions](https://nextjs.org/docs/app/api-reference/config/next-config-js/pageExtensions)
Was this helpful?
Send
* * *
* * *
#### Resources
[Docs](https://nextjs.org/docs)[Support Policy](https://nextjs.org/support-policy)[Learn](https://nextjs.org/learn)[Showcase](https://nextjs.org/showcase)[Blog](https://nextjs.org/blog)[Team](https://nextjs.org/team)[Next.js Conf](https://nextjs.org/conf)[Evals](https://nextjs.org/evals)
#### More
[Telemetry](https://nextjs.org/telemetry)[Governance](https://nextjs.org/governance)
#### About Vercel
#### Legal
Cookie Preferences
#### Subscribe to our newsletter
Stay updated on new releases and features, guides, and case studies.
Subscribe
© 2026 Vercel, Inc.
* * *
* * *
