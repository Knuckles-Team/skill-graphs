## Potential ESLint errors[](https://nextjs.org/docs/pages/api-reference/functions/use-router#potential-eslint-errors)
Certain methods accessible on the `router` object return a Promise. If you have the ESLint rule,
If your application needs this rule, you should either `void` the promise – or use an `async` function, `await` the Promise, then void the function call. **This is not applicable when the method is called from inside an`onClick` handler**.
The affected methods are:
  * `router.push`
  * `router.replace`
  * `router.prefetch`


### Potential solutions[](https://nextjs.org/docs/pages/api-reference/functions/use-router#potential-solutions)
```
import { useEffect } from 'react'
import { useRouter } from 'next/router'

// Here you would fetch and return the user
const useUser = () => ({ user: null, loading: false })

export default function Page() {
  const { user, loading } = useUser()
  const router = useRouter()

  useEffect(() => {
    // disable the linting on the next line - This is the cleanest solution
    // eslint-disable-next-line no-floating-promises
    router.push('/login')

    // void the Promise returned by router.push
    if (!(user || loading)) {
      void router.push('/login')
    }
    // or use an async function, await the Promise, then void the function call
    async function handleRouteChange() {
      if (!(user || loading)) {
        await router.push('/login')
      }
    }
    void handleRouteChange()
  }, [user, loading])

  return <p>Redirecting...</p>
}
```
