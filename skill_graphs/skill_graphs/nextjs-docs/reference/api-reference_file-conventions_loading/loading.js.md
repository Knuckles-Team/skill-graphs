# loading.js
Last updated February 27, 2026
The special file `loading.js` helps you create meaningful Loading UI with [instant loading state](https://nextjs.org/docs/app/api-reference/file-conventions/loading#instant-loading-states) from the server while the content of a route segment streams in. The new content is automatically swapped in once complete.
![Loading UI](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Floading-ui.png&w=3840&q=75)![Loading UI](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Floading-ui.png&w=3840&q=75)
app/feed/loading.tsx
TypeScript
JavaScript TypeScript
```
export default function Loading() {
  // Or a custom loading skeleton component
  return <p>Loading...</p>
}
```

Inside the `loading.js` file, you can add any light-weight loading UI. You may find it helpful to use the
By default, this file is a [Server Component](https://nextjs.org/docs/app/getting-started/server-and-client-components) - but can also be used as a Client Component through the `"use client"` directive.
