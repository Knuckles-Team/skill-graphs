## Reference[](https://nextjs.org/docs/pages/api-reference/components/link#reference)
The following props can be passed to the `<Link>` component:
Prop | Example | Type | Required
---|---|---|---
[`href`](https://nextjs.org/docs/pages/api-reference/components/link#href-required) | `href="/dashboard"` | String or Object | Yes
[`as`](https://nextjs.org/docs/pages/api-reference/components/link#as) | `as="/post/abc"` | String or Object | -
[`replace`](https://nextjs.org/docs/pages/api-reference/components/link#replace) | `replace={false}` | Boolean | -
[`scroll`](https://nextjs.org/docs/pages/api-reference/components/link#scroll) | `scroll={false}` | Boolean | -
[`prefetch`](https://nextjs.org/docs/pages/api-reference/components/link#prefetch) | `prefetch={false}` | Boolean | -
[`shallow`](https://nextjs.org/docs/pages/api-reference/components/link#shallow) | `shallow={false}` | Boolean | -
[`locale`](https://nextjs.org/docs/pages/api-reference/components/link#locale) | `locale="fr"` | String or Boolean | -
[`onNavigate`](https://nextjs.org/docs/pages/api-reference/components/link#onnavigate) | `onNavigate={(e) => {}}` | Function | -
> **Good to know** : `<a>` tag attributes such as `className` or `target="_blank"` can be added to `<Link>` as props and will be passed to the underlying `<a>` element.
###  `href` (required)[](https://nextjs.org/docs/pages/api-reference/components/link#href-required)
The path or URL to navigate to.
pages/index.tsx
TypeScript
JavaScript TypeScript
```
import Link from 'next/link'

// Navigate to /about?name=test
export default function Home() {
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

###  `replace`[](https://nextjs.org/docs/pages/api-reference/components/link#replace)
**Defaults to`false`.** When `true`, `next/link` will replace the current history state instead of adding a new URL into the
pages/index.tsx
TypeScript
JavaScript TypeScript
```
import Link from 'next/link'

export default function Home() {
  return (
    <Link href="/dashboard" replace>
      Dashboard
    </Link>
  )
}
```

###  `scroll`[](https://nextjs.org/docs/pages/api-reference/components/link#scroll)
**Defaults to`true`.** The default scrolling behavior of `<Link>` in Next.js **is to maintain scroll position** , similar to how browsers handle back and forwards navigation. When you navigate to a new [Page](https://nextjs.org/docs/app/api-reference/file-conventions/page), scroll position will stay the same as long as the Page is visible in the viewport. However, if the Page is not visible in the viewport, Next.js will scroll to the top of the first Page element.
When `scroll = {false}`, Next.js will not attempt to scroll to the first Page element.
> **Good to know** : Next.js checks if `scroll: false` before managing scroll behavior. If scrolling is enabled, it identifies the relevant DOM node for navigation and inspects each top-level element. All non-scrollable elements and those without rendered HTML are bypassed, this includes sticky or fixed positioned elements, and non-visible elements such as those calculated with `getBoundingClientRect`. Next.js then continues through siblings until it identifies a scrollable element that is visible in the viewport.
pages/index.tsx
TypeScript
JavaScript TypeScript
```
import Link from 'next/link'

export default function Home() {
  return (
    <Link href="/dashboard" scroll={false}>
      Dashboard
    </Link>
  )
}
```

###  `prefetch`[](https://nextjs.org/docs/pages/api-reference/components/link#prefetch)
Prefetching happens when a `<Link />` component enters the user's viewport (initially or through scroll). Next.js prefetches and loads the linked route (denoted by the `href`) and data in the background to improve the performance of client-side navigation's. **Prefetching is only enabled in production**.
The following values can be passed to the `prefetch` prop:
  * **`true`(default)** : The full route and its data will be prefetched.
  * `false`: Prefetching will not happen when entering the viewport, but will happen on hover. If you want to completely remove fetching on hover as well, consider using an `<a>` tag or [incrementally adopting](https://nextjs.org/docs/app/guides/migrating/app-router-migration) the App Router, which enables disabling prefetching on hover too.


pages/index.tsx
TypeScript
JavaScript TypeScript
```
import Link from 'next/link'

export default function Home() {
  return (
    <Link href="/dashboard" prefetch={false}>
      Dashboard
    </Link>
  )
}
```

###  `shallow`[](https://nextjs.org/docs/pages/api-reference/components/link#shallow)
Update the path of the current page without rerunning [`getStaticProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props), [`getServerSideProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props) or [`getInitialProps`](https://nextjs.org/docs/pages/api-reference/functions/get-initial-props). Defaults to `false`.
pages/index.tsx
TypeScript
JavaScript TypeScript
```
import Link from 'next/link'

export default function Home() {
  return (
    <Link href="/dashboard" shallow={false}>
      Dashboard
    </Link>
  )
}
```

###  `locale`[](https://nextjs.org/docs/pages/api-reference/components/link#locale)
The active locale is automatically prepended. `locale` allows for providing a different locale. When `false` `href` has to include the locale as the default behavior is disabled.
pages/index.tsx
TypeScript
JavaScript TypeScript
```
import Link from 'next/link'

export default function Home() {
  return (
    <>
      {/* Default behavior: locale is prepended */}
      <Link href="/dashboard">Dashboard (with locale)</Link>

      {/* Disable locale prepending */}
      <Link href="/dashboard" locale={false}>
        Dashboard (without locale)
      </Link>

      {/* Specify a different locale */}
      <Link href="/dashboard" locale="fr">
        Dashboard (French)
      </Link>
    </>
  )
}
```

###  `as`[](https://nextjs.org/docs/pages/api-reference/components/link#as)
Optional decorator for the path that will be shown in the browser URL bar. Before Next.js 9.5.3 this was used for dynamic routes, check our
When this path differs from the one provided in `href` the previous `href`/`as` behavior is used as shown in the
###  `onNavigate`[](https://nextjs.org/docs/pages/api-reference/components/link#onnavigate)
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
