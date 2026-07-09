# Image Component
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
