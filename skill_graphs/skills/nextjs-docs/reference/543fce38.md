## Possible Ways to Fix It[](https://nextjs.org/docs/messages/no-title-in-document-head#possible-ways-to-fix-it)
Within a page or component, import and use `next/head` to define a page title:
pages/index.js
```
import Head from 'next/head'

export function Home() {
  return (
    <div>
      <Head>
        <title>My page title</title>
      </Head>
    </div>
  )
}
```
