# How to optimize package bundling
Last updated February 27, 2026
Bundling is the process of combining your application code and its dependencies into optimized output files for the client and server. Smaller bundles load faster, reduce JavaScript execution time, improve
Next.js automatically optimizes bundles by code splitting, tree-shaking, and other techniques. However, there are some cases where you may need to optimize your bundles manually.
There are two tools for analyzing your application's bundles:
  * [Next.js Bundle Analyzer for Turbopack (experimental)](https://nextjs.org/docs/pages/guides/package-bundling#nextjs-bundle-analyzer-experimental)
  * [`@next/bundle-analyzer` plugin for Webpack](https://nextjs.org/docs/pages/guides/package-bundling#nextbundle-analyzer-for-webpack)


This guide will walk you through how to use each tool and how to [optimize large bundles](https://nextjs.org/docs/pages/guides/package-bundling#optimizing-large-bundles).
