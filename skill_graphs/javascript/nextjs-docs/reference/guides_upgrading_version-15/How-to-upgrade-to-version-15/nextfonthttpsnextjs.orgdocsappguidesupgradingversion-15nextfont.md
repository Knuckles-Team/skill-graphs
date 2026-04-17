##  `next/font`[](https://nextjs.org/docs/app/guides/upgrading/version-15#nextfont)
The `@next/font` package has been removed in favor of the built-in [`next/font`](https://nextjs.org/docs/app/api-reference/components/font). A [codemod is available](https://nextjs.org/docs/app/guides/upgrading/codemods#built-in-next-font) to safely and automatically rename your imports.
app/layout.js
```
// Before
import { Inter } from '@next/font/google'

// After
import { Inter } from 'next/font/google'
```
