## Data fetching approaches[](https://nextjs.org/docs/app/guides/data-security#data-fetching-approaches)
There are three main approaches we recommend for fetching data in Next.js, depending on the size and age of your project:
  * [HTTP APIs](https://nextjs.org/docs/app/guides/data-security#external-http-apis): for existing large applications and organizations.
  * [Data Access Layer](https://nextjs.org/docs/app/guides/data-security#data-access-layer): for new projects.
  * [Component-Level Data Access](https://nextjs.org/docs/app/guides/data-security#component-level-data-access): for prototypes and learning.


We recommend choosing one data fetching approach and avoiding mixing them. This makes it clear for both developers working in your code base and security auditors what to expect.
### External HTTP APIs[](https://nextjs.org/docs/app/guides/data-security#external-http-apis)
You should follow a **Zero Trust** model when adopting Server Components in an existing project. You can continue calling your existing API endpoints such as REST or GraphQL from Server Components using [`fetch`](https://nextjs.org/docs/app/api-reference/functions/fetch), just as you would in Client Components.
app/page.tsx
```
import { cookies } from 'next/headers'

export default async function Page() {
  const cookieStore = cookies()
  const token = cookieStore.get('AUTH_TOKEN')?.value

  const res = await fetch('https://api.example.com/profile', {
    headers: {
      Cookie: `AUTH_TOKEN=${token}`,
      // Other headers
    },
  })

  // ....
}
```

This approach works well when:
  * You already have security practices in place.
  * Separate backend teams use other languages or manage APIs independently.


### Data Access Layer[](https://nextjs.org/docs/app/guides/data-security#data-access-layer)
For new projects, we recommend creating a dedicated **Data Access Layer (DAL)**. This is a internal library that controls how and when data is fetched, and what gets passed to your render context.
A Data Access Layer should:
  * Only run on the server.
  * Perform authorization checks.
  * Return safe, minimal **Data Transfer Objects (DTOs)**.


This approach centralizes all data access logic, making it easier to enforce consistent data access and reduces the risk of authorization bugs. You also get the benefit of sharing an in-memory cache across different parts of a request.
data/auth.ts
```
import { cache } from 'react'
import { cookies } from 'next/headers'

// Cached helper methods makes it easy to get the same value in many places
// without manually passing it around. This discourages passing it from Server
// Component to Server Component which minimizes risk of passing it to a Client
// Component.
export const getCurrentUser = cache(async () => {
  const token = cookies().get('AUTH_TOKEN')
  const decodedToken = await decryptAndValidate(token)
  // Don't include secret tokens or private information as public fields.
  // Use classes to avoid accidentally passing the whole object to the client.
  return new User(decodedToken.id)
})
```

data/user-dto.tsx
```
import 'server-only'
import { getCurrentUser } from './auth'

function canSeeUsername(viewer: User) {
  // Public info for now, but can change
  return true
}

function canSeePhoneNumber(viewer: User, team: string) {
  // Privacy rules
  return viewer.isAdmin || team === viewer.team
}

export async function getProfileDTO(slug: string) {
  // Don't pass values, read back cached values, also solves context and easier to make it lazy

  // use a database API that supports safe templating of queries
  const [rows] = await sql`SELECT * FROM user WHERE slug = ${slug}`
  const userData = rows[0]

  const currentUser = await getCurrentUser()

  // only return the data relevant for this query and not everything
  // <https://www.w3.org/2001/tag/doc/APIMinimization>
  return {
    username: canSeeUsername(currentUser) ? userData.username : null,
    phonenumber: canSeePhoneNumber(currentUser, userData.team)
      ? userData.phonenumber
      : null,
  }
}
```

app/page.tsx
```
import { getProfile } from '../../data/user'

export async function Page({ params: { slug } }) {
  // This page can now safely pass around this profile knowing
  // that it shouldn't contain anything sensitive.
  const profile = await getProfile(slug);
  ...
}
```

> **Good to know:** Secret keys should be stored in environment variables, but only the Data Access Layer should access `process.env`. This keeps secrets from being exposed to other parts of the application.
### Component-level data access[](https://nextjs.org/docs/app/guides/data-security#component-level-data-access)
For quick prototypes and iteration, database queries can be placed directly in Server Components.
This approach, however, makes it easier to accidentally expose private data to the client, for example:
app/page.tsx
```
import Profile from './components/profile.tsx'

export async function Page({ params: { slug } }) {
  const [rows] = await sql`SELECT * FROM user WHERE slug = ${slug}`
  const userData = rows[0]
  // EXPOSED: This exposes all the fields in userData to the client because
  // we are passing the data from the Server Component to the Client.
  return <Profile user={userData} />
}
```

app/ui/profile.tsx
```
'use client'

// BAD: This is a bad props interface because it accepts way more data than the
// Client Component needs and it encourages server components to pass all that
// data down. A better solution would be to accept a limited object with just
// the fields necessary for rendering the profile.
export default async function Profile({ user }: { user: User }) {
  return (
    <div>
      <h1>{user.name}</h1>
      ...
    </div>
  )
}
```

You should sanitize the data before passing it to the Client Component:
data/user.ts
```
import { sql } from './db'

export async function getUser(slug: string) {
  const [rows] = await sql`SELECT * FROM user WHERE slug = ${slug}`
  const user = rows[0]

  // Return only the public fields
  return {
    name: user.name,
  }
}
```

app/page.tsx
```
import { getUser } from '../data/user'
import Profile from './ui/profile'

export default async function Page({
  params: { slug },
}: {
  params: { slug: string }
}) {
  const publicProfile = await getUser(slug)
  return <Profile user={publicProfile} />
}
```
