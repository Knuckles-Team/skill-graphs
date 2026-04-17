# images
Last updated February 27, 2026
If you want to use a cloud provider to optimize images instead of using the Next.js built-in Image Optimization API, you can configure `next.config.js` with the following:
next.config.js
```
module.exports = {
  images: {
    loader: 'custom',
    loaderFile: './my/image/loader.js',
  },
}
```

This `loaderFile` must point to a file relative to the root of your Next.js application. The file must export a default function that returns a string, for example:
my/image/loader.js
```
export default function myImageLoader({ src, width, quality }) {
  return `https://example.com/${src}?w=${width}&q=${quality || 75}`
}
```

Alternatively, you can use the [`loader` prop](https://nextjs.org/docs/pages/api-reference/components/image#loader) to pass the function to each instance of `next/image`.
To learn more about configuring the behavior of the built-in [Image Optimization API](https://nextjs.org/docs/pages/api-reference/components/image) and the [Image Component](https://nextjs.org/docs/pages/api-reference/components/image), see [Image Configuration Options](https://nextjs.org/docs/pages/api-reference/components/image#configuration-options) for available options.
