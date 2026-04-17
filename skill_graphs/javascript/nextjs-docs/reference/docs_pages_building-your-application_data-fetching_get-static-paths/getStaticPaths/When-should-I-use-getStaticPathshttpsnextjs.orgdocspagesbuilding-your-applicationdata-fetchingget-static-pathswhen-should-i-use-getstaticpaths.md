## When should I use getStaticPaths?[](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-paths#when-should-i-use-getstaticpaths)
You should use `getStaticPaths` if you’re statically pre-rendering pages that use dynamic routes and:
  * The data comes from a headless CMS
  * The data comes from a database
  * The data comes from the filesystem
  * The data can be publicly cached (not user-specific)
  * The page must be pre-rendered (for SEO) and be very fast — `getStaticProps` generates `HTML` and `JSON` files, both of which can be cached by a CDN for performance
