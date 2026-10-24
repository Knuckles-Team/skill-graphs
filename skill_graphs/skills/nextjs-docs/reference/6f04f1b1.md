## Possible Ways to Fix It[](https://nextjs.org/docs/messages/no-script-component-in-head#possible-ways-to-fix-it)
Move the `<Script />` component outside of `<Head>` instead.
**Before**
pages/index.js
```
import Script from 'next/script'
import Head from 'next/head'

export default function Index() {
  return (
    <Head>
      <title>Next.js</title>
      <Script src="/my-script.js" />
    </Head>
  )
}
```

**After**
pages/index.js
```
import Script from 'next/script'
import Head from 'next/head'

export default function Index() {
  return (
    <>
      <Head>
        <title>Next.js</title>
      </Head>
      <Script src="/my-script.js" />
    </>
  )
}
```
