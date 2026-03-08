## Caching Behavior[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#caching-behavior)
The following describes the caching algorithm for the default [loader](https://nextjs.org/docs/pages/api-reference/components/image-legacy#loader). For all other loaders, please refer to your cloud provider's documentation.
Images are optimized dynamically upon request and stored in the `<distDir>/cache/images` directory. The optimized image file will be served for subsequent requests until the expiration is reached. When a request is made that matches a cached but expired file, the expired image is served stale immediately. Then the image is optimized again in the background (also called revalidation) and saved to the cache with the new expiration date.
The cache status of an image can be determined by reading the value of the `x-nextjs-cache` (`x-vercel-cache` when deployed on Vercel) response header. The possible values are the following:
  * `MISS` - the path is not in the cache (occurs at most once, on the first visit)
  * `STALE` - the path is in the cache but exceeded the revalidate time so it will be updated in the background
  * `HIT` - the path is in the cache and has not exceeded the revalidate time


The expiration (or rather Max Age) is defined by either the [`minimumCacheTTL`](https://nextjs.org/docs/pages/api-reference/components/image-legacy#minimum-cache-ttl) configuration or the upstream image `Cache-Control` header, whichever is larger. Specifically, the `max-age` value of the `Cache-Control` header is used. If both `s-maxage` and `max-age` are found, then `s-maxage` is preferred. The `max-age` is also passed-through to any downstream clients including CDNs and browsers.
  * You can configure [`minimumCacheTTL`](https://nextjs.org/docs/pages/api-reference/components/image-legacy#minimum-cache-ttl) to increase the cache duration when the upstream image does not include `Cache-Control` header or the value is very low.
  * You can configure [`deviceSizes`](https://nextjs.org/docs/pages/api-reference/components/image-legacy#device-sizes) and [`imageSizes`](https://nextjs.org/docs/pages/api-reference/components/image-legacy#image-sizes) to reduce the total number of possible generated images.
  * You can configure [formats](https://nextjs.org/docs/pages/api-reference/components/image-legacy#acceptable-formats) to disable multiple formats in favor of a single image format.


### Minimum Cache TTL[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#minimum-cache-ttl)
You can configure the Time to Live (TTL) in seconds for cached optimized images. In many cases, it's better to use a [Static Image Import](https://nextjs.org/docs/pages/api-reference/components/image#src) which will automatically hash the file contents and cache the image forever with a `Cache-Control` header of `immutable`.
If no configuration is provided, the default below is used.
next.config.js
```
module.exports = {
  images: {
    minimumCacheTTL: 14400, // 4 hours
  },
}
```

You can increase the TTL to reduce the number of revalidations and potentially lower cost:
next.config.js
```
module.exports = {
  images: {
    minimumCacheTTL: 2678400, // 31 days
  },
}
```

The expiration (or rather Max Age) of the optimized image is defined by either the `minimumCacheTTL` or the upstream image `Cache-Control` header, whichever is larger.
If you need to change the caching behavior per image, you can configure [`headers`](https://nextjs.org/docs/pages/api-reference/config/next-config-js/headers) to set the `Cache-Control` header on the upstream image (e.g. `/some-asset.jpg`, not `/_next/image` itself).
There is no mechanism to invalidate the cache at this time, so its best to keep `minimumCacheTTL` low. Otherwise you may need to manually change the [`src`](https://nextjs.org/docs/pages/api-reference/components/image-legacy#src) prop or delete `<distDir>/cache/images`.
### Disable Static Imports[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#disable-static-imports)
The default behavior allows you to import static files such as `import icon from './icon.png'` and then pass that to the `src` property.
In some cases, you may wish to disable this feature if it conflicts with other plugins that expect the import to behave differently.
You can disable static image imports inside your `next.config.js`:
next.config.js
```
module.exports = {
  images: {
    disableStaticImages: true,
  },
}
```

### Dangerously Allow SVG[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#dangerously-allow-svg)
The default [loader](https://nextjs.org/docs/pages/api-reference/components/image-legacy#loader) does not optimize SVG images for a few reasons. First, SVG is a vector format meaning it can be resized losslessly. Second, SVG has many of the same features as HTML/CSS, which can lead to vulnerabilities without proper [Content Security Policy (CSP) headers](https://nextjs.org/docs/app/api-reference/config/next-config-js/headers#content-security-policy).
Therefore, we recommended using the [`unoptimized`](https://nextjs.org/docs/pages/api-reference/components/image-legacy#unoptimized) prop when the [`src`](https://nextjs.org/docs/pages/api-reference/components/image-legacy#src) prop is known to be SVG. This happens automatically when `src` ends with `".svg"`.
However, if you need to serve SVG images with the default Image Optimization API, you can set `dangerouslyAllowSVG` inside your `next.config.js`:
next.config.js
```
module.exports = {
  images: {
    dangerouslyAllowSVG: true,
    contentDispositionType: 'attachment',
    contentSecurityPolicy: "default-src 'self'; script-src 'none'; sandbox;",
  },
}
```

In addition, it is strongly recommended to also set `contentDispositionType` to force the browser to download the image, as well as `contentSecurityPolicy` to prevent scripts embedded in the image from executing.
###  `contentDispositionType`[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#contentdispositiontype)
The default [loader](https://nextjs.org/docs/pages/api-reference/components/image-legacy#loader) sets the `attachment` for added protection since the API can serve arbitrary remote images.
The default value is `attachment` which forces the browser to download the image when visiting directly. This is particularly important when [`dangerouslyAllowSVG`](https://nextjs.org/docs/pages/api-reference/components/image-legacy#dangerously-allow-svg) is true.
You can optionally configure `inline` to allow the browser to render the image when visiting directly, without downloading it.
next.config.js
```
module.exports = {
  images: {
    contentDispositionType: 'inline',
  },
}
```

### Animated Images[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#animated-images)
The default [loader](https://nextjs.org/docs/pages/api-reference/components/image-legacy#loader) will automatically bypass Image Optimization for animated images and serve the image as-is.
Auto-detection for animated files is best-effort and supports GIF, APNG, and WebP. If you want to explicitly bypass Image Optimization for a given animated image, use the [unoptimized](https://nextjs.org/docs/pages/api-reference/components/image-legacy#unoptimized) prop.
