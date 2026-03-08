## Static metadata[](https://nextjs.org/docs/app/getting-started/metadata-and-og-images#static-metadata)
To define static metadata, export a [`Metadata` object](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#metadata-object) from a static [`layout.js`](https://nextjs.org/docs/app/api-reference/file-conventions/layout) or [`page.js`](https://nextjs.org/docs/app/api-reference/file-conventions/page) file. For example, to add a title and description to the blog route:
app/blog/layout.tsx
TypeScript
JavaScript TypeScript
```
import type { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'My Blog',
  description: '...',
}

export default function Layout() {}
```

You can view a full list of available options, in the [`generateMetadata` documentation](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#metadata-fields).
