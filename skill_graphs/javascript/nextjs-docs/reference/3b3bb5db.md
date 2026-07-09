## Execution order[](https://nextjs.org/docs/app/api-reference/file-conventions/proxy#execution-order)
Proxy will be invoked for **every route in your project**. Given this, it's crucial to use [matchers](https://nextjs.org/docs/app/api-reference/file-conventions/proxy#matcher) to precisely target or exclude specific routes. The following is the execution order:
  1. `headers` from `next.config.js`
  2. `redirects` from `next.config.js`
  3. Proxy (`rewrites`, `redirects`, etc.)
  4. `beforeFiles` (`rewrites`) from `next.config.js`
  5. Filesystem routes (`public/`, `_next/static/`, `pages/`, `app/`, etc.)
  6. `afterFiles` (`rewrites`) from `next.config.js`
  7. Dynamic Routes (`/blog/[slug]`)
  8. `fallback` (`rewrites`) from `next.config.js`
