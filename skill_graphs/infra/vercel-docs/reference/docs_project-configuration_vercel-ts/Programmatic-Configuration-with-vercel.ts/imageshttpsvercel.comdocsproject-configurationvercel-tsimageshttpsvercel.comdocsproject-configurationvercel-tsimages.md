##  [images](https://vercel.com/docs/project-configuration/vercel-ts#images)[](https://vercel.com/docs/project-configuration/vercel-ts#images)
The `images` property defines the behavior of [Vercel's native Image Optimization API](https://vercel.com/docs/image-optimization), which allows on-demand optimization of images at runtime.
Type: `Object`
###  [Value definition](https://vercel.com/docs/project-configuration/vercel-ts#value-definition)[](https://vercel.com/docs/project-configuration/vercel-ts#value-definition)
  * `sizes` - Required - Array of allowed image widths. The Image Optimization API will return an error if the `w` parameter is not defined in this list.
  * `localPatterns` - Allow-list of local image paths which can be used with the Image Optimization API.
  * `remotePatterns` - Allow-list of external domains which can be used with the Image Optimization API.
  * `minimumCacheTTL` - Cache duration (in seconds) for the optimized images.
  * `qualities` - Array of allowed image qualities. The Image Optimization API will return an error if the `q` parameter is not defined in this list.
  * `formats` - Supported output image formats. Allowed values are either `"image/avif"` and/or `"image/webp"`.
  * `dangerouslyAllowSVG` - Allow SVG input image URLs. This is disabled by default for security purposes.
  * `contentSecurityPolicy` - Specifies the
  * `contentDispositionType` - Specifies the value of the `"Content-Disposition"` response header. Allowed values are `"inline"` or `"attachment"`.


vercel.ts
```
import type { VercelConfig } from '@vercel/config/v1';

export const config: VercelConfig = {
  images: {
    sizes: [256, 640, 1080, 2048, 3840],
    localPatterns: [
      {
        pathname: '^/assets/.*$',
        search: '',
      },
    ],
    remotePatterns: [
      {
        protocol: 'https',
        hostname: 'example.com',
        port: '',
        pathname: '^/account123/.*$',
        search: '?v=1',
      },
    ],
    minimumCacheTTL: 60,
    qualities: [25, 50, 75],
    formats: ['image/webp'],
    dangerouslyAllowSVG: false,
    contentSecurityPolicy: "script-src 'none'; frame-src 'none'; sandbox;",
    contentDispositionType: 'inline',
  },
};
```
