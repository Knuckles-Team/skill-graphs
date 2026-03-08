## Reference[](https://nextjs.org/docs/app/api-reference/file-conventions/error#reference)
### Props[](https://nextjs.org/docs/app/api-reference/file-conventions/error#props)
####  `error`[](https://nextjs.org/docs/app/api-reference/file-conventions/error#error)
An instance of an `error.js` Client Component.
> **Good to know:** During development, the `Error` object forwarded to the client will be serialized and include the `message` of the original error for easier debugging. However, **this behavior is different in production** to avoid leaking potentially sensitive details included in the error to the client.
####  `error.message`[](https://nextjs.org/docs/app/api-reference/file-conventions/error#errormessage)
  * Errors forwarded from Client Components show the original `Error` message.
  * Errors forwarded from Server Components show a generic message with an identifier. This is to prevent leaking sensitive details. You can use the identifier, under `errors.digest`, to match the corresponding server-side logs.


####  `error.digest`[](https://nextjs.org/docs/app/api-reference/file-conventions/error#errordigest)
An automatically generated hash of the error thrown. It can be used to match the corresponding error in server-side logs.
####  `reset`[](https://nextjs.org/docs/app/api-reference/file-conventions/error#reset)
The cause of an error can sometimes be temporary. In these cases, trying again might resolve the issue.
An error component can use the `reset()` function to prompt the user to attempt to recover from the error. When executed, the function will try to re-render the error boundary's contents. If successful, the fallback error component is replaced with the result of the re-render.
app/dashboard/error.tsx
TypeScript
JavaScript TypeScript
```
'use client' // Error boundaries must be Client Components

export default function Error({
  error,
  reset,
}: {
  error: Error & { digest?: string }
  reset: () => void
}) {
  return (
    <div>
      <h2>Something went wrong!</h2>
      <button onClick={() => reset()}>Try again</button>
    </div>
  )
}
```
