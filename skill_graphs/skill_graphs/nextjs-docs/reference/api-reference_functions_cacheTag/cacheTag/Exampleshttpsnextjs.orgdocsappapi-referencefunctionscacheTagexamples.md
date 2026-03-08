## Examples[](https://nextjs.org/docs/app/api-reference/functions/cacheTag#examples)
### Tagging components or functions[](https://nextjs.org/docs/app/api-reference/functions/cacheTag#tagging-components-or-functions)
Tag your cached data by calling `cacheTag` within a cached function or component:
app/components/bookings.tsx
TypeScript
JavaScript TypeScript
```
import { cacheTag } from 'next/cache'

interface BookingsProps {
  type: string
}

export async function Bookings({ type = 'haircut' }: BookingsProps) {
  'use cache'
  cacheTag('bookings-data')

  async function getBookingsData() {
    const data = await fetch(`/api/bookings?type=${encodeURIComponent(type)}`)
    return data
  }

  return //...
}
```

### Creating tags from external data[](https://nextjs.org/docs/app/api-reference/functions/cacheTag#creating-tags-from-external-data)
You can use the data returned from an async function to tag the cache entry.
app/components/bookings.tsx
TypeScript
JavaScript TypeScript
```
import { cacheTag } from 'next/cache'

interface BookingsProps {
  type: string
}

export async function Bookings({ type = 'haircut' }: BookingsProps) {
  async function getBookingsData() {
    'use cache'
    const data = await fetch(`/api/bookings?type=${encodeURIComponent(type)}`)
    cacheTag('bookings-data', data.id)
    return data
  }
  return //...
}
```

### Invalidating tagged cache[](https://nextjs.org/docs/app/api-reference/functions/cacheTag#invalidating-tagged-cache)
Using [`revalidateTag`](https://nextjs.org/docs/app/api-reference/functions/revalidateTag), you can invalidate the cache for a specific tag when needed:
app/actions.ts
TypeScript
JavaScript TypeScript
```
'use server'

import { revalidateTag } from 'next/cache'

export async function updateBookings() {
  await updateBookingData()
  revalidateTag('bookings-data')
}
```
