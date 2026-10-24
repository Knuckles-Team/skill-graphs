## Step 2: Update `getStaticProps`[](https://nextjs.org/docs/pages/guides/draft-mode#step-2-update-getstaticprops)
The next step is to update `getStaticProps` to support draft mode.
If you request a page which has `getStaticProps` with the cookie set (via `res.setDraftMode`), then `getStaticProps` will be called at **request time** (instead of at build time).
Furthermore, it will be called with a `context` object where `context.draftMode` will be `true`.
```
export async function getStaticProps(context) {
  if (context.draftMode) {
    // dynamic data
  }
}
```

We used `res.setDraftMode` in the draft API route, so `context.draftMode` will be `true`.
If you’re also using `getStaticPaths`, then `context.params` will also be available.
### Fetch draft data[](https://nextjs.org/docs/pages/guides/draft-mode#fetch-draft-data)
You can update `getStaticProps` to fetch different data based on `context.draftMode`.
For example, your headless CMS might have a different API endpoint for draft posts. If so, you can modify the API endpoint URL like below:
```
export async function getStaticProps(context) {
  const url = context.draftMode
    ? 'https://draft.example.com'
    : 'https://production.example.com'
  const res = await fetch(url)
  // ...
}
```

That’s it! If you access the draft API route (with `secret` and `slug`) from your headless CMS or manually, you should now be able to see the draft content. And if you update your draft without publishing, you should be able to view the draft.
Set this as the draft URL on your headless CMS or access manually, and you should be able to see the draft.
Terminal
```
https://<your-site>/api/draft?secret=<token>&slug=<path>
```
