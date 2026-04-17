# NEXTJS_SAFE_URL_IMPORTS
Last updated March 4, 2025
Conformance is available on [Enterprise plans](https://vercel.com/docs/plans/enterprise)
URL imports are an experimental feature that allows you to import modules directly from external servers (instead of from the local disk). When you opt-in, and supply URL prefixes inside `next.config.js`, like so:
next.config.js
```
module.exports = {
  experimental: {
    urlImports: ['https://example.com/assets/', 'https://cdn.skypack.dev'],
  },
};
```

If any of the URLs have not been added to the safe import conformance configuration, then this will cause this rule to fail.
