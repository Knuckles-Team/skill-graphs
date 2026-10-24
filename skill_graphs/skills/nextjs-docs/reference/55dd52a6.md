## Possible Ways to Fix It[](https://nextjs.org/docs/messages/no-before-interactive-script-outside-document#possible-ways-to-fix-it)
### App Router[](https://nextjs.org/docs/messages/no-before-interactive-script-outside-document#app-router)
If you want a global script, and you are using the App Router, move the script inside `app/layout.jsx`.
app/layout.jsx
```
import Script from 'next/script'

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>{children}</body>
      <Script
        src="https://example.com/script.js"
        strategy="beforeInteractive"
      />
    </html>
  )
}
```

### Pages Router[](https://nextjs.org/docs/messages/no-before-interactive-script-outside-document#pages-router)
If you want a global script, and you are using the Pages Router, move the script inside `pages/_document.js`.
pages/_document.js
```
import { Html, Head, Main, NextScript } from 'next/document'
import Script from 'next/script'

export default function Document() {
  return (
    <Html>
      <Head />
      <body>
        <Main />
        <NextScript />
        <Script
          src="https://example.com/script.js"
          strategy="beforeInteractive"
        ></Script>
      </body>
    </Html>
  )
}
```
