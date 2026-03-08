## Types[](https://nextjs.org/docs/app/api-reference/functions/generate-viewport#types)
You can add type safety to your viewport object by using the `Viewport` type. If you are using the [built-in TypeScript plugin](https://nextjs.org/docs/app/api-reference/config/typescript) in your IDE, you do not need to manually add the type, but you can still explicitly add it if you want.
###  `viewport` object[](https://nextjs.org/docs/app/api-reference/functions/generate-viewport#viewport-object)
```
import type { Viewport } from 'next'

export const viewport: Viewport = {
  themeColor: 'black',
}
```

###  `generateViewport` function[](https://nextjs.org/docs/app/api-reference/functions/generate-viewport#generateviewport-function-1)
#### Regular function[](https://nextjs.org/docs/app/api-reference/functions/generate-viewport#regular-function)
```
import type { Viewport } from 'next'

export function generateViewport(): Viewport {
  return {
    themeColor: 'black',
  }
}
```

#### With segment props[](https://nextjs.org/docs/app/api-reference/functions/generate-viewport#with-segment-props)
```
import type { Viewport } from 'next'

type Props = {
  params: Promise<{ id: string }>
  searchParams: Promise<{ [key: string]: string | string[] | undefined }>
}

export function generateViewport({ params, searchParams }: Props): Viewport {
  return {
    themeColor: 'black',
  }
}

export default function Page({ params, searchParams }: Props) {}
```

#### JavaScript Projects[](https://nextjs.org/docs/app/api-reference/functions/generate-viewport#javascript-projects)
For JavaScript projects, you can use JSDoc to add type safety.
```
/** @type {import("next").Viewport} */
export const viewport = {
  themeColor: 'black',
}
```
