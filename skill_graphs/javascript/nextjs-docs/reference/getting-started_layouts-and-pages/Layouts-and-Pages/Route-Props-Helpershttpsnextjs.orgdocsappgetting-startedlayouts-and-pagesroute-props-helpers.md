## Route Props Helpers[](https://nextjs.org/docs/app/getting-started/layouts-and-pages#route-props-helpers)
Next.js exposes utility types that infer `params` and named slots from your route structure:
  * [**PageProps**](https://nextjs.org/docs/app/api-reference/file-conventions/page#page-props-helper): Props for `page` components, including `params` and `searchParams`.
  * [**LayoutProps**](https://nextjs.org/docs/app/api-reference/file-conventions/layout#layout-props-helper): Props for `layout` components, including `children` and any named slots (e.g. folders like `@analytics`).


These are globally available helpers, generated when running either `next dev`, `next build` or [`next typegen`](https://nextjs.org/docs/app/api-reference/cli/next#next-typegen-options).
app/blog/[slug]/page.tsx
```
export default async function Page(props: PageProps<'/blog/[slug]'>) {
  const { slug } = await props.params
  return <h1>Blog post: {slug}</h1>
}
```

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

> **Good to know**
>   * Static routes resolve `params` to `{}`.
>   * `PageProps`, `LayoutProps` are global helpers — no imports required.
>   * Types are generated during `next dev`, `next build` or `next typegen`.
>
