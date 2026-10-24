## Advanced Props[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#advanced-props)
In some cases, you may need more advanced usage. The `<Image />` component optionally accepts the following advanced properties.
### style[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#style)
Allows
Note that all `layout` modes apply their own styles to the image element, and these automatic styles take precedence over the `style` prop.
Also keep in mind that the required `width` and `height` props can interact with your styling. If you use styling to modify an image's `width`, you must set the `height="auto"` style as well, or your image will be distorted.
### objectFit[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#objectfit)
Defines how the image will fit into its parent container when using `layout="fill"`.
This value is passed to the `src` image.
### objectPosition[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#objectposition)
Defines how the image is positioned within its parent element when using `layout="fill"`.
This value is passed to the
### onLoadingComplete[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#onloadingcomplete)
A callback function that is invoked once the image is completely loaded and the [placeholder](https://nextjs.org/docs/pages/api-reference/components/image-legacy#placeholder) has been removed.
The `onLoadingComplete` function accepts one parameter, an object with the following properties:
### loading[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#loading)
The loading behavior of the image. Defaults to `lazy`.
When `lazy`, defer loading the image until it reaches a calculated distance from the viewport.
When `eager`, load the image immediately.
### blurDataURL[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#blurdataurl)
A `src` image successfully loads. Only takes effect when combined with [`placeholder="blur"`](https://nextjs.org/docs/pages/api-reference/components/image-legacy#placeholder).
Must be a base64-encoded image. It will be enlarged and blurred, so a very small image (10px or less) is recommended. Including larger images as placeholders may harm your application performance.
Try it out:
You can also
### lazyBoundary[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#lazyboundary)
A string (with similar syntax to the margin property) that acts as the bounding box used to detect the intersection of the viewport with the image and trigger lazy [loading](https://nextjs.org/docs/pages/api-reference/components/image-legacy#loading). Defaults to `"200px"`.
If the image is nested in a scrollable parent element other than the root document, you will also need to assign the [lazyRoot](https://nextjs.org/docs/pages/api-reference/components/image-legacy#lazyroot) prop.
### lazyRoot[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#lazyroot)
A React `null` (the document viewport).
The Ref must point to a DOM element or a React component that
**Example pointing to a DOM element**
```
import Image from 'next/legacy/image'
import React from 'react'

const Example = () => {
  const lazyRoot = React.useRef(null)

  return (
    <div ref={lazyRoot} style={{ overflowX: 'scroll', width: '500px' }}>
      <Image lazyRoot={lazyRoot} src="/one.jpg" width="500" height="500" />
      <Image lazyRoot={lazyRoot} src="/two.jpg" width="500" height="500" />
    </div>
  )
}
```

**Example pointing to a React component**
```
import Image from 'next/legacy/image'
import React from 'react'

const Container = React.forwardRef((props, ref) => {
  return (
    <div ref={ref} style={{ overflowX: 'scroll', width: '500px' }}>
      {props.children}
    </div>
  )
})

const Example = () => {
  const lazyRoot = React.useRef(null)

  return (
    <Container ref={lazyRoot}>
      <Image lazyRoot={lazyRoot} src="/one.jpg" width="500" height="500" />
      <Image lazyRoot={lazyRoot} src="/two.jpg" width="500" height="500" />
    </Container>
  )
}
```

### unoptimized[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#unoptimized)
When true, the source image will be served as-is from the `src` instead of changing quality, size, or format. Defaults to `false`.
This is useful for images that do not benefit from optimization such as small images (less than 1KB), vector images (SVG), or animated images (GIF).
```
import Image from 'next/image'

const UnoptimizedImage = (props) => {
  return <Image {...props} unoptimized />
}
```

Since Next.js 12.3.0, this prop can be assigned to all images by updating `next.config.js` with the following configuration:
next.config.js
```
module.exports = {
  images: {
    unoptimized: true,
  },
}
```
