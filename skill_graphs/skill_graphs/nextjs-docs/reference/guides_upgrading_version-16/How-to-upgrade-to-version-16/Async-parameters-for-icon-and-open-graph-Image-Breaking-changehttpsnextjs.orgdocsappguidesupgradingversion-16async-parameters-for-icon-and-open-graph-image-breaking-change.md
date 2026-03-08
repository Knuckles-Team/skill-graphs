## Async parameters for icon, and open-graph Image (Breaking change)[](https://nextjs.org/docs/app/guides/upgrading/version-16#async-parameters-for-icon-and-open-graph-image-breaking-change)
> The props passed to the image generating functions in `opengraph-image`, `twitter-image`, `icon`, and `apple-icon`, are now Promises.
In previous versions, both the `Image` (image generation function), and the `generateImageMetadata` received a `params` object. The `id` returned by `generateImageMetadata` was passed as a string to the image generation function.
app/shop/[slug]/opengraph-image.js
```
// Next.js 15 - synchronous params access
export function generateImageMetadata({ params }) {
  const { slug } = params
  return [{ id: '1' }, { id: '2' }]
}

// Next.js 15 - synchronous params and id access
export default function Image({ params, id }) {
  const slug = params.slug
  const imageId = id // string
  // ...
}
```

Starting with **Next.js 16** , to align with the [Async Request APIs](https://nextjs.org/docs/app/guides/upgrading/version-16#async-request-apis-breaking-change) change, the image generating function now receives `params` and `id` as promises. The `generateImageMetadata` function continues to receive synchronous `params`.
app/shop/[slug]/opengraph-image.js
```
export async function generateImageMetadata({ params }) {
  const { slug } = params
  return [{ id: '1' }, { id: '2' }]
}

// Next.js 16 - asynchronous params and id access
export default async function Image({ params, id }) {
  const { slug } = await params // params now async
  const imageId = await id // id is now Promise<string> when using generateImageMetadata
  // ...
}
```
