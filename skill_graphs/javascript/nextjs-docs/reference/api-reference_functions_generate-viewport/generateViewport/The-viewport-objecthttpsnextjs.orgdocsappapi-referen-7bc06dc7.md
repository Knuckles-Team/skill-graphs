## The `viewport` object[](https://nextjs.org/docs/app/api-reference/functions/generate-viewport#the-viewport-object)
To define the viewport options, export a `viewport` object from a `layout.jsx` or `page.jsx` file.
layout.tsx | page.tsx
TypeScript
JavaScript TypeScript
```
import type { Viewport } from 'next'

export const viewport: Viewport = {
  themeColor: 'black',
}

export default function Page() {}
```
