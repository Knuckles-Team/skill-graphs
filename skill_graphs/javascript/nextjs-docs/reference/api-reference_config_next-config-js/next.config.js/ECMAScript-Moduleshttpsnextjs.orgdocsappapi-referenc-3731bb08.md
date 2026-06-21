## ECMAScript Modules[](https://nextjs.org/docs/app/api-reference/config/next-config-js#ecmascript-modules)
`next.config.js` is a regular Node.js module, not a JSON file. It gets used by the Next.js server and build phases, and it's not included in the browser build.
If you need `next.config.mjs`:
next.config.mjs
```
// @ts-check

/**
 * @type {import('next').NextConfig}
 */
const nextConfig = {
  /* config options here */
}

export default nextConfig
```

> **Good to know** : `next.config` with the `.cjs` or `.cts` extensions are currently **not** supported.
