## Generate icons using code (.js, .ts, .tsx)[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#generate-icons-using-code-js-ts-tsx)
In addition to using [literal image files](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#image-files-ico-jpg-png), you can programmatically **generate** icons using code.
Generate an app icon by creating an `icon` or `apple-icon` route that default exports a function.
File convention | Supported file types
---|---
`icon` |  `.js`, `.ts`, `.tsx`
`apple-icon` |  `.js`, `.ts`, `.tsx`
The easiest way to generate an icon is to use the [`ImageResponse`](https://nextjs.org/docs/app/api-reference/functions/image-response) API from `next/og`.
app/icon.tsx
TypeScript
JavaScript TypeScript
```
import { ImageResponse } from 'next/og'

// Image metadata
export const size = {
  width: 32,
  height: 32,
}
export const contentType = 'image/png'

// Image generation
export default function Icon() {
  return new ImageResponse(
    (
      // ImageResponse JSX element
      <div
        style={{
          fontSize: 24,
          background: 'black',
          width: '100%',
          height: '100%',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          color: 'white',
        }}
      >
        A
      </div>
    ),
    // ImageResponse options
    {
      // For convenience, we can reuse the exported icons size metadata
      // config to also set the ImageResponse's width and height.
      ...size,
    }
  )
}
```

<head> output
```
<link rel="icon" href="/icon?<generated>" type="image/png" sizes="32x32" />
```

> **Good to know** :
>   * By default, generated icons are [**statically optimized**](https://nextjs.org/docs/app/guides/caching#static-rendering) (generated at build time and cached) unless they use [Dynamic APIs](https://nextjs.org/docs/app/guides/caching#dynamic-rendering) or uncached data.
>   * You can generate multiple icons in the same file using [`generateImageMetadata`](https://nextjs.org/docs/app/api-reference/functions/generate-image-metadata).
>   * You cannot generate a `favicon` icon. Use [`icon`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#icon) or a [favicon.ico](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#favicon) file instead.
>   * App icons are special Route Handlers that are cached by default unless they use a [Dynamic API](https://nextjs.org/docs/app/guides/caching#dynamic-apis) or [dynamic config](https://nextjs.org/docs/app/guides/caching#segment-config-options) option.
>

### Props[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#props)
The default export function receives the following props:
####  `params` (optional)[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#params-optional)
A promise that resolves to an object containing the [dynamic route parameters](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes) object from the root segment down to the segment `icon` or `apple-icon` is colocated in.
> **Good to know** : If you use [`generateImageMetadata`](https://nextjs.org/docs/app/api-reference/functions/generate-image-metadata), the function will also receive an `id` prop that is a promise resolving to the `id` value from one of the items returned by `generateImageMetadata`.
app/shop/[slug]/icon.tsx
TypeScript
JavaScript TypeScript
```
export default async function Icon({
  params,
}: {
  params: Promise<{ slug: string }>
}) {
  const { slug } = await params
  // ...
}
```

Route | URL | `params`
---|---|---
`app/shop/icon.js` | `/shop` | `undefined`
`app/shop/[slug]/icon.js` | `/shop/1` | `Promise<{ slug: '1' }>`
`app/shop/[tag]/[item]/icon.js` | `/shop/1/2` | `Promise<{ tag: '1', item: '2' }>`
### Returns[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#returns)
The default export function should return a `Blob` | `ArrayBuffer` | `TypedArray` | `DataView` | `ReadableStream` | `Response`.
> **Good to know** : `ImageResponse` satisfies this return type.
### Config exports[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#config-exports)
You can optionally configure the icon's metadata by exporting `size` and `contentType` variables from the `icon` or `apple-icon` route.
Option | Type
---|---
[`size`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#size) | `{ width: number; height: number }`
[`contentType`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#contenttype) |  `string` -
####  `size`[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#size)
icon.tsx | apple-icon.tsx
TypeScript
JavaScript TypeScript
```
export const size = { width: 32, height: 32 }

export default function Icon() {}
```

<head> output
```
<link rel="icon" sizes="32x32" />
```

####  `contentType`[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#contenttype)
icon.tsx | apple-icon.tsx
TypeScript
JavaScript TypeScript
```
export const contentType = 'image/png'

export default function Icon() {}
```

<head> output
```
<link rel="icon" type="image/png" />
```

#### Route Segment Config[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#route-segment-config)
`icon` and `apple-icon` are specialized [Route Handlers](https://nextjs.org/docs/app/api-reference/file-conventions/route) that can use the same [route segment configuration](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config) options as Pages and Layouts.
