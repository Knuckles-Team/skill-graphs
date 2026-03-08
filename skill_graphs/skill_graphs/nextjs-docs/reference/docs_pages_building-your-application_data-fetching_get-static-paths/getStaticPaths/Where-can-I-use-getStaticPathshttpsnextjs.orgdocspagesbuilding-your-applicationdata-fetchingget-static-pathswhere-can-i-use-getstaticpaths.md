## Where can I use getStaticPaths[](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-paths#where-can-i-use-getstaticpaths)
  * `getStaticPaths` **must** be used with `getStaticProps`
  * You **cannot** use `getStaticPaths` with [`getServerSideProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props)
  * You can export `getStaticPaths` from a [Dynamic Route](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes) that also uses `getStaticProps`
  * You **cannot** export `getStaticPaths` from non-page file (e.g. your `components` folder)
  * You must export `getStaticPaths` as a standalone function, and not a property of the page component
