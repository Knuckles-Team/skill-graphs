# error.js
Last updated February 27, 2026
An **error** file allows you to handle unexpected runtime errors and display fallback UI.
![error.js special file](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Ferror-special-file.png&w=3840&q=75)![error.js special file](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Ferror-special-file.png&w=3840&q=75)
app/dashboard/error.tsx
TypeScript
JavaScript TypeScript
```
'use client' // Error boundaries must be Client Components

import { useEffect } from 'react'

export default function Error({
  error,
  reset,
}: {
  error: Error & { digest?: string }
  reset: () => void
}) {
  useEffect(() => {
    // Log the error to an error reporting service
    console.error(error)
  }, [error])

  return (
    <div>
      <h2>Something went wrong!</h2>
      <button
        onClick={
          // Attempt to recover by trying to re-render the segment
          () => reset()
        }
      >
        Try again
      </button>
    </div>
  )
}
```

`error.js` wraps a route segment and its nested children in a `error` component shows as the fallback UI.
![How error.js works](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Ferror-overview.png&w=3840&q=75)![How error.js works](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Ferror-overview.png&w=3840&q=75)
> **Good to know** :
>   * The
>   * If you want errors to bubble up to the parent error boundary, you can `throw` when rendering the `error` component.
>
