## Comparison[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#comparison)
Compared to `next/legacy/image`, the new `next/image` component has the following changes:
  * Removes `<span>` wrapper around `<img>` in favor of
  * Adds support for canonical `style` prop
    * Removes `layout` prop in favor of `style` or `className`
    * Removes `objectFit` prop in favor of `style` or `className`
    * Removes `objectPosition` prop in favor of `style` or `className`
  * Removes `IntersectionObserver` implementation in favor of
    * Removes `lazyBoundary` prop since there is no native equivalent
    * Removes `lazyRoot` prop since there is no native equivalent
  * Removes `loader` config in favor of [`loader`](https://nextjs.org/docs/pages/api-reference/components/image-legacy#loader) prop
  * Changed `alt` prop from optional to required
  * Changed `onLoadingComplete` callback to receive reference to `<img>` element
