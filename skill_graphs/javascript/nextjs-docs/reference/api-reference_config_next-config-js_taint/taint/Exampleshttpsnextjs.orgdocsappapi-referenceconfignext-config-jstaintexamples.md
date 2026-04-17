## Examples[](https://nextjs.org/docs/app/api-reference/config/next-config-js/taint#examples)
### Tainting an object reference[](https://nextjs.org/docs/app/api-reference/config/next-config-js/taint#tainting-an-object-reference)
In this case, the `getUserDetails` function returns data about a given user. We taint the user object reference, so that it cannot cross a Server-Client boundary. For example, assuming `UserCard` is a Client Component.
```
import { experimental_taintObjectReference } from 'react'

function getUserDetails(id: string): UserDetails {
  const user = await db.queryUserById(id)

  experimental_taintObjectReference(
    'Do not use the entire user info object. Instead, select only the fields you need.',
    user
  )

  return user
}
```

We can still access individual fields from the tainted `userDetails` object.
```
export async function ContactPage({
  params,
}: {
  params: Promise<{ id: string }>
}) {
  const { id } = await params
  const userDetails = await getUserDetails(id)

  return (
    <UserCard
      firstName={userDetails.firstName}
      lastName={userDetails.lastName}
    />
  )
}
```

Now, passing the entire object to the Client Component will throw an error.
```
export async function ContactPage({
  params,
}: {
  params: Promise<{ id: string }>
}) {
  const userDetails = await getUserDetails(id)

  // Throws an error
  return <UserCard user={userDetails} />
}
```

### Tainting a unique value[](https://nextjs.org/docs/app/api-reference/config/next-config-js/taint#tainting-a-unique-value)
In this case, we can access the server configuration by awaiting calls to `config.getConfigDetails`. However, the system configuration contains the `SERVICE_API_KEY` that we don't want to expose to clients.
We can taint the `config.SERVICE_API_KEY` value.
```
import { experimental_taintUniqueValue } from 'react'

function getSystemConfig(): SystemConfig {
  const config = await config.getConfigDetails()

  experimental_taintUniqueValue(
    'Do not pass configuration tokens to the client',
    config,
    config.SERVICE_API_KEY
  )

  return config
}
```

We can still access other properties of the `systemConfig` object.
```
export async function Dashboard() {
  const systemConfig = await getSystemConfig()

  return <ClientDashboard version={systemConfig.SERVICE_API_VERSION} />
}
```

However, passing `SERVICE_API_KEY` to `ClientDashboard` throws an error.
```
export async function Dashboard() {
  const systemConfig = await getSystemConfig()
  // Someone makes a mistake in a PR
  const version = systemConfig.SERVICE_API_KEY

  return <ClientDashboard version={version} />
}
```

Note that, even though, `systemConfig.SERVICE_API_KEY` is reassigned to a new variable. Passing it to a Client Component still throws an error.
Whereas, a value derived from a tainted unique value, will be exposed to the client.
```
export async function Dashboard() {
  const systemConfig = await getSystemConfig()
  // Someone makes a mistake in a PR
  const version = `version::${systemConfig.SERVICE_API_KEY}`

  return <ClientDashboard version={version} />
}
```

A better approach is to remove `SERVICE_API_KEY` from the data returned by `getSystemConfig`.
[PreviousstaticGeneration*](https://nextjs.org/docs/app/api-reference/config/next-config-js/staticGeneration)[NexttrailingSlash](https://nextjs.org/docs/app/api-reference/config/next-config-js/trailingSlash)
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
