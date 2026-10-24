## Client-side Router Cache[](https://nextjs.org/docs/app/guides/caching#client-side-router-cache)
Next.js has an in-memory client-side router cache that stores the RSC payload of route segments, split by layouts, loading states, and pages.
When a user navigates between routes, Next.js caches the visited route segments and [prefetches](https://nextjs.org/docs/app/getting-started/linking-and-navigating#prefetching) the routes the user is likely to navigate to. This results in instant back/forward navigation, no full-page reload between navigations, and preservation of browser state and React state in shared layouts.
With the Router Cache:
  * **Layouts** are cached and reused on navigation ([partial rendering](https://nextjs.org/docs/app/getting-started/linking-and-navigating#client-side-transitions)).
  * **Loading states** are cached and reused on navigation for [instant navigation](https://nextjs.org/docs/app/api-reference/file-conventions/loading#instant-loading-states).
  * **Pages** are not cached by default, but are reused during browser backward and forward navigation. You can enable caching for page segments by using the experimental [`staleTimes`](https://nextjs.org/docs/app/api-reference/config/next-config-js/staleTimes) config option.


> **Good to know:** This cache specifically applies to Next.js and Server Components, and is different to the browser's
### Duration[](https://nextjs.org/docs/app/guides/caching#duration-3)
The cache is stored in the browser's temporary memory. Two factors determine how long the router cache lasts:
  * **Session** : The cache persists across navigation. However, it's cleared on page refresh.
  * **Automatic Invalidation Period** : The cache of layouts and loading states is automatically invalidated after a specific time. The duration depends on how the resource was [prefetched](https://nextjs.org/docs/app/api-reference/components/link#prefetch), and if the resource was [statically generated](https://nextjs.org/docs/app/guides/caching#static-rendering):
    * **Default Prefetching** (`prefetch={null}` or unspecified): not cached for dynamic pages, 5 minutes for static pages.
    * **Full Prefetching** (`prefetch={true}` or `router.prefetch`): 5 minutes for both static & dynamic pages.


While a page refresh will clear **all** cached segments, the automatic invalidation period only affects the individual segment from the time it was prefetched.
> **Good to know** : The experimental [`staleTimes`](https://nextjs.org/docs/app/api-reference/config/next-config-js/staleTimes) config option can be used to adjust the automatic invalidation times mentioned above.
### Invalidation[](https://nextjs.org/docs/app/guides/caching#invalidation-1)
There are two ways you can invalidate the Router Cache:
  * In a **Server Action** :
    * Revalidating data on-demand by path with ([`revalidatePath`](https://nextjs.org/docs/app/api-reference/functions/revalidatePath)) or by cache tag with ([`revalidateTag`](https://nextjs.org/docs/app/api-reference/functions/revalidateTag))
    * Using [`cookies.set`](https://nextjs.org/docs/app/api-reference/functions/cookies#setting-a-cookie) or [`cookies.delete`](https://nextjs.org/docs/app/api-reference/functions/cookies#deleting-cookies) invalidates the Router Cache to prevent routes that use cookies from becoming stale (e.g. authentication).
  * Calling [`router.refresh`](https://nextjs.org/docs/app/api-reference/functions/use-router) will invalidate the Router Cache and make a new request to the server for the current route.


### Opting out[](https://nextjs.org/docs/app/guides/caching#opting-out-3)
As of Next.js 15, page segments are opted out by default.
> **Good to know:** You can also opt out of [prefetching](https://nextjs.org/docs/app/getting-started/linking-and-navigating#prefetching) by setting the `prefetch` prop of the `<Link>` component to `false`.
