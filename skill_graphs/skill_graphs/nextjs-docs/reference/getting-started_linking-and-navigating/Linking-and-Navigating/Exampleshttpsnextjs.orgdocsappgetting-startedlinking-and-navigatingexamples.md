## Examples[](https://nextjs.org/docs/app/getting-started/linking-and-navigating#examples)
### Native History API[](https://nextjs.org/docs/app/getting-started/linking-and-navigating#native-history-api)
Next.js allows you to use the native
`pushState` and `replaceState` calls integrate into the Next.js Router, allowing you to sync with [`usePathname`](https://nextjs.org/docs/app/api-reference/functions/use-pathname) and [`useSearchParams`](https://nextjs.org/docs/app/api-reference/functions/use-search-params).
####  `window.history.pushState`[](https://nextjs.org/docs/app/getting-started/linking-and-navigating#windowhistorypushstate)
Use it to add a new entry to the browser's history stack. The user can navigate back to the previous state. For example, to sort a list of products:
```
'use client'

import { useSearchParams } from 'next/navigation'

export default function SortProducts() {
  const searchParams = useSearchParams()

  function updateSorting(sortOrder: string) {
    const params = new URLSearchParams(searchParams.toString())
    params.set('sort', sortOrder)
    window.history.pushState(null, '', `?${params.toString()}`)
  }

  return (
    <>
      <button onClick={() => updateSorting('asc')}>Sort Ascending</button>
      <button onClick={() => updateSorting('desc')}>Sort Descending</button>
    </>
  )
}
```

####  `window.history.replaceState`[](https://nextjs.org/docs/app/getting-started/linking-and-navigating#windowhistoryreplacestate)
Use it to replace the current entry on the browser's history stack. The user is not able to navigate back to the previous state. For example, to switch the application's locale:
```
'use client'

import { usePathname } from 'next/navigation'

export function LocaleSwitcher() {
  const pathname = usePathname()

  function switchLocale(locale: string) {
    // e.g. '/en/about' or '/fr/contact'
    const newPath = `/${locale}${pathname}`
    window.history.replaceState(null, '', newPath)
  }

  return (
    <>
      <button onClick={() => switchLocale('en')}>English</button>
      <button onClick={() => switchLocale('fr')}>French</button>
    </>
  )
}
```

### [Link Component Enable fast client-side navigation with the built-in `next/link` component.](https://nextjs.org/docs/app/api-reference/components/link)### [loading.js API reference for the loading.js file.](https://nextjs.org/docs/app/api-reference/file-conventions/loading)### [Prefetching Learn how to configure prefetching in Next.js](https://nextjs.org/docs/app/guides/prefetching)
[PreviousLayouts and Pages](https://nextjs.org/docs/app/getting-started/layouts-and-pages)[NextServer and Client Components](https://nextjs.org/docs/app/getting-started/server-and-client-components)
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
