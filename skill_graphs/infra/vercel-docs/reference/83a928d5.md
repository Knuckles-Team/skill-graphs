##  [Blob sorting and organization](https://vercel.com/docs/vercel-blob#blob-sorting-and-organization)[](https://vercel.com/docs/vercel-blob#blob-sorting-and-organization)
Blobs are returned in lexicographical order by pathname (not creation date) when using [`list()`](https://vercel.com/docs/vercel-blob/using-blob-sdk#list). Numbers are treated as characters, so `file10.txt` comes before `file2.txt`.
Sort by creation date: Include timestamps in pathnames:
```
const timestamp = new Date().toISOString().split('T')[0]; // YYYY-MM-DD
await put(`reports/${timestamp}-quarterly-report.pdf`, file, {
  access: 'private' /* or 'public' */
});
```

Use prefixes for search: Consider lowercase pathnames for consistent matching:
```
await put('user-uploads/avatar.jpg', file, { access: 'private' /* or 'public' */ });
const userUploads = await list({ prefix: 'user-uploads/' });
```

For complex sorting, sort results client-side using `uploadedAt` or other properties.
