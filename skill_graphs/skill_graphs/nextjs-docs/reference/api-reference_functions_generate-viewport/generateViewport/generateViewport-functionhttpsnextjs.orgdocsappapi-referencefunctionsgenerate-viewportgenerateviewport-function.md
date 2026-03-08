##  `generateViewport` function[](https://nextjs.org/docs/app/api-reference/functions/generate-viewport#generateviewport-function)
`generateViewport` should return a [`Viewport` object](https://nextjs.org/docs/app/api-reference/functions/generate-viewport#viewport-fields) containing one or more viewport fields.
layout.tsx | page.tsx
TypeScript
JavaScript TypeScript
```
export function generateViewport({ params }) {
  return {
    themeColor: '...',
  }
}
```

In TypeScript, the `params` argument can be typed via [`PageProps<'/route'>`](https://nextjs.org/docs/app/api-reference/file-conventions/page#page-props-helper) or [`LayoutProps<'/route'>`](https://nextjs.org/docs/app/api-reference/file-conventions/layout#layout-props-helper) depending on where `generateViewport` is defined.
> **Good to know** :
>   * If the viewport doesn't depend on runtime information, it should be defined using the static [`viewport` object](https://nextjs.org/docs/app/api-reference/functions/generate-viewport#the-viewport-object) rather than `generateViewport`.
>
