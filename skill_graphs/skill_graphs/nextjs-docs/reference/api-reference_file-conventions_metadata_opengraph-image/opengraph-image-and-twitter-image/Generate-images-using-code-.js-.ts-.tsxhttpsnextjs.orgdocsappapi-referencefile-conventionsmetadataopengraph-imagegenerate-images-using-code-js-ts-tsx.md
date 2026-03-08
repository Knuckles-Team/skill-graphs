## Generate images using code (.js, .ts, .tsx)[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#generate-images-using-code-js-ts-tsx)
In addition to using [literal image files](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#image-files-jpg-png-gif), you can programmatically **generate** images using code.
Generate a route segment's shared image by creating an `opengraph-image` or `twitter-image` route that default exports a function.
File convention | Supported file types
---|---
`opengraph-image` |  `.js`, `.ts`, `.tsx`
`twitter-image` |  `.js`, `.ts`, `.tsx`
> **Good to know** :
>   * By default, generated images are [**statically optimized**](https://nextjs.org/docs/app/guides/caching#static-rendering) (generated at build time and cached) unless they use [Dynamic APIs](https://nextjs.org/docs/app/guides/caching#dynamic-rendering) or uncached data.
>   * You can generate multiple Images in the same file using [`generateImageMetadata`](https://nextjs.org/docs/app/api-reference/functions/generate-image-metadata).
>   * `opengraph-image.js` and `twitter-image.js` are special Route Handlers that is cached by default unless it uses a [Dynamic API](https://nextjs.org/docs/app/guides/caching#dynamic-apis) or [dynamic config](https://nextjs.org/docs/app/guides/caching#segment-config-options) option.
>

The easiest way to generate an image is to use the [ImageResponse](https://nextjs.org/docs/app/api-reference/functions/image-response) API from `next/og`.
app/about/opengraph-image.tsx
TypeScript
JavaScript TypeScript
```
import { ImageResponse } from 'next/og'
import { readFile } from 'node:fs/promises'
import { join } from 'node:path'

// Image metadata
export const alt = 'About Acme'
export const size = {
  width: 1200,
  height: 630,
}

export const contentType = 'image/png'

// Image generation
export default async function Image() {
  // Font loading, process.cwd() is Next.js project directory
  const interSemiBold = await readFile(
    join(process.cwd(), 'assets/Inter-SemiBold.ttf')
  )

  return new ImageResponse(
    (
      // ImageResponse JSX element
      <div
        style={{
          fontSize: 128,
          background: 'white',
          width: '100%',
          height: '100%',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
        }}
      >
        About Acme
      </div>
    ),
    // ImageResponse options
    {
      // For convenience, we can reuse the exported opengraph-image
      // size config to also set the ImageResponse's width and height.
      ...size,
      fonts: [
        {
          name: 'Inter',
          data: interSemiBold,
          style: 'normal',
          weight: 400,
        },
      ],
    }
  )
}
```

<head> output
```
<meta property="og:image" content="<generated>" />
<meta property="og:image:alt" content="About Acme" />
<meta property="og:image:type" content="image/png" />
<meta property="og:image:width" content="1200" />
<meta property="og:image:height" content="630" />
```

### Props[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#props)
The default export function receives the following props:
####  `params` (optional)[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#params-optional)
A promise that resolves to an object containing the [dynamic route parameters](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes) object from the root segment down to the segment `opengraph-image` or `twitter-image` is colocated in.
> **Good to know** : If you use [`generateImageMetadata`](https://nextjs.org/docs/app/api-reference/functions/generate-image-metadata), the function will also receive an `id` prop that is a promise resolving to the `id` value from one of the items returned by `generateImageMetadata`.
app/shop/[slug]/opengraph-image.tsx
TypeScript
JavaScript TypeScript
```
export default async function Image({
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
`app/shop/opengraph-image.js` | `/shop` | `undefined`
`app/shop/[slug]/opengraph-image.js` | `/shop/1` | `Promise<{ slug: '1' }>`
`app/shop/[tag]/[item]/opengraph-image.js` | `/shop/1/2` | `Promise<{ tag: '1', item: '2' }>`
### Returns[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#returns)
The default export function should return a `Blob` | `ArrayBuffer` | `TypedArray` | `DataView` | `ReadableStream` | `Response`.
> **Good to know** : `ImageResponse` satisfies this return type.
### Config exports[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#config-exports)
You can optionally configure the image's metadata by exporting `alt`, `size`, and `contentType` variables from `opengraph-image` or `twitter-image` route.
Option | Type
---|---
[`alt`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#alt) | `string`
[`size`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#size) | `{ width: number; height: number }`
[`contentType`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#contenttype) |  `string` -
####  `alt`[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#alt)
opengraph-image.tsx | twitter-image.tsx
TypeScript
JavaScript TypeScript
```
export const alt = 'My images alt text'

export default function Image() {}
```

<head> output
```
<meta property="og:image:alt" content="My images alt text" />
```

####  `size`[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#size)
opengraph-image.tsx | twitter-image.tsx
TypeScript
JavaScript TypeScript
```
export const size = { width: 1200, height: 630 }

export default function Image() {}
```

<head> output
```
<meta property="og:image:width" content="1200" />
<meta property="og:image:height" content="630" />
```

####  `contentType`[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#contenttype)
opengraph-image.tsx | twitter-image.tsx
TypeScript
JavaScript TypeScript
```
export const contentType = 'image/png'

export default function Image() {}
```

<head> output
```
<meta property="og:image:type" content="image/png" />
```

#### Route Segment Config[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#route-segment-config)
`opengraph-image` and `twitter-image` are specialized [Route Handlers](https://nextjs.org/docs/app/api-reference/file-conventions/route) that can use the same [route segment configuration](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config) options as Pages and Layouts.
### Examples[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#examples)
#### Using external data[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#using-external-data)
This example uses the `params` object and external data to generate the image.
> **Good to know** : By default, this generated image will be [statically optimized](https://nextjs.org/docs/app/guides/caching#static-rendering). You can configure the individual `fetch` [`options`](https://nextjs.org/docs/app/api-reference/functions/fetch) or route segments [options](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#revalidate) to change this behavior.
app/posts/[slug]/opengraph-image.tsx
TypeScript
JavaScript TypeScript
```
import { ImageResponse } from 'next/og'

export const alt = 'About Acme'
export const size = {
  width: 1200,
  height: 630,
}
export const contentType = 'image/png'

export default async function Image({
  params,
}: {
  params: Promise<{ slug: string }>
}) {
  const { slug } = await params
  const post = await fetch(`https://.../posts/${slug}`).then((res) =>
    res.json()
  )

  return new ImageResponse(
    (
      <div
        style={{
          fontSize: 48,
          background: 'white',
          width: '100%',
          height: '100%',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
        }}
      >
        {post.title}
      </div>
    ),
    {
      ...size,
    }
  )
}
```

#### Using Node.js runtime with local assets[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#using-nodejs-runtime-with-local-assets)
These examples use the Node.js runtime to fetch a local image from the file system and pass it to the `<img>` `src` attribute, either as a base64 string or an `ArrayBuffer`. Place the local asset relative to the project root, not the example source file.
app/opengraph-image.tsx
TypeScript
JavaScript TypeScript
```
import { ImageResponse } from 'next/og'
import { join } from 'node:path'
import { readFile } from 'node:fs/promises'

export default async function Image() {
  const logoData = await readFile(join(process.cwd(), 'logo.png'), 'base64')
  const logoSrc = `data:image/png;base64,${logoData}`

  return new ImageResponse(
    (
      <div
        style={{
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
        }}
      >
        <img src={logoSrc} height="100" />
      </div>
    )
  )
}
```

Passing an `ArrayBuffer` to the `src` attribute of an `<img>` element is not part of the HTML spec. The rendering engine used by `next/og` supports it, but because TypeScript definitions follow the spec, you need a `@ts-expect-error` directive or similar to use this
app/opengraph-image.tsx
TypeScript
JavaScript TypeScript
```
import { ImageResponse } from 'next/og'
import { join } from 'node:path'
import { readFile } from 'node:fs/promises'

export default async function Image() {
  const logoData = await readFile(join(process.cwd(), 'logo.png'))
  const logoSrc = Uint8Array.from(logoData).buffer

  return new ImageResponse(
    (
      <div
        style={{
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
        }}
      >
        {/* @ts-expect-error Satori accepts ArrayBuffer/typed arrays for <img src> at runtime */}
        <img src={logoSrc} height="100" />
      </div>
    )
  )
}
```
