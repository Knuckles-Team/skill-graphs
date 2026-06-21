## Examples[](https://nextjs.org/docs/app/api-reference/file-conventions/parallel-routes#examples)
### With `useSelectedLayoutSegment(s)`[](https://nextjs.org/docs/app/api-reference/file-conventions/parallel-routes#with-useselectedlayoutsegments)
Both [`useSelectedLayoutSegment`](https://nextjs.org/docs/app/api-reference/functions/use-selected-layout-segment) and [`useSelectedLayoutSegments`](https://nextjs.org/docs/app/api-reference/functions/use-selected-layout-segments) accept a `parallelRoutesKey` parameter, which allows you to read the active route segment within a slot.
app/layout.tsx
TypeScript
JavaScript TypeScript
```
'use client'

import { useSelectedLayoutSegment } from 'next/navigation'

export default function Layout({ auth }: { auth: React.ReactNode }) {
  const loginSegment = useSelectedLayoutSegment('auth')
  // ...
}
```

When a user navigates to `app/@auth/login` (or `/login` in the URL bar), `loginSegment` will be equal to the string `"login"`.
### Conditional Routes[](https://nextjs.org/docs/app/api-reference/file-conventions/parallel-routes#conditional-routes)
You can use Parallel Routes to conditionally render routes based on certain conditions, such as user role. For example, to render a different dashboard page for the `/admin` or `/user` roles:
![Conditional routes diagram](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Fconditional-routes-ui.png&w=3840&q=75)![Conditional routes diagram](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Fconditional-routes-ui.png&w=3840&q=75)
app/dashboard/layout.tsx
TypeScript
JavaScript TypeScript
```
import { checkUserRole } from '@/lib/auth'

export default function Layout({
  user,
  admin,
}: {
  user: React.ReactNode
  admin: React.ReactNode
}) {
  const role = checkUserRole()
  return role === 'admin' ? admin : user
}
```

### Tab Groups[](https://nextjs.org/docs/app/api-reference/file-conventions/parallel-routes#tab-groups)
You can add a `layout` inside a slot to allow users to navigate the slot independently. This is useful for creating tabs.
For example, the `@analytics` slot has two subpages: `/page-views` and `/visitors`.
![Analytics slot with two subpages and a layout](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Fparallel-routes-tab-groups.png&w=3840&q=75)![Analytics slot with two subpages and a layout](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Fparallel-routes-tab-groups.png&w=3840&q=75)
Within `@analytics`, create a [`layout`](https://nextjs.org/docs/app/api-reference/file-conventions/layout) file to share the tabs between the two pages:
app/@analytics/layout.tsx
TypeScript
JavaScript TypeScript
```
import Link from 'next/link'

export default function Layout({ children }: { children: React.ReactNode }) {
  return (
    <>
      <nav>
        <Link href="/page-views">Page Views</Link>
        <Link href="/visitors">Visitors</Link>
      </nav>
      <div>{children}</div>
    </>
  )
}
```

### Modals[](https://nextjs.org/docs/app/api-reference/file-conventions/parallel-routes#modals)
Parallel Routes can be used together with [Intercepting Routes](https://nextjs.org/docs/app/api-reference/file-conventions/intercepting-routes) to create modals that support deep linking. This allows you to solve common challenges when building modals, such as:
  * Making the modal content **shareable through a URL**.
  * **Preserving context** when the page is refreshed, instead of closing the modal.
  * **Closing the modal on backwards navigation** rather than going to the previous route.
  * **Reopening the modal on forwards navigation**.


Consider the following UI pattern, where a user can open a login modal from a layout using client-side navigation, or access a separate `/login` page:
![Parallel Routes Diagram](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Fparallel-routes-auth-modal.png&w=3840&q=75)![Parallel Routes Diagram](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Fparallel-routes-auth-modal.png&w=3840&q=75)
To implement this pattern, start by creating a `/login` route that renders your **main** login page.
![Parallel Routes Diagram](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Fparallel-routes-modal-login-page.png&w=3840&q=75)![Parallel Routes Diagram](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Fparallel-routes-modal-login-page.png&w=3840&q=75)
app/login/page.tsx
TypeScript
JavaScript TypeScript
```
import { Login } from '@/app/ui/login'

export default function Page() {
  return <Login />
}
```

Then, inside the `@auth` slot, add [`default.js`](https://nextjs.org/docs/app/api-reference/file-conventions/default) file that returns `null`. This ensures that the modal is not rendered when it's not active.
app/@auth/default.tsx
TypeScript
JavaScript TypeScript
```
export default function Default() {
  return null
}
```

Inside your `@auth` slot, intercept the `/login` route by importing the `<Modal>` component and its children into the `@auth/(.)login/page.tsx` file, and updating the folder name to `/@auth/(.)login/page.tsx`.
app/@auth/(.)login/page.tsx
TypeScript
JavaScript TypeScript
```
import { Modal } from '@/app/ui/modal'
import { Login } from '@/app/ui/login'

export default function Page() {
  return (
    <Modal>
      <Login />
    </Modal>
  )
}
```

> **Good to know:**
>   * The convention `(.)` is used for intercepting routes. See [Intercepting Routes](https://nextjs.org/docs/app/api-reference/file-conventions/intercepting-routes#convention) docs for more information.
>   * By separating the `<Modal>` functionality from the modal content (`<Login>`), you can ensure any content inside the modal, e.g. [forms](https://nextjs.org/docs/app/guides/forms), are Server Components. See [Interleaving Client and Server Components](https://nextjs.org/docs/app/getting-started/server-and-client-components#examples#supported-pattern-passing-server-components-to-client-components-as-props) for more information.
>

#### Opening the modal[](https://nextjs.org/docs/app/api-reference/file-conventions/parallel-routes#opening-the-modal)
Now, you can leverage the Next.js router to open and close the modal. This ensures the URL is correctly updated when the modal is open, and when navigating backwards and forwards.
To open the modal, pass the `@auth` slot as a prop to the parent layout and render it alongside the `children` prop.
app/layout.tsx
TypeScript
JavaScript TypeScript
```
import Link from 'next/link'

export default function Layout({
  auth,
  children,
}: {
  auth: React.ReactNode
  children: React.ReactNode
}) {
  return (
    <>
      <nav>
        <Link href="/login">Open modal</Link>
      </nav>
      <div>{auth}</div>
      <div>{children}</div>
    </>
  )
}
```

When the user clicks the `<Link>`, the modal will open instead of navigating to the `/login` page. However, on refresh or initial load, navigating to `/login` will take the user to the main login page.
#### Closing the modal[](https://nextjs.org/docs/app/api-reference/file-conventions/parallel-routes#closing-the-modal)
You can close the modal by calling `router.back()` or by using the `Link` component.
app/ui/modal.tsx
TypeScript
JavaScript TypeScript
```
'use client'

import { useRouter } from 'next/navigation'

export function Modal({ children }: { children: React.ReactNode }) {
  const router = useRouter()

  return (
    <>
      <button
        onClick={() => {
          router.back()
        }}
      >
        Close modal
      </button>
      <div>{children}</div>
    </>
  )
}
```

When using the `Link` component to navigate away from a page that shouldn't render the `@auth` slot anymore, we need to make sure the parallel route matches to a component that returns `null`. For example, when navigating back to the root page, we create a `@auth/page.tsx` component:
app/ui/modal.tsx
TypeScript
JavaScript TypeScript
```
import Link from 'next/link'

export function Modal({ children }: { children: React.ReactNode }) {
  return (
    <>
      <Link href="/">Close modal</Link>
      <div>{children}</div>
    </>
  )
}
```

app/@auth/page.tsx
TypeScript
JavaScript TypeScript
```
export default function Page() {
  return null
}
```

Or if navigating to any other page (such as `/foo`, `/foo/bar`, etc), you can use a catch-all slot:
app/@auth/[...catchAll]/page.tsx
TypeScript
JavaScript TypeScript
```
export default function CatchAll() {
  return null
}
```

> **Good to know:**
>   * We use a catch-all route in our `@auth` slot to close the modal because of how parallel routes behave. Since client-side navigations to a route that no longer match the slot will remain visible, we need to match the slot to a route that returns `null` to close the modal.
>   * Other examples could include opening a photo modal in a gallery while also having a dedicated `/photo/[id]` page, or opening a shopping cart in a side modal.
>

### Loading and Error UI[](https://nextjs.org/docs/app/api-reference/file-conventions/parallel-routes#loading-and-error-ui)
Parallel Routes can be streamed independently, allowing you to define independent error and loading states for each route:
![Parallel routes enable custom error and loading states](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Fparallel-routes-cinematic-universe.png&w=3840&q=75)![Parallel routes enable custom error and loading states](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Fparallel-routes-cinematic-universe.png&w=3840&q=75)
See the [Loading UI](https://nextjs.org/docs/app/api-reference/file-conventions/loading) and [Error Handling](https://nextjs.org/docs/app/getting-started/error-handling) documentation for more information.
### [default.js API Reference for the default.js file.](https://nextjs.org/docs/app/api-reference/file-conventions/default)
[Previouspage.js](https://nextjs.org/docs/app/api-reference/file-conventions/page)[Nextproxy.js](https://nextjs.org/docs/app/api-reference/file-conventions/proxy)
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
