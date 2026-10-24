# pageExtensions
Last updated February 27, 2026
You can extend the default Page extensions (`.tsx`, `.ts`, `.jsx`, `.js`) used by Next.js. Inside `next.config.js`, add the `pageExtensions` config:
next.config.js
```
module.exports = {
  pageExtensions: ['mdx', 'md', 'jsx', 'js', 'tsx', 'ts'],
}
```

Changing these values affects _all_ Next.js pages, including the following:
  * [`proxy.js`](https://nextjs.org/docs/pages/api-reference/file-conventions/proxy)
  * [`instrumentation.js`](https://nextjs.org/docs/pages/guides/instrumentation)
  * `pages/_document.js`
  * `pages/_app.js`
  * `pages/api/`


For example, if you reconfigure `.ts` page extensions to `.page.ts`, you would need to rename pages like `proxy.page.ts`, `instrumentation.page.ts`, `_app.page.ts`.
