## Behavior[](https://nextjs.org/docs/app/api-reference/functions/image-response#behavior)
  * `ImageResponse` uses
  * Only flexbox and a subset of CSS properties are supported. Advanced layouts (e.g. `display: grid`) will not work.
  * Maximum bundle size of `500KB`. The bundle size includes your JSX, CSS, fonts, images, and any other assets. If you exceed the limit, consider reducing the size of any assets or fetching at runtime.
  * Only `ttf`, `otf`, and `woff` font formats are supported. To maximize the font parsing speed, `ttf` or `otf` are preferred over `woff`.
