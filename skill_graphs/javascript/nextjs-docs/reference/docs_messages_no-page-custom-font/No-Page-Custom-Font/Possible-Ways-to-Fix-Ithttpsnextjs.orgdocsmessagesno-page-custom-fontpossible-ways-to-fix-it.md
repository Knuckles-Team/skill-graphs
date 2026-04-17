## Possible Ways to Fix It[](https://nextjs.org/docs/messages/no-page-custom-font#possible-ways-to-fix-it)
Create the file `./pages/_document.js` and add the font to a custom Document:
pages/_document.js
```
import Document, { Html, Head, Main, NextScript } from 'next/document'

class MyDocument extends Document {
  render() {
    return (
      <Html>
        <Head>
          <link
            href="https://fonts.googleapis.com/css2?family=Inter&display=optional"
            rel="stylesheet"
          />
        </Head>
        <body>
          <Main />
          <NextScript />
        </body>
      </Html>
    )
  }
}

export default MyDocument
```

Or as a function component:
pages/_document.js
```
import { Html, Head, Main, NextScript } from 'next/document'

export default function Document() {
  return (
    <Html>
      <Head>
        <link
          href="https://fonts.googleapis.com/css2?family=Inter&display=optional"
          rel="stylesheet"
        />
      </Head>
      <body>
        <Main />
        <NextScript />
      </body>
    </Html>
  )
}
```

### When Not To Use It[](https://nextjs.org/docs/messages/no-page-custom-font#when-not-to-use-it)
If you have a reason to only load a font for a particular page or don't care about font optimization, then you can disable this rule.
