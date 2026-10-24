##  [Copy a blob](https://vercel.com/docs/vercel-blob/using-blob-sdk#copy-a-blob)[](https://vercel.com/docs/vercel-blob/using-blob-sdk#copy-a-blob)
This example creates a Function that copies an existing blob to a new path in the store.
Next.js (/app)Next.js (/pages)Other frameworks
app/copy-blob/route.ts
TypeScript
TypeScript JavaScript Bash
```
import { copy } from '@vercel/blob';

export async function PUT(request: Request) {
  const form = await request.formData();

  const fromUrl = form.get('fromUrl') as string;
  const toPathname = form.get('toPathname') as string;

  const blob = await copy(fromUrl, toPathname, { access: 'private' /* or 'public' */ });

  return Response.json(blob);
}
```

###  [`copy()`](https://vercel.com/docs/vercel-blob/using-blob-sdk#copy)[](https://vercel.com/docs/vercel-blob/using-blob-sdk#copy)
The `copy` method copies an existing blob object to a new path inside the blob store.
The `contentType` and `cacheControlMaxAge` will not be copied from the source blob. If the values should be carried over to the copy, they need to be defined again in the options object.
Contrary to `put()`, `addRandomSuffix` is false by default. This means no automatic random id suffix is added to your blob url, unless you pass `addRandomSuffix: true`.
TypeScriptPython
```
copy(fromUrlOrPathname, toPathname, options);
```

```
copy(
    src_path: str,
    dst_path: str,
    *,
    access: Literal['private', 'public'],
    content_type: str | None = None,
    add_random_suffix: bool = False,
    overwrite: bool = False,
    cache_control_max_age: int | None = None,
    token: str | None = None,
) -> PutBlobResult
```

It accepts the following parameters:
  * `fromUrlOrPathname`: (Required) A blob URL or pathname identifying an already existing blob
  * `toPathname`: (Required) A string specifying the new path inside the blob store. This will be the base value of the return URL
  * `options`: (Required) A `JSON` object with the following required and optional parameters:


Parameter | Required | Values
---|---|---
`access` | Yes |  [`'private'` or `'public'`](https://vercel.com/docs/vercel-blob#private-and-public-storage). Determines the access level of the blob.
`contentType` | No | A string indicating the
`token` | No | A string specifying the token to use when making requests. It defaults to `process.env.BLOB_READ_WRITE_TOKEN` when deployed on Vercel as explained in [Read-write token](https://vercel.com/docs/vercel-blob/using-blob-sdk#read-write-token)
`addRandomSuffix` | No | A boolean specifying whether to add a random suffix to the pathname. It defaults to `false`.
`allowOverwrite` | No | A boolean to allow overwriting blobs. By default an error will be thrown if you try to overwrite a blob by using the same `pathname` for multiple blobs.
`cacheControlMaxAge` | No | A number in seconds to configure the edge and browser cache. Defaults to one month. See the [caching](https://vercel.com/docs/storage/vercel-blob#caching) documentation for more details.
`ifMatch` | No | An ETag value. The copy only succeeds if the source blob's current ETag matches this value. Use this for [conditional writes](https://vercel.com/docs/vercel-blob#conditional-writes) to prevent copying a blob that has been modified since you last read it. Throws `BlobPreconditionFailedError` if the ETag doesn't match.
`abortSignal` | No | An
`copy()` returns a `JSON` object with the following data for the copied blob object:
TypeScriptPython
```
{
  pathname: string;
  contentType: string;
  contentDisposition: string;
  url: string;
  downloadUrl: string;
  etag: string;
}
```

```
result.pathname             # str
result.content_type         # str
result.content_disposition  # str
result.url                  # str
result.download_url         # str
result.etag                 # str
```

An example blob is:
```
{
  "pathname": "profilesv1/user-12345-copy.txt",
  "contentType": "text/plain",
  "contentDisposition": "attachment; filename=\"user-12345-copy.txt\"",
  "url": "https://ce0rcu23vrrdzqap.public.blob.vercel-storage.com/profilesv1/user-12345-copy.txt",
  "downloadUrl": "https://ce0rcu23vrrdzqap.public.blob.vercel-storage.com/profilesv1/user-12345-copy.txt?download=1",
  "etag": "\"a1b2c3d4e5f6\""
}
```
