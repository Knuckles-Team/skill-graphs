##  [Get blob metadata](https://vercel.com/docs/vercel-blob/using-blob-sdk#get-blob-metadata)[](https://vercel.com/docs/vercel-blob/using-blob-sdk#get-blob-metadata)
This example creates a Function that returns a blob object's metadata.
Next.js (/app)Next.js (/pages)Other frameworks
app/get-blob/route.ts
TypeScript
TypeScript JavaScript Bash
```
import { head } from '@vercel/blob';

export async function GET(request: Request) {
  const { searchParams } = new URL(request.url);
  const blobUrl = searchParams.get('url');
  const blobDetails = await head(blobUrl);

  return Response.json(blobDetails);
}
```

###  [`head()`](https://vercel.com/docs/vercel-blob/using-blob-sdk#head)[](https://vercel.com/docs/vercel-blob/using-blob-sdk#head)
The `head` method returns a blob object's metadata.
TypeScriptPython
```
head(urlOrPathname, options);
```

```
head(url_or_path: str, *, token: str | None = None) -> HeadBlobResult
```

It accepts the following parameters:
  * `urlOrPathname`: (Required) A string specifying the URL or pathname of the blob object to read.
  * `options`: (Optional) A `JSON` object with the following optional parameter:


Parameter | Required | Values
---|---|---
`token` | No | A string specifying the read-write token to use when making requests. It defaults to `process.env.BLOB_READ_WRITE_TOKEN` when deployed on Vercel as explained in [Read-write token](https://vercel.com/docs/vercel-blob/using-blob-sdk#read-write-token)
`abortSignal` | No | An
`head()` returns one of the following:
  * a `JSON` object with the requested blob object's metadata
  * throws a `BlobNotFoundError` if the blob object was not found


TypeScriptPython
```
{
  size: number;
  uploadedAt: Date;
  pathname: string;
  contentType: string;
  contentDisposition: string;
  url: string;
  downloadUrl: string;
  cacheControl: string;
  etag: string;
}
```

```
result.size                 # int
result.uploaded_at          # datetime
result.pathname             # str
result.content_type         # str
result.content_disposition  # str
result.url                  # str
result.download_url         # str
result.cache_control        # str
result.etag                 # str
```
