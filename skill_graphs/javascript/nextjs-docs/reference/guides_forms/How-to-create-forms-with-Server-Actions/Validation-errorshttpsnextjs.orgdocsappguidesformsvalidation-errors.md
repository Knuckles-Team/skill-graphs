## Validation errors[](https://nextjs.org/docs/app/guides/forms#validation-errors)
To display validation errors or messages, turn the component that defines the `<form>` into a Client Component and use React
When using `useActionState`, the Server function signature will change to receive a new `prevState` or `initialState` parameter as its first argument.
app/actions.ts
TypeScript
JavaScript TypeScript
```
'use server'

import { z } from 'zod'

export async function createUser(initialState: any, formData: FormData) {
  const validatedFields = schema.safeParse({
    email: formData.get('email'),
  })
  // ...
}
```

You can then conditionally render the error message based on the `state` object.
app/ui/signup.tsx
TypeScript
JavaScript TypeScript
```
'use client'

import { useActionState } from 'react'
import { createUser } from '@/app/actions'

const initialState = {
  message: '',
}

export function Signup() {
  const [state, formAction, pending] = useActionState(createUser, initialState)

  return (
    <form action={formAction}>
      <label htmlFor="email">Email</label>
      <input type="text" id="email" name="email" required />
      {/* ... */}
      <p aria-live="polite">{state?.message}</p>
      <button disabled={pending}>Sign up</button>
    </form>
  )
}
```
