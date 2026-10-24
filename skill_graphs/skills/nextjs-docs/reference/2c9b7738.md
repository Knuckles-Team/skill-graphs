## How it works[](https://nextjs.org/docs/pages/building-your-application/rendering/automatic-static-optimization#how-it-works)
If `getServerSideProps` or `getInitialProps` is present in a page, Next.js will switch to render the page on-demand, per-request (meaning [Server-Side Rendering](https://nextjs.org/docs/pages/building-your-application/rendering/server-side-rendering)).
If the above is not the case, Next.js will **statically optimize** your page automatically by prerendering the page to static HTML.
During prerendering, the router's `query` object will be empty since we do not have `query` information to provide during this phase. After hydration, Next.js will trigger an update to your application to provide the route parameters in the `query` object.
The cases where the query will be updated after hydration triggering another render are:
  * The page is a [dynamic-route](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes).
  * The page has query values in the URL.
  * [Rewrites](https://nextjs.org/docs/pages/api-reference/config/next-config-js/rewrites) are configured in your `next.config.js` since these can have parameters that may need to be parsed and provided in the `query`.


To be able to distinguish if the query is fully updated and ready for use, you can leverage the `isReady` field on [`next/router`](https://nextjs.org/docs/pages/api-reference/functions/use-router#router-object).
> **Good to know** : Parameters added with [dynamic routes](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes) to a page that's using [`getStaticProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props) will always be available inside the `query` object.
`next build` will emit `.html` files for statically optimized pages. For example, the result for the page `pages/about.js` would be:
Terminal
```
.next/server/pages/about.html
```

And if you add `getServerSideProps` to the page, it will then be JavaScript, like so:
Terminal
```
.next/server/pages/about.js
```
