## Viewport Fields[](https://nextjs.org/docs/app/api-reference/functions/generate-viewport#viewport-fields)
###  `themeColor`[](https://nextjs.org/docs/app/api-reference/functions/generate-viewport#themecolor)
Learn more about
**Simple theme color**
layout.tsx | page.tsx
TypeScript
JavaScript TypeScript
```
import type { Viewport } from 'next'

export const viewport: Viewport = {
  themeColor: 'black',
}
```

<head> output
```
<meta name="theme-color" content="black" />
```

**With media attribute**
layout.tsx | page.tsx
TypeScript
JavaScript TypeScript
```
import type { Viewport } from 'next'

export const viewport: Viewport = {
  themeColor: [
    { media: '(prefers-color-scheme: light)', color: 'cyan' },
    { media: '(prefers-color-scheme: dark)', color: 'black' },
  ],
}
```

<head> output
```
<meta name="theme-color" media="(prefers-color-scheme: light)" content="cyan" />
<meta name="theme-color" media="(prefers-color-scheme: dark)" content="black" />
```

###  `width`, `initialScale`, `maximumScale` and `userScalable`[](https://nextjs.org/docs/app/api-reference/functions/generate-viewport#width-initialscale-maximumscale-and-userscalable)
> **Good to know** : The `viewport` meta tag is automatically set, and manual configuration is usually unnecessary as the default is sufficient. However, the information is provided for completeness.
layout.tsx | page.tsx
TypeScript
JavaScript TypeScript
```
import type { Viewport } from 'next'

export const viewport: Viewport = {
  width: 'device-width',
  initialScale: 1,
  maximumScale: 1,
  userScalable: false,
  // Also supported but less commonly used
  // interactiveWidget: 'resizes-visual',
}
```

<head> output
```
<meta
  name="viewport"
  content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no"
/>
```

###  `colorScheme`[](https://nextjs.org/docs/app/api-reference/functions/generate-viewport#colorscheme)
Learn more about
layout.tsx | page.tsx
TypeScript
JavaScript TypeScript
```
import type { Viewport } from 'next'

export const viewport: Viewport = {
  colorScheme: 'dark',
}
```

<head> output
```
<meta name="color-scheme" content="dark" />
```
