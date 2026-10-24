##  [Deleting blobs](https://vercel.com/docs/vercel-blob/using-blob-sdk#deleting-blobs)[](https://vercel.com/docs/vercel-blob/using-blob-sdk#deleting-blobs)
This example creates a function that deletes a blob object from the Blob store. You can delete multiple blob objects in a single request by passing an array of blob URLs.
Next.js (/app)Next.js (/pages)Other frameworks
app/delete/route.ts
TypeScript
TypeScript JavaScript Bash
```
import { del } from '@vercel/blob';

export async function DELETE(request: Request) {
  const { searchParams } = new URL(request.url);
  const urlToDelete = searchParams.get('url') as string;
  await del(urlToDelete);

  return new Response();
}
```

###  [`del()`](https://vercel.com/docs/vercel-blob/using-blob-sdk#del)[](https://vercel.com/docs/vercel-blob/using-blob-sdk#del)
The `del` method deletes one or multiple blob objects from the Blob store.
Since blobs are cached, it may take up to one minute for them to be fully removed from the Vercel CDN cache.
TypeScriptPython
```
del(urlOrPathname, options);

del([urlOrPathname], options); // You can pass an array to delete multiple blob objects
```

```
delete(url_or_path: str | Iterable[str], *, token: str | None = None) -> None
```

It accepts the following parameters:
  * `urlOrPathname`: (Required) A string or array of strings specifying the URL(s) or pathname(s) of the blob object(s) to delete.
  * `options`: (Optional) A `JSON` object with the following optional parameter:


Parameter | Required | Values
---|---|---
`token` | No | A string specifying the read-write token to use when making requests. It defaults to `process.env.BLOB_READ_WRITE_TOKEN` when deployed on Vercel as explained in [Read-write token](https://vercel.com/docs/vercel-blob/using-blob-sdk#read-write-token)
`ifMatch` | No | An ETag value. The delete only succeeds if the blob's current ETag matches this value. Use this for [conditional writes](https://vercel.com/docs/vercel-blob#conditional-writes) to ensure you're deleting the expected version. Throws `BlobPreconditionFailedError` if the ETag doesn't match. Only works with a single URL (not arrays).
`abortSignal` | No | An
`del()` returns a `void` response. A delete action is always successful if the blob url exists. A delete action won't throw if the blob url doesn't exist.
