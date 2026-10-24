## More Details[](https://nextjs.org/docs/pages/guides/preview-mode#more-details)
> **Good to know** : during rendering `next/router` exposes an `isPreview` flag, see the [router object docs](https://nextjs.org/docs/pages/api-reference/functions/use-router#router-object) for more info.
### Specify the Preview Mode duration[](https://nextjs.org/docs/pages/guides/preview-mode#specify-the-preview-mode-duration)
`setPreviewData` takes an optional second parameter which should be an options object. It accepts the following keys:
  * `maxAge`: Specifies the number (in seconds) for the preview session to last for.
  * `path`: Specifies the path the cookie should be applied under. Defaults to `/` enabling preview mode for all paths.


```
setPreviewData(data, {
  maxAge: 60 * 60, // The preview mode cookies expire in 1 hour
  path: '/about', // The preview mode cookies apply to paths with /about
})
```

### Clear the Preview Mode cookies[](https://nextjs.org/docs/pages/guides/preview-mode#clear-the-preview-mode-cookies)
By default, no expiration date is set for Preview Mode cookies, so the preview session ends when the browser is closed.
To clear the Preview Mode cookies manually, create an API route that calls `clearPreviewData()`:
pages/api/clear-preview-mode-cookies.js
```
export default function handler(req, res) {
  res.clearPreviewData({})
}
```

Then, send a request to `/api/clear-preview-mode-cookies` to invoke the API Route. If calling this route using [`next/link`](https://nextjs.org/docs/pages/api-reference/components/link), you must pass `prefetch={false}` to prevent calling `clearPreviewData` during link prefetching.
If a path was specified in the `setPreviewData` call, you must pass the same path to `clearPreviewData`:
pages/api/clear-preview-mode-cookies.js
```
export default function handler(req, res) {
  const { path } = req.query

  res.clearPreviewData({ path })
}
```

###  `previewData` size limits[](https://nextjs.org/docs/pages/guides/preview-mode#previewdata-size-limits)
You can pass an object to `setPreviewData` and have it be available in `getStaticProps`. However, because the data will be stored in a cookie, there’s a size limitation. Currently, preview data is limited to 2KB.
### Works with `getServerSideProps`[](https://nextjs.org/docs/pages/guides/preview-mode#works-with-getserversideprops)
The preview mode works on `getServerSideProps` as well. It will also be available on the `context` object containing `preview` and `previewData`.
> **Good to know** : You shouldn't set the `Cache-Control` header when using Preview Mode because it cannot be bypassed. Instead, we recommend using [ISR](https://nextjs.org/docs/pages/guides/incremental-static-regeneration).
### Works with API Routes[](https://nextjs.org/docs/pages/guides/preview-mode#works-with-api-routes)
API Routes will have access to `preview` and `previewData` under the request object. For example:
```
export default function myApiRoute(req, res) {
  const isPreview = req.preview
  const previewData = req.previewData
  // ...
}
```

### Unique per `next build`[](https://nextjs.org/docs/pages/guides/preview-mode#unique-per-next-build)
Both the bypass cookie value and the private key for encrypting the `previewData` change when `next build` is completed. This ensures that the bypass cookie can’t be guessed.
> **Good to know** : To test Preview Mode locally over HTTP your browser will need to allow third-party cookies and local storage access.
Was this helpful?
Send
* * *
* * *
#### Resources
[Docs](https://nextjs.org/docs)[Support Policy](https://nextjs.org/support-policy)[Learn](https://nextjs.org/learn)[Showcase](https://nextjs.org/showcase)[Blog](https://nextjs.org/blog)[Team](https://nextjs.org/team)[Next.js Conf](https://nextjs.org/conf)[Evals](https://nextjs.org/evals)
#### More
[Telemetry](https://nextjs.org/telemetry)[Governance](https://nextjs.org/governance)
#### About Vercel
#### Legal
Cookie Preferences
#### Subscribe to our newsletter
Stay updated on new releases and features, guides, and case studies.
Subscribe
© 2026 Vercel, Inc.
* * *
* * *
