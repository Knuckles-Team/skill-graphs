## Returns[](https://nextjs.org/docs/app/api-reference/functions/use-search-params#returns)
`useSearchParams` returns a **read-only** version of the
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


> **Good to know** :
>   * `useSearchParams` is a [Client Component](https://nextjs.org/docs/app/getting-started/server-and-client-components) hook and is **not supported** in [Server Components](https://nextjs.org/docs/app/getting-started/server-and-client-components) to prevent stale values during [partial rendering](https://nextjs.org/docs/app/getting-started/linking-and-navigating#client-side-transitions).
>   * If you want to fetch data in a Server Component based on search params, it's often a better option to read the [`searchParams` prop](https://nextjs.org/docs/app/api-reference/file-conventions/page#searchparams-optional) of the corresponding Page. You can then pass it down by props to any component (Server or Client) within that Page.
>   * If an application includes the `/pages` directory, `useSearchParams` will return `ReadonlyURLSearchParams | null`. The `null` value is for compatibility during migration since search params cannot be known during pre-rendering of a page that doesn't use `getServerSideProps`
>
