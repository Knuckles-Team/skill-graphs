##  `@next/bundle-analyzer` for Webpack[](https://nextjs.org/docs/app/guides/package-bundling#nextbundle-analyzer-for-webpack)
The [lazy-load](https://nextjs.org/docs/app/guides/lazy-loading) your code.
### Step 1: Installation[](https://nextjs.org/docs/app/guides/package-bundling#step-1-installation)
Install the plugin by running the following command:
pnpmnpmyarnbun
Terminal
```
pnpm add @next/bundle-analyzer
```

Then, add the bundle analyzer's settings to your `next.config.js`.
next.config.js
```
/** @type {import('next').NextConfig} */
const nextConfig = {}

const withBundleAnalyzer = require('@next/bundle-analyzer')({
  enabled: process.env.ANALYZE === 'true',
})

module.exports = withBundleAnalyzer(nextConfig)
```

### Step 2: Generating a report[](https://nextjs.org/docs/app/guides/package-bundling#step-2-generating-a-report)
Run the following command to analyze your bundles:
```
ANALYZE=true npm run build
# or
ANALYZE=true yarn build
# or
ANALYZE=true pnpm build
```

The report will open three new tabs in your browser, which you can inspect.
