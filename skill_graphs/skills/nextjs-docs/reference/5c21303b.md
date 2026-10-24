## Rendering MDX[](https://nextjs.org/docs/pages/guides/mdx#rendering-mdx)
You can render MDX using Next.js's file based routing or by importing MDX files into other pages.
### Using file based routing[](https://nextjs.org/docs/pages/guides/mdx#using-file-based-routing)
When using file based routing, you can use MDX pages like any other page.
Create a new MDX page within the `/pages` directory:
```
  my-project
  |── mdx-components.(tsx/js)
  ├── pages
  │   └── mdx-page.(mdx/md)
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
### Using imports[](https://nextjs.org/docs/pages/guides/mdx#using-imports)
Create a new page within the `/pages` directory and an MDX file wherever you'd like:
```
  .
  ├── markdown/
  │   └── welcome.(mdx/md)
  ├── pages/
  │   └── mdx-page.(tsx/js)
  ├── mdx-components.(tsx/js)
  └── package.json
```

You can use MDX in these files, and even import React components, directly inside your MDX page:
Import the MDX file inside the page to display the content:
pages/mdx-page.tsx
TypeScript
JavaScript TypeScript
```
import Welcome from '@/markdown/welcome.mdx'

export default function Page() {
  return <Welcome />
}
```

Navigating to the `/mdx-page` route should display your rendered MDX page.
