## Turbopack by default[](https://nextjs.org/docs/app/guides/upgrading/version-16#turbopack-by-default)
Starting with **Next.js 16** , Turbopack is stable and used by default with `next dev` and `next build`
Previously you had to enable Turbopack using `--turbopack`, or `--turbo`.
package.json
```
{
  "scripts": {
    "dev": "next dev --turbopack",
    "build": "next build --turbopack",
    "start": "next start"
  }
}
```

This is no longer necessary. You can update your `package.json` scripts:
package.json
```
{
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start"
  }
}
```

If your project has a [custom `webpack`](https://nextjs.org/docs/app/api-reference/config/next-config-js/webpack) configuration and you run `next build` (which now uses Turbopack by default), the build will **fail** to prevent misconfiguration issues.
You have a few different ways to address this:
  * **Use Turbopack anyway:** Run with `next build --turbopack` to build using Turbopack and ignore your `webpack` config.
  * **Switch to Turbopack fully:** Migrate your `webpack` config to Turbopack-compatible options.
  * **Keep using Webpack:** Use the `--webpack` flag to opt out of Turbopack and build with Webpack.


> **Good to know** : If you see failing builds because a `webpack` configuration was found, but you don't define one yourself, it is likely that a plugin is adding a `webpack` option
### Opting out of Turbopack[](https://nextjs.org/docs/app/guides/upgrading/version-16#opting-out-of-turbopack)
If you need to continue using Webpack, you can opt out with the `--webpack` flag. For example, to use Turbopack in development but Webpack for production builds:
package.json
```
{
  "scripts": {
    "dev": "next dev",
    "build": "next build --webpack",
    "start": "next start"
  }
}
```

We recommend using Turbopack for development and production. Submit a comment to this
### Turbopack configuration location[](https://nextjs.org/docs/app/guides/upgrading/version-16#turbopack-configuration-location)
The `experimental.turbopack` configuration is out of experimental.
next.config.ts
```
import type { NextConfig } from 'next'

// Next.js 15 - experimental.turbopack
const nextConfig: NextConfig = {
  experimental: {
    turbopack: {
      // options
    },
  },
}

export default nextConfig
```

You can use it as a top-level `turbopack` option:
next.config.ts
```
import type { NextConfig } from 'next'

// Next.js 16 - turbopack at the top level of nextConfig
const nextConfig: NextConfig = {
  turbopack: {
    // options
  },
}

export default nextConfig
```

Make sure to review the `Turbopack` configuration [options](https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopack). **Next.js 16** introduces various improvements and new options, for example:
  * [Advanced Webpack loader conditions](https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopack#advanced-webpack-loader-conditions)
  * [debugIds](https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopack#debug-ids)


### Resolve alias fallback[](https://nextjs.org/docs/app/guides/upgrading/version-16#resolve-alias-fallback)
In some projects, client-side code may import files containing Node.js native modules. This will cause `Module not found: Can't resolve 'fs'` type of errors.
When this happens, you should refactor your code so that your client-side bundles do not reference these Node.js native modules.
However, in some cases, this might not be possible. In Webpack the `resolve.fallback` option was typically used to **silence** the error. Turbopack offers a similar option, using `turbopack.resolveAlias`. In this case, tell Turbopack to load an empty module when `fs` is requested for the browser.
next.config.ts
```
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  turbopack: {
    resolveAlias: {
      fs: {
        browser: './empty.ts', // We recommend to fix code imports before using this method
      },
    },
  },
}

export default nextConfig
```

It is preferable to refactor your modules so that client code doesn't ever import from modules using Node.js native modules.
### Sass node_modules imports[](https://nextjs.org/docs/app/guides/upgrading/version-16#sass-node_modules-imports)
Turbopack fully supports importing Sass files from `node_modules`. Note that while Webpack allowed the legacy tilde (`~`) prefix, Turbopack does not support this syntax.
In Webpack:
styles/globals.scss
```
@import '~bootstrap/dist/css/bootstrap.min.css';
```

In Turbopack:
styles/globals.scss
```
@import 'bootstrap/dist/css/bootstrap.min.css';
```

If changing the imports is not possible, you can use `turbopack.resolveAlias`. For example:
next.config.ts
```
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  turbopack: {
    resolveAlias: {
      '~*': '*',
    },
  },
}

export default nextConfig
```

### Turbopack File System Caching (beta)[](https://nextjs.org/docs/app/guides/upgrading/version-16#turbopack-file-system-caching-beta)
Turbopack now supports filesystem caching in development, storing compiler artifacts on disk between runs for significantly faster compile times across restarts.
Enable filesystem caching in your configuration:
next.config.ts
TypeScript
JavaScript TypeScript
```
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  experimental: {
    turbopackFileSystemCacheForDev: true,
  },
}

export default nextConfig
```
