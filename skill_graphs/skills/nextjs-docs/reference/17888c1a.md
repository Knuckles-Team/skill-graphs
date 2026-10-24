## Reference[](https://nextjs.org/docs/app/api-reference/components/link#reference)
The following props can be passed to the `<Link>` component:
Prop | Example | Type | Required
---|---|---|---
[`href`](https://nextjs.org/docs/app/api-reference/components/link#href-required) | `href="/dashboard"` | String or Object | Yes
[`replace`](https://nextjs.org/docs/app/api-reference/components/link#replace) | `replace={false}` | Boolean | -
[`scroll`](https://nextjs.org/docs/app/api-reference/components/link#scroll) | `scroll={false}` | Boolean | -
[`prefetch`](https://nextjs.org/docs/app/api-reference/components/link#prefetch) | `prefetch={false}` | Boolean or null | -
[`onNavigate`](https://nextjs.org/docs/app/api-reference/components/link#onnavigate) | `onNavigate={(e) => {}}` | Function | -
> **Good to know** : `<a>` tag attributes such as `className` or `target="_blank"` can be added to `<Link>` as props and will be passed to the underlying `<a>` element.
###  `href` (required)[](https://nextjs.org/docs/app/api-reference/components/link#href-required)
The path or URL to navigate to.
app/page.tsx
TypeScript
JavaScript TypeScript
```
import Link from 'next/link'

// Navigate to /about?name=test
export default function Page() {
  return (
    <Link
      href={{
        pathname: '/about',
        query: { name: 'test' },
      }}
    >
      About
    </Link>
  )
}
```

###  `replace`[](https://nextjs.org/docs/app/api-reference/components/link#replace)
**Defaults to`false`.** When `true`, `next/link` will replace the current history state instead of adding a new URL into the
app/page.tsx
TypeScript
JavaScript TypeScript
```
import Link from 'next/link'

export default function Page() {
  return (
    <Link href="/dashboard" replace>
      Dashboard
    </Link>
  )
}
```

###  `scroll`[](https://nextjs.org/docs/app/api-reference/components/link#scroll)
**Defaults to`true`.** The default scrolling behavior of `<Link>` in Next.js **is to maintain scroll position** , similar to how browsers handle back and forwards navigation. When you navigate to a new [Page](https://nextjs.org/docs/app/api-reference/file-conventions/page), scroll position will stay the same as long as the Page is visible in the viewport. However, if the Page is not visible in the viewport, Next.js will scroll to the top of the first Page element.
When `scroll = {false}`, Next.js will not attempt to scroll to the first Page element.
> **Good to know** : Next.js checks if `scroll: false` before managing scroll behavior. If scrolling is enabled, it identifies the relevant DOM node for navigation and inspects each top-level element. All non-scrollable elements and those without rendered HTML are bypassed, this includes sticky or fixed positioned elements, and non-visible elements such as those calculated with `getBoundingClientRect`. Next.js then continues through siblings until it identifies a scrollable element that is visible in the viewport.
app/page.tsx
TypeScript
JavaScript TypeScript
```
import Link from 'next/link'

export default function Page() {
  return (
    <Link href="/dashboard" scroll={false}>
      Dashboard
    </Link>
  )
}
```

###  `prefetch`[](https://nextjs.org/docs/app/api-reference/components/link#prefetch)
Prefetching happens when a `<Link />` component enters the user's viewport (initially or through scroll). Next.js prefetches and loads the linked route (denoted by the `href`) and its data in the background to improve the performance of client-side navigations. If the prefetched data has expired by the time the user hovers over a `<Link />`, Next.js will attempt to prefetch it again. **Prefetching is only enabled in production**.
The following values can be passed to the `prefetch` prop:
  * **`"auto"`or`null` (default)**: Prefetch behavior depends on whether the route is static or dynamic. For static routes, the full route will be prefetched (including all its data). For dynamic routes, the partial route down to the nearest segment with a [`loading.js`](https://nextjs.org/docs/app/api-reference/file-conventions/loading#instant-loading-states) boundary will be prefetched.
  * `true`: The full route will be prefetched for both static and dynamic routes.
  * `false`: Prefetching will never happen both on entering the viewport and on hover.


app/page.tsx
TypeScript
JavaScript TypeScript
```
import Link from 'next/link'

export default function Page() {
  return (
    <Link href="/dashboard" prefetch={false}>
      Dashboard
    </Link>
  )
}
```

###  `onNavigate`[](https://nextjs.org/docs/app/api-reference/components/link#onnavigate)
An event handler called during client-side navigation. The handler receives an event object that includes a `preventDefault()` method, allowing you to cancel the navigation if needed.
app/page.tsx
TypeScript
JavaScript TypeScript
```
import Link from 'next/link'

export default function Page() {
  return (
    <Link
      href="/dashboard"
      onNavigate={(e) => {
        // Only executes during SPA navigation
        console.log('Navigating...')

        // Optionally prevent navigation
        // e.preventDefault()
      }}
    >
      Dashboard
    </Link>
  )
}
```

> **Good to know** : While `onClick` and `onNavigate` may seem similar, they serve different purposes. `onClick` executes for all click events, while `onNavigate` only runs during client-side navigation. Some key differences:
>   * When using modifier keys (`Ctrl`/`Cmd` + Click), `onClick` executes but `onNavigate` doesn't since Next.js prevents default navigation for new tabs.
>   * External URLs won't trigger `onNavigate` since it's only for client-side and same-origin navigations.
>   * Links with the `download` attribute will work with `onClick` but not `onNavigate` since the browser will treat the linked URL as a download.
>
