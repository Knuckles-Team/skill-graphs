## Mutating Data[](https://nextjs.org/docs/app/guides/data-security#mutating-data)
Next.js handles mutations with
### Built-in Server Actions Security features[](https://nextjs.org/docs/app/guides/data-security#built-in-server-actions-security-features)
By default, when a Server Action is created and exported, it creates a public HTTP endpoint and should be treated with the same security assumptions and authorization checks. This means, even if a Server Action or utility function is not imported elsewhere in your code, it's still publicly accessible.
To improve security, Next.js has the following built-in features:
  * **Secure action IDs:** Next.js creates encrypted, non-deterministic IDs to allow the client to reference and call the Server Action. These IDs are periodically recalculated between builds for enhanced security.
  * **Dead code elimination:** Unused Server Actions (referenced by their IDs) are removed from client bundle to avoid public access.


> **Good to know** :
> The IDs are created during compilation and are cached for a maximum of 14 days. They will be regenerated when a new build is initiated or when the build cache is invalidated. This security improvement reduces the risk in cases where an authentication layer is missing. However, you should still treat Server Actions like public HTTP endpoints.
```
// app/actions.js
'use server'

// If this action **is** used in our application, Next.js
// will create a secure ID to allow the client to reference
// and call the Server Action.
export async function updateUserAction(formData) {}

// If this action **is not** used in our application, Next.js
// will automatically remove this code during `next build`
// and will not create a public endpoint.
export async function deleteUserAction(formData) {}
```

### Validating client input[](https://nextjs.org/docs/app/guides/data-security#validating-client-input)
You should always validate input from client, as they can be easily modified. For example, form data, URL parameters, headers, and searchParams:
app/page.tsx
```
// BAD: Trusting searchParams directly
export default async function Page({ searchParams }) {
  const isAdmin = searchParams.get('isAdmin')
  if (isAdmin === 'true') {
    // Vulnerable: relies on untrusted client data
    return <AdminPanel />
  }
}

// GOOD: Re-verify every time
import { cookies } from 'next/headers'
import { verifyAdmin } from './auth'

export default async function Page() {
  const token = cookies().get('AUTH_TOKEN')
  const isAdmin = await verifyAdmin(token)

  if (isAdmin) {
    return <AdminPanel />
  }
}
```

### Authentication and authorization[](https://nextjs.org/docs/app/guides/data-security#authentication-and-authorization)
You should always ensure that a user is authorized to perform an action. For example:
app/actions.ts
```
'use server'

import { auth } from './lib'

export function addItem() {
  const { user } = auth()
  if (!user) {
    throw new Error('You must be signed in to perform this action')
  }

  // ...
}
```

Learn more about [Authentication](https://nextjs.org/docs/app/guides/authentication) in Next.js.
### Closures and encryption[](https://nextjs.org/docs/app/guides/data-security#closures-and-encryption)
Defining a Server Action inside a component creates a `publish` action has access to the `publishVersion` variable:
app/page.tsx
TypeScript
JavaScript TypeScript
```
export default async function Page() {
  const publishVersion = await getLatestVersion();

  async function publish() {
    "use server";
    if (publishVersion !== await getLatestVersion()) {
      throw new Error('The version has changed since pressing publish');
    }
    ...
  }

  return (
    <form>
      <button formAction={publish}>Publish</button>
    </form>
  );
}
```

Closures are useful when you need to capture a _snapshot_ of data (e.g. `publishVersion`) at the time of rendering so that it can be used later when the action is invoked.
However, for this to happen, the captured variables are sent to the client and back to the server when the action is invoked. To prevent sensitive data from being exposed to the client, Next.js automatically encrypts the closed-over variables. A new private key is generated for each action every time a Next.js application is built. This means actions can only be invoked for a specific build.
> **Good to know:** We don't recommend relying on encryption alone to prevent sensitive values from being exposed on the client.
### Overwriting encryption keys (advanced)[](https://nextjs.org/docs/app/guides/data-security#overwriting-encryption-keys-advanced)
When **self-hosting** your Next.js application across multiple servers, each server instance may end up with a different encryption key, leading to potential inconsistencies.
To mitigate this, you can overwrite the encryption key using the `process.env.NEXT_SERVER_ACTIONS_ENCRYPTION_KEY` environment variable. Specifying this variable ensures that your encryption keys are persistent across builds, and all server instances use the same key.
The key must be a base64-encoded value whose decoded length matches a valid AES key size (16, 24, or 32 bytes). Next.js generates 32-byte keys by default. You can generate a compatible key using your platform’s cryptographic tools, for example:
```
openssl rand -base64 32
```

This is an advanced use case where consistent encryption behavior across multiple deployments is critical for your application. Follow standard security practices such as key rotation and signing. See the [Self-Hosting guide](https://nextjs.org/docs/app/guides/self-hosting#server-functions-encryption-key) for deployment-specific considerations.
### Allowed origins (advanced)[](https://nextjs.org/docs/app/guides/data-security#allowed-origins-advanced)
Since Server Actions can be invoked in a `<form>` element, this opens them up to
Behind the scenes, Server Actions use the `POST` method, and only this HTTP method is allowed to invoke them. This prevents most CSRF vulnerabilities in modern browsers, particularly with
As an additional protection, Server Actions in Next.js also compare the `X-Forwarded-Host`). If these don't match, the request will be aborted. In other words, Server Actions can only be invoked on the same host as the page that hosts it.
For large applications that use reverse proxies or multi-layered backend architectures (where the server API differs from the production domain), it's recommended to use the configuration option [`serverActions.allowedOrigins`](https://nextjs.org/docs/app/api-reference/config/next-config-js/serverActions) option to specify a list of safe origins. The option accepts an array of strings.
next.config.js
```
/** @type {import('next').NextConfig} */
module.exports = {
  experimental: {
    serverActions: {
      allowedOrigins: ['my-proxy.com', '*.my-proxy.com'],
    },
  },
}
```

Learn more about [Security and Server Actions](https://nextjs.org/blog/security-nextjs-server-components-actions).
### Avoiding side-effects during rendering[](https://nextjs.org/docs/app/guides/data-security#avoiding-side-effects-during-rendering)
Mutations (e.g. logging out users, updating databases, invalidating caches) should never be a side-effect, either in Server or Client Components. Next.js explicitly prevents setting cookies or triggering cache revalidation within render methods to avoid unintended side effects.
app/page.tsx
```
// BAD: Triggering a mutation during rendering
export default async function Page({ searchParams }) {
  if (searchParams.get('logout')) {
    cookies().delete('AUTH_TOKEN')
  }

  return <UserProfile />
}
```

Instead, you should use Server Actions to handle mutations.
app/page.tsx
```
// GOOD: Using Server Actions to handle mutations
import { logout } from './actions'

export default function Page() {
  return (
    <>
      <UserProfile />
      <form action={logout}>
        <button type="submit">Logout</button>
      </form>
    </>
  )
}
```

> **Good to know:** Next.js uses `POST` requests to handle mutations. This prevents accidental side-effects from GET requests, reducing Cross-Site Request Forgery (CSRF) risks.
