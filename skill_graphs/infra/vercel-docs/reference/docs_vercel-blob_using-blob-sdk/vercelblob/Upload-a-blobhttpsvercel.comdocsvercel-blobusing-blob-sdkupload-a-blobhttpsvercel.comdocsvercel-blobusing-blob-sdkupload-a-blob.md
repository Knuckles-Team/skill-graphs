##  [Upload a blob](https://vercel.com/docs/vercel-blob/using-blob-sdk#upload-a-blob)[](https://vercel.com/docs/vercel-blob/using-blob-sdk#upload-a-blob)
This example creates a Function that accepts a file from a `multipart/form-data` form and uploads it to the Blob store. The function returns a unique URL for the blob.
TypeScriptPython
Next.js (/app)Next.js (/pages)Other frameworks
app/upload/route.ts
TypeScript
TypeScript JavaScript Bash
```
import { put } from '@vercel/blob';

export async function PUT(request: Request) {
  const form = await request.formData();
  const file = form.get('file') as File;
  const blob = await put(file.name, file, {
    access: 'private' /* or 'public' */,
    addRandomSuffix: true,
  });

  return Response.json(blob);
}
```

```
import asyncio
import os
import tempfile
from dotenv import load_dotenv
from vercel.blob import UploadProgressEvent, BlobClient, AsyncBlobClient

load_dotenv(".env.local")
load_dotenv()

def on_progress(e: UploadProgressEvent) -> None:
    print(f"progress: {e.loaded}/{e.total} bytes ({e.percentage}%)")

async def handler(form: dict) -> dict:
    client = AsyncBlobClient()

    file: bytes = form["file"]  # your uploaded bytes
    uploaded = await client.put(
        f"profiles/{form['filename']}",
        file,
        access="private",  # or "public",
        add_random_suffix=True,
        on_upload_progress=on_progress,
    )
    return dict(uploaded)
```

###  [`put()`](https://vercel.com/docs/vercel-blob/using-blob-sdk#put)[](https://vercel.com/docs/vercel-blob/using-blob-sdk#put)
The `put` method uploads a blob object to the Blob store.
TypeScriptPython
```
put(pathname, body, options);
```

```
put(
    pathname: str,
    body: bytes | AsyncIterator[bytes],
    *,
    access: Literal['private', 'public'],
    content_type: str | None = None,
    add_random_suffix: bool = False,
    overwrite: bool = False,
    cache_control_max_age: int | None = None,
    token: str | None = None,
    multipart: bool | None = None,
    on_upload_progress: Callable[[UploadProgressEvent], None] | None = None
)
```

It accepts the following parameters:
  * `pathname`: (Required) A string specifying the base value of the return URL
  * `body`: (Required) A blob object as `ReadableStream`, `String`, `ArrayBuffer` or `Blob` based on these
  * `options`: (Required) A `JSON` object with the following required and optional parameters:


Parameter | Required | Values
---|---|---
`access` | Yes |  [`'private'` or `'public'`](https://vercel.com/docs/vercel-blob#private-and-public-storage). Determines the access level of the blob.
`addRandomSuffix` | No | A boolean specifying whether to add a random suffix to the `pathname`. It defaults to `false`. We recommend using this option to ensure there are no conflicts in your blob filenames.
`allowOverwrite` | No | A boolean to allow overwriting blobs. By default an error will be thrown if you try to overwrite a blob by using the same `pathname` for multiple blobs.
`cacheControlMaxAge` | No | A number in seconds to configure how long Blobs are cached. Defaults to one month. Cannot be set to a value lower than 1 minute. See the [caching](https://vercel.com/docs/storage/vercel-blob#caching) documentation for more details.
`contentType` | No | A string indicating the
`token` | No | A string specifying the token to use when making requests. It defaults to `process.env.BLOB_READ_WRITE_TOKEN` when deployed on Vercel as explained in [Read-write token](https://vercel.com/docs/vercel-blob/using-blob-sdk#read-write-token). You can also pass a client token created with the `generateClientTokenFromReadWriteToken` method
`multipart` | No | Pass `multipart: true` when uploading large files. It will split the file into multiple parts, upload them in parallel and retry failed parts.
`abortSignal` | No | An
`onUploadProgress` | No | Callback to track upload progress: `onUploadProgress({loaded: number, total: number, percentage: number})`
`ifMatch` | No | An ETag value. The operation only succeeds if the blob's current ETag matches this value. Use this for [conditional writes](https://vercel.com/docs/vercel-blob#conditional-writes) to prevent overwriting changes made by others. Throws `BlobPreconditionFailedError` if the ETag doesn't match.
####  [Example code with folder output](https://vercel.com/docs/vercel-blob/using-blob-sdk#example-code-with-folder-output)[](https://vercel.com/docs/vercel-blob/using-blob-sdk#example-code-with-folder-output)
To upload your file to an existing [folder](https://vercel.com/docs/vercel-blob/using-blob-sdk#folders) inside your blob storage, pass the folder name in the `pathname` as shown below:
TypeScriptPython
```
const imageFile = formData.get('image') as File;
const blob = await put(`existingBlobFolder/${imageFile.name}`, imageFile, {
  access: 'private' /* or 'public' */,
  addRandomSuffix: true,
});
```

```
import os
from dotenv import load_dotenv
from vercel.blob import AsyncBlobClient

load_dotenv('.env.local')
load_dotenv()

client = AsyncBlobClient()

image_bytes = b"..."
blob = await client.put(
    f"existingBlobFolder/image.png",
    image_bytes,
    access="private",  # or "public",
    add_random_suffix=True,
)
```

####  [Example responses](https://vercel.com/docs/vercel-blob/using-blob-sdk#example-responses)[](https://vercel.com/docs/vercel-blob/using-blob-sdk#example-responses)
`put()` returns a `JSON` object with the following data for the created blob object:
```
{
  "pathname": "string",
  "contentType": "string",
  "contentDisposition": "string",
  "url": "string",
  "downloadUrl": "string",
  "etag": "string"
}
```

An example blob (uploaded with `addRandomSuffix: true`) is:
```
{
  "pathname": "profilesv1/user-12345-NoOVGDVcqSPc7VYCUAGnTzLTG2qEM2.txt",
  "contentType": "text/plain",
  "contentDisposition": "attachment; filename=\"user-12345-NoOVGDVcqSPc7VYCUAGnTzLTG2qEM2.txt\"",
  "url": "https://ce0rcu23vrrdzqap.private.blob.vercel-storage.com/profilesv1/user-12345-NoOVGDVcqSPc7VYCUAGnTzLTG2qEM2.txt",
  "downloadUrl": "https://ce0rcu23vrrdzqap.private.blob.vercel-storage.com/profilesv1/user-12345-NoOVGDVcqSPc7VYCUAGnTzLTG2qEM2.txt?download=1",
  "etag": "\"a1b2c3d4e5f6\""
}
```

If `access` is `'public'`, the URL domain will be `.public.blob.vercel-storage.com` instead of `.private.blob.vercel-storage.com`.
An example blob uploaded without `addRandomSuffix: true` (default) is:
```
{
  "pathname": "profilesv1/user-12345.txt",
  "contentType": "text/plain",
  "contentDisposition": "attachment; filename=\"user-12345.txt\"",
  // no automatic random suffix added 👇
  "url": "https://ce0rcu23vrrdzqap.private.blob.vercel-storage.com/profilesv1/user-12345.txt",
  "downloadUrl": "https://ce0rcu23vrrdzqap.private.blob.vercel-storage.com/profilesv1/user-12345.txt?download=1",
  "etag": "\"f6e5d4c3b2a1\""
}
```
