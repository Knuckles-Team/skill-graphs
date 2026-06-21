## Default Spans in Next.js[](https://nextjs.org/docs/app/guides/open-telemetry#default-spans-in-nextjs)
Next.js automatically instruments several spans for you to provide useful insights into your application's performance.
Attributes on spans follow `next` namespace:
  * `next.span_name` - duplicates span name
  * `next.span_type` - each span type has a unique identifier
  * `next.route` - The route pattern of the request (e.g., `/[param]/user`).
  * `next.rsc` (true/false) - Whether the request is an RSC request, such as prefetch.
  * `next.page`
    * This is an internal value used by an app router.
    * You can think about it as a route to a special file (like `page.ts`, `layout.ts`, `loading.ts` and others)
    * It can be used as a unique identifier only when paired with `next.route` because `/layout` can be used to identify both `/(groupA)/layout.ts` and `/(groupB)/layout.ts`


###  `[http.method] [next.route]`[](https://nextjs.org/docs/app/guides/open-telemetry#httpmethod-nextroute)
  * `next.span_type`: `BaseServer.handleRequest`


This span represents the root span for each incoming request to your Next.js application. It tracks the HTTP method, route, target, and status code of the request.
Attributes:
  *     * `http.method`
    * `http.status_code`
  *     * `http.route`
    * `http.target`
  * `next.span_name`
  * `next.span_type`
  * `next.route`


###  `render route (app) [next.route]`[](https://nextjs.org/docs/app/guides/open-telemetry#render-route-app-nextroute)
  * `next.span_type`: `AppRender.getBodyResult`.


This span represents the process of rendering a route in the app router.
Attributes:
  * `next.span_name`
  * `next.span_type`
  * `next.route`


###  `fetch [http.method] [http.url]`[](https://nextjs.org/docs/app/guides/open-telemetry#fetch-httpmethod-httpurl)
  * `next.span_type`: `AppRender.fetch`


This span represents the fetch request executed in your code.
Attributes:
  *     * `http.method`
  *     * `http.url`
    * `net.peer.name`
    * `net.peer.port` (only if specified)
  * `next.span_name`
  * `next.span_type`


This span can be turned off by setting `NEXT_OTEL_FETCH_DISABLED=1` in your environment. This is useful when you want to use a custom fetch instrumentation library.
###  `executing api route (app) [next.route]`[](https://nextjs.org/docs/app/guides/open-telemetry#executing-api-route-app-nextroute)
  * `next.span_type`: `AppRouteRouteHandlers.runHandler`.


This span represents the execution of an API Route Handler in the app router.
Attributes:
  * `next.span_name`
  * `next.span_type`
  * `next.route`


###  `getServerSideProps [next.route]`[](https://nextjs.org/docs/app/guides/open-telemetry#getserversideprops-nextroute)
  * `next.span_type`: `Render.getServerSideProps`.


This span represents the execution of `getServerSideProps` for a specific route.
Attributes:
  * `next.span_name`
  * `next.span_type`
  * `next.route`


###  `getStaticProps [next.route]`[](https://nextjs.org/docs/app/guides/open-telemetry#getstaticprops-nextroute)
  * `next.span_type`: `Render.getStaticProps`.


This span represents the execution of `getStaticProps` for a specific route.
Attributes:
  * `next.span_name`
  * `next.span_type`
  * `next.route`


###  `render route (pages) [next.route]`[](https://nextjs.org/docs/app/guides/open-telemetry#render-route-pages-nextroute)
  * `next.span_type`: `Render.renderDocument`.


This span represents the process of rendering the document for a specific route.
Attributes:
  * `next.span_name`
  * `next.span_type`
  * `next.route`


###  `generateMetadata [next.page]`[](https://nextjs.org/docs/app/guides/open-telemetry#generatemetadata-nextpage)
  * `next.span_type`: `ResolveMetadata.generateMetadata`.


This span represents the process of generating metadata for a specific page (a single route can have multiple of these spans).
Attributes:
  * `next.span_name`
  * `next.span_type`
  * `next.page`


###  `resolve page components`[](https://nextjs.org/docs/app/guides/open-telemetry#resolve-page-components)
  * `next.span_type`: `NextNodeServer.findPageComponents`.


This span represents the process of resolving page components for a specific page.
Attributes:
  * `next.span_name`
  * `next.span_type`
  * `next.route`


###  `resolve segment modules`[](https://nextjs.org/docs/app/guides/open-telemetry#resolve-segment-modules)
  * `next.span_type`: `NextNodeServer.getLayoutOrPageModule`.


This span represents loading of code modules for a layout or a page.
Attributes:
  * `next.span_name`
  * `next.span_type`
  * `next.segment`


###  `start response`[](https://nextjs.org/docs/app/guides/open-telemetry#start-response)
  * `next.span_type`: `NextNodeServer.startResponse`.


This zero-length span represents the time when the first byte has been sent in the response.
[PreviousMulti-zones](https://nextjs.org/docs/app/guides/multi-zones)[NextPackage Bundling](https://nextjs.org/docs/app/guides/package-bundling)
Was this helpful?
Send
* * *
* * *
#### Resources
[Docs](https://nextjs.org/docs)[Support Policy](https://nextjs.org/support-policy)[Learn](https://nextjs.org/learn)[Showcase](https://nextjs.org/showcase)[Blog](https://nextjs.org/blog)[Team](https://nextjs.org/team)[Next.js Conf](https://nextjs.org/conf)[Evals](https://nextjs.org/evals)
#### More
[Telemetry](https://nextjs.org/telemetry)[Governance](https://nextjs.org/governance)
#### About Vercel
#### Legal
Cookie Preferences
#### Subscribe to our newsletter
Stay updated on new releases and features, guides, and case studies.
Subscribe
© 2026 Vercel, Inc.
* * *
* * *
