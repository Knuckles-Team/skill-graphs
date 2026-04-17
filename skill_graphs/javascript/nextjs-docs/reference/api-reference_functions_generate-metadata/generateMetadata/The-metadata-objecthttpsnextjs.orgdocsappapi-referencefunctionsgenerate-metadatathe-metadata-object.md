## The `metadata` object[](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#the-metadata-object)
To define static metadata, export a [`Metadata` object](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#metadata-fields) from a `layout.js` or `page.js` file.
layout.tsx | page.tsx
TypeScript
JavaScript TypeScript
```
import type { Metadata } from 'next'

export const metadata: Metadata = {
  title: '...',
  description: '...',
}

export default function Page() {}
```

> See the [Metadata Fields](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#metadata-fields) for a complete list of supported options.
