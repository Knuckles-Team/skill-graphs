## Parallel Routes `default.js` requirement[](https://nextjs.org/docs/app/guides/upgrading/version-16#parallel-routes-defaultjs-requirement)
All [parallel route](https://nextjs.org/docs/app/api-reference/file-conventions/parallel-routes) slots now require explicit `default.js` files. Builds will fail without them.
To maintain previous behavior, create a [`default.js`](https://nextjs.org/docs/app/api-reference/file-conventions/default) file that calls `notFound()` or returns `null`.
app/@modal/default.tsx
```
import { notFound } from 'next/navigation'

export default function Default() {
  notFound()
}
```

Or return `null`:
app/@modal/default.tsx
```
export default function Default() {
  return null
}
```
