##  [bunVersion](https://vercel.com/docs/project-configuration/vercel-json#bunversion)[](https://vercel.com/docs/project-configuration/vercel-json#bunversion)
The Bun runtime is available in [Beta](https://vercel.com/docs/release-phases#beta) on [all plans](https://vercel.com/docs/plans)
Type: `string`
Value: `"1.x"`
The `bunVersion` property configures your project to use the Bun runtime instead of Node.js. When set, all [Vercel Functions](https://vercel.com/docs/functions) and [Routing Middleware](https://vercel.com/docs/routing-middleware) not using the [Edge runtime](https://vercel.com/docs/functions/runtimes/edge) will run using the specified Bun version.
vercel.json
```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "bunVersion": "1.x"
}
```

Vercel manages the Bun minor and patch versions automatically. `1.x` is the only valid value currently.
When using Next.js with [ISR](https://vercel.com/docs/incremental-static-regeneration) (Incremental Static Regeneration), you must also update your `build` and `dev` commands in `package.json`:
package.json
```
{
  "scripts": {
    "dev": "bun run --bun next dev",
    "build": "bun run --bun next build"
  }
}
```

To learn more about using Bun with Vercel Functions, see the [Bun runtime documentation](https://vercel.com/docs/functions/runtimes/bun).
