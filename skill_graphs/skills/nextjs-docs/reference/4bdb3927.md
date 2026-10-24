# Head
Last updated February 27, 2026
We expose a built-in component for appending elements to the `head` of the page:
```
import Head from 'next/head'

function IndexPage() {
  return (
    <div>
      <Head>
        <title>My page title</title>
      </Head>
      <p>Hello world!</p>
    </div>
  )
}

export default IndexPage
```
