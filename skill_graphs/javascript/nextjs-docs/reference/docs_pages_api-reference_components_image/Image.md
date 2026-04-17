# Image
Last updated February 27, 2026
The Next.js Image component extends the HTML `<img>` element for automatic image optimization.
app/page.js
```
import Image from 'next/image'

export default function Page() {
  return (
    <Image
      src="/profile.png"
      width={500}
      height={500}
      alt="Picture of the author"
    />
  )
}
```

> **Good to know** : If you are using a version of Next.js prior to 13, you'll want to use the [next/legacy/image](https://nextjs.org/docs/pages/api-reference/components/image-legacy) documentation since the component was renamed.
