## Session Management[](https://nextjs.org/docs/pages/guides/authentication#session-management)
Session management ensures that the user's authenticated state is preserved across requests. It involves creating, storing, refreshing, and deleting sessions or tokens.
There are two types of sessions:
  1. [**Stateless**](https://nextjs.org/docs/pages/guides/authentication#stateless-sessions): Session data (or a token) is stored in the browser's cookies. The cookie is sent with each request, allowing the session to be verified on the server. This method is simpler, but can be less secure if not implemented correctly.
  2. [**Database**](https://nextjs.org/docs/pages/guides/authentication#database-sessions): Session data is stored in a database, with the user's browser only receiving the encrypted session ID. This method is more secure, but can be complex and use more server resources.


> **Good to know:** While you can use either method, or both, we recommend using a session management library such as
### Stateless Sessions[](https://nextjs.org/docs/pages/guides/authentication#stateless-sessions)
#### Setting and deleting cookies[](https://nextjs.org/docs/pages/guides/authentication#setting-and-deleting-cookies)
You can use [API Routes](https://nextjs.org/docs/pages/building-your-application/routing/api-routes) to set the session as a cookie on the server:
pages/api/login.ts
TypeScript
JavaScript TypeScript
```
import { serialize } from 'cookie'
import type { NextApiRequest, NextApiResponse } from 'next'
import { encrypt } from '@/app/lib/session'

export default function handler(req: NextApiRequest, res: NextApiResponse) {
  const sessionData = req.body
  const encryptedSessionData = encrypt(sessionData)

  const cookie = serialize('session', encryptedSessionData, {
    httpOnly: true,
    secure: process.env.NODE_ENV === 'production',
    maxAge: 60 * 60 * 24 * 7, // One week
    path: '/',
  })
  res.setHeader('Set-Cookie', cookie)
  res.status(200).json({ message: 'Successfully set cookie!' })
}
```

### Database Sessions[](https://nextjs.org/docs/pages/guides/authentication#database-sessions)
To create and manage database sessions, you'll need to follow these steps:
  1. Create a table in your database to store session and data (or check if your Auth Library handles this).
  2. Implement functionality to insert, update, and delete sessions
  3. Encrypt the session ID before storing it in the user's browser, and ensure the database and cookie stay in sync (this is optional, but recommended for optimistic auth checks in [Proxy](https://nextjs.org/docs/pages/guides/authentication#optimistic-checks-with-proxy-optional)).


**Creating a Session on the Server** :
pages/api/create-session.ts
TypeScript
JavaScript TypeScript
```
import db from '../../lib/db'
import type { NextApiRequest, NextApiResponse } from 'next'

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  try {
    const user = req.body
    const sessionId = generateSessionId()
    await db.insertSession({
      sessionId,
      userId: user.id,
      createdAt: new Date(),
    })

    res.status(200).json({ sessionId })
  } catch (error) {
    res.status(500).json({ error: 'Internal Server Error' })
  }
}
```
