## Authentication[](https://nextjs.org/docs/pages/guides/authentication#authentication)
Here are the steps to implement a sign-up and/or login form:
  1. The user submits their credentials through a form.
  2. The form sends a request that is handled by an API route.
  3. Upon successful verification, the process is completed, indicating the user's successful authentication.
  4. If verification is unsuccessful, an error message is shown.


Consider a login form where users can input their credentials:
pages/login.tsx
TypeScript
JavaScript TypeScript
```
import { FormEvent } from 'react'
import { useRouter } from 'next/router'

export default function LoginPage() {
  const router = useRouter()

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault()

    const formData = new FormData(event.currentTarget)
    const email = formData.get('email')
    const password = formData.get('password')

    const response = await fetch('/api/auth/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, password }),
    })

    if (response.ok) {
      router.push('/profile')
    } else {
      // Handle errors
    }
  }

  return (
    <form onSubmit={handleSubmit}>
      <input type="email" name="email" placeholder="Email" required />
      <input type="password" name="password" placeholder="Password" required />
      <button type="submit">Login</button>
    </form>
  )
}
```

The form above has two input fields for capturing the user's email and password. On submission, it triggers a function that sends a POST request to an API route (`/api/auth/login`).
You can then call your Authentication Provider's API in the API route to handle authentication:
pages/api/auth/login.ts
TypeScript
JavaScript TypeScript
```
import type { NextApiRequest, NextApiResponse } from 'next'
import { signIn } from '@/auth'

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  try {
    const { email, password } = req.body
    await signIn('credentials', { email, password })

    res.status(200).json({ success: true })
  } catch (error) {
    if (error.type === 'CredentialsSignin') {
      res.status(401).json({ error: 'Invalid credentials.' })
    } else {
      res.status(500).json({ error: 'Something went wrong.' })
    }
  }
}
```
