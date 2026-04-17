# mdx-components.js
Last updated February 27, 2026
The `mdx-components.js|tsx` file is **required** to use [`@next/mdx` with App Router](https://nextjs.org/docs/app/guides/mdx) and will not work without it. Additionally, you can use it to [customize styles](https://nextjs.org/docs/app/guides/mdx#using-custom-styles-and-components).
Use the file `mdx-components.tsx` (or `.js`) in the root of your project to define MDX Components. For example, at the same level as `pages` or `app`, or inside `src` if applicable.
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
