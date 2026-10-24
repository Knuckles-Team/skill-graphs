## Image Optimization[](https://nextjs.org/docs/pages/guides/self-hosting#image-optimization)
[Image Optimization](https://nextjs.org/docs/app/api-reference/components/image) through `next/image` works self-hosted with zero configuration when deploying using `next start`. If you would prefer to have a separate service to optimize images, you can [configure an image loader](https://nextjs.org/docs/app/api-reference/components/image#loader).
Image Optimization can be used with a [static export](https://nextjs.org/docs/app/guides/static-exports#image-optimization) by defining a custom image loader in `next.config.js`. Note that images are optimized at runtime, not during the build.
> **Good to know:**
>   * On glibc-based Linux systems, Image Optimization may require
>   * Learn more about the [caching behavior of optimized images](https://nextjs.org/docs/app/api-reference/components/image#minimumcachettl) and how to configure the TTL.
>   * You can also [disable Image Optimization](https://nextjs.org/docs/app/api-reference/components/image#unoptimized) and still retain other benefits of using `next/image` if you prefer. For example, if you are optimizing images yourself separately.
>
