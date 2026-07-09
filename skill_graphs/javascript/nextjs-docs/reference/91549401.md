## Examples[](https://nextjs.org/docs/app/api-reference/components/form#examples)
### Search form that leads to a search result page[](https://nextjs.org/docs/app/api-reference/components/form#search-form-that-leads-to-a-search-result-page)
You can create a search form that navigates to a search results page by passing the path as an `action`:
/app/page.tsx
TypeScript
JavaScript TypeScript
```
import Form from 'next/form'

export default function Page() {
  return (
    <Form action="/search">
      <input name="query" />
      <button type="submit">Submit</button>
    </Form>
  )
}
```

When the user updates the query input field and submits the form, the form data will be encoded into the URL as search params, e.g. `/search?query=abc`.
> **Good to know** : If you pass an empty string `""` to `action`, the form will navigate to the same route with updated search params.
On the results page, you can access the query using the [`searchParams`](https://nextjs.org/docs/app/api-reference/file-conventions/page#searchparams-optional) `page.js` prop and use it to fetch data from an external source.
/app/search/page.tsx
TypeScript
JavaScript TypeScript
```
import { getSearchResults } from '@/lib/search'

export default async function SearchPage({
  searchParams,
}: {
  searchParams: Promise<{ [key: string]: string | string[] | undefined }>
}) {
  const results = await getSearchResults((await searchParams).query)

  return <div>...</div>
}
```

When the `<Form>` becomes visible in the user's viewport, shared UI (such as `layout.js` and `loading.js`) on the `/search` page will be prefetched. On submission, the form will immediately navigate to the new route and show loading UI while the results are being fetched. You can design the fallback UI using [`loading.js`](https://nextjs.org/docs/app/api-reference/file-conventions/loading):
/app/search/loading.tsx
TypeScript
JavaScript TypeScript
```
export default function Loading() {
  return <div>Loading...</div>
}
```

To cover cases when shared UI hasn't yet loaded, you can show instant feedback to the user using
First, create a component that displays a loading state when the form is pending:
/app/ui/search-button.tsx
TypeScript
JavaScript TypeScript
```
'use client'
import { useFormStatus } from 'react-dom'

export default function SearchButton() {
  const status = useFormStatus()
  return (
    <button type="submit">{status.pending ? 'Searching...' : 'Search'}</button>
  )
}
```

Then, update the search form page to use the `SearchButton` component:
/app/page.tsx
TypeScript
JavaScript TypeScript
```
import Form from 'next/form'
import { SearchButton } from '@/ui/search-button'

export default function Page() {
  return (
    <Form action="/search">
      <input name="query" />
      <SearchButton />
    </Form>
  )
}
```

### Mutations with Server Actions[](https://nextjs.org/docs/app/api-reference/components/form#mutations-with-server-actions)
You can perform mutations by passing a function to the `action` prop.
/app/posts/create/page.tsx
TypeScript
JavaScript TypeScript
```
import Form from 'next/form'
import { createPost } from '@/posts/actions'

export default function Page() {
  return (
    <Form action={createPost}>
      <input name="title" />
      {/* ... */}
      <button type="submit">Create Post</button>
    </Form>
  )
}
```

After a mutation, it's common to redirect to the new resource. You can use the [`redirect`](https://nextjs.org/docs/app/guides/redirecting) function from `next/navigation` to navigate to the new post page.
> **Good to know** : Since the "destination" of the form submission is not known until the action is executed, `<Form>` cannot automatically prefetch shared UI.
/app/posts/actions.ts
TypeScript
JavaScript TypeScript
```
'use server'
import { redirect } from 'next/navigation'

export async function createPost(formData: FormData) {
  // Create a new post
  // ...

  // Redirect to the new post
  redirect(`/posts/${data.id}`)
}
```

Then, in the new page, you can fetch data using the `params` prop:
/app/posts/[id]/page.tsx
TypeScript
JavaScript TypeScript
```
import { getPost } from '@/posts/data'

export default async function PostPage({
  params,
}: {
  params: Promise<{ id: string }>
}) {
  const { id } = await params
  const data = await getPost(id)

  return (
    <div>
      <h1>{data.title}</h1>
      {/* ... */}
    </div>
  )
}
```

See the [Server Actions](https://nextjs.org/docs/app/getting-started/updating-data) docs for more examples.
[PreviousFont](https://nextjs.org/docs/app/api-reference/components/font)[NextImage Component](https://nextjs.org/docs/app/api-reference/components/image)
Was this helpful?
Send
* * *
* * *
#### Resources
[Docs](https://nextjs.org/docs)[Support Policy](https://nextjs.org/support-policy)[Learn](https://nextjs.org/learn)[Showcase](https://nextjs.org/showcase)[Blog](https://nextjs.org/blog)[Team](https://nextjs.org/team)[Next.js Conf](https://nextjs.org/conf)[Evals](https://nextjs.org/evals)
#### More
[Telemetry](https://nextjs.org/telemetry)[Governance](https://nextjs.org/governance)
#### About Vercel
#### Legal
Cookie Preferences
#### Subscribe to our newsletter
Stay updated on new releases and features, guides, and case studies.
Subscribe
© 2026 Vercel, Inc.
* * *
* * *
