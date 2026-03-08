## Transition between locales[](https://nextjs.org/docs/pages/guides/internationalization#transition-between-locales)
You can use `next/link` or `next/router` to transition between locales.
For `next/link`, a `locale` prop can be provided to transition to a different locale from the currently active one. If no `locale` prop is provided, the currently active `locale` is used during client-transitions. For example:
```
import Link from 'next/link'

export default function IndexPage(props) {
  return (
    <Link href="/another" locale="fr">
      To /fr/another
    </Link>
  )
}
```

When using the `next/router` methods directly, you can specify the `locale` that should be used via the transition options. For example:
```
import { useRouter } from 'next/router'

export default function IndexPage(props) {
  const router = useRouter()

  return (
    <div
      onClick={() => {
        router.push('/another', '/another', { locale: 'fr' })
      }}
    >
      to /fr/another
    </div>
  )
}
```

Note that to handle switching only the `locale` while preserving all routing information such as [dynamic route](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes) query values or hidden href query values, you can provide the `href` parameter as an object:
```
import { useRouter } from 'next/router'
const router = useRouter()
const { pathname, asPath, query } = router
// change just the locale and maintain all other route information including href's query
router.push({ pathname, query }, asPath, { locale: nextLocale })
```

See [here](https://nextjs.org/docs/pages/api-reference/functions/use-router#with-url-object) for more information on the object structure for `router.push`.
If you have a `href` that already includes the locale you can opt-out of automatically handling the locale prefixing:
```
import Link from 'next/link'

export default function IndexPage(props) {
  return (
    <Link href="/fr/another" locale={false}>
      To /fr/another
    </Link>
  )
}
```
