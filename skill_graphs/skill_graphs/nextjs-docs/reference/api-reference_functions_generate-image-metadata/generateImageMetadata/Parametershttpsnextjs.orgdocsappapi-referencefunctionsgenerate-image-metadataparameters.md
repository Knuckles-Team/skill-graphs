## Parameters[](https://nextjs.org/docs/app/api-reference/functions/generate-image-metadata#parameters)
`generateImageMetadata` function accepts the following parameters:
####  `params` (optional)[](https://nextjs.org/docs/app/api-reference/functions/generate-image-metadata#params-optional)
An object containing the [dynamic route parameters](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes) object from the root segment down to the segment `generateImageMetadata` is called from.
icon.tsx
TypeScript
JavaScript TypeScript
```
export function generateImageMetadata({
  params,
}: {
  params: { slug: string }
}) {
  // ...
}
```

Route | URL | `params`
---|---|---
`app/shop/icon.js` | `/shop` | `undefined`
`app/shop/[slug]/icon.js` | `/shop/1` | `{ slug: '1' }`
`app/shop/[tag]/[item]/icon.js` | `/shop/1/2` | `{ tag: '1', item: '2' }`
