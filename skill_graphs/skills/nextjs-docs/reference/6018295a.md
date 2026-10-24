## Local images[](https://nextjs.org/docs/pages/getting-started/images#local-images)
You can store static files, like images and fonts, under a folder called [`public`](https://nextjs.org/docs/app/api-reference/file-conventions/public-folder) in the root directory. Files inside `public` can then be referenced by your code starting from the base URL (`/`).
![Folder structure showing app and public folders](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Fpublic-folder.png&w=3840&q=75)![Folder structure showing app and public folders](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Fpublic-folder.png&w=3840&q=75)
app/page.tsx
TypeScript
JavaScript TypeScript
```
import Image from 'next/image'

export default function Page() {
  return (
    <Image
      src="/profile.png"
      alt="Picture of the author"
      width={500}
      height={500}
    />
  )
}
```

If the image is statically imported, Next.js will automatically determine the intrinsic [`width`](https://nextjs.org/docs/app/api-reference/components/image#width-and-height) and [`height`](https://nextjs.org/docs/app/api-reference/components/image#width-and-height). These values are used to determine the image ratio and prevent
app/page.tsx
TypeScript
JavaScript TypeScript
```
import Image from 'next/image'
import ProfileImage from './profile.png'

export default function Page() {
  return (
    <Image
      src={ProfileImage}
      alt="Picture of the author"
      // width={500} automatically provided
      // height={500} automatically provided
      // blurDataURL="data:..." automatically provided
      // placeholder="blur" // Optional blur-up while loading
    />
  )
}
```
