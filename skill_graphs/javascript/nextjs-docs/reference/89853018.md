# Custom Document
Last updated February 27, 2026
A custom `Document` can update the `<html>` and `<body>` tags used to render a [Page](https://nextjs.org/docs/pages/building-your-application/routing/pages-and-layouts).
To override the default `Document`, create the file `pages/_document` as shown below:
pages/_document.tsx
TypeScript
JavaScript TypeScript
```
import { Html, Head, Main, NextScript } from 'next/document'

export default function Document() {
  return (
    <Html lang="en">
      <Head />
      <body>
        <Main />
        <NextScript />
      </body>
    </Html>
  )
}
```

> **Good to know** :
>   * `_document` is only rendered on the server, so event handlers like `onClick` cannot be used in this file.
>   * `<Html>`, `<Head />`, `<Main />` and `<NextScript />` are required for the page to be properly rendered.
>
