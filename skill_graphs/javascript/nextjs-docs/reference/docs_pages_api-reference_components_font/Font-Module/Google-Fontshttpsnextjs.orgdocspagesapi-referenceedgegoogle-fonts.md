## Google Fonts[](https://nextjs.org/docs/pages/api-reference/edge#google-fonts)
To use a Google font, import it from `next/font/google` as a function. We recommend using
To use the font in all your pages, add it to [`_app.js` file](https://nextjs.org/docs/pages/building-your-application/routing/custom-app) under `/pages` as shown below:
pages/_app.js
```
import { Inter } from 'next/font/google'

// If loading a variable font, you don't need to specify the font weight
const inter = Inter({ subsets: ['latin'] })

export default function MyApp({ Component, pageProps }) {
  return (
    <main className={inter.className}>
      <Component {...pageProps} />
    </main>
  )
}
```

If you can't use a variable font, you will **need to specify a weight** :
pages/_app.js
```
import { Roboto } from 'next/font/google'

const roboto = Roboto({
  weight: '400',
  subsets: ['latin'],
})

export default function MyApp({ Component, pageProps }) {
  return (
    <main className={roboto.className}>
      <Component {...pageProps} />
    </main>
  )
}
```

You can specify multiple weights and/or styles by using an array:
app/layout.js
```
const roboto = Roboto({
  weight: ['400', '700'],
  style: ['normal', 'italic'],
  subsets: ['latin'],
  display: 'swap',
})
```

> **Good to know** : Use an underscore (_) for font names with multiple words. E.g. `Roboto Mono` should be imported as `Roboto_Mono`.
### Apply the font in `<head>`[](https://nextjs.org/docs/pages/api-reference/edge#apply-the-font-in-head)
You can also use the font without a wrapper and `className` by injecting it inside the `<head>` as follows:
pages/_app.js
```
import { Inter } from 'next/font/google'

const inter = Inter({ subsets: ['latin'] })

export default function MyApp({ Component, pageProps }) {
  return (
    <>
      <style jsx global>{`
        html {
          font-family: ${inter.style.fontFamily};
        }
      `}</style>
      <Component {...pageProps} />
    </>
  )
}
```

### Single page usage[](https://nextjs.org/docs/pages/api-reference/edge#single-page-usage)
To use the font on a single page, add it to the specific page as shown below:
pages/index.js
```
import { Inter } from 'next/font/google'

const inter = Inter({ subsets: ['latin'] })

export default function Home() {
  return (
    <div className={inter.className}>
      <p>Hello World</p>
    </div>
  )
}
```

### Specifying a subset[](https://nextjs.org/docs/pages/api-reference/edge#specifying-a-subset)
Google Fonts are automatically [`preload`](https://nextjs.org/docs/app/api-reference/components/font#preload) is `true` will result in a warning.
This can be done by adding it to the function call:
pages/_app.js
```
const inter = Inter({ subsets: ['latin'] })
```

View the [Font API Reference](https://nextjs.org/docs/app/api-reference/components/font) for more information.
