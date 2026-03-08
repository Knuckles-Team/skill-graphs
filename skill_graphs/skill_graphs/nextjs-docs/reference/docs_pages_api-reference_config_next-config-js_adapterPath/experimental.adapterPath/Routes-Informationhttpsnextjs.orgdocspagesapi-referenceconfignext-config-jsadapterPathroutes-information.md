## Routes Information[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/adapterPath#routes-information)
The `routes` object in `onBuildComplete` provides complete routing information with processed patterns ready for deployment:
### Headers[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/adapterPath#headers)
Each header route includes:
  * `source`: Original route pattern (e.g., `/about`)
  * `sourceRegex`: Compiled regex for matching requests
  * `headers`: Key-value pairs of headers to apply
  * `has`: Optional conditions that must be met
  * `missing`: Optional conditions that must not be met
  * `priority`: Optional flag for internal routes


### Redirects[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/adapterPath#redirects)
Each redirect route includes:
  * `source`: Original route pattern
  * `sourceRegex`: Compiled regex for matching
  * `destination`: Target URL (can include captured groups)
  * `statusCode`: HTTP status code (301, 302, 307, 308)
  * `has`: Optional positive conditions
  * `missing`: Optional negative conditions
  * `priority`: Optional flag for internal routes


### Rewrites[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/adapterPath#rewrites)
Rewrites are categorized into three phases:
  * `beforeFiles`: Checked before filesystem (including pages and public files)
  * `afterFiles`: Checked after pages/public files but before dynamic routes
  * `fallback`: Checked after all other routes


Each rewrite includes `source`, `sourceRegex`, `destination`, `has`, and `missing`.
### Dynamic Routes[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/adapterPath#dynamic-routes)
Generated from dynamic route segments (e.g., `[slug]`, `[...path]`). Each includes:
  * `source`: Route pattern
  * `sourceRegex`: Compiled regex with named capture groups
  * `destination`: Internal destination with parameter substitution
  * `has`: Optional positive conditions
  * `missing`: Optional negative conditions
