## Troubleshooting[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/devIndicators#troubleshooting)
### Indicator not marking a route as static[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/devIndicators#indicator-not-marking-a-route-as-static)
If you expect a route to be static and the indicator has marked it as dynamic, it's likely the route has opted out of static rendering.
You can confirm if a route is [static](https://nextjs.org/docs/app/guides/caching#static-rendering) or [dynamic](https://nextjs.org/docs/app/guides/caching#dynamic-rendering) by building your application using `next build --debug`, and checking the output in your terminal. Static (or prerendered) routes will display a `○` symbol, whereas dynamic routes will display a `ƒ` symbol. For example:
Build Output
```
Route (app)
┌ ○ /_not-found
└ ƒ /products/[id]

○  (Static)   prerendered as static content
ƒ  (Dynamic)  server-rendered on demand
```

When exporting [`getServerSideProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props) or [`getInitialProps`](https://nextjs.org/docs/pages/api-reference/functions/get-initial-props) from a page, it will be marked as dynamic.
