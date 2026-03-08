## Supported Features[](https://nextjs.org/docs/pages/guides/static-exports#supported-features-1)
The majority of core Next.js features needed to build a static site are supported, including:
  * [Dynamic Routes when using `getStaticPaths`](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes)
  * Prefetching with `next/link`
  * Preloading JavaScript
  * [Dynamic Imports](https://nextjs.org/docs/pages/guides/lazy-loading)
  * Any styling options (e.g. CSS Modules, styled-jsx)
  * [Client-side data fetching](https://nextjs.org/docs/pages/building-your-application/data-fetching/client-side)
  * [`getStaticProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props)
  * [`getStaticPaths`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-paths)


### Image Optimization[](https://nextjs.org/docs/pages/guides/static-exports#image-optimization)
[Image Optimization](https://nextjs.org/docs/app/api-reference/components/image) through `next/image` can be used with a static export by defining a custom image loader in `next.config.js`. For example, you can optimize images with a service like Cloudinary:
next.config.js
```
/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'export',
  images: {
    loader: 'custom',
    loaderFile: './my-loader.ts',
  },
}

module.exports = nextConfig
```

This custom loader will define how to fetch images from a remote source. For example, the following loader will construct the URL for Cloudinary:
my-loader.ts
TypeScript
JavaScript TypeScript
```
export default function cloudinaryLoader({
  src,
  width,
  quality,
}: {
  src: string
  width: number
  quality?: number
}) {
  const params = ['f_auto', 'c_limit', `w_${width}`, `q_${quality || 'auto'}`]
  return `https://res.cloudinary.com/demo/image/upload/${params.join(
    ','
  )}${src}`
}
```

You can then use `next/image` in your application, defining relative paths to the image in Cloudinary:
app/page.tsx
TypeScript
JavaScript TypeScript
```
import Image from 'next/image'

export default function Page() {
  return <Image alt="turtles" src="/turtles.jpg" width={300} height={300} />
}
```
