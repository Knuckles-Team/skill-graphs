## Possible Ways to Fix It[](https://nextjs.org/docs/messages/no-document-import-in-page#possible-ways-to-fix-it)
Only import and use `next/document` within `pages/_document.js` (or `pages/_document.tsx`) to override the default `Document` component:
pages/_document.js
```
import Document, { Html, Head, Main, NextScript } from 'next/document'

class MyDocument extends Document {
  //...
}

export default MyDocument
```
