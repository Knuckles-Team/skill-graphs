# Image Optimization
Last updated February 27, 2026
The Next.js [`<Image>`](https://nextjs.org/docs/app/api-reference/components/image) component extends the HTML `<img>` element to provide:
  * **Size optimization:** Automatically serving correctly sized images for each device, using modern image formats like WebP.
  * **Visual stability:** Preventing
  * **Faster page loads:** Only loading images when they enter the viewport using native browser lazy loading, with optional blur-up placeholders.
  * **Asset flexibility:** Resizing images on-demand, even images stored on remote servers.


To start using `<Image>`, import it from `next/image` and render it within your component.
app/page.tsx
TypeScript
JavaScript TypeScript
```
import Image from 'next/image'

export default function Page() {
  return <Image src="" alt="" />
}
```

The `src` property can be a [local](https://nextjs.org/docs/app/getting-started/images#local-images) or [remote](https://nextjs.org/docs/app/getting-started/images#remote-images) image.
> **🎥 Watch:** Learn more about how to use `next/image` →
