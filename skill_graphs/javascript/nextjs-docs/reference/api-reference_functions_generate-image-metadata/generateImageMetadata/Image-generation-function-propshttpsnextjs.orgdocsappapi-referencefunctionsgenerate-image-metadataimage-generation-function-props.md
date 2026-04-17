## Image generation function props[](https://nextjs.org/docs/app/api-reference/functions/generate-image-metadata#image-generation-function-props)
When using `generateImageMetadata`, the default export image generation function receives the following props:
####  `id`[](https://nextjs.org/docs/app/api-reference/functions/generate-image-metadata#id)
A promise that resolves to the `id` value from one of the items returned by `generateImageMetadata`. The `id` will be a `string` or `number` depending on what was returned from `generateImageMetadata`.
icon.tsx
TypeScript
JavaScript TypeScript
```
export default async function Icon({ id }: { id: Promise<string | number> }) {
  const iconId = await id
  // Use iconId to generate the image
}
```

####  `params` (optional)[](https://nextjs.org/docs/app/api-reference/functions/generate-image-metadata#params-optional-1)
A promise that resolves to an object containing the [dynamic route parameters](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes) from the root segment down to the segment the image is colocated in.
icon.tsx
TypeScript
JavaScript TypeScript
```
export default async function Icon({
  params,
}: {
  params: Promise<{ slug: string }>
}) {
  const { slug } = await params
  // Use slug to generate the image
}
```

### Examples[](https://nextjs.org/docs/app/api-reference/functions/generate-image-metadata#examples)
#### Using external data[](https://nextjs.org/docs/app/api-reference/functions/generate-image-metadata#using-external-data)
This example uses the `params` object and external data to generate multiple [Open Graph images](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image) for a route segment.
app/products/[id]/opengraph-image.tsx
TypeScript
JavaScript TypeScript
```
import { ImageResponse } from 'next/og'
import { getCaptionForImage, getOGImages } from '@/app/utils/images'

export async function generateImageMetadata({
  params,
}: {
  params: { id: string }
}) {
  const images = await getOGImages(params.id)

  return images.map((image, idx) => ({
    id: idx,
    size: { width: 1200, height: 600 },
    alt: image.text,
    contentType: 'image/png',
  }))
}

export default async function Image({
  params,
  id,
}: {
  params: Promise<{ id: string }>
  id: Promise<number>
}) {
  const productId = (await params).id
  const imageId = await id
  const text = await getCaptionForImage(productId, imageId)

  return new ImageResponse(
    (
      <div
        style={
          {
            // ...
          }
        }
      >
        {text}
      </div>
    )
  )
}
```
