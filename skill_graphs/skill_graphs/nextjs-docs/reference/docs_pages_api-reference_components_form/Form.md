# Form
Last updated February 27, 2026
The `<Form>` component extends the HTML `<form>` element to provide  **client-side navigation** on submission, and **progressive enhancement**.
It's useful for forms that update URL search params as it reduces the boilerplate code needed to achieve the above.
Basic usage:
/ui/search.js
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
