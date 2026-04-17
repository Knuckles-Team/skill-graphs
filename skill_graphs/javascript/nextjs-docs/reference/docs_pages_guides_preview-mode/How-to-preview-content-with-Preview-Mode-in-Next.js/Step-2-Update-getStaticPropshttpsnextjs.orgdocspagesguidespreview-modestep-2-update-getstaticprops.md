## Step 2: Update `getStaticProps`[](https://nextjs.org/docs/pages/guides/preview-mode#step-2-update-getstaticprops)
The next step is to update `getStaticProps` to support the preview mode.
If you request a page which has `getStaticProps` with the preview mode cookies set (via `res.setPreviewData`), then `getStaticProps` will be called at **request time** (instead of at build time).
Furthermore, it will be called with a `context` object where:
  * `context.preview` will be `true`.
  * `context.previewData` will be the same as the argument used for `setPreviewData`.


```
export async function getStaticProps(context) {
  // If you request this page with the preview mode cookies set:
  //
  // - context.preview will be true
  // - context.previewData will be the same as
  //   the argument used for `setPreviewData`.
}
```

We used `res.setPreviewData({})` in the preview API route, so `context.previewData` will be `{}`. You can use this to pass session information from the preview API route to `getStaticProps` if necessary.
If you’re also using `getStaticPaths`, then `context.params` will also be available.
### Fetch preview data[](https://nextjs.org/docs/pages/guides/preview-mode#fetch-preview-data)
You can update `getStaticProps` to fetch different data based on `context.preview` and/or `context.previewData`.
For example, your headless CMS might have a different API endpoint for draft posts. If so, you can use `context.preview` to modify the API endpoint URL like below:
```
export async function getStaticProps(context) {
  // If context.preview is true, append "/preview" to the API endpoint
  // to request draft data instead of published data. This will vary
  // based on which headless CMS you're using.
  const res = await fetch(`https://.../${context.preview ? 'preview' : ''}`)
  // ...
}
```

That’s it! If you access the preview API route (with `secret` and `slug`) from your headless CMS or manually, you should now be able to see the preview content. And if you update your draft without publishing, you should be able to preview the draft.
Set this as the preview URL on your headless CMS or access manually, and you should be able to see the preview.
Terminal
```
https://<your-site>/api/preview?secret=<token>&slug=<path>
```
