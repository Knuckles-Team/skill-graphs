## Pending states[](https://nextjs.org/docs/app/guides/forms#pending-states)
The `pending` boolean that can be used to show a loading indicator or disable the submit button while the action is being executed.
app/ui/signup.tsx
TypeScript
JavaScript TypeScript
```
'use client'

import { useActionState } from 'react'
import { createUser } from '@/app/actions'

export function Signup() {
  const [state, formAction, pending] = useActionState(createUser, initialState)

  return (
    <form action={formAction}>
      {/* Other form elements */}
      <button disabled={pending}>Sign up</button>
    </form>
  )
}
```

Alternatively, you can use the
app/ui/button.tsx
TypeScript
JavaScript TypeScript
```
'use client'

import { useFormStatus } from 'react-dom'

export function SubmitButton() {
  const { pending } = useFormStatus()

  return (
    <button disabled={pending} type="submit">
      Sign Up
    </button>
  )
}
```

You can then nest the `SubmitButton` component inside the form:
app/ui/signup.tsx
TypeScript
JavaScript TypeScript
```
import { SubmitButton } from './button'
import { createUser } from '@/app/actions'

export function Signup() {
  return (
    <form action={createUser}>
      {/* Other form elements */}
      <SubmitButton />
    </form>
  )
}
```

> **Good to know:** In React 19, `useFormStatus` includes additional keys on the returned object, like data, method, and action. If you are not using React 19, only the `pending` key is available.
