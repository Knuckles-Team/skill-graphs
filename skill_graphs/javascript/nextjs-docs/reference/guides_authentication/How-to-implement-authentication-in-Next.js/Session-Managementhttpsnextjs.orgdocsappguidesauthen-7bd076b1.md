## Session Management[](https://nextjs.org/docs/app/guides/authentication#session-management)
Session management ensures that the user's authenticated state is preserved across requests. It involves creating, storing, refreshing, and deleting sessions or tokens.
There are two types of sessions:
  1. [**Stateless**](https://nextjs.org/docs/app/guides/authentication#stateless-sessions): Session data (or a token) is stored in the browser's cookies. The cookie is sent with each request, allowing the session to be verified on the server. This method is simpler, but can be less secure if not implemented correctly.
  2. [**Database**](https://nextjs.org/docs/app/guides/authentication#database-sessions): Session data is stored in a database, with the user's browser only receiving the encrypted session ID. This method is more secure, but can be complex and use more server resources.


> **Good to know:** While you can use either method, or both, we recommend using a session management library such as
### Stateless Sessions[](https://nextjs.org/docs/app/guides/authentication#stateless-sessions)
To create and manage stateless sessions, there are a few steps you need to follow:
  1. Generate a secret key, which will be used to sign your session, and store it as an [environment variable](https://nextjs.org/docs/app/guides/environment-variables).
  2. Write logic to encrypt/decrypt session data using a session management library.
  3. Manage cookies using the Next.js [`cookies`](https://nextjs.org/docs/app/api-reference/functions/cookies) API.


In addition to the above, consider adding functionality to [update (or refresh)](https://nextjs.org/docs/app/guides/authentication#updating-or-refreshing-sessions) the session when the user returns to the application, and [delete](https://nextjs.org/docs/app/guides/authentication#deleting-the-session) the session when the user logs out.
> **Good to know:** Check if your [auth library](https://nextjs.org/docs/app/guides/authentication#auth-libraries) includes session management.
#### 1. Generating a secret key[](https://nextjs.org/docs/app/guides/authentication#1-generating-a-secret-key)
There are a few ways you can generate secret key to sign your session. For example, you may choose to use the `openssl` command in your terminal:
terminal
```
openssl rand -base64 32
```

This command generates a 32-character random string that you can use as your secret key and store in your [environment variables file](https://nextjs.org/docs/app/guides/environment-variables):
.env
```
SESSION_SECRET=your_secret_key
```

You can then reference this key in your session management logic:
app/lib/session.js
```
const secretKey = process.env.SESSION_SECRET
```

#### 2. Encrypting and decrypting sessions[](https://nextjs.org/docs/app/guides/authentication#2-encrypting-and-decrypting-sessions)
Next, you can use your preferred [session management library](https://nextjs.org/docs/app/guides/authentication#session-management-libraries) to encrypt and decrypt sessions. Continuing from the previous example, we'll use [Edge Runtime](https://nextjs.org/docs/app/api-reference/edge)) and React's
app/lib/session.ts
TypeScript
JavaScript TypeScript
```
import 'server-only'
import { SignJWT, jwtVerify } from 'jose'
import { SessionPayload } from '@/app/lib/definitions'

const secretKey = process.env.SESSION_SECRET
const encodedKey = new TextEncoder().encode(secretKey)

export async function encrypt(payload: SessionPayload) {
  return new SignJWT(payload)
    .setProtectedHeader({ alg: 'HS256' })
    .setIssuedAt()
    .setExpirationTime('7d')
    .sign(encodedKey)
}

export async function decrypt(session: string | undefined = '') {
  try {
    const { payload } = await jwtVerify(session, encodedKey, {
      algorithms: ['HS256'],
    })
    return payload
  } catch (error) {
    console.log('Failed to verify session')
  }
}
```

> **Tips** :
>   * The payload should contain the **minimum** , unique user data that'll be used in subsequent requests, such as the user's ID, role, etc. It should not contain personally identifiable information like phone number, email address, credit card information, etc, or sensitive data like passwords.
>

#### 3. Setting cookies (recommended options)[](https://nextjs.org/docs/app/guides/authentication#3-setting-cookies-recommended-options)
To store the session in a cookie, use the Next.js [`cookies`](https://nextjs.org/docs/app/api-reference/functions/cookies) API. The cookie should be set on the server, and include the recommended options:
  * **HttpOnly** : Prevents client-side JavaScript from accessing the cookie.
  * **Secure** : Use https to send the cookie.
  * **SameSite** : Specify whether the cookie can be sent with cross-site requests.
  * **Max-Age or Expires** : Delete the cookie after a certain period.
  * **Path** : Define the URL path for the cookie.


Please refer to
app/lib/session.ts
TypeScript
JavaScript TypeScript
```
import 'server-only'
import { cookies } from 'next/headers'

export async function createSession(userId: string) {
  const expiresAt = new Date(Date.now() + 7 * 24 * 60 * 60 * 1000)
  const session = await encrypt({ userId, expiresAt })
  const cookieStore = await cookies()

  cookieStore.set('session', session, {
    httpOnly: true,
    secure: true,
    expires: expiresAt,
    sameSite: 'lax',
    path: '/',
  })
}
```

Back in your Server Action, you can invoke the `createSession()` function, and use the [`redirect()`](https://nextjs.org/docs/app/guides/redirecting) API to redirect the user to the appropriate page:
app/actions/auth.ts
TypeScript
JavaScript TypeScript
```
import { createSession } from '@/app/lib/session'

export async function signup(state: FormState, formData: FormData) {
  // Previous steps:
  // 1. Validate form fields
  // 2. Prepare data for insertion into database
  // 3. Insert the user into the database or call an Library API

  // Current steps:
  // 4. Create user session
  await createSession(user.id)
  // 5. Redirect user
  redirect('/profile')
}
```

> **Tips** :
>   * **Cookies should be set on the server** to prevent client-side tampering.
>   * 🎥 Watch: Learn more about stateless sessions and authentication with Next.js →
>

#### Updating (or refreshing) sessions[](https://nextjs.org/docs/app/guides/authentication#updating-or-refreshing-sessions)
You can also extend the session's expiration time. This is useful for keeping the user logged in after they access the application again. For example:
app/lib/session.ts
TypeScript
JavaScript TypeScript
```
import 'server-only'
import { cookies } from 'next/headers'
import { decrypt } from '@/app/lib/session'

export async function updateSession() {
  const session = (await cookies()).get('session')?.value
  const payload = await decrypt(session)

  if (!session || !payload) {
    return null
  }

  const expires = new Date(Date.now() + 7 * 24 * 60 * 60 * 1000)

  const cookieStore = await cookies()
  cookieStore.set('session', session, {
    httpOnly: true,
    secure: true,
    expires: expires,
    sameSite: 'lax',
    path: '/',
  })
}
```

> **Tip:** Check if your auth library supports refresh tokens, which can be used to extend the user's session.
#### Deleting the session[](https://nextjs.org/docs/app/guides/authentication#deleting-the-session)
To delete the session, you can delete the cookie:
app/lib/session.ts
TypeScript
JavaScript TypeScript
```
import 'server-only'
import { cookies } from 'next/headers'

export async function deleteSession() {
  const cookieStore = await cookies()
  cookieStore.delete('session')
}
```

Then you can reuse the `deleteSession()` function in your application, for example, on logout:
app/actions/auth.ts
TypeScript
JavaScript TypeScript
```
import { cookies } from 'next/headers'
import { deleteSession } from '@/app/lib/session'

export async function logout() {
  await deleteSession()
  redirect('/login')
}
```

### Database Sessions[](https://nextjs.org/docs/app/guides/authentication#database-sessions)
To create and manage database sessions, you'll need to follow these steps:
  1. Create a table in your database to store session and data (or check if your Auth Library handles this).
  2. Implement functionality to insert, update, and delete sessions
  3. Encrypt the session ID before storing it in the user's browser, and ensure the database and cookie stay in sync (this is optional, but recommended for optimistic auth checks in [Proxy](https://nextjs.org/docs/app/guides/authentication#optimistic-checks-with-proxy-optional)).


For example:
app/lib/session.ts
TypeScript
JavaScript TypeScript
```
import cookies from 'next/headers'
import { db } from '@/app/lib/db'
import { encrypt } from '@/app/lib/session'

export async function createSession(id: number) {
  const expiresAt = new Date(Date.now() + 7 * 24 * 60 * 60 * 1000)

  // 1. Create a session in the database
  const data = await db
    .insert(sessions)
    .values({
      userId: id,
      expiresAt,
    })
    // Return the session ID
    .returning({ id: sessions.id })

  const sessionId = data[0].id

  // 2. Encrypt the session ID
  const session = await encrypt({ sessionId, expiresAt })

  // 3. Store the session in cookies for optimistic auth checks
  const cookieStore = await cookies()
  cookieStore.set('session', session, {
    httpOnly: true,
    secure: true,
    expires: expiresAt,
    sameSite: 'lax',
    path: '/',
  })
}
```

> **Tips** :
>   * For faster access, you may consider adding server caching for the lifetime of the session. You can also keep the session data in your primary database, and combine data requests to reduce the number of queries.
>   * You may opt to use database sessions for more advanced use cases, such as keeping track of the last time a user logged in, or number of active devices, or give users the ability to log out of all devices.
>

After implementing session management, you'll need to add authorization logic to control what users can access and do within your application. Continue to the [Authorization](https://nextjs.org/docs/app/guides/authentication#authorization) section to learn more.
