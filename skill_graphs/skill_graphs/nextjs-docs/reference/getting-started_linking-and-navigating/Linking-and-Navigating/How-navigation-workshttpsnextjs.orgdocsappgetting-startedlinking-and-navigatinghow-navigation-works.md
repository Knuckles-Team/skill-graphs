## How navigation works[](https://nextjs.org/docs/app/getting-started/linking-and-navigating#how-navigation-works)
To understand how navigation works in Next.js, it helps to be familiar with the following concepts:
  * [Server Rendering](https://nextjs.org/docs/app/getting-started/linking-and-navigating#server-rendering)
  * [Prefetching](https://nextjs.org/docs/app/getting-started/linking-and-navigating#prefetching)
  * [Streaming](https://nextjs.org/docs/app/getting-started/linking-and-navigating#streaming)
  * [Client-side transitions](https://nextjs.org/docs/app/getting-started/linking-and-navigating#client-side-transitions)


### Server Rendering[](https://nextjs.org/docs/app/getting-started/linking-and-navigating#server-rendering)
In Next.js, [Layouts and Pages](https://nextjs.org/docs/app/getting-started/layouts-and-pages) are [Server Component Payload](https://nextjs.org/docs/app/getting-started/server-and-client-components#how-do-server-and-client-components-work-in-nextjs) is generated on the server before being sent to the client.
There are two types of server rendering, based on _when_ it happens:
  * **Static Rendering (or Prerendering)** happens at build time or during [revalidation](https://nextjs.org/docs/app/getting-started/caching-and-revalidating) and the result is cached.
  * **Dynamic Rendering** happens at request time in response to a client request.


The trade-off of server rendering is that the client must wait for the server to respond before the new route can be shown. Next.js addresses this delay by [prefetching](https://nextjs.org/docs/app/getting-started/linking-and-navigating#prefetching) routes the user is likely to visit and performing [client-side transitions](https://nextjs.org/docs/app/getting-started/linking-and-navigating#client-side-transitions).
> **Good to know** : HTML is also generated for the initial visit.
### Prefetching[](https://nextjs.org/docs/app/getting-started/linking-and-navigating#prefetching)
Prefetching is the process of loading a route in the background before the user navigates to it. This makes navigation between routes in your application feel instant, because by the time a user clicks on a link, the data to render the next route is already available client side.
Next.js automatically prefetches routes linked with the [`<Link>` component](https://nextjs.org/docs/app/api-reference/components/link) when they enter the user's viewport.
app/layout.tsx
TypeScript
JavaScript TypeScript
```
import Link from 'next/link'

export default function Layout({ children }: { children: React.ReactNode }) {
  return (
    <html>
      <body>
        <nav>
          {/* Prefetched when the link is hovered or enters the viewport */}
          <Link href="/blog">Blog</Link>
          {/* No prefetching */}
          <a href="/contact">Contact</a>
        </nav>
        {children}
      </body>
    </html>
  )
}
```

How much of the route is prefetched depends on whether it's static or dynamic:
  * **Static Route** : the full route is prefetched.
  * **Dynamic Route** : prefetching is skipped, or the route is partially prefetched if [`loading.tsx`](https://nextjs.org/docs/app/api-reference/file-conventions/loading) is present.


By skipping or partially prefetching dynamic routes, Next.js avoids unnecessary work on the server for routes the users may never visit. However, waiting for a server response before navigation can give the users the impression that the app is not responding.
![Server Rendering without Streaming](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Fserver-rendering-without-streaming.png&w=3840&q=75)![Server Rendering without Streaming](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Fserver-rendering-without-streaming.png&w=3840&q=75)
To improve the navigation experience to dynamic routes, you can use [streaming](https://nextjs.org/docs/app/getting-started/linking-and-navigating#streaming).
### Streaming[](https://nextjs.org/docs/app/getting-started/linking-and-navigating#streaming)
Streaming allows the server to send parts of a dynamic route to the client as soon as they're ready, rather than waiting for the entire route to be rendered. This means users see something sooner, even if parts of the page are still loading.
For dynamic routes, it means they can be **partially prefetched**. That is, shared layouts and loading skeletons can be requested ahead of time.
![How Server Rendering with Streaming Works](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Fserver-rendering-with-streaming.png&w=3840&q=75)![How Server Rendering with Streaming Works](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Fserver-rendering-with-streaming.png&w=3840&q=75)
To use streaming, create a `loading.tsx` in your route folder:
![loading.js special file](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Floading-special-file.png&w=3840&q=75)![loading.js special file](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Floading-special-file.png&w=3840&q=75)
app/dashboard/loading.tsx
TypeScript
JavaScript TypeScript
```
export default function Loading() {
  // Add fallback UI that will be shown while the route is loading.
  return <LoadingSkeleton />
}
```

Behind the scenes, Next.js will automatically wrap the `page.tsx` contents in a `<Suspense>` boundary. The prefetched fallback UI will be shown while the route is loading, and swapped for the actual content once ready.
> **Good to know** : You can also use
Benefits of `loading.tsx`:
  * Immediate navigation and visual feedback for the user.
  * Shared layouts remain interactive and navigation is interruptible.
  * Improved Core Web Vitals:


To further improve the navigation experience, Next.js performs a [client-side transition](https://nextjs.org/docs/app/getting-started/linking-and-navigating#client-side-transitions) with the `<Link>` component.
### Client-side transitions[](https://nextjs.org/docs/app/getting-started/linking-and-navigating#client-side-transitions)
Traditionally, navigation to a server-rendered page triggers a full page load. This clears state, resets scroll position, and blocks interactivity.
Next.js avoids this with client-side transitions using the `<Link>` component. Instead of reloading the page, it updates the content dynamically by:
  * Keeping any shared layouts and UI.
  * Replacing the current page with the prefetched loading state or a new page if available.


Client-side transitions are what makes a server-rendered apps _feel_ like client-rendered apps. And when paired with [prefetching](https://nextjs.org/docs/app/getting-started/linking-and-navigating#prefetching) and [streaming](https://nextjs.org/docs/app/getting-started/linking-and-navigating#streaming), it enables fast transitions, even for dynamic routes.
Next.js also handles [scrolling to the top of the page](https://nextjs.org/docs/app/api-reference/components/link#scroll) during client-side transitions. If content scrolls behind a sticky or fixed header after navigation, you can fix this with CSS [`scroll-padding-top`](https://nextjs.org/docs/app/api-reference/components/link#scroll-offset-with-sticky-headers).
