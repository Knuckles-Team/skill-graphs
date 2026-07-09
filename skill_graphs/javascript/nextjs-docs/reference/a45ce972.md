# Form Component
Last updated February 27, 2026
The `<Form>` component extends the HTML `<form>` element to provide [**prefetching**](https://nextjs.org/docs/app/getting-started/linking-and-navigating#prefetching) of [loading UI](https://nextjs.org/docs/app/api-reference/file-conventions/loading), **client-side navigation** on submission, and **progressive enhancement**.
It's useful for forms that update URL search params as it reduces the boilerplate code needed to achieve the above.
Basic usage:
/app/ui/search.tsx
TypeScript
JavaScript TypeScript
```
import Form from 'next/form'

export default function Page() {
  return (
    <Form action="/search">
      {/* On submission, the input value will be appended to
          the URL, e.g. /search?query=abc */}
      <input name="query" />
      <button type="submit">Submit</button>
    </Form>
  )
}
```
