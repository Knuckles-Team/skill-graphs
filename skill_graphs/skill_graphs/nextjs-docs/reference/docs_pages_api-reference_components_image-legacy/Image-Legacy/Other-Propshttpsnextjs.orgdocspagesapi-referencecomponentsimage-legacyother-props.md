## Other Props[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#other-props)
Other properties on the `<Image />` component will be passed to the underlying `img` element with the exception of the following:
  * `srcSet`. Use [Device Sizes](https://nextjs.org/docs/pages/api-reference/components/image-legacy#device-sizes) instead.
  * `ref`. Use [`onLoadingComplete`](https://nextjs.org/docs/pages/api-reference/components/image-legacy#onloadingcomplete) instead.
  * `decoding`. It is always `"async"`.
