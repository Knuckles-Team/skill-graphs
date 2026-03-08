## Next.js Bundle Analyzer (Experimental)[](https://nextjs.org/docs/pages/guides/package-bundling#nextjs-bundle-analyzer-experimental)
> Available in v16.1 and later. You can share feedback in the
The Next.js Bundle Analyzer is integrated with Turbopack's module graph. You can inspect server and client modules with precise import tracing, making it easier to find large dependencies. Open the interactive Bundle Analyzer demo to explore the module graph.
### Step 1: Run the Turbopack Bundle Analyzer[](https://nextjs.org/docs/pages/guides/package-bundling#step-1-run-the-turbopack-bundle-analyzer)
To get started, run the following command and open up the interactive view in your browser.
pnpmnpmyarnbun
Terminal
```
pnpm next experimental-analyze
```

### Step 2: Filter and inspect modules[](https://nextjs.org/docs/pages/guides/package-bundling#step-2-filter-and-inspect-modules)
Within the UI, you can filter by route, environment (client or server), and type (JavaScript, CSS, JSON), or search by file:
Next.js bundle analyzer UI walkthrough
### Step 3: Trace modules with import chains[](https://nextjs.org/docs/pages/guides/package-bundling#step-3-trace-modules-with-import-chains)
The treemap shows each module as a rectangle. Where the size of the module is represented by the area of the rectangle.
Click a module to see its size, inspect its full import chain and see exactly where it’s used in your application:
![Next.js Bundle Analyzer import chain view](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Fbundle-analyzer.png&w=3840&q=75)![Next.js Bundle Analyzer import chain view](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Fbundle-analyzer.png&w=3840&q=75)Next.js Bundle Analyzer import chain view
### Step 4: Write output to disk for sharing or diffing[](https://nextjs.org/docs/pages/guides/package-bundling#step-4-write-output-to-disk-for-sharing-or-diffing)
If you want to share the analysis with teammates or compare bundle sizes before/after optimizations, you can skip the interactive view and save the analysis as a static file with the `--output` flag:
pnpmnpmyarnbun
Terminal
```
pnpm next experimental-analyze --output
```

This command writes the output to `.next/diagnostics/analyze`. You can copy this directory elsewhere to compare results:
Terminal
```
cp -r .next/diagnostics/analyze ./analyze-before-refactor
```

> More options are available for the Bundle Analyzer, see Next.js CLI reference docs for the full list.
