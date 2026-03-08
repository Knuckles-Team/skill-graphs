## Reference[](https://nextjs.org/docs/app/api-reference/file-conventions/layout#reference)
### Props[](https://nextjs.org/docs/app/api-reference/file-conventions/layout#props)
####  `children` (required)[](https://nextjs.org/docs/app/api-reference/file-conventions/layout#children-required)
Layout components should accept and use a `children` prop. During rendering, `children` will be populated with the route segments the layout is wrapping. These will primarily be the component of a child [Layout](https://nextjs.org/docs/app/api-reference/file-conventions/page) (if it exists) or [Page](https://nextjs.org/docs/app/api-reference/file-conventions/page), but could also be other special files like [Loading](https://nextjs.org/docs/app/api-reference/file-conventions/loading) or [Error](https://nextjs.org/docs/app/getting-started/error-handling) when applicable.
####  `params` (optional)[](https://nextjs.org/docs/app/api-reference/file-conventions/layout#params-optional)
A promise that resolves to an object containing the [dynamic route parameters](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes) object from the root segment down to that layout.
app/dashboard/[team]/layout.tsx
TypeScript
JavaScript TypeScript
```
export default async function Layout({
  children,
  params,
}: {
  children: React.ReactNode
  params: Promise<{ team: string }>
}) {
  const { team } = await params
}
```

Example Route | URL | `params`
---|---|---
`app/dashboard/[team]/layout.js` | `/dashboard/1` | `Promise<{ team: '1' }>`
`app/shop/[tag]/[item]/layout.js` | `/shop/1/2` | `Promise<{ tag: '1', item: '2' }>`
`app/blog/[...slug]/layout.js` | `/blog/1/2` | `Promise<{ slug: ['1', '2'] }>`
  * Since the `params` prop is a promise. You must use `async/await` or React's
    * In version 14 and earlier, `params` was a synchronous prop. To help with backwards compatibility, you can still access it synchronously in Next.js 15, but this behavior will be deprecated in the future.


### Layout Props Helper[](https://nextjs.org/docs/app/api-reference/file-conventions/layout#layout-props-helper)
You can type layouts with `LayoutProps` to get a strongly typed `params` and named slots inferred from your directory structure. `LayoutProps` is a globally available helper.
app/dashboard/layout.tsx
```
export default function Layout(props: LayoutProps<'/dashboard'>) {
  return (
    <section>
      {props.children}
      {/* If you have app/dashboard/@analytics, it appears as a typed slot: */}
      {/* {props.analytics} */}
    </section>
  )
}
```

> **Good to know** :
>   * Types are generated during `next dev`, `next build` or `next typegen`.
>   * After type generation, the `LayoutProps` helper is globally available. It doesn't need to be imported.
>

### Root Layout[](https://nextjs.org/docs/app/api-reference/file-conventions/layout#root-layout)
The `app` directory **must** include a **root layout** , which is the top-most layout in the root `app` directory. Typically, the root layout is `app/layout.js`.
app/layout.tsx
TypeScript
JavaScript TypeScript
```
export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html>
      <body>{children}</body>
    </html>
  )
}
```

  * The root layout **must** define `<html>` and `<body>` tags.
    * You should **not** manually add `<head>` tags such as `<title>` and `<meta>` to root layouts. Instead, you should use the [Metadata API](https://nextjs.org/docs/app/getting-started/metadata-and-og-images) which automatically handles advanced requirements such as streaming and de-duplicating `<head>` elements.
  * You can create **multiple root layouts**. Any layout without a `layout.js` above it is a root layout. Two common approaches:
    * Using [route groups](https://nextjs.org/docs/app/api-reference/file-conventions/route-groups) like `app/(shop)/layout.js` and `app/(marketing)/layout.js`
    * Omitting `app/layout.js` so layouts in subdirectories like `app/dashboard/layout.js` and `app/blog/layout.js` each become root layouts for their respective directories.
    * Navigating **across multiple root layouts** will cause a **full page load** (as opposed to a client-side navigation).
  * The root layout can be under a **dynamic segment** , for example when implementing [internationalization](https://nextjs.org/docs/app/guides/internationalization) with `app/[lang]/layout.js`.
