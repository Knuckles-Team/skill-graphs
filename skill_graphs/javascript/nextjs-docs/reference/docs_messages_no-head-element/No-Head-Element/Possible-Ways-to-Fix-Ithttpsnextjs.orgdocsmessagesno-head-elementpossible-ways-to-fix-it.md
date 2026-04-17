## Possible Ways to Fix It[](https://nextjs.org/docs/messages/no-head-element#possible-ways-to-fix-it)
Import and use the `<Head />` component:
pages/index.js
```
import Head from 'next/head'

function Index() {
  return (
    <>
      <Head>
        <title>My page title</title>
        <meta name="viewport" content="initial-scale=1.0, width=device-width" />
      </Head>
    </>
  )
}

export default Index
```
