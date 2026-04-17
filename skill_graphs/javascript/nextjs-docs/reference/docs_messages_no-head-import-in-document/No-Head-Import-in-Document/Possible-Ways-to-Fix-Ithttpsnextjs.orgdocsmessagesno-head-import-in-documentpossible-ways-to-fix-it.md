## Possible Ways to Fix It[](https://nextjs.org/docs/messages/no-head-import-in-document#possible-ways-to-fix-it)
Only import and use `next/document` within `pages/_document.js` to override the default `Document` component. If you are importing `next/head` to use the `Head` component, import it from `next/document` instead in order to modify `<head>` code across all pages:
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
        <Head></Head>
      </Html>
    )
  }
}

export default MyDocument
```
