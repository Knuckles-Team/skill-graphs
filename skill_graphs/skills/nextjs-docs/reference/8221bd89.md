## Example[](https://nextjs.org/docs/app/api-reference/functions/use-link-status#example)
### Inline link hint[](https://nextjs.org/docs/app/api-reference/functions/use-link-status#inline-link-hint)
Add a subtle, fixed-size hint that doesn’t affect layout to confirm a click when prefetching hasn’t completed.
app/components/loading-indicator.tsx
TypeScript
JavaScript TypeScript
```
'use client'

import { useLinkStatus } from 'next/link'

export default function LoadingIndicator() {
  const { pending } = useLinkStatus()
  return (
    <span aria-hidden className={`link-hint ${pending ? 'is-pending' : ''}`} />
  )
}
```

app/shop/layout.tsx
TypeScript
JavaScript TypeScript
```
import Link from 'next/link'
import LoadingIndicator from './components/loading-indicator'

const links = [
  { href: '/shop/electronics', label: 'Electronics' },
  { href: '/shop/clothing', label: 'Clothing' },
  { href: '/shop/books', label: 'Books' },
]

function Menubar() {
  return (
    <div>
      {links.map((link) => (
        <Link key={link.label} href={link.href}>
          <span className="label">{link.label}</span> <LoadingIndicator />
        </Link>
      ))}
    </div>
  )
}

export default function Layout({ children }: { children: React.ReactNode }) {
  return (
    <div>
      <Menubar />
      {children}
    </div>
  )
}
```
