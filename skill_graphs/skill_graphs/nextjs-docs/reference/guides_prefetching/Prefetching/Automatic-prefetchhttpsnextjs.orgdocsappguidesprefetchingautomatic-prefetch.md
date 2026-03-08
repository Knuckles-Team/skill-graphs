## Automatic prefetch[](https://nextjs.org/docs/app/guides/prefetching#automatic-prefetch)
app/ui/nav-link.tsx
TypeScript
JavaScript TypeScript
```
import Link from 'next/link'

export default function NavLink() {
  return <Link href="/about">About</Link>
}
```

**Context** | **Prefetched payload** | **Client Cache TTL**
---|---|---
No `loading.js` | Entire page | Until app reload
With `loading.js` | Layout to first loading boundary | 30s ([configurable](https://nextjs.org/docs/app/api-reference/config/next-config-js/staleTimes))
Automatic prefetching runs only in production. Disable with `prefetch={false}` or use the wrapper in [Disabled Prefetch](https://nextjs.org/docs/app/guides/prefetching#disabled-prefetch).
