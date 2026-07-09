# Font Module
Last updated February 27, 2026
[`next/font`](https://nextjs.org/docs/app/api-reference/components/font) automatically optimizes your fonts (including custom fonts) and removes external network requests for improved privacy and performance.
It includes **built-in automatic self-hosting** for any font file. This means you can optimally load web fonts with no
You can also conveniently use all **No requests are sent to Google by the browser.**
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

> **🎥 Watch:** Learn more about using `next/font` →
