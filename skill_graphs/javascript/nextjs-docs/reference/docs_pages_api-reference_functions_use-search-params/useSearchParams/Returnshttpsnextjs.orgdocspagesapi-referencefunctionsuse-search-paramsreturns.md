## Returns[](https://nextjs.org/docs/pages/api-reference/functions/use-search-params#returns)
`useSearchParams` returns a **read-only** version of the `null` during [pre-rendering](https://nextjs.org/docs/pages/api-reference/functions/use-search-params#behavior-during-pre-rendering).
The interface includes utility methods for reading the URL's query string:
  * URL | `searchParams.get("a")`
---|---
`/dashboard?a=1` | `'1'`
`/dashboard?a=` | `''`
`/dashboard?b=3` | `null`
`/dashboard?a=1&a=2` |  `'1'` _- use_
  * URL | `searchParams.has("a")`
---|---
`/dashboard?a=1` | `true`
`/dashboard?b=3` | `false`
  * Learn more about other **read-only** methods of


> **Good to know** : `useSearchParams` is a
