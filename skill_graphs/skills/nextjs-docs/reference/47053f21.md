## Passing additional arguments[](https://nextjs.org/docs/app/guides/forms#passing-additional-arguments)
Outside of form fields, you can pass additional arguments to a Server Function using the JavaScript `userId` argument to the `updateUser` Server Function:
app/client-component.tsx
TypeScript
JavaScript TypeScript
```
'use client'

import { updateUser } from './actions'

export function UserProfile({ userId }: { userId: string }) {
  const updateUserWithId = updateUser.bind(null, userId)

  return (
    <form action={updateUserWithId}>
      <input type="text" name="name" />
      <button type="submit">Update User Name</button>
    </form>
  )
}
```

The Server Function will receive the `userId` as an additional argument:
app/actions.ts
TypeScript
JavaScript TypeScript
```
'use server'

export async function updateUser(userId: string, formData: FormData) {}
```

> **Good to know** :
>   * An alternative is to pass arguments as hidden input fields in the form (e.g. `<input type="hidden" name="userId" value={userId} />`). However, the value will be part of the rendered HTML and will not be encoded.
>   * `bind` works in both Server and Client Components and supports progressive enhancement.
>
