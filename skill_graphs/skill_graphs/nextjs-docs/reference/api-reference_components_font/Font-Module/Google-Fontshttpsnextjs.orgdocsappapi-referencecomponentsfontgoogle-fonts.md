## Google Fonts[](https://nextjs.org/docs/app/api-reference/components/font#google-fonts)
To use a Google font, import it from `next/font/google` as a function. We recommend using
app/layout.tsx
TypeScript
JavaScript TypeScript
```
import { Inter } from 'next/font/google'

// If loading a variable font, you don't need to specify the font weight
const inter = Inter({
  subsets: ['latin'],
  display: 'swap',
})

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" className={inter.className}>
      <body>{children}</body>
    </html>
  )
}
```

If you can't use a variable font, you will **need to specify a weight** :
app/layout.tsx
TypeScript
JavaScript TypeScript
```
import { Roboto } from 'next/font/google'

const roboto = Roboto({
  weight: '400',
  subsets: ['latin'],
  display: 'swap',
})

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" className={roboto.className}>
      <body>{children}</body>
    </html>
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
### Specifying a subset[](https://nextjs.org/docs/app/api-reference/components/font#specifying-a-subset)
Google Fonts are automatically [`preload`](https://nextjs.org/docs/app/api-reference/components/font#preload) is `true` will result in a warning.
This can be done by adding it to the function call:
app/layout.tsx
TypeScript
JavaScript TypeScript
```
const inter = Inter({ subsets: ['latin'] })
```

View the [Font API Reference](https://nextjs.org/docs/app/api-reference/components/font) for more information.
