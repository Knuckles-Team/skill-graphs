## Full Route Cache[](https://nextjs.org/docs/app/guides/caching#full-route-cache)
> **Related terms** :
> You may see the terms **Automatic Static Optimization** , **Static Site Generation** , or **Static Rendering** being used interchangeably to refer to the process of rendering and caching routes of your application at build time.
Next.js automatically renders and caches routes at build time. This is an optimization that allows you to serve the cached route instead of rendering on the server for every request, resulting in faster page loads.
To understand how the Full Route Cache works, it's helpful to look at how React handles rendering, and how Next.js caches the result:
### 1. React Rendering on the Server[](https://nextjs.org/docs/app/guides/caching#1-react-rendering-on-the-server)
On the server, Next.js uses React's APIs to orchestrate rendering. The rendering work is split into chunks: by individual routes segments and Suspense boundaries.
Each chunk is rendered in two steps:
  1. React renders Server Components into a special data format, optimized for streaming, called the **React Server Component Payload**.
  2. Next.js uses the React Server Component Payload and Client Component JavaScript instructions to render **HTML** on the server.


This means we don't have to wait for everything to render before caching the work or sending a response. Instead, we can stream a response as work is completed.
> **What is the React Server Component Payload?**
> The React Server Component Payload is a compact binary representation of the rendered React Server Components tree. It's used by React on the client to update the browser's DOM. The React Server Component Payload contains:
>   * The rendered result of Server Components
>   * Placeholders for where Client Components should be rendered and references to their JavaScript files
>   * Any props passed from a Server Component to a Client Component
>

> To learn more, see the [Server Components](https://nextjs.org/docs/app/getting-started/server-and-client-components) documentation.
### 2. Next.js Caching on the Server (Full Route Cache)[](https://nextjs.org/docs/app/guides/caching#2-nextjs-caching-on-the-server-full-route-cache)
![Default behavior of the Full Route Cache, showing how the React Server Component Payload and HTML are cached on the server for statically rendered routes.](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Ffull-route-cache.png&w=3840&q=75)![Default behavior of the Full Route Cache, showing how the React Server Component Payload and HTML are cached on the server for statically rendered routes.](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Ffull-route-cache.png&w=3840&q=75)
The default behavior of Next.js is to cache the rendered result (React Server Component Payload and HTML) of a route on the server. This applies to statically rendered routes at build time, or during revalidation.
### 3. React Hydration and Reconciliation on the Client[](https://nextjs.org/docs/app/guides/caching#3-react-hydration-and-reconciliation-on-the-client)
At request time, on the client:
  1. The HTML is used to immediately show a fast non-interactive initial preview of the Client and Server Components.
  2. The React Server Components Payload is used to reconcile the Client and rendered Server Component trees, and update the DOM.
  3. The JavaScript instructions are used to


### 4. Next.js Caching on the Client (Router Cache)[](https://nextjs.org/docs/app/guides/caching#4-nextjs-caching-on-the-client-router-cache)
The React Server Component Payload is stored in the client-side [Router Cache](https://nextjs.org/docs/app/guides/caching#client-side-router-cache) - a separate in-memory cache, split by individual route segment. This Router Cache is used to improve the navigation experience by storing previously visited routes and prefetching future routes.
### 5. Subsequent Navigations[](https://nextjs.org/docs/app/guides/caching#5-subsequent-navigations)
On subsequent navigations or during prefetching, Next.js will check if the React Server Components Payload is stored in the Router Cache. If so, it will skip sending a new request to the server.
If the route segments are not in the cache, Next.js will fetch the React Server Components Payload from the server, and populate the Router Cache on the client.
### Static and Dynamic Rendering[](https://nextjs.org/docs/app/guides/caching#static-and-dynamic-rendering)
Whether a route is cached or not at build time depends on whether it's statically or dynamically rendered. Static routes are cached by default, whereas dynamic routes are rendered at request time, and not cached.
This diagram shows the difference between statically and dynamically rendered routes, with cached and uncached data:
![How static and dynamic rendering affects the Full Route Cache. Static routes are cached at build time or after data revalidation, whereas dynamic routes are never cached](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Fstatic-and-dynamic-routes.png&w=3840&q=75)![How static and dynamic rendering affects the Full Route Cache. Static routes are cached at build time or after data revalidation, whereas dynamic routes are never cached](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Fstatic-and-dynamic-routes.png&w=3840&q=75)
Learn more about [static and dynamic rendering](https://nextjs.org/docs/app/guides/caching#rendering-strategies).
### Duration[](https://nextjs.org/docs/app/guides/caching#duration-2)
By default, the Full Route Cache is persistent. This means that the render output is cached across user requests.
### Invalidation[](https://nextjs.org/docs/app/guides/caching#invalidation)
There are two ways you can invalidate the Full Route Cache:
  * **[Revalidating Data](https://nextjs.org/docs/app/guides/caching#revalidating)** : Revalidating the [Data Cache](https://nextjs.org/docs/app/guides/caching#data-cache), will in turn invalidate the Router Cache by re-rendering components on the server and caching the new render output.
  * **Redeploying** : Unlike the Data Cache, which persists across deployments, the Full Route Cache is cleared on new deployments.


### Opting out[](https://nextjs.org/docs/app/guides/caching#opting-out-2)
You can opt out of the Full Route Cache, or in other words, dynamically render components for every incoming request, by:
  * **Using a[Dynamic API](https://nextjs.org/docs/app/guides/caching#dynamic-apis)**: This will opt the route out from the Full Route Cache and dynamically render it at request time. The Data Cache can still be used.
  * **Using the`dynamic = 'force-dynamic'` or `revalidate = 0` route segment config options**: This will skip the Full Route Cache and the Data Cache. Meaning components will be rendered and data fetched on every incoming request to the server. The Router Cache will still apply as it's a client-side cache.
  * **Opting out of the[Data Cache](https://nextjs.org/docs/app/guides/caching#data-cache)**: If a route has a `fetch` request that is not cached, this will opt the route out of the Full Route Cache. The data for the specific `fetch` request will be fetched for every incoming request. Other `fetch` requests that explicitly enable caching will still be cached in the Data Cache. This allows for a hybrid of cached and uncached data.
