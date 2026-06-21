## Advanced[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#advanced)
The following configuration is for advanced use cases and is usually not necessary. If you choose to configure the properties below, you will override any changes to the Next.js defaults in future updates.
### Device Sizes[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#device-sizes)
If you know the expected device widths of your users, you can specify a list of device width breakpoints using the `deviceSizes` property in `next.config.js`. These widths are used when the `next/legacy/image` component uses `layout="responsive"` or `layout="fill"` to ensure the correct image is served for user's device.
If no configuration is provided, the default below is used.
next.config.js
```
module.exports = {
  images: {
    deviceSizes: [640, 750, 828, 1080, 1200, 1920, 2048, 3840],
  },
}
```

### Image Sizes[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#image-sizes)
You can specify a list of image widths using the `images.imageSizes` property in your `next.config.js` file. These widths are concatenated with the array of [device sizes](https://nextjs.org/docs/pages/api-reference/components/image-legacy#device-sizes) to form the full array of sizes used to generate image
The reason there are two separate lists is that imageSizes is only used for images which provide a [`sizes`](https://nextjs.org/docs/pages/api-reference/components/image-legacy#sizes) prop, which indicates that the image is less than the full width of the screen. **Therefore, the sizes in imageSizes should all be smaller than the smallest size in deviceSizes.**
If no configuration is provided, the default below is used.
next.config.js
```
module.exports = {
  images: {
    imageSizes: [32, 48, 64, 96, 128, 256, 384],
  },
}
```

### Acceptable Formats[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#acceptable-formats)
The default [Image Optimization API](https://nextjs.org/docs/pages/api-reference/components/image-legacy#loader-configuration) will automatically detect the browser's supported image formats via the request's `Accept` header in order to determine the best output format.
If the `Accept` header matches more than one of the configured formats, the first match in the array is used. Therefore, the array order matters. If there is no match (or the source image is [animated](https://nextjs.org/docs/pages/api-reference/components/image-legacy#animated-images)), the Image Optimization API will fallback to the original image's format.
If no configuration is provided, the default below is used.
next.config.js
```
module.exports = {
  images: {
    formats: ['image/webp'],
  },
}
```

You can enable AVIF support, which will fallback to the original format of the src image if the browser
next.config.js
```
module.exports = {
  images: {
    formats: ['image/avif'],
  },
}
```

You can also enable both AVIF and WebP formats together. AVIF will be preferred for browsers that support it, with WebP as a fallback:
next.config.js
```
module.exports = {
  images: {
    formats: ['image/avif', 'image/webp'],
  },
}
```

> **Good to know** :
>   * We still recommend using WebP for most use cases.
>   * AVIF generally takes 50% longer to encode but it compresses 20% smaller compared to WebP. This means that the first time an image is requested, it will typically be slower and then subsequent requests that are cached will be faster.
>   * When using multiple formats, Next.js will cache each format separately. This means increased storage requirements compared to using a single format, as both AVIF and WebP versions of images will be stored for different browser support.
>   * If you self-host with a Proxy/CDN in front of Next.js, you must configure the Proxy to forward the `Accept` header.
>
