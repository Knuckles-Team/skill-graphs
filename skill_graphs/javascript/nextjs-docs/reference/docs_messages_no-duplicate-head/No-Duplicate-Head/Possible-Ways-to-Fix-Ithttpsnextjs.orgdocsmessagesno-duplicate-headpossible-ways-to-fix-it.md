## Possible Ways to Fix It[](https://nextjs.org/docs/messages/no-duplicate-head#possible-ways-to-fix-it)
Only use a single `<Head />` component in your custom document in `pages/_document.js`.
pages/_document.js
```
import Document, { Html, Head, Main, NextScript } from 'next/document'

class MyDocument extends Document {
  static async getInitialProps(ctx) {
    //...
  }

  render() {
    return (
      <Html>
        <Head />
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
