## Examples[](https://nextjs.org/docs/app/api-reference/functions/use-search-params#examples)
### Updating `searchParams`[](https://nextjs.org/docs/app/api-reference/functions/use-search-params#updating-searchparams)
You can use [`useRouter`](https://nextjs.org/docs/app/api-reference/functions/use-router) or [`Link`](https://nextjs.org/docs/app/api-reference/components/link) to set new `searchParams`. After a navigation is performed, the current [`page.js`](https://nextjs.org/docs/app/api-reference/file-conventions/page) will receive an updated [`searchParams` prop](https://nextjs.org/docs/app/api-reference/file-conventions/page#searchparams-optional).
app/example-client-component.tsx
TypeScript
JavaScript TypeScript
```
'use client'

export default function ExampleClientComponent() {
  const router = useRouter()
  const pathname = usePathname()
  const searchParams = useSearchParams()

  // Get a new searchParams string by merging the current
  // searchParams with a provided key/value pair
  const createQueryString = useCallback(
    (name: string, value: string) => {
      const params = new URLSearchParams(searchParams.toString())
      params.set(name, value)

      return params.toString()
    },
    [searchParams]
  )

  return (
    <>
      <p>Sort By</p>

      {/* using useRouter */}
      <button
        onClick={() => {
          // <pathname>?sort=asc
          router.push(pathname + '?' + createQueryString('sort', 'asc'))
        }}
      >
        ASC
      </button>

      {/* using <Link> */}
      <Link
        href={
          // <pathname>?sort=desc
          pathname + '?' + createQueryString('sort', 'desc')
        }
      >
        DESC
      </Link>
    </>
  )
}
```
