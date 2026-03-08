## Functions[](https://nextjs.org/docs/pages/api-reference/components/image#functions)
###  `getImageProps`[](https://nextjs.org/docs/pages/api-reference/components/image#getimageprops)
The `getImageProps` function can be used to get the props that would be passed to the underlying `<img>` element, and instead pass them to another component, style, canvas, etc.
```
import { getImageProps } from 'next/image'

const { props } = getImageProps({
  src: 'https://example.com/image.jpg',
  alt: 'A scenic mountain view',
  width: 1200,
  height: 800,
})

function ImageWithCaption() {
  return (
    <figure>
      <img {...props} />
      <figcaption>A scenic mountain view</figcaption>
    </figure>
  )
}
```

This also avoid calling React `useState()` so it can lead to better performance, but it cannot be used with the [`placeholder`](https://nextjs.org/docs/pages/api-reference/components/image#placeholder) prop because the placeholder will never be removed.
