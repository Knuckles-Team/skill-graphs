## Shallow Routing[](https://nextjs.org/docs/pages/building-your-application/routing/linking-and-navigating#shallow-routing)
Examples
Shallow routing allows you to change the URL without running data fetching methods again, that includes [`getServerSideProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props), [`getStaticProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props), and [`getInitialProps`](https://nextjs.org/docs/pages/api-reference/functions/get-initial-props).
You'll receive the updated `pathname` and the `query` via the [`router` object](https://nextjs.org/docs/pages/api-reference/functions/use-router#router-object) (added by [`useRouter`](https://nextjs.org/docs/pages/api-reference/functions/use-router) or [`withRouter`](https://nextjs.org/docs/pages/api-reference/functions/use-router#withrouter)), without losing state.
To enable shallow routing, set the `shallow` option to `true`. Consider the following example:
```
import { useEffect } from 'react'
import { useRouter } from 'next/router'

// Current URL is '/'
function Page() {
  const router = useRouter()

  useEffect(() => {
    // Always do navigations after the first render
    router.push('/?counter=10', undefined, { shallow: true })
  }, [])

  useEffect(() => {
    // The counter changed!
  }, [router.query.counter])
}

export default Page
```

The URL will get updated to `/?counter=10` and the page won't get replaced, only the state of the route is changed.
You can also watch for URL changes via
```
componentDidUpdate(prevProps) {
  const { pathname, query } = this.props.router
  // verify props have changed to avoid an infinite loop
  if (query.counter !== prevProps.router.query.counter) {
    // fetch data based on the new query
  }
}
```

### Caveats[](https://nextjs.org/docs/pages/building-your-application/routing/linking-and-navigating#caveats)
Shallow routing **only** works for URL changes in the current page. For example, let's assume we have another page called `pages/about.js`, and you run this:
```
router.push('/?counter=10', '/about?counter=10', { shallow: true })
```

Since that's a new page, it'll unload the current page, load the new one and wait for data fetching even though we asked to do shallow routing.
When shallow routing is used with proxy it will not ensure the new page matches the current page like previously done without proxy. This is due to proxy being able to rewrite dynamically and can't be verified client-side without a data fetch which is skipped with shallow, so a shallow route change must always be treated as shallow.
Was this helpful?
Send
* * *
* * *
#### Resources
[Docs](https://nextjs.org/docs)[Support Policy](https://nextjs.org/support-policy)[Learn](https://nextjs.org/learn)[Showcase](https://nextjs.org/showcase)[Blog](https://nextjs.org/blog)[Team](https://nextjs.org/team)[Next.js Conf](https://nextjs.org/conf)[Evals](https://nextjs.org/evals)
#### More
[Telemetry](https://nextjs.org/telemetry)[Governance](https://nextjs.org/governance)
#### About Vercel
#### Legal
Cookie Preferences
#### Subscribe to our newsletter
Stay updated on new releases and features, guides, and case studies.
Subscribe
© 2026 Vercel, Inc.
* * *
* * *
