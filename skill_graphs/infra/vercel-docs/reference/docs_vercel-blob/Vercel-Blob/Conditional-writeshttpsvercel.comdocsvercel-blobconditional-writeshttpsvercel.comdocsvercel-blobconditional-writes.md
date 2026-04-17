##  [Conditional writes](https://vercel.com/docs/vercel-blob#conditional-writes)[](https://vercel.com/docs/vercel-blob#conditional-writes)
Conditional writes use the `ifMatch` option to implement optimistic concurrency control. When writing, pass a known ETag from a previous upload, [`get()`](https://vercel.com/docs/vercel-blob/using-blob-sdk#get), or [`head()`](https://vercel.com/docs/vercel-blob/using-blob-sdk#head) call. The operation only succeeds if the blob hasn't changed since that ETag was issued. If another process modified the blob in between, the ETag won't match and the SDK throws a `BlobPreconditionFailedError`.
This works the same way for both private and public storage, and is available on [`put()`](https://vercel.com/docs/vercel-blob/using-blob-sdk#put), [`copy()`](https://vercel.com/docs/vercel-blob/using-blob-sdk#copy), and [`del()`](https://vercel.com/docs/vercel-blob/using-blob-sdk#del):
```
import { head, put, BlobPreconditionFailedError } from '@vercel/blob';

// 1. Read the current blob and its ETag
const metadata = await head('config.json');

// 2. Write with the ETag — only succeeds if the blob hasn't changed
try {
  await put('config.json', JSON.stringify(newConfig), {
    access: 'private' /* or 'public' */,
    allowOverwrite: true,
    ifMatch: metadata.etag,
  });
} catch (error) {
  if (error instanceof BlobPreconditionFailedError) {
    // The blob was modified by another process — retry or handle the conflict
  }
  throw error;
}
```

Use conditional writes when multiple processes or users may update the same blob concurrently, such as shared configuration files or collaborative documents.
