# Font Optimization
Last updated February 27, 2026
The [`next/font`](https://nextjs.org/docs/app/api-reference/components/font) module automatically optimizes your fonts and removes external network requests for improved privacy and performance.
It includes **built-in self-hosting** for any font file. This means you can optimally load web fonts with no layout shift.
To start using `next/font`, import it from [`next/font/local`](https://nextjs.org/docs/app/getting-started/fonts#local-fonts) or [`next/font/google`](https://nextjs.org/docs/app/getting-started/fonts#google-fonts), call it as a function with the appropriate options, and set the `className` of the element you want to apply the font to. For example:
app/layout.tsx
TypeScript
JavaScript TypeScript
```
import { Geist } from 'next/font/google'

const geist = Geist({
  subsets: ['latin'],
})

export default function Layout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" className={geist.className}>
      <body>{children}</body>
    </html>
  )
}
```

Fonts are scoped to the component they're used in. To apply a font to your entire application, add it to the [Root Layout](https://nextjs.org/docs/app/api-reference/file-conventions/layout#root-layout).
