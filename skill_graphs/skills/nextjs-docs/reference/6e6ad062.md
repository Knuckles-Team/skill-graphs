## Creating Server Functions[](https://nextjs.org/docs/app/getting-started/updating-data#creating-server-functions)
A Server Function can be defined by using the **asynchronous** function to mark the function as a Server Function, or at the top of a separate file to mark all exports of that file.
app/lib/actions.ts
TypeScript
JavaScript TypeScript
```
export async function createPost(formData: FormData) {
  'use server'
  const title = formData.get('title')
  const content = formData.get('content')

  // Update data
  // Revalidate cache
}

export async function deletePost(formData: FormData) {
  'use server'
  const id = formData.get('id')

  // Update data
  // Revalidate cache
}
```

### Server Components[](https://nextjs.org/docs/app/getting-started/updating-data#server-components)
Server Functions can be inlined in Server Components by adding the `"use server"` directive to the top of the function body:
app/page.tsx
TypeScript
JavaScript TypeScript
```
export default function Page() {
  // Server Action
  async function createPost(formData: FormData) {
    'use server'
    // ...
  }

  return <></>
}
```

> **Good to know:** Server Components support progressive enhancement by default, meaning forms that call Server Actions will be submitted even if JavaScript hasn't loaded yet or is disabled.
### Client Components[](https://nextjs.org/docs/app/getting-started/updating-data#client-components)
It's not possible to define Server Functions in Client Components. However, you can invoke them in Client Components by importing them from a file that has the `"use server"` directive at the top of it:
app/actions.ts
TypeScript
JavaScript TypeScript
```
'use server'

export async function createPost() {}
```

app/ui/button.tsx
TypeScript
JavaScript TypeScript
```
'use client'

import { createPost } from '@/app/actions'

export function Button() {
  return <button formAction={createPost}>Create</button>
}
```

> **Good to know:** In Client Components, forms invoking Server Actions will queue submissions if JavaScript isn't loaded yet, and will be prioritized for hydration. After hydration, the browser does not refresh on form submission.
### Passing actions as props[](https://nextjs.org/docs/app/getting-started/updating-data#passing-actions-as-props)
You can also pass an action to a Client Component as a prop:
```
<ClientComponent updateItemAction={updateItem} />
```

app/client-component.tsx
TypeScript
JavaScript TypeScript
```
'use client'

export default function ClientComponent({
  updateItemAction,
}: {
  updateItemAction: (formData: FormData) => void
}) {
  return <form action={updateItemAction}>{/* ... */}</form>
}
```
