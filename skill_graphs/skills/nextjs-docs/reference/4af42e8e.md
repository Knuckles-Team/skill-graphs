## Convention[](https://nextjs.org/docs/app/api-reference/file-conventions/parallel-routes#convention)
### Slots[](https://nextjs.org/docs/app/api-reference/file-conventions/parallel-routes#slots)
Parallel routes are created using named **slots**. Slots are defined with the `@folder` convention. For example, the following file structure defines two slots: `@analytics` and `@team`:
![Parallel Routes File-system Structure](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Fparallel-routes-file-system.png&w=3840&q=75)![Parallel Routes File-system Structure](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Fparallel-routes-file-system.png&w=3840&q=75)
Slots are passed as props to the shared parent layout. For the example above, the component in `app/layout.js` now accepts the `@analytics` and `@team` slots props, and can render them in parallel alongside the `children` prop:
app/layout.tsx
TypeScript
JavaScript TypeScript
```
export default function Layout({
  children,
  team,
  analytics,
}: {
  children: React.ReactNode
  analytics: React.ReactNode
  team: React.ReactNode
}) {
  return (
    <>
      {children}
      {team}
      {analytics}
    </>
  )
}
```

However, slots are **not** route segments and do not affect the URL structure. For example, for `/@analytics/views`, the URL will be `/views` since `@analytics` is a slot. Slots are combined with the regular [Page](https://nextjs.org/docs/app/api-reference/file-conventions/page) component to form the final page associated with the route segment. Because of this, you cannot have separate [static](https://nextjs.org/docs/app/guides/caching#static-rendering) and [dynamic](https://nextjs.org/docs/app/guides/caching#dynamic-rendering) slots at the same route segment level. If one slot is dynamic, all slots at that level must be dynamic.
> **Good to know** :
>   * The `children` prop is an implicit slot that does not need to be mapped to a folder. This means `app/page.js` is equivalent to `app/@children/page.js`.
>

###  `default.js`[](https://nextjs.org/docs/app/api-reference/file-conventions/parallel-routes#defaultjs)
You can define a `default.js` file to render as a fallback for unmatched slots during the initial load or full-page reload.
Consider the following folder structure. The `@team` slot has a `/settings` page, but `@analytics` does not.
![Parallel Routes unmatched routes](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Fparallel-routes-unmatched-routes.png&w=3840&q=75)![Parallel Routes unmatched routes](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Fparallel-routes-unmatched-routes.png&w=3840&q=75)
When navigating to `/settings`, the `@team` slot will render the `/settings` page while maintaining the currently active page for the `@analytics` slot.
On refresh, Next.js will render a `default.js` for `@analytics`. If `default.js` doesn't exist, a `404` is rendered instead.
Additionally, since `children` is an implicit slot, you also need to create a `default.js` file to render a fallback for `children` when Next.js cannot recover the active state of the parent page.
