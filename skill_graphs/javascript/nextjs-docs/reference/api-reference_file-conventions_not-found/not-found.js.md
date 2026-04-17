# not-found.js
Last updated February 27, 2026
Next.js provides two conventions to handle not found cases:
  * **`not-found.js`**: Used when you call the[`notFound`](https://nextjs.org/docs/app/api-reference/functions/not-found) function in a route segment.
  * **`global-not-found.js`**: Used to define a global 404 page for unmatched routes across your entire app. This is handled at the routing level and doesn't depend on rendering a layout or page.
