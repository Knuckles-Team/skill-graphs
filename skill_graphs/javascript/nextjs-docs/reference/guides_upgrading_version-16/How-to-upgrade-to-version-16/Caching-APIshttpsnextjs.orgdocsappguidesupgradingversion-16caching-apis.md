## Caching APIs[](https://nextjs.org/docs/app/guides/upgrading/version-16#caching-apis)
### revalidateTag[](https://nextjs.org/docs/app/guides/upgrading/version-16#revalidatetag)
[`revalidateTag`](https://nextjs.org/docs/app/api-reference/functions/revalidateTag) has a new function signature. You can pass a [`cacheLife`](https://nextjs.org/docs/app/api-reference/functions/cacheLife#reference) profile as the second argument.
app/actions.ts
TypeScript
JavaScript TypeScript
```
'use server'

import { revalidateTag } from 'next/cache'

export async function updateArticle(articleId: string) {
  // Mark article data as stale - article readers see stale data while it revalidates
  revalidateTag(`article-${articleId}`, 'max')
}
```

Use `revalidateTag` for content where a slight delay in updates is acceptable, such as blog posts, product catalogs, or documentation. Users receive stale content while fresh data loads in the background.
### updateTag[](https://nextjs.org/docs/app/guides/upgrading/version-16#updatetag)
[`updateTag`](https://nextjs.org/docs/app/api-reference/functions/updateTag) is a new [Server Actions](https://nextjs.org/docs/app/getting-started/updating-data#what-are-server-functions)-only API that provides **read-your-writes** semantics, where a user makes a change and the UI immediately shows the change, rather than stale data.
It does this by expiring and immediately refreshing data within the same request.
app/actions.ts
TypeScript
JavaScript TypeScript
```
'use server'

import { updateTag } from 'next/cache'

export async function updateUserProfile(userId: string, profile: Profile) {
  await db.users.update(userId, profile)

  // Expire cache and refresh immediately - user sees their changes right away
  updateTag(`user-${userId}`)
}
```

This ensures interactive features reflect changes immediately. Perfect for forms, user settings, and any workflow where users expect to see their updates instantly.
Learn more about when to use `updateTag` or `revalidateTag` [here](https://nextjs.org/docs/app/api-reference/functions/updateTag#when-to-use-updatetag).
### refresh[](https://nextjs.org/docs/app/guides/upgrading/version-16#refresh)
[`refresh`](https://nextjs.org/docs/app/api-reference/functions/refresh) allows you to refresh the client router from within a Server Action.
app/actions.ts
TypeScript
JavaScript TypeScript
```
'use server'

import { refresh } from 'next/cache'

export async function markNotificationAsRead(notificationId: string) {
  // Update the notification in the database
  await db.notifications.markAsRead(notificationId)

  // Refresh the notification count displayed in the header
  refresh()
}
```

Use it when you need to refresh the client router after performing an action.
### cacheLife and cacheTag[](https://nextjs.org/docs/app/guides/upgrading/version-16#cachelife-and-cachetag)
[`cacheLife`](https://nextjs.org/docs/app/api-reference/functions/cacheLife) and [`cacheTag`](https://nextjs.org/docs/app/api-reference/functions/cacheTag) are now stable. The `unstable_` prefix is no longer needed.
Wherever you had aliased imports like:
```
import {
  unstable_cacheLife as cacheLife,
  unstable_cacheTag as cacheTag,
} from 'next/cache'
```

You can update your imports to:
```
import { cacheLife, cacheTag } from 'next/cache'
```
