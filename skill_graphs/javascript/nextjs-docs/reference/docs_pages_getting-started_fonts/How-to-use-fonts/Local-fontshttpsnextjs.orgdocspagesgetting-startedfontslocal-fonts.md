## Local fonts[](https://nextjs.org/docs/pages/getting-started/fonts#local-fonts)
To use a local font, import your font from `next/font/local` and specify the [`src`](https://nextjs.org/docs/pages/api-reference/components/font#src) of your local font file. Fonts can be stored in the [`public`](https://nextjs.org/docs/pages/api-reference/file-conventions/public-folder) folder or inside the `pages` folder. For example:
pages/_app.tsx
TypeScript
JavaScript TypeScript
```
import localFont from 'next/font/local'
import type { AppProps } from 'next/app'

const myFont = localFont({
  src: './my-font.woff2',
})

export default function MyApp({ Component, pageProps }: AppProps) {
  return (
    <main className={myFont.className}>
      <Component {...pageProps} />
    </main>
  )
}
```

If you want to use multiple files for a single font family, `src` can be an array:
```
const roboto = localFont({
  src: [
    {
      path: './Roboto-Regular.woff2',
      weight: '400',
      style: 'normal',
    },
    {
      path: './Roboto-Italic.woff2',
      weight: '400',
      style: 'italic',
    },
    {
      path: './Roboto-Bold.woff2',
      weight: '700',
      style: 'normal',
    },
    {
      path: './Roboto-BoldItalic.woff2',
      weight: '700',
      style: 'italic',
    },
  ],
})
```
