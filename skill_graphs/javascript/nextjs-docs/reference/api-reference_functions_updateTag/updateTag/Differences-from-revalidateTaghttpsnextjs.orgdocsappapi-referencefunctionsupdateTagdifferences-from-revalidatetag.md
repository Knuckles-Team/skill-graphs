## Differences from revalidateTag[](https://nextjs.org/docs/app/api-reference/functions/updateTag#differences-from-revalidatetag)
While both `updateTag` and `revalidateTag` invalidate cached data, they serve different purposes:
  * **`updateTag`**:
    * Can only be used in Server Actions
    * Next request waits for fresh data (no stale content served)
    * Designed for read-your-own-writes scenarios
  * **`revalidateTag`**:
    * Can be used in Server Actions and Route Handlers
    * With `profile="max"` (recommended): Serves cached data while fetching fresh data in the background (stale-while-revalidate)
    * With custom profile: Can be configured to any cache life profile for advanced usage
    * Without profile: legacy behavior which is equivalent to `updateTag`
