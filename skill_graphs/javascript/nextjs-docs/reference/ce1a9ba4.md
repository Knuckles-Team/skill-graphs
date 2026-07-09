## Exports[](https://nextjs.org/docs/app/api-reference/file-conventions/mdx-components#exports)
###  `useMDXComponents` function[](https://nextjs.org/docs/app/api-reference/file-conventions/mdx-components#usemdxcomponents-function)
The file must export a single function named `useMDXComponents`. This function does not accept any arguments.
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
