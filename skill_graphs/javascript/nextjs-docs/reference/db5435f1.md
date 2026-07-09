## When to use updateTag[](https://nextjs.org/docs/app/api-reference/functions/updateTag#when-to-use-updatetag)
Use `updateTag` when:
  * You're in a Server Action
  * You need immediate cache invalidation for read-your-own-writes
  * You want to ensure the next request sees updated data


Use `revalidateTag` instead when:
  * You're in a Route Handler or other non-action context
  * You want stale-while-revalidate semantics
  * You're building a webhook or API endpoint for cache invalidation
