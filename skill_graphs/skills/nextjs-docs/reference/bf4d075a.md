## Step 1: Create and access the API route[](https://nextjs.org/docs/pages/guides/draft-mode#step-1-create-and-access-the-api-route)
> Take a look at the [API Routes documentation](https://nextjs.org/docs/pages/building-your-application/routing/api-routes) first if you’re not familiar with Next.js API Routes.
First, create the **API route**. It can have any name - e.g. `pages/api/draft.ts`
In this API route, you need to call `setDraftMode` on the response object.
```
export default function handler(req, res) {
  // ...
  res.setDraftMode({ enable: true })
  // ...
}
```

This will set a **cookie** to enable draft mode. Subsequent requests containing this cookie will trigger **Draft Mode** changing the behavior for statically generated pages (more on this later).
You can test this manually by creating an API route like below and accessing it from your browser manually:
pages/api/draft.ts
```
// simple example for testing it manually from your browser.
export default function handler(req, res) {
  res.setDraftMode({ enable: true })
  res.end('Draft mode is enabled')
}
```

If you open your browser’s developer tools and visit `/api/draft`, you’ll notice a `Set-Cookie` response header with a cookie named `__prerender_bypass`.
### Securely accessing it from your Headless CMS[](https://nextjs.org/docs/pages/guides/draft-mode#securely-accessing-it-from-your-headless-cms)
In practice, you’d want to call this API route _securely_ from your headless CMS. The specific steps will vary depending on which headless CMS you’re using, but here are some common steps you could take.
These steps assume that the headless CMS you’re using supports setting **custom draft URLs**. If it doesn’t, you can still use this method to secure your draft URLs, but you’ll need to construct and access the draft URL manually.
**First** , you should create a **secret token string** using a token generator of your choice. This secret will only be known by your Next.js app and your headless CMS. This secret prevents people who don’t have access to your CMS from accessing draft URLs.
**Second** , if your headless CMS supports setting custom draft URLs, specify the following as the draft URL. This assumes that your draft API route is located at `pages/api/draft.ts`.
Terminal
```
https://<your-site>/api/draft?secret=<token>&slug=<path>
```

  * `<your-site>` should be your deployment domain.
  * `<token>` should be replaced with the secret token you generated.
  * `<path>` should be the path for the page that you want to view. If you want to view `/posts/foo`, then you should use `&slug=/posts/foo`.


Your headless CMS might allow you to include a variable in the draft URL so that `<path>` can be set dynamically based on the CMS’s data like so: `&slug=/posts/{entry.fields.slug}`
**Finally** , in the draft API route:
  * Check that the secret matches and that the `slug` parameter exists (if not, the request should fail).
  * Call `res.setDraftMode`.
  * Then redirect the browser to the path specified by `slug`. (The following example uses a


```
export default async (req, res) => {
  // Check the secret and next parameters
  // This secret should only be known to this API route and the CMS
  if (req.query.secret !== 'MY_SECRET_TOKEN' || !req.query.slug) {
    return res.status(401).json({ message: 'Invalid token' })
  }

  // Fetch the headless CMS to check if the provided `slug` exists
  // getPostBySlug would implement the required fetching logic to the headless CMS
  const post = await getPostBySlug(req.query.slug)

  // If the slug doesn't exist prevent draft mode from being enabled
  if (!post) {
    return res.status(401).json({ message: 'Invalid slug' })
  }

  // Enable Draft Mode by setting the cookie
  res.setDraftMode({ enable: true })

  // Redirect to the path from the fetched post
  // We don't redirect to req.query.slug as that might lead to open redirect vulnerabilities
  res.redirect(post.slug)
}
```

If it succeeds, then the browser will be redirected to the path you want to view with the draft mode cookie.
