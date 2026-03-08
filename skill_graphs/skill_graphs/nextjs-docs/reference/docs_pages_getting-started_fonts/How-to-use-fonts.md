# How to use fonts
Last updated February 27, 2026
The [`next/font`](https://nextjs.org/docs/app/api-reference/components/font) module automatically optimizes your fonts and removes external network requests for improved privacy and performance.
It includes **built-in self-hosting** for any font file. This means you can optimally load web fonts with no layout shift.
To start using `next/font`, import it from [`next/font/local`](https://nextjs.org/docs/pages/getting-started/fonts#local-fonts) or [`next/font/google`](https://nextjs.org/docs/pages/getting-started/fonts#google-fonts), call it as a function with the appropriate options, and set the `className` of the element you want to apply the font to. For example, you can apply fonts globally in your [Custom App](https://nextjs.org/docs/pages/building-your-application/routing/custom-app) (`pages/_app`):
pages/_app.tsx
TypeScript
JavaScript TypeScript
```
import { Geist } from 'next/font/google'
import type { AppProps } from 'next/app'

const geist = Geist({
  subsets: ['latin'],
})

export default function MyApp({ Component, pageProps }: AppProps) {
  return (
    <main className={geist.className}>
      <Component {...pageProps} />
    </main>
  )
}
```

If you want to apply the font to the `<html>` element, you can use a [Custom Document](https://nextjs.org/docs/pages/building-your-application/routing/custom-document) (`pages/_document`):
pages/_document.tsx
TypeScript
JavaScript TypeScript
```
import { Html, Head, Main, NextScript } from 'next/document'
import { Geist } from 'next/font/google'

const geist = Geist({
  subsets: ['latin'],
})

export default function Document() {
  return (
    <Html lang="en" className={geist.className}>
      <Head />
      <body>
        <Main />
        <NextScript />
      </body>
    </Html>
  )
}
```
