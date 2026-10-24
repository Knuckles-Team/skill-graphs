## Optional Props[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#optional-props)
The `<Image />` component accepts a number of additional properties beyond those which are required. This section describes the most commonly-used properties of the Image component. Find details about more rarely-used properties in the [Advanced Props](https://nextjs.org/docs/pages/api-reference/components/image-legacy#advanced-props) section.
### layout[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#layout)
The layout behavior of the image as the viewport changes size.
`layout` | Behavior | `srcSet` | `sizes` | Has wrapper and sizer
---|---|---|---|---
`intrinsic` (default) | Scale _down_ to fit width of container, up to image size |  `1x`, `2x` (based on [imageSizes](https://nextjs.org/docs/pages/api-reference/components/image-legacy#image-sizes)) | N/A | yes
`fixed` | Sized to `width` and `height` exactly |  `1x`, `2x` (based on [imageSizes](https://nextjs.org/docs/pages/api-reference/components/image-legacy#image-sizes)) | N/A | yes
`responsive` | Scale to fit width of container |  `640w`, `750w`, ... `2048w`, `3840w` (based on [imageSizes](https://nextjs.org/docs/pages/api-reference/components/image-legacy#image-sizes) and [deviceSizes](https://nextjs.org/docs/pages/api-reference/components/image-legacy#device-sizes)) | `100vw` | yes
`fill` | Grow in both X and Y axes to fill container |  `640w`, `750w`, ... `2048w`, `3840w` (based on [imageSizes](https://nextjs.org/docs/pages/api-reference/components/image-legacy#image-sizes) and [deviceSizes](https://nextjs.org/docs/pages/api-reference/components/image-legacy#device-sizes)) | `100vw` | yes
  *     * When `intrinsic`, the image will scale the dimensions down for smaller viewports, but maintain the original dimensions for larger viewports.
  *     * When `fixed`, the image dimensions will not change as the viewport changes (no responsiveness) similar to the native `img` element.
  *     * When `responsive`, the image will scale the dimensions down for smaller viewports and scale up for larger viewports.
    * Ensure the parent element uses `display: block` in their stylesheet.
  *     * When `fill`, the image will stretch both width and height to the dimensions of the parent element, provided the parent element is relative.
    * This is usually paired with the [`objectFit`](https://nextjs.org/docs/pages/api-reference/components/image-legacy#objectfit) property.
    * Ensure the parent element has `position: relative` in their stylesheet.


### loader[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#loader)
A custom function used to resolve URLs. Setting the loader as a prop on the Image component overrides the default loader defined in the [`images` section of `next.config.js`](https://nextjs.org/docs/pages/api-reference/components/image-legacy#loader-configuration).
A `loader` is a function returning a URL string for the image, given the following parameters:
  * [`src`](https://nextjs.org/docs/pages/api-reference/components/image-legacy#src)
  * [`width`](https://nextjs.org/docs/pages/api-reference/components/image-legacy#width)
  * [`quality`](https://nextjs.org/docs/pages/api-reference/components/image-legacy#quality)


Here is an example of using a custom loader:
```
import Image from 'next/legacy/image'

const myLoader = ({ src, width, quality }) => {
  return `https://example.com/${src}?w=${width}&q=${quality || 75}`
}

const MyImage = (props) => {
  return (
    <Image
      loader={myLoader}
      src="me.png"
      alt="Picture of the author"
      width={500}
      height={500}
    />
  )
}
```

### sizes[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#sizes)
A string that provides information about how wide the image will be at different breakpoints. The value of `sizes` will greatly affect performance for images using `layout="responsive"` or `layout="fill"`. It will be ignored for images using `layout="intrinsic"` or `layout="fixed"`.
The `sizes` property serves two important purposes related to image performance:
First, the value of `sizes` is used by the browser to determine which size of the image to download, from `next/legacy/image`'s automatically-generated source set. When the browser chooses, it does not yet know the size of the image on the page, so it selects an image that is the same size or larger than the viewport. The `sizes` property allows you to tell the browser that the image will actually be smaller than full screen. If you don't specify a `sizes` value, a default value of `100vw` (full screen width) is used.
Second, the `sizes` value is parsed and used to trim the values in the automatically-created source set. If the `sizes` property includes sizes such as `50vw`, which represent a percentage of the viewport width, then the source set is trimmed to not include any values which are too small to ever be necessary.
For example, if you know your styling will cause an image to be full-width on mobile devices, in a 2-column layout on tablets, and a 3-column layout on desktop displays, you should include a sizes property such as the following:
```
import Image from 'next/legacy/image'
const Example = () => (
  <div className="grid-element">
    <Image
      src="/example.png"
      layout="fill"
      sizes="(max-width: 768px) 100vw,
              (max-width: 1200px) 50vw,
              33vw"
    />
  </div>
)
```

This example `sizes` could have a dramatic effect on performance metrics. Without the `33vw` sizes, the image selected from the server would be 3 times as wide as it needs to be. Because file size is proportional to the square of the width, without `sizes` the user would download an image that's 9 times larger than necessary.
Learn more about `srcset` and `sizes`:
### quality[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#quality)
The quality of the optimized image, an integer between `1` and `100` where `100` is the best quality. Defaults to `75`.
### priority[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#priority)
When true, the image will be considered high priority and `priority`.
You should use the `priority` property on any image detected as the [Largest Contentful Paint (LCP)](https://nextjs.org/learn/seo/web-performance/lcp) element. It may be appropriate to have multiple priority images, as different images may be the LCP element for different viewport sizes.
Should only be used when the image is visible above the fold. Defaults to `false`.
### placeholder[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#placeholder)
A placeholder to use while the image is loading. Possible values are `blur` or `empty`. Defaults to `empty`.
When `blur`, the [`blurDataURL`](https://nextjs.org/docs/pages/api-reference/components/image-legacy#blurdataurl) property will be used as the placeholder. If `src` is an object from a [static import](https://nextjs.org/docs/pages/api-reference/components/image#src) and the imported image is `.jpg`, `.png`, `.webp`, or `.avif`, then `blurDataURL` will be automatically populated.
For dynamic images, you must provide the [`blurDataURL`](https://nextjs.org/docs/pages/api-reference/components/image-legacy#blurdataurl) property. Solutions such as `base64` generation.
When `empty`, there will be no placeholder while the image is loading, only empty space.
Try it out:
