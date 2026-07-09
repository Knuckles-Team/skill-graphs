## Step 3: Preview the Draft Content[](https://nextjs.org/docs/app/guides/draft-mode#step-3-preview-the-draft-content)
The next step is to update your page to check the value of `draftMode().isEnabled`.
If you request a page which has the cookie set, then data will be fetched at **request time** (instead of at build time).
Furthermore, the value of `isEnabled` will be `true`.
app/page.tsx
TypeScript
JavaScript TypeScript
```
// page that fetches data
import { draftMode } from 'next/headers'

async function getData() {
  const { isEnabled } = await draftMode()

  const url = isEnabled
    ? 'https://draft.example.com'
    : 'https://production.example.com'

  const res = await fetch(url)

  return res.json()
}

export default async function Page() {
  const { title, desc } = await getData()

  return (
    <main>
      <h1>{title}</h1>
      <p>{desc}</p>
    </main>
  )
}
```

If you access the draft Route Handler (with `secret` and `slug`) from your headless CMS or manually using the URL, you should now be able to see the draft content. And, if you update your draft without publishing, you should be able to view the draft.
