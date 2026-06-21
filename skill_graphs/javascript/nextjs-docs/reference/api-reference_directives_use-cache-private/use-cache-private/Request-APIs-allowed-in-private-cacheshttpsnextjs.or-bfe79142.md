## Request APIs allowed in private caches[](https://nextjs.org/docs/app/api-reference/directives/use-cache-private#request-apis-allowed-in-private-caches)
The following request-specific APIs can be used inside `'use cache: private'` functions:
API | Allowed in `use cache` | Allowed in `'use cache: private'`
---|---|---
`cookies()` | No | Yes
`headers()` | No | Yes
`searchParams` | No | Yes
`connection()` | No | No
> **Note:** The [`connection()`](https://nextjs.org/docs/app/api-reference/functions/connection) API is prohibited in both `use cache` and `'use cache: private'` as it provides connection-specific information that cannot be safely cached.
