## When does getStaticPaths run[](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-paths#when-does-getstaticpaths-run)
`getStaticPaths` will only run during build in production, it will not be called during runtime. You can validate code written inside `getStaticPaths` is removed from the client-side bundle
### How does getStaticProps run with regards to getStaticPaths[](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-paths#how-does-getstaticprops-run-with-regards-to-getstaticpaths)
  * `getStaticProps` runs during `next build` for any `paths` returned during build
  * `getStaticProps` runs in the background when using `fallback: true`
  * `getStaticProps` is called before initial render when using `fallback: blocking`
