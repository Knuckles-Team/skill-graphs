## Development vs Production[](https://nextjs.org/docs/pages/getting-started/css#development-vs-production)
  * In development (`next dev`), CSS updates apply instantly with [Fast Refresh](https://nextjs.org/docs/architecture/fast-refresh).
  * In production (`next build`), all CSS files are automatically concatenated into **many minified and code-split** `.css` files, ensuring the minimal amount of CSS is loaded for a route.
  * CSS still loads with JavaScript disabled in production, but JavaScript is required in development for Fast Refresh.
  * CSS ordering can behave differently in development, always ensure to check the build (`next build`) to verify the final CSS order.
