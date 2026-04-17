## Add an `mdx-components.tsx` file[](https://nextjs.org/docs/pages/guides/mdx#add-an-mdx-componentstsx-file)
Create an `mdx-components.tsx` (or `.js`) file in the root of your project to define global MDX Components. For example, at the same level as `pages` or `app`, or inside `src` if applicable.
mdx-components.tsx
TypeScript
JavaScript TypeScript
```
import type { MDXComponents } from 'mdx/types'

const components: MDXComponents = {}

export function useMDXComponents(): MDXComponents {
  return components
}
```

> **Good to know** :
>   * `mdx-components.tsx` is **required** to use `@next/mdx` with App Router and will not work without it.
>   * Learn more about the [`mdx-components.tsx` file convention](https://nextjs.org/docs/app/api-reference/file-conventions/mdx-components).
>   * Learn how to [use custom styles and components](https://nextjs.org/docs/pages/guides/mdx#using-custom-styles-and-components).
>
