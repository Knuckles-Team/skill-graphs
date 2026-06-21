## Why This Warning Occurred[](https://nextjs.org/docs/messages/sync-dynamic-apis#why-this-warning-occurred)
Somewhere in your code you used an API that opts into [dynamic rendering](https://nextjs.org/docs/app/glossary#dynamic-rendering).
Dynamic APIs are:
  * The `params` and `searchParams` props that get provided to pages, layouts, metadata APIs, and route handlers.
  * `cookies()`, `draftMode()`, and `headers()` from `next/headers`


In Next 15, these APIs have been made asynchronous. You can read more about this in the Next.js 15 [Upgrade Guide](https://nextjs.org/docs/app/guides/upgrading/version-15).
For example, the following code will issue a warning:
app/[id]/page.js
```
function Page({ params }) {
  // direct access of `params.id`.
  return <p>ID: {params.id}</p>
}
```

This also includes enumerating (e.g. `{...params}`, or `Object.keys(params)`) or iterating over the return value of these APIs (e.g. `[...headers()]` or `for (const cookie of cookies())`, or explicitly with `cookies()[Symbol.iterator]()`).
