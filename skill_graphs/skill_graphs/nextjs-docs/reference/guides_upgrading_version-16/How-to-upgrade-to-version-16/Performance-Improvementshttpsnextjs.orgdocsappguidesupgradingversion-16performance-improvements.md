## Performance Improvements[](https://nextjs.org/docs/app/guides/upgrading/version-16#performance-improvements)
Significant performance optimizations for `next dev` and `next start` commands, along with improved terminal output with clearer formatting, better error messages, and improved performance metrics.
**Next.js 16** removes the `size` and `First Load JS` metrics from the `next build` output. We found these to be inaccurate in server-driven architectures using React Server Components. Both our Turbopack and Webpack implementations had issues, and disagreed on how to account for Client Components payload.
The most effective way to measure actual route performance is through tools such as
###  `next dev` config load[](https://nextjs.org/docs/app/guides/upgrading/version-16#next-dev-config-load)
In previous versions the Next config file was loaded twice during development:
  * When running the `next dev` command
  * When the `next dev` command started the Next.js server


This was inefficient because the `next dev` command doesn't need the config file to start the Next.js server.
A consequence of this change is that, when running `next dev` checking if `process.argv` includes `'dev'`, in your Next.js config file, will return `false`.
> **Good to know** : The `typegen`, and `build` commands, are still visible in `process.argv`.
This is specially important for plugins that trigger side-effects on `next dev`. If that's the case, it might be enough to check if `NODE_ENV` is set to `development`.
next.config.js
```
import { startServer } from 'docs-lib/dev-server'

const isDev = process.env.NODE_ENV === 'development'

if (isDev) {
  startServer()
}

const nextConfig = {
  /* Your config options */
}

module.exports = nextConfig
```

Alternatively, use the [`phase`](https://nextjs.org/docs/app/api-reference/config/next-config-js#phase) in which the configuration is loaded.
