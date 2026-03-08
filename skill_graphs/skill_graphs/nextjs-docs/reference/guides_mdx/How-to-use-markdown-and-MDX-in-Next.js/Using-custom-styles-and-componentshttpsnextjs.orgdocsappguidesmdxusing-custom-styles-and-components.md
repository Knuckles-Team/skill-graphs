## Using custom styles and components[](https://nextjs.org/docs/app/guides/mdx#using-custom-styles-and-components)
Markdown, when rendered, maps to native HTML elements. For example, writing the following markdown:
```
## This is a heading

This is a list in markdown:

- One
- Two
- Three
```

Generates the following HTML:
```
<h2>This is a heading</h2>

<p>This is a list in markdown:</p>

<ul>
  <li>One</li>
  <li>Two</li>
  <li>Three</li>
</ul>
```

To style your markdown, you can provide custom components that map to the generated HTML elements. Styles and components can be implemented globally, locally, and with shared layouts.
### Global styles and components[](https://nextjs.org/docs/app/guides/mdx#global-styles-and-components)
Adding styles and components in `mdx-components.tsx` will affect _all_ MDX files in your application.
mdx-components.tsx
TypeScript
JavaScript TypeScript
```
import type { MDXComponents } from 'mdx/types'
import Image, { ImageProps } from 'next/image'

// This file allows you to provide custom React components
// to be used in MDX files. You can import and use any
// React component you want, including inline styles,
// components from other libraries, and more.

const components = {
  // Allows customizing built-in components, e.g. to add styling.
  h1: ({ children }) => (
    <h1 style={{ color: 'red', fontSize: '48px' }}>{children}</h1>
  ),
  img: (props) => (
    <Image
      sizes="100vw"
      style={{ width: '100%', height: 'auto' }}
      {...(props as ImageProps)}
    />
  ),
} satisfies MDXComponents

export function useMDXComponents(): MDXComponents {
  return components
}
```

### Local styles and components[](https://nextjs.org/docs/app/guides/mdx#local-styles-and-components)
You can apply local styles and components to specific pages by passing them into imported MDX components. These will merge with and override [global styles and components](https://nextjs.org/docs/app/guides/mdx#global-styles-and-components).
app/mdx-page/page.tsx
TypeScript
JavaScript TypeScript
```
import Welcome from '@/markdown/welcome.mdx'

function CustomH1({ children }) {
  return <h1 style={{ color: 'blue', fontSize: '100px' }}>{children}</h1>
}

const overrideComponents = {
  h1: CustomH1,
}

export default function Page() {
  return <Welcome components={overrideComponents} />
}
```

### Shared layouts[](https://nextjs.org/docs/app/guides/mdx#shared-layouts)
To share a layout across MDX pages, you can use the [built-in layouts support](https://nextjs.org/docs/app/api-reference/file-conventions/layout) with the App Router.
app/mdx-page/layout.tsx
TypeScript
JavaScript TypeScript
```
export default function MdxLayout({ children }: { children: React.ReactNode }) {
  // Create any shared layout or styles here
  return <div style={{ color: 'blue' }}>{children}</div>
}
```

### Using Tailwind typography plugin[](https://nextjs.org/docs/app/guides/mdx#using-tailwind-typography-plugin)
If you are using
The plugin adds a set of `prose` classes that can be used to add typographic styles to content blocks that come from sources, like markdown.
[shared layouts](https://nextjs.org/docs/app/guides/mdx#shared-layouts) to add the `prose` you want.
app/mdx-page/layout.tsx
TypeScript
JavaScript TypeScript
```
export default function MdxLayout({ children }: { children: React.ReactNode }) {
  // Create any shared layout or styles here
  return (
    <div className="prose prose-headings:mt-8 prose-headings:font-semibold prose-headings:text-black prose-h1:text-5xl prose-h2:text-4xl prose-h3:text-3xl prose-h4:text-2xl prose-h5:text-xl prose-h6:text-lg dark:prose-headings:text-white">
      {children}
    </div>
  )
}
```
