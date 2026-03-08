## Version History[](https://nextjs.org/docs/app/api-reference/functions/generate-sitemaps#version-history)
Version | Changes
---|---
`v16.0.0` | The `id` values returned from `generateSitemaps` are now passed as a promise that resolves to a `string` to the sitemap function.
`v15.0.0` |  `generateSitemaps` now generates consistent URLs between development and production
`v13.3.2` |  `generateSitemaps` introduced. In development, you can view the generated sitemap on `/.../sitemap.xml/[id]`. For example, `/product/sitemap.xml/1`.
