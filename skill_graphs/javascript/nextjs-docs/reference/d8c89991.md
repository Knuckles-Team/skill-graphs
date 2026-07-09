## Troubleshooting[](https://nextjs.org/docs/app/api-reference/config/next-config-js/devIndicators#troubleshooting)
### Indicator not marking a route as static[](https://nextjs.org/docs/app/api-reference/config/next-config-js/devIndicators#indicator-not-marking-a-route-as-static)
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

There are two reasons a route might opt out of static rendering:
  * The presence of [Dynamic APIs](https://nextjs.org/docs/app/guides/caching#dynamic-rendering) which rely on runtime information.
  * An [uncached data request](https://nextjs.org/docs/app/getting-started/fetching-data), like a call to an ORM or database driver.


Check your route for any of these conditions, and if you are not able to statically render the route, then consider using [`loading.js`](https://nextjs.org/docs/app/api-reference/file-conventions/loading) or [streaming](https://nextjs.org/docs/app/getting-started/linking-and-navigating#streaming).
