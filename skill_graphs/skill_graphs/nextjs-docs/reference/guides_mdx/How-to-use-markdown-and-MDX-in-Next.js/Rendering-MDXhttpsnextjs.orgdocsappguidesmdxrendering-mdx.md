## Rendering MDX[](https://nextjs.org/docs/app/guides/mdx#rendering-mdx)
You can render MDX using Next.js's file based routing or by importing MDX files into other pages.
### Using file based routing[](https://nextjs.org/docs/app/guides/mdx#using-file-based-routing)
When using file based routing, you can use MDX pages like any other page.
In App Router apps, that includes being able to use [metadata](https://nextjs.org/docs/app/getting-started/metadata-and-og-images).
Create a new MDX page within the `/app` directory:
```
  my-project
  ├── app
  │   └── mdx-page
  │       └── page.(mdx/md)
  |── mdx-components.(tsx/js)
  └── package.json
```

You can use MDX in these files, and even import React components, directly inside your MDX page:
```
import { MyComponent } from 'my-component'

# Welcome to my MDX page!

This is some **bold** and _italics_ text.

This is a list in markdown:

- One
- Two
- Three

Checkout my React component:

<MyComponent />
```

Navigating to the `/mdx-page` route should display your rendered MDX page.
### Using imports[](https://nextjs.org/docs/app/guides/mdx#using-imports)
Create a new page within the `/app` directory and an MDX file wherever you'd like:
```
  .
  ├── app/
  │   └── mdx-page/
  │       └── page.(tsx/js)
  ├── markdown/
  │   └── welcome.(mdx/md)
  ├── mdx-components.(tsx/js)
  └── package.json
```

You can use MDX in these files, and even import React components, directly inside your MDX page:
Import the MDX file inside the page to display the content:
app/mdx-page/page.tsx
TypeScript
JavaScript TypeScript
```
import Welcome from '@/markdown/welcome.mdx'

export default function Page() {
  return <Welcome />
}
```

Navigating to the `/mdx-page` route should display your rendered MDX page.
### Using dynamic imports[](https://nextjs.org/docs/app/guides/mdx#using-dynamic-imports)
You can import dynamic MDX components instead of using filesystem routing for MDX files.
For example, you can have a dynamic route segment which loads MDX components from a separate directory:
![Route segments for dynamic MDX components](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Fmdx-files.png&w=3840&q=75)![Route segments for dynamic MDX components](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Fmdx-files.png&w=3840&q=75)
[`generateStaticParams`](https://nextjs.org/docs/app/api-reference/functions/generate-static-params) can be used to prerender the provided routes. By marking `dynamicParams` as `false`, accessing a route not defined in `generateStaticParams` will 404.
app/blog/[slug]/page.tsx
TypeScript
JavaScript TypeScript
```
export default async function Page({
  params,
}: {
  params: Promise<{ slug: string }>
}) {
  const { slug } = await params
  const { default: Post } = await import(`@/content/${slug}.mdx`)

  return <Post />
}

export function generateStaticParams() {
  return [{ slug: 'welcome' }, { slug: 'about' }]
}

export const dynamicParams = false
```

> **Good to know** : Ensure you specify the `.mdx` file extension in your import. While it is not required to use [module path aliases](https://nextjs.org/docs/app/getting-started/installation#set-up-absolute-imports-and-module-path-aliases) (e.g., `@/content`), it does simplify your import path.
