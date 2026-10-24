Menu
Menu
# NEXTJS_MISSING_OPTIMIZE_PACKAGE_IMPORTS
Last updated September 24, 2025
Conformance is available on [Enterprise plans](https://vercel.com/docs/plans/enterprise)
Barrel files make the process of exporting code from a package convenient by allowing all the code to be exported from a single file. This makes it easier to import any part of the package into your application. However, since they export a lot of code from the same file, importing these packages can cause tools to do additional work analyzing files that are unused in the application.
For further reading, see:
  * [How we optimized package imports in Next.js](https://vercel.com/blog/how-we-optimized-package-imports-in-next-js)


As of Next.js 14.2.3, this configuration option is still experimental. Check the Next.js documentation for the latest information here:
##  [How to fix](https://vercel.com/docs/conformance/rules/NEXTJS_MISSING_OPTIMIZE_PACKAGE_IMPORTS#how-to-fix)[](https://vercel.com/docs/conformance/rules/NEXTJS_MISSING_OPTIMIZE_PACKAGE_IMPORTS#how-to-fix)
To fix this, you can add a `modularizeImports` config to `next.config.js` for the package that uses barrel files. For example:
next.config.js
```
experimental: {
  optimizePackageImports: ['@vercel/geistcn/components'];
}
```

* * *
Was this helpful?
Send
