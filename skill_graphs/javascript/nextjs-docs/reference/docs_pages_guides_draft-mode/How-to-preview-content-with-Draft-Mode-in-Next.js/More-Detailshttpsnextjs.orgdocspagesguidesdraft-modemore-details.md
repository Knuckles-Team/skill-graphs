## More Details[](https://nextjs.org/docs/pages/guides/draft-mode#more-details)
### Clear the Draft Mode cookie[](https://nextjs.org/docs/pages/guides/draft-mode#clear-the-draft-mode-cookie)
By default, the Draft Mode session ends when the browser is closed.
To clear the Draft Mode cookie manually, create an API route that calls `setDraftMode({ enable: false })`:
pages/api/disable-draft.ts
```
export default function handler(req, res) {
  res.setDraftMode({ enable: false })
}
```

Then, send a request to `/api/disable-draft` to invoke the API Route. If calling this route using [`next/link`](https://nextjs.org/docs/pages/api-reference/components/link), you must pass `prefetch={false}` to prevent accidentally deleting the cookie on prefetch.
### Works with `getServerSideProps`[](https://nextjs.org/docs/pages/guides/draft-mode#works-with-getserversideprops)
Draft Mode works with `getServerSideProps`, and is available as a `draftMode` key in the [`context`](https://nextjs.org/docs/pages/api-reference/functions/get-server-side-props#context-parameter) object.
> **Good to know** : You shouldn't set the `Cache-Control` header when using Draft Mode because it cannot be bypassed. Instead, we recommend using [ISR](https://nextjs.org/docs/pages/guides/incremental-static-regeneration).
### Works with API Routes[](https://nextjs.org/docs/pages/guides/draft-mode#works-with-api-routes)
API Routes will have access to `draftMode` on the request object. For example:
```
export default function myApiRoute(req, res) {
  if (req.draftMode) {
    // get draft data
  }
}
```

### Unique per `next build`[](https://nextjs.org/docs/pages/guides/draft-mode#unique-per-next-build)
A new bypass cookie value will be generated each time you run `next build`.
This ensures that the bypass cookie can’t be guessed.
> **Good to know** : To test Draft Mode locally over HTTP, your browser will need to allow third-party cookies and local storage access.
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
