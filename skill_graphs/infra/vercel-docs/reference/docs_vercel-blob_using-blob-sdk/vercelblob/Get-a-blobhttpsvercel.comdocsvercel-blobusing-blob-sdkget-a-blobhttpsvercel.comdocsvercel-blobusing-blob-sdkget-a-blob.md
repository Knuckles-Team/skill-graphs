##  [Get a blob](https://vercel.com/docs/vercel-blob/using-blob-sdk#get-a-blob)[](https://vercel.com/docs/vercel-blob/using-blob-sdk#get-a-blob)
Retrieve blob content as a stream. For private blobs, this is how you deliver files through your functions. For public blobs, you can use this to process blob content server-side.
###  [`get()`](https://vercel.com/docs/vercel-blob/using-blob-sdk#get)[](https://vercel.com/docs/vercel-blob/using-blob-sdk#get)
TypeScriptPython
```
get(urlOrPathname, options);
```

```
get(
    url_or_path: str,
    *,
    access: Literal['private', 'public'],
    token: str | None = None,
    if_none_match: str | None = None,
) -> GetBlobResult | None
```

It accepts the following parameters:
  * `urlOrPathname`: (Required) A string specifying the URL or pathname of the blob object to retrieve
  * `options`: (Required) A `JSON` object with the following required and optional parameters:


Parameter | Required | Values
---|---|---
`access` | Yes |  [`'private'` or `'public'`](https://vercel.com/docs/vercel-blob#private-and-public-storage). Determines the access level of the blob.
`token` | No | A string specifying the read-write token to use when making requests. It defaults to `process.env.BLOB_READ_WRITE_TOKEN` when deployed on Vercel as explained in [Read-write token](https://vercel.com/docs/vercel-blob/using-blob-sdk#read-write-token)
`ifNoneMatch` | No | An ETag value. When the blob's current ETag matches, returns `statusCode: 304` with `stream: null` instead of the full response. See [browser caching with conditional requests](https://vercel.com/docs/vercel-blob/private-storage#browser-caching-with-conditional-requests) for a full example.
`headers` | No | Additional headers to include in the fetch request. The authorization header is set automatically.
`abortSignal` | No | An
`get()` returns `null` (`None` in Python) if the blob is not found, or an object with the following properties:
TypeScriptPython
```
{
  statusCode: number; // 200 or 304
  stream: ReadableStream<Uint8Array> | null; // null on 304
  headers: Headers;
  blob: {
    url: string;
    downloadUrl: string;
    pathname: string;
    contentType: string | null; // null on 304
    contentDisposition: string;
    cacheControl: string;
    etag: string;
    size: number | null; // null on 304
    uploadedAt: Date;
  };
}
```

```
# GetBlobResult:
result.status_code          # int (200 or 304)
result.stream               # AsyncIterator[bytes] | None (None on 304)
result.headers              # dict
result.blob.url             # str
result.blob.download_url    # str
result.blob.pathname        # str
result.blob.content_type    # str | None (None on 304)
result.blob.content_disposition  # str
result.blob.cache_control   # str
result.blob.etag            # str
result.blob.size            # int | None (None on 304)
result.blob.uploaded_at     # datetime
```

####  [Example](https://vercel.com/docs/vercel-blob/using-blob-sdk#example)[](https://vercel.com/docs/vercel-blob/using-blob-sdk#example)
TypeScriptPython
app/api/documents/[...pathname]/route.ts
```
import { type NextRequest, NextResponse } from 'next/server';
import { get } from '@vercel/blob';

export async function GET(
  request: NextRequest,
  { params }: { params: Promise<{ pathname: string[] }> },
) {
  // Your auth goes here: await authRequest(request)

  const { pathname } = await params;
  const result = await get(pathname.join('/'), { access: 'private' });

  if (result?.statusCode !== 200) {
    return new NextResponse('Not found', { status: 404 });
  }

  return new NextResponse(result.stream, {
    headers: {
      'Content-Type': result.blob.contentType,
    },
  });
}
```

```
from vercel.blob import AsyncBlobClient

client = AsyncBlobClient()

result = await client.get("documents/report.pdf", access="private")

if result is None or result.status_code != 200:
    print("Not found")
else:
    # result.stream is an async iterator of bytes
    async for chunk in result.stream:
        # process each chunk
        pass
```
